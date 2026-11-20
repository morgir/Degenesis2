import { ATTRIBUTES, SKILL_ATTRIBUTE, BACKGROUNDS, DIFFICULTIES, MAX_EGO_DICE, MAX_BACKGROUND_DICE, SYSTEM_ID } from "./config.mjs";
import { buildPool, evaluateRoll, parseDamage, oracle } from "./rules.mjs";

const { DialogV2 } = foundry.applications.api;
const renderTemplate = foundry.applications.handlebars.renderTemplate;
const loc = (k, d) => game.i18n.format(k, d ?? {});

const OUTCOME_CLASS = { "tak-i": "great", "tak": "success", "tak-ale": "partial", "nie": "fail", "nie-i": "botch", "brak": "neutral" };

/**
 * Otwiera okno rzutu i wykonuje rzut.
 * @param {Actor} actor
 * @param {object} opts { attr, skill, item, difficulty, label }
 */
export async function rollDialog(actor, opts = {}) {
  const sys = actor.system;
  const isPC = actor.type === "postac";
  const item = opts.item ?? null;
  let skill = opts.skill ?? (item?.type === "bron" ? item.system.skill : null);
  let attr = opts.attr ?? (skill ? SKILL_ATTRIBUTE[skill] : "cia");

  const attrOptions = Object.keys(ATTRIBUTES).map(k => ({ value: k, label: loc(`D2.Attr.${k}`), selected: k === attr }));
  const skillOptions = [{ value: "", label: "—", selected: !skill }].concat(
    Object.entries(ATTRIBUTES).flatMap(([a, def]) => def.skills.map(s => ({
      value: s, label: `${loc(`D2.Skill.${s}`)} (${loc(`D2.Attr.${a}`)})`, selected: s === skill
    })))
  );
  const diffOptions = [{ value: "none", label: loc("D2.Roll.noDifficulty"), selected: opts.difficulty === null }]
    .concat(DIFFICULTIES.map(d => ({ value: String(d.value), label: `${d.value} — ${loc(d.label)}`, selected: (opts.difficulty ?? 2) === d.value })));
  const bgOptions = isPC
    ? [{ value: "", label: "—" }].concat(BACKGROUNDS.map(b => ({ value: b, label: `${loc(`D2.Background.${b}`)} (${sys.backgrounds[b].available})` })))
    : [];

  const content = await renderTemplate(`systems/${SYSTEM_ID}/templates/dialog/roll.hbs`, {
    attrOptions, skillOptions, diffOptions, bgOptions, isPC,
    egoMax: Math.min(MAX_EGO_DICE, sys.ego?.value ?? 0),
    archetypeAvailable: isPC && !sys.archetypeUsed,
    woundPenalty: sys.woundPenalty ?? 0,
    handling: item?.type === "bron" ? item.system.handling : 0,
    item, gang: actor.type === "npc" && sys.scale === "banda"
  });

  const title = opts.label ?? (item ? item.name : (skill ? loc(`D2.Skill.${skill}`) : loc("D2.Roll.title")));
  const data = await DialogV2.prompt({
    window: { title: `${actor.name}: ${title}` },
    content,
    position: { width: 420 },
    ok: {
      label: loc("D2.Roll.roll"),
      icon: "fa-solid fa-dice-six",
      callback: (event, button) => {
        const f = button.form.elements;
        return {
          attr: f.attr.value,
          skill: f.skill.value || null,
          mod: Number(f.mod.value) || 0,
          difficulty: f.difficulty.value === "none" ? null : Number(f.difficulty.value),
          ego: Math.max(0, Number(f.ego?.value) || 0),
          background: f.background?.value || null,
          archetype: !!f.archetype?.checked,
          cechy: Math.max(0, Number(f.cechy.value) || 0)
        };
      }
    },
    rejectClose: false
  });
  if (!data) return null;
  return performRoll(actor, { ...data, item, label: title });
}

/** Rzut bez okna (makra, inicjatywa itp.) */
export async function performRoll(actor, { attr, skill, mod = 0, difficulty = 2, ego = 0, background = null, archetype = false, cechy = 0, item = null, label = "" }) {
  const sys = actor.system;
  const isPC = actor.type === "postac";
  const parts = [];
  const base = sys.attributes[attr]?.value ?? 0;
  parts.push({ label: loc(`D2.Attr.${attr}`), value: base });
  if (skill) parts.push({ label: loc(`D2.Skill.${skill}`), value: sys.skills[skill]?.value ?? 0 });
  if (mod) parts.push({ label: loc("D2.Roll.modifier"), value: mod });
  if (item?.type === "bron" && item.system.handling) parts.push({ label: loc("D2.Weapon.handling"), value: item.system.handling });

  const egoSpent = Math.min(ego, MAX_EGO_DICE, sys.ego?.value ?? 0);
  if (egoSpent) parts.push({ label: loc("D2.Ego"), value: egoSpent });

  let bgDice = 0;
  if (isPC && background) {
    bgDice = Math.min(MAX_BACKGROUND_DICE, sys.backgrounds[background]?.value ?? 0);
    if (bgDice) parts.push({ label: loc(`D2.Background.${background}`), value: bgDice });
  }
  const archetypeUsed = isPC && archetype && !sys.archetypeUsed;
  if (archetypeUsed) parts.push({ label: loc("D2.Archetype"), value: 2 });
  if (cechy) parts.push({ label: loc("D2.Cecha.invokes"), value: cechy * 2 });
  if (actor.type === "npc" && sys.scale === "banda") {
    const gb = Math.min(4, Math.floor((sys.size?.value ?? 0) / 2));
    if (gb) parts.push({ label: loc("D2.Npc.gangBonus"), value: gb });
  }
  if (sys.woundPenalty) parts.push({ label: loc("D2.Wounds.penalty"), value: -sys.woundPenalty });

  const total = parts.reduce((t, p) => t + p.value, 0);
  const pool = buildPool(total);

  let results = [];
  let roll = null;
  if (pool.dice > 0) {
    roll = new Roll(`${pool.dice}d6`);
    await roll.evaluate();
    results = roll.dice[0].results.map(r => r.result);
  }
  const ev = evaluateRoll(results, { difficulty, autoSuccesses: pool.autoSuccesses });

  // Koszty zasobów
  const updates = {};
  if (egoSpent) updates["system.ego.value"] = Math.max(0, sys.ego.value - egoSpent);
  if (archetypeUsed) updates["system.archetypeUsed"] = true;
  if (Object.keys(updates).length) await actor.update(updates);

  // Obrażenia przy ataku
  let damage = null;
  if (item?.type === "bron" && (ev.outcome === "tak" || ev.outcome === "tak-i" || ev.outcome === "brak")) {
    const base = parseDamage(item.system.damage, sys.force);
    damage = { base, triggers: ev.triggers, total: base + ev.triggers };
  }

  const content = await renderTemplate(`systems/${SYSTEM_ID}/templates/chat/roll.hbs`, {
    label, parts, total, pool, results: results.map(r => ({ r, cls: r === 6 ? "trigger" : r >= 4 ? "success" : r === 1 ? "one" : "" })),
    ev, difficulty, outcomeLabel: loc(`D2.Outcome.${ev.outcome}`), outcomeHint: loc(`D2.OutcomeHint.${ev.outcome}`),
    outcomeClass: OUTCOME_CLASS[ev.outcome], damage, item
  });

  const msgData = {
    speaker: ChatMessage.getSpeaker({ actor }),
    content,
    flags: { [SYSTEM_ID]: { type: "roll", damage } },
    sound: CONFIG.sounds.dice
  };
  if (roll) msgData.rolls = [roll];
  await ChatMessage.create(msgData);
  return { ...ev, results, damage };
}

/** Wyrocznia FU */
export async function rollOracle(mode = "normal", question = "") {
  const n = mode === "normal" ? 1 : 2;
  const roll = new Roll(`${n}d6`);
  await roll.evaluate();
  const results = roll.dice[0].results.map(r => r.result);
  const key = oracle(results, mode);
  const content = await renderTemplate(`systems/${SYSTEM_ID}/templates/chat/oracle.hbs`, {
    question, results, mode: loc(`D2.Oracle.${mode}`), answer: loc(`D2.OracleAnswer.${key}`), key
  });
  await ChatMessage.create({ content, rolls: [roll], sound: CONFIG.sounds.dice, speaker: { alias: loc("D2.Oracle.title") } });
  return key;
}

export async function oracleDialog() {
  const content = await renderTemplate(`systems/${SYSTEM_ID}/templates/dialog/oracle.hbs`, {});
  const data = await DialogV2.prompt({
    window: { title: loc("D2.Oracle.title") },
    content,
    ok: {
      label: loc("D2.Roll.roll"),
      callback: (event, button) => ({ question: button.form.elements.question.value, mode: button.form.elements.mode.value })
    },
    rejectClose: false
  });
  if (data) return rollOracle(data.mode, data.question);
}


/**
 * Zjawisko Psychonauty (Katharsys s. 285, przeniesione do 2.0):
 * pula = Zarażenie (Prymer) − Przeciążenie (+ premie maski/sprzętu); nadwyżka ponad 12 = sukcesy automatyczne;
 * Trudność = poziom Zjawiska; każdy punkt Przeciążenia wzmacnia efekt i trwale zużywa 1 punkt Zarażenia.
 */
export async function phenomenonDialog(actor, item) {
  const sys = actor.system;
  const spores = sys.prymer?.value ?? 0;
  const level = item.system.poziomZjawiska ?? 0;
  const content = `<div class="d2-dialog">
    <p><b>${item.name}</b> — ${loc("D2.Phenomenon.level")}: ${level} · ${loc("D2.Phenomenon.spores")}: ${spores}</p>
    <label>${loc("D2.Phenomenon.overload")} <input type="number" name="overload" value="0" min="0" max="${spores}"></label>
    <label>${loc("D2.Roll.modifier")} <input type="number" name="mod" value="${sys.zjawiskaBonus ?? 0}"></label>
    <p class="hint">${loc("D2.Phenomenon.hint")}</p></div>`;
  const data = await DialogV2.prompt({
    window: { title: item.name },
    content,
    ok: {
      label: loc("D2.Roll.roll"),
      callback: (event, button) => {
        const f = button.form.elements;
        return { overload: Math.max(0, Math.min(spores, Number(f.overload.value) || 0)), mod: Number(f.mod.value) || 0 };
      }
    },
    rejectClose: false
  });
  if (!data) return null;
  return rollPhenomenon(actor, item, data);
}

export async function rollPhenomenon(actor, item, { overload = 0, mod = 0 } = {}) {
  const sys = actor.system;
  const spores = sys.prymer?.value ?? 0;
  const difficulty = item.system.poziomZjawiska ?? 0;
  const parts = [{ label: loc("D2.Phenomenon.spores"), value: spores }];
  if (overload) parts.push({ label: loc("D2.Phenomenon.overload"), value: -overload });
  if (mod) parts.push({ label: loc("D2.Roll.modifier"), value: mod });
  if (sys.woundPenalty) parts.push({ label: loc("D2.Wounds.penalty"), value: -sys.woundPenalty });
  const total = parts.reduce((t, p) => t + p.value, 0);
  const pool = buildPool(total);
  let results = [], roll = null;
  if (pool.dice > 0) {
    roll = new Roll(`${pool.dice}d6`);
    await roll.evaluate();
    results = roll.dice[0].results.map(r => r.result);
  }
  const ev = evaluateRoll(results, { difficulty, autoSuccesses: pool.autoSuccesses });
  if (overload) await actor.update({ "system.prymer.value": Math.max(0, spores - overload) });
  const label = `${item.name} (${loc("D2.Phenomenon.overload")} ${overload})`;
  const content = await renderTemplate(`systems/${SYSTEM_ID}/templates/chat/roll.hbs`, {
    label, parts, total, pool, results: results.map(r => ({ r, cls: r === 6 ? "trigger" : r >= 4 ? "success" : r === 1 ? "one" : "" })),
    ev, difficulty, outcomeLabel: loc(`D2.Outcome.${ev.outcome}`), outcomeHint: loc(`D2.OutcomeHint.${ev.outcome}`),
    outcomeClass: OUTCOME_CLASS[ev.outcome], damage: null, item
  });
  const msg = { speaker: ChatMessage.getSpeaker({ actor }), content, flags: { [SYSTEM_ID]: { type: "phenomenon", overload } }, sound: CONFIG.sounds.dice };
  if (roll) msg.rolls = [roll];
  await ChatMessage.create(msg);
  return { ...ev, results, overload };
}

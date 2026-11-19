/**
 * Kreator postaci Katharsys 2.0 — krok po kroku według zasad z Katharsys (rozdz. 6) + dodatki 2.0.
 */
import { ATTRIBUTES, ALL_SKILLS, BACKGROUNDS, SKILL_ATTRIBUTE, SYSTEM_ID } from "../config.mjs";
import { attrLimit, skillLimit, creationBudget, checkPrereqs, CREATION } from "../rules.mjs";

const { ApplicationV2, HandlebarsApplicationMixin } = foundry.applications.api;
const loc = (k, d) => game.i18n.format(k, d ?? {});

const STEPS = ["origin", "path", "attrs", "skills", "bgs", "rank", "potential", "person", "summary"];

function prereqLabel(e) {
  if (e[0] === "bg") return `${loc(`D2.Background.${e[1]}`)} ${e[2]}`;
  if (e[0] === "txt") return e[1];
  return `${ATTRIBUTES[e[0]].abbr}+${loc(`D2.Skill.${e[1]}`)} ${e[2]}`;
}

export class D2CharacterCreator extends HandlebarsApplicationMixin(ApplicationV2) {
  constructor(options = {}) {
    super(options);
    this.actor = options.actor;
    this.d2state = {
      step: 0,
      kultura: "", koncept: "", kult: "",
      path: "skupienie", belief: "wola",
      attrs: Object.fromEntries(Object.keys(ATTRIBUTES).map(k => [k, 1])),
      skills: Object.fromEntries(ALL_SKILLS.map(k => [k, 0])),
      bgs: Object.fromEntries(BACKGROUNDS.map(k => [k, 0])),
      rank: -1, potential: "",
      name: this.actor?.name ?? "", wiek: "", plec: "",
      ambicja: "", tajemnica: "", wiez1: "", wiez2: "", cien: ""
    };
    this._data = null;
  }

  static DEFAULT_OPTIONS = {
    id: "d2-creator-{id}",
    tag: "form",
    classes: ["d2", "d2-creator"],
    window: { title: "D2.Creator.title", icon: "fa-solid fa-user-plus", resizable: true },
    position: { width: 820, height: 760 },
    form: { handler: D2CharacterCreator.#onChange, submitOnChange: true, closeOnSubmit: false },
    actions: {
      step: D2CharacterCreator.#onStep,
      goto: D2CharacterCreator.#onGoto,
      bump: D2CharacterCreator.#onBump,
      finish: D2CharacterCreator.#onFinish
    }
  };

  static PARTS = { main: { template: `systems/${SYSTEM_ID}/templates/apps/creator.hbs`, scrollable: [".d2-creator-body"] } };

  /** Wczytuje Kultury, Koncepty, Kulty i Potencjały z kompendiów systemu. */
  async #loadData() {
    if (this._data) return this._data;
    const get = async (name) => {
      const pack = game.packs.get(`${SYSTEM_ID}.${name}`);
      return pack ? (await pack.getDocuments()).sort((a, b) => a.name.localeCompare(b.name, "pl")) : [];
    };
    const [kultury, koncepty, kulty, potencjaly] = await Promise.all([get("kultury"), get("koncepty"), get("kulty"), get("potencjaly")]);
    koncepty.sort((a, b) => (a.sort ?? 0) - (b.sort ?? 0));
    this._data = { kultury, koncepty, kulty, potencjaly };
    return this._data;
  }

  #bonusLists(data) {
    const kul = data.kultury.find(d => d.id === this.d2state.kultura);
    const kon = data.koncepty.find(d => d.id === this.d2state.koncept);
    const kt = data.kulty.find(d => d.id === this.d2state.kult);
    return {
      attr: [kul?.system.attributeBonuses ?? [], kon?.system.attributeBonuses ?? []],
      skill: [kul?.system.skillBonuses ?? [], kon?.system.skillBonuses ?? [], kt?.system.skillBonuses ?? []],
      kul, kon, kt
    };
  }

  #lockedSkills() {
    const s = this.d2state;
    return new Set([s.path === "skupienie" ? "pierwotnosc" : "skupienie", s.belief === "wiara" ? "wola" : "wiara"]);
  }

  /** Lista rang z oceną wymagań. Ranga poziomu n wymaga dostępnej rangi poziomu n−1. */
  #rankOptions(kt) {
    if (!kt) return [];
    const stats = { attrs: this.d2state.attrs, skills: this.d2state.skills, bgs: this.d2state.bgs };
    const ranks = kt.system.ranks.map((r, i) => {
      let prereq = [];
      try { prereq = JSON.parse(r.prereq || "[]"); } catch { prereq = []; }
      const c = checkPrereqs(prereq, stats, prereqLabel);
      return { ...r, index: i, ok: c.ok, missing: c.missing, manual: c.manual };
    });
    const okLevels = new Set([1]);
    for (const lvl of [2, 3, 4, 5, 6]) {
      if (ranks.some(r => r.level === lvl - 1 && r.ok && okLevels.has(lvl - 1))) okLevels.add(lvl);
    }
    for (const r of ranks) {
      const campaign = (r.manual ?? []).some(m => /kampania|urodzenie jako syn|musi|wolne|mianowany|co najmniej|wyrył|zjednoczył|pokonać|Dysk|statek|warsztat|przyjęty/i.test(m));
      r.reachable = r.ok && r.level >= 1 && !campaign && (r.level <= 1 || okLevels.has(r.level));
    }
    return ranks;
  }

  async _prepareContext(options) {
    try {
      return await this.#context();
    } catch (err) {
      console.error(`${SYSTEM_ID} | Kreator postaci`, err);
      ui.notifications.error(`Kreator postaci: ${err.message}`);
      throw err;
    }
  }

  async #context() {
    const data = await this.#loadData();
    const s = this.d2state;
    const b = this.#bonusLists(data);
    const locked = this.#lockedSkills();
    const budget = creationBudget(s);

    const attributes = Object.entries(ATTRIBUTES).map(([k, def]) => ({
      key: k, abbr: def.abbr, label: loc(`D2.Attr.${k}`), value: s.attrs[k],
      max: attrLimit(k, b.attr), bonus: b.attr.filter(l => l.includes(k)).length,
      skills: def.skills.map(sk => ({
        key: sk, label: loc(`D2.Skill.${sk}`), value: s.skills[sk], locked: locked.has(sk),
        max: locked.has(sk) ? 0 : skillLimit(sk, b.skill), bonus: b.skill.filter(l => l.includes(sk)).length,
        pool: s.attrs[k] + s.skills[sk]
      }))
    }));

    const ranks = this.#rankOptions(b.kt);
    if (s.rank >= 0 && !ranks[s.rank]?.reachable) s.rank = -1;
    const chosenRank = ranks[s.rank] ?? ranks.find(r => r.level === 1);
    const pots = data.potencjaly.filter(p => !p.system.kult || p.system.kult === b.kt?.name || p.system.kult === "Ogólne");
    const pathAttr = s.path === "pierwotnosc" ? "ins" : "int";
    const derived = {
      ego: (s.attrs[pathAttr] + s.skills[s.path]) * 2,
      spores: (s.attrs.psy + s.skills[s.belief]) * 2,
      prog: s.attrs.cia + s.skills.twardosc,
      money: b.kt ? ((chosenRank?.level ?? 1) + s.bgs.zasoby) * (b.kt.system.moneyFactor ?? 50) : 0,
      currency: b.kt?.system.currency ?? "CD"
    };

    const problems = [];
    if (!b.kul || !b.kon || !b.kt) problems.push(loc("D2.Creator.err.origin"));
    if (budget.attrLeft !== 0) problems.push(loc("D2.Creator.err.attr", { n: budget.attrLeft }));
    if (budget.skillLeft !== 0) problems.push(loc("D2.Creator.err.skill", { n: budget.skillLeft }));
    if (budget.bgLeft !== 0) problems.push(loc("D2.Creator.err.bg", { n: budget.bgLeft }));
    if (!s.potential) problems.push(loc("D2.Creator.err.potential"));

    return {
      s, step: STEPS[s.step], stepIndex: s.step, steps: STEPS.map((k, i) => ({ key: k, i, label: loc(`D2.Creator.step.${k}`), active: i === s.step })),
      isFirst: s.step === 0, isLast: s.step === STEPS.length - 1,
      kultury: data.kultury.map(d => ({ id: d.id, name: d.name, selected: d.id === s.kultura })),
      koncepty: data.koncepty.map(d => ({ id: d.id, name: d.name, selected: d.id === s.koncept })),
      kulty: data.kulty.map(d => ({ id: d.id, name: d.name, selected: d.id === s.kult })),
      kul: b.kul, kon: b.kon, kt: b.kt,
      bonusText: {
        kul: this.#bonusText(b.kul), kon: this.#bonusText(b.kon), kt: this.#bonusText(b.kt)
      },
      attributes, budget, locked: [...locked].map(k => loc(`D2.Skill.${k}`)).join(", "),
      bgs: BACKGROUNDS.map(k => ({ key: k, label: loc(`D2.Background.${k}`), value: s.bgs[k], max: CREATION.bgMax, hint: loc(`D2.Creator.bgHint.${k}`) })),
      ranks, chosenRank,
      potentials: pots.map(p => ({ id: p.id, name: p.name, kult: p.system.kult, prereq: p.system.prerequisite, desc: p.system.description, selected: p.id === s.potential })),
      derived, problems, ready: problems.length === 0
    };
  }

  #bonusText(doc) {
    if (!doc) return "";
    const a = (doc.system.attributeBonuses ?? []).map(k => loc(`D2.Attr.${k}`));
    const sk = (doc.system.skillBonuses ?? []).map(k => loc(`D2.Skill.${k}`));
    return [...a, ...sk].join(", ");
  }

  static async #onChange(event, form, formData) {
    const o = foundry.utils.expandObject(formData.object);
    const s = this.d2state;
    for (const k of ["kultura", "koncept", "kult", "path", "belief", "potential", "name", "wiek", "plec", "ambicja", "tajemnica", "wiez1", "wiez2", "cien"]) {
      if (o[k] !== undefined) s[k] = o[k];
    }
    if (o.rank !== undefined) s.rank = Number(o.rank);
    // Koncept podpowiada Cień
    if (o.koncept !== undefined && !s.cien) {
      const kon = this._data?.koncepty.find(d => d.id === s.koncept);
      if (kon) s.cien = kon.system.cien;
    }
    // Wykluczone umiejętności zerujemy
    for (const k of this.#lockedSkills()) s.skills[k] = 0;
    this.render();
  }

  static #onStep(event, target) {
    this.d2state.step = Math.max(0, Math.min(STEPS.length - 1, this.d2state.step + Number(target.dataset.delta)));
    this.render();
  }

  static #onGoto(event, target) {
    this.d2state.step = Number(target.dataset.i);
    this.render();
  }

  /** +/− na atrybucie, umiejętności albo Zapleczu, z limitami. */
  static async #onBump(event, target) {
    const { kind, key } = target.dataset;
    const delta = Number(target.dataset.delta);
    const data = await this.#loadData();
    const b = this.#bonusLists(data);
    const s = this.d2state;
    const budget = creationBudget(s);
    if (kind === "attr") {
      const v = s.attrs[key] + delta;
      if (v < 1 || v > attrLimit(key, b.attr) || (delta > 0 && budget.attrLeft <= 0)) return;
      s.attrs[key] = v;
    } else if (kind === "skill") {
      if (this.#lockedSkills().has(key)) return;
      const v = s.skills[key] + delta;
      if (v < 0 || v > skillLimit(key, b.skill) || (delta > 0 && budget.skillLeft <= 0)) return;
      s.skills[key] = v;
    } else if (kind === "bg") {
      const v = s.bgs[key] + delta;
      if (v < 0 || v > CREATION.bgMax || (delta > 0 && budget.bgLeft <= 0)) return;
      s.bgs[key] = v;
    }
    this.render();
  }

  static async #onFinish() {
    const ctx = await this._prepareContext();
    if (!ctx.ready) {
      const ok = await foundry.applications.api.DialogV2.confirm({
        window: { title: loc("D2.Creator.title") },
        content: `<p>${loc("D2.Creator.notReady")}</p><ul>${ctx.problems.map(p => `<li>${p}</li>`).join("")}</ul>`,
        rejectClose: false
      });
      if (!ok) return;
    }
    await this.#apply(ctx);
    ui.notifications.info(loc("D2.Creator.done", { name: this.actor.name }));
    this.close();
    this.actor.sheet.render(true);
  }

  async #apply(ctx) {
    const s = this.d2state;
    const actor = this.actor;
    const rank = ctx.chosenRank;
    const update = {
      name: s.name || actor.name,
      "system.path": s.path, "system.belief": s.belief,
      "system.identity.kultura": ctx.kul?.name ?? "", "system.identity.koncept": ctx.kon?.name ?? "",
      "system.identity.kult": ctx.kt?.name ?? "", "system.identity.ranga": rank?.name ?? "",
      "system.identity.wiek": s.wiek, "system.identity.plec": s.plec,
      "system.ambicja": s.ambicja, "system.tajemnica": s.tajemnica, "system.cien": s.cien,
      "system.wiezi": [s.wiez1, s.wiez2].filter(Boolean).join("\n"),
      "system.ego.value": ctx.derived.ego,
      "system.money": `${ctx.derived.money} ${ctx.derived.currency}`,
      "system.archetypeUsed": false
    };
    for (const k of Object.keys(ATTRIBUTES)) update[`system.attributes.${k}.value`] = s.attrs[k];
    for (const k of ALL_SKILLS) update[`system.skills.${k}.value`] = s.skills[k];
    for (const k of BACKGROUNDS) { update[`system.backgrounds.${k}.value`] = s.bgs[k]; update[`system.backgrounds.${k}.spent`] = 0; }
    await actor.update(update);

    // Zastąp poprzednie 3K i dodaj Potencjał oraz ekwipunek rangi
    const old = actor.items.filter(i => ["kultura", "koncept", "kult"].includes(i.type)).map(i => i.id);
    if (old.length) await actor.deleteEmbeddedDocuments("Item", old);
    const items = [ctx.kul, ctx.kon, ctx.kt].filter(Boolean).map(d => d.toObject());
    const pot = this._data.potencjaly.find(p => p.id === s.potential);
    if (pot) items.push(pot.toObject());
    const ranksUpTo = (ctx.kt?.system.ranks ?? []).filter((r, i) => (r.level === 1 && i <= (rank?.index ?? 0)) || i === rank?.index);
    const eq = ranksUpTo.map(r => r.equipment).filter(Boolean).join("; ");
    if (eq) items.push({ name: loc("D2.Creator.rankGear", { rank: rank?.name ?? "" }), type: "ekwipunek", img: "icons/svg/chest.svg",
      system: { description: `<p>${eq}</p><p><i>${loc("D2.Creator.rankGearHint")}</i></p>`, quantity: 1 } });
    for (const it of items) delete it._id;
    await actor.createEmbeddedDocuments("Item", items);
  }
}

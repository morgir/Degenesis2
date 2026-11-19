/**
 * Rozwój postaci (PD): przyznawanie, zakupy atrybutów, umiejętności i Potencjałów, dziennik.
 * Koszty z Katharsys przeniesione do 2.0 (rules.xpCost). Zaplecze rośnie tylko przez fikcję.
 */
import { ATTRIBUTES, SYSTEM_ID } from "./config.mjs";
import { xpCost } from "./rules.mjs";

const { DialogV2 } = foundry.applications.api;
const loc = (k, d) => game.i18n.format(k, d ?? {});
export const MAX_ATTR = 6;
export const MAX_SKILL = 6;

export const AWARDS = [
  { amount: 5, reason: "Udział w sesji" },
  { amount: 2, reason: "Ważny Wniosek" },
  { amount: 2, reason: "Odkryty Sekret" },
  { amount: 1, reason: "Przyjęta Pokusa Archetypu" },
  { amount: 1, reason: "Ideał lub Więź ponad interes" }
];

/** Dokumenty Kultury, Konceptu i Kultu postaci: z jej przedmiotów, a gdy ich brak — z kompendiów po nazwie. */
async function originDocs(actor) {
  const out = {};
  const id = actor.system.identity ?? {};
  for (const [type, pack, name] of [["kultura", "kultury", id.kultura], ["koncept", "koncepty", id.koncept], ["kult", "kulty", id.kult]]) {
    let doc = actor.items.find(i => i.type === type);
    if (!doc && name) {
      const p = game.packs.get(`${SYSTEM_ID}.${pack}`);
      if (p) {
        const clean = String(name).split("(")[0].trim().toLowerCase();
        const hit = p.index.find(e => e.name.toLowerCase() === clean || e.name.toLowerCase().startsWith(clean) || clean.startsWith(e.name.toLowerCase()));
        if (hit) doc = await p.getDocument(hit._id);
      }
    }
    out[type] = doc ?? null;
  }
  return out;
}

export async function preferredSets(actor) {
  const o = await originDocs(actor);
  const attrs = new Set([...(o.kultura?.system.attributeBonuses ?? []), ...(o.koncept?.system.attributeBonuses ?? [])]);
  const skills = new Set([...(o.kultura?.system.skillBonuses ?? []), ...(o.koncept?.system.skillBonuses ?? []), ...(o.kult?.system.skillBonuses ?? [])]);
  return { attrs, skills, origin: o };
}

function lockedSkills(sys) {
  return new Set([sys.path === "skupienie" ? "pierwotnosc" : "skupienie", sys.belief === "wiara" ? "wola" : "wiara"]);
}

function potSum(actor) {
  return actor.items.filter(i => i.type === "potencjal" && !i.system.zjawisko).reduce((t, i) => t + (i.system.level ?? 1), 0);
}

/** Kontekst zakładki Rozwój. */
export async function progressionContext(actor) {
  const sys = actor.system;
  const avail = sys.xp.available;
  const pref = await preferredSets(actor);
  const locked = lockedSkills(sys);
  const groups = Object.entries(ATTRIBUTES).map(([k, def]) => {
    const v = sys.attributes[k].value;
    const isPref = pref.attrs.has(k);
    const cost = xpCost("attribute", v + 1, isPref);
    return {
      key: k, abbr: def.abbr, label: loc(`D2.Attr.${k}`), value: v, pref: isPref, cost,
      max: v >= MAX_ATTR, can: v < MAX_ATTR && cost <= avail,
      skills: def.skills.filter(s => !locked.has(s)).map(s => {
        const sv = sys.skills[s].value;
        const sp = pref.skills.has(s);
        const sc = xpCost("skill", sv + 1, sp);
        return { key: s, label: loc(`D2.Skill.${s}`), value: sv, pref: sp, cost: sc, max: sv >= MAX_SKILL, can: sv < MAX_SKILL && sc <= avail, pool: v + sv };
      })
    };
  });
  const sum = potSum(actor);
  const potentials = actor.items.filter(i => i.type === "potencjal" && !i.system.zjawisko).map(i => {
    const lvl = i.system.level ?? 1;
    const cost = xpCost("potential", sum + 1);
    return { id: i.id, name: i.name, level: lvl, cost, max: lvl >= 3, can: lvl < 3 && cost <= avail };
  });
  const log = [...(sys.xp.log ?? [])].reverse().slice(0, 15).map(e => ({ ...e, pos: e.delta > 0 }));
  return {
    groups, potentials, log, avail, total: sys.xp.total, spent: sys.xp.spent,
    newPotCost: xpCost("potential", sum + 1), awards: AWARDS, isGM: game.user.isGM,
    origin: [pref.origin.kultura?.name, pref.origin.koncept?.name, pref.origin.kult?.name].filter(Boolean).join(" · ")
  };
}

async function confirm(title, html) {
  return DialogV2.confirm({ window: { title }, content: html, rejectClose: false, modal: true });
}

function logEntry(sys, t, delta) {
  const log = [...(sys.xp.log ?? []), { t, delta, date: new Date().toLocaleDateString("pl-PL") }];
  return log.slice(-60);
}

export async function awardXp(actor, amount, reason) {
  const sys = actor.system;
  await actor.update({ "system.xp.total": sys.xp.total + amount, "system.xp.log": logEntry(sys, reason, amount) });
  ChatMessage.create({ speaker: ChatMessage.getSpeaker({ actor }), content: `<p><b>${actor.name}</b> otrzymuje <b>${amount} PD</b>: ${reason}.</p>`, whisper: [] });
}

/** Zakup: kind = attr | skill | potential */
export async function buy(actor, kind, key) {
  const sys = actor.system;
  const ctx = await progressionContext(actor);
  let label, cost, update = {};
  if (kind === "attr") {
    const g = ctx.groups.find(g => g.key === key);
    if (!g || g.max) return;
    label = `${g.label} ${g.value} → ${g.value + 1}`; cost = g.cost;
    update[`system.attributes.${key}.value`] = g.value + 1;
  } else if (kind === "skill") {
    const s = ctx.groups.flatMap(g => g.skills).find(s => s.key === key);
    if (!s || s.max) return;
    label = `${s.label} ${s.value} → ${s.value + 1}`; cost = s.cost;
    update[`system.skills.${key}.value`] = s.value + 1;
  } else if (kind === "potential") {
    const p = ctx.potentials.find(p => p.id === key);
    if (!p || p.max) return;
    label = `${p.name}: poziom ${p.level} → ${p.level + 1}`; cost = p.cost;
  } else return;
  if (cost > sys.xp.available) return ui.notifications.warn(`Za mało PD: potrzeba ${cost}, dostępne ${sys.xp.available}.`);
  const ok = await confirm("Rozwój postaci", `<p>Kupić <b>${label}</b> za <b>${cost} PD</b>?</p><p>Zostanie: ${sys.xp.available - cost} PD.</p>`);
  if (!ok) return;
  update["system.xp.spent"] = sys.xp.spent + cost;
  update["system.xp.log"] = logEntry(sys, label, -cost);
  if (kind === "potential") await actor.items.get(key).update({ "system.level": ctx.potentials.find(p => p.id === key).level + 1 });
  await actor.update(update);
  ChatMessage.create({ speaker: ChatMessage.getSpeaker({ actor }), content: `<p><b>${actor.name}</b> rozwija się: ${label} (−${cost} PD).</p>` });
}

/** Nowy Potencjał z kompendium (poziom 1). */
export async function buyNewPotential(actor) {
  const sys = actor.system;
  const pack = game.packs.get(`${SYSTEM_ID}.potencjaly`);
  if (!pack) return;
  const docs = await pack.getDocuments();
  const { origin } = await preferredSets(actor);
  const kult = origin.kult?.name ?? sys.identity.kult ?? "";
  const owned = new Set(actor.items.filter(i => i.type === "potencjal").map(i => i.name));
  const list = docs.filter(d => !owned.has(d.name) && (!d.system.kult || d.system.kult === "Ogólne" || (kult && kult.startsWith(d.system.kult))))
    .sort((a, b) => (a.system.kult === "Ogólne") - (b.system.kult === "Ogólne") || a.name.localeCompare(b.name, "pl"));
  const cost = xpCost("potential", potSum(actor) + 1);
  if (!list.length) return ui.notifications.info("Brak dostępnych Potencjałów.");
  const opts = list.map(d => `<option value="${d.id}">${d.name} — ${d.system.kult || "Ogólne"}${d.system.prerequisite ? ` (wym.: ${d.system.prerequisite})` : ""}</option>`).join("");
  const choice = await DialogV2.prompt({
    window: { title: "Nowy Potencjał" },
    content: `<p>Koszt: <b>${cost} PD</b> (masz ${sys.xp.available}). Sprawdź wymaganie — MG zatwierdza.</p><select name="pot" style="width:100%">${opts}</select>`,
    ok: { label: "Kup", callback: (e, b) => b.form.elements.pot.value },
    rejectClose: false
  });
  if (!choice) return;
  if (cost > sys.xp.available) return ui.notifications.warn(`Za mało PD: potrzeba ${cost}.`);
  const doc = list.find(d => d.id === choice);
  const data = doc.toObject(); delete data._id; data.system.level = 1;
  await actor.createEmbeddedDocuments("Item", [data]);
  await actor.update({ "system.xp.spent": sys.xp.spent + cost, "system.xp.log": logEntry(sys, `Nowy Potencjał: ${doc.name}`, -cost) });
  ChatMessage.create({ speaker: ChatMessage.getSpeaker({ actor }), content: `<p><b>${actor.name}</b> zdobywa Potencjał <b>${doc.name}</b> (−${cost} PD).</p>` });
}

/** Cofnięcie ostatniego wpisu (tylko MG). */
export async function undoLast(actor) {
  const sys = actor.system;
  const log = [...(sys.xp.log ?? [])];
  const last = log.pop();
  if (!last) return;
  const ok = await confirm("Cofnij wpis", `<p>Cofnąć wpis „${last.t}” (${last.delta > 0 ? "+" : ""}${last.delta} PD)? Wartości cech popraw ręcznie, jeśli to był zakup.</p>`);
  if (!ok) return;
  const upd = { "system.xp.log": log };
  if (last.delta > 0) upd["system.xp.total"] = Math.max(0, sys.xp.total - last.delta);
  else upd["system.xp.spent"] = Math.max(0, sys.xp.spent + last.delta);
  await actor.update(upd);
}

/** Masowe przyznanie PD wszystkim postaciom graczy (makro / przycisk MG). */
export async function awardParty() {
  const pcs = game.actors.filter(a => a.type === "postac" && a.hasPlayerOwner);
  if (!pcs.length) return ui.notifications.warn("Brak postaci graczy.");
  const rows = pcs.map(a => `<label style="display:block"><input type="checkbox" name="a" value="${a.id}" checked> ${a.name}</label>`).join("");
  const aw = AWARDS.map((w, i) => `<label style="display:block"><input type="checkbox" name="w" value="${i}" ${i === 0 ? "checked" : ""}> +${w.amount} ${w.reason}</label>`).join("");
  const res = await DialogV2.prompt({
    window: { title: "Przyznaj PD drużynie" },
    content: `<div class="d2-grid-2"><div><h4>Postacie</h4>${rows}</div><div><h4>Za co</h4>${aw}<label>Inne: <input type="number" name="extra" value="0" style="width:4em"></label></div></div>`,
    ok: { label: "Przyznaj", callback: (e, b) => ({
      actors: [...b.form.querySelectorAll("input[name=a]:checked")].map(i => i.value),
      awards: [...b.form.querySelectorAll("input[name=w]:checked")].map(i => AWARDS[Number(i.value)]),
      extra: Number(b.form.elements.extra.value) || 0 }) },
    rejectClose: false
  });
  if (!res) return;
  for (const id of res.actors) {
    const a = game.actors.get(id);
    for (const w of res.awards) await awardXp(a, w.amount, w.reason);
    if (res.extra) await awardXp(a, res.extra, "Decyzja MG");
  }
}

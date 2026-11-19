/**
 * Dług i Imię — operacje na Rejestrze Długów i Imieniu frakcji.
 */
import { SYSTEM_ID } from "./config.mjs";
import { adjustEcho, debtEchoDelta } from "./rules.mjs";

const loc = (k, d) => game.i18n.format(k, d ?? {});

/** Aktor po UUID (synchronicznie, tylko dokumenty świata). */
export function actorFromRef(ref) {
  if (!ref) return null;
  try {
    return foundry.utils.fromUuidSync(ref) ?? null;
  } catch {
    return null;
  }
}

export function partyName(ref, text) {
  return actorFromRef(ref)?.name ?? (text || "—");
}

/** Wszystkie długi, w których aktor jest dłużnikiem albo wierzycielem. */
export function debtsFor(actor, { includeHidden = false } = {}) {
  const out = [];
  for (const reg of game.actors?.filter(a => a.type === "rejestr") ?? []) {
    reg.system.debts.forEach((d, index) => {
      if (d.hidden && !includeHidden) return;
      const asDebtor = d.debtor === actor.uuid;
      const asCreditor = d.creditor === actor.uuid;
      if (!asDebtor && !asCreditor) return;
      out.push({
        ...d, index, registry: reg.id,
        role: asDebtor ? "debtor" : "creditor",
        other: asDebtor ? partyName(d.creditor, d.creditorText) : partyName(d.debtor, d.debtorText)
      });
    });
  }
  return out;
}

/** Zmiana Echa frakcji z komunikatem na czacie. */
export async function shiftEcho(faction, delta, reason = "") {
  if (!faction || faction.type !== "frakcja" || !delta) return null;
  const { value, echo } = faction.system.imie;
  const r = adjustEcho(value, echo, delta);
  await faction.update({ "system.imie.value": r.imie, "system.imie.echo": r.echo });
  const tier = loc(`D2.Imie.tier.${String(r.imie)}`);
  let content = loc("D2.Imie.echoChat", { faction: faction.name, delta: delta > 0 ? `+${delta}` : `${delta}`, reason });
  if (r.change) content += `<br><b>${loc(r.change > 0 ? "D2.Imie.up" : "D2.Imie.down", { faction: faction.name, tier })}</b>`;
  await ChatMessage.create({
    content: `<div class="d2 chat-note imie-note"><i class="fa-solid fa-scale-balanced"></i> ${content}</div>`,
    whisper: game.users.filter(u => u.isGM).map(u => u.id)
  });
  return r;
}

/** Zmiana statusu długu (Spłać, Ściągnij, Zerwij) z automatyką Echa. */
export async function setDebtStatus(registry, index, status) {
  const debts = foundry.utils.deepClone(registry.system.debts);
  const d = debts[index];
  if (!d) return;
  const prev = d.status;
  d.status = status;
  await registry.update({ "system.debts": debts });

  const debtor = partyName(d.debtor, d.debtorText);
  const creditor = partyName(d.creditor, d.creditorText);
  const content = loc(`D2.Dlug.chat.${status}`, { debtor, creditor, powod: d.powod || "—", waga: loc(`D2.Dlug.waga.${d.waga}`) });
  await ChatMessage.create({
    content: `<div class="d2 chat-note dlug-note dlug-${status}"><i class="fa-solid fa-handshake"></i> ${content}</div>`,
    whisper: d.hidden ? game.users.filter(u => u.isGM).map(u => u.id) : []
  });

  // Echo frakcji-wierzyciela tylko przy pierwszym przejściu z „otwarty”
  if (prev === "otwarty") {
    const faction = actorFromRef(d.creditor);
    const delta = debtEchoDelta(status, d.waga);
    if (faction?.type === "frakcja" && delta) await shiftEcho(faction, delta, d.powod);
  }
}

/** Wezwanie długu: komunikat na czacie, status bez zmian. */
export async function callDebt(registry, index) {
  const d = registry.system.debts[index];
  if (!d) return;
  const content = loc("D2.Dlug.chat.wezwanie", {
    debtor: partyName(d.debtor, d.debtorText), creditor: partyName(d.creditor, d.creditorText),
    powod: d.powod || "—", waga: loc(`D2.Dlug.waga.${d.waga}`)
  });
  return ChatMessage.create({ content: `<div class="d2 chat-note dlug-note dlug-wezwanie"><i class="fa-solid fa-bell"></i> ${content}</div>` });
}

/** Lista aktorów do wyboru jako strona długu. */
export function partyOptions() {
  const groups = { postac: [], npc: [], frakcja: [] };
  for (const a of game.actors ?? []) if (groups[a.type]) groups[a.type].push({ value: a.uuid, label: a.name });
  for (const g of Object.values(groups)) g.sort((x, y) => x.label.localeCompare(y.label, "pl"));
  return [
    { label: loc("TYPES.Actor.postac"), options: groups.postac },
    { label: loc("TYPES.Actor.frakcja"), options: groups.frakcja },
    { label: loc("TYPES.Actor.npc"), options: groups.npc }
  ];
}

export { SYSTEM_ID };

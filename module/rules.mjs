/**
 * Czysta logika reguł Katharsys 2.0 — bez zależności od Foundry,
 * dzięki czemu da się ją testować w Node.
 */
import { MAX_DICE, WOUND_SLOTS } from "./config.mjs";

/**
 * Pula: atrybut + umiejętność + modyfikatory. Powyżej 12 kości nadwyżka
 * zamienia się w automatyczne sukcesy. Pula nie spada poniżej 0.
 * @returns {{dice:number, autoSuccesses:number}}
 */
export function buildPool(total) {
  const n = Math.max(0, Math.floor(total));
  if (n <= MAX_DICE) return { dice: n, autoSuccesses: 0 };
  return { dice: MAX_DICE, autoSuccesses: n - MAX_DICE };
}

/**
 * Ocena rzutu.
 * @param {number[]} results  wyniki k6
 * @param {object} opts
 * @param {number|null} opts.difficulty  null = rzut bez progu (np. inicjatywa)
 * @param {number} [opts.autoSuccesses=0]
 * @returns {{successes:number, triggers:number, ones:number, outcome:string, shortfall:number}}
 *
 * outcome: "tak-i" | "tak" | "tak-ale" | "nie" | "nie-i" | "brak" (bez progu)
 */
export function evaluateRoll(results, { difficulty = 2, autoSuccesses = 0 } = {}) {
  const successes = results.filter(r => r >= 4).length + autoSuccesses;
  const triggers = results.filter(r => r === 6).length;
  const ones = results.filter(r => r === 1).length;

  if (difficulty === null || difficulty === undefined) {
    return { successes, triggers, ones, outcome: "brak", shortfall: 0 };
  }

  const shortfall = Math.max(0, difficulty - successes);

  // Zgrzyt: więcej jedynek niż sukcesów (i porażka)
  if (shortfall > 0 && ones > successes) {
    return { successes, triggers: 0, ones, outcome: "nie-i", shortfall };
  }
  if (shortfall === 0) {
    return { successes, triggers, ones, outcome: triggers > 0 ? "tak-i" : "tak", shortfall };
  }
  // Sukces z kosztem: min. 1 sukces i brakuje najwyżej 2
  if (successes >= 1 && shortfall <= 2) {
    return { successes, triggers: 0, ones, outcome: "tak-ale", shortfall };
  }
  return { successes, triggers: 0, ones, outcome: "nie", shortfall };
}

/** Starcie: zwraca "atak" | "obrona" (remis -> obrońca / status quo). */
export function resolveContest(a, b) {
  if (a.successes !== b.successes) return a.successes > b.successes ? "atak" : "obrona";
  if (a.triggers !== b.triggers) return a.triggers > b.triggers ? "atak" : "obrona";
  return "obrona";
}

/**
 * Obrażenia broni. Obsługuje liczby i wyrażenia typu "2+F/2", "F/3", "F", "8".
 * F = CIA + Siła. Dzielenie zaokrągla w dół (jak w Rebirth).
 */
export function parseDamage(expr, force = 0) {
  if (typeof expr === "number") return expr;
  const s = String(expr ?? "").replace(/\s+/g, "").toUpperCase();
  if (!s) return 0;
  if (!/^[0-9F+\-/]+$/.test(s)) return 0;
  let total = 0;
  const terms = s.match(/[+-]?[^+-]+/g) ?? [];
  for (const term of terms) {
    const sign = term.startsWith("-") ? -1 : 1;
    const body = term.replace(/^[+-]/, "");
    const [base, div] = body.split("/");
    let v = base === "F" ? force : Number(base);
    if (!Number.isFinite(v)) v = 0;
    if (div) {
      const d = Number(div);
      v = d > 0 ? Math.floor(v / d) : v;
    }
    total += sign * v;
  }
  return total;
}

/**
 * Stopień rany wg obrażeń netto i Progu.
 * @returns {null|"lekkie"|"powazne"|"krytyczna"}
 */
export function woundTier(net, threshold) {
  const t = Math.max(1, threshold);
  if (net <= 0) return null;
  if (net >= 2 * t) return "krytyczna";
  if (net >= t) return "powazne";
  return "lekkie";
}

const ORDER = ["lekkie", "powazne", "krytyczna"];

export function downgradeTier(tier, steps = 1) {
  if (!tier) return null;
  const i = ORDER.indexOf(tier) - steps;
  return i < 0 ? null : ORDER[i];
}

/**
 * Nakłada ranę na stan. Pełne miejsca -> rana o stopień wyżej.
 * Brak miejsca na Krytyczną -> wyeliminowany.
 * @param {{lekkie:number,powazne:number,krytyczna:number}} wounds
 * @param {string} tier
 * @param {{lekkie:number,powazne:number,krytyczna:number}} slots
 * @returns {{wounds:object, appliedTier:string|null, eliminated:boolean}}
 */
export function applyWound(wounds, tier, slots = WOUND_SLOTS.antagonista) {
  const w = { lekkie: 0, powazne: 0, krytyczna: 0, ...wounds };
  if (!tier) return { wounds: w, appliedTier: null, eliminated: false };
  let i = ORDER.indexOf(tier);
  while (i < ORDER.length) {
    const key = ORDER[i];
    if (w[key] < (slots[key] ?? 0)) {
      w[key] += 1;
      return { wounds: w, appliedTier: key, eliminated: false };
    }
    i += 1;
  }
  return { wounds: w, appliedTier: null, eliminated: true };
}

/** Kara do pul z ran: −1K za Poważną, −2K za Krytyczną. */
export function woundPenalty(wounds) {
  return (wounds?.powazne ?? 0) * 1 + (wounds?.krytyczna ?? 0) * 2;
}

/** Banda: eliminacje wg stopnia rany. */
export function gangCasualties(tier) {
  return { lekkie: 1, powazne: 2, krytyczna: 3 }[tier] ?? 0;
}

/** Banda: bonus do ataku +1K za każdych 2 członków, maks. +4K. */
export function gangBonus(size) {
  return Math.min(4, Math.floor(Math.max(0, size) / 2));
}

/** Pełny przebieg trafienia. */
export function resolveHit({ damage, triggers = 0, armor = 0, threshold }) {
  const net = damage + triggers - armor;
  return { net, tier: woundTier(net, threshold) };
}

/** Wyrocznia FU: k6 -> klucz odpowiedzi. */
export function oracle(results, mode = "normal") {
  let r;
  if (mode === "likely") r = Math.max(...results);
  else if (mode === "unlikely") r = Math.min(...results);
  else r = results[0];
  return ["nie-i", "nie", "nie-ale", "tak-ale", "tak", "tak-i"][r - 1];
}

/** Koszt PD: atrybut/umiejętność do nowej wartości. */
export function xpCost(kind, newValue, preferred = false) {
  if (kind === "attribute") return newValue * (preferred ? 10 : 12);
  if (kind === "skill") return newValue * (preferred ? 4 : 5);
  if (kind === "potential") return newValue * 10; // newValue = suma poziomów po podniesieniu
  return 0;
}

/* -------------------- Dług i Imię -------------------- */

/** Domyślna Postawa członków frakcji wynikająca z Imienia drużyny. */
export function imieToAttitude(imie) {
  const v = Math.max(-3, Math.min(3, Math.trunc(imie)));
  return { "-3": -2, "-2": -2, "-1": -1, "0": 0, "1": 1, "2": 1, "3": 2 }[String(v)];
}

/**
 * Przesuwa Echo. Przy ±4 Imię zmienia się o 1, a Echo wraca do 0.
 * Nadwyżka przechodzi dalej (np. −6 przy Echu 0 = Imię −1, Echo −2).
 * Na krańcach skali (±3) Echo zatrzymuje się na granicy.
 * @returns {{imie:number, echo:number, change:number}}
 */
export function adjustEcho(imie, echo, delta, limit = 4) {
  let i = imie, e = echo + delta, change = 0;
  while (e >= limit && i < 3) { i += 1; e -= limit; change += 1; }
  while (e <= -limit && i > -3) { i -= 1; e += limit; change -= 1; }
  e = Math.max(i <= -3 ? -limit : -(limit - 1), Math.min(i >= 3 ? limit : limit - 1, e));
  return { imie: i, echo: e, change };
}

/** Zmiana Echa frakcji wierzyciela przy zmianie statusu długu. */
export function debtEchoDelta(status, weight) {
  if (status === "splacony") return 1;
  if (status === "zerwany") return -2 * weight;
  return 0;
}

/* -------------------- Tworzenie postaci -------------------- */

export const CREATION = { attrPoints: 10, skillPoints: 28, bgPoints: 4, attrBase: 1, attrSpend: 2, skillSpend: 2, bgMax: 3 };

/** Limit atrybutu: 1 + 2 + liczba bonusów 3K. */
export function attrLimit(key, bonusLists) {
  return CREATION.attrBase + CREATION.attrSpend + bonusLists.filter(l => (l ?? []).includes(key)).length;
}

/** Limit umiejętności: 2 + liczba bonusów 3K. */
export function skillLimit(key, bonusLists) {
  return CREATION.skillSpend + bonusLists.filter(l => (l ?? []).includes(key)).length;
}

/**
 * Bilans punktów kreatora.
 * @param {object} s {attrs:{k:n}, skills:{k:n}, bgs:{k:n}}
 */
export function creationBudget(s) {
  const attrSpent = Object.values(s.attrs).reduce((t, v) => t + Math.max(0, v - CREATION.attrBase), 0);
  const skillSpent = Object.values(s.skills).reduce((t, v) => t + Math.max(0, v), 0);
  const bgSpent = Object.values(s.bgs).reduce((t, v) => t + Math.max(0, v), 0);
  return {
    attrLeft: CREATION.attrPoints - attrSpent,
    skillLeft: CREATION.skillPoints - skillSpent,
    bgLeft: CREATION.bgPoints - bgSpent
  };
}

/**
 * Sprawdza wymagania rangi.
 * Wpis: [attr, skill, n] (AN = atrybut+umiejętność) · ["bg", key, n] · ["txt", opis] · lista wpisów = LUB.
 * @param {Array} prereqs
 * @param {{attrs:object, skills:object, bgs:object}} stats
 * @returns {{ok:boolean, manual:string[], missing:string[]}}
 */
export function checkPrereqs(prereqs, stats, label = (e) => e.join(" ")) {
  const missing = [], manual = [];
  const test = (e) => {
    if (e[0] === "txt") { manual.push(e[1]); return true; }
    if (e[0] === "bg") return (stats.bgs[e[1]] ?? 0) >= e[2];
    return (stats.attrs[e[0]] ?? 0) + (stats.skills[e[1]] ?? 0) >= e[2];
  };
  for (const p of prereqs ?? []) {
    if (Array.isArray(p[0])) {
      if (!p.some(test)) missing.push(p.map(label).join(" lub "));
    } else if (!test(p)) missing.push(label(p));
  }
  return { ok: missing.length === 0, manual, missing };
}

import test from "node:test";
import assert from "node:assert/strict";
import { buildPool, evaluateRoll, parseDamage, woundTier, applyWound, woundPenalty, resolveContest, oracle, gangBonus, gangCasualties, xpCost, resolveHit, downgradeTier } from "../module/rules.mjs";
import { WOUND_SLOTS, ALL_SKILLS } from "../module/config.mjs";

test("36 umiejętności", () => assert.equal(ALL_SKILLS.length, 36));
test("pula > 12 daje auto sukcesy", () => {
  assert.deepEqual(buildPool(15), { dice: 12, autoSuccesses: 3 });
  assert.deepEqual(buildPool(-2), { dice: 0, autoSuccesses: 0 });
});
test("drabina wyników", () => {
  assert.equal(evaluateRoll([6, 4, 2], { difficulty: 2 }).outcome, "tak-i");
  assert.equal(evaluateRoll([5, 4, 2], { difficulty: 2 }).outcome, "tak");
  assert.equal(evaluateRoll([5, 2, 2], { difficulty: 3 }).outcome, "tak-ale");
  assert.equal(evaluateRoll([5, 2, 2], { difficulty: 4 }).outcome, "nie");
  assert.equal(evaluateRoll([2, 3, 2], { difficulty: 1 }).outcome, "nie");
  assert.equal(evaluateRoll([1, 1, 4], { difficulty: 3 }).outcome, "nie-i");
  assert.equal(evaluateRoll([6, 6], { difficulty: null }).outcome, "brak");
  // Wyzwalacze przepadają przy sukcesie z kosztem
  assert.equal(evaluateRoll([6, 2, 2], { difficulty: 2 }).triggers, 0);
  assert.equal(evaluateRoll([], { difficulty: 1, autoSuccesses: 1 }).outcome, "tak");
});
test("obrażenia z F", () => {
  assert.equal(parseDamage("2+F/2", 8), 6);
  assert.equal(parseDamage("F/3", 7), 2);
  assert.equal(parseDamage("9", 3), 9);
  assert.equal(parseDamage(10, 0), 10);
  assert.equal(parseDamage("alert(1)", 3), 0);
});
test("stopnie ran", () => {
  assert.equal(woundTier(0, 6), null);
  assert.equal(woundTier(5, 6), "lekkie");
  assert.equal(woundTier(6, 6), "powazne");
  assert.equal(woundTier(12, 6), "krytyczna");
  assert.deepEqual(resolveHit({ damage: 8, triggers: 1, armor: 2, threshold: 6 }), { net: 7, tier: "powazne" });
  assert.equal(downgradeTier("lekkie"), null);
});
test("pełne miejsca przechodzą wyżej i eliminują", () => {
  let w = { lekkie: 3, powazne: 1, krytyczna: 0 };
  let r = applyWound(w, "lekkie", WOUND_SLOTS.antagonista);
  assert.equal(r.appliedTier, "powazne"); assert.equal(r.wounds.powazne, 2);
  r = applyWound(r.wounds, "lekkie", WOUND_SLOTS.antagonista);
  assert.equal(r.appliedTier, "krytyczna");
  r = applyWound(r.wounds, "lekkie", WOUND_SLOTS.antagonista);
  assert.equal(r.eliminated, true);
  assert.equal(woundPenalty({ lekkie: 3, powazne: 2, krytyczna: 1 }), 4);
  const wet = applyWound({ lekkie: 0, powazne: 0, krytyczna: 0 }, "powazne", WOUND_SLOTS.weteran);
  assert.equal(wet.appliedTier, "powazne");
  assert.equal(applyWound(wet.wounds, "lekkie", WOUND_SLOTS.weteran).appliedTier, "lekkie");
});
test("starcie, wyrocznia, banda, PD", () => {
  assert.equal(resolveContest({ successes: 3, triggers: 0 }, { successes: 3, triggers: 1 }), "obrona");
  assert.equal(resolveContest({ successes: 3, triggers: 2 }, { successes: 3, triggers: 1 }), "atak");
  assert.equal(oracle([1]), "nie-i"); assert.equal(oracle([6]), "tak-i");
  assert.equal(oracle([2, 5], "likely"), "tak"); assert.equal(oracle([2, 5], "unlikely"), "nie");
  assert.equal(gangBonus(9), 4); assert.equal(gangCasualties("powazne"), 2);
  assert.equal(xpCost("skill", 4), 20); assert.equal(xpCost("attribute", 4), 48);
});

import { adjustEcho, imieToAttitude, debtEchoDelta } from "../module/rules.mjs";
test("Imię i Echo", () => {
  assert.deepEqual(adjustEcho(0, 3, 1), { imie: 1, echo: 0, change: 1 });
  assert.deepEqual(adjustEcho(0, 0, -6), { imie: -1, echo: -2, change: -1 });
  assert.deepEqual(adjustEcho(3, 3, 5), { imie: 3, echo: 4, change: 0 });
  assert.deepEqual(adjustEcho(-3, -3, -2), { imie: -3, echo: -4, change: 0 });
  assert.deepEqual(adjustEcho(1, -1, -11), { imie: -2, echo: 0, change: -3 });
  assert.equal(imieToAttitude(-3), -2); assert.equal(imieToAttitude(2), 1); assert.equal(imieToAttitude(3), 2);
  assert.equal(debtEchoDelta("zerwany", 3), -6); assert.equal(debtEchoDelta("splacony", 2), 1); assert.equal(debtEchoDelta("sciagniety", 2), 0);
});

import { checkPrereqs, creationBudget, attrLimit, skillLimit } from "../module/rules.mjs";
import fs from "node:fs";
test("kreator: limity i budżet", () => {
  assert.equal(attrLimit("int", [["int"], ["int"]]), 5);
  assert.equal(skillLimit("medycyna", [["medycyna"], [], ["medycyna"]]), 4);
  const b = creationBudget({ attrs: { cia: 3, zre: 1, cha: 1, int: 1, psy: 1, ins: 1 }, skills: { a: 5 }, bgs: { x: 1 } });
  assert.deepEqual(b, { attrLeft: 8, skillLeft: 23, bgLeft: 3 });
});
test("wymagania rang z danych kompendium", () => {
  const dir = new URL("../src/packs/kulty", import.meta.url).pathname;
  const sp = fs.readdirSync(dir).map(f => JSON.parse(fs.readFileSync(`${dir}/${f}`))).find(d => d.name === "Spitalianie");
  const fam = sp.system.ranks.find(r => r.name === "Famulancer");
  const pre = JSON.parse(fam.prereq);
  const ok = checkPrereqs(pre, { attrs: { cia: 2, int: 3 }, skills: { twardosc: 3, medycyna: 4, nauka: 3 }, bgs: {} });
  assert.equal(ok.ok, true);
  const no = checkPrereqs(pre, { attrs: { cia: 2, int: 3 }, skills: { twardosc: 1, medycyna: 2, nauka: 3 }, bgs: {} });
  assert.equal(no.ok, false); assert.equal(no.missing.length, 2);
  // LUB: Protektor (Skupienie lub Pierwotność 6)
  const sd = fs.readdirSync(dir).map(f => JSON.parse(fs.readFileSync(`${dir}/${f}`))).find(d => d.name === "Sędziowie");
  const prot = JSON.parse(sd.system.ranks.find(r => r.name.startsWith("Protektor")).prereq);
  const r = checkPrereqs(prot, { attrs: { zre: 3, ins: 4, psy: 3 }, skills: { prowadzenie: 3, pierwotnosc: 2, refleks: 3 }, bgs: { sojusznicy: 2 } });
  assert.equal(r.ok, true);
  // pole txt -> do oceny MG
  const an = fs.readdirSync(dir).map(f => JSON.parse(fs.readFileSync(`${dir}/${f}`))).find(d => d.name === "Anubianie");
  const ini = checkPrereqs(JSON.parse(an.system.ranks[0].prereq), { attrs: {}, skills: {}, bgs: {} });
  assert.equal(ini.ok, true); assert.equal(ini.manual.length, 1);
});

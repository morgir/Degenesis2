/**
 * Degenesis: Katharsys 2.0 — nieoficjalny system fanowski dla Foundry VTT v14.
 */
import * as CONFIG_D2 from "./module/config.mjs";
import * as rules from "./module/rules.mjs";
import { PostacModel, NpcModel, FrakcjaModel, SledztwoModel, LokacjaModel, RejestrModel } from "./module/data/actors.mjs";
import { BronModel, PancerzModel, EkwipunekModel, PotencjalModel, KulturaModel, KonceptModel, KultModel } from "./module/data/items.mjs";
import { D2Actor, D2Item } from "./module/documents.mjs";
import { D2PostacSheet, D2NpcSheet, D2FrakcjaSheet, D2SledztwoSheet, D2LokacjaSheet, D2RejestrSheet } from "./module/sheets/actor-sheet.mjs";
import { D2ItemSheet } from "./module/sheets/item-sheet.mjs";
import { rollDialog, performRoll, rollOracle, oracleDialog } from "./module/dice.mjs";
import { D2CharacterCreator } from "./module/apps/creator.mjs";
import { awardParty } from "./module/progression.mjs";
import { registerInstallerSettings, checkInstaller, openInstaller } from "./module/apps/installer.mjs";
import { shiftEcho, setDebtStatus, callDebt, debtsFor } from "./module/debts.mjs";

const { SYSTEM_ID } = CONFIG_D2;

Hooks.once("init", () => {
  registerInstallerSettings();
  console.log(`${SYSTEM_ID} | Inicjalizacja Degenesis: Katharsys 2.0`);

  CONFIG.Actor.documentClass = D2Actor;
  CONFIG.Item.documentClass = D2Item;

  Object.assign(CONFIG.Actor.dataModels, {
    postac: PostacModel, npc: NpcModel, frakcja: FrakcjaModel, sledztwo: SledztwoModel, lokacja: LokacjaModel, rejestr: RejestrModel
  });
  Object.assign(CONFIG.Item.dataModels, {
    bron: BronModel, pancerz: PancerzModel, ekwipunek: EkwipunekModel, potencjal: PotencjalModel,
    kultura: KulturaModel, koncept: KonceptModel, kult: KultModel
  });

  CONFIG.Actor.trackableAttributes = {
    postac: { bar: ["ego"], value: [] },
    npc: { bar: ["ego", "size"], value: [] }
  };

  // Inicjatywa: PSY+Refleks, liczy sukcesy (4+). Rzucana raz na starcie.
  CONFIG.Combat.initiative = { formula: "(@initPool)d6cs>=4", decimals: 0 };

  const DSC = foundry.applications.apps.DocumentSheetConfig;
  DSC.registerSheet(Actor, SYSTEM_ID, D2PostacSheet, { types: ["postac"], makeDefault: true, label: "D2.Sheet.postac" });
  DSC.registerSheet(Actor, SYSTEM_ID, D2NpcSheet, { types: ["npc"], makeDefault: true, label: "D2.Sheet.npc" });
  DSC.registerSheet(Actor, SYSTEM_ID, D2FrakcjaSheet, { types: ["frakcja"], makeDefault: true, label: "D2.Sheet.frakcja" });
  DSC.registerSheet(Actor, SYSTEM_ID, D2SledztwoSheet, { types: ["sledztwo"], makeDefault: true, label: "D2.Sheet.sledztwo" });
  DSC.registerSheet(Actor, SYSTEM_ID, D2LokacjaSheet, { types: ["lokacja"], makeDefault: true, label: "D2.Sheet.lokacja" });
  DSC.registerSheet(Actor, SYSTEM_ID, D2RejestrSheet, { types: ["rejestr"], makeDefault: true, label: "D2.Sheet.rejestr" });
  DSC.registerSheet(Item, SYSTEM_ID, D2ItemSheet, { makeDefault: true, label: "D2.Sheet.item" });

  registerHelpers();
  foundry.applications.handlebars.loadTemplates([
    `systems/${SYSTEM_ID}/templates/parts/clocks.hbs`,
    `systems/${SYSTEM_ID}/templates/parts/stats.hbs`,
    `systems/${SYSTEM_ID}/templates/parts/wounds.hbs`,
    `systems/${SYSTEM_ID}/templates/parts/weapons.hbs`
  ]);

  game.degenesis2 = {
    config: CONFIG_D2, rules, rollDialog, performRoll, rollOracle, oracleDialog,
    newSession, applyDamageToTargets,
    shiftEcho, setDebtStatus, callDebt, debtsFor,
    openCreator: openCreatorSafe,
    awardParty, newCharacter,
    install: openInstaller
  };
});

function registerHelpers() {
  const H = Handlebars;
  H.registerHelper("d2eq", (a, b) => a === b);
  H.registerHelper("d2or", (a, b) => !!(a || b));
  H.registerHelper("d2signed", n => (n > 0 ? `+${n}` : `${n}`));
  H.registerHelper("d2loc", (prefix, key) => game.i18n.localize(`${prefix}.${key}`));
}

/** Nowa sesja: odnawia Archetyp wszystkim postaciom graczy. */
async function newSession() {
  if (!game.user.isGM) return ui.notifications.warn(game.i18n.localize("D2.Warn.gmOnly"));
  const pcs = game.actors.filter(a => a.type === "postac");
  for (const a of pcs) await a.update({ "system.archetypeUsed": false });
  ChatMessage.create({ content: `<div class="d2 chat-note"><i class="fa-solid fa-sun"></i> ${game.i18n.localize("D2.Session.new")}</div>` });
}

/** Nakłada obrażenia na tokeny wybrane jako cele, a gdy ich brak — na kontrolowane. */
async function applyDamageToTargets(damage, opts = {}) {
  let tokens = [...game.user.targets];
  if (!tokens.length) tokens = canvas.tokens?.controlled ?? [];
  if (!tokens.length) return ui.notifications.warn(game.i18n.localize("D2.Warn.noTarget"));
  for (const t of tokens) {
    const actor = t.actor;
    if (!actor) continue;
    if (!actor.isOwner && !game.user.isGM) {
      ui.notifications.warn(game.i18n.format("D2.Warn.notOwner", { name: actor.name }));
      continue;
    }
    await actor.applyDamage(damage, opts);
  }
}

Hooks.on("renderChatMessageHTML", (message, html) => {
  html.querySelectorAll("[data-d2-action='apply-damage']").forEach(btn => {
    btn.addEventListener("click", ev => {
      ev.preventDefault();
      const dmg = Number(btn.dataset.damage) || 0;
      applyDamageToTargets(dmg);
    });
  });
});

Hooks.once("ready", () => {
  console.log(`${SYSTEM_ID} | Gotowe`);
  checkInstaller();
});

/** Przycisk instalatora w zakładkach Dzienniki, Aktorzy i Sceny (tylko MG). */
for (const hook of ["renderJournalDirectory", "renderActorDirectory", "renderSceneDirectory"]) {
  Hooks.on(hook, (app, html) => {
    if (!game.user.isGM) return;
    const root = html instanceof HTMLElement ? html : html[0];
    const target = root?.querySelector(".header-actions");
    if (!target || target.querySelector(".d2-install-btn")) return;
    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = "d2-install-btn";
    btn.innerHTML = `<i class="fa-solid fa-box-open"></i> Degenesis 2.0`;
    btn.dataset.tooltip = "Instalator zawartości: zasady, przygoda, postacie, przeciwnicy";
    btn.addEventListener("click", () => openInstaller());
    target.append(btn);
  });
}


/** Otwiera kreator i pokazuje błąd zamiast cichej porażki. */
async function openCreatorSafe(actor) {
  try {
    const app = new D2CharacterCreator({ actor });
    await app.render({ force: true });
    return app;
  } catch (err) {
    console.error(`${SYSTEM_ID} | Kreator postaci`, err);
    ui.notifications.error(`Kreator postaci: ${err.message}`);
  }
}

/** Nowa postać + kreator jednym kliknięciem. */
async function newCharacter() {
  const actor = await Actor.create({ name: "Nowa postać", type: "postac", ownership: { default: 0, [game.user.id]: 3 } });
  if (actor) return openCreatorSafe(actor);
}

Hooks.on("renderActorDirectory", (app, html) => {
  if (!game.user.can("ACTOR_CREATE")) return;
  const root = html instanceof HTMLElement ? html : html[0];
  const target = root?.querySelector(".header-actions");
  if (!target || target.querySelector(".d2-newpc-btn")) return;
  const btn = document.createElement("button");
  btn.type = "button";
  btn.className = "d2-newpc-btn";
  btn.innerHTML = `<i class="fa-solid fa-user-plus"></i> Nowa postać (kreator)`;
  btn.addEventListener("click", () => newCharacter());
  target.append(btn);
});

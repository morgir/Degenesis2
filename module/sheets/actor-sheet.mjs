import { ATTRIBUTES, BACKGROUNDS, SYSTEM_ID, NPC_SCALES, IMIE_TIERS } from "../config.mjs";
import { imieToAttitude } from "../rules.mjs";
import { progressionContext, buy, awardXp, buyNewPotential, undoLast } from "../progression.mjs";
import { debtsFor, setDebtStatus, callDebt, shiftEcho, partyOptions, partyName, actorFromRef } from "../debts.mjs";

const { HandlebarsApplicationMixin } = foundry.applications.api;
const { ActorSheetV2 } = foundry.applications.sheets;
const loc = (k, d) => game.i18n.format(k, d ?? {});

const TIERS = [
  { key: "lekkie", slots: "lekkie" },
  { key: "powazne", slots: "powazne" },
  { key: "krytyczna", slots: "krytyczna" }
];

function boxes(value, max) {
  return Array.from({ length: max }, (_, i) => ({ index: i, filled: i < value }));
}

function clockView(clocks) {
  return (clocks ?? []).map((c, i) => ({
    ...c, index: i,
    segments: Array.from({ length: c.size }, (_, s) => ({ seg: s + 1, filled: s < c.value }))
  }));
}

/**
 * Wspólna baza arkuszy aktorów.
 * Pola tablicowe (zegary, tropy, cechy) edytowane przez data-array, nie przez formularz.
 */
export class D2ActorSheet extends HandlebarsApplicationMixin(ActorSheetV2) {
  static DEFAULT_OPTIONS = {
    classes: ["d2", "sheet", "actor"],
    position: { width: 760, height: 820 },
    window: { resizable: true },
    form: { submitOnChange: true, closeOnSubmit: false },
    actions: {
      d2tab: D2ActorSheet.#onTab,
      rollSkill: D2ActorSheet.#onRollSkill,
      rollAttr: D2ActorSheet.#onRollAttr,
      rollItem: D2ActorSheet.#onRollItem,
      itemEdit: D2ActorSheet.#onItemEdit,
      itemDelete: D2ActorSheet.#onItemDelete,
      itemCreate: D2ActorSheet.#onItemCreate,
      itemEquip: D2ActorSheet.#onItemEquip,
      woundBox: D2ActorSheet.#onWoundBox,
      track: D2ActorSheet.#onTrack,
      arrayAdd: D2ActorSheet.#onArrayAdd,
      arrayDelete: D2ActorSheet.#onArrayDelete,
      clockSeg: D2ActorSheet.#onClockSeg,
      bgSpend: D2ActorSheet.#onBgSpend,
      resetArchetype: D2ActorSheet.#onResetArchetype,
      cechaInvoke: D2ActorSheet.#onCechaInvoke,
      cechaToggle: D2ActorSheet.#onCechaToggle,
      oracle: D2ActorSheet.#onOracle,
      reviveEliminated: D2ActorSheet.#onRevive,
      debtStatus: D2ActorSheet.#onDebtStatus,
      debtCall: D2ActorSheet.#onDebtCall,
      echoShift: D2ActorSheet.#onEchoShift,
      applyFactionAttitude: D2ActorSheet.#onApplyFactionAttitude,
      openActor: D2ActorSheet.#onOpenActor,
      openCreator: D2ActorSheet.#onOpenCreator,
      xpBuy: D2ActorSheet.#onXpBuy,
      xpAward: D2ActorSheet.#onXpAward,
      xpNewPotential: D2ActorSheet.#onXpNewPotential,
      xpUndo: D2ActorSheet.#onXpUndo
    }
  };

  /** Aktywna zakładka (pamiętana per arkusz) */
  _activeTab = null;

  async _prepareContext(options) {
    const context = await super._prepareContext(options);
    const actor = this.document;
    const sys = actor.system;
    context.actor = actor;
    context.system = sys;
    context.isGM = game.user.isGM;
    context.editable = this.isEditable;
    context.config = { SYSTEM_ID };
    return context;
  }

  _onRender(context, options) {
    super._onRender?.(context, options);
    const root = this.element;
    // Zakładki
    const tabs = root.querySelectorAll("[data-tab-panel]");
    if (tabs.length) {
      const first = tabs[0].dataset.tabPanel;
      const active = this._activeTab ?? first;
      root.querySelectorAll("[data-tab-panel]").forEach(el => el.classList.toggle("active", el.dataset.tabPanel === active));
      root.querySelectorAll("[data-action='d2tab']").forEach(el => el.classList.toggle("active", el.dataset.tab === active));
    }
    // Pola tablicowe
    root.querySelectorAll("[data-array]").forEach(el => {
      el.addEventListener("change", ev => this.#onArrayChange(ev));
    });
  }

  async #onArrayChange(event) {
    const el = event.currentTarget;
    const path = el.dataset.array;
    const index = Number(el.dataset.index);
    const field = el.dataset.field;
    const arr = foundry.utils.deepClone(foundry.utils.getProperty(this.document.system, path) ?? []);
    if (!arr[index]) return;
    let value = el.type === "checkbox" ? el.checked : el.value;
    if (el.type === "number" || el.dataset.number !== undefined) value = Number(value) || 0;
    arr[index][field] = value;
    if (path === "clocks" && field === "size") arr[index].value = Math.min(arr[index].value, value);
    await this.document.update({ [`system.${path}`]: arr });
  }

  static #onTab(event, target) {
    this._activeTab = target.dataset.tab;
    this.element.querySelectorAll("[data-tab-panel]").forEach(el => el.classList.toggle("active", el.dataset.tabPanel === this._activeTab));
    this.element.querySelectorAll("[data-action='d2tab']").forEach(el => el.classList.toggle("active", el.dataset.tab === this._activeTab));
  }

  static #onRollSkill(event, target) {
    return this.document.rollSkill(target.dataset.skill);
  }

  static #onRollAttr(event, target) {
    return this.document.rollAttribute(target.dataset.attr);
  }

  static #onRollItem(event, target) {
    const item = this.document.items.get(target.closest("[data-item-id]").dataset.itemId);
    return item?.roll();
  }

  static #onItemEdit(event, target) {
    const item = this.document.items.get(target.closest("[data-item-id]").dataset.itemId);
    return item?.sheet.render(true);
  }

  static async #onItemDelete(event, target) {
    const item = this.document.items.get(target.closest("[data-item-id]").dataset.itemId);
    if (!item) return;
    const ok = await foundry.applications.api.DialogV2.confirm({
      window: { title: loc("D2.Sheet.deleteTitle") },
      content: `<p>${loc("D2.Sheet.deleteConfirm", { name: item.name })}</p>`,
      rejectClose: false
    });
    if (ok) return item.delete();
  }

  static #onItemCreate(event, target) {
    const type = target.dataset.type;
    return this.document.createEmbeddedDocuments("Item", [{ name: loc(`TYPES.Item.${type}`), type }]);
  }

  static #onItemEquip(event, target) {
    const item = this.document.items.get(target.closest("[data-item-id]").dataset.itemId);
    return item?.update({ "system.equipped": !item.system.equipped });
  }

  /** Klik w kratkę rany: ustaw licznik na tę kratkę (albo zdejmij, gdy klikniesz ostatnią pełną) */
  static #onWoundBox(event, target) {
    const tier = target.dataset.tier;
    const idx = Number(target.dataset.index);
    const current = this.document.system.wounds[tier];
    const value = current === idx + 1 ? idx : idx + 1;
    return this.document.update({ [`system.wounds.${tier}`]: value });
  }

  /** Ogólny licznik: data-path, data-delta */
  static #onTrack(event, target) {
    const path = target.dataset.path;
    const delta = Number(target.dataset.delta);
    const current = foundry.utils.getProperty(this.document, path) ?? 0;
    let value = current + delta;
    const min = target.dataset.min !== undefined ? Number(target.dataset.min) : 0;
    const max = target.dataset.max !== undefined ? Number(target.dataset.max) : Infinity;
    value = Math.max(min, Math.min(max, value));
    return this.document.update({ [path]: value });
  }

  static #onArrayAdd(event, target) {
    const path = target.dataset.path;
    const arr = foundry.utils.deepClone(foundry.utils.getProperty(this.document.system, path) ?? []);
    const templates = {
      clocks: { name: loc("D2.Clock.new"), size: 6, value: 0 },
      tropy: { text: "", source: "", kind: "kluczowy" },
      cechy: { name: loc("D2.Cecha.new"), hidden: false, free: 0 },
      debts: { debtor: "", debtorText: "", creditor: "", creditorText: "", waga: 1, powod: "", status: "otwarty", hidden: false }
    };
    arr.push(foundry.utils.deepClone(templates[path] ?? {}));
    return this.document.update({ [`system.${path}`]: arr });
  }

  static #onArrayDelete(event, target) {
    const path = target.dataset.path;
    const index = Number(target.dataset.index);
    const arr = foundry.utils.deepClone(foundry.utils.getProperty(this.document.system, path) ?? []);
    arr.splice(index, 1);
    return this.document.update({ [`system.${path}`]: arr });
  }

  static #onClockSeg(event, target) {
    const index = Number(target.dataset.index);
    const seg = Number(target.dataset.seg);
    const arr = foundry.utils.deepClone(this.document.system.clocks);
    const c = arr[index];
    c.value = c.value === seg ? seg - 1 : seg;
    return this.document.update({ "system.clocks": arr });
  }

  static async #onBgSpend(event, target) {
    const key = target.dataset.key;
    const delta = Number(target.dataset.delta);
    const bg = this.document.system.backgrounds[key];
    const spent = Math.max(0, Math.min(bg.value, bg.spent + delta));
    await this.document.update({ [`system.backgrounds.${key}.spent`]: spent });
    if (delta > 0 && spent !== bg.spent) {
      ChatMessage.create({
        speaker: ChatMessage.getSpeaker({ actor: this.document }),
        content: `<div class="d2 chat-note"><i class="fa-solid fa-handshake"></i> ${loc("D2.Background.usedChat", { name: this.document.name, bg: loc(`D2.Background.${key}`), value: bg.value })}</div>`
      });
    }
  }

  static #onResetArchetype() {
    return this.document.update({ "system.archetypeUsed": false });
  }

  static async #onCechaInvoke(event, target) {
    const index = Number(target.dataset.index);
    const arr = foundry.utils.deepClone(this.document.system.cechy);
    const c = arr[index];
    const free = c.free > 0;
    if (free) c.free -= 1;
    // Gracz bez uprawnień właściciela tylko ogłasza wywołanie; licznik poprawia MG.
    if (free && this.document.isOwner) await this.document.update({ "system.cechy": arr });
    ChatMessage.create({
      speaker: ChatMessage.getSpeaker(),
      content: `<div class="d2 chat-note"><i class="fa-solid fa-location-dot"></i> ${loc(free ? "D2.Cecha.invokedFree" : "D2.Cecha.invokedEgo", { name: c.name, place: this.document.name })}</div>`
    });
  }

  static async #onCechaToggle(event, target) {
    const index = Number(target.dataset.index);
    const arr = foundry.utils.deepClone(this.document.system.cechy);
    arr[index].hidden = !arr[index].hidden;
    if (!arr[index].hidden) {
      ChatMessage.create({
        speaker: ChatMessage.getSpeaker(),
        content: `<div class="d2 chat-note"><i class="fa-solid fa-eye"></i> ${loc("D2.Cecha.revealed", { name: arr[index].name, place: this.document.name })}</div>`
      });
    }
    return this.document.update({ "system.cechy": arr });
  }

  static #onOracle() {
    return game.degenesis2.oracleDialog();
  }

  static #onDebtStatus(event, target) {
    return setDebtStatus(this.document, Number(target.dataset.index), target.dataset.status);
  }

  static #onDebtCall(event, target) {
    return callDebt(this.document, Number(target.dataset.index));
  }

  static async #onEchoShift(event, target) {
    const delta = Number(target.dataset.delta);
    const reason = await foundry.applications.api.DialogV2.prompt({
      window: { title: loc("D2.Imie.echoTitle") },
      content: `<label>${loc("D2.Imie.reason")} <input type="text" name="reason" autofocus></label>`,
      ok: { callback: (ev, btn) => btn.form.elements.reason.value ?? "" },
      rejectClose: false
    });
    if (reason === null || reason === undefined) return;
    return shiftEcho(this.document, delta, reason);
  }

  static #onApplyFactionAttitude() {
    const f = actorFromRef(this.document.system.frakcja);
    if (f?.type !== "frakcja") return;
    return this.document.update({ "system.postawa": imieToAttitude(f.system.imie.value) });
  }

  static #onOpenActor(event, target) {
    return actorFromRef(target.dataset.uuid)?.sheet.render(true);
  }

  static #onOpenCreator() {
    return game.degenesis2.openCreator(this.document);
  }

  static #onXpBuy(event, target) {
    const { kind, key } = target.dataset;
    return buy(this.document, kind, key);
  }

  static #onXpAward(event, target) {
    return awardXp(this.document, Number(target.dataset.amount), target.dataset.reason);
  }

  static #onXpNewPotential() {
    return buyNewPotential(this.document);
  }

  static #onXpUndo() {
    return undoLast(this.document);
  }

  static #onRevive() {
    return this.document.update({ "system.eliminated": false });
  }
}

/* -------------------------------------------- */

function statsContext(actor) {
  const sys = actor.system;
  const attributes = Object.entries(ATTRIBUTES).map(([key, def]) => ({
    key, abbr: def.abbr, label: loc(`D2.Attr.${key}`), value: sys.attributes[key].value,
    skills: def.skills.map(s => ({
      key: s, label: loc(`D2.Skill.${s}`), value: sys.skills[s].value,
      total: sys.attributes[key].value + sys.skills[s].value,
      locked: actor.type === "postac" && (
        (s === "skupienie" && sys.path !== "skupienie") || (s === "pierwotnosc" && sys.path !== "pierwotnosc") ||
        (s === "wiara" && sys.belief !== "wiara") || (s === "wola" && sys.belief !== "wola"))
    }))
  }));
  const slots = sys.woundSlots;
  const wounds = TIERS.filter(t => slots[t.slots] > 0).map(t => ({
    key: t.key, label: loc(`D2.Wounds.${t.key}`), boxes: boxes(sys.wounds[t.key], slots[t.slots])
  }));
  const weapons = actor.items.filter(i => i.type === "bron").map(i => ({
    id: i.id, name: i.name, img: i.img, system: i.system, skillLabel: loc(`D2.Skill.${i.system.skill}`)
  }));
  const armors = actor.items.filter(i => i.type === "pancerz");
  return { attributes, wounds, weapons, armors, armorValue: actor.armorValue };
}

export class D2PostacSheet extends D2ActorSheet {
  static DEFAULT_OPTIONS = { classes: ["d2", "sheet", "actor", "postac"] };
  static PARTS = { sheet: { template: `systems/${SYSTEM_ID}/templates/actor/postac.hbs`, scrollable: [".tab-panel"] } };

  async _prepareContext(options) {
    const context = await super._prepareContext(options);
    const actor = this.document;
    const sys = actor.system;
    Object.assign(context, statsContext(actor));
    context.backgrounds = BACKGROUNDS.map(k => ({
      key: k, label: loc(`D2.Background.${k}`), value: sys.backgrounds[k].value, spent: sys.backgrounds[k].spent,
      boxes: Array.from({ length: 6 }, (_, i) => ({ filled: i < sys.backgrounds[k].value, spent: i >= sys.backgrounds[k].value - sys.backgrounds[k].spent && i < sys.backgrounds[k].value }))
    }));
    context.egoBoxes = boxes(sys.ego.value, sys.ego.max);
    const zmax = sys.zarazenie.max;
    context.sporeBoxes = Array.from({ length: zmax }, (_, i) => ({
      index: i,
      permanent: i < sys.zarazenie.permanent,
      filled: i >= sys.zarazenie.permanent && i < sys.zarazenie.permanent + sys.zarazenie.value,
      half: i === Math.ceil(zmax / 2) - 1
    }));
    context.sporeOver = Math.max(0, sys.zarazenie.permanent + sys.zarazenie.value - zmax);
    context.items = {
      potencjaly: actor.items.filter(i => i.type === "potencjal"),
      ekwipunek: actor.items.filter(i => i.type === "ekwipunek"),
      tozsamosc: actor.items.filter(i => ["kultura", "koncept", "kult"].includes(i.type))
    };
    const koncept = actor.items.find(i => i.type === "koncept");
    context.cienHint = koncept?.system.cien ?? "";
    const kult = actor.items.find(i => i.type === "kult");
    context.metoda = kult?.system.metoda ?? "";
    context.ideal = kult?.system.ideal ?? "";
    const debts = debtsFor(actor, { includeHidden: game.user.isGM });
    context.debtsOwed = debts.filter(d => d.role === "debtor" && d.status === "otwarty").map(d => ({ ...d, wagaLabel: loc(`D2.Dlug.waga.${d.waga}`) }));
    context.debtsHeld = debts.filter(d => d.role === "creditor" && d.status === "otwarty").map(d => ({ ...d, wagaLabel: loc(`D2.Dlug.waga.${d.waga}`) }));
    context.debtsClosed = debts.filter(d => d.status !== "otwarty").map(d => ({ ...d, statusLabel: loc(`D2.Dlug.status.${d.status}`) }));
    context.reputation = (game.actors?.filter(a => a.type === "frakcja" && a.visible) ?? []).map(f => ({
      uuid: f.uuid, name: f.name, value: f.system.imie.value, echo: f.system.imie.echo,
      tier: loc(`D2.Imie.tier.${String(f.system.imie.value)}`), cls: f.system.imie.value > 0 ? "pos" : f.system.imie.value < 0 ? "neg" : "",
      osobiste: f.system.osobiste
    })).sort((a, b) => b.value - a.value);
    context.pathOptions = { skupienie: loc("D2.Skill.skupienie"), pierwotnosc: loc("D2.Skill.pierwotnosc") };
    context.beliefOptions = { wiara: loc("D2.Skill.wiara"), wola: loc("D2.Skill.wola") };
    context.rozwoj = await progressionContext(actor);
    return context;
  }
}

export class D2NpcSheet extends D2ActorSheet {
  static DEFAULT_OPTIONS = { classes: ["d2", "sheet", "actor", "npc"], position: { width: 720, height: 760 } };
  static PARTS = { sheet: { template: `systems/${SYSTEM_ID}/templates/actor/npc.hbs`, scrollable: [".tab-panel"] } };

  async _prepareContext(options) {
    const context = await super._prepareContext(options);
    const actor = this.document;
    const sys = actor.system;
    Object.assign(context, statsContext(actor));
    context.scaleOptions = Object.fromEntries(NPC_SCALES.map(s => [s, loc(`D2.Npc.scale.${s}`)]));
    context.attitudeOptions = { "-2": loc("D2.Attitude.wrogi"), "-1": loc("D2.Attitude.nieufny"), "0": loc("D2.Attitude.obojetny"), "1": loc("D2.Attitude.zyczliwy"), "2": loc("D2.Attitude.oddany") };
    context.factionOptions = { "": "—" };
    for (const f of game.actors?.filter(a => a.type === "frakcja") ?? []) context.factionOptions[f.uuid] = f.name;
    const faction = actorFromRef(sys.frakcja);
    if (faction?.type === "frakcja") {
      const att = imieToAttitude(faction.system.imie.value);
      context.factionImie = { name: faction.name, tier: loc(`D2.Imie.tier.${String(faction.system.imie.value)}`), attitude: att,
        attitudeLabel: context.attitudeOptions[String(att)], differs: att !== sys.postawa };
    }
    context.isGang = sys.scale === "banda";
    context.isMook = sys.scale === "statysta";
    context.potencjaly = actor.items.filter(i => i.type === "potencjal");
    context.ekwipunek = actor.items.filter(i => i.type === "ekwipunek");
    return context;
  }
}

export class D2FrakcjaSheet extends D2ActorSheet {
  static DEFAULT_OPTIONS = { classes: ["d2", "sheet", "actor", "frakcja"], position: { width: 620, height: 640 } };
  static PARTS = { sheet: { template: `systems/${SYSTEM_ID}/templates/actor/frakcja.hbs`, scrollable: [".d2-body"] } };

  async _prepareContext(options) {
    const context = await super._prepareContext(options);
    context.clocks = clockView(this.document.system.clocks);
    const im = this.document.system.imie;
    context.imieOptions = Object.fromEntries(Object.keys(IMIE_TIERS).map(k => [k, `${Number(k) > 0 ? "+" : ""}${k} ${loc(`D2.Imie.tier.${k}`)}`]));
    context.imieEffect = loc(`D2.Imie.effect.${String(im.value)}`);
    context.imieAttitude = loc(`D2.Attitude.${["wrogi", "wrogi", "nieufny", "obojetny", "zyczliwy", "zyczliwy", "oddany"][im.value + 3]}`);
    context.echoBoxes = [-4, -3, -2, -1, 0, 1, 2, 3, 4].map(v => ({ v, filled: v !== 0 && ((im.echo > 0 && v > 0 && v <= im.echo) || (im.echo < 0 && v < 0 && v >= im.echo)), zero: v === 0, neg: v < 0 }));
    context.isGM = game.user.isGM;
    return context;
  }
}

export class D2SledztwoSheet extends D2ActorSheet {
  static DEFAULT_OPTIONS = { classes: ["d2", "sheet", "actor", "sledztwo"], position: { width: 720, height: 780 } };
  static PARTS = { sheet: { template: `systems/${SYSTEM_ID}/templates/actor/sledztwo.hbs`, scrollable: [".d2-body"] } };

  async _prepareContext(options) {
    const context = await super._prepareContext(options);
    context.clocks = clockView(this.document.system.clocks);
    context.tropy = this.document.system.tropy.map((t, i) => ({ ...t, index: i }));
    context.kindOptions = ["kluczowy", "szczegol", "powiazanie", "dzwignia", "ostrzezenie", "czas"].map(k => ({ value: k, label: loc(`D2.Trop.${k}`) }));
    return context;
  }
}

export class D2LokacjaSheet extends D2ActorSheet {
  static DEFAULT_OPTIONS = { classes: ["d2", "sheet", "actor", "lokacja"], position: { width: 620, height: 620 } };
  static PARTS = { sheet: { template: `systems/${SYSTEM_ID}/templates/actor/lokacja.hbs`, scrollable: [".d2-body"] } };

  async _prepareContext(options) {
    const context = await super._prepareContext(options);
    const gm = game.user.isGM;
    context.cechy = this.document.system.cechy.map((c, i) => ({ ...c, index: i })).filter(c => gm || !c.hidden);
    context.hiddenCount = this.document.system.cechy.filter(c => c.hidden).length;
    return context;
  }
}


export class D2RejestrSheet extends D2ActorSheet {
  static DEFAULT_OPTIONS = { classes: ["d2", "sheet", "actor", "rejestr"], position: { width: 860, height: 700 } };
  static PARTS = { sheet: { template: `systems/${SYSTEM_ID}/templates/actor/rejestr.hbs`, scrollable: [".d2-body"] } };

  _filter = "otwarty";

  async _prepareContext(options) {
    const context = await super._prepareContext(options);
    const gm = game.user.isGM;
    context.partyOptions = partyOptions();
    context.wagaOptions = [1, 2, 3].map(v => ({ value: v, label: loc(`D2.Dlug.waga.${v}`) }));
    const all = this.document.system.debts.map((d, i) => ({
      ...d, index: i,
      debtorName: partyName(d.debtor, d.debtorText), creditorName: partyName(d.creditor, d.creditorText),
      statusLabel: loc(`D2.Dlug.status.${d.status}`), open: d.status === "otwarty"
    })).filter(d => gm || !d.hidden);
    context.open = all.filter(d => d.open);
    context.closed = all.filter(d => !d.open);
    context.totals = [1, 2, 3].map(w => ({ label: loc(`D2.Dlug.waga.${w}`), n: context.open.filter(d => d.waga === w).length }));
    return context;
  }
}

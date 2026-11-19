import { ATTRIBUTES, ALL_SKILLS, SYSTEM_ID } from "../config.mjs";

const { HandlebarsApplicationMixin } = foundry.applications.api;
const { ItemSheetV2 } = foundry.applications.sheets;
const loc = (k, d) => game.i18n.format(k, d ?? {});

export class D2ItemSheet extends HandlebarsApplicationMixin(ItemSheetV2) {
  static DEFAULT_OPTIONS = {
    classes: ["d2", "sheet", "item"],
    position: { width: 540, height: 560 },
    window: { resizable: true },
    form: { submitOnChange: true, closeOnSubmit: false },
    actions: {
      toggleBonus: D2ItemSheet.#onToggleBonus
    }
  };

  static PARTS = { sheet: { template: `systems/${SYSTEM_ID}/templates/item/item.hbs`, scrollable: [".d2-body"] } };

  async _prepareContext(options) {
    const context = await super._prepareContext(options);
    const item = this.document;
    const sys = item.system;
    context.item = item;
    context.system = sys;
    context.editable = this.isEditable;
    context.isType = Object.fromEntries(["bron", "pancerz", "ekwipunek", "potencjal", "kultura", "koncept", "kult"].map(t => [t, item.type === t]));
    context.weaponSkillOptions = { bronBiala: loc("D2.Skill.bronBiala"), bijatyka: loc("D2.Skill.bijatyka"), strzelectwo: loc("D2.Skill.strzelectwo") };
    const hasBonuses = ["kultura", "koncept", "kult"].includes(item.type);
    if (hasBonuses) {
      const attrSet = new Set(sys.attributeBonuses ?? []);
      const skillSet = new Set(sys.skillBonuses ?? []);
      context.bonusGrid = Object.entries(ATTRIBUTES).map(([a, def]) => ({
        key: a, label: loc(`D2.Attr.${a}`), active: attrSet.has(a), showAttr: item.type !== "kult",
        skills: def.skills.map(s => ({ key: s, label: loc(`D2.Skill.${s}`), active: skillSet.has(s) }))
      }));
    }
    context.hasBonuses = hasBonuses;
    return context;
  }

  static #onToggleBonus(event, target) {
    if (!this.isEditable) return;
    const kind = target.dataset.kind; // attributeBonuses | skillBonuses
    const key = target.dataset.key;
    const list = new Set(this.document.system[kind] ?? []);
    list.has(key) ? list.delete(key) : list.add(key);
    const valid = kind === "skillBonuses" ? ALL_SKILLS : Object.keys(ATTRIBUTES);
    return this.document.update({ [`system.${kind}`]: [...list].filter(k => valid.includes(k)) });
  }
}

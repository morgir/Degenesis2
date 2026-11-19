import { SYSTEM_ID } from "./config.mjs";
import { woundTier, applyWound, gangCasualties } from "./rules.mjs";
import { rollDialog, phenomenonDialog } from "./dice.mjs";

const renderTemplate = foundry.applications.handlebars.renderTemplate;
const loc = (k, d) => game.i18n.format(k, d ?? {});

export class D2Actor extends Actor {
  /** Dane do formuł (np. inicjatywa) */
  getRollData() {
    const data = super.getRollData();
    const s = this.system;
    if (s?.attributes) {
      data.initPool = Math.max(0, (s.attributes.psy.value + s.skills.refleks.value) - (s.woundPenalty ?? 0));
    }
    return data;
  }

  /** Pancerz: główny + 1 za okrycie, jeśli główny ma 1–3 (zasada warstw z Rebirth). */
  get armorValue() {
    const worn = this.items.filter(i => i.type === "pancerz" && i.system.equipped).map(i => i.system.armor).sort((a, b) => b - a);
    let armor = worn[0] ?? 0;
    if (worn.length > 1 && armor >= 1 && armor <= 3) armor += 1;
    if (this.type === "npc") armor = Math.max(armor, this.system.armor ?? 0);
    return armor;
  }

  rollSkill(skill, opts = {}) {
    return rollDialog(this, { skill, ...opts });
  }

  rollAttribute(attr, opts = {}) {
    return rollDialog(this, { attr, skill: null, ...opts });
  }

  /**
   * Nakłada obrażenia (przed pancerzem) i zapisuje ranę.
   * @param {number} damage  obrażenia broni + Wyzwalacze
   * @param {object} [opts]
   * @param {boolean} [opts.ignoreArmor]
   */
  async applyDamage(damage, { ignoreArmor = false } = {}) {
    const sys = this.system;
    const armor = ignoreArmor ? 0 : this.armorValue;
    const net = damage - armor;
    const tier = woundTier(net, sys.threshold);
    const result = { actor: this.name, damage, armor, net, threshold: sys.threshold, tier, eliminated: false, casualties: 0 };

    if (tier) {
      if (this.type === "npc" && sys.scale === "banda") {
        const cas = gangCasualties(tier);
        const left = Math.max(0, sys.size.value - cas);
        result.casualties = cas;
        result.eliminated = left === 0;
        await this.update({ "system.size.value": left, "system.eliminated": result.eliminated });
      } else if (this.type === "npc" && sys.scale === "statysta") {
        result.eliminated = true;
        await this.update({ "system.eliminated": true });
      } else {
        const r = applyWound(sys.wounds, tier, sys.woundSlots);
        result.appliedTier = r.appliedTier;
        result.eliminated = r.eliminated;
        await this.update({ "system.wounds": r.wounds, "system.eliminated": r.eliminated || sys.eliminated });
      }
    }

    const content = await renderTemplate(`systems/${SYSTEM_ID}/templates/chat/damage.hbs`, {
      ...result,
      tierLabel: tier ? loc(`D2.Wounds.${result.appliedTier ?? tier}`) : loc("D2.Wounds.none"),
      upgraded: result.appliedTier && result.appliedTier !== tier,
      isPC: this.type === "postac"
    });
    await ChatMessage.create({ content, speaker: ChatMessage.getSpeaker({ actor: this }), flags: { [SYSTEM_ID]: { type: "damage" } } });
    return result;
  }
}

export class D2Item extends Item {
  /** Rzut bronią */
  async roll() {
    if (!this.actor) return;
    if (this.type === "bron") return rollDialog(this.actor, { item: this, skill: this.system.skill });
    if (this.type === "potencjal" && this.system.zjawisko) return phenomenonDialog(this.actor, this);
    return this.toChat();
  }

  async toChat() {
    const content = `<div class="d2 chat-item"><h3>${this.name}</h3>${this.system.description ?? ""}</div>`;
    return ChatMessage.create({ content, speaker: ChatMessage.getSpeaker({ actor: this.actor }) });
  }
}

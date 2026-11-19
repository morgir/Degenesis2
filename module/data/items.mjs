import { ALL_SKILLS, ATTRIBUTES } from "../config.mjs";

const fields = foundry.data.fields;
const int = (initial = 0, min = undefined, max = undefined) =>
  new fields.NumberField({ required: true, nullable: false, integer: true, initial, min, max });
const str = (initial = "") => new fields.StringField({ required: false, blank: true, initial });
const html = () => new fields.HTMLField({ required: false, blank: true, initial: "" });

class BaseItemModel extends foundry.abstract.TypeDataModel {
  static defineSchema() {
    return { description: html() };
  }
}

export class BronModel extends BaseItemModel {
  static defineSchema() {
    return {
      ...super.defineSchema(),
      skill: new fields.StringField({ required: true, initial: "bronBiala", choices: ["bronBiala", "bijatyka", "strzelectwo"] }),
      handling: int(0, -5, 5),
      damage: str("2+F/2"),
      range: str("1"),
      magazine: new fields.SchemaField({ value: int(0, 0), max: int(0, 0) }),
      qualities: str(),
      encumbrance: int(1, 0),
      equipped: new fields.BooleanField({ initial: true })
    };
  }
}

export class PancerzModel extends BaseItemModel {
  static defineSchema() {
    return {
      ...super.defineSchema(),
      armor: int(1, 0, 10),
      qualities: str(),
      encumbrance: int(1, 0),
      equipped: new fields.BooleanField({ initial: true })
    };
  }
}

export class EkwipunekModel extends BaseItemModel {
  static defineSchema() {
    return {
      ...super.defineSchema(),
      quantity: int(1, 0),
      encumbrance: int(0, 0),
      value: str()
    };
  }
}

export class PotencjalModel extends BaseItemModel {
  static defineSchema() {
    return {
      ...super.defineSchema(),
      level: int(1, 1, 3),
      kult: str(),
      prerequisite: str(),
      zjawisko: new fields.BooleanField({ initial: false }),
      poziomZjawiska: int(0, 0, 20)
    };
  }
}

const attrChoices = Object.keys(ATTRIBUTES);

export class KulturaModel extends BaseItemModel {
  static defineSchema() {
    return {
      ...super.defineSchema(),
      attributeBonuses: new fields.ArrayField(new fields.StringField({ choices: attrChoices })),
      skillBonuses: new fields.ArrayField(new fields.StringField({ choices: ALL_SKILLS })),
      kulty: str()
    };
  }
}

export class KonceptModel extends BaseItemModel {
  static defineSchema() {
    return {
      ...super.defineSchema(),
      tarot: str(),
      attributeBonuses: new fields.ArrayField(new fields.StringField({ choices: attrChoices })),
      skillBonuses: new fields.ArrayField(new fields.StringField({ choices: ALL_SKILLS })),
      cien: str()
    };
  }
}

export class KultModel extends BaseItemModel {
  static defineSchema() {
    return {
      ...super.defineSchema(),
      skillBonuses: new fields.ArrayField(new fields.StringField({ choices: ALL_SKILLS })),
      metoda: str(),
      ideal: str(),
      moneyFactor: int(50, 0),
      currency: str("CD"),
      ranks: new fields.ArrayField(new fields.SchemaField({
        level: int(1, 0, 7),
        name: str(),
        prereq: str("[]"),   // JSON: lista wymagań (patrz rules.checkPrereqs)
        prereqText: str(),
        result: str(),
        equipment: str()
      }))
    };
  }
}

import { ATTRIBUTES, ALL_SKILLS, BACKGROUNDS, WOUND_SLOTS } from "../config.mjs";
import { woundPenalty, imieToAttitude } from "../rules.mjs";

const fields = foundry.data.fields;

const int = (initial = 0, min = 0, max = undefined) =>
  new fields.NumberField({ required: true, nullable: false, integer: true, initial, min, max });

const html = () => new fields.HTMLField({ required: false, blank: true, initial: "" });
const str = (initial = "") => new fields.StringField({ required: false, blank: true, initial });

function attributesSchema() {
  return new fields.SchemaField(
    Object.fromEntries(Object.keys(ATTRIBUTES).map(k => [k, new fields.SchemaField({ value: int(1, 0, 6) })]))
  );
}

function skillsSchema() {
  return new fields.SchemaField(
    Object.fromEntries(ALL_SKILLS.map(k => [k, new fields.SchemaField({ value: int(0, 0, 6) })]))
  );
}

function woundsSchema() {
  return new fields.SchemaField({
    lekkie: int(0, 0, 3),
    powazne: int(0, 0, 2),
    krytyczna: int(0, 0, 1)
  });
}

function clocksSchema() {
  return new fields.ArrayField(new fields.SchemaField({
    name: str(""),
    size: int(6, 2, 12),
    value: int(0, 0, 12)
  }));
}

/** Część wspólna: statystyki postaci i NPC */
class BaseStatsModel extends foundry.abstract.TypeDataModel {
  static defineSchema() {
    return {
      attributes: attributesSchema(),
      skills: skillsSchema(),
      wounds: woundsSchema(),
      ego: new fields.SchemaField({ value: int(0, 0) }),
      defense: new fields.SchemaField({ bonus: int(0, -5, 10) }),
      notes: html()
    };
  }

  /** Wartość umiejętności + atrybutu */
  actionNumber(attr, skill) {
    const a = this.attributes[attr]?.value ?? 0;
    const s = skill ? (this.skills[skill]?.value ?? 0) : 0;
    return a + s;
  }

  get force() {
    return this.actionNumber("cia", "sila");
  }

  prepareDerivedData() {
    const a = this.attributes;
    const s = this.skills;
    this.threshold = Math.max(1, a.cia.value + s.twardosc.value);
    this.threshold2 = this.threshold * 2;
    this.woundPenalty = woundPenalty(this.wounds);
    this.defense.value = 1 + this.defense.bonus;
  }
}

export class PostacModel extends BaseStatsModel {
  static defineSchema() {
    return {
      ...super.defineSchema(),
      path: new fields.StringField({ required: true, initial: "skupienie", choices: ["skupienie", "pierwotnosc"] }),
      belief: new fields.StringField({ required: true, initial: "wola", choices: ["wiara", "wola"] }),
      backgrounds: new fields.SchemaField(
        Object.fromEntries(BACKGROUNDS.map(k => [k, new fields.SchemaField({ value: int(0, 0, 6), spent: int(0, 0, 6) })]))
      ),
      zarazenie: new fields.SchemaField({ value: int(0, 0), permanent: int(0, 0) }),
      archetypeUsed: new fields.BooleanField({ initial: false }),
      identity: new fields.SchemaField({
        kultura: str(), koncept: str(), kult: str(), ranga: str(),
        wiek: str(), plec: str()
      }),
      ambicja: str(),
      tajemnica: str(),
      cien: str(),
      wiezi: html(),
      blizny: html(),
      xp: new fields.SchemaField({ total: int(0, 0), spent: int(0, 0),
        log: new fields.ArrayField(new fields.SchemaField({ t: str(), delta: int(0), date: str() })) }),
      money: str(""),
      eliminated: new fields.BooleanField({ initial: false }),
      // Psychonauci: zarażenie sporami = pula Zjawisk w fazie Prymarnej (Katharsys s. 285)
      prymer: new fields.SchemaField({ value: int(0, 0), max: int(0, 0) }),
      zjawiskaBonus: int(0, 0, 12)
    };
  }

  prepareDerivedData() {
    super.prepareDerivedData();
    const a = this.attributes;
    const s = this.skills;
    const pathAttr = this.path === "pierwotnosc" ? "ins" : "int";
    this.ego.max = (a[pathAttr].value + s[this.path].value) * 2;
    this.zarazenie.max = (a.psy.value + s[this.belief].value) * 2;
    this.zarazenie.stigma = this.zarazenie.value + this.zarazenie.permanent >= Math.ceil(this.zarazenie.max / 2) && this.zarazenie.max > 0;
    this.zarazenie.leperos = this.zarazenie.max > 0 && this.zarazenie.permanent >= Math.ceil(this.zarazenie.max / 2);
    this.woundSlots = WOUND_SLOTS.antagonista;
    for (const b of Object.values(this.backgrounds)) b.available = Math.max(0, b.value - b.spent);
    this.xp.available = this.xp.total - this.xp.spent;
  }
}

export class NpcModel extends BaseStatsModel {
  static defineSchema() {
    return {
      ...super.defineSchema(),
      scale: new fields.StringField({ required: true, initial: "weteran", choices: ["statysta", "weteran", "antagonista", "banda"] }),
      size: new fields.SchemaField({ value: int(5, 0), max: int(5, 0) }),
      ego: new fields.SchemaField({ value: int(4, 0), max: int(4, 0) }),
      armor: int(0, 0, 10),
      progBonus: int(0, 0, 20),
      kult: str(),
      ranga: str(),
      motyw: str(),
      lek: str(),
      sekret: str(),
      cena: str(),
      postawa: int(0, -2, 2),
      frakcja: str(),
      eliminated: new fields.BooleanField({ initial: false })
    };
  }

  prepareDerivedData() {
    super.prepareDerivedData();
    this.threshold += this.progBonus;
    this.threshold2 = this.threshold * 2;
    this.woundSlots = WOUND_SLOTS[this.scale] ?? WOUND_SLOTS.weteran;
    this.attitudeDifficulty = { "-2": 4, "-1": 3, "0": 2, "1": 1, "2": 0 }[String(this.postawa)];
  }
}

export class FrakcjaModel extends foundry.abstract.TypeDataModel {
  static defineSchema() {
    return {
      cel: str(),
      zasoby: int(2, 1, 5),
      imie: new fields.SchemaField({ value: int(0, -3, 3), echo: int(0, -4, 4) }),
      osobiste: str(),
      cecha: str(),
      clocks: clocksSchema(),
      notes: html()
    };
  }

  /** v0.1 miało pole „stosunek” — przenosimy do Imienia. */
  static migrateData(source) {
    if (source.stosunek !== undefined && source.imie === undefined) {
      source.imie = { value: source.stosunek, echo: 0 };
    }
    delete source.stosunek;
    return super.migrateData(source);
  }

  prepareDerivedData() {
    this.attitude = imieToAttitude(this.imie.value);
  }
}

export class RejestrModel extends foundry.abstract.TypeDataModel {
  static defineSchema() {
    return {
      debts: new fields.ArrayField(new fields.SchemaField({
        debtor: str(),        // UUID aktora albo pusty
        debtorText: str(),    // wpis ręczny
        creditor: str(),
        creditorText: str(),
        waga: int(1, 1, 3),
        powod: str(),
        status: new fields.StringField({ required: true, initial: "otwarty", choices: ["otwarty", "splacony", "sciagniety", "zerwany"] }),
        hidden: new fields.BooleanField({ initial: false })
      })),
      notes: html()
    };
  }
}

export class SledztwoModel extends foundry.abstract.TypeDataModel {
  static defineSchema() {
    return {
      pytanie: str(),
      tropy: new fields.ArrayField(new fields.SchemaField({
        text: str(),
        source: str(),
        kind: new fields.StringField({ required: true, initial: "kluczowy", choices: ["kluczowy", "szczegol", "powiazanie", "dzwignia", "ostrzezenie", "czas"] })
      })),
      teorie: html(),
      clocks: clocksSchema(),
      notes: html()
    };
  }
}

export class LokacjaModel extends foundry.abstract.TypeDataModel {
  static defineSchema() {
    return {
      region: str(),
      cechy: new fields.ArrayField(new fields.SchemaField({
        name: str(),
        hidden: new fields.BooleanField({ initial: false }),
        free: int(0, 0, 5)
      })),
      description: html()
    };
  }
}

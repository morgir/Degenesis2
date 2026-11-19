/**
 * Stałe systemu Degenesis: Katharsys 2.0.
 * Klucze są stabilne (używane w danych), etykiety idą przez lang/pl.json.
 */
export const SYSTEM_ID = "degenesis2";

export const ATTRIBUTES = {
  cia: { abbr: "CIA", skills: ["atletyka", "bijatyka", "sila", "bronBiala", "kondycja", "twardosc"] },
  zre: { abbr: "ZRĘ", skills: ["rzemioslo", "zwinnePalce", "prowadzenie", "mobilnosc", "strzelectwo", "skradanie"] },
  cha: { abbr: "CHA", skills: ["sztuka", "obycie", "ekspresja", "przywodztwo", "negocjacje", "uwodzenie"] },
  int: { abbr: "INT", skills: ["artefakty", "inzynieria", "skupienie", "legendy", "medycyna", "nauka"] },
  psy: { abbr: "PSY", skills: ["spryt", "oszustwo", "dominacja", "wiara", "refleks", "wola"] },
  ins: { abbr: "INS", skills: ["empatia", "orientacja", "percepcja", "pierwotnosc", "przetrwanie", "oswajanie"] }
};

/** skill -> attribute */
export const SKILL_ATTRIBUTE = Object.fromEntries(
  Object.entries(ATTRIBUTES).flatMap(([attr, def]) => def.skills.map(s => [s, attr]))
);

export const ALL_SKILLS = Object.keys(SKILL_ATTRIBUTE);

export const BACKGROUNDS = ["sojusznicy", "autorytet", "slawa", "zasoby", "sekrety", "siec"];

/** Ścieżki wykluczające się parami */
export const PATHS = { skupienie: "int", pierwotnosc: "ins" };
export const BELIEFS = ["wiara", "wola"];

/** Atrybuty preferowane wg ścieżki (tańszy rozwój) */
export const PREFERRED_ATTRIBUTES = {
  skupienie: ["int", "zre", "psy"],
  pierwotnosc: ["cia", "cha", "ins"]
};

export const WOUND_SLOTS = {
  antagonista: { lekkie: 3, powazne: 2, krytyczna: 1 },
  weteran: { lekkie: 1, powazne: 1, krytyczna: 0 },
  statysta: { lekkie: 0, powazne: 0, krytyczna: 0 },
  banda: { lekkie: 0, powazne: 0, krytyczna: 0 }
};

export const WOUND_PENALTY = { lekkie: 0, powazne: 1, krytyczna: 2 };

export const ATTITUDES = {
  "-2": { label: "D2.Attitude.wrogi", difficulty: 4 },
  "-1": { label: "D2.Attitude.nieufny", difficulty: 3 },
  "0": { label: "D2.Attitude.obojetny", difficulty: 2 },
  "1": { label: "D2.Attitude.zyczliwy", difficulty: 1 },
  "2": { label: "D2.Attitude.oddany", difficulty: 0 }
};

export const DIFFICULTIES = [
  { value: 1, label: "D2.Difficulty.1" },
  { value: 2, label: "D2.Difficulty.2" },
  { value: 3, label: "D2.Difficulty.3" },
  { value: 4, label: "D2.Difficulty.4" },
  { value: 6, label: "D2.Difficulty.6" }
];

export const WEAPON_SKILLS = ["bronBiala", "bijatyka", "strzelectwo"];

export const NPC_SCALES = ["statysta", "weteran", "antagonista", "banda"];

export const MAX_DICE = 12;
export const MAX_EGO_DICE = 3;
export const MAX_BACKGROUND_DICE = 3;

/** Imię (reputacja drużyny u frakcji), skala −3…+3 */
export const IMIE_TIERS = {
  "-3": { key: "krwawyWrog", attitude: -2 },
  "-2": { key: "wrog", attitude: -2 },
  "-1": { key: "podejrzany", attitude: -1 },
  "0": { key: "obcy", attitude: 0 },
  "1": { key: "znany", attitude: 1 },
  "2": { key: "szanowany", attitude: 1 },
  "3": { key: "swoi", attitude: 2 }
};
export const ECHO_LIMIT = 4;

export const DEBT_STATUS = ["otwarty", "splacony", "sciagniety", "zerwany"];
export const DEBT_WEIGHTS = [1, 2, 3];

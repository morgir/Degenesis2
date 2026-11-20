import re
# -*- coding: utf-8 -*-
import json, os, random, string, shutil, sys
sys.path.insert(0, os.path.dirname(__file__))
from zones import zone
from content import KULTURY, KONCEPTY, KULTY, WEAPONS, ARMORS, GEAR
from rules_pages import PAGES, GM_PAGE
from cult_data import RANKS, COMMON, POTENTIALS, RANK_PAGES
from enemies import ENEMIES
from player_pages import PLAYER_PAGES, ADVENTURE_PAGES, PREGENS
from adventure_full import ADVENTURE, GM_SCHOOL, PREGEN_EXTRA, NEW_NPCS
from maps import MAPS

ROOT = "/home/claude/degenesis2/src/packs"
random.seed(2595)  # stabilne ID między buildami

def rid():
    return "".join(random.choice(string.ascii_letters + string.digits) for _ in range(16))

STATS = {"compendiumSource": None, "duplicateSource": None, "coreVersion": "14.370", "systemId": "degenesis2", "systemVersion": "0.1.0"}

def item(name, type_, system, img="icons/svg/item-bag.svg"):
    _id = rid()
    return {"_id": _id, "_key": f"!items!{_id}", "name": name, "type": type_, "img": img, "system": system,
            "effects": [], "folder": None, "sort": 0, "ownership": {"default": 0}, "flags": {}, "_stats": STATS}

def p(text):
    return f"<p>{text}</p>"

packs = {k: [] for k in ["kultury", "koncepty", "kulty", "ekwipunek", "zasady", "makra", "przyklady", "potencjaly", "przeciwnicy", "postacie", "gracze", "przygoda", "sceny", "muzyka"]}

for name, attrs, skills, cults, desc in KULTURY:
    packs["kultury"].append(item(name, "kultura", {"description": p(desc), "attributeBonuses": attrs, "skillBonuses": skills, "kulty": cults}, "icons/svg/village.svg"))

for _i, (tarot, name, attr, skills, cien) in enumerate(KONCEPTY):
    packs["koncepty"].append(item(f"{tarot}. {name}", "koncept", {
        "description": p(f"Arkana {tarot}. Raz na sesję +2K w sytuacji zgodnej z Archetypem. <b>Cień:</b> {cien}"),
        "tarot": tarot, "attributeBonuses": [attr], "skillBonuses": skills, "cien": cien}, "icons/svg/book.svg"))
    packs["koncepty"][-1]["sort"] = (_i + 1) * 100

MONEY = {"Spitalianie": (100, "CD"), "Kronikarze": (128, "CD"), "Hellveci": (50, "CD"), "Sędziowie": (50, "CD"), "Klanowcy": (50, "CD"),
         "Złomiarze": (50, "CD"), "Neolibijczycy": (1000, "Dinarów"), "Skurgerzy": (100, "Dinarów"), "Anubianie": (100, "Dinarów"),
         "Jehammedanie": (100, "CD"), "Apokaliptycy": (200, "CD"), "Anabaptyści": (50, "CD"), "Palerzy": (50, "CD")}
SKL = {"cia": "Ciało", "zre": "Zręczność", "cha": "Charyzma", "int": "Intelekt", "psy": "Psyche", "ins": "Instynkt"}
import json as _json
from make_lang_names import SKILL_PL, BG_PL
def preq_label(e):
    if e[0] == "bg": return f"{BG_PL[e[1]]} {e[2]}"
    if e[0] == "txt": return e[1]
    return f"{SKL[e[0]]} + {SKILL_PL[e[1]]} {e[2]}"
def preq_text(pre):
    out = []
    for x in pre:
        out.append(" lub ".join(preq_label(y) for y in x) if isinstance(x, list) else preq_label(x))
    return "; ".join(out) or "—"
def rank_rows(cult):
    rows = []
    for lvl, nm, pre, res, eq in RANKS.get(cult, []):
        rows.append({"level": lvl, "name": nm, "prereq": _json.dumps([list(x) if not isinstance(x, list) else [list(y) for y in x] for x in pre], ensure_ascii=False),
                     "prereqText": preq_text(pre), "result": res, "equipment": eq})
    return rows
def rank_table(cult):
    h = "<table><tr><th>Poz.</th><th>Ranga</th><th>Wymagania</th><th>Co daje</th><th>Ekwipunek</th></tr>"
    for r in rank_rows(cult):
        h += f"<tr><td>{r['level'] or 'spec.'}</td><td><b>{r['name']}</b></td><td>{r['prereqText']}</td><td>{r['result']}</td><td>{r['equipment']}</td></tr>"
    return h + "</table>"
def pot_list(cult):
    if not POTENTIALS.get(cult): return "<p>Ten kult nie ma własnych Potencjałów — korzysta z ogólnych (Katharsys).</p>"
    return "<ul>" + "".join(f"<li><b>{n}</b>{' <i>(wym.: ' + pr + ')</i>' if pr else ''}: {d}</li>" for n, pr, d in POTENTIALS.get(cult, [])) + "</ul>"

for name, skills, metoda, ideal, desc in KULTY:
    mf, cur = MONEY[name]
    packs["kulty"].append(item(name, "kult", {"description": p(desc), "skillBonuses": skills, "metoda": metoda, "ideal": ideal,
        "moneyFactor": mf, "currency": cur, "ranks": rank_rows(name)}, "icons/svg/temple.svg"))

for n, pr, d in COMMON:
    packs["potencjaly"].append(item(n, "potencjal", {"description": p(d), "level": 1, "kult": "Ogólne", "prerequisite": pr}, "icons/svg/aura.svg"))
for cult, lst in POTENTIALS.items():
    for n, pr, d in lst:
        if n.startswith("("): continue
        packs["potencjaly"].append(item(n, "potencjal", {"description": p(d), "level": 1, "kult": cult, "prerequisite": pr}, "icons/svg/aura.svg"))

for name, skill, hand, dmg, rng, mag, q, enc in WEAPONS:
    img = "icons/svg/sword.svg" if skill != "strzelectwo" else "icons/svg/target.svg"
    packs["ekwipunek"].append(item(name, "bron", {"description": "", "skill": skill, "handling": hand, "damage": dmg, "range": zone(rng),
        "magazine": {"value": mag, "max": mag}, "qualities": q, "encumbrance": enc, "equipped": True}, img))
for name, armor, q, enc in ARMORS:
    packs["ekwipunek"].append(item(name, "pancerz", {"description": "", "armor": armor, "qualities": q, "encumbrance": enc, "equipped": True}, "icons/svg/shield.svg"))
for name, qty, desc in GEAR:
    packs["ekwipunek"].append(item(name, "ekwipunek", {"description": p(desc) if desc else "", "quantity": qty, "encumbrance": 0, "value": ""}))

# --- Dzienniki ---
def journal(name, pages):
    jid = rid()
    out = {"_id": jid, "_key": f"!journal!{jid}", "name": name, "pages": [], "folder": None, "sort": 0,
           "ownership": {"default": 0}, "flags": {}, "_stats": STATS, "categories": []}
    for i, (title, html) in enumerate(pages):
        pid = rid()
        out["pages"].append({"_id": pid, "_key": f"!journal.pages!{jid}.{pid}", "name": title, "type": "text",
            "title": {"show": True, "level": 1}, "text": {"format": 1, "content": html.strip()},
            "sort": (i + 1) * 100000, "ownership": {"default": -1}, "flags": {}, "_stats": STATS,
            "image": {}, "video": {"controls": True, "volume": 0.5}, "src": None, "system": {}, "category": None})
    return out

world_html = ["<p>Rok 2595, 522 lata po Eshatonie. Streszczenia własnymi słowami; szczegóły w Primal Punk.</p><h2>Kultury</h2>"]
for name, attrs, skills, cults, desc in KULTURY:
    world_html.append(f"<h3>{name}</h3><p>{desc}</p><p><i>Typowe kulty:</i> {cults}</p>")
world_html.append("<h2>Kulty</h2>")
for name, skills, metoda, ideal, desc in KULTY:
    world_html.append(f"<h3>{name}</h3><p>{desc}</p><p><b>Metoda:</b> {metoda}<br><b>Ideał:</b> {ideal}</p>")
world_html.append("""<h2>Prymer i Psychonauci</h2><p>Z asteroid przyszedł Prymer. Sepsa porasta ziemię polami zarodników, Burn kusi rozkoszą i mocą, a w pobliżu pól macierzystych rodzą się dzieci bez duszy: Psychonauci. W każdym regionie objawiają się inaczej: Biokinetycy (Pollen), Feromanci (Franka), Dushani (Balkhan), Pregnoktycy (Hybrispania), Psychokinetycy (Purgare).</p>""")

packs["zasady"].append(journal("Katharsys 2.0 — zasady", PAGES))
packs["zasady"].append(journal("Świat — ściągawka", [("Kultury, kulty, Prymer", "".join(world_html))]))
packs["zasady"].append(journal("Dla MG", [GM_PAGE]))

# --- Makra ---
def macro(name, command, img):
    mid = rid()
    return {"_id": mid, "_key": f"!macros!{mid}", "name": name, "type": "script", "scope": "global", "command": command,
            "img": img, "folder": None, "sort": 0, "ownership": {"default": 0}, "flags": {}, "_stats": STATS, "author": None}

packs["makra"] += [
    macro("Wyrocznia FU", "game.degenesis2.oracleDialog();", "icons/svg/eye.svg"),
    macro("Przyznaj PD drużynie", "game.degenesis2.awardParty();", "icons/svg/upgrade.svg"),
    macro("Nowa postać (kreator)", "game.degenesis2.newCharacter();", "icons/svg/mystery-man.svg"),
    macro("Nowa sesja (odnów Archetypy)", "game.degenesis2.newSession();", "icons/svg/sun.svg"),
    macro("Rzut pulą (wybrany token)", """const actor = canvas.tokens.controlled[0]?.actor ?? game.user.character;
if (!actor) ui.notifications.warn("Zaznacz token albo przypisz postać.");
else game.degenesis2.rollDialog(actor);""", "icons/svg/d20-grey.svg"),
    macro("Utwórz sceny przygody", """const maps = [["Justitian — plan dzielnicy Dostawców","dzielnica",2400,1600,0],["Targ i studnia przy Bramie","targ-studnia",2100,1400,1],["Lazaret Spitalian","lazaret",1960,1260,1],["Pod Złamanym Skrzydłem (spelunka Kruków)","spelunka-krukow",1820,1260,1],["Kancelaria Sędziego Vargi","kancelaria-vargi",1680,1260,1]];
for (const [name, f, w, h, g] of maps) {
  if (game.scenes.getName(name)) continue;
  await Scene.create({ name, width: w, height: h, padding: 0.05, background: { src: `systems/degenesis2/assets/maps/${f}.webp` },
    grid: { type: g, size: 70, distance: 1, units: "m", alpha: 0 } });
}
ui.notifications.info("Sceny przygody gotowe.");""", "icons/svg/castle.svg"),
    macro("Kreator postaci", """let a = game.user.character ?? canvas.tokens.controlled[0]?.actor;
if (!a || a.type !== "postac") a = await Actor.create({ name: "Nowa postać", type: "postac" });
if (a) game.degenesis2.openCreator(a);""", "icons/svg/statue.svg"),
    macro("Nałóż obrażenia na cel", """const v = await foundry.applications.api.DialogV2.prompt({
  window: { title: "Obrażenia" },
  content: '<label>Obrażenia (z Wyzwalaczami, przed pancerzem) <input type="number" name="dmg" value="5" autofocus></label>',
  ok: { callback: (ev, btn) => Number(btn.form.elements.dmg.value) || 0 }, rejectClose: false });
if (v) game.degenesis2.applyDamageToTargets(v);""", "icons/svg/blood.svg"),
]

# --- Przykłady: mini-śledztwo w Justitian ---
ATTRS = ["cia", "zre", "cha", "int", "psy", "ins"]
SK = {"cia": ["atletyka","bijatyka","sila","bronBiala","kondycja","twardosc"], "zre": ["rzemioslo","zwinnePalce","prowadzenie","mobilnosc","strzelectwo","skradanie"],
      "cha": ["sztuka","obycie","ekspresja","przywodztwo","negocjacje","uwodzenie"], "int": ["artefakty","inzynieria","skupienie","legendy","medycyna","nauka"],
      "psy": ["spryt","oszustwo","dominacja","wiara","refleks","wola"], "ins": ["empatia","orientacja","percepcja","pierwotnosc","przetrwanie","oswajanie"]}

def actor(name, type_, system, img="icons/svg/mystery-man.svg", items=None, token=None):
    aid = rid()
    its = []
    for it in items or []:
        it = dict(it); iid = rid(); it["_id"] = iid; it["_key"] = f"!actors.items!{aid}.{iid}"; its.append(it)
    return {"_id": aid, "_key": f"!actors!{aid}", "name": name, "type": type_, "img": img, "system": system,
            "items": its, "effects": [], "folder": None, "sort": 0, "ownership": {"default": 0}, "flags": {}, "_stats": STATS,
            "prototypeToken": {"name": name, "actorLink": type_ in ("postac",), "disposition": -1 if type_ == "npc" else (1 if type_ == "postac" else 0),
                               "texture": {"src": token or img}}}

def stats(attrs, skills):
    return {"attributes": {a: {"value": attrs.get(a, 1)} for a in ATTRS},
            "skills": {s: {"value": skills.get(s, 0)} for a in ATTRS for s in SK[a]}}

def weapon(name):
    w = next(x for x in packs["ekwipunek"] if x["name"] == name)
    return {k: v for k, v in w.items() if k not in ("_id", "_key", "folder")}

packs["przyklady"].append(actor("Śledztwo: Ciche studnie", "sledztwo", {
    "pytanie": "Kto zatruwa studnie w dzielnicy Dostawców w Justitian i dlaczego Sędziowie milczą?",
    "tropy": [
        {"text": "Chorzy piją ze studni przy Bramie Wschodniej; z innych studni nikt nie choruje.", "source": "Spitaliański lazaret", "kind": "kluczowy"},
        {"text": "W cembrowinie studni białe włókna, ale Mollusk reaguje słabo.", "source": "Oględziny studni", "kind": "kluczowy"},
        {"text": "Przekupka Halka widziała nocą wóz z beczkami bez znaków.", "source": "Targ przy Bramie", "kind": "kluczowy"}
    ],
    "teorie": "",
    "clocks": [{"name": "Epidemia wybucha w całej dzielnicy", "size": 8, "value": 2}],
    "notes": "Prawda (dla MG): Apokaliptycy z Kruczego Stada testują rozcieńczony Burn (Unity), żeby uspokoić robotników przed strajkiem, na zlecenie skorumpowanego Sędziego miejskiego. Spitalianie podejrzewają Sepsę i chcą spalić dzielnicę."
}, "icons/svg/book.svg"))

packs["przyklady"].append(actor("Lokacja: Targ przy Bramie Wschodniej", "lokacja", {
    "region": "Justitian, Borca",
    "cechy": [
        {"name": "Tłum, w którym łatwo zniknąć", "hidden": False, "free": 0},
        {"name": "Patrole Sędziów co kwadrans", "hidden": False, "free": 0},
        {"name": "Przekupki widzą wszystko, mówią za drobne", "hidden": True, "free": 1}
    ],
    "description": "Brud, krzyk, zapach smażonych szczurów. Studnia na środku placu stoi teraz zamknięta łańcuchem Spitalian."
}, "icons/svg/house.svg"))

packs["przyklady"].append(actor("Frakcja: Krucze Stado (Apokaliptycy)", "frakcja", {
    "cel": "Uspokoić dzielnicę Dostawców Burnem i zgarnąć zapłatę od Sędziego",
    "zasoby": 3, "imie": {"value": 0, "echo": 0}, "osobiste": "", "cecha": "Każdy jest coś winien Krukom",
    "clocks": [{"name": "Dostawa dla Sędziego", "size": 6, "value": 3}], "notes": ""
}, "icons/svg/wing.svg"))

packs["przyklady"].append(actor("Frakcja: Spitalianie z lazaretu", "frakcja", {
    "cel": "Wypalić ognisko Sepsy, zanim się rozprzestrzeni", "zasoby": 4, "imie": {"value": 1, "echo": 2}, "osobiste": "", "cecha": "Lepiej spalić za dużo niż za mało",
    "clocks": [{"name": "Kwarantanna i podpalenie dzielnicy", "size": 6, "value": 1}], "notes": ""
}, "icons/svg/fire.svg"))

packs["przyklady"].append(actor("Rejestr Długów (kampania)", "rejestr", {
    "debts": [
        {"debtor": "", "debtorText": "Drużyna", "creditor": "", "creditorText": "Spitalianie z lazaretu", "waga": 2, "powod": "Leczenie bez pytań o pochodzenie ran", "status": "otwarty", "hidden": False},
        {"debtor": "", "debtorText": "Halka, przekupka", "creditor": "", "creditorText": "Drużyna", "waga": 1, "powod": "Nie wydali jej syna Sędziom", "status": "otwarty", "hidden": False},
        {"debtor": "", "debtorText": "Sędzia Varga", "creditor": "", "creditorText": "Krucze Stado", "waga": 3, "powod": "Burn w studniach — Kruki wiedzą wszystko", "status": "otwarty", "hidden": True}
    ],
    "notes": "Po imporcie wybierz dłużników i wierzycieli z listy aktorów — wtedy spłata i zerwanie same przesuną Echo frakcji."
}, "icons/svg/coins.svg"))

npc_halka = stats({"cia": 2, "zre": 2, "cha": 3, "int": 2, "psy": 2, "ins": 3}, {"negocjacje": 3, "spryt": 2, "percepcja": 3, "empatia": 2, "twardosc": 1, "wola": 2})
npc_halka.update({"scale": "statysta", "size": {"value": 1, "max": 1}, "ego": {"value": 4, "max": 4}, "armor": 0, "kult": "brak (Dostawcy)", "ranga": "",
    "motyw": "Utrzymać stragan i syna z dala od Sędziów", "lek": "Że syn pił z zatrutej studni", "sekret": "Syn nosi beczki dla Kruków",
    "cena": "Lekarstwo dla syna albo glejt od Sędziów", "postawa": -1, "eliminated": False, "defense": {"bonus": 0}, "wounds": {"lekkie": 0, "powazne": 0, "krytyczna": 0}, "notes": ""})
packs["przyklady"].append(actor("Halka, przekupka", "npc", npc_halka))

npc_sedzia = stats({"cia": 3, "zre": 2, "cha": 3, "int": 2, "psy": 4, "ins": 2}, {"dominacja": 4, "bronBiala": 3, "strzelectwo": 2, "obycie": 3, "oszustwo": 3, "wola": 3, "twardosc": 2, "refleks": 2})
npc_sedzia.update({"scale": "antagonista", "size": {"value": 1, "max": 1}, "ego": {"value": 8, "max": 8}, "armor": 2, "kult": "Sędziowie", "ranga": "Sędzia miejski",
    "motyw": "Spokój w dzielnicy przed wizytą Senatora", "lek": "Że Kodeks go dosięgnie", "sekret": "Opłacił Kruki za Burn w studniach",
    "cena": "Czyjaś głowa zamiast jego", "postawa": 0, "eliminated": False, "defense": {"bonus": 0}, "wounds": {"lekkie": 0, "powazne": 0, "krytyczna": 0}, "notes": ""})
packs["przyklady"].append(actor("Sędzia Varga", "npc", npc_sedzia, items=[weapon("Pałka / maczuga"), weapon("Muszkiet")]))

npc_banda = stats({"cia": 3, "zre": 2, "cha": 1, "int": 1, "psy": 2, "ins": 2}, {"bronBiala": 2, "bijatyka": 2, "twardosc": 1, "skradanie": 1, "refleks": 1})
npc_banda.update({"scale": "banda", "size": {"value": 6, "max": 6}, "ego": {"value": 3, "max": 3}, "armor": 1, "kult": "Apokaliptycy", "ranga": "",
    "motyw": "Zarobić i nie dać się złapać", "lek": "Sędziowie", "sekret": "", "cena": "Dinary", "postawa": -1, "eliminated": False,
    "defense": {"bonus": 0}, "wounds": {"lekkie": 0, "powazne": 0, "krytyczna": 0}, "notes": "Morale: uciekają przy 3 stratach."})
packs["przyklady"].append(actor("Banda tragarzy Kruków", "npc", npc_banda, items=[weapon("Nóż")]))


# ---------------- v0.3: dzienniki graczy, przygoda, przeciwnicy, gotowe postacie ----------------
SKILL_ATTR = {sk: a for a, lst in SK.items() for sk in lst}
ASSET = "systems/degenesis2/assets"
packs["gracze"].append(journal("Podręcznik gracza", PLAYER_PAGES))
_pdf = journal("Podręcznik Gracza (PDF)", [("Podręcznik Gracza", "")])
_pdf["pages"][0].update({"type": "pdf", "src": "systems/degenesis2/assets/docs/Degenesis-2.0-Podrecznik-Gracza.pdf", "text": {"format": 1, "content": ""}})
_pdf["sort"] = -1
packs["gracze"].append(_pdf)

cult_pages = []
for name, skills, metoda, ideal, desc in KULTY:
    bon = ", ".join(SKILL_PL[x] for x in skills)
    html = (f"<p>{desc}</p><p><b>Bonusy do limitu umiejętności:</b> {bon}</p><p><b>Metoda (śledztwo):</b> {metoda}</p>"
            f"<p><b>Ideał:</b> {ideal}</p><h3>Rangi</h3><p>Wymagania liczą sumę Atrybut+Umiejętność. Każdy zaczyna od rangi 1 i wspina się, dopóki je spełnia.</p>{rank_table(name)}"
            f"<h3>Potencjały</h3>{pot_list(name)}"
            f"<p class='d2-gmnote'>Źródło: Katharsys, rangi s. {RANK_PAGES[name][0]}–{RANK_PAGES[name][0] + 1}, Potencjały s. {RANK_PAGES[name][1]}. Treść streszczona i przeliczona na 2.0 (+1D → +1K, Rany Powierzchowne → Lekkie rany, Trauma → rana Poważna). Dopiski w nawiasie [2.0] są nasze. „spec.” = ranga poboczna (np. Zero, Lekarz wiejski), nie do wyboru w kreatorze.</p>")
    cult_pages.append((name, html))
cult_pages.append(("Potencjały ogólne", "<p>Dostępne dla każdego kultu. PP = poziom Potencjału (1–3).</p><ul>" + "".join(f"<li><b>{n}</b>{' <i>(wym.: ' + pr + ')</i>' if pr else ''}: {d}</li>" for n, pr, d in COMMON) + "</ul>"))
packs["gracze"].append(journal("Kulty — przewodnik", cult_pages))

ATTR_PL = {"cia": "Ciało", "zre": "Zręczność", "cha": "Charyzma", "int": "Intelekt", "psy": "Psyche", "ins": "Instynkt"}
kul_pages = [(n, f"<p>{d}</p><p><b>Atrybuty z bonusem:</b> {', '.join(ATTR_PL[a] for a in at)}<br><b>Umiejętności z bonusem:</b> {', '.join(SKILL_PL[x] for x in sk)}</p><p><b>Typowe kulty:</b> {c}</p>") for n, at, sk, c, d in KULTURY]
kon_html = "<p>Koncept to archetyp z Tarota Apokaliptyków. Raz na sesję daje +2K w zgodnej sytuacji. Jego Cień to pokusa, którą MG może wykorzystać.</p><table><tr><th>Arkana</th><th>Archetyp</th><th>Bonusy</th><th>Cień</th></tr>"
for t, n, a, sk, c in KONCEPTY:
    kon_html += f"<tr><td>{t}</td><td><b>{n}</b></td><td>{ATTR_PL[a]}; {', '.join(SKILL_PL[x] for x in sk)}</td><td>{c}</td></tr>"
kon_html += "</table>"
packs["gracze"].append(journal("Kultury i Archetypy", kul_pages + [("Archetypy (Koncepty)", kon_html)]))

packs["przygoda"].append(journal("Ciche studnie — przygoda (MG)", ADVENTURE))
packs["przygoda"].append(journal("Szkoła MG: pierwsza sesja", GM_SCHOOL))
from music_links import MUSIC_PAGES
packs["przygoda"].append(journal("Muzyka do sesji (Spotify, YouTube)", MUSIC_PAGES))

def folder(name, type_="Actor", sort=0):
    fid = rid()
    return {"_id": fid, "_key": f"!folders!{fid}", "name": name, "type": type_, "folder": None, "sorting": "a", "sort": sort,
            "color": None, "description": "", "flags": {}, "_stats": STATS}

def pools_to_stats(pools):
    attrs = {a: 1 for a in ATTRS}; skills = {}
    norm = {"init": "refleks", "mental": "wola"}
    by_attr = {}
    for k, v in pools.items():
        if k in ("prymer", "zjb", "obr"): continue
        sk = norm.get(k, k); a = SKILL_ATTR[sk]
        by_attr.setdefault(a, []).append((sk, v))
    for a, lst in by_attr.items():
        mx = max(v for _, v in lst)
        attrs[a] = max(1, min(6, max(mx - 6, (mx + 1) // 2)))
        for sk, v in lst:
            skills[sk] = max(0, min(6, v - attrs[a]))
    return attrs, skills

folders = {}
for grp in ["Ludzie", "Bestie", "Prymer", "Maszyny i Śpiący", "Psychonauci"]:
    f = folder(grp, sort=len(folders) * 100); folders[grp] = f["_id"]; packs["przeciwnicy"].append(f)
for grp, name, scale, ego, armor, prog, pools, attacks, pots, motyw, lek, sekret, cena, desc in ENEMIES:
    attrs, skills = pools_to_stats(pools)
    st = stats(attrs, skills)
    base_prog = attrs["cia"] + skills.get("twardosc", 0)
    st.update({"scale": scale, "size": {"value": 6 if scale == "banda" else 1, "max": 6 if scale == "banda" else 1},
               "ego": {"value": ego, "max": ego}, "armor": armor, "progBonus": max(0, prog - base_prog), "kult": grp, "ranga": "",
               "motyw": motyw, "lek": lek, "sekret": sekret, "cena": cena, "postawa": -2 if grp != "Ludzie" else -1, "frakcja": "",
               "eliminated": False, "prymer": {"value": pools.get("prymer", (0, 0))[0], "max": pools.get("prymer", (0, 0))[1]},
               "zjawiskaBonus": pools.get("zjb", 0), "defense": {"bonus": pools.get("obr", 0)}, "wounds": {"lekkie": 0, "powazne": 0, "krytyczna": 0}, "notes": f"<p>{desc}{' [2.0 — profil własny]' if grp == 'Ludzie' and '[' not in desc else ''}</p>"})
    its = []
    for wn, wsk, dmg, rng, q, hand in attacks:
        its.append({"name": wn, "type": "bron", "img": "icons/svg/sword.svg" if wsk != "strzelectwo" else "icons/svg/target.svg",
                    "system": {"description": "", "skill": wsk, "handling": hand, "damage": dmg, "range": zone(rng), "magazine": {"value": 0, "max": 0},
                               "qualities": q, "encumbrance": 0, "equipped": True}, "effects": [], "flags": {}, "_stats": STATS})
    for pt in pots:
        pn, pd = pt[0], pt[1]
        zl = pt[2] if len(pt) > 2 else None
        its.append({"name": pn, "type": "potencjal", "img": "icons/svg/aura.svg" if zl is None else "icons/svg/biohazard.svg",
                    "system": {"description": p(pd), "level": 1, "kult": "", "prerequisite": "", "zjawisko": zl is not None, "poziomZjawiska": zl or 0},
                    "effects": [], "flags": {}, "_stats": STATS})
    a = actor(name, "npc", st, "icons/svg/skull.svg" if grp != "Ludzie" else "icons/svg/mystery-man.svg", items=its)
    a["folder"] = folders[grp]
    packs["przeciwnicy"].append(a)

def find_item(pack, pred):
    d = next(x for x in packs[pack] if pred(x))
    return {k: v for k, v in d.items() if k not in ("_id", "_key", "folder", "sort")}

for nm, kul, kon, kt, path, belief, attrs, skills, bgs, rank, pot, weapons, desc in PREGENS:
    assert sum(attrs.values()) - 6 == 10, (nm, "attrs", sum(attrs.values()) - 6)
    assert sum(skills.values()) == 28, (nm, "skills", sum(skills.values()))
    assert sum(bgs.values()) == 4, (nm, "bgs")
    st = stats(attrs, skills)
    pa = "ins" if path == "pierwotnosc" else "int"
    st.update({"path": path, "belief": belief,
        "backgrounds": {b: {"value": bgs.get(b, 0), "spent": 0} for b in ["sojusznicy", "autorytet", "slawa", "zasoby", "sekrety", "siec"]},
        "zarazenie": {"value": 0, "permanent": 0}, "archetypeUsed": False,
        "identity": {"kultura": kul, "koncept": next(x["name"] for x in packs["koncepty"] if kon in x["name"]), "kult": kt, "ranga": rank, "wiek": "", "plec": ""},
        "ambicja": "", "tajemnica": "", "cien": next(c for t, n, a_, s_, c in KONCEPTY if n == kon), "wiezi": "", "blizny": "",
        "xp": {"total": 0, "spent": 0}, "money": "", "eliminated": False,
        "ego": {"value": (attrs[pa] + skills.get(path, 0)) * 2}, "defense": {"bonus": 0}, "wounds": {"lekkie": 0, "powazne": 0, "krytyczna": 0},
        "notes": f"<p>{desc}</p>"})
    its = [find_item("kultury", lambda x: x["name"] == kul), find_item("koncepty", lambda x: kon in x["name"]),
           find_item("kulty", lambda x: x["name"] == kt), find_item("potencjaly", lambda x: x["name"] == pot)]
    its += [find_item("ekwipunek", lambda x, w=w: x["name"] == w) for w in weapons]
    its.append(find_item("ekwipunek", lambda x: x["name"] == "Płaszcz skórzany"))
    key, amb, taj, wiez, bio = PREGEN_EXTRA[nm]
    st.update({"ambicja": amb, "tajemnica": taj, "wiezi": wiez, "notes": f"<p>{bio}</p>"})
    a = actor(nm, "postac", st, f"{ASSET}/portraits/{key}.webp", items=its, token=f"{ASSET}/tokens/{key}.webp")
    packs["postacie"].append(a)


# ---- obrazy dla NPC z przykładów + nowi NPC ----
IMG = {"Halka, przekupka": "halka", "Sędzia Varga": "varga", "Banda tragarzy Kruków": "tragarze"}
for a in packs["przyklady"]:
    k = IMG.get(a["name"])
    if k:
        a["img"] = f"{ASSET}/portraits/{k}.webp"; a["prototypeToken"]["texture"] = {"src": f"{ASSET}/tokens/{k}.webp"}
for nm, key, scale, att, attrs, skills, motyw, lek, sekret, cena, desc, weapons in NEW_NPCS:
    st = stats(attrs, skills)
    st.update({"scale": scale, "size": {"value": 1, "max": 1}, "ego": {"value": 6, "max": 6}, "armor": 1, "progBonus": 0, "kult": "", "ranga": "",
               "motyw": motyw, "lek": lek, "sekret": sekret, "cena": cena, "postawa": att, "frakcja": "", "eliminated": False,
               "defense": {"bonus": 0}, "wounds": {"lekkie": 0, "powazne": 0, "krytyczna": 0}, "notes": f"<p>{desc}</p>"})
    its = [find_item("ekwipunek", lambda x, w=w: x["name"] == w) for w in weapons]
    packs["przyklady"].append(actor(nm, "npc", st, f"{ASSET}/portraits/{key}.webp", items=its, token=f"{ASSET}/tokens/{key}.webp"))

# ---- sceny ----
SCENE_NAMES = {"dzielnica": "Justitian — plan dzielnicy Dostawców", "targ-studnia": "Targ i studnia przy Bramie", "lazaret": "Lazaret Spitalian",
               "spelunka-krukow": "Pod Złamanym Skrzydłem (spelunka Kruków)", "kancelaria-vargi": "Kancelaria Sędziego Vargi"}
STATS13 = dict(STATS, coreVersion="13.351")
for i, (key, (fn, gridsize)) in enumerate(MAPS.items()):
    sid = rid()
    w, h = (2400, 1600) if gridsize is None else (gridsize[0] * 70, gridsize[1] * 70)
    packs["sceny"].append({"_id": sid, "_key": f"!scenes!{sid}", "name": SCENE_NAMES[key], "navName": "", "navigation": True, "navOrder": i,
        "active": False, "width": w, "height": h, "padding": 0.05, "backgroundColor": "#0b0a09",
        "background": {"src": f"{ASSET}/maps/{key}.webp"}, "thumb": None,
        "grid": {"type": 0 if gridsize is None else 1, "size": 70 if gridsize else 100, "distance": 1, "units": "m", "alpha": 0, "color": "#000000"},
        "initial": {"x": None, "y": None, "scale": None}, "tokenVision": False, "fog": {"exploration": False},
        "tokens": [], "lights": [], "notes": [], "sounds": [], "tiles": [], "walls": [], "drawings": [], "regions": [],
        "folder": None, "sort": i * 100, "ownership": {"default": 0}, "flags": {}, "_stats": STATS13})

# ---- muzyka i odgłosy (licencje: assets/audio/CREDITS.md) ----
M = f"{ASSET}/audio/muzyka"; O = f"{ASSET}/audio/odglosy"
def kb(n): return f"{M}/kb-{n}.ogg"
def ae(n): return f"{M}/aeris-{n}.mp3"
KB_T = {"empty-world": "Empty World", "last-man-on-earth": "Last Man On Earth", "forest-and-the-trees-earlymix": "Forest and the Trees",
        "abandoned-cabin-in-the-woods": "Abandoned Cabin in the Woods", "civil-twilight-in-orange-and-black": "Civil Twilight in Orange and Black",
        "rebuild": "Rebuild", "day-one-theme": "Day One Theme", "government-camp": "Government Camp", "isherwood-theme": "Isherwood Theme",
        "subway-tunnel": "Subway Tunnel", "shaken-breath": "Shaken Breath", "deep-freeze-facility": "Deep Freeze Facility",
        "moldy-arabesque": "Moldy Arabesque", "meteor-strike": "Meteor Strike", "amniotic-cocoon": "Amniotic Cocoon",
        "electric-sky": "Electric Sky", "the-cosmic-hum": "The Cosmic Hum", "boneseer": "Boneseer"}
AE_T = {"signal-lost": "Signal Lost", "beneath": "Beneath", "the-long-walk-signal-lost": "The Long Walk", "ash": "Ash",
        "colder-air": "Colder Air", "overdrive-signal-lost": "Overdrive", "quiet-room": "Quiet Room"}
def K(n): return (f"{KB_T[n]} — Kaelin Bougneit", kb(n))
def E(n): return (f"{AE_T[n]} — AERIS", ae(n))
PLAYLISTS = [
 ("Degenesis — Odgłosy (tło)", "Pętle tła do łączenia z twoją muzyką: kliknij pojedynczy odgłos, żeby go włączyć.", -1, "environment", 0.35, True,
  [("Deszcz", f"{O}/deszcz.ogg"), ("Mżawka", f"{O}/mzawka.ogg"), ("Ulewa pod dachem", f"{O}/ulewa-pod-dachem.ogg"), ("Burza", f"{O}/burza.ogg"),
   ("Zamieć", f"{O}/zamiec.ogg"), ("Noc — świerszcze", f"{O}/noc-swierszcze.ogg"), ("Noc — wiatr", f"{O}/noc-wiatr.ogg"),
   ("Pochmurny dzień", f"{O}/pochmurny-dzien.ogg"), ("Podziemia, kanały", f"{O}/podziemia.ogg"), ("Wnętrze budynku", f"{O}/wnetrze.ogg")]),
 ("Degenesis — Efekty (jednorazowe)", "Pojedyncze dźwięki: dzwon lazaretu, alarm, grzmot.", -1, "environment", 0.6, False,
  [("Dzwony", f"{O}/dzwony.ogg"), ("Alarm", f"{O}/alarm.ogg"), ("Grzmot", f"{O}/grzmot.ogg")]),
]
SCENE_SOUND = {}
for i, (name, desc, mode, channel, vol, repeat, tracks) in enumerate(PLAYLISTS):
    plid = rid(); sounds = []
    for j, (nm, path) in enumerate(tracks):
        sid = rid()
        sounds.append({"_id": sid, "_key": f"!playlists.sounds!{plid}.{sid}", "name": nm, "description": "", "path": path, "channel": "",
                       "repeat": repeat, "volume": vol, "fade": 1500, "sort": j * 100, "playing": False, "pausedTime": None, "flags": {}, "_stats": STATS})
        if name.startswith("Ciche studnie"): SCENE_SOUND[nm] = (plid, sid)
    packs["muzyka"].append({"_id": plid, "_key": f"!playlists!{plid}", "name": name, "description": desc,
        "mode": mode, "channel": channel, "playing": False, "fade": 1500, "sounds": sounds, "folder": None, "sort": i * 100, "seed": None,
        "ownership": {"default": 0}, "flags": {}, "_stats": STATS})
packs["gracze"].append(journal("Odgłosy — źródła i licencje", [("Źródła", open("/home/claude/degenesis2/assets/audio/CREDITS.html", encoding="utf-8").read())]))

# --- Stałe ID (deterministyczne): te same dokumenty mają te same ID w każdej wersji ---
import hashlib
_ALPH = string.ascii_letters + string.digits
def _sid(*parts):
    h = hashlib.sha256("|".join(parts).encode("utf-8")).digest()
    return "".join(_ALPH[b % len(_ALPH)] for b in h[:16])
_IDMAP = {}
for _pname, _docs in packs.items():
    _seen = {}
    for _d in _docs:
        _kind = _d["_key"].split("!")[1]
        _base = f"{_pname}|{_kind}|{_d.get('type', '')}|{_d['name']}"
        _n = _seen.get(_base, 0); _seen[_base] = _n + 1
        _new = _sid(_base, str(_n))
        _IDMAP[_d["_id"]] = _new
        for _emb in ("items", "pages", "sounds"):
            _eseen = {}
            for _e in _d.get(_emb, []) or []:
                _eb = f"{_new}|{_emb}|{_e.get('name', '')}"
                _en = _eseen.get(_eb, 0); _eseen[_eb] = _en + 1
                if "_id" in _e: _IDMAP[_e["_id"]] = _sid(_eb, str(_en))
_RX = re.compile("|".join(map(re.escape, sorted(_IDMAP, key=len, reverse=True)))) if _IDMAP else None
def _remap(obj):
    if isinstance(obj, dict): return {k: _remap(v) for k, v in obj.items()}
    if isinstance(obj, list): return [_remap(v) for v in obj]
    if isinstance(obj, str) and _RX: return _RX.sub(lambda m: _IDMAP[m.group(0)], obj)
    return obj
packs = {k: [_remap(d) for d in v] for k, v in packs.items()}

# --- Zapis ---
shutil.rmtree(ROOT, ignore_errors=True)
for name, docs in packs.items():
    d = os.path.join(ROOT, name); os.makedirs(d, exist_ok=True)
    for doc in docs:
        safe = "".join(c if c.isalnum() else "_" for c in doc["name"])[:40]
        json.dump(doc, open(os.path.join(d, f"{safe}_{doc['_id']}.json"), "w"), ensure_ascii=False, indent=1)
print({k: len(v) for k, v in packs.items()})

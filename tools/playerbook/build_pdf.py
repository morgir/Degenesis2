# -*- coding: utf-8 -*-
import sys, os, re, subprocess, html, json
sys.path.insert(0, "/home/claude/build"); sys.path.insert(0, os.path.dirname(__file__))
from content import KULTURY, KULTY, KONCEPTY
from cult_data import RANKS, POTENTIALS
from player_pages import PREGENS
from adventure_full import PREGEN_EXTRA
from content_pb import INTRO, WORLD, REGIONS, CULT_FLAVOR
from rules_pb import RULES, CREATION, GLOSSARY

A = "/home/claude/degenesis2/assets"
OUT = "/home/claude/playerbook"
ATTR = {"cia": "Ciało", "zre": "Zręczność", "cha": "Charyzma", "int": "Intelekt", "psy": "Psyche", "ins": "Instynkt"}
SK = {"atletyka": "Atletyka", "bijatyka": "Bijatyka", "sila": "Siła", "bronBiala": "Broń biała", "kondycja": "Kondycja", "twardosc": "Twardość",
      "rzemioslo": "Rzemiosło", "zwinnePalce": "Zwinne palce", "prowadzenie": "Prowadzenie", "mobilnosc": "Mobilność", "strzelectwo": "Strzelectwo", "skradanie": "Skradanie",
      "sztuka": "Sztuka", "obycie": "Obycie", "ekspresja": "Ekspresja", "przywodztwo": "Przywództwo", "negocjacje": "Negocjacje", "uwodzenie": "Uwodzenie",
      "artefakty": "Artefakty", "inzynieria": "Inżynieria", "skupienie": "Skupienie", "legendy": "Legendy", "medycyna": "Medycyna", "nauka": "Nauka",
      "spryt": "Spryt", "oszustwo": "Oszustwo", "dominacja": "Dominacja", "wiara": "Wiara", "refleks": "Refleks", "wola": "Wola",
      "empatia": "Empatia", "orientacja": "Orientacja", "percepcja": "Percepcja", "pierwotnosc": "Pierwotność", "przetrwanie": "Przetrwanie", "oswajanie": "Oswajanie"}
SKATTR = {}
for a, sks in {"cia": ["atletyka", "bijatyka", "sila", "bronBiala", "kondycja", "twardosc"], "zre": ["rzemioslo", "zwinnePalce", "prowadzenie", "mobilnosc", "strzelectwo", "skradanie"],
               "cha": ["sztuka", "obycie", "ekspresja", "przywodztwo", "negocjacje", "uwodzenie"], "int": ["artefakty", "inzynieria", "skupienie", "legendy", "medycyna", "nauka"],
               "psy": ["spryt", "oszustwo", "dominacja", "wiara", "refleks", "wola"], "ins": ["empatia", "orientacja", "percepcja", "pierwotnosc", "przetrwanie", "oswajanie"]}.items():
    for s in sks: SKATTR[s] = a
BG = {"sojusznicy": "Sojusznicy", "autorytet": "Autorytet", "slawa": "Sława", "zasoby": "Zasoby", "sekrety": "Sekrety", "siec": "Sieć"}

TOC = []
def H1(title, kicker=""):
    i = f"s{len(TOC)}"; TOC.append((1, title, i))
    return f'<section class="part" id="{i}"><div class="kicker">{kicker}</div><h1>{title}</h1></section>'
def H2(title, cls=""):
    i = f"s{len(TOC)}"; TOC.append((2, title, i))
    return f'<h2 id="{i}" class="{cls}">{title}</h2>'

def img(path): return "file://" + path

# ---------- Treść ----------
body = []
body.append(f"""<section class="cover"><div class="cover-in">
<div class="c-top">Degenesis · Katharsys · edycja fanowska</div>
<div class="c-title">DEGENESIS<span>2.0</span></div>
<div class="c-sub">Podręcznik Gracza</div>
<div class="c-line"></div>
<div class="c-desc">Świat · Regiony · Kulty · Zasady · Postacie<br>oraz zajawka przygody <b>„Ciche studnie”</b></div>
<div class="c-port">{''.join(f'<img src="{img(A + "/portraits/" + p + ".webp")}">' for p in ["wera", "oddo", "sroka", "borsuk", "modus", "anja", "kaspar"])}</div>
<div class="c-foot">Rok 2595. Świat jest groźny, ale nie morderczy.</div></div></section>""")
body.append("@@TOC@@")

# I. Świat
body.append(H1("Świat", "Część I"))
body.append(H2("Witaj w 2595 roku")); body.append(INTRO)
for t, h in WORLD:
    body.append(H2(t)); body.append(h)

# II. Regiony
body.append(H1("Regiony", "Część II"))
body.append('<p class="lead">Europa i Afryka po Eshatonie dzielą się na siedem Kultur. Twoja postać pochodzi z jednej z nich. Kultura daje bonus dwóm atrybutom i kilku umiejętnościom oraz mówi, jakie kulty spotkasz w domu. <b>Bonus podnosi limit cechy przy tworzeniu postaci o 1</b> i obniża koszt jej rozwoju; nie jest darmowym punktem.</p>')
kul = {k[0]: k for k in KULTURY}
for name, motto, h, skills, attrs in REGIONS:
    k = kul[name]
    attrs = ", ".join(ATTR[a] for a in k[1]); skills = ", ".join(SK[s] for s in k[2])
    body.append(f'<div class="region">{H2(name)}<div class="motto">{motto}</div>{h}'
                f'<div class="meta"><b>Bonus (limit +1), atrybuty:</b> {attrs} · <b>umiejętności:</b> {skills}<br><b>Kulty obecne:</b> {k[3]}</div></div>')

# III. Kulty
body.append(H1("Kulty", "Część III"))
body.append('<p class="lead">Kult to więcej niż pracodawca. To rodzina, ideologia i sieć długów. Daje ci Zaplecze, rangę, Potencjały i metodę dochodzenia do prawdy, ale też rozkazy, wrogów i oczekiwania. Kult daje bonus kilku umiejętnościom: <b>limit każdej z nich przy tworzeniu postaci rośnie o 1</b>, a rozwój jest tańszy.</p>'
            '<p>Przy każdym kulcie znajdziesz: kim są, ich <b>Ideał</b> (który przywraca Ego, gdy dochowasz mu wierności wbrew własnemu interesowi), <b>Metodę</b> śledczą (raz na scenę dodatkowa Odsłona) i rangi dostępne na starcie. Pełne tabele rang i Potencjałów są w Foundry, w dzienniku <i>Kulty — przewodnik</i>.</p>')
for name, skills, metoda, ideal, desc in KULTY:
    ranks = [r for r in RANKS[name] if r[0] in (1, 2, 3) and not any(isinstance(x, tuple) and x[0] == "txt" and "kampania" in x[1] for x in r[2])]
    rk = " → ".join(sorted({f"{r[1].split(' (')[0]}" for r in ranks if r[0] == 1})) + " → " + ", ".join(r[1].split(' (')[0] for r in ranks if r[0] in (2, 3))
    pots = ", ".join(p[0].split(" (")[0] for p in POTENTIALS.get(name, [])) or "brak własnych, korzysta z ogólnych"
    bon = ", ".join(SK[s] for s in skills)
    body.append(f'<div class="cult">{H2(name)}<p class="cdesc">{desc}</p><p class="flav">{CULT_FLAVOR[name]}</p>'
                f'<table class="kv"><tr><th>Ideał</th><td>{ideal}</td></tr><tr><th>Metoda</th><td>{metoda}</td></tr>'
                f'<tr><th>Bonus (limit +1)</th><td>{bon}</td></tr><tr><th>Rangi startowe</th><td>{rk}</td></tr>'
                f'<tr><th>Potencjały</th><td>{pots}</td></tr></table></div>')

# IV. Zasady
body.append(H1("Zasady", "Część IV"))
body.append('<p class="lead">Degenesis 2.0 opiera się na kościach z Katharsys (pula k6, sukces od 4, szóstki jako Wyzwalacze), ale wyniki czyta się jak w grach narracyjnych: „Tak, i…”, „Tak, ale…”, „Nie, i…”. Poniżej wszystko, czego potrzebujesz przy stole. Resztę MG wyjaśni w trakcie gry.</p>')
for t, h in RULES:
    body.append(H2(t)); body.append(h)
body.append(H2("Przykład z gry"))
body.append("""<div class="example"><p><b>MG:</b> Lazaret śmierdzi wapnem. Na pryczy leży tragarz i uśmiecha się do sufitu. Co robisz?</p>
<p><b>Gracz (Wera):</b> Badam go. Szukam śladów Sepsy: zarodników w nosie, stygmatu na piersi.</p>
<p><b>MG:</b> To dobre miejsce i dobra umiejętność, więc trop kluczowy dostajesz od razu: <i>to nie jest Sepsa, nie ma ani śladu zarodników</i>. Rzuć Intelekt + Medycyna, Trudność 2, żeby wiedzieć więcej.</p>
<p><b>Gracz:</b> Mam 7 kości i dokładam 1 Ego. Wypada 6, 6, 5, 3, 2, 1, 1, czyli 3 sukcesy i 2 Wyzwalacze: „Tak, i…”. Biorę dwie Odsłony.</p>
<p><b>MG:</b> Źrenice są rozszerzone jak po narkotyku (Szczegół), a na kubku przy łóżku osiadł biały, słodkawy osad (Powiązanie, prowadzi do studni). Zapisz oba tropy na tablicy.</p></div>""")

# V. Postać
body.append(H1("Twoja postać", "Część V"))
body.append(H2("Tworzenie krok po kroku")); body.append(CREATION)
body.append(H2("Koncepty — 22 Archetypy"))
body.append('<p>Koncept to karta Tarota, która opisuje, kim twoja postać jest w głębi. Daje bonus do jednego atrybutu i 2–3 umiejętności (limit każdej z tych cech +1 przy tworzeniu), raz na sesję +2K, gdy działasz zgodnie z nim, oraz <b>Cień</b>, czyli pokusę, której możesz ulec za Ego i PD.</p>')
rows = "".join(f"<tr><td class='num'>{k[0]}</td><td><b>{k[1]}</b></td><td>{ATTR[k[2]]}</td><td>{', '.join(SK[s] for s in k[3])}</td><td><i>{k[4]}</i></td></tr>" for k in KONCEPTY)
body.append(f'<table class="small"><tr><th>#</th><th>Koncept</th><th>Atrybut ☆</th><th>Umiejętności ☆</th><th>Cień</th></tr>{rows}</table>')
body.append(H2("Atrybuty i umiejętności"))
grid = "".join(f"<div class='att'><h4>{n}</h4><p>{', '.join(SK[s] for s in SKATTR if SKATTR[s] == a)}</p></div>" for a, n in
               [("cia", "Ciało"), ("zre", "Zręczność"), ("cha", "Charyzma"), ("int", "Intelekt"), ("psy", "Psyche"), ("ins", "Instynkt")])
body.append(f'<div style="break-inside:avoid"><div class="attgrid">{grid}</div><p class="note">Skupienie/Pierwotność i Wiara/Wola to pary: wybierasz po jednej z każdej przy tworzeniu postaci.</p></div>')

# VI. Gotowe postacie
body.append(H1("Gotowe postacie", "Część VI"))
body.append('<p class="lead">Siedem postaci przygotowanych do przygody „Ciche studnie”. Każda ma osobisty powód, żeby tam być. <b>Swoją Tajemnicę dostaniesz od MG na osobnej kartce</b>, dlatego nie ma jej tutaj.</p>')
TRIM = {
 "Brat Kaspar": "Gdy usłyszał o uśmiechniętych chorych w dzielnicy Dostawców, od razu rozpoznał objawy.",
 "Kasia „Sroka”": "Stado kazało jej mieć oko na wszystko, co dzieje się przy studni.",
 "Mirek „Borsuk”": "Wczoraj zobaczył, że ktoś zamalował jego runę na włazie kanału pod dzielnicą Dostawców.",
 "Modus": "Klaster zauważył, że wydajność dzielnicy Dostawców spadła o jedną trzecią, i wysłał go, żeby ustalił dlaczego, zanim zrobią to Sędziowie.",
}
for pg in PREGENS:
    name, kultura, koncept, kult, path, belief, attrs, skills, bgs, ranga, pot, weapons, desc = pg
    ex = PREGEN_EXTRA[name]; port, ambicja, _secret, wiez, hist = ex
    if name in TRIM:
        cut = TRIM[name]; key = cut.split(",")[0].split(" ")[0:3]
        # obetnij historię po zdaniu-kotwicy i dopisz bezpieczną wersję
        sentences = re.split(r"(?<=[.!?])\s+", hist)
        keep = []
        for s in sentences:
            if any(w in s for w in ["Burn Unity", "Wie też", "beczki", "dziecko", "sprzedał Krukom", "Wczoraj", "archiwach", "Gdy usłyszał", "Ilsa Kruczyca kazała", "Klaster zauważył", "Problem w tym"]): break
            keep.append(s)
        hist = " ".join(keep + [cut])
    pathattr = "int" if path == "skupienie" else "ins"
    ego = (attrs[pathattr] + skills.get(path, 0)) * 2
    zar = (attrs["psy"] + skills.get(belief, 0)) * 2
    prog = attrs["cia"] + skills.get("twardosc", 0)
    top = sorted(skills.items(), key=lambda kv: -(kv[1] + attrs[SKATTR[kv[0]]]))
    pools = ", ".join(f"{SK[s]} {v + attrs[SKATTR[s]]}" for s, v in top[:9])
    at = " · ".join(f"{ATTR[a]} {attrs[a]}" for a in ["cia", "zre", "cha", "int", "psy", "ins"])
    bg = ", ".join(f"{BG[k]} {v}" for k, v in bgs.items() if v)
    body.append(f'''<div class="pregen">{H2(name, "pg")}<div class="pg-in"><img src="{img(A + "/portraits/" + port + ".webp")}">
<div><div class="pg-tag">{kult} · {ranga.split(" (")[0]} · {kultura} · {koncept}</div>
<p>{hist}</p>
<p><b>Ambicja:</b> {ambicja}<br><b>Więź:</b> {wiez}</p>
<table class="kv small"><tr><th>Atrybuty</th><td>{at}</td></tr>
<tr><th>Najlepsze pule</th><td>{pools}</td></tr>
<tr><th>Ego / Zarażenie / Próg</th><td>{ego} / maks. {zar} / {prog} &nbsp;({SK[path]}, {SK[belief]})</td></tr>
<tr><th>Zaplecze</th><td>{bg}</td></tr><tr><th>Potencjał</th><td>{pot.split(" (")[0]}</td></tr>
<tr><th>Broń</th><td>{", ".join(weapons)}</td></tr></table></div></div></div>''')

# VII. Zajawka
body.append(H1("Ciche studnie", "Część VII · Zajawka przygody"))
body.append("""<div class="readaloud"><p>Justitian budzi się w szarym świcie. Nad dzielnicą Dostawców wisi smród gnijących warzyw, dymu i wapna. Od tygodnia jest tu za cicho. Tragarze nie kłócą się o miejsce przy bramie, przekupki nie przekrzykują się nad koszami, dzieci nie biegają między wozami. Ludzie uśmiechają się do siebie łagodnie, jak po dobrym winie, i zapominają, co mieli zrobić.</p>
<p>Przy Bramie Wschodniej studnię oplata łańcuch z pieczęcią Spitalu: biały krzyż w okręgu. Obok stoi Sędzia w szerokim kapeluszu i patrzy na tłum tak, jakby wszyscy byli winni. Z lazaretu dochodzi dzwon. Ktoś znów umarł z uśmiechem na ustach.</p></div>""")
body.append(H2("Co wiecie"))
body.append("""<ul><li><b>Justitian</b> to stolica Sędziów i serce Protektoratu w Borce. Miasto Kodeksu, młotów i wielkich obietnic.</li>
<li><b>Dzielnica Dostawców</b> karmi całe miasto. Mieszkają tu tragarze, przekupki, woźnice i rzeźnicy. Brud, praca i targ, który zaczyna się przed świtem.</li>
<li>Od tygodnia ludzie chorują. Majaczą, uśmiechają się do ścian, przestają pracować. Niektórzy umierają.</li>
<li><b>Spitalianie</b> zamknęli studnię przy Bramie Wschodniej. W lazarecie brakuje rąk, a ktoś już mówi o „oczyszczeniu ogniem”.</li>
<li><b>Sędziowie</b> pilnują studni i nie odpowiadają na pytania.</li>
<li>Każde z was ma swój powód, żeby tu być. Poznacie się przy studni.</li></ul>""")
body.append(H2("Mapa dzielnicy"))
body.append(f'<figure style="margin:0;break-inside:avoid"><img class="map" src="{img(A + "/maps/dzielnica.webp")}"><p class="caption">Justitian, dzielnica Dostawców. Miejsca, które zna każdy mieszkaniec.</p></figure>')
body.append(H2("Twarze dzielnicy"))
faces = [("varga", "Sędzia Varga", "Sędzia miejski, gospodarz dzielnicy. Twardy, zmęczony, coraz bardziej nerwowy."),
         ("kessel", "Higienista Kessel", "Spitalianin w masce gazowej. Uważa, że lepiej spalić za dużo niż za mało."),
         ("tobiasz", "Brat Tobiasz", "Famulancer z lazaretu. Zmęczony, uczciwy, nie śpi od kilku dni."),
         ("halka", "Halka", "Przekupka z targu przy Bramie. Wie wszystko o wszystkich i nikomu nie ufa."),
         ("ilsa", "Ilsa Kruczyca", "Gospodyni spelunki „Pod Złamanym Skrzydłem”, Apokaliptyczka. Uprzejma i cierpliwa.")]
body.append('<div class="faces">' + "".join(f'<div class="face"><img src="{img(A + "/portraits/" + f + ".webp")}"><b>{n}</b><p>{d}</p></div>' for f, n, d in faces) + "</div>")
body.append(H2("Przed pierwszą sesją"))
body.append("""<ul><li><b>Wybierz postać</b> z części VI albo stwórz własną (MG podpowie, jak połączyć ją z przygodą).</li>
<li><b>Przeczytaj</b> strony o swoim kulcie i Kulturze oraz rozdziały „Rzut kośćmi”, „Co znaczą wyniki” i „Śledztwo”. Reszta wyjdzie w grze.</li>
<li><b>Pomyśl</b>, co twoja postać chce chronić w tej dzielnicy, i zapytaj MG o swoją Tajemnicę.</li>
<li><b>Ustalcie granice.</b> Przygoda dotyczy choroby, uzależnienia i władzy, która milczy. Jeśli któryś temat jest dla ciebie za ciężki, powiedz o tym przed grą albo zatrzymaj scenę w trakcie.</li>
<li><b>Ta przygoda to śledztwo.</b> Walka jest możliwa, ale rzadko jest najlepszą odpowiedzią. Pytajcie, słuchajcie, łączcie tropy i zapisujcie długi.</li></ul>
<p class="tagline">Ktoś w tym mieście chce, żeby ludzie byli spokojni. Pytanie, ile ten spokój kosztuje i kto za niego płaci.</p>""")

# Dodatki
body.append(H1("Dodatki", ""))
body.append(H2("Słowniczek"))
body.append('<table class="small gl">' + "".join(f"<tr><th>{a}</th><td>{b}</td></tr>" for a, b in GLOSSARY) + "</table>")
body.append(H2("Ściąga gracza", "cheat"))
body.append("""<div class="cheat"><div class="two"><div>
<h4>Rzut</h4><p>Atrybut + Umiejętność k6. <b>4–6</b> sukces, <b>6</b> Wyzwalacz. Trudność: 1 rutyna · 2 standard · 3 trudne · 4 bardzo trudne · 6 desperackie.</p>
<h4>Wyniki</h4><p><b>Tak, i</b>: Efekt za każdy Wyzwalacz · <b>Tak</b> · <b>Tak, ale</b> (brak 1–2): sukces z Kosztem albo porażka · <b>Nie</b> · <b>Nie, i</b> (więcej jedynek niż sukcesów).</p>
<h4>Efekty</h4><p>Szybko · Czysto · Więcej · Przewaga · Wrażenie · Ochrona</p>
<h4>Dodatkowe kości</h4><p>Ego +1K/pkt (maks. 3) · Zaplecze maks. +3K · Cecha +2K · Dźwignia +2K · Archetyp +2K raz na sesję · Pomoc +1K/+2K</p>
<h4>Ego</h4><p>kość 1 · aktywna obrona 1 · rana o stopień lżej 2 · przerzut porażek 3</p>
</div><div>
<h4>Typowe rzuty</h4><table class="small">
<tr><td>Zauważyć, przeszukać</td><td>Instynkt + Percepcja</td></tr><tr><td>Wyczuć kłamstwo</td><td>Instynkt + Empatia</td></tr>
<tr><td>Przekonać, targować się</td><td>Charyzma + Negocjacje</td></tr><tr><td>Zastraszyć, przesłuchać</td><td>Psyche + Dominacja</td></tr>
<tr><td>Okłamać, przebrać się</td><td>Psyche + Oszustwo</td></tr><tr><td>Wiedza o kultach</td><td>Intelekt + Legendy</td></tr>
<tr><td>Leczyć, badać zwłoki</td><td>Intelekt + Medycyna</td></tr><tr><td>Zakraść się</td><td>Zręczność + Skradanie</td></tr>
<tr><td>Strzelać</td><td>Zręczność + Strzelectwo</td></tr><tr><td>Walczyć wręcz</td><td>Ciało + Broń biała / Bijatyka</td></tr>
<tr><td>Inicjatywa</td><td>Psyche + Refleks</td></tr><tr><td>Opór, Sepsa</td><td>Psyche + Wiara / Wola</td></tr></table>
<h4>Rany</h4><p>Próg = Ciało + Twardość. Lekka &lt; Próg (3) · Poważna ≥ Próg (2, −1K) · Krytyczna ≥ 2×Próg (1, −2K). Wyeliminowany ≠ martwy.</p>
<h4>Strefy</h4><p>Zwarcie · Blisko · Daleko · Poza zasięgiem. Tura: akcja + 1 strefa; bieg o 2 strefy = cała tura, +1 Obrony.</p>
<h4>Śledztwo</h4><p>Trop kluczowy zawsze. Odsłony: Szczegół · Powiązanie · Dźwignia · Ostrzeżenie · Czas. Wniosek (2): MG mówi „ciepło” albo „zimno” i nie kłamie.</p>
</div></div></div>""")

body.append(H2("Karta postaci"))
body.append('<p>Dwie ostatnie strony to karta postaci do wydruku. Wypełniaj ją ołówkiem według rozdziału <i>Tworzenie krok po kroku</i> (Część V). Ta sama karta jest osobnym plikiem w systemie: <i>assets/docs/Degenesis-2.0-Karta-Postaci.pdf</i> oraz w dzienniku „Podręcznik Gracza (PDF)” w Foundry.</p>')

# ---------- CSS ----------
CSS = f"""
@page {{ size: A4; margin: 18mm 17mm 20mm 17mm; @bottom-center {{ content: counter(page); font: 9pt Inter; color: #7a6a58; }} }}
@page :first {{ margin: 0; @bottom-center {{ content: none; }} }}
* {{ box-sizing: border-box; }}
html {{ -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
body {{ font-family: Lora, 'DejaVu Serif', serif; font-size: 10.2pt; line-height: 1.5; color: #241d17; margin: 0; }}
h1, h2, h3, h4, .kicker, .c-top, .c-title, .c-sub, th, .pg-tag, .motto, .caption {{ font-family: Inter, 'DejaVu Sans', sans-serif; }}
h2 {{ font-size: 15pt; color: #7b1e12; margin: 16pt 0 5pt; padding-bottom: 3pt; border-bottom: 1.2pt solid #c9b79c; letter-spacing: .02em; break-after: avoid; }}
h4 {{ font-size: 10pt; margin: 9pt 0 3pt; color: #3a2d22; text-transform: uppercase; letter-spacing: .06em; break-after: avoid; }}
p {{ margin: 0 0 6pt; text-align: justify; hyphens: auto; }}
ul, ol {{ margin: 0 0 7pt; padding-left: 15pt; }} li {{ margin-bottom: 2.5pt; }}
.lead {{ font-size: 11.2pt; font-style: italic; color: #3d3127; }}
.note {{ font-size: 9.4pt; color: #5b4a3b; border-left: 2.5pt solid #b33a24; padding: 2pt 0 2pt 8pt; }}
.box {{ background: #f1e8da; border: 0.8pt solid #d8c6aa; border-radius: 3pt; padding: 7pt 10pt; margin: 8pt 0; break-inside: avoid; }}
.box h4 {{ margin-top: 0; color: #7b1e12; }}
table {{ width: 100%; border-collapse: collapse; margin: 4pt 0 9pt; font-size: 9.4pt; break-inside: avoid; }}
th {{ text-align: left; background: #3a2d22; color: #f4ead8; font-weight: 600; padding: 3pt 6pt; font-size: 8.8pt; }}
td {{ padding: 3pt 6pt; border-bottom: 0.5pt solid #ddd0bb; vertical-align: top; }}
tr:nth-child(even) td {{ background: #f7f1e7; }}
table.kv th {{ width: 30%; background: #ece1cf; color: #3a2d22; border-bottom: 0.5pt solid #ddd0bb; }}
table.small {{ font-size: 8.6pt; }} td.num {{ font-family: Inter; color: #7b1e12; font-weight: 700; }}
.two {{ display: grid; grid-template-columns: 1fr 1fr; gap: 14pt; }}
.part {{ break-before: page; break-after: page; height: 245mm; display: flex; flex-direction: column; justify-content: center; align-items: flex-start;
  background: linear-gradient(180deg, transparent 0, transparent 60%, #f1e8da 60%); padding-left: 6mm; border-left: 4pt solid #7b1e12; }}
.part h1 {{ font-size: 40pt; margin: 0; color: #241d17; letter-spacing: .04em; text-transform: uppercase; }}
.part .kicker {{ font-size: 11pt; letter-spacing: .3em; text-transform: uppercase; color: #7b1e12; margin-bottom: 6pt; }}
.cover {{ height: 297mm; width: 210mm; background: radial-gradient(ellipse at 50% 30%, #4a2a1d 0, #1b1410 70%); color: #efe3cf; display: flex; }}
.cover-in {{ margin: auto; width: 170mm; text-align: center; }}
.c-top {{ letter-spacing: .35em; text-transform: uppercase; font-size: 9pt; color: #c9a77f; }}
.c-title {{ font-size: 62pt; font-weight: 800; letter-spacing: .12em; margin-top: 30mm; line-height: 1; }}
.c-title span {{ display: block; font-size: 30pt; color: #d0492f; letter-spacing: .3em; margin-top: 4mm; }}
.c-sub {{ font-size: 18pt; letter-spacing: .25em; text-transform: uppercase; margin-top: 10mm; }}
.c-line {{ width: 40mm; height: 1.5pt; background: #d0492f; margin: 8mm auto; }}
.c-desc {{ font-size: 11.5pt; color: #d9c8ad; }}
.c-port {{ display: flex; justify-content: center; gap: 2.5mm; margin-top: 22mm; }}
.c-port img {{ width: 21mm; height: 28mm; object-fit: cover; border: 0.8pt solid #8a6a4c; filter: sepia(.25) contrast(1.05); }}
.c-foot {{ margin-top: 20mm; font-style: italic; color: #c9a77f; font-size: 11pt; }}
.toc {{ break-before: page; }} .toc h2 {{ border: 0; font-size: 22pt; color: #241d17; }}
.toc .l1 {{ font-family: Inter; font-weight: 700; margin-top: 8pt; text-transform: uppercase; font-size: 9.5pt; letter-spacing: .08em; color: #7b1e12; }}
.toc div {{ display: flex; }} .toc .l2 {{ padding-left: 10pt; font-size: 9.6pt; }}
.toc .dots {{ flex: 1; border-bottom: 0.6pt dotted #a89276; margin: 0 4pt 4pt; }}
.toc a {{ color: inherit; text-decoration: none; }}
.region, .cult {{ break-inside: avoid; }}
.motto {{ color: #7b1e12; font-size: 9pt; letter-spacing: .2em; text-transform: uppercase; margin: -3pt 0 5pt; }}
.meta {{ font-size: 8.8pt; background: #f1e8da; padding: 5pt 8pt; margin-bottom: 10pt; }}
.cdesc {{ font-weight: 600; }} .flav {{ font-style: italic; color: #4e3f33; }}
.example {{ background: #f1e8da; padding: 8pt 12pt; border-left: 3pt solid #3a2d22; font-size: 9.6pt; break-inside: avoid; }}
.attgrid {{ display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 6pt; }}
.att {{ background: #f1e8da; padding: 5pt 8pt; }} .att h4 {{ margin-top: 0; color: #7b1e12; }} .att p {{ font-size: 9pt; margin: 0; }}
.steps {{ padding-left: 21pt; }} .steps li {{ margin-bottom: 4pt; }}
.pregen {{ break-inside: avoid; margin-bottom: 8pt; }}
.pregen h2 {{ margin-top: 10pt; }}
.pg-in {{ display: grid; grid-template-columns: 36mm 1fr; gap: 10pt; }}
.pg-in img {{ width: 36mm; height: 48mm; object-fit: cover; border: 0.8pt solid #8a6a4c; }}
.pg-in p {{ font-size: 9.4pt; margin-bottom: 4pt; }}
.pg-tag {{ font-size: 8.6pt; color: #7b1e12; text-transform: uppercase; letter-spacing: .08em; margin-bottom: 3pt; }}
.readaloud {{ background: #241d17; color: #efe3cf; padding: 12pt 16pt; font-style: italic; font-size: 11pt; border-left: 4pt solid #d0492f; margin: 6pt 0 10pt; }}
.readaloud p {{ margin-bottom: 7pt; }}
img.map {{ width: 100%; border: 0.8pt solid #8a6a4c; }}
.caption {{ font-size: 8.6pt; color: #6a5948; text-align: center; }}
.faces {{ display: grid; grid-template-columns: repeat(5, 1fr); gap: 6pt; break-inside: avoid; }}
.face img {{ width: 100%; height: 40mm; object-fit: cover; border: 0.8pt solid #8a6a4c; }}
.face b {{ font-family: Inter; font-size: 9pt; display: block; margin-top: 2pt; }} .face p {{ font-size: 8.4pt; text-align: left; line-height: 1.35; }}
.tagline {{ font-size: 12pt; font-style: italic; text-align: center; color: #7b1e12; margin-top: 14pt; }}
.gl th {{ width: 28%; background: #ece1cf; color: #3a2d22; }}
h2.cheat {{ break-before: page; }}
.cheat p, .cheat td {{ font-size: 8.9pt; }} .cheat h4 {{ color: #7b1e12; }}
"""

def render(toc_pages=None):
    toc = '<section class="toc"><h2>Spis treści</h2>'
    for lvl, t, i in TOC:
        pg = (toc_pages or {}).get(i, "")
        toc += f'<div class="l{lvl}"><a href="#{i}">{t}</a><span class="dots"></span><span>{pg}</span></div>'
    toc += "</section>"
    doc = f'<!DOCTYPE html><html lang="pl"><head><meta charset="utf-8"><title>Degenesis 2.0 — Podręcznik Gracza</title><style>{CSS}</style></head><body>' + "\n".join(body).replace("@@TOC@@", toc) + "</body></html>"
    open(f"{OUT}/book.html", "w", encoding="utf-8").write(doc)
    subprocess.run(["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--allow-file-access-from-files",
                    "--no-pdf-header-footer", f"--print-to-pdf={OUT}/book.pdf", f"file://{OUT}/book.html"], check=True, capture_output=True)

render({i: "00" for _, _, i in TOC})
# 2. przebieg: znajdź strony nagłówków
import pdfplumber
pages = {}
with pdfplumber.open(f"{OUT}/book.pdf") as pdf:
    texts = [p.extract_text() or "" for p in pdf.pages]
toc_end = 3
for lvl, t, i in TOC:
    key = t.upper() if lvl == 1 else t
    for n, tx in enumerate(texts):
        if n < toc_end: continue
        norm = lambda x: re.sub(r"[„”\"“\u02ee]", "", x).strip()
        lines = [norm(l) for l in tx.splitlines()]
        if norm(key) in lines or (lvl == 1 and t.upper() in tx.upper().splitlines()):
            pages[i] = n + 1; break
render(pages)
print(len(texts), "stron;", sum(1 for v in pages.values() if v), "/", len(TOC), "nagłówków znalezionych")
missing = [t for _, t, i in TOC if i not in pages]
print("brak:", missing)
# 3. karta postaci na końcu
subprocess.run(["python3", "-I", f"{OUT}/karta.py"], check=True)
subprocess.run(["qpdf", "--empty", "--pages", f"{OUT}/book.pdf", f"{OUT}/karta.pdf", "--", f"{OUT}/book_full.pdf"], check=True)
os.replace(f"{OUT}/book_full.pdf", f"{OUT}/book.pdf")
print("z kartą:", len(__import__("pypdf").PdfReader(f"{OUT}/book.pdf").pages), "stron")

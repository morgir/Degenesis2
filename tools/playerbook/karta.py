# -*- coding: utf-8 -*-
"""Karta postaci Degenesis 2.0 do druku (2 strony A4) -> karta.pdf"""
import subprocess
OUT = "/home/claude/playerbook"

ATTRS = [
 ("Ciało", ["Atletyka", "Bijatyka", "Siła", "Broń biała", "Kondycja", "Twardość"]),
 ("Zręczność", ["Rzemiosło", "Zwinne palce", "Prowadzenie", "Mobilność", "Strzelectwo", "Skradanie"]),
 ("Charyzma", ["Sztuka", "Obycie", "Ekspresja", "Przywództwo", "Negocjacje", "Uwodzenie"]),
 ("Intelekt", ["Artefakty", "Inżynieria", "Skupienie", "Legendy", "Medycyna", "Nauka"]),
 ("Psyche", ["Spryt", "Oszustwo", "Dominacja", "Wiara", "Refleks", "Wola"]),
 ("Instynkt", ["Empatia", "Orientacja", "Percepcja", "Pierwotność", "Przetrwanie", "Oswajanie"]),
]
PAIRS = {"Skupienie": "para z Pierwotnością", "Pierwotność": "para ze Skupieniem",
         "Wiara": "para z Wolą", "Wola": "para z Wiarą"}
BGS = ["Sojusznicy", "Autorytet", "Sława", "Zasoby", "Sekrety", "Sieć"]

def boxes(n, cls="bx"):
    return "".join(f'<span class="{cls}"></span>' for _ in range(n))

def attr_block(name, skills):
    rows = ""
    for s in skills:
        mark = ' <span class="pair" title="">⇄</span>' if s in PAIRS else ""
        rows += f'<tr><td class="st">☆</td><td class="sn">{s}{mark}</td><td class="v"></td><td class="m"></td><td class="p"></td></tr>'
    return f'''<div class="attr">
<div class="ah"><span class="an">{name}</span><span class="lab">☆</span><span class="sq sm"></span><span class="lab">maks.</span><span class="sq sm"></span><span class="lab">wartość</span><span class="sq big"></span></div>
<table class="sk"><tr><th>☆</th><th>Umiejętność</th><th>wart.</th><th>maks.</th><th>pula</th></tr>{rows}</table></div>'''

def lines(n):
    return "".join('<div class="ln"></div>' for _ in range(n))

page1 = f'''<section class="page">
<header><div class="logo">DEGENESIS <b>2.0</b></div><div class="ttl">Karta postaci</div></header>
<div class="id">
 <div class="f w2"><label>Imię</label></div><div class="f"><label>Gracz</label></div>
 <div class="f"><label>Kultura</label></div><div class="f"><label>Koncept (Arkan)</label></div><div class="f"><label>Kult</label></div>
 <div class="f"><label>Ranga (poziom)</label></div><div class="f"><label>Wiek · płeć</label></div><div class="f w4"><label>Wygląd, znaki szczególne</label></div>
</div>
<div class="grid">{"".join(attr_block(a, s) for a, s in ATTRS)}</div>
<p class="hint">☆ = liczba bonusów (Kultura, Koncept, Kult). Limit przy tworzeniu: atrybut 3 + ☆, umiejętność 2 + ☆. Pula = atrybut + umiejętność.
⇄ = para Ścieżki: Skupienie/Pierwotność i Wiara/Wola. Jedną z każdej pary skreśl, zostaje na 0.</p>
<div class="row3">
 <div class="card"><h3>Ego</h3><div class="kv"><span>maks. = (Intelekt + Skupienie) ×2<br>albo (Instynkt + Pierwotność) ×2</span><span class="sq big"></span></div>{boxes(24, "tick")}
  <p class="tiny">1 Ego: +1K (maks. 3 na rzut) · aktywna obrona 1 · rana o stopień lżej 2 · przerzut porażek 3</p></div>
 <div class="card"><h3>Zarażenie</h3><div class="kv"><span>maks. = (Psyche + Wiara/Wola) ×2</span><span class="sq big"></span></div>{boxes(24, "tick")}
  <p class="tiny">Zaznacz trwałe kółkiem. Połowa skali: stygmat. Trwałe do połowy: Leperos.</p></div>
 <div class="card"><h3>Rany</h3><div class="kv"><span>Próg = Ciało + Twardość</span><span class="sq big"></span></div>
  <div class="wr"><span>Lekka (&lt; Próg)</span><span>{boxes(3)}</span></div>
  <div class="wr"><span>Poważna (≥ Próg) −1K</span><span>{boxes(2)}</span></div>
  <div class="wr"><span>Krytyczna (≥ 2×Próg) −2K</span><span>{boxes(1)}</span></div>
  <div class="kv"><span>Obrona (1 + osłona, ruch, teren)</span><span class="sq"></span></div></div>
</div>
</section>'''

wrows = "".join('<tr>' + '<td></td>' * 7 + '</tr>' for _ in range(5))
prows = "".join('<tr><td></td><td></td><td></td></tr>' for _ in range(4))
brows = "".join(f'<tr><td>{b}</td><td class="c"></td><td class="c"></td></tr>' for b in BGS)

page2 = f'''<section class="page">
<header><div class="logo">DEGENESIS <b>2.0</b></div><div class="ttl">Karta postaci · str. 2</div></header>
<div class="row2">
 <div class="card"><h3>Zaplecze</h3><table class="t"><tr><th>Zaplecze</th><th>poziom</th><th>wykorzystane</th></tr>{brows}</table>
  <p class="tiny">Start: 4 punkty, maks. 3 w jednym. +1K na poziom do pasujących rzutów albo Wykorzystanie (przysługa).</p></div>
 <div class="card"><h3>Potencjały</h3><table class="t"><tr><th style="width:38%">Nazwa</th><th style="width:10%">poz.</th><th>Efekt</th></tr>{prows}</table>
  <p class="tiny">Start: 1 Potencjał na poziomie 1 (kultowy albo ogólny).</p></div>
</div>
<div class="card"><h3>Broń</h3><table class="t"><tr><th style="width:24%">Nazwa</th><th>Umiejętność</th><th>Poręcz.</th><th>Obrażenia</th><th>Strefa</th><th>Mag.</th><th style="width:26%">Cechy</th></tr>{wrows}</table>
 <p class="tiny">Strefy: Zwarcie · Blisko · Daleko · Poza zasięgiem. Tura: akcja + 1 strefa; bieg o 2 strefy = cała tura, +1 Obrony. F (Siła) = Ciało + Siła.</p></div>
<div class="row2">
 <div class="card"><h3>Pancerz i ekwipunek</h3><div class="kv"><span>Pancerz</span><span class="sq"></span></div>{lines(7)}<div class="kv"><span>Pieniądze = (poziom rangi + Zasoby) × stawka kultu</span><span class="sq wide"></span></div></div>
 <div class="card"><h3>Człowiek</h3>
  <label>Ambicja</label>{lines(1)}<label>Tajemnica</label>{lines(1)}<label>Cień Konceptu</label>{lines(1)}
  <label>Więzi</label>{lines(2)}<div class="kv"><span>Archetyp użyty w tej sesji (+2K)</span><span class="bx"></span></div></div>
</div>
<div class="row2">
 <div class="card"><h3>Długi</h3><table class="t"><tr><th>Komu / kto mi</th><th>za co</th><th>waga</th></tr>{"".join('<tr><td></td><td></td><td></td></tr>' for _ in range(3))}</table>
  <label>Blizny (maks. 3)</label>{lines(1)}</div>
 <div class="card"><h3>Doświadczenie (PD)</h3><div class="kv"><span>Zdobyte</span><span class="sq wide"></span></div><div class="kv"><span>Wydane</span><span class="sq wide"></span></div>
  <p class="tiny">Atrybut: nowa wartość ×12 (☆ ×10). Umiejętność: nowa wartość ×5 (☆ ×4). Potencjał: suma poziomów ×10.</p>
  <label>Notatki</label>{lines(3)}</div>
</div>
<div class="check"><b>Tworzenie w skrócie:</b> Kultura, Koncept, Kult (☆) → Ścieżka → atrybuty 1 + 10 pkt (suma 16) → umiejętności 0 + 28 pkt → Zaplecze 4 pkt → ranga → 1 Potencjał → Ego, Zarażenie, Próg, pieniądze → Ambicja, Tajemnica, Więzi. Punkty wydajesz 1:1.</div>
</section>'''

CSS = """
@page { size: A4; margin: 0; }
* { box-sizing: border-box; }
body { margin: 0; font-family: Inter, 'DejaVu Sans', sans-serif; color: #241d17; font-size: 8.2pt; }
.page { width: 210mm; height: 297mm; padding: 10mm 10mm 8mm; page-break-after: always; display: flex; flex-direction: column; gap: 3.2mm; overflow: hidden; }
.page:last-child { page-break-after: auto; }
header { display: flex; justify-content: space-between; align-items: baseline; border-bottom: 1.4pt solid #7b1e12; padding-bottom: 1.5mm; }
.logo { font-family: Lora, serif; font-size: 17pt; letter-spacing: .12em; color: #241d17; } .logo b { color: #7b1e12; }
.ttl { font-size: 10pt; text-transform: uppercase; letter-spacing: .14em; color: #7b1e12; }
.id { display: grid; grid-template-columns: repeat(4, 1fr); gap: 2mm 3mm; }
.f { border-bottom: .7pt solid #8a7a66; height: 8.5mm; position: relative; } .f.w2 { grid-column: span 2; } .f.w4 { grid-column: span 4; }
label, .f label { font-size: 6.4pt; text-transform: uppercase; letter-spacing: .08em; color: #7a6a58; display: block; margin-top: 1mm; }
.grid { display: grid; grid-template-columns: 1fr 1fr; gap: 3mm 4mm; }
.attr { border: .9pt solid #3a2d22; border-radius: 1.5mm; padding: 1.6mm 2mm; }
.ah { display: flex; align-items: center; gap: 1.4mm; border-bottom: .9pt solid #3a2d22; padding-bottom: 1.2mm; margin-bottom: .8mm; }
.an { font-size: 11pt; font-weight: 700; text-transform: uppercase; letter-spacing: .08em; color: #7b1e12; flex: 1; }
.lab { font-size: 6.2pt; text-transform: uppercase; color: #7a6a58; }
.sq { display: inline-block; width: 9mm; height: 7mm; border: .9pt solid #3a2d22; border-radius: 1mm; background: #fff; flex: none; }
.sq.sm { width: 6mm; height: 6mm; } .sq.big { width: 11mm; height: 9mm; border-width: 1.3pt; } .sq.wide { width: 24mm; }
table { border-collapse: collapse; width: 100%; }
.sk th { font-size: 6pt; font-weight: 600; text-transform: uppercase; color: #7a6a58; text-align: center; padding: .3mm; }
.sk th:nth-child(2) { text-align: left; }
.sk td { height: 6.1mm; border-bottom: .5pt solid #c9b79c; }
.sk td.st { width: 5mm; color: #b8a58c; text-align: center; font-size: 8pt; }
.sk td.sn { font-size: 8.6pt; }
.sk td.v, .sk td.m, .sk td.p { width: 9.5mm; border-left: .5pt solid #c9b79c; }
.sk td.p { background: #f3ece1; }
.pair { color: #7b1e12; font-size: 7.5pt; }
.hint { font-size: 7pt; color: #5b4a3b; margin: 0; line-height: 1.35; }
.row3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 3mm; flex: 1; }
.row2 { display: grid; grid-template-columns: 1fr 1fr; gap: 3mm; }
.card { border: .9pt solid #3a2d22; border-radius: 1.5mm; padding: 2mm 2.4mm; }
.card h3 { margin: 0 0 1.4mm; font-size: 9pt; text-transform: uppercase; letter-spacing: .1em; color: #7b1e12; }
.kv { display: flex; justify-content: space-between; align-items: center; gap: 2mm; margin: 1mm 0; font-size: 7.4pt; color: #3a2d22; }
.tick { display: inline-block; width: 5.2mm; height: 5.2mm; border: .7pt solid #3a2d22; border-radius: 50%; margin: .6mm .5mm 0 0; }
.bx { display: inline-block; width: 5.5mm; height: 5.5mm; border: .9pt solid #3a2d22; margin-left: 1.2mm; flex: none; }
.wr { display: flex; justify-content: space-between; align-items: center; margin: 1.3mm 0; font-size: 7.6pt; }
.tiny { font-size: 6.6pt; color: #5b4a3b; margin: 1.4mm 0 0; line-height: 1.35; }
.t th { font-size: 6.4pt; text-transform: uppercase; color: #7a6a58; text-align: left; font-weight: 600; border-bottom: .8pt solid #3a2d22; padding: .5mm 1mm; }
.t td { height: 7mm; border-bottom: .5pt solid #c9b79c; padding: 0 1mm; font-size: 8.4pt; }
.t td + td { border-left: .5pt solid #e0d4c2; } .t td.c { width: 22mm; }
.ln { border-bottom: .6pt solid #b8a58c; height: 6.2mm; }
.check { font-size: 7.4pt; background: #f3ece1; border-left: 2.5pt solid #7b1e12; padding: 2mm 3mm; margin-top: auto; line-height: 1.4; }
"""

doc = f'<!DOCTYPE html><html lang="pl"><head><meta charset="utf-8"><title>Degenesis 2.0 — Karta postaci</title><style>{CSS}</style></head><body>{page1}{page2}</body></html>'
open(f"{OUT}/karta.html", "w", encoding="utf-8").write(doc)
subprocess.run(["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                f"--print-to-pdf={OUT}/karta.pdf", f"file://{OUT}/karta.html"], check=True, capture_output=True)
print("karta.pdf")

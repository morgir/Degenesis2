# -*- coding: utf-8 -*-
"""Stylizowane portrety-sylwetki i tokeny (SVG -> WebP)."""
import os, re

BUST = "M120 800 C120 650 190 585 300 570 C410 585 480 650 480 800 Z"
HEAD = '<ellipse cx="300" cy="420" rx="92" ry="112"/>'
NECK = '<rect x="262" y="500" width="76" height="90" rx="20"/>'

GEAR = {
 "bald": "",
 "hat": '<ellipse cx="300" cy="330" rx="175" ry="32"/><path d="M215 330 Q220 230 300 225 Q380 230 385 330Z"/>',
 "scarf": '<path d="M200 430 Q195 300 300 290 Q405 300 400 430 Q420 520 380 560 L360 470 Q300 330 240 470 L220 560 Q180 520 200 430Z"/>',
 "hood": '<path d="M180 470 Q170 290 300 280 Q430 290 420 470 L440 600 L160 600Z"/>',
 "mohawk": '<path d="M285 300 L300 230 L315 300 L330 240 L330 315 L270 315 L270 240Z"/><path d="M200 380 L120 330 L210 410Z M400 380 L480 330 L390 410Z"/>',
 "goggles": '<path d="M215 360 Q300 330 385 360 L385 385 Q300 360 215 385Z"/><circle cx="260" cy="395" r="28" fill="#c27b3a" fill-opacity=".55"/><circle cx="340" cy="395" r="28" fill="#c27b3a" fill-opacity=".55"/>',
 "gasmask": '<path d="M230 430 Q300 520 370 430 L360 480 Q300 560 240 480Z"/><circle cx="300" cy="505" r="26"/>',
 "feathers": '<path d="M150 600 L110 520 L175 560 L150 470 L215 540 L215 470 L260 560 Z M450 600 L490 520 L425 560 L450 470 L385 540 L385 470 L340 560Z"/>',
 "collar": '<path d="M210 590 L240 520 L300 560 L360 520 L390 590 Z"/>',
 "helmet": '<path d="M195 400 Q190 280 300 270 Q410 280 405 400 L420 410 L180 410Z"/><rect x="230" y="360" width="140" height="14" rx="6"/>',
 "dots": '<circle cx="270" cy="345" r="9" fill="#d9c8a0"/><circle cx="300" cy="338" r="9" fill="#d9c8a0"/><circle cx="330" cy="345" r="9" fill="#d9c8a0"/>',
 "mask": '<path d="M215 380 Q300 340 385 380 L380 470 Q300 520 220 470Z"/>',
}

SYMBOL = {
 "spital": '<circle r="38" fill="none" stroke-width="8"/><path d="M0 -26V26M-26 0H26" stroke-width="10"/>',
 "judge": '<path d="M-26 -18H26V-2H-26Z M-4 -2H4V34H-4Z" stroke-width="2"/>',
 "apoc": '<path d="M-34 10 Q0 -40 34 10 Q10 0 0 30 Q-10 0 -34 10Z" stroke-width="2"/>',
 "scrap": '<path d="M-24 -30 L0 30 L24 -30 M-30 0 H30" fill="none" stroke-width="8"/>',
 "chron": '<polygon points="0,-36 31,-18 31,18 0,36 -31,18 -31,-18" fill="none" stroke-width="7"/><path d="M-14 -10V10M-6 -10V10M2 -10V10M10 -10V10" stroke-width="4"/>',
 "hellv": '<path d="M-34 24 L-10 -22 L4 4 L14 -10 L34 24Z" stroke-width="2"/>',
 "anab": '<path d="M0 -36 Q22 -6 10 16 Q22 8 18 -6 Q34 18 0 36 Q-34 18 -18 -6 Q-22 8 -10 16 Q-22 -6 0 -36Z" stroke-width="2"/>',
 "none": '<circle r="10"/>',
}

def portrait_svg(name, subtitle, gear, color, accent, symbol, eyes=None):
    gear_svg = "".join(GEAR[g] for g in gear)
    eye = ""
    if eyes:
        eye = f'<circle cx="262" cy="410" r="9" fill="{eyes}"/><circle cx="338" cy="410" r="9" fill="{eyes}"/>'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="600" height="800" viewBox="0 0 600 800">
<defs>
 <radialGradient id="bg" cx="50%" cy="38%" r="70%"><stop offset="0" stop-color="{accent}"/><stop offset="1" stop-color="#0b0a09"/></radialGradient>
 <filter id="grain"><feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="2" seed="4"/><feColorMatrix type="saturate" values="0"/>
  <feComponentTransfer><feFuncA type="table" tableValues="0 0.22"/></feComponentTransfer><feComposite in2="SourceGraphic" operator="in"/></filter>
 <filter id="rim"><feMorphology operator="dilate" radius="3" in="SourceAlpha" result="d"/><feFlood flood-color="{accent}" flood-opacity=".7"/><feComposite in2="d" operator="in" result="r"/>
  <feGaussianBlur in="r" stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<rect width="600" height="800" fill="url(#bg)"/>
<g fill="none" stroke="{color}" stroke-opacity=".25" stroke-width="2">{''.join(f'<circle cx="300" cy="380" r="{r}"/>' for r in range(140, 420, 34))}</g>
<g filter="url(#rim)" fill="#0d0c0b"><path d="{BUST}"/>{NECK}{HEAD}</g><g fill="#2c2824" stroke="{color}" stroke-opacity=".45" stroke-width="3">{gear_svg}</g>
{eye}
<g transform="translate(300 690)" fill="{color}" stroke="{color}">{SYMBOL[symbol]}</g>
<rect width="600" height="800" fill="#000" filter="url(#grain)"/>
<rect x="14" y="14" width="572" height="772" fill="none" stroke="{color}" stroke-width="4"/>
<rect x="0" y="735" width="600" height="65" fill="#0b0a09" opacity=".85"/>
<text x="300" y="770" font-family="DejaVu Serif" font-size="34" font-weight="bold" fill="#efe6d2" text-anchor="middle">{name}</text>
<text x="300" y="792" font-family="DejaVu Serif" font-size="17" fill="{color}" text-anchor="middle">{subtitle}</text>
</svg>'''

def token_svg(portrait_inner_id, color):
    return None  # tokeny robimy z portretu (wycinek + ramka) w PIL

CHARS = {
 # klucz: (imię, podpis, gear, kolor ramki, akcent tła, symbol, oczy)
 "wera": ("Siostra Wera", "Spitalianka · Famulancer", ["bald", "collar"], "#d9d2c3", "#31403f", "spital", None),
 "oddo": ("Oddo", "Sędzia miejski", ["hat", "collar"], "#c9a35a", "#3b2c1c", "judge", None),
 "sroka": ("Kasia „Sroka”", "Apokaliptyczka · Sroka", ["mohawk", "feathers"], "#b4373a", "#3a1a22", "apoc", "#e7c75a"),
 "borsuk": ("Mirek „Borsuk”", "Złomiarz · Borsuk", ["hood", "goggles"], "#c27b3a", "#33291b", "scrap", None),
 "modus": ("Modus", "Kronikarz · Agent", ["hood", "mask"], "#58c3c9", "#16272b", "chron", "#7ff3ff"),
 "anja": ("Kapral Anja Reiss", "Hellwetka · Kapral", ["helmet", "collar"], "#8fa36a", "#1f261a", "hellv", None),
 "kaspar": ("Brat Kaspar", "Anabaptysta · Orgiasta", ["bald", "dots"], "#d48a3a", "#33200f", "anab", "#f0b04a"),
 "halka": ("Halka", "przekupka z targu", ["scarf"], "#a99a7c", "#2f2a22", "none", None),
 "varga": ("Sędzia Varga", "Sędzia miejski", ["hat", "collar"], "#8a6a2c", "#251d14", "judge", "#c9a35a"),
 "ilsa": ("Ilsa Kruczyca", "Kruk Kruczego Stada", ["feathers", "scarf"], "#7a2a3a", "#1d1418", "apoc", "#e04a4a"),
 "kessel": ("Higienista Kessel", "Spitalianin", ["bald", "gasmask", "collar"], "#9fb0b3", "#1f2a2c", "spital", None),
 "tobiasz": ("Brat Tobiasz", "Famulancer z lazaretu", ["bald", "collar"], "#c8c1b3", "#2b3433", "spital", None),
 "tragarze": ("Tragarze Kruków", "banda", ["hood"], "#7a5a3a", "#221a12", "apoc", "#b08a4a"),
}

if __name__ == "__main__":
    os.makedirs("/tmp/portraits", exist_ok=True)
    for k, (n, sub, gear, col, acc, sym, eyes) in CHARS.items():
        open(f"/tmp/portraits/{k}.svg", "w").write(portrait_svg(n, sub, gear, col, acc, sym, eyes))
    print("ok")

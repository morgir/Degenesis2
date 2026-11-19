# -*- coding: utf-8 -*-
"""Mapy przygody „Ciche studnie” rysowane w SVG i renderowane do WebP."""
import random, math, os

OUT = "/home/claude/degenesis2/assets/maps"
G = 70  # px na kratkę (1 m)

DEFS = """
<defs>
 <filter id="grain" x="0" y="0" width="100%" height="100%">
  <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="7" result="n"/>
  <feColorMatrix type="saturate" values="0"/>
  <feComponentTransfer><feFuncA type="table" tableValues="0 0.18"/></feComponentTransfer>
  <feComposite in2="SourceGraphic" operator="in"/>
 </filter>
 <filter id="stain"><feTurbulence type="fractalNoise" baseFrequency="0.012" numOctaves="4" seed="3"/>
  <feColorMatrix values="0 0 0 0 0.25  0 0 0 0 0.18  0 0 0 0 0.10  0 0 0 0.55 0"/></filter>
 <filter id="rough"><feTurbulence type="fractalNoise" baseFrequency="0.04" numOctaves="2" seed="9" result="t"/>
  <feDisplacementMap in="SourceGraphic" in2="t" scale="5"/></filter>
 <filter id="shadow"><feDropShadow dx="4" dy="5" stdDeviation="4" flood-color="#000" flood-opacity="0.55"/></filter>
 <pattern id="cobble" width="44" height="40" patternUnits="userSpaceOnUse">
  <rect width="44" height="40" fill="#5c564c"/>
  <path d="M2 2h18v16H2zM24 2h18v16H24zM-9 22h18v16H-9zM13 22h18v16H13zM35 22h18v16H35z" fill="#6f685c" stroke="#3d3830" stroke-width="2"/>
 </pattern>
 <pattern id="planks" width="70" height="24" patternUnits="userSpaceOnUse">
  <rect width="70" height="24" fill="#5b4430"/><path d="M0 23.5h70M40 0v24" stroke="#33261a" stroke-width="2"/>
  <path d="M5 8h28M45 15h20" stroke="#6c533b" stroke-width="2"/>
 </pattern>
 <pattern id="tiles" width="35" height="35" patternUnits="userSpaceOnUse">
  <rect width="35" height="35" fill="#b9b2a3"/><path d="M0 34.5h35M34.5 0v35" stroke="#8e877a" stroke-width="2"/>
 </pattern>
 <pattern id="stone" width="60" height="30" patternUnits="userSpaceOnUse">
  <rect width="60" height="30" fill="#4a4741"/><path d="M0 29.5h60M30 0v15M0 15h60M15 15v15M45 15v15" stroke="#2f2d29" stroke-width="2"/>
 </pattern>
 <pattern id="dirt" width="200" height="200" patternUnits="userSpaceOnUse">
  <rect width="200" height="200" fill="#6b5b45"/><rect width="200" height="200" filter="url(#stain)"/>
 </pattern>
 <pattern id="roof" width="30" height="16" patternUnits="userSpaceOnUse">
  <rect width="30" height="16" fill="#463a31"/><path d="M0 15.5h30M15 0v8M0 8h30" stroke="#2c241e" stroke-width="2"/>
 </pattern>
 <radialGradient id="vign" cx="50%" cy="50%" r="75%"><stop offset="55%" stop-color="#000" stop-opacity="0"/><stop offset="100%" stop-color="#000" stop-opacity="0.65"/></radialGradient>
 <radialGradient id="lamp" r="50%"><stop offset="0" stop-color="#ffcf7a" stop-opacity=".55"/><stop offset="1" stop-color="#ffcf7a" stop-opacity="0"/></radialGradient>
 <radialGradient id="spore" r="50%"><stop offset="0" stop-color="#e8f0c8" stop-opacity=".55"/><stop offset="1" stop-color="#e8f0c8" stop-opacity="0"/></radialGradient>
</defs>"""

def svg(w, h, body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{DEFS}{body}</svg>'

def R(x, y, w, h, fill, stroke="none", sw=0, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>'

def wall_room(x, y, w, h, floor, wall=14, color="#25211d"):
    """Pokój w kratkach: podłoga + ściany."""
    X, Y, W, H = x * G, y * G, w * G, h * G
    return (R(X, Y, W, H, f"url(#{floor})") +
            R(X, Y, W, H, "none", color, wall, 'filter="url(#rough)"'))

def door(x, y, horizontal=True, size=1):
    X, Y = x * G, y * G
    if horizontal:
        return R(X + 6, Y - 10, size * G - 12, 20, "#6b4a2b", "#2a1d12", 3)
    return R(X - 10, Y + 6, 20, size * G - 12, "#6b4a2b", "#2a1d12", 3)

def gap(x, y, horizontal=True, size=1, floor="planks"):
    X, Y = x * G, y * G
    if horizontal:
        return R(X + 4, Y - 12, size * G - 8, 24, f"url(#{floor})")
    return R(X - 12, Y + 4, 24, size * G - 8, f"url(#{floor})")

def crate(x, y, s=1):
    X, Y = x * G + 6, y * G + 6
    S = s * G - 12
    return (f'<g filter="url(#shadow)">{R(X, Y, S, S, "#7a5a36", "#3b2a18", 4)}'
            f'<path d="M{X} {Y}L{X+S} {Y+S}M{X+S} {Y}L{X} {Y+S}" stroke="#3b2a18" stroke-width="4"/></g>')

def barrel(x, y, r=0.42, mark=False):
    cx, cy = x * G, y * G
    m = f'<circle cx="{cx}" cy="{cy}" r="{r*G*0.35}" fill="#f2f0e6" opacity=".85"/>' if mark else ""
    return (f'<g filter="url(#shadow)"><circle cx="{cx}" cy="{cy}" r="{r*G}" fill="#6a4a2c" stroke="#2e2014" stroke-width="5"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r*G*0.7}" fill="none" stroke="#3d2b1a" stroke-width="3"/>{m}</g>')

def table(x, y, w, h, color="#6e5236"):
    return f'<g filter="url(#shadow)">{R(x*G+8, y*G+8, w*G-16, h*G-16, color, "#2e2014", 4, "rx=\"6\"")}</g>'

def chair(x, y):
    return f'<g filter="url(#shadow)">{R(x*G+20, y*G+20, G-40, G-40, "#4e3a26", "#22180e", 3, "rx=\"4\"")}</g>'

def bed(x, y, vertical=True, blood=False):
    w, h = (1, 2) if vertical else (2, 1)
    b = f'<circle cx="{x*G+w*G*0.55}" cy="{y*G+h*G*0.55}" r="10" fill="#7a1a14" opacity=".7"/>' if blood else ""
    pil = R(x*G+14, y*G+12, w*G-28, 22, "#e8e2d2", "#8a8272", 2, 'rx="6"') if vertical else R(x*G+12, y*G+14, 22, h*G-28, "#e8e2d2", "#8a8272", 2, 'rx="6"')
    return f'<g filter="url(#shadow)">{R(x*G+6, y*G+6, w*G-12, h*G-12, "#cfc6b2", "#5a5244", 3, "rx=\"5\"")}{pil}{b}</g>'

def stall(x, y, w, h, cloth):
    X, Y, W, H = x*G, y*G, w*G, h*G
    stripes = "".join(f'<path d="M{X+i} {Y}V{Y+H}" stroke="#00000033" stroke-width="10"/>' for i in range(10, W, 28))
    return f'<g filter="url(#shadow)">{R(X+4, Y+4, W-8, H-8, cloth, "#1c1712", 4)}{stripes}</g>'

def label(x, y, text, size=40, color="#1d1a16", anchor="middle", weight="bold", stroke=None):
    st = f'stroke="{stroke}" stroke-width="6" paint-order="stroke"' if stroke else ""
    return f'<text x="{x}" y="{y}" font-family="DejaVu Serif" font-size="{size}" font-weight="{weight}" fill="{color}" text-anchor="{anchor}" {st}>{text}</text>'

def grid_overlay(w, h):
    return "".join(f'<path d="M{i*G} 0V{h*G}" stroke="#000" stroke-opacity=".18" stroke-width="1"/>' for i in range(w + 1)) + \
           "".join(f'<path d="M0 {j*G}H{w*G}" stroke="#000" stroke-opacity=".18" stroke-width="1"/>' for j in range(h + 1))

def rubble(rng, n, W, H, color="#3b352d"):
    out = []
    for _ in range(n):
        x, y, r = rng.uniform(0, W), rng.uniform(0, H), rng.uniform(3, 12)
        pts = " ".join(f"{x+math.cos(a)*r*rng.uniform(.6,1.2):.0f},{y+math.sin(a)*r*rng.uniform(.6,1.2):.0f}" for a in [i*math.pi/3 for i in range(6)])
        out.append(f'<polygon points="{pts}" fill="{color}" opacity=".8"/>')
    return "".join(out)

def finish(body, w, h, vign=True):
    W, H = w * G, h * G
    return svg(W, H, body + R(0, 0, W, H, "#000", extra='filter="url(#grain)" opacity=".9"') +
               (R(0, 0, W, H, "url(#vign)") if vign else "") + grid_overlay(w, h))

# --------------------------------------------------------------------------
def map_targ():
    rng = random.Random(11); w, h = 30, 20; W, H = w*G, h*G
    b = R(0, 0, W, H, "url(#cobble)") + R(0, 0, W, H, "url(#dirt)", extra='opacity=".35"')
    # budynki dookoła
    for (x, y, bw, bh) in [(0, 0, 9, 4), (9, 0, 7, 3), (17, 0, 13, 4), (0, 4, 4, 7), (0, 14, 6, 6), (6, 16, 9, 4), (16, 17, 8, 3), (24, 15, 6, 5)]:
        b += R(x*G, y*G, bw*G, bh*G, "url(#roof)", "#1a1511", 10, 'filter="url(#rough)"')
    # brama wschodnia
    b += R(28*G, 6*G, 2*G, 8*G, "url(#stone)", "#151310", 10) + R(28*G, 8.5*G, 2*G, 3*G, "url(#cobble)") + label(29.9*G, 5.6*G, "BRAMA", 34, "#e9e1cf", anchor="end", stroke="#000")
    # studnia
    cx, cy = 15*G, 10*G
    b += f'<circle cx="{cx}" cy="{cy}" r="{2.6*G}" fill="url(#spore)"/>'
    b += f'<g filter="url(#shadow)"><circle cx="{cx}" cy="{cy}" r="{1.3*G}" fill="#4a4741" stroke="#22201c" stroke-width="12"/><circle cx="{cx}" cy="{cy}" r="{0.85*G}" fill="#0d0d0c"/></g>'
    b += f'<path d="M{cx-1.6*G} {cy}H{cx+1.6*G}" stroke="#2a2723" stroke-width="12"/><path d="M{cx-1.2*G} {cy-1.2*G}L{cx+1.2*G} {cy+1.2*G}" stroke="#8a8478" stroke-width="6" stroke-dasharray="14 6"/>'
    b += f'<circle cx="{cx+1.25*G}" cy="{cy+1.25*G}" r="16" fill="#e6e0d0" stroke="#7a1a14" stroke-width="5"/>'  # pieczęć Spitalu
    b += f'<path d="M{cx+1.3*G} {cy+0.2*G}Q{cx+6*G} {cy+0.5*G} {28*G} {cy}" stroke="#2c2721" stroke-width="10" stroke-opacity=".5" stroke-dasharray="30 18" fill="none"/>'  # ślady beczek
    # stragany
    for (x, y, sw, sh, c) in [(6, 5, 3, 2, "#7a2f22"), (10, 4, 3, 2, "#5d6b3a"), (20, 5, 3, 2, "#7b6a3a"), (6, 12, 2, 3, "#3e5468"), (21, 12, 3, 2, "#7a2f22"), (10, 14, 3, 2, "#6b4f6b")]:
        b += stall(x, y, sw, sh, c)
    for (x, y) in [(9, 7), (13, 15), (19, 8), (23, 9)]:
        b += crate(x, y)
    for (x, y) in [(5.5, 8.5), (24.5, 12.5), (25.5, 12.5), (18.5, 15.5)]:
        b += barrel(x, y)
    # wóz
    b += f'<g filter="url(#shadow)">{R(24*G, 3*G+40, 3*G, 1.6*G, "#6b4c2c", "#2a1d12", 6, "rx=\"8\"")}<circle cx="{24.4*G}" cy="{3*G+40}" r="22" fill="#2a1d12"/><circle cx="{26.6*G}" cy="{3*G+40}" r="22" fill="#2a1d12"/><circle cx="{24.4*G}" cy="{4.6*G+40}" r="22" fill="#2a1d12"/><circle cx="{26.6*G}" cy="{4.6*G+40}" r="22" fill="#2a1d12"/></g>'
    b += rubble(rng, 260, W, H)
    for (x, y) in [(4, 11), (27, 5), (16, 3), (12, 17)]:
        b += f'<circle cx="{x*G}" cy="{y*G}" r="{2.2*G}" fill="url(#lamp)"/>'
    return finish(b, w, h)

def map_lazaret():
    rng = random.Random(21); w, h = 28, 18; W, H = w*G, h*G
    b = R(0, 0, W, H, "url(#dirt)")
    b += wall_room(1, 1, 18, 11, "tiles")          # sala chorych
    b += wall_room(19, 1, 8, 6, "tiles")           # sekcja
    b += wall_room(19, 7, 8, 5, "planks")          # biuro
    b += wall_room(1, 12, 12, 5, "tiles")          # kwarantanna
    b += wall_room(13, 12, 14, 5, "stone")         # magazyn / wapno
    b += gap(19, 3, False, 2, "tiles") + gap(19, 9, False, 1, "planks") + gap(6, 12, True, 2, "tiles") + gap(16, 12, True, 2, "stone") + gap(9, 1, True, 3, "tiles")
    for i in range(7):
        b += bed(2 + i*2.3, 2, True, blood=(i == 3)) + bed(2 + i*2.3, 9, True)
    b += table(8, 5.5, 4, 1.5, "#8f8a7c")  # stół z wapnem
    # kwarantanna: zasłony
    b += "".join(f'<path d="M{1*G+20} {(12.8+k*1.4)*G}H{12*G}" stroke="#d8cfb6" stroke-width="10" stroke-dasharray="40 10" opacity=".85"/>' for k in range(3))
    for i in range(4):
        b += bed(2 + i*2.6, 14.6, False)
    # sekcja
    b += f'<g filter="url(#shadow)">{R(21*G, 3*G, 4*G, 1.4*G, "#9da3a6", "#3b4144", 5, "rx=\"6\"")}</g>' + f'<ellipse cx="{23*G}" cy="{3.7*G}" rx="{1.3*G}" ry="{0.35*G}" fill="#b9b0a0"/>'
    b += crate(20, 1) + crate(25, 1) + barrel(26, 5.5)
    # biuro
    b += table(20, 8, 3, 2) + chair(23, 8) + R(25*G, 7.3*G, 1.5*G, 4.4*G, "#4e3a26", "#22180e", 4)
    # magazyn
    for (x, y) in [(14, 13), (15, 13), (14, 14), (22, 13), (23, 13), (24, 15), (25, 15)]:
        b += crate(x, y)
    for (x, y) in [(18.5, 15.5), (19.5, 15.5), (20.5, 15.5)]:
        b += barrel(x, y)
    b += label(10*G, 7.2*G, "SALA CHORYCH", 46, "#3a332a") + label(23*G, 5.8*G, "SEKCJA", 40, "#2c2b28") + label(7*G, 16.6*G, "KWARANTANNA", 40, "#3a332a")
    b += rubble(rng, 80, W, H, "#4b4339")
    return finish(b, w, h)

def map_spelunka():
    rng = random.Random(31); w, h = 26, 18; W, H = w*G, h*G
    b = R(0, 0, W, H, "url(#cobble)") + R(0, 0, W, H, "url(#dirt)", extra='opacity=".5"')
    b += wall_room(1, 1, 16, 12, "planks") + wall_room(17, 1, 8, 7, "stone") + wall_room(17, 8, 8, 5, "planks")
    b += gap(8, 13, True, 2, "planks") + gap(17, 10, False, 1, "planks") + gap(25, 4, False, 2, "stone")
    # kurtyna do magazynu
    b += f'<path d="M{17*G} {2.2*G}V{6.8*G}" stroke="#5a1418" stroke-width="18" stroke-dasharray="22 6"/>'
    # bar
    b += f'<g filter="url(#shadow)">{R(2*G, 2*G, 1.2*G, 8*G, "#3d2a1a", "#160f08", 5)}</g>'
    for k in range(5):
        b += barrel(1.55, 3 + k*1.4, 0.3)
    # scena
    b += f'<g filter="url(#shadow)">{R(11*G, 1.4*G, 5.4*G, 2.6*G, "#4a2f1d", "#1b120a", 6)}</g>' + f'<circle cx="{13.7*G}" cy="{2.7*G}" r="{1.6*G}" fill="url(#lamp)"/>'
    for (x, y) in [(5, 4), (8, 4), (5, 8), (8, 8), (11.5, 6), (12, 9.5)]:
        b += table(x, y, 2, 2) + chair(x - 1, y) + chair(x + 2, y + 1)
    # magazyn: beczki z białym pyłem
    for (x, y, m) in [(18.5, 2.5, 1), (19.5, 2.5, 1), (20.5, 2.5, 0), (18.5, 3.5, 1), (22.5, 5.5, 1), (23.5, 5.5, 0), (23.5, 2.5, 0)]:
        b += barrel(x, y, 0.4, bool(m))
    b += f'<circle cx="{20*G}" cy="{3*G}" r="{1.6*G}" fill="url(#spore)"/>'
    b += crate(21, 6) + crate(22, 6)
    # pokój kapłanki
    b += table(19, 9.5, 3, 2, "#3a2433") + chair(22, 10) + f'<circle cx="{20.5*G}" cy="{10.5*G}" r="{1.4*G}" fill="url(#lamp)"/>'
    b += R(23.3*G, 8.4*G, 1.4*G, 4.2*G, "#2e1d2a", "#140c12", 4)
    # wóz w zaułku
    b += f'<g filter="url(#shadow)">{R(19*G, 14.2*G, 4*G, 1.8*G, "#6b4c2c", "#2a1d12", 6, "rx=\"8\"")}</g>' + barrel(20, 15.1, 0.35, True) + barrel(21, 15.1, 0.35, True) + barrel(22, 15.1, 0.35, True)
    b += label(8.5*G, 12.4*G, "POD ZŁAMANYM SKRZYDŁEM", 40, "#e9e1cf", stroke="#000") + label(21*G, 7.5*G, "MAGAZYN", 34, "#e9e1cf", stroke="#000") + label(21*G, 17.3*G, "ZAUŁEK", 34, "#e9e1cf", stroke="#000")
    b += rubble(rng, 150, W, H)
    return finish(b, w, h)

def map_kancelaria():
    rng = random.Random(41); w, h = 24, 18; W, H = w*G, h*G
    b = R(0, 0, W, H, "url(#cobble)")
    b += wall_room(1, 1, 22, 5, "stone") + wall_room(1, 6, 10, 11, "planks") + wall_room(11, 6, 12, 11, "stone")
    b += gap(10, 1, True, 3, "stone") + gap(5, 6, True, 1, "planks") + gap(16, 6, True, 2, "stone") + gap(11, 12, False, 1, "planks")
    # sala z kolumnami
    for x in [4, 8, 15, 19]:
        b += f'<circle cx="{x*G}" cy="{3.5*G}" r="{0.45*G}" fill="#5e5a52" stroke="#262420" stroke-width="6" filter="url(#shadow)"/>'
    # ławy i podest sędziowski
    for x in [3, 6, 13, 16]:
        b += R(x*G, 2*G, 2.4*G, 0.6*G, "#3b2716", "#160d06", 4, 'filter="url(#shadow)"') + R(x*G, 4.4*G, 2.4*G, 0.6*G, "#3b2716", "#160d06", 4, 'filter="url(#shadow)"')
    b += R(20*G, 1.6*G, 2.6*G, 3.8*G, "#4a3020", "#160d06", 6, 'filter="url(#shadow)"') + f'<circle cx="{21.3*G}" cy="{3.5*G}" r="{1.6*G}" fill="url(#lamp)"/>'
    b += "".join(R(x*G, 1.15*G, 0.6*G, 1.1*G, "#6b1d16", "#2a0b08", 3) for x in [5.5, 9.5, 14.5, 18.5])
    # gabinet: biurko, pulpit z Kodeksem, regały
    b += table(3, 9, 4, 2, "#4a3020") + chair(4.5, 11) + chair(4.5, 7.8)
    b += f'<g filter="url(#shadow)">{R(8*G, 7.3*G, 1.5*G, 1.5*G, "#3b2716", "#160d06", 5)}{R(8.2*G, 7.6*G, 1.1*G, 0.8*G, "#d9cfb7", "#6b6150", 2)}</g>'
    for y in [13, 15]:
        b += R(2*G, y*G, 8*G, 0.8*G, "#3b2716", "#160d06", 4, 'filter="url(#shadow)"') + "".join(R((2.1+i*0.32)*G, (y+0.1)*G, 0.25*G, 0.6*G, rng.choice(["#6b2a1d", "#3a4a2e", "#5a4a2a", "#2f3a4a"])) for i in range(24))
    b += f'<circle cx="{5*G}" cy="{10*G}" r="{2*G}" fill="url(#lamp)"/>'
    # cele
    for i in range(4):
        x = 12 + i * 2.7
        b += R(x*G, 13*G, 2.5*G, 3.6*G, "url(#stone)", "#151310", 8) + "".join(f'<path d="M{(x+0.2+k*0.35)*G} {13*G}V{13.2*G}" stroke="#202020" stroke-width="8"/>' for k in range(6))
    b += table(14, 8, 3, 1.5) + chair(13, 8) + chair(17, 8)  # stół strażników
    b += label(12*G, 3.6*G, "HALA SĄDOWA", 44, "#e9e1cf", stroke="#000") + label(6*G, 12.6*G, "GABINET", 34, "#e9e1cf", stroke="#000") + label(17*G, 12.6*G, "STRAŻNICA I CELE", 34, "#e9e1cf", stroke="#000")
    b += rubble(rng, 60, W, H)
    return finish(b, w, h)

def map_dzielnica():
    """Plan ogólny w stylu atramentu na papierze (bez siatki)."""
    rng = random.Random(51); W, H = 2400, 1600
    b = R(0, 0, W, H, "#d9ccae") + R(0, 0, W, H, "#8a6a3a", extra='filter="url(#stain)" opacity=".55"')
    ink = "#2b2118"
    # mur Justitian
    b += f'<path d="M80 1500 L80 300 Q200 120 600 90 L2300 90 L2300 1500" fill="none" stroke="{ink}" stroke-width="22" filter="url(#rough)"/>'
    for x in range(140, 2300, 180):
        b += R(x, 72, 40, 40, ink)
    # ulice
    for d in ["M80 800 H2300", "M700 90 V1500", "M1500 90 V1500", "M300 400 Q900 520 1500 450 T2300 380", "M300 1200 Q1000 1100 1500 1250 T2300 1150"]:
        b += f'<path d="{d}" fill="none" stroke="#b9a882" stroke-width="46"/><path d="{d}" fill="none" stroke="{ink}" stroke-width="3" stroke-dasharray="2 10" opacity=".6"/>'
    # zabudowa (kreskowane bloki)
    for _ in range(140):
        x, y = rng.uniform(120, 2240), rng.uniform(130, 1460)
        bw, bh = rng.uniform(40, 120), rng.uniform(30, 90)
        b += f'<rect x="{x:.0f}" y="{y:.0f}" width="{bw:.0f}" height="{bh:.0f}" fill="#c8b994" stroke="{ink}" stroke-width="2" opacity=".75" transform="rotate({rng.uniform(-6,6):.1f} {x:.0f} {y:.0f})"/>'
    # kanał
    b += f'<path d="M80 1000 Q600 950 900 1050 T1700 1000 T2300 1060" fill="none" stroke="#5b6f73" stroke-width="30" opacity=".7"/>'
    # brama
    b += R(2270, 700, 60, 200, ink) + label(2250, 670, "Brama Wschodnia", 34, ink, anchor="end")
    locs = [("A", 520, 560, "Lazaret Spitalian"), ("B", 1800, 640, "Targ przy Bramie"), ("C", 1960, 900, "Studnia"),
            ("D", 1100, 1230, "Pod Złamanym Skrzydłem"), ("E", 900, 680, "Domy chorych"), ("F", 1500, 300, "Kancelaria Sędziego Vargi")]
    for k, x, y, name in locs:
        b += f'<circle cx="{x}" cy="{y}" r="34" fill="#7a1a14" stroke="{ink}" stroke-width="4"/>' + label(x, y + 13, k, 36, "#f3ead6")
        b += label(x, y + 72, name, 34, ink, stroke="#d9ccae")
    # róża wiatrów i tytuł
    b += f'<g transform="translate(2120 1380)"><circle r="90" fill="none" stroke="{ink}" stroke-width="4"/><path d="M0 -110 L18 0 L0 110 L-18 0Z" fill="{ink}"/><path d="M-110 0 L0 14 L110 0 L0 -14Z" fill="{ink}" opacity=".6"/>{label(0, -122, "N", 34, ink)}</g>'
    b += label(160, 1560, "JUSTITIAN — DZIELNICA DOSTAWCÓW", 52, ink, anchor="start")
    b += f'<path d="M80 1000 Q600 950 900 1050" fill="none"/>' + label(400, 1020, "kanał", 26, "#2f3d40", weight="normal")
    return svg(W, H, b + R(0, 0, W, H, "#000", extra='filter="url(#grain)" opacity=".6"') + R(0, 0, W, H, "url(#vign)", extra='opacity=".6"'))

MAPS = {
    "dzielnica": (map_dzielnica, None),
    "targ-studnia": (map_targ, (30, 20)),
    "lazaret": (map_lazaret, (28, 18)),
    "spelunka-krukow": (map_spelunka, (26, 18)),
    "kancelaria-vargi": (map_kancelaria, (24, 18)),
}

if __name__ == "__main__":
    os.makedirs("/tmp/maps", exist_ok=True)
    for name, (fn, _) in MAPS.items():
        open(f"/tmp/maps/{name}.svg", "w").write(fn())
    print("ok")

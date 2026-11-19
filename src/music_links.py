# -*- coding: utf-8 -*-
"""Dziennik MG: muzyka do sesji (linki zewnętrzne — Spotify, YouTube, Bandcamp, Tabletop Audio)."""
from urllib.parse import quote

def sp(q): return f"https://open.spotify.com/search/{quote(q)}"
def yt(q): return f"https://www.youtube.com/results?search_query={quote(q).replace('%20', '+')}"
def a(url, label): return f'<a href="{url}" target="_blank" rel="noopener">{label}</a>'

ROWS = [
 ("Pustkowia i podróż", "ruiny, wędrówka, pustka po Eschatonie", [
   ("Post-Apocalyptic Ambience (playlista, 108 utworów)", [a("https://open.spotify.com/playlist/1NgtMYR7HG4EYMbQzAJJVW", "Spotify")]),
   ("Nick Cave & Warren Ellis — <i>The Road</i> (OST)", [a("https://music.apple.com/album/1435936237", "Apple Music"), a(sp("The Road Nick Cave Warren Ellis"), "Spotify (szukaj)"), a(yt("The Road soundtrack Nick Cave Warren Ellis full"), "YouTube (szukaj)")]),
 ]),
 ("Prymer, pola spor, Psychonauci", "obcość, groza, coś żywego w powietrzu", [
   ("Ben Salisbury & Geoff Barrow — <i>Annihilation</i> (OST)", [a("https://invada.bandcamp.com/album/annihilation-music-from-the-motion-picture", "Bandcamp"), a(sp("Annihilation Ben Salisbury Geoff Barrow"), "Spotify (szukaj)"), a(yt("Annihilation soundtrack Salisbury Barrow full album"), "YouTube (szukaj)")]),
   ("Cryo Chamber — wytwórnia dark ambient (długie miksy)", [a("https://www.youtube.com/channel/UCVHOgH4XEyYx-ZEaya1XqCQ", "YouTube (kanał)"), a("https://cryochamber.bandcamp.com/", "Bandcamp"), a(sp("Cryo Chamber dark ambient"), "Spotify (szukaj)")]),
 ]),
 ("Miasto, śledztwo, intryga", "Justitian, przesłuchania, kancelarie, kulty", [
   ("Jóhann Jóhannsson — <i>Sicario</i> (OST)", [a(sp("Sicario Johann Johannsson"), "Spotify (szukaj)"), a(yt("Sicario soundtrack Johann Johannsson full"), "YouTube (szukaj)")]),
   ("Cyberpunk Meditations — dark & dystopian ambient (playlista)", [a("https://open.spotify.com/playlist/7xIEp8VMrMijKiPUWCfxEB", "Spotify")]),
 ]),
 ("Bunkry, Kronikarze, technika dawnego świata", "zimne światło, szum maszyn, Klastry i bunkry Palerów", [
   ("Ben Frost — <i>Dark</i> (Netflix, OST)", [a(sp("Ben Frost Dark soundtrack"), "Spotify (szukaj)"), a(yt("Ben Frost Dark soundtrack"), "YouTube (szukaj)")]),
   ("Ben Salisbury & Geoff Barrow — <i>Ex Machina</i> (OST)", [a(sp("Ex Machina soundtrack Salisbury Barrow"), "Spotify (szukaj)")]),
 ]),
 ("Afryka, Neolibijczycy, pustynia", "karawany, przepych Trypolisu, Skurgerzy", [
   ("Hans Zimmer — <i>Dune</i> (OST)", [a(sp("Dune Hans Zimmer soundtrack"), "Spotify (szukaj)"), a(yt("Dune Hans Zimmer soundtrack full"), "YouTube (szukaj)")]),
 ]),
 ("Walka i pościg", "krótko, głośno, wyłącz po walce", [
   ("Jóhann Jóhannsson — „The Beast” (<i>Sicario</i>)", [a(sp("The Beast Johann Johannsson"), "Spotify (szukaj)"), a(yt("Sicario The Beast Johann Johannsson"), "YouTube (szukaj)")]),
   ("Junkie XL — <i>Mad Max: Fury Road</i> (OST)", [a(sp("Mad Max Fury Road Junkie XL"), "Spotify (szukaj)")]),
 ]),
 ("Spelunka, targ, życie dzielnicy", "gwar, dym, tani alkohol", [
   ("Tabletop Audio — darmowe pętle pod miejsca (tawerna, targ, deszcz, kanały)", [a("https://tabletopaudio.com/", "Tabletop Audio")]),
 ]),
]

def page():
    h = ["<p>Foundry nie odtwarza Spotify ani YouTube w playlistach, więc puszczaj muzykę obok (druga karta przeglądarki, telefon, głośnik), a w Foundry zostaw <b>Odgłosy</b> jako tło. Linki „(szukaj)” otwierają wyszukiwanie — wybierz oficjalny album.</p>",
         "<p><b>Zasada:</b> bez wokalu pod narrację; po walce wróć do ciszy albo samego ambientu. Głośność muzyki niższa niż twój głos.</p>"]
    for mood, desc, items in ROWS:
        h.append(f"<h2>{mood}</h2><p><i>{desc}</i></p><ul>")
        for name, links in items:
            h.append(f"<li>{name}: {' · '.join(links)}</li>")
        h.append("</ul>")
    h.append("<h2>Ciche studnie — co kiedy</h2><table><tr><th>Scena</th><th>Nastrój</th></tr>"
             "<tr><td>Świt nad dzielnicą, targ</td><td>Pustkowia (The Road) + Odgłos „Mżawka”</td></tr>"
             "<tr><td>Lazaret</td><td>Prymer (Annihilation), cicho</td></tr>"
             "<tr><td>Spelunka Kruków</td><td>Tabletop Audio — tawerna</td></tr>"
             "<tr><td>Kancelaria Vargi, przesłuchania</td><td>Miasto (Sicario)</td></tr>"
             "<tr><td>Kanały, piwnice</td><td>Cryo Chamber + Odgłos „Podziemia”</td></tr>"
             "<tr><td>Konfrontacja</td><td>Walka (The Beast) — potem cisza</td></tr></table>")
    return "".join(h)

MUSIC_PAGES = [("Playlisty i albumy", page())]

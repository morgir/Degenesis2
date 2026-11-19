# Degenesis: Katharsys 2.0 (fanowski) — system dla Foundry VTT v14

Nieoficjalna, fanowska wersja mechaniki Degenesis: narracyjna, śledcza i mniej śmiertelna.
Do użytku prywatnego. Degenesis © SIXMOREVODKA. Dokument projektowy zawiera pełny opis zasad.

## Instalacja (zalecana: przez manifest)
1. Foundry → **Game Systems** → **Install System**.
2. W polu **Manifest URL** na dole wklej:
   ```
   https://github.com/morgir/degenesis2/releases/latest/download/system.json
   ```
3. Kliknij **Install**. Kolejne wersje instalujesz przyciskiem **Update** przy systemie.
4. **Game Worlds** → **Create World** → system „Degenesis 2.0”. Przy pierwszym wejściu do świata instalator zaproponuje przeniesienie zasad, przygody, postaci i przeciwników.

Instalacja ręczna: pobierz `degenesis2.zip` z [Releases](https://github.com/morgir/degenesis2/releases) i rozpakuj do `Data/systems/`.

## Dla twórców: wydanie nowej wersji
1. Zmiany w kodzie wypchnij na `main`. Źródła kompendiów to pliki JSON w `src/packs/` (kompilowane automatycznie).
2. Opisz zmiany w `RELEASE_NOTES.md`.
3. Podbij `"version"` w `system.json` (np. na `0.6.2`) i wypchnij na `main`.
4. Akcja „Wydanie systemu” sama utworzy wydanie `v0.6.2`, ustawi wersję, skompiluje kompendia, uruchomi testy i dołączy `degenesis2.zip` oraz `system.json` do wydania.

Lokalnie: `npm install`, `npm run build` (kompendia do `packs/`), `npm test`.

## Pierwsze kroki
- Kompendia: **Zasady Katharsys 2.0** (dziennik), **Kultury / Koncepty / Kulty** (przeciągnij na kartę postaci), **Ekwipunek ogólny**, **Przykłady** (gotowe mini-śledztwo „Ciche studnie” w Justitian), **Makra MG**.
- Zaimportuj makra „Wyrocznia FU” i „Nowa sesja” na pasek makr.
- Rzut: kliknij nazwę umiejętności albo atrybutu na karcie. Atak: kliknij broń. Obrażenia: wybierz cel (T) i kliknij „Nałóż na cel” na karcie czatu.
- Aktor **Lokacja** pokazuje graczom tylko jawne Cechy (ukryte widzi MG). Gracze z uprawnieniem Obserwator mogą ogłaszać wywołania, a licznik darmowych wywołań poprawia MG. Z uprawnieniem Właściciel odliczają go sami.
- Aktor **Śledztwo** to wspólna tablica tropów. Daj graczom uprawnienie „Właściciel”.

## Nowe w 0.4.0: kompletna przygoda „Ciche studnie”
- **Sceny** (kompendium „Quick start: sceny”): plan dzielnicy + 4 mapy taktyczne z siatką 1 m. Zapasowo: makro „Utwórz sceny przygody”.
- **Dziennik przygody**: 11 stron z tekstami do czytania, scenami-węzłami, tropami, handoutami i epilogami.
- **Szkoła MG: pierwsza sesja**: 11 stron, od przygotowania w Foundry, przez sesję zero i rytm sesji, po każdą mechanikę na przykładach, plus muzyka.
- **7 gotowych postaci** (0.4.1: + Hellwetka Anja i Anabaptysta Kaspar) z historią, Ambicją, Tajemnicą, Więzią, portretem i tokenem (dołączył Kronikarz Modus).
- **Nowi NPC** z portretami: Ilsa Kruczyca, Higienista Kessel, brat Tobiasz (+ Halka, Varga, tragarze).
- Grafiki są wygenerowane kodem, bez praw autorskich. Możesz je podmienić w `assets/`.

## Nowe w 0.3.0
- **Kreator postaci**: przycisk „Kreator” na karcie postaci (albo makro „Kreator postaci”). 9 kroków według Katharsys: 3K, Ścieżka, atrybuty, umiejętności, Zaplecze, ranga (z automatycznym sprawdzaniem wymagań), Potencjał, Więzi i podsumowanie.
- **Rangi wszystkich 13 kultów** (z wymaganiami, efektami i ekwipunkiem) zapisane w przedmiotach Kultów.
- **81 Potencjałów** (ogólne i kultowe), opisanych po polsku i przeliczonych na zasady 2.0.
- **Dla graczy**: Podręcznik gracza (7 stron), Kulty — przewodnik (strona na kult: rangi, Metoda, Ideał, Potencjały), Kultury i Archetypy.
- **Gotowe postacie**: 4 postacie do przygody startowej.
- **Przeciwnicy**: 25 profili (ludzie, bestie, Prymer, maszyny i Śpiący, Psychonauci) w skalach 2.0.
- **Przygoda startowa „Ciche studnie”** (dziennik MG + aktorzy w kompendium „Quick start”).

## Dług i Imię (0.2.0)
- Utwórz jednego aktora **Rejestr Długów** na kampanię (tylko MG). Dłużnika i wierzyciela wybierasz z listy aktorów albo wpisujesz ręcznie.
- **Spłacony** daje Echo +1 frakcji-wierzycielowi, **Zerwany** daje Echo −2×waga. Zmiana Imienia przy ±4 dzieje się automatycznie, a komunikat trafia szeptem do MG.
- NPC przypisany do Frakcji pokazuje Postawę wynikającą z Imienia drużyny i przycisk do jej ustawienia.
- Karta postaci ma zakładkę **Dług i Imię**: kto jest jej winien, komu ona jest winna, Imię u znanych frakcji.

## Typy
Aktorzy: Postać, NPC (Statysta / Weteran / Antagonista / Banda), Frakcja (z Imieniem i Echem), Śledztwo, Lokacja, Rejestr Długów.
Przedmioty: Broń, Pancerz, Ekwipunek, Potencjał, Kultura, Koncept, Kult.

## Dla twórcy
- `src/` zawiera generator treści kompendiów (`build_packs.py`), kompilator do LevelDB (`compile.mjs`, wymaga `@foundryvtt/foundryvtt-cli`) i testy reguł (`node --test src/rules.test.mjs`).
- Tłumaczenia: `lang/pl.json`.

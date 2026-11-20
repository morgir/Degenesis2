# -*- coding: utf-8 -*-
PAGES = [
("1. Rdzeń mechaniki", """
<p>Rzucasz pulą k6 = <b>Atrybut + Umiejętność ± modyfikatory</b> (maks. 12 kości, nadwyżka = automatyczne sukcesy). Każde 4–6 to sukces, każda 6 to także <b>Wyzwalacz</b>.</p>
<p><b>Kiedy rzucać:</b> tylko gdy oba wyniki są ciekawe i coś realnego jest na szali. W innych przypadkach MG mówi „tak” albo „tak, ale…”.</p>
<table><tr><th>Trudność</th><th>Opis</th></tr>
<tr><td>1</td><td>Rutynowa</td></tr><tr><td>2</td><td>Wymagająca</td></tr><tr><td>3</td><td>Trudna</td></tr><tr><td>4</td><td>Bardzo trudna</td></tr><tr><td>6</td><td>Desperacka</td></tr></table>
<h3>Drabina wyników (czytana jak FU)</h3>
<table><tr><th>Wynik</th><th>Warunek</th><th>Skutek</th></tr>
<tr><td><b>Tak, i…</b></td><td>sukcesy ≥ Trudność i są Wyzwalacze</td><td>Każdy Wyzwalacz = 1 Efekt.</td></tr>
<tr><td><b>Tak</b></td><td>sukcesy ≥ Trudność</td><td>Udaje się.</td></tr>
<tr><td><b>Tak, ale…</b></td><td>≥1 sukces, brakuje najwyżej 2</td><td>Gracz wybiera: porażka albo sukces z Kosztem. Wyzwalacze przepadają.</td></tr>
<tr><td><b>Nie (ale…)</b></td><td>brak sukcesów lub brakuje 3+</td><td>Porażka, MG wykonuje ruch. Jeśli postać coś mimo to zyskuje (np. trop kluczowy), to „Nie, ale…”.</td></tr>
<tr><td><b>Nie, i…</b></td><td>więcej jedynek niż sukcesów</td><td>Zgrzyt: porażka i poważna komplikacja.</td></tr></table>
<h3>Efekty Wyzwalaczy (1 Wyzwalacz każdy)</h3>
<ul><li><b>Szybko</b>: bez tyku zegara.</li><li><b>Czysto</b>: bez śladu i świadków.</li><li><b>Więcej</b>: +1 Odsłona albo +1 obrażenie.</li>
<li><b>Przewaga</b>: tworzysz Cechę sceny z darmowym wywołaniem.</li><li><b>Wrażenie</b>: Postawa świadka +1 albo plotka o tobie.</li><li><b>Ochrona</b>: zapobiegasz jednemu Kosztowi dla grupy.</li></ul>
<h3>Koszty (MG wybiera jeden)</h3>
<p>Lekka rana · −1 Ego · tyk zegara · hałas lub ślad · utrata sprzętu lub amunicji · Postawa NPC −1 · +1 Zarażenie (w strefie spor) · więcej czasu · dług.</p>
<p><b>Starcie:</b> więcej sukcesów wygrywa, potem decydują Wyzwalacze, przy dalszym remisie wygrywa obrońca. <b>Pomoc:</b> +1K (+2K z Wyzwalaczem pomocnika), pomocnik dzieli Koszty.</p>
"""),
("2. Cechy miejsc i ruchy MG", """
<p>Każda ważna lokacja i scena ma 1–3 <b>Cechy</b>, jak aspekty w Fate („Gęsta mgła zarodników”, „Tłum na targu”). Prowadź je na aktorze typu <i>Lokacja</i>.</p>
<ul><li><b>Jawne</b> Cechy MG ogłasza od razu. <b>Ukryte</b> postacie odkrywają przez Odsłony, Percepcję albo dobre pytania. Uważność się opłaca.</li>
<li><b>Wywołanie</b>: opisz, jak Cecha pomaga, i weź +2K. Odkrywca lub twórca ma 1 darmowe wywołanie, kolejne kosztują 1 Ego.</li>
<li><b>Przeciw graczom</b>: MG wywołuje Cechę (−2K) albo używa jej jako Kosztu. Poza rzutem, jako komplikację, gracz dostaje za to 1 Ego.</li>
<li><b>Tworzenie</b>: efekt Przewaga, przygotowanie w Interludium albo Wykorzystanie Zaplecza.</li></ul>
<h3>Ruchy MG (styl PbtA)</h3>
<ul><li>Zapowiedz zagrożenie.</li><li>Zadaj obrażenia albo nalicz Koszt.</li><li>Przesuń zegar.</li><li>Ujawnij niewygodną prawdę.</li><li>Zabierz coś albo kogoś.</li>
<li>Postaw przed trudnym wyborem.</li><li>Wywołaj Cechę przeciw postaciom.</li><li>Daj frakcji zrobić ruch poza kadrem.</li><li>Odpowiedz Prymerem: Szept, zarodniki, insekty.</li></ul>
"""),
("3. Śledztwo", """
<p><b>Trop kluczowy nigdy nie zależy od rzutu.</b> Właściwe miejsce, sensowne podejście i umiejętność co najmniej 1 (albo pasujące Zaplecze) wystarczą. Rzut decyduje o tym, ile dostajesz ponad to, jak szybko i jakim kosztem.</p>
<ul><li><b>Sukces</b>: 1 Odsłona, każdy Wyzwalacz kolejna.</li><li><b>Tak, ale</b>: Odsłona, ale ktoś cię widział, zatarłeś ślad albo tyka zegar.</li><li><b>Porażka</b>: tylko trop kluczowy plus komplikacja.</li></ul>
<table><tr><th>Odsłona</th><th>Co daje</th></tr>
<tr><td>Szczegół</td><td>zawęża listę podejrzanych lub miejsc</td></tr><tr><td>Powiązanie</td><td>link do innego tropu, NPC albo frakcji</td></tr>
<tr><td>Dźwignia</td><td>Motyw, Lęk, Sekret albo Cena NPC</td></tr><tr><td>Ostrzeżenie</td><td>zagrożenie, zanim uderzy</td></tr><tr><td>Czas</td><td>cofasz 1 tyk Zegara zagrożenia</td></tr></table>
<p><b>Metoda kultu</b>: raz na scenę, gdy śledzisz metodą swojego kultu, dostajesz +1 Odsłonę bez rzutu (opis metody jest w przedmiocie Kultu).</p>
<p><b>Wniosek</b>: połączcie 2+ tropy w teorię i rzućcie Intelekt + Legendy, Instynkt + Empatia albo Psyche + Spryt (2). Sukces: MG mówi „ciepło” lub „zimno” i dodaje fakt. Porażka: tylko „ciepło” lub „zimno”. MG nie kłamie przy Wniosku.</p>
<p><b>Zegar zagrożenia</b> (6–8) to plan antagonisty. Tyka od Kosztów, czasu i hałasu. To on daje presję, nie ryzyko śmierci. Prowadź go na aktorze typu <i>Śledztwo</i>.</p>
"""),
("4. Interakcje i wpływ", """
<p>Ważny NPC ma <b>Motyw</b>, <b>Lęk</b>, <b>Sekret</b>, <b>Cenę</b> i <b>Postawę</b>.</p>
<table><tr><th>Postawa</th><th>Trudność bazowa</th></tr><tr><td>Wrogi (−2)</td><td>4</td></tr><tr><td>Nieufny (−1)</td><td>3</td></tr>
<tr><td>Obojętny (0)</td><td>2</td></tr><tr><td>Życzliwy (+1)</td><td>1</td></tr><tr><td>Oddany (+2)</td><td>bez rzutu przy drobnych prośbach</td></tr></table>
<p>Waga prośby: +0 drobna, +1 istotna, +2 ryzykowna dla NPC. Prośba sprzeczna z Motywem lub kultem NPC wymaga Dźwigni.</p>
<p><b>Opór</b>: przy manipulacji (Uwodzenie, Oszustwo, Dominacja) ważny NPC może rzucić Psyche + Wiara lub Wola w Starciu.</p>
<p><b>Dźwignia</b>: każdy znany i użyty element (Motyw, Lęk, Sekret, zapłacona Cena) daje +2K albo czyni niemożliwe możliwym.</p>
<p><b>Wynik</b>: sukces = prośba spełniona albo Postawa +1 (Wyzwalacz: oba lub informacja). „Tak, ale” = spełniona z warunkiem lub plotką. Porażka = Postawa −1 albo NPC robi coś po swojemu.</p>
<h3>Zaplecze</h3>
<ul><li><b>Wsparcie</b>: wartość Zaplecza jako kości (maks. +3K).</li><li><b>Wykorzystanie</b>: tymczasowo −1, pewny efekt bez rzutu (informacja, przysługa, sprzęt, dostęp). Wraca w Interludium.</li></ul>
<p><b>Ranga</b> działa jak status: niżsi rangą z kultu mają Postawę +1 w sprawach kultu, wyżsi rangą mogą wydawać rozkazy.</p>
"""),
("4b. Dług i Imię", """
<p>Dwie waluty ważniejsze od pieniędzy. Obie prowadzi MG: długi w aktorze <i>Rejestr Długów</i>, Imię na aktorach <i>Frakcja</i>.</p>
<h3>Dług</h3>
<table><tr><th>Waga</th><th>Przykład</th><th>Wartość</th></tr>
<tr><td>Drobny</td><td>nocleg, informacja, przemilczenie</td><td>+2K albo drobna przysługa bez rzutu</td></tr>
<tr><td>Poważny</td><td>uratowany towar, ukryty zbieg, lekarstwo</td><td>+4K albo istotna przysługa bez rzutu</td></tr>
<tr><td>Krwawy</td><td>uratowane życie, cudza zemsta</td><td>prośba ryzykowna dla dłużnika, bez rzutu</td></tr></table>
<ul><li><b>Zaciągnięcie</b>: pomoc nieopłacona od ręki. Typowy Koszt przy „Tak, ale…” i Konsekwencja po wyeliminowaniu.</li>
<li><b>Ściągnięcie</b> (dług wobec ciebie): przysługa skali wagi bez rzutu albo premia do rzutu przeciw dłużnikowi. Dług można też odstąpić jako zapłatę.</li>
<li><b>Wezwanie długu</b> (ruch MG): wierzyciel żąda spłaty teraz. Spłać albo zerwij.</li>
<li><b>Zerwanie</b>: Echo −2×waga u frakcji wierzyciela, wróg osobisty, plotka.</li></ul>
<h3>Imię</h3>
<table><tr><th>Imię</th><th>Nazwa</th><th>Postawa członków</th><th>Znaczenie</th></tr>
<tr><td>−3</td><td>Krwawy wróg</td><td>Wrogi</td><td>polowanie, nagroda za głowę</td></tr>
<tr><td>−2</td><td>Wróg</td><td>Wrogi</td><td>zamknięte drzwi, donosy</td></tr>
<tr><td>−1</td><td>Podejrzany</td><td>Nieufny</td><td>kontrole, wyższe ceny</td></tr>
<tr><td>0</td><td>Obcy</td><td>Obojętny</td><td>nikt was nie zna</td></tr>
<tr><td>+1</td><td>Znany</td><td>Życzliwy</td><td>pierwsza drobna prośba bez rzutu</td></tr>
<tr><td>+2</td><td>Szanowany</td><td>Życzliwy</td><td>usługi, sprzęt, ludzie frakcji</td></tr>
<tr><td>+3</td><td>Swoi</td><td>Oddany</td><td>schronienie, wsparcie, kredyt bez długu</td></tr></table>
<p><b>Echo</b> (−4…+4): spłacony dług +1, zlecenie +1/+2, publiczny czyn +2, zerwany dług −2×waga, zbrodnia przy świadkach −2…−4. Przy ±4 Imię zmienia się o 1, a Echo wraca do 0. Spłata i zerwanie w Rejestrze przesuwają Echo automatycznie.</p>
<p><b>Imię a Zaplecze</b>: Zaplecze to pozycja we własnym kulcie, a Imię to drużyna w oczach innych. <b>Imię osobiste</b> (opcja): MG wpisuje osobny modyfikator ±1 dla jednej postaci.</p>
"""),
("5. Ego i Archetyp", """
<p>Ego maks. = (Intelekt + Skupienie)×2 albo (Instynkt + Pierwotność)×2.</p>
<table><tr><th>Wydatek</th><th>Koszt</th></tr><tr><td>+1K (maks. 3 na rzut)</td><td>1 Ego za kość</td></tr><tr><td>Aktywna obrona</td><td>1</td></tr>
<tr><td>Nowa rana o stopień niżej</td><td>2</td></tr><tr><td>Przebłysk: przerzut kości bez sukcesu</td><td>3</td></tr></table>
<p><b>Załamanie</b> (Ego 0): ucieczka, apatia (−2K na scenę), wybuch zgodny z Cieniem albo przyjęcie Szeptu Prymera. Drugie przed odpoczynkiem zostawia Bliznę psychiczną.</p>
<p><b>Odzyskiwanie</b>: +1 za każdy dzień, +1 za działanie zgodne z Archetypem kosztem postaci, +2 raz na sesję za Ideał kultu wbrew interesowi, całość przy Więzi w Interludium, Burn +Moc (z Zarażeniem).</p>
<p><b>Archetyp</b>: raz na sesję +2K w zgodnej sytuacji. <b>Pokusa Archetypu</b>: MG proponuje działanie zgodne z Cieniem. Zgoda daje +2 Ego, +1 PD i komplikację.</p>
"""),
("6. Rany i konsekwencje", """
<p><b>Próg Ran = Ciało + Twardość.</b> Obrażenia netto = obrażenia broni + Wyzwalacze − pancerz.</p>
<table><tr><th>Netto</th><th>Rana</th><th>Miejsca</th><th>Kara</th></tr><tr><td>≤ 0</td><td>draśnięcie</td><td>—</td><td>—</td></tr>
<tr><td>1 … Próg−1</td><td>Lekka</td><td>3</td><td>—</td></tr><tr><td>Próg … 2×Próg−1</td><td>Poważna</td><td>2</td><td>−1K każda</td></tr><tr><td>≥ 2×Próg</td><td>Krytyczna</td><td>1</td><td>−2K, opieka po scenie</td></tr></table>
<p>Pełne miejsca: rana o stopień wyżej. Rana przy zajętej Krytycznej: <b>Wyeliminowany</b>.</p>
<p><b>Wyeliminowany ≠ martwy.</b> Po scenie przychodzi Konsekwencja: niewola lub przesłuchanie, utrata sprzętu, trwała Blizna, dług, upokorzenie (−1 Sława lub Autorytet), +1k6 Zarażenia, cenę płaci Więź.</p>
<p><b>Śmierć tylko przy Stawce Śmierci</b>, ogłoszonej przed konfliktem (Psychonauta, Maruder, egzekucja), albo z wyboru gracza.</p>
<p><b>Absorpcja</b>: 2 Ego albo trwała Blizna (Cecha postaci, maks. 3) obniża ranę o stopień.</p>
<p><b>Leczenie</b>: Lekkie znikają po scenie odpoczynku. Poważna: tydzień albo Intelekt + Medycyna (2) w Interludium. Krytyczna: tygodnie i Medycyna (3), bez opieki zostaje Blizna.</p>
<p><b>Skala NPC</b>: Statysta pada od 1 rany. Weteran ma 1 Lekką i 1 Poważną. Antagonista ma pełną drabinę. Banda: Lekka −1, Poważna −2, Krytyczna −3 członków. <b>Morale</b>: ucieczka przy połowie strat albo Poważnej ranie przywódcy.</p>
"""),
("7. Walka", """
<ol><li><b>Inicjatywa raz na starcie</b>: Psyche + Refleks (tracker walki liczy sukcesy). 2 Wyzwalacze dają dodatkową akcję w 1. rundzie.</li>
<li><b>Tura</b>: 1 akcja i przejście o jedną strefę. Przejście o dwie strefy zabiera całą turę (bieg), ale daje +1 Obrony.</li>
<li><b>Atak</b>: Bijatyka, Broń biała albo Strzelectwo (+ Poręczność) przeciw Obronie celu.</li>
<li><b>Trafienie</b>: obrażenia + Wyzwalacze, potem pancerz i drabina ran. Zamiast obrażeń Wyzwalacze można wydać na efekt: rozbrój, powal, przyszpil, odrzuć, zajmij pozycję.</li></ol>
<p><b>Obrona</b>: 1 bazowo, +1 osłona, +1 ruch, +1 tarcza lub teren, +2 ciemność albo cel Daleko. Cechy sceny też działają.</p>
<p><b>Strefy zamiast metrów</b>: odległość mierzymy strefami, a mapa tylko ilustruje scenę.</p>
<table><tr><th>Strefa</th><th>Co znaczy</th></tr>
<tr><td><b>Zwarcie</b></td><td>na wyciągnięcie ręki; walka wręcz, chwyty</td></tr>
<tr><td><b>Blisko</b></td><td>kilka kroków; rzut nożem lub granatem, pistolet i strzelba bez kary</td></tr>
<tr><td><b>Daleko</b></td><td>druga strona placu lub hali; tylko broń palna, łuk, kusza</td></tr>
<tr><td><b>Poza zasięgiem</b></td><td>dalej niż zwykły strzał; tylko broń oznaczona „Daleko+” po akcji celowania</td></tr></table>
<p>Strzał do strefy dalszej niż zasięg broni: −2K albo w ogóle niemożliwy (decyduje MG). Wyjście ze Zwarcia z wrogiem, który nie jest przyszpilony, daje mu darmowy atak, chyba że wydasz na to akcję.</p>

<p><b>Aktywna obrona</b>: 1 Ego, Starcie (Mobilność, Broń biała, Bijatyka). Wygrana wręcz z 3 Wyzwalaczami to kontratak. Statyści się nie bronią.</p>
<p><b>Banda</b>: 1 atak na rundę, +1K za każdych 2 członków (maks. +4K).</p>
<p><b>Wyjście z walki</b> jest zawsze możliwe: ucieczka, kapitulacja, rozmowa. Po Poważnej ranie przywódcy MG proponuje negocjacje.</p>
<p>W Foundry: atak z karty broni, potem na karcie czatu „Nałóż na cel” (cel = klawisz T). Pancerz i Próg liczą się same.</p>
"""),
("8. Sepsa, Burn i Zew Prymera", """
<ul><li>Zarażenie maks. = (Psyche + Wiara/Wola)×2. Przy połowie skali pojawia się stygmat.</li>
<li>Przekroczenie maksimum: rzut Psyche + Wiara/Wola przeciw nadwyżce. Porażka daje +1 trwałe (Nosiciel Nasienia).</li>
<li>Trwałe Zarażenie na połowie skali oznacza Leperosa. Ostatnia scena należy do gracza.</li></ul>
<p><b>Burn</b>: +Moc Ego, +Moc Zarażenia, efekt czakry przez Moc godzin (Bion, Glory, Unity, Muse, Argus; Discordia to ruletka). <b>Głód</b>: 3 dawki w tygodniu dają −1K do kolejnej dawki albo do wygranego w Interludium rzutu Psyche + Wola (2).</p>
<p><b>Zew Prymera</b>: przy Zarażeniu ≥ 1 MG może zaoferować <b>Szept</b>: wizję z prawdziwą, choć zniekształconą Odsłoną, +2K, przeczucie, gdzie jest Psychonauta albo pole, rozumienie insektów przez scenę. Przyjęcie: +1 Zarażenia (silny Szept +2). Odmowa nic nie kosztuje. Od stygmatu wizje przychodzą same, bez korzyści.</p>
<p>Psychonauci uderzają w Ego i Zarażenie. To typowa okazja do Stawki Śmierci.</p>
<h3>Zjawiska Psychonautów (z Katharsys, s. 285)</h3>
<ul><li><b>Pula = Zarażenie − Przeciążenie</b> (pole „Zarażenie (Prymer)” na karcie NPC). Ponad 12 kości działa zwykła zasada 2.0: nadwyżka to sukcesy automatyczne.</li>
<li><b>Trudność = poziom Zjawiska</b> (0–16). Drabina wyników 2.0 działa normalnie: „Tak, ale” to Zjawisko z kosztem albo słabsze.</li>
<li><b>Przeciążenie</b> wybiera MG (maks. tyle, ile zostało Zarażenia). Wzmacnia efekt (np. Trudność obrony, obrażenia, utratę Ego), a każdy punkt trwale zużywa 1 punkt Zarażenia. Kliknij Zjawisko na karcie — okno zapyta o Przeciążenie i samo odejmie spory.</li>
<li>Inhibitory sepsy (EX Aerosol, EG-1) i kolejne Przeciążenia odbierają najpierw najwyższe Zjawiska. Przy Zarażeniu 0 Psychonauta jest „odsporzony”: działa przez Skupienie i Ego jak człowiek, unika walki, a przyparty do muru woli się poddać i planować ucieczkę.</li>
<li><b>Rój (Plaga)</b>: zaatakowani mają karę równą Sile roju do wszystkich akcji i 1 Lekką ranę na rundę; rój ranią tylko broń obszarowa i ogień.</li>
<li>Przeliczenia: Rana Powierzchowna → Lekka rana, Trauma → rana Poważna, „(Przeciążenie)” przy obronie → Trudność obrony = Przeciążenie.</li></ul>
"""),
("9. Sandbox i Interludium", """
<table><tr><th>Zegar</th><th>Do czego</th><th>Przesuwa go</th></tr><tr><td>Zagrożenie</td><td>plan antagonisty</td><td>Koszty, czas, hałas</td></tr>
<tr><td>Postęp</td><td>długie zadania</td><td>sukces = 1, Wyzwalacz = +1</td></tr><tr><td>Frakcja</td><td>cel frakcji</td><td>Interludium, ruchy MG</td></tr></table>
<p><b>Frakcja</b>: Cel z zegarem, Zasoby 1–5, Stosunek −3…+3, jedna Cecha. W Interludium MG przesuwa 1–2 zegary, a w razie wątpliwości rzuca Zasobami przeciw Trudności 2.</p>
<p><b>Interludium</b> (2 akcje na postać): Leczenie · Śledzenie tropu (Odsłona, ale tyka zegar) · Służba kultowi (odzyskaj Zaplecze, dostań zadanie) · Handel/złom · Plotki (1 prawdziwa, 1 fałszywa) · Przygotowanie (Cecha na następną scenę) · Więź (całe Ego) · Odwyk.</p>
<p><b>Więzi</b>: 1–2 osoby, miejsca albo ideały spoza kultu. Zagrożona Więź to najmocniejszy hak fabularny.</p>
<table><tr><th>k6</th><th>Wyrocznia FU</th></tr><tr><td>1</td><td>Nie, i…</td></tr><tr><td>2</td><td>Nie</td></tr><tr><td>3</td><td>Nie, ale…</td></tr><tr><td>4</td><td>Tak, ale…</td></tr><tr><td>5</td><td>Tak</td></tr><tr><td>6</td><td>Tak, i…</td></tr></table>
<p>Odpowiedź prawdopodobna: 2k6, bierzesz wyższą. Mało prawdopodobna: 2k6, bierzesz niższą. Makro „Wyrocznia FU” robi to za ciebie.</p>
"""),
("10. Postać i rozwój", """
<ol><li>3K: Kultura, Koncept, Kult (przeciągnij z kompendium na kartę). Każde podnosi limit wybranych cech o 1.</li>
<li>Atrybuty: start 1 + 10 punktów, limit 3. Umiejętności: 28 punktów, limit 2. Wybierz Skupienie albo Pierwotność oraz Wiarę albo Wolę.</li>
<li>Zaplecze: 4 punkty, limit 3. Ranga według kultu. Potencjał: 1 na poziomie 1.</li>
<li>Nowe: 1–2 Więzi, Ambicja, Tajemnica, Cień Archetypu.</li></ol>
<table><tr><th>PD za sesję</th><th></th></tr><tr><td>Udział</td><td>5</td></tr><tr><td>Ważny Wniosek</td><td>+2</td></tr><tr><td>Przyjęta Pokusa Archetypu</td><td>+1</td></tr><tr><td>Ideał lub Więź ponad interes</td><td>+1</td></tr><tr><td>Odkryty Sekret</td><td>+2</td></tr></table>
<p>Koszty rozwoju jak w Katharsys: atrybut nowa×12 (preferowany ×10), umiejętność nowa×5 (preferowana ×4), Potencjał suma poziomów×10. Zaplecze rośnie tylko przez czyny.</p>
<p><b>Z podręczników</b>: Potencjały działają bez zmian (Rany Powierzchowne = obrażenia, Trauma = rana Poważna). NPC: licz Próg i przypisz skalę.</p>
"""),
]

GM_PAGE = ("Jak prowadzić: pierwsza sesja", """
<ol><li><b>Sesja zero</b>: pytania z Katharsys (oś gry, dlaczego ta grupa, kto kogo gra) plus jedno nowe: <i>czyja prawda jest stawką?</i></li>
<li><b>Przygotuj region</b>: 2–3 Frakcje z zegarami, 3–4 Lokacje z Cechami (jedną ukrytą w każdej), 4–6 NPC z Motywem, Lękiem, Sekretem i Ceną.</li>
<li><b>Przygotuj śledztwo</b>: pytanie główne, 3 tropy kluczowe dla każdej sceny-węzła (zasada trzech tropów), Zegar zagrożenia na 6–8.</li>
<li><b>Graj od pytań</b>: gdy nie wiesz, co jest za drzwiami, użyj Wyroczni FU i zbuduj odpowiedź z fikcji.</li>
<li><b>Nagradzaj uważność</b>: ukryte Cechy, Dźwignie i Wnioski to waluta graczy. Dawaj ją hojnie tym, którzy pytają i słuchają.</li>
<li><b>Ogłaszaj Stawki</b>: przed naprawdę śmiertelnym starciem powiedz to wprost. Reszta walk kosztuje, ale nie zabija.</li>
<li><b>Na koniec sesji</b>: PD, przesunięcie zegarów frakcji, makro „Nowa sesja” (odnawia Archetypy).</li></ol>
""")

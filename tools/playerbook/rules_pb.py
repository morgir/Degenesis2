# -*- coding: utf-8 -*-
"""Zasady 2.0 w wersji dla graczy."""

RULES = [
("Rzut kośćmi", """
<p>Rzucasz tylko wtedy, gdy wynik jest niepewny, a na szali leży coś ważnego. Inaczej MG po prostu mówi „tak” albo „tak, ale…”.</p>
<p><b>Pula</b> to Atrybut + Umiejętność, na przykład Instynkt + Percepcja. Rzucasz tyle kości k6 (oznaczamy je K). Każda kość z wynikiem <b>4, 5 lub 6</b> to <b>sukces</b>, a każda <b>6</b> to dodatkowo <b>Wyzwalacz</b>. Pula ma najwyżej 12 kości. Każdy punkt ponad 12 to sukces automatyczny.</p>
<table><tr><th>Trudność</th><th>Kiedy</th></tr>
<tr><td>1</td><td>rutynowe działanie pod presją</td></tr><tr><td>2</td><td>wymagające, standard</td></tr>
<tr><td>3</td><td>trudne</td></tr><tr><td>4</td><td>bardzo trudne</td></tr><tr><td>6</td><td>desperackie</td></tr></table>
<h4>Skąd wziąć dodatkowe kości</h4>
<ul><li><b>Ego:</b> 1 punkt = +1K, najwyżej 3 na rzut.</li>
<li><b>Zaplecze</b> (pomoc twojego kultu): jego wartość jako kości, najwyżej +3K.</li>
<li><b>Cecha miejsca:</b> +2K za każdą wywołaną Cechę.</li>
<li><b>Dźwignia</b> na rozmówcę: +2K.</li>
<li><b>Archetyp:</b> raz na sesję +2K, gdy działasz zgodnie ze swoim Konceptem.</li>
<li><b>Pomoc</b> towarzysza: +1K (+2K, jeśli pomagający rzucił z Wyzwalaczem). Pomocnik dzieli też Koszty.</li></ul>
<p><b>Starcie:</b> gdy ktoś aktywnie ci się przeciwstawia, rzucacie oboje. Wygrywa ten, kto ma więcej sukcesów, potem decydują Wyzwalacze, a przy dalszym remisie wygrywa obrońca.</p>
"""),
("Co znaczą wyniki", """
<table><tr><th>Wynik</th><th>Kiedy</th><th>Co się dzieje</th></tr>
<tr><td><b>Tak, i…</b></td><td>sukcesy ≥ Trudność i są szóstki</td><td>Udało się, a każdy Wyzwalacz kupuje jeden Efekt.</td></tr>
<tr><td><b>Tak</b></td><td>sukcesy ≥ Trudność</td><td>Udało się.</td></tr>
<tr><td><b>Tak, ale…</b></td><td>co najmniej 1 sukces, brakuje 1–2</td><td>Wybierasz: porażka albo sukces z Kosztem, który nalicza MG.</td></tr>
<tr><td><b>Nie</b></td><td>za mało sukcesów</td><td>Nie wychodzi, a sytuacja się zmienia. Trop kluczowy i tak dostajesz.</td></tr>
<tr><td><b>Nie, i…</b></td><td>więcej jedynek niż sukcesów</td><td>Zgrzyt: porażka i poważna komplikacja.</td></tr></table>
<div class="two" style="break-inside:avoid;page-break-inside:avoid"><div><h4>Efekty (1 Wyzwalacz = 1 Efekt)</h4><ul>
<li><b>Szybko:</b> bez straty czasu.</li><li><b>Czysto:</b> bez śladów i świadków.</li>
<li><b>Więcej:</b> dodatkowa informacja (Odsłona) albo +1 obrażenie.</li>
<li><b>Przewaga:</b> tworzysz nową Cechę sceny z darmowym wywołaniem.</li>
<li><b>Wrażenie:</b> świadek zaczyna cię lubić albo rusza plotka.</li>
<li><b>Ochrona:</b> osłaniasz drużynę przed jednym Kosztem.</li></ul></div>
<div><h4>Koszty (przy „Tak, ale…”)</h4><ul>
<li>Lekka rana albo −1 Ego.</li><li>Hałas, ślad, świadek.</li><li>Zgubiony sprzęt lub amunicja.</li>
<li>Ktoś cię mniej lubi.</li><li>Więcej czasu: tyka zegar zagrożenia.</li><li>Dług.</li>
<li>+1 Zarażenia (w strefie spor).</li></ul></div></div>
"""),
("Cechy miejsc", """
<p>Każde ważne miejsce i scena ma 1–3 <b>Cechy</b>, na przykład „Tłum na targu”, „Zardzewiałe rusztowania” albo „Gęsta mgła zarodników”. Część MG ogłasza od razu, a część jest ukryta.</p>
<ul><li><b>Odkrywanie:</b> kto pyta, patrzy i szuka, znajduje ukryte Cechy (Odsłoną, rzutem na Percepcję albo dobrym pytaniem).</li>
<li><b>Wywołanie:</b> opisz, jak Cecha ci pomaga, i weź +2K. Kto Cechę odkrył albo stworzył, ma jedno darmowe wywołanie, a każde kolejne kosztuje 1 Ego.</li>
<li><b>Przeciw wam:</b> MG też może wywołać Cechę (−2K dla was). Jeśli zrobi to jako komplikację poza rzutem, dostajesz 1 Ego.</li>
<li><b>Tworzenie:</b> efekt Przewaga, przygotowanie w Interludium albo przysługa kultu.</li></ul>
"""),
("Śledztwo", """
<p>Śledztwa są sercem tej gry. Działają według prostej zasady: <b>trop kluczowy dostajecie zawsze</b>. Wystarczy szukać we właściwym miejscu, sensownie i z pasującą umiejętnością (albo Zapleczem). Rzut decyduje o tym, ile dowiecie się ponad to, jak szybko i jakim kosztem.</p>
<table><tr><th>Odsłona</th><th>Co daje</th></tr>
<tr><td>Szczegół</td><td>zawęża listę podejrzanych albo miejsc</td></tr>
<tr><td>Powiązanie</td><td>łączy trop z innym tropem, osobą lub frakcją</td></tr>
<tr><td>Dźwignia</td><td>czego ktoś chce, czego się boi, co ukrywa albo za co pomoże</td></tr>
<tr><td>Ostrzeżenie</td><td>zagrożenie, zanim uderzy</td></tr>
<tr><td>Czas</td><td>cofa o jeden krok zegar zagrożenia</td></tr></table>
<ul><li>Sukces daje 1 Odsłonę, a każdy Wyzwalacz kolejną. „Tak, ale” daje Odsłonę z kosztem. Porażka daje tylko trop kluczowy i komplikację.</li>
<li><b>Metoda kultu:</b> każdy kult ma swój sposób szukania prawdy (opisany przy kulcie). Raz na scenę, gdy działasz tą metodą, dostajesz dodatkową Odsłonę bez rzutu.</li>
<li><b>Wniosek:</b> gdy połączycie dwa tropy lub więcej w teorię, rzućcie Intelekt + Legendy, Instynkt + Empatia albo Psyche + Spryt (Trudność 2). Przy sukcesie MG powie „ciepło” albo „zimno” i doda fakt. Przy porażce powie samo „ciepło” albo „zimno”. <b>MG przy Wniosku nie kłamie.</b></li>
<li><b>Zegar zagrożenia:</b> antagonista ma plan, który posuwa się naprzód przez wasze Koszty, hałas i stracony czas. To on daje presję.</li></ul>
<p class="note">Rada: prowadźcie wspólną tablicę śledztwa (kartka albo dziennik w Foundry): osoby, miejsca, tropy i strzałki między nimi.</p>
"""),
("Rozmowa i wpływ", """
<p>Każdy ważny NPC ma <b>Motyw</b>, <b>Lęk</b>, <b>Sekret</b>, <b>Cenę</b> i <b>Postawę</b> wobec was. Postawa wyznacza Trudność rozmowy.</p>
<table><tr><th>Postawa</th><th>Trudność</th></tr>
<tr><td>Wrogi</td><td>4</td></tr><tr><td>Nieufny</td><td>3</td></tr><tr><td>Obojętny</td><td>2</td></tr>
<tr><td>Życzliwy</td><td>1</td></tr><tr><td>Oddany</td><td>drobne prośby bez rzutu</td></tr></table>
<ul><li>Istotna prośba to +1 do Trudności, a prośba ryzykowna dla NPC +2.</li>
<li>Prośba sprzeczna z Motywem NPC albo jego kultem wymaga <b>Dźwigni</b>.</li>
<li><b>Dźwignia</b> to każdy znany i użyty element (Motyw, Lęk, Sekret albo zapłacona Cena). Daje +2K albo sprawia, że niemożliwe staje się możliwe. Najlepsze rozmowy wygrywa się wcześniej, w śledztwie.</li>
<li>Przy manipulacji (Uwodzenie, Oszustwo, Dominacja) ważny NPC może się opierać rzutem Psyche + Wiara lub Wola.</li>
<li>Sukces: prośba spełniona albo Postawa +1. „Tak, ale”: spełniona z warunkiem albo plotką. Porażka: Postawa −1 albo NPC robi coś po swojemu.</li></ul>
"""),
("Zaplecze — twój kult za plecami", """
<p>Zaplecze to sześć rodzajów pomocy: <b>Sojusznicy, Autorytet, Sława, Zasoby, Sekrety i Sieć</b> (informatorzy). Możesz z niego skorzystać na dwa sposoby:</p>
<ul><li><b>Wsparcie:</b> wartość Zaplecza jako dodatkowe kości (najwyżej +3K).</li>
<li><b>Wykorzystanie:</b> pewny efekt bez rzutu (informacja, przysługa, sprzęt, dostęp). Punkt jest wtedy zużyty do następnego Interludium.</li></ul>
<p><b>Ranga</b> działa jak status. Niżsi rangą w twoim kulcie są wobec ciebie życzliwsi w sprawach kultu, a wyżsi mogą wydawać ci rozkazy.</p>
"""),
("Dług i Imię", """
<p>W świecie po końcu świata przysługa i reputacja są warte więcej niż pieniądze. MG prowadzi oba rejestry.</p>
<h4>Dług</h4>
<table><tr><th>Waga</th><th>Przykład</th><th>Co jest wart</th></tr>
<tr><td>Drobny</td><td>nocleg, informacja, przemilczenie</td><td>+2K albo drobna przysługa bez rzutu</td></tr>
<tr><td>Poważny</td><td>ukryty zbieg, lekarstwo, uratowany towar</td><td>+4K albo istotna przysługa bez rzutu</td></tr>
<tr><td>Krwawy</td><td>uratowane życie, cudza zemsta</td><td>ryzykowna prośba bez rzutu</td></tr></table>
<ul><li>Kto pomógł wam bez zapłaty, ma u was dług. Kto ma dług u was, jest wam winien przysługę. Dług można też oddać komuś jako zapłatę.</li>
<li>Wierzyciel może <b>wezwać dług</b> w najmniej wygodnym momencie. Wtedy spłacacie albo zrywacie.</li>
<li><b>Zerwany dług</b> to wróg, plotka i strata Imienia u frakcji wierzyciela.</li></ul>
<h4>Imię</h4>
<p>Imię to reputacja waszej drużyny u każdej frakcji, od −3 do +3.</p>
<table><tr><th>Imię</th><th>Nazwa</th><th>Co to znaczy</th></tr>
<tr><td>−3</td><td>Krwawy wróg</td><td>polowanie, nagroda za głowę</td></tr>
<tr><td>−2</td><td>Wróg</td><td>zamknięte drzwi, donosy</td></tr>
<tr><td>−1</td><td>Podejrzany</td><td>kontrole, wyższe ceny</td></tr>
<tr><td>0</td><td>Obcy</td><td>nikt was nie zna</td></tr>
<tr><td>+1</td><td>Znany</td><td>pierwsza drobna prośba bez rzutu</td></tr>
<tr><td>+2</td><td>Szanowany</td><td>usługi, sprzęt, ludzie frakcji</td></tr>
<tr><td>+3</td><td>Swoi</td><td>schronienie, wsparcie, kredyt bez długu</td></tr></table>
<p>Imię zmienia się powoli. Spłacone długi, wykonane zlecenia i publiczne czyny budują je krok po kroku, a zerwane długi i zbrodnie przy świadkach szybko je niszczą.</p>
"""),
("Ego, Archetyp i Cień", """
<p><b>Ego</b> to odporność psychiczna i jednocześnie waluta. Maksimum to (Intelekt + Skupienie)×2 albo (Instynkt + Pierwotność)×2, zależnie od ścieżki.</p>
<table><tr><th>Wydatek</th><th>Koszt</th></tr>
<tr><td>+1K do rzutu (najwyżej 3)</td><td>1 Ego za kość</td></tr>
<tr><td>Aktywna obrona w walce</td><td>1</td></tr>
<tr><td>Nowa rana o stopień lżejsza</td><td>2</td></tr>
<tr><td>Przebłysk: przerzuć kości bez sukcesu</td><td>3</td></tr></table>
<p>Ego tracisz przez grozę, presję i Psychonautów. Przy zerze się łamiesz: uciekasz, popadasz w apatię, wybuchasz albo ulegasz Prymerowi.</p>
<p>Ego odzyskujesz snem (+1 dziennie), działaniem zgodnym z Archetypem kosztem postaci, wiernością Ideałowi kultu wbrew własnemu interesowi (+2 raz na sesję), czasem z Więzią w Interludium (całe Ego) i Burnem, który podnosi jednak Zarażenie.</p>
<p><b>Archetyp</b> (twój Koncept) raz na sesję daje +2K w zgodnej sytuacji. Jego <b>Cień</b> to ciemna strona. Gdy MG zaproponuje <b>Pokusę</b>, czyli działanie zgodne z Cieniem, możesz ją przyjąć. Dostajesz wtedy +2 Ego i +1 PD, a historia się komplikuje.</p>
"""),
("Rany — groźnie, ale nie morderczo", """
<p>Twój <b>Próg</b> to Ciało + Twardość. Gdy cię trafią, obrażenia netto to obrażenia broni + Wyzwalacze − pancerz.</p>
<table><tr><th>Netto</th><th>Rana</th><th>Miejsca</th><th>Kara</th></tr>
<tr><td>0 lub mniej</td><td>draśnięcie</td><td>—</td><td>—</td></tr>
<tr><td>poniżej Progu</td><td>Lekka</td><td>3</td><td>—</td></tr>
<tr><td>od Progu</td><td>Poważna</td><td>2</td><td>−1K każda</td></tr>
<tr><td>od podwójnego Progu</td><td>Krytyczna</td><td>1</td><td>−2K, potrzebna opieka</td></tr></table>
<ul><li>Gdy brakuje miejsc danego rodzaju, rana staje się cięższa. Gdy zabraknie miejsca na Krytyczną, jesteś <b>wyeliminowany</b>.</li>
<li><b>Wyeliminowany to nie martwy.</b> Po scenie przychodzi Konsekwencja: niewola, przesłuchanie, utrata sprzętu, blizna, dług, upokorzenie albo kłopoty kogoś bliskiego.</li>
<li><b>Śmierć</b> grozi tylko przy <b>Stawce Śmierci</b>, którą MG ogłasza przed konfliktem (Psychonauta, egzekucja, maruderzy), albo gdy sam ją wybierzesz dla swojej postaci.</li>
<li>Lekkie rany znikają po odpoczynku. Poważna goi się tydzień albo szybciej z pomocą medyka. Krytyczna wymaga tygodni opieki, a bez niej zostaje blizna.</li></ul>
"""),
("Walka", """
<ul><li><b>Inicjatywa</b> raz na początku starcia: Psyche + Refleks. Dwa Wyzwalacze dają dodatkową akcję w pierwszej rundzie.</li>
<li><b>Tura:</b> jedna akcja i przejście o jedną strefę. Przejście o dwie strefy zabiera całą turę (bieg) i daje +1 Obrony.</li>
<li><b>Strefy zamiast metrów:</b> <b>Zwarcie</b> (na wyciągnięcie ręki), <b>Blisko</b> (kilka kroków: rzut nożem, pistolet bez kary), <b>Daleko</b> (druga strona placu: tylko broń palna, łuk, kusza) i <b>Poza zasięgiem</b> (tylko broń „Daleko+” po celowaniu). Mapa ilustruje scenę, nie odmierza kroków.</li>
<li><b>Atak:</b> Bijatyka, Broń biała albo Strzelectwo przeciw <b>Obronie</b> celu (zwykle 1). Trafienie: obrażenia + Wyzwalacze, potem pancerz i rana.</li>
<li>Zamiast obrażeń Wyzwalacze możesz wydać na efekt: rozbroić, powalić, przyszpilić, odrzucić albo zająć lepszą pozycję.</li>
<li><b>Obrona:</b> 1 bazowo, +1 za osłonę, +1 za ruch, +1 za tarczę lub teren, +2 za ciemność albo gdy cel jest Daleko.</li>
<li><b>Aktywna obrona:</b> za 1 Ego rzucasz Mobilność, Broń białą albo Bijatykę w Starciu z atakującym. Wygrana wręcz z 3 Wyzwalaczami to kontratak.</li>
<li><b>Bandy</b> walczą jak jedna postać: jeden atak na rundę z premią za liczebność, a każda rana zabiera kilku członków.</li>
<li><b>Z walki zawsze można wyjść:</b> ucieczką, kapitulacją albo rozmową. Gdy przywódca wroga jest poważnie ranny, MG zaproponuje negocjacje.</li></ul>
"""),
("Sepsa, Burn i Szept Prymera", """
<p><b>Zarażenie</b> rośnie od zarodników, pól spor, Burnu i kontaktu z Prymerem. Maksimum to (Psyche + Wiara albo Wola)×2.</p>
<ul><li>Od połowy skali na piersi wykwita <b>stygmat</b>, a wizje przychodzą same.</li>
<li>Powyżej maksimum walczysz o duszę rzutem Psyche + Wiara/Wola. Każda porażka zostawia trwały ślad. Postać, której trwałe Zarażenie dojdzie do połowy skali, staje się <b>Leperosem</b>. Ostatnia scena należy wtedy do jej gracza.</li>
<li><b>Burn</b> daje Ego i moc zależną od odmiany, ale podnosi Zarażenie. Trzy dawki w tygodniu to początek <b>Głodu</b>.</li></ul>
<div class="box"><h4>Szept Prymera</h4><p>Gdy masz choć 1 punkt Zarażenia, MG może zaproponować ci <b>Szept</b>: wizję, która zawiera prawdziwą, choć zniekształconą wskazówkę, +2K, przeczucie, gdzie czai się Psychonauta, albo zrozumienie mowy owadów przez scenę. Za przyjęcie płacisz +1 Zarażenia (za silny Szept +2). <b>Odmowa nic nie kosztuje.</b> Czasem Szept jest jedyną drogą do prawdy, a czasem pułapką.</p></div>
"""),
("Między przygodami", """
<p><b>Interludium</b> to czas między scenami albo przygodami. Każda postać ma w nim <b>2 akcje</b>:</p>
<ul><li><b>Leczenie</b> ran.</li><li><b>Śledzenie tropu:</b> zdobywasz Odsłonę, ale tyka zegar.</li>
<li><b>Służba kultowi:</b> odzyskujesz Zaplecze i dostajesz zadanie.</li><li><b>Handel</b> albo zbieranie złomu.</li>
<li><b>Plotki:</b> jedna prawdziwa i jedna fałszywa, ale nie wiesz która jest która.</li>
<li><b>Przygotowanie:</b> tworzysz Cechę na następną scenę.</li><li><b>Więź:</b> czas z bliską osobą przywraca całe Ego.</li>
<li><b>Odwyk</b> od Burnu.</li></ul>
<p>Świat w tym czasie żyje: frakcje realizują swoje plany, a długi rosną.</p>
<h4>Doświadczenie (PD)</h4>
<table><tr><th>Za co</th><th>PD</th></tr><tr><td>Udział w sesji</td><td>5</td></tr><tr><td>Ważny Wniosek</td><td>+2</td></tr>
<tr><td>Odkryty Sekret</td><td>+2</td></tr><tr><td>Przyjęta Pokusa Archetypu</td><td>+1</td></tr><tr><td>Ideał albo Więź ponad własny interes</td><td>+1</td></tr></table>
<p><b>Koszty:</b> atrybut: nowa wartość ×12 (z bonusem Kultury, Konceptu lub Kultu ×10). Umiejętność: nowa wartość ×5 (z bonusem ×4). Potencjał: suma poziomów ×10. Zaplecze rośnie tylko przez czyny w fikcji.</p>
"""),
]

CREATION = """
<p>Postać możesz zrobić na dwa sposoby. W Foundry: utwórz aktora typu Postać, otwórz kartę i kliknij <b>Kreator</b> w nagłówku, a program sam policzy punkty. Na papierze: weź <b>kartę postaci</b> z końca podręcznika i przejdź kroki poniżej. Oba sposoby dają tę samą postać.</p>
<div class="box"><h4>Trzy zasady liczenia</h4><ul>
<li><b>Punkty wydajesz 1:1.</b> Jeden punkt to +1 do jednej cechy. Nie ma rosnących kosztów przy tworzeniu (rosnące koszty PD dotyczą dopiero rozwoju).</li>
<li><b>Atrybuty zaczynają od 1, umiejętności i Zaplecze od 0.</b> 10 punktów atrybutów dokładasz ponad te jedynki, więc suma atrybutów nowej postaci wynosi zawsze 16.</li>
<li><b>Bonus = limit +1.</b> Gdy Kultura, Koncept albo Kult daje bonus do cechy, jej maksimum przy tworzeniu rośnie o 1. Bonusy z różnych źródeł się sumują. Bonus nie daje darmowego punktu, a później obniża koszt rozwoju tej cechy (×10 zamiast ×12 dla atrybutu, ×4 zamiast ×5 dla umiejętności).</li></ul></div>
<h3>Krok po kroku</h3>
<ol class="steps">
<li><b>Kultura.</b> Wybierz region pochodzenia (Część II). Zapisz na karcie, które dwa atrybuty i które umiejętności mają bonus: postaw przy nich gwiazdkę ☆ w kratce „bonus”.</li>
<li><b>Koncept.</b> Wybierz kartę Tarota (tabela niżej). Dostawiasz gwiazdkę przy jednym atrybucie i 2–3 umiejętnościach. Wpisz Cień Konceptu.</li>
<li><b>Kult.</b> Wybierz kult (Część III). Kult daje gwiazdki tylko umiejętnościom. Teraz policz limity: atrybut ma maksimum <b>3 + liczba gwiazdek</b>, umiejętność <b>2 + liczba gwiazdek</b>. Wpisz je w kolumnę „maks.”.</li>
<li><b>Ścieżka.</b> Skreśl jedną umiejętność z pary <i>Skupienie</i> (Intelekt) / <i>Pierwotność</i> (Instynkt) i jedną z pary <i>Wiara</i> / <i>Wola</i> (Psyche). Skreślona zostaje na 0 na zawsze. Skupienie albo Pierwotność zasila Ego, a Wiara albo Wola chroni przed Sepsą.</li>
<li><b>Atrybuty: 10 punktów.</b> Wpisz 1 przy każdym z sześciu atrybutów, potem rozdaj 10 punktów, nie przekraczając limitów. Sprawdź: suma = 16.</li>
<li><b>Umiejętności: 28 punktów.</b> Jest ich 36, po sześć przy każdym atrybucie. Wszystkie startują od 0. Rozdaj 28 punktów, nie przekraczając limitów i omijając skreślone. Nie musisz mieć wszystkiego: zero znaczy tylko, że rzucasz samym atrybutem.</li>
<li><b>Pule.</b> Przy każdej umiejętności wpisz pulę: atrybut + umiejętność. To liczba kości, którą rzucasz. Te liczby są też wymaganiami rang.</li>
<li><b>Zaplecze: 4 punkty</b>, maksimum 3 w jednym: Sojusznicy, Autorytet, Sława, Zasoby, Sekrety, Sieć.</li>
<li><b>Ranga.</b> Zaczynasz od rangi poziomu 1. Możesz wejść wyżej, jeśli spełniasz wymagania kolejnej rangi i wszystkich poprzednich w łańcuchu (np. „Intelekt + Medycyna 4” znaczy pula co najmniej 4). Rangi z dopiskiem „kampania” zdobywa się tylko w grze. Wpisz ekwipunek z wybranej rangi i rang niższych.</li>
<li><b>Potencjał.</b> Jeden, na poziomie 1: z listy twojego kultu albo ogólny. Musisz spełniać jego wymaganie.</li>
<li><b>Wartości pochodne.</b> <b>Ego</b> maks. = (Intelekt + Skupienie) ×2 albo (Instynkt + Pierwotność) ×2. <b>Zarażenie</b> maks. = (Psyche + Wiara albo Wola) ×2. <b>Próg</b> ran = Ciało + Twardość. <b>Obrona</b> = 1. <b>Pieniądze</b> = (poziom rangi + Zasoby) × stawka kultu (tabela niżej). Ego zaczyna pełne, Zarażenie na 0.</li>
<li><b>Człowiek.</b> Imię, <b>Ambicja</b> (czego chcesz), <b>Tajemnica</b> (czego nikt nie może wiedzieć) i 1–2 <b>Więzi</b> (osoby, miejsca albo ideały spoza kultu).</li></ol>
<table class="small"><tr><th>Kult</th><th>Stawka</th><th>Kult</th><th>Stawka</th></tr>
<tr><td>Anabaptyści, Hellveci, Klanowcy, Palerzy, Sędziowie, Złomiarze</td><td>50 CD</td><td>Spitalianie, Jehammedanie</td><td>100 CD</td></tr>
<tr><td>Kronikarze</td><td>128 CD</td><td>Apokaliptycy</td><td>200 CD</td></tr>
<tr><td>Anubianie, Skurgerzy</td><td>100 Dinarów</td><td>Neolibijczycy</td><td>1000 Dinarów</td></tr></table>

<h3>Przykład: Ida Rehm, Spitalianka</h3>
<div class="box">
<p><b>1–3. Pochodzenie.</b> Borca (☆ Zręczność, Instynkt; ☆ Twardość, Artefakty, Inżynieria, Rzemiosło, Przetrwanie). Koncept VI Uzdrowiciel (☆ Zręczność; ☆ Medycyna, Rzemiosło). Kult Spitalianie (☆ Twardość, Medycyna, Nauka, Percepcja, Wiara, Wola).<br>
Limity: Zręczność 3+2 = <b>5</b>, Instynkt <b>4</b>, reszta atrybutów 3. Twardość, Medycyna i Rzemiosło mają po dwie gwiazdki, więc limit <b>4</b>. Artefakty, Inżynieria, Przetrwanie, Nauka, Percepcja, Wiara i Wola: <b>3</b>. Pozostałe: 2.</p>
<p><b>4. Ścieżka.</b> Skupienie (skreśla Pierwotność) i Wiara (skreśla Wolę).</p>
<p><b>5. Atrybuty</b> (1 + wydane): Ciało 2 (+1), Zręczność 3 (+2), Charyzma 2 (+1), Intelekt 3 (+2), Psyche 3 (+2), Instynkt 3 (+2). Wydane 10, suma 16.</p>
<p><b>6. Umiejętności</b> (28): Medycyna 4, Twardość 3, Nauka 3, Wiara 3, Percepcja 2, Skupienie 2, Empatia 2, Rzemiosło 2, Kondycja 2, Refleks 2, Broń biała 1, Obycie 1, Atletyka 1. Reszta 0.</p>
<p><b>7. Pule</b> (przykłady): Intelekt + Medycyna 7, Intelekt + Nauka 6, Ciało + Twardość 5, Instynkt + Percepcja 5, Psyche + Wiara 6, Ciało + Broń biała 3.</p>
<p><b>8. Zaplecze</b> (4): Zasoby 2, Sojusznicy 1, Sieć 1.</p>
<p><b>9. Ranga.</b> Rekrut (poziom 1) bez wymagań. Sanitariusz (poziom 2) chce Intelekt + Medycyna 4 (ma 7) i Ciało + Kondycja 4 (ma 4): spełnione. Spełnia nawet wymagania Famulancera (poziom 3), ale gracz woli zacząć nisko i bierze Sanitariusza. Ekwipunek: podręcznik, skórzany fartuch i kombinezon spitaliański.</p>
<p><b>10. Potencjał.</b> Nauki Kranzlera (wymaga Skupienia, które Ida ma).</p>
<p><b>11. Pochodne.</b> Ego (3 + 2) ×2 = <b>10</b>. Zarażenie maks. (3 + 3) ×2 = <b>12</b>. Próg 2 + 3 = <b>5</b>. Obrona 1. Pieniądze (2 + 2) × 100 = <b>400 CD</b>.</p>
<p><b>12. Człowiek.</b> Ambicja: wrócić do Justitian z lekiem na „suchy kaszel”. Tajemnica: raz spaliła żywcem pacjenta, który nie był zarażony. Więź: młodszy brat w szkole Kronikarzy.</p></div>
<div class="box"><h4>Rada</h4><p>Najpierw wybierz kult i pomyśl, kim jesteś w jego szeregach. Potem zadaj sobie trzy pytania: Kogo kochasz? Komu jesteś winien? Czego się wstydzisz? Odpowiedzi to najlepsze haki dla MG.</p></div>
"""

GLOSSARY = [
("Burn", "narkotyk z pól spor; daje moc, odbiera duszę"),
("Cecha", "właściwość miejsca lub sceny; wywołana daje +2K"),
("Cień", "ciemna strona twojego Archetypu"),
("Drafty", "pieniądz Kronikarzy"),
("Dźwignia", "wiedza o czyimś Motywie, Lęku, Sekrecie lub Cenie"),
("Ego", "odporność psychiczna i waluta na kości"),
("Eshaton", "deszcz asteroid, który zakończył dawny świat"),
("Imię", "reputacja drużyny u frakcji (−3…+3)"),
("Interludium", "czas między scenami; 2 akcje na postać"),
("K", "kość k6; „+2K” to dwie dodatkowe kości"),
("Leperos", "człowiek, któremu Prymer odebrał duszę"),
("Odsłona", "dodatkowa informacja w śledztwie"),
("Próg", "Ciało + Twardość; wyznacza ciężkość ran"),
("Prymer", "obca siła, która przyszła z asteroidami"),
("Psychonauta", "dziecko Prymera, następny gatunek"),
("Sepsa", "grzyb Prymera, źródło Zarażenia"),
("Stawka Śmierci", "ogłoszona z góry sytuacja, w której można zginąć"),
("Szept", "oferta Prymera: wizja lub siła za Zarażenie"),
("Trop kluczowy", "informacja, którą zawsze dostajesz bez rzutu"),
("Wyzwalacz", "każda szóstka; kupuje Efekt"),
("Zaplecze", "pomoc twojego kultu (6 rodzajów)"),
("Zegar", "licznik planu antagonisty albo długiego zadania"),
]

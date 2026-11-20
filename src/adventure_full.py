# -*- coding: utf-8 -*-
"""Pełna przygoda „Ciche studnie”: teksty do czytania, sceny, handouty."""

def read(txt):
    return f'<blockquote class="d2-read"><p>{txt}</p></blockquote>'

def gm(txt):
    return f'<div class="d2-gmnote"><p>{txt}</p></div>'

ADVENTURE = [
("0. Zanim zaczniesz", """
<p><b>Ciche studnie</b> to przygoda startowa na 1–2 sesje (6–8 godzin) dla 3–5 graczy. Dzieje się w dzielnicy Dostawców w Justitian, mieście Sędziów w Borce. To śledztwo z rozmowami w centrum. Walka może się zdarzyć, ale nie musi.</p>
<h3>Co jest w pakiecie</h3>
<ul><li><b>Sceny</b> (kompendium „Quick start: sceny”): plan dzielnicy i 4 mapy taktyczne (targ ze studnią, lazaret, spelunka Kruków, kancelaria Vargi).</li>
<li><b>Aktorzy</b> (kompendium „Quick start: aktorzy”): Śledztwo, Lokacja, 2 Frakcje, Rejestr Długów, NPC z portretami i tokenami.</li>
<li><b>Gotowe postacie</b>: 7 postaci graczy z historią, portretem i tokenem, każda z osobistym hakiem w tej przygodzie.</li>
<li><b>Dźwięk</b>: playlista „Degenesis — Odgłosy” (deszcz, noc, podziemia) i „Efekty” (dzwony, alarm). Muzykę dobierz sam — propozycje utworów są w „Szkole MG”.</li></ul>
<h3>Jak czytać ten dziennik</h3>
<p>Ramki z cytatem to <b>teksty do przeczytania graczom</b>. Szare ramki to <b>notatki dla ciebie</b>. Każda scena ma: tekst wejściowy, Cechy miejsca (jawne i ukryte), kto tu jest, tropy kluczowe (zawsze do zdobycia), Odsłony (nagrody za dobre rzuty), komplikacje, mapę i muzykę.</p>
""" + gm("Jeśli to twoja pierwsza sesja jako MG, przeczytaj najpierw dziennik <b>Szkoła MG: pierwsza sesja</b>. Prowadzi przez przygotowanie w Foundry, rytm sesji i każdą mechanikę na przykładach z tej przygody.")),

("1. Prawda i zegary (tylko MG)", """
<p><b>Co się naprawdę dzieje:</b> Sędzia miejski <b>Varga</b> odpowiada za spokój w dzielnicy Dostawców, która karmi Justitian. Za dwa tygodnie przyjeżdża Senator, a Dostawcy szykują strajk. Varga zapłacił <b>Kruczemu Stadu</b> (Apokaliptykom) za „uspokojenie dzielnicy”. Kruki od tygodnia nocą wlewają do studni przy Bramie Wschodniej rozcieńczony Burn <b>Unity</b>. Ludzie robią się łagodni, posłuszni, uśmiechnięci. Ale Burn zaraża i najwrażliwsi zaczynają chorować.</p>
<p><b>Spitalianie</b> widzą objawy Sepsy bez pola spor i bez Leperosa. Podejrzewają Psychonautę ukrytego pod miastem. Higienista <b>Kessel</b> chce kwarantanny i ognia, brat <b>Tobiasz</b> ma wątpliwości.</p>
<p><b>Głębsza warstwa</b> (na przyszłość): chorzy śnią ten sam sen o „matce pod miastem”. To Prymer odpowiadający na Burn w wodzie. Tę nić możesz zostawić otwartą na kampanię.</p>
<h3>Kto czego chce</h3>
<table><tr><th>Kto</th><th>Chce</th><th>Boi się</th><th>Sekret</th></tr>
<tr><td>Sędzia Varga</td><td>spokoju przed Senatorem</td><td>że Kodeks go dosięgnie</td><td>zapłacił Krukom</td></tr>
<tr><td>Ilsa Kruczyca (Kruk Stada)</td><td>zapłaty i długu Vargi</td><td>że Burn kogoś zabije i wina spadnie na Stado</td><td>ma list z pieczęcią Vargi</td></tr>
<tr><td>Higienista Kessel</td><td>wypalić „ognisko”</td><td>Psychonauty w mieście</td><td>dostał rozkaz, by nie pytać Sędziów</td></tr>
<tr><td>Brat Tobiasz</td><td>wyleczyć ludzi</td><td>Kessela</td><td>wie, że to Burn, ale nie ma dowodu</td></tr>
<tr><td>Halka, przekupka</td><td>ochronić syna</td><td>że syn pił wodę</td><td>syn nosi beczki dla Kruków</td></tr></table>
<h3>Zegary (na aktorach Śledztwo i Frakcje)</h3>
<ul><li><b>Epidemia</b> (8, start 2): +1 co dzień gry, +1 za hałas (Koszt), +1 za Zgrzyt w dzielnicy. Na 4: pierwsi chorzy umierają. Na 6: Kessel ogłasza kwarantannę. Na 8: ogień.</li>
<li><b>Dostawa dla Sędziego</b> (Kruki, 6, start 3): +1 każdej nocy. Na 6 Kruki kończą, sprzątają magazyn i znikają z dowodami.</li>
<li><b>Kwarantanna i podpalenie</b> (Spitalianie, 6, start 1): +1, gdy postacie coś przed Spitalem ukrywają albo Kessel zobaczy kolejnego chorego. Cofa się, gdy dostarczą mu dowód na Burn.</li></ul>
""" + gm("Zegary to twoja presja zamiast ryzyka śmierci. Przesuwaj je jawnie („słyszycie dzwon z lazaretu, kolejny zmarły”). Gracze, którzy widzą tykający zegar, sami przyspieszają.")),

("2. Otwarcie", read("Justitian budzi się w szarym świcie. Nad dzielnicą Dostawców wisi smród gnijących warzyw, dymu i wapna. Od tygodnia jest tu za cicho. Tragarze nie kłócą się o miejsce przy bramie, przekupki nie przekrzykują się nad koszami, dzieci nie biegają między wozami. Ludzie uśmiechają się do siebie łagodnie, jak po dobrym winie, i zapominają, co mieli zrobić.") +
 read("Przy Bramie Wschodniej studnię oplata łańcuch z pieczęcią Spitalu: biały krzyż w okręgu. Obok stoi Sędzia w szerokim kapeluszu i patrzy na tłum tak, jakby wszyscy byli winni. Z lazaretu dochodzi dzwon. Ktoś znów umarł z uśmiechem na ustach.") + """
<h3>Dlaczego postacie tu są (haki osobiste)</h3>
<ul><li><b>Siostra Wera</b> (Spitalianka): jej brat Lew, tragarz, leży w lazarecie. Kessel każe jej trzymać się z daleka od sprawy.</li>
<li><b>Oddo</b> (Sędzia miejski): Varga osobiście przydzielił go do patrolu przy studni z rozkazem „nikogo nie dopuszczać i o nic nie pytać”.</li>
<li><b>Kasia „Sroka”</b> (Apokaliptyczka): Stado kazało jej „pilnować, żeby nikt nie węszył”, a ona wie, co jest w beczkach.</li>
<li><b>Mirek „Borsuk”</b> (Złomiarz): sprzedał Krukom mapę kanałów pod dzielnicą i dopiero teraz rozumie, do czego jej użyli.</li>
<li><b>Kapral Anja Reiss</b> (Hellwetka): jej ostatni żołnierz, Pit, leży w lazarecie. Forteca każe jej obserwować Sędziów, a nie się wtrącać.</li>
<li><b>Brat Kaspar</b> (Anabaptysta): rozpoznaje objawy Burnu Unity, bo kiedyś sam go brał, i wie, że w tym mieście handlują nim Kruki. Ilsa pamięta jego stary dług.</li>
<li><b>Modus</b> (Kronikarz): Klaster zauważył spadek wydajności dzielnicy o jedną trzecią i chce wiedzieć dlaczego, zanim zrobią to Sędziowie.</li></ul>
""" + gm("Zacznij od krótkiej sceny dla każdej postaci (1–2 minuty): Wera przy łóżku brata, Oddo dostaje rozkaz od Vargi, Sroka odbiera polecenie od Ilsy, Borsuk widzi swoją runę ostrzegawczą zamalowaną na włazie kanału, Modus odbiera raport z Alkowy, Anja szuka Pita w lazarecie, a Kaspar wącha osad na kubku chorego i zaciska pięść. Potem zbierz ich przy studni: tłum, kolejny chory pada na bruk i wszyscy są na miejscu. Tak drużyna formuje się sama.") + """
<p><b>Mapa:</b> „Plan dzielnicy”, potem „Targ i studnia”. <b>Dźwięk:</b> „Mżawka” z Odgłosów, a na koniec sceny „Dzwony” z Efektów.</p>
"""),

("A. Lazaret Spitalian", read("Wapno chrzęści pod butami. Długa sala, dwa rzędy łóżek, na każdym ktoś, kto się uśmiecha. Kobieta nuci kołysankę do sufitu. Mężczyzna w kącie głaszcze ścianę, jakby była żywa. Między łóżkami chodzi Spitalianin w masce z goglami i liczy oddechy.") + """
<p><b>Cechy:</b> „Smród wapna i strachu”, „Za mało łóżek”. Ukryta: „Brat Tobiasz ma wątpliwości” (odkrywa Instynkt + Empatia albo szczera rozmowa).</p>
<p><b>Kto tu jest:</b> Higienista Kessel (Nieufny, Spitalianin wysokiej rangi), brat Tobiasz (Życzliwy wobec Wery), chorzy, w tym brat Wery, Lew.</p>
<p><b>Tropy kluczowe:</b></p>
<ol><li>Chorują tylko ludzie pijący ze studni przy Bramie. Z innych studni nikt. → <b>C</b></li>
<li>W ślinie chorych są białe włókna, ale Mollusk reaguje słabo. To nie wygląda na zwykłą Sepsę. → <b>C</b> albo <b>D</b></li>
<li>Chorzy śnią ten sam sen o „matce pod miastem”. → <b>E</b></li></ol>
<p><b>Odsłony:</b> objawy przypominają odurzenie Burnem Unity, a nie chorobę (Intelekt + Medycyna z Wyzwalaczem); Kessel ma rozkaz „nie pytać Sędziów” (Dźwignia na Kessela); Tobiasz odda próbki za obietnicę ochrony przed Kesselem (tworzy <b>dług Drobny</b> Tobiasza wobec drużyny albo odwrotnie).</p>
<p><b>Komplikacje:</b> Kessel każe wszystkim przejść oczyszczanie wapnem (−1 Ego, zgubiony sprzęt); Lew w majakach mówi o „beczkach w nocy” przy wszystkich, co spala Srokę przed drużyną, jeśli jest obecna.</p>
""" + gm("Metoda Spitalian (sekcja, testy) daje Werze automatyczną Odsłonę raz na scenę. To dobry moment, by pokazać graczom, że ich kult ma znaczenie w śledztwie.") + "<p><b>Mapa:</b> Lazaret. <b>Muzyka:</b> „Lazaret”.</p>"),

("B. Targ przy Bramie Wschodniej", read("Targ żyje, ale jakoś wolniej. Kupcy podają towar z uśmiechem i zapominają wziąć zapłatę. Tragarze siedzą na skrzyniach i patrzą w niebo. Tylko jedna przekupka, stara i twarda jak rzemień, ogląda się nerwowo na studnię i na Sędziów.") + """
<p><b>Cechy:</b> „Tłum, w którym łatwo zniknąć”, „Patrole Sędziów co kwadrans”. Ukryta: „Przekupki widzą wszystko” (darmowe wywołanie dla odkrywcy).</p>
<p><b>Kto tu jest:</b> Halka (Nieufna), tragarze, patrol Sędziów.</p>
<p><b>Tropy kluczowe:</b></p>
<ol><li>Halka widziała nocą wóz z beczkami bez znaków, który jechał od strony kanałów. → <b>D</b></li>
<li>Tragarze płacą za piwo dinarami, choć zarabiają w Draftach. Ktoś płaci im po afrykańsku. → <b>D</b></li>
<li>Sędziowie pilnują studni od tygodnia, czyli zanim ktokolwiek zachorował. → <b>F</b></li></ol>
<p><b>Halka:</b> Motyw: utrzymać stragan i syna. Lęk: że syn pił wodę. Sekret: syn nosi beczki dla Kruków. Cena: lekarstwo dla syna albo glejt od Sędziów. Gdy postacie użyją Dźwigni (lęk o syna, Wera z lekarstwem, Oddo z glejtem), Halka mówi wszystko. Jeśli ochronią syna, ma u nich <b>dług Drobny</b>.</p>
""" + gm("To idealne miejsce, żeby nauczyć graczy Postawy i Dźwigni. Pierwsza próba „po prostu ją przekonać” ma Trudność 3 (Nieufna) +1 (istotna prośba) = 4. Gdy gracze odkryją lęk o syna, dostają +2K albo prośba staje się łatwa.") + "<p><b>Mapa:</b> Targ i studnia. <b>Muzyka:</b> „Wiatr nad dzielnicą”.</p>"),

("C. Studnia", read("Łańcuch jest gruby, pieczęć świeża. Z dołu ciągnie chłód i coś jeszcze, słodkawy zapach, jak od zwiędłych kwiatów. Na kamiennej cembrowinie osiada biały pył, cienki jak mąka. Gdy się nachylasz, przez moment wydaje ci się, że ktoś na dole nuci.") + """
<p><b>Cechy:</b> „Łańcuch i pieczęć Spitalu”, „Wilgoć i ciemność”. Ukryta: „Ślady ciągnięcia beczek po bruku” (prowadzą w stronę kanałów).</p>
<p><b>Tropy kluczowe:</b></p>
<ol><li>Na cembrowinie biały, słodkawy osad, którego nie wyczuwa Mollusk. → <b>A</b> albo <b>D</b></li>
<li>Świeże rysy po linie, jakby coś spuszczano nocą. → <b>D</b></li>
<li>W szczelinie tkwi czarne pióro, znak Kruczego Stada. → <b>D</b></li></ol>
<p><b>Sporyzacja:</b> kto schodzi do studni albo wącha osad bez maski, rzuca Ciało + Twardość (2). Porażka daje +1 Zarażenie. Kto ma Zarażenie ≥ 1, może dostać pierwszy <b>Szept Prymera</b>:</p>
""" + read("Ciepło. Wszyscy razem, wszyscy spokojni, nikt nie musi się bać. Dzielnica oddycha jednym oddechem jak śpiące dziecko. Wystarczy przestać się opierać…") + """
<p>Jeśli gracz przyjmie Szept (+1 Zarażenie), powiedz mu wprost: <i>to Burn Unity, dużo, rozcieńczony w wodzie</i>. To prawdziwa Odsłona za cenę ciała.</p>
""" + gm("Zatrzymaj się tu na chwilę i zapytaj gracza: „Chcesz to poczuć? Dostaniesz odpowiedź, ale Prymer cię dotknie”. To najlepszy moment, żeby pokazać, czym jest Degenesis.") + "<p><b>Mapa:</b> Targ i studnia. <b>Muzyka:</b> „Studnia”.</p>"),

("D. Pod Złamanym Skrzydłem", read("Dym, muzyka i śmiech. Na ścianach wiszą kości ptaków i karty Tarota przybite nożami. Za barem łysy Apokaliptyk poleruje kufel. Pod sceną ktoś przegrywa ostatnią koszulę. Za czerwoną kurtyną, przy której stoi dwóch tragarzy, coś bieleje w półmroku.") + """
<p><b>Cechy:</b> „Dym, kości i muzyka”, „Każdy coś jest winien Krukom”. Ukryta: „Magazyn za kurtyną” (beczki z resztkami białego pyłu).</p>
<p><b>Kto tu jest:</b> Ilsa Kruczyca (Kruk Stada, Obojętna; dla Sroki Życzliwa), banda tragarzy Kruków (6 osób), goście.</p>
<p><b>Tropy kluczowe:</b></p>
<ol><li>W magazynie stoją beczki z resztkami białego pyłu, czyli Burnu Unity. → <b>F</b></li>
<li>Ilsa wie, kto płaci, i sprzeda to za <b>dług Poważny</b> albo za ochronę Stada przed winą. → <b>F</b></li>
<li>Wóz w zaułku rusza o świcie (zegar Dostawy). Kto go zatrzyma, ma beczki jako dowód. → <b>F</b></li></ol>
<p><b>Ilsa:</b> Motyw: zapłata i dług Vargi. Lęk: że wina spadnie na Stado. Sekret: ma list z pieczęcią Vargi (handout). Cena: dług albo obietnica, że Kruki wyjdą z tego czyste.</p>
<p><b>Walka (opcjonalnie):</b> banda tragarzy (Banda, liczebność 6, morale pęka po 3 stratach). To nie jest Stawka Śmierci. Pokonani gracze budzą się w zaułku bez sakiewek, z długiem wobec Kruków za „darowane życie”.</p>
""" + gm("Kruk woli dłużnika niż trupa. Zanim padnie pierwszy cios, Ilsa proponuje rozmowę. Pokaż graczom, że w tej grze walka jest tylko jedną z opcji.") + "<p><b>Mapa:</b> Spelunka Kruków. <b>Muzyka:</b> „Napięcie” (walka) albo muzyka z listy (spelunka).</p>"),

("E. Sny chorych", read("Stary tragarz łapie cię za rękę zaskakująco mocno. „Ona jest pod nami” — szepcze z uśmiechem. — „Ciepła. Mówi, że już nie musimy się bać. Sędzia pił z nami wino w zeszłym tygodniu. A potem woda zrobiła się słodka.”") + """
<p>Rozmowy z chorymi w domach dzielnicy (Instynkt + Empatia, Trudność 2) albo w wizji przez Szept Prymera.</p>
<p><b>Tropy kluczowe:</b></p>
<ol><li>Wszyscy śnią to samo: „matkę pod miastem”. → zostaw jako nić kampanii</li>
<li>Sen nasila się po wypiciu wody. → <b>C</b></li>
<li>„Sędzia pił z nami wino, a potem woda zrobiła się słodka.” Varga był w dzielnicy dzień przed pierwszym zatruciem. → <b>F</b></li></ol>
""" + gm("Ta scena to horror, nie akcja. Mów cicho, rób pauzy. Puść „Studnię” albo „Lazaret” i pozwól graczom się bać.") + "<p><b>Mapa:</b> Plan dzielnicy (teatr wyobraźni). <b>Muzyka:</b> „Studnia”.</p>"),

("F. Kancelaria Sędziego Vargi", read("Hala sądowa pachnie woskiem i starym papierem. Na pulpicie leży Kodeks, otwarty na rozdziale o porządku publicznym. Sędzia Varga nie wstaje zza biurka. Kapelusz zdjął, ale rękę trzyma na młocie. „Słucham. Krótko. Mam miasto do pilnowania.”") + """
<p><b>Cechy:</b> „Kodeks na pulpicie”, „Dwaj Protektorzy przy drzwiach”. Ukryta: „Księga wydatków z podwójnymi wpisami” (Kronikarz albo Intelekt + Nauka, Trudność 3).</p>
<p><b>Varga:</b> Obojętny. Motyw: spokój przed Senatorem. Lęk: że Kodeks go dosięgnie. Sekret: zapłacił Krukom. Cena: czyjaś głowa zamiast jego. Bez Dźwigni nie powie nic i każe wyprowadzić gości. Każdy dowód (księga, pióro, beczki, list Ilsy, zeznanie chorego) to Dźwignia: +2K i coraz mniej miejsca na kłamstwa. Przy trzech dowodach zaczyna negocjować.</p>
""" + gm("Oddo w tej scenie stoi przed wyborem: lojalność wobec przełożonego czy wobec Kodeksu. Nie rozstrzygaj tego za gracza. Zaproponuj Pokusę Archetypu: „Sprawiedliwy dzieli świat na winnych i niewinnych, a ty jesteś zawsze po właściwej stronie. Czy aby na pewno?”") + "<p><b>Mapa:</b> Kancelaria Vargi. <b>Muzyka:</b> „Napięcie”.</p>"),

("G. Finał i epilogi", """
<table><tr><th>Rozwiązanie</th><th>Co się dzieje</th><th>Imię i długi</th></tr>
<tr><td>Zdemaskować Vargę przed Sędziami</td><td>Arbiter odbiera Vargę; Kruki mszczą się na informatorach</td><td>Sędziowie Echo +2; Krucze Stado Echo −2; Halka ma dług, jeśli ją chroniono</td></tr>
<tr><td>Szantażować Vargę</td><td>Varga odwołuje Kruki, ale zostaje u władzy</td><td>Varga ma dług Krwawy (ukryty); wróg osobisty</td></tr>
<tr><td>Wydać wszystko Spitalianom</td><td>kwarantanna bez ognia, chorzy na badania</td><td>Spitalianie Echo +2; Dostawcy pamiętają</td></tr>
<tr><td>Dogadać się z Krukami</td><td>Kruki kończą za dobrą cenę</td><td>dług Poważny wobec Stada; Sędziowie podejrzliwi</td></tr>
<tr><td>Spóźnić się</td><td>zegar epidemii pełny: ogień</td><td>Imię −1 u wszystkich; −Ego dla świadków</td></tr></table>
<h3>Epilogi do przeczytania</h3>
""" + read("<b>Gdy prawda wyszła na jaw:</b> Trzy dni później studnię odpieczętowano. Woda znów jest gorzka i zimna, a dzielnica znów krzyczy, kłóci się i targuje. Nigdy nie była piękniejsza. Tylko chorzy w lazarecie wciąż czasem nucą tę samą kołysankę.") +
 read("<b>Gdy przyszedł ogień:</b> Spitalianie palili przez całą noc. Rano z dzielnicy Dostawców zostały czarne kikuty domów i zapach wapna. Varga wygłosił mowę o bezpieczeństwie. Senator przyjechał punktualnie.") + """
<p><b>PD:</b> 5 za sesję, +2 za Wniosek „to Burn, nie Psychonauta”, +2 za Sekret (Varga i Kruki), +1 za przyjętą Pokusę Archetypu.</p>
<p><b>Ciąg dalszy:</b> „matka pod miastem”. Borsuk zna kanały. Coś odpowiedziało na Burn w wodzie i teraz wie, gdzie są ludzie.</p>
"""),

("H. Handouty", """
<p>Przeczytaj albo skopiuj graczom, gdy znajdą.</p>
<h3>List z pieczęcią Vargi (u Ilsy)</h3>
""" + read("<i>Do Stada. Spokój w dzielnicy do przyjazdu Senatora. Sposób wasz, cena jak ustalono. Żadnych trupów na bruku. Po wszystkim — nic się nie wydarzyło. — V.</i>") + """
<h3>Notatka Tobiasza (lazaret)</h3>
""" + read("<i>Pacjenci 11–19: euforia, posłuszeństwo, ślinotok z włóknami. Mollusk: reakcja śladowa. Brak pola spor w promieniu kilometra. To nie wygląda na naturalną sporyzację. Raczej na podanie. Higienista nie chce słuchać. — T.</i>") + """
<h3>Księga wydatków Vargi (wpis podwójny)</h3>
""" + read("<i>„Utrzymanie porządku, dzielnica Dostawców — 1200 dinarów.” Dwa wiersze niżej, inną ręką: „Ptaszki — zaliczka”.</i>") + """
<h3>Runa Borsuka</h3>
""" + read("Na włazie kanału ktoś zamalował twoją runę ostrzegawczą świeżą sadzą. Pod spodem wydrapano czarne pióro.")),
]

GM_SCHOOL = [
("1. Przygotowanie w Foundry (45 minut)", """
<p>Zrób to dzień przed sesją, nie godzinę przed. Spokojna głowa jest ważniejsza niż wszystko inne.</p>
<ol><li><b>Zaimportuj sceny</b> z kompendium „Quick start: sceny” (prawy przycisk na kompendium → Importuj wszystko). Jeśli któraś scena nie ma tła, uruchom makro „Utwórz sceny przygody”.</li>
<li><b>Zaimportuj aktorów</b> z „Quick start: aktorzy” i „Gotowe postacie”.</li>
<li><b>Przydziel postacie</b>: Ustawienia → Użytkownicy → przypisz każdemu graczowi postać. Daj graczom uprawnienie <i>Właściciel</i> do aktora <i>Śledztwo: Ciche studnie</i>, bo to ich wspólna tablica.</li>
<li><b>Lokacje</b>: graczom uprawnienie <i>Obserwator</i> do Lokacji. Ukryte Cechy zobaczą dopiero, gdy je ujawnisz (ikonka oka).</li>
<li><b>Sprawdź muzykę:</b> instalator dodał playlisty do zakładki Playlisty. Ustaw głośność muzyki w ustawieniach dźwięku na około 40%.</li>
<li><b>Makra</b>: przeciągnij na pasek „Wyrocznia FU”, „Nowa sesja” i „Nałóż obrażenia na cel”.</li>
<li><b>Przeczytaj</b> raz cały dziennik przygody. Drugi raz przeczytaj tylko tabelę „Kto czego chce” i zegary. To wystarczy.</li></ol>
<p><b>Test techniczny:</b> wejdź jako gracz (drugie okno przeglądarki w trybie incognito) i sprawdź, czy widzisz kartę postaci, Tablicę śledztwa i scenę z targiem.</p>
"""),
("2. Sesja zero w 15 minut", """
<p>Na początku pierwszej sesji, zanim padnie pierwsza kość:</p>
<ol><li><b>Ton</b>: „Gramy w horror postapokaliptyczny. Świat jest okrutny, ale wasze postacie rzadko giną przypadkiem. Częściej płacą: zdrowiem, długami, duszą.”</li>
<li><b>Granice (linie i zasłony)</b>: zapytaj, czego nie chcą w grze wcale (linie) i co ma się dziać tylko poza kadrem (zasłony). W tej przygodzie są choroba, narkotyki, śmierć i manipulacja. Zapytaj o to wprost.</li>
<li><b>Karta X</b>: połóż na stole kartkę z X (albo umów słowo w czacie). Kto ją dotknie, ten fragment znika bez tłumaczenia.</li>
<li><b>Postacie</b>: każdy gracz w 30 sekund mówi, kim jest jego postać i czego chce. Potem jedno pytanie do każdego: „Kogo z drużyny znasz i skąd?”</li>
<li><b>Zasady w 3 zdaniach</b>: „Rzucacie tyle kości, ile macie Atrybut + Umiejętność. Każde 4–6 to sukces, 6 to Wyzwalacz. Ja mówię, ile sukcesów trzeba, a wy mówicie, co robicie, nie co rzucacie.”</li></ol>
"""),
("3. Rytm sesji (4 godziny)", """
<table><tr><th>Czas</th><th>Co</th><th>Uwagi</th></tr>
<tr><td>0:00–0:15</td><td>Sesja zero</td><td>strona 2</td></tr>
<tr><td>0:15–0:35</td><td>Otwarcie: haki osobiste, zbiórka przy studni</td><td>tekst „Otwarcie”, muzyka „Wiatr”</td></tr>
<tr><td>0:35–2:15</td><td>Śledztwo: 3–4 sceny (A–E)</td><td>gracze wybierają kolejność; przesuwaj zegary co scenę</td></tr>
<tr><td>2:15–2:25</td><td>Przerwa</td><td>i ty, i gracze jej potrzebujecie</td></tr>
<tr><td>2:25–3:15</td><td>Spelunka i/lub kancelaria</td><td>tu rosną stawki</td></tr>
<tr><td>3:15–3:45</td><td>Finał</td><td>pozwól graczom wybrać rozwiązanie</td></tr>
<tr><td>3:45–4:00</td><td>Epilog, PD, długi, Imię</td><td>makro „Nowa sesja” na koniec</td></tr></table>
<p><b>Jeśli gracze są wolni</b>, zostań przy jednej sesji i pomiń scenę E. <b>Jeśli są szybcy</b>, Varga ucieka i finał w kanałach (z mapą Borsuka) przenosi się na drugą sesję.</p>
"""),
("4. Jak prowadzić rzut — krok po kroku", """
<p><b>Złota zasada:</b> gracz opisuje, <i>co robi</i>, a ty decydujesz, <i>czy i co rzuca</i>. Nie odwrotnie.</p>
<ol><li><b>Czy w ogóle rzut?</b> Rzucaj tylko, gdy oba wyniki są ciekawe. Otworzenie drzwi to nie rzut. Otworzenie drzwi, zanim patrol skręci, już tak.</li>
<li><b>Który rzut?</b> Wybierz Atrybut + Umiejętność pasujące do opisu. Ściąga jest w Podręczniku gracza.</li>
<li><b>Trudność</b>: zwykle 2. Trudna sytuacja 3, bardzo trudna 4. Nie podawaj 6, chyba że to akt desperacji.</li>
<li><b>Stawka</b>: powiedz, co się stanie przy porażce, zanim rzuci. „Jeśli się nie uda, ktoś cię zauważy.”</li>
<li><b>Wynik</b>: czytaj z karty czatu (Tak, i… / Tak / Tak, ale… / Nie / Nie, i…) i opowiedz go.</li></ol>
<h3>Przykład z przygody</h3>
""" + read("<b>Gracz (Borsuk):</b> Chcę się prześlizgnąć za kurtynę w spelunce, kiedy tragarze patrzą na scenę.<br><b>MG:</b> Rzuć Zręczność + Skradanie, Trudność 3, bo jest ich dwóch, ale są zajęci. Jeśli się nie uda, zauważą cię w połowie drogi.<br><b>Gracz:</b> Mam 5 kości… 6, 5, 3, 2, 1. Dwa sukcesy, jedna szóstka.<br><b>MG:</b> Brakuje ci jednego, więc to „Tak, ale…”. Możesz wejść, ale jeden z tragarzy odwraca się, gdy już jesteś za kurtyną. Słyszysz kroki. Wchodzisz?") + """
<p><b>Uwaga:</b> przy „Tak, ale…” to gracz wybiera, czy przyjmuje koszt. Wyzwalacze przepadają.</p>
"""),
("5. Śledztwo w praktyce", """
<p><b>Najważniejsze:</b> tropu kluczowego nie da się „nie znaleźć”. Jeśli gracz szuka we właściwym miejscu i ma umiejętność, po prostu mu go dajesz. Rzut decyduje o dodatkach.</p>
<h3>Przykład: lazaret</h3>
""" + read("<b>Gracz (Wera):</b> Badam ślinę chorych pod Molluskiem.<br><b>MG:</b> Jesteś Spitalianką, więc od razu widzisz trop: białe włókna, ale Mollusk prawie nie reaguje. To nie jest zwykła Sepsa. Chcesz rzucić Intelekt + Medycyna, żeby dowiedzieć się więcej?<br><b>Gracz:</b> Tak. 3 sukcesy, 1 Wyzwalacz.<br><b>MG:</b> Sukces daje ci Odsłonę: objawy pasują do odurzenia Burnem Unity, nie do choroby. Za Wyzwalacz możesz wziąć drugą Odsłonę albo zrobić to Szybko, zanim wróci Kessel.") + """
<h3>Gdy gracze utkną</h3>
<ul><li><b>Zegar</b>: przesuń go i pokaż skutek („dzwon, kolejny zmarły”).</li><li><b>NPC przychodzi do nich</b>: Halka, Tobiasz albo Ilsa szukają ich sami.</li>
<li><b>Wniosek</b>: zaproponuj rzut na Wniosek z tropów, które już mają.</li><li><b>Zapytaj</b>: „Co twoja postać myśli, że tu się dzieje?” Gracze często wiedzą więcej, niż mówią.</li></ul>
<p>Zapisujcie tropy na aktorze <b>Śledztwo</b>. Niech robi to jeden gracz, „protokolant”.</p>
"""),
("6. Rozmowy i Dźwignia", """
<ol><li><b>Sprawdź Postawę</b> NPC (na jego karcie). Nieufna Halka = Trudność 3.</li>
<li><b>Waga prośby</b>: „powiedz, co widziałaś” to prośba istotna, więc +1. Razem 4.</li>
<li><b>Dźwignia</b>: gdy gracze znają lęk Halki o syna i go użyją, dostają +2K albo prośba schodzi do drobnej.</li>
<li><b>Wynik</b>: sukces to informacja albo lepsza Postawa. „Tak, ale…” to informacja z warunkiem albo plotka. Porażka to Postawa −1.</li></ol>
""" + read("<b>Gracz (Oddo):</b> Mówię Halce, że jak powie prawdę, załatwię jej syna glejt od Sędziów, żeby nikt go nie ruszył.<br><b>MG:</b> To jej Cena. Nie rzucasz, Halka mięknie i mówi o wozie z beczkami. Ale teraz jesteś jej winien glejt. Zapisuję dług Drobny: Oddo wobec Halki.") + """
<p><b>Rada:</b> nagradzaj odgrywanie. Dobry argument to Dźwignia. Nie każ rzucać za każde zdanie.</p>
"""),
("7. Walka krok po kroku", """
<p>Przykład: drużyna kontra Banda tragarzy Kruków (liczebność 6, Próg 4, pancerz 1).</p>
<ol><li><b>Ogłoś stawkę</b>: „To nie Stawka Śmierci. Jeśli przegracie, obudzicie się w zaułku z długiem.”</li>
<li><b>Inicjatywa</b>: w trackerze walki kliknij „Rzuć wszystkim”. Liczą się sukcesy Psyche + Refleks. Rzucasz raz na całą walkę.</li>
<li><b>Tura gracza</b>: Oddo atakuje młotem. Klik na broń, Trudność to Obrona Bandy (1). Wynik: 3 sukcesy, 1 Wyzwalacz.</li>
<li><b>Obrażenia</b>: młot 4+F/2, przy F=5 to 6, plus 1 za Wyzwalacz = 7. Gracz wybiera cel (klawisz T) i klika „Nałóż na cel”. Pancerz 1, więc netto 6 przy Progu 4: rana Poważna, Banda traci 2 członków.</li>
<li><b>Tura Bandy</b>: Banda atakuje raz z +2K za liczebność (4 członków). Oddo może wydać 1 Ego na aktywną obronę.</li>
<li><b>Morale</b>: po 3 stratach Banda ucieka. Opisz to.</li></ol>
<p><b>Najczęstszy błąd:</b> walka do ostatniego. Wrogowie chcą żyć. Uciekają, poddają się, negocjują.</p>
"""),
("8. Sepsa i Szept Prymera", """
<p>Szept to propozycja, nie atak. Zawsze pytaj.</p>
<ol><li>Postać ma Zarażenie ≥ 1 i jest w pobliżu źródła (studnia, chorzy, Burn).</li>
<li>Opisz pokusę i powiedz, co zyska: odpowiedź, siłę, przeczucie.</li>
<li>Gracz decyduje. Przyjęcie daje +1 Zarażenia (zaznacz na karcie, zakładka Dusza i Sepsa) i prawdziwą Odsłonę.</li>
<li>Odmowa nic nie kosztuje. Pochwal ją, bo to też jest decyzja postaci.</li></ol>
<p>Przy połowie skali Zarażenia opisz stygmat na piersi. Gracze powinni się tego bać.</p>
"""),
("9. Po każdej scenie: zegary, długi, Imię", """
<ul><li><b>Zegary</b>: przesuń te, które wynikają z fikcji (hałas, czas, Koszty).</li>
<li><b>Długi</b>: ktoś pomógł za darmo? Wpisz dług w Rejestrze. Dług spłacony albo zerwany? Kliknij odpowiedni przycisk, a Echo frakcji zmieni się samo.</li>
<li><b>Imię</b>: publiczny czyn albo zbrodnia przy świadkach? Kliknij +/− przy Echu frakcji i wpisz powód.</li>
<li><b>Ego i rany</b>: po scenie odpoczynku Lekkie rany znikają.</li></ul>
<p>Na koniec sesji: PD (5 + premie), makro „Nowa sesja” (odnawia Archetypy), krótka rozmowa: co się podobało, co zmienić.</p>
"""),
("10. Błędy nowego MG i improwizacja", """
<ul><li><b>Za dużo rzutów.</b> Jeśli nic nie zależy od wyniku, nie rzucaj.</li>
<li><b>Ukrywanie tropów.</b> Tropy kluczowe dawaj zawsze. Śledztwo bez tropów to nuda, nie wyzwanie.</li>
<li><b>Gotowe zakończenie.</b> Nie planuj, jak gracze rozwiążą sprawę. Zaplanuj, co zrobią NPC, gdy gracze nic nie zrobią.</li>
<li><b>Zasady przed fikcją.</b> Gdy nie pamiętasz reguły, zdecyduj sensownie i graj dalej. Sprawdzisz po sesji.</li></ul>
<h3>Improwizacja</h3>
<ul><li><b>Wyrocznia FU</b> (makro): gdy nie wiesz, czy coś jest prawdą, zadaj pytanie tak/nie i rzuć.</li>
<li><b>Imiona na podorędziu</b>: Borca: Jarek, Dagna, Lew, Wilma, Gerold. Kruki: Szpak, Wronka, Czerń. Spitalianie: Kessel, Tobiasz, Marten.</li>
<li><b>„Tak, ale…”</b> jako odpowiedź na pomysł gracza prawie zawsze działa.</li></ul>
"""),
("11. Muzyka i klimat", """
<p><b>W Foundry:</b> system zawiera tylko odgłosy tła (playlisty <i>Odgłosy</i> i <i>Efekty</i>). Muzykę dodaj własną: utwórz playlistę w zakładce Playlisty i wrzuć pliki albo linki. Poniżej propozycje.</p>
<h3>Poza Foundry (Spotify lub YouTube) — moje propozycje</h3>
<table><tr><th>Scena / nastrój</th><th>Muzyka</th><th>Dlaczego</th></tr>
<tr><td>Dzielnica, codzienna groza</td><td>Hildur Guðnadóttir — <i>Chernobyl</i> (OST)</td><td>skażenie, które słychać, zanim się je zobaczy</td></tr>
<tr><td>Studnia, Szept Prymera</td><td>Ben Salisbury &amp; Geoff Barrow — <i>Annihilation</i> (OST)</td><td>piękna, obca przemiana, idealna na Prymer</td></tr>
<tr><td>Sny chorych</td><td>Mica Levi — <i>Under the Skin</i> (OST)</td><td>niepokój, coś nieludzkiego</td></tr>
<tr><td>Lazaret</td><td>Jóhann Jóhannsson — <i>Arrival</i> (OST)</td><td>smutek i tajemnica</td></tr>
<tr><td>Kancelaria, konfrontacja</td><td>Jóhann Jóhannsson — <i>Sicario</i> (OST)</td><td>ciężkie, dudniące napięcie</td></tr>
<tr><td>Spelunka Kruków</td><td>Tom Waits — <i>Rain Dogs</i>; Nick Cave &amp; the Bad Seeds — <i>Murder Ballads</i></td><td>brud, hazard, półświatek</td></tr>
<tr><td>Kanały, ruiny</td><td>Lustmord — <i>Heresy</i>; wytwórnia Cryo Chamber (dark ambient)</td><td>podziemny, przytłaczający ambient</td></tr>
<tr><td>Klany i pustkowia (na przyszłość)</td><td>Heilung — <i>Ofnir</i>; Wardruna</td><td>plemienne, rytualne</td></tr>
<tr><td>Ruiny Bygone, Kronikarze</td><td>Eduard Artemiew — <i>Stalker</i></td><td>mistyka zony i martwej techniki</td></tr></table>
<p><b>Rada:</b> muzyka bez słów pod narrację, ze słowami tylko w spelunce. Zbuduj 2–3 playlisty (Napięcie, Groza, Spelunka) i przełączaj je jednym kliknięciem, nie co scenę.</p>
<p>Darmowe ambienty pod konkretne miejsca znajdziesz na Tabletop Audio (szukaj: plague, sewer, tavern, rain).</p>
"""),
]

# Gotowe postacie — rozszerzenie: klucz obrazka, ambicja, tajemnica, więzi, historia
PREGEN_EXTRA = {
 "Kapral Anja Reiss": ("anja", "Wrócić do Fortecy z raportem, który da jej własny oddział.", "Ma rozkaz z Fortecy: ocenić, czy Sędziowie panują nad Justitian, i raportować każdą ich słabość. Także o drużynie.", "Szeregowy Pit, ostatni żyjący z jej dawnego oddziału",
  "Anja przeżyła zasadzkę Klanów na przełęczy, w której zginęła połowa jej oddziału. Forteca dała jej awans i odesłała ją z dala od gór, do Justitian, jako łącznika przy Sędziach. Rozkaz brzmi: obserwować, raportować, nie strzelać bez potrzeby. Od tygodnia szeregowy Pit, ostatni z jej dawnych ludzi, nie zgłosił się na raport. Anja znalazła go w lazarecie. Uśmiecha się i nie pamięta jej imienia."),
 "Brat Kaspar": ("kaspar", "Wypalić handel Burnem w Justitian, zanim zje miasto tak, jak zjadł jego młodość.", "Jako chłopak był Burnerem i dłużnikiem Kruczego Stada. Ilsa Kruczyca wciąż pamięta jego twarz i jego dług.", "Rodzina rolników spod Justitian, która przyjęła go, gdy wychodził z nałogu",
  "Kaspar spędził młodość w spelunkach Justitian, z kokonem Burnu przy ustach i długiem u Kruków na karku. Wyciągnęli go Anabaptyści: trzy kropki na czole, miecz w dłoni, wiara zamiast cusp. Teraz poluje na dilerów, a jego gniew jest szczery i niebezpieczny. Gdy usłyszał o uśmiechniętych chorych w dzielnicy Dostawców, od razu rozpoznał objawy. To Burn Unity, ten sam, który kiedyś brał. Wie też, kto w tym mieście nim handluje."),
 "Siostra Wera": ("wera", "Udowodnić, że da się leczyć bez ognia.", "Raz spróbowała Burnu, żeby zrozumieć swoich pacjentów, i nigdy nie zapomniała tego ciepła.", "Lew, młodszy brat, tragarz z dzielnicy Dostawców (teraz chory w lazarecie)",
  "Wera trafiła do Spitalu jako dziecko, oddana przez matkę w zamian za worek antybiotyków dla reszty rodzeństwa. Przez dwanaście lat uczyła się, że jedno życie nic nie znaczy wobec ludzkości. Wierzyła w to do dnia, w którym musiała wypalić wioskę razem z dziećmi. Od tamtej pory pracuje w lazarecie przy Bramie Wschodniej i robi wszystko, żeby nie musieć więcej sięgać po ogień. Higienista Kessel uważa ją za miękką. Brat Tobiasz za jedyną rozsądną. Teraz na sali leży jej brat Lew i uśmiecha się do sufitu."),
 "Oddo, Sędzia miejski": ("oddo", "Zostać Protektorem i nosić młot z czystym sumieniem.", "Jego ojciec był Klanowcem z plemienia Karaluchów; Oddo ukrywa to przed wszystkimi Sędziami.", "Halka, przekupka, która karmiła go, gdy był ulicznym dzieckiem",
  "Oddo wyrósł na bruku dzielnicy Dostawców. Halka dawała mu chleb, a Sędziowie dali mu cel. Kodeks zna na pamięć i wierzy w niego bardziej niż ci, którzy go piszą. Sędzia Varga przydzielił go do pilnowania studni z rozkazem „nikogo nie dopuszczać i o nic nie pytać”. Oddo nigdy jeszcze nie złamał rozkazu. Nigdy też nie widział, żeby prawo milczało, gdy ludzie umierają."),
 "Kasia „Sroka”": ("sroka", "Założyć własne Stado, w którym nikt nie będzie towarem.", "Wie, co Kruki wlewają do studni, i boi się, że to ją obciąży.", "Matka Agna, stara akuszerka z Franki, która nauczyła ją czytać z kart",
  "Sroka przyszła do Justitian z Franki, z rzeki, przed rojem. W Kruczym Stadzie nauczyła się, że każdy sekret ma cenę, a każdy człowiek jest coś winien. Zna wszystkie plotki dzielnicy, połowę jej łóżek i całą jej biedę. Ilsa Kruczyca kazała jej pilnować, żeby nikt nie węszył przy studni. Sroka widziała beczki z białym pyłem. Widziała też, jak dziecko, które piło tę wodę, przestało płakać. Na zawsze."),
 "Mirek „Borsuk”": ("borsuk", "Znaleźć legendarny bunkier pod Justitian, o którym mówią runy na murach.", "Sprzedał Krukom mapę kanałów pod dzielnicą, a teraz rozumie, do czego jej użyli.", "Kot imieniem Kronikarz, który mieszka w jego norze w ruinach",
  "Borsuk zna podziemia Justitian lepiej niż Sędziowie i Kronikarze razem wzięci. Pracuje sam, bo ludzie zawodzą, a ruiny nie. Na każdym niebezpiecznym przejściu zostawia swoją runę ostrzegawczą. Miesiąc temu sprzedał Krukom mapę kanałów pod dzielnicą Dostawców za skrzynkę amunicji. Wczoraj zobaczył, że ktoś zamalował jego runę na włazie i wydrapał w sadzy czarne pióro."),
 "Modus": ("modus", "Zostać Streamerem i poznać tajemnice innych kultów.", "W Strumieniu zobaczył dane, których nie powinien widzieć: Klaster wiedział o Burnie w dzielnicy wcześniej, niż mu powiedziano.", "Bit imieniem Szum, młodsza siostra, która wciąż pracuje w Alkowie",
  "Modus był sierotą z ruin, zanim Kronikarze wytatuowali mu kod kreskowy na czole. Wierzy w Strumień, w dane, w porządek liczb, a ludzie to dla niego wzory, które jeszcze nie zostały policzone. Klaster zauważył, że wydajność dzielnicy Dostawców spadła o jedną trzecią, i wysłał go, żeby ustalił dlaczego, zanim zrobią to Sędziowie. Problem w tym, że w archiwach Alkowy Modus znalazł wpis sprzed dwóch tygodni: „Dzielnica D: testy Unity, nie ingerować”."),
}

NEW_NPCS = [
 # name, img, scale, attitude, pools-like attrs/skills, motyw, lek, sekret, cena, desc, weapons
 ("Ilsa Kruczyca", "ilsa", "antagonista", 0, {"cia": 2, "zre": 3, "cha": 4, "int": 2, "psy": 4, "ins": 3},
  {"uwodzenie": 4, "oszustwo": 4, "spryt": 4, "dominacja": 3, "legendy": 3, "empatia": 3, "bronBiala": 2, "refleks": 2, "wiara": 3},
  "Zapłata i dług Vargi", "Że wina spadnie na Stado", "Ma list z pieczęcią Vargi", "Dług Poważny albo czyste ręce Stada",
  "Kruk Kruczego Stada, czyta z Tarota i z ludzi. Uprzejma, cierpliwa, bezlitosna. Woli dłużnika niż trupa.", ["Nóż"]),
 ("Higienista Kessel", "kessel", "weteran", -1, {"cia": 3, "zre": 2, "cha": 2, "int": 3, "psy": 3, "ins": 2},
  {"medycyna": 3, "nauka": 3, "dominacja": 3, "twardosc": 3, "bronBiala": 2, "wola": 3, "percepcja": 2},
  "Wypalić ognisko, zanim się rozprzestrzeni", "Psychonauty ukrytego w mieście", "Dostał rozkaz, by nie pytać Sędziów", "Dowód, że to nie Sepsa",
  "Higienista Spitalu w masce gazowej. Wierzy, że lepiej spalić za dużo niż za mało. Nie jest zły, tylko przerażony.", ["Pistolet"]),
 ("Brat Tobiasz", "tobiasz", "weteran", 1, {"cia": 2, "zre": 2, "cha": 2, "int": 3, "psy": 2, "ins": 3},
  {"medycyna": 4, "nauka": 2, "empatia": 3, "twardosc": 2, "bronBiala": 2, "wola": 2},
  "Wyleczyć ludzi", "Kessela i ognia", "Wie, że to Burn, ale nie ma dowodu", "Ochrona przed Kesselem",
  "Famulancer z lazaretu, zmęczony i uczciwy. Sojusznik Wery i każdego, kto chce prawdy.", ["Włócznia"]),
]

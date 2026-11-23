# -*- coding: utf-8 -*-
"""Podręcznik gracza, przygoda „Ciche studnie” i gotowe postacie."""

PLAYER_PAGES = [
("1. Witaj w 2595 roku", """
<p>Rok 2595. Pięćset lat temu asteroidy spaliły świat i przyniosły <b>Prymer</b>: obcą siłę, która przepisuje życie. Ziemię porasta <b>Sepsa</b>, grzyb tworzący pola zarodników. Z pól zbiera się <b>Burn</b>, narkotyk, który daje rozkosz i moc, ale zaraża. Przy polach rodzą się <b>Psychonauci</b>, dzieci bez duszy, następny gatunek.</p>
<p>Ludzie żyją w siedmiu <b>Kulturach</b> (Borca, Franka, Pollen, Balkhan, Hybrispania, Purgare, Afryka) i służą trzynastu <b>Kultom</b>. Każdy kult ma inną odpowiedź na pytanie, jak przetrwać, i inną prawdę, którą ukrywa.</p>
<p>Gracie ludźmi, którzy muszą wybrać, czyja prawda jest warta ceny. W tej wersji zasad świat jest groźny, ale was nie morduje: rany, długi i Sepsa kosztują, a śmierć przychodzi tylko wtedy, gdy stawka zostanie ogłoszona.</p>
<h3>Co musisz wiedzieć na pierwszą sesję</h3>
<ol><li>Jak rzucać kośćmi (strona 2).</li><li>Co znaczą wyniki (strona 3).</li><li>Co możesz robić w scenie (strona 4).</li><li>Czym płacisz (strona 5).</li></ol>
<p>Resztę wyjaśnia MG w trakcie gry. Na pierwszą sesję możesz wziąć gotową postać z kompendium <i>Gotowe postacie</i> albo zrobić własną w kreatorze (strona 6).</p>
"""),
("2. Jak rzucać", """
<p>Kiedy postać robi coś ryzykownego, MG mówi: „rzuć Atrybut + Umiejętność”, np. <b>Instynkt + Percepcja</b>.</p>
<ol><li>Na karcie kliknij <b>nazwę umiejętności</b>. Liczba „5K” obok niej to twoja pula: tyle kości k6 rzucasz.</li>
<li>W oknie rzutu ustaw <b>Trudność</b>, którą podał MG (zwykle 2). Możesz dodać kości:<ul>
<li><b>Ego</b>: 1 punkt = +1 kość, maks. 3 na rzut;</li><li><b>Zaplecze</b>: pomoc twojego kultu, maks. +3;</li>
<li><b>Archetyp</b>: raz na sesję +2, gdy działasz zgodnie ze swoim Konceptem;</li><li><b>Cechy miejsca</b>: +2 za każdą wywołaną Cechę.</li></ul></li>
<li>Każda kość z wynikiem <b>4, 5 lub 6 to sukces</b>. Każda <b>6 to także Wyzwalacz</b>, czyli coś ekstra.</li>
<li>Wynik pojawi się na czacie razem z podpowiedzią, co dalej.</li></ol>
<p><b>Przykład:</b> Wera (Intelekt 3 + Medycyna 4 = 7 kości) opatruje rannego. Trudność 2. Wypada 6, 5, 4, 3, 2, 2, 1, czyli 3 sukcesy i 1 Wyzwalacz. Wynik: „Tak, i…”. Wera kupuje za Wyzwalacz efekt <i>Szybko</i> i zdąży przed patrolem.</p>
<p><b>Starcie:</b> gdy ktoś ci się przeciwstawia, rzucacie oboje. Więcej sukcesów wygrywa, potem decydują Wyzwalacze, a przy remisie wygrywa obrońca.</p>
"""),
("3. Co znaczą wyniki", """
<table><tr><th>Wynik</th><th>Kiedy</th><th>Co się dzieje</th></tr>
<tr><td><b>Tak, i…</b></td><td>sukcesów ≥ Trudność, są szóstki</td><td>Udało się, a każdy Wyzwalacz kupuje Efekt.</td></tr>
<tr><td><b>Tak</b></td><td>sukcesów ≥ Trudność</td><td>Udało się.</td></tr>
<tr><td><b>Tak, ale…</b></td><td>co najmniej 1 sukces, brakuje 1–2</td><td>Ty wybierasz: porażka albo sukces, za który MG naliczy Koszt.</td></tr>
<tr><td><b>Nie</b></td><td>za mało sukcesów</td><td>Nie wychodzi i sytuacja się zmienia. Trop kluczowy i tak dostajesz.</td></tr>
<tr><td><b>Nie, i…</b></td><td>więcej jedynek niż sukcesów</td><td>Zgrzyt: coś idzie bardzo źle.</td></tr></table>
<h3>Efekty Wyzwalaczy (1 Wyzwalacz = 1 Efekt)</h3>
<ul><li><b>Szybko</b>: bez straty czasu.</li><li><b>Czysto</b>: bez śladów i świadków.</li><li><b>Więcej</b>: dodatkowa informacja albo +1 obrażenie.</li>
<li><b>Przewaga</b>: tworzysz nową Cechę sceny, np. „Strażnik patrzy w złą stronę”, z darmowym wywołaniem.</li><li><b>Wrażenie</b>: ktoś zaczyna cię lubić albo o tobie mówić.</li><li><b>Ochrona</b>: osłaniasz drużynę przed jednym Kosztem.</li></ul>
<h3>Koszty (przy „Tak, ale…”)</h3>
<p>Lekka rana, utrata Ego, hałas, ślad, zgubiony sprzęt, ktoś cię mniej lubi, dług, upływ czasu. Wybiera je MG, ale zawsze z sensem w fikcji.</p>
"""),
("4. Co możesz robić w scenie", """
<h3>Śledzić</h3>
<p>Jeśli szukasz we właściwym miejscu i masz odpowiednią umiejętność, <b>trop kluczowy dostajesz zawsze</b>, bez rzutu. Rzut daje <b>Odsłony</b>: szczegół, powiązanie, haczyk na kogoś (Dźwignię), ostrzeżenie albo czas. Twój kult ma swoją <b>Metodę</b> (jest w opisie kultu): raz na scenę daje dodatkową Odsłonę.</p>
<p>Zapisujcie tropy na wspólnej <b>Tablicy śledztwa</b>. Gdy połączycie dwa tropy w teorię, rzućcie na <b>Wniosek</b>: MG powie „ciepło” albo „zimno” i nie skłamie.</p>
<h3>Rozmawiać</h3>
<p>Każdy NPC ma Postawę: Wrogi, Nieufny, Obojętny, Życzliwy albo Oddany. Im gorsza Postawa, tym trudniej. <b>Dźwignia</b> to znajomość tego, czego NPC chce, czego się boi, co ukrywa albo za co pomoże. Daje +2 kości albo pozwala na prośbę, która bez niej byłaby niemożliwa. Najlepsze rozmowy wygrywa się wcześniej, w śledztwie.</p>
<h3>Patrzeć uważnie</h3>
<p>Miejsca mają <b>Cechy</b>, np. „Tłum na targu” albo „Zardzewiałe rusztowania”. Część jest ukryta. Kto pyta i patrzy, odkrywa je i dostaje darmowe +2 kości. Opisz, jak Cecha ci pomaga, i ją wywołaj.</p>
<h3>Korzystać z kultu</h3>
<p><b>Zaplecze</b> to Sojusznicy, Autorytet, Sława, Zasoby, Sekrety i Sieć. Daje kości do rzutu albo pewną przysługę bez rzutu (Wykorzystanie), ale wtedy punkt jest zużyty do Interludium.</p>
<h3>Zaciągać i ściągać długi</h3>
<p>Kto ci pomógł za darmo, ma u ciebie <b>dług</b>. Kto ma dług u ciebie, jest ci winien przysługę. Długi wpisuje MG. Zerwany dług psuje twoje <b>Imię</b>, czyli reputację drużyny u frakcji. Imię decyduje, czy w mieście otwierają się drzwi, czy szykuje się stryczek.</p>
"""),
("5. Czym płacisz", """
<h3>Ego</h3>
<p>Twoja odporność psychiczna i waluta. Wydajesz je na kości (+1 za punkt), na aktywną obronę w walce (1) albo na złagodzenie rany (2). Tracisz je przez grozę, presję i Psychonautów. Przy zerze się łamiesz. Odzyskujesz je snem, grą zgodną z Archetypem, Ideałem kultu, Więziami i Burnem (ten ostatni kosztuje Zarażenie).</p>
<h3>Rany</h3>
<p>Twój <b>Próg</b> to Ciało + Twardość. Trafienie poniżej Progu to rana Lekka, od Progu Poważna, a od podwójnego Progu Krytyczna. Masz 3 miejsca na Lekkie, 2 na Poważne i 1 na Krytyczną. Poważna daje −1 kość, Krytyczna −2. Gdy zabraknie miejsc, jesteś <b>wyeliminowany</b>: nie martwy, ale coś tracisz (niewola, sprzęt, blizna, dług). Śmierć grozi tylko wtedy, gdy MG ogłosi <b>Stawkę Śmierci</b>.</p>
<h3>Zarażenie (Sepsa)</h3>
<p>Zarodniki, Burn i pola spor podnoszą Zarażenie. Od połowy skali na piersi wykwita stygmat. Powyżej maksimum walczysz o duszę. Uwaga na <b>Szept Prymera</b>: gdy jesteś zarażony, MG może zaproponować ci wizję albo siłę za kolejny punkt Zarażenia. Czasem to jedyna droga do prawdy. Zawsze możesz odmówić.</p>
<h3>Archetyp i jego Cień</h3>
<p>Twój Koncept raz na sesję daje +2 kości. Jego <b>Cień</b> to ciemna strona. Gdy MG zaproponuje Pokusę, czyli działanie zgodne z Cieniem, i się zgodzisz, dostajesz +2 Ego i +1 PD, a historia się komplikuje.</p>
"""),
("6. Tworzenie postaci (kreator)", """
<p>Utwórz aktora typu <b>Postać</b>, otwórz kartę i kliknij <b>Kreator</b> w nagłówku. Kreator prowadzi przez 9 kroków i pilnuje punktów. Bez Foundry: karta do druku i procedura na papierze są w dzienniku „Podręcznik Gracza (PDF)”.</p>
<ol><li><b>Pochodzenie</b>: Kultura, Koncept, Kult. Każde podnosi limit kilku cech o 1 (gwiazdka). Bonus nie jest darmowym punktem, ale obniża koszt rozwoju.</li>
<li><b>Ścieżka</b>: Skupienie albo Pierwotność (skąd bierzesz Ego) i Wiara albo Wola (co cię chroni). Druga z pary zostaje na zawsze na 0.</li>
<li><b>Atrybuty</b>: każdy zaczyna od 1, dokładasz 10 punktów (1 punkt = +1, suma zawsze 16), limit 3 (+1 za gwiazdkę).</li>
<li><b>Umiejętności</b>: zaczynają od 0, rozdajesz 28 punktów (1 punkt = +1), limit 2 (+1 za gwiazdkę).</li>
<li><b>Zaplecze</b>: 4 punkty, limit 3.</li>
<li><b>Ranga</b>: kreator pokazuje, które rangi kultu już osiągasz. Wybierz jedną.</li>
<li><b>Potencjał</b>: jedna specjalna zdolność z kultu albo ogólna.</li>
<li><b>Człowiek</b>: imię, Ambicja, Tajemnica, 1–2 Więzi, Cień.</li>
<li><b>Podsumowanie</b>: Ego, Zarażenie, Próg i pieniądze liczą się same.</li></ol>
<p><b>Rada:</b> postać w Degenesis to najpierw ktoś z kultu. Zanim wydasz punkty, przeczytaj stronę swojego kultu w dzienniku <i>Kulty — przewodnik</i>: rangi, Metodę, Ideał i Potencjały.</p>
"""),
("7. Ściąga", """
<table><tr><th>Sytuacja</th><th>Rzut</th></tr>
<tr><td>Zauważyć, nasłuchiwać, przeszukać</td><td>Instynkt + Percepcja</td></tr><tr><td>Wyczuć kłamstwo, nastrój</td><td>Instynkt + Empatia</td></tr>
<tr><td>Przekonać, targować się</td><td>Charyzma + Negocjacje</td></tr><tr><td>Zastraszyć, przesłuchać</td><td>Psyche + Dominacja</td></tr>
<tr><td>Okłamać, przebrać się</td><td>Psyche + Oszustwo</td></tr><tr><td>Wiedzieć o kultach, historii</td><td>Intelekt + Legendy</td></tr>
<tr><td>Leczyć, zbadać zwłoki</td><td>Intelekt + Medycyna</td></tr><tr><td>Zakraść się</td><td>Zręczność + Skradanie</td></tr>
<tr><td>Strzelać</td><td>Zręczność + Strzelectwo</td></tr><tr><td>Walczyć bronią / pięściami</td><td>Ciało + Broń biała / Bijatyka</td></tr>
<tr><td>Uskoczyć, uciec z więzów</td><td>Zręczność + Mobilność</td></tr><tr><td>Inicjatywa</td><td>Psyche + Refleks</td></tr>
<tr><td>Oprzeć się wpływowi, Sepsie</td><td>Psyche + Wiara albo Wola</td></tr><tr><td>Przetrwać w dziczy</td><td>Instynkt + Przetrwanie</td></tr></table>
<p><b>Trudność:</b> 1 rutynowa, 2 wymagająca, 3 trudna, 4 bardzo trudna, 6 desperacka.</p>
<p><b>Walka w skrócie:</b> inicjatywa raz na starcie, potem 1 akcja i ruch na turę. Atak to rzut przeciw Obronie celu (zwykle 1). Obrażenia + Wyzwalacze − pancerz dają ranę. Aktywna obrona kosztuje 1 Ego. Uciekać wolno zawsze.</p>
"""),
]

ADVENTURE_PAGES = [
("Ciche studnie — o przygodzie", """
<p><b>Przygoda startowa</b> na 1–2 sesje dla 3–5 postaci. Miejsce: dzielnica Dostawców w Justitian (Borca). Ciężar: śledztwo i rozmowy, walka jest opcjonalna. Uczy wszystkich zasad 2.0: tropów, Cech, Dźwigni, długów, Imienia, Sepsy i Szeptu Prymera.</p>
<p><b>Haczyk:</b> w dzielnicy, która karmi całe Justitian, ludzie chorują. Majaczą, uśmiechają się do ścian, przestają pracować. Spitalianie zamknęli studnię przy Bramie Wschodniej i przebąkują o „oczyszczeniu ogniem”. Sędziowie nabrali wody w usta. Postacie trafiają tu, bo ktoś bliski choruje, bo kult kazał to zbadać albo bo w lazarecie brakuje rąk.</p>
<p><b>Aktorzy</b> są w kompendium <i>Przykłady</i>: Śledztwo „Ciche studnie”, Lokacja „Targ przy Bramie Wschodniej”, frakcje Krucze Stado i Spitalianie z lazaretu, NPC Halka i Sędzia Varga, banda tragarzy Kruków oraz Rejestr Długów. Gotowe postacie są w kompendium <i>Gotowe postacie</i>.</p>
"""),
("Prawda (tylko dla MG)", """
<p><b>Sędzia miejski Varga</b> boi się buntu: Dostawcy mają zastrajkować tuż przed wizytą Senatora. Zapłacił <b>Kruczemu Stadu</b> (Apokaliptykom) za „uspokojenie dzielnicy”. Kruki od tygodnia wlewają do studni rozcieńczony Burn <b>Unity</b>: ludzie robią się łagodni i posłuszni. Rozcieńczony Burn i tak zaraża, a część ofiar zaczyna wykazywać pierwsze objawy Sepsy.</p>
<p><b>Spitalianie</b> widzą Sepsę bez Leperosa i pola spor. Podejrzewają ukrytego Psychonautę i szykują kwarantannę i ogień. Pod spodem dzieje się coś jeszcze: chorzy śnią ten sam sen o „matce pod miastem”. To nieprawda o Psychonaucie, ale prawdziwy Szept Prymera, który czuje Burn w wodzie. Możesz to rozwinąć w kolejnej przygodzie.</p>
<h3>Zegary</h3>
<ul><li><b>Epidemia wybucha w całej dzielnicy</b> (8; startuje na 2): tyka co dzień gry i od hałasu w śledztwie. Na 8 Spitalianie palą kwartał.</li>
<li><b>Dostawa dla Sędziego</b> (6; Kruki, start 3): na 6 Kruki kończą robotę, znikają z dzielnicy, a dowody idą z nimi.</li>
<li><b>Kwarantanna i podpalenie</b> (6; Spitalianie, start 1): rośnie, gdy postacie nie dzielą się wiedzą z lazaretem.</li></ul>
"""),
("Sceny i tropy", """
<p>Sceny to <b>węzły</b>: kolejność wybierają gracze. Każdy węzeł ma 3 tropy kluczowe, a każdy trop prowadzi do innego węzła (zasada trzech tropów). Odsłony to nagrody za dobre rzuty.</p>
<h3>A. Lazaret Spitalian</h3>
<p><i>Cechy:</i> „Smród wapna i strachu”, „Za mało łóżek” (ukryta: „Brat Famulancer ma wątpliwości”).</p>
<ul><li><b>Tropy:</b> chorują tylko ludzie pijący ze studni przy Bramie (→ C); w ślinie chorych są włókna, ale Mollusk reaguje słabo, niepodobnie do zwykłej Sepsy (→ C); chorzy śnią o „matce pod miastem” (→ E).</li>
<li><b>Odsłony:</b> objawy przypominają odurzenie Burnem, a nie chorobę (Medycyna, Wyzwalacz); Hygienista chce podpalić kwartał za 3 dni (Ostrzeżenie); brat Famulancer odda próbki za obietnicę ochrony (Dźwignia → dług).</li></ul>
<h3>B. Targ przy Bramie Wschodniej</h3>
<p><i>Cechy:</i> „Tłum, w którym łatwo zniknąć”, „Patrole Sędziów co kwadrans” (ukryta: „Przekupki widzą wszystko”).</p>
<ul><li><b>Tropy:</b> przekupka Halka widziała nocą wóz z beczkami bez znaków (→ D); tragarze płacą za piwo dinarami, choć zwykle płacą Draftami (→ D); Sędziowie nie dopuszczają nikogo do studni od tygodnia, a nie od dnia zachorowań (→ F).</li>
<li><b>Halka</b> jest Nieufna. Jej Lęk: syn pił wodę. Jej Sekret: syn nosi beczki dla Kruków. Jeśli postacie ochronią syna, Halka powie wszystko i będzie miała u nich dług Drobny.</li></ul>
<h3>C. Studnia</h3>
<p><i>Cechy:</i> „Łańcuch i pieczęć Spitalu”, „Wilgoć i ciemność” (ukryta: „Ślady ciągnięcia beczek po bruku”).</p>
<ul><li><b>Tropy:</b> na cembrowinie biały, słodkawy osad, którego nie wyczuwa Mollusk (→ A albo D); świeże rysy po linie, jakby coś spuszczano nocą (→ D); w szczelinie skrawek czarnego pióra, znak Kruczego Stada (→ D).</li>
<li><b>Sporyzacja:</b> kto schodzi do studni bez maski, rzuca Ciało + Twardość (2). Porażka daje +1 Zarażenie. To dobra okazja do pierwszego <b>Szeptu Prymera</b>: wizja ciepłej, posłusznej dzielnicy i obietnica „spokoju”. Kto przyjmie Szept, wie od razu, że to Burn Unity.</li></ul>
<h3>D. Spelunka Kruków („Pod Złamanym Skrzydłem”)</h3>
<p><i>Cechy:</i> „Dym, kości i muzyka”, „Każdy coś jest winien Krukom” (ukryta: „Magazyn za kurtyną”).</p>
<ul><li><b>Tropy:</b> Kruki mają w magazynie beczki z resztkami białego pyłu (→ F); kapłanka Stada wie, kto płaci, i sprzeda to za dług Poważny (→ F); tragarze (banda) pilnują wozu, który rusza o świcie (Zegar Dostawy).</li>
<li>Ta scena może skończyć się walką z bandą tragarzy. Morale łamie się po 3 stratach. Kruki wolą jednak handlować: Kruk woli dłużnika niż trupa.</li></ul>
<h3>E. Sny chorych</h3>
<p>Rozmowy z chorymi (Instynkt + Empatia) albo Szept Prymera. <b>Tropy:</b> wszyscy śnią to samo; sen nasila się po wypiciu wody (→ C); jeden chory powtarza „sędzia pił z nami wino, a potem woda zrobiła się słodka” (→ F).</p>
<h3>F. Kancelaria Sędziego Vargi</h3>
<p><i>Cechy:</i> „Kodeks na pulpicie”, „Dwaj Protektorzy przy drzwiach” (ukryta: „Księga wydatków z podwójnymi wpisami”).</p>
<ul><li>Varga jest Obojętny. Jego Motyw: spokój przed wizytą Senatora. Lęk: że Kodeks go dosięgnie. Sekret: zapłacił Krukom. Cena: czyjaś głowa zamiast jego. Bez Dźwigni nie powie nic. Z dowodami (księga, pióro, beczki, zeznanie kapłanki) zaczyna negocjować.</li></ul>
"""),
("Finały i konsekwencje", """
<p>Nie ma jednego „dobrego” zakończenia. Każda droga zmienia <b>Imię</b> drużyny i <b>Rejestr Długów</b>.</p>
<table><tr><th>Rozwiązanie</th><th>Co się dzieje</th><th>Imię i długi</th></tr>
<tr><td>Zdemaskować Vargę przed Sędziami</td><td>Varga staje przed Arbitrem; Kruki mszczą się na informatorach</td><td>Sędziowie: Echo +2; Krucze Stado: Echo −2; Halka ma u was dług, jeśli ją chroniliście</td></tr>
<tr><td>Szantażować Vargę</td><td>Varga płaci i odwołuje Kruki, ale zostaje u władzy</td><td>Varga ma u was dług Krwawy (ukryty); wy macie wroga osobistego</td></tr>
<tr><td>Wydać wszystko Spitalianom</td><td>Spital przejmuje sprawę: kwarantanna bez ognia, ale chorzy trafiają na badania</td><td>Spitalianie: Echo +2; Dostawcy pamiętają, kto wydał ich chorych</td></tr>
<tr><td>Dogadać się z Krukami</td><td>Kruki przestają za dobrą cenę i „zapominają” o was</td><td>Dług Poważny wobec Kruczego Stada; Sędziowie podejrzliwi, jeśli wyjdzie na jaw</td></tr>
<tr><td>Nic nie zrobić na czas</td><td>Zegar epidemii pełny: Spitalianie palą kwartał</td><td>Imię u wszystkich −1; trauma postaci, które to widziały (−Ego)</td></tr></table>
<p><b>PD:</b> 5 za sesję, +2 za ważny Wniosek (np. „to Burn, nie Psychonauta”), +2 za odkryty Sekret (Varga i Kruki), +1 za przyjętą Pokusę Archetypu.</p>
<p><b>Ciąg dalszy:</b> „matka pod miastem” ze snów chorych. Coś pod Justitian odpowiedziało na Burn w wodzie.</p>
"""),
]

# Gotowe postacie: (imię, kultura, koncept (fragment nazwy), kult, path, belief, attrs, skills, bgs, ranga, potencjał, broń, opis)
PREGENS = [
 ("Siostra Wera", "Borca", "Uzdrowiciel", "Spitalianie", "skupienie", "wola",
  {"cia": 2, "zre": 3, "cha": 2, "int": 3, "psy": 3, "ins": 3},
  {"medycyna": 4, "nauka": 3, "twardosc": 3, "skupienie": 2, "wola": 3, "percepcja": 3, "rzemioslo": 2, "bronBiala": 2, "empatia": 2, "kondycja": 2, "refleks": 2},
  {"slawa": 1, "sojusznicy": 1, "zasoby": 1, "siec": 1}, "Famulancer", "Ostatni Bastion (Last Bastion)", ["Włócznia", "Pistolet"],
  "Famulancerka z lazaretu przy Bramie Wschodniej. Ambicja: udowodnić, że da się leczyć bez ognia. Tajemnica: raz spróbowała Burnu. Więź: młodszy brat, tragarz w dzielnicy Dostawców."),
 ("Oddo, Sędzia miejski", "Borca", "Sprawiedliwy", "Sędziowie", "pierwotnosc", "wola",
  {"cia": 3, "zre": 2, "cha": 2, "int": 2, "psy": 3, "ins": 4},
  {"bronBiala": 3, "strzelectwo": 2, "prowadzenie": 3, "obycie": 2, "dominacja": 3, "ekspresja": 2, "legendy": 2, "spryt": 2, "negocjacje": 2, "pierwotnosc": 2, "refleks": 2, "empatia": 2, "percepcja": 1},
  {"autorytet": 2, "sojusznicy": 1, "zasoby": 1}, "Sędzia miejski (City Judge)", "Twarz Janusa (Janus Face)", ["Pałka / maczuga", "Muszkiet"],
  "Młody Sędzia, który wierzy w Kodeks bardziej niż jego przełożeni. Ambicja: zostać Protektorem. Tajemnica: jego ojciec był Klanowcem. Więź: przekupka Halka, która go wykarmiła."),
 ("Kasia „Sroka”", "Franka", "Wizjoner", "Apokaliptycy", "pierwotnosc", "wola",
  {"cia": 2, "zre": 3, "cha": 4, "int": 1, "psy": 3, "ins": 3},
  {"uwodzenie": 4, "spryt": 3, "zwinnePalce": 3, "oszustwo": 3, "sztuka": 2, "atletyka": 2, "ekspresja": 2, "empatia": 2, "bijatyka": 2, "pierwotnosc": 2, "wola": 1, "skradanie": 2},
  {"slawa": 2, "siec": 2}, "Sroka (Magpie)", "Gniazdo (Crow's Nest)", ["Nóż"],
  "Sroka Kruczego Stada, która zna każdy sekret dzielnicy. Ambicja: własne Stado. Tajemnica: wie, co Kruki wlewają do studni, i boi się, że to ją zabije. Więź: stara akuszerka z Franki."),
 ("Mirek „Borsuk”", "Borca", "Pustelnik", "Złomiarze", "skupienie", "wola",
  {"cia": 3, "zre": 3, "cha": 1, "int": 3, "psy": 2, "ins": 4},
  {"przetrwanie": 4, "artefakty": 3, "rzemioslo": 3, "percepcja": 2, "orientacja": 2, "skradanie": 3, "strzelectwo": 2, "atletyka": 2, "twardosc": 2, "spryt": 2, "skupienie": 2, "inzynieria": 1},
  {"zasoby": 1, "siec": 2, "sekrety": 1}, "Borsuk (Badger)", "Darwin", ["Strzelba", "Nóż"],
  "Samotnik z ruin pod Justitian. Zna kanały i stare rury pod dzielnicą lepiej niż Sędziowie. Ambicja: znaleźć legendarny bunkier. Tajemnica: sprzedał Krukom mapę kanałów. Więź: kot imieniem Kronikarz."),
 ("Modus", "Borca", "Badacz", "Kronikarze", "skupienie", "wola",
  {"cia": 2, "zre": 3, "cha": 2, "int": 4, "psy": 2, "ins": 3},
  {"artefakty": 5, "inzynieria": 4, "nauka": 3, "skupienie": 2, "negocjacje": 3, "oszustwo": 3, "rzemioslo": 2, "percepcja": 2, "legendy": 2, "wola": 2},
  {"sekrety": 1, "siec": 2, "zasoby": 1}, "Mediator", "Pamięć fraktalna (Fractal Memory)", ["Pistolet", "Nóż"],
  "Kronikarz-Mediator z kodem kreskowym na czole. Ambicja: zostać Streamerem. Tajemnica: Klaster wiedział o Burnie wcześniej. Więź: siostra Szum w Alkowie."),
 ("Kapral Anja Reiss", "Borca", "Obrońca", "Hellveci", "skupienie", "wola",
  {"cia": 3, "zre": 3, "cha": 2, "int": 2, "psy": 3, "ins": 3},
  {"strzelectwo": 3, "sila": 2, "kondycja": 3, "twardosc": 3, "refleks": 3, "przywodztwo": 2, "przetrwanie": 2, "percepcja": 2, "skupienie": 2, "wola": 2, "bronBiala": 2, "mobilnosc": 2},
  {"autorytet": 2, "sojusznicy": 1, "zasoby": 1}, "Kapral (Corporal)", "Ściana tarcz (Shield Wall)", ["Karabin myśliwski", "Nóż"],
  "Hellwetka z Fortecy Alpejskiej, kapral bez oddziału."),
 ("Brat Kaspar", "Borca", "Zelota", "Anabaptyści", "pierwotnosc", "wiara",
  {"cia": 3, "zre": 3, "cha": 2, "int": 1, "psy": 3, "ins": 4},
  {"bronBiala": 3, "pierwotnosc": 2, "twardosc": 2, "wiara": 4, "sila": 3, "mobilnosc": 3, "legendy": 2, "refleks": 3, "przetrwanie": 2, "percepcja": 2, "ekspresja": 2},
  {"slawa": 2, "sojusznicy": 2}, "Orgiasta (Orgiastic)", "Zelota (Zealot)", ["Miecz"],
  "Anabaptysta-Orgiasta, łowca handlarzy Burnem."),
]

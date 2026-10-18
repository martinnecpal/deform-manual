---
lang: sk
title: "Tvárnenie za tepla"
---

Tvárnenie za tepla

Pri simulácii tvárnenia za tepla je dôležité simulovať všetky kroky procesu vrátane prenosu z pece a odpočinku na matrici, pretože teplotná strata spôsobená prenosom z pece a chladením matrice môže ovplyvniť správanie prietoku. Postup simulácie viacpolohového procesu je podrobne opísaný na konci tejto časti.

V tejto časti sa načrtne postup nastavenia pre nasledujúce operácie:

1. Nastavte jednotnú teplotu objektu na simuláciu úplného namočenia pece.

2. Ochlaďte na vzduchu, aby ste simulovali prenos z pece do lisovníc

3. Odpočívajte na matriciach

4. Kováčstvo

5. Opakujte pre viacnásobné kovanie úderov

1. **Vytvoriť nový priečinok problémov (adresár)**

Každý problém s deformáciou by mal byť umiestnený vo vlastnom priečinku. Daný problém však môže obsahovať veľa operácií, všetky v tom istom databázovom súbore.

1. **Spustite predprocesor DEFORMÁCIE **

2. **Nastavte základné ovládacie prvky simulácie **

Pre prvú operáciu sa nastavia simulačné ovládacie prvky – simulácia chladenia počas prechodu z pece do lisu.

1. Názov problému (nepovinné)

Popisný názov problému – zobrazí sa na obrazovke počas predbežného a následného spracovania.

1. Názov operácie

Názov činnosti

1. Jednotkový systém

Vyberte jednotky v angličtine alebo SI. Tým sa zmení mnoho predvolených hodnôt a ovplyvní sa spôsob importu údajov o materiáli.

1. Vyberte režim simulácie

Pre simuláciu prenosu obrobku z pece do lisu bude modelovaný iba prenos tepla, preto zapnite prenos tepla a vypnite deformáciu.

1. **Definujte materiál**

Definujte tepelné vlastnosti materiálu. Pre väčšinu ocelí majú súbory STEEL_E.KEY alebo STEEL_S.KEY primerané tepelné vlastnosti. Tieto súbory je možné načítať z ponuky Vlastnosti materiálu v hlavnom okne preprocesora.

1. **Definujte obrobok**

1. Definujte typ objektu

Pre väčšinu simulácií je vhodný typ plastového objektu.

1. Definujte geometriu

Geometriu je možné definovať zo súboru STL.

Požiadavky na geometriu obrobku:

* Geometria musí byť definovaná s normálmi smerujúcimi von

* Vždy skontrolujte geometriu.

1. Povrchová sieť objektu

Typické postupnosti by mali používať veľkosti prvkov, ktoré predstavujú vlastnosti dielu. V prípade pochybností bude mať viac prvkov tendenciu poskytovať presnejšie výsledky. Typické váhy:

* Zakrivenie=0,9

* Miera deformácie =0,7

* Kmeň =0,5

Teplota

1. Definujte tepelné hraničné podmienky

V prípade pevných častí definujte výmenu tepla s prostredím na všetkých plochách okrem symetrických povrchov.

1. Inicializujte teplotu objektu

Nastavte počiatočnú teplotu objektu na teplotu namočenia alebo predhriatia pece.

1. **Kompletné ovládacie prvky simulácie **

1. Definujte počet krokov

Typickú operáciu prenosu je možné simulovať v 10 až 20 krokoch.

1. Vyberte primárnu matricu

Zadajte objekt 1 (definovaný iba objekt) ako primárnu matricu.

1. Vypočítajte čas na krok

Vydeľte celkový čas prenosu počtom krokov.

1. **Uložiť údaje**

Uložte súbor kľúčového slova.

Prejdite na Generovanie databázy. Skontrolujte údaje. Ak sú nejaké žlté alebo červené príznaky, vyriešte ich a potom vygenerujte databázu. Opustite preprocesor a spustite simuláciu.

1. **Načítanie výsledkov simulácie do predprocesora na definovanie druhej operácie**

Vráťte sa do preprocesora a načítajte posledný krok z databázy.

1. **Definujte údaje o materiáli pre nástroje**

Zadajte tepelné údaje pre materiál nástroja

1. **Definujte nástroje**

1. Priradenie názvov nástrojov (voliteľné)

Pre referenciu počas predbežného a následného spracovania.

1. Definujte geometriu nástroja

Importujte alebo definujte geometriu hornej matrice (razníka) a spodnej matrice. Platia všetky pravidlá geometrie uvedené vyššie pre obrobok. Okrem toho:

* V prípade viacdielnych nástrojov nakreslite jedinú hranicu nástroja, ktorá definuje všetky vložky, vyradenia atď. Geometriu je možné neskôr oddeliť pre analýzu napätia formy. Pozrite si príručku alebo kontaktujte technickú podporu, ak je pre danú stanicu viac ako jeden pohyblivý nástroj.

* Geometriu nástroja mierne predĺžte pozdĺž stredovej čiary.

* V prípade nástrojov s klznou vôľou medzi razidlom a matricou zvýšte OD razidla, aby sa matrica mierne pretínala. Ďalšie podrobnosti nájdete v príručke alebo školiacom materiáli

* Na špičku akýchkoľvek špicatých dierovačov položte mierne rovnú plochu.

* Aj keď to nie je nevyhnutne potrebné, je vhodné, aby sa objekt 2 stal dierovačom alebo pohyblivým objektom.

1. Sieťovanie nástrojov

Použite približne 400 prvkov. Použite hustotu definovanú používateľom s 3 na kontaktnej ploche a 1 na zadnej strane matrice.

1. Priradenie materiálu nástroja

Uistite sa, že k nástrojom aj obrobku je priradený správny materiál

1. Priradenie teploty nástroja

Pred začatím tvarovania nastavte jednotnú teplotu nástroja.

1. **Definujte údaje o interobjekte**

1. Medziobjektové vzťahy

Obrobok by mal byť podriadený obom nástrojom. Koeficient prenosu tepla rozhrania by mal byť približne 0,004 pre anglické jednotky alebo 10 pre jednotky SI.

1. Umiestnenie objektu

Pomocou polohovania interferencie umiestnite obrobok na spodnú matricu. Počas tejto operácie nechajte hornú matricu mimo obrobku.

1. Vytvorte hraničné podmienky kontaktu

Predvolená hodnota tolerancie je primeraná.

1. **Kompletné ovládacie prvky simulácie **

1. Definujte počet krokov

Typickú operáciu odpočinku matrice je možné simulovať v 10 až 20 krokoch.

1. Vyberte primárnu matricu

Zadajte objekt 1 ako primárnu matricu.

1. Vypočítajte čas na krok

Vydeľte celkový čas prenosu počtom krokov.

1. Definujte názov operácie (voliteľné)

1. **Uložiť údaje**

Uložte súbor kľúčového slova.

Prejdite na Generovanie databázy. Skontrolujte údaje. Ak sú nejaké žlté alebo červené príznaky, vyriešte ich a potom vygenerujte databázu. Opustite preprocesor a spustite simuláciu.

1. **Načítanie výsledkov simulácie do predprocesora na definovanie operácie tvárnenia **

Vráťte sa do preprocesora a načítajte posledný krok z databázy.

1. **Nastaviť ovládacie prvky simulácie **

1. Názov operácie (voliteľné)

2. Vyberte režim simulácie

Teraz budeme simulovať kovanie, takže zapnite deformáciu (áno)

1. **Definujte údaje o materiáli pre obrobok**

Priraďte plastové (prietokové) údaje pre materiál obrobku. Uistite sa, že zvolený materiál pokrýva správny teplotný rozsah vrátane akéhokoľvek deformačného ohrevu a chladenia formy.

1. **Priraďte pohyb hornej matrice (razníka) **

Správanie tlače môže zohrávať úlohu vo výsledkoch. Viac informácií o správaní tlače nájdete v príručke alebo technickej podpore SFTC.

Nastavte smer (zvyčajne smerom nadol). Hodnota zdvihu by sa nemala meniť, pokiaľ sa nepoužije model mechanického lisu.

1. **Definujte údaje o interobjekte**

1. Medziobjektové vzťahy

Priraďte faktory trenia. Pre mazané kovanie za tepla sú typické hodnoty 0,2 až 0,3. Pre nemazané kovanie za tepla sú typické hodnoty od 0,8 do 1,0.

1. Umiestnenie objektu

Pomocou interferencie s obrobkom ako referenčným objektom umiestnite oba nástroje do kontaktu s obrobkom.

1. Vytvorte hraničné podmienky kontaktu

Predvolená hodnota tolerancie je primeraná.

1. **Kompletné ovládacie prvky simulácie **

1. Definujte počet krokov

* Pri veľmi obmedzenej deformácii, ako je štvorcová, použite 50 krokov

* Pre priemernú deformáciu, ako je smer, použite 100 krokov

* Pri problémoch s veľkým množstvom deformácie, ako je vytláčanie, použite 200 krokov

* Ušetrite každých 5 až 10 krokov.

1. Vyberte primárnu matricu

Zadajte číslo objektu pre razník(všeobecne objekt č.2)

1. Vypočítajte zdvih na krok

Odhadnite vzdialenosť, ktorú sa bude dierovač pohybovať (celkový zdvih). Vydeľte túto hodnotu počtom krokov a zadajte túto hodnotu do poľa Ťah na krok. Ak si nie ste istí celkovým úderom, pridajte 10 alebo 15 ďalších krokov. Tým sa prekročí cieľ a môžete zálohovať niekoľko krokov, aby ste dosiahli konečný výsledok.

1. Nastavte ovládacie prvky zastavenia (voliteľné)

Ak poznáte presnú vzdialenosť, do ktorej sa bude dierovač pohybovať, zadajte túto hodnotu pod ovládacími prvkami zastavenia. Ak nebola zadaná žiadna hodnota, simulácia sa zastaví po dokončení všetkých krokov.

1. Nastavte ovládanie čiastkových krokov

V časti Advanced Step Controls nastavte **Strain per Step** na 0,025.

1. **Uložiť údaje**

Uložte súbor kľúčových slov.

Prejdite na Generovanie databázy, Skontrolujte údaje. Ak sa vyskytnú nejaké žlté alebo červené príznaky, vyriešte ich a potom vygenerujte databázu. Opustite preprocesor a spustite simuláciu.

1. **Spustenie druhej operácie**

1. Identifikácia koncového bodu prvej operácie

Po dokončení simulácie prejdite do postprocesora a skontrolujte výsledky. Identifikujte krok, v ktorom bude dokončená prvá operácia, a poznačte si toto číslo kroku.

1. Načítanie výsledkov simulácie do predprocesora.

Vráťte sa do preprocesora a načítajte príslušný krok z databázy.

1. Simulujte chladenie počas prepravy na ďalšiu stanicu

Zvážte čas prenosu medzi stanicami. Pokyny na simuláciu prenosu tepla nájdete na začiatku tejto časti.

1. Zmena geometrie nástroja

Prejdite do editora geometrie, odstráňte geometriu nástroja (nie celý objekt) a importujte alebo vytvorte novú geometriu nástroja pre každý nástroj.

Umiestňovanie objektov

Z Interobject premiestnite nástroje proti obrobku pomocou interferencie.

1. Vytvoriť kontakt

Inicializujte a vygenerujte hraničné podmienky kontaktu.

1. Resetovať ovládacie prvky simulácie

Určte celkový počet krokov a zdvih na krok, ako je popísané vyššie.

1. Reset Zastavovací zdvih

Ak sa použil ovládací prvok zastavenia zdvihu, resetujte zdvih na nulu na ovládacích prvkoch pohybu objektu a resetujte ovládací prvok zastavenia pod ovládacími prvkami simulácie.

1. Napíšte databázu

Pri písaní starej databázy sa údaje pridajú na koniec existujúcej databázy. Prepíše všetky kroky po kroku, ktorý bol načítaný.

1. Ak nie je uložený príslušný koncový krok…..

Ak sa stretnete so situáciou, keď napríklad krok 90 nie je dostatočne formovaný, krok 100 je príliš formovaný a medzi tým nie sú uložené žiadne kroky, môžete načítať krok 90, zmeniť interval ukladania na 1 (uložiť každý krok) a potom zopakovať posledných 10 krokov simulácie, aby ste dosiahli správny krok zastavenia.

  

****

---
lang: sk
title: "Tvárnenie za studena"
---

# Tvárnenie za studena

Pri simulácii tvárnenia za studena je dôležité simulovať všetky kroky procesu, pretože účinky skorých krokov môžu ovplyvniť správanie sa neskorších krokov. Postup simulácie viacpolohového procesu je podrobne opísaný na konci tejto časti.

1. **Vytvoriť nový priečinok problémov (adresár)**

Každý problém s deformáciou by mal byť umiestnený vo vlastnom priečinku. Daný problém však môže obsahovať veľa operácií, všetky v tom istom databázovom súbore.

1. **Spustite predprocesor DEFORMÁCIE **

2. **Nastavte základné ovládacie prvky simulácie **

1. Názov problému (nepovinné)

Popisný názov problému – zobrazí sa na obrazovke počas predbežného a následného spracovania.

1. Jednotkový systém

Vyberte jednotky v angličtine alebo SI. Tým sa zmení mnoho predvolených hodnôt a ovplyvní sa spôsob importu údajov o materiáli.

1. Vyberte režim simulácie

Pri studených izotermických simuláciách by mal byť režim deformácie zapnutý (áno), prenos tepla a všetky ostatné režimy by mali byť vypnuté.

1. **Definujte materiál**

Definujte vlastnosti plastového materiálu pre materiál obrobku. Údaje o materiáli je možné načítať z databázy DEFORMAČNÝCH materiálov. Dávajte pozor, aby ste vybrali materiál s údajmi v teplotnom rozsahu, ktorý budete simulovať.

1. **Definujte obrobok**

1. Definujte typ objektu

Pre väčšinu simulácií je vhodný typ plastového objektu.

1. Definujte geometriu

Geometriu je možné definovať zo súboru STL alebo zadaním údajov tabuľky.

Požiadavky na geometriu obrobku:

* Normály geometrie musia vždy smerovať von

* Vždy skontrolujte geometriu.

1. **Sieťovanie objektu**

Typické postupnosti by mali používať veľkosti prvkov reprezentujúce geometrický detail dielu. V prípade pochybností bude mať viac prvkov tendenciu poskytovať presnejšie výsledky. Typické váhy:

* Zakrivenie=0,9

* Miera deformácie =0,7

* Kmeň =0,5

Teplota

1. **Definujte hraničné podmienky**

Symetrické roviny by mali byť definované buď s hraničnou podmienkou rýchlosti alebo s hraničnou podmienkou symetrie.

1. **Definujte nástroje**

1. Priradenie názvov nástrojov (voliteľné)

Pre referenciu počas predbežného a následného spracovania.

1. Definujte geometriu nástroja

Importujte alebo definujte geometriu pre dierovač a matricu. Platia všetky pravidlá geometrie uvedené vyššie pre obrobok. Okrem toho:

* V prípade viacdielnych nástrojov nakreslite jedinú hranicu nástroja, ktorá definuje všetky vložky, vyradenia atď. Geometriu je možné neskôr oddeliť pre analýzu napätia formy. Pozrite si príručku alebo kontaktujte technickú podporu, ak je pre danú stanicu viac ako jeden pohyblivý nástroj.

* Geometriu nástroja mierne predĺžte pozdĺž stredovej čiary.

* V prípade nástrojov s klznou vôľou medzi razidlom a matricou zvýšte OD razidla, aby sa matrica mierne pretínala. Ďalšie podrobnosti nájdete v príručke alebo školiacom materiáli

* Na špičku akýchkoľvek špicatých dierovačov položte mierne rovnú plochu.

* Aj keď to nie je nevyhnutne potrebné, je vhodné, aby sa objekt 2 stal dierovačom alebo pohyblivým objektom.

1. Definujte pohyb lisu pre dierovač

Všeobecne platí, že rýchlosť lisu neovplyvní výsledky simulácie pre simulácie tvárnenia za studena. Konštantná rýchlosť lisovania 10 in/sec alebo 250mm/sec je vo všeobecnosti primeraná. Nastavte smer (zvyčajne smerom nadol pre dierovač na vrchu). Používateľ by vo všeobecnosti nemal meniť hodnotu zdvihu.

1. **Definujte údaje o interobjekte**

1. Medziobjektové vzťahy

Obrobok by mal byť podriadený obom nástrojom. Pri dobre namazanom tvárnení za studena je primeraný koeficient trenia 0,08.

1. Umiestnenie objektu

Pomocou interferencie s obrobkom ako referenčným objektom umiestnite oba nástroje do kontaktu s obrobkom. Pre extrémne malé diely môže byť potrebná menšia tolerancia rušenia, aby sa zabránilo nadmernému prekrývaniu nástroja a obrobku.

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

Odhadnite vzdialenosť, ktorú sa bude dierovač pohybovať (celkový zdvih). Vydeľte túto hodnotu počtom krokov a zadajte túto hodnotu do poľa Ťah na krok. Ak si nie ste istí celkovým úderom, pridajte 10 alebo 15 ďalších krokov. Tým sa prekročí cieľ a môžete zálohovať niekoľko krokov

získať konečný výsledok.

1. Nastavte ovládacie prvky zastavenia (voliteľné)

Ak poznáte presnú vzdialenosť, do ktorej sa bude dierovač pohybovať, zadajte túto hodnotu pod ovládacími prvkami zastavenia. Ak nebola zadaná žiadna hodnota, simulácia sa zastaví po dokončení všetkých krokov.

1. Nastavte ovládanie čiastkových krokov

V časti Advanced Step Controls nastavte **Strain per Step** na 0,025.

1. **Uložiť údaje**

Uložte súbor kľúčového slova.

Prejdite na Generovanie databázy. Skontrolujte údaje. Ak sú nejaké žlté alebo červené príznaky, vyriešte ich a potom vygenerujte databázu. Opustite preprocesor a spustite simuláciu.

1. **Spustenie druhej operácie**

1. Identifikácia koncového bodu prvej operácie

Po dokončení simulácie prejdite do postprocesora a skontrolujte výsledky. Identifikujte krok, v ktorom bude dokončená prvá operácia, a poznačte si toto číslo kroku.

1. Načítanie výsledkov simulácie do predprocesora.

Vráťte sa do preprocesora a načítajte príslušný krok z databázy.

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

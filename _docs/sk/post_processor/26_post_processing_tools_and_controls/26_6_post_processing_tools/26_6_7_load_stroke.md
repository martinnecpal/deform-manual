---
lang: sk
title: "26.6.7. Zdvih zaťaženia"
---

# 26.6.7. Zaťaženie / zdvih ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }})

**[2D, 3D]**: Okno grafov slúži na vytváranie grafov závislosti zaťaženia, rýchlosti, krútiaceho momentu, uhlovej rýchlosti, energie a objemu od času (alebo zdvihu) pre daný objekt. (Pozri obr. 26.6.7.1.) Používateľ musí vybrať premenné osí X a Y, objekty z tabuľky objektov grafu a potom kliknúť na tlačidlo ![]({{ '/assets/icons/post_icons/mo_plot_button.jpg' | relative_url }}), aby sa graf zobrazil v grafickom okne. Jediný graf možno použiť na vytvorenie grafu pre viaceré objekty pre vybrané premenné osí X a Y. Kliknutím na bod v grafe sa načíta najbližší uložený krok z databázy.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_7_load_stroke/image001.jpg' | relative_url }})

Načítať okno s grafom zdvihu

Používateľ môže exportovať údaje grafu zobrazené v grafickom okne pomocou možnosti „Exportovať údaje grafu“, ktorá sa zobrazí po kliknutí pravým tlačidlom myši. Vlastnosti grafu, ako sú názvy a ich písmo, rozsah hodnôt, počet desatinných miest, štýl zobrazenia a zapnutie/vypnutie legendy, je možné zmeniť pomocou možnosti „Nastaviť vlastnosti grafu“, ktorá sa zobrazí po kliknutí pravým tlačidlom myši.

Poznámka:

V dôsledku rôznych faktorov je pri analýze metódou konečných prvkov (FEM) určitá strata objemu nevyhnutná. Ak však strata objemu presiahne približne 1 % celkového objemu, malo by to byť dôvodom na obavy.

Na karte „Ovládacie prvky“ sú k dispozícii možnosti „Mierka“, „Jednotky“, „Plynulý pohyb“, „Kumulatívna energia“ a „Operácie“, ktoré slúžia na výber konkrétnych premenných osí X a Y a na určenie počtu operácií. Účel týchto možností je vysvetlený nižšie,

  * **Mierka:** Pomocou tejto možnosti je možné zmeniť mierku hodnôt na osi Y grafu. Táto možnosť je k dispozícii iba pre premenné zaťaženia a sily.

  * **Jednotky:** Používateľ si môže z roletového menu vybrať jednotky, v ktorých sa majú zobrazovať hodnoty zaťaženia a sily. Pole „Jednotky“ je aktívne pre premenné zaťaženia a sily. V databáze anglických jednotiek ponúka možnosti zobrazenia zaťaženia v klb, anglických tonách alebo tonách SI, v databáze jednotiek SI ponúka možnosti zobrazenia zaťaženia v N, anglických tonách alebo tonách SI.

  * **Operácie:** Toto pole sa aktivuje, keď používateľ načíta databázu s viacerými operáciami. Používateľ môže vytvoriť graf pre príslušné operácie výberom čísiel operácií z roletového menu.

  * **Plynulý zdvih:** Táto funkcia sa aktivuje, keď používateľ znázorní graf závislosti zdvihu od zaťaženia. Ak si používateľ želá zobraziť graf plynule pre viaceré operácie, môže použiť túto možnosť. Ak používateľ načíta databázu viacerých operácií a je zaškrtnuté políčko „Plynulý zdvih“, zdvih bude plynulý počas všetkých operácií. Ak používateľ toto políčko odškrtne, zdvih nebude počas operácií plynulý.

  * **Kumulatívna energia:** Táto funkcia sa aktivuje, keď používateľ vykreslí premennú „Čas vs. energetický stav“. Táto voľba vykresľuje kumulatívnu spotrebu energie za všetky operácie. Ak používateľ načíta databázu s viacerými operáciami a je zaškrtnuté políčko „Kumulatívna energia“, graf spotreby energie bude kumulatívny pre všetky operácie. Ak používateľ toto políčko odškrtne, spotreba energie pre každú operáciu sa znázorní samostatne.

  * **Karta „Možnosti“:** ponúka možnosti zobrazenia, ako napríklad zapnutie/vypnutie zobrazenia priebehu krokov, zobrazenie absolútnej hodnoty a možnosti vyhladenia grafu (pozri obr. 26.6.7.2.). Účel týchto možností je vysvetlený nižšie,

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_7_load_stroke/image002.jpg' | relative_url }})

Okno s nastaveniami grafu zaťaženia a zdvihu

  * **Zobrazovač krokov:** Zaškrtnutím tohto políčka sa v okne grafu zobrazí zobrazovač krokov, ktorý označuje hodnoty a polohu v grafe. Ak používateľ vyberie akýkoľvek medzistupeň, v danom kroku sa zobrazia hodnoty na osiach X a Y.

  * **Absolútna hodnota:** Zaškrtnutím tohto políčka sa v grafe zobrazujú iba absolútne hodnoty.

  * **Vyhladenie:** Možnosť vyhladenia slúži na vyhladenie grafu pomocou prepínačov prvého a druhého rádu a hodnoty vizuálnych efektov. Čím vyššia je hodnota vizuálnych efektov, tým väčšia bude chyba vyhladenia.

  * **Medzi príčiny straty objemu a spôsoby ich odstránenia patria:** Zmenšovanie rozmerov pri opätovnom vytváraní siete: Prejavuje sa výrazným poklesom objemu v jednotlivých krokoch opätovného vytvárania siete. Ak sú prvky v okolí relatívne ostrého rohu príliš veľké, časť prvku, ktorá preniká do rohu, sa pri premeshovaní stratí. Tomu je možné zabrániť vynútením jemnejšej siete v danej oblasti pomocou okien hustoty siete a použitím spúšťača premeshovania „Maximálna hĺbka interferencie“.

  * **Nadmerné hydrostatické napätie** alebo **príliš malá konštanta objemovej penalizácie:** Prejavuje sa strmým sklonom objemovej krivky medzi jednotlivými prepočítaniami siete. Skontrolujte, či údaje o prietokovom napätí používajú správne jednotky. Pri úlohách, ako je extrudovanie s vysokým pomerom a extrémne vysokým hydrostatickým napätím, môže byť potrebné zvýšiť konštantu objemovej penalizácie o jeden alebo dva rády. Zvýšenie konštanty penalizácie môže viesť k problémom s konvergenciou, preto je potrebné nájsť rovnováhu.

  * Kompenzácia objemu (vlastnosti objektov predspracovateľa) sa dá použiť na reguláciu straty objemu počas opätovného vytvárania siete.

  * Na obmedzenie straty objemu počas simulácie je možné použiť subkrokovanie polygónov.

## Vlastnosť grafu

Možnosť „Vlastnosti grafu“, ktorá slúži na úpravu zobrazenia grafu, je dostupná v kontextovom menu grafu, ako je znázornené na obr. 26.6.7.3. Táto voľba umožňuje používateľovi zmeniť vlastnosti grafu, ako sú Názov a popisy, Rozsah, Legenda, Séria, Značkovač krokov, Téma, Vyhladenie, Rovnica a Mriežka/Značky, ako je znázornené na obr. 26.6.7.4. Pomocou týchto možností môže používateľ upraviť zobrazenie názvov, legendy, krokov a mriežok, rozsah hodnôt osí, definovať rovnicu a podobne.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_7_load_stroke/image003.jpg' | relative_url }})

Kontextové menu grafu

### Názov a popisy

Na tejto karte môže používateľ zmeniť názov a veľkosť písma nadpisu a popiskov osí X a Y (pozri obr. 26.6.7.4.). Zaškrtnutím políčka „Preložiť nadpis a popisky osí“ môže používateľ preložiť názvy nadpisu a popiskov osí do jazyka vybraného v nastaveniach prostredia programu DEFORM.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_7_load_stroke/image004.jpg' | relative_url }})

Karta „Názov a štítky“

### Rozsah

Na tejto karte máme k dispozícii viacero možností na nastavenie rozsahu osí.

  * **Určuje systém:** Možnosť „Určuje systém“ je predvolene zvolená a ak je táto možnosť zvolená, minimálnu a maximálnu hodnotu osi určí systém na základe výstupnej hodnoty premennej osi. 

  * **Zobraziť počiatok:** Minimálna hodnota osi je nastavená na nulu a maximálna hodnota osi sa určuje na základe výstupných hodnôt premennej osi.

  * **Aktuálna operácia:** Táto možnosť je k dispozícii iba pre os X a pri jej výbere sa minimálna a maximálna hodnota osi X nastavia na základe výstupnej hodnoty premennej osi X pri aktuálnej operácii.

  * **Definované používateľom:** Používateľ môže nastaviť maximálne a minimálne hodnoty pre os.

  * **Vedecký formát:** Zaškrtnutím tohto políčka sa hodnoty na osiach zobrazia vo vedeckom formáte.

  * **Počet desatinných miest:** Používateľ môže nastaviť počet desatinných miest, ktoré sa majú zobrazovať pri premenných na osi.

  * **Mierka:** Táto možnosť je k dispozícii iba pre os Y. Používateľ môže zmeniť mierku hodnôt na osi Y stanovením mierky. Ak sa použije mierka, akákoľvek rovnica definovaná na karte „Rovnica“ sa prepíše funkciou mierky. 

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_7_load_stroke/image005.jpg' | relative_url }})

Karta Rozsah

### Legenda

Táto voľba umožňuje používateľovi zobraziť alebo skryť legendu na grafe, ako je znázornené na obr. 26.6.7.6.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_7_load_stroke/image006.jpg' | relative_url }})

Karta „Legenda“

### Séria

Ak graf pozostáva z viacerých kriviek, používateľ môže zmeniť farbu, typ a hrúbku každej krivky kliknutím na príslušnú bunku v tabuľke zobrazenú na tejto karte. Krivky môžeme tiež zobraziť alebo skryť pomocou príslušného začiarkavacieho políčka v stĺpci „Viditeľnosť“, ako je znázornené na obr. 26.6.7.7.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_7_load_stroke/image007.jpg' | relative_url }})

Karta „Séria“

### Sledovanie krokov

  * **Indikačná čiara**: Nad grafom sa zobrazuje indikačná čiara kroku, ktorá označuje aktuálnu pozíciu kroku na grafe. 

  * **Stav zapnutia/vypnutia**: Používateľ môže zobraziť alebo skryť indikátor krokov výberom príslušného prepínača, ako je znázornené na obr. 26.6.7.8.

  * **Hrúbka**: Hrúbku čiary kroku je možné nastaviť výberom príslušného prepínača, ako je znázornené na obr. 26.6.7.8.

  * **Farba**: Farbu čiary sledovania krokov je možné zmeniť kliknutím na tlačidlo „Farba“ a výberom farby z rozbaľovacieho menu, ako je znázornené na obr. 26.6.7.8.

  * **Popisky**: Hodnoty premenných osí sa zobrazujú ako popisky na základe aktuálneho výberu kroku. Používateľ môže popisky zobraziť alebo skryť výberom príslušného prepínača so stavom Zapnuté/Vypnuté v časti Popisky, ako je znázornené na obr. 26.6.7.8.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_7_load_stroke/image008.jpg' | relative_url }})

Sledovanie krokov

### Téma

Tu môže používateľ zmeniť farbu pozadia grafu, ako je znázornené na obr. 26.6.7.9. Systém má ako predvolenú tému nastavenú možnosť „Štandardná na bielom pozadí“. Ak chce používateľ ako predvolenú tému pre všetky grafy použiť akúkoľvek inú možnosť dostupnú na tejto karte, môže po výbere témy zaškrtnúť políčko „Nastaviť ako predvolenú tému“ a kliknúť na tlačidlo „Použiť“.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_7_load_stroke/image009.jpg' | relative_url }})

Karta „Téma“

### Vyhladzovanie

Vo väčšine prípadov výstupné krivky nemusia byť hladké a môžu byť zvlnené; v takom prípade môže používateľ krivky vyhladzovať na prvý alebo druhý rád, a to výberom príslušného prepínača a hodnoty v položke „Vizuálne efekty“.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_7_load_stroke/image010.jpg' | relative_url }})

Karta „Vyhladenie“

### Rovnica

Používateľ môže definovať rovnicu pre os Y zaškrtnutím políčka „Použiť rovnicu“. Premenné, ktoré je možné použiť v rovnici, sú k dispozícii v roletovom menu „Premenné“ a funkcie, ktoré je možné použiť v rovnici, sú k dispozícii v roletovom menu „Funkcie“, ako je znázornené na obr. 26.6.7.11. Definovaná funkcia bude prepísaná škálovacou funkciou, ak používateľ zaškrtne políčko „Škálovací faktor“ na karte „Rozsah“.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_7_load_stroke/image011.jpg' | relative_url }})

Karta „Rovnica“

### Mriežka/Čiarka

**Značka**: Používateľ môže nastaviť počet značiek pre hlavnú a vedľajšiu mriežku na osiach X a Y pomocou príslušných polí s dvojitým rámčekom v časti „Tick“. 

**Mriežka:** Používateľ môže zapnúť alebo vypnúť zobrazenie mriežkových čiar pomocou príslušných začiarkavacích políčok na karte „Mriežka“, ako je znázornené na obr. 26.6.7.12. Hrúbku a štýl mriežkových čiar je možné nastaviť pomocou možností dostupných v roletovom menu, ako je znázornené na obr. 26.6.7.12. Používateľ môže nastaviť farbu mriežkových čiar pomocou tlačidla Farba, ako je znázornené na obr. 26.6.7.12.

  
![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_7_load_stroke/image012.jpg' | relative_url }})

Karta „Mriežka/Označenie“

---
lang: sk
title: "28. Vytváranie správ"
---

# 28\. Vytváranie správ

28.1. Kapitola

28.2. Časti

28.2.1. Prehľad vstupných údajov pre simuláciu

28.2.2. Tok kovu

28.2.3. Zhrnutie

28.2.4. Graf (zaťaženie – zdvih)

28.2.5. Stavová premenná

28.2.6. Oblasť záujmu

28.2.7. Kupóny

28.2.8. Sledovanie bodov

28.2.9. Flownet

28.2.10. Sledovanie premenných používateľa po odoslaní

28.2.11. Vlastné nastavenia

Vytvorenie správy

Na karte Správa môžeme pridať viacero kapitol kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) a dvojitým kliknutím na názov kapitoly môžeme tento názov upraviť (štandardne sa zobrazí názov databázy), ako je znázornené na obr. 28.1.

![]({{ '/assets/images/post_processor/28_report_generation/image001.jpg' | relative_url }})

Pridávanie kapitol do zoznamu správ

**Hierarchia správ:**

Správa je rozdelená na kapitoly, pričom každá kapitola obsahuje oddiely a každý oddiel obsahuje vybrané výstupy, ako sú grafy, diagramy stavových premenných atď., ako je znázornené na obr. 28.2.

![]({{ '/assets/images/post_processor/28_report_generation/image002.jpg' | relative_url }})

Strom objektov správy

## Kapitola

Kapitola obsahuje sekcie s rôznymi typmi výstupov, ako je sledovanie bodov, kontúrové znázornenie stavových premenných, grafy atď., a používateľ si môže vybrať rozsah operácií, ktoré je možné pridať do správy, ako je znázornené na obr. 28.3. Ďalšie informácie týkajúce sa úpravy kapitoly nájdete v [28.2. Editing Chapters](/docs/en/post_processor/28_report_generation/28_1_editing_chapters/).

![]({{ '/assets/images/post_processor/28_report_generation/image003.jpg' | relative_url }})

Stránka kapitoly

### Výber databázy

V zozname „Výber databázy“ môžeme vybrať databázu potrebnú na vytvorenie správy.

### Názov kapitoly

V zozname kapitol môžeme podľa potreby upraviť názvy kapitol.

### Výber prevádzkového rozsahu

V rámci kapitoly je k dispozícii výber rozsahu operácií, čo umožňuje generovanie správ po jednotlivých operáciách. Používateľ si môže vybrať rozsah operácií, pre ktoré sa má správa vygenerovať. Ak chce používateľ vygenerovať správu pre nepo sebe idúce operácie, je potrebné pre príslušné operácie vytvoriť ďalšie kapitoly.

## Časti

V časti „Sekcie“ zaškrtnite políčko príslušného nástroja, ktorý chcete pridať do správy, a všimnete si, že príslušné nástroje sa pridajú do stromu objektov. (Pozri obr. 28.3.)

Na vytváranie správ sú k dispozícii nasledujúce nástroje:

  * Prehľad vstupných údajov pre simuláciu

  * Prúdenie kovu

  * Zhrnutie

  * Graf (zaťaženie – zdvih)

  * Stavová premenná

  * Oblasť záujmu

  * Kupóny

  * Sledovanie bodov

  * Flownet

  * Sledovanie premenných používateľa príspevku

  * Na mieru

### **Súhrn vstupných údajov simulácie**

Ak pri generovaní správy zaškrtneme políčko „Simulation input summary“, môžeme si prezrieť obsah jednotlivých kapitol, súhrn jednotlivých operácií a údajov o objektoch, ako aj výstupy jednotlivých sekcií. Obr. 28.4. znázorňuje ukážku správy vygenerovanej pre položku „Simulation input summary“.

Od verzie 12.0.2, ak používateľ nechce, aby sa v súbore PDF so správou nachádzal súhrn simulácie, je potrebné na stránke „Kapitola“ zrušiť zaškrtnutie políčka „Súhrn vstupných údajov simulácie“.

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image004.jpg' | relative_url }}) ![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image005.jpg' | relative_url }})

Súhrn simulácie v súbore PDF

### Metal Flow

Prúdenie kovu v jednotlivých operáciách je možné pridať do správy pomocou sekcie „Prúdenie kovu“. Na stránke „Prúdenie kovu“ môžeme vybrať počiatočný, stredný (možno vybrať až 7 krokov) a konečný krok, ako je znázornené na obr. 28.5. Funkcia „Prúdenie kovu“ zobrazuje deformáciu objektu bez akýchkoľvek kontúr stavových premenných vo vybraných krokoch operácií. Súradnice uzlov a údaje o prepojení prvkov môžeme exportovať zaškrtnutím políčka „Export súradníc uzlov a prepojení prvkov“. V poslednom kroku môžeme tiež exportovať 2D (formát DXF) alebo 3D (formát STL) geometriu zaškrtnutím políčka „Geometria“. Obr. 28.6. ukazuje ukážku správy vygenerovanej pre tok kovu.

![]({{ '/assets/images/post_processor/28_report_generation/image004.jpg' | relative_url }})

Stránka Metal Flow

![]({{ '/assets/images/post_processor/28_report_generation/image005.jpg' | relative_url }})

Vygenerovaná správa pre úsek toku kovu

### Zhrnutie

Súhrnný graf stavovej premennej je možné pridať do správy pomocou tlačidla ![]({{ '/assets/icons/post_icons/mo_add_report_output_button.jpg' | relative_url }}) a výberom požadovanej stavovej premennej (ako je znázornené na obr. 28.7.). Príslušné súhrnné údaje o stavovej premennej môžeme tiež exportovať zaškrtnutím políčka Export. Ak je políčko Export zaškrtnuté, vybraný súhrnný výstup sa počas generovania správy uloží do priečinka Report vo formáte .CSV. Pre vybraný objekt a prevádzkový rozsah sa vygenerujú krivky min/max vybranej stavovej premennej, ako je znázornené na obr. 28.8.

![]({{ '/assets/images/post_processor/28_report_generation/image006.jpg' | relative_url }})

Súhrnný výstup

![]({{ '/assets/images/post_processor/28_report_generation/image007.jpg' | relative_url }})

Náhľad vybranej stavovej premennej

### Graf (zaťaženie – zdvih)

Na stránke „Graph output“ je možné definovať viacero grafov x-y, ako napríklad záťaž-zdvih, rýchlosť-čas, zdvih-energia atď., pomocou tlačidla ![]({{ '/assets/icons/post_icons/mo_add_report_output_button.jpg' | relative_url }}), ako je znázornené na obr. 28.9. Príslušné údaje o zaťažení a zdvihu môžeme tiež exportovať zaškrtnutím políčka Export. Ak je políčko Export zaškrtnuté, vybraný súhrnný výstup sa počas generovania správy uloží do priečinka Report vo formáte .CSV. Pre vybraný objekt a rozsah prevádzky sa vygeneruje príslušný graf; na obr. 28.10 je znázornený graf zaťaženia a zdvihu.

![]({{ '/assets/images/post_processor/28_report_generation/image008.jpg' | relative_url }})

Výber grafu výstupných údajov

![]({{ '/assets/images/post_processor/28_report_generation/image009.jpg' | relative_url }})

Náhľad výstupu grafu zdvihu zaťaženia

### Stavová premenná

Do správy je možné pridať kontúrový graf stavových premenných na základe výstupu stavových premenných. V závislosti od požiadaviek môže používateľ na stránke „Stavové premenné“ vybrať počiatočný krok, stredné kroky (až 7) a konečný krok, ktoré sa majú zahrnúť do správy, ako je znázornené na obr. 28.11. Pre vybrané kroky sa vygeneruje kontúrový graf a pridá sa do správy.

![]({{ '/assets/images/post_processor/28_report_generation/image010.jpg' | relative_url }})

Stránka výberu kroku pre stavovú premennú

Na výstupnej stránke môže používateľ pomocou tlačidla „![]({{ '/assets/icons/post_icons/mo_add_report_output_button.jpg' | relative_url }}) premenné“ vybrať premennú stavu, pre ktorú sa má do správy pridať kontúrový graf, a môžeme tiež exportovať príslušné údaje o premennej stavu zaškrtnutím políčka „Export“, ako je znázornené na obr. 28.12., 

![]({{ '/assets/images/post_processor/28_report_generation/image011.jpg' | relative_url }})

Zoznam výstupov stavových premenných

Pre každú stavovú premennú môže používateľ vybrať objekty, pre ktoré sa má v správe vygenerovať kontúrový graf, typ zobrazenia, typ kontúry, rozsah kontúry a typ farebnej stupnice. 3D model s výškovým grafom je možné zahrnúť do súboru PDF zaškrtnutím políčka „Zahrnúť 3D model (PDF)“, ako je znázornené na obr. 28.13. Vygenerované. V priečinku „Modely“ sa pre každú stavovú premennú vygeneruje súbor 3D PDF.

![]({{ '/assets/images/post_processor/28_report_generation/image012.jpg' | relative_url }})

Výber objektu a zobrazenia pre príslušné okno výstupnej premennej

Súbory PDF a PPT vytvorené v rámci generovania správ sú zobrazené na obr. 28.14 až obr. 26.16.

![]({{ '/assets/images/post_processor/28_report_generation/image013.jpg' | relative_url }})

Vygenerovaný súbor PDF obsahujúci 9 uložených krokov operácie (vo forme viacerých obrázkov)

![]({{ '/assets/images/post_processor/28_report_generation/image014.jpg' | relative_url }})

Vygenerovaný 3D PDF súbor pre operáciu 4

![]({{ '/assets/images/post_processor/28_report_generation/image015.jpg' | relative_url }})

Vygenerovaný 3D PDF súbor pre premennú efektívneho stavu napätia

### Oblast záujmu

Oblasť záujmu (ROI) je ľubovoľný tvar (2D alebo 3D), ktorý vymedzuje oblasť, z ktorej systém zhromažďuje informácie o stavových premenných vybraného objektu a zobrazuje minimálnu a maximálnu hodnotu vybranej stavovej premennej.

Na stránke výberu oblasti záujmu môžeme pridať oblasti pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}). Pre pridanú oblasť môžeme vytvoriť geometriu pomocou základných tvarov alebo môžeme importovať súbor s geometriou pomocou možností importu (pozri obr. 28.17.),

![]({{ '/assets/images/post_processor/28_report_generation/image016.jpg' | relative_url }})

Stránka na výber oblasti záujmu

Na stránke „Výstupy“ môžeme pridať požadovanú premennú stavu výstupu a v stĺpci „Oblasť“ môžeme z roletového menu vybrať oblasť, z ktorej sa majú údaje o premennej stavu extrahovať, ako je znázornené na obr. 28.18.

![]({{ '/assets/images/post_processor/28_report_generation/image017.jpg' | relative_url }})

Výstupná stránka „Region of Interest“

### Kupón

Kvalifikácia dielov si vyžaduje podrobné vyhodnotenie kritických miest z hľadiska mikrostruktúry a správania mechanických vlastností, pričom priemysel musí identifikovať kritické oblasti v diele na základe výsledkov modelovania tvárnenia a tepelného spracovania. Pre identifikované kritické oblasti je potrebné extrahovať stavové premenné modelovania. Na tento proces je možné využiť funkciu „Coupon capability“ v programe DEFORM.

Na stránke výberu kupónu pridajte oblasť kupónu, aby sa mohli extrahovať údaje o premenných stavu v danej oblasti kupónu (pozri obr. 28.19.).

![]({{ '/assets/images/post_processor/28_report_generation/image018.jpg' | relative_url }})

Stránka s výberom kupónov

Na stránke „Coupon Output“ môžeme pridať požadované premenné výstupného stavu, z ktorých je potrebné extrahovať údaje. (Pozri obr. 28.20.)

![]({{ '/assets/images/post_processor/28_report_generation/image019.jpg' | relative_url }})

Výber premennej stavu výstupu kupónu

Správa vygenerovaná pre sekcie s kupónmi je zobrazená nižšie na obr. 28.21.

![]({{ '/assets/images/post_processor/28_report_generation/image020.jpg' | relative_url }})

Výsledok vygenerovania kupónu

### Sledovanie bodov

Používateľ môže pridať grafy, aby pochopil správanie konkrétnej stavovej premennej vo vybraných bodoch pomocou sledovania bodov. Na stránke výberu sledovania bodov vyberte krok, typ bodov (môže byť „Pohyblivé“ alebo „Pevné“) a v okne „Definovať“ vyberte body pre sledovanie bodov, ako je znázornené na obr. 28.22.

![]({{ '/assets/images/post_processor/28_report_generation/image021.jpg' | relative_url }})

Stránka výberu sledovania bodov

Na výstupnej stránke „Sledovanie bodov“ vyberte stavovú premennú, pre ktorú sa má vykresliť graf, a zaškrtnite políčko „Exportovať“, ak je potrebné exportovať údaje o stavovej premennej zo sledovania bodov (pozri obr. 28.23.).

![]({{ '/assets/images/post_processor/28_report_generation/image022.jpg' | relative_url }})

Výber stavovej premennej výstupu sledovania bodu

Na každej stránke s výstupnými stavovými premennými si môže používateľ vybrať objekty, ktoré sa majú zahrnúť do sledovania bodov, a v možnostiach zobrazenia (ako je znázornené na obr. 28.24) môže tiež zvoliť, či sa majú vykresliť kontúry a graf, alebo len graf.

![]({{ '/assets/images/post_processor/28_report_generation/image023.jpg' | relative_url }})

Okno premennej výstupného stavu

Vygenerovaná správa pre časť „Sledovanie bodov“ je znázornená na obr. 28.25.

![]({{ '/assets/images/post_processor/28_report_generation/image024.jpg' | relative_url }})

Zobrazuje ukážku vygenerovanej správy o sledovaní bodov 

### Flownet

Ak chcete do správy zahrnúť sieť tokov objektu, na stránke „Flownet“ vyberte krok, v ktorom sa má sieť tokov pridať do správy. V súčasnosti sú k dispozícii možnosti „Začiatočný krok“, „Konečný krok“ alebo „Začiatočný a konečný krok“, ktoré je možné použiť zaškrtnutím príslušného políčka (pozri obr. 28.26).

![]({{ '/assets/images/post_processor/28_report_generation/image025.jpg' | relative_url }})

Stránka Flownet

Na stránke „Výber objektu“ vyberte objekt, pre ktorý sa má vygenerovať graf Flownet, vyberte typ vzoru a nastavte parametre vzoru tak, ako je znázornené na obr. 28.27. Ukážka grafu Flownet z vygenerovanej správy je zobrazená na obr. 28.28.

![]({{ '/assets/images/post_processor/28_report_generation/image026.jpg' | relative_url }})

Nastavenie vzoru Flownet

![]({{ '/assets/images/post_processor/28_report_generation/image027.jpg' | relative_url }})

Vygenerovaný súbor PPT pre jednoduchú obsluhu

### Sledovanie premenných používateľa príspevku

To umožňuje používateľovi vygenerovať správu pre používateľom definované premenné, ktoré sú definované v používateľských rutinách postprocesora.

Na stránke „Knižnica“ vyberte v poli „Knižnica“ súbor DLL vygenerovaný z užívateľskej rutiny a z roletového zoznamu rutín vyberte číslo rutiny, ako je znázornené na obr. 28.29.

![]({{ '/assets/images/post_processor/28_report_generation/image028.jpg' | relative_url }})

Stránka výberu knižnice a rutiny

Na stránke „Tracking“ vyberte v položke „Method type“ (Typ metódy) voľbu „Tracking variables“ (Sledovanie premenných), ak nie je k dispozícii súbor PDB, potom v položke „Calculation type“ (Typ výpočtu) vyberte typ „Nodes“ (Uzly) alebo „Elements“ (Prvky) a následne kliknite na „Track data“ (Sledovať údaje), Po dokončení sledovania premenných pre konkrétnu databázu sa v adresári problému vygeneruje súbor PDB, takže v nasledujúcich fázach následného spracovania môže používateľ na karte Sledovanie vybrať existujúci súbor PDB a následne priamo vykresliť používateľské premenné. (Pozri obr. 28.30.)

![]({{ '/assets/images/post_processor/28_report_generation/image029.jpg' | relative_url }})

Stránka s údajmi o sledovaní

Na stránke Výstup pridajte stavové premenné tak, že v roletovom zozname vyberiete typ stavovej premennej „Post user var“ a v stĺpci „Komponenta“ vyberiete stavové premenné; príslušné údaje o stavových premenných môžete tiež exportovať zaškrtnutím políčka „Export“, ako je znázornené na obr. 28.31. Pre každú stavovú premennú môže používateľ vybrať objekt, zobrazenie, typ kontúry, rozsah kontúry a typ farebnej lišty, ako je znázornené na obr. 28.32, a následne vygenerovať správu na stránke „Generate report“.

![]({{ '/assets/images/post_processor/28_report_generation/image030.jpg' | relative_url }})

Stránka výberu výstupu

![]({{ '/assets/images/post_processor/28_report_generation/image031.jpg' | relative_url }})

Stránka výberu objektov a zobrazenia

### Na mieru

Na vlastnej stránke sa aktivujú možnosti nástrojov pre príspevky a je možné uložiť väčšinu úkonov súvisiacich s následným spracovaním, ako napríklad výber objektov, režim zobrazenia a výber krokov.

**Príklad** :

V tomto príklade vytvárame správu pre jednoduchú 2D databázu impulzov s využitím nástrojov Graph (Load-Stroke), State variable, Point tracking a Flownet post.

Otvorte databázu vyriešených 2D špičiek v príspevku „Next gen“, kliknite na kartu „Report“. Na stránke „Chapter“ zaškrtnite políčka „Graph (Load-Stroke)“, „State variable“, „Point tracking“ a v sekcii „Flownet“, ako je znázornené na obr. 28.33. Kliknite na ![]({{ '/assets/icons/post_icons/mo_flownet_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/post_processor/28_report_generation/image032.jpg' | relative_url }})

Vybrané nástroje na tvorbu príspevkov na stránke „Kapitola“

**Graf (zdvih zaťaženia):**

Na stránke „Graph“ použite predvolený názov sekcie a kliknite na ![]({{ '/assets/icons/post_icons/mo_flownet_next_button.jpg' | relative_url }}). Vykreslíme graf zaťaženia a zdvihu pre hornú matricu, preto kliknite na ![]({{ '/assets/icons/post_icons/mo_add_report_output_button.jpg' | relative_url }}). V pridanom zozname vyberte pre os X položku „Stroke“ z roletového menu a pre os Y položku „Y-Load“, ako je znázornené na obr. 28.34, a kliknite na ![]({{ '/assets/icons/post_icons/mo_flownet_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/post_processor/28_report_generation/image033.jpg' | relative_url }})

Stránka výberu výstupu grafu

Na stránke „Load-Stroke“ vyberte ako „Objects“ položku „Primary die“ a zobrazí sa náhľad grafu, ktorý bude zahrnutý do správy, ako je znázornené na obr. 28.35. Následne kliknite na ![]({{ '/assets/icons/post_icons/mo_flownet_next_button.jpg' | relative_url }})..

![]({{ '/assets/images/post_processor/28_report_generation/image034.jpg' | relative_url }})

Výber objektu grafu „Zaťaženie – zdvih“ a jeho náhľad

**Stavová premenná:**

Na stránke „State variable“ (Premenné stavu) nastavte počiatočný, koncový a stredný krok na hodnotu 7 a kliknite na ![]({{ '/assets/icons/post_icons/mo_flownet_next_button.jpg' | relative_url }}). Na stránke „Output“ (Výstup) (obr. 28.36.) pridajte premenné „Damage“ (Poškodenie) a „Strain“ (Deformácia) na vykreslenie obrysov a kliknite na ![]({{ '/assets/icons/post_icons/mo_flownet_next_button.jpg' | relative_url }}). Na príslušných stránkach premenných vyberte v položke „Objekty“ hodnotu „Obrobok“. V položke „Zobrazenie“ vyberte „Auto“ a ostatné polia ponechajte v predvolených nastaveniach. Kliknite na ![]({{ '/assets/icons/post_icons/mo_flownet_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/post_processor/28_report_generation/image035.jpg' | relative_url }})

Zoznam výstupov stavových premenných

**Sledovanie bodov:**

Na stránke výberu sledovania bodov definujte body pre sledovanie bodov v okne „Definovať“, ako je znázornené na obr. 28.37., ponechajte predvolené nastavenie a kliknite na ![]({{ '/assets/icons/post_icons/mo_flownet_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/post_processor/28_report_generation/image036.jpg' | relative_url }})

Výber bodov pre sledovanie bodov

Na výstupnej stránke pridajte jednu výstupnú premennú, ako premennú pre sledovanie bodu vyberte „Teplota“ a kliknite na ![]({{ '/assets/icons/post_icons/mo_flownet_next_button.jpg' | relative_url }}). V okne „Výstup teploty“ vyberte ako typ zobrazenia možnosť „Kontúra + graf“ a ako obrobok vyberte „Objekty“, potom kliknite na ![]({{ '/assets/icons/post_icons/mo_flownet_next_button.jpg' | relative_url }}).

**Flownet:**

Na stránke Flownet použite predvolený typ krokov (ako pre počiatočný, tak aj pre koncový krok) a kliknite na ![]({{ '/assets/icons/post_icons/mo_flownet_next_button.jpg' | relative_url }}). Na stránke Výber objektu vyberte ako objekt Obrobok a kliknite na ![]({{ '/assets/icons/post_icons/mo_flownet_next_button.jpg' | relative_url }}). Na stránke Mriežka vyberte typ Posun a kliknite na ![]({{ '/assets/icons/post_icons/mo_flownet_next_button.jpg' | relative_url }}). Na stránke Definícia mriežky nastavte hodnotu Vzdialenosť posunu na 0,01in a kliknite na ![]({{ '/assets/icons/post_icons/mo_preview_button.jpg' | relative_url }}). Posunutá hranica objektu sa zobrazí v strome objektov, ako je znázornené na obr. 28.38. Potom klikajte na ![]({{ '/assets/icons/post_icons/mo_flownet_next_button.jpg' | relative_url }}), až sa zobrazí stránka Vytvoriť správu.

![]({{ '/assets/images/post_processor/28_report_generation/image037.jpg' | relative_url }})

Náhľad ofsetovej sieťky proti hmyzu

**Vytvorenie správy:**

**Správa vo formáte PDF:**

Na vytvorenie správy vo formáte PDF je potrebné zaškrtnúť políčko PDF a následne kliknúť na ![]({{ '/assets/icons/post_icons/mo_generate_button.jpg' | relative_url }}), čím sa správa vygeneruje. V vygenerovanom súbore PDF si používateľ môže prezrieť obsah (pozri obr. 28.39.), súhrn simulácie (obr. 28.40.) a následne pridané časti správy (pozri obr. 28.41. až obr. 28.44.).

![]({{ '/assets/images/post_processor/28_report_generation/image042.jpg' | relative_url }})

Obsah v súbore PDF

![]({{ '/assets/images/post_processor/28_report_generation/image043.jpg' | relative_url }}) ![]({{ '/assets/images/post_processor/28_report_generation/image044.jpg' | relative_url }})

Súhrn simulácie v súbore PDF

Od verzie 12.0.2, ak používateľ nechce, aby sa v PDF súbore správy nachádzalo zhrnutie simulácie, musí na stránke „Kapitola“ zrušiť zaškrtnutie políčka „Zahrnúť zhrnutie simulácie“.

  
![]({{ '/assets/images/post_processor/28_report_generation/image039.jpg' | relative_url }})

Graf závislosti zaťaženia od zdvihu vytvorený v programe PPT

![]({{ '/assets/images/post_processor/28_report_generation/image038.jpg' | relative_url }})

Graf premennej „Generated Damage State“ vo formáte PDF

![]({{ '/assets/images/post_processor/28_report_generation/image040.jpg' | relative_url }})

Vytvorený graf sledovania bodov pre premennú „Teplota“ v programe PPT

![]({{ '/assets/images/post_processor/28_report_generation/image041.jpg' | relative_url }})

Graf s posunutým bodom Flownet v poslednom kroku

**Správa v formáte PPT:** Ak chcete vygenerovať správu do súboru PPT, je potrebné zaškrtnúť políčko PPT a kliknúť na ![]({{ '/assets/icons/post_icons/mo_generate_button.jpg' | relative_url }}). Spustí sa generovanie správy a po jej dokončení V súboroch PDF a PPT si používateľ môže zobraziť výstup kliknutím na tlačidlo ![]({{ '/assets/icons/post_icons/mo_view_button.jpg' | relative_url }}) (Zobraziť).

Poznámka: V súbore PPT sa nevytvorí výstup vo formáte 3D PDF; okrem výstupu vo formáte 3D PDF sa všetky ostatné výstupy uložia do súboru PPT.

**Súvisiace témy:**

[Report Generation Setup in MO Preprocessor](/docs/en/operation_templates/41_report_generation/41_1_report_generation/)

[25\. Post Processor Layout](/docs/en/post_processor/25_post_processor_layout/25_post_processor_layout/)

[27\. Introduction to Report Generation](/docs/en/post_processor/27_introduction_to_report_generation/27_introduction_to_report_generation/)

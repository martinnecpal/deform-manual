---
lang: sk
title: "41.1. Vytváranie správ"
---

# 41.1. Vytváranie správ

41.1.1. Správa

Hierarchia správ

41.1.2. Kapitola

Názov kapitoly

Výber prevádzkového rozsahu

41.1.3. Časti

  * Prehľad vstupných údajov pre simuláciu

  * Prúdenie kovu

  * Zhrnutie

  * Graf (zaťaženie – zdvih)

  * Premenná stavu

  * Oblast záujmu

  * Kupóny

  * Sledovanie bodov

  * Flownet

  * Sledovanie premenných používateľa príspevku

  * Na mieru

## Správa

V správe môžeme pridať viacero kapitol kliknutím na tlačidlo ![]({{ '/assets/icons/post_icons/mo_add_report_section_button.jpg' | relative_url }}) a dvojitým kliknutím na názov kapitoly môžeme tento názov upraviť (štandardne sa zobrazí „Operation range“), ako je znázornené na obr. 41.1.1.

Pomocou možností „Importovať šablónu správy do súboru“ ![]({{ '/assets/icons/post_icons/mo_import_button.jpg' | relative_url }}) a „Importovať šablónu správy do knižnice“****![]({{ '/assets/icons/post_icons/mo_import_form_library_button.jpg' | relative_url }}) môžeme importovať uloženú šablónu správy (.DS) a pomocou možností Exportovať šablónu správy do súboru ![]({{ '/assets/icons/post_icons/mo_export_report_template_button.jpg' | relative_url }}) a Exportovať šablónu správy do knižnice ![]({{ '/assets/icons/post_icons/mo_export_template_to_librart_button.jpg' | relative_url }}) môžeme šablónu správy uložiť. 

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image001.jpg' | relative_url }})

Pridávanie kapitol do zoznamu správ

### Hierarchia správ

Správa je rozdelená na kapitoly, pričom každá kapitola obsahuje oddiely a každý oddiel obsahuje vybrané výstupy, ako sú grafy, diagramy stavových premenných atď., pozri obr. 41.1.2.

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image002.jpg' | relative_url }})

Strom objektov správy

## Kapitola

Kapitola obsahuje sekcie s rôznymi typmi výstupov, ako je sledovanie bodov, kontúrové znázornenie stavových premenných, grafy atď., a používateľ môže zmeniť názov kapitoly a vybrať rozsah operácií, ktoré sa môžu pridať do správy, ako je znázornené na obr. 41.1.3.

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image003.jpg' | relative_url }})

Stránka kapitoly

### Názov kapitoly

V poli so zoznamom kapitol môžeme podľa potreby upraviť názov kapitoly. Obr. 41.1.4. znázorňuje možnosti nastavenia názvu kapitoly, ktoré sú k dispozícii na jeho definovanie.

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image006.jpg' | relative_url }})

Možnosti názvov kapitol

### Výber prevádzkového rozsahu

V rámci kapitoly je k dispozícii výber rozsahu operácií, čo umožňuje generovanie správ po jednotlivých operáciách. Používateľ si môže vybrať rozsah operácií, pre ktoré sa má správa vygenerovať. Ak chce používateľ vygenerovať správu pre nepo sebe idúce operácie, je potrebné pre príslušné operácie vytvoriť ďalšie kapitoly.

## Časti

V časti „Sekcie“ zaškrtnite políčko príslušného nástroja, ktorý chcete pridať do správy, a všimnete si, že príslušné nástroje sa pridajú do stromu objektov (pozri obr. 41.1.3.).

Na vytváranie správ sú k dispozícii nasledujúce nástroje:

  * Prehľad vstupných údajov pre simuláciu

  * Prúdenie kovu

  * Zhrnutie

  * Graf (zaťaženie – zdvih)

  * Premenná stavu

  * Oblast záujmu

  * Kupóny

  * Sledovanie bodov

  * Flownet

  * Sledovanie premenných používateľa príspevku

  * Na mieru

  * **Súhrn vstupných údajov simulácie**

Ak pri generovaní správy zaškrtneme políčko „Súhrn vstupných údajov simulácie“, môžeme si prezrieť obsah jednotlivých kapitol, súhrn jednotlivých operácií, údaje o objektoch a výstupy jednotlivých sekcií. Obr. 41.1.5. znázorňuje ukážku správy vygenerovanej pre súhrn vstupných údajov simulácie.

Od verzie 12.0.2, ak používateľ nechce, aby sa v PDF súbore správy nachádzalo zhrnutie simulácie, je potrebné na stránke „Kapitola“ zrušiť zaškrtnutie políčka „Zhrnutie vstupných údajov simulácie“.

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image004.jpg' | relative_url }}) ![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image005.jpg' | relative_url }})

Súhrn simulácie v súbore PDF

  * **Metal Flow**

Prúdenie kovu v jednotlivých operáciách je možné pridať do správy pomocou sekcie „Prúdenie kovu“. Na stránke „Tok kovu“ môžeme vybrať počiatočný krok, stredný krok (môžeme vybrať až 7 krokov) a konečný krok, ako je znázornené na obr. 41.1.6. Tok kovu zobrazuje deformáciu objektu bez akéhokoľvek obrysu stavovej premennej vo vybraných krokoch operácií. 

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image007.jpg' | relative_url }})

Stránka Metal Flow

Na stránke „Ovládacie prvky“ môžeme vybrať objekty, ktoré sa majú zobraziť v nástroji Metal Flow, typ zobrazenia, spôsob zobrazenia kontaktov a rozloženie PDF pre výstup z nástroja Metal Flow (pozri obr. 41.1.7.). Okrem toho môžeme exportovať súradnice uzlov a údaje o prepojeniach prvkov zaškrtnutím políčok „Exportovať súradnice uzlov“ a „Prepojenia prvkov“ na stránke „Ovládacie prvky“. V poslednom kroku môžeme tiež exportovať 2D (formát DXF) alebo 3D (formát STL) geometriu zaškrtnutím políčka „Geometria“. Obr. 41.1.8. ukazuje ukážku správy vygenerovanej pre program Metal Flow.

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image008.jpg' | relative_url }})

Stránka „Regulátory prietoku kovov“

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image009.jpg' | relative_url }})

Vygenerovaná správa pre úsek toku kovu

  * **Zhrnutie**

Súhrnný graf stavovej premennej je možné pridať do správy pomocou tlačidla ![]({{ '/assets/icons/post_icons/mo_add_report_output_button.jpg' | relative_url }}) a výberom požadovanej stavovej premennej. Príslušné súhrnné údaje o stavových premenných môžeme tiež exportovať zaškrtnutím políčka Export. Ak je políčko Export zaškrtnuté, vybraný súhrnný výstup sa počas generovania správy uloží do priečinka Report vo formáte .CSV. (pozri obr. 41.1.9.). Následne musí používateľ pre každú vybranú stavovú premennú vybrať objekty, pre ktoré sa majú vygenerovať krivky min/max stavovej premennej v okne každej stavovej premennej, ako je znázornené na obr. 41.1.10. Ukážka správy vygenerovanej pre súhrn je znázornená na obr. 41.1.11.

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image010.jpg' | relative_url }})

Súhrnný výstup

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image011.jpg' | relative_url }})

Výber objektu pre výstup príslušnej stavovej premennej

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image012.jpg' | relative_url }})

Vygenerovaná správa pre časť „Súhrn“

  * **Graf (zaťaženie – zdvih)**

Na stránke „Graph output“ je možné definovať viaceré grafy x-y, ako napríklad záťaž-zdvih, rýchlosť-čas, zdvih-energia atď., pomocou tlačidla ![]({{ '/assets/icons/post_icons/mo_add_report_output_button.jpg' | relative_url }}), ako je znázornené na obr. 41.1.12. Príslušné údaje o zaťažení a zdvihu je možné exportovať zaškrtnutím políčka „Export“. Ak je políčko „Export“ zaškrtnuté, vybraný súhrnný výstup sa počas generovania správy uloží do priečinka „Report“ vo formáte .CSV. Následne musí používateľ pre každý typ výstupu na stránke „Graph output“ (Výstup grafu) vybrať objekt, pre ktorý sa má graf vygenerovať (obr. 41.1.13). Ukážka správy vygenerovanej pre graf je zobrazená na obr. 41.1.14.

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image013.jpg' | relative_url }})

Výber grafu výstupných údajov

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image014.jpg' | relative_url }})

Výber objektov pre výstup grafu času načítania

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image015.jpg' | relative_url }})

Vygenerovaná správa pre sekciu „Graf“

  * **Stavová premenná**

Do správy je možné pridať kontúrový graf stavovej premennej z výstupu stavovej premennej. V závislosti od požiadaviek môže používateľ na stránke „Stavové premenné“ vybrať počiatočný krok, stredné kroky (až 7) a konečný krok, ktoré sa majú zahrnúť do správy, ako je znázornené na obr. 41.1.15. Kontúrový graf sa vygeneruje pre vybrané kroky a pridá sa do správy.

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image016.jpg' | relative_url }})

Stránka výberu krokov pre stavové premenné

Na výstupnej stránke môže používateľ pomocou tlačidla „![]({{ '/assets/icons/post_icons/mo_add_report_output_button.jpg' | relative_url }}) premenné“ vybrať premennú stavu, pre ktorú sa má do správy pridať kontúrový graf, a môžeme tiež exportovať príslušné údaje o premennej stavu zaškrtnutím políčka „Export“, ako je znázornené na obr. 41.1.16.

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image017.jpg' | relative_url }})

Zoznam výstupov stavových premenných

Pre každú stavovú premennú môže používateľ vybrať objekty, pre ktoré sa má v správe vygenerovať kontúrový graf, okno zobrazenia, typ kontúry, rozsah kontúry, typ farebnej stupnice a rozloženie PDF.3D model s kontúrovým grafom je možné zahrnúť do PDF zaškrtnutím políčka „Zahrnúť 3D model (PDF)“, ako je znázornené na obr. 41.1.17. Výstup v 3D PDF formáte sa teraz uloží do priečinka „Modely“, a to pre každý výstup zvlášť.

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image018.jpg' | relative_url }})

Výber objektu a rozloženia PDF pre príslušné okno výstupnej premennej

Súbory PDF a PPT vytvorené v rámci generovania správ sú zobrazené na obr. 41.1.18 až obr. 41.1.20.

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image019.jpg' | relative_url }})

Vygenerovaný súbor PDF obsahujúci 9 uložených krokov operácie (rozloženie PDF 9)

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image020.jpg' | relative_url }})

Vygenerovaný 3D PDF súbor pre operáciu 4

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image021.jpg' | relative_url }})

Vygenerovaná prezentácia PPT pre premennú „Stress Effective State“

  * **Zaujímavá oblasť**

Oblasť záujmu (ROI) je ľubovoľný tvar (2D alebo 3D), ktorý vymedzuje oblasť, z ktorej systém zhromažďuje informácie o stavových premenných vybraného objektu a zobrazuje minimálnu a maximálnu hodnotu vybranej stavovej premennej.

Na stránke výberu oblasti záujmu môžeme pridávať oblasti pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}). Pre pridanú oblasť môžeme vytvoriť geometriu pomocou základných tvarov alebo môžeme importovať súbor s geometriou pomocou možností importu. (Pozri obr. 41.1.21.)

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image022.jpg' | relative_url }})

Stránka na výber oblasti záujmu

Na stránke „Výstupy“ môžeme pridať požadovanú premennú stavu výstupu a v stĺpci „Oblasť“ môžeme z roletového menu vybrať oblasť, z ktorej sa majú údaje o premennej stavu extrahovať (pozri obr. 41.1.22).

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image023.jpg' | relative_url }})

Výstupná stránka „Region of Interest“

Správa vygenerovaná pre sekcie s kupónmi je zobrazená nižšie na obr. 41.1.23.

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image024.jpg' | relative_url }})

Výsledok generovania oblasti záujmu

  * **Kupón**

Kvalifikácia dielov si vyžaduje podrobné vyhodnotenie kritických miest z hľadiska mikrostruktúry a zmien mechanických vlastností, pričom priemysel musí identifikovať kritické oblasti v diele na základe výsledkov modelovania tvárnenia a tepelného spracovania. Pre identifikované kritické oblasti je potrebné extrahovať stavové premenné modelovania. Na tento proces je možné využiť funkciu „Coupon capability“ v programe DEFORM.

Na stránke výberu kupónu pridajte oblasť kupónu, aby sa mohli extrahovať údaje o premenných stavu v danej oblasti kupónu (pozri obr. 41.1.24.).

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image025.jpg' | relative_url }})

Stránka s výberom kupónov

Na stránke „Coupon Output“ môžeme pridať požadované premenné výstupného stavu, z ktorých je potrebné extrahovať údaje. (Pozri obr. 41.1.25.)

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image026.jpg' | relative_url }})

Výber premennej stavu výstupu kupónu

Správa vygenerovaná pre sekcie s kupónmi je zobrazená nižšie na obr. 41.1.26.

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image028.jpg' | relative_url }})

Výsledok vygenerovaného kupónu vo formáte PDF

  * **Sledovanie bodov**

Používateľ môže pridať grafy, aby pochopil správanie konkrétnej stavovej premennej vo vybraných bodoch pomocou sledovania bodov. Na stránke výberu sledovania bodov vyberte krok, typ bodov (môže byť „Pohyblivé“ alebo „Pevné“) a v okne „Definovať“ vyberte body pre sledovanie bodov, ako je znázornené na obr. 41.1.27.

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image027.jpg' | relative_url }})

Stránka na výber sledovania bodov

Na stránke „Výstup sledovania bodov“ vyberte stavovú premennú, pre ktorú sa má vykresliť graf (pozri obr. 41.1.28), a zaškrtnite políčko „Exportovať“, ak je potrebné exportovať údaje o stavovej premennej zo sledovania bodov.

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image029.jpg' | relative_url }})

Výber stavovej premennej výstupu sledovania bodu

Na každej stránke s výstupnými stavovými premennými si používateľ môže vybrať objekty, ktoré sa majú zahrnúť do sledovania bodov, a tiež si môže v možnostiach zobrazenia vybrať, či sa má zobraziť „Kontúra + graf“, „Graf“ alebo „Iba kontúra“, ako je znázornené na obr. 41.1.29.

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image030.jpg' | relative_url }})

Okno premennej výstupného stavu

Vygenerovaná správa vo formáte PDF pre časť „Sledovanie bodov“ je znázornená na obr. 41.1.30.

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image031.jpg' | relative_url }})

Ukazuje ukážku vygenerovanej správy vo formáte PDF pre sledovanie bodov s grafickým znázornením v programe Contour+ 

  * **Flownet**

Ak chcete do správy zahrnúť sieť tokov objektu, na stránke „Flownet“ vyberte krok, v ktorom sa má sieť tokov pridať do správy. V súčasnosti sú k dispozícii možnosti „Začiatočný krok“, „Konečný krok“ alebo „Začiatočný a konečný krok“, ktoré je možné použiť zaškrtnutím príslušného políčka (pozri obr. 41.1.31).

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image032.jpg' | relative_url }})

Stránka Flownet

Na stránke „Výber objektu“ vyberte objekt, pre ktorý sa má vygenerovať graf Flownet, vyberte typ vzoru a nastavte parametre vzoru podľa obr. 41.1.32. Ukážka grafu Flownet z vygenerovanej správy je zobrazená na obr. 41.1.33.

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image033.jpg' | relative_url }})

Nastavenie vzoru Flownet

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image034.jpg' | relative_url }})

Vytvorený súbor PPT pre jednoduchú obsluhu

  * **Sledovanie premenných používateľa príspevku**

Toto umožňuje používateľovi vygenerovať správu pre používateľom definované premenné po spracovaní, ktoré sú definované v používateľských rutínach postprocesora (pozri obr. 41.1.34.). V závislosti od požiadaviek si používateľ môže na stránke „Premenné stavu“ vybrať počiatočný krok, stredné kroky (až 7) a konečný krok, ktoré sa majú zahrnúť do správy.

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image035.jpg' | relative_url }})

Stránka pre používateľské premenné príspevkov

Na stránke „Knižnica“ vyberte v poli „Knižnica“ súbor DLL vygenerovaný z užívateľskej rutiny a z roletového zoznamu „Rutina“ vyberte číslo rutiny. (Pozri obr. 41.1.35.)

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image036.jpg' | relative_url }})

Stránka výberu knižnice a rutiny

Na stránke „Tracking“ vyberte v položke „Method type“ (Typ metódy) voľbu „Tracking variables“ (Sledovanie premenných), ak nie je k dispozícii súbor PDB, potom v položke „Calculation type“ (Typ výpočtu) vyberte typ „Nodes“ (Uzly) alebo „Elements“ (Prvky) a následne kliknite na „Track data“ (Sledovať údaje), Po dokončení sledovania premenných pre konkrétnu databázu sa v adresári problému vygeneruje súbor PDB, takže v nasledujúcich fázach následného spracovania môže používateľ na karte Sledovanie vybrať existujúci súbor PDB a následne priamo vykresliť používateľské premenné. (Pozri obr. 41.1.36.)

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image037.jpg' | relative_url }})

Stránka s údajmi o sledovaní

Na stránke „Výstup“ pridajte stavové premenné tak, že v roletovom zozname vyberiete typ stavovej premennej „Post user var“ a v stĺpci „Komponenta“ vyberiete stavové premenné. Príslušné údaje o stavových premenných môžete tiež exportovať zaškrtnutím políčka „Export“, ako je znázornené na obr. 41.1.37. Pre každú stavovú premennú môže používateľ vybrať objekt, zobrazenie, typ kontúry, rozsah kontúry, rozloženie PDF a typ farebnej lišty, ako je znázornené na obr. 41.1.38.

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image038.jpg' | relative_url }})

Stránka výberu výstupu

![]({{ '/assets/images/operation_templates/41_report_generation/41_1_report_generation/image039.jpg' | relative_url }})

Stránka výberu objektov a zobrazenia

  * **Na mieru**

Na vlastnej stránke môžeme uložiť aktuálne zobrazenie objektu, pričom zobrazenie v okne na vlastnej stránke sa uloží do správy.

**Súvisiace témy:**

[41\. Introduction ot Report Generation](/docs/en/operation_templates/41_report_generation/41_introduction_to_report_generation/)

[28.1. Editing Chapters](/docs/en/post_processor/28_report_generation/28_1_editing_chapters/)

[28\. Report Generation in Post-Processor](/docs/en/post_processor/28_report_generation/28_report_generation/)

[Report Generation lab in MO](/docs/en/labs/report_generation_lab/report_generation_lab_in_mo/)

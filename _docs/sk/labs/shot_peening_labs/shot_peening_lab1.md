---
lang: sk
title: "Laboratórium kužeľovania injekcií1"
---

# Lab1: Laboratórium peeningu

Toto laboratórium demonštruje nastavenie kužeľového kužeľového ozubenia pomocou šablóny kužeľového kužeľa.

1.1. Spustenie sprievodcu Shot Peen

1.2. Vytvorenie nového projektu

1.3. Definovanie parametrov procesu zpevňovania povrchu

1.4. Nakladací materiál pre šikmé ozubené koleso

1.5. Definovanie vstupu napätia

1.5.1. Nastavenie mikro modelu (2D)

1.5.2. Spustiť

1.5.3. 2D mikro model nárazového napätia a výstupu reziduálneho napätia

1.5.4. Merané zostatkové napätie

1.6. Definovanie 3D modelu pre kuličkovanie

1.6.1. Definovanie obrobku

1.6.1.1. Stránka objektu obrobku

1.6.1.2. Definovanie geometrie obrobku

1.6.1.3. Definovanie materiálu pre obrobok

1.6.1.4. Generovanie pletiva pre obrobok

1.6.1.5. Priradenie hraničných podmienok k obrobku

1.6.1.6. Definovanie pohybu obrobku

1.6.2. Definovanie trysky #1

1.6.2.1. Definícia objektu tryskyč.1

1.6.2.2. Definovanie umiestnenia dýzy

1.6.2.3. Definovanie pohybu dýzy

1.6.3. Umiestnenie

1.7. Analýza procesu kužeľového zpevňovania

1.7.1. Simulácia častíc

1.7.1.1. Nastavenia simulácie častíc

1.7.1.2. Výsledok simulácie častíc

1.7.2. Simulácia nárazu

1.7.2.1. Nastavenia simulácie nárazu

1.7.2.2. Výsledok simulácie nárazu

1.7.3. Analýza zvyškového napätia

1.7.3.1. Nastavenia analýzy zvyškového napätia

1.7.3.2. Simulácia analýzy zostatkového napätia

1.7.3.3. Výsledky analýzy zvyškového napätia

## Spustenie sprievodcu Shot Peen

Ak chcete spustiť Sprievodcu zrýchlením záberu, dvakrát kliknite na „DEF_GUI_SHOTPEEN_64.EXE“ v inštalačnom adresári softvéru Deform. Sprievodca kužeľovým kužeľom vyzerá tak, ako je znázornené na obr. STPL1.1.

![]({{ '/assets/images/labs/shot_peening_labs/shot_peening_lab1/image0001.jpg' | relative_url }})

Používateľské rozhranie Sprievodcu kužeľovaním

Vytvára sa nový projekt

Vytvorte nový problém buď výberom **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})* ***New** alebo kliknutím na ikonu New project ![]({{ '/assets/icons/pre_icons/mo_new_file_button.jpg' | relative_url }}). Zobrazí sa okno Nový projekt (pozri obr. STPL1.2.), definujte názov projektu ako „**Gear_Lab** “ a vyberte systém jednotky ako „**System* ***International (SI)** “, ako je znázornené v [Fig. STPL1.2]()., kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) otvorte projekt Shot peen.

![]({{ '/assets/images/labs/shot_peening_labs/shot_peening_lab1/image0002.jpg' | relative_url }})

Vytvára sa nový projekt

V používateľskom rozhraní sa pridá nová karta Gear_Lab a môžeme pozorovať, že na nastavenie procesu je k dispozícii operačný strom na zpevňovanie povrchu. V predvolenom nastavení sa otvorí okno „Shot Peen Process“ na definovanie parametrov procesu peeningu, pozri obr. STPL1.3.

![]({{ '/assets/images/labs/shot_peening_labs/shot_peening_lab1/image0003.jpg' | relative_url }})

Používateľské rozhranie Shot Peening zobrazujúce operačný strom a okno procesu Shot Peen

## Definovanie parametrov procesu zpevňovania povrchu

Na stránke Shot Peen Process môžeme importovať predtým uložený súbor modelu Data Analytics (DA) pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) a pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}) môžeme uložiť existujúci súbor modelu DA projektu do knižnice alebo do priečinka projektu.

Do poľa Process Tag (Značka procesu) môžeme zadať informácie o procese pre referenciu.

V časti Pelety je možné definovať priemer pelety a jej hmotnosť. Vyberte možnosť „Nový…“ pomocou rozbaľovacieho poľa Názov a definujte priemer peliet ako 0,2794 mm a hmotnosť ako 0,08976 mg a uložte súbor modelu DA do priečinka projektu pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}). Uložené parametre palety môžeme načítať aj výberom príslušného názvu z rozbaľovacieho zoznamu Name (Názov). Vzhľadom na to, že simulujeme operáciu kužeľového kužeľa na 20 sekúnd, definujte čas kužeľového kužeľa ako **20** s, ako je znázornené na obr. STPL1.4. V časti Proces môžeme definovať parametre procesu, ako je čas kužeľovania, hmotnostný prietok, tlak vzduchu a výstupná rýchlosť. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku zoznamu materiálov.

![]({{ '/assets/images/labs/shot_peening_labs/shot_peening_lab1/image0004.jpg' | relative_url }})

Definovanie parametrov procesu zpevňovania povrchu

## Nakladací materiál pre šikmé ozubené koleso

Na stránke zoznamu materiálov kliknite na ikonu ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať materiál z knižnice) a načítajte materiál "** AISI-302,COLD[70F(20C)]** " dostupný v skupine **Stainless_steel** v knižnici materiálov, ako je znázornené na obr. STPL1.5.

![]({{ '/assets/images/labs/shot_peening_labs/shot_peening_lab1/image0005.jpg' | relative_url }})

Načítava sa materiál z knižnice pre špirálový gar

## Definovanie vstupu stresu

Vstupné hodnoty napätia pre objekt prechádzajúci kužeľovým kužeľom môžu byť dané buď zo simulovaného mikro modelu (2D), alebo z experimentálne nameraných hodnôt zostatkového napätia. V tomto laboratóriu použijeme mikro model (2D) a experimentálne namerané hodnoty reziduálneho napätia.

### Nastavenie mikro modelu (2D)

Kliknite na položku „* * Mikro *** *model (2D**)“ v operačnom strome pod vstupom napätia. Na karte Proces je v zozname predvolene vybraný materiál „AISI-302,COLD[70F(20C)]“. Nastavte maximálny počet zásahov ako 10 a počet uhlov nárazu ako 3\. Predvolené uhly nárazu sú 80, 50 a 20 s účinnosťou 0,5, 0,5 a 0,85, ako je znázornené na obr. STPL1.6.

Na karte Nastavenia môžeme definovať nastavenia riadenia simulácie, ako je čas na krok, počet krokov a krokový prírastok na uloženie pre simuláciu nakladania a vykladania. V tomto laboratóriu použijeme predvolené nastavenia riadenia simulácie, takže kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_2_button.jpg' | relative_url }}) a vygenerujte databázy pre simuláciu Micro model 2D. Vygeneruje sa nezávislá databáza s každým uhlom nárazu. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) spustite stránku na simuláciu 2D databáz mikro modelu.

![]({{ '/assets/images/labs/shot_peening_labs/shot_peening_lab1/image0006.jpg' | relative_url }})

Nastavenia procesu pre simuláciu 2D mikro modelu

CHOD

Na stránke Run môžeme simulovať databázy 2D mikro modelu pomocou tlačidla Run action v dolnej časti (pozri obr. STPL1.7.). Keď klikneme na ![]({{ '/assets/icons/post_icons/run_label_button.jpg' | relative_url }}), otvorí sa dialógové okno Spustiť možnosti. Vyberte simulačný server a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_submit_to_qeue_button.jpg' | relative_url }}) spustite simuláciu.

Po ukončení simulácie môžeme sledovať stav Progress ako 100 %. Po dokončení simulácie začne automatická extrakcia údajov extrahovať výstup (nárazové napätie a výstup zvyškového napätia) zo simulovanej databázy a potom exportovať do súboru Data Analytics (DA model) na ďalšie spracovanie. Po dokončení extrakcie a exportu údajov môžeme správu pozorovať ako „Hotovo“ (pozri obr. STPL1.8.). Pomocou možnosti ![]({{ '/assets/icons/post_icons/mo_extract_label_button.jpg' | relative_url }}) môžeme znova extrahovať údaje a uložiť ich do súboru modelu DA. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku Impact stress.

![]({{ '/assets/images/labs/shot_peening_labs/shot_peening_lab1/image0007.jpg' | relative_url }})

Spustiť stránku Možnosti na simuláciu 2D mikro modelu

![]({{ '/assets/images/labs/shot_peening_labs/shot_peening_lab1/image0008.jpg' | relative_url }})

Spustiť stránku zobrazujúcu stav po dokončení simulácie

### 2D mikro model má vplyv na napätie a výstup zvyškového napätia

Po dokončení simulácie môžeme kliknúť na položku Impact stress alebo Residual Stress v operačnom strome a zobraziť príslušný výstup z 2D Micro modelu. Výsledky simulácie mikro modelu je možné zobraziť pomocou obrysových grafov a grafov.

Pomocou ![]({{ '/assets/icons/post_icons/mo_contour_plot_button.jpg' | relative_url }}) môžeme vykresliť kontúry a pomocou ![]({{ '/assets/icons/post_icons/mo_graph_plot_button.jpg' | relative_url }}) môžeme vykresliť grafy pre radiálne napätie, efektívne napätie a efektívne napätie, ako je znázornené na obr. STPL1.9. a obr. STPL1.10.

![]({{ '/assets/images/labs/shot_peening_labs/shot_peening_lab1/image0009.jpg' | relative_url }})

Radiálne nárazové napätie Obrysový graf

![]({{ '/assets/images/labs/shot_peening_labs/shot_peening_lab1/image0010.jpg' | relative_url }})

Radiálne napätie nárazu pozdĺž hĺbky

Zobrazenie grafov a obrysových grafov pre viaceré uhly a viaceré zásahy je možné ovládať pomocou možností dostupných pod ovládaním displeja, ako je znázornené na obr. STPL1.11. Používateľ môže vybrať rozsah údajov, ktoré sa majú zobraziť pomocou ![]({{ '/assets/icons/post_icons/mo_grid_selection_button.jpg' | relative_url }}), na obr. STPL1.11. Zobrazí sa hit #10. (Pozri obr. STPL1.11.) Grafické znázornenia sa môžu prekrývať, aby sa porovnali výsledky pomocou ![]({{ '/assets/icons/post_icons/mo_superimpose_icon.jpg' | relative_url }}), ako je znázornené na obr. STPL1.12.

![]({{ '/assets/images/labs/shot_peening_labs/shot_peening_lab1/image0011.jpg' | relative_url }})

Zobrazenie výberu rozsahu údajov (hit #10) grafov

![]({{ '/assets/images/labs/shot_peening_labs/shot_peening_lab1/image0012.jpg' | relative_url }})

Super impozantné grafy nad sebou pre vybraný rozsah údajov (hit #10)

  
Pomocou možností ![]({{ '/assets/icons/post_icons/mo_sv_value_table_icon.jpg' | relative_url }}) môžeme zobraziť hodnoty Max radiálneho napätia, Max efektívneho napätia, Max efektívneho napätia, Dimple diameter a Dimple height state variables buď ako tabuľku alebo ako zobrazenie grafu v závislosti od výberu v ovládacom prvku Display (Zobrazenie). (Pozri obr. STPL1.13. a obr. STPL1.14.).

![]({{ '/assets/images/labs/shot_peening_labs/shot_peening_lab1/image0013.jpg' | relative_url }})

Maximálne hodnoty radiálneho napätia nárazu ako tabuľka

![]({{ '/assets/images/labs/shot_peening_labs/shot_peening_lab1/image0014.jpg' | relative_url }})

Maximálne hodnoty radiálneho napätia nárazu podľa grafu

### Merané zostatkové napätie

Ak chcete poskytnúť merané zvyškové napätie ako vstup, kliknite na položku „**Merané zvyškové napätie** “ v strome objektov. Musíme poskytnúť údaje aspoň pre dva uhly nárazu. V tomto laboratóriu definujeme rovnaké namerané hodnoty zostatkového napätia pre oba uhly nárazu 90 a 20, ako je znázornené na obr. STPL1.15.

**Hĺbka** |  **Stres**
---|---
0,0001  |  -93
0,00025  |  -95
0,0005  |  -72
0,00075  |  -50
0,001  |  -27
0,002  |  -11
0,005  |  0
0,01  |  0,2
  
  
  
![]({{ '/assets/images/labs/shot_peening_labs/shot_peening_lab1/image0015.jpg' | relative_url }})

Vstupné údaje nameraných hodnôt zostatkového napätia

## Definovanie 3D modelu na zpevňovanie povrchu

Kliknite na položku „* * Model ** * * 3D * * “ v strome objektov, na stránke Model 3D môžeme vybrať objekty potrebné na nastavenie 3D modelu. V tomto laboratóriu požadujeme obrobok a jeden predmet dýzy. V predvolenom nastavení sa vyberie jeden obrobok a jeden objekt dýzy, pozri obr. STPL1.16. Pri predvolených nastaveniach teda kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku Obrobok.

![]({{ '/assets/images/labs/shot_peening_labs/shot_peening_lab1/image0016.jpg' | relative_url }})

Definovanie požadovaných objektov pre 3D model zpevňovania povrchu

### Definovanie obrobku

#### Stránka objektu obrobku

Na stránke obrobku ponechajte predvolený názov objektu ako „* * Workpeice** “ a kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku Geometria obrobku.

#### Definovanie geometrie obrobku

Kliknite na Import geometrie z knižnice ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) a zaťažte** Gear.stl** z priečinka * *3D/LABS/Shotpeening **, importovaná geometria špirálového ozubeného kolesa vyzerá ako na obr. STPL1.17. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po stránku Materiál obrobku.

![]({{ '/assets/images/labs/shot_peening_labs/shot_peening_lab1/image0017.jpg' | relative_url }})

Importovaná geometria ozubeného kolesa

#### Definovanie materiálu pre obrobok

Priraďte materiál „**AISI ****-302,STUDENÝ[70F(20C)]** “ pre obrobok, kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_back_button.jpg' | relative_url }}) vytvorte sieťovinu pre obrobok.

#### Generovanie pletiva pre obrobok

Na stránke Mesh definujte cieľový počet prvkov ako * * 128000 * * a pomer veľkosti ako **2**. Kliknite na **Povlak** Tab, kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) pre pridanie **8***vrstiev * * a pre každú vrstvu definujte hrúbku povlaku (mikrón) ako **10 * * , potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) pre vytvorenie povrchovej siete. Kliknite na „**Áno** “ v kontextovom okne „Generovať povrchovú sieť?“ a „**Nie** “ v kontextovom okne „Predvolená hraničná podmienka“. Vygenerovaná sieť pre obrobok je, ako je znázornené na obr. STPL1.19. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po stránku Podmienky ohraničenia.

**Poznámka** : Po vytvorení povrchovej siete je vhodné skontrolovať povrchovú sieť. Ak sa zistí problém, môže byť potrebné znížiť hustotu ôk (vytvoriť väčšie prvky) alebo znížiť celkovú hĺbku povlaku. V súčasnosti existuje obmedzenie, že celková hĺbka náteru nemôže byť väčšia ako ½ veľkosti najmenšieho prvku.

![]({{ '/assets/images/labs/shot_peening_labs/shot_peening_lab1/image0018.jpg' | relative_url }})

Všeobecné nastavenie povrchovej siete pre obrobok

![]({{ '/assets/images/labs/shot_peening_labs/shot_peening_lab1/image0019.jpg' | relative_url }})

Nastavenia povrchovej siete pre obrobok

#### Priradenie hraničných podmienok k obrobku

V tomto laboratóriu opravíme uzly na spodnom výčnelku v strede ozubeného kolesa, ako je znázornené na obr. STPL1.20. Takže vyberte možnosť Velocity, vyberte povrch, ako je znázornené na obr. STPL1.20., potom zvoľte prepínač smeru "* * Všetky * * " a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}), priradené BCC rýchlosti pre prevodový objekt je, ako je znázornené na obr. STPL1.20. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku Pohyb.

![]({{ '/assets/images/labs/shot_peening_labs/shot_peening_lab1/image0020.jpg' | relative_url }})

Priradená hraničná podmienka rýchlosti pre obrobok

#### Definovanie pohybu obrobku

Na stránke Pohyb definujte uhlovú rýchlosť ako * * 10 * * **ot/min.**. Definujte hodnotu stredu ako 0, 0, 0 a hodnotu osi ako 0, 0, 1, ako je znázornené na obr. STPL1.21. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po stranu trysky #1.

![]({{ '/assets/images/labs/shot_peening_labs/shot_peening_lab1/image0021.jpg' | relative_url }})

Stránka pohybu obrobku

### Definovanie trysky #1

#### Dýza#1 Definícia objektu

Pre dýzu môžeme definovať názov a jeho geometriu na stránke objektu dýzy. Na stránke objektu Tryska #1 ponecháme názov Tryska # 1. * * Priemer ** definujeme ako ** 5 mm * * a * * Kužeľ * *** uhol * * ako **20** stupňov, * * hmotnosť ** ** prietok ** ako **2,3 kg/min* * a * * vzduch * * ** tlak * * ako * *172 kpa**, ako je znázornené na obr. STPL1.22\. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku Umiestnenie.

![]({{ '/assets/images/labs/shot_peening_labs/shot_peening_lab1/image0022.jpg' | relative_url }})

Definované parametre trysky č.1 na stránke objektu

#### Definovanie umiestnenia dýzy

Definujte **referenciu**** súradnicu ** **X** ako **9.793** , **Y** ako **-12.395** a **Z** ako **1.86717**. Definujte **vzdialenosť** ako **37 mm** , **Theta** ako **61 stupňov** a **Phi** ako **308****stupňov** vzhľadom na referenčný bod, ako je znázornené na obr. STPL1.23. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku pohybu.

![]({{ '/assets/images/labs/shot_peening_labs/shot_peening_lab1/image0023.jpg' | relative_url }})

Určenie umiestnenia dýzy

#### Definovanie pohybu dýzy

Definujte dýzu **Rýchlosť** ako **1** *mm/s** a smer pohybu ako * * Z * *, ako je znázornené na obr. STPL1.24. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku Polohovanie.

![]({{ '/assets/images/labs/shot_peening_labs/shot_peening_lab1/image0024.jpg' | relative_url }})

Definovanie pohybu dýzy

VIZUÁL PRE

Na stránke positioning môžeme pomocou ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) umiestniť objekt. V tomto laboratóriu nemusíme používať polohovanie, pretože objekty obrobku a dýzy sú v správnej polohe.

## Analýza procesu kužeľového zpevňovania

Proces zpevňovania povrchu v 3D je možné analyzovať na základe vstupného napätia, parametrov procesu a geometrie objektov.

** Simulácia častíc ** : Počas simulácie častíc náhodne generované častice zasiahnu obrobok a vypočítajú priemery uhlov nárazu, počty zásahov, rýchlosti nárazu atď. na každom povrchovom prvku. Simulácia častíc je pomalšia ako simulácia Impact a zvláda odrazy.

** Simulácia nárazu ** : Počas simulácie nárazu vykonáva jednoduché priesečníky kužeľov s obrobkom a vypočítava uhly nárazu, počty zásahov, rýchlosti nárazu atď. pre každý povrchový prvok. Simulácia nárazu je rýchla a nezohľadňuje vplyvy odrazov. Nezohľadňuje ani čiastočné pokrytie povrchových prvkov.

** Analýza reziduálneho napätia ** : Nárazové napätia buď zo simulácie častíc alebo simulácie nárazu môžu byť priradené objektu na vykonanie analýzy reziduálneho napätia na predpovedanie reziduálneho napätia. Ak je vstup napätia iba z meraného reziduálneho napätia, analýza reziduálneho napätia sa nevyžaduje, merané reziduálne napätie bude interpolované nad 3D modelom na základe výstupu simulácie častíc alebo výstupu simulácie nárazu v závislosti od výberu používateľa.

### Simulácia častíc

#### Nastavenia simulácie častíc

Kliknite na položku „**Časticová *** *simulácia * * “ v strome objektov. V tomto laboratóriu definujeme % straty energie počas kolízie Shot-Workpiece ako 0,3. Nebudeme strieľať na streľbu z kolízie, preto začiarknite políčko Shot-shot collision. Časový krok definujeme ako 0,002, príliš veľký časový krok môže viesť k záberom prenikajúcim do obrobku.

Simuláciu môžeme spustiť buď s náhľadom alebo bez náhľadu, ak spustíme simuláciu s náhľadom, simulácia zaberie viac času, ale môžeme pozorovať pelety dopadajúce na obrobok a v prípade potreby môžeme upraviť parametre zastavením simulácie. Pre toto laboratórium spustíme simuláciu vypnutím začiarkavacieho políčka Spustiť s náhľadom. Kliknite na tlačidlo ![]({{ '/assets/icons/post_icons/mo_run_simulation_label_button.jpg' | relative_url }}), simulácia sa spustí a aktuálny čas procesu sa aktualizuje v konzole, ako je znázornené na obr. STPL1.25. Po dokončení simulácie častíc kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku s výsledkami.

![]({{ '/assets/images/labs/shot_peening_labs/shot_peening_lab1/image0025.jpg' | relative_url }})

Nastavenia simulácie častíc

#### Výsledok simulácie častíc

Z častíc sa získajú tieto výstupné parametre:

* Vertikálna (normálna k povrchovému prvku) rýchlosť.

Θ: uhol nárazu

* Počet zásahov.

* Hustota zásahu (počet zásahov vydelený plochou povrchového prvku).

Expozičná doba

Krytie.

Kliknite na položku „**Výsledok** “ v časti Simulácia častíc v strome objektov. Na stránke Výsledky simulácie častíc môžeme vykresliť obrys rôznych výstupov spolu s histogramami, ako je znázornené na obr. STPL1.26. Pod záložkou * * Stavová premenná * * môžeme vykresliť kontúry nárazového napätia, reziduálne napätia a namerané premenné stavu napätia.

![]({{ '/assets/images/labs/shot_peening_labs/shot_peening_lab1/image0026.jpg' | relative_url }})

Histogram vertikálnej rýchlosti spolu s obrysom zo simulácie častíc

![]({{ '/assets/images/labs/shot_peening_labs/shot_peening_lab1/image0027.jpg' | relative_url }})

Histogram nárazového napätia spolu s obrysom zo simulácie častíc

  
Animáciu simulácie častíc môžeme zobraziť kliknutím na tlačidlo ![]({{ '/assets/icons/post_icons/mo_show_animation_button.jpg' | relative_url }})action.

![]({{ '/assets/images/labs/shot_peening_labs/shot_peening_lab1/image0028.jpg' | relative_url }})

Stránka animácie simulácie častíc

Simulácia nárazu

#### Nastavenia simulácie vplyvu

Kliknite na položku „**Vplyv *** *simulácia * * “ v strome objektov. V tomto laboratóriu použijeme predvolený časový krok * * 0,0333 * * s. Môžeme ovládať zobrazenie dýzy, kužeľa dýzy a dráhy dýzy, ale zapnúť/ vypnúť príslušné začiarkavacie políčka. Kliknite na ![]({{ '/assets/icons/post_icons/mo_run_simulation_label_button.jpg' | relative_url }}) a sledujte simuláciu nárazu. V tomto laboratóriu vypneme všetky začiarkavacie políčka. Počas simulácie nárazu môžeme pozorovať nárazový kužeľ a cestu na displeji a stav v stavovom riadku, Určenie zásahov : čas na ľavej strane a celkové dokončenie v percentách na pravej strane. (Pozri obr. STPL1.29.). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) zobrazíte stránku s výsledkami simulácie nárazu

![]({{ '/assets/images/labs/shot_peening_labs/shot_peening_lab1/image0029.jpg' | relative_url }})

Nastavenia simulácie nárazu

#### Výsledok simulácie nárazu

Podobne ako na stránke s výsledkami simulácie častíc môžeme vykresliť obrys rôznych výsledkov hit spolu s histogramom, ako je znázornené na obr. STPL1.30. a obr. STPL1.31. V záložke Stav premennej môžeme vykresliť obrys nárazového napätia, zostatkového napätia a premenného výstupu stavu meraného napätia. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na analýzu zvyškového napätia

![]({{ '/assets/images/labs/shot_peening_labs/shot_peening_lab1/image0030.jpg' | relative_url }})

Histogram vertikálnej rýchlosti spolu s obrysom zo simulácie nárazu

![]({{ '/assets/images/labs/shot_peening_labs/shot_peening_lab1/image0031.jpg' | relative_url }})

Histogram nárazového napätia spolu s obrysom zo simulácie nárazu

### Analýza zvyškového stresu

#### Nastavenia analýzy zvyškového stresu

Na stránke analýzy reziduálneho napätia môžeme obrobku priradiť hodnoty počiatočného nárazového napätia buď zo simulácie častíc alebo simulácie nárazu. V tomto laboratóriu vyberieme prepínač ** Simulácia nárazu ** a klikneme na tlačidlo **Priradiť počiatočné napätie**. S "**MUMPS** " ako riešiteľom kliknite na ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) a potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) pre vygenerovanie databázy (pozri obr. STPL1.32.) Po vygenerovaní databázy kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku Spustiť.

![]({{ '/assets/images/labs/shot_peening_labs/shot_peening_lab1/image0032.jpg' | relative_url }})

Nastavenia analýzy zvyškového napätia

#### Simulácia analýzy zvyškového stresu

Kliknite na ![]({{ '/assets/icons/post_icons/run_label_button.jpg' | relative_url }}) pre spustenie jednorazovej simulácie napätia MKP (analýza zvyškového napätia). Po dokončení simulácie kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku Výsledky. Obr. STPL1.33. Zobrazuje koniec analýzy zvyškového napätia.

![]({{ '/assets/images/labs/shot_peening_labs/shot_peening_lab1/image0033.jpg' | relative_url }})

Analýza zvyškového napätia Spustiť stránku

#### Výsledky analýzy zvyškového stresu

Na stránke s výsledkami môžeme vykresliť obrysy pre vybraný výstup, obr. STPL1.34. Zobrazuje efektívny graf reziduálneho napätia.

**Reziduálne napätie (MKP)** – Vypočítané zo simulácie MKP na základe simulácie Impact/ Particle

**Reziduálne napätie (z mikro modelu)** – Reziduálne napätia z 2D mikro modelu sú interpolované do 3D modelu na základe simulácie Impact/ Particle

**Rázové napätie (z mikro modelu)** – Rázové napätia z 2D mikro modelu sú interpolované do 3D modelu na základe simulácie Impact/ Particle

**Namerané napätie** \- Zostatkové napätia z nameraných údajov poskytnutých používateľom sú interpolované do 3D modelu na základe simulácie nárazu/ častíc

![]({{ '/assets/images/labs/shot_peening_labs/shot_peening_lab1/image0034.jpg' | relative_url }})

Efektívny výstup napätia pre rôzne výstupy Mikromodel, Merané napätie a MKP

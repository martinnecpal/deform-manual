---
lang: sk
title: "Lab03 Kovanie hrotov"
---

# Laboratórna práca č. 3. Falšovanie signálov

  
3.1. Kovanie hrotov – presun z pece do foriem

3.2. Kovanie hrotov – zdržanie na spodnej matrici

3.3. Kovanie hrotu – 1. úder

3.4. Kovanie hrotov – výmena formy a úder 2

V štyroch operáciách sa bude modelovať kovanie za tepla. Keďže ide o proces za tepla, najpresnejšia simulácia bude modelovať nielen samotnú operáciu kovania, ale aj všetky prebiehajúce procesy prenosu tepla. Celý proces sa rozdelí nasledovne:

  * Simulácia prenosu tepla bude znázorňovať 10-sekundový presun sochory z pece do foriem. Ide výlučne o simuláciu prenosu tepla.

  * Operácia „Dwelling“ bude simulovať 2-sekundovú dobu odpočinku polotovaru na spodnej matrici pred kováním. Ide zároveň o simuláciu prenosu tepla.

  * Operácia tvárnenia bude simulovať prvý úder a vykoná výmenu formy pre druhý úder v rámci dvojúderového procesu kovania.

Ak chcete pre túto konfiguráciu vykonať analýzu napätia v matrici, pozrite si laboratórnu úlohu č. 2 v sprievodcovi analýzou napätia v matrici.

Keďže sochor a matrice sú osovo symetrické, proces by bolo možné modelovať v 2D. S cieľom hlbšie preskúmať symetriu a ďalšie dôležité 3D pojmy však bude proces modelovaný v 3D s využitím 1/4 symetrie pre sochor a matrice.

## Kovanie hrotov – presun z pece do foriem

Vytvorte nový problém buď výberom položky **Súbor** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému, ako je znázornené na obr. 3DL3.1. Vyberte prepínač „**Integrovaný výrobný proces**“ a v poli jednotiek vyberte prepínač „**Angličtina**“. Názov úlohy zadajte ako „**Spike_Forging**“ a uistite sa, že je zaškrtnuté políčko „**Zobraziť dialógové okno s možnosťami**“ (ak políčko „Zobraziť dialógové okno s možnosťami“ nezaškrtnete, nezobrazí sa dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), čím otvoríte nový problém s využitím integrovaného výrobného procesu Deform.

V tomto momente sa otvorí sprievodca MO a používateľ bude vyzvaný, aby zadal názov projektu (systém vytvorí samostatnú zložku s týmto názvom projektu) a názov tejto relácie. V tejto relácii použijeme ako názov projektu „**Spike_Forging**“. Používateľ môže tiež zmeniť systém jednotiek (v ponuke Súbor sa automaticky vyberie systém jednotiek, ktorý bol zvolený v ponuke Súbor) a pridať operáciu výberom z roletového zoznamu Prvá operácia a zaškrtnutím príslušného políčka. Pomocou možnosti Kopírovať existujúci projekt môžeme importovať predtým uložené projekty ako nové projekty. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otváraní operácie.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

Priradenie názvu problému

Otvorí sa sprievodca viacerými operáciami. Zoznamu operácií v prehliadači pridajte operáciu 3D Heat Transfer. Operáciu pridáte kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa položky **3D Heat Transfer** alebo ju môžete pridať aj pretiahnutím do editora operácií. (Pozri obr. 3DL3.2.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0002.jpg' | relative_url }})

Okno sprievodcu MO

### Nastavenie typu prenosu tepla

Keďže vykonávame prevod vzduchom, ako typ prenosu tepla vyberte **Prenos vzduchom**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Priradiť podmienku procesu

Nastavte **čas prenosu tepla** na **10** sekúnd a ostatné polia ponechajte bez zmeny. (Pozri obr. 3DL3.3.) Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Object“.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0003.jpg' | relative_url }})

Priradenie operácie prenosu – podmienka procesu

### Objekty

V tejto úvodnej simulácii prenosu tepla sa sochársky polotovar bude premiestňovať z pece do foriem. Pre túto operáciu sa do zoznamu štandardne pridá len jeden objekt; použite predvolený výber a (pozri obr. 3DL3.4.) kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0004.jpg' | relative_url }})

Okno „Objekty“

### Určenie teploty objektu

Na stránke „Workpiece“ nastavte **teplotu objektu** na hodnotu **2000** °F, ako je znázornené na obr. 3DL3.5. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0005.jpg' | relative_url }})

Určenie teploty obrobku

### Import geometrie

Na stránke „Geometria“ kliknite na možnosť „Importovať geometriu z knižnice“ (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})) a importujte súbor **Spike_Billet.STL** z adresára \3d\LABS v inštalačnej zložke programu DEFORM, ako je znázornené na obr. 3DL3.6. Na kontrolu geometrie použite akciu ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}). Ak je geometria v poriadku, mala by sa zobraziť správa znázornená na obr. 3DL3.7.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0006.jpg' | relative_url }})

Import geometrie

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0007.jpg' | relative_url }})

Vyskakovacie okno na kontrolu geometrie

### Určenie podmienok symetrie

Kliknite na možnosť ![]({{ '/assets/icons/pre_icons/mo_symmetry_planes_label.jpg' | relative_url }}), vyberte jednu z rovín symetrie obrobku a kliknutím definujte rovinnú symetriu, ako je znázornené na obr. 3DL3.8. Tento postup zopakujte pre druhú rovinu symetrie a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0008.jpg' | relative_url }})

Priradenie rovinná symetria k obrobku

### Vytvorenie siete na obrobku

Prepnite do režimu Expert kliknutím na ikonu ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) (Prepnúť do režimu Expert) na paneli nástrojov. Režim Expert ponúka viac možností pre podrobné nastavenia.

Na stránke „Mesh“ vyberte typ „Absolute“, nastavte **Min Element Size** na hodnotu **0,04** a tiež nastavte **Size****Ratio** na hodnotu **3**. Po zmene týchto nastavení kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}) otvoríte okno s predvolenými okrajovými podmienkami. (Pozri obr. 3DL3.9.) Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0009.jpg' | relative_url }})

Definovanie údajov o sieti

### Priradenie materiálu k obrobku

V okne „Materiál“ kliknite na tlačidlo „Načítať údaje o materiáli z knižnice“ ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) a načítajte materiál „**AISI-1025[1800-2200F(1000-1200C)]** “ z kategórie **Oceľ** kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}), ako je znázornené na obr. 3DL3.10. Z okna vyberte pridaný materiál a priraďte ho k obrobku, ako je znázornené na obr. 3DL3.11. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0010.jpg' | relative_url }})

Okno „Materiál“

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0011.jpg' | relative_url }})

Priradenie materiálu k obrobku

### Okrajové podmienky

Pre toto laboratórne cvičenie sú v danom nastavení pre obrobok postačujúce prednastavené okrajové podmienky (pozri obr. 3DL3.12.). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Step“.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0012.jpg' | relative_url }})

Okno „Okrajové podmienky“

### Nastavenie ovládacích prvkov krokov

V definícii kroku nastavte **Počet simulačných krokov** na **50**, **Krok****Prírastok** **na** **Uložiť** na hodnotu **5** a **Čas** definície kroku riešenia nastavte na **0,2** s (pozri obr. 3DL3.13.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0013.jpg' | relative_url }})

Okno Ovládacie prvky simulačných krokov

### Vytvoriť databázu

Po výbere možnosti **Export** v ponuke **Súbor** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) uložte súbor s kľúčovými slovami pre danú úlohu pod názvom „**Spike_Air_transfer**“.

Kliknite na popisok akcie ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby ste skontrolovali problém. Vytvorte databázu kliknutím na popisok akcie ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}).

### Spustenie simulácie

Po vytvorení databázy prejdite do režimu simulácie výberom tlačidla ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom objektov. Kliknite na názov akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) na karte Simulácia; otvorí sa dialógové okno Možnosti spustenia, ako je znázornené na obr. 3DL3.14. Použite predvolenú možnosť **Pokračovať v spúšťaní**, vyberte možnosť „**Pokračovať od posledného kroku**“, potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0014.jpg' | relative_url }})

Spustiť okno simulácie

Sledujte priebeh simulácie na kartách „Simulation Message“ a „Simulation Log“ a uistite sa, že je zaškrtnutá voľba ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}). (Pozri obr. 3DL3.15.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0015.jpg' | relative_url }})

Súbor so simulačnými správami

### Následné spracovanie

Po dokončení simulácie si výsledky prezrite tak, že prejdete do režimu Post pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) nad panelom nástrojov Simulácia.

Zobrazte premennú stavu teploty ![]({{ '/assets/icons/post_icons/mo_temp_sv.jpg' | relative_url }}). Okrem toho kliknite pravým tlačidlom myši na farebnú lištu v okne DISPLAY a ako typ farebnej lišty vyberte možnosť **Teplota**. Týmto spôsobom získate pri zobrazení teplôt intuitívnejšie farebné schéma.

Prejdite jednotlivými krokmi simulácie a sledujte, ako sa sochor ochladzuje pri preprave z pece do foriem. (Pozri obr. 3DL3.16.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0016.jpg' | relative_url }})

Okno postprocesora s grafom teploty

Teraz vyberte posledný krok v prehliadači krokov a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}), aby ste pokračovali v inštalácii.

## Kovanie hrotov – zdržanie na spodnej matrici

V predchádzajúcej operácii sa obrobok prenášal z pece do foriem. Akonáhle sa obrobok dostane do foriem, pred začatím kovania zostane 2 sekundy ležať na spodnej forme. Toto zdržanie sa v tejto operácii zohľadní. Zdržanie sa nastaví výberom typu nastavenia „Batch mode“ (Dávkový režim).

Pridajte operáciu „3D Heat Transfer“ zo zoznamu operácií v okne Explorer. Operáciu pridáte kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa položky „3D Heat Transfer“ alebo ju môžete pridať aj pomocou funkcie „drag and drop“ do editora operácií, ako je znázornené na obr. 3DL3.17.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0017.jpg' | relative_url }})

Sprievodca MO s dvoma operáciami

V editore operácií vyberte 2. operáciu, zobrazí sa rozbaľovacie okno „Setup type“ (Typ nastavenia) a kliknite na tlačidlo režimu ![]({{ '/assets/icons/pre_icons/mo_no_batch_setup_button.jpg' | relative_url }}) (keďže nastavujeme operáciu Dwell v dávkovom režime). Pozrite obr. 3DL3.18.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0018.jpg' | relative_url }})

Rozbaľovacie okno na výber typu nastavenia

Na stránke „Prenos tepla“ bude štandardne vybraný typ ohrevu **Rest on******Die**, ak nezvolíte typ prenosu tepla „Rest on Die“. Predchádzajúce nastavenia operácie sa prenesú do tejto operácie – pozri obr. 3DL3.19. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0019.jpg' | relative_url }})

Stránka na výber typu prenosu tepla

### Prevádzkové podmienky

Nastavte **Čas odpočinku** na **2** sekundy, keďže obrobok bude ležať na spodnej matrici 2 sekundy (pozri obr. 3DL3.20.). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Objekty“.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0020.jpg' | relative_url }})

Stránka „Režim odpočinku – Stav procesu“

###  Pridávanie objektov

Na stránke „Objekt“ sa štandardne pridajú 3 objekty. V závislosti od počtu objektov potrebných na simuláciu môže používateľ pridať toľko foriem, koľko je potrebné, kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}). V tomto laboratórnom cvičení použijeme 3 objekty (obrobok a 2 formy) (pozri obr. 3DL3.21.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0021.jpg' | relative_url }})

Okno „Objekty“

Keďže prechádzame z operácie prenosu tepla do operácie zadržiavania tepla, obrobok sa automaticky považuje za načítaný z databázového objektu. Keďže ide o objekt načítaný z databázy, všetky údaje, ako sú teplota, sieť a BCC objektu, sa prenesú z predchádzajúcej operácie (pozri obr. 3DL3.22.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Top die“ (Horná matrica).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0022.jpg' | relative_url }})

Objekt „Obrobok načítaný z databázy“

### Horná matrica

Na stránke „Top Die“ môže používateľ nastaviť požadovanú teplotu hornej formy. Pre toto laboratórne cvičenie je v poriadku predvolená teplota **300°F** (pozri obr. 3DL3.23.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0023.jpg' | relative_url }})

Okno s objektom „Top die“

#### Import geometrie

Na stránke Geometria kliknite na možnosť „Importovať geometriu z knižnice“ (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})) a importujte súbor **Spike_Topdie1.STL** z priečinka \3D\LABS v inštalačnom adresári programu DEFORM. Pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) skontrolujte geometriu. Kliknite na možnosť ![]({{ '/assets/icons/pre_icons/mo_symmetry_planes_label.jpg' | relative_url }}), definujte rovinnú symetriu a kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) (pozri obr. 3DL3.24.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0024.jpg' | relative_url }})

Priradená symetria v rovine hornej formy

#### Vytvoriť sieť

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) a v rozbaľovacom okne „Východisková okrajová podmienka“ vyberte možnosť „Áno“; vytvorí sa sieť s 28 000 prvkami.

#### Priradenie údajov o materiáli

V okne „Material“ kliknite na ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}), aby ste načítali údaje o materiáli z knižnice, a načítate materiál „**AISI-H-13**“ z kategórie **Die_material** kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}), ako je znázornené na obr. 3DL3.25. Z okna vyberte pridaný materiál a priraďte ho k hornej matrici, ako je znázornené na obr. 3DL3.26. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0025.jpg' | relative_url }})

Okno s materiálmi

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0026.jpg' | relative_url }})

Priradenie materiálu k hornej matrici

#### Nastavenie skrytých kópií (BCC)

Predvolená výmena tepla s okrajovými podmienkami prostredia pre hornú formu je v poriadku (pozri obr. 3DL3.27.), klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Spodná forma“.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0027.jpg' | relative_url }})

Priradené okrajové podmienky výmeny tepla pre hornú formu

### Spodná matrica

Pre toto laboratórne cvičenie je pre spodnú matricu v poriadku predvolená teplota 300 °F (pozri obr. 3DL3.28.), kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0028.jpg' | relative_url }})

Okienko spodnej matrice

#### Import geometrie

Na stránke „Geometria“ kliknite na možnosť „Importovať geometriu z knižnice“ (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})) a importujte súbor **Spike_BottomDie.STL** z adresára \3d\LABS v inštalačnej zložke programu DEFORM. Geometriu skontrolujte pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}). Kliknite na možnosť ![]({{ '/assets/icons/pre_icons/mo_symmetry_planes_label.jpg' | relative_url }}), definujte rovinnú symetriu a kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) (pozri obr. 3DL3.29). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0029.jpg' | relative_url }})

Stránka o symetrii spodnej matrice

#### Vytvoriť sieť

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}), v rozbaľovacom okne „Predvolená okrajová podmienka“ vyberte ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}); vytvorí sa sieť s 30 500 prvkami. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

#### Priradenie údajov o materiáli

Zoznamu materiálov vyberte materiál **AISI-H-13** a priraďte ho k spodnej matrici, ako je znázornené na obr. 3DL3.26. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

#### Nastavenie skrytých kópií (BCC)

Prednastavená výmena tepla s okrajovými podmienkami prostredia pre spodnú formu je v poriadku, pozri obr. 3DL3.30. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka s naplánovaným umiestnením.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0030.jpg' | relative_url }})

Zadané okrajové podmienky výmeny tepla pre spodnú formu

### Plánované polohovanie

Obrobok je potrebné umiestniť tak, aby spočíval na spodnej matrici. Keďže obrobok sa načítava z databázy typu DB, je potrebné ho umiestniť pomocou naplánovaného polohovania. Na naplánovanie polohy kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) a vyberte ![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}). Zmeňte objekt polohovania na **obrobok** a referenčný bod na **spodnú****matricu**. Vyberte smer priblíženia **-Z**, ako je znázornené na obr. 3DL3.31, a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Definované naplánované polohovanie sa zobrazí tak, ako je znázornené na obr. 3DL3.32, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0031.jpg' | relative_url }})

Okno na umiestňovanie objektov

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0032.jpg' | relative_url }})

Plánované časové okno na určovanie polohy

### Vzťahy medzi objektmi

Vyberte kontakt typu **užívateľ** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}). Tým sa pridá vzťah medzi obrobkom, hornou maticou a spodnou maticou, ako je znázornené na obr. 3DL3.33.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0033.jpg' | relative_url }})

Okno vzťahov medzi objektmi

Zvýraznite vzťah medzi spodnou matricou a obrobkom a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) tento vzťah upravte. V časti obrazovky venovanej treniu (pozri obr. 3DL3.34.) sa nachádza roletové menu, ktoré používateľovi umožňuje vybrať vhodné podmienky trenia pre procesy prenosu tepla. Na karte „Thermal“ (Tepelné vlastnosti) vyberte v zozname koeficient prenosu tepla typu **Free Resting**. Do poľa „Heat transfer coefficient“ (Koeficient prenosu tepla) sa vloží hodnota **0,0002**.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0034.jpg' | relative_url }})

Stránka „Inter Object Relation Thermal“

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) sa vrátite do okna „Inter-Object“, keďže typ nastavenia problému je „Batch mode“ (Dávkový režim) a pri generovaní databázy sa vytvoria kontakty. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Step“ (Krok).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0035.jpg' | relative_url }})

Okno vzťahov medzi objektmi

### Nastavenie ovládacích prvkov simulácie

V časti „Definícia kroku“ nastavte **počet krokov** na **10**, **krok prírastku** na **5** a **čas** **definície kroku riešenia** na **0,2 s** (pozri obr. 3DL3.36.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0036.jpg' | relative_url }})

Okno ovládacích prvkov krokov

### Vytvoriť databázu

Keď navštívime stránku „Generovať databázu“, objekty sa umiestnia podľa definovaných údajov o plánovanom umiestnení (pozri obr. 3DL3.37.).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0037.jpg' | relative_url }})

Vytvoriť databázu

Po výbere možnosti **Export** v ponuke **Súbor** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) uložte súbor kľúčových slov pod názvom „**Spike_Dwelling**“.

Kliknite na popisok akcie ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby ste skontrolovali problém. Vytvorte databázu kliknutím na popisok akcie ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}).

Po vytvorení databázy prejdite do režimu simulácie výberom tlačidla ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom objektov. Kliknite na označenie akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) na karte simulácie; otvorí sa dialógové okno „Run Options“ (Možnosti spustenia), ako je znázornené na obr. 3DL3.38. Pomocou predvolenej možnosti **Pokračovať v spúšťaní** vyberte možnosť „**Pokračovať od posledného kroku**“, potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0038.jpg' | relative_url }})

Vyskočiace okno „Spustiť simuláciu“

Sledujte priebeh simulácie na kartách „Simulation Message“ a „Simulation Log“ a uistite sa, že je zaškrtnutá voľba ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}).

### Následné spracovanie

Po ukončení simulácie kliknite na ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}). V prehliadači krokov kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_all_button.jpg' | relative_url }}), aby ste si zobraili všetky kroky. 

Ak chcete lepšie vidieť ochladzovanie obrobku na forme, vyberte obrobok v strome objektov a kliknite na ikonu režimu jedného objektu ![]({{ '/assets/icons/pre_icons/mo_show_single_obj_icon.jpg' | relative_url }}). V okne DISPLAY sa zobrazí iba obrobok. Vyberte stavovú premennú Teplota (![]({{ '/assets/icons/post_icons/mo_temp_sv.jpg' | relative_url }})), kliknite pravým tlačidlom myši na farebný pruh a ako typ farebného pruhu vyberte **Teplota**. (Pozri obr. 3DL3.39.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0039.jpg' | relative_url }})

Graf premennej teploty pre obrobok

Prejdite jednotlivými krokmi simulácie a sledujte teplotu obrobku. V kroku -51 sa poloha obrobku posunie nadol, kde sa oprel o spodnú formu. Všímajte si, ako sa spodná časť obrobku ochladzuje od kroku -51 po krok 60, kde je v kontakte s formou. Zapnite spodnú formu a sledujte rozloženie jej teploty. Pozorujte, ako sa forma zahrieva počas 2-sekundového zdržania. (Pozri obr. 3DL3.40.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0040.jpg' | relative_url }})

Graf premennej teploty pre spodnú formu

Teraz vyberte posledný krok v prehliadači krokov a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}), aby ste pokračovali v inštalácii.

## Kovanie hrotov – úder kováča 1

V predchádzajúcich operáciách prešiel obrobok presunom do pece a zdržaním na spodnej matrici. Posledný krok zdržania sa nahraje do režimu predspracovania a nastaví sa prvý kováčsky úder.

Pridajte operáciu 3D tvárnenia zo zoznamu operácií v Průzkumníku. Operáciu pridáte kliknutím na tlačidlo 3D tvárnenie ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) alebo ju môžete pridať aj pretiahnutím do editora operácií, ako je znázornené na obr. 3DL3.41. Vyberte operáciu Formovanie v editore operácií, zobrazí sa kontextové menu Typ nastavenia a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_no_batch_setup_button.jpg' | relative_url }}) v tomto menu. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí stránka objektov.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0041.jpg' | relative_url }})

Pridanie operácie tvarovania do editora operácií

### Pridať objekty

Štandardne sa zobrazia tri objekty z predchádzajúcej operácie. Ak tomu tak nie je, kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) pridajte tri objekty, ako je znázornené na obr. 3DL3.42. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0042.jpg' | relative_url }})

Pridávanie objektov

### Obrobok

Na stránke „Obrobok“ vyberte prepínač „**Načítať z databázy**“, ako je znázornené na obr. 3DL3.43. Keďže ide o objekt typu „Načítať z databázy“, všetky údaje tohto objektu sa prenesú do tejto operácie z predchádzajúcich operácií. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Horná matrica“.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0022.jpg' | relative_url }})

Výber obrobku na základe údajov z databázy

### Horná matrica

Na stránke „Top Die“ vyberte prepínač „**Čítať z databázy**“. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Movement“.

#### **Priradenie pohybu kocky**

****Na stránke „Pohyb“ nastavte **rýchlosť** **2** palce za sekundu v smere **-Z**, ako je znázornené na obr. 3DL3.44. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Spodná forma“.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0044.jpg' | relative_url }})

Okno na ovládanie pohybu

### Spodná matrica

Na stránke „Spodná matrica“ vyberte prepínač „**Načítať z databázy**“. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Naplánované polohovanie“.

### Plánované nastavenie polohy hornej matrice

Na stránke „Plánované polohovanie“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) a vyberte prepínač ![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}). Zmeňte „Polohovací objekt“ na **Horná matrica** a „Referenčný bod“ na **obrobok**. Zmeňte smer priblíženia na **-Z** a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) (pozri obr. 3DL3.45). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0045.jpg' | relative_url }})

Plánované časové okno na určovanie polohy

### Vzťahy medzi objektmi

V okne „Inter-Object“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}). Pridajú sa predvolené vzťahy, ako je znázornené na obr. 3DL3.46.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0046.jpg' | relative_url }})

Okno „Medzi objektmi“

Tepelné údaje je potrebné upraviť tak, aby sa namiesto koeficientu voľného odpočinku, ktorý sa používal v predchádzajúcej operácii, použil koeficient prenosu tepla pri tvárnení. V tejto laboratórnej úlohe sa automaticky pridá predvolený koeficient prenosu tepla pre tvárnenie za tepla, ktorý sa v nej používa.

Je potrebné definovať trenie medzi obrobkom a formami, keďže teraz bude dochádzať k deformácii. Zvýraznite prvý vzťah v tabuľke a kliknite na ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}). Na **kartu Deformácia****** použite roletové menu „Trenie“ a zo zoznamu vyberte položku **Tepelné kovanie (s mazaním)**, ako je znázornené na obr. 3DL3.47., potom kliknite na **kartu „Thermal“****** a z roletového menu vyberte položku **Forming** (pozri obr. 3DL3.48.), následne kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Späť v okne INTER-OBJECT kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}), aby ste zmenili nastavenia aj pre druhý vzťah.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0047.jpg' | relative_url }})

Okno definície deformácie údajov medzi objektmi

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0048.jpg' | relative_url }})

Okno s definíciou tepelnej charakteristiky medzi objektmi

Kontakt sa vytvorí počas generovania databázy. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až kým sa nezobrazí stránka „Step“.

### Priradenie ovládacích prvkov krokov

Nastavte **Počet simulačných krokov** na **30** a **Krok pre uloženie** na **5**. Zmeňte **Primárnu maticu** na **Hornú****maticu**, keďže sa pohybuje práve horná matica, a v časti Definícia krokov riešenia nastavte položku S **konštantným posunom matice** na hodnotu **0,025** ", ako je znázornené na obr. 3DL3.49. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0049.jpg' | relative_url }})

Okno „Ovládacie prvky simulačného kroku“

### Vytvorenie databázy

V ponuke **Súbor** vyberte položku **Exportovať** a uložte súbor s kľúčovými slovami pre túto úlohu pod názvom „**Spike_Forging_Blow1**“.

Kliknite na názov akcie ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby ste skontrolovali problém. Vytvorte databázu kliknutím na názov akcie ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}).

### Spúšťanie simulácií

Po vytvorení databázy prejdite do režimu simulácie kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom objektov. Kliknite na názov akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) na karte „Simulácia“; otvorí sa dialógové okno „Možnosti spustenia“, ako je znázornené na obr. 3DL3.38. Pomocou predvolenej možnosti **Pokračovať v spúšťaní** vyberte možnosť „**Pokračovať od posledného kroku**“, potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

Sledujte priebeh simulácie na kartách „Simulation Message“ a „Simulation Log“ a uistite sa, že je zaškrtnutá možnosť ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}).

Počas behu simulácie je možné zobraziť naposledy uložený krok. Na paneli nástrojov so stavovými premennými, ako je znázornené na obr. 3DL3.50, je možné zobraziť mnoho rôznych premenných, ako napríklad plastické deformácie, rýchlosť plastického deformovania, teplotu atď.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0050.jpg' | relative_url }})

Okno „Simulačná grafika“

### Následné spracovanie

Po dokončení simulácie kliknite na ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}). V prehliadači krokov kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_all_button.jpg' | relative_url }}), aby ste si zobraili všetky kroky.

Pozrite sa na **Teplotu** aj na **Efektívne****deformácie**, ako je znázornené na obr. 3DL3.51 a obr. 3DL3.52. V závislosti od prezeranej premennej môže používateľ prepínať medzi geometriou a sieťou na lisovacích formách. Pri zobrazení teploty je možné zobraziť sieť/teplotný gradient v maticiach kliknutím na tlačidlo Zobraziť sieť ![]({{ '/assets/icons/pre_icons/mo_show_mesh_icon.jpg' | relative_url }}) (a tiež kliknutím na tlačidlo Zobraziť geometriu ![]({{ '/assets/icons/pre_icons/mo_show_geo_icon.jpg' | relative_url }}), čím sa geometria skryje). Podobne pri zobrazení premennej, ako je efektívna deformácia, ktorú by mali len deformujúce sa objekty, by sa namiesto siete mali pravdepodobne zobraziť geometrie foriem.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0051.jpg' | relative_url }})

Graf premenných teplotného stavu

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0052.jpg' | relative_url }})

Graf premenných stavu pri efektívnom napätí

Veľkosť zaťaženia potrebného na deformáciu objektu je dôležitý výsledok, ktorý možno získať zo simulácie. Kliknite na ikonu ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}). Keď sa zobrazí okno GRAPH, vyberte iba položku Top Die, pričom os X je nastavená na **Stroke** a os Y na **Z-Load**. Kliknite na ![]({{ '/assets/icons/post_icons/mo_plot_button.jpg' | relative_url }}) a nad objektmi v okne DISPLAY sa zobrazí priehľadná krivka zaťaženia v závislosti od zdvihu, ako je znázornené na obr. 3DL3.53.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0053.jpg' | relative_url }})

Graf zaťaženia a zdvihu

V okne „Load Stroke Graph“ prejdite na kartu „Options“ a zaškrtnite políčko „Step tracer“, ako je znázornené na obr. 3DL3.54.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0054.jpg' | relative_url }})

Okno „Možnosti grafu zdvihu zaťaženia“

Tak, že keď sa vyberie iný krok, pruh v krivke zaťaženia a zdvihu tento krok zvýrazní a zaťaženie pre tento krok sa zobrazí v grafe. Okrem toho je možné myšou vybrať bod v grafe a zobrazený krok sa automaticky zmení na ten, ktorý zodpovedá danému bodu v grafe.

Teraz v prehliadači krokov vyberte posledný krok a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}), aby ste pokračovali v inštalácii.

## Kovanie hrotov – výmena formy a úder č. 2

Bol simulovaný prvý úder pri kovanie a teraz je čas modelovať druhý úder, pri ktorom sa používa iná horná matrica. Importuje sa geometria novej hornej matrice a nastaví sa druhý kováčsky úkon.

Pridajte operáciu 3D tvárnenia zo zoznamu operácií v Průzkumníku. Operáciu pridáte kliknutím na tlačidlo „3D Forming“ (![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }})) alebo ju môžete pridať aj pretiahnutím do editora operácií. V editore operácií vyberte operáciu „Forming“ (Tvarovanie), zobrazí sa rozbaľovacie okno „Setup type“ (Typ nastavenia) a v ňom kliknite na tlačidlo „NO – Batch mode“ (Nie – dávkový režim). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka s objektmi.

### Pridať objekty

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí stránka „Objekty“. Štandardne sa zobrazia tri objekty z predchádzajúcej operácie. Ak tomu tak nie je, kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) pridajte tri objekty, ako je znázornené na obr. 3DL3.42. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Obrobok

Na stránke „Obrobok“ vyberte prepínač „**Načítať z databázy**“. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Horná matrica“.

### Výmena hornej matrice pre Blow2

Je potrebné zmeniť geometriu aj sieť vrchného lisovacieho nástroja. Na stránke „Top Die“ zmeňte typ objektu na **rigid** a nastavte teplotu na **300** °F, potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

#### Importovať geometriu

Na stránke „Geometria“ kliknite na možnosť „Importovať geometriu z knižnice“ (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})) a importujte súbor **Spike_Topdie2.STL** z adresára \3d\LABS v inštalačnej zložke programu DEFORM. Pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) skontrolujte geometriu. Kliknite na možnosť ![]({{ '/assets/icons/pre_icons/mo_symmetry_planes_label.jpg' | relative_url }}), definujte rovinnú symetriu a kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) (pozri obr. 3DL3.55). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0055.jpg' | relative_url }})

Priradená rovinná symetria pre hornú formu

#### Vytvoriť sieť

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) a v rozbaľovacom okne „Predvolená okrajová podmienka“ vyberte ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}). Vytvorí sa sieť s predvoleným počtom prvkov.

#### Priradiť materiál

Z okna materiálov vyberte materiál „**AISI-H-13**“ a priraďte ho k hornej matrici. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

#### Nastavenie BCC

Na stránke BCC skontrolujte predvolene priradenú výmenu tepla s prostredím BCC pre hornú matricu a uistite sa, že táto predvolene priradená výmena tepla s prostredím BCC je priradená k celému vonkajšiemu povrchu hornej matrice s výnimkou symetrických rovín (pozri obr. 3DL3.56.).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0056.jpg' | relative_url }})

Priradenie výmeny tepla s prostredím BCC pre hornú matricu

#### Určenie pohybu kocky

Na stránke „Pohyb“ nastavte **rýchlosť** **2** palcov za sekundu v smere -Z. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Spodná matrica

Na stránke „Bottom Die“ vyberte prepínač „**Čítať z databázy**“. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Plánované nastavenie polohy hornej matrice

Na stránke „Plánované polohovanie“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) a vyberte voľbové tlačidlo ![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}). Zmeňte objekt polohovania na **Top****Die** a referenčný bod na **obrobok**. Zmeňte smer priblíženia na **-Z** a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). 

### Vzťahy medzi objektmi

V okne „Inter-Object“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}). Pridajú sa predvolené vzťahy, ako je znázornené na obr. 3DL3.47.

Je potrebné definovať trenie medzi obrobkom a lisovacími formami, keďže teraz bude dochádzať k deformácii. Okrem toho je potrebné upraviť tepelné údaje tak, aby sa namiesto koeficientu voľného odpočinku, ktorý sa používal v predchádzajúcej operácii, použil koeficient prenosu tepla pri tvárnení.

Zvýraznite prvý vzťah v tabuľke a kliknite na ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}). Na karte „Deformácia“ použite roletové menu „Trenie“ a zo zoznamu vyberte položku **Kovanie za tepla (s mazaním)**, ako je znázornené na obr. 3DL3.48. Následne kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Späť v okne INTER-OBJECT kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}), aby ste zmenili nastavenia aj pre druhý vzťah.

Pri vytváraní databázy dôjde k kontaktu medzi polotovarom a hornou aj spodnou matricou.

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku „Ovládacie prvky krokov“.

### Priradenie ovládacích prvkov krokov

Nastavte **Počet simulačných krokov** na **10** a **Krok na uloženie** na **5**. Zmeňte primárnu maticu na hornú maticu, keďže sa pohybuje práve horná matica, a v časti Definícia krokov riešenia nastavte **S konštantným posunom matice** na **0,025**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Vytvorenie databázy

Po výbere možnosti **Export**** v ponuke **Súbor**** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **Uložte súbor s kľúčovými slovami pre daný problém pod názvom „**Spike_Forging_Blow2**“.

Kliknite na názov akcie ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby ste skontrolovali problém. Vytvorte databázu kliknutím na názov akcie ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}).

Po vytvorení databázy prejdite do režimu simulácie výberom tlačidla ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom objektov. Kliknite na názov akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) na karte Simulácia; otvorí sa dialógové okno Možnosti spustenia. Pomocou predvolenej možnosti **Pokračovať v spustení** vyberte možnosť „**Pokračovať od posledného kroku**“, potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

Sledujte priebeh simulácie na kartách „Simulation Message“ a „Simulation Log“ a uistite sa, že je zaškrtnutá voľba ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}).

### Následné spracovanie

Po dokončení simulácie kliknite na ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}). V prehliadači krokov kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_all_button.jpg' | relative_url }}), aby ste zobraili všetky kroky.

Prejdite si jednotlivé kroky a venujte osobitnú pozornosť krokom týkajúcim sa druhého kováčskeho úderu (kroky 90 až 101). Pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_show_cotact_icon.jpg' | relative_url }}) si pozrite, ako sa v priebehu simulácie mení kontakt. Preskúmajte tiež správanie teploty, efektívneho deformácie a zaťaženia v závislosti od zdvihu.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0057.jpg' | relative_url }})

Okno zaťaženia a zdvihu s grafom efektívnej premennej deformačného stavu

---
lang: sk
title: "Lab02 Štvorcový prsteň"
---

# Lab2 – štvorcový prsteň

  
2.1. Úvod

2.2. Vytvorenie nového problému

2.3. Pridanie operácie

2.4. Pridávanie objektov

2.5. Obrobok

2.6. Horná matrica

2.7. Vzťahy medzi objektmi

2.8. Ovládacie prvky krokov

2.9. Vytvorenie databázy

2.10. Spustenie simulácie

2.11. Následné spracovanie

## Úvod

V simuláciách by sa mala vždy, keď je to možné, využiť symetria. Takýmto spôsobom sa šetrí výpočtový čas a môže sa zvýšiť presnosť riešenia. Okrem toho by sa mal modelovať čo najmenší úsek, ktorý problém primerane opisuje.

V tomto cvičení budeme simulovať deformáciu štvorcového prstena. Štvorcový prsten má pomerne veľkú symetriu, ktorú môžeme využiť. Toto cvičenie vám ukáže, že deformáciu celého prstena je možné určiť len na základe modelovania 1/16 jeho celkovej geometrie.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0001.jpg' | relative_url }})

Rozdelenie štvorcového prstena modelovaného na účely analýzy

## Vytvorenie nového problému

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte DEFORM-v1x.xxx (.xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte **DEFORM GUI Main** vxx.xx. Zobrazí sa hlavné okno DEFORM GUI Main, ako je znázornené nižšie na obr. 3DL2.2.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0001.jpg' | relative_url }})

Hlavné okno grafického rozhrania programu DEFORM

Vytvorte nový problém buď výberom položky **Súbor** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie úlohy, ako je znázornené na obr. 3DL2.3. Vyberte prepínač „**Integrovaný výrobný proces**“ a v poli jednotiek vyberte prepínač „**Angličtina**“. Názov úlohy zadajte ako „******Square_Ring**“ a uistite sa, že je zaškrtnuté políčko „**Zobraziť dialógové okno s možnosťami**“ (ak nezaškrtnete políčko „Zobraziť dialógové okno s možnosťami“, nezobrazí sa dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), čím otvoríte novú úlohu s použitím integrovaného výrobného procesu Deform.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

Okno na výber typu problému

Otvorí sa sprievodca viacerými operáciami s dialógovým oknom Nový projekt (pozri obr. 3DL2.4.), kde bude používateľ vyzvaný na zadanie názvu projektu (systém vytvorí samostatnú zložku s týmto názvom projektu) a názvu tejto relácie. V tejto relácii použijeme ako názov projektu „**Square_Ring**“.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0004.jpg' | relative_url }})

Okno výberu nového projektu

Používateľ môže tiež zmeniť systém jednotiek (v ponuke Súbor sa ako predvolený vyberie zvolený systém jednotiek) a pridať operáciu výberom z roletového zoznamu „Prvá operácia“ a zaškrtnutím príslušného políčka (pozri obr. 3DL2.5.). Pomocou možnosti „Kopírovať existujúci projekt“ môžeme importovať predtým uložené projekty ako nový projekt. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otváraní operácie.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0005.jpg' | relative_url }})

Priradenie názvu problému

Na simuláciu kovania tohto štvorcového prsteňa sú potrebné iba obrobok a horná forma – spodná forma nie je potrebná vzhľadom na symetriu.

## Pridanie operácie

Pridajte operáciu „3D Forming“ zo zoznamu operácií v Průzkumníku. Operáciu pridáte kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}), ktoré sa nachádza vedľa položky „3D Forming“, alebo ju môžete pridať aj pretiahnutím do editora operácií. (Pozri obr. 3DL2.6.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0006.jpg' | relative_url }})

Operácia Explorer

V tejto operácii nastavujeme jednoduchý izotermický režim, preto na stránke „Simulation control“ v záložke „Sim Mode“ **vypnite** zaškrtávacie políčko **„Heat transfer mode“**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

V okne Zoznam materiálov načítajte materiál „**AISI-1045, COLD**“ z knižnice materiálov DEFORM v kategórii **Oceľ** pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať údaje o materiáli z knižnice). To môžete urobiť tak, ako je znázornené na nižšie uvedenom obr. 3DL2.7, kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0007.jpg' | relative_url }})

Okno knižnice materiálov

## Pridávanie objektov

Ak tam ešte nie sú dva objekty, pridajte ich kliknutím na tlačidlo „Vložiť objekt“ ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}). Tieto dva objekty budú pomenované ako „Obrobok“ a „Horná matrica“. Ak sú tam tri objekty, odstráňte „Spodnú matricu“ tak, že ju vyberiete a kliknete na tlačidlo „Odstrániť vybraný objekt“ ![]({{ '/assets/icons/pre_icons/mo_delete_object_button.jpg' | relative_url }}) (pozri obr. 3DL2.8.), potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0008.jpg' | relative_url }})

Okno objektu

## Obrobok

V okne „Workpiece“ (Obrobok) zmeňte názov objektu na **Billet**, ako typ objektu vyberte **Plastic** a ako teplotu nastavte **68°F**, ako je znázornené na obr. 3DL2.9. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0009.jpg' | relative_url }})

Objekt z polotovaru – Okno

### Načítanie geometrie polotovaru

V okne Geometria načítajte súbor geometrie **SquareRing_Billet.STL** z knižnice pomocou možnosti (Načítať geometriu z knižnice) alebo ho môžete importovať aj pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu zo súboru), ako je znázornené na obr. 3DL2.10. Geometria sa nachádza v inštalačnej zložke DEFORM v adresári \3d\LABS. Geometriu skontrolujte pomocou možností ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/mo_show_geometry_normal_vectors_option.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0010.jpg' | relative_url }})

Okno „Geometria polotovaru“

V tejto simulácii sa využíva symetria a modeluje sa iba 1/16 štvorcového prstena. Pomocou možnosti „Planárna symetria“ definujte symetrické roviny, aby ste zabezpečili správnu deformáciu (pozri obr. 3DL2.11.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_symmetry_planes_label.jpg' | relative_url }}), v časti **Planárna symetria** vyberte symetrickú rovinu, ktorá je kolmá na os X (ako je znázornené nižšie na obr. 3DL2.12.). Vybraná polygónová plocha na rovine sa zvýrazní a informácie o rovine sa zobrazia v oblasti „Plane“ (Rovina).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0013.jpg' | relative_url }})

Rovina symetrie

Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) pridáte symetrické okrajové podmienky. Táto symetrická rovina sa teraz zobrazí v zozname „Planárna symetria“ ako (1, 0, 0), čo je normála k rovine X. (Pozri obr. 3DL2.12.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0028.jpg' | relative_url }})

Zadaná rovinná symetria voči rovine X

Vyššie uvedený postup zopakujte, aby ste pridali rovinnú symetriu pre ďalšie dve symetrické roviny. Najskôr vyberte symetrickú rovinu tak, aby sa vybraná rovina zvýraznila, a potom ich pridajte pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}). Keď sú pridané všetky tri roviny symetrie, oblasť rovinných symetrií by mala vyzerať tak, ako je znázornené na obr. 3DL2.13. Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) na stránke „Planar symmetry“ a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na vytvorenie siete.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0029.jpg' | relative_url }})

Priradené údaje o rovinnom symetrickom usporiadaní pre geometriu

### Vytvorenie siete na polotovare

V okne „Mesh“ zmeňte **Cieľový počet prvkov** na **8000** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_preview_mesh_button2.jpg' | relative_url }}). Vytvorená sieť povrchu vyzerá dobre. Kliknite teda na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}), aby ste dokončili proces vytvárania siete. (Pozri obr. 3DL2.14.) Po dokončení vytvárania siete by mal objekt obsahovať približne 5000 prvkov. Keď sa zobrazí otázka „Chcete priradiť predvolené okrajové podmienky?“, kliknite na ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku s materiálmi.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0011.jpg' | relative_url }})

Okno z liatinovej mriežky

### Priradenie materiálu k sochárskej surovine

Na priradenie materiálu k obrobku vyberte v okne materiálov materiál **AISI-1045 COLD**. Postupujte podľa obrázku 3DL2.15 nižšie. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Okrajové podmienky“.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0012.jpg' | relative_url }})

Okno „Materiál polotovaru“

### Nastavenie symetrických okrajových podmienok

Na stránke „Okrajové podmienky“ skontrolujte zadané údaje o rovine symetrie; oblasť „Okrajové podmienky“ by mala vyzerať tak, ako je znázornené na obr. 3DL2.16.

Keďže ide o izotermické nastavenie, odstráňte predvolene priradenú výmenu tepla s okolím typu BCC. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí okno s objektom hornej matrice.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0014.jpg' | relative_url }})

Okrajové podmienky symetrie

## Horná matrica

V okne „Top die object“ ponechajte typ objektu nastavený na **rigid** a teplotu na 68 °F, tiež sa uistite, že je zaškrtnuté políčko „primary die“, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). (Pozri obr. 3DL2.17.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0016.jpg' | relative_url }})

Okno s objektom „Top die“

### Načítanie geometrie hornej matrice

V okne Geometria načítajte geometrický súbor **SquareRing_TopDie.STL** z knižnice pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice). Geometria sa nachádza v inštalačnom priečinku DEFORM v adresári \3d\LABS. Skontrolujte geometriu pomocou možností ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/mo_show_geometry_normal_vectors_option.jpg' | relative_url }}), potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí okno „Pohyb“. Keďže ide o izotermický problém, nie je potrebné špecifikovať sieť ani súvisiace údaje.

### Priradenie pohybu k hornej kocku

Nastavte **rýchlosť** **1** palec za sekundu v smere **-Z**. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí okno „Contact“, keď sú obidve časti – surovec aj horná matrica – v správnej polohe. (Pozri obr. 3DL2.18.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0017.jpg' | relative_url }})

Okno „Pohyb hornej matrice“

## Vzťahy medzi objektmi

Vyberte prepínač typu **user** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}). Tým sa pridá vzťah medzi polotovarom a hornou matricou, ako je znázornené na obr. 3DL2.19.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0018.jpg' | relative_url }})

Okno „Medzi objektmi“

Trenie pre daný vzťah nastavte kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}). Z roletového menu vyberte trenie vhodné pre **tvarovanie za studena (oceľové formy)**. (Pozri obr. 3DL2.20.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0019.jpg' | relative_url }})

Okno definície údajov medzi objektmi

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) sa vrátite do okna Inter-Object, pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) určite vhodnú toleranciu kontaktu (vypočíta sa hodnota približne 0,00192") a potom kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_button.jpg' | relative_url }}) vytvorte kontakt. Ak objekty otočíte v grafickom okne, uvidíte, že medzi oboma objektmi bol vytvorený kontakt. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí okno „Step“, keďže nie sú potrebné žiadne ovládacie prvky na zastavenie.

## Ovládacie prvky krokov

V okne „Step controls“ (Ovládacie prvky krokov) prepnite režim nastavení predprocesora na „Expert“ pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) (Prejsť do režimu Expert) na paneli nástrojov. Režim Expert ponúka viac možností pre podrobné nastavenia. (Pozri obr. 3DL2.21.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0020.jpg' | relative_url }})

Ovládacie prvky krokov – karta „Hlavné“ v expertnom režime

Vyberte kartu „Kroky“ (![]({{ '/assets/icons/pre_icons/mo_simulation_step.jpg' | relative_url }})), nastavte **Počet simulačných krokov** na **30** a **Krok****Prírastok****na****Uložiť** na **2**. Nastavte **Hornú matricu** ako **Primárnu maticu**. (Pozri obr. 3DL2.22.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0021.jpg' | relative_url }})

Krok ovláda kartu „Simulačné kroky“ v expertnom režime

Na určenie vhodnej veľkosti kroku vyberte ikonu ![]({{ '/assets/icons/pre_icons/mo_measure_tool_icon.jpg' | relative_url }}) a zmerajte dĺžku hrany niekoľkých menších prvkov v polotovare. Priemerná dĺžka krátkej hrany je približne 0,06”. V záložke „Krok“ (![]({{ '/assets/icons/pre_icons/mo_step_increment.jpg' | relative_url }})) použite ako veľkosť kroku **konštantný posun matrice** **0,02** palca na krok, čo predstavuje 1/3 tejto dĺžky krátkej hrany. (Pozri obr. 3DL2.23.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0022.jpg' | relative_url }})

Ovládacie prvky simulácie – karta „Krok“ v expertnom režime

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a uložte súbor s kľúčovými slovami pre daný problém výberom možnosti Exportovať v ponuke Súbor.

## Vytvorenie databázy 

Kliknite na akčný štítok ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby ste skontrolovali problém. Jediné varovanie, ktoré by sa malo objaviť v okne konzoly, sa týka kompenzácie objemu – v rámci tohto cvičenia ho ignorujte. Vytvorte databázu kliknutím na akčný štítok ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}).

## Spustenie simulácie

Po vytvorení databázy prejdite do režimu simulácie kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom operácií.

Kliknite na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}), aby sa otvorilo dialógové okno „Run Options“ (Možnosti spustenia). Pomocou predvolenej možnosti **Continue Run** (Pokračovať v spúšťaní) vyberte možnosť „**Continue from the last step**“ (Pokračovať od posledného kroku), potom nastavte režim simulácie na **Interactive** (Interaktívny) a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

Priebeh simulácie môžete sledovať v okne „Simulačná grafika“ a na kartách „Simulačné správy“ a „Simulačný protokol“, pričom sa uistite, že je zaškrtnutá možnosť ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) (pozri). Pomocou možností na paneli nástrojov „Simulačná grafika“ môžete počas simulácie problému vykresľovať základné stavové premenné a kontakty objektov.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0023.jpg' | relative_url }})

Simulačný režim MO

## Následné spracovanie

Po dokončení simulácie si výsledky prezrite tak, že pomocou tlačidla nad panelom nástrojov „Simulácia“ prejdete do režimu „Post“. (Pozri obr. 3DL2.25.)

V skutočnosti ide o úplný štvorcový prstenec, preto by bolo užitočné mať možnosť zobraziť celý diel v postprocesore. Na vytvorenie celého objektu je potrebné malú časť s rozmerom 1/16 zrkadlovo otočiť okolo symetrických rovín. Kliknutím na ikonu ![]({{ '/assets/icons/post_icons/mo_3d_mirroring_icon.jpg' | relative_url }}) otvoríte okno 3D zrkadlenia. (Pozri obr. 3DL2.26.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0024.jpg' | relative_url }})

Režim MO Post

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0025.jpg' | relative_url }})

Okno 3D zrkadlenia

Kliknite myšou na roviny symetrie na polotovare. Pri každom kliknutí sa zobrazí zrkadlový obraz polotovaru. Postup opakujte, kým sa nezobrazí celý polotovar. Tento postup je znázornený nižšie. (Pozri obr. 3DL2.27.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0026.jpg' | relative_url }})

Definícia symetrie

Akonáhle sa kompletný diel zobrazí v okne „Graphics“, zatvorte okno „Symmetry definition“ kliknutím na tlačidlo „OK“. Prejdite jednotlivé kroky a sledujte, ako sa štvorcový prstenec deformuje pri stlačení. Vyskúšajte si zobrazenie rôznych stavových premenných, ako je napríklad efektívne deformácia. (Pozri obr. 3DL2.28.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0027.jpg' | relative_url }})

Efektívny výsledok deformácie

Po dokončení prezerania výsledkov simulácie použite ikonu ![]({{ '/assets/icons/pre_icons/mo_quit_icon.jpg' | relative_url }}) na návrat do hlavného okna grafického používateľského rozhrania.

**Súvisiace témy:**

[1\. Simulation Control]({{ '/docs/sk/pre_processor/9_simulation_controls/9_simulation_controls/' | relative_url }})

[2\. General]({{ '/docs/sk/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }})

[3\. Geometry]({{ '/docs/sk/pre_processor/12_geometry_modelling/12_3_3d_geometry_data_defining/' | relative_url }})

[4\. Movement]({{ '/docs/sk/pre_processor/15_movement_controls_definition/15_movement_controls_settings/' | relative_url }})

[5\. Mesh]({{ '/docs/sk/pre_processor/13_mesh_generation/13_mesh_generation/' | relative_url }})

[6\. Positioning]({{ '/docs/sk/pre_processor/16_object_properties/16_object_properties/' | relative_url }})

[7\. Inter-Object]({{ '/docs/sk/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/' | relative_url }})

[8\. Post - Processor]({{ '/docs/sk/post_processor/24_introduction_to_post_processor/24_introduction_to_post_processor/' | relative_url }})

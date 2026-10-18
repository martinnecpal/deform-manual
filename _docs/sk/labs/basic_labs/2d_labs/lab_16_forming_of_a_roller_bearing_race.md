---
lang: sk
title: "Laboratórna práca č. 16: Výroba oběžnice valivého ložiska z porézneho materiálu"
---

# Laboratórna práca č. 16: VÝROBA BEHÚNKU VALČEKOVÉHO LOŽISKA Z PORÉZNÉHO MATERIÁLU

V tomto laboratórnom cvičení budeme simulovať tvárnenie dráhy kužeľíkového ložiska, znázornenej nižšie, s použitím porézneho materiálu. Keďže tento diel je osovo symetrický, modelovať a simulovať budeme len jeho časť. Formy budú tuhé. Pre zjednodušenie bude kombinácia hornej formy a trnu modelovaná ako jeden objekt. 

16.1 Vytvorenie novej úlohy

16.2 Pridanie operácie

16.3. Výber typu geometrie

16.4. Ovládacie prvky simulácie

16.5. Vkladanie materiálu do obrobku

16.6. Pridávanie objektov

16.7. Obrobok

16.8. Horná matrica

16.9. Spodná matrica

16.10. Polohovanie objektov

16.11. Nastavenie vzťahov medzi objektmi

16.12. Definícia riadenia zastavenia

16.13. Definovanie ovládacích prvkov krokov pre formovanie

16.14. Vytvorenie databázy

16.15. Spustenie simulácie

16.16. Následné spracovanie výsledkov

## Vytvorenie nového problému

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte položku DEFORM-v1x.xxx (kde .xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte položku **DEFORM GUI Main** vxx.xx. Zobrazí sa hlavné okno DEFORM GUI Main, ako je znázornené na obrázku L16.1 nižšie.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image0001.jpg' | relative_url }})

Hlavné okno programu DEFORM GUI

Nový problém vytvoríte buď výberom položky **Súbor** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie úlohy, ako je znázornené na obr. L16.2. Vyberte prepínač „**Integrovaný výrobný proces**“ a ako systém jednotiek vyberte „**Angličtina**“. Názov úlohy zadajte ako „**Porous_Race**“, pozri obr. L16.2. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) otvoríte novú úlohu s využitím integrovaného výrobného procesu Deform.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image0002.jpg' | relative_url }})

Okno na výber typu problému

## Pridanie operácie

V sprievodcovi viacerých operácií pridajte operáciu **2D formovanie** zo zoznamu Explorer![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})Operations. Operáciu pridáte kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa operácie 2D Forming, alebo ju môžete pridať aj pretiahnutím do editora operácií. Po pridaní operácie 2D Forming sa štandardne otvorí okno nastavení procesu (pozri obr. L16.3.).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image0003.jpg' | relative_url }})

Pridať operáciu 2D tvarovania

## Výber typu geometrie

V tomto laboratórnom cvičení používame osovo symetrické geometrie, preto v položke „Typ geometrie“ vyberte tlačidlo **2D osovo symetrické** (obr. L16.4.) a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image0004.jpg' | relative_url }})

Výber typu geometrie

## Ovládacie prvky simulácie

V tomto cvičení vám ukážeme, ako nastaviť jednoduchú izotermickú úlohu. V okne „Simulation controls“ teda **zrušte zaškrtnutie** políčka **Heat****transfer** (pozri obr. L16.5.) a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image0005.jpg' | relative_url }})

Okno riadenia simulácie

## Načítavanie materiálu pre obrobok

V okne so zoznamom materiálov načítajte materiál „**AISI-4340 [1550–2200 F]**“ z knižnice materiálov DEFORM v kategórii **Oceľ** pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať údaje o materiáli z knižnice). Postupujte podľa obr. L16.6. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Objekt.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image0006.jpg' | relative_url }})

Okno knižnice materiálov

## Pridávanie objektov

Na túto operáciu potrebujeme tri objekty. Ak tam ešte nie sú tri objekty, pridajte ich kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}). Tieto tri objekty budú pomenované ako „Obrobok“, „Horná matrica“ a „Spodná matrica“ (pozri obr. L16.7.), potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image0007.jpg' | relative_url }})

Okno na pridávanie objektov

## Obrobok

V okne „Workpiece“ (Obrobok) zmeňte názov objektu na **Race**, nastavte teplotu na **2000** F a ako typ objektu vyberte „Porous (Plastic)“ (Pórovitý (plast)), ako je znázornené na obr. L16.8. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image0008.jpg' | relative_url }})

Objekt „Billet“ – Okno

### Načítavanie geometrie polotovaru

V okne Geometria načítajte súbor geometrie **PM_pre.igs** z knižnice pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice) alebo ho môžete importovať z inštalačnej zložky DEFORM do adresára \2D\LABS pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Načítať geometriu zo súboru), ako je znázornené na obr. L16.9.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image0009.jpg' | relative_url }})

Okno „Geometria pretekov“

### Vytvorenie siete obrobku

Nastavte počet prvkov na **1000** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}), aby sa vygenerovala sieť pre objekt Race (pozri obr. L16.10.). V expertnom režime (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})) je k dispozícii kompletná škála možností vytvárania sietí, ak potrebujete mať väčšiu kontrolu nad generovanou sieťou. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image00010.jpg' | relative_url }})

Stránka s mriežkou

### Priradiť materiál obrobku

Ak chcete priradiť materiál pre Race, vyberte materiál „**AISI****-4340**“ z okna materiálov. Postupujte podľa obrázku L16.11. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image00011.jpg' | relative_url }})

Stránka s materiálmi

### Inicializácia hustoty obrobku

Na stránke „Inicializácia“ kliknite na kartu „**Major**“ a nastavte hodnotu **Hustota** na „**0,9**“, ako je znázornené na obr. L16.12. Následne kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}), aby sa táto hodnota inicializovala pre celý obrobok. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pokračovali.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image00012.jpg' | relative_url }})

Inicializovať stránku

## Horná matrica

Na stránke „Top Die“ (pozri obr. L16.13.) vyberte ako typ objektu **Rigid** a zaškrtnite **políčko „Primary die check“**, keďže hornej matrici bude priradená definícia pohybu, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image00029.jpg' | relative_url }})

Inicializovať stránku

### Načítavanie geometrie hornej matrice

V okne Geometria načítajte geometrický súbor **PM_top.igs** z knižnice pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice) alebo ho môžete importovať aj pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Načítať geometriu zo súboru) z inštalačnej zložky programu DEFORM \2D\Labs, ako je znázornené na obr. L16.14. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Top Die movement.

  
![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image00013.jpg' | relative_url }})

Stránka Geometria lisovacej matice

### Priradiť pohyb k hornej kocku

Na stránke „Top Die Movement“ nastavte pre toto laboratórne cvičenie **rýchlosť** na hodnotu **7** in/sec v smere **-Y** (pozri obr. L16.15.). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Bottom Die“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image00014.jpg' | relative_url }})

Hlavná stránka „Pohyb matrice“

## Spodná matrica

Na stránke „Spodná forma“ vyberte typ objektu **Pevný** a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) (pozri obr. L16.16.).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image00015.jpg' | relative_url }})

Stránka spodnej matrice

### Načítanie geometrie spodnej matrice

V okne Geometria načítajte geometrický súbor **PM_btm.igs** z knižnice pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice) alebo ho môžete importovať pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Načítať geometriu zo súboru) z inštalačného priečinka DEFORM v adresári \2D\Labs. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Positioning“ (Polohovanie).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image00016.jpg' | relative_url }})

Stránka o geometrii spodnej matrice

## Umiestňovanie objektov

Najskôr posunieme hornú a dolnú formu ďalej od dráhy, aby sme mohli obe formy – hornú aj dolnú – správne umiestniť vo vzťahu k objektu „Race“.

Na to najprv kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}). Vyberte hornú maticu, zvoľte metódu „**Offset**“ a nastavte vektor vzdialenosti na (x=0, y=2). Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}), aby ste posunuli hornú matricu ďalej od dráhy. (pozri obr. L16.18.) Podobne vyberte spodnú matricu, použite metódu „**Offset**“ a vektor vzdialenosti (x=0, y=-2) a posuňte spodnú matricu ďalej od dráhy.

Pomocou polohovania s kolíziou v smere **-Y** umiestnime hornú formu nad dráhu. Vyberte metódu „**Interferencia**“, ako „Polohovaný objekt“ zvoľte „**Horná matrica**“ a ako referenčný objekt zvoľte „**Dráha**“, ako je znázornené na obr. L16.19. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) umiestnite hornú matricu. Podobným spôsobom umiestnite „spodnú matricu“ pomocou metódy interferenčného polohovania v smere +Y. Po umiestnení by malo nastavenie vyzerať tak, ako je znázornené na obr. L16.20. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Kontakt“.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image00017.jpg' | relative_url }})

Polohovanie objektov s posunom

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image00018.jpg' | relative_url }})

Polohovanie rušivého objektu

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image00019.jpg' | relative_url }})

Po umiestnení predmetov

## Naplánovať vzťahy medzi objektmi

Na stránke „Kontakt“ vyberte typ kontaktu „Používateľ“ a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}). Tým sa pridá vzťah medzi ložiskom, hornou maticou a spodnou maticou (pozri obr. L16.21.). Keďže matice sú tuhé a ložisko je z plastu, horná a spodná matica sa považujú za „Master“ a polotovar za „Slave“.

Zvýraznite vzťah „Top **Die – Race**“ a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) upravte podmienky kontaktu. V časti obrazovky venovanej treniu (pozri obr. L16.21.) sa nachádza roletové menu, ktoré používateľovi umožňuje vybrať vhodné podmienky trenia pre bežné tvárniace procesy.

Keďže ide o simuláciu tvárnenia za tepla a formy sú z ocele, použite rozbaľovacie menu a zo zoznamu vyberte možnosť **Tvárnenie za tepla (s mazáním)**. Hodnota trenia **0,3** sa nastaví automaticky.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image00020.jpg' | relative_url }})

Okno na zadanie koeficientu trenia medzi objektmi

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) sa vrátite na stránku Kontakt, keďže podmienky trenia sú rovnaké pre všetky páry objektov, pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) môžete skopírovať vlastnosti rozhrania z prvého vzťahu do všetkých ostatných. Po vykonaní tejto operácie budú mať všetky vzťahy trenie 0,3, definované tak, ako je znázornené na obr. L16.22. Zaškrtnite políčka Initialize a Generate, aby sa kontakt inicializoval a vygeneroval počas generovania databázy. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste definovali ovládacie prvky zastavenia.

  
![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image00021.jpg' | relative_url }})

Definícia vzťahu medzi objektmi pre formovaciu operáciu

## Definícia riadenia zastavenia

V okne riadenia zastavenia zaškrtnite políčko „Max. zdvih matrice“ a nastavte **primárny posun matrice** na (0,**0,915**), ako je znázornené na obr. L16.23. Pokročilé možnosti zastavenia sú k dispozícii v režime Expert (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste definovali krokové ovládacie prvky.

  
![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image00022.jpg' | relative_url }})

Ovládanie zastavenia zdvihu matice

## Definovanie ovládacích prvkov krokov pre formovanie

V okne nastavení krokov nastavte **Počet krokov** na **100** a **0,0092** ” ako **Posun matrice na krok** , Prírastok kroku na uloženie nastavte na **5**, horná matrica vybraná ako primárna matrica na stránke objektu sa zobrazí ako primárna matrica na stránke krokov, ako je znázornené na obr. L16.24.

  
![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image00023.jpg' | relative_url }})

Nastavenia ovládacích prvkov krokov

## Vytvorenie databázy 

Na stránke „Generate DB“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby program skontroloval, či v nastavení úlohy niečo nechýba. Počas kontroly červené správy označujú údaje, ktoré je potrebné opraviť pred spustením simulácie (napríklad ak ste zabudli definovať údaje o materiáloch).  
  
Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste vytvorili databázu. Akonáhle program dokončí zapisovanie databázy, prepnite do režimu simulácie kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom operácií.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image00024.jpg' | relative_url }})

Vytvoriť stránku databázy

## Spustenie simulácie

Kliknite na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) na karte „Simulácia“ (pozri obr. L16.26). Otvorí sa dialógové okno „Možnosti spustenia“, ako je znázornené na obr. L16.27. Použite predvolenú možnosť **Pokračovať v spustení** → „**Pokračovať****od posledného kroku**“ a vyberte prepínač **Interaktívne**, aby ste simuláciu spustili v interaktívnom režime. Kliknite na tlačidlo na spustenie simulácie.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image00025.jpg' | relative_url }})

Možnosti simulácie

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image00026.jpg' | relative_url }})

Okno „Spustiť simuláciu“

## Následné spracovanie výsledkov

Po dokončení simulácie prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}), kde si môžete prezrieť výsledky; otvorí sa postprocesor MO. (Pozri obr. L16.28.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image00027.jpg' | relative_url }})

Okno postprocesora MO

**Stavová premenná**

Kliknite na tlačidlo ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) a z ponuky „Deformácia stavových premenných“ vyberte položku **Hustota**, potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). Obr. L16.29 znázorňuje rozloženie hustoty v kanáli Race v poslednom kroku deformácie.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image00028.jpg' | relative_url }})

Premenná stavu „Hustota pozemkov“

**Súvisiace témy:**

[12.1. 2D Geometry Data Defining ]({{ '/docs/sk/pre_processor/12_geometry_modelling/12_1_2d_geometry_data_defining/' | relative_url }})

[12.2. 2D Geometry Data Editing]({{ '/docs/sk/pre_processor/12_geometry_modelling/12_2_2d_geometry_editing/' | relative_url }})

[13.1. 2D Mesh Generation]({{ '/docs/sk/pre_processor/13_mesh_generation/13_1_2d_mesh_generation/' | relative_url }})

[14\. Boundary Conditions]({{ '/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/' | relative_url }})

[15\. Movement Controls Settings]({{ '/docs/sk/pre_processor/15_movement_controls_definition/15_movement_controls_settings/' | relative_url }})

[17\. Object Data Initialize]({{ '/docs/sk/pre_processor/17_object_data_initialization/17_object_data_initialize/' | relative_url }})

[19\. Object Positioning]({{ '/docs/sk/pre_processor/19_object_positioning/19_object_positioning/' | relative_url }})

[20\. Inter-Object Data Definition]({{ '/docs/sk/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/' | relative_url }})

[9\. Simulation Controls]({{ '/docs/sk/pre_processor/9_simulation_controls/9_simulation_controls/' | relative_url }})

[6.3. Integrated Manufacturing Process Post-processor layout]({{ '/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_3_integrated_manufacturing_process_post_layout/' | relative_url }})

[25\. Post Processor Layout]({{ '/docs/sk/post_processor/25_post_processor_layout/25_post_processor_layout/' | relative_url }})

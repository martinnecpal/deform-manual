---
lang: sk
title: "Laboratórium na kreslenie 2D nábojníc"
---

# Laboratórium kreslenia 2D nábojníc

**Zhrnutie problému:**

V tomto laboratórnom cvičení si ukážeme, ako pomocou používateľského rozhrania integrovaného výrobného procesu (MO) nastaviť viaceré fázy tvárniaceho procesu v dávkovom režime. Nastavíme viacstupňový proces extrudovania s cieľom simulovať tvárnenie nábojníc pomocou operácie [2D]Forming v používateľskom rozhraní integrovaného výrobného procesu. Proces zahŕňa tri fázy extrudovania s medzilehlým žíhaním medzi jednotlivými fázami na zmiernenie napätia. 

Všetky tri stanice nastavíme naraz v dávkovom režime; obrobok bude prenášaný do všetkých operácií počas výmeny foriem na stanici 2 a stanici 3. V tomto laboratórnom cvičení budeme simulovať iba proces tvárnenia, nie proces žíhania; namiesto toho inicializujeme deformáciu, poškodenie a rýchlosť obrobku v po sebe nasledujúcich operáciách tvárnenia. Polohovanie foriem sa vykoná pomocou plánovaného polohovania tak, aby sa objekty umiestnili počas generovania databázy. Generovanie kontaktov sa tiež naplánuje tak, aby sa kontakty medzi objektmi vytvorili počas generovania databázy.

[1\. Creating New Problem and Adding Operations]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#1_Creating_New_problem_and_Adding_Operations)

[1.1. Creating New Problem]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#1_1_Creating_a_New_problem)

[1.2. Adding operations to Operation Editor]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#1_2_Adding_operations_to_Operation_Editor)

[2\. Setting up Station 1]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#2_Setting_up_Station1)

[2.1. Select Geometry Type and Simulation Controls]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#2_1_Select_Geometry_Type_and_Simulation_modes)

[2.2. Material List]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#2_2_Material_List)

[2.3. Objects]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#2_3_Objects)

[2.4. Workpiece]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#2_4_Workpiece)

[2.5. Punch]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#2_5_Punch)

[2.6. Die]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#2_6_Die)

[2.7. Ejector]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#2_7_Ejector)

[2.8. Defining Scheduled positioning]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#2_8_Defining_Scheduled_positioning)

[2.9. Defining contact conditions]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#2_9_Defining_contact_conditions)

[2.10. Stopping controls]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#2_10_Stopping_controls)

[2.11. Step Controls]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#2_11_Step_Controls)

[2.12. Generating Database]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#2_12_Generating_Database)

[3\. Setting up Station 2]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#3_Setting_up_Station2)

[3.1. Select Geometry Type and Simulation modes]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#3_1_Select_Geometry_Type_and_Simulation_modes)

[3.2. Workpiece]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#3_2_Workpiece)

[3.3. Punch]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#3_3_Punch)

[3.4. Die]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#3_4_Die)

[3.5. Ejector]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#3_5_Ejector)

[3.6. Scheduled Positioning]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#3_6_Scheduled_Positioning)

[3.7. Defining Contact conditions and scheduling contact generation for Station2]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#3_7_Defining_Contact_conditions_and_scheduling_contact_generation_for_Station2)

[3.8.Stopping controls for Station2]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#3_8_Stopping_controls_for_Station2)

[3.9. Step Controls for Station2]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#3_9_Step_Controls_for_Station2)

[4\. Setting up Station3]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#4_Station3)

[4.1. Select Geometry Type and Simulation modes]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#4_1_Select_Geometry_Type_and_Simulation_modes)

[4.2. Workpiece]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#4_2_Workpiece)

[4.3. Punch]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#4_3_Punch)

[4.4 Die]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#4_4_Die)

[4.5. Ejector]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#4_5_Ejector)

[4.6. Scheduled Positioning]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#4_6_Scheduled_Positioning)

[4.7. Defining Contact Conditions and scheduling contact generation for Station3]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#4_7_Defining_Contact_conditions_and_scheduling_contact_generation_for_Station3)

[4.8. Stopping controls for Station3]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#4_8_Stopping_controls_for_Station3)

[4.9. Step Controls for Station3]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#4_9_Step_Controls_for_Station3)

[5\. Running Simulation]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#5_Running_Simulation)

[6\. Post Processing]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#6_Post_Processing)

## Vytvorenie nového problému a pridanie operácií

### Vytvorenie nového problému

Na **počítači so systémom Windows** stlačte tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte položku DEFORM-v1x.xxx (kde .xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte položku **DEFORM GUI Main** vxx.xx. Zobrazí sa hlavné okno programu DEFORM GUI Main.

Vytvorte nový problém buď výberom položky **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému. Zvoľte rádio tlačidlo „**Integrovaný výrobný proces**“ a ako systém jednotiek zvoľte „**Angličtina**“ pomocou rádio tlačidla. Názov úlohy zadajte ako „**Cartridge_Case_Lab**“ a uistite sa, že je zaškrtnuté políčko „**Zobraziť dialógové okno s možnosťami**“ (ak nezaškrtnete políčko „**Zobraziť dialógové okno s možnosťami**“, v používateľskom rozhraní MO sa nezobrazí dialógové okno Nový projekt). Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) zatvoríte dialógové okno Nový problém a otvoríte projekt v používateľskom rozhraní Integrovaný výrobný proces.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image001.jpg' | relative_url }})

Dialógové okno „Nový problém“

### Pridávanie operácií do editora operácií

Sprievodca viacerými operáciami otvorí nový projekt. Pridajte tri 2D tvárniace operácie zo zoznamu v Průzkumníku operácií kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image002.jpg' | relative_url }})

Pridávanie operácií

## Nastavenie stanice 1:

Vyberte prvú formovaciu operáciu a zmeňte jej názov na „**Station1**“ dvojitým kliknutím na názov operácie v okne Editor operácií a stlačte klávesu Enter na klávesnici.

### Výber typu geometrie a režimov simulácie

V okne typu geometrie vyberte voľbu **2D osovo symetrická**, ako je znázornené na obrázku [Fig. 2DCCDL1.3.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig_2DCCDL1_3_Geometry_type_selection), a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Nastavenia simulácie. Na stránke Ovládacie prvky simulácie zrušte zaškrtnutie políčka Režim prenosu tepla, ako je znázornené na obrázku [Fig. 2DCCDL1.4.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig_2DCCDL1_4_Simulation_controls_page), a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image003.jpg' | relative_url }})

Výber typu geometrie

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image004.jpg' | relative_url }})

Stránka s ovládacími prvkami simulácie

### Zoznam materiálov 

Po nastavení typu geometrie a simulačných režimov načítajú materiály potrebné pre túto konfiguráciu. Pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) na stránke Zoznam materiálov importujte „**C26000, Mosadz na náboje, 70 %, žíhaná [70F(20C)]**“ z priečinka /2D/LABS/Cartridge_Lab, pozri [Fig. 2DCCDL1.5.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig_2DCCDL1_5_Material_List). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Objekt.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image005.jpg' | relative_url }})

Zoznam materiálov

### Objekty

Na modelovanie tohto nastavenia potrebujeme štyri objekty: obrobok, razník a vyhadzovač. V predvolenom nastavení sú do zoznamu objektov pridané tri objekty; ďalší pridáme kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}). Objekty budú v priebehu nastavovania primerane premenované. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku „Obrobok“.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image006.jpg' | relative_url }})

Stránka so zoznamom objektov

### Obrobok

#### Definícia typu objektu obrobku

Nechajte predvolený názov objektu „**Obrobok**“, typ objektu **Plast** a jeho teplotu **68** °F, ako je znázornené v [Fig. 2DCCDL1.7.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig_2DCCDL1_7_Workpiece_object_page). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Geometria, kde môžete definovať geometriu obrobku.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image007.jpg' | relative_url }})

Stránka objektu obrobku

#### Definovanie geometrie obrobku

Geometriu obrobku definujeme pomocou základných tvarov. Na stránke „Geometria obrobku“ kliknite na ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}), vyberte možnosť „Plný valec“ a nastavte **priemer** na hodnotu **0,82** " a **Výšku** ako **0,125** ", pozri [Fig. 2DCCDL1.8.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig_2DCCDL1_8_Defining_Workpiece_geometry). Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) v okne „Základné tvary“, aby ste okno zatvorili, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli na stránku „Sieť obrobku“.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image008.jpg' | relative_url }})

Definovanie geometrie obrobku

#### Vytvorenie siete pre obrobok

Na stránke „Mesh“ kliknite na ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}), aby ste prešli do expertného režimu, v ktorom budete mať prístup k rôznym možnostiam ovládania siete. Nastavte **cieľový počet prvkov** na **1000**, **hrúbku** **prvkov** na **4** a **Pomer veľkostí****** na **3**, kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) na vytvorenie siete pre obrobok, pozri [Fig. 2DCCDL1.9.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig_2DCCDL1_9_Mesh_settings_for_Workpiece). Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Materiál.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image009.jpg' | relative_url }})

Nastavenia siete pre obrobok

####  Priradenie materiálu k obrobku

V okne materiálov vyberte „**C26000, Mosadz na kazety, 70 %, žíhaná [70 °F (20 °C)]**“ v okne materiálov, aby ste priradili materiál k obrobku, pozri [Fig. 2DCCDL1.10.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig_2DCCDL1_10_Assigning_material_to_Workpiece). Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Okrajové podmienky obrobku.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image010.jpg' | relative_url }})

Priradenie materiálu k obrobku

#### Okrajové podmienky pre obrobok

Pri predvolenom osovo-symetrickom nastavení bude rýchlosť v smere osi x pevne stanovená pre všetky uzly pozdĺž tejto osi; to isté môžeme pozorovať na stránke BCC pre obrobok, pozri [Fig. 2DCCDL1.11.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig_2DCCDL1_11_Velocity_BCC_for_Workpiece). Nepotrebujeme žiadne ďalšie nastavenia BCC, preto kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku Vlastnosti obrobku.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image011.jpg' | relative_url }})

Rýchlosť BCC pre obrobok

#### Nastavenie hodnoty medznej rýchlosti deformácie pre obrobok

Na stránke „Vlastnosti obrobku“ upravíme hodnotu ****medznej** **rýchlosti** **deformácie** z **Rýchlosť deformácie** na **0,001**, aby sme presnejšie zachytili deformácie pri nižších rýchlostiach deformácie, pozri [Fig. 2DCCDL1.12.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig_2DCCDL1_12_Setting_Limiting_strain_rate_value_for_Workpiece). Keďže pre obrobok nemusíme definovať nič ďalšie, budeme klikať na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nedostaneme na stránku objektu Horná matrica, alebo vyberieme položku Dierovač zo stromu operácií.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image012.jpg' | relative_url }})

Nastavenie hodnoty medznej rýchlosti deformácie pre obrobok.

### Punch

#### Definícia typu objektu „Punch“

Zmeňte názov objektu na „**Punch**“, typ objektu ponechajte ako **Rigid** a teplotu ako **68** °F. Uistite sa, že je zaškrtnuté políčko **Primary die**, pretože ide o pohybujúci sa objekt a na tento objekt sa budú uplatňovať ovládacie prvky krokovania a zastavenia, pozrite si stránku [Fig. 2DCCDL1.13.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig_2DCCDL1_13_Punch_object_definition) Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre vyrazenie geometrie.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image013.jpg' | relative_url }})

Definícia objektu „Punch“

#### Definícia geometrie razníka

Geometriu pre nástroj Punch načítajeme zo súboru uloženého v adresári \2D\LABS\Cartridge_Lab. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Načítať geometriu zo súboru) a importujte súbor „**Punch.geo**“ vyhľadaním cesty k súboru s geometriou v inštalačnom priečinku DEFORM /2D/LABS/Cartridge_Lab, pozri [Fig. 2DCCDL1.14.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig_2DCCDL1_14_Loading_Punch_geometry). Skontrolujte geometriu pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}), aby ste sa uistili, že je v poriadku. Importovaná geometria by nemala mať žiadne problémy. Po definovaní geometrie pre Punch použijeme tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na prechod na stránku Movement. Pre Punch nebudeme generovať sieť, pretože typ objektu je Rigid a nemáme v úmysle vypočítať rozloženie teploty.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image014.jpg' | relative_url }})

Načítavanie geometrie razníka

#### Definovanie pohybu pre úder

Predvolený režim pohybu vŕtačky je „Konštantná rýchlosť“. Zadajte hodnotu **10** in/sec do poľa „Constant“ a overte, či je smer nastavený na **-Y**, pozri [Fig. 2DCCDL1.15.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig_2DCCDL1_15_Movement_controls_for_Punch). Keďže pre Punch nemusíme definovať nič ďalšie, budeme klikať na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým nedosiahneme objekt „Bottom Die“.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image015.jpg' | relative_url }})

Ovládanie pohybu v hre Punch

### Zomrieť

#### Definícia typu objektu „Die“

Zmeňte názov objektu na „**Die**“, typ objektu ponechajte ako **Rigid** a teplotu ako **68** °F, pozri [Fig. 2DCCDL1.16.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig_2DCCDL1_16_Die_Object_page). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Geometria Die.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image016.jpg' | relative_url }})

Stránka objektu „Die“

#### Geometria lisovacej formy

V prípade geometrie formy naimportujeme súbor „**Die.geo**“ tak, že vyhľadáme cestu k súboru s geometriou nachádzajúcu sa v inštalačnej zložke programu DEFORM \2D\LABS\Cartridge_Lab pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Načítať geometriu zo súboru) na stránke Geometria, pozri [Fig. 2DCCDL1.17.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig_2DCCDL1_17_Loading_Die_geometry). Skontrolujte geometriu pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}), aby ste sa uistili, že je v poriadku. Pre matricu nemusíme definovať sieť ani ovládacie prvky pohybu, pretože matrica je tuhý objekt, je nehybná a nevypočítavame rozloženie teploty na matrici; budeme klikať na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nedostaneme na stránku „Object 4“.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image017.jpg' | relative_url }})

Načítavanie geometrie lisovacej formy

### Vyhadzovač

#### Definícia typu objektu „Ejector“

Zmeňte názov objektu z „Object 4“ na „**Ejector**“, typ objektu ponechajte ako **Rigid** a teplotu ako **68** °F; pozrite si [Fig. 2DCCDL1.18.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig_2DCCDL1_18_Ejector_object_page). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Ejector Geometry“.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image018.jpg' | relative_url }})

Stránka objektu „Ejector“

#### Definovanie geometrie vyhadzovača

Na načítanie geometrie vyhadzovača importujeme súbor „**Ejector.geo**“ tak, že vyhľadáme cestu k súboru s geometriou nachádzajúcu sa v inštalačnej zložke DEFORM v adresári \2D\LABS\Cartridge_Lab pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Načítať geometriu zo súboru) na stránke Geometria, pozri [Fig. 2DCCDL1.19.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig_2DCCDL1_19_Loading_Ejector_geometry). Skontrolujte geometriu pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}), aby ste sa uistili, že je v poriadku. Pre Ejector nemusíme definovať sieť ani ovládacie prvky pohybu, keďže Ejector je tuhý objekt, ktorý je nehybný a nevypočítavame rozloženie teploty na Ejectore; budeme klikať na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nedostaneme na stránku Naplánované polohovanie.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image019.jpg' | relative_url }})

Načítavanie geometrie vyhadzovača

### Definícia plánovaného umiestnenia

Budeme používať funkciu „Plánované polohovanie“, aby sa objekty automaticky umiestnili na základe postupnosti polohovania definovanej na stránke „Plánované polohovanie“ ešte pred vytvorením databázy na stránke „Vytvorenie databázy“. Ak chcete naplánovať polohu pre objekty Station1, kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}), aby ste pridali položku polohovania, a vyberte ![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}). Zmeňte objekt polohovania na **Obrobok** a referenčný objekt na **Formu**, vyberte smer priblíženia **-Y**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) a uvidíte, že sa pridáva krok polohovania na základe našej definície na stránke Naplánované polohovanie. 

Podobne nastavte polohu razníka nad obrobkom kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) a vyberte ![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}), zmeňte polohovací objekt na **razník**, referenčný objekt na **obrobok** a vyberte smer priblíženia **-Y**. Môžeme si prezrieť naplánovanú sekvenciu polohovania, ako je znázornené na obrázku [Fig. 2DCCDL1.20.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig_2DCCDL1_20_Scheduled_positioning_definition_for_Station). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Kontakt“, kde môžete definovať podmienky kontaktu.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image020.jpg' | relative_url }})

Definícia plánovaného polohovania pre stanicu 1

### Stanovenie podmienok kontaktu

Keďže na umiestňovanie objektov používame funkciu „Schedule positioning“, musíme naplánovať generovanie kontaktov tak, aby sa kontakty medzi objektmi mohli generovať na základe umiestnenia definovaného v tejto funkcii. Zaškrtnite políčka Inicializovať a Generovať, aby sa inicializovali kontakty a následne vygenerovali nové kontakty na základe definovaných kontaktných vzťahov, pozri obr. 2DCCDL1.21\. Priraďte predvolené vzťahy medzi objektmi pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}). Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) pre jeden z vzťahov. Otvorí sa okno „Inter-object data“ (Dáta medzi objektmi), na karte „Deformation“ (Deformácia) vyberte prepínač typu trenia **Hybrid** a pre Coulomb aj Shear nastavte hodnotu **0,1**. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte okno „Inter-object data“. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}), aby ste uplatnili rovnaké podmienky trenia, ktoré ste definovali pre vybraný vzťah, na všetky ostatné vzťahy v zozname, pozrite [Fig. 2DCCDL1.21.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig_2DCCDL1_21_Defining_contact_conditions). Keďže kontakty budú generované počas generovania databázy, klikneme na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby sme prešli na stránku Ovládacie prvky zastavenia a definovali ovládacie prvky zastavenia.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image021.jpg' | relative_url }})

Definovanie podmienok kontaktu

### Ovládacie prvky na zastavenie

Nastavíme kontrolné body zastavenia tak, aby sa simulácia zastavila v okamihu, keď obrobok prekročí rovinu. Na stránke „Kontrolné body zastavenia“ kliknite na kartu **Zastavenie****rovina**, zaškrtnite políčko „Definované“ a nastavte počiatok na (**0,-0,1**) a vektor na (**0,****-1**), pozri [Fig. 2DCCDL1.22.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig_2DCCDL1_22_Defining_Stopping_controls_for_Station1). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli na stránku „Krok“ a definovali ovládacie prvky krokov simulácie.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image022.jpg' | relative_url }})

Nastavenie ovládacích prvkov zastavenia pre stanicu 1

### Ovládacie prvky krokov

Na stránke „Step“ nastavíme parametre na riadenie krokov simulácie. Nastavte **počet krokov** simulácie na hodnotu **10000**, **Krok prírastku na uloženie** krokov do databázy nastavte na **10** a **Posun matrice na krok** na **0,001**, pozri [ Fig. 2DCCDL1.23.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig_2DCCDL1_23_Simulation_step_controls_for_Station1). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre generovanie stránky databázy.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image023.jpg' | relative_url }})

Ovládacie prvky simulačných krokov pre stanicu 1

### Vytvorenie databázy

Na stránke „Vytvoriť databázu“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}). Systém kontroly údajov potvrdí, či zadané údaje sú vhodné na spustenie simulácie. Červené značky označujú chýbajúce alebo nesprávne údaje, ktoré zabránia spusteniu simulácie. Pred vytvorením databázy je potrebné tieto chyby opraviť.

  
Žlté značky označujú údaje, ktoré môžu byť pochybné a mali by sa skontrolovať. Tieto údaje je potrebné dôkladne preveriť, pretože môžu viesť k nestabilite systému alebo k chybným (nesprávnym) výsledkom.  
  
Preverte si informácie o kontrole údajov. Ak sa nezobrazujú žiadne žlté ani červené značky, kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}).  
Na karte Správa by ste mali hľadať text: „Databáza bola vytvorená“. Keď sa tento text zobrazí, znamená to, že vaše údaje boli uložené do databázy.

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}), aby ste pokračovali v nastavení „Station2“.

## Nastavenie Station2:

Zmeňte názov operácie na „**Station2**“ pre druhú operáciu tvárnenia na karte „Editor operácií“, rovnako ako v prípade prvej operácie – dvojitým kliknutím na názov operácie a po úprave názvu stlačením klávesy Enter. 

Keď prejdeme na stanicu 2, všetky objekty zo stanice 1 sa presunú na stanicu 2 ako objekty načítané z databázy. Na stanici 2 zmeníme geometriu matrice, razníka a vyhadzovača a nastavenia deformácie, poškodenia a rýchlosti obrobku na hodnotu 0, keďže obrobok medzi jednotlivými operáciami tvárnenia prejde relaxáciou deformácie.

### Výber typu geometrie a režimov simulácie

Nechajte zaškrtnuté tlačidlo **2D Axisymmetric** ako typ geometrie a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli na stránku „Simulation controls“. Na stránke Ovládacie prvky simulácie zrušte zaškrtnutie políčka Režim prenosu tepla, ako je znázornené na obrázku [Fig. 2DCCDL1.3.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig_2DCCDL1_3_Geometry_type_selection) v stanici 1, a klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa dostanete na stránku Obrobok, pretože pre túto operáciu nepotrebujeme do zoznamu objektov pridávať žiadne ďalšie objekty.

### Obrobok 

#### Definícia typu objektu obrobku

Môžeme si všimnúť, že typ objektu „Obrobok“ je nastavený na „Načítané z databázy“; údaje objektu „Obrobok“ sa načítajú z posledného kroku predchádzajúcej operácie. Necháme nastavenie „Obrobok“ ako „Načítané z databázy“ (pozri [Fig. 2DCCDL1.24.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig_2DCCDL1_24_Workpiece_object_page)). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí stránka „Vlastnosti obrobku“, pretože nebudeme pre obrobok nanovo definovať sieť ani bcc.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image024.jpg' | relative_url }})

Stránka objektu obrobku

#### Nastavenie hodnoty medznej rýchlosti deformácie pre obrobok

Zmeníme hodnotu „Limiting Strain rate“, aby sme zohľadnili nižšie rýchlosti deformácie v obrobku. Zaškrtneme **políčko Redefine Strain rate** a nastavíme **Limiting** na hodnotu „**0,001**“, pozri stránku [Fig. 2DCCDL1.25.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig_2DCCDL1_25_Redefining_Limiting_Strain_rate_for_Workpiece) Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Initialize, kde inicializujeme podmienky obrobku.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image025.jpg' | relative_url }})

Nové vymedzenie medznej rýchlosti deformácie pre obrobok

#### Inicializácia podmienok obrobku

Na stránke „Initialize“ zapnite políčka **Strain**, **Poškodenie** a **Rýchlosť** a nastavte hodnotu na „**0**“, aby sme mohli zohľadniť relaxáciu deformácie obrobku, pozri [Fig. 2DCCDL1.26.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig_2DCCDL1_26_Initializing_Workpiece_conditions_in_Station2). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa dostanete na stránku objektu „Punch“.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image026.jpg' | relative_url }})

Inicializácia podmienok obrobku v stanici 2

### Punch

#### Definícia typu objektu „Punch“

Musíme zmeniť geometriu výrezu pre Station2, a preto zmeniť typ objektu z „Read from DB“ na **Rigid**; pozri [Fig. 2DCCDL1.27.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig_2DCCDL1_27_Punch_object_page). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Punch Geometry“.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image027.jpg' | relative_url }})

Stránka objektu „Punch“

#### Zmena geometrie razníka

Na stránke „Punch Geometry“ (Geometria výseku) načítajte súbor „**Punch2.geo**“ tak, že vyhľadáte cestu k súboru s geometriou nachádzajúcu sa v inštalačnej zložke programu DEFORM v adresári \2D\LABS\Cartridge_Lab, pozri [Fig. 2DCCDL1.28.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig_2DCCDL1_28_Punch_geometry_in_Station2). Skontrolujte geometriu pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}), aby ste sa uistili, že je v poriadku. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nedostanete na stránku „Punch movement“.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image028.jpg' | relative_url }})

Geometria dier v programe Station2

#### Priradenie pohybu k úderu v Station2

Predvoleným režimom je konštantná rýchlosť. Do poľa „Constant“ zadajte hodnotu **10** in/sec a overte, či je smer nastavený na -Y. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka objektu „Die“.

### Zomrieť

#### Definícia typu objektu „Die“

Musíme zmeniť geometriu formy pre Station2, a preto zmeniť typ objektu z „Read from DB“ na **Rigid**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli na stránku „Die Geometry“.

#### Zmena geometrie lisovacej formy

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Načítať geometriu zo súboru) a importujte súbor „**Die2.geo**“ tak, že vyhľadáte cestu k súboru s geometriou nachádzajúcu sa v inštalačnej zložke programu DEFORM \2D\LABS\Cartridge_Lab, pozri [Fig. 2DCCDL1.29.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig_2DCCDL1_29_Die_geometry_for_Station2). Skontrolujte geometriu pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}), aby ste sa uistili, že je v poriadku. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka objektu Ejector.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image029.jpg' | relative_url }})

Geometria matrice pre Station2

### Vyhadzovač

#### Definícia typu objektu „Ejector“

Musíme zmeniť geometriu vyhadzovača pre Station2, a preto zmeniť typ objektu z „Read from DB“ na **Rigid**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli na stránku „Ejector Geometry“.

#### Zmena geometrie vyhadzovača

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Načítať geometriu zo súboru) a importujte súbor „**Ejector2.geo**“ tak, že vyhľadáte cestu k súboru s geometriou nachádzajúcu sa v inštalačnom priečinku DEFORM \2D\LABS\Cartridge_Lab, pozri [Fig. 2DCCDL1.30.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig_2DCCDL1_30_Ejector_geometry_for_Station2). Skontrolujte geometriu pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}), aby ste sa uistili, že je v poriadku. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Naplánované polohovanie.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image030.jpg' | relative_url }})

Geometria vyhadzovača pre Station2

### Plánované polohovanie

V súčasnosti nemáme k dispozícii výstup geometrie obrobku zo simulácie stanice 1, ktorý by slúžil na umiestnenie foriem, keďže simulácia stanice 1 ešte nebola vykonaná. Preto použijeme metódu umiestňovania podľa plánu, ktorá umiestni formy počas generovania databázy pre stanicu 2 s ohľadom na geometriu obrobku získanú zo stanice 1; typ objektu obrobku je „Načítané z databázy“. 

Ak chcete naplánovať polohu pre objekty Station2, kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}), aby ste pridali polohovaciu položku, a vyberte ![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}). Zmeňte objekt polohovania na **Obrobok** a referenčný objekt na **Formu**, ako smer priblíženia vyberte **-Y.** Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) môžeme pozorovať, že sa pridáva polohovací krok na základe našej definície na stránke Naplánované polohovanie. Podobne umiestnite razník nad obrobok kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) a výberom ![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}), zmeňte objekt polohovania na **razník**, referenčný objekt na **obrobok** a vyberte smer priblíženia **-Y**. Môžeme vidieť naplánovanú sekvenciu polohovania, ako je znázornené v [Fig. 2DCCDL1.31.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig_2DCCDL1_31_Scheduled_positioning_definition_for_Station2). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli na stránku „Kontakt“ a definovali podmienky kontaktu.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image031.jpg' | relative_url }})

Definícia plánovaného polohovania pre stanicu 2

### Definovanie podmienok kontaktu a naplánovanie vytvorenia kontaktov pre Station2

Musíme naplánovať generovanie vzťahov tak, aby sa vzťahy medzi objektmi mohli generovať na základe polohy definovanej v položke „Plánovanie polohy“. Zaškrtnite políčka Inicializovať a Generovať, aby sa inicializovali kontakty a následne sa vygenerovali nové kontakty na základe definovaných kontaktných vzťahov, pozri [Fig. 2DCCDL1.32.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig_2DCCDl1_32_Defining_contact_conditions_for_Stage_2). Priraďte predvolené vzťahy medzi objektmi pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}). Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) pre jeden z vzťahov. Na karte Deformácia vyberte prepínač **Hybridný typ** trenia a v okne Medziobjektové údaje nastavte hodnotu **0,1** pre položky **Coulomb** aj **Šmyk**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), aby ste opustili okno **Medziobjektové údaje**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}), aby ste uplatnili rovnaké podmienky trenia definované pre vybraný vzťah na všetky ostatné vzťahy v zozname, pozri [Fig. 2DCCDL1.32.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig_2DCCDl1_32_Defining_contact_conditions_for_Stage_2). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli na stránku **Ovládacie prvky zastavenia** a definovali ovládacie prvky zastavenia.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image032.jpg' | relative_url }})

Stanovenie podmienok kontaktu pre 2. fázu

### Ovládacie prvky na zastavenie pre Stanicu 2

Na stránke „Ovládacie prvky zastavenia“ definujeme rovinu zastavenia ako kritérium zastavenia. Kliknite na kartu **Rovina zastavenia**, zaškrtnite políčko „Definované“ a nastavte počiatok na (**0**, **-0,1**) a vektor na (**0**, **-1**), pozri [Fig. 2DCCDL1.33.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig2DCCDL1_33_Stopping_plane_stopping_criteria_for_Station2). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli na stránku „Step“ (Krok) a definovali ovládacie prvky simulačných krokov.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image033.jpg' | relative_url }})

Kritériá zastavenia lietadla pre stanicu 2

### Ovládacie prvky krokov pre stanicu 2

Na stránke „Kroky“ nastavte **Počet krokov** na hodnotu **10000**, **Krok pre uloženie** do databázy na hodnotu **10** a **Posun matrice na krok** na hodnotu **0,001**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránke „Generovať databázu“. Keďže databáza sa vygeneruje počas behu programu po dokončení simulácie stanice 1 v rámci nastavenia dávkového režimu, klikneme na ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}), aby sme nastavili stanicu 3.

## Stanica 3

Zmeňte názov operácie na „**Station3**“ pre tretiu operáciu tvarovania na karte „Editor operácií“, tak ako ste to urobili pri nastavení predchádzajúcich operácií – dvojitým kliknutím na názov operácie a stlačením klávesy Enter po úprave názvu operácie. 

Podobne ako v prípade stanice 2 aj pre stanicu 3 zmeníme geometriu matrice, razníka a vyhadzovača a nastavíme deformáciu, poškodenie a rýchlosť obrobku na hodnotu 0, keďže obrobok bude medzi jednotlivými operáciami tvárnenia podliehať relaxácii deformácie.

### Výber typu geometrie a režimov simulácie

Nechajte zaškrtnuté tlačidlo **2D Axisymmetric** ako typ geometrie a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli na stránku „Simulation controls“. Na stránke Ovládacie prvky simulácie zrušte zaškrtnutie políčka Režim prenosu tepla, ako je znázornené na obr. 2DCCDL1.4\. v Station1, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa dostanete na stránku Obrobok, pretože pre túto operáciu nepotrebujeme do zoznamu Objektov pridávať žiadne ďalšie objekty.

### Obrobok 

#### Definícia typu objektu obrobku

Môžeme si všimnúť, že typ objektu „Workpiece“ je nastavený na „Read from DB“; údaje objektu „Workpiece“ sa načítajú z posledného kroku predchádzajúcej operácie. Typ objektu „Workpiece“ ponecháme nastavený na „Read from DB“. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Workpiece Properties“.

#### Nastavenie hodnoty medznej rýchlosti deformácie pre obrobok

Zaškrtneme políčko **Predefinovať** **rýchlosť deformácie** a nastavíme **Obmedzenie** na hodnotu „**0,001**“; pozri stránku [Fig. 2DCCDL1.34.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig_2DCCDL1_34_Redefining_Limiting_Strain_rate_for_Workpiece). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na inicializáciu podmienok obrobku inicializujeme podmienky obrobku.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image034.jpg' | relative_url }})

Nové vymedzenie medznej rýchlosti deformácie pre obrobok

#### Inicializácia podmienok obrobku

Na stránke „Initialize“ zaškrtnite políčka „Strain“, „Damage“ a „Velocity“ a nastavte hodnotu na „**0**“, aby sme mohli zohľadniť relaxáciu deformácie obrobku; pozri [Fig. 2DCCDL1.35.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig_2DCCDL1_35_Initializing_Workpiece_conditions_in_Station3). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Punch object“.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image035.jpg' | relative_url }})

Inicializácia podmienok obrobku v stanici 3

### Punch

#### Definícia typu objektu „Punch“

Musíme zmeniť geometriu výrezu pre Station3, a preto zmeniť typ objektu z „Read from DB“ na **Rigid**; pozri [Fig. 2DCCDL1.36.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig_2DCCDL1_36_Punch_object_page_Station3). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli na stránku „Punch Geometry“.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image036.jpg' | relative_url }})

Stránka objektu Punch – Stanica 3

#### Zmena geometrie razníka

Na stránke „Punch Geometry“ (Geometria dierovacieho nástroja) načítajte súbor „**Punch3.geo**“ tak, že vyhľadáte cestu k súboru s geometriou nachádzajúcu sa v inštalačnej zložke programu DEFORM v adresári \2D\LABS\Cartridge_Lab, pozri [Fig. 2DCCDL1.37.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig_2DCCDL1_37_Punch_geometry_for_Station3). Skontrolujte geometriu pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}), aby ste sa uistili, že je v poriadku. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nedostanete na stránku „Punch movement“.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image037.jpg' | relative_url }})

Geometria razníka pre Station3

#### Priradenie pohybu k úderu v Station2

Predvoleným režimom je konštantná rýchlosť. Do poľa „Constant“ zadajte hodnotu **10** in/sec a overte, či je v poli „Direction“ nastavená hodnota **-Y**. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka objektu „Die“.

### Zomrieť

#### Definícia typu objektu „Die“

Musíme zmeniť geometriu formy pre **Station3**, a preto zmeniť typ objektu z „Read from DB“ na **Rigid**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli na stránku „Die Geometry“.

#### Zmena geometrie lisovacej formy

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Načítať geometriu zo súboru) a importujte súbor „**Die3.geo**“ tak, že vyhľadáte cestu k súboru s geometriou nachádzajúcu sa v inštalačnej zložke DEFORM v adresári \2D\LABS\Cartridge_Lab, pozri obr. 2DCCDL1.38\. Skontrolujte geometriu pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}), aby ste sa uistili, že je v poriadku. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka objektu Ejector.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image038.jpg' | relative_url }})

Geometria matrice pre Station3

### Vyhadzovač

#### Definícia typu objektu „Ejector“

Musíme zmeniť geometriu vyhadzovača pre Station3, a preto zmeniť typ objektu z „Read from DB“ na **Rigid**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli na stránku „Ejector Geometry“.

#### Zmena geometrie vyhadzovača

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Načítať geometriu zo súboru) a importujte súbor „**Ejector3.geo**“ tak, že vyhľadáte cestu k súboru s geometriou nachádzajúcu sa v inštalačnej zložke programu DEFORM v adresári \2D\LABS\Cartridge_Lab, pozri [Fig. 2DCCDL1.39.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig_2DCCDL1_39_Ejector_geometry_for_Station3). Skontrolujte geometriu pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}), aby ste sa uistili, že je v poriadku. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Naplánované polohovanie.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image039.jpg' | relative_url }})

Geometria vyhadzovača pre Station3

### Plánované polohovanie

Podobne ako v prípade Station2 použijeme aj pre Station3 polohovanie podľa plánu. Pridajte polohovanie kolízie podľa plánu pre **obrobok** s **matricou** ako referenčným objektom v smere **-Y**. Pridajte položku polohovania kolízie **razníka** s **obrobkom** ako referenčným objektom v smere **-Y**. Môžeme si prezrieť naplánovanú sekvenciu polohovania, ako je znázornené v [Fig. 2DCCDL1.40.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig_2DCCDL1_40_Scheduled_positioning_definition_for_Station3). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Kontakt, kde môžete definovať kontaktné podmienky.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image040.jpg' | relative_url }})

Definícia plánovaného polohovania pre stanicu 3

### Definovanie podmienok kontaktu a naplánovanie generovania kontaktov pre Station3

Podobne ako v prípade stanice 2 naplánujeme generovanie kontaktov pre stanicu 3, zaškrtneme políčka „Inicializovať“ a „Generovať“, aby sme inicializovali kontakty a následne vygenerovali nové kontakty; pozri [Fig. 2DCCDL1.41.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig_2DCCDL1_41_Defining_contact_conditions_for_Stage_3) – priradenie predvolených vzťahov medzi objektmi pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}). Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) pre jeden z vzťahov. Na karte **Deformácia** vyberte prepínač typu trenia **Hybridný** a v okne **Dáta medzi objektmi** nastavte hodnotu **0,1** pre položky **Coulomb** aj **Šmyk**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), aby ste opustili okno **Inter-object data**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}), aby ste uplatnili rovnaké podmienky trenia definované pre vybraný vzťah na všetky ostatné vzťahy v zozname, pozri [Fig. 2DCCDL1.41.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig_2DCCDL1_41_Defining_contact_conditions_for_Stage_3). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli na stránku **Stopping controls** a definovali ovládacie prvky zastavenia.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image046.jpg' | relative_url }})

Stanovenie podmienok kontaktu pre 3. fázu

### Ovládacie prvky na zastavenie pre Stanicu 3

Na stránke „Ovládacie prvky zastavenia“ kliknite na kartu **Zastavenie****roviny**, zaškrtnite **políčko „Definované“** a nastavte počiatok na (**0,-0,25**) a vektor na (**0**,**-1**), pozri [Fig. 2DCCDL1.42.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig_2DCCDL1_42_Stopping_plane_stopping_criteria_in_3rd_operation). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli na stránku „Step“ (Krok) a definovali ovládacie prvky simulačných krokov.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image041.jpg' | relative_url }})

Kritériá zastavenia lietadla v 3. fáze operácie

### Ovládacie prvky krokov pre Station3

Na stránke „Kroky“ nastavte **Počet krokov** na hodnotu **10000**, **Krok pre uloženie** do databázy na hodnotu **10** a **Posun matrice** na jeden krok na hodnotu **0,001**. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránke „Generovať databázu“. Keďže sa databáza vygeneruje počas behu programu po dokončení simulácie Station2 v rámci nastavenia prevádzky v dávkovom režime, teraz spustíme simuláciu.

## Spustenie simulácie

Prepnite do režimu simulácie kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom operácií. Kliknutím na názov akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno „Run Options“ (Možnosti spustenia), ako je znázornené na obrázku [Fig. 2DCCDL1.43.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig_2DCCDL1_43_Run_Simulation_popup_window). Použite predvolenú možnosť **Continue Run** (Pokračovať v spúšťaní) a vyberte možnosť „**Pokračovať od posledného kroku**“ a potom vyberte režim simulácie ako **Interaktívny** a kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) na spustenie simulácie.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image042.jpg' | relative_url }})

Vyskočiace okno „Spustiť simuláciu“

## Následné spracovanie 

Po dokončení simulácie sa DB presunie do sekcie „Dokončené“ na karte „Simulácia“ a v súbore protokolu sa zobrazí správa „Dokončených bolo viacero operácií.“. Teraz môžeme prejsť do **režimu Post** kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) a zobraziť výsledky simulácie. V režime Post prehliadač krokov pod grafickou oblasťou zobrazuje čísla krokov dostupných z rôznych simulovaných operácií, pozri [Fig. 2DCCDL1.44.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig_2DCCDL1_44_Step_list_page). Sada stavových premenných dostupných v ponuke „**Post**“ možno použiť na kontrolu odozvy modelu, pozri [Fig. 2DCCDL1.45.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig_2DCCDL1_45_Damage_results_at_last_step_of_last_operation), ktorý zobrazuje rozloženie stavovej premennej poškodenia v poslednom kroku stanice 1, stanice 2 a stanice 3. [Fig. 2DCCDL1.46.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig_2DCCDL1_46_Strain_effective_results_at_last_step_of_last_operation) zobrazuje rozloženie stavovej premennej efektívneho deformácie v poslednom kroku stanice 1, stanice 2 a stanice 3. [ Fig. 2DCCDL1.47.]({{ '/docs/sk/labs/forming_labs/2d_cartridge_case_drawing_lab/' | relative_url }}#Fig_2DCCDL1_47_Stress_effective_results_at_last_step_of_last_operation) znázorňuje rozloženie stavovej premennej efektívneho napätia v poslednom kroku stanice 1, stanice 2 a stanice 3.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image047.jpg' | relative_url }})

Zoznam krokov v postprocesore

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image043.jpg' | relative_url }})

Výsledok poškodenia v poslednom kroku poslednej operácie

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image044.jpg' | relative_url }})

Výsledky s ohľadom na deformáciu v poslednom kroku poslednej operácie

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image045.jpg' | relative_url }})

Výsledky zohľadňujúce napätie v poslednom kroku poslednej operácie

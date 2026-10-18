---
lang: sk
title: "Polotovar na ozubené kolesá SI – laboratórna úloha č. 5"
---

# Laboratórna práca č. 5. 3D neizotermické tvárnenie

Pridajte operáciu 3D tvárnenia ako druhú operáciu z Průzkumníka, aby ste pokračovali v nastavení neizotermického tvárnenia. Kliknite na pridanú operáciu tvárnenia a z roletového menu Typ nastavenia vyberte ![]({{ '/assets/icons/pre_icons/mo_no_batch_setup_button.jpg' | relative_url }}), čím otvoríte a nastavíte úlohu v režime dávkového spracovania. Zmeňte názov operácie na **Forge**. Kliknite na položku **Object** v stromovej štruktúre operácií, aby ste pridali lisovacie formy.

### Pridať objekty pre výsekové formy

Keďže sa objekt obrobku odovzdáva do operácie tvárnenia, dvakrát kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) (Pridať objekt), aby ste pridali zástupné symboly pre hornú a spodnú matricu. Po pridaní sa zobrazí zoznam objektov, ako je znázornené na obrázku [Fig. L5.1.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab5/' | relative_url }}#Fig_L5_1_Object_list_for_3D_forming_operation). Keďže sa obrobok načíta z predchádzajúcej operácie, jeho typ objektu je „Načítané z databázy“. Kliknite na vlastnosť **Obrobok** v strome operácií, aby ste definovali cieľový objem.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab5_image0001.jpg' | relative_url }})

Zoznam objektov pre operáciu 3D tvarovania

### Určiť cieľový objem obrobku

Na karte „Deformačné vlastnosti“ zaškrtnite políčko **Predefinovať**: Cieľový objem a nastavte Cieľový objem ako **Aktívny iba vo FEM**. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_target_volume_icon.jpg' | relative_url }}) (Vypočítať objem) a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}), aby ste potvrdili odporúčaný objem. Upozorňujeme, že sa môže mierne líšiť od hodnoty uvedenej na snímke obrazovky [Fig. L5.2.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab5/' | relative_url }}#Fig_L5_2_Target_Volume_definition_for_workpiece)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab5_image0002.jpg' | relative_url }})

Definícia cieľového objemu pre obrobok

Kliknite na vetvu **Top****die** v prevádzkovom strome, aby ste definovali lisovacie formy.

### Definovanie objektu „Top die“

Overte, či je typ objektu „Top Die“ nastavený na **tuhý**, a nastavte teplotu na **148,889** °C. Vložte hornú matricu z druhej operácie simulácie ozubeného kolesa, ktorú ste spustili vyššie (v projekte „Project Gear“). Kliknite teda na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli do okna Geometria.

\- Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Importovať geometriu zo súboru)

\- Vyhľadajte súbor „**Gear.DB**“ (v priečinku Project Gear)

\- Vyberte prvý krok (-N) v operácii 3 (ľavý stĺpec zoznamu krokov, pozri [Fig. L5.3.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab5/' | relative_url }}#Fig_L5_3_DB_step_list_display_for_Import_Geometry_option))

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab5_image0003.jpg' | relative_url }})

Zobrazenie zoznamu krokov databázy pre možnosť „Importovať geometriu“

\- Stlačte ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }})

\- Vyberte hornú matricu (pozri [Fig. L5.4.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab5/' | relative_url }}#Fig_L5_4_Object_selection_for_import_geometry_option))

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab5_image0004.jpg' | relative_url }})

Možnosť výberu objektov pre import geometrie

\- Stlačte ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}).

_Upozorňujeme, že poloha importovanej hornej matrice bude opravená v [section 5.5.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab5/' | relative_url }}#5_5_Schedule_position_the_objects)_

Kliknite na vetvu **Pohyb** v hornej časti stromu operácií, aby ste definovali ovládacie prvky pohybu.

\- Nastavte konštantnú **rýchlosť** pohybu **76,2** mm/s v smere **–Y**.

Kliknite na vetvu **Spodná****matrica** v prevádzkovom strome, aby ste definovali spodnú matricu.

### Definovanie objektu spodnej matrice

Podobne ako pri definícii hornej formy nastavte teplotu spodnej formy na **148,889** °C a načítajte geometriu z databázy Gear.DB z predchádzajúceho laboratórneho cvičenia.

_Upozorňujeme, že poloha importovanej hornej formy bude opravená v [section 5.5.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab5/' | relative_url }}#5_5_Schedule_position_the_objects)_

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab5_image0005.jpg' | relative_url }})

Importované objekty „Top die“ a „Bottom Die“

Kliknite na vetvu **Plánované umiestnenie** v časti „Umiestnenie“, aby ste naplánovali polohy objektov pre formovanie. 

### Rozmiestnenie objektov podľa plánu

Keďže obrobok je vytvorený z primitívu, jeho smer výšky je Z, avšak smer dovozu foriem smerom nahor je Y, preto kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Pridať). Otočte obrobok o 90 stupňov okolo osi –X, pričom stred ponechajte na (0,0,0), ako je znázornené na obrázku [Fig. L5.6.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab5/' | relative_url }}#Fig_L5_6_Workpiece_scheduled_rotate_definition), aby ste všetky objekty zarovnali smerom nahor na os Y. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) definíciu uzavrite.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab5_image0006.jpg' | relative_url }})

Definícia plánovaného otáčania obrobku

Podobne dvakrát kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Pridať), aby ste naplánovali polohu nástrojov tak, aby sa dotkli obrobku pomocou polohovania s ohľadom na kolízie.

Po pridaní sa v okne naplánovaných polôh zobrazia podrobnosti o pridaných naplánovaných polohách, ako je znázornené v [Fig. L5.7.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab5/' | relative_url }}#Fig_L5_7_Scheduled_positioned_details_for_forge_operation)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab5_image0007.jpg' | relative_url }})

Plánované údaje o polohe pre prevádzku kováčskej dielne

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pridali kontakt.

### Definícia kontaktu

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}). Upravte jeden z vzťahov a nastavte konštantnú hodnotu trenia **0,3**. Prejdite na kartu **Tepelné** a z roletového menu „Konštanta“ vyberte možnosť **Tvarovanie** (pozri [Fig. L5.8.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab5/' | relative_url }}#Fig_L5_8_Inter-object_Thermal_settings_window)). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), aby ste zatvorili okno definície, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}), aby ste uplatnili koeficient trenia a prenosu tepla na ostatné vzťahy. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), aby ste opustili okno.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab5_image0008.jpg' | relative_url }})

Okno nastavení tepelného správania medzi objektmi

Keďže sa objekt „obrobok“ načítava z databázy objektov, vzťahy medzi objektmi sa v tejto fáze nemôžu generovať, preto sa uistite, že sú zaškrtnuté políčka „Scheduled Initialize“ a „Generate contact“, ako je znázornené na obrázku [Fig. L5.9.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab5/' | relative_url }}#Fig_L5_9_Inter-object_definition_window_after_adding_fiction_and_HTC). Tým sa počas behu simulácie inicializujú predchádzajúce kontakty a vygenerujú nové kontakty.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab5_image0009.jpg' | relative_url }})

Okno s definíciami medzi objektmi po pridaní fikcie a HTC

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste nastavili ovládacie prvky zastavenia.

### Nastavenie ovládacích prvkov zastavenia a simulácie

Nastavte hrúbku výstupku na 5,08 mm pomocou možnosti „Vzdialenosť medzi objektmi“ tak, že vyberiete body na dosadacej ploche hornej a spodnej matrice (pozri [ Lab3 section 3.10. Define Distance between objects Stopping controls]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab3/' | relative_url }}#3_10_Define_Distance_between_objects_Stopping_controls)).

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste nastavili ďalšie ovládacie prvky simulácie.

Nastavte ovládacie prvky krokov v časti „Simulation Controls“. Pre túto operáciu použite 300 krokov. Zmerajte vzdialenosť medzi nástrojmi, aby ste určili vhodnú hodnotu posunu matrice. Celkovú vzdialenosť (203,2) vydelite počtom krokov (300), čím získate posun formy (**0,67733**). (Pozrite [Fig. L5.10.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab5/' | relative_url }}#Fig_L5_10_Guided_mode_Simulation_controls_settings)) Ukladajte každých **10** krokov.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab5_image0010.jpg' | relative_url }})

Nastavenia ovládacích prvkov simulácie v režime s navádzaním

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na vytvorenie databázy.

### Kontrola a vytvorenie databázy

Pozrite si náhľad naplánovaného umiestnenia v zobrazovacom okne, ako je znázornené na obrázku [Fig. L5.11.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab5/' | relative_url }}#Fig_L5_11_Scheduled_positioning_preview_in_DB_generation_window). Ak je potrebná korekcia umiestnenia, vráťte sa späť a opravte ju v okne naplánovaného umiestnenia. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) a skontrolujte informácie o kontrole údajov v súbore správ. Uistite sa, že kontrola databázy nepreukázala žiadne problémy. Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) na vytvorenie databázy a skontrolujte, či sa zobrazila správa „Databáza bola vytvorená“.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab5_image0011.jpg' | relative_url }})

Náhľad plánovaného umiestnenia v okne na generovanie databázy

Kliknutím na tlačidlo „![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode“ (nad stromom operácií) spustíte simuláciu.

### Spustiť simuláciu

Kliknutím na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno „Run Options“ (Možnosti spustenia). Pomocou predvolenej možnosti **Continue Run** (Pokračovať v spustení) vyberte možnosť „**Continue from the last step**“ (Pokračovať od posledného kroku), potom nastavte režim simulácie na **Interactive** (Interaktívny) a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

Pri pohľade na grafické znázornenie simulácie získate prvotnú predstavu o tom, čo môžete očakávať po otvorení postprocesora. Simuláciu sledujte aj v časti „Simulácia“ a v protokoloch. V poslednom riadku súboru správ a protokolu sa zobrazí informácia o dokončení simulácie, čo potvrdí, že môžete kliknúť na tlačidlo „![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode“ a prezrieť si výsledky.

### Výsledky hodnotenia

**Výsledky hry**

Pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_preview_play_button.jpg' | relative_url }}) (Prehrávať dopredu) si prehrajte priebeh procesu kovania.

Vyskúšajte všetky rôzne možnosti zobrazenia obrobku ![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab5_image0000.jpg' | relative_url }}), aby ste si prezreli tok materiálu. Patria sem ![]({{ '/assets/icons/post_icons/mo_slice.jpg' | relative_url }}) (rezanie), ![]({{ '/assets/icons/post_icons/mo_show_cotact_icon.jpg' | relative_url }}) (kontakt) a ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) (premenné poľa).

Hoci sa táto laboratórna úloha simuluje rýchlo, sieť je príliš hrubá a časový krok je príliš veľký na to, aby sa dala odhaliť chyba. Náznak záhybu je možné vidieť pri rozrezaní objektu v poslednom kroku v rovine Z, ako je znázornené v [Fig. L5.12.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab5/' | relative_url }}#Fig_L5_12_Fold_indication_area_marked_by_red_circle)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab5_image0012.jpg' | relative_url }})

Oblasť indikácie zloženia označená červeným kruhom

**Sledovanie bodov**

Kliknite na ikonu ![]({{ '/assets/icons/post_icons/mo_point_tracking_icon.jpg' | relative_url }}) v nástrojoch príspevku a vyberte dva body na obrobku, pričom sa zobrazuje krok -1. Kliknite na ikonu ![]({{ '/assets/icons/pre_icons/mo_settings_icon.jpg' | relative_url }}) (Nastavenia) a uistite sa, že je zvolená možnosť „Typ pohyblivého bodu“, aby sa sledoval tok materiálu. Kliknite na tlačidlo ![]({{ '/assets/icons/post_icons/mo_track_button.jpg' | relative_url }}), aby ste spustili sledovanie bodov, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}), aby ste zatvorili okno sledovania bodov. (Pozrite [Fig. L5.13.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab5/' | relative_url }}#Fig_L1_13_Top_die_object_window)).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab5_image0013.jpg' | relative_url }})

Definícia sledovania bodov pre obrobok

Zapnite zobrazenie teplotných kontúr, prehrávajte jednotlivé kroky a sledujte, ako sa body zaznamenávajú pri teplotách v strede a na okrajoch. (Pozri [Fig. L5.14.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab5/' | relative_url }}#Fig_L5_14_Point_tracking_graph_at_first_step) a [Fig. L5.15.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab5/' | relative_url }}#Fig_L5_15_Point_tracking_graph_at_last_step))

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab5_image0014.jpg' | relative_url }})

Graf sledovania bodov v prvom kroku

Vyberte posledný krok simulácie zo zoznamu krokov alebo pomocou ikony posledného kroku. Graf sleduje teplotu v každom bode počas celého procesu ako funkciu času. Poloha týchto bodov sa v priebehu simulácie sleduje na základe toku materiálu. Polohu je možné zobraziť krok za krokom.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab5_image0015.jpg' | relative_url }})

Graf sledovania bodov v poslednom kroku

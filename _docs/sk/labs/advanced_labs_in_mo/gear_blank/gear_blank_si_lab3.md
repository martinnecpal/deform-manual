---
lang: sk
title: "Polotovar na ozubené kolesá SI Lab 3"
---

# Cvičenie č. 3. Postupné kroky pri práci s programom 3D Forge

V tomto cvičení sa dozviete, ako pokračovať v postupných 3D operáciách po konverzii 2D objektov na 3D pomocou konvertora 2D na 3D.

### Pridať operáciu 3D tvárnenia

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa položky „3D Forming“ v zozname „Forming operations“ na karte **Explorer**, ako je znázornené na obrázku [Fig. L3.1.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab3/' | relative_url }}#Fig_L3_1_Adding_3D_forming_operation_after_2D_to_3D_convertor)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab3_image0001.jpg' | relative_url }})

Pridanie operácie 3D tvarovania po konvertore z 2D na 3D

Otvorte operáciu 3D tvarovania v editore operácií kliknutím na ňu a vyberte tlačidlo ![]({{ '/assets/icons/pre_icons/mo_no_batch_setup_button.jpg' | relative_url }}), čím sa otvorí kontextové menu „Typ nastavenia“ (pozri [Fig. L3.2.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab3/' | relative_url }}#Fig_l3_2_Setup_type_popup_for_3rd_operation_3D_Forming)), aby ste mohli nastaviť úlohu v dávkovom režime.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab3_image0002.jpg' | relative_url }})

Vyskakovacie okno s typom nastavenia pre tretiu operáciu – 3D tvarovanie

Premenujte operáciu 3D tvárnenia na **Kovanie** tak, že v editore operácií kliknete na názov „Tvárnenie“ v položke „Operácia 3D tvárnenia“ a stlačením klávesy Enter potvrdíte zmenu.

### Nastavenie režimu simulácie a pridávanie objektov

V okne „Simulation controls“ zrušte zaškrtnutie políčka „Heat transfer mode“ na hlavnej karte „Simulation control“, keďže ide o izotermickú simuláciu. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Objects“.

Pokračujte v nastavení pridaním troch objektov, ktoré budú slúžiť ako polohovacie prvky pre obrobok a hornú a dolnú matricu potrebné pre túto operáciu.

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste začali definovať objekt obrobku.

### Definícia objektu obrobku

Vyberte typ objektu obrobku „načítanie z databázy“, ako je znázornené v [Fig. L3.3.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab3/' | relative_url }}#Fig_L3_3_Workpiece_object_window_for_3D_forge_operation). Objekt „Načítanie z databázy“ prečíta všetky údaje o objekte z posledného kroku predchádzajúcej operácie, takže prečíta údaje o konvertovanom 3D objekte.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab3_image0003.jpg' | relative_url }})

Okno s objektom obrobku pre operáciu v 3D Forge

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste zmenili nastavenia siete obrobku.

### Zmena nastavení siete obrobku

****Zaškrtnite políčko **Nastaviť parametre siete**, ak chcete zmeniť nastavenia siete. Nastavte **veľkosť****pomer** na hodnotu 2 a potom vyberte typ **Absolútny** ****(pozri [ Fig. L3.4.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab3/' | relative_url }}#Fig_L3_4_Expert_mode_general_mesh_settings_for_Read_from_DB_object)). Týmto sa určí počet prvkov na základe najmenšej veľkosti prvku a pomeru veľkostí. Počet prvkov sa bude zvyšovať s rastúcou zložitosťou geometrie.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab3_image0004.jpg' | relative_url }})

Všeobecné nastavenia siete v expertnom režime pre objekt „Čítanie z databázy“

Vyberte kartu **Remesh** a nastavte hĺbku kolízie na hodnotu **0,7** **Relatívna**. (pozri [Fig. L3.5.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab3/' | relative_url }}#Fig_L3_5_Expert_mode_remesh_criteria_settings_for_Read_from_DB_object))

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab3_image0005.jpg' | relative_url }})

Nastavenia kritérií pregenerovania siete v expertnom režime pre objekt „Read from DB“

Keďže údaje, ako napríklad materiál a okrajové podmienky, sa preberajú z predchádzajúcej operácie, nie je potrebné tieto údaje meniť. V stromovej štruktúre operácií vyberte položku **Vlastnosť** pod položkou „obrobok“, aby ste nastavili cieľový objem.

### Nastavenie cieľového objemu obrobku

Na karte „Deformačné vlastnosti“ zaškrtnite políčko **Predefinovať**: Cieľový objem a nastavte iba možnosť **Cieľový objem ako aktívny v FEM**. Toto nastavenie by sa malo používať pri väčšine simulácií kovania. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_target_volume_icon.jpg' | relative_url }}) (Vypočítať objem) a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}), aby ste potvrdili odporúčaný objem. Upozorňujeme, že sa môže mierne líšiť od hodnoty zobrazennej v [Fig. L3.6.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab3/' | relative_url }}#Fig_L3_6_Target_volume_definition_in_deformation_property_window)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab3_image0006.jpg' | relative_url }})

Definícia cieľového objemu v okne vlastností deformácie

Kliknite na položku **Geometria** pod položkou **Horná matrica** v strome operácií, aby ste pokračovali v definovaní hornej matrice.

### Definícia hornej matrice

Načítajte geometriu „**gear_top_die_SI****.STL**“. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať geometriu z knižnice) a kliknite na ![]({{ '/assets/icons/pre_icons/mo_open_button.jpg' | relative_url }}), aby ste otvorili (načítali) súbor „**gear_top_die_SI****.****STL**”. Geometria hornej matrice sa nachádza v inštalačnom priečinku DEFORM v adresári \3D\Labs.

Skontrolujte geometriu pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) a uistite sa, že v výsledkoch, ako je znázornené na obrázku [Fig. L3.7.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab3/' | relative_url }}#Fig_L3_7_Top_die_geometry_checking_result), nie sú prítomné neplatné hrany a orientácie, malé plochy, počet voľných hrán je 0 a počet plôch je 1. To znamená, že geometria je v poriadku, takže kliknite na **Pohyb** pod hornou maticou v strome operácií, aby ste nastavili ovládacie prvky pohybu hornej matice.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab3_image0007.jpg' | relative_url }})

Výsledok kontroly geometrie hornej matrice

V okne **Pohyb** nastavte pohyb s konštantnou **rýchlosťou** **76,2** mm/s v smere **–Y**, ako je znázornené na obrázku [Fig. L3.8.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab3/' | relative_url }}#Fig_L3_8_Top_die_movement_window)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab3_image0008.jpg' | relative_url }})

Okienko pre pohyb hornej matrice

Kliknite na položku **Geometria** pod položkou **Spodná** **matrica** v strome operácií, aby ste definovali spodnú matricu.

### Definícia spodnej matrice

Načítajte súbor „**gear_bottom_die_SI****.****STL**“ pre spodnú maticu (objekt 3) z knižnice. Skontrolujte geometriu pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) a uistite sa, že geometria je bez chýb, ako je vysvetlené v [3.6. Top die definition.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab3/' | relative_url }}#3_6_Define_Top_die).

Na umiestnenie objektov kliknite na položku **Plánované****Umiestnenie** v časti Ovládacie prvky v stromovej štruktúre operácií.

### Plánovanie objektov pozícií

Po importe nových foriem sa môže stať, že nebudú v správnej polohe. Preto použite funkciu „Polohovanie podľa kolízie“ na posunutie hornej formy v smere –Y, kým sa nedotkne obrobku, a spodnej formy v smere +Y, kým sa nedotkne obrobku. Keďže sa obrobok načítava z objektu DB, v tejto operácii nemôže byť umiestnený, preto musí byť naplánovaný tak, aby bol umiestnený počas behu programu.

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Pridať) a naplánujte umiestnenie **hornej matrice** pomocou interferencie v smere **-****Y** vzhľadom na **W******orkp** iece **, ako je znázornené na obrázku [Fig. L3.9.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab3/' | relative_url }}#Fig_L3_9_Top_die_scheduled_positioning_settings). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) definíciu uzavrite.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab3_image0009.jpg' | relative_url }})

Najdôležitejšie nastavenia plánovaného polohovania matice

Podobne umiestnite **spodnú maticu** tak, aby dochádzalo k tesnému uloženie v smere **+Y** vo vzťahu k **obrobku**, a to pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Pridať). Po pridaní zoznamu naplánovaných polôh sa zobrazia podrobnosti o pridaných naplánovaných polohách, ako je znázornené na obrázku [Fig. L3.10.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab3/' | relative_url }}#Fig_L3_10_Scheduled_positioned_details_for_forge_operation). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pridajte kontakt.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab3_image0010.jpg' | relative_url }})

Plánované údaje o polohe pre prevádzku kováčskej dielne

### Definícia kontaktu

Pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) nastavte predvolené vzťahy medzi objektmi. Obrobok by mal byť podriadený ako hornej, tak aj spodnej matrici. Pri 3D simuláciách sa vlastný kontakt (obrobok ako hlavný objekt voči sebe samému) zvyčajne nepoužíva, pretože môže výrazne predĺžiť dobu simulácie. Na sledovanie ohýbania sú k dispozícii aj iné nástroje. Tým sa budeme venovať v neskoršom laboratórnom cvičení.

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) pre jeden z vzťahov. V poli **Trenie** -> **Hodnota** použite roletové menu „Konštanta“ a vyberte možnosť **Kovanie za tepla (s mazaním) 0,3**. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) opustite menu. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}), aby ste hodnotu trenia aplikovali na ďalšie dva vzťahy. Keďže objekt obrobku pridaný vo vzťahu sa načíta z databázy, medziobjektové vzťahy sa teraz nemôžu generovať tak ako v laboratóriu 1, preto sa uistite, že sú zaškrtnuté políčka Scheduled Initialize a Generate contact, ako je znázornené na obrázku [Fig. L3.11.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab3/' | relative_url }}#Fig_L3_11_Scheduled_Inter-object_contact_generation_settings). Týmto sa počas simulácie inicializujú predchádzajúce kontakty a vygenerujú nové kontakty.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab3_image0011.jpg' | relative_url }})

Nastavenia generovania plánovaných kontaktov medzi objektmi

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste pridali ovládacie prvky na zastavenie.

### Určenie vzdialenosti medzi objektmi – ovládacie prvky zastavenia

Vyberte režim s navádzaním ![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }}); kritérium zastavenia pre hrúbku výrezu môžete nastaviť zaškrtnutím políčka **Vzdialenosť medzi objektmi**. Táto voľba aktivuje výber myšou, čo vám umožní vybrať dva referenčné body. Vyberte referenčné body na ploche prebytočného materiálu. Rozrežte objekty pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_slice.jpg' | relative_url }}) (Rezanie) v smere +Z až do bodu (0,0,0,001) a potom vyberte ikonu ![]({{ '/assets/icons/pre_icons/mo_plus_z_icon.jpg' | relative_url }}) pred výberom bodov na hrúbke prebytočného materiálu, ako je znázornené na obrázku [Fig. L3.12.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab3/' | relative_url }}#Fig_L3_12_Distance_between_dies_stopping_controls_definition)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab3_image0012.jpg' | relative_url }})

Definícia ovládacích prvkov na zastavenie lisovacích nástrojov

V tomto prípade je dôležité vybrať vnútornú časť plochy výrezu. Zvoľte smer **Y**, aby sa použila vzdialenosť v osi Y, a potom do poľa „Vzdialenosť medzi objektmi“ zadajte hodnotu **5,08** mm. Ak chcete tento rez odstrániť, môžete sa opäť vrátiť do ponuky rezania.

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste nastavili ovládacie prvky simulácie.

### Definovanie ovládacích prvkov simulácie

Kliknutím na ikonu ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) (Prejsť do expertného režimu) (na paneli nástrojov v hlavičke) otvoríte nastavenia pokročilých ovládacích prvkov simulácie. Všimnite si, že číslo operácie sa automaticky aktualizuje na 3, ako je znázornené na obrázku [Fig. L3.13.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab3/' | relative_url }}#Fig_L1_13_Top_die_object_window)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab3_image0013.jpg' | relative_url }})

Hlavná karta „Krokové riadenie“

Prejdite na kartu **Krok prírastku**. Určite vhodný **posun matrice na krok** (DSMAX) a počet simulačných krokov, ktoré budete potrebovať na uzavretie nástrojov. Zmerajte vzdialenosť medzi hornou a spodnou maticou pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_measure_tool_icon.jpg' | relative_url }}) (merací nástroj). Pri používaní meracieho nástroja môžete kliknúť pravým tlačidlom myši na hlavný displej a vybrať možnosť CAD Style. Tým získate meranie v definovanom smere osi (X, Y alebo Z). Znovu kliknite pravým tlačidlom myši na displej a vyberte požadovanú os. Vzdialenosť Y medzi nástrojmi je ~48,26 mm. Táto operácia kovania by mala trvať ~100 krokov. Celkovú vzdialenosť (48,26) vydelíte počtom krokov, čím získate posun matrice **0,4826**. (Pozri [Fig. L3.14.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab3/' | relative_url }}#Fig_L1_14_Top_die_Geometry_window))

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab3_image0014.jpg' | relative_url }})

Definícia krokového posunu pre hornú matricu

Prejdite na kartu „Kroky“, kde nastavte hodnotu **100** ako **počet krokov** a uložte **každých****5** **krokov**. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) vygenerujte databázu.

### Kontrola a vytvorenie databázy

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) a prezrite si informácie o kontrole údajov v súbore so správami. Uistite sa, že kontrola databázy nepreukázala žiadne problémy. Následne kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) na vytvorenie databázy a počkajte, kým sa zobrazí správa „Databáza bola vytvorená“.

Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) MO Mode (nad stromom operácií) spustíte simuláciu.

### Spustiť simuláciu na viacerých procesoroch

Kliknutím na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno „Run Options“ (Možnosti spustenia). Pomocou predvolenej možnosti **Continue Run** (Pokračovať v spustení) vyberte možnosť „**Continue from the last step**“ (Pokračovať od posledného kroku), potom nastavte režim simulácie na **Interactive** (Interaktívny) a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

Ak chcete nastaviť parametre MPI, kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_more_button.jpg' | relative_url }}). Rozbalí sa okno „Run Options“, v ktorom sa zobrazia možnosti na nastavenie parametrov MPI pre simuláciu (maximálny počet procesorov, ktorý je možné nastaviť, závisí od vašej licencie 3D MPI).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab3_image0015.jpg' | relative_url }})

Spustiť možnosti – nastavenia viacerých procesorov

Kliknite na ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}), aby ste spustili simuláciu.

Sledujte okno s grafickým zobrazením simulácie a kartu „Simulation message“ (Správy simulácie), aby ste mohli monitorovať stav prebiehajúcej úlohy, ako je znázornené v [Fig. L3.16.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab3/' | relative_url }}#Fig_l3_16_MO_Simulation_mode_3rd_operation_running_status)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab3_image0016.jpg' | relative_url }})

Režim simulácie MO – stav 3. operácie počas prevádzky

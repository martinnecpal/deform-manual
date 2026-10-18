---
lang: sk
title: "Polotovar na ozubené kolesá – laboratórium 5 (EN)"
---

# Laboratórna práca č. 5: 3D neizotermické tvárnenie

Pridajte **3D****tvarovanie****operáciu** ako druhú operáciu z **Exploreru**, aby ste pokračovali v nastavení neizotermického tvarovania. Kliknite na pridanú operáciu tvárnenia a z roletového menu Typ nastavenia vyberte ![]({{ '/assets/icons/pre_icons/mo_no_batch_setup_button.jpg' | relative_url }}), aby ste otvorili a nastavili úlohu v režime Batch. Zmeňte názov operácie na **Kovanie**.

Kliknite na položku **Objekt** v strome operácií, aby ste pridali lisovacie formy.

### Pridať objekty

Keďže objekt obrobku je odovzdaný do operácie tvárnenia, dvakrát kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) (Pridať objekt), aby ste pridali zástupné symboly pre hornú a spodnú matricu. Po pridaní objektov sa zobrazí zoznam, ako je znázornené na obr. L5.1. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab5_image0001.jpg' | relative_url }})

Zoznam objektov pre operáciu 3D tvarovania

Kliknite na položku **Vlastnosti obrobku** v strome operácií, aby ste definovali cieľový objem.

### Určiť cieľový objem obrobku

Na karte „Deformačné vlastnosti“ zaškrtnite políčko **Predefinovať**: **Cieľový** objem a nastavte iba možnosť **Cieľový objem ako aktívny v FEM**. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_target_volume_icon.jpg' | relative_url }}) (Vypočítať objem) a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}), aby ste potvrdili odporúčaný objem. Upozorňujeme, že sa môže mierne líšiť od hodnoty uvedenej na snímke obrazovky na obr. L5.2.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab5_image0002.jpg' | relative_url }})

Definícia cieľového objemu pre obrobok

Kliknite na vetvu **Top****die** v prevádzkovom strome, aby ste definovali lisovacie formy.

### Definovanie objektu „Top die“

Overte, či je typ objektu „Top Die“ tuhý, a nastavte teplotu na **300** °F. Načítajte hornú matricu z druhej operácie simulácie ozubeného kolesa, ktorú ste spustili vyššie (v projekte „Project Gear“). Kliknite teda na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli do okna „Geometry“.

\- Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_import_file_icon2.jpg' | relative_url }}) (Importovať geometriu zo súboru)

\- Prejdite do priečinka „**G****ear.****DB**“ (v priečinku projektu **Gear**)

\- Vyberte prvý krok (-N) v operácii **2** (ľavý stĺpec zoznamu krokov, pozri obr. L5.3.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab5_image0003.jpg' | relative_url }})

Zobrazenie zoznamu krokov databázy pre možnosť „Importovať geometriu“

\- Stlačte ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}).

\- Vyberte **Top****die** (pozri obr. L5.4.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab5_image0004.jpg' | relative_url }})

Možnosť výberu objektov pre import geometrie

\- Stlačte ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}).

Kliknite na vetvu **Top****die****Movement** v prevádzkovom strome, aby ste definovali ovládacie prvky pohybu.

Nastavte konštantnú **rýchlosť** pohybu **3** palcov za sekundu v smere **–Y**.

_Poznámka: Poloha importovanej hornej matrice bude opravená v súbore _[section 5.5.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/' | relative_url }}#5_5_Schedule_position_the_objects)__

Kliknite na vetvu **Spodná****matrica** v prevádzkovom strome, aby ste definovali spodnú matricu.

### Definovanie objektu spodnej matrice

Podobne ako pri definícii hornej formy nastavte teplotu spodnej formy na **300** °F a načítajte geometriu zo súboru **Gear.DB** z predchádzajúceho cvičenia. 

_Poznámka: Poloha importovanej hornej matrice bude opravená v [section 5.5.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/' | relative_url }}#5_5_Schedule_position_the_objects)_

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab5_image0005.jpg' | relative_url }})

Importované objekty „Horná forma“ a „Spodná forma“

Kliknite na vetvu **Plánované****polohovanie** v časti **Polohovanie**, aby ste naplánovali polohy objektov pre tvarovanie.

### Rozmiestnenie objektov podľa plánu

Keďže obrobok je vytvorený z primitívu, jeho smer výšky je Z, avšak smer nahor pri importovaných formách je Y, preto kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Pridať) a otočte obrobok o 90 stupňov okolo osi –X, pričom stred ponechajte na (0,0,0), ako je znázornené na obr. L5.6, aby ste všetky objekty zarovnali smerom nahor podľa osi Y. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) uzavrite definíciu.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab5_image0006.jpg' | relative_url }})

Definícia plánovaného otáčania obrobku

Podobne dvakrát kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Pridať), aby ste naplánovali polohu nástrojov tak, aby sa dotkli obrobku pomocou polohovania na základe kolízie.

Po pridaní sa v okne naplánovaného polohovania zobrazia podrobnosti o pridaných naplánovaných polohách, ako je znázornené na obr. L5.7.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab5_image0007.jpg' | relative_url }})

Plánované údaje o polohe pre prevádzku kováčskej dielne

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku **Kontakt**.

### Definovanie vzťahov medzi objektmi

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}). Upravte jeden z vzťahov a nastavte konštantnú hodnotu trenia **0,3**. Prejdite na **kartu Thermal****** a z roletového menu Constant vyberte možnosť **Forming** (pozri obr. L5.8.). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte okno definície a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) nastavte koeficient trenia a prenosu tepla aj pre ostatné vzťahy.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab5_image0008.jpg' | relative_url }})

Okno nastavení tepelného správania medzi objektmi

Keďže sa objekt „obrobok“ načítava z databázy objektov, vzťahy medzi objektmi sa v tejto fáze nemôžu generovať, preto sa uistite, že sú zaškrtnuté políčka „Scheduled Initialize“ a „Generate contact“, ako je znázornené na obr. L5.9. Týmto sa počas behu simulácie inicializujú predchádzajúce kontakty a vygenerujú nové kontakty.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab5_image0009.jpg' | relative_url }})

Okno s definíciami medzi objektmi po pridaní fiktívneho objektu a HTC

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste nastavili ovládacie prvky zastavenia.

### Definovanie ovládacích prvkov zastavenia a krokovania

Nastavte hrúbku výstupku na **0,2** ” pomocou možnosti „Vzdialenosť medzi objektmi“ tak, že vyberiete body na výstupkovej ploche hornej a dolnej matrice (pozri časť [3.10. Define Distance between objects Stopping controls]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab3/' | relative_url }}#3_10_Define_Distance_between_objects_Stopping_controls) v laboratórnej úlohe 3).

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste nastavili ďalšie ovládacie prvky simulácie.

Nastavte ovládacie prvky krokov v časti „Simulation Controls“. Pre túto operáciu použite **300** krokov. Zmerajte vzdialenosť medzi nástrojmi, aby ste určili vhodnú hodnotu posunu matrice. Celkovú vzdialenosť (8,0) vydelte počtom krokov (300), čím získate posun formy (**0,02667**). (Pozri obr. L5.10.) **Uložte** **každých****10** krokov.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab5_image0010.jpg' | relative_url }})

Nastavenia ovládacích prvkov simulácie v režime s návodom

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste vytvorili databázu.

### Kontrola a vytvorenie databázy

Pozrite si náhľad naplánovaného polohovania v zobrazovacom okne, ako je znázornené na obr. L5.11. Ak je potrebná korekcia polohovania, vráťte sa späť a opravte ju v okne naplánovaného polohovania. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) a skontrolujte informácie o kontrole údajov v súbore správ. Uistite sa, že kontrola databázy nepreukázala žiadne problémy. Následne kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) na vytvorenie databázy a počkajte na zobrazenie správy „Databáza bola vytvorená“.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab5_image0011.jpg' | relative_url }})

Náhľad plánovaného umiestnenia v okne na vytváranie databázy

Kliknutím na tlačidlo „![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode“ (nad stromom operácií) spustíte simuláciu.

### Spustiť simuláciu

Kliknutím na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno „Run Options“ (Možnosti spustenia). Pomocou predvolenej možnosti **Continue Run** (Pokračovať v spúšťaní) vyberte možnosť „**Continue from the last step**“ (Pokračovať od posledného kroku), potom nastavte režim simulácie na **Interactive** (Interaktívny) a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

Pri pohľade na grafické zobrazenie simulácie získate prvotnú predstavu o tom, čo môžete očakávať po otvorení postprocesora. Simuláciu sledujte aj v časti „Simulácia“ a prostredníctvom správ v protokole. V poslednom riadku súboru správ a protokolu sa zobrazí informácia o dokončení simulácie, čo potvrdí, že môžete kliknúť na tlačidlo „![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode“ a prezrieť si výsledky.

### Výsledky hodnotenia

**Výsledky hry**

Pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_preview_play_button.jpg' | relative_url }}) (Prehrávať dopredu) si prehrajte priebeh procesu kovania.

Vyskúšajte všetky rôzne možnosti zobrazenia obrobku ![]({{ '/assets/icons/pre_icons/mo_display_modes_options.jpg' | relative_url }}), aby ste si overili tok materiálu. Patria sem ![]({{ '/assets/icons/post_icons/mo_slice.jpg' | relative_url }}) (rezanie), ![]({{ '/assets/icons/post_icons/mo_show_cotact_icon.jpg' | relative_url }}) (kontakt) a ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) (premenné poľa).

Hoci sa táto laboratórna úloha simuluje rýchlo, sieť je príliš hrubá a časový krok príliš veľký na to, aby sa dala identifikovať chyba. Náznak záhybu je možné vidieť pri rozrezaní objektu v poslednom kroku v rovine Z, ako je znázornené na obr. L5.12.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab5_image0012.jpg' | relative_url }})

Oblasť indikácie prehybu označená červeným kruhom

**Sledovanie bodov**

Kliknite na ikonu ![]({{ '/assets/icons/post_icons/mo_point_tracking_icon.jpg' | relative_url }}) v nástrojovej lište a vyberte dva body na obrobku, pričom sa zobrazuje krok -1. Kliknite na ikonu ![]({{ '/assets/icons/pre_icons/mo_settings_icon.jpg' | relative_url }}) (Nastavenia) a uistite sa, že je zvolená možnosť „Typ pohyblivého bodu“, aby sa sledoval tok materiálu. Kliknite na tlačidlo ![]({{ '/assets/icons/post_icons/mo_track_button.jpg' | relative_url }}) na spustenie sledovania bodov a kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) na zatvorenie okna sledovania bodov. (Pozri obr. L5.13.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab5_image0013.jpg' | relative_url }})

Definícia sledovania bodov pre obrobok

Zapnite zobrazenie teplotných kontúr, prehrávajte jednotlivé kroky a sledujte, ako sa body vyznačujú pri teplotách v strede a na okraji. (Pozri obr. L5.14 a obr. L5.15.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab5_image0014.jpg' | relative_url }})

Graf sledovania bodov v prvom kroku

Vyberte posledný krok simulácie zo zoznamu krokov alebo pomocou ikony posledného kroku. Graf zaznamenáva teplotu v každom bode počas celého procesu ako funkciu času. Poloha týchto bodov sa v priebehu simulácie sleduje na základe toku materiálu. Polohu je možné zobraziť krok za krokom.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab5_image0015.jpg' | relative_url }})

Graf sledovania bodov v poslednom kroku

Kliknite na [Lab 6. Mechanical Press]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab6/' | relative_url }}), aby ste nastavili Lab6.

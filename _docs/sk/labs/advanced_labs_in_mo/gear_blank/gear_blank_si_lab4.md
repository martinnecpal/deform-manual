---
lang: sk
title: "Polotovar na ozubené koleso SI Lab 4"
---

# Laboratórna práca č. 4. 3D neizotermický proces prenosu vzduchu

V programe DEFORM vytvorte nový projekt s názvom **Gear_t** podľa pokynov v laboratórnej úlohe 1. Ide o simuláciu pozostávajúcu z dvoch operácií. Operácia 1 sa týka výlučne prenosu tepla a znázorňuje pohyb obrobku z ohrievača k nástrojom. Operácia 2 je kovanie s povolenými výpočtami teploty.

### Operácia pridania a pomenovania

Pridajte operáciu „3D Heat Transfer“ z karty „Explorer“, ako je znázornené na obrázku [Fig. L4.1.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab4/' | relative_url }}#Fig_L4_1_Adding_3D_Heat_Transfer_operation_and_selecting_process_window_settings)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab4_image0001.jpg' | relative_url }})

Pridanie operácie 3D prenosu tepla a výber nastavení procesného okna

Potvrďte voľbu „Prenos vzduchom“ v okne „Prenos tepla“. V editore operácií zmeňte názov operácie na „**Prenos z ohrievača**“, ako je znázornené na obrázku [Fig. L4.2.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab4/' | relative_url }}#Fig_L4_2_Naming_operation_as_Transfer_From_Heater). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab4_image0002.jpg' | relative_url }})

Pomenovanie operácie ako „Prenos z ohrievača“

### Definovanie podmienok procesu

Nastavte ****čas prenosu**** na **15** sekúnd (pozri [Fig. L4.3.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab4/' | relative_url }}#Fig_L4_3_Process_condition_settings_window)), čo zodpovedá 15-sekundovému prenosu z pece (alebo indukčných cievok) do nástroja. Nechajte predvolené hodnoty **Teploty okolia** **20** °C a **Koeficientu konvekcie****0,02** N/s/mm/°C a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí okno objektu. V tejto operácii sa bude spracovávať len jeden objekt, preto kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na definovanie obrobku.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab4_image0003.jpg' | relative_url }})

Okno nastavení prevádzkových podmienok

### Definovanie všeobecných údajov o obrobku

Nastavte teplotu na **1******232.** 22**°C a overte, či je typ objektu **Plast**, ako je znázornené v [Fig. L4.4.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab4/' | relative_url }}#Fig_L4_4_Workpiece_object_general_definition_window). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) vytvorte geometriu z primitívu.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab4_image0004.jpg' | relative_url }})

Okno so všeobecnou definíciou objektu obrobku

### Vytvorenie 3D primitívnej geometrie

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}), aby ste vytvorili obrobok. Zo zoznamu ikon vľavo vyberte **Valec**. Nastavte **priemer** (2R) obrobku na **127** mm a **výšku** (H) na **207,01** mm s polomerom rohu (r) **2,54** mm. Upozorňujeme, že smer výšky primitívu je Z. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) na vytvorenie geometrie. (Pozrite [Fig. L4.5.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab4/' | relative_url }}#Fig_L4_5_3D_geometry_primitive_window)) 

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab4_image0005.jpg' | relative_url }})

Okno s 3D geometrickými primitívami

Akonáhle bude geometria k dispozícii, v okne geometrie budú dostupné nástroje na prácu s geometriou, ako napríklad „Check“, „Fix“, „Scale“, „Reverse“ atď., ako je znázornené na obrázku [Fig. L4.6.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab4/' | relative_url }}#Fig_L4_6_Geometry_window_options)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab4_image0006.jpg' | relative_url }})

Možnosti okna „Geometria“

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka so sieťou.

### Vytvorenie siete pre obrobok

V okne stránky „Mesh“ zmeňte režim nastavení preprocesora na „Expert“ pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) (Prejsť do režimu Expert) na paneli nástrojov. Režim „Expert“ ponúka viac možností pre podrobné nastavenia. Nastavte **Cieľový počet prvkov** na **20 000** prvkov a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). Vyberte typ siete **Absolute**, nastavte veľkosť prvkov siete na hodnotu **2,5**, ako je znázornené na obrázku [Fig. L4.7.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab4/' | relative_url }}#Fig_L4_7_Advanced_mesh_settings), aby sa pri premenovaní siete použil typ Absolute. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) priraďte materiál.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab4_image0007.jpg' | relative_url }})

Pokročilé nastavenia mriežky

### Načítanie a priradenie materiálu k obrobku

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať materiál z knižnice), ako je znázornené na obrázku [Fig. L1.16.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab4/' | relative_url }}#Fig_L1_16_Reversing_the_direction_of_the_geometry_orientation). Vyberte kategóriu **Steel_at_Extended_Temperatures**, potom **AISI-8620[1550-2200F(850 -1200C)]** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}).

Kliknite na **AISI-8620[1550–2200 °F (850–1200 °C)]**, aby ste obrobku priradili materiál. Potvrďte priradenie v strome objektov, kde sa názov materiálu zobrazí vedľa položky „materiál“ a v texte „Informácie o priradenom materiáli“ nad zoznamom materiálov, ako je znázornené na obrázku [Fig. L1.11.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab4/' | relative_url }}#Fig_L1_11_Object_Material_Assigning_window). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste definovali okrajové podmienky.

### Definovanie okrajovej podmienky

Pre obrobok definujte okrajovú podmienku „Výmena tepla s okolím“. Predvolené okrajové podmienky sú priradené; ak nie, kliknite na vetvu „Výmena tepla s okolím“. Vyberte celý povrch obrobku kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_select_all_icon.jpg' | relative_url }}) (Vybrať všetko) v okne „Výber uzlov“ (vľavo na paneli nástrojov pod prehliadačom). Po výbere uzlov kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) (pridať okrajovú podmienku). Kliknite na vetvu „Defined“, aby ste sa uistili, že je okrajová podmienka definovaná. (Pozri [Fig. L4.8.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab4/' | relative_url }}#Fig_L4_8_Confirming_boundary_condition_definition_by_selecting_Defined_branch))

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab4_image0008.jpg' | relative_url }})

Potvrdenie definície okrajovej podmienky výberom vetvy „Defined“

Kliknite na vetvu **Krok** v strome operácií, aby ste definovali ovládacie prvky kroku

### Nastavenie ovládacích prvkov krokov

Prepnite do režimu s návodom ![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }}), nastavte **Počet krokov** na **60**, **Krok****prírastok** na **5** krokov a definíciu kroku riešenia **Čas** na **0,25** **sek** pre operáciu prenosu tepla (pozri [Fig. L4.9.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab4/' | relative_url }}#Fig_L4_9_Guided_mode_Step_controls)).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab4_image0009.jpg' | relative_url }})

Ovládacie prvky v režime s navádzaním

### Vytvoriť databázu a odoslať na simuláciu

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) a skontrolujte informácie o overovaní údajov. Uistite sa, že v definícii údajov nie sú žiadne chyby. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}). Uistite sa, že bola vygenerovaná databáza, a spustite simuláciu.

Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) MO Mode (nad stromom operácií) spustíte simuláciu.

Kliknutím na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno „Možnosti spustenia“. Pomocou predvolenej možnosti **Pokračovať v spustení** vyberte možnosť „**Pokračovať od posledného kroku**“, potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

Simuláciu môžete sledovať v oknách „Simulačná grafika“ a „Simulačné správy“. V poslednom riadku súboru správ a protokolu sa zobrazí informácia, že simulácia bola dokončená. Kliknutím na tlačidlo „![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode“ si môžete prezrieť výsledky.

### Prehľad výsledkov leteckého prepravy

Po dokončení simulácie skontrolujte teplotné straty v obrobku, najmä v rohoch.

Kliknite na ikonu stavovej premennej ![]({{ '/assets/icons/post_icons/mo_temp_sv.jpg' | relative_url }}) (Zobraziť teplotu) v nástrojoch grafu. Kliknite pravým tlačidlom myši s kurzorom nad farebným pruhom a vyberte možnosť „Typ farebného pruhu / Teplota“, čím získate realistickejší výber farieb, ako je znázornené na obrázku [Fig. L4.10.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab4/' | relative_url }}#Fig_L4_10_Temperature_State_variable_plot_with_color_bar_type_Temperature).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab4_image0010.jpg' | relative_url }})

Graf premennej „Teplota“ s farebným pruhom typu „Teplota“

Kliknite na ikonu **Súhrn**![]({{ '/assets/icons/post_icons/mo_summary_icon.jpg' | relative_url }}). Prejdite na kartu ![]({{ '/assets/icons/post_icons/mo_thermal_sv_icon.jpg' | relative_url }}) (Tepelné) a zadajte ![]({{ '/assets/icons/post_icons/mo_plot_button.jpg' | relative_url }}) maximálne a minimálne teplotné hodnoty. Tým sa v každom kroku vykreslia najvyššia a najnižšia teplota kdekoľvek v obrobku, ako je znázornené na obrázku [Fig. L4.11.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab4/' | relative_url }}#Fig_L4_11_Temperature_summary_plot)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab4_image0011.jpg' | relative_url }})

Graf s prehľadom teplôt

Kliknutím na tlačidlo režimu ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}) prejdete do režimu Pre, aby ste mohli pokračovať v postupnom tvárnení v režime [Lab 5.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab4/' | relative_url }}#Lab5_3D_Non-isothermal_Forming_operation)

Kliknite na [Gear Blank SI Lab 5]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab5/' | relative_url }}), aby ste pokračovali v operácii postupného tvárnenia.

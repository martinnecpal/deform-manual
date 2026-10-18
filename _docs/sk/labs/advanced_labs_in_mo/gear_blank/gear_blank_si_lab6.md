---
lang: sk
title: "Polotovar na ozubené kolesá SI Lab 6"
---

# Laboratórna práca č. 6. Mechanický lis

### Duplikát projektu

Spustite program DEFORM a vytvorte nový projekt s názvom **Gear_m**.

Pridajte operáciu 3D tvárnenia a v ponuke Súbor kliknite na ![]({{ '/assets/icons/pre_icons/mo_import_icon.jpg' | relative_url }}) (Importovať databázu). Otvorte súbor „**Gear.DB**“. Vyberte prvý krok tretej operácie (Kovanie) a kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}).

### Definovanie ovládacích prvkov simulácie

V tomto cvičení ukážeme, ako nastaviť ovládacie prvky mechanického lisu pre neizotermickú simuláciu s výpočtami prenosu tepla pre obrobok aj lisovacie formy. V nastaveniach simulácie je políčko „Prenos tepla“ štandardne zaškrtnuté; ak nie je, zaškrtnite ho.

### Definovanie okrajovej podmienky pre obrobok

Kliknite na vetvu **Okrajová podmienka obrobku** a pre celý objekt definujte okrajovú podmienku „Výmena tepla s okolím“ pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_select_all_icon.jpg' | relative_url }}) (Vybrať všetko), ak ju systém automaticky nepriradil.

### Definícia prenosu tepla s hornou matricou

Kliknite na vetvu **Top die** v prevádzkovom strome a nastavte teplotu na **148,889** °C.

Oba nástroje prepojíme, aby sme simulovali teplotu matrice. V strome operácií kliknite na vetvu **Top****die** Mesh, nastavte **20000** prvkov a kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}).

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), potom na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať materiál z knižnice) a vyberte kategóriu **Die_material**, následne **AISI-H-13**. Načítaný materiál priraďte tak, že ho vyberiete zo zoznamu materiálov.

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a nastavte okrajovú podmienku „Výmena tepla s okolím“ pre celý objekt s výnimkou hornej plochy, ako je znázornené na obrázku [Fig. L6.1.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab6/' | relative_url }}#Fig_L6_1_Top_die_Heat_exchange_with_environment_boundary_condition_surfaces)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab6_image0001.jpg' | relative_url }})

Horná matrica – Výmena tepla s povrchmi okrajových podmienok prostredia

### Definícia mechanického lisu

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste zmenili ovládacie prvky pohybu hornej matrice. Z horného riadka prepínačov vyberte možnosť „Mechanický lis“. Zadajte:

\- **Celkový zdvih** : **304,8** [ide o celkový zdvih piesta od hornej mŕtvej polohy po dolnú mŕtvu polohu]

\- **Zdvih kovania**: **40,005** [toto predstavuje zdvih hornej matrice z aktuálnej polohy do dolnej úvrate]

\- **Cyklov/s** : **1,0** [to zodpovedá otáčkam zotrvačníka 60 ot./min] (pozri [Fig. L6.2.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab6/' | relative_url }}#Fig_L6_2_Mechanical_press_movement_definition_for_top_die))

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab6_image0002.jpg' | relative_url }})

Definícia pohybu mechanického lisu pre hornú maticu

### Definícia prenosu tepla pomocou spodnej matrice

Podobne ako v definícii tepelného prenosu hornej formy nastavte počiatočnú teplotu spodnej formy na **148,889** °C a sieť s **50 000** prvkami. (Pozri [section 6.4 Define Heat transfer with Top die]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab6/' | relative_url }}#6_4_Define_Heat_transfer_with_Top_die))

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a zo zoznamu materiálov vyberte **AISI-H-13**, aby ste priradili materiál. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste definovali okrajovú podmienku „Výmena tepla s okolím“, a vyberte všetky povrchy okrem spodného povrchu, ako je znázornené v [Fig. L6.3.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab6/' | relative_url }}#Fig_L6_3_Bottom_die_Heat_exchange_with_environment_boundary_condition_surfaces)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab6_image0003.jpg' | relative_url }})

Spodná forma – Výmena tepla s povrchmi okrajových podmienok prostredia

Kliknite na položku **Kontakt** v strome operácií, aby ste definovali vzťah medzi objektmi.

### Definícia vzťahov medzi objektmi

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) pre ľubovoľný vzťah a zadajte **koeficient prenosu tepla** s hodnotou **11** N/s/mm/C. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) pridajte ďalšie vzťahy. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) (Tolerancia) a následne na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) (v spodnej časti okna medziobjektových vzťahov). Mali by ste vidieť kontaktné uzly na obrobku, kde bol kontakt vygenerovaný. Pozrite si [Fig. L6.4.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab6/' | relative_url }}#Fig_L6_4_Top_and_bottom_die_contact_with_workpiece), kde je zobrazené, ako vyzerá okno „Medziobjektové“ a ako sa generovanie kontaktu zobrazuje v grafickom okne.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab6_image0004.jpg' | relative_url }})

Horná a spodná matrica prichádzajú do styku s obrobkom

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste nastavili ovládacie prvky zastavenia.

### Definovanie ovládacích prvkov zastavenia a simulácie

Pridajte kritérium zastavenia, aby sa simulácia zastavila, keď zdvih dosiahne hodnotu -**304,8** (maximálny zdvih matrice) v poli smeru Y, ako je znázornené na stránke [Fig. L6.5.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab6/' | relative_url }}#Fig_L6_5_Maximum_primary_die_displacement_stopping_controls), a zrušte zaškrtnutie ovládacích prvkov zastavenia „Vzdialenosť medzi objektmi“. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Krok“.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab6_image0005.jpg' | relative_url }})

Ovládacie prvky na zastavenie maximálneho posunu primárnej matrice

Zachovajte nastavenia ovládacích prvkov simulácie importované z databázy a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste skontrolovali a vygenerovali databázu.

### Vytvorte databázu a spustite simuláciu

Zaškrtnite políčko „Skontroluj a vygeneruj databázu“ a kliknite na tlačidlo „Režim ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }})“ (nad stromom operácií), aby ste spustili simuláciu.

Spustite simuláciu a po jej dokončení kliknite na tlačidlo „![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode“, aby ste si prezreli výsledky.

### Výsledky hodnotenia

V postprocesore MO prejdite na graf „load-stroke“ ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) a vyneste graf rýchlosti razníka (rýchlosť na osi Y) v závislosti od zdvihu.

Zaznačte závislosť zaťaženia od času pre primárnu maticu.

* * *

Voliteľné cvičenie – ak to čas dovolí

\- Porovnajte maximálne zaťaženie so simuláciou založenou na aproximácii konštantnej rýchlosti.

\- Porovnajte dobu trvania procesu so simuláciou, pri ktorej sa používa aproximácia s konštantnou rýchlosťou.

\- Spustite úlohu **Gear** znovu so sieťovým modelom nástrojov a zaškrtnutím políčka **Prenos tepla**. Použite rovnaké vstupné údaje pre sieťovú modeláciu matrice, materiál a teplotu. Porovnajte teplotu na stredovej ploche spodnej matrice medzi aproximáciou s konštantnou rýchlosťou a týmto prípadom s využitím modelu mechanického lisu.

\- Exportujte údaje z grafu a importujte ich do programu Excel alebo iného programu. Kliknutím pravým tlačidlom myši na ľubovoľný graf a výberom možnosti „Exportovať údaje z grafu“ môžete vytvoriť výstupný textový súbor.

* * *

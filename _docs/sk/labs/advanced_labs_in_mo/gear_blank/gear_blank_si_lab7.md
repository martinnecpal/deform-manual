---
lang: sk
title: "Polotovar na ozubené kolesá – laboratórna úloha č. 7"
---

# Laboratórna práca č. 7. Kladivo

### Pridanie projektu

Spustite program DEFORM a vytvorte nový projekt s názvom **Gear_h**.

Pridajte operáciu **3D Forming Express** a v ponuke Súbor kliknite na položku ![]({{ '/assets/icons/pre_icons/mo_import_icon.jpg' | relative_url }}) (Importovať databázu). Otvorte súbor „**Gear.DB**“. Vyberte prvý krok tretej operácie (Kovanie) a kliknite na položku ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}).

### Definovanie nastavení procesu

V tomto cvičení ukážeme, ako nastaviť ovládacie prvky programu Hammer pre neizotermickú simuláciu s výpočtami prenosu tepla pre obrobok aj lisovacie formy. Ako typ procesu vyberte **Kovanie za tepla** (pozri [Fig. L7.1.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab7/' | relative_url }}#Fig_L7_1_Process_settings_selection_window)). Tým sa aktivuje režim prenosu tepla.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab7_image0001.jpg' | relative_url }})

Okno výberu nastavení procesu

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a vyberte možnosť **Vypočítať teplotu v obrobku a formách** (pozri [Fig. L7.2.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab7/' | relative_url }}#Fig_L7_2_Temperature_calculation_settings_window)). Tým sa pridajú okná so sieťou a okrajovými podmienkami pre formy.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab7_image0002.jpg' | relative_url }})

Okno nastavení výpočtu teploty

### Definovanie okrajovej podmienky pre obrobok

Kliknite na vetvu **Okrajová podmienka obrobku** a pre celý objekt definujte okrajovú podmienku „Výmena tepla s okolím“ pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_select_all_icon.jpg' | relative_url }}) (Vybrať všetko), ak systém túto podmienku nepriradil automaticky.

### Vysvetlenie prenosu tepla pomocou hornej matrice

Kliknite na vetvu **Top die** v prevádzkovom strome a nastavte teplotu na **148,889 °****C**.

Vytvorte sieť pre nástroje na simuláciu teploty foriem. Kliknite na vetvu **Mesh** v strome operácií a nastavte **20000** prvkov pomocou možnosti **User defined**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}).

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), potom na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať materiál z knižnice) a vyberte kategóriu **Die_material**, následne **AISI-H-13**. Načítaný materiál priraďte tak, že ho vyberiete zo zoznamu materiálov.

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a nastavte okrajovú podmienku „Výmena tepla s okolím“ pre celý objekt s výnimkou hornej plochy, ako je znázornené na obrázku [Fig. L7.3.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab7/' | relative_url }}#Fig_L7_3_Top_die_Heat_exchange_with_environment_boundary_condition_surfaces)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab7_image0003.jpg' | relative_url }})

Horná matrica – Výmena tepla s povrchmi okrajových podmienok prostredia

### Nastavenie ovládania kladiva

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste zmenili ovládacie prvky pohybu hornej matrice. Z horného riadku prepínačov vyberte možnosť **Hammer**. (Pozri [Fig. L7.4.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab7/' | relative_url }}#Fig_L7_4_Mechanical_press_movement_definition_for_top_die)) Zadajte:

\- **Energia** : 56 492 419,4 N-mm.

\- **Hmotnosť**: 4,37817126 N·s²/mm.

\- **Účinnosť**: 0,85 (85 %)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab7_image0004.jpg' | relative_url }})

Definícia pohybu mechanického lisu pre hornú matricu

Zaškrtnite políčko **Použiť tabuľku úderov** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) (Definovať) vedľa tohto políčka. Nastavte **doba zdržania** na **0,5** s pre úder 1 a pomocou tlačidla „No. Hits increment“ pridajte ďalšie 4 údery. Tým sa pridajú ďalšie 4 údery s rovnakými hodnotami, ako je zobrazené v [Fig. L7.5.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab7/' | relative_url }}#Fig_L7_5_Multiple_blow_definition_table). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) uzavrite definíciu viacerých úderov.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab7_image0005.jpg' | relative_url }})

Tabuľka definícií viacerých úderov

### Definícia prenosu tepla pomocou spodnej matrice

Podobne ako pri definícii tepelného prenosu hornej formy nastavte počiatočnú teplotu spodnej formy na **148,889** °**C** a nastavte **50 000** prvkov pomocou možnosti **Definované používateľom**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}).

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a zo zoznamu materiálov vyberte **AISI-H-13**, aby ste priradili materiál. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste definovali **hraničné podmienky výmeny tepla s okolím**, a vyberte všetky povrchy okrem spodného povrchu, ako je znázornené v [Fig. L7.6.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab7/' | relative_url }}#Fig_L7_6_Bottom_die_Heat_exchange_with_environment_boundary_condition_surfaces)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab7_image0006.jpg' | relative_url }})

Spodná forma – Výmena tepla s povrchmi okrajových podmienok prostredia

Kliknite na položku **Kontakt** v strome operácií, aby ste definovali vzťah medzi objektmi.

### Definícia vzťahov medzi objektmi

Vyberte tlačidlo **Užívateľsky definované kĺbové spojenie** a nastavte hodnotu šmykového trenia na 0,3 a koeficient tepelnej vodivosti na hodnotu **11**. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_generate_contact_nodes_label.jpg' | relative_url }}) vytvoríte kontakt s koeficientom tepelnej vodivosti a trením, ako je znázornené na obrázku [Fig. L7.7.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab7/' | relative_url }}#Fig_L7_7_Forming_express_contact_generation_window).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab7_image0007.jpg' | relative_url }})

Zobrazenie okna na rýchle vytvorenie kontaktu

Na obrobku by ste mali vidieť kontaktné body v miestach, kde došlo k vytvoreniu kontaktu. Na obrázku [Fig. L7.8.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab7/' | relative_url }}#Fig_L7_8_Top_and_bottom_die_contact_with_workpiece) si môžete pozrieť, ako vyzerá okno objektu „Inter“ a ako sa v grafickom okne zobrazuje vytvorenie kontaktu. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdete na stránku „Ovládacie prvky zastavenia“.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab7_image0008.jpg' | relative_url }})

Horná a spodná matrica prichádzajú do styku s obrobkom

### Primárny zdvih matrice

V poli „Celkový posun primárneho lisovacieho nástroja“ nastavte hodnotu 40 a zaškrtnite políčko „Presná hodnota“, potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste nastavili zastavovacie ovládacie prvky.

### Definovanie ovládacích prvkov zastavenia

Zachovajte vzdialenosť medzi ovládacími prvkami zastavenia, ktoré boli importované z databázy. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Simulačné ovládacie prvky“.

### Definovanie ovládacích prvkov simulácie

Pozrite si definíciu ovládacích prvkov krokov importovanú z databázy. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste skontrolovali a vygenerovali databázu.

### Vytvorenie databázy a spustenie simulácie

Zaškrtnite políčko „Skontrolovať a vygenerovať databázu“ a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }})Mode (nad stromom operácií), čím spustíte simuláciu.

Spustite simuláciu a po jej dokončení kliknite na tlačidlo „![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode“, aby ste si prezreli výsledky.

### Výsledky hodnotenia

V postprocesore MO prejdite na graf „load-stroke“ ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) a vyneste graf rýchlosti razníka (rýchlosť na osi Y) v závislosti od zdvihu pre prvú, tretiu a deviatu operáciu (z roletového menu v dolnej časti vyberte 1, 3 a 9). Pre každú z týchto tvárniacich operácií vyneste tiež graf energie v závislosti od času.

Zaznačte priebeh zaťaženia osi Y v závislosti od času pre celý proces (všetky operácie). Zapnite kontakt s čipom a všimnite si mierne nedoplnenie.

* * *

Voliteľné cvičenie – ak to čas dovolí

\- Porovnajte maximálne zaťaženie so simuláciou, pri ktorej sa používa aproximácia s konštantnou rýchlosťou.

\- Porovnajte dobu trvania procesu so simuláciou s použitím aproximácie s konštantnou rýchlosťou.

\- Znovu spustite úlohu týkajúcu sa ozubeného kolesa s použitím siete nástrojov a nastavení výpočtu teploty v obrobku a formách (neizotermický výpočet). Použite rovnaké vstupné údaje pre sieť formy, materiál a teplotu. Porovnajte teplotu na stredovej ploche spodnej formy medzi aproximáciou s konštantnou rýchlosťou a týmto prípadom s využitím modelu kladiva.

\- Exportujte údaje z grafu a importujte ich do programu Excel alebo iného programu. Môžete kliknúť pravým tlačidlom na ľubovoľný graf a vybrať možnosť „Exportovať údaje z grafu“, čím vytvoríte výstupný textový súbor.

* * *

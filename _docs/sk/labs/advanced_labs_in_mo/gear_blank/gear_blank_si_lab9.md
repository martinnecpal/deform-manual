---
lang: sk
title: "Polotovar na ozubené kolesá SI Lab 9"
---

# Laboratórna práca č. 9. Hydraulický lis

### Duplikovaný projekt

Spustite program DEFORM a vytvorte nový projekt s názvom **Gear_p**.

Pridajte operáciu **3D****Forming** a v ponuke Súbor kliknite na ![]({{ '/assets/icons/pre_icons/mo_import_icon.jpg' | relative_url }}) (Importovať databázu). Otvorte súbor „**Gear.DB**“. Vyberte prvý krok tretej operácie (Kovanie) a kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}).

### Definovanie ovládacích prvkov simulácie

V tomto cvičení ukážeme, ako nastaviť ovládacie prvky hydraulického lisu pre neizotermickú simuláciu s výpočtami prenosu tepla pre obrobok aj lisovacie formy. V časti „Simulation controls“ skontrolujte stav začiarkavacieho políčka **Heat****Transfer**; ak nie je začiarknuté, začiarknite ho.

### Definovanie okrajových podmienok pre obrobok

Kliknite na vetvu **Okrajová podmienka obrobku** a definujte **Okrajovú podmienku výmeny tepla s okolím** pre celý objekt pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_select_all_icon.jpg' | relative_url }}) (Vybrať všetko), ak systém túto podmienku nepriradil automaticky.

### Vysvetlenie prenosu tepla pomocou hornej matrice

Kliknite na vetvu „Top die“ v prevádzkovom strome a nastavte teplotu na **148,889** **°C**.

Oba nástroje prepojíme, aby sme simulovali teplotu lisovacej formy. Kliknite na vetvu **Mesh** (sieť) „Top Die“ v stromovej štruktúre operácií a nastavte **20000** prvkov. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), potom na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať materiál z knižnice) a vyberte kategóriu **Die_material**, následne **AISI-H-13**. Načítaný materiál priraďte tak, že ho vyberiete zo zoznamu materiálov.

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a nastavte okrajovú podmienku „Výmena tepla s okolím“ pre celý objekt s výnimkou hornej plochy, ako je znázornené na obrázku [Fig. L9.1.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab9/' | relative_url }}#Fig_L9_1_Top_die_Heat_exchange_with_environment_boundary_condition_surfaces)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab6_image0001.jpg' | relative_url }})

Horná matrica – výmena tepla s povrchmi okrajových podmienok prostredia

### Definícia hydraulického lisu

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste zmenili nastavenia pohybu hornej matrice. V hornom riadku prepínačov vyberte možnosť **Hydraulický** lis. Zadajte:

\- **Rýchlosť** (konštantná): **63,5** mm/s (pozri [Fig. L9.2.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab9/' | relative_url }}#Fig_L9_2_Hydraulic_press_movement_definition_main_tab))

\- **Skontrolujte****limit výkonu****** a zadajte **údaje** pomocou tlačidla **![]({{ '/assets/icons/pre_icons/mo_define..._button2.jpg' | relative_url }})**, ako je znázornené nižšie [Fig. L9.3.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab9/' | relative_url }}#Fig_L9_3_Power_limit_definition)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab9_image0002.jpg' | relative_url }})

Hlavná záložka s definíciou pohybu hydraulického lisu

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab9_image0003.jpg' | relative_url }})

Definícia výkonového limitu

Zadajte limit zastavenia (maximálne zaťaženie primárnej matrice) v smere Y v hodnote **17792880** N. Vyberte teda kartu ovládacích prvkov **Dwell** a v poli **Y** nastavte **Maximálne****zaťaženie** na hodnotu 17792880 N, ako je znázornené v [Fig. L9.4.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab9/' | relative_url }}#Fig_L9_4_Hydraulic_press_stopping_load_defined_in_dwell_controls_tab)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab9_image0004.jpg' | relative_url }})

Zastavovacie zaťaženie hydraulického lisu definované na karte „Ovládanie zdržania“

### Vysvetlite prenos tepla pomocou spodnej matrice

Podobne ako v definícii prenosu tepla pre hornú formu nastavte počiatočnú teplotu spodnej formy na **148,889** °C a sieť s **50 000** prvkami. (Pozri [Section 6.4 Define Heat transfer with Top die]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab6/' | relative_url }}#Fig_L6_4_Top_and_bottom_die_contact_with_workpiece))

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a zo zoznamu materiálov vyberte **AISI-H-13**, aby ste priradili materiál. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste definovali okrajovú podmienku „Výmena tepla s okolím“, a vyberte všetky povrchy okrem spodného povrchu, ako je znázornené na obrázku [Fig. L9.5.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab9/' | relative_url }}#Fig_L9_5_Bottom_die_Heat_exchange_with_environment_boundary_condition_surfaces)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab6_image0003.jpg' | relative_url }})

Spodná forma – Výmena tepla s povrchmi okrajových podmienok prostredia

Kliknite na položku **Kontakt** v strome operácií, aby ste definovali vzťah medzi objektmi.

### Definícia vzťahov medzi objektmi

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) pre ľubovoľný vzťah a pridajte **koeficient prenosu tepla** s hodnotou **11** N/s/mm/C. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}), aby ste pridali ďalšie vzťahy. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) (Tolerancia) a následne na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) (v dolnej časti okna medzi objektmi). Mali by ste vidieť kontaktné uzly na obrobku, kde bol kontakt vygenerovaný. Pozrite si [Fig. L9.6.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab9/' | relative_url }}#Fig_L9_6_Top_and_bottom_die_contact_with_workpiece), kde uvidíte, ako vyzerá okno Inter object a ako sa generovanie kontaktu zobrazuje v grafickom okne.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab6_image0004.jpg' | relative_url }})

Horná a spodná matrica prichádzajú do styku s obrobkom

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste nastavili ovládacie prvky na zastavenie.

### Nastavenie ovládacích prvkov zastavenia a simulácie

Obmedzenie zastavenia, ktoré určuje maximálne zaťaženie primárneho lisovacieho nástroja (**17792880** N) definované v nastaveniach pohybu primárneho lisovacieho nástroja, sa premieta do obmedzenia zastavenia. **Zrušte zaškrtnutie** obmedzenia zastavenia **Vzdialenosť medzi lisovacími nástrojmi** importovaného z databázy.

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a zachovajte definíciu ovládacích prvkov krokov importovanú z databázy.

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste skontrolovali a vygenerovali databázu.

### Vytvoriť databázu a spustiť simuláciu

Zaškrtnite políčko „Skontrolovať a vygenerovať databázu“ a kliknite na tlačidlo „Režim ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }})“ (nad stromom operácií), čím spustíte simuláciu.

Spustite simuláciu a po jej dokončení kliknite na tlačidlo „![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode“, aby ste si prezreli výsledky.

### Výsledky hodnotenia

V postprocesore prejdite na graf ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) [Graph (load-stroke)] a znázornite rýchlosť hornej matrice (rýchlosť na osi Y) v závislosti od zdvihu.

Zobrazte graf závislosti zaťaženia Y na čase.

Všimnite si nárast teploty v dutine formy v blízkosti povrchu. 

* * *

Voliteľné cvičenie – ak to čas dovolí

\- Porovnajte maximálne zaťaženie so simuláciou, pri ktorej sa používa aproximácia s konštantnou rýchlosťou.

\- Porovnajte čas trvania procesu so simuláciou, pri ktorej sa používa aproximácia s konštantnou rýchlosťou.

\- Zopakujte výpočet problému **Gear** so sieťovým modelom nástrojov a zaškrtnutím políčka **Prenos tepla**. Použite rovnaké vstupné údaje pre sieťovú modeláciu matrice, materiál a teplotu. Porovnajte teplotu na stredovej ploche spodnej matrice medzi aproximáciou s konštantnou rýchlosťou a týmto prípadom s využitím modelu hydraulického lisu.

\- Exportujte údaje z grafu a importujte ich do programu Excel alebo iného programu. Môžete kliknúť pravým tlačidlom myši na ľubovoľný graf a vybrať možnosť **Exportovať údaje z grafu**, čím vytvoríte výstupný textový súbor.

* * *

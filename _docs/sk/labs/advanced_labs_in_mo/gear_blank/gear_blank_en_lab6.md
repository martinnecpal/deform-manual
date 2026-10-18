---
lang: sk
title: "Polotovar na ozubené kolesá – EN, laboratórna úloha č. 6"
---

# Laboratórna práca č. 6: Mechanický lis

### Duplikát projektu

Spustite program DEFORM a vytvorte nový projekt s názvom **Gear_m**.

Pridajte operáciu 3D tvárnenia a v ponuke Súbor kliknite na ![]({{ '/assets/icons/pre_icons/mo_import_icon.jpg' | relative_url }}) (Importovať databázu). Otvorte súbor „**Gear.****DB**“. Vyberte prvý krok **tretej** (kovárskej) operácie a kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}).

### Definovanie ovládacích prvkov simulácie

V tomto cvičení ukážeme, ako nastaviť ovládacie prvky mechanického lisu pre neizotermickú simuláciu s výpočtami prenosu tepla pre obrobok aj lisovacie formy. V okne „Simulation controls“ je políčko „Heat Transfer“ štandardne zaškrtnuté; ak nie je, **zaškrtnite** políčko **Heat****Transfer**.

### Definovanie okrajových podmienok pre obrobok

Kliknite na vetvu **Obrobok****Okrajová****podmienka** a pre celý objekt definujte okrajovú podmienku „Výmena tepla s okolím“ pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_select_all_icon.jpg' | relative_url }}) (Vybrať všetko), ak ju systém automaticky nepriradil.

### Vysvetlite prenos tepla pomocou hornej matrice

Kliknite na vetvu **Top****die** v prevádzkovom strome a nastavte teplotu na **300** °F.

Oba nástroje prepojíme, aby sme simulovali teplotu matrice. Kliknite na vetvu **Top****die****Mesh** v strome operácií, nastavte **20000** prvkov a kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}).

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), potom na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať materiál z knižnice) a vyberte kategóriu **Die_material**, následne **AISI-H-13**. Načítaný materiál priraďte tak, že ho vyberiete zo zoznamu materiálov.

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a nastavte okrajovú podmienku „Výmena tepla s okolím“ pre celý objekt s výnimkou hornej plochy, ako je znázornené na obr. L6.1.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab6_image0001.jpg' | relative_url }})

Horná forma – výmena tepla s povrchmi okrajových podmienok prostredia

### Definícia mechanického lisu

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste zmenili ovládacie prvky pohybu hornej matrice. Z horného riadku prepínačov vyberte možnosť **Mechanický****lis**. Zadajte:****

**\- Celkový zdvih** : **12,0****** [toto predstavuje celkový zdvih piestu od hornej mŕtvej polohy po dolnú mŕtvu polohu]****

**\- Zdvih kováčskej** : **1,575** [toto predstavuje zdvih hornej matrice od aktuálnej polohy po dolný mŕtvy bod]

**-****Cyklov/s** : **1,0** [to zodpovedá otáčkam zotrvačníka 60 ot./min] (pozri obr. L6.2.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab6_image0002.jpg' | relative_url }})

Definícia pohybu mechanického lisu pre hornú matricu

### Definícia prenosu tepla pomocou spodnej formy

Podobne ako pri definícii prenosu tepla pre hornú formu nastavte počiatočnú teplotu spodnej formy na **300** °F a sieť s **50 000** prvkami. (Pozri časť 6.4 Definícia prenosu tepla pre hornú formu)

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a zo zoznamu materiálov vyberte **AISI-H-13**, aby ste priradili materiál. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste definovali **hraničnú podmienku výmeny tepla s okolím**, a vyberte všetky povrchy okrem spodného povrchu, ako je znázornené na obr. L6.3.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab6_image0003.jpg' | relative_url }})

Spodná forma – Výmena tepla s povrchmi okrajových podmienok prostredia

Kliknite na položku **Kontakt** v strome operácií, aby ste definovali vzťah medzi objektmi.

### Definícia vzťahov medzi objektmi

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) pre ľubovoľný vzťah a pridajte **koeficient prenosu tepla** s hodnotou **0,004**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}), aby ste pridali ďalšie vzťahy. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) (Tolerancia) a následne na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) (v spodnej časti okna medziobjektových vzťahov). Mali by ste vidieť kontaktné uzly na obrobku, kde bol vygenerovaný kontakt. Pozrite si obr. L6.4., kde je zobrazené, ako vyzerá okno Medziobjektové a ako sa generovanie kontaktov zobrazuje v grafickom okne.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab6_image0004.jpg' | relative_url }})

Horná a spodná matrica prichádzajú do styku s obrobkom

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste nastavili ovládacie prvky zastavenia.

### Nastavenie ovládacích prvkov zastavenia a simulačného kroku

Pridajte **kritérium zastavenia**, aby sa simulácia zastavila, keď zdvih dosiahne hodnotu **12** (Max. zdvih matrice) v poli smeru **Y**, ako je znázornené na obr. L6.5, a **zrušte zaškrtnutie** kontrolných prvkov zastavenia **Vzdialenosť****medzi****objektmi**.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab6_image0005.jpg' | relative_url }})

Ovládacie prvky na zastavenie maximálneho posunu primárnej matrice

Zachovajte nastavenia **krokov****ovládacích prvkov** importované z databázy a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste skontrolovali a vygenerovali databázu.

### Vytvorenie databázy a spustenie simulácie

Zaškrtnite políčko „Skontrolovať a vygenerovať databázu“ a kliknite na tlačidlo „Režim ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }})“ (nad stromom operácií), čím spustíte simuláciu.

Spustite simuláciu a po jej dokončení kliknite na tlačidlo „![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode“, aby ste si prezreli výsledky.

### Výsledky hodnotenia

V postprocesore MO prejdite na graf „load-stroke“ ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) a vyneste graf rýchlosti razníka (rýchlosť na osi Y) v závislosti od zdvihu.

Zaznačte graf závislosti zaťaženia od času pre primárnu matricu.

* * *

Voliteľné cvičenie – ak to čas dovolí

\- Porovnajte maximálne zaťaženie so simuláciou, v ktorej sa používa aproximácia s konštantnou rýchlosťou.

\- Porovnajte čas trvania procesu so simuláciou, pri ktorej sa používa aproximácia s konštantnou rýchlosťou.

Zopakujte výpočet problému **Gear** so sieťou nástrojov a zaškrtnutím políčka **Prenos tepla**. Použite rovnaké vstupné údaje pre sieť matrice, materiál a teplotu. Porovnajte teplotu na stredovej ploche spodnej matrice medzi aproximáciou s konštantnou rýchlosťou a týmto prípadom s využitím modelu mechanického lisu.

\- Exportujte údaje z grafu a importujte ich do programu Excel alebo iného programu. Akýmkoľvek grafom môžete kliknúť pravým tlačidlom myši a vybrať možnosť „Exportovať údaje z grafu“, čím vytvoríte výstupný textový súbor.

* * *

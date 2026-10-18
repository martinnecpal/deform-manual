---
lang: sk
title: "Polotovar na ozubené kolesá SI Lab 8"
---

# Laboratórna práca č. 8. Šnekový lis

### Duplikovaný projekt

Spustite program DEFORM a vytvorte nový projekt s názvom **Gear_s**.

Pridajte operáciu 3D tvarovania a v ponuke Súbor kliknite na položku ![]({{ '/assets/icons/post_icons/mo_import_icon.jpg' | relative_url }}) (Importovať databázu). Otvorte súbor „**Gear.DB**“. Vyberte prvý krok tretej operácie (Kovanie) a kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}).

### Definovanie ovládacích prvkov simulácie

V tomto cvičení ukážeme, ako nastaviť ovládacie prvky šnekového lisu pre neizotermickú simuláciu s výpočtami prenosu tepla pre obrobok aj lisovacie formy. V časti „Simulation controls“ skontrolujte stav začiarkavacieho políčka „Heat Transfer“ a ak nie je začiarknuté, začiarknite ho.

### Definovanie okrajovej podmienky pre obrobok

Kliknite na vetvu **Okrajová podmienka obrobku** a pre celý objekt definujte okrajovú podmienku „Výmena tepla s okolím“ pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_select_all_icon.jpg' | relative_url }}) (Vybrať všetko), ak systém túto podmienku nepriradil automaticky.

### Vysvetlenie prenosu tepla s hornou matricou

Kliknite na vetvu „Top die“ v prevádzkovom strome a nastavte teplotu na **148,889** °C.

Oba nástroje prepojíme, aby sme simulovali teplotu matrice. V strome operácií kliknite na vetvu **Mesh** (Sieť) pre hornú matricu a nastavte **20 000** prvkov. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}).

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), potom na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať materiál z knižnice) a vyberte kategóriu **Die_material**, následne **AISI-H-13**. Načítaný materiál priraďte tak, že ho vyberiete zo zoznamu materiálov.

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a definujte okrajovú podmienku „Výmena tepla s okolitým prostredím“ pre celý objekt s výnimkou hornej plochy, ako je znázornené na obr. L8.1.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab6_image0001.jpg' | relative_url }})

Horná matrica – výmena tepla s povrchmi okrajových podmienok prostredia

### Definícia šnekového lisu

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste zmenili nastavenia pohybu hornej matrice. V hornom riadku prepínačov vyberte možnosť **Šnekový lis**. Zadajte:

\- **Energia**: 209021951,8 N-mm.

\- **Účinnosť**: 0,80 (80 %)

\- **Moment zotrvačnosti** : 8756325,007 N·mm·s²

\- **Rozstup vodiacich skrutiek**: 381 mm/otáč. (Pozri obr. L8.2.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab8_image0002.jpg' | relative_url }})

Definícia pohybu skrutkového lisu pre hornú matricu

### Definícia prenosu tepla pomocou spodnej formy

Podobne ako v definícii tepelného prenosu hornej formy nastavte počiatočnú teplotu spodnej formy na **148,889** °C a sieť s **50 000** prvkami. (Pozri [Section 6.4 Define Heat transfer with Top die]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab6/' | relative_url }}#Fig_L6_4_Top_and_bottom_die_contact_with_workpiece))

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a zo zoznamu materiálov vyberte **AISI-H-13**, aby ste priradili materiál. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste definovali okrajovú podmienku „Výmena tepla s okolím“, a vyberte všetky povrchy okrem spodného povrchu, ako je znázornené na obr. L8.3.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab6_image0003.jpg' | relative_url }})

Spodná forma – Výmena tepla s povrchmi okrajových podmienok prostredia

Kliknite na položku **Kontakt** v strome operácií, aby ste definovali vzťah medzi objektmi.

### Definícia vzťahov medzi objektmi

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) pre ľubovoľný vzťah a zadajte koeficient prenosu tepla **11**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}), aby ste pridali ďalšie vzťahy. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) (Tolerancia) a následne na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) (v spodnej časti okna medzi objektmi). Mali by ste vidieť kontaktné uzly na obrobku, kde bol vytvorený kontakt. Pozrite si obr. L8.4., kde je znázornený vzhľad okna „Inter object“ a zobrazenie vytvorených kontaktov v grafickom okne.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab6_image0004.jpg' | relative_url }})

Horná a spodná matrica prichádzajú do kontaktu s obrobkom

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste nastavili ovládacie prvky zastavenia.

### Definovanie ovládacích prvkov zastavenia a simulácie

Udržujte vzdialenosť medzi ovládacími prvkami zastavenia matrice importovanými z databázy.

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a zachovajte definíciu ovládacích prvkov krokov importovanú z databázy.

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste skontrolovali a vytvorili databázu.

### Vytvorenie databázy a spustenie simulácie

Zaškrtnite políčko „Skontrolovať a vygenerovať databázu“ a kliknite na tlačidlo „Režim ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }})“ (nad stromom operácií), čím spustíte simuláciu.

Spustite simuláciu a po jej dokončení kliknite na tlačidlo „![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode“, aby ste si prezreli výsledky.

### Výsledky hodnotenia

V postprocesore MO prejdite na graf [Graph (load-stroke)] a vyneste graf rýchlosti hornej matrice (rýchlosť Y) v závislosti od zdvihu pre druhú operáciu.

Zaznačte graf závislosti zaťaženia Y od času a závislosti energie od zdvihu.

Zapnite kontakt s matricou a všimnite si mierne vyprázdnenie, keď lisovi dochádza energia.

* * *

Voliteľné cvičenie – ak to čas dovolí

\- Porovnajte maximálne zaťaženie so simuláciou, pri ktorej sa používa aproximácia s konštantnou rýchlosťou.

\- Porovnajte čas trvania procesu so simuláciou, pri ktorej sa používa aproximácia s konštantnou rýchlosťou.

\- Spustite znovu výpočet problému **Gear** so sieťovým modelom nástrojov a zaškrtnite políčko **Heat****transfer**. Použite rovnaké vstupné údaje pre sieťovú modeláciu matrice, materiál a teplotu. Porovnajte teplotu na stredovej ploche spodnej matrice medzi aproximáciou s konštantnou rýchlosťou a týmto prípadom s využitím modelu skrutkového lisu.

\- Exportujte údaje z grafu a importujte ich do programu Excel alebo iného programu. Stačí kliknúť pravým tlačidlom myši na ľubovoľný graf a vybrať možnosť „Exportovať údaje z grafu“, čím vytvoríte výstupný textový súbor.

* * *

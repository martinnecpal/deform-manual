---
lang: sk
title: "Polotovar na ozubené kolesá – Lab 8 (EN)"
---

# Laboratórna úloha č. 8: Šnekový lis

### Duplikát projektu

Spustite program DEFORM a vytvorte nový projekt s názvom **Gear_s**.

Pridajte **operáciu 3D tvarovania** a v ponuke Súbor kliknite na položku ![]({{ '/assets/icons/pre_icons/mo_import_icon.jpg' | relative_url }}) (Importovať databázu). Otvorte súbor „**Gear****.****DB**“. Vyberte prvý krok tretej operácie (Kovanie) a kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}).

### Definovanie ovládacích prvkov simulácie

V tomto laboratórnom cvičení ukážeme, ako nastaviť ovládacie prvky šnekového lisu pre neizotermickú simuláciu s výpočtami prenosu tepla pre obrobok aj pre lisovacie formy. V časti **Ovládacie prvky simulácie** skontrolujte stav **zaškrtávacieho políčka Prenos tepla**; ak nie je zaškrtnuté, zaškrtnite ho.

### Definovanie okrajovej podmienky pre obrobok

Kliknite na vetvu **Obrobok****Okrajová****podmienka** a definujte okrajovú podmienku „Výmena tepla s okolím“ pre celý objekt pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_select_all_icon.jpg' | relative_url }}) (Vybrať všetko), ak systém túto podmienku nepriradil automaticky.

### Vysvetlite prenos tepla pomocou hornej matrice

Kliknite na vetvu **Top****die** v prevádzkovom strome a nastavte teplotu na **300** °F.

Oba nástroje prepojíme, aby sme simulovali teplotu matrice. Kliknite na vetvu **Mesh** v strome operácií a nastavte **20000** prvkov. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}).

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), potom na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať materiál z knižnice) a vyberte kategóriu **Die_material**, následne **AISI-H-13**. Načítaný materiál priraďte tak, že ho vyberiete zo zoznamu materiálov.

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a definujte okrajovú podmienku **Výmena tepla s okolím** pre celý objekt s výnimkou hornej plochy, ako je znázornené na obr. L8.1.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab6_image0001.jpg' | relative_url }})

Horná matrica – výmena tepla s povrchmi okrajových podmienok prostredia

### Definícia šnekového lisu

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste zmenili ovládacie prvky pohybu hornej matrice. Z horného riadku rádiových tlačidiel vyberte možnosť **Skrutka**. Zadajte:

\- **Energia** : **1850** klb.-in.

\- **Účinnosť**: .**80** (80 %)

\- **Moment zotrvačnosti**: **77,5** klb.-in.-sec.^2

\- **Stúpanie vodiacich skrutiek**: **15** palcov na otáčku (pozri obr. L8.2.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab8_image0002.jpg' | relative_url }})

Definícia pohybu šnekového lisu pre hornú matricu

### Definícia prenosu tepla pomocou spodnej matrice

Podobne ako v definícii prenosu tepla pre hornú formu nastavte počiatočnú teplotu spodnej formy na **300°** F a sieť s **50 000** prvkami. (Pozri [Section 6.4 Define Heat transfer with Top die]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab6/' | relative_url }}#6_4_Define_Heat_transfer_with_Top_die))

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a zo zoznamu materiálov vyberte **AISI-H-13**, aby ste priradili materiál. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste definovali okrajovú podmienku „Výmena tepla s okolím“, a vyberte všetky povrchy okrem spodného povrchu, ako je znázornené na obr. L8.3.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab6_image0003.jpg' | relative_url }})

Spodná forma – Výmena tepla s povrchmi okrajových podmienok prostredia

Kliknite na položku **Kontakt** v strome operácií, aby ste definovali vzťah medzi objektmi.

### Definícia vzťahov medzi objektmi

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) pre ľubovoľný vzťah a zadajte **koeficient** **prenosu tepla** **0,004**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}), aby ste pridali ďalšie vzťahy. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) (Tolerancia) a následne na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) (v spodnej časti okna medzi objektmi). Mali by ste vidieť kontaktné uzly na obrobku, kde bol vygenerovaný kontakt. Pozrite si obr. L8.4., kde je znázornené, ako vyzerá okno Inter object a zobrazenie generovania kontaktu v grafickom okne.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab6_image0004.jpg' | relative_url }})

Horná a spodná matrica prichádzajú do styku s obrobkom

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste nastavili ovládacie prvky zastavenia.

### Nastavenie ovládacích prvkov zastavenia a simulačného kroku

Udržujte vzdialenosť medzi ovládacími prvkami zastavenia matrice importovanými z databázy.

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a zachovajte definíciu ovládacích prvkov krokov importovanú z databázy.

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste skontrolovali a vytvorili databázu.

### Vytvorenie databázy a spustenie simulácie

Zaškrtnite políčko „Skontrolovať a vygenerovať databázu“ a kliknite na tlačidlo „Režim ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }})“ (nad stromom operácií), čím spustíte simuláciu.

Spustite simuláciu a po jej dokončení kliknite na tlačidlo „![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode“, aby ste si prezreli výsledky.

### Výsledky hodnotenia

V postprocesore MO prejdite na graf ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) a znázornite maximálnu rýchlosť čipu (**rýchlosť Y**) v závislosti od **zdvihu** pre druhú operáciu.

Zaznačte graf závislosti zaťaženia Y na čase a závislosti energie na zdvihu.

Zapnite kontakt s matricou a všimnite si mierne vyprázdnenie, keď lisovi dochádza energia.

* * *

Voliteľné cvičenie – ak to čas dovolí

\- Porovnajte maximálne zaťaženie so simuláciou, pri ktorej sa používa aproximácia s konštantnou rýchlosťou.

\- Porovnajte čas trvania procesu so simuláciou, pri ktorej sa používa aproximácia konštantnej rýchlosti.

\- Znovu spustite úlohu **Gear** so sieťovou modeláciou nástrojov a zaškrtnutím políčka **Prenos tepla**. Použite rovnaké vstupné údaje pre sieťovú modeláciu matice, materiál a teplotu. Porovnajte teplotu na stredovej ploche spodnej matice medzi aproximáciou s konštantnou rýchlosťou a týmto prípadom s využitím modelu skrutkového lisu.

\- Exportujte údaje z grafu a importujte ich do programu Excel alebo iného programu. Akýmkoľvek grafom môžete kliknúť pravým tlačidlom myši a vybrať možnosť „Exportovať údaje z grafu“, čím vytvoríte výstupný textový súbor.

* * *

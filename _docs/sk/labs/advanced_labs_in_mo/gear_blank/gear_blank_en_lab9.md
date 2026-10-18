---
lang: sk
title: "Polotovar na ozubené kolesá EN Lab 9"
---

# Laboratórna práca č. 9: Hydraulický lis

### Duplicitný projekt

Spustite program DEFORM a vytvorte nový projekt s názvom **Gear_p**.

Pridajte **operáciu 3D tvarovania** a v ponuke Súbor kliknite na položku ![]({{ '/assets/icons/pre_icons/mo_import_icon.jpg' | relative_url }}) (Importovať databázu). Otvorte súbor „**Gear****.****DB**“. Vyberte prvý krok tretej operácie (Kovanie) a kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}).

### Definovanie ovládacích prvkov simulácie

V tomto laboratórnom cvičení ukážeme, ako nastaviť ovládacie prvky hydraulického lisu pre neizotermickú simuláciu s výpočtami prenosu tepla pre obrobok aj lisovacie formy. V časti **Ovládacie prvky simulácie** skontrolujte stav začiarkavacieho políčka **Prenos tepla**; ak nie je začiarknuté, začiarknite ho.

### Definovanie okrajovej podmienky pre obrobok

Kliknite na vetvu **Okrajová podmienka obrobku** a definujte okrajovú podmienku „Výmena tepla s okolím“ pre celý objekt pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_select_all_icon.jpg' | relative_url }}) (Vybrať všetko), ak systém túto podmienku nepriradil automaticky.

### Vysvetlenie prenosu tepla pomocou hornej formy

Kliknite na vetvu **Top****die** v prevádzkovom strome a nastavte teplotu na **300** °F.

Oba nástroje prepojíme, aby sme simulovali teplotu matrice. Kliknite na vetvu **Mesh** v strome operácií a nastavte **20000** prvkov. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}).

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), potom na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať materiál z knižnice) a vyberte kategóriu **Die_material**, následne **AISI-H-13**. Načítaný materiál priraďte tak, že ho vyberiete zo zoznamu materiálov.

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a nastavte **hraničnú podmienku výmeny tepla s okolím** pre celý objekt s výnimkou hornej plochy, ako je znázornené na obr. L9.1.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab6_image0001.jpg' | relative_url }})

Horná forma – výmena tepla s povrchmi okrajových podmienok prostredia

### Definícia hydraulického lisu

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste zmenili ovládacie prvky pohybu hornej matrice. Z horného riadku prepínačov vyberte možnosť **Hydraulický** lis. Zadajte:

\- **Rýchlosť** (konštantná): **2,5** palca/sek. (pozri obr. L9.2.)

\- Skontrolujte **limit výkonu** a zadajte údaje pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_define..._button2.jpg' | relative_url }}), ako je znázornené na obr. L9.3 nižšie.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab9_image0002.jpg' | relative_url }})

Hlavná záložka s definíciou pohybu hydraulického lisu

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab9_image0003.jpg' | relative_url }})

Definícia výkonového limitu

Zadajte **zastavovací limit** (maximálne zaťaženie primárnej matrice) **4000** klb v smere **Y**. Vyberte teda kartu **Dwell** a v poli **Y** nastavte **Maximálne****zaťaženie** na hodnotu **4000** klb, ako je znázornené na obr. L9.4.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab9_image0004.jpg' | relative_url }})

Zastavovacie zaťaženie hydraulického lisu definované na karte „Ovládanie zdržania“

### Definícia prenosu tepla pomocou spodnej matrice

Podobne ako v definícii prenosu tepla pre hornú formu nastavte počiatočnú teplotu **spodnej****formy** na **300** °F a sieť s **50 000** prvkami. (Pozri časť [ 6.4 Define Heat transfer with Top die]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab6/' | relative_url }}#6_4_Define_Heat_transfer_with_Top_die))

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a zo zoznamu materiálov vyberte **AISI-H-13**, aby ste priradili materiál. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste definovali **hraničnú podmienku výmeny tepla s okolím**, a vyberte všetky povrchy okrem spodného povrchu, ako je znázornené na obr. L9.5.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab6_image0003.jpg' | relative_url }})

Spodná forma – Výmena tepla s povrchmi okrajových podmienok prostredia

Kliknite na položku **Kontakt** v strome operácií, aby ste definovali vzťah medzi objektmi.

### Definícia vzťahov medzi objektmi

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) pre ľubovoľný vzťah a zadajte **koeficient prenosu tepla** s hodnotou **0,004**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}), aby ste pridali ďalšie vzťahy. Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) (Tolerancia) a následne na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) (v spodnej časti okna medzi objektmi). Mali by ste vidieť kontaktné uzly na obrobku, kde bol kontakt vygenerovaný. Pozrite si obr. L9.6., kde je zobrazené, ako vyzerá okno medzi objektmi a zobrazenie generovania kontaktu v grafickom okne.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab6_image0004.jpg' | relative_url }})

Horná a spodná matrica prichádzajú do styku s obrobkom

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste nastavili ovládacie prvky zastavenia.

### Nastavenie ovládacích prvkov zastavenia a simulačného kroku

V nastaveniach zastavenia sa zohľadňuje **maximálne****zaťaženie** **primárnej****matrice** (4000 klb), definované v nastaveniach pohybu primárnej matrice. Zrušte zaškrtnutie políčka „Vzdialenosť medzi nastaveniami zastavenia matrice“ importovaného z databázy.

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a zachovajte definíciu ovládacích prvkov krokov importovanú z databázy.

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste skontrolovali a vygenerovali databázu.

### Vytvorenie databázy a spustenie simulácie

Zaškrtnite políčko „Skontrolovať a vygenerovať databázu“ a kliknite na tlačidlo „Režim ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }})“ (nad stromom operácií), aby ste spustili simuláciu.

Spustite simuláciu a po jej dokončení kliknite na tlačidlo „![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode“, aby ste si prezreli výsledky.

### Výsledky hodnotenia

V postprocesore prejdite na graf ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) [Graf (zaťaženie – zdvih)] a vyneste graf rýchlosti hornej matrice (rýchlosť na osi Y) v závislosti od zdvihu.

Zobrazte graf závislosti zaťaženia Y na čase.

Všimnite si nárast teploty v dutine formy v blízkosti povrchu. 

* * *

Voliteľné cvičenie – ak to čas dovolí

\- Porovnajte maximálne zaťaženie so simuláciou, pri ktorej sa používa aproximácia s konštantnou rýchlosťou.

\- Porovnajte dobu trvania procesu so simuláciou, pri ktorej sa používa aproximácia s konštantnou rýchlosťou.

\- Znovu spustite výpočet problému **Gear** so sieťovým modelom nástrojov a zaškrtnutím políčka **Prenos tepla**. Použite rovnaké vstupné údaje pre sieťovú modeláciu matrice, materiál a teplotu. Porovnajte teplotu na stredovej ploche spodnej matrice medzi aproximáciou s konštantnou rýchlosťou a týmto prípadom s využitím modelu hydraulického lisu.

\- Exportujte údaje z grafu a importujte ich do programu Excel alebo iného programu. Akýmkoľvek grafom môžete kliknúť pravým tlačidlom myši a vybrať možnosť „Exportovať údaje z grafu“, čím vytvoríte výstupný textový súbor.

* * *

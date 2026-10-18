---
lang: sk
title: "Polotovar na ozubené kolesá EN Lab 7"
---

# Laboratórna práca č. 7: Kladivo

### Duplicitný projekt

Spustite program DEFORM a vytvorte nový projekt s názvom **Gear_h.**

Pridajte operáciu **3D Forming Express** a v ponuke Súbor kliknite na ![]({{ '/assets/icons/pre_icons/mo_import_icon.jpg' | relative_url }}) (Importovať databázu). Otvorte súbor „**Gear.****DB**“. Vyberte prvý krok **tretej** (kovanej) operácie a kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}).

### Definovanie nastavenia procesu

V tomto cvičení ukážeme, ako nastaviť ovládacie prvky programu Hammer pre neizotermickú simuláciu s výpočtami prenosu tepla pre obrobok aj pre lisovacie formy. Ako typ procesu teda vyberte **Horúce****kovanie** (pozri obr. L7.1.). Tým sa aktivuje režim prenosu tepla.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab7_image0001.jpg' | relative_url }})

Okno výberu nastavení procesu

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a vyberte možnosť **Vypočítať teplotu v obrobku a formách** (pozri obr. L7.2.). Tým sa pridajú okná so sieťou a okrajovými podmienkami pre formy.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab7_image0002.jpg' | relative_url }})

Okno nastavení výpočtu teploty

### Definovanie okrajovej podmienky pre obrobok

Kliknite na vetvu **Obrobok****Okrajové podmienky** a definujte **okrajovú podmienku výmeny tepla s okolím** pre celý objekt pomocou ikony ![]({{ '/assets/icons/pre_icons/mo_select_all_icon.jpg' | relative_url }}) (Vybrať všetko), ak systém túto podmienku nepriradil automaticky.

### Vysvetlenie prenosu tepla pomocou hornej matrice

Kliknite na vetvu **Top****die** v prevádzkovom strome a nastavte teplotu na **300** °F.

Oba nástroje prepojíme, aby sme simulovali teplotu formy. Kliknite na vetvu **Mesh** v strome operácií a nastavte **20000****prvkov** pomocou možnosti **User****defined**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}).

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), potom na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať materiál z knižnice) a vyberte kategóriu **Die_material**, následne **AISI-H-13**. Načítaný materiál priraďte tak, že ho vyberiete zo zoznamu materiálov.

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a definujte okrajovú podmienku „Výmena tepla s okolím“ pre celý objekt s výnimkou hornej plochy, ako je znázornené na obr. L7.3.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab7_image0003.jpg' | relative_url }})

Horná matrica – výmena tepla s povrchmi okrajových podmienok prostredia

### Nastavenie ovládania kladiva

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste zmenili ovládanie pohybu hornej matrice. Z horného riadku prepínačov vyberte položku **Hammer**. (Pozri obr. L7.4.) Zadajte:

\- **Energia** : **500** klb.-in.

\- **Hmotnosť**: **0,025** ~ (10 000 libier)

\- **Účinnosť**: **0,85** (85 %)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab7_image0004.jpg' | relative_url }})

Definícia pohybu mechanického lisu pre hornú matricu

Zaškrtnite políčko **Použiť tabuľku úderov** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) (Definovať) vedľa tohto políčka. Nastavte dobu zdržania na **0,5** s pre úder 1 a pomocou tlačidla **Počet úderov** pridajte ďalšie 4 údery. Tým sa pridajú ďalšie 4 údery s rovnakými hodnotami, ako je znázornené na obr. L7.5. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) uzavrite definíciu viacerých úderov.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab7_image0005.jpg' | relative_url }})

Tabuľka definícií viacerých úderov

### Definícia prenosu tepla pomocou spodnej matrice

Podobne ako pri definícii prenosu tepla pre hornú formu nastavte počiatočnú teplotu spodnej formy na **300** °F a počet prvkov mriežky na **50 000****prvkov**. (Pozri časť 7.4 Definícia prenosu tepla pre hornú formu)

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a zo zoznamu materiálov vyberte **AISI-H-13**, aby ste priradili materiál. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste definovali okrajovú podmienku „Výmena tepla s okolím“, a vyberte všetky povrchy okrem spodného povrchu, ako je znázornené na obr. L7.6.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab7_image0006.jpg' | relative_url }})

Spodná matrica – Výmena tepla s povrchmi okrajových podmienok prostredia

Kliknite na položku **Kontakt** v strome operácií, aby ste definovali vzťah medzi objektmi.

### Definícia vzťahov medzi objektmi

Vyberte tlačidlo **Užívateľsky definované kĺbové spojenie** a nastavte hodnotu trenia pri **šmyku** na **0,3** a koeficient tepelného vedenia na **0,004**. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_generate_contact_nodes_label.jpg' | relative_url }}) vytvoríte kontakt s koeficientom tepelného vedenia a trením, ako je znázornené na obr. L7.7.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab7_image0007.jpg' | relative_url }})

Zobrazenie okna na rýchle vytvorenie kontaktu

Na obrobku by ste mali vidieť kontaktné body v miestach, kde došlo k vytvoreniu kontaktu. Pozrite si obr. L7.8., kde je znázornené, ako vyzerá okno „Inter object“ a ako sa v grafickom okne zobrazuje vytvorenie kontaktu. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste definovali celkový primárny posun matrice.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab7_image0008.jpg' | relative_url }})

Horná a spodná matrica prichádzajú do styku s obrobkom

### Definovanie primárneho posuvu matrice

V poli „Celkový posuv primárneho lisovacieho nástroja“ nastavte hodnotu **1,575** a zaškrtnite **políčko „Presná hodnota“**, potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste nastavili zastavovacie ovládacie prvky.

### Definovanie ovládacích prvkov zastavenia a simulácie

Zachovajte vzdialenosť medzi ovládacími prvkami zastavenia, ktoré boli importované z databázy. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Definovanie ovládacích prvkov simulácie

Pozrite si definíciu ovládacích prvkov krokov importovanú z databázy. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na vygenerovanie databázy.

### Vytvorenie databázy a spustenie simulácie

Zaškrtnite políčko „Skontrolovať a vygenerovať databázu“ a kliknite na tlačidlo „Režim ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }})“ (nad stromom operácií), čím spustíte simuláciu.

Spustite simuláciu a po jej dokončení kliknite na tlačidlo „![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode“, aby ste si prezreli výsledky.

### Výsledky hodnotenia

V postprocesore MO prejdite na graf **load-stroke** ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) a znázornite rýchlosť razníka (rýchlosť na osi Y) v závislosti od zdvihu pre prvú, tretiu a deviatu operáciu (z roletového menu v spodnej časti vyberte 1, 3 a 9). Zaznačte tiež graf energie v závislosti od času pre každú z týchto operácií tvárnenia.

Zaznačte graf závislosti zaťaženia osi Y od času pre celý proces (všetky operácie). Zapnite kontakt s čipom a všimnite si mierne nedoplnenie.

* * *

Voliteľné cvičenie – ak to čas dovolí

\- Porovnajte maximálne zaťaženie so simuláciou, pri ktorej sa používa aproximácia s konštantnou rýchlosťou.

\- Porovnajte čas trvania procesu so simuláciou, pri ktorej sa používa aproximácia s konštantnou rýchlosťou.

\- Spustite úlohu **ozubeného kolesa** znovu so sieťou nástrojov a nastaveniami **Výpočet teploty v obrobku a formách (neizotermický)**. Použite rovnaké vstupné údaje pre sieť formy, materiál a teplotu. Porovnajte teplotu na stredovej ploche spodnej matrice medzi aproximáciou s konštantnou rýchlosťou a týmto prípadom s použitím modelu kladiva.

\- Exportujte údaje z grafu a importujte ich do programu Excel alebo iného programu. Môžete kliknúť pravým tlačidlom myši na ľubovoľný graf a vybrať možnosť „Exportovať údaje z grafu“, čím vytvoríte výstupný textový súbor.

* * *

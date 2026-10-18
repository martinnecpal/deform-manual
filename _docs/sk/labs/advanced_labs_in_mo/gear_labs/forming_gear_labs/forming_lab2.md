---
lang: sk
title: "Laboratórium tvarovania 2"
---

# Laboratórna úloha č. 2. Opakované spustenie sekvencie s väčším polotovarom

Kliknite na ikonu „New ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }})“ v ľavom hornom rohu rozhrania. Kliknutím na „![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }})“ zatvoríte aktuálny projekt a uložíte všetky zmeny.

Názov projektu nastavte na **Gear_LargerBillet**. Použite možnosť „Kopírovať existujúci projekt“ a vyhľadajte súbor PROBLEM **2DGear\2DGear.moproj** (pozri obr. L1.1.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab2_image0001.jpg' | relative_url }})

Nové okno projektu MO

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Systém skopíruje všetky informácie z pôvodného projektu do novej zložky **Gear_LargerBillet**.

Poznámka: Pri kopírovaní projektu prostredníctvom používateľského rozhrania sa automaticky premenujú viaceré súbory a priečinky v projekte. Je to oveľa prehľadnejšie ako kopírovanie a vkladanie problematického priečinka.

### Zmena veľkosti polotovaru

Kliknite na dlaždicu „Upset“ v editore operácií, aby ste vybrali prvú operáciu v projekte. Pre túto operáciu sa otvorí predspracovateľ (pozri obr. L2.2.). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí stránka „Geometria obrobku“.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab2_image0002.jpg' | relative_url }})

Výber prevádzky v režime „Upset“

### Vytvorenie novej geometrie pre obrobok

Zmeňte rozmery obrobku na polomer 2,5 in, výšku 8,267 in a rohy 0,1 in. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/mo_no_button.jpg' | relative_url }}) v okne „Odstrániť sieť“, aby ste odstránili sieť (pozri obr. L2.3.). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Sieť obrobku“.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab2_image0003.jpg' | relative_url }})

Vyskakovacie okno „Odstrániť sieť“

### Vytvorenie siete pre novú geometriu obrobku

Nastavte cieľový počet prvkov na **2000** a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) vygenerujte sieť pre obrobok. Klikajte na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka s nastavením polohy.

###  Polohovanie

Pomocou ![]({{ '/assets/icons/pre_icons/mo_automatic_positioning_button.jpg' | relative_url }}) nastavte polohu nástrojov voči obrobku. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Kontakt“.

### Vytvorenie kontaktu

Vytvorte kontakt pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Ovládacie prvky zastavenia.

### Ovládacie prvky na zastavenie

V časti „Ovládacie prvky zastavenia“ zmeňte hodnotu primárneho ovládacieho prvku zastavenia posuvu matice z 6 palcov na **6,5** palca. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Ovládacie prvky krokovania“.

### Ovládacie prvky krokov

Prejdite na položku „Krok“ a zmeňte **počet** krokov **simulácie** na **1000**. Takéto nastavenie vysokého počtu krokov zaručuje, že simulácii nedôjdu kroky a namiesto toho sa zastaví na základe definovaných kritérií ukončenia. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) vygenerujte stránku databázy

### Vytvoriť databázu

Databázu vytvoríte kliknutím na ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}).

Kliknutím na tlačidlo „MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode“ (nad stromom operácií) spustíte simuláciu.

### Spustenie a sledovanie simulácie

Keďže pri druhej operácii nie je potrebné meniť žiadne nastavenia, môžeme vytvoriť databázu a spustiť simuláciu.

Kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) a potom zrušte zaškrtnutie políčka „Odoslať úlohu do fronty simulácií“. Zrušením zaškrtnutia tejto možnosti sa úloha spustí na lokálnom počítači. Použite predvolenú možnosť **Začať od posledného záporného kroku**. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) spustíte simuláciu.

Po dokončení operácie prevrátenia program DEFORM automaticky načíta nové nástroje a spustí druhú operáciu.

### Prezrite si výsledky

Po dokončení simulácie kliknite na tlačidlo „MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode“, aby ste si prezreli výsledky.

Prejdite všetkými krokmi. Dajte pozor, aby diel úplne vyplnil dutinu formy.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab2_image0004.jpg' | relative_url }})

Tvar obrobku v poslednom kroku druhej operácie

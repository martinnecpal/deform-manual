---
lang: sk
title: "Vytvorenie Express Lab2"
---

# Laboratórna úloha č. 2. Opakované spustenie sekvencie s väčším polotovarom

  
Aby sme mohli spustiť výpočet s väčšou veľkosťou polotovaru, vytvoríme nový projekt na základe existujúceho projektu.

Kliknite na ikonu „New ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }})“ v ľavom hornom rohu rozhrania. Kliknutím na „![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }})“ zatvorte aktuálny projekt a uložte všetky zmeny. Názov projektu nastavte na **FE_Gear_LargerBillet.** Použite možnosť **Kopírovať existujúci projekt** a vyhľadajte súbor PROBLEM \**2DGear\FE_Gear.moproj** (pozri obr. L2.1.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab2_image0001.jpg' | relative_url }})

Nové okno projektu MO

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}). Systém skopíruje všetky informácie z pôvodného projektu do novej zložky **FE_Gear_LargerBillet**.

**Poznámka:** Pri kopírovaní projektu prostredníctvom používateľského rozhrania sa automaticky premenujú viaceré súbory a priečinky v projekte. Je to oveľa prehľadnejšie ako kopírovanie a vkladanie príslušného priečinka.

### Zmena veľkosti polotovaru

Kliknutím na dlaždicu „Upset“ v editore operácií vyberte prvú operáciu v projekte. Pre túto operáciu sa otvorí predspracovateľ (pozri obr. L2.2.). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Geometria obrobku“.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab2_image0002.jpg' | relative_url }})

Výber prevádzky v režime „Upset“

### Vytvorenie novej geometrie pre obrobok

Zmeňte rozmery obrobku na **2,5** palca v **polomere**, **8,267** palca vo **výške** a **0,1** palca v **rohoch**. V rozbaľovacom okne Odstrániť sieť kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) a ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}) (pozri obr. L2.3.). Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka Sieť obrobku.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab2_image0003.jpg' | relative_url }})

Vyskakovacie okno „Odstrániť sieť“

### Vytvoriť sieť pre novú geometriu obrobku

Nastavte cieľový počet prvkov na **2000** a kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) vygenerujte sieť pre obrobok. Klikajte na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka s nastavením polohy.

### Polohovanie

Pomocou ![]({{ '/assets/icons/pre_icons/mo_automatic_positioning_button.jpg' | relative_url }}) nastavte polohu nástrojov voči obrobku. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Kontakt“.

### Vytvorenie kontaktu

Vytvorte kontakt pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_generate_contact_nodes_label.jpg' | relative_url }}). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdete na stránku „Primárny zdvih matrice“.

### Zdvih primárneho valca

Zmeňte hodnotu „Celkový **primárny****posun****matrice**“ na **6,5** palca. Kliknite na ovládacie prvky zastavenia ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Ovládacie prvky na zastavenie

V časti „Stopping controls“ (Ovládacie prvky zastavenia) zmeňte hodnotu ovládacieho prvku zastavenia **Primary die displacement** (Primárny posun matrice) z 6 in na **6,5** in. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Generate DB“ (Vytvoriť databázu).

### Vytvoriť databázu

Keďže nastavenia pre druhú operáciu sa nemusia meniť, môžeme vygenerovať databázu a spustiť simuláciu. Databázu vygenerujte kliknutím na ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}).

Kliknutím na tlačidlo „MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode“ (nad stromom operácií) spustíte simuláciu.

### Spustenie a sledovanie simulácie

Kliknutím na štítok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno Možnosti spustenia. Pomocou predvolenej možnosti **Pokračovať v spustení** vyberte možnosť „**Pokračovať od posledného kroku**“, potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

Po dokončení operácie prevrátenia program DEFORM automaticky načíta nové nástroje a spustí druhú operáciu.

### Prezrite si výsledky

Po dokončení simulácie kliknite na tlačidlo „MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode“, aby ste si prezreli výsledky.

Prejdite všetkými krokmi. Všimnite si, že diel úplne vyplňuje dutinu formy.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab2_image0004.jpg' | relative_url }})

Tvar obrobku v poslednom kroku druhej operácie

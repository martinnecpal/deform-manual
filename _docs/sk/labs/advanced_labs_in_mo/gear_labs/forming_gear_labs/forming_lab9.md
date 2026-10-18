---
lang: sk
title: "Laboratórium tvarovania 9"
---

# Laboratórna práca č. 9. Šnekový lis

### Vytvoriť nový problém

Vytvorte nový projekt s názvom **Gear_Screw** a skopírujte existujúci projekt **Gear_LargerBillet**. Kliknite na operáciu **Upset** a prejdite na stránku **Top****Die** Movement.

### Pohyb hornej matrice

Použijeme skrutkový lis s maximálnou energiou **3450** Klb-in., momentom zotrvačnosti (MOI) zotrvačníka 250 Klbin-s² a stúpaním vodiacich skrutiek 4 in/rev.

Pri prvom údere použijeme zníženú energiu a pri druhom údere plnú energiu.

Vyberte pohyb typu **Šnekový****lis****** pre pohyb **Horného****lisovacieho nástroja**, nastavte **Energiu** na hodnotu **1000** a **Moment****zotrvačnosti** na hodnotu **250** a **rozstup závitov vodiacich skrutiek** na hodnotu **4**, ako je znázornené na obr. L9.1. Definujte **účinnosť** ako **funkciu****sily** podľa tejto tabuľky a obr. L9.2.

**Sila** |  **Účinnosť šnekového lisu**  
---|---  
0 |  0,9  
1,0e3 |  0,8  
1,0e4 |  0,7  
1,0e5 |  0,6  
1,0e6 |  0,5  
1,0e7 |  0,2  
  
![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab9_image0001.jpg' | relative_url }})

Okienko na sledovanie pohybu vrchného lisovacieho šneku

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab9_image0002.jpg' | relative_url }})

Funkcia okna zobrazujúceho účinnosť silového úderu

Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Generate DB“.

### Vytvoriť databázu

Vytvorte databázu a klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka s názvom „Next operation **Top****die****movement**“.

### Tvarovacia operácia

**Pohyb hornej matrice**

Použite ten istý pohyb, ktorý bol definovaný v prvej operácii (pozri časť 9.2), avšak použite celkovú energiu **3450** Klb-in.

Uložte projekt a kliknite na tlačidlo „MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode“ (nad stromom operácií), aby ste spustili simuláciu.

### Spustenie a sledovanie simulácie

Kliknite na názov akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}), čím otvoríte dialógové okno Možnosti spustenia. Použite predvolenú možnosť **Pokračovať****Spustiť**, aby ste vybrali možnosť „**Pokračovať od posledného kroku**“, a potom vyberte režim simulácie pomocou prepínača **Interaktívny**. Kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}), aby ste spustili simuláciu.

Všimnite si, že prevádzka 1 sa ukončí, keď sa energia zotrvačníka vyčerpá. Prevádzka 2 sa zastaví na základe vopred definovaného riadiaceho signálu na zastavenie.

### Prezrite si výsledky

Po dokončení simulácie kliknite na tlačidlo „MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode“, aby ste si prezreli výsledky.

**Graf**  
V postprocesore použite nástroj Graph ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) na vytvorenie grafu **Rýchlosť Y** v závislosti od **Času**, aby ste mohli sledovať pokles rýchlosti ram počas tvarovania dielu. (Pozri obr. L9.3.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab9_image0003.jpg' | relative_url }})

Graf závislosti rýchlosti Y od času

---
lang: sk
title: "Založenie spoločnosti Express Lab9"
---

# Laboratórna práca č. 9. Šnekový lis

### Vytvoriť nový problém

Vytvorte nový projekt s názvom **FE_Gear_Screw** a skopírujte existujúci projekt **FE_Gear_LargerBillet** spolu s databázou. Kliknite na operáciu „Upset“ a prejdite na stránku „Top Die Movement“.

Použijeme **skrutkový lis** s maximálnou energiou 3450 Klb-in., momentom zotrvačnosti (MOI) zotrvačníka 250 Klbin-s² a stúpaním vodiacich skrutiek 4 in/rev.

Pri prvom údere (Upset) použijeme zníženú energiu a pri druhom údere (Forming) plnú energiu.

### Definovanie pohybu hornej matrice pri zúžení

Kliknite na dlaždicu operácie **Upset**. Pre pohyb **hornej matrice** vyberte typ pohybu **Šnekový lis**, nastavte **energiu** na hodnotu **1000**, **Moment zotrvačnosti** na hodnotu **250**, **Rozstup závitov vodiacich skrutiek** na hodnotu **4** a **účinnosť** na hodnotu **0,6**. (Pozri obr. L9.1.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab9_image0001.jpg' | relative_url }})

Ovládacie prvky šnekového lisu pre proces lisovania

Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Generate DB“.

### Vytvoriť databázu

Vytvorte databázu a klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa zobrazí stránka s pohybom hornej formy.

### Definovanie pohybu hornej matrice pri tvárnení

Použite ten istý pohyb, ktorý bol definovaný v prvej operácii (pozri časť 9.2.), avšak s plnou **energiou** **3450**. Pre túto operáciu použijeme energiu 3450 klb-in. (Pozri obr. L9.2.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab9_image0002.jpg' | relative_url }})

Riadenie šnekového lisu pre tvárnenie

### Nastavenie primárneho zdvihu matice a krokových ovládačov

Keďže sme v 1. operácii nastavili nižšiu energiu, nedosiahneme očakávanú hodnotu 6,5 v režime „upset“, preto nastavíme väčší zdvih primárneho lisovacieho nástroja, aby sme v 2. operácii dosiahli požadovaný zdvih. Zmeňte **zdvih primárneho lisovacieho nástroja** na **5** palcov.

Uložte projekt a kliknite na tlačidlo „MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode“ (nad stromom operácií), aby ste spustili simuláciu.

### Spustenie a monitorovanie simulácie

Kliknite na názov akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}), čím otvoríte dialógové okno Možnosti spustenia. Pomocou predvolenej možnosti **Pokračovať****Spustiť** vyberte možnosť „**Pokračovať od posledného kroku**“ a následne vyberte režim simulácie pomocou prepínača **Interaktívny**. Kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) na spustenie simulácie.

Všimnite si, že prevádzka 1 sa ukončí, keď sa energia zotrvačníka vyčerpá. Prevádzka 2 sa zastaví na základe vopred definovaného riadiaceho signálu na zastavenie.

### Prezrite si výsledky

Po dokončení simulácie kliknite na tlačidlo „MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode“, aby ste si prezreli výsledky.

**Graf**

V postprocesore použite nástroj Graph ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) na vytvorenie grafu **Y** – **rýchlosť** v závislosti od času, aby ste mohli sledovať pokles rýchlosti ram počas tvarovania dielu. (Pozri obr. L9.3.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab9_image0003.jpg' | relative_url }})

Graf závislosti rýchlosti Y od času

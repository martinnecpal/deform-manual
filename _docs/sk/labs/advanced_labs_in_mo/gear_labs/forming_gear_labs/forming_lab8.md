---
lang: sk
title: "Laboratórium formovania 8"
---

# Laboratórna práca č. 8. Kovanie kladivom

### Vytvorenie nového problému

Vytvorte nový projekt s názvom **Gear_Hammer**. Zaškrtnite políčko **Operácia****kontrola** a nastavte ho na **[2D] Kovanie viacerými údermi**. Systém jednotiek by mal byť nastavený na **anglický**.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab8_image0001.jpg' | relative_url }})

Okno „Nový problém“

### Postup

Na stránke „Process“ nastavte hodnotu **Energy** na **150** Klb-in. Ide o maximálnu energiu úderu. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby sa zobrazil prehľadný tabuľkový prehľad.

### Tabuľka výdychov

Pre **Hit****1** nastavte % **Blow** na **50** a **Efficiency** na **0,7**.

**Poznámka:** Pole „Počet zásahov“ okamžite aktualizuje tabuľku. Ak sa pokúsite číslo zadať ručne, ľahko sa môže stať, že omylom prepíšete predtým zadané zásahy. Z tohto dôvodu sa odporúča používať šípky nahor/nadol na úpravu počtu zásahov pre túto operáciu.

Pomocou šípky nahor zvýšte počet úderov na 2. Nastavte **%****energie****úderu** na **100** a potom zmeňte **počet** **Hits****na****10** kliknutím na šípku nahor. Táto tabuľka úderov obsahuje jeden ľahký prvý úder a potom deväť úderov s plnou energiou (pozri obr. L8.2.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre typ geometrie.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab8_image0002.jpg' | relative_url }})

Zatvoriť okno „Tabuľka“

V tejto fáze naimportujeme predtým nastavený model z iného projektu. Prejdite na **Súbor![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Import** a otvorte súbor **Gear_LargerBillet**.**DB**. Vyberte **prvý** (záporný) **krok****operácie****2**. Mal by to byť približne krok 101 (pozri obr. L8.3.). V kontextovom okne **Globálny/lokálny čas** s otázkou „Chcete použiť novú definíciu času?“ pre globálny čas kliknite na **Nie**. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka s pohybom hornej matrice.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab8_image0003.jpg' | relative_url }})

Okno výberu krokov

### Pohyb hornej matrice

**Pohyb** v dialógovom okne by mal byť definovaný ako **kladivo** s **energiou** **150** Klb-in.

Kliknite na ikonu Kalkulátor hmotnosti ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}). Zadajte **hmotnosť** **1000** libier. Systém prepočíta hmotnosť na jednotky kompatibilné so systémom DEFORM. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Generate DB“. 

### Vytvorenie databázy

Prejdite na stránku „Generate DB“ a vygenerujte databázu. Kliknutím na tlačidlo „MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode“ (nad stromom operácií) spustite simuláciu.

### Spustenie a sledovanie simulácie

Kliknite na názov akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}), čím otvoríte dialógové okno Možnosti spustenia. Použite predvolenú možnosť **Pokračovať****Spustiť**, aby ste vybrali možnosť „**Pokračovať od posledného kroku**“, a potom vyberte režim simulácie pomocou prepínača **Interaktívny**. Kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) na spustenie simulácie.

### Prezrite si výsledky

Po dokončení simulácie kliknite na tlačidlo „MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode“, aby ste si prezreli výsledky.

**Graf**

Prejdite jednotlivé kroky a všimnite si, že formy sa nenapĺňajú a simulácia sa zastaví po vykonaní všetkých úderov.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab8_image0004.jpg' | relative_url }})

Posledný krok operácie „Last of last blow“

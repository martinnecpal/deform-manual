---
lang: sk
title: "Založenie spoločnosti Express Lab8"
---

# Laboratórna práca č. 8. Kovanie kladivom

### Vytvorenie nového problému

Vytvorte nový projekt s názvom **FE_Gear_Hammer**. Zaškrtnite políčko „Prvá operácia“ a nastavte ju na **[2D] Kovanie viacerými údermi**. Systém jednotiek by mal byť **anglický**.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab8_image0001.jpg' | relative_url }})

Okno „Nový problém“

### Postup

Na stránke **Proces** nastavte hodnotu **Energia** na **150** Klb-in. Ide o maximálnu energiu kladiva. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre prechod na tabuľku výbuchov.

### Tabuľka výdychov

Pre úder 1 nastavte **% sily úderu** na **50** a **účinnosť** na **0,7**.

Poznámka: Pole „Počet zásahov“ okamžite aktualizuje tabuľku. Ak sa pokúsite číslo zadať ručne, ľahko sa môže stať, že omylom prepíšete predtým zadané zásahy. Z tohto dôvodu sa odporúča používať šípky nahor/nadol na úpravu počtu zásahov pre túto operáciu.

Pomocou šípky nahor zvýšte počet úderov na 2. Nastavte % energie úderu na 100 pre úder č. 2, potom kliknite na šípku nahor, aby ste zvýšili počet úderov na 10. Táto tabuľka úderov obsahuje jeden ľahký úvodný úder a potom deväť úderov s plnou energiou (pozri obr. L8.2.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) pre typ geometrie.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab8_image0002.jpg' | relative_url }})

Zatvoriť okno „Tabuľka“

V tejto fáze naimportujeme predtým vytvorený model z iného projektu. Prejdite do **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Import** a otvorte súbor **FE_Gear_LargerBillet.DB.** Vyberte **prvý** (záporný) **krok** **operácie****2**. Malo by to byť okolo kroku **101**. V okienku s otázkou „Chcete použiť novú definíciu času?“ pre globálny čas kliknite na **Nie**. Táto voľba vynuluje globálny čas z databázy. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka s pohybom hornej matrice.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab8_image0003.jpg' | relative_url }})

Okno výberu krokov

### Pohyb hornej matrice

Pohyb v dialógu by mal byť definovaný ako **Hammer** s energiou **150** Klb-in.

Kliknite na ikonu kalkulátora hmotnosti ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}). Zadajte hmotnosť **1000** libier. Systém prepočíta hmotnosť na jednotky kompatibilné s DEFORM. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Generate DB“.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab8_image0004.jpg' | relative_url }})

Okienko s mechanizmom kladivka

### Vytvorenie databázy

Prejdite na stránku „Generate DB“ a vygenerujte databázu. Kliknutím na tlačidlo „MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode“ (nad stromom operácií) spustite simuláciu.

### Spustenie a sledovanie simulácie

Kliknite na názov akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}), čím otvoríte dialógové okno Možnosti spustenia. Použite predvolenú možnosť **Pokračovať****Spustiť**, aby ste vybrali možnosť „**Pokračovať od posledného kroku**“, a potom vyberte režim simulácie pomocou prepínača **Interaktívny**. Kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}), aby ste spustili simuláciu.

### Prezrite si výsledky

Po dokončení simulácie kliknite na tlačidlo „MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode“, aby ste si prezreli výsledky.

Prejdite jednotlivé kroky a všimnite si, že formy sa nenapĺňajú a simulácia sa zastaví po dokončení všetkých úderov. (Pozri obr. L8.5.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab8_image0005.jpg' | relative_url }})

Posledný krok operácie „Last of Last Blow“

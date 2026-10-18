---
lang: sk
title: "Forming Lab 10"
---

# Laboratórna práca č. 10. Napätie v matrici

### Otvoriť projekt

Otvorte projekt **Gear_LargerBillet**.

### Pridať analýzu napätia v matrici

V tomto laboratórnom cvičení vykonáme výpočet napätia v lisovacích formách pomocou funkcie „Die stress study“. Kliknite teda na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) v ľavom hornom rohu grafického okna a zo zoznamu vyberte položku „Die stress study“ (pozri obr. L10.1.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab10_image0001.jpg' | relative_url }})

Pridanie analýzy napätia v matrici zo zoznamu

### Výber kroku

Vyberte posledný krok v zozname krokov (pozri obr. L10.2.) a potom klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí hlavná stránka hornej formy.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab10_image0002.jpg' | relative_url }})

Okno výberu kroku

### Definovanie údajov o hornej matrici

Overte, či je teplota hornej matrice **300** °F. V predvolenom nastavení sa typ tuhých objektov z načítaného kroku zmení na pružný. Pre objekt „Top Die“ ponechajte typ objektu ako pružný. Od verzie v13.1.1 boli na stránke objektov zavedené dve nové možnosti na umiestnenie foriem v budúcich krokoch pre analýzu napätia foriem vo viacerých krokoch; pri analýze napätia foriem v jednom kroku tieto možnosti nemusíme používať, preto nechajte políčko „Potrebné umiestnenie“ nezaškrtnuté. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka siete.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab10_image0009.jpg' | relative_url }})

Stránka „Top Die“

#### Vytvoriť sieť hornej formy

Nastavte cieľový počet prvkov na **1000** a vygenerujte sieť. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Material“.

#### Určiť materiál hornej formy

V okne „Materiál“ načítajte materiál **AISI-H-13** z knižnice materiálov a priraďte ho k hornej matrici. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku BCC.

#### Nastaviť BCC pre hornú matricu

Na stránke BCC skontrolujte predvolene priradenú deformáciu BCC pre ľavú stranu hornej formy v smere osi X a následne aplikujte okrajovú podmienku rýchlosti **Vy = 0** na horný povrch hornej formy (pozri obr. L10.4.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste otvorili stránku „Vynútiť interpoláciu“.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab10_image0004.jpg' | relative_url }})

Zatvoriť okno BCC

#### Interpolačná sila pre hornú matricu 

Na stránke „Interpolácia síl“ kliknite na názov akcie ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}), aby ste vykonali interpoláciu síl, ako je znázornené na obr. L10.5. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Spodná matrica“.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab10_image0003.jpg' | relative_url }})

Okno interpolácie sily horného lisovacieho nástroja

### Údaje o spodnej matrici

Skontrolujte, či je teplota spodnej formy **300** °F. Pre spodnú formu ponecháme typ objektu nastavený na „Elastic“ a zrušíme zaškrtnutie políčka „Need positioning“. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka so sieťou.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab10_image0010.jpg' | relative_url }})

Stránka spodnej matrice

#### Vytvoriť sieť spodnej formy

Nastavte cieľový počet prvkov na **1000** a vygenerujte sieť. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Material“.

#### Určiť materiál spodnej matrice

V okne „Materiál“ vyberte materiál **AISI-H-13** zo zoznamu materiálov a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku BCC.

#### Priradiť BCC pre spodnú formu

Na stránke BCC skontrolujte predvolene priradenú deformáciu BCC pre ľavú stranu spodnej formy v **smeru X** a potom na spodnej ploche spodnej formy nastavte okrajovú podmienku rýchlosti **Vy = 0** (pozri obr. L10.7.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby ste prešli na stránku Vynútiť interpoláciu.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab10_image0006.jpg' | relative_url }})

Spodná časť stránky BCC

#### Interpolačná sila pre spodný výlisok 

Na stránke „Interpolácia síl“ kliknite na označenie akcie ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}), aby ste vykonali interpoláciu síl, ako je znázornené na obr. L10.8.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab10_image0005.jpg' | relative_url }})

Okno interpolácie sily spodnej matrice

### Vytvoriť databázu

Kliknite na názov akcie ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby ste skontrolovali problém. Vytvorte databázu kliknutím na názov akcie ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}).

Uložte projekt a kliknite na tlačidlo „MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode“ (nad stromom operácií), aby ste spustili simuláciu.

### Spustiť a sledovať simuláciu

Kliknite na názov akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}), čím otvoríte dialógové okno Možnosti spustenia. Použite predvolenú možnosť **Pokračovať****Spustiť**, aby ste vybrali možnosť „**Pokračovať od posledného kroku**“, a potom vyberte režim simulácie pomocou prepínača **Interaktívny**. Kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustíte simuláciu.

### Prezrite si výsledky

Po dokončení simulácie kliknite na tlačidlo „MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode“, aby ste si prezreli výsledky.

V postprocesore kliknite na kladný krok v zozname krokov.

Zobrazte stavovú premennú **efektívneho****napätia** (pozri obr. L10.9.) . 

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab10_image0007.jpg' | relative_url }})

Graf premennej stavu „efektívne napätie“

Prejdite do dialógového okna „Nastaviť ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }})“ a zobrazte maximálne hlavné napätie (pozri obr. L10.10.) a ostatné zložky napätia.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab10_image0008.jpg' | relative_url }})

Graf premennej stavu „Maximálne hlavné napätie“

Prepnite do režimu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) a pridajte ďalšiu analýzu namáhania čipu, aby ste mohli pridať funkciu „Shrink Fit“. Kliknite na [Lab 11. Die stres with a press fit.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/forming_lab11/' | relative_url }}) a pokračujte v laboratórnom cvičení „Shrink Fit“.

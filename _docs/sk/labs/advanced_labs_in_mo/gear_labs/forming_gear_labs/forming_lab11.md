---
lang: sk
title: "Forming Lab 11"
---

# Cvičenie 11. Pridajte puzdro s lisovaným uložením

### Výber kroku

V zozname krokov vyberte **posledný****krok** a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), čím sa dostanete na stránku „Objekty“.

### Pridať objekt

V tabuľke „Objekty“ pridajte tretí objekt. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Horná matrica“.

### Horná a spodná matrica

Zopakujte rovnaký postup týkajúci sa siete, interpolácie, materiálu a BCC, ako je vysvetlené v [Lab 10: Die stress for the top and bottom die.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/forming_lab10/' | relative_url }}). Po dokončení kliknite na 

### Objekt 4 – Všeobecná stránka

Zmeňte názov objektu na **Case** a nastavte teplotu na **300** °F. Pre objekt Case vyberieme typ Elastic a zrušíme začiarknutie políčka Need positioning. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku s geometriou.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab11_image0010.jpg' | relative_url }})

Stránka objektu prípadu

#### Vytvorenie geometrie prípadu

Pomocou funkcie „Definovať primitívu“ vytvorte **dutý****valec** s **vnútorným****polomerom** **8,5** palca, **vonkajším polomerom****14,4** palca a výškou **5,4** palca.(Pozri obr. L11.2.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab11_image0001.jpg' | relative_url }})

Okno s geometrickými základnými prvkami

#### Vytvoriť sieť prvkov

Vytvorte sieť s **250** prvkami. Klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Material“.

#### Priradiť materiál k prípadu

V okne „Materiál“ vyberte materiál **AISI-H-13**, ktorý chcete priradiť, a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránke BCC.

#### Nastaviť skrytú kópiu (BCC)

Nastavíme okrajovú podmienku sťahovania pozdĺž vnútorného priemeru (ID). V zozname okrajových podmienok kliknite na položku **Shrink Fit** a potom pomocou nástroja By edge ![]({{ '/assets/icons/pre_icons/mo_bcc_edge_icon.jpg' | relative_url }}) vyberte **ID** puzdra. Následne zadajte hodnotu **0,002** (pozri obr. L11.3.) do oboch vstupných polí pre interferenciu. Ako smer zúženia zvoľte smer **x**. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab11_image0002.jpg' | relative_url }})

Výber identifikátora na definovanie BCC s kontrakčným uložením

**Poznámka:** Účelom týchto dvoch vstupných polí je umožniť variabilnú interferenciu pozdĺž definovanej hranice. Šípka v blízkosti stredovej čiary označuje počiatočný a koncový bod vybranej hranice. Keďže ide o rovnomernú interferenciu, pre počiatočný aj koncový bod zvolíme rovnakú hodnotu.

Vyskočí okienko s otázkou, či chcete posunúť uzly o zadanú vzdialenosť. 

Ak sú nástroje nakreslené v skutočnej veľkosti (t. j. prekrývajú sa), je potrebné posunúť uzly. V tomto prípade sú už nakreslené ako zhodné plochy, preto uzly NEPOSÚVAJTE (t. j. odpovedzte **Nie**) (pozri obr. L11.4). Priraďte BCC s tlakovým uložením pre objekt „Case“, ako je znázornené na obr. L11.5. Keďže obrobok sa s týmto puzdrom nedotýka, nie je potrebná žiadna interpolácia síl – klikajte na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým sa nezobrazí stránka „Positioning“.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab11_image0003.jpg' | relative_url }})

Presunúť objekt – kontextové menu s uzlovými súradnicami

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab11_image0004.jpg' | relative_url }})

Priradený BCC s termoplastickým upevnením pre puzdro

#### Prípad polohovania

Prejdite do časti **Polohovanie** a pretiahnite puzdro nadol, až kým sa spodná časť puzdra a spodná forma nezosúladia. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Kontakt

### Kontakt

Pridajte jeden vzťah kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}), ako objekt **Case** vyberte **Maser** a ako objekt **Bottom****Die** vyberte **Slave**. Nastavte hodnotu trenia na **0,1**. Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) vygenerujte kontakt (pozri obr. L11.6). Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Ovládacie prvky simulácie.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab11_image0005.jpg' | relative_url }})

Okná vzťahov medzi objektmi

### Ovládacie prvky simulácie

Pre tento model sú prijateľné štandardné ovládacie prvky simulácie. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) vygenerujte databázu.

### Vytvoriť databázu

Kliknite na popisok akcie ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby ste skontrolovali problém. Vytvorte databázu kliknutím na popisok akcie ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}).

Uložte projekt a kliknite na tlačidlo „MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode“ (nad stromom operácií), aby ste spustili simuláciu.

### Spustenie a sledovanie simulácie

Kliknite na názov akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}), čím otvoríte dialógové okno Možnosti spustenia. Použite predvolenú možnosť **Pokračovať****Spustiť**, aby ste vybrali možnosť „**Pokračovať od posledného kroku**“, a potom vyberte režim simulácie pomocou prepínača **Interaktívny**. Kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) na spustenie simulácie.

### Prezrite si výsledky

Po dokončení simulácie kliknite na tlačidlo „MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode“, aby ste si prezreli výsledky.

V postprocesore kliknite na príslušný krok v zozname krokov a vyberte možnosť „Vykresliť premennú efektívneho napätia“ (pozri obr. L11.7.). 

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab11_image0006.jpg' | relative_url }})

Graf premennej stavu „efektívne napätie“

Prejdite do dialógového okna „Nastavenie ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }})“ a zobrazte maximálne hlavné napätie (pozri obr. L11.8.) a ostatné zložky napätia.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab11_image0007.jpg' | relative_url }})

Graf premennej stavu „Maximálne hlavné napätie“

Porovnajte grafy napätia medzi prvým a druhým prípadom zaťaženia matice.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab11_image0008.jpg' | relative_url }})

Graf stavovej premennej „Stress Effective“ pre obe štúdie napätia v matrici: Štúdia napätia v matrici 1 (vľavo) a Štúdia napätia v matrici 2 (vpravo)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab11_image0009.jpg' | relative_url }})

Graf premennej „Maximálne hlavné napätie“ pre obe štúdie napätia v matrici: Štúdia napätia v matrici 1 (vľavo) a Štúdia napätia v matrici 2 (vpravo)

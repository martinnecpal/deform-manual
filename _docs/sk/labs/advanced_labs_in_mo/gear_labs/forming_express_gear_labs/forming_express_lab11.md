---
lang: sk
title: "Založenie spoločnosti Express Lab11"
---

# Cvičenie 11. Pridajte puzdro s lisovaným uložením

### Výber kroku

V zozname krokov vyberte **posledný****krok** a potom kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), čím sa dostanete na stránku „Objekty“.

### Pridať objekt

V tabuľke „Objekty“ pridajte tretí objekt. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku „Nový objekt“.

### Horná a spodná forma

Pre hornú a spodnú maticu zopakujte rovnaký postup týkajúci sa siete, interpolácie, materiálu a BCC, ako je vysvetlené v [Lab 10: Die stress]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/forming_express_lab10/' | relative_url }}). Po dokončení nastavenia kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a prejdite na stránku „Object 4“.

### Objekt 4 – Všeobecná stránka

Zmeňte názov objektu na **Case** a nastavte teplotu na **300** °F. Pre objekt Case vyberieme typ „Elastic“ a zrušíme zaškrtnutie políčka „Need positioning“. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku s geometriou.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab11_image0010.jpg' | relative_url }})

Stránka objektu prípadu

#### Vytvorenie geometrie prípadu

Pomocou funkcie „Definovať primitív“ vytvorte **dutý****valec** s vnútorným **polomerom****8,5** palca, **vonkajším polomerom 14,4** palca a **výškou** **5,4** palca.(Pozri obr. L11.2.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab11_image0001.jpg' | relative_url }})

Okno s geometrickými primitívami puzdra

#### Vytvoriť sieť prvkov

Vytvorte sieť s **250** prvkami. Keďže obrobok sa s týmto puzdrom nedotýka, nie je potrebná žiadna interpolácia síl. Klikajte teda na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), až sa dostanete na stránku „Material“ (Materiál).

#### Priradiť materiál k prípadu

V okne „Materiál“ priraďte materiál **AISI-H-13** z knižnice materiálov v kategórii **Die_material** a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránke BCC.

#### Nastaviť skrytú kópiu (BCC)

Počas vnútorného priemeru (ID) nastavíme okrajovú podmienku **shrink fit**. V zozname okrajových podmienok kliknite na položku „Shrink Fit“ a následne pomocou nástroja ![]({{ '/assets/icons/pre_icons/mo_bcc_edge_icon.jpg' | relative_url }}) „By edge“ vyberte vnútorný priemer (ID) plášťa. Ďalej vyberte typ **User** a do oboch vstupných polí Interference zadajte hodnotu **0,002** (pozri obr. L11.3.). Ako smer zúženého uloženia vyberte smer x. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab11_image0002.jpg' | relative_url }})

Výber identifikátora na definovanie BCC s kontrakčným uložením

Poznámka: Účelom týchto dvoch vstupných polí je umožniť variabilnú interferenciu pozdĺž definovanej hranice. Šípka v blízkosti stredovej čiary označuje počiatočný a koncový bod vybranej hranice. Keďže ide o rovnomernú interferenciu, pre počiatočný aj koncový bod sme zvolili rovnakú hodnotu.

Vyskočí okienko s otázkou, či chcete uzly posunúť o zadanú vzdialenosť. 

Ak sú nástroje nakreslené v skutočnej veľkosti (t. j. prekrývajú sa), musíme posunúť uzly. V tomto prípade sú už nakreslené ako zhodné plochy, preto uzly NEPOSÚVAJTE (t. j. odpovedzte **Nie**) (pozri obr. L11.4.). Priradený model BCC s kontrakčným uložením pre objekt Case je znázornený na obr. L11.5.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab11_image0003.jpg' | relative_url }})

Presunúť objekt – kontextové menu s uzlovými súradnicami

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab11_image0004.jpg' | relative_url }})

Priradený BCC s tepelne zmrštiteľným obalom pre puzdro

#### Prípad polohovania

Prejdite do časti **Umiestnenie** a **pretiahnite** **obal** nadol, kým sa **spodná****plochu** **obalu** a **spodná****matrica** **nezosúladia**. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Kontakt.

### Kontakt

Pridajte jeden vzťah kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}), ako objekt **Case** vyberte **Maser** a ako objekt **Bottom****Die** vyberte **Slave**. Nastavte hodnotu trenia na **0,1**. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) vygenerujte kontakt. (Pozri obr. L11.6.) Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku Ovládacie prvky simulácie.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab11_image0005.jpg' | relative_url }})

Okná vzťahov medzi objektmi

### Ovládacie prvky simulácie

Pre tento model sú prijateľné štandardné ovládacie prvky simulácie. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) vygenerujte databázu.

### Vytvoriť databázu

Kliknite na názov akcie ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby ste skontrolovali problém. Vytvorte databázu kliknutím na názov akcie ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}).

Uložte projekt a kliknite na tlačidlo „MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode“ (nad stromom operácií), aby ste spustili simuláciu.

### Spustenie a sledovanie simulácie

Kliknite na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}), čím otvoríte dialógové okno Možnosti spustenia. Použite predvolenú možnosť **Pokračovať****Spustiť**, aby ste vybrali možnosť „**Pokračovať od posledného kroku**“, a potom vyberte režim simulácie pomocou rádiového tlačidla **Interaktívny**. Kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) na spustenie simulácie.

### Prezrite si výsledky

Po dokončení simulácie kliknite na tlačidlo „MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode“, aby ste si prezreli výsledky.

V postprocesore kliknite na príslušný krok v zozname krokov a vyberte možnosť „Vykresliť stavovú premennú **efektívneho****napätia**“ (pozri obr. L11.7.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab11_image0006.jpg' | relative_url }})

Graf premennej stavu „efektívne napätie“

Prejdite do dialógového okna „Nastavenie ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }})“ a zobrazte maximálne hlavné napätie (pozri obr. L11.8.) a ďalšie zložky napätia.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab11_image0007.jpg' | relative_url }})

Graf premennej stavu „Maximálne hlavné napätie“

Porovnajte grafy napätia medzi prvým a druhým prípadom zaťaženia výlisku. (Pozri obr. L11.9 a [Fig. L11.10.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/forming_express_lab10/' | relative_url }}#Fig_L10_10_Max_Principal_Stress_state_variable_plot))

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab11_image0008.jpg' | relative_url }})

Graf premennej efektívneho stavu napätia pre obe štúdie napätia v matrici: Štúdia napätia v matrici 1 (vľavo) a Štúdia napätia v matrici 2 (vpravo)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab11_image0009.jpg' | relative_url }})

Graf premennej maximálneho hlavného napätia pre obe štúdie napätí v matrici: Štúdia napätí v matrici 1 (vľavo) a Štúdia napätí v matrici 2 (vpravo)

---
lang: sk
title: "Polotovar na ozubené koleso EN Lab 12"
---

# Laboratórna práca č. 12 – Analýza napätia v lisovacej forme – Kovanie za tepla

Cieľom tohto laboratórneho cvičenia je vykonať analýzu napätí v lisovacej forme. Ak sa analýza napätia vykonáva len na jednom nástroji, na získanie presných hodnôt napätia stačí jednokroková simulácia. Ak sa analýza napätia vykonáva na zostavách lisovacích foriem, kde dochádza k interakcii medzi nástrojmi, zvyčajne je potrebných viac ako jeden krok, aby sa sústava foriem dostala do rovnovážneho stavu pri pôsobiacom zaťažení.

Pri typickej simulácii namáhania foriem sa obrobok odstráni a sily, ktoré obrobok pôsobí na formy, sa interpolujú na nástroje. 

Otvorte v programe DEFORM MO predtým simulovaný súbor Gear.moproj kliknutím na ![]({{ '/assets/icons/pre_icons/mo_integrated_manufacturing_proc.jpg' | relative_url }}). Otvorí sa predspracovateľ MO.

### Pridať štúdiu o namáhaní výliskov

V ľavom hornom rohu okna displeja kliknite ľavým tlačidlom myši na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) a vyberte operáciu **Die****stress****Study**, ako je znázornené na obr. L12.1.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab12_image0001.jpg' | relative_url }})

Doplnenie štúdie o namáhaní výliskov

Ak chcete vykonať operáciu „Die stress“, vyberte na stránke „Step selection“ posledný krok, ako je znázornené na obr. L12.2. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab12_image0002.jpg' | relative_url }})

Výber zoznamu krokov

### Definovanie všeobecných údajov hornej matrice

Nastavte teplotu hornej formy na **300** °F. Štandardne sa typ tuhých objektov z načítaného kroku zmení na pružný. Pre objekt „Top Die“ ponechajte typ objektu ako pružný. Od verzie v13.1.1 boli na stránke objektu zavedené dve nové možnosti na umiestnenie foriem v budúcich krokoch pre analýzu napätia foriem vo viacerých krokoch. Pre analýzu napätia foriem v jednom kroku tieto možnosti nemusíme používať, preto nechajte políčko „Potrebné umiestnenie“ nezaškrtnuté, ako je znázornené na obr. L12.3.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab12_image0003.jpg' | relative_url }})

Okienko „Top Die“

### Vytvoriť sieť hornej formy

Na stránke „Mesh“ zadajte požadovaný počet prvkov siete ako **40000** a potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}), ako je znázornené na obr. L12.4, čím sa vygeneruje sieť.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab12_image0004.jpg' | relative_url }})

Okno so sieťkou

### Interpolácia síl pre hornú matricu

Na stránke „Interpolácia síl“ kliknite na názov akcie ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}), aby ste vykonali interpoláciu síl, ako je znázornené na obr. L12.5. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab12_image0005.jpg' | relative_url }})

Vynútiť interpoláciu hornej matrice

### Priradiť materiál pre hornú formu

V okne materiálu priraďte materiál **AISI-H-13** z knižnice materiálov a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

###  Priradenie okrajových podmienok pre hornú formu

Na hornú plochu hornej matrice nastavte okrajovú podmienku rýchlosti **Vx=Vy=Vz=0**. Táto okrajová podmienka zabraňuje odletu matrice pri pôsobení síl. (Pozri obr. L12.6.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab12_image0006.jpg' | relative_url }})

Okno „Okrajové podmienky“

Z stromu operácií vyberte položku **Spodná forma**, aby ste definovali objekt „Spodná forma“ a jeho vlastnosti, keďže pre „Hornú formu“ už nie sú žiadne premenné, ktoré by bolo potrebné inicializovať.

### Definovanie všeobecných údajov spodnej matrice

Nastavte teplotu spodnej formy na **300** °F. Typ objektu pre spodnú formu ponecháme ako „Elastic“ a zrušíme zaškrtnutie políčka „Need positioning“, ako je znázornené na obr. L12.7.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab12_image0007.jpg' | relative_url }})

Okienko spodnej matrice

### Vytvorenie siete spodnej formy

Na stránke „Mesh“ zadajte požadovaný počet prvkov siete ako **50000** a potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), ako je znázornené na obr. L12.8, aby sa vygenerovala sieť.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab12_image0008.jpg' | relative_url }})

Okno so sieťkou

### Interpolácia síl pre spodnú maticu

Na stránke „Interpolácia síl“ kliknite na názov akcie ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}), aby ste vykonali interpoláciu síl, ako je znázornené na obr. L12.9. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab12_image0009.jpg' | relative_url }})

Okno vynútenej interpolácie

### Priradiť materiál pre spodnú matricu

V okne „Materiál“ vyberte materiál **AISI-H-13**, priraďte ho spodnej matrici a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Nastavenie okrajových podmienok pre spodnú formu

Na spodnej ploche spodnej formy nastavte okrajovú podmienku rýchlosti **Vx=Vy=Vz=0**. (Pozri obr. L12.10.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab12_image0010.jpg' | relative_url }})

Priradenie BCC pre spodnú formu

Kliknite na vetvu **Simulácia****Ovládacie prvky** v strome operácií, keďže premenné nemusíme inicializovať a nastavenie nevyžaduje polohovanie ani generovanie kontaktov.

### Definovanie ovládacích prvkov simulácie

Nastavte **Počet****simulačných****krokov** na **1** a **Krok****prirastku****na****uloženie** na **1**. Nastavte **Max**. **uplynutý****čas****procesu****na****krok** na **1** sekundu. (Pozri obr. L12.11.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab12_image0011.jpg' | relative_url }})

Okno „Ovládacie prvky simulácie“

### Vytvorenie databázy a spustenie simulácie

Výberom možnosti **Súbor****menu![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Export** uložte súbor s kľúčovými slovami pre daný problém pod názvom „Diestress“.

Kliknite na názov akcie ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) a skontrolujte, či v nastaveniach nie sú nejaké problémy. Vytvorte databázu kliknutím na názov akcie ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}).

Po vytvorení databázy prejdite do režimu simulácie kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom objektov.

Kliknite na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}), čím otvoríte dialógové okno „Run Options“ (Možnosti spustenia), ako je znázornené na obr. L12.12. Pomocou predvolenej možnosti **Pokračovať v behu** vyberte možnosť „**Pokračovať od posledného kroku**“ (od kroku -1), potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab12_image0012.jpg' | relative_url }})

Vyskočiace okno „Spustiť simuláciu“

Po dokončení simulácie kliknite na tlačidlo režimu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}), aby ste si prezreli výsledky.

### Výsledky hodnotenia

Pomocou možnosti ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) (Stavové premenné) vyneste do grafu **efektívne napätie** a **maximálne hlavné napätie**, dve z najdôležitejších premenných pri simuláciách napätia v lisovacej forme. (Pozri obr. L12.13 a obr. L12.14.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab12_image0013.jpg' | relative_url }})

Graf obrysov s ohľadom na napätie; (a) pre hornú maticu, (b) pre spodnú maticu

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab12_image0014.jpg' | relative_url }})

Graf kontúry maximálneho hlavného napätia; (a) pre hornú maticu, (b) pre spodnú maticu

* * *

### Voliteľné cvičenie – pridajte zúžovací krúžok na spodnú maticu

\- Otvorte projekt „**Gear**“ v programe DEFORM MO z hlavného okna DEFORM GUI.

\- Pridať druhú **štúdiu napätia v lisovacej forme** a pridať operáciu „Die Stress“, ako je znázornené v laboratórnej úlohe č. 12: [12.1 Add Die Stress Study.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/' | relative_url }}#12_1_Add_Die_stress_Study)

\- Zachovajte vybraný posledný krok, kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a pridajte ďalší objekt z okna objektov (pozri obr. L12.15.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab12_image0015.jpg' | relative_url }})

Bol pridaný ďalší objekt

\- Pokračujte v nastavení **hornej** a **spodnej** **matrice** podľa **Laboratórnej úlohy 12** **až po****časť** **12.11**.

Definovať všeobecné údaje o prípade

\- Premenujte ďalší objekt 3 na **Case** a overte, či je teplota objektu nastavená na **68** °F. Ako typ objektu vyberieme **elastic** a zrušíme zaškrtnutie políčka „Potrebné polohovanie“.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab12_image0022.jpg' | relative_url }})

Stránka objektu prípadu

  * Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a naimportujte geometriu „**gear_die_case_ENG****.****STL**“ z knižnice.

  * Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a vygenerujte sieť s **50 000** prvkami.

  * Interpolácia s vynútením nie je potrebná. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a priraďte materiál **AISI-H-13**.

  * Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a spodnej ploche priraďte hodnotu Vy=0, ako je znázornené na obr. L12.17.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab12_image0016.jpg' | relative_url }})

Nastavte rýchlosť na spodnej ploche v smere Y

Na vnútorný priemer (ID) v smere **Y** aplikujte interferenčné zúženie **Shrink****Fit** s hodnotou **0,020** ’’ (na každú stranu) – vektor smeruje v smere **Y**, ako je znázornené na obr. L12.18.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab12_image0017.jpg' | relative_url }})

Tepelné zúženie na vnútorný priemer zúžovacieho krúžku kolmo na smer osi Y

Pri vykonávaní tepelného zúženia sa program DEFORM opýta, či chcete, aby boli uzly puzdra posunuté o rovnakú hodnotu ako je tolerancia tepelného zúženia (pozri obr. L12.18.). Vo väčšine prípadov, tak ako aj v tomto cvičení, najprv umiestnite nástroj tak, aby došlo k kontaktu, a až potom vykonáte tepelné zúženie. V tomto prípade je potrebné odpovedať **Nie**. Tým sa zabráni posunutiu uzlov. Ak importujete geometriu nástroja tak, že kolízia je znázornená prekrývaním medzi maticou a puzdrom, potom je správnou voľbou kliknutie na **Áno**, čím sa posunú uzly puzdra, aby bolo možné definovať kontakt.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab12_image0018.jpg' | relative_url }})

Rozbaľovacie okno na presun uzlových súradníc objektu pre BCC „Shrink“

-Inicializácia premenných nie je potrebná a objekty sú správne umiestnené, preto kliknite na vetvu **Kontakt** v operačnom strome, aby ste vytvorili kontakt medzi spodnou matricou a zmršťovacím krúžkom.

  * Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}), ako objekt puzdra vyberte „Maser“ a ako objekt spodnej matrice vyberte „Slave“. Nastavte hodnotu trenia na 0,08. 

  * Kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}), aby ste vytvorili kontakt. (Pozri obr. L12.19.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab12_image0019.jpg' | relative_url }})

Okno vzťahov medzi objektmi

\- Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a zmeňte **počet simulačných krokov** na **5** krokov a **ukladajte****každých****5**.

\- Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a zapíšte databázu.

\- Kliknite na tlačidlo režimu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) a spustite simuláciu.

\- Po dokončení simulácie kliknite na ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}), aby ste otvorili postprocesor, a porovnajte hodnoty napätia v mieste koncentrácie napätia na spodnej matrici v jednotlivých zaťažovacích prípadoch s krúžkom a bez zúžovacieho krúžku (výsledky laboratórnej úlohy č. 12), ako je znázornené na obr. L12.21 a obr. L12.22.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab12_image0020.jpg' | relative_url }})

Efektívne napätie v spodnej matrici s a bez zúžovacieho krúžku

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab12_image0021.jpg' | relative_url }})

Maximálne hlavné napätie v spodnej matrici s a bez zúžovacieho krúžku

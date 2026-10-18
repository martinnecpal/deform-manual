---
lang: sk
title: "Polotovar na ozubené kolesá SI Lab 12"
---

# Lab12. Analýza napätí v lisovacej forme – Kovanie za tepla

Cieľom tohto laboratórneho cvičenia je vykonať analýzu napätí v lisovacej forme. Ak sa analýza napätia vykonáva len na jednom nástroji, na získanie presných hodnôt napätia stačí jednokroková simulácia. Ak sa analýza napätia vykonáva na zostavách lisovacích foriem, kde dochádza k interakcii medzi nástrojmi, zvyčajne je potrebných viac krokov, aby sa sústava foriem dostala do rovnovážneho stavu pri pôsobiacom zaťažení.

Pri typickej simulácii namáhania foriem sa obrobok odstráni a sily, ktoré na formy pôsobí obrobok, sa interpolujú na nástroje. 

Otvorte v programe DEFORM MO predtým simulovaný súbor Gear.moproj kliknutím na ![]({{ '/assets/icons/pre_icons/mo_integrated_manufacturing_proc.jpg' | relative_url }}). Otvorí sa predspracovateľ MO.

### Pridať štúdiu o namáhaní výliskov

V ľavom hornom rohu okna displeja kliknite ľavým tlačidlom myši na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) a vyberte operáciu „Pridať analýzu napätia čipu“, ako je znázornené na obrázku [Fig. L12.1.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab12/' | relative_url }}#Fig_L12_1_Adding_Die_stress_Study)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab12_image0001.jpg' | relative_url }})

Doplnenie štúdie o namáhaní foriem

Ak chcete vykonať operáciu „Die stress“, vyberte na stránke „Step selection“ posledný krok, ako je znázornené na obrázku [Fig. L12.2.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab12/' | relative_url }}#Fig_L12_2_Step_selection_for_Die_stress_study), a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab12_image0002.jpg' | relative_url }})

Výber kroku pre analýzu napätia v lisovacej forme

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), aby sa zobrazila stránka s objektmi, keďže nie sú potrebné žiadne ďalšie objekty.

### Definícia všeobecných údajov hornej matrice

Nastavte teplotu hornej matrice na **148,89°** C. Štandardne sa typ tuhých objektov z načítaného kroku zmení na pružný. Pre objekt „Punch“ ponechajte typ objektu ako pružný. Od verzie v13.1.1 boli na stránke objektov zavedené dve nové možnosti na polohovanie lisovacích foriem v budúcich krokoch pri analýze napätia v lisovacích formách s viacerými krokmi; pri analýze napätia v lisovacích formách s jedným krokom tieto možnosti nemusíme používať, preto ponechajte políčko „Potreba polohovania“ nezaškrtnuté, ako je znázornené na obrázku [Fig. L12.3.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab12/' | relative_url }}#Fig_L12_3_Top_Die_window).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab12_image0003.jpg' | relative_url }})

Okienko na hornej matrici

### Vytvorenie siete hornej formy

Na stránke „Mesh“ zadajte požadovaný počet prvkov siete ako **40000** a potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}), ako je znázornené na obrázku [Fig. L12.4.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab12/' | relative_url }}#Fig_L12_4_Mesh_window), aby sa vygenerovala sieť.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab12_image0004.jpg' | relative_url }})

Okno so sieťkou

### Interpolácia síl pre hornú formu

Na stránke „Interpolácia síl“ kliknite na označenie akcie ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}), aby ste vykonali interpoláciu síl tak, ako je znázornené na obrázku [Fig. L12.5.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab12/' | relative_url }}#Fig_L12_5_Force_interpolation_of_Top_Die). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab12_image0005.jpg' | relative_url }})

Vynútiť interpoláciu hornej matrice

### Priradiť materiál pre hornú formu

V okne „Materiál“ vyberte materiál **AISI-H-13** z knižnice materiálov a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Nastavenie okrajových podmienok pre hornú formu

Na hornú plochu hornej matrice nastavte okrajovú podmienku rýchlosti **Vx=Vy=Vz=0**. Táto okrajová podmienka zabraňuje odletu matrice pri pôsobení síl. (Pozri [Fig. L12.6.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab12/' | relative_url }}#Fig_L12_6_Boundary_Conditions_window))

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab12_image0006.jpg' | relative_url }})

Okno „Okrajové podmienky“

Z operačného stromu vyberte položku **Spodná forma**, aby ste definovali objekt „Spodná forma“ a jeho vlastnosti, keďže pre „Hornú formu“ už nie sú žiadne premenné, ktoré by bolo potrebné inicializovať.

### Definovanie všeobecných údajov spodnej matrice

Nastavte teplotu spodnej formy na **148,89** °C. Typ objektu pre spodnú formu ponecháme ako „Elastic“ a zrušte zaškrtnutie políčka „Need positioning“, ako je znázornené na obrázku [Fig. L12.7.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab12/' | relative_url }}#Fig_L12_7_Bottom_Die_Window).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab12_image0007.jpg' | relative_url }})

Okienko spodnej matrice

### Vytvorenie siete spodnej formy

Na stránke „Mesh“ zadajte požadovaný počet prvkov siete ako **50000** a potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}), ako je znázornené na obrázku [Fig. L12.8.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab12/' | relative_url }}#Fig_L12_8_Mesh_window), aby ste vytvorili sieť.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab12_image0008.jpg' | relative_url }})

Okno so sieťkou

### Interpolácia síl pre spodnú maticu

Na stránke „Interpolácia síl“ kliknite na označenie akcie ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}), aby ste vykonali interpoláciu síl tak, ako je znázornené v [Fig. L12.9.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab12/' | relative_url }}#Fig_L12_9_Force_Interpolation_Window). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab12_image0009.jpg' | relative_url }})

Okno vynútenej interpolácie

### Priradiť materiál pre spodnú matricu

V okne „Materiál“ vyberte materiál **AISI-H-13**, priraďte ho k spodnej matrici a kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Nastavenie okrajových podmienok pre spodnú formu

Na spodnej ploche spodnej formy nastavte okrajovú podmienku pre rýchlosť Vx=Vy=Vz=0. (Pozri [Fig. L12.10.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab12/' | relative_url }}#Fig_L12_10_Assigning_BCC_for_Bottom_Die))

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab12_image0010.jpg' | relative_url }})

Priradenie BCC pre spodnú formu

Kliknite na vetvu **Ovládacie prvky simulácie** v strome operácií, keďže premenné nie je potrebné inicializovať a nastavenie nevyžaduje polohovanie ani generovanie kontaktov.

### Definovanie ovládacích prvkov simulácie

Nastavte **Počet simulačných krokov** na **1** a **Krok****Prírastok****na****Uložiť** na **1**. Nastavte **Max. uplynutý čas procesu na krok** na **1** sekundu. (Pozri [Fig. L12.11.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab12/' | relative_url }}#Fig_L12_11_Simulation_Controls_window))

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab12_image0011.jpg' | relative_url }})

Okno „Ovládacie prvky simulácie“

### Vytvorenie databázy a spustenie simulácie

V ponuke Súbor vyberte možnosť **Exportovať** a uložte súbor s kľúčovými slovami pre daný problém pod názvom „**Diestress**“.

Kliknite na názov akcie ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) a skontrolujte, či v nastaveniach nie sú nejaké problémy. Vytvorte databázu kliknutím na názov akcie ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}).

Po vytvorení databázy prejdite do režimu simulácie kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom objektov. Kliknutím na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvoríte dialógové okno Možnosti spustenia. Použite predvolenú možnosť **Pokračovať v spúšťaní**, vyberte možnosť „**Pokračovať od posledného kroku**“ a potom nastavte režim simulácie na **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab12_image0012.jpg' | relative_url }})

Vyskočie okno „Spustiť simuláciu“

Po dokončení simulácie kliknite na tlačidlo „![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) MO Mode“, aby ste si prezreli výsledky.

### Výsledky hodnotenia

Pomocou voľby ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) (Stavové premenné) vykreslite efektívne napätie a maximálne hlavné napätie, dve z najdôležitejších premenných pri simuláciách napätia v lisovacej forme. (Pozri [Fig. L12.13.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab12/' | relative_url }}#Flg_L12_13_Stress_Effective_contour_plot) a [Fig. L12.14.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab12/' | relative_url }}#Fig_L12_14_Stress_Max_principal_contour_plot))

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab12_image0013.jpg' | relative_url }})

Graf obrysov s ohľadom na napätie; (a) pre hornú matricu, (b) pre spodnú matricu

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab12_image0014.jpg' | relative_url }})

Graf hlavných kontúr metódy Stress Max; (a) pre hornú maticu, (b) pre spodnú maticu

* * *

### Voliteľné cvičenie – pridajte zúžovací krúžok na spodnú maticu

\- Otvorte projekt „Gear“ v programe DEFORM MO z hlavnej obrazovky DEFORM GUI. 

\- Pridať druhú analýzu napätia v matrici a pridať operáciu „Die Stress“ podľa obrázku v súbore [Lab 12: 12.1 Add Die Stress Study.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab12/' | relative_url }}#12_1_Add_Die_stress_Study)

\- Zachovajte naposledy vybraný krok, kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a pridajte ďalší objekt z okna objektov (pozri [Fig. L12.15.]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab12/' | relative_url }}#Fig_L12_15_Added_additional_object)).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab12_image0015.jpg' | relative_url }})

Bol pridaný ďalší objekt

\- Pokračujte v nastavení hornej a dolnej matrice podľa [Lab 12]({{ '/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab12/' | relative_url }}#Lab12_Die_Stress_analysis_-_Hot_Forging) až po časť 12.11.

**Vymedzenie všeobecných údajov o prípade**

\- Premenujte ďalší objekt 3 na „case“ a overte, či je teplota objektu nastavená na **20** °C. Ako typ objektu zvolíme **elastic** a zrušíme zaškrtnutie políčka „Need positioning“.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab12_image0022.jpg' | relative_url }})

Stránka objektu prípadu

  * Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a naimportujte geometriu „**gear_die_case_SI.STL**“ z knižnice.

  * Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a vygenerujte sieť s **50 000** prvkami.

  * Interpolácia sily nie je potrebná. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a priraďte materiál **AISI-H-13**.

  * Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a spodnej ploche priraďte hodnotu **Vy=0**, ako je znázornené na obr. L12.17.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab12_image0016.jpg' | relative_url }})

Nastavte rýchlosť na spodnej ploche v smere Y

  * Použite**0,508** ’’ interferenčné zúženie (na každej strane) s vtiahnutím na vnútorný priemer v smere Y

\- vektor smeruje v smere osi Y, ako je znázornené na obr. L12.18.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab12_image0017.jpg' | relative_url }})

Tepelné zúženie na vnútorný priemer zúžovacieho krúžku kolmo na smer osi Y

Pri vykonávaní tepelného zúženia sa program DEFORM opýta, či chcete, aby boli uzly puzdra posunuté o rovnakú hodnotu ako tolerancia tepelného zúženia (pozri obr. L12.19.). Vo väčšine prípadov, ako aj v tomto cvičení, najprv umiestnite nástroj tak, aby došlo k styku, a až potom vykonáte tepelné zúženie. V tomto prípade je potrebné odpovedať „nie“. Tým sa zabráni posunutiu uzlov. Ak importujete geometriu nástroja tak, že kolízia je znázornená prekrývaním medzi maticou a puzdrom, správnou voľbou je kliknúť na „áno“, čím sa posunú uzly puzdra, aby bolo možné definovať kontakt.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab12_image0018.jpg' | relative_url }})

Rozbaľovacie okno s uzlovými súradnicami objektu pre BCC „Zmenšiť“

\- Inicializácia premenných nie je potrebná a objekty sú správne umiestnené, preto kliknite na vetvu **Kontakt** v strome operácií, aby ste vytvorili kontakt medzi spodnou matricou a zmršťovacím krúžkom.

  * Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}), ako objekt „Case“ vyberte „Maser“ a ako objekt „Bottom Die“ vyberte „Slave“. Nastavte hodnotu trenia na 0,08. 

  * Kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}), aby ste vytvorili kontakt. (Pozri obr. L12.20.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab12_image0019.jpg' | relative_url }})

Okno vzťahov medzi objektmi

\- Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), nastavte počet simulačných krokov na 5 a uložte výsledky každých 5 krokov.

\- Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) a zapíšte databázu.

\- Kliknite na tlačidlo režimu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) a spustite simuláciu.

\- Po dokončení simulácie kliknite na tlačidlo pre vstup do postprocesora a porovnajte hodnoty napätia v mieste koncentrácie napätia na spodnej matrici medzi zaťažovacími prípadmi s krúžkom a bez zúžovacieho krúžku (výsledky cvičenia 12), ako je znázornené na obr. L12.21 a obr. L12.22.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab12_image0020.jpg' | relative_url }})

Efektívne napätie v spodnej matrici s a bez zúžovacieho krúžku

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab12_image0021.jpg' | relative_url }})

Maximálne hlavné napätie v spodnej matrici s a bez zúžovacieho krúžku

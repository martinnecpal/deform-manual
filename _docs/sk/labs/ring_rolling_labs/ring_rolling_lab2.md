---
lang: sk
title: "Krúžok valcovania Lab2"
---

# Ring Rolling Lab2

V tomto laboratóriu nastavujeme jednoduchú operáciu valcovania krúžkov s axiálnymi valcami.

  
2.1. Vytvorenie nového problému

2.2. Stránka procesu

2.3. Nastavenie simulácie

2.4. Výber objektu

2.4.1. Všeobecná stránka krúžku obrobku

2.4.2. Stránka objektu Driving Roll

2.4.3. Stránka objektu tlakového rolovania

2.4.4. Axial Roll #1 Object Page

2.4.5. Všeobecná stránka axiálneho valca č.2

2.5. Kontaktná stránka

2.6. Ovládacie prvky zastavenia

2.7. Ovládacie prvky Step a Remeshing Strana

2.8. Vytvoriť databázu

2.9. Simulácia chodu

2.10. Post Processing

## Vytvorenie nového problému

Na ** zariadení so systémom Windows ** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), zvoľte DEFORM-v1x.xxx (.xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte * * DEFORM GUI Main * * vxx.xx. Zobrazí SA hlavné okno Deform GUI.

Vytvorte nový problém buď výberom **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})* ***Nový problém** alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Problem Setup (Nastavenie problému), ako je znázornené na obr. RRL2.1. Pomocou prepínača vyberte prepínač „ * * Integrated Manufacturing Process * *“ a systém jednotiek ako „** English * * “. Definujte názov problému ako "**RING_ROLL_LAB2 ** " a uistite sa, že je zapnuté začiarkavacie políčko "Zobraziť dialóg možností" (ak nezapneme začiarkavacie políčko "**Zobraziť dialóg možností ** ", potom nedostaneme dialógové okno Nový projekt v používateľskom rozhraní MO). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) a otvorte nový problém pomocou integrovaného výrobného procesu deformácie.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

Nový problém

V dialógovom okne Nový projekt sa otvorí sprievodca viacerými operáciami, v tomto bode sa používateľovi zobrazí výzva na zadanie názvu projektu (systém vytvorí samostatný priečinok s týmto názvom projektu) a názvu tejto relácie. V tejto relácii použijeme ako názov projektu „**RING_ROLL_LAB2 ** “. Operáciu 3D Ring Rolling je možné pridať aj v dialógu „Nový projekt“ (pozri obr. RRL2.2.), v tomto laboratóriu pridáme operáciu valcovania krúžku zo zoznamu operácií prieskumníka, takže nezačiarknite políčko "Prvá operácia" a operáciu "Valcovanie krúžku" v dialógovom okne "Nový projekt". Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otvorení operácie.

Pridajte operáciu valcovania 3D prstenca zo zoznamu operácií prieskumníka. Pridajte operáciu kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}), ktoré je k dispozícii vedľa funkcie 3D Ring Rolling, alebo ho môžete pridať aj presunutím myšou do editora operácií (pozri obr. RRL2.3.). Keď pridáme operáciu Ring Rolling, predvolene sa otvorí okno nastavení procesu.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab2/image0002.jpg' | relative_url }})

Pridanie operácie valcovania krúžku z nového projektu

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab2/image0003.jpg' | relative_url }})

Pridanie operácie valcovania krúžku z Prieskum

## Stránka procesu

Na stránke Proces sa predvolene vyberie prepínač „* * Valcovanie krúžku (predvolené) * * “ (pozri obr. RRL2.4.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na nastavenie simulácie.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab2/image0004.jpg' | relative_url }})

Stránka procesu

## Nastavenie simulácie

Vyberte prepínač „**Celá časť** “ typu 3D modelu. Keďže nás zaujíma zmena teploty v prstenci, vyberte Tepelné výpočty ako typ „ ** Len obrobok (neizotermický)** “ na stránke nastavenia simulácie, ako je znázornené na obr. RRL2.5. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po stránku Objekty.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab2/image0005.jpg' | relative_url }})

Nastavenie simulácie

Object Selection

Predpokladá sa, že procesy valcovania krúžkov majú hlavný vonkajší hnací valec a vnútorný tlakový valec alebo tŕň. Tieto „radiálne“ valce znižujú hrúbku steny a rozširujú krúžok. V závislosti od konfigurácie mlyna sa axiálne valce môžu použiť aj na ovládanie šírky alebo výšky krúžku. Ak sa majú použiť axiálne valce, začiarknite možnosť „Axial Rolls“ (Axiálne valce).

Pre symetrické diely použite 1 axiálny valec. Pre celé diely použite 2 axiálne valce. Predvolene sa predpokladá, že axiálne valce sú priamo (180 stupňov) oproti radiálnym valcom.

Riešič MKP používa automatický centrovací systém, takže vodiace valce nie sú potrebné a momentálne nie sú k dispozícii.

Na stránke „Objects“ (Objekty) začiarknite políčko **Axial Roll # 1* * a * *Axial Roll # 2**, ako je znázornené na obr. RRL2.6. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku Obrobok - krúžok.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab2/image0006.jpg' | relative_url }})

Stránka výberu objektov

### Všeobecná stránka kruhového obrobku

Na stránke Obrobok - krúžok definujte teplotu objektu ako **2100** F, ako je znázornené na obr. RRL2.7., Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na 2D prierez.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab2/image0007.jpg' | relative_url }})

Obrobok - stránka Objekt krúžku

#### Stránka 2D prierezu krúžku obrobku

Na stránke prierezu 2D obrobku kliknite na ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}) a definujte údaje súradníc, ako je znázornené na obr. RRL2.8. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte okno úprav a kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na 2D povrchovú sieť.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab2/image0029.jpg' | relative_url }})

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab2/image0008.jpg' | relative_url }})

Stránka geometrie úpravy obrobku

#### Stránka 2D sieťoviny krúžku obrobku

V nastaveniach 2D povrchovej siete definujte **Cieľový počet prvkov** ako **120** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) a sledujte vygenerovanú povrchovú sieť v okne displeja (pozri obr. RRL2.9.). Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na 3D geometriu.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab2/image0009.jpg' | relative_url }})

Stránka 2D povrchovej siete obrobku

#### Stránka 3D geometrie krúžku obrobku

Na stránke 3D geometrie kliknite na možnosť "** Otočiť z 2D** ", Použite predvolené hodnoty v ** Otočiť z 2D** stránky a kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) pre zatvorenie. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na 3D povrchovú sieť.

#### Stránka 3D sieťoviny krúžku obrobku

Na stránke 3D povrchová sieť s predvolenou hodnotou **120** pre „**Počet otočných sekcií** “ vytvorte 3D povrchovú sieť kliknutím na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). Sledujte vygenerovanú 3D sieť pre obrobok, ako je znázornené na obr. RRL2.10. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po stránku Materiál.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab2/image0010.jpg' | relative_url }})

Stránka 3D sieťoviny krúžku obrobku

#### Priradiť materiál krúžku obrobku

Na stránke Materiál kliknite na ikonu ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať materiál z knižnice) a načítajte * * oceľ * * skupinový materiál "**AISI-8620 [1550-2200F (850-1200C)]** " z okna knižnice materiálov. Priraďte materiál „**AISI-8620[1550-2200F(850-1200C)]** “ pre obrobok. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Workpiece BCC.

#### Priradiť BCC pre krúžok obrobku

Skontrolujte predvolené BCC priradené pre obrobok, predvolená výmena tepla BCC by mala byť priradená pre vonkajší povrch, ako je znázornené na obr. RRL2.11. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až do stránky Driving Roll Object.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab2/image0011.jpg' | relative_url }})

Stránka stavu ohraničenia obrobku

### Stránka objektu Driving Roll

Meno „ Driving Roll“ ponechajte nezmenené a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku geometrie prierezu 2D.

#### Stránka 2D prierezu riadiaceho valca

Na stránke Driving Roll 2D Geometry kliknite na ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}) a definujte údaje súradníc, ako je znázornené na obr. RRL2.12 alebo Importujte **Driving_Roll.GEO** z priečinka 2D LABS a kliknite na „Upraviť“. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte okno úprav a kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na 3D geometriu.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab2/image0030.jpg' | relative_url }})

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab2/image0012.jpg' | relative_url }})

Driving Roll 2D Geometry page

#### Stránka 3D geometrie Driving Roll

Na stránke 3D geometrie kliknite na možnosť „** Otočiť z 2D** “, použite predvolenú hodnotu * * 100 * * pre „**Počet vrstiev v smere obruče ** “ v položke Otočiť z 2D stránky a zatvorte kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na orientáciu.

#### Orientácia na šoférovanie

Na stránke Orientácia jazdného valca zvoľte možnosť „**Nastaviť relatívnu vzdialenosť medzi stredom objektu ** “ a definujte „ Vertikálnu vzdialenosť (d)“ ako * * 2,25 ** * * v * * a „Relatívnu polohu aktuálneho stredu objektu“ v „* * -Z * * “ a kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_orientation_angle_button.jpg' | relative_url }}) pre posunutie jazdného valca o 2,25 in pozdĺž osi Z vzhľadom na stred prstencového objektu (pozri obr. RRL2.13.). Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku Pohyb.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab2/image0013.jpg' | relative_url }})

Orientačná stránka jazdného valca

#### Pohyb hnacieho valca

Vyberte ** Uhlovú rýchlosť** v ovládacích prvkoch rotačného pohybu pre hnací valec a definujte konštantnú hodnotu **6.28318***rad/sec**. Všimnite si zelenú šípku otáčania zobrazujúcu smer otáčania v okne displeja (pozri obr. RRL2.14.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku Objekt v tlakovom valci.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab2/image0014.jpg' | relative_url }})

Stránka Driving Roll Movement

### Stránka objektu tlakového valca

Názov „Pressure Roll“ ponechajte nezmenený a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku s prierezom 2D.

#### Stránka 2D prierezu tlakového valca

Na stránke Pressure Roll 2D Geometry kliknite na ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}) a definujte údaje súradníc, ako je znázornené na obr. RRL2.15. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte okno úprav a kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na 3D geometriu.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab2/image0031.jpg' | relative_url }})

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab2/image0015.jpg' | relative_url }})

Stránka Geometria tlakového kotúča

#### Stránka 3D geometrie tlakového valca

Na stránke 3D geometrie kliknite na možnosť "** Otočiť z 2D** ", použite predvolenú hodnotu * * 100 * * pre "Počet vrstiev v smere obruče" na Otočiť z 2D stránky a kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) pre zatvorenie. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na orientáciu.

#### Orientácia tlakového valca

Vyberte možnosť „**Nastaviť relatívnu vzdialenosť medzi stredmi objektov ** “ a definujte „ Vertikálnu vzdialenosť (d)“ ako * * 5,5 * * a „Relatívne umiestnenie aktuálneho stredu objektu“ v „**-Z * * “ a kliknite na ![]({{ '/assets/icons/pre_icons/mo_apply_orientation_button.jpg' | relative_url }}) pre posunutie valca tlaku nadol pozdĺž osi Z o 5,5 palca (pozri obr. RRL2.13.) na stránke Orientácia tlakového kotúča. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Movement.

#### Pohyb tlakového valca

Vyberte "**Funkcia času** " v rýchlosti a definujte hodnoty, ako je uvedené nižšie v tabuľke a na obr. RRL2.16. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po stranu Axial Roll #1.

**Čas** |  **Rýchlosť**
---|---
0 |  0,05
5 |  0,05
20 |  0,025
60 |  0,005
  
![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab2/image0016.jpg' | relative_url }})

Rýchlosť valenia tlaku ako funkcia pohybu času

### Axial Roll #1 Stránka objektu

Meno „Axial Roll # 1“ ponechajte nezmenené a definujte teplotu objektu ako **300 F**. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdete na stránku 2D prierezu.

#### Stránka 2D prierezu axiálneho valca #1

Na stránke Axial Roll #1 2D Geometry kliknite na "![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}) a definujte údaje súradníc, ako je znázornené na obr. RRL2.17. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte okno úprav a kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na 3D geometriu.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab2/image0032.jpg' | relative_url }})

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab2/image0017.jpg' | relative_url }})

Axial Roll #1 Geometry page

#### Stránka 3D geometrie axiálneho valca #1

Na stránke 3D geometrie kliknite na možnosť "** Otočiť z 2D** ", použite predvolenú hodnotu * * 100 * * pre "Počet vrstiev v smere obruče" na Otočiť z 2D stránky a kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) pre zatvorenie. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na orientáciu.

#### Orientácia axiálneho valca #1

Na stránke Orientácia je automaticky správne umiestnený axiálny valec na obrobku pod uhlom 180 stupňov, stačí kliknúť na ![]({{ '/assets/icons/pre_icons/mo_apply_orientation_button.jpg' | relative_url }}) s predvolenými hodnotami (pozri obr. RRL2.18) na stránke Axial Roll # 1Orientation. Orientačná stránka sa môže použiť na umiestnenie axiálneho valca pozdĺž obvodu prstenca v smere obručí zadaním uhla v podanom uhle otáčania a pozdĺž šírky prstenca zadaním horizontálnej vzdialenosti medzi koncom kužeľa a stredom prstenca, ako je znázornené na obr. RRL2.18. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku Pohyb.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab2/image0018.jpg' | relative_url }})

Stránka Axial Roll # 1Orientation

#### Axial Roll #1 Stránka pohybu

Definujte **konštantnú*** * rýchlosť * * 0,016 * * in/sec pre axiálny valec #1 (pozri obr. RRL2.19.). Ak sa axiálne valce pohybujú spolu s expanziou krúžku, používateľ môže skontrolovať začiarkavacie políčko „Automatický radiálny pohyb obrobku s expanziou obrobku“, potom sa axiálne valce pohybujú spolu s obrobkom počas simulácie. Ak používateľ začiarkne políčko „Adaptívne riadenie rotačného pohybu“, potom sa axiálne valce otáčajú podľa otáčania krúžku bez sklzu, kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až do stránky Axial Roll #2.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab2/image0019.jpg' | relative_url }})

Stránka pohybu axiálneho valca č.1

### Axial Roll #2 Všeobecná stránka

Meno „Axial Roll # 2“ ponechajte nezmenené a definujte teplotu objektu ako **300 F**. Kliknite na možnosť „**Kopírovať axiálny valec č.1** “, aby sa všetky údaje axiálneho valca č.1 skopírovali do objektu axiálneho valca č. 2 (pozri obr. RRL2.20.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po orientačnú stránku.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab2/image0020.jpg' | relative_url }})

Axial Roll #2 Všeobecná stránka

#### Orientačná stránka axiálneho valca č.2

Na stránke Orientácia je automaticky osový valec č.2 správne umiestnený na obrobku a v uhle polohy ** 180 * * stupňov stačí kliknúť na ![]({{ '/assets/icons/pre_icons/mo_apply_orientation_button.jpg' | relative_url }}) s predvolenými hodnotami (pozri obr. RRL2.21.) v Axial Roll #2 Orientation page. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Movement.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab2/image0021.jpg' | relative_url }})

Orientačná stránka axiálneho valca č.2

#### Axial Roll #2 Stránka pohybu

Ponechajte skopírovaný pohyb z objektu Axial Roll #1, kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až do stránky Kontakt.

Kontakty

Na stránke Kontakt použite predvolenú hodnotu šmykového trenia a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) pre výpočet predvolenej hodnoty tolerancie, kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) pre generovanie kontaktov medzi valcami a obrobkom, ako je znázornené na obr. RRL2.22. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku Zastavenie ovládacích prvkov.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab2/image0022.jpg' | relative_url }})

stránka s kontaktnými informáciami

## Zastavenie ovládacích prvkov

Definujte "**Max. vonkajší priemer obrobku** " ako **24** v, **Proces* ***trvanie** ako **60** s a vyberte "**Tlakový valec (tŕň)** " ako **Primárny****die** a definujte * * Y * * hodnotu posunu ako "* * 15 * * ", ako je znázornené na obr. RRL2.23. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na ovládacie prvky Step a Remeshing.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab2/image0023.jpg' | relative_url }})

Stránka Zastavenie ovládacích prvkov

## Stránka s ovládacími prvkami Step a Remeshing

Zadajte **Počet krokov** ako **10000** , prírastok rotácie na uloženie ako **180** a maximálny povolený časový krok ako **0,05**. Ponechajte predvolené „**Vypočítajte teplotu tak často, ako je deformácia** “ Typ výpočtu teploty a ponechajte predvolené kontrolné údaje premiešania, ako je znázornené na obr. RRL2.24. Používateľ môže nastaviť frekvenciu výpočtov teploty na rovnakú ako deformáciu alebo po špecifickom uhle otáčania pomocou možností na karte Výpočet teploty. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}), kým nevytvoríte DB.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab2/image0024.jpg' | relative_url }})

Stránka s ovládacími prvkami Step a Remeshing

Všeobecné

Na stránke Generate DB kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) a vygenerujte databázu. Sledujte správu na karte Správa, ktorá informuje o stave generovania databázy.

## Simulácia behu

Po vygenerovaní databázy prepnite do režimu simulácie výberom tlačidla ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom objektov. Kliknutím na štítok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvorte dialógové okno Možnosti točenia, ako je znázornené na obr. RRL2.25.[]({{ '/docs/sk/labs/tool_life_study_lab/tool_life_study_lab1/' | relative_url }}#Fig_TLSL1_17_Run_Options_Popup) Použite predvolenú možnosť **Pokračovať v spustení** na výber možnosti „**Pokračovať z posledného kroku** “ (z kroku -1) a potom vyberte režim simulácie ako * * Interaktívny * * a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab2/image0025.jpg' | relative_url }})

Okno Spustiť simuláciu

Sledujte priebeh simulácie tak, že sa pozriete na kartu Simulation Message and Simulation Log a uistite sa, že je začiarknutá možnosť ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}). Používateľ môže zobraziť proces valcovania krúžku, keď simulácia pokračuje podľa zadaných kritérií zastavenia z grafiky simulácie.

Postprocessing

Po dokončení simulácie s „normálnym zastavením“ skontrolujte výsledky prepnutím do režimu Post pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) nad panelom nástrojov simulácie.

Prehrajte si kroky simulácie a pozrite sa, ako sa tvorí krúžok obrobku.

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_show_single_obj_icon.jpg' | relative_url }}) Režim jedného objektu výberom krúžku obrobku a grafu Efektívne napätie a Efektívne napätie krúžku obrobku. Pri prehrávaní krokov môžeme pozorovať nárast hodnoty deformácie ( obr. RRL2.26.). Hodnota efektívnej deformácie a napätia na konci simulácie by mala vyzerať tak, ako je znázornené na obr. RRL2.26.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab2/image0026.jpg' | relative_url }})

Preukázanie účinného namáhania a účinného stresu

Na nižšie uvedenom obr. RRL2.27 zobrazuje počiatočné a konečné rozmery krúžku. Na konci simulácie môže používateľ rozoznať rozdiel v priemere krúžku.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab2/image0027.jpg' | relative_url }})

Zobrazenie počiatočných a konečných rozmerov krúžku.

Konečný prierez krúžku je znázornený nižšie na obr. RRL2.28.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab2/image0028.jpg' | relative_url }})

Zobrazenie hrúbky prierezu pri rôznych zakriveniach po súťaži simulácie.

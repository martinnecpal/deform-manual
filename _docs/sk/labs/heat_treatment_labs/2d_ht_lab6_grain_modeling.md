---
lang: sk
title: "2D HT – laboratórna cvičenie č. 6: Modelovanie zŕn"
---

# 2D HT – laboratórna práca č. 6: Modelovanie zŕn

6.1. Úvod

6.2. Vytvorenie nového projektu a načítanie súboru s kľúčovými slovami deformácie

6.3. Špecifikácia údajov o materiáloch súvisiacich so zrnom

6.4. Zadanie počiatočných premenných zrna

6.5. Vytvorenie databázy a spustenie simulácie deformácie

6.6. Príprava a spustenie simulácie vzduchového chladenia

6.7. Príprava a spustenie simulácie kalenia vodou

6.8. Následné spracovanie

6.9. Meniace sa podmienky

## Úvod

Cieľom laboratórneho cvičenia je ukázať, ako používať model zŕn DEFORM na simuláciu vývoja mikrostruktúry zŕn počas procesov tvárnenia a tepelného spracovania.

Zohľadňujú sa štyri mechanizmy vývoja: statická rekryštalizácia, metadynamická rekryštalizácia, dynamická rekryštalizácia a rast zŕn. Z týchto štyroch mechanizmov dochádza k dynamickej rekryštalizácii počas deformácie, zatiaľ čo ostatné mechanizmy prebiehajú v obdobiach bez deformácie. Pre každý časový krok sa na základe aktuálneho času, lokálnej teploty, deformácie, rýchlosti deformácie a histórie vývoja určí mechanizmus vývoja a aktualizujú sa stavové premenné. V databáze je uložených šestnásť stavových premenných súvisiacich so zrnami, ktorých podrobný popis je k dispozícii v používateľskej príručke. Pre používateľov sú zvyčajne najzaujímavejšie podiel rekryštalizácie a priemerné veľkosti zŕn.

(Poznámka: Model zŕn DEFORM nevypočítava dynamickú rekryštalizáciu súbežne. Dynamická rekryštalizácia, ku ktorej by došlo počas deformácie, sa v skutočnosti vypočíta v kroku bezprostredne nasledujúcom po deformácii. To znamená, že používatelia neuvidia žiadne výsledky, pokiaľ po simulácii deformácie nenásleduje simulácia bez deformácie, napríklad proces tepelného spracovania. Okrem toho, aby bolo možné simulovať kompletný vývoj mikrostruktúry, mal by byť obrobok na konci simulácie dostatočne ochladený.)

V tomto laboratórnom cvičení je modelovaný jednoduchý proces zúženia, po ktorom nasleduje chladenie vzduchom a kalenie vodou. Úloha je osovo symetrická a používa jednotky SI. Materiál obrobku je IN718 a materiál matrice je oceľ H-13.

## Vytvorenie nového projektu a načítanie súboru s kľúčovými slovami deformácie

Na **počítači so systémom Windows** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), vyberte DEFORM-v1x.xxx (.xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte **DEFORM GUI Main** vxx.xx. Zobrazí sa hlavné okno DEFORM GUI Main, ako je znázornené nižšie na obr. 2DHTML6.1.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0001.jpg' | relative_url }})

Hlavné okno grafického rozhrania programu DEFORM

Vytvorte nový problém buď výberom položky **Súbor![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Nový problém**, alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému, ako je znázornené na obr. 2DHTML6.2. Vyberte prepínač „**Integrovaný výrobný proces**“ a ako systém jednotiek vyberte „**SI**“ pomocou prepínača. Názov úlohy zadajte ako „**GRAIN_LAB**“ a uistite sa, že je zaškrtnuté políčko „Zobraziť dialógové okno s možnosťami“ (ak nezaškrtnete políčko „**Zobraziť dialógové okno s možnosťami**“, v používateľskom rozhraní MO sa nezobrazí dialógové okno Nový projekt). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), aby ste otvorili nový problém s využitím integrovaného výrobného procesu Deform.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image014.jpg' | relative_url }})

Okno na výber typu problému

Spustí sa sprievodca MO spolu s oknom na zadanie názvu projektu, pričom ako názov projektu sa automaticky použije definovaný názov problému „**GRAIN_LAB**“ (pozri [Fig. 2DHTML6.3.]()).

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab6_grain_modeling/image0003.jpg' | relative_url }})

Okno na výber miesta problému

Používateľ môže tiež zmeniť systém jednotiek (systém jednotiek vybraný v ponuke Súbor sa nastaví ako predvolený); pre toto cvičenie vyberieme systém jednotiek **SI** a pridáme operáciu 2D tvárnenia zo zoznamu operácií v Průzkumníku, preto nezaškrtávajte políčko „Prvá operácia“ (pozri obr. 2DHTML6.4.). Pomocou možnosti „Kopírovať existujúci projekt“ môžeme importovať predtým uložené projekty ako nové projekty. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otváraní operácie.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab6_grain_modeling/image0004.jpg' | relative_url }})

Priradenie názvu problému

Otvorí sa sprievodca viacerými operáciami s novým projektom s názvom **GRAIN_LAB**. Zoznamu operácií v Průzkumníku pridajte operáciu **2D****Forming**. Operáciu pridáte kliknutím na tlačidlo vedľa položky 2D Forming alebo ju môžete pridať aj pretiahnutím do Editoru operácií. (Pozri obr. 2DHTML6.5.)

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab6_grain_modeling/image0005.jpg' | relative_url }})

Sprievodca MO s operáciou 2D tvárnenia

Načítajte súbor kľúčových slov **GRN_UPSET.KEY** z adresára DEFORM/v*/2D/LABS. Tento súbor kľúčových slov obsahuje všetky informácie potrebné na simuláciu kovania zúžením (pozri obr. 2DHTML6.6.).

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab6_grain_modeling/image0006.jpg' | relative_url }})

Načítanie súboru s kľúčom

## Zadajte údaje o materiáloch súvisiace so zrnom

V strome operácií vyberte vetvu riadenia simulácie a zaškrtnite políčko **Grain**, ako je znázornené na obr. 2DHTML6.7.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab6_grain_modeling/image0007.jpg' | relative_url }})

Zaškrtnutie políčka „Grain“

V strome operácií vyberte vetvu materiálu **IN718** v zozname materiálov. Na karte „Zrno“ vyberte model Avrami. Aktivujte meta-dynamickú rekryštalizáciu a rast zŕn a deaktivujte ostatné dve možnosti. Do príslušných matíc zadajte nasledujúce údaje.

Maximálne napätie:

Temp. |  a1 |  n1 |  m1 |  Q1 |  c1 |  a2  
---|---|---|---|---|---|---  
0 |  4,659e-3 |  0 |  0,1238 |  49 520 |  0 |  0,83  
  
Okrajová podmienka rýchlosti deformácie:

Teplota |  A |  b1 |  b2 |  Q2  
---|---|---|---|---  
0 |  0,01 |  0 |  0 |  0  
  
Kinetika metadynamickej rekryštalizácie:

Temp. |  a4 |  H4 |  n4 |  m4 |  Q4 |  Beta_m |  Km  
---|---|---|---|---|---|---|---  
0 |  3,794e-9 |  0 |  -1,42 |  -0,408 |  196 000 |  0,693 |  1  
  
Veľkosť zŕn pri metadynamickej rekryštalizácii:

Temp. |  a7 |  h7 |  n7 |  m7 |  Q7 |  c7  
---|---|---|---|---|---|---  
0 |  4,85e10 |  0 |  -0,41 |  -0,028 |  -240 000 |  0  
  
Rast zŕn:

Teplota |  M |  a9 |  Q9  
---|---|---|---  
0 |  2 |  9,44e+19 |  467 114,7  
  
Zadajte hodnotu **300** pre **Teplotný****limit**, pod ktorým sa vývoj zŕn nepočíta. Pre koeficient **Deformácie****udržania** ponechajte hodnotu **0**.

## Zadanie počiatočných premenných zrna

Vyberte objekt obrobku a kliknite na ikonu „Element Data ![]({{ '/assets/icons/pre_icons/mo_elemental_data_icon.jpg' | relative_url }})“. Kliknite na kartu **Grain** v časti „Microstructure“. Tu je možné definovať a zobraziť všetky premenné týkajúce sa zŕn. Inicializujte hodnoty **Average****Grain****Size** aj **Initial****Grain****Size** na hodnotu **100**, ako je znázornené na obr. 2DHTML6.8., pričom jednotkou je µm. Počiatočná veľkosť zŕn predstavuje veľkosť nekryštalizovaných zŕn. Upozorňujeme, že na zadanie údajov pre všetky prvky naraz budete musieť použiť tlačidlo „Inicializovať“. Kliknutím na tlačidlo „Zobraziť premenné“ ![]({{ '/assets/icons/pre_icons/mo_plot_icon.jpg' | relative_url }}) môžete zobraziť a overiť správnosť inicializácie.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab6_grain_modeling/image0008.jpg' | relative_url }})

Definovanie premenných zrna

## Vytvorenie databázy a spustenie simulácie deformácie

Na stránke „Generate DB“ kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), aby program skontroloval, či v nastaveniach úlohy niečo nechýba. Počas kontroly červené správy označujú údaje, ktoré je potrebné opraviť pred spustením simulácie (napríklad ak ste zabudli definovať údaje o materiáloch).

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), aby ste vytvorili databázu. Keď program dokončí zapisovanie databázy, prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) a spustite simuláciu.

Kliknite na popisok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}), čím otvoríte dialógové okno „Run Options“ (Možnosti spustenia), ako je znázornené na obr. 2DHTML6.9. Pomocou predvolenej možnosti **Pokračovať v spustení** vyberte možnosť „**Pokračovať od posledného kroku**“, potom nastavte režim simulácie na **Interaktívny** a kliknite na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}), čím spustíte simuláciu.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab6_grain_modeling/image0009.jpg' | relative_url }})

Okno „Spustiť simuláciu“

Priebeh simulácie je možné počas jej vykonávania sledovať na karte „Simulation Message“ a v časti „Simulation Graphics“ v oblasti zobrazenia „Graphics“ v režime simulácie. Pokiaľ je na karte „Simulation Message“ zaškrtnutá možnosť „![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }})“ (čo je predvolené nastavenie), súbor správ sa bude automaticky aktualizovať.

Súbor „Message“ obsahuje informácie o tom, v ktorom simulačnom kroku sa simulácia práve nachádza, a zároveň poskytuje údaje o tom, ako dobre simulácia prebieha.

Ak simulácia prebehne bez problémov, na koniec súboru so správami sa pridá nasledujúca správa: „Program sa zastavil!“

Hodnota STROKE -8,8530000 prekročila stanovený limit 8,8530000"

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab6_grain_modeling/image0010.jpg' | relative_url }})

Dokončenie prvej operácie

Po dokončení simulácie prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}), aby ste pridali druhú operáciu.

## Príprava a spustenie simulácie vzduchového chladenia

  
Pridajte 2D tvárniacu operáciu zo zoznamu operácií v prehliadači. Potom kliknite na druhú tvárniacu operáciu, aby sa otvorila. Po kliknutí na druhú operáciu sa zobrazí vyskakovacie okno s typom nastavenia; v ňom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_yes_interactive_setup_button.jpg' | relative_url }}), ako je znázornené na obr. 2DHTML6.11.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab6_grain_modeling/image0011.jpg' | relative_url }})

Výber typu interaktívnej inštalácie pre druhú operáciu

V strome operácií vyberte vetvu riadenia simulácie a **vypnite** začiarkavacie políčko **Deformácia**, ako je znázornené na obr. 2DHTML6.12.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab6_grain_modeling/image0012.jpg' | relative_url }})

Stránka „Riadenie simulácie“

Vyberte vetvu „Top Die Movement“ a nastavte rýchlosť na **0**, ako je znázornené na obr. 2DHTML6.13.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab6_grain_modeling/image0013.jpg' | relative_url }})

Odstránenie pohybu hornej matrice

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) v vetve „Ovládacie prvky“. Nastavte **posun** **hornej** **matrice** smerom nahor o **5** mm, ako je znázornené na obr. 2DHTML6.14. Ukončite dialógové okno „Polohovanie objektu“.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab6_grain_modeling/image0014.jpg' | relative_url }})

Stránka „Polohovanie objektov“

V prevádzkovom strome vyberte vetvu „Step control“ a v položke „Step Definition“ nastavte prírastok na **Constant****Time**. Zadajte **0,1** sekundy na krok. Počet **simulačných krokov** nastavte na **20** a **počet krokov na uloženie** na **5.** Týmto spôsobom namodelujete proces vzduchového chladenia trvajúci 2 sekundy (pozri obr. 2DHTML6.15.).

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab6_grain_modeling/image0015.jpg' | relative_url }})

Stránka riadenia simulácie druhej operácie

Vytvorte databázu a spustite simuláciu druhej operácie podľa pokynov v časti 6.5

Po dokončení simulácie prejdite do režimu ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}), aby ste pridali tretiu operáciu tvárnenia.

## Príprava a spustenie simulácie kalenia vodou

Pridajte 2D tvárniacu operáciu zo zoznamu operácií v prehliadači. Potom kliknite na tretiu tvárniacu operáciu, aby sa otvorila. Po kliknutí na tretiu operáciu sa zobrazí vyskakovacie okno s typom nastavenia; v ňom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_yes_interactive_setup_button.jpg' | relative_url }}), ako je znázornené na obr. 2DHTML6.16.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab6_grain_modeling/image0016.jpg' | relative_url }})

Výber typu interaktívnej inštalácie pre tretiu operáciu

Kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) v vetve „Ovládacie prvky“. Posuňte **spodnú****matricu** smerom nadol o **5** **mm**, ako je znázornené na obr. 2DHTML6.17. Ukončite dialógové okno „Polohovanie objektu“.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab6_grain_modeling/image0017.jpg' | relative_url }})

Stránka s pokynmi pre tretiu operáciu

V prevádzkovom strome vyberte vetvu „Step control“ a kliknutím na ikonu ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) prejdite do expertného režimu. Na karte **Spracovanie****Podmienky** zmeňte hodnotu **environmentálneho****konvekčného****koeficientu** na **15**, aby ste simulovali chladenie vodou.

Na karte „Step“ nastavte **počet****simulačných****krokov** na **100**. Nastavte definíciu kroku riešenia na konštantný **časový** prírastok. Zadajte **0,1** sekundy na krok (pozri obr. 2DHTML6.18 a obr. 2DHTML6.19).

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab6_grain_modeling/image0018.jpg' | relative_url }})

Určenie konvekčného koeficientu

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab6_grain_modeling/image0019.jpg' | relative_url }})

Stránka riadenia simulácie pre tretiu operáciu

Vytvorte databázu a spustite simuláciu druhej operácie podľa pokynov v časti 6.5.

## Následné spracovanie

Po dokončení simulácie prejdite na kartu ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}), kde si môžete prezrieť výsledky; otvorí sa postprocesor MO.

Otvorte okno „State Variable“ a zobrazte mikrostruktúru ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}), model zŕn ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) a priemernú veľkosť zŕn (pozri obr. 2DHTML6.20.). (Pre lepšie zobrazenie môže byť potrebné použiť metódu lokálneho škálovania.) Všimnite si, že, ako bolo spomenuté vyššie, účinky rekryštalizácie sa neprejavia, kým sa neukončí fáza deformácie. Ďalšou dôležitou premennou je „Rex. Vol. Fraction“ (pozri obr. 2DHTML6.21.), čo predstavuje celkový objemový podiel rekristalizovaného materiálu. V tomto prípade môžete vidieť, že spodná a pravá horná časť sochory vykazujú relatívne nižšiu rekristalizáciu kvôli nižšiemu deformovaniu. Objemový podiel rekristalizovaného materiálu a veľkosť zŕn pre konkrétny mechanizmus môžete zobraziť aj kliknutím na príslušné stavové premenné. Stavové premenné zŕn sú k dispozícii aj v časti „Element Data“ (Údaje o prvkoch). Okrem toho je možné tieto výsledky sledovať pomocou funkcie „Point-Tracked“ (Sledovanie bodov).

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab6_grain_modeling/image0020.jpg' | relative_url }})

Model zŕn Avrami – priemerná veľkosť zŕn

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab6_grain_modeling/image0021.jpg' | relative_url }})

Model obilnín Avrami – Rex. objemový podiel

## Meniace sa podmienky

Často je zaujímavé sledovať, ako sa mení konečná mikrostruktúra pri zmene podmienok spracovania. Môžete napríklad zmeniť dĺžku vzduchového chladenia z 2 sekúnd na 10 sekúnd a pozorovať tak výrazne odlišné konečné rozdelenie veľkostí zŕn. Môžete tiež zvýšiť koeficient „a4“ v „Meta-dynamickej kinetike rekryštalizácie“, aby ste urýchlili rekryštalizáciu atď. (Ak vás zaujímajú ďalšie údaje o materiáli týkajúce sa zŕn, načítajte „WASPALOY\[1750- 2100F(950-1150C)\](Grain)“ zo systémovej knižnice materiálov).

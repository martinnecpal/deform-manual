---
lang: sk
title: "Laboratórium valcovania krúžkov1"
---

# Ring Rolling Lab1

V tomto laboratóriu nastavíme jednoduchý model symetrie typu Ring Rolling.

1.1 Vytvorenie nového problému

1.2. Stránka procesu

1.3. Nastavenie simulácie

1.4. Výber objektu

1.4.1. Všeobecná stránka krúžku obrobku

1.4.2. Stránka objektu Driving Roll

1.4.3. Stránka objektu tlakového rolovania

1.5. Kontaktná stránka

1.6. Ovládacie prvky zastavenia

1.7. Ovládacie prvky Step a Remeshing Strana

1.8. Ovládacie prvky simulácie

1.9. Generovať databázu

1.10. Simulácia chodu

1.11. Post Processing

## Vytvorenie nového problému

Na ** zariadení so systémom Windows ** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), zvoľte DEFORM-v1x.xxx (.xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte * * DEFORM GUI Main * * vxx.xx. Zobrazí SA hlavné okno Deform GUI.

Vytvorte nový problém buď výberom **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})* ***Nový problém** alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Problem Setup (Nastavenie problému), ako je znázornené na obr. RRL1.1. Pomocou prepínača vyberte prepínač „ * * Integrated Manufacturing Process * *“ a systém jednotiek ako „** English * * “. Definujte názov problému ako "**RING_ROLL_LAB1** " a uistite sa, že je zapnuté začiarkavacie políčko "Zobraziť dialóg možností" (ak nezapneme začiarkavacie políčko "**Zobraziť dialóg možností ** ", potom nedostaneme dialógové okno Nový projekt v používateľskom rozhraní MO). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) a otvorte nový problém pomocou integrovaného výrobného procesu deformácie.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

Nový problém

V dialógovom okne Nový projekt sa otvorí sprievodca viacerými operáciami, v tomto bode sa používateľovi zobrazí výzva na zadanie názvu projektu (systém vytvorí samostatný priečinok s týmto názvom projektu) a názvu tejto relácie. V tejto relácii použijeme ako názov projektu „**RING_ROLL_LAB1** “. Operáciu 3D Ring Rolling je možné pridať aj v dialógu „Nový projekt“ (pozri obr. RRL1.2.), v tomto laboratóriu pridáme operáciu valcovania krúžku zo zoznamu operácií prieskumníka, takže nezačiarknite políčko "Prvá operácia" a operáciu "Valcovanie krúžku" v dialógovom okne "Nový projekt". Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) pokračujte v otvorení operácie.

Pridajte operáciu valcovania 3D prstenca zo zoznamu operácií prieskumníka. Pridajte operáciu kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}), ktoré je k dispozícii vedľa položky 3D Ring Rolling alebo používateľ môže tiež pridať presunutím myšou do editora prevádzky (pozri obr. RRL1.3.). Keď pridáme operáciu Ring Rolling, predvolene sa otvorí okno nastavení procesu.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0002.jpg' | relative_url }})

Pridanie operácie valcovania krúžku z nového projektu

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0003.jpg' | relative_url }})

Pridanie operácie valcovania krúžku z Prieskum

## Stránka procesu

Na stránke Proces sa predvolene vyberie prepínač „* * Valcovanie krúžku (predvolené) * * “ (pozri obr. RRL1.4.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na nastavenie simulácie.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0004.jpg' | relative_url }})

Stránka procesu

## Nastavenie simulácie

Vyberte prepínač „**Symetria * * “ typu 3D modelu a ponechajte predvolený typ tepelného výpočtu ako „**Konštantná teplota (izotermická)** “ na stránke nastavenia simulácie, ako je znázornené na obr. RRL1.5. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po stránku Objekty.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0005.jpg' | relative_url }})

Stránka nastavenia simulácie

Object Selection

Na stránke „* * Objekty * * “ použijeme aktuálne predvolené objekty, ako je znázornené na obr. RRL1.6. Na nastavenie jednoduchej operácie valcovania krúžku sú potrebné minimálne 3 predmety obrobku (krúžok), tlakový valec (tŕň) a hnací valec. V tomto laboratóriu nebudeme používať žiadny axiálny valec. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku Obrobok - krúžok definujete objekt krúžku.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0006.jpg' | relative_url }})

Zoznam objektov pre model symetrie

### Všeobecná stránka krúžku obrobku

Na stránke Obrobok-krúžok definujte teplotu objektu ako 70F, ako je znázornené na obr. RRL1.7, predvolený typ objektu pre obrobok (krúžok) je plast. V tomto laboratóriu vytvoríme obrobok, a preto ponecháme predvolené hodnoty, ako je znázornené na obr. RRL1.7. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku 2DCross- section.

#### Extrahujte prierez z 3D tvaru

V prípade, že používateľ importuje objekt zo súboru, potom Axis/Center možno vypočítať pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) a prierez extrakcie bude povolený tak, aby používateľ mohol extrahovať prierez importovaného objektu (pozri obr. RRL1.8.). Z importovaného objektu môže používateľ extrahovať jeden prierez z konkrétnej vrstvy pomocou „Extrahovať prierez na vrstve č.“ alebo môže používateľ extrahovať viac prierezov z rôznych vrstiev v prípade nerovnomerného krúžku a použiť priemernú veľkosť ako prierez pomocou „Extrahovať prierez z vrstiev a použiť ich priemer“.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0007.jpg' | relative_url }})

Strana krúžku obrobku

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0008.jpg' | relative_url }})

Extrahovať stranu prierezu

#### Prierez 2D krúžku obrobku Strana

Na stránke prierezu 2D obrobku kliknite na **![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }})**a definujte údaje súradníc, ako je znázornené na obr. RRL1.9. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte okno úprav a kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na 2D povrchovú sieť. V 2D Geometry má užívateľ tiež možnosti importovať 2D prierez pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) zo súboru alebo pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) z knižnice.

**X** |  **Y** |  **R**
---|---|---
4 |  3,25 |  0
4,75 |  3,25 |  0
4,75 |  4,5 |  0,062
3,75 |  4,5 |  0,03
3,75 |  3,25 |  0
4 |  3,25 |  0
  
![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0009.jpg' | relative_url }})

Stránka geometrie úpravy obrobku

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0010.jpg' | relative_url }})

Stránka 2D geometrie obrobku

#### Stránka 2D sieťoviny krúžku obrobku

V nastaveniach 2D povrchovej siete definujte **Cieľový počet prvkov** ako **80** a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) a sledujte vygenerovanú povrchovú sieť v okne povrchovej siete (pozri obr. RRL1.11.). Expertný režim je k dispozícii pre používateľa v prípade zložitých geometrií krúžkov na definovanie pokročilých podmienok povrchovej siete, ako sú okná oka, zmeny vážiacich faktorov atď., ako je znázornené na obr. RRL1.12. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na 3D geometriu.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0011.jpg' | relative_url }})

Stránka 2D povrchovej siete obrobku - Režim vedenia

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0012.jpg' | relative_url }})

2D sieťovina obrobku - režim Expert

#### Stránka 3D geometrie krúžku obrobku

Na stránke 3D geometrie kliknite na možnosť „** Otočiť z 2D** “ (pozri obr. RRL1.13.), použite predvolené hodnoty v Revolve from 2D page a zatvorte kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Ak používateľ nahral 3D geometriu obrobku zo súboru, potom je možné použiť možnosť Extrahovať prierez na extrakciu prierezu z 3D geometrie a použiť ju na otočenie do 3D geometrie. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na 3D povrchovú sieť.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0013.jpg' | relative_url }})

Stránka 3D geometrie obrobku - krúžok

#### Stránka 3D sieťoviny krúžku obrobku

Na stránke 3D Mesh máme možnosti vytvoriť sieť s rovnomerným prierezom alebo prispôsobiť 3D tvar v prípade obrobku s nerovnomerným prierezom. Pre toto laboratórium použijeme predvolenú hodnotu * * 120 * * pre „ **Počet otočných sekcií** “ a vygenerujeme 3D povrchovú sieť kliknutím na ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). Všimnite si, že vygenerovaná 3D sieť pre obrobok by mala vyzerať ako obr. RRL1.14. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku Orientácia obrobku.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0014.jpg' | relative_url }})

Stránka 3D sieťoviny krúžku obrobku

#### Orientácia obrobku

Obrobok je v uhle 0 od osi objektu po os +Z, takže nie je potrebné obrobok umiestňovať (pozri obr. RRL1.15.), kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na materiál obrobku.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0015.jpg' | relative_url }})

Orientačná stránka obrobku

#### Priradiť materiál krúžku obrobku

Na stránke Materiál kliknite na ikonu ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať materiál z knižnice) a načítajte materiál * * oceľ * * skupinový materiál " **AISI-5135H,STUDENÝ[70-550F (20-300C)]** " z okna knižnice materiálov. Priraďte materiál „**AISI-5135H,STUDENÝ[70-550F(20-300C)]** “ tak, že ho vyberiete pre obrobok. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Workpiece BCC.

#### Priradiť BCC pre krúžok obrobku

Skontrolujte predvolenú symetriu BCC priradenú pre obrobok, predvolená symetria BCC by mala byť priradená pre povrch symetrie, ako je znázornené na obr. RRL1.16. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až do stránky Driving Roll Object.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0016.jpg' | relative_url }})

Stránka stavu ohraničenia krúžku obrobku

**Poznámka k operácii valcovania krúžku pridaná ako druhá operácia v dávkovom režime:**

Operáciu valcovania krúžku je možné pridať ako druhú operáciu v dávkovom režime po predbežnom tvarovaní krúžku pomocou operácie tvárnenia alebo po operácii prenosu tepla. V takom prípade môže používateľ regenerovať krúžok začiarknutím políčka Regenerovať krúžok (pozri obr. RRL1.17.). Keď používateľ začiarkne políčko „ Regenerovať krúžok “, pridá sa stránka „Extrahovať prierez“, ktorá je prístupná pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) zo stránky objektu obrobku. Používateľ môže extrahovať geometriu prierezu pre 2D sieť prierezu pomocou možností zo stránky extrahovania prierezu objektu obrobku, dostupné možnosti sú uvedené na obr. RRL1.18.

Používateľ môže extrahovať jeden prierez pomocou možnosti „Extrahovať jeden prierez“ z karty „Konštantný prierez“. Ak chce používateľ jeden prierez z viacerých vrstiev nerovnomerného krúžku, môže extrahovať viac prierezov z rôznych vrstiev a použiť priemernú veľkosť ako prierez pomocou možnosti „Extrahovať viac prierezov z vrstiev a použiť ich priemer“.

Používateľ môže extrahovať viaceré prierezy a ponechať si ich na vytvorenie nerovnomerného krúžku pomocou možnosti „Extrahovať viaceré prierezy z vrstiev“ z karty „Variabilný prierez“

Keď používateľ regeneruje prsteň v dávkovom režime, prsteň sa automaticky zarovná na os Z a súradnica X jeho stredu sa presunie na „0“. Ak používateľ neregeneruje prsteň, prsteň sa zarovná na os Z bez úpravy súradníc stredu prsteňa.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0017.jpg' | relative_url }})

Čítať zo všeobecnej stránky obrobku DB

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0018.jpg' | relative_url }})

Čítať z DB obrobku Extrahovať stranu prierezu

### Stránka objektu šoférovania rolky

Meno hnacieho valca ponechajte nezmenené a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku geometrie prierezu 2D.

#### Prierez 2D riadiaceho valca Strana

Na stránke Geometria jazdného valca kliknite na ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}) a definujte údaje súradníc, ako je znázornené na obr. RRL1.19. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte okno úprav a kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na 3D geometriu.

**X** |  **Y** |  **R**
---|---|---
0 |  1,25 |  0
5 |  1,25 |  0
5 |  1,9875 |  0,025
4,66 |  2 |  0,093
4,66 |  4,5 |  0,093
5 |  4,525 |  0,025
5 |  5,25 |  0
0 |  5,25 |  0
  
![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0019.jpg' | relative_url }})

Driving Roll 2D Geometry page

#### Driving Roll 3D Geometry Page

Na stránke 3D geometrie kliknite na možnosť „** Otočiť z 2D** “, použite predvolenú hodnotu * * 100 * * pre „**Počet vrstiev v smere obruče ** “ v položke Otočiť z 2D stránky a zatvorte kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na orientáciu.

#### Orientácia na šoférovanie

Keď navštívime stránku Orientácia v predvolenom nastavení, valce budú v interferenčnej polohe s obrobkom, teraz sú obrobok a valce v správnej polohe, takže nie je potrebné robiť polohu. Takže kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Movement.

Orientačnú stránku je možné použiť na umiestnenie hnacieho valca pozdĺž osi zadaním vzdialenosti vzhľadom na stredy objektov alebo vzdialenosti medzi spodnými plochami objektov, pozri obr. RRL1.20.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0020.jpg' | relative_url }})

Orientačná stránka Driving Roll

#### Pohyb hnacieho valca

Vyberte ** Uhlovú rýchlosť** v ovládacích prvkoch rotačného pohybu pre hnací valec a definujte konštantnú hodnotu **20,943** rad/s. Všimnite si zelenú šípku otáčania zobrazujúcu smer otáčania v okne displeja (pozri obr. RRL1.21.). Kliknite na![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku Objekt v tlakovom valci.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0021.jpg' | relative_url }})

Stránka Driving Roll Movement

### Stránka objektu tlakového rolovania

Meno „Pressure Roll“ ponechajte nezmenené a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdite na stránku s prierezom 2D.

#### Tlakový valec 2D prierez Strana

Na stránke Pressure Roll 2D Geometry kliknite na ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}) a definujte údaje súradníc, ako je znázornené na obr. RRL1.22. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvorte okno úprav a kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na 3D geometriu.

**X** |  **Y** |  **R**
---|---|---
0 |  0 |  0
2 0
2 |  1,975 |  0,025
1,62 |  2 |  0,093
1,62 |  2,75 |  0
1,75 |  3,25 |  1,5
1,62 |  3,75 |  0
1,62 |  4,5 |  0,093
2 |  4,525 |  0,025
2 6
0 6
  
![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0022.jpg' | relative_url }})

Stránka Geometria tlakového kotúča

#### Stránka 3D geometrie tlakového valca

Na stránke 3D geometrie kliknite na možnosť "** Otočiť z 2D** ", použite predvolenú hodnotu * * 100 * * pre "**Počet vrstiev v smere obruče ** " na Otočiť z 2D stránky a kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) pre zatvorenie. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na orientáciu.

#### Orientácia tlakového valca

Teraz sú obrobok a valce v správnej polohe, takže nie je potrebné ich umiestňovať. Takže kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Movement.

Orientačná stránka môže byť použitá na umiestnenie tlakového valca pozdĺž osi zadaním vzdialenosti vzhľadom na stredy objektov alebo vzdialenosti medzi spodnými plochami objektov, pozri obr. RRL1.23.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0023.jpg' | relative_url }})

Orientačná stránka tlakového valca

#### Pohyb tlakového valca

Pohyb tlakového valca * * Rýchlosť ** definujeme ako „* * Funkciu času * * “, ako je uvedené nižšie v tabuľke a na obr. RRL1.24. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) až po stránku Kontakt.

**Čas** |  **Rýchlosť**
---|---
0 |  0,03
5 |  0,03
15 |  0,015
20 |  0,015
  
![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0024.jpg' | relative_url }})

Rýchlosť valenia tlaku ako funkcia pohybu času

Kontakty

Na stránke Kontakt použite predvolenú hodnotu šmykového trenia a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) vytvorte kontakty medzi hnacím valcom a obrobkom, ako aj medzi tlakovým valcom a obrobkom (pozri obr. RRL1.25.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku Zastavenie ovládacích prvkov.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0025.jpg' | relative_url }})

stránka s kontaktnými informáciami

## Zastavenie ovládacích prvkov

Vyberte položku Primárna matrica ako „**Tlakový valec (tŕň)** “a definujte hodnotu posunutia * * Y * * ako „**0,375** “ pod Max. posunutím primárnej matrice, ako je znázornené na obr. RRL1.26. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) definujte stránku krokových a remeshingových ovládacích prvkov.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0026.jpg' | relative_url }})

Stránka Zastavenie ovládacích prvkov

## Ovládacie prvky Step a Remeshing Strana

Zadajte počet krokov ako **20000** , prírastok rotácie na uloženie ako **360** a maximálny povolený časový krok ako **0,02**. Použite predvolený ovládací prvok Remeshing, ako je znázornené na obr. RRL1.27., túto možnosť môže používateľ zapnúť, aby objekt po zadanom počte otáčok zachoval dobrý tvar obrobku v prípade zložitých geometrií. Kliknite na ovládacie prvky simulácie ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0027.jpg' | relative_url }})

Stránka s ovládacími prvkami Step a Remeshing

## Ovládacie prvky simulácie

Na tejto stránke môže používateľ definovať obmedzenia pre stred obrobku, ako je znázornené na obr. RRL1.28. začiarknutím príslušného políčka.

Používateľ môže tiež pridať virtuálny stôl hore alebo dole začiarknutím príslušného políčka a zadaním vzdialenosti umiestnenia virtuálneho stola od horného / dolného povrchu.

Pomocou pokročilých nastavení na karte Rozšírené ovládanie môže používateľ definovať frekvenciu krokov na overenie penetrácie uzla v prípade, že používateľ pozoruje silnú penetráciu do kotúčov. Používateľ môže tiež špecifikovať uhol pre vyhľadávanie kontaktov, aby sa zvýšila rýchlosť riešenia.

Ak sa predmet krúžku neotáča správne, používateľ môže skontrolovať „Vynútiť otáčanie obrobku, keď sa v určitých krokoch neotáča dobre“, aby vykonal malé korekcie otáčania krúžku počas procesu valcovania krúžku.

Údaje definované na tejto stránke sa zapíšu do súboru **DEF_RRE.DAT* *.

V tomto laboratóriu použijeme predvolené nastavenia a kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) vygenerujeme stránku DB.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0028.jpg' | relative_url }})

a. Kontroly stability

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0029.jpg' | relative_url }})

b. Pokročilé ovládacie prvky

Ovládacie prvky simulácie

Všeobecné

Na stránke Generate DB kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) a vygenerujte databázu. Sledujte správu na karte Správa, ktorá informuje o stave generovania databázy.

## Simulácia behu

Po vygenerovaní databázy prepnite do režimu simulácie výberom tlačidla ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom objektov. Kliknutím na štítok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvorte dialógové okno Možnosti točenia, ako je znázornené na obr. RRL1.29. Pomocou predvolenej možnosti **Pokračovať v spustení** vyberte možnosť „**Pokračovať z posledného kroku** “ (z kroku -1) a potom vyberte režim simulácie ako **Interaktívny** a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0035.jpg' | relative_url }})

Okno Spustiť simuláciu

Sledujte priebeh simulácie tak, že sa pozriete na kartu Simulation Message and Simulation Log a uistite sa, že je začiarknutá možnosť ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}). Používateľ môže zobraziť proces valcovania krúžku, keď simulácia pokračuje podľa zadaných kritérií zastavenia z grafiky simulácie.

Postprocessing

Po dokončení simulácie s „normálnym zastavením“ skontrolujte výsledky prepnutím do režimu Post pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) nad panelom nástrojov simulácie.

Prehrajte si kroky simulácie a pozrite sa, ako sa tvorí krúžok obrobku.

Kliknite na 3D zrkadlenie a pridajte symetriu v rovine symetrie obrobku - krúžok.

Kliknite na ![]({{ '/assets/icons/pre_icons/mo_show_single_obj_icon.jpg' | relative_url }}) Režim jedného objektu výberom krúžku obrobku a grafu Efektívne napätie a Efektívne napätie krúžku obrobku. Pri prehrávaní krokov môžeme pozorovať nárast hodnoty napätia. Hodnota efektívnej deformácie a napätia na konci simulácie by mala vyzerať tak, ako je znázornené na obr. RRL1.30.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0030.jpg' | relative_url }})

Preukázanie účinného namáhania a účinného stresu

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0031.jpg' | relative_url }})

Zobrazenie krúžku po dokončení simulácie

Nižšie uvedený obrázok RRL1.32. zobrazuje počiatočné a konečné rozmery krúžku. Na konci simulácie môže používateľ rozoznať rozdiel v priemere krúžku.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0032.jpg' | relative_url }})

Počiatočné a konečné rozmery krúžku.

Konečný prierez krúžku je znázornený na obr. RRL1.33. a chyba plutvy pri valcovaní krúžku je znázornená na obr. RRL1.34.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0033.jpg' | relative_url }})

Zobrazenie hrúbky prierezu po ukončení simulácie pri rôznych zakriveniach.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0034.jpg' | relative_url }})

Zobrazuje sa chyba plutvy pri valcovaní krúžku

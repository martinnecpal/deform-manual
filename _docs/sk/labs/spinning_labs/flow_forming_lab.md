---
lang: sk
title: "Flow Forming Lab"
---

# Flow Forming Lab

V tomto laboratóriu nastavíme jednoduchý proces tvárnenia Forward Flow.

1.1. Vytvorenie nového problému

1.2. Stránka procesu

1.3. Nastavenie simulácie

1.4. Výber objektov

1.5. Obrobok

1.6. Vreteno

1.7. Hlavové zásoby

1.8. Koncový materiál

1.9. Roll 1

1.10. Roll 2

1.11. Roll 3

1.12. Priechodný stôl

1.13. Ovládacie prvky

1.14. Kontakt

1.15. Ovládacie prvky zastavenia

1.16. Ovládacie prvky simulácie

1.17. Generovať databázu

1.18. Simulácia chodu

1.19. Po spracovaní

## Vytvorenie nového problému

Na ** zariadení so systémom Windows ** prejdite na tlačidlo ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}), zvoľte DEFORM-v1x.xxx (.xxx označuje číslo verzie, napr. v14.0.2) a z ponuky vyberte * * DEFORM GUI Main * * vxx.xx. Zobrazí SA hlavné okno Deform GUI.

Vytvorte nový problém buď výberom **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})* ***Nový problém** alebo kliknutím na ikonu Nový problém ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}). Zobrazí sa okno Nastavenie problému, ako je znázornené na obr. 3DFFL1.1. Pomocou prepínača vyberte prepínač „ * * Integrovaný výrobný proces * *“ a systém jednotiek ako „** Angličtina * * “. Definujte názov problému ako "** Flowformlab * * " a uistite sa, že je zapnuté začiarkavacie políčko "Zobraziť dialóg možností" (ak nezapneme začiarkavacie políčko "**Zobraziť dialóg možností ** ", potom nedostaneme dialógové okno Nový projekt v používateľskom rozhraní MO). Potom kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) a otvorte nový problém pomocou integrovaného výrobného procesu deformácie.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

Nový problém

Sprievodca viacerými operáciami sa otvorí v dialógovom okne Nový projekt. V tomto bode sa používateľovi zobrazí výzva na zadanie názvu projektu (systém vytvorí samostatný priečinok s týmto názvom projektu) a názvu tejto relácie. V tejto relácii použijeme ako názov projektu „** Flowformlab * * “. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) pokračujte v otváraní nového projektu.

Pridajte operáciu 3D Spinning zo zoznamu Explorer Operations (Operácie prieskumníka). Pridajte operáciu kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}), ktoré je k dispozícii vedľa 3D Spinning, alebo ho môžete pridať aj presunutím myšou do editora operácií (pozri obr. 3DFFL1.2.). Keď pridáme operáciu Spinning, Keď pridáme operáciu Spinning, Ak je aktuálny smer obrazovky smerom nahor "* * Z * * ", potom sa dostaneme pod vyskakovacie okno. V kontextovom okne „Change screen upward axis“ (Zmeniť obrazovku smerom nahor) kliknite na „** YES-Change * *“ (Zmeniť). V predvolenom nastavení sa otvorí okno nastavení procesu. Operáciu 3D Spinning je možné pridať aj v dialógovom okne "Nový projekt" v MO.

![]({{ '/assets/images/labs/spinning_labs/flow_forming_lab/image0002.jpg' | relative_url }})

Pridanie operácie 3D Spinning

## Stránka procesu

Na stránke Proces vyberte "** Formovanie toku ** " a typ formovania toku ako "**Vpred** ". Definujte vreteno **Rotačná****rýchlosť** ako **300** ot./min., pozri obr. 3DFFL1.3. Táto rýchlosť otáčania sa použije na hlavový a koncový materiál. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku nastavenia simulácie.

![]({{ '/assets/images/labs/spinning_labs/flow_forming_lab/image0003.jpg' | relative_url }})

Stránka procesu

## Nastavenie simulácie

Na stránke Simulation Setup (Nastavenie simulácie) vyberte metódu riešenia ako „* * ale * * “ a typ riešiteľa ako „**Explicit** “. V tomto laboratóriu nebudeme vykonávať žiadne tepelné výpočty, preto vyberte Tepelný výpočet ako „**Konštantná teplota (izotermická)** “ (pozri obr. 3DFFL1.4). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) nastavíte explicitné ovládacie prvky riešiteľa nasledovne.

![]({{ '/assets/images/labs/spinning_labs/flow_forming_lab/image0004.jpg' | relative_url }})

Stránka nastavenia simulácie

* Nastavte ** Koeficient tlmenia ** na **1**. To tlmí vibrácie. Nastavenie 0-1 je konzervatívne a 5-10 je agresívnejšie.

* Nastaviť **Hmotnosť****škálovanie****faktor** na **200**. To ovplyvňuje časový krok, presnosť a dobu chodu. Nižší faktor hmotnostnej mierky má za následok menší časový krok a väčšiu presnosť, ale vyžaduje dlhší čas simulácie. To je možné upraviť podľa potreby na základe skúseností, aplikácie a cieľov.

* Nastavte **Cyklus** na **100**. Týmto sa riadi pomer explicitných cyklov riešenia na krok. Kombináciu tohto nastavenia a prírastku uloženia kroku databázy možno použiť na nastavenie toho, ako často sa cykly zapisujú do databázy. Nastavenie 0 má za následok 1 cyklus na krok (pomer 1:1). Nastavenie 100 má za následok 100 cyklov na krok (pomer 100:1). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvoríte stránku s nastaveniami explicitných riešiteľov. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na objekty.

![]({{ '/assets/images/labs/spinning_labs/flow_forming_lab/image0005.jpg' | relative_url }})

Explicitné nastavenia riešiteľov

## Výber objektov

Na stránke „**Počet objektov** “ definujte počet valcov ako **3** , v nižšie uvedenej tabuľke Počet kotúčov môže používateľ definovať uhol medzi kotúčmi, pre toto laboratórium použijeme predvolenú hodnotu * * 120 * * ° pre ![]({{ '/assets/images/labs/spinning_labs/flow_forming_lab/theta1.jpg' | relative_url }}) a ![]({{ '/assets/images/labs/spinning_labs/flow_forming_lab/theta2.jpg' | relative_url }}). Začiarknite políčko Tŕň, Hlava a Chvost (ak nie je začiarknuté) (pozri obr. 3DFFL1.6.), ak chcete tieto predmety použiť v nastavení. Koncový materiál sa nepoužíva v procese tvárnenia pri spätnom toku a voliteľne v tvarovaní pri doprednom toku. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na všeobecnú stránku obrobku.

![]({{ '/assets/images/labs/spinning_labs/flow_forming_lab/image0006.jpg' | relative_url }})

Object Selection

## Obrobok

Na stránke objektu obrobku ponechajte predvolené hodnoty pre názov obrobku a teplotu 68° F. Zmeňte typ objektu na „**Elasto-plastic** “, ako je znázornené na obr. 3DFFL1.7., pre explicitné nastavenia simulácie typu riešiteľa musí byť obrobok typu Elasto-plastic object. Kliknite na stránku prierezu ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na geometriu 2D.

![]({{ '/assets/images/labs/spinning_labs/flow_forming_lab/image0007.jpg' | relative_url }})

Stránka obrobku

### 2D prierez obrobku

Importujte 2D geometriu, „**workpiece_lab.GEO** “ zo zložky 3D/LABS/Spinning. Na tejto stránke môžete upraviť, skontrolovať alebo uložiť 2D geometriu, ako je znázornené na obr. 3DFFL1.8. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Mesh.

![]({{ '/assets/images/labs/spinning_labs/flow_forming_lab/image0008.jpg' | relative_url }})

Geometria obrobku 2D prierez strana

### Sieťovina obrobku

Definujte počet prvkov pre 2D prierez ako 100 a kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_2d_mesh_button.jpg' | relative_url }}). Definujte **Počet otočných profilov** ako **100** , vyberte „**Rovnomerná hrúbka vrstiev v smere obruče ** “, ktorá je preferovaná pre explicitný riešiteľ a kliknite na ![]({{ '/assets/icons/pre_icons/mo_generate_3d_mesh_button.jpg' | relative_url }}). Vygenerovaná 2D a 3D sieť by mala vyzerať tak, ako je znázornené na obr. 3DFFL1.9. a obr. 3DFFL1.10. Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na materiál.

![]({{ '/assets/images/labs/spinning_labs/flow_forming_lab/image0009.jpg' | relative_url }})

Vygenerované 2D pletivo pre obrobok

![]({{ '/assets/images/labs/spinning_labs/flow_forming_lab/image0010.jpg' | relative_url }})

Vygenerované 3D pletivo pre obrobok

### Priradiť materiál pre obrobok

Na stránke Materiál kliknite na ikonu ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Načítať materiál z knižnice) a načítajte materiál * * Hliník * * skupinový materiál "**AL-3003,COLD[70-250F (20-120C)]** " z okna knižnice materiálov. Priraďte materiál „**AL-3003,COLD[70-250F(20-120C)]** “ pre obrobok, ako je znázornené na obr. 3DFFL1.11. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) do stránky Mandrel.

![]({{ '/assets/images/labs/spinning_labs/flow_forming_lab/image0011.jpg' | relative_url }})

Stránka Materiál obrobku

Priebojník

Na všeobecnej stránke vretena ponechajte predvolené hodnoty pre názov vretena a teplotu 68 °F. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku 2D prierezu geometrie.

### Geometria vretena - 2D prierez

Importujte 2D geometriu, „**tŕň_lab.GEO** “ z priečinka 3D/LABS/Spinning. Na tejto stránke môžete upraviť, skontrolovať alebo uložiť 2D geometriu, ako je znázornené na obr. 3DFFL1.12. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Geometry - 3D page.

![]({{ '/assets/images/labs/spinning_labs/flow_forming_lab/image0012.jpg' | relative_url }})

Geometria vretena - 2D prierez

### Geometria vretena 3D

Pomocou predvoleného nastavenia „**Počet otočených sekcií** “ ako * * 100 * * vygenerujte 3D geometriu kliknutím na možnosť ![]({{ '/assets/icons/pre_icons/mo_generate_3d_geometry_button.jpg' | relative_url }}) (pozri obr. 3DFFL1.13.). Fine Geometry at Contact region (Jemná geometria v oblasti kontaktu) sa pre explicitný riešiteľ nevyžaduje, preto ho môžete ponechať nezaškrtnuté. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku nastavenia referenčného bodu.

![]({{ '/assets/images/labs/spinning_labs/flow_forming_lab/image0013.jpg' | relative_url }})

Geometria vretena-3D

### Nastavenie referenčného bodu vretena

Na tejto stránke môžeme definovať referenčný bod tŕňa, použijeme predvolenú hodnotu D "* * 1.99 * * ", ako je znázornené na obr. 3DFFL1.14. „**D * * “ je vzdialenosť medzi začiatkom deformácie a začiatkom vretena pozdĺž osi X a použije sa na umiestnenie vretena. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku Head Stock.

![]({{ '/assets/images/labs/spinning_labs/flow_forming_lab/image0014.jpg' | relative_url }})

Stránka nastavenia referenčného bodu vretena

## Head Stock

Na všeobecnej stránke Head Stock ponechajte predvolené hodnoty pre názov ako Head stock a teplotu ako 68°F. Kliknite na stránku prierezu ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na geometriu 2D.

### Geometria hlavových zásob - 2D prierez

Importujte 2D geometriu, „**Headstock_lab.GEO** “ z priečinka **3D/LABS/Spinning**. Na tejto stránke môžete upraviť, skontrolovať alebo uložiť 2D geometriu, ako je znázornené na obr. 3DFFL1..15. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Geometry - 3D page.

![]({{ '/assets/images/labs/spinning_labs/flow_forming_lab/image0015.jpg' | relative_url }})

Hlava pažby Geometria - 2D prierez

### Head Stock 3D - Geometria

Pomocou predvoleného nastavenia „**Počet otočených sekcií** “ ako * * 100 * * vygenerujte 3D geometriu kliknutím na možnosť ![]({{ '/assets/icons/pre_icons/mo_generate_3d_geometry_button.jpg' | relative_url }}) (pozri obr. 3DFFL1.16.). Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Tail stock.

![]({{ '/assets/images/labs/spinning_labs/flow_forming_lab/image0016.jpg' | relative_url }})

Head stock Geometry-3D strana

## Koncový materiál

Na stránke Tail Stock General ponechajte predvolené hodnoty pre názov ako Tail stock a teplotu ako 68°F. Kliknite na stránku prierezu ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na geometriu 2D.

### Geometria chvosta - 2D prierez

Importujte 2D geometriu, „**tailstock_lab.GEO** “ z priečinka 3D/LABS/Spinning. Na tejto stránke môžete upraviť, skontrolovať alebo uložiť 2D geometriu, ako je znázornené na obr. 3DFFL1.17. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Geometry - 3D page.

![]({{ '/assets/images/labs/spinning_labs/flow_forming_lab/image0017.jpg' | relative_url }})

Geometria chvosta - 2D prierez

### Chvostová pažba 3D - geometria

Pomocou predvoleného nastavenia „**Počet otočených sekcií** “ ako * * 100 * * vygenerujte 3D geometriu kliknutím na možnosť ![]({{ '/assets/icons/pre_icons/mo_generate_3d_geometry_button.jpg' | relative_url }}) (pozri obr. 3DFFL1.18.). Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Roll.

![]({{ '/assets/images/labs/spinning_labs/flow_forming_lab/image0018.jpg' | relative_url }})

Chvostová geometria-3D strana

## Roll 1

Na všeobecnej stránke Roll 1 ponechajte predvolené hodnoty pre name ako Roll 1 a teplotu ako 68°F. Kliknite na stránku prierezu ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na geometriu 2D.

### Geometria role 1 - 2D prierez

Importujte 2D geometriu, „**roller_lab.GEO** “ z priečinka **3D/LABS/Spinning**. Na tejto stránke môžete upraviť, skontrolovať alebo uložiť 2D geometriu, ako je znázornené na obr. 3DFFL1.19. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Geometry - 3D page.

![]({{ '/assets/images/labs/spinning_labs/flow_forming_lab/image0019.jpg' | relative_url }})

Geometria rolky 1 - 2D prierez

### 3D geometria role 1

Pomocou predvoleného nastavenia „**Počet otočených sekcií** “ ako * * 100 * * vygenerujte 3D geometriu kliknutím na možnosť ![]({{ '/assets/icons/pre_icons/mo_generate_3d_geometry_button.jpg' | relative_url }}) (pozri obr. 3DFFL1.20.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na orientačnú stránku.

![]({{ '/assets/images/labs/spinning_labs/flow_forming_lab/image0020.jpg' | relative_url }})

Roll 1 Geometry-3D page

### Orientácia role 1

Na tejto stránke môžeme upraviť orientačný uhol Roll pomocou možnosti Roll Orientation angle a tiež je možné zvoliť počiatočný bod Roll pomocou možností nastavenia počiatočného bodu Roll.

V tomto laboratóriu nemeníme orientačný uhol a počiatočný bod Roll Rolls, takže kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku Roll 2 bez akýchkoľvek zmien.

![]({{ '/assets/images/labs/spinning_labs/flow_forming_lab/image0021.jpg' | relative_url }})

Orientačná stránka Roll1

## Roll 2

Na všeobecnej stránke Roll 2 ponechajte predvolené hodnoty pre name ako Roll 2 a teplotu ako 68°F. Kliknite na stránku prierezu ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na geometriu 2D.

### Geometria role 2 - 2D prierez

Importujte 2D geometriu, „**roller_lab.GEO** “ z priečinka 3D/LABS/Spinning. Na tejto stránke môžete upraviť, skontrolovať alebo uložiť 2D geometriu, ako je znázornené na obr. 3DFFL1.19. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Geometry - 3D page.

### Roll 2 3D - Geometria

Pomocou predvoleného "Počet otočených sekcií" ako 100 vygenerujte 3D geometriu kliknutím na možnosť ![]({{ '/assets/icons/pre_icons/mo_generate_3d_geometry_button.jpg' | relative_url }}) (pozri obr. 3DFFL1.20.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na orientačnú stránku.

### Orientácia role 2

V tomto laboratóriu nemeníme orientačný uhol a počiatočný bod Roll Rolls, takže kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku Roll 3 bez akýchkoľvek zmien.

## Roll 3

Na všeobecnej stránke Roll 3 ponechajte predvolené hodnoty pre name ako Roll 3 a teplotu ako 68°F. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku 2D prierezu geometrie.

### Geometria role 3 - 2D prierez

Importujte 2D geometriu, „**roller_lab.GEO** “ z priečinka **3D/LABS/Spinning**. Na tejto stránke môžete upraviť, skontrolovať alebo uložiť 2D geometriu, ako je znázornené na obr. 3DFFL1.19. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Geometry - 3D page.

### Roll 3 3D-Geometry

Pomocou predvoleného nastavenia „**Počet otočených sekcií** “ ako * * 100 * * vygenerujte 3D geometriu kliknutím na možnosť ![]({{ '/assets/icons/pre_icons/mo_generate_3d_geometry_button.jpg' | relative_url }}) (pozri obr. 3DFFL1.20.). Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na orientačnú stránku.

### Orientácia rolky 3

V tomto laboratóriu nemeníme orientačný uhol a počiatočný bod Roll Rolls, kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) prejdete na stránku tabuľky.

## Tabuľka preukazov

Tu budeme definovať rýchlosť valcov pozdĺž osi vretena ako **0,25** v/s. V tomto laboratóriu budeme uvažovať o rotácii valcov na základe voľného krútiaceho momentu, preto vyberieme **Krútiaci moment** na karte Rotácia a definujeme jeho hodnotu ako**0 klb-in**. Takže kliknite na tlačidlo Roll 1 ![]({{ '/assets/icons/pre_icons/mo_edit..._2_button.jpg' | relative_url }}) v tabuľke Pass a definujte **rýchlosť * * ako * *0,25 * * v/s a krútiaci moment ako 0 klb-in, ako je znázornené na obr. 3DFFL1.23. a kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) pre zatvorenie stránky pohybu. Definujte rovnaké údaje o pohybe na stránke pohybu Roll 2 a Roll 3 kliknutím na príslušné tlačidlo. V súčasnosti nedefinujeme žiadne iné údaje z tabuľky Pass. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku Ovládacie prvky.

![]({{ '/assets/images/labs/spinning_labs/flow_forming_lab/image0022.jpg' | relative_url }})

Stránka tabuľky Pass

![]({{ '/assets/images/labs/spinning_labs/flow_forming_lab/image0023.jpg' | relative_url }})

Roll 1 Movement page

Príkazy

Kliknite na "**Automatické polohovanie** ", definujte parametre

**D=8,6** , Vzdialenosť medzi povrchom hlavy a dátumovým bodom valenia

**K=10** , orientačný uhol valcov s obrobkom

**A1=0,15** , **A2=0,3** , bočná vzdialenosť medzi valcami pozdĺž osi tŕňa

Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) zmeníte nastavenia aplikácie. Umiestni všetky 3 valce a obrobok a chvost do správnej polohy, ako je znázornené na obr. 3DFFL1.24. Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) zatvoríte stránku Automatická pozícia. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku Kontakt.

![]({{ '/assets/images/labs/spinning_labs/flow_forming_lab/image0024.jpg' | relative_url }})

Okno automatickej polohy

Kontakt

Nastavenie Flowforming predpokladá nízke šmykové trenie pre tŕň a koník. Bude to podobné tvárneniu za studena, keď materiál kĺže po povrchu matrice. Pre valček sa predpokladá vysoké šmykové trenie, typické pre valcovanie. Lokálne vyhľadávanie kontaktov sa používa na skrátenie času výpočtu vyhľadávania kontaktov, čo je užitočné pri explicitných simuláciách. Pre každý pár objektov musia byť definované trecie okná nad oblasťou nástroja, kde môže dôjsť k kontaktu. Oblasti mimo okna nebudú považované za kontaktné. Nastavenia trenia nachádzajúce sa v ponuke trecieho okna majú prednosť pred globálnymi nastaveniami. Trecie okná musia byť nastavené tak, aby sa v prípade potreby riadili pohyblivými nástrojmi.

Na stránke Kontakt vyberte typ „**User** “ a kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}). V tabuľke budeme sledovať pridávané predvolené vzťahy a prilepený kontakt bude skontrolovaný na chvostový materiál - obrobok a hlavový materiál - vzťahy obrobku. Pre toto laboratórium zapneme začiarkavacie políčko Tŕň - Prilepenie obrobku a vypneme začiarkavacie políčko Hlava - Prilepenie obrobku a ako je znázornené na obr. 3DFFL1.30.

* Vyberte vzťah **Tŕň - obrobok** a ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}). Definujte **strih** trenie **0,12**. Prepnite na kartu Friction Window (Okno trenia). Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) pridáte nové okno. Kliknite na tlačidlo Plný valec na paneli s nástrojmi, ktorý sa nachádza pozdĺž úplne ľavej strany obrazovky. Kliknutím na ľubovoľné miesto na modeli umiestnite okno. Kliknutím na ikonu ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) definujte veľkosť okna, ako je znázornené na obr. 3DFFL1.25., kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Vyberte šmykové trenie a nastavte konštantnú hodnotu * * 0,12 * * a vyberte "* * Tŕň * * " ako objekt na sledovanie okna, kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/spinning_labs/flow_forming_lab/image0025.jpg' | relative_url }})

Tŕň - definícia okna obrobku

* Vyberte **Head stock - Workpiece** vzťah a ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}). Definujte šmykové trenie 0,12 a kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}).

* Vyberte ** Vzťah chvost - obrobok** a ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}). Definujte **Strih** trenie **1**. Prepnite na kartu Friction Window (Okno trenia). Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) pridáte nové okno. Kliknite na tlačidlo Plný valec na paneli s nástrojmi, ktorý sa nachádza pozdĺž úplne ľavej strany obrazovky. Kliknutím na ľubovoľné miesto na modeli umiestnite okno. Kliknutím na ikonu ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) definujte veľkosť okna, ako je znázornené na obr. 3DFFL1.26., kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Vyberte možnosť Šmykové trenie a nastavte konštantnú hodnotu 1 a ako objekt, ktorý chcete sledovať, vyberte možnosť „Koncový materiál“, kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}).

![]({{ '/assets/images/labs/spinning_labs/flow_forming_lab/image0026.jpg' | relative_url }})

Koncový materiál - definícia okna obrobku

* Vyberte vzťah **Roll 1 -Obrobok* * a ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}). Definujte **strih** trenie **0,12**. Prepnite na kartu Friction Window (Okno trenia). Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) pridáte nové okno. Kliknite na tlačidlo Dutý valec na paneli s nástrojmi, ktorý sa nachádza pozdĺž úplne ľavej strany obrazovky. Kliknutím na ľubovoľné miesto na modeli umiestnite okno. Kliknutím na ikonu ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) definujte veľkosť okna, ako je znázornené na obr. 3DFFL1.27., kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Vyberte šmykové trenie a nastavte konštantnú hodnotu 0,12 a vyberte "Roll 1" ako objekt na sledovanie okna, kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}).

![]({{ '/assets/images/labs/spinning_labs/flow_forming_lab/image0027.jpg' | relative_url }})

Roll 1 - Definícia okna obrobku

* Vyberte vzťah **Roll 2 -Obrobok* * a ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}). Definujte **šmykové* ***trenie** z **0,12**. Prepnite na kartu Friction Window (Okno trenia). Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) pridáte nové okno. Kliknite na tlačidlo Dutý valec na paneli s nástrojmi, ktorý sa nachádza pozdĺž úplne ľavej strany obrazovky. Kliknutím na ľubovoľné miesto na modeli umiestnite okno. Kliknutím na ikonu ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) definujte veľkosť okna, ako je znázornené na obr. 3DFFL1.28., kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Vyberte šmykové trenie a nastavte konštantnú hodnotu 0,12 a vyberte "Roll 2" ako objekt na sledovanie okna, kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}).

![]({{ '/assets/images/labs/spinning_labs/flow_forming_lab/image0028.jpg' | relative_url }})

Roll 2 - Definícia okna obrobku

* Vyberte vzťah **Roll 3 -Obrobok* * a ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}). Definujte **Šmykové trenie** s hodnotou **0,12**. Prepnite na kartu Friction Window (Okno trenia). Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) pridáte nové okno. Kliknite na tlačidlo **Dutý valec** na paneli s nástrojmi, ktorý sa nachádza na ľavej strane obrazovky. Kliknutím na ľubovoľné miesto na modeli umiestnite okno. Kliknutím na ikonu ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) definujte veľkosť okna, ako je znázornené na obr. 3DFFL1.29., kliknite na ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Vyberte šmykové trenie a nastavte konštantnú hodnotu 0,12 a vyberte "* * Roll 3 * * " ako objekt na sledovanie okna, kliknite na tlačidlo![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) .

![]({{ '/assets/images/labs/spinning_labs/flow_forming_lab/image0029.jpg' | relative_url }})

Roll 3 - Definícia okna obrobku

Kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) vypočítajte predvolenú hodnotu tolerancie a vytvorte kontakt kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) a tiež vyberte možnosť Áno v kontextovom okne „** STAV PRILEPENIA ** “. Vygenerovaný kontakt bude vyzerať tak, ako je znázornené na obr. 3DFFL1.30. Kliknite na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na stránku Zastavenie ovládacích prvkov.

![]({{ '/assets/images/labs/spinning_labs/flow_forming_lab/image0030.jpg' | relative_url }})

Kontakty

## Zastavenie ovládacích prvkov

Definujte ** Trvanie procesu ** ako **10** s na stránke Ovládacie prvky zastavenia (pozri obr. 3DFFL1.31). Kliknite na stránku ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) na ovládacie prvky simulácie.

![]({{ '/assets/images/labs/spinning_labs/flow_forming_lab/image0031.jpg' | relative_url }})

Stránka Kritériá zastavenia

## Ovládacie prvky simulácie

Zadajte **Počet krokov** ako **10000** , ** Prírastok krokov na uloženie** ako **100** a **Čas** na krok ako **0,001** na stránke Ovládacie prvky simulácie (pozri obr. 3DFFL1.32.). Kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) vygenerujete stránku DB.

![]({{ '/assets/images/labs/spinning_labs/flow_forming_lab/image0032.jpg' | relative_url }})

Stránka s ovládacími prvkami simulácie

Všeobecné

Na stránke Generate DB kliknite na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) a vygenerujte databázu. Sledujte správu na karte Správa, ktorá informuje o stave generovania databázy.

## Simulácia behu

Po vygenerovaní databázy prepnite do režimu simulácie výberom tlačidla ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) nad stromom objektov. Kliknutím na štítok akcie ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) otvorte dialógové okno Možnosti točenia, ako je znázornené na obr. 3DFFL1.33. Použite predvolenú možnosť **Pokračovať v točení * * a vyberte možnosť „* *Pokračovať z posledného kroku** “ a potom vyberte režim simulácie ako * * Interaktívny * * a kliknutím na tlačidlo ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) spustite simuláciu.

![]({{ '/assets/images/labs/spinning_labs/flow_forming_lab/image0033.jpg' | relative_url }})

Okno Spustiť simuláciu

Sledujte priebeh simulácie tak, že sa pozriete na kartu Simulation Message and Simulation Log a uistite sa, že je začiarknutá možnosť ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}). Používateľ môže zobraziť proces Flow Forming, keď simulácia postupuje k zadaným kritériám zastavenia zo simulačnej grafiky.

Postprocessing

Po dokončení simulácie skontrolujte výsledky prepnutím do režimu Post pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) nad panelom nástrojov simulácie.

Prehrajte si kroky simulácie a pozrite sa, ako sa časť obrobku tvorí v procese formovania prietoku.

![]({{ '/assets/images/labs/spinning_labs/flow_forming_lab/image0034.jpg' | relative_url }})

Operácia tvarovania prietoku posledný krok

Vykreslite premennú Efektívny stav napätia a sledujte rozdelenie napätia (pozri obr. 3DFFL1.35.).

![]({{ '/assets/images/labs/spinning_labs/flow_forming_lab/image0035.jpg' | relative_url }})

Efektívne rozloženie napätia v poslednom kroku

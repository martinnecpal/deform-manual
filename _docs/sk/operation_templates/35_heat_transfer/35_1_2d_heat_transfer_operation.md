---
lang: sk
title: "35.1. 2D výpočet prenosu tepla"
---

# 35.1. 2D prevádzka prenosu tepla

35.1.1. Ako pridať operáciu prenosu tepla

35.1.2. Typ geometrie

35.1.3. Typ prenosu tepla

35.1.4. Podmienky procesu

35.1.5. Ovládacie prvky simulácie

35.1.6. Zoznam materiálov

35.1.7. Pridávanie objektov

35.1.8. Obrobok

  * Geometria

  * Sieť objektu

  * Materiál predmetu

  * Okrajové podmienky

  * Ovládanie pohybu

  * Nehnuteľnosť

  * Inicializovať

35.1.9. Polohovanie

35.1.10. Plánované umiestnenie

35.1.11. Vzťahy medzi objektmi

35.1.12. Ovládacie prvky na zastavenie

35.1.13. Ovládacie prvky krokov

35.1.14. Vytvorenie databázy

## Ako pridať operáciu prenosu tepla

Operáciu prenosu tepla je možné otvoriť cez sprievodcu MO, ktorý je dostupný z hlavného grafického rozhrania. Operáciu prenosu tepla je možné pridať v sprievodcovi MO na karte „Explorer“ kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) vedľa položky „2D Heat Transfer“. Užívateľ ju môže pridať aj pomocou funkcie drag and drop do Editoru operácií, ako je znázornené na obr. 35.1.1. Kombináciu operácií prenosu tepla na základe procesu je možné nastaviť v dávkovom alebo plánovanom režime.

![]({{ '/assets/images/operation_templates/35_heat_transfer/35_1_2d_heat_transfer_operation/image001.jpg' | relative_url }})

Do editora operácií bola pridaná operácia „2D prenos tepla“

## Typ geometrie

V režime 2D prenosu tepla je v súčasnosti možné nastaviť štyri typy geometrických modelov ([GEOTYP](/docs/en/keyword_documentation/g/geotyp/)), ako je znázornené na obr. 35.1.2.

![]({{ '/assets/images/operation_templates/35_heat_transfer/35_1_2d_heat_transfer_operation/image002.jpg' | relative_url }})

Okno „Typ 2D geometrie“

  * Osovo symetrický

  * Rovinné deformácie

  * Krútiaci moment

  * Rovinné napätie

  
Ďalšie informácie o týchto typoch geometrie nájdete v [9.1.2. Geometry type (GEOTYP](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#9.1.2._Geometry_type_\(GEOTYP\)_\[2D\])).

## Typ prenosu tepla

![]({{ '/assets/images/operation_templates/35_heat_transfer/35_1_2d_heat_transfer_operation/image003.jpg' | relative_url }})

Okno na výber typu prenosu tepla

K dispozícii sú štyri typy procesov prenosu tepla (pozri obr. 35.1.3.),

  1. **Ohrev v peci** – Ohrev obrobku v peci

  2. **Preprava vzduchom** – Preprava obrobku z pece do lisu

  3. **Odpočinok na matrici** – Tepelné straty počas odpočinku na matrici pred začatím deformácie

  4. **Doba zotrvania na matrici** – Tepelné straty počas zotrvania na matrici po dokončení deformácie

  
Ďalšie podrobnosti o týchto typoch vykurovania sú uvedené v [35\. Introduction to Heat Transfer operation](/docs/en/operation_templates/35_heat_transfer/35_introduction_to_heat_transfer_operations/), pozri časť „Typy vykurovania“.

## Prevádzkové podmienky

V tomto okne je možné definovať procesné podmienky, ako sú doba prenosu (trvanie procesu), teplota okolia a koeficient konvekcie, ako je znázornené na obr. 35.1.4. V závislosti od výberu operácie prenosu tepla je možné načítať predvolené nastavenia procesu pre príslušnú operáciu, ktoré je možné zmeniť podľa požiadaviek používateľa.

![]({{ '/assets/images/operation_templates/35_heat_transfer/35_1_2d_heat_transfer_operation/image004.jpg' | relative_url }})

Okno nastavení podmienok procesu

## Ovládacie prvky simulácie

Systém DEFORM rieši časovo závislé nelineárne úlohy generovaním série riešení metódou konečných prvkov (FEM) v diskrétnych časových krokoch. V každom časovom kroku sa rýchlosti, teploty a ďalšie kľúčové premenné každého uzla v sieti konečných prvkov určujú na základe okrajových podmienok, termomechanických vlastností materiálov obrobku a prípadne riešení z predchádzajúcich krokov. Ostatné stavové premenné sa odvodzujú z týchto kľúčových hodnôt a aktualizujú sa pri každom časovom kroku. Dĺžka tohto časového kroku a počet simulovaných krokov sa určujú na základe informácií zadaných v ponuke nastavení krokov.

V ovládacích prvkoch simulácie v režime s návodom môže používateľ vybrať typ režimu simulácie a typ výstupu. Obr. 35.1.6 znázorňuje ovládacie prvky simulácie v režime s návodom. Obr. 35.1.5. znázorňuje ovládacie prvky simulácie v expertnom režime, kde môže používateľ definovať ovládacie prvky krokov operácie a definíciu krokov. Tu sú k dispozícii základné možnosti potrebné na nastavenie operácie prenosu tepla, pričom expertný režim ponúka podrobnejšie možnosti. 

![]({{ '/assets/images/operation_templates/35_heat_transfer/35_1_2d_heat_transfer_operation/image006.jpg' | relative_url }})

Ovládacie prvky simulácie v režime pre pokročilých

![]({{ '/assets/images/operation_templates/35_heat_transfer/35_1_2d_heat_transfer_operation/image005.jpg' | relative_url }})

Ovládacie prvky simulácie v režime s návodom

## Zoznam materiálov

Materiály potrebné pre tento proces je možné načítať buď z knižnice pomocou ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}), alebo z databázy či kľúčového súboru pomocou ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}), ako je znázornené na obr. 35.1.7. Používateľ môže tiež pridať nový materiál a definovať požadované údaje na príslušnej karte kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). Ďalšie informácie o definovaní údajov o materiáloch nájdete v [10\. Material Data.](/docs/en/pre_processor/10_material_data/10_material_data/).

![]({{ '/assets/images/operation_templates/35_heat_transfer/35_1_2d_heat_transfer_operation/image007.jpg' | relative_url }})

Importovať materiál z knižnice

## Pridať objekty

Používateľ môže pridať požadovaný počet objektov pre simuláciu kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}). Obr. 35.1.8. znázorňuje tri objekty pridané pre jednoduchú operáciu prenosu tepla. 

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image007.jpg' | relative_url }})

Okno „Objekty“

## Obrobok

Na tejto stránke môže používateľ nastaviť požadovanú teplotu pre objekt a vybrať typ objektu, ako je znázornené na obr. 35.1.9. Pre obrobok je štandardne vybraný typ objektu „Plast“ a používateľ môže tiež importovať objekt z iných databáz alebo súborov kľúčov pomocou možnosti ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) a vyhľadaním príslušného súboru. 

![]({{ '/assets/images/operation_templates/35_heat_transfer/35_1_2d_heat_transfer_operation/image008.jpg' | relative_url }})

Okno obrobku

### Geometria

Používateľ môže definovať novú geometriu pomocou primitív a tiež môže importovať geometriu z iného súboru pomocou ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) alebo z knižnice pomocou ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}); používateľ môže tiež importovať geometrie v iných formátoch, ako sú .DXF a .IGES. Primitívy slúžia na jednoduchú definíciu základných geometrických tvarov. (Pozri obr. 35.1.10.) 

Ďalšie informácie o vytváraní a úpravách 2D geometrií nájdete v [12.1. 2D Geometry Data Defining.](/docs/en/pre_processor/12_geometry_modelling/12_1_2d_geometry_data_defining/)

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image009.jpg' | relative_url }})

Okno s definíciou geometrie

### Sieť objektu

Stránka „Mesh“ ponúka možnosti vytvorenia siete pre objekt. Režim „Guided ![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }})“ umožňuje nastaviť počet prvkov výlučne pomocou posuvníka na vytvorenie siete. Ak je geometria objektu zložitá alebo ak chce používateľ ovládať hustotu siete na celom objekte, musí prejsť do expertného režimu kliknutím na ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}). Odborný režim ponúka rôzne možnosti, ako sú váhové faktory, okná siete a režim definovaný používateľom, ktoré slúžia na riadenie hustoty siete. Možnosti vytvárania siete dostupné v odbornom režime a v režime „Guided“ sú znázornené na obr. 35.1.12 a obr. 35.1.11.

Podrobnejší popis týchto možností nájdete v [131\. 2D Mesh Generation.](/docs/en/pre_processor/13_mesh_generation/13_1_2d_mesh_generation/)

  
![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image019.jpg' | relative_url }})

Režim s navádzaním – možnosť „Mesh“

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image020.jpg' | relative_url }})

Možnosť vytvorenia siete v expertnom režime

### Materiál objektu

Na stránke materiálov sa zobrazujú všetky materiály pridané do zoznamu materiálov (ako je znázornené na obr. 35.1.13.) a používateľ si môže zo zoznamu materiálov vybrať požadovaný materiál, ktorý chce priradiť k príslušnému objektu. Užívateľ môže materiál na stránke Materiál objektu načítať aj pomocou možnosti Importovať údaje o materiáli zo súboru ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) alebo pomocou možnosti Načítať z knižnice ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}). 

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image029.jpg' | relative_url }})

Okno výberu materiálu

### Okrajové podmienky

Na stránke „Okrajové podmienky“ môže používateľ objektu priradiť rôzne okrajové obmedzenia. Okrajové podmienky určujú, ako okraj objektu interaguje s ostatnými objektmi a s okolím. Najčastejšie sa pri simuláciách zahŕňajúcich prenos tepla používajú okrajové podmienky týkajúce sa výmeny tepla s okolím. Obr. 35.1.14. znázorňuje rôzne okrajové podmienky, ktoré je možné priradiť k objektu v operácii „Prenos tepla“.

![]({{ '/assets/images/operation_templates/35_heat_transfer/35_1_2d_heat_transfer_operation/image009.jpg' | relative_url }})

Okno s okrajovými podmienkami

  
Ďalšie informácie o týchto BCC nájdete v dokumente [14\. Boundary Conditions](/docs/en/pre_processor/14_boundary_conditions/14_boundary_conditions/).

### Ovládanie pohybu

Ovládanie pohybu sa uplatňuje na tuhé objekty, ak je v nastaveniach simulácie zapnutá deformácia a ak sa ovládanie pohybu nepoužíva pri operácii „Prenos tepla“.  
Ďalšie informácie o týchto ovládacích prvkoch nájdete v [15\. Movement Controls Settings.](/docs/en/pre_processor/15_movement_controls_definition/15_movement_controls_settings/)

### Nehnuteľnosť

V okne „Vlastnosti objektu“ sa zadávajú rôzne parametre objektu, ktoré ovplyvňujú buď termomechanické správanie objektu, alebo správanie numerického riešenia. (Pozri [Fig. 35.1.15.](35_introduction_to_heat_transfer_operations.htm#Fig_35_1_14_Boundary_conditions_window)) Ďalšie informácie nájdete v [16\. Object properties](/docs/en/pre_processor/16_object_properties/16_object_properties/).

![]({{ '/assets/images/operation_templates/35_heat_transfer/35_1_2d_heat_transfer_operation/image010.jpg' | relative_url }})

Okno vlastností

### Inicializácia

V okne „Initialize“ sú na inicializáciu k dispozícii niektoré bežne používané stavové premenné, ako napríklad teplota, deformácia, napätie, poškodenie, rýchlosť, posunutie atď.  
Používateľ môže inicializovať hodnoty týchto stavových premenných kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}). Obr. 35.1.16. znázorňuje rôzne stavové premenné, ktoré sú k dispozícii v okne Initialize. V závislosti od typu stavovej premennej ich môže používateľ inicializovať aj z dátových okien Node a Element (pozri obr. 35.1.17. a obr. 35.1.18. ). Ďalšie informácie o tom, ako inicializovať stavové premenné v oknách „Node“ a „Element“, nájdete v [17.1 Node data Window](/docs/en/pre_processor/17_object_data_initialization/17_1_node_data_window/) a [17.2. Element data Window](/docs/en/pre_processor/17_object_data_initialization/17_2_element_data_window/).

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image028.jpg' | relative_url }})

Inicializovať okno

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image026.jpg' | relative_url }})

Okno „Údaje uzla“

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image027.jpg' | relative_url }})

Okno „Údaje o prvku“

## Polohovanie

Na obr. 35.1.19. je zobrazené okno na nastavenie polohy.

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image030.jpg' | relative_url }})

Okno ovládacích prvkov

****

**Automatické polohovanie** ![]({{ '/assets/icons/pre_icons/mo_automatic_positioning_button.jpg' | relative_url }})

Kliknutím na toto tlačidlo systém automaticky umiestni objekty vzhľadom na smer pohybu hornej matrice; táto možnosť sa najlepšie hodí pre jednoduché nastavenie s tromi objektmi – obrobkom, hornou matricou a spodnou matricou.

**Umiestňovanie objektov**![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }})

Kliknutím na toto tlačidlo môže používateľ umiestniť objekty do požadovaných smerov. K dispozícii sú rôzne typy možností umiestnenia, ako napríklad [Drag](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_1_Drag_Positioning), [Offset](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_2_Offset_Positioning), [Interference](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_3_Interference_positioning), [Flip](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_6_Flip_positioning) a [Rotational](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_4_Rotational_positioning), ako je znázornené na obr. 35.1.20. Ďalšie informácie o týchto možnostiach nájdete v časti [19\. Object Positioning.](/docs/en/pre_processor/19_object_positioning/19_object_positioning/)

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image029.jpg' | relative_url }})

Okno na umiestňovanie objektov

## Plánované polohovanie

Ak si používateľ nie je istý polohou objektu, ako je to v prípade objektov typu „Read From DB“, naplánované umiestňovanie pomôže objekty presne umiestniť.  
Funkcia „Schedule positioning“ umožňuje používateľovi definovať umiestnenie objektov v nastavení MO pre nasledujúce operácie, pre ktoré sa nevytvára databáza (DB), tak, aby boli objekty umiestnené ešte pred vytvorením databázy počas spustenia simulácie v dávkovom režime. (Pozri obr. 35.1.21.)

![]({{ '/assets/images/operation_templates/35_heat_transfer/35_1_2d_heat_transfer_operation/image011.jpg' | relative_url }})

Plánované časové okno na určovanie polohy

## Vzťahy medzi objektmi

Účelom vzťahov medzi objektmi je definovať, ako rôzne objekty v simulácii vzájomne interagujú. Tabuľka vzťahov zobrazuje aktuálne vzťahy medzi objektmi, ktoré boli definované tak, ako je znázornené na obr. 35.1.22. Všetky objekty, ktoré môžu prísť do kontaktu v priebehu simulácie, musia mať definovaný kontaktný vzťah.

**Systém**: Po výbere tohto prepínača systém priradí predvolené vzťahy medzi objektmi. Používateľ môže hodnoty upraviť kliknutím na tlačidlo „Upraviť“.

**Používateľ**: Pri operácii „Prenos tepla“ je štandardne zaškrtnuté políčko „Používateľ“. Používateľ môže pridať vzťahy kliknutím na tlačidlo „Pridať“, ako je znázornené na obr. 35.1.22.

Ďalšie informácie nájdete v dokumente [20\. Inter-Object Relations.](/docs/en/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/)

![]({{ '/assets/images/operation_templates/35_heat_transfer/35_1_2d_heat_transfer_operation/image012.jpg' | relative_url }})

Okno definície medzi objektmi

## Ovládacie prvky na zastavenie

Parametre ukončenia určujú čas priebehu, po uplynutí ktorého sa simulácia ukončí. Simuláciu je možné ukončiť na základe maximálneho počtu simulovaných časových krokov alebo maximálneho času priebehu. Simulácia sa zastaví, keď bude splnená podmienka ktoréhokoľvek z parametrov ukončenia. Ďalšie informácie nájdete v [Stopping Controls](../33_forming/33_2_3d_forming_setup.htm#33_2_7_Stopping_Controls) v [3D Forming setup](/docs/en/operation_templates/33_forming/33_2_3d_forming_setup/).

## Ovládacie prvky krokov

**Počet simulačných krokov (NSTEP)**

Parameter „Počet simulačných krokov“ určuje počet krokov, ktoré sa majú spustiť od počiatočného čísla kroku. Simulácia sa zastaví po vykonaní tohto počtu simulačných krokov, pokiaľ sa nespustí riadiaci signál na zastavenie simulácie alebo ak simulácia nenarazí na problém. Napríklad, ak je počiatočné číslo kroku -35 (NSTART) a je špecifikovaných 30 krokov (NSTEP), simulácia sa zastaví po 65. kroku, pokiaľ sa skôr nespustí iný príkaz na zastavenie.

**Krok pri ukladaní (STPINC)**

Hodnota krokového prírastku (STPINC), ktorá sa ukladá do databázy, určuje počet krokov, ktoré systém uloží do databázy. Pri spustení simulácie sa musí vypočítať každý krok, ale nie je nutné ho vždy ukladať do databázy. Uložením väčšieho počtu krokov sa zachová viac informácií o procese, čo však bude vyžadovať väčší úložný priestor.

**Ovládanie krokového prírastku (DSMAX/DTMAX)**

Veľkosť kroku pri riešení úloh prenosu tepla je možné riadiť pomocou časového kroku. Systém DEFORM rieši časovo závislé nelineárne úlohy generovaním série riešení metódou konečných prvkov (FEM) v diskrétnych časových krokoch. V každom časovom kroku sa na základe okrajových podmienok, termomechanických vlastností materiálov obrobku a prípadne riešení z predchádzajúcich krokov určujú rýchlosti, teploty a ďalšie kľúčové premenné každého uzla v sieti konečných prvkov. Ostatné stavové premenné sa odvodzujú z týchto kľúčových hodnôt a aktualizujú sa pre každý časový krok. Dĺžka tohto časového kroku a počet simulovaných krokov sa určujú na základe informácií zadaných v ponuke nastavení krokov. Obr. 35.1.23. znázorňuje stránku Definícia kroku v režime s návodom.

![]({{ '/assets/images/operation_templates/35_heat_transfer/35_1_2d_heat_transfer_operation/image013.jpg' | relative_url }})

Okno „Definícia kroku v režime s návodom“

Možnosti definované na stránke „Definícia kroku“ ovplyvňujú numerické správanie riešenia. Ovládacie prvky simulácie v expertnom režime – hlavné ovládacie prvky umožňujú špecifikovať názov simulácie, systém jednotiek, typ geometrie atď.

  
[Step](/docs/en/pre_processor/9_simulation_controls/9_1_simulation_type_settings/) a [stopping controls](/docs/en/pre_processor/9_simulation_controls/9_3_stopping_controls/) slúžia na určenie časového kroku, celkového počtu krokov a kritérií na ukončenie simulácie. [Processing conditions](/docs/en/pre_processor/9_simulation_controls/9_6_process_conditions/) – tu je možné zadať napríklad teplotu okolia alebo konvekčný koeficient.

Ďalšie informácie a popis možností v ovládacích prvkoch simulácie nájdete v [9\. Simulation Controls.](/docs/en/pre_processor/9_simulation_controls/9_simulation_controls/)

## Vytvoriť databázu

****

**Overiť údaje**![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }})****

Systém skontroluje údaje. Ak sú údaje správne, môžeme vytvoriť databázu. Ak sa však pri kontrole údajov vyskytnú chyby alebo varovania, je potrebné ich opraviť pred vytvorením databázy. Chyby zabránia vytvoreniu databázy, zatiaľ čo varovania vytvorenie databázy neumožnia.

**Vytvoriť databázu ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }})**

Kliknutím na toto tlačidlo sa vygenerovala databáza pre nastavenie. (Pozri obr. 35.1.24.)

**Pridať súbor s kľúčmi**

Akékoľvek informácie, ktoré nie sú definované v sprievodcovi, ale napriek tomu sa vzťahujú na daný proces, je možné načítať ako súbor s príponou .key. Táto možnosť je užitočná aj v prípadoch, keď je potrebné zmeniť len niekoľko hodnôt – tieto hodnoty je možné definovať v súbore s príponou .key, následne stačí zmeniť len tento súbor a simuláciu je možné spustiť znova.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image048.jpg' | relative_url }})

Okno „Vytvoriť databázu“

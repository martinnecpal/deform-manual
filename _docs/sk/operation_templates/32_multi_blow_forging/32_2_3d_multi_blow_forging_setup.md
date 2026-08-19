---
lang: sk
title: "32.2. Nastavenie 3D viacnásobného výkovu"
---

# 32.2. Nastavenie 3D viacnásobného výkovu

32.2.1. Podrobnosti o procese

32.2.2. Tabuľka výdychov

32.2.3. Ovládacie prvky simulácie

32.2.4. Zoznam materiálov

32.2.5. Pridávanie objektov

32.2.6. Obrobok

  * Geometria

  * Sieť objektu

  * Materiál predmetu

  * Okrajové podmienky

32.2.7. Horná matrica

32.2.8. Spodná matrica

32.2.9. Polohovanie

32.2.10. Plánované umiestnenie

32.2.11. Kontakt

32.2.12. Ovládacie prvky na zastavenie

32.2.13. Ovládacie prvky krokov

32.2.14. Vytvorenie databázy

## Podrobnosti o procese

Na tejto stránke procesu môže používateľ definovať energiu kladiva a spôsob jej zadávania spolu s riadiacimi parametrami procesu, ako sú opätovné zahrievanie a doba zdržania. Používateľ môže definovať podmienky opätovného zahrievania a ich riadiace parametre spolu s podmienkami doby zdržania. Používateľ má tiež možnosť určiť, či sa objekt medzi údermi otáča, a môže tiež inicializovať deformáciu pri opätovnom zahrievaní. (Pozri obr. 32.2.1.)

![]({{ '/assets/images/operation_templates/32_multi_blow_forging/32_2_3d_multi_blow_forging_setup/image001.jpg' | relative_url }})

Okno procesu

**Tlač**: Používateľ môže zadať názov kladiva a údaje o energii. Pomocou funkcií „Načítať pohyb zo súboru“ (![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }})) a „Načítať pohyb z knižnice“ (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})) môže používateľ načítať údaje o kladive. 

**Poznámka**: V súčasnosti nie je možné načítať údaje o tlači z knižnice zariadení na karte „Explorer“.

**Spôsob stanovenia energetickej náročnosti:**

  * **Absolútna**: Spotreba energie sa bude riadiť definovanou hodnotou energie.

  * **Podiel na maximálnej energii (%)**: Spotreba energie sa bude uvádzať v percentách.

  
**Doba zdržania**: Pomocou tejto funkcie môže používateľ nastaviť čas, počas ktorého obrobok zostáva na matrici pred začatím ďalšieho úderu. Používateľ môže tiež určiť časový krok simulácie a koeficient prenosu tepla, ktoré sa majú použiť pri simulácii procesu zdržania.

**Otáčanie obrobku**: Zapnutím tejto možnosti môže používateľ nastaviť otáčanie obrobku medzi údermi v zadaných smeroch.

**Použiť opätovné zahriatie**: Počas procesu kovania kladivom, ktorý zahŕňa viacero úderov, teplota obrobku klesá a môže byť potrebné ho opätovne zahriať. Zapnutím tejto možnosti môže používateľ naplánovať proces opätovného zahriatia medzi jednotlivými údermi. 

**Teplota opätovného ohrevu**: Teplota opätovného ohrevu je teplota, na ktorú sa zvýši teplota obrobku. Ak je zapnutá len teplota opätovného ohrevu bez simulácií ohrevu, teplota vo všetkých uzloch obrobku sa jednoducho nastaví na hodnotu teploty opätovného ohrevu.

**Simulácie ohrevu**: Ak je funkcia „Simulácie ohrevu“ zapnutá, v zadanom čase medzi údermi prebieha simulácia ohrevu obrobku. Zahŕňa čas ohrevu, čas prenosu dovnútra, čas prenosu von, ako aj konkrétny časový krok simulácie pre čas ohrevu a čas prenosu.

**Adaptívne opätovné zahrievanie:** Po zapnutí funkcie „Adaptívne opätovné zahrievanie“ systém sám rozhodne o opätovnom zahrievaní obrobku a naplánuje ho na základe uzlových teplôt obrobku a nastavení adaptívneho opätovného zahrievania. Ak je táto funkcia vypnutá, používateľ musí opätovné zahrievanie naplánovať ručne. Ak teplota uzlov obrobku klesne pod dolnú hranicu, proces opätovného ohrevu sa naplánuje automaticky. Počas simulácie bez deformácie sa simulácia zastaví, ak teplota uzlov obrobku prekročí rozsah špecifikovaný hornou a dolnou hranicou. Simulácia sa zastaví počas opätovného ohrevu, ak všetky uzly dosiahnu teplotu špecifikovanú v parametri „Teplota na zastavenie opätovného ohrevu“.

**Inicializácia deformácie po opätovnom zahriatí:** Zapnutím tejto funkcie môže používateľ po opätovnom zahriatí inicializovať deformáciu v obrobku.

**Simulácie ohrevu**: Zahŕňajú dobu ohrevu, dobu ohrevu na jeden krok, čas začiatku prenosu, čas ukončenia prenosu a časový krok prenosu.

## Tabuľka výdychov

Pri kovaní kladivom sa používa viacero úderov a tabuľka úderov pomáha používateľovi určiť počet úderov a naplánovať otáčanie obrobku, dobu zdržania a opätovné zahrievanie.

**Energia**: Energia zotrvačníka je veličina vyjadrujúca celkovú energiu, ktorú bude zotrvačník obsahovať po dosiahnutí požadovanej rýchlosti a pred zapojením spojky. Jednotky pre energiu zotrvačníka sú v anglickom systéme klb-in a v systéme SI N-mm. (Pozri obr. 32.2.2.)

**Počet úderov**: Používateľ môže určiť počet úderov potrebných na vykonanie procesu. Po zadaní počtu úderov sa do tabuľky pridá rovnaký počet riadkov s predvolenými hodnotami. Používateľ môže ovládať účinnosť každého úderu a množstvo energie, ktorá sa má využiť. Používateľ môže tiež naplánovať opätovné zahriatie a otočenie obrobku po každom úderu zaškrtnutím príslušných políčok. V prípade potreby môže používateľ tiež definovať rôzne doby zdržania pre jednotlivé údery. Príklad tabuľky úderov je zobrazený na nižšie uvedenom obr. 32.2.2.

![]({{ '/assets/images/operation_templates/32_multi_blow_forging/32_2_3d_multi_blow_forging_setup/image002.jpg' | relative_url }})

Okno „Blow Table“

## Ovládacie prvky simulácie

V ovládacích prvkoch simulácie v režime s návodom môže používateľ vybrať typ simulačného režimu a typ výstupu (pozri obr. 32.2.3.). Tu sú k dispozícii základné možnosti potrebné na operáciu tvárnenia, zatiaľ čo režim Expert ponúka podrobnejšie možnosti. Ďalšie informácie o možnostiach simulácie v režime Export nájdete v [9\. Simulation Controls](/docs/en/pre_processor/9_simulation_controls/9_simulation_controls/)

![]({{ '/assets/images/operation_templates/32_multi_blow_forging/32_1_2d_multi_blow_forging_setup/image004.jpg' | relative_url }})

Ovládacie prvky simulácie v režime s návodom

## Zoznam materiálov

Materiály potrebné pre tento proces je možné načítať buď z knižnice pomocou ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}), alebo z databázy či kľúčového súboru pomocou ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}), ako je znázornené na obr. 32.2.4. Používateľ môže tiež pridať nový materiál a definovať požadované údaje na príslušnej karte kliknutím na ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). Ďalšie informácie o definícii údajov o materiáloch nájdete v zozname materiálov.

![]({{ '/assets/images/operation_templates/32_multi_blow_forging/32_1_2d_multi_blow_forging_setup/image005.jpg' | relative_url }})

Importovať materiál z knižnice

## Pridať objekty

Používateľ môže pridať požadovaný počet objektov pre simuláciu kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}). Na obr. 32.2.5 sú zobrazené tri objekty pridané pre jednoduchú operáciu zúženia. 

![]({{ '/assets/images/operation_templates/32_multi_blow_forging/32_1_2d_multi_blow_forging_setup/image006.jpg' | relative_url }})

Okno „Objekty“

## Obrobok

Na tejto stránke môže používateľ nastaviť požadovanú teplotu pre objekt a vybrať typ objektu, ako je znázornené na obr. 32.2.6. Pre obrobok je štandardne vybraný typ objektu „Plast“ a používateľ môže tiež importovať objekt z iných databáz alebo súborov kľúčov pomocou tlačidla ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) a vyhľadaním príslušného súboru. 

![]({{ '/assets/images/operation_templates/32_multi_blow_forging/32_2_3d_multi_blow_forging_setup/image003.jpg' | relative_url }})

Okno obrobku

**Geometria**

Okno „Geometria“ slúži na definovanie geometrie objektu, ako je znázornené na obr. 32.2.7. Ak nie je definovaná žiadna geometria, aktívne bude iba pole „Definovať primitívy“, ostatné možnosti budú sivé. Po vytvorení geometrie sa aktivujú všetky možnosti.

  
Používateľ môže definovať novú geometriu pomocou primitív a tiež môže importovať geometriu z iného súboru alebo z knižnice; môže tiež importovať geometrie v iných formátoch, ako sú .STL, .UNV, .PDA, .GEO a ... Primitívy slúžia na jednoduché definovanie základných geometrických tvarov. Ďalšie informácie o vytváraní a úpravách 2D geometrií nájdete v [12.1. 2D Geometry Data Defining.](/docs/en/pre_processor/12_geometry_modelling/12_1_2d_geometry_data_defining/)

![]({{ '/assets/images/operation_templates/32_multi_blow_forging/32_2_3d_multi_blow_forging_setup/image004.jpg' | relative_url }})

Okno Geometria

  
**Sieť objektu**

Stránka „Mesh“ ponúka možnosti vytvorenia siete pre objekt. Režim „Guided ![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }})“ umožňuje nastaviť počet prvkov výlučne pomocou posuvníka na vytvorenie siete. Ak je geometria objektu zložitá alebo ak chce používateľ ovládať hustotu siete na celom objekte, musí prejsť do expertného režimu kliknutím na ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}). Odborný režim ponúka rôzne možnosti, ako sú váhové faktory, okná siete a užívateľsky definovaný režim na riadenie hustoty siete. Možnosti vytvárania siete dostupné v odbornom režime a v režime „Guided“ sú znázornené na obr. 32.2.8 a obr. 32.2.9. Podrobnejší popis týchto možností nájdete v [13\. Mesh Generation.](/docs/en/pre_processor/13_mesh_generation/13_mesh_generation/).

![]({{ '/assets/images/operation_templates/32_multi_blow_forging/32_2_3d_multi_blow_forging_setup/image005.jpg' | relative_url }})

Režim s navádzaním – možnosť „Mesh“

![]({{ '/assets/images/operation_templates/32_multi_blow_forging/32_2_3d_multi_blow_forging_setup/image006.jpg' | relative_url }})

Možnosť vytvorenia siete v expertnom režime

**Materiál objektu**

Na stránke materiálov sa zobrazujú všetky materiály pridané do zoznamu materiálov (ako je znázornené na obr. 32.2.10.) a používateľ si môže zo zoznamu materiálov vybrať požadovaný materiál, ktorý chce priradiť k príslušnému objektu. Užívateľ môže materiál na stránke Materiál objektu načítať aj pomocou možnosti Importovať údaje o materiáli zo súboru ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) alebo pomocou možnosti Načítať z knižnice ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}).

![]({{ '/assets/images/operation_templates/30_die_stress/30_1_2d_die_stress_setup/image011.jpg' | relative_url }})

Okno výberu materiálu

  
**Okrajové podmienky**

Na stránke „Okrajové podmienky“ môže používateľ priradiť objektu rôzne okrajové obmedzenia. Okrajové podmienky určujú, ako okraj objektu interaguje s ostatnými objektmi a s prostredím. Najčastejšie používané okrajové podmienky sú výmena tepla s prostredím pri simuláciách zahŕňajúcich prenos tepla, predpísaná rýchlosť na vynútenie symetrie alebo predpísanie pohybu v úlohách, ako je ťahanie dielu cez lisovaciu formu, zúženie pri modelovaní zúžených krúžkov na nástrojoch, predpísaná sila pre analýzu napätia v lisovacej forme a kontakt medzi objektmi v modeli. Obr. 32.2.11. znázorňuje rôzne okrajové podmienky, ktoré je možné priradiť k objektu.

![]({{ '/assets/images/operation_templates/32_multi_blow_forging/32_2_3d_multi_blow_forging_setup/image007.jpg' | relative_url }})

Okno s okrajovými podmienkami

BCC sú rozdelené do kategórií [Deformation](/docs/en/pre_processor/14_boundary_conditions/14_2_deformation_boundary_conditions/), [Thermal](/docs/en/pre_processor/14_boundary_conditions/14_3_thermal_boundary_conditions/), [Diffusion](/docs/en/pre_processor/14_boundary_conditions/14_4_diffusion_boundary_conditions/) a [Heating](/docs/en/pre_processor/14_boundary_conditions/14_5_heating_boundary_conditions/). Ďalšie informácie o týchto BCC nájdete v [14\. Boundary Conditions](/docs/en/pre_processor/14_boundary_conditions/14_boundary_conditions/).

## Horná matrica

V prípade hornej formy môže používateľ definovať všetky potrebné údaje, ako sú geometria, sieť, materiál a BCC, tak ako bolo vysvetlené v prípade objektu obrobku.   
Pohyb hornej matrice však musíme definovať osobitne pre hornú matricu.

**Pohyb hornej matrice**

**Kladivový lis**

Proces kovania kladivom je riadený energiou. Počas pracovného zdvihu prebieha deformácia dovtedy, kým sa celková kinetická energia nevyčerpá prostredníctvom plastickej deformácie materiálu a pružnej deformácie piestu a kovadliny v okamihu, keď sa povrchy matrice a piestu dotknú.(Pozri obr. 32.2.12.)

![]({{ '/assets/images/operation_templates/32_multi_blow_forging/32_2_3d_multi_blow_forging_setup/image008.jpg' | relative_url }})

Nastavenia riadenia pohybu kladiva

  
Pri kovaní kladivom sa na plastickú deformáciu obrobku využíva len časť kinetickej energie piestu. Zvyšná energia sa stráca cez kovadlinu a rám stroja. Tieto hodnoty je možné nastaviť v okne ovládania pohybu.

V zásade existujú dva typy kladív. Prvým je [anvil type hammer](../../pre_processor/15_movement_controls_definition/15_3_hammer.htm#15_3_1_Anvil_Type_Hammer) a druhým c[ounter blow hammer](../../pre_processor/15_movement_controls_definition/15_3_hammer.htm#15_3_2_Counterblow_Hammer). Pokiaľ ide o vzorce a predpoklady použité pre oba typy operácií kovania kladivom, pozrite si [15.3. Hammer](/docs/en/pre_processor/15_movement_controls_definition/15_3_hammer/).

Pri **kladive typu kovadlina** sa obrobok spolu so spodnou sadou foriem umiestňuje na kovadlinu, ktorá je nehybná. V prípade jednoduchého gravitačného kladiva sa piest zrýchľuje pôsobením gravitácie a akumuluje energiu.

**Kladivo s protirazom** je možné nastaviť tak, že zaškrtnete políčko „Kladivo s protirazom“, ako je znázornené na obr. 6.7.5.3.12. Následne je možné špecifikovať aj druhý pohybujúci sa objekt kladiva, ako aj hmotnosť tohto druhého pohybujúceho sa kladiva. Hmotnosti objektov nemusia byť rovnaké, celková energia sa však rozdelí medzi obe matrice kladiva.

**Šnekový lis**

Jedinečnou vlastnosťou šnekového lisu (pozri obr. 32.2.13.) je spôsob jeho pohonu. Motor poháňa zotrvačník, ktorý je buď priamo spojený so šnekovým vretenom, alebo sa k nemu môže pripojiť.

![]({{ '/assets/images/operation_templates/32_multi_blow_forging/32_2_3d_multi_blow_forging_setup/image009.jpg' | relative_url }})

Nastavenia riadenia pohybu šnekového lisu

  
**Údaje potrebné na prevádzku nástroja poháňaného šnekovým lisom sú:**

  * **Energia**: Energia rozbehu je veličina vyjadrujúca celkovú energiu, ktorú bude zotrvačník obsahovať po dosiahnutí požadovanej rýchlosti a pred zapojením spojky. Jednotky pre energiu rozbehu sú v anglickom systéme klb-in a v systéme SI N-mm.

  * **Účinnosť vyfukovania**: Účinnosť vyfukovania predstavuje podiel celkovej energie, ktorý sa premení na energiu deformácie. Zvyšná energia sa absorbuje prostredníctvom spojkového mechanizmu, trenia a rámu stroja. Táto veličina nemá žiadne jednotky. V programe Forming Express môžeme použiť iba konštantnú hodnotu, avšak pri formovacích operáciách môže používateľ definovať aj funkciu sily. Ďalšie informácie nájdete v [15.4. Screw Press.](/docs/en/pre_processor/15_movement_controls_definition/15_4_screw_press/).

  * **Moment****zotrvačnosti**: Moment zotrvačnosti je moment zotrvačnosti zotrvačníka. Jednotky zotrvačnosti v anglickom systéme sú klb*in*s², v systéme SI sú to N-mm*s². Moment zotrvačnosti pre kruhový disk s osou Z kolmou na stred je I = 2 ET /ω², kde ET je celková energia zotrvačníka a ω je uhlová rýchlosť v radiánoch za sekundu.

  * **Posun zdvihového piestu****alebo stúpanie vodiacich skrutiek**: Posun zdvihového piestu udáva vzdialenosť, o ktorú sa skrutka posunie pri jednej otáčke zotrvačníka. To pomáha pri určovaní lineárnej rýchlosti zdvihového piestu. Anglické jednotky pre posuv ramena sú palce/otáčka, zatiaľ čo jednotky SI sú mm/otáčka. Ak sú známe len uhol stúpania a priemer vretena, posuv ramena je možné vypočítať pomocou vzorca πdsin(θt), kde d je priemer vretena a θt je uhol stúpania vretena.

  
Ďalšie informácie o šnekovom lise nájdete v katalógu [15.4. Screw Press.](/docs/en/pre_processor/15_movement_controls_definition/15_4_screw_press/)

## Spodná forma

V prípade spodnej formy môže používateľ definovať všetky potrebné údaje, ako sú geometria, sieť, materiál a BCC, tak ako bolo vysvetlené v prípade objektu obrobku.

## Polohovanie

Na obr. 32.2.14 je zobrazené okno na nastavenie polohy.

![]({{ '/assets/images/operation_templates/32_multi_blow_forging/32_2_3d_multi_blow_forging_setup/image010.jpg' | relative_url }})

Okno na nastavenie polohy

**Automatické polohovanie ![]({{ '/assets/icons/pre_icons/mo_automatic_positioning_button.jpg' | relative_url }})**

Kliknutím na toto tlačidlo systém automaticky umiestni objekty vzhľadom na smer pohybu hornej matrice; táto možnosť sa najlepšie hodí pre jednoduché nastavenie s tromi objektmi – obrobkom, hornou matricou a spodnou matricou.

**Umiestňovanie objektov ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) **

Kliknutím na toto tlačidlo môže používateľ umiestniť objekty do požadovaných smerov.K dispozícii sú rôzne typy možností umiestnenia, ako napríklad [Drag](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_1_Drag_Positioning), [Offset](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_2_Offset_Positioning), [Interference](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_3_Interference_positioning), [Flip](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_6_Flip_positioning) a [Rotational](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_4_Rotational_positioning), ako je znázornené na obr. 32.2.15. Ďalšie informácie o týchto možnostiach nájdete v časti [19\. Object Positioning](/docs/en/pre_processor/19_object_positioning/19_object_positioning/)

![]({{ '/assets/images/operation_templates/32_multi_blow_forging/32_2_3d_multi_blow_forging_setup/image011.jpg' | relative_url }})

Okno na umiestňovanie objektov

## Plánované polohovanie

Ak si používateľ nie je istý umiestnením objektu, naplánované umiestňovanie mu pomôže objekty presne umiestniť.

  
Funkcia plánovania umiestnenia umožňuje používateľovi definovať umiestnenie objektov v nastaveniach MO pre nasledujúce operácie, pre ktoré sa nevytvára databáza (DB), tak, aby boli objekty umiestnené ešte pred vytvorením databázy počas spustenia simulácie v dávkovom režime.

## Kontakt

Účelom vzťahov medzi objektmi je definovať, ako rôzne objekty v simulácii vzájomne interagujú. Všetky objekty, ktoré sa v priebehu simulácie môžu navzájom dotýkať, musia mať definovaný kontaktný vzťah. 

  
Vzťahy medzi objektmi určujú, ktoré objekty sa môžu navzájom dotýkať a ako sa dotýkajúce sa objekty budú správať počas kontaktu. Pre každú dvojicu objektov sa tu nastavujú vzťahy dotyku, okrajové podmienky medzi objektmi, trenie a prenos tepla. (Pozri obr. 32.2.16.) Vygenerované správy o kontaktoch sa zobrazia na karte Správy pod grafickým oknom.

![]({{ '/assets/images/operation_templates/32_multi_blow_forging/32_1_2d_multi_blow_forging_setup/image015.jpg' | relative_url }})

Okno na generovanie kontaktov

  
Používateľ si môže vybrať typ trenia – šmykové alebo Coulombovo – a nastaviť koeficient trenia. Mazivo použité na nástroji má veľký vplyv na veľkosť trenia medzi nástrojom a obrobkom. Trenie zase ovplyvňuje tok kovu na kontaktných plochách.

  
Pre šmykové trenie sú uvedené typické hodnoty, ako je znázornené nižšie,  
(0,08) pre procesy tvárnenia za studena (karbidové matrice)

(0,12) pre procesy tvárnenia za studena (oceľové formy)

(0,25) pre procesy tepelného tvárnenia

(0,3) pre procesy mazaného kovania za tepla

(0,7) pre procesy horúceho kovania bez mazania (nasucho)

(0,4) pre procesy tvárnenia hliníka

Hodnotu koeficientu prenosu tepla vedením si môže užívateľ nastaviť sám; systém zároveň ponúka aj typické hodnoty, a to:

(1 N/s/mm/°C alebo 0,0003 Btu/s/in²/°F) pre stav voľného pokoja

(1 N/s/mm/°C alebo 0,0003 Btu/s/in²/°F) pre obytné priestory

(11 N/s/mm/°C alebo 0,004 Btu/s/in²/°F) pri tvárnení

## Ovládacie prvky na zastavenie

Parametre ukončenia určujú čas procesu, v ktorom sa simulácia ukončí. Simuláciu je možné ukončiť na základe maximálneho počtu simulovaných časových krokov, maximálnej kumulovanej elementárnej deformácie, maximálnej doby trvania procesu, maximálneho zdvihu, minimálnej rýchlosti alebo maximálneho zaťaženia primárneho objektu. Simulácia sa zastaví, keď je splnená podmienka ktoréhokoľvek z parametrov ukončenia. (Pozri obr. 32.2.17.)

![]({{ '/assets/images/operation_templates/32_multi_blow_forging/32_2_3d_multi_blow_forging_setup/image012.jpg' | relative_url }})

Okno ovládacích prvkov zastavenia

Ďalšie informácie nájdete v dokumente [Stopping Controls in Forming 3D setup](../33_forming/33_2_3d_forming_setup.htm#33_2_7_Stopping_Controls).

## Ovládacie prvky krokov

Systém DEFORM rieši časovo závislé nelineárne úlohy generovaním série riešení metódou konečných prvkov (FEM) v diskrétnych časových krokoch. V každom časovom kroku sa rýchlosti, teploty a ďalšie kľúčové premenné každého uzla v sieti konečných prvkov určujú na základe okrajových podmienok, termomechanických vlastností materiálov obrobku a prípadne riešení z predchádzajúcich krokov. Ostatné stavové premenné sa odvodzujú z týchto kľúčových hodnôt a aktualizujú sa pri každom časovom kroku. Dĺžka tohto časového kroku a počet simulovaných krokov sa určujú na základe informácií zadaných v ponuke nastavení krokov. Obr. 32.2.18. Zobrazuje možnosti riadenia simulácie v režime „Guided“ (Vedený); tu sú k dispozícii základné možnosti potrebné pre operáciu tvárnenia, zatiaľ čo režim „Expert“ (Odborný) ponúka podrobnejšie možnosti.

![]({{ '/assets/images/operation_templates/32_multi_blow_forging/32_1_2d_multi_blow_forging_setup/image017.jpg' | relative_url }})

Okno ovládacích prvkov krokov v režime s navádzaním

**Počet simulačných krokov (NSTEP)**

Parameter „Počet simulačných krokov“ určuje počet krokov, ktoré sa majú spustiť od počiatočného čísla kroku. Simulácia sa zastaví po vykonaní tohto počtu simulačných krokov, pokiaľ sa nespustí príkaz na zastavenie simulácie alebo ak simulácia nenarazí na problém. Napríklad, ak je počiatočné číslo kroku -35 ([NSTART](/docs/en/keyword_documentation/n/nstart/)) a je špecifikovaných 30 krokov ([NSTEP](/docs/en/keyword_documentation/n/nstep/)), simulácia sa zastaví po 65. kroku, pokiaľ sa skôr nespustí iný príkaz na zastavenie. V prípade procesu opätovného ohrevu to môže byť teplota, pri ktorej sa má opätovný ohrievanie zastaviť.

Ďalšie informácie nájdete v dokumente [Stopping Controls.](/docs/en/pre_processor/9_simulation_controls/9_3_stopping_controls/)

  
**Krok pri ukladaní (STPINC)**

Krok prírastku ([STPINC](/docs/en/keyword_documentation/s/stpinc/)), ktorý sa má uložiť do databázy, určuje počet krokov, ktoré systém uloží do databázy. Pri spustení simulácie sa musí vypočítať každý krok, ale nemusí sa nutne uložiť do databázy. Uložením väčšieho počtu krokov sa zachová viac informácií o procese, čo však bude vyžadovať väčší úložný priestor.

  
**Primárny čip (PDIE)**

Primárna matrica ([PDIE](/docs/en/keyword_documentation/p/pdie/)) je objekt, pre ktorý je definovaných mnoho kritérií zastavenia a krokovania. Napríklad brzdná vzdialenosť založená na zdvihu primárnej matrice. Keď zdvih objektu definovaného ako primárna matrica dosiahne hodnotu posunu primárnej matrice, simulácia sa zastaví bez ohľadu na to, či boli špecifikované ďalšie kroky. Funkcia „Krok podľa zdvihu“ určuje veľkosť kroku na základe pohybu primárnej matrice. Primárna matrica je zvyčajne priradená k objektu, ktorý je najviac riadený kováčskym strojom. Napríklad matrica pripevnená k piestu mechanického lisu by bola označená ako primárny objekt. V prípade kladivového alebo skrutkového lisu je primárna matrica zvyčajne priradená k hornej matrici.

**Ovládanie krokového posunu ([DSMAX](/docs/en/keyword_documentation/d/dsmax/)/[DTMAX](/docs/en/keyword_documentation/d/dtmax/))**

Veľkosť kroku riešenia je možné riadiť časovým krokom alebo posunom primárnej matrice. Ak je špecifikovaný zdvih na krok, primárna matrica sa v každom časovom kroku posunie o zadanú hodnotu. Celkový posun primárnej matrice bude rovný posunu na krok vynásobenému celkovým počtom krokov. Ak je špecifikovaný čas na krok, použije sa časový interval na krok. Posun matrice na krok bude rovný časovému kroku vynásobenému rýchlosťou matrice.

Definícia riadenia krokového prírastku bola rozšírená tak, aby zahŕňala krokové funkcie závislé od času aj od zdvihu; tieto možnosti sú k dispozícii v režime Expert. To znamená, že veľkosť kroku (či už čas na krok, alebo zdvih na krok) je teraz možné definovať ako funkciu času alebo zdvihu. Táto funkcia umožňuje jemnejšie rozlíšenie uložených informácií o modeli tam, kde je to žiaduce. (typicky na konci zdvihu, kde môže dochádzať k prudkým zmenám zaťaženia formy, plnenia dutiny alebo tvorby prebytku materiálu)

  
Počet zdvihov na krok je často intuitívnejší. Čas na krok je však potrebné určiť pri každej úlohe, v ktorej nedochádza k pohybu matice (napríklad pri prenose tepla), alebo pri každej úlohe, kde sa používa regulácia sily.

Obr. 32.2.19.. znázorňuje ovládacie prvky simulácie v režime Expert.

![]({{ '/assets/images/operation_templates/32_multi_blow_forging/32_2_3d_multi_blow_forging_setup/image013.jpg' | relative_url }})

Okno ovládacích prvkov simulácie v režime pre pokročilých

  
Možnosti definované v časti „Ovládacie prvky simulácie“ (pozri obr. 32.2.19.) riadia numerické správanie riešenia. Hlavné ovládacie prvky obsahujú podrobnosti týkajúce sa zadania názvu simulácie, sústavy jednotiek, typu geometrie atď.

  
Ovládacie prvky pre kroky a ukončenie slúžia na určenie časového kroku, celkového počtu krokov a kritérií na ukončenie simulácie.

  
Tu je možné zadať podmienky spracovania, ako napríklad teplotu okolia a konvekčný koeficient.

Ďalšie informácie a popis možností v ovládacích prvkoch simulácie nájdete v [9\. Simulation Controls.](/docs/en/pre_processor/9_simulation_controls/9_simulation_controls/)

## Vytvoriť databázu

**Skontrolujte Data![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) **

Systém skontroluje údaje. Ak sú údaje správne, môžeme vytvoriť databázu. Ak sa však pri kontrole údajov vyskytnú chyby alebo varovania, je potrebné ich opraviť pred vytvorením databázy. Chyby zabránia vytvoreniu databázy, zatiaľ čo varovania vytvorenie databázy neumožnia.

**Vytvoriť databázu ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }})**

Kliknutím na toto tlačidlo sa vygenerovala databáza pre nastavenie. (Pozri obr. 32.2.20.)

**Pridať súbor s kľúčom**

Akékoľvek informácie, ktoré nie sú definované v sprievodcovi, ale napriek tomu sa vzťahujú na daný proces, je možné načítať ako súbor s príponou .key. Táto možnosť je užitočná aj v prípadoch, keď je potrebné zmeniť len niekoľko hodnôt – tieto hodnoty je možné definovať v súbore s príponou .key, následne stačí zmeniť len tento súbor a simuláciu je možné odoslať znovu.

  
![]({{ '/assets/images/operation_templates/30_die_stress/30_1_2d_die_stress_setup/image024.jpg' | relative_url }})

Okno „Vytvoriť databázu“

**Súvisiace témy:**

[6.1. Integrated Manufacturing Process Pre- Processor Layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_1_integrated_manufacturing_process_preprocessor_layout/)

[6.2. Integrated Manufacturing Process.Simulation layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_2_integrated_manufacturing_process_simulation_layout/)

[6.3. Integrated Manufacturing Process Post - Processor layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_3_integrated_manufacturing_process_post_layout/)

[32.1. 2D Multi Blow Forging](/docs/en/operation_templates/32_multi_blow_forging/32_1_2d_multi_blow_forging_setup/)

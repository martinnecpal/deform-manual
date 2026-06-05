---
lang: sk
title: "19. Umiestnenie objektu"
---

# 19\. Umiestnenie objektu

19.1. Polohovanie ťahaním

19.2. Umiestnenie s posunom

19.3. Umiestnenie rušenia

19.4. Rotačné polohovanie

19.5. Umiestnenie kvapky

19.6 Umiestnenie flipu

19.7. Spájané polohovanie

Dialógové okno polohovania objektu je prístupné kliknutím na tlačidlo ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) na stránke Polohovanie. (Pozri obr. 19.1. a obr. 19.2.)

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image001.jpg' | relative_url }})

Okno na polohovanie 2D objektov

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image002.jpg' | relative_url }})

Okno na polohovanie 3D objektov

Po definovaní objektu sú k dispozícii rôzne polohovacie funkcie na umiestnenie objektov do správnej polohy pred modelovaním procesu. Objekt možno pretiahnuť pomocou myši, možno ho vpustiť do dutiny matrice, posunúť o určitú vzdialenosť posunu, umiestniť pomocou interferencie alebo umiestniť pomocou rotačného pohybu. Súbor komponentov možno tiež vybrať a umiestniť spoločne pomocou spojeného polohovania.

**Aktualizovať aktuálny ťah** : Keď používateľ začiarkne toto políčko, aktuálna hodnota ťahu "polohovacieho objektu" sa aktualizuje v závislosti od polohovanej vzdialenosti.

**Aktualizácia systému Windows Nasledujúci objekt polohovania** : Keď používateľ zaškrtne toto políčko, definované okná (okná siete alebo okná prostredia) sa budú polohovať s ohľadom na metódy polohovania objektov, ako sú Drag, Interference atď., ktoré sú popísané v nasledujúcich častiach 19.1 až 19.7.

**Reset![]({{ '/assets/icons/pre_icons/mo_reset_button.jpg' | relative_url }}) **: pomocou tejto možnosti môže používateľ resetovať objekty do ich pôvodnej polohy.

## Polohovanie ťahaním

**[2D, 3D]:** Objekty možno pomocou myši ťahať alebo dynamicky otáčať v určitom smere pomocou možnosti ťahania. Ťahanie myšou v požadovanom smere, aby sme mohli umiestniť podľa našich požiadaviek. Ak vyberiete možnosť Pohyb prekladu, objekt sa preloží na základe smeru ťahania. Ak vyberiete možnosť Rotation motion, objekt sa bude otáčať na základe ťahania myšou (pozri obr. 19.3., obr. 19.4. a obr. 19.5.).

**Polohovanie riadené myšou**

Polohovanie riadené myšou sa používa na pohyb alebo otáčanie objektu tak, že používateľ môže vybrať vektor, pozdĺž ktorého môže ťahať alebo otáčať ľubovoľný určený objekt pozdĺž tohto vektora alebo okolo neho.

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image003.jpg' | relative_url }})

Okno na polohovanie ťahaním pre 2D

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image004.jpg' | relative_url }})

Okno na polohovanie ťahaním pre 3D

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image005.jpg' | relative_url }})

Príklad použitia polohovania ťahaním

## Posunutie polohy

**[2D, 3D]:** Polohovanie s posunom sa používa na posunutie objektu na pozíciu o daný posun vo zvolenom smere. Objekt, ktorý sa má polohovať, by mal byť zvýraznený v tabuľke Zoznam polohovacích objektov. Posunutie v súradniciach X, Y a Z (pre 3D) by sa malo zadať do príslušných polí. ( Obr. 19.6. a obr. 19.7.)

**Vektor vzdialenosti****:** pomocou********Vektor vzdialenosti** **možnosť používateľ musí definovať posunutie v súradniciach X, Y a Z (pre 3D) by sa mala zadať do príslušných polí.

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image006.jpg' | relative_url }})

Vektor vzdialenosti - okno na určovanie polohy s posunom pre 2D

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image007.jpg' | relative_url }})

Vektor vzdialenosti - okno na určovanie polohy s posunom pre 3D

**Dva body:** pomocou možnosti Dva body môže používateľ vykonať posun zadaním hodnôt polí Od a Do. Aj kliknutím myšou na hraničné body môže používateľ definovať hodnoty polí Od a Do. (Pozri obr. 19.8., obr. 19.9. a obr. 19.10.).

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image008.jpg' | relative_url }})

Dva body - okno na určovanie polohy s posunom pre 2D

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image009.jpg' | relative_url }})

Dva body - okno na určovanie polohy s posunom pre 3D

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image010.jpg' | relative_url }})

Príklad zobrazujúci použitie posunutého polohovania pomocou dvojbodovej metódy

**Centroid dvoch objektov typu Offset Positioning :** Používateľ môže pomocou centroidu zarovnať polohovanie objektu. (Pozri obr. 19.11.)

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image011.jpg' | relative_url }})

Príklad posunutého centroidného polohovania

## Umiestnenie rušenia

**[2D, 3D]** : Interferenčné polohovanie posúva objekt pre daný súbor "polohového" a "referenčného" vzťahu medzi dvoma objektmi, vzdialenosť medzi dvoma objektmi sa vypočíta z polohových aj referenčných objektov a potom sa menšia hodnota tejto vzdialenosti použije ako hodnota posunu pre polohovanie (pozri obr. 19.12., obr. 19.13. a obr. 19.14.). Počas procesu polohovania sa polohovaný objekt najprv posunie o veľkú vzdialenosť od referenčného objektu, potom sa posunie späť k referenčnému objektu v naznačenom smere, až kým nedôjde k prvému kontaktu.

V prípade netuhého objektu (plastického, pružného, pórovitého, elastoplastického), ak sieť neexistuje, sa na polohovanie interferencie použije geometria objektu.

**Častá otázka: Aká je primeraná hodnota interferencie?**

**Odpoveď** : Interferencia by mala byť nastavená tak, aby pri generovaní medzipredmetových okrajových podmienok bol primeraný počet uzlov v kontakte s nástrojmi. Kontaktné uzly by sa mali generovať všade tam, kde by sa mal objekt primerane dotýkať nástrojov.

To si môže vyžadovať zvýšenie alebo zníženie hodnoty interferencie aj tolerancie generovania kontaktných uzlov.

**Pred polohovaním neposúvať objekt mimo ohraničenia referenčného objektu** : možnosť interferenčného polohovania je k dispozícii pre preprocesor DEFORM-2D (od verzie 10.2.1), táto možnosť polohovania je implementovaná pre prípad deformácie pri obrábaní s podrezaným povrchom, kde interferenčné polohovanie nefungovalo správne.

Umiestňuje objekt interferenciou vzhľadom na najvnútornejšiu (vnútornú hranicu) hranicu referenčného objektu v zadanom smere.

**Napríklad** : V 2d rovinnej deformácii pre hornú časť dutého valca alebo hranola s vnútorným tlakom pôsobiacim na ľubovoľný objekt, potom tento objekt na umiestnenie voči vnútornému povrchu musíme použiť polohovanie pomocou ohraničujúceho poľa.

**Napr.** : pri nastavovaní valcovania krúžku v 3d, ak chceme umiestniť tŕň vzhľadom na vnútorný kruhový povrch obrobku alebo voči nemu, musíme použiť polohovanie pomocou ohraničujúceho poľa.

**Sledovanie smeru pohybu** : Keď používateľ začiarkne toto políčko, objekt sa umiestni vzhľadom na definovaný smer pohybu.

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image012.jpg' | relative_url }})

Okno na určovanie polohy pre 2D

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image013.jpg' | relative_url }})

Interferenčné polohovacie okno pre 3D

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image014.jpg' | relative_url }})

Príklad zobrazujúci polohovanie rušenia pri používaní

Od verzie DEFORM V12.0.2 je v polohovaní rušivých objektov k dispozícii možnosť "Prvé stretnutie" (pozri obr. 19.15). Táto možnosť umožňuje používateľovi polohovať objekt tak, že polohovací objekt príde a polohuje sa automaticky s objektom, ktorý sa na svojej pohybovej dráhe stretne ako prvý.

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image026.jpg' | relative_url }})

Prvá podporovaná referenčná možnosť

## Rotačné polohovanie

**[2D, 3D]:** Rotačné polohovanie umožňuje používateľovi otáčať ľubovoľný objekt okolo určenej osi. Os otáčania sa zadáva z bodu a smerového vektora. Zadaný uhol rotácie je kladný pre pravotočivú rotáciu okolo osi.

Pri rotačnom polohovaní môže mať polohovací objekt svoj vlastný stred objektu ako stred otáčania. Uhol (stupeň) sa meria v protichodnom smere. (Pozri obr. 19.16. až obr. 19.20.)

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image015.jpg' | relative_url }})

Rotačné polohovacie okno pre 2D

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image016.jpg' | relative_url }})

Rotačné polohovacie okno pre 3D

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image017.jpg' | relative_url }})

2D Príklad zobrazujúci použitie polohovania rotácie

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image018.jpg' | relative_url }})

3D Príklad 1 zobrazujúci použitie polohovania rotácie

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image019.jpg' | relative_url }})

3D Príklad 2 zobrazujúci použitie polohovania rotácie

## Umiestnenie kvapky

**[3D]:** Polohovanie kvapky sa používa na posunutie objektu smerom k inému objektu rušivým vplyvom alebo vplyvom gravitácie (pozri obr. 19.21. a obr. 19.22.).

  * **Povolenie rotácie len o:** Používateľ môže obmedziť smer rotácie pustením objektu zaškrtnutím políčka a uvedeného smeru.

  * **Nepovoliť otáčanie:** Ak používateľ nechce definovať otáčanie pred upustením objektu, začiarknutím tohto políčka môže vykonať polohovanie pri upustení.

  * **Uložiť filmový súbor:** Začiarknutím tohto políčka môže používateľ uložiť animáciu polohovania kvapky.

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image020.jpg' | relative_url }})

Okno 3D Drop Positioning

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image021.jpg' | relative_url }})

Príklad použitia polohovania Drop

  * **Gravitačná aktivácia** : V prípade aktivácie gravitácie by umiestnený objekt mal byť objektom s okami. Smer by mal byť smer, ktorým by ho gravitácia hnala k pádu na iný objekt. Objekt sa môže pohybovať v 6 stupňoch voľnosti (3 smery translácie a 3 osi rotácie) bez akéhokoľvek daného obmedzenia. Obmedzenie v smere otáčania možno pridať, ak sa vyžaduje len jeden stupeň voľnosti otáčania. Ak sa vyžaduje len jeden smer otáčania, treba vybrať možnosť Allow rotation only about box (Povoliť otáčanie len okolo poľa) a určiť vektor, okolo ktorého sa má otáčať.

  * **Gravitácia nie je aktivovaná** : V prípade, že gravitácia nie je aktivovaná, správa sa presne ako metóda interferenčného polohovania.

## Flipové polohovanie

**[2D]** : Prevrátenie umožňuje používateľovi zrkadliť objekt okolo vybranej osi alebo ľubovoľnej čiary rovnobežnej s vybranou osou, ako je znázornené na obr. 19.23 a obr. 19.24.

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image022.jpg' | relative_url }})

2D okno Flip Positioning

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image023.jpg' | relative_url }})

Príklad použitia polohovania flipu

## Spájané polohovanie

**[2D, 3D]** : Umožňuje pohyb viacerých objektov pri rovnakej polohovacej akcii (pozri obr. 19.25. a obr. 19.26.). Zaškrtnutím objektov v dialógovom okne polohovania dvojice sa objekty polohujú presne o rovnakú hodnotu ako polohovaný objekt.

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image024.jpg' | relative_url }})

Spájané okno polohovania

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image025.jpg' | relative_url }})

Príklad zobrazujúci použitie polohovania páru s možnosťou Drag positioning

****

**Súvisiace témy:**

[2D-Primitive geometries](../12_geometry_modelling/12_1_2d_geometry_data_defining.htm#Define_Primitives)

[3D-Primitive geometries](../12_geometry_modelling/12_3_3d_geometry_data_defining.htm#Define_Primitive)

[12\. Geometry Modelling](/docs/sk/pre_processor/12_geometry_modelling/12_geometry_modelling/)

[13\. Mesh Generation](/docs/sk/pre_processor/13_mesh_generation/13_mesh_generation/)

[Selecting the Movement direction of the objects](../15_movement_controls_definition/15_movement_controls_settings.htm#Directions)

[20\. Inter-object Data Definition](/docs/sk/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/)

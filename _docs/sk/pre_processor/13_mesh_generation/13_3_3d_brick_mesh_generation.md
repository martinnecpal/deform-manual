---
lang: sk
title: "13.3. Generovanie 3D siete z tehál"
---

# 13.3. Generovanie 3D siete z tehál

13.3.1. Všeobecné nastavenia pre Brick mesh
13.3.2. 2D prierez pre tehlovú sieť
13.3.3. Faktory váženia siete
13.3.4. Okno hustoty siete pre tehlovú sieť
13.3.5. Povlaková sieť
13.3.6. Kritériá na opravu
13.3.7. Rozšírené nastavenia

Na nasledujúcom Obr. 13.3.1. sú zobrazené možnosti generovania siete Brick v režime Expert.

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_3_3d_brick_mesh_generation/13_3_image001.jpg' | relative_url }})

Expertný režim Generovanie siete Brick

## Všeobecné nastavenia pre Brick mesh

**Jednotná hrúbka vrstiev** : Keď je táto možnosť vybratá, na základe počtu definovaných vrstiev sa vytvorí sieť s rovnomernou hrúbkou vrstiev.

**Oblasti s jemnejšou sieťou** :Používateľ môže definovať oblasti s jemnejšou sieťou definovaním počtu vrstiev požadovaných v rámci určenej oblasti, ako je znázornené na obr. 13.3.2.

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_3_3d_brick_mesh_generation/13_3_image003.jpg' | relative_url }})

Definícia oblastí s jemnejšou sieťou

Hustotu vrstiev siete môžete ovládať pomocou možnosti Fine Mesh areas. Používateľ môže kontrolovať počet vrstiev siete v rámci oblasti výberom počiatočného a koncového bodu oblasti. Na obr. 13.3.3. je znázornený objekt s premenlivou hustotou siete.

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_3_3d_brick_mesh_generation/13_3_image002.jpg' | relative_url }})

Príklad zobrazujúci definíciu oblastí s jemnejšou sieťou

**Aplikácia listu:**

Možnosť aplikácie listu aktivuje remeshing založený na projekcii pre objekty v tvare listu, ktoré boli skonštruované pomocou tehlových prvkov. Nastavenie sa vzťahuje len na objekt, ktorý bol pôvodne vytvorený ako 2D sieť a potom vytlačený do 3D siete.

Ak je možnosť aplikácie listu deaktivovaná (predvolené nastavenie), objekt sa pri každom následnom remeshovaní sieťuje pomocou tetových prvkov.

Ak je toto nastavenie aktivované, pokúsi sa o remeselnú úpravu tehál pomocou projekčných techník. Omietanie sa vráti k tetovým prvkom, ak sa deformovaný tvar výrazne odchyľuje od tvaru plechu, pretože takýto stav môže spôsobiť zlyhanie omietania tehál z plechu. (Pozri obr. 13.3.4.)

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_3_3d_brick_mesh_generation/13_3_image009.jpg' | relative_url }})

Vybraná možnosť aplikácie hárkov

## 2D prierez pre sieť Brick

Na vytvorenie tehlovej siete sa definuje 2D prierez, ktorý sa v závislosti od požiadavky na 3D geometriu buď vytlačí, alebo sa otáča s určeným počtom vrstiev.

**Generovanie mapovej siete** : Mapované siete možno použiť v počiatočných fázach procesu tvárnenia. Keďže geometria obrobku nadobúda počas tvárnenia zložitý tvar, sieť je vystavená niekoľkým zmenám sieťovania a mapované sieťovanie nemusí byť schopné prežiť takéto zmeny geometrie a zmena sieťovania môže zlyhať. Generovanie mapovanej siete je vidieť na obr. 13.3.5.

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_3_3d_brick_mesh_generation/13_3_image004.jpg' | relative_url }})

Generovanie mapovanej siete pre 2D prierez

**Použiť hrubú vnútornú sieť:** Používateľ môže vytvoriť hrubú sieť vo vnútri oblasti, ako je znázornené na obr. 13.3.6.

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_3_3d_brick_mesh_generation/13_3_image005.jpg' | relative_url }})

Generovanie hrubej vnútornej siete pre 2D prierez

## Váhové faktory siete

Váhové faktory alebo parametre (systémovo definovaná hustota siete) pre hraničné zakrivenie, teplotu, deformáciu a mieru deformácie určujú relatívne váhy hustoty siete, ktoré sa majú priradiť príslušnému parametru. Ďalšie informácie nájdete v časti [13.2.5. Mesh weighting factors.](13_2_3d_tet_mesh_generation.htm#13.2.5._Mesh_weighting_factors)

## **Okienko hustoty siete pre sieť Brick**

Koncept okna Hustota siete (pozri obr. 13.3.7.) je podobný konceptu hustoty siete definovanej používateľom. Hustota siete zadaná pre dané okno sa aplikuje na akýkoľvek geometrický bod (uzol alebo vrchol STL) vo vnútri okna. Okno hustoty siete sa však používa počas opätovného sieťovania aj počiatočného generovania siete, zatiaľ čo hustoty siete definované používateľom sa používajú len počas počiatočného generovania. Môže jej byť tiež priradená rýchlosť alebo môže sledovať pohyb iného objektu a môže byť definovaná v oblasti, cez ktorú ešte nebol obrobok deformovaný.

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_3_3d_brick_mesh_generation/13_3_image006.jpg' | relative_url }})

Okná hustoty siete pre 2D

## Povlak Mesh

Používateľ môže pomocou tejto možnosti pridať vrstvy povlaku a vygenerovať pre ne sieť. Povlaková sieť je tenká vrstva prvkov pozdĺž hranice objektu so špecifickými vlastnosťami. Pre pridané povlakové vrstvy môže používateľ priradiť materiál. Ďalšie informácie o používaní povlakovej siete nájdete v dokumente [Appendix XI](/docs/sk/appendices/appendix_xi__near_surface_mesh_functions/).

## Kritériá odstraňovania

Kritériá remeshingu (Autoremesh) sú najvhodnejším spôsobom, ako zvládnuť remeshing objektov, ktoré prechádzajú veľkou plastickou deformáciou. Okno Remeshing Criteria (Kritériá opätovného remeshovania) (pozri obr. 13.3.8.) obsahuje skupinu parametrov, ktoré riadia, kedy a ako často sa bude sieť na objekte s okom regenerovať na základe priradenia určitých spúšťačov. Existujú štyri kľúčové slová, ktoré riadia spustenie postupu remeshingu pre objekt, sú to Hĺbka zásahu ([RMDPTH](/docs/sk/keyword_documentation/r/rmdpth/)),Max. Time Increment ([RMTIME](/docs/sk/keyword_documentation/r/rmtime/)), Max. Step Increment ([RMSTEP](/docs/sk/keyword_documentation/r/rmstep/)) a Max. Prírastok zdvihu ([RMSTRK](/docs/sk/keyword_documentation/r/rmstrk/)). Keď sa splnia kritériá remeshovania podľa niektorého z týchto kľúčových slov alebo sa sieť stane nepoužiteľnou (záporný jakobián), objekt sa remeshuje. Ak objekt počas simulácie splní niektoré z kritérií remeshingu, vygeneruje sa nová sieť, informácie o riešení zo starej siete sa interpolujú na novú sieť a simulácia pokračuje.

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_3_3d_brick_mesh_generation/13_3_image007.jpg' | relative_url }})

Možnosť kritérií Remesh pre sieť Brick

  
Podrobnosti o maximálnej hĺbke zásahu (RMDPTH), maximálnom prírastku zdvihu (RMSTRK), maximálnom prírastku času (RMTIME), maximálnom prírastku kroku (RMSTEP) a účele kritérií nájdete v časti [13.2.8. Remeshing criteria.](13_2_3d_tet_mesh_generation.htm#13.2.8._Remeshing_criteria)

## Rozšírené nastavenia

  
Na nasledujúcom Obr. 13.3.9. je zobrazené okno Advanced Settings (Rozšírené nastavenia) pre 3D Brick mesh.

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_3_3d_brick_mesh_generation/13_3_image008.jpg' | relative_url }})

Okno pokročilých nastavení pre sieť Brick

**Rozlíšenie siete**(**MGGRID**)

Keď je objekt vynesený do 2D siete, na diskretizáciu hustoty siete v celej východiskovej geometrii je potrebná vzorkovacia sieť. Rozlíšenie mriežky ([MGGRID](/docs/sk/keyword_documentation/m/mggrid/)) určuje rozstupy vzorkovacích mriežok, ktoré sa používajú na vzorkovanie hustoty siete. Zvýšenie hodnoty delenia X alebo delenia Y bude mať za následok ostrejšie gradienty medzi oblasťami s rôznou hustotou siete. V prípade zaslepenia, keď sa vyžaduje veľmi vysoký gradient siete v úzkej oblasti, môže byť potrebné tieto hodnoty zvýšiť, aby sa zachytili veľké zmeny gradientu siete na krátkych vzdialenostiach.

**Parametre pridávania uzlov** (**MGERR**)
Parametre pridávania uzlov ([MGERR](/docs/sk/keyword_documentation/m/mgerr/)) určujú maximálnu povolenú chybu vzdialenosti a uhla medzi hranicou objektu a jeho pridruženou stranou prvku mriežky. Tolerancie vzdialenosti a uhla sa používajú na zachytenie kritickej geometrie hraníc, ktorá by sa inak mohla stratiť pri generovaní siete. Ak sa vyžaduje, aby objekt zachytil veľmi malé prvky, maximálna vzdialenosť sa môže znížiť, alebo ak je potrebné umiestniť uzol na malom uhle, môže sa znížiť aj chyba uhla. Len zriedkakedy bude musieť používateľ tieto hodnoty meniť. V prípade dielov, ktoré sú veľmi malé, je hodnota 0,01 % ohraničenia objektu dobrým východiskovým číslom, ktoré možno použiť pre [MGERR](/docs/sk/keyword_documentation/m/mgerr/) na lepšiu manipuláciu s rozlíšením siete.

Súvisiace témy:

[13\. Mesh Generation](/docs/sk/pre_processor/13_mesh_generation/13_mesh_generation/)

[13.1. 2D Mesh Generation](/docs/sk/pre_processor/13_mesh_generation/13_1_2d_mesh_generation/)

[13.2. 3D Tet Mesh Generation](/docs/sk/pre_processor/13_mesh_generation/13_2_3d_tet_mesh_generation/)

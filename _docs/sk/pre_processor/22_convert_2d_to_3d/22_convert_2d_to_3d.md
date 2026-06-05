---
lang: sk
title: "22. Premena 2D na 3D"
---

# 22\. Premena 2D na 3D ![]({{ '/assets/icons/pre_icons/convert_2d_to_3d_icon.jpg' | relative_url }})

22.1. Úvod do integrovaného konverzného modulu

22.2. Postup konverzie objektov z 2D do 3D

22.3. Pokročilé nastavenia geometrie

Integrovaný systém dokáže spracovať aj 2D databázy, aj 3D databázy; jedna databáza môže obsahovať buď 2D výsledky, 3D výsledky, alebo hybridné 2D/3D výsledky. Každý krok bude buď 2D, alebo 3D. Integrovaný systém ponúka zjednodušený tok dát, rýchle nastavenie 3D úlohy z 2D úlohy, rýchle nastavenie 2D úlohy z 3D úlohy (vo vývoji) a jednoduché porovnanie medzi 2D a 3D výsledkami.

Predspracovateľ ponúka dvojaké definície, zjednotený formát [simulation controls](/docs/sk/pre_processor/9_simulation_controls/9_simulation_controls/), integrovaný konverzný modul a konverziu modelov z 2D do 3D.

Integrovaná databáza ponúka jednotné úložisko na ukladanie a načítavanie 2D a 3D simulačných údajov. Integrovaná databáza bude obsahovať informácie o rozmeroch a čísle verzie pre každý krok a ukladá 2D a 3D simulácie do jednej databázy.

Predspracovateľ bol vybavený možnosťou prepínania medzi 2D a 3D režimom (pozri obr. 22.1.).

**Zobraziť 2D model ![]({{ '/assets/icons/pre_icons/show_2d_model.jpg' | relative_url }}) **: Pomocou tohto tlačidla môže používateľ po konverzii prepnúť do 2D režimu.

**Zobraziť 3D model ![]({{ '/assets/icons/pre_icons/show_3d_model.jpg' | relative_url }}) **: Pomocou tohto tlačidla môže používateľ po konverzii prepnúť do 3D režimu.

![]({{ '/assets/images/pre-processor/22_convert_2d_to_3d/image001.jpg' | relative_url }})

Okno predspracovateľa grafického rozhrania s tlačidlami pre 2D a 3D režim a tlačidlom na konverziu objektu

## Úvod do integrovaného konverzného modulu

Vstavaný konverzný modul predstavuje vylepšenie predchádzajúcej možnosti pokročilej geometrie.

Rýchle vytvorenie 3D geometrie z 2D geometrie je možné dosiahnuť pomocou možnosti typu „Revolution“ a možnosti typu „Extrusion“, ktoré sú k dispozícii v rozšírených nastaveniach geometrie.

Rýchle vytvorenie 3D siete z 2D siete je možné pomocou vstavaného konverzného modulu, ako je znázornené na obr. 22.2. Ako vstupné údaje dokáže spracovať súbory s kľúčovými slovami aj databázové súbory. Používateľ môže konvertovať jeden objekt alebo viacero objektov naraz. Na prepojenie 2D a 3D modelu bola zavedená konverzná os. Tá sa aktualizuje počas polohovania. Používateľ môže ovládať uhly otáčania a počiatočné uhly objektu (pozri obr. 22.3.).

![]({{ '/assets/images/pre-processor/22_convert_2d_to_3d/image002.jpg' | relative_url }})

Okno programu 2D to 3D Converter pred konverziou

![]({{ '/assets/images/pre-processor/22_convert_2d_to_3d/image003.jpg' | relative_url }})

Okno programu 2D to 3D Converter po konverzii

## Postup pri prevode objektov z 2D do 3D

  1. **Spustite konvertor 2D na 3D**: Otvorte 2D nastavenie v predprocesore. Kliknite na konvertor (![]({{ '/assets/icons/pre_icons/convert_2d_to_3d_icon.jpg' | relative_url }})) a prekonvertujte celé nastavenie.

  1. **Zoznam objektov**: Používateľ môže vybrať objekty zo zoznamu zaškrtnutím políčka vedľa príslušných objektov.

  1. **Výber súradnicového systému**: Smer osí pre otáčanie alebo vytláčanie je možné zvoliť v súradnicovom systéme

  1. **3D parametre** :

  * Ak chcete otočiť 2D rez do 3D, môžete na karte „3D parametre“ zadať počiatočný uhol, uhol otáčania a toleranciu.

  * Pri extrudovaní 2D rezu do 3D je potrebné určiť dĺžku extrudovania a počiatočnú polohu.

  1. **Geometria**: Ak je potrebné previesť len geometriu, je nutné určiť počet rezov a zaškrtnúť políčko „Skontrolovať výstupnú geometriu“.

  1. **Sieť**: V prípade objektov so sieťou zapnite výstupnú sieť a vyberte typ siete. Zadajte počet 3D prvkov pre objekty so sieťou. Pomocou tlačidla „Pokročilé“ môžete nastaviť rôzne parametre 3D siete. Ďalšie informácie nájdete v dokumentácii [13.2. 3D Tet Mesh Data Generation](/docs/sk/pre_processor/13_mesh_generation/13_2_3d_tet_mesh_generation/) a [13.3. 3D Brick Mesh Generation](/docs/sk/pre_processor/13_mesh_generation/13_3_3d_brick_mesh_generation/).

  1. **Preview![]({{ '/assets/icons/pre_icons/converter_preview_button.jpg' | relative_url }}) **: Túto funkciu možno použiť na náhľad objektov.

  1. **Convert![]({{ '/assets/icons/pre_icons/converter_convert_button.jpg' | relative_url }}) **: Túto funkciu je možné použiť na konverziu objektov.

  1. Nastavenia 3D modelu je možné aktivovať kliknutím na ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), čím sa prepnete do 3D režimu, v ktorom sa zobrazia konvertované objekty.

Tlačidlom ![]({{ '/assets/icons/pre_icons/converter_cancel_button.jpg' | relative_url }}) môžete opustiť okno konvertora bez uloženia zmien.

Tlačidlom ![]({{ '/assets/icons/pre_icons/converter_2d_toggle_button.jpg' | relative_url }}) môžete po konverzii prepínať medzi 2D a 3D zobrazením.

Používateľ môže vytvoriť objekt s tetrahedrálnou sieťou pomocou voľby [3D mesh windows](../13_mesh_generation/13_2_3d_tet_mesh_generation.htm#13.2.6._Mesh_density_windows) (pozri obr. 22.4.) a s tehlovou sieťou pomocou voľby [2D mesh windows](../13_mesh_generation/13_3_3d_brick_mesh_generation.htm#Fig._13.3.6.Mesh_density_windows_for_2D) (pozri obr. 22.5.) s plnou kontrolou nad parametrami vytvárania siete vrátane váhových faktorov. Okno hustoty 2D siete (typ polylínia) sa počas konverzie zmení na okno hustoty siete typu polygónová plocha. (Pozri obr. 22.6.)

![]({{ '/assets/images/pre-processor/22_convert_2d_to_3d/image004.jpg' | relative_url }})

Model mriežky tehál vytvorený pomocou okna 2D Mesh

![]({{ '/assets/images/pre-processor/22_convert_2d_to_3d/image005.jpg' | relative_url }})

Model so sieťou tetraédrov vytvorený pomocou okna 2D Mesh

![]({{ '/assets/images/pre-processor/22_convert_2d_to_3d/image006.jpg' | relative_url }})

Spracovanie okien s hustotou mriežky

Používateľ môže využiť interpolačný modul priamo z integrovaného okna pre konverziu na zobrazenie hodnôt napätia, deformácie a teploty.

Pri konverzii modelu z 2D do 3D sa priradenia [symmetry plane](../14_boundary_conditions/14_1_symmetry_boundary_conditions.htm#Fig._14.1.1_Symmetry_plane_BCC_for_quarter_symmetry_model) a [BCC](/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/) spolu s materiálmi automaticky priradia k príslušným objektom. (Pozri [Fig. 22.7.](22_convert_2d_to_3d.htm#Fig_22_7_Automated_symmetry_plane_assignment_to_die/workpiece_geometry_and_boundary_code_assignment_for_mesh))

![]({{ '/assets/images/pre-processor/22_convert_2d_to_3d/image007.jpg' | relative_url }})

Automatické priradenie symetrickej roviny k geometrii formy/obrobku a priradenie okrajových podmienok pre sieť

##  Pokročilé nastavenia geometrie

  
**Extrudovať**  
Používateľ môže na stránke „3D geometrické primitíva“ importovať alebo vytvoriť 2D rez geometrie a vytiahnuť ho v požadovanom smere. To je možné urobiť aj pri importe súborov 2D priečnych rezov z databázy alebo kľúčového súboru. Pri konverzii 2D modelu na 3D model sa štandardne ako smer vytiahnutia používa os Z (pozri obr. 22.8).

![]({{ '/assets/images/pre-processor/22_convert_2d_to_3d/image008.jpg' | relative_url }})

Extrudovaný objekt vo výkladnej skrine

**Revolve**  
Na stránke „3D geometrické primitíva“ môže používateľ importovať alebo vytvoriť 2D rez geometrie a na základe symetrie ju otočiť, čím získa 3D geometriu. Túto funkciu je možné využiť na vytvorenie 3D geometrie z 2D geometrie, ak nie je geometria príliš zložitá.

Používateľ môže podľa potreby nastaviť uhol otočenia, smer a otočené časti geometrie (pozri obr. 22.9.).

![]({{ '/assets/images/pre-processor/22_convert_2d_to_3d/image009.jpg' | relative_url }})

2D geometria sa prevádza na 3D geometriu pomocou prepočtu v smere Z

**Súvisiace témy:**

[2D Geometry Data Defining](/docs/sk/pre_processor/12_geometry_modelling/12_1_2d_geometry_data_defining/)

[3D Geometry Data Defining](/docs/sk/pre_processor/12_geometry_modelling/12_3_3d_geometry_data_defining/)

[2D Mesh Data Generation](/docs/sk/pre_processor/13_mesh_generation/13_1_2d_mesh_generation/)

[3D Tet Mesh Generation](/docs/sk/pre_processor/13_mesh_generation/13_2_3d_tet_mesh_generation/)

[3D Brick Mesh Generation](/docs/sk/pre_processor/13_mesh_generation/13_3_3d_brick_mesh_generation/)

[Boundary condition](/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/)

[Simulation controls](/docs/sk/pre_processor/9_simulation_controls/9_simulation_controls/)

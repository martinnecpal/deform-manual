---
lang: sk
title: "14.4. Difúzne okrajové podmienky"
---

# 14.4. Difúzne okrajové podmienky

14.4.1. Difúzia s prostredím BCC

14.4.2. Obsah atómu BCC

14.4.3. Atómový tok BCC

14.4.4. Pokročilá difúzia BCC

## Difúzia s prostredím BCC [2D/3D]

Určuje difúziu dominantného atómu cez hraničné prvky ohraničené uvedenými uzlami. Obsah dominantného atómu prostredia ([ECCATM]({{ '/docs/sk/keyword_documentation/e/eccatm/' | relative_url }})) a rýchlosť povrchovej reakcie sa špecifikujú v ponuke Simulation Controls (Ovládanie simulácie), Processing Conditions (Podmienky spracovania). Obsah prostredia a rýchlosť reakcie pre rôzne oblasti súčiastky možno upraviť pomocou difúznych okien.

## Pevný obsah atómov BCC [2D/3D]

Určuje pevný dominantný obsah atómov v daných uzloch.

## Atomový tok BCC [2D/3D]

Určuje pevnú rýchlosť toku dominantného atómu cez prvky ohraničené uvedenými hranami. Tok atómov môže byť definovaný ako konštanta alebo ako funkcia. Kľúčové slová pre túto funkciu sú [ECCATM]({{ '/docs/sk/keyword_documentation/e/eccatm/' | relative_url }}) a [ECAFLX]({{ '/docs/sk/keyword_documentation/e/ecaflx/' | relative_url }}).

## Pokročilá difúzia BCC [2D/3D]

Účelom tejto definície okrajových podmienok je umožniť používateľovi flexibilne špecifikovať všetky rôzne typy difúznych okrajových podmienok na tej istej hrane. Používateľ môže zadať buď číslo používateľského podprogramu, alebo lokálnu definíciu difúzie. (Pozri obr. 14.4.1.) Ak chce používateľ zadať používateľskú rutinu, je potrebné zadať číslo používateľskej rutiny. Zadané číslo užívateľskej rutiny bude zodpovedať podrutine, ktorej bude zodpovedať okrajová podmienka. Ďalšie informácie o používaní týchto používateľských okrajových podmienok nájdete v časti User Routines (Používateľské rutiny). Ak číslo rutiny zostane nulové, používateľ potom môže definovať lokálne definovanú okrajovú podmienku, kde je potrebné určiť obsah atómov prostredia, koeficient reakčnej rýchlosti a tok atómov hrany. Všetky tieto tri premenné môžu byť definované ako konštanty alebo funkcie. Ak chcete použiť lokálnu hraničnú podmienku definovanú používateľom, nastavte požadované premenné, nastavte lokálne definované číslo na jedinečnú hodnotu a použite ju na sadu hrán prvkov. Kľúčové slová na tento účel sú [ECCATM]({{ '/docs/sk/keyword_documentation/e/eccatm/' | relative_url }}) , [ECAFLX]({{ '/docs/sk/keyword_documentation/e/ecaflx/' | relative_url }})a [LOCATM]({{ '/docs/sk/keyword_documentation/l/locatm/' | relative_url }}).

![]({{ '/assets/images/pre-processor/14_boundary_conditions/14_4__diffusion_boundary_conditions/14_4_image001.jpg' | relative_url }})

Pokročilé okno okrajovej podmienky objektu Difúzia

Vo V12 môžeme definovať možnosti Diffusion BCC pre každý typ atómu zvlášť, oba typy atómov môžeme pozorovať na stránke Simulation controls [Diffusion]({{ '/docs/sk/pre_processor/9_simulation_controls/9_6_process_conditions/' | relative_url }}#9.6.2._Diffusion_). (Pozri obr. 14.4.2.)

![]({{ '/assets/images/pre-processor/14_boundary_conditions/14_4__diffusion_boundary_conditions/14_4_image002.jpg' | relative_url }})

Výber iného typu atómu z rozbaľovacieho zoznamu

**Súvisiace témy:**

[14\. Boundary Conditions]({{ '/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/' | relative_url }})

[14.1. Symmetry Boundary Conditions]({{ '/docs/sk/pre_processor/14_boundary_conditions/14_1_symmetry_boundary_conditions/' | relative_url }})

[14.2. Deformation Boundary Conditions]({{ '/docs/sk/pre_processor/14_boundary_conditions/14_2_deformation_boundary_conditions/' | relative_url }})

[14.3. Thermal Boundary Conditions]({{ '/docs/sk/pre_processor/14_boundary_conditions/14_3_thermal_boundary_conditions/' | relative_url }})

[14.5. Heating Boundary Conditions]({{ '/docs/sk/pre_processor/14_boundary_conditions/14_5_heating_boundary_conditions/' | relative_url }})

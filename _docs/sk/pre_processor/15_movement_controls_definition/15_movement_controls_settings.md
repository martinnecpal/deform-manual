---
lang: sk
title: "15. Nastavenia ovládania pohybu"
---

# 15\. Nastavenia ovládania pohybu

15.1. Typy kontrol pohybu
15.1.1. Pohyb v preklade
15.1.2. Rotačný pohyb
15.1.3. Krútiaci pohyb
15.1.4. Pohyb pri zváraní trením
15.2. Priradenie pohybu deformovateľným objektom
15.3. Nástroje na ovládanie pohybu

15.4. Používateľská rutina kontroly pohybu

Ovládacie prvky pohybu možno použiť na tuhé objekty a hraničné uzly sieťovaných objektov. Povrch definovaný týmito uzlami možno považovať za "tuhý povrch". Počas simulácie sa ohraničené uzly budú synchrónne pohybovať rýchlosťou a smerom definovaným ovládacími prvkami pohybu. Okná ovládacích prvkov pohybu pre 2D a 3D sú znázornené na obr. 15.1., resp. na obr. 15.2.

![]({{ '/assets/images/pre-processor/15_movement_controls/15_image001.jpg' | relative_url }})

Okno nastavení ovládacích prvkov pohybu 2D

![]({{ '/assets/images/pre-processor/15_movement_controls/15_image002.jpg' | relative_url }})

Okno nastavení ovládacích prvkov 3D Movement

## Ovládacie prvky pohybu Typy

Pre 3D objekt sa ovládanie pohybu rozdeľuje na ovládanie translačného pohybu a ovládanie rotačného pohybu.

Pre typ geometrie 2D Axisymmetric máme k dispozícii ovládacie prvky pohybu Translation.

Pre geometriu typu 2D Torsion máme k dispozícii ovládacie prvky pre pohyb v translácii a torzii.

Pre geometriu typu 2D Plane stress a Plane strain máme k dispozícii ovládacie prvky pohybu Translation a Rotation.

Pre geometriu 2,5D trecieho zvárania máme k dispozícii ovládacie prvky prekladu a trecieho zvárania.

### **Prekladový pohyb**

Počas simulácie sa obmedzené uzly pohybujú synchrónne rýchlosťou a smerom definovaným ovládacími prvkami pohybu. Typy ovládacích prvkov pohybu, ktoré sú k dispozícii v ovládacích prvkoch pohybu prekladu, sú rýchlosť, sila, kladivo, skrutkový lis, mechanický lis, hydraulický lis, posuvná matrica a cesta. Translačný pohyb pre 2D a 3D je znázornený na obr. 15.1 a obr. 15.2. Ďalšie informácie nájdete v častiach [15.1. Speed](/docs/sk/pre_processor/15_movement_controls_definition/15_1_speed/), [15.2. Force](/docs/sk/pre_processor/15_movement_controls_definition/15_2_force/), [15.3. Hammer](/docs/sk/pre_processor/15_movement_controls_definition/15_3_hammer/), [15.4. Screw press](/docs/sk/pre_processor/15_movement_controls_definition/15_4_screw_press/), [15.5. Mechanical press](/docs/sk/pre_processor/15_movement_controls_definition/15_5_mechanical_press/), [15.6. Hydraulic press](/docs/sk/pre_processor/15_movement_controls_definition/15_6_hydraulic_press/), [15.7. Sliding Die](/docs/sk/pre_processor/15_movement_controls_definition/15_7_sliding_die/) a [15.8. Path](/docs/sk/pre_processor/15_movement_controls_definition/15_8_path/).

### **Rotačný pohyb**

****Rotačný pohyb je definovaný uhlovou rýchlosťou/krútiacim momentom okolo pevného stredu otáčania. Tento typ pohybu spôsobuje len rotáciu. Ak nie je uvedené inak, translácia je obmedzená. Rotačná rýchlosť sa riadi prostredníctvom voľby Controlling Method (Spôsob riadenia) a bod, okolo ktorého sa objekt otáča, sa nastavuje prostredníctvom Center of Rotational Movement (Stred rotačného pohybu). Ďalšie informácie nájdete v časti[15.9. Rotational Movement](/docs/sk/pre_processor/15_movement_controls_definition/15_9_rotational_movement/).

### **Krútiaci pohyb**

Kontrola krútenia sa uplatňuje len v prípade krútiacich sa formulácií. Táto možnosť riadenia pohybu je aktívna len pre DEFORM-2D. Ďalšie informácie nájdete v časti [15.10. Torsional movement](/docs/sk/pre_processor/15_movement_controls_definition/15_10_torsional_movement/).

### **Pohyb frikčného zvárania**

Kontrola pohybu pri trecom zváraní sa uplatňuje len v prípade 2,5D formulácií trecieho zvárania. Táto možnosť riadenia pohybu je aktívna len v prípade DEFORM-2D. Ďalšie informácie nájdete v časti [15.11. Friction Welding movement](/docs/sk/pre_processor/15_movement_controls_definition/15_11_friction_welding_movement/).

**Smery [2D, 3D]** : Na základe nastavenia problému môže používateľ vybrať smer pohybu prekladu. Pre výber uhlových smerov je k dispozícii aj možnosť Iné smery.

Pre 2D model sú k dispozícii smery X, Y, -X, -Y a Iné. Typ iného smeru vyžaduje uhol v stupňoch spolu so znamienkom, pričom znamienko +ve označuje smer nahor a znamienko -ve označuje smer nadol.

Pre 3D model sú k dispozícii smery X,Y,Z,-X,-Y,-Z a iné. Typ Other direction (Iný smer) potrebuje smerové vektory so znamienkami pozdĺž smerov X, Y a Z. Napríklad ak sa kocka pohybuje v oboch smeroch +ve Y a -ve Z, potom v poliach vektorov iných smerov musia byť definované (0,1,-1).

## Priradenie pohybu deformovateľným objektom

[2D, 3D]: V prípade štúdie spojeného napätia alebo inej situácie, keď používateľ potrebuje definovať translačný pohyb pre deformovateľné objekty, ako napríklad elastický, plastický, elastoplastický a porézny pohyb, musí byť pre tento objekt definovaný strom BCC. Pohybová hraničná podmienka definovaná rovinou musí byť povrch, ktorý nie je v kontakte s inými objektmi, kde je zamýšľaná deformácia, pretože pohybová BCC definovaná rovina sa nebude deformovať, ale pohybovať sa s definovaným translačným pohybom. (Pozri obr. 15.3. a obr. 15.4.)

![]({{ '/assets/images/pre-processor/15_movement_controls/15_image004.jpg' | relative_url }})

Definícia 2D Movement BCC pre pružné lisovacie formy na spojenú analýzu napätia v lisovacích formách

![]({{ '/assets/images/pre-processor/15_movement_controls/15_image005.jpg' | relative_url }})

Definícia 3D Movement BCC pre pružné matrice na analýzu napätia v matrici

## Nástroje na ovládanie pohybu

**Nastavenie ovládacích prvkov pohybu** : Pomocou možností Importovať pohyb zo súboru ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) a Načítať pohyb z knižnice ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) môže používateľ importovať uložený pohyb do objektu.

****Uloženie nastavení ovládania pohybu**** : Pomocou možností Uložiť pohyb do súboru ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) a Uložiť pohyb do knižnice ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) môže používateľ uložiť údaje o pohybe.

**Náhľad pohybu** ![]({{ '/assets/icons/pre_icons/mo_preview_icon.jpg' | relative_url }}): Kliknutím na tlačidlo náhľadu si používateľ môže pozrieť pohyb, ktorý bol zadaný pre daný objekt (pozri obr. 15.5.). Možnosti v dialógovom okne náhľadu pohybu umožňujú používateľovi vidieť pohyb aktuálneho objektu na obrazovke displeja. Pritom sa zohľadní len translačný a rotačný pohyb, ale nie riadenie sily alebo krútiaceho momentu.

![]({{ '/assets/images/pre-processor/15_movement_controls/15_image003.jpg' | relative_url }})

Okno náhľadu pohybu

**Odstrániť nastavenia ovládacích prvkov pohybu** ![]({{ '/assets/icons/pre_icons/mo_clear_icon.jpg' | relative_url }}): Pomocou tejto možnosti môže používateľ odstrániť priradené údaje o pohybe.

## Používateľské podprogramy na riadenie pohybu

[2D, 3D]: Komplexný pohyb kocky možno definovať pomocou podprogramov jazyka FORTRAN definovaných používateľom. Rutina USRDSP umožňuje používateľovi vypočítať rýchlosť tuhého objektu, ktorý má pohyb definovaný ako používateľský model. Popis implementácie používateľsky definovaných podprogramov nájdete v časti [chapter 56.2.3.2 USER ROUTINE USRDSP](../../user_routines/56_user_routines_in_deform/56_2_2d_user_defined_fem_routines.htm#56_2_3_2_User_defined_movement_control_\(USRDSP\)) pre 2D a 3D. Číslo definovanej rutiny musí byť uvedené v okne ovládania pohybu, ako je znázornené na nasledujúcich obr. 15.6. a obr. 15.7.

![]({{ '/assets/images/pre-processor/15_movement_controls/15_image006.jpg' | relative_url }})

2D Kontrola pohybu sily Okno volania čísla užívateľskej rutiny

![]({{ '/assets/images/pre-processor/15_movement_controls/15_image007.jpg' | relative_url }})

3D Riadenie pohybu rýchlosti Okno na vyvolanie čísla používateľskej rutiny

**Súvisiace témy:**

[15.1. Speed](/docs/sk/pre_processor/15_movement_controls_definition/15_1_speed/)

[15.2. Force](/docs/sk/pre_processor/15_movement_controls_definition/15_2_force/)

[15.3. Hammer](/docs/sk/pre_processor/15_movement_controls_definition/15_3_hammer/)

[15.4. Screw press](/docs/sk/pre_processor/15_movement_controls_definition/15_4_screw_press/)

[15.5. Mechanical press](/docs/sk/pre_processor/15_movement_controls_definition/15_5_mechanical_press/)

[15.6. Hydraulic press](/docs/sk/pre_processor/15_movement_controls_definition/15_6_hydraulic_press/)

[15.7. Sliding Die](/docs/sk/pre_processor/15_movement_controls_definition/15_7_sliding_die/)

[15.8. Path](/docs/sk/pre_processor/15_movement_controls_definition/15_8_path/)

[15.9. Rotational Movement](/docs/sk/pre_processor/15_movement_controls_definition/15_9_rotational_movement/)

[15.10. Torsional movement](/docs/sk/pre_processor/15_movement_controls_definition/15_10_torsional_movement/)

[15.11. Friction Welding movement](/docs/sk/pre_processor/15_movement_controls_definition/15_11_friction_welding_movement/)

[Primary die selection from simulation controls](../9_simulation_controls/9_2_defining_step.htm#Primary_die_\(PDIE\))

[Step increment control (DSMAX/DTMAX)](../9_simulation_controls/9_2_defining_step.htm#Step_increment_control_\(DSMAX/DTMAX\)) [2D, 3D]

[Selecting time step and number of steps](../9_simulation_controls/9_2_defining_step.htm#Selecting_time_step_and_number_of_steps) [2D, 3D]

[Primary die stopping controls from simulation controls](../9_simulation_controls/9_3_stopping_controls.htm#9.3.2._Primary_Die_Displacement_\(SMAX\))

[Primary die selection from general object data definition window](../11_general_object_data_definition/11_general_object_data_definition.htm#11.5._Primary_Die)

[2D Geometry type selection from Simulation controls](../9_simulation_controls/9_1_simulation_type_settings.htm#9.1.2._Geometry_type_\(GEOTYP\)_\[2D\])

[14\. Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/)

[18\. Object Positioning](/docs/sk/pre_processor/19_object_positioning/19_object_positioning/)

[Movement-User Routine (USRDSP)](../../user_routines/56_user_routines_in_deform/56_2_2d_user_defined_fem_routines.htm#56_2_3_2_User_defined_movement_control_\(USRDSP\))

[2D Basic Labs](/docs/sk/labs/basic_labs/2d_labs/2d_labs/)

[3D Basic Labs](/docs/sk/labs/basic_labs/3d_labs/3d_labs/)

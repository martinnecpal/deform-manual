---
lang: sk
title: "16.4. Vlastnosti lomu"
---

# 16.4. Lomové vlastnosti

16.4.1. Zlomový krok (FRCSTP)

16.4.2. Lomové prvky (FRCNEL)

16.4.3. Odstránenie lomového prvku (FRCNEL)

16.4.4 Deaktivácia lomového prvku

  
V programe DEFORM možno modelovať tvárny lom deformujúceho sa obrobku. Ak je zapnutá funkcia lom, oddelenie materiálu sa bude modelovať pre všetky prvky, ktoré prekročia hodnotu kritického poškodenia zadanú na karte Vlastnosti materiálu ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})Rôzne![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})[Fracture]({{ '/docs/sk/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/' | relative_url }}). Táto funkcia je užitočná pri modelovaní strihania a zaslepovania, obrábania, lomov deformovateľných montážnych spojovacích prvkov (popnitov) a iných aplikácií.

**[2D]:****Vymazanie lomových prvkov** sa modeluje vymazaním všetkých prvkov, ktoré prekročia kritickú hodnotu poškodenia.

Preto by sa mala v každej oblasti, kde sa očakáva lom, použiť extrémne jemná sieť, aby sa obmedzila strata objemu. Simulácia MKP sa dočasne zastaví, aby sa vykonalo vymazanie prvkov. Zastavenie môže byť spustené danými krokmi lomu (pozri obr. 16.4.1.) alebo vždy, keď hodnota poškodenia v určenom počte prvkov prekročí kritickú hodnotu.

**Deaktivácia lomových prvkov** je nová metóda na štúdium šírenia trhlín. Tá deaktivuje prvok namiesto jeho vymazania, keď jeho poškodenie dosiahne kritickú hodnotu jeho materiálu (pozri obr. 16.4.2.).

**[3D]** : Ak chcete aktivovať typ vymazania lomových prvkov, používateľ musí vybrať typ **Vymazanie lomového prvku** z rozbaľovacieho poľa Lom ([FRCNEL]({{ '/docs/sk/keyword_documentation/f/frcnel/' | relative_url }})) (pozri obr. 16.4.1.) Tým sa iniciuje vymazanie prvkov, ktorých hodnota lomu je väčšia ako kritická hodnota definovaná v modeloch lomu/poškodenia materiálu počas postupov remeshingu. Model poškodenia a faktor kritického poškodenia definovaný v údajoch o materiáli sú dôležité údaje potrebné na aktiváciu tejto funkcie. Prehľad lomov nájdete v časti [3D Fracture.]({{ '/docs/sk/applications/55_applications/55_fracture/3d_fracture/' | relative_url }})

**Deaktivácia lomových prvkov** je nová metóda na štúdium šírenia trhlín. Tá deaktivuje prvok namiesto jeho vymazania, keď jeho poškodenie dosiahne kritickú hodnotu jeho materiálu (pozri obr. 16.4.2.).

![]({{ '/assets/images/pre-processor/16_object_properties/16_4_fracture_properties/16_4_image001.jpg' | relative_url }})

Typ odstránenia zlomového prvku

![]({{ '/assets/images/pre-processor/16_object_properties/16_4_fracture_properties/16_4_image002.jpg' | relative_url }})

Typ deaktivácie lomového prvku

## Zlomový krok ([FRCSTP]({{ '/docs/sk/keyword_documentation/f/frcstp/' | relative_url }})) [2D]

Krok (**[FRCSTP]({{ '/docs/sk/keyword_documentation/f/frcstp/' | relative_url }}))** interval, v ktorom sa má simulácia zastaviť, aby sa vykonalo vymazanie prvku. Ak žiadny prvok nie je nad kritickou hodnotou poškodenia, žiadny sa nevymaže.

## Odstránenie zlomových prvkov ([FRCNEL]({{ '/docs/sk/keyword_documentation/f/frcnel/' | relative_url }})) [2D]

Počet prvkov, ktoré musia byť nad kritickou hodnotou poškodenia, aby sa simulácia zastavila a vykonalo sa vymazanie prvkov. Typická hodnota je približne 4.

## Odstránenie zlomového prvku ([FRCNEL]({{ '/docs/sk/keyword_documentation/f/frcnel/' | relative_url }})) [3D]

Táto možnosť iniciuje odstránenie prvkov s hodnotou lomu vyššou ako kritická hodnota definovaná v modeloch lomu/poškodenia materiálu počas postupov remeshingu.

Vo všeobecnosti sa na štúdium šírenia trhlín v systéme DEFORM použije vymazanie lomových prvkov. Z dôvodu ťažkostí pri remeshovaní tehál vymazávanie lomových prvkov v súčasnosti nepodporuje 3D tehlovú sieť.

## Deaktivácia lomového prvku [2D, 3D]

Deaktivácia lomových prvkov je nová metóda na štúdium šírenia trhlín. Pri nej sa prvok deaktivuje namiesto vymazania, keď jeho poškodenie dosiahne kritickú hodnotu jeho materiálu. Umožňuje pokračovať v simulácii bez opätovného oddeľovania alebo s menším oddeľovaním pri procesoch tvárnenia. Deaktivácia lomových prvkov môže podporovať 3D tehlovú sieť, 3D štvorstennú sieť a 2D sieť na predpovedanie vzniku a šírenia trhlín.

**Súvisiace témy:**

[16\. Object properties]({{ '/docs/sk/pre_processor/16_object_properties/16_object_properties/' | relative_url }})

[16.1. Deformation properties]({{ '/docs/sk/pre_processor/16_object_properties/16_1_deformation_properties/' | relative_url }})

[16.2. Thermal properties]({{ '/docs/sk/pre_processor/16_object_properties/16_2_thermal_properties/' | relative_url }})

[16.3. Reference]({{ '/docs/sk/pre_processor/16_object_properties/16_3_Reference/' | relative_url }})

[16.5. Hardness Properties]({{ '/docs/sk/pre_processor/16_object_properties/16_5_hardness_properties/' | relative_url }})

[16.6. Heating Properties]({{ '/docs/sk/pre_processor/16_object_properties/16_6_heating_properties/' | relative_url }})

[16.7. Symmetry Properties]({{ '/docs/sk/pre_processor/16_object_properties/16_7_symmetry_properties/' | relative_url }})

[16.8. Body Force]({{ '/docs/sk/pre_processor/16_object_properties/16_8_body_force/' | relative_url }})

[16.9. RSE]({{ '/docs/sk/pre_processor/16_object_properties/16_9_rse/' | relative_url }})

[16.10. User]({{ '/docs/sk/pre_processor/16_object_properties/16_10_user/' | relative_url }})

[Material Fracture/damage models]({{ '/docs/sk/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/' | relative_url }})

[Applications - 3D Fracture]({{ '/docs/sk/applications/55_applications/55_fracture/3d_fracture/' | relative_url }})

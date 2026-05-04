---
lang: sk
title: "1.7. Reprezentácia geometrie"
---

# 1.7. Reprezentácia geometrie

![]({{ '/assets/images/about_deform/1_7_geometry_representation/1_7_image001.jpg' | relative_url }})

Príklady znázornenia geometrie: a) osovo súmerné b) krútenie c) rovinné napätie a rovinná deformácia

Simulácie DEFORM sa môžu vykonávať ako dvojrozmerné (2D) alebo trojrozmerné (3D) modely. Vo všeobecnosti sú 2D modely menšie, ľahšie sa nastavujú a spúšťajú sa rýchlejšie ako 3D modely. Často sa stáva, že pridané detaily 3D modelu nestojí za dodatočný čas potrebný oproti 2D simulácii, ak sa proces dá primerane reprezentovať v 2D.

Existujú štyri 2D-geometrické reprezentácie - osovo symetrická, rovinná deformácia, torzia a rovinné napätie. Osovo symetrické geometrie predpokladajú, že geometria každej roviny vyžarujúcej z osi je rovnaká. Rovinná deformácia a rovinné napätie predpokladajú, že v smere mimo roviny nedochádza k toku materiálu a že tok v každej rovine rovnobežnej s modelovaným rezom je identický. Torzné modely sú osovo symetrické modely charakterizujúce skrutku alebo skrutku. Na obr. 1.7.1 sú znázornené osovo súmerné, torzné, rovinné deformačné a rovinné napäťové modely.

Objekty, ktoré sú presne aproximované osovo symetrickými alebo rovinnými deformačnými modelmi, možno modelovať aj v 2D zanedbaním menších odchýlok. Ak napríklad tvar hlavy nie je kritický, skrutku so šesťhrannou hlavou možno modelovať ako osovo symetrickú definovaním polomeru hlavy, ktorý zachováva konštantný objem (polomer = 0,525*(vzdialenosť cez roviny)). Postupne sa zužujúcu časť, ako je napríklad lopatka turbíny, možno modelovať modelovaním niekoľkých rovinných deformačných úsekov.

![]({{ '/assets/images/about_deform/1_7_geometry_representation/1_7_image002.jpg' | relative_url }})

Vypínanie

Vzpínanie valcových súčiastok je plne trojrozmerný proces, a ak sa očakáva takéto správanie, musí sa modelovať ako taký. Osovo symetrická simulácia nezobrazí vybočenie, aj keď sa v skutočnom procese vyskytne (pozri obr. 1.7.2.). Časti, ktoré nemožno zjednodušiť na 2D, sa musia modelovať ako 3D.

**Súvisiace témy:**

[2D Geometry Types](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#9.1.2._Geometry_type_\(GEOTYP\)_\[2D\])

[2D Plane Strain](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#Plane_strain)

[2D Geo Edit Tool](/docs/sk/pre_processor/12_geometry_modelling/12_2_2d_geometry_editing/)

[3D Geo Tool Manual](/docs/sk/pre_processor/12_geometry_modelling/12_4_3d_geometry_data_editing_geo_tooll/)

[Lab 01 Geometry Manipulation](/docs/sk/labs/basic_labs/2d_labs/lab_01_geometry_manipulation_and_uniform_mesh/)

[Lab 02 Geometry Correction](/docs/sk/labs/basic_labs/2d_labs/lab_02_geometry_correction/)

---
lang: sk
title: "15.5. Mechanický lis"
---

# 15.5. Mechanický lis

15.5.1. Stláčanie kľuky
15.5.2. Kĺbový alebo klinový lis
15.5.3. Sekundárna(-é) kontrola(-y)
15.5.4. Elastické straty

## Stlačenie kľuky [2D, 3D]

Typ Mechanický lis kopíruje cyklický pohyb mechanického lisu. Parametrami potrebnými na simuláciu pohybu sú celkový posun lisu (![]({{ '/assets/equations/pre_processor/15_movement_controls/dtot.jpg' | relative_url }})) vzhľadom na aktuálny posun (![]({{ '/assets/equations/pre_processor/15_movement_controls/dcur.jpg' | relative_url }})) a počet zdvihov za jednotku času ( ![]({{ '/assets/equations/pre_processor/15_movement_controls/s_dash.jpg' | relative_url }})). Pomocou týchto parametrov môže DEFORM vypočítať rýchlosť lisu v ktoromkoľvek bode dráhy lisu. Smer pohybu je možné zadať len v smeroch X, Y, Z, -X, -Y alebo -Z. (Pozri obr. 15.5.1. a obr. 15.5.2.)

Rovnica na odvodenie rýchlosti matrice je:

![]({{ '/assets/equations/pre_processor/15_movement_controls/eq_15_5_1.jpg' | relative_url }}) |
---|---
  
![]({{ '/assets/images/pre-processor/15_movement_controls/15_5_mechanical_press/15_5_image001.jpg' | relative_url }})

2D Mechanický pohyb kľukového lisu ovláda okno

![]({{ '/assets/images/pre-processor/15_movement_controls/15_5_mechanical_press/15_5_image002.jpg' | relative_url }})

3D Mechanické ovládanie pohybu kľukového lisu

Parametre potrebné na špecifikáciu pohybu mechanického lisu sú:

**Celkový zdvih** : Celkový zdvih mechanického lisu predstavuje celkový pohyb matrice z jej hornej polohy do najnižšej polohy. Jednotkou v anglických jednotkách je palec a v jednotkách SI je mm.

**Údery za sekundu** : Údery za sekundu predstavujú frekvenciu úderov lisu. Ide o mieru úderov za sekundu alebo cyklov za sekundu.

**Kovanie ťahu** : Táto hodnota predstavuje celkovú zostávajúcu vzdialenosť zápustky v danom zdvihu. Táto hodnota bude závisieť od aktuálnej polohy pohyblivej zápustky vzhľadom na nepohyblivú zápustku.

**Smerovanie** : Smer sa používa na určenie smeru, v ktorom sa použije ťah objektu.

**Dĺžka spojovacej tyče** : Ako je vidieť na obr. 15.5.3, dĺžka ojnice môže mať vplyv na rýchlosť barana. Ak je dĺžka ojnice známa, možno ju zadať ako pole. Ak nie je známa, môže sa ponechať ako nula a jej príspevok k rýchlosti barana sa nebude brať do úvahy.

![]({{ '/assets/images/pre-processor/15_movement_controls/15_5_mechanical_press/15_5_image003.jpg' | relative_url }})

Náčrt jednoduchého priameho kľukového pohonu

## Stláčanie kĺbov alebo klinov [2D, 3D]

  
V prípade menej bežných lisov existuje možnosť modelovať ich pohyb ich striktným definovaním ako rýchlostný profil ( obr. 15.5.4 a obr. 15.5.5).  
Profil rýchlosti alebo **profil zdvihu** je definovaný ako uhol (v stupňoch) v závislosti od zdvihu alebo polohy matrice. Ako uhol súvisí s uhlom otáčania hnacieho motora.

Profil zdvihu musí byť kladný v hornom mŕtvom bode a nulový v dolnom mŕtvom bode.

**Kovací zdvih** je (kladná) vzdialenosť zostávajúca do BDC.

**Cykly/sekundy** predstavujú frekvenciu úderov lisu. Ide o mieru úderov za sekundu alebo cyklov za sekundu.

![]({{ '/assets/images/pre-processor/15_movement_controls/15_5_mechanical_press/15_5_image004.jpg' | relative_url }})

Ovládanie okna stlačením kĺbu

![]({{ '/assets/images/pre-processor/15_movement_controls/15_5_mechanical_press/15_5_image005.jpg' | relative_url }})

Profil zdvihu kĺbového lisu

**Príklad mechanického lisu:**

Uvažujte príklad, keď je celkový posun pre lis (od horného mŕtveho stredu po dolný mŕtvy stred) 10 palcov.

  * Prvou informáciou, ktorú treba určiť, je smer pohybu pohyblivej kocky. V tomto prípade uvažujme, že pohybujúca sa kocka sa pohybuje v smere Y. Môžeme teda nastaviť smer pohybu na Y.

  * Druhou informáciou sú parametre lisu: rýchlosť a výtlak. Tie sú pre lis spravidla pevne stanovené a po ich určení ich možno uložiť do knižnice lisu. V tomto prípade predpokladajme, že tieto hodnoty sú 10 palcov posunu a rýchlosť 1 cyklus za sekundu (1 sekunda na prejdenie z TDC do BDC a späť).

  * Poslednou informáciou, ktorú je potrebné poskytnúť, je aktuálna poloha pohyblivej matrice na začiatku zdvihu. To možno vykonať pomocou meracieho nástroja na určenie vzdialenosti v smere Y pohyblivého nástroja od BDC kľuky. Je veľmi dôležité, aby sa toto meranie vykonalo starostlivo, pretože ovplyvní konečnú výšku dielu a bude mať vplyv na konečné zaťaženie procesu. V tomto prípade, ak pohyblivý nástroj začína na 9 palcoch do zdvihu, počiatočná poloha bude nastavenie aktuálneho zdvihu nástroja na (0, -9). To znamená, že pohyblivá matrica sa už posunula o 9 palcov smerom nadol a musí prejsť ďalší 1 palec smerom nadol, čo nie je nič iné ako kovací zdvih.

## Sekundárna kontrola(-y)

Typ ovládania závisí od typu zadaného pohybu. V prípade mechanického lisu a skrutkového lisu (ako je vidieť na obr. 15.5.6. a obr. 15.5.7.) je jediná regulácia založená na zaťažení. V prípade kladiva neexistuje žiadne sekundárne ovládanie, pretože jediný spôsob, ako zastaviť, je vyčerpanie energie. V prípade hydraulického lisu sa môže zastaviť na základe zaťaženia alebo minimálnej rýchlosti.

![]({{ '/assets/images/pre-processor/15_movement_controls/15_5_mechanical_press/15_5_image006.jpg' | relative_url }})

2D Sekundárne ovládacie prvky pre pohyb objektu

![]({{ '/assets/images/pre-processor/15_movement_controls/15_5_mechanical_press/15_5_image007.jpg' | relative_url }})

3D Sekundárne ovládacie prvky pre pohyb objektu

## Elastické straty

V tomto dialógovom okne môžete definovať tuhosť lisu alebo kladiva. (Pozri obr. 15.5.8.) V prípade lisu môže dôjsť k roztiahnutiu na základe zaťaženia kovania a konečná vzdialenosť lisu bude menšia o veľkosť roztiahnutia. V prípade kladiva poddajnosť zohľadňuje elastickú stratu energie.

![]({{ '/assets/images/pre-processor/15_movement_controls/15_5_mechanical_press/15_5_image008.jpg' | relative_url }})

Definícia tuhosti/poddajnosti pre lis alebo kladivo

**Súvisiace témy:**

[15\. Movement Controls Settings](/docs/sk/pre_processor/15_movement_controls_definition/15_movement_controls_settings/)

[15.1. Speed](/docs/sk/pre_processor/15_movement_controls_definition/15_1_speed/)

[15.2. Force](/docs/sk/pre_processor/15_movement_controls_definition/15_2_force/)

[15.3. Hammer](/docs/sk/pre_processor/15_movement_controls_definition/15_3_hammer/)

[15.4. Screw press](/docs/sk/pre_processor/15_movement_controls_definition/15_4_screw_press/)

[15.6. Hydraulic press](/docs/sk/pre_processor/15_movement_controls_definition/15_6_hydraulic_press/)

[15.7. Sliding Die](/docs/sk/pre_processor/15_movement_controls_definition/15_7_sliding_die/)

[15.8. Path](/docs/sk/pre_processor/15_movement_controls_definition/15_8_path/)

[15.9. Rotational Movement](/docs/sk/pre_processor/15_movement_controls_definition/15_9_rotational_movement/)

[15.10. Torsional movement](/docs/sk/pre_processor/15_movement_controls_definition/15_10_torsional_movement/)

[15.11. Friction Welding movement](/docs/sk/pre_processor/15_movement_controls_definition/15_11_friction_welding_movement/)

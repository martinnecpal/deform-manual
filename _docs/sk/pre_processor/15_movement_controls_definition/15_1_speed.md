---
lang: sk
title: "15.1. Rýchlosť"
---

# 15.1. Rýchlosť

**[2D, 3D]:** Toto je predvolené ovládanie pohybu (pozri obr. 15.1.1 a obr. 15.1.2), ktoré určuje rýchlosť a smer pohybu objektu. Rýchlosť môže byť definovaná jedným z nasledujúcich spôsobov.

  * Konštanta

  * Funkcia zdvihu primárneho objektu

  * Funkcia času

  * Funkcia sily (zaťaženia) na objekt

  * Úmerná rýchlosti iného objektu

  * Sínusová funkcia

Ak je objekt tuhý, celý objekt sa bude pohybovať priradenou rýchlosťou. Keď je objekt pružný, plastický alebo pórovitý, každý uzol s priradenou okrajovou podmienkou pohybu bude udržiavať priradenú rýchlosť. Všimnite si, že okrajové podmienky pohybu by nikdy nemali byť priradené pre všetky uzly povrchu. Vo všeobecnosti platí, že nie viac ako 1/2 až 2/3 okrajových uzlov na objekte by mali mať pridelené okrajové podmienky pohybu.

Roviny symetrie sú definované s okrajovými podmienkami V=0 kolmo na aplikovaný povrch. Kvôli obmedzeniam pri extrakcii hraníc počas remeshingu by sa mali definovať rovnobežné roviny symetrie pomocou aspoň jednej tuhej plochy symetrie namiesto okrajových podmienok V=0 na oboch stranách objektu.

Pole Aktuálna sila je pridané pre všetky typy pohybu a používateľ môže sledovať aktuálnu silu v rôznych krokoch.

![]({{ '/assets/images/pre-processor/15_movement_controls/15_1_speed/15_1_image001.jpg' | relative_url }})

2D okno kontroly pohybu rýchlosti

![]({{ '/assets/images/pre-processor/15_movement_controls/15_1_speed/15_1_image002.jpg' | relative_url }})

Okno 3D Speed movement contros

Súvisiace témy:

[15\. Movement Controls Settings](/docs/sk/pre_processor/15_movement_controls_definition/15_movement_controls_settings/)

[15.2. Force](/docs/sk/pre_processor/15_movement_controls_definition/15_2_force/)

[15.3. Hammer](/docs/sk/pre_processor/15_movement_controls_definition/15_3_hammer/)

[15.4. Screw press](/docs/sk/pre_processor/15_movement_controls_definition/15_4_screw_press/)

[15.5. Mechanical press](/docs/sk/pre_processor/15_movement_controls_definition/15_5_mechanical_press/)

[15.6. Hydraulic press](/docs/sk/pre_processor/15_movement_controls_definition/15_6_hydraulic_press/)

[15.7. Sliding Die](/docs/sk/pre_processor/15_movement_controls_definition/15_7_sliding_die/)

[15.8. Path](/docs/sk/pre_processor/15_movement_controls_definition/15_8_path/)

[15.9. Rotational Movement](/docs/sk/pre_processor/15_movement_controls_definition/15_9_rotational_movement/)

[15.10. Torsional movement](/docs/sk/pre_processor/15_movement_controls_definition/15_10_torsional_movement/)

[15.11. Friction Welding movement](/docs/sk/pre_processor/15_movement_controls_definition/15_11_friction_welding_movement/).

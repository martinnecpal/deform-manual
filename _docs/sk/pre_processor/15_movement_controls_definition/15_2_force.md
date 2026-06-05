---
lang: sk
title: "15.2. Sila"
---

# 15.2. Force

**[2D, 3D]** : Pri riadení sily (záťaže) (pozri obr. 15.2.1 a obr. 15.2.2) sa rýchlosť objektu obmedzuje tak, aby sa udržiavalo určené zaťaženie objektu. Sila môže byť definovaná jedným z nasledujúcich spôsobov.

  * Konštanta

  * Funkcia zdvihu primárneho objektu

  * Funkcia času

Ak je objekt tuhý, zaťaženie je výsledné zaťaženie pôsobiace na všetky netuhé objekty, ktoré sa ho dotýkajú. Ak je objekt pružný, plastický alebo pórovitý, zaťaženie je súčtom uzlových zaťažení všetkých uzlov s definovanými kódmi okrajových podmienok pohybu. Táto okrajová podmienka pridáva stupeň voľnosti do sústavy rovníc, ktoré sa majú riešiť počas simulácie. Ľubovoľné použitie tejto podmienky môže spôsobiť ťažkosti pri získavaní konvergentného riešenia.

![]({{ '/assets/images/pre-processor/15_movement_controls/15_2_force/15_2_image001.jpg' | relative_url }})

2D okno ovládania pohybu sily

![]({{ '/assets/images/pre-processor/15_movement_controls/15_2_force/15_2_image002.jpg' | relative_url }})

3D okno ovládania pohybu sily

**Súvisiace témy:**

[15\. Movement Controls Settings](/docs/sk/pre_processor/15_movement_controls_definition/15_movement_controls_settings/)

[15.1. Speed](/docs/sk/pre_processor/15_movement_controls_definition/15_1_speed/)

[15.3. Hammer](/docs/sk/pre_processor/15_movement_controls_definition/15_3_hammer/)

[15.4. Screw press](/docs/sk/pre_processor/15_movement_controls_definition/15_4_screw_press/)

[15.5. Mechanical press](/docs/sk/pre_processor/15_movement_controls_definition/15_5_mechanical_press/)

[15.6. Hydraulic press](/docs/sk/pre_processor/15_movement_controls_definition/15_6_hydraulic_press/)

[15.7. Sliding Die](/docs/sk/pre_processor/15_movement_controls_definition/15_7_sliding_die/)

[15.8. Path](/docs/sk/pre_processor/15_movement_controls_definition/15_8_path/)

[15.9. Rotational Movement](/docs/sk/pre_processor/15_movement_controls_definition/15_9_rotational_movement/)

[15.10. Torsional movement](/docs/sk/pre_processor/15_movement_controls_definition/15_10_torsional_movement/)

[15.11. Friction Welding movement](/docs/sk/pre_processor/15_movement_controls_definition/15_11_friction_welding_movement/).

---
lang: sk
title: "15.7. Posuvná matrica"
---

# 15.7. Posuvná matrica

[2D, 3D]: Definovanie posuvného pohybu je možné vykonať v okne ovládania pohybu, ako je vidieť na obr. 15.7.1 a obr. 15.7.2. Ak chcete použiť pružinové matrice, objekt by mal byť tuhý a nemal by mať zadaný žiadny iný pohyb.

Pre všetky pružinové zápustky by sa mali špecifikovať tieto položky:

  * Otočte ovládacie prvky pružinového lisu do polohy ON.

  * Smer pohybu by mal byť zadaný v smere, ktorý stláča pružinu. Sila pružiny bude pôsobiť proti smeru pohybu.

  * **Tuhosť** udáva tuhosť v jednotkách klb/in (anglicky) alebo N/mm (SI). Tuhosť môže byť buď konštantná, alebo funkcia veľkosti stlačenia.

  * **Predpätie** udáva veľkosť sily, ktorú je potrebné prekonať pred stlačením, v klb (anglicky) alebo N (SI).
  * **Maximálny posun** je vzdialenosť, v ktorej sa pružina nakoniec dostane na dno a ktorá spôsobí, že sa pružina už nebude pohybovať v smere stlačenia.
  * **Druhý koniec pružiny** určuje, či je pružina pripevnená k inému pevnému predmetu alebo či je druhý koniec pripevnený k polohe v priestore. V prípade, že je objekt pevne spojený s polohou v priestore, smer stlačenia, aktuálny posun a maximálny posun určujú, ako veľmi je pružina stlačená a či je na dne. V prípade, že je pružina pripevnená k inému objektu, vzdialenosť medzi týmito dvoma objektmi určuje veľkosť stlačenia.
  * **Číslo krokov pred tlmením** : **Text, ktorý sa má doplniť**

![]({{ '/assets/images/pre-processor/15_movement_controls/15_7_sliding_die/15_7_image001.jpg' | relative_url }})

2D Posuvné okno na ovládanie pohybu kocky

![]({{ '/assets/images/pre-processor/15_movement_controls/15_7_sliding_die/15_7_image002.jpg' | relative_url }})

3D Posuvné okno na ovládanie pohybu kocky

**Súvisiace témy:**

[15\. Movement Controls Settings](/docs/sk/pre_processor/15_movement_controls_definition/15_movement_controls_settings/)

[15.1. Speed](/docs/sk/pre_processor/15_movement_controls_definition/15_1_speed/)

[15.2. Force](/docs/sk/pre_processor/15_movement_controls_definition/15_2_force/)

[15.3. Hammer](/docs/sk/pre_processor/15_movement_controls_definition/15_3_hammer/)

[15.4. Screw press](/docs/sk/pre_processor/15_movement_controls_definition/15_4_screw_press/)

[15.5. Mechanical press](/docs/sk/pre_processor/15_movement_controls_definition/15_5_mechanical_press/)

[15.6. Hydraulic press](/docs/sk/pre_processor/15_movement_controls_definition/15_6_hydraulic_press/)

[15.8. Path](/docs/sk/pre_processor/15_movement_controls_definition/15_8_path/)

[15.9. Rotational Movement](/docs/sk/pre_processor/15_movement_controls_definition/15_9_rotational_movement/)

[15.10. Torsional movement](/docs/sk/pre_processor/15_movement_controls_definition/15_10_torsional_movement/)

[15.11. Friction Welding movement](/docs/sk/pre_processor/15_movement_controls_definition/15_11_friction_welding_movement/)

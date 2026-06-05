---
lang: sk
title: "15.9. Rotačný pohyb"
---

# 15.9. Rotačný pohyb

15.9.1. Krútiaci moment

15.9.2. Uhlová rýchlosť

  
**[2D, 3D]** : Rotačný pohyb je definovaný uhlovou rýchlosťou okolo pevného stredu otáčania. Tento typ pohybu spôsobuje iba rotáciu. Ak nie je uvedené inak, translácia je obmedzená. Rotačná rýchlosť sa riadi prostredníctvom možnosti Controlling Method (Spôsob riadenia) a bod, okolo ktorého sa objekt otáča, sa nastavuje prostredníctvom možnosti Center of Rotational Movement (Stred rotačného pohybu). Nastavenia rotačného pohybu 2d a 3d modelu nájdete na obr. 15.9.1., obr. 15.9.2. a obr. 15.9.3.

![]({{ '/assets/images/pre-processor/15_movement_controls/15_9_rotational_movement/15_9_image001.jpg' | relative_url }})

Nastavenia okna ovládania pohybu otáčania pre 2D Torque

![]({{ '/assets/images/pre-processor/15_movement_controls/15_9_rotational_movement/15_9_image002.jpg' | relative_url }})

Ovládacie prvky pohybu otáčania Nastavenia okna pre 2D uhlovú rýchlosť

![]({{ '/assets/images/pre-processor/15_movement_controls/15_9_rotational_movement/15_9_image003.jpg' | relative_url }})

Nastavenia okna pre ovládanie rotačného pohybu pre 3D krútiaci moment a uhlovú rýchlosť

Rotačný pohyb možno použiť na simuláciu valenia alebo akéhokoľvek typu pohybu, pri ktorom sa objekt otáča okolo pevnej osi. Rotational Motion možno použiť len na tuhé objekty. Rigidné objekty môžu mať súčasne pohyb [Rotational](15_movement_controls_settings.htm#15.1.2._Rotational_movement) aj [Translational](15_movement_controls_settings.htm#15.1.1._Translation_movement).

**Kontrolná metóda**

Otáčanie objektov možno ovládať uhlovou rýchlosťou alebo krútiacim momentom. Vyberte požadované ovládanie a zadajte hodnotu pre otáčanie hneď pod ním.

## **Torque**

Typ pohybu Torque vykoná rotačný pohyb okolo definovanej osi so zadaným krútiacim momentom. Krútiaci moment môže byť zadaný ako konštanta alebo ako funkcia času alebo uhla.

## **Angulárna rýchlosť**

Uhlová rýchlosť použije rotačný pohyb okolo definovanej osi pri zadanej uhlovej rýchlosti v radiánoch za sekundu. Uhlová rýchlosť môže byť zadaná ako konštanta alebo ako funkcia času alebo uhla. Spolu s údajmi o osi sú k dispozícii možnosti na výpočet stredu a osi z geometrie.

Poznámka:

Voľnobežné valce možno definovať zadaním riadenia krútiaceho momentu s veľmi nízkou hodnotou krútiaceho momentu.

**Osa otáčania** : je určená vektorom vychádzajúcim zo stredu bodu a prechádzajúcim smerom bodu. Smer rotácie je definovaný pravidlom pravej ruky. To znamená, že kladná rotácia je v smere hodinových ručičiek pri pohľade zo stredu bodu smerom k bodu smeru.

**Aktuálny uhol** : aktuálna poloha objektu.

**Súvisiace témy:**

[15\. Movement Controls Settings](/docs/sk/pre_processor/15_movement_controls_definition/15_movement_controls_settings/)

[15.1. Speed](/docs/sk/pre_processor/15_movement_controls_definition/15_1_speed/)

[15.2. Force](/docs/sk/pre_processor/15_movement_controls_definition/15_2_force/)

[15.3. Hammer](/docs/sk/pre_processor/15_movement_controls_definition/15_3_hammer/)

[15.4. Screw press](/docs/sk/pre_processor/15_movement_controls_definition/15_4_screw_press/)

[15.5. Mechanical press](/docs/sk/pre_processor/15_movement_controls_definition/15_5_mechanical_press/)

[15.6. Hydraulic press](/docs/sk/pre_processor/15_movement_controls_definition/15_6_hydraulic_press/)

[15.7. Sliding Die](/docs/sk/pre_processor/15_movement_controls_definition/15_7_sliding_die/)

[15.8. Path](/docs/sk/pre_processor/15_movement_controls_definition/15_8_path/)

[15.10. Torsional movement](/docs/sk/pre_processor/15_movement_controls_definition/15_10_torsional_movement/)

[15.11. Friction Welding movement](/docs/sk/pre_processor/15_movement_controls_definition/15_11_friction_welding_movement/)

[Appendix XIV: Rotating Workpiece Simulations](/docs/sk/appendices/appendix_xiv_rotating_workpiece_simulations/)

[3D Orbital Movement](/docs/sk/applications/55_applications/55_orbital_movement/3d_orbital_movement/)

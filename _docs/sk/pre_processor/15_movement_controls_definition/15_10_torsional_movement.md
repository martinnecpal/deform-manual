---
lang: sk
title: "15.10. Krútiaci pohyb"
---

# 15.10. Krútiaci pohyb

15.10.1. Uhlová rýchlosť

15.10.2. Energia

**[2D]** : Kontroly krútiaceho pohybu sa uplatňujú len v prípade krútiacich sa formulácií. Táto možnosť riadenia pohybu je aktívna len pre DEFORM-2D. Nastavenia týchto pohybov nájdete na obr. 15.10.1 a obr. 15.10.2.

![]({{ '/assets/images/pre-processor/15_movement_controls/15_10_torsional_movement/15_10_image001.jpg' | relative_url }})

Nastavenia okna pre uhlovú rýchlosť torzného pohybu

![]({{ '/assets/images/pre-processor/15_movement_controls/15_10_torsional_movement/15_10_image002.jpg' | relative_url }})

Torzný pohyb ovláda nastavenia okien pre Energy

**Kontrolná metóda**
Torziu objektov možno ovládať uhlovou rýchlosťou alebo energiou. Vyberte požadované ovládanie a zadajte hodnoty.

## Uhlová rýchlosť

Angular Velocity (Uhlová rýchlosť) použije torzný pohyb okolo definovanej osi so zadanou uhlovou rýchlosťou v radiánoch za sekundu. Uhlová rýchlosť môže byť zadaná ako konštanta alebo ako funkcia času alebo uhla. (Pozri obr. 15.10.1.)

Poznámka:

Voľnobežné valce možno definovať zadaním riadenia krútiaceho momentu s veľmi nízkou hodnotou krútiaceho momentu.

## Energia

Krútiaci pohyb je založený na hodnotách energie, momentu zotrvačnosti a účinnosti, ako je znázornené na obr. 15.10.2.

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

[15.9. Rotational Movement](/docs/sk/pre_processor/15_movement_controls_definition/15_9_rotational_movement/)

[15.11. Friction Welding movement](/docs/sk/pre_processor/15_movement_controls_definition/15_11_friction_welding_movement/)

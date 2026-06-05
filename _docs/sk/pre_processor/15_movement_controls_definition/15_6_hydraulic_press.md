---
lang: sk
title: "15.6. Hydraulický lis"
---

# 15.6. Hydraulický lis

15.6.1. Rýchlosť
15.6.2. Priemerná miera deformácie
15.6.3. Ovládacie prvky Dwell
15.6.4. Elastické straty

**[2D, 3D]:** Používanie modelu hydraulického lisu môže používateľ ovládať jedným z dvoch spôsobov.

## Rýchlosť [2D, 3D]

Rýchlosť lisu možno definovať jedným z nasledujúcich spôsobov (pozri obr. 15.6.1 a obr. 15.6.2).

  * Konštanta

  * Funkcia času

  * Funkcia zdvihu primárneho objektu

Ako funkciu zaťaženia možno zadať aj krivku medzného výkonu charakterizujúcu hydraulický lis. Pozri príklad [2D Basic lab 10 Hydraulic press.](/docs/sk/labs/basic_labs/2d_labs/lab_10_hydraulic_press/)

Poznámka:

Ak chcete aktivovať reguláciu maximálnych otáčok, je potrebné definovať limit výkonu.

![]({{ '/assets/images/pre-processor/15_movement_controls/15_6_hydraulic_press/15_6_image001.jpg' | relative_url }})

2D Nastavenia ovládania rýchlosti pohybu hydraulického lisu

![]({{ '/assets/images/pre-processor/15_movement_controls/15_6_hydraulic_press/15_6_image002.jpg' | relative_url }})

3D Hydraulické nastavenie ovládania rýchlosti pohybu lisu

## Priemerná miera deformácie [2D, 3D]

  
Regulácia priemernej rýchlosti deformácie sa môže použiť aj na definovanie rýchlosti lisovania (pozri obr. 15.6.3.). Všimnite si, že je potrebné zadať počiatočnú výšku polotovaru a malo by ísť o pomerne presné meranie.

**Povolená maximálna miera deformácie** : Toto nastavenie je možné definovať ako doplnok k vyššie uvedeným ovládacím prvkom. Tým sa zabráni prekročeniu rýchlosti v stave, keď by maximálna miera deformácie v diele prekročila definovanú maximálnu mieru deformácie.

![]({{ '/assets/images/pre-processor/15_movement_controls/15_6_hydraulic_press/15_6_image003.jpg' | relative_url }})

Hydraulický lis Nastavenie kontroly priemernej rýchlosti pohybu

## Ovládacie prvky Dwell [2D, 3D]

V hydraulickom lise môžeme simuláciu zastaviť na základe zaťaženia alebo kritéria zastavenia minimálnej rýchlosti. V hydraulickom lise môžeme definovať aj čas zastavenia, keď sa dosiahne kritérium zastavenia Výpočet sa spustí až do definovaného celkového času zastavenia. Možnosti ovládania Dwell sú znázornené na obr. 15.6. 4.

![]({{ '/assets/images/pre-processor/15_movement_controls/15_6_hydraulic_press/15_6_image004.jpg' | relative_url }})

Hydraulické ovládacie prvky pre zdržanie lisu

## Elastické straty

V tomto dialógovom okne možno definovať tuhosť lisu alebo kladiva. V prípade lisu môže dôjsť k roztiahnutiu na základe zaťaženia kovania a konečná vzdialenosť lisu bude menšia o veľkosť roztiahnutia. V prípade kladiva poddajnosť zohľadňuje pružnú stratu energie.

**Súvisiace témy:**

[15\. Movement Controls Settings](/docs/sk/pre_processor/15_movement_controls_definition/15_movement_controls_settings/)

[15.1. Speed](/docs/sk/pre_processor/15_movement_controls_definition/15_1_speed/)

[15.2. Force](/docs/sk/pre_processor/15_movement_controls_definition/15_2_force/)

[15.3. Hammer](/docs/sk/pre_processor/15_movement_controls_definition/15_3_hammer/)

[15.4. Screw press](/docs/sk/pre_processor/15_movement_controls_definition/15_4_screw_press/)

[15.5. Mechanical press](/docs/sk/pre_processor/15_movement_controls_definition/15_5_mechanical_press/)

[15.7. Sliding Die](/docs/sk/pre_processor/15_movement_controls_definition/15_7_sliding_die/)

[15.8. Path](/docs/sk/pre_processor/15_movement_controls_definition/15_8_path/)

[15.9. Rotational Movement](/docs/sk/pre_processor/15_movement_controls_definition/15_9_rotational_movement/)

[15.10. Torsional movement](/docs/sk/pre_processor/15_movement_controls_definition/15_10_torsional_movement/)

[15.11. Friction Welding movement](/docs/sk/pre_processor/15_movement_controls_definition/15_11_friction_welding_movement/)

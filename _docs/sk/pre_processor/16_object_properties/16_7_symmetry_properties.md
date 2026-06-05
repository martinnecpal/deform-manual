---
lang: sk
title: "16.7. Vlastnosti symetrie"
---

# 16.7. Vlastnosti symetrie

**[3D]** : Táto okrajová podmienka umožňuje používateľovi prispôsobiť rýchlosť uzlov ľubovoľného povrchu telesa uzlom ľubovoľného iného povrchu toho istého telesa. Účelom je modelovať všeobecnejší prípad, keď počas tvárnenia súčiastky dochádza k rotačnému pohybu, ako napríklad v prípade kovania šikmého ozubeného kolesa. Spôsob, akým sa nastavuje problém rotačnej symetrie, je prejsť do okna Objekt, Vlastnosti objektu a vybrať záložku Symetria a potom nastaviť nasledujúce hodnoty: (Pozri obr. 16.7.1.).

  * **Úhol** : Uhol simulovanej časti v jednotkách stupňov. Napríklad 180 znamená, že sa simuluje len polovica časti a 90 znamená, že sa simuluje štvrtina časti.
  * **Centrum** : Bod na osi, okolo ktorého dochádza k deformácii. Formát je v globálnych súradniciach (x, y, z).
  * **Os** : Vektor, s ktorým je os rovnobežná. Formát je v súradniciach (x, y, z). Ak chce napríklad používateľ zadať vektor rovnobežný s osou z, treba zadať hodnotu (0, 0, 1).

Druhou položkou, ktorú musí používateľ zadať, sú plochy, ktoré majú navzájom vzťah rotačnej symetrie. Spôsob, akým sa to robí, je umiestnenie kontaktných okrajových podmienok na plochu, ktorá sa riadi pravidlom pravej ruky. Okrajovú podmienku možno aplikovať v okne Objekty, okrajové podmienky pomocou rozšírených okrajových podmienok. Používateľ musí vybrať plochu, ktorá sa riadi pravidlom pravej ruky, a aplikovať na ňu podmienky vlastného kontaktu. To umožní simulačnému motoru zistiť, na ktoré plochy sa vzťahuje podmienka rotačnej symetrie.

![](../../../assets/Images/Pre-Processor/16_Object_Properties/16_7_Symmetry_Properties/16_7_Image001.jpg)

Okno vlastností objektu rotačnej symetrie

**Súvisiace témy:**

[16\. Object properties](/docs/sk/pre_processor/16_object_properties/16_object_properties/)

[16.1. Deformation properties](/docs/sk/pre_processor/16_object_properties/16_1_deformation_properties/)

[16.2. Thermal properties](/docs/sk/pre_processor/16_object_properties/16_2_thermal_properties/)

[16.3. Reference](/docs/sk/pre_processor/16_object_properties/16_3_Reference/)

[16.4. Fracture Properties](/docs/sk/pre_processor/16_object_properties/16_4_Fracture_properties/)

[16.5. Hardness Properties](/docs/sk/pre_processor/16_object_properties/16_5_hardness_properties/)

[16.6. Heating Properties](/docs/sk/pre_processor/16_object_properties/16_6_heating_properties/)

[16.8. Body Force](/docs/sk/pre_processor/16_object_properties/16_8_body_force/)

[16.9. RSE](/docs/sk/pre_processor/16_object_properties/16_9_rse/)

[16.10. User](/docs/sk/pre_processor/16_object_properties/16_10_user/)

[3D-Geometry symmetry surface definition](../12_Geometry_Modelling/12_3_3d_geometry_data_defining.htm#Parallel_symmetry_planes)

[3D-Mesh symmetry BCC definition](/docs/sk/pre_processor/14_Boundary_Conditions/14_1_symmetry_boundary_conditions/)

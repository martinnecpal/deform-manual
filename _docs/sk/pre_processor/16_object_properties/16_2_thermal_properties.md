---
lang: sk
title: "16.2. Tepelné vlastnosti"
---

# 16.2. Tepelné vlastnosti

16.2.1. Referenčná teplota (REFTMP)

16.2.2. Teplota skrátenia (TMPLMT)

16.2.3. Teplota zastavenia (OTPRNG)

![](../../../assets/Images/Pre-Processor/16_Object_Properties/16_2_Thermal_properties/16_2_Image001.jpg)

2D okno vlastností tepelného objektu

![](../../../assets/Images/Pre-Processor/16_Object_Properties/16_2_Thermal_properties/16_2_Image002.jpg)

Okno vlastností 3D tepelného objektu

## Referenčná teplota (REFTMP) [2D, 3D]

  
V prípade pružných objektov je referenčná teplota ([REFTMP)](/docs/sk/Keyword_Documentation/R/REFTMP/) teplota, na ktorej sú založené výpočty tepelnej rozťažnosti. Tepelné deformácie sú dané: (Pozri obr. 16.2.1. a obr. 16.2.2.)

![](../../../assets/Equations/Pre_Processor/16_Object_Properties/EQ_16_2_1.jpg) |
---|---
  
Pre elasto-plastické objekty sa používa okamžitý koeficient tepelnej rozťažnosti.

Koeficient tepelnej rozťažnosti sa nastavuje v ponuke Material Properties Elastic, pozri tiež časť [10.2.4. Material Reference temperature](../10_Material_Data/10_2_Elastic_Data/10_2_Elastic_Data.htm#Material_Reference_Temperature) pre rozdiel medzi referenčnými teplotami materiálu a objektu.

## Teplota skrátenia (TMPLMT) [2D, 3D]

Teplota skrátenia ([TMPLMT](/docs/sk/Keyword_Documentation/T/TMPLMT/)) je maximálna prípustná teplota uzla v ktoromkoľvek bode objektu. Ak vypočítaná teplota prekročí túto hodnotu, zníži sa na túto hodnotu.

## Teplota zastavenia (OTPRNG) [2D, 3D]

Teplota zastavenia ([OTPRNG](/docs/sk/Keyword_Documentation/O/OTPRNG/)) nastavuje horný a dolný teplotný limit, ktorého prekročenie zastaví simuláciu. Používateľ má možnosť vynútiť tento limit, ak niektorý jednotlivý uzol prekročí teplotu, len ak všetky uzly prekročia teplotu alebo na základe teploty v konkrétnom uzle. Ďalšie informácie týkajúce sa možnosti zastavenia rozsahu teploty nájdete v časti [9.3.10. Temperature stopping control](../9_Simulation_Controls/9_3_Stopping_Controls.htm#9.3.10._Temperature_stopping_control)

**Súvisiace témy:**

[16\. Object properties](/docs/sk/pre_processor/16_object_properties/16_object_properties/)

[16.1. Deformation properties](/docs/sk/pre_processor/16_object_properties/16_1_deformation_properties/)

[16.3. Reference](/docs/sk/pre_processor/16_object_properties/16_3_Reference/)

[16.4. Fracture Properties](/docs/sk/pre_processor/16_object_properties/16_4_Fracture_properties/)

[16.5. Hardness Properties](/docs/sk/pre_processor/16_object_properties/16_5_hardness_properties/)

[16.6. Heating Properties](/docs/sk/pre_processor/16_object_properties/16_6_heating_properties/)

[16.7. Symmetry Properties](/docs/sk/pre_processor/16_object_properties/16_7_symmetry_properties/)

[16.8. Body Force](/docs/sk/pre_processor/16_object_properties/16_8_body_force/)

[16.9. RSE](/docs/sk/pre_processor/16_object_properties/16_9_rse/)

[16.10. User](/docs/sk/pre_processor/16_object_properties/16_10_user/)

[Difference b/w material and object reference temperature](../10_Material_Data/10_2_Elastic_Data/10_2_Elastic_Data.htm#Material_Reference_Temperature)

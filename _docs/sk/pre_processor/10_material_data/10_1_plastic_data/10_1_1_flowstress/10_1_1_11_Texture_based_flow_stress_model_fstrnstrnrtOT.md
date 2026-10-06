---
lang: sk
title: "10.1.1.11. Model napätia pri prúdení založený na textúre f(strn,strnrt,O,T)"
---

# 10.1.1.11. Model napätia pri prúdení založený na textúre f(strn,strnrt,O,T)

Veľkosť napätia pri prúdení môže byť silne závislá od mikroštruktúry materiálu. Tento model prietokového napätia možno použiť na zohľadnenie vplyvu kryštalografickej orientácie na prietokové napätie. Tento typ prúdového napätia by sa mal používať len pre tuhé plastické objekty.

  
Pred definovaním tohto modelu prietokového napätia musí používateľ definovať základné informácie o textúre na karte textúry, ako je znázornené na nasledujúcom obr. 10.1.1.11.1. Definícia modelu textúry zahŕňa definovanie typu kryštálu (kryštálová štruktúra), typu textúry (Rodriguesove alebo Eulerove uhly) a typu siete textúry. Typ textúry Eulerových uhlov zatiaľ nebol implementovaný.

  
![]({{ '/assets/images/pre-processor/10_material_data/10_1_plastic_data/10_1_1_flow_stress/10_1_1_11_texture_based_f%28strn%2Cstrnrt%2Co%2Ct%29/10_1_1_11_image001.jpg' | relative_url }})

Definícia modelu textúry

  
Po definovaní informácií o textúre musí používateľ vybrať model prietokového napätia kryštalografickej orientácie a definovať prietokové napätie pre každú Rodriguesovu orientáciu, ktoré je založené na vybranom type textúrnej siete ako funkcia deformácie, rýchlosti deformácie a teploty ( obr. 10.1.1.11.2.).

![]({{ '/assets/images/pre-processor/10_material_data/10_1_plastic_data/10_1_1_flow_stress/10_1_1_11_texture_based_f%28strn%2Cstrnrt%2Co%2Ct%29/10_1_1_11_image002.jpg' | relative_url }})

Kryštalografická orientácia na základe okna prietokového napätia

[10.1.1.1. Tabular data format]({{ '/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_1_Tabular_data_format/' | relative_url }})
[10.1.1.2. Power Law]({{ '/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_2_Power_Law/' | relative_url }})
[10.1.1.3. Flow stress for aluminum alloys (Type 1)]({{ '/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_3_Flow_stress_for_aluminum_alloys_Type_1/' | relative_url }})
[10.1.1.4. Flow stress for aluminum alloys (Type 2)]({{ '/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_4_Flow_stress_for_aluminum_alloys_Type_2/' | relative_url }})
[10.1.1.5. Linear hardening]({{ '/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_5_Linear_hardening/' | relative_url }})

[10.1.1.6. Tabular data format (Atom)]({{ '/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_6_Tabular_data_format_2/' | relative_url }})

[10.1.1.7. Generalized Johnson and Cook model]({{ '/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_7_Generalized_Johnson_and_Cook_model/' | relative_url }})
[10.1.1.8. Zerilli-Armstrong model]({{ '/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_8_Zerilli-Armstrong_model/' | relative_url }})
[10.1.1.9. Norton-Hoff Law model]({{ '/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_9_Norton-Hoff_Law_model/' | relative_url }})
[10.1.1.10. Microstructure Flow stress model based on dislocation density and burgers vector]({{ '/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_10_Microstructure_dislocation_density_and_burgers_vector/' | relative_url }})
[10.1.1.12. User defined Tabular data]({{ '/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_12_User_defined_Tabular_data/' | relative_url }})
[10.1.1.13. User defined Tabular data (Log)]({{ '/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_13_User_defined_Tabular_data_log/' | relative_url }})
[10.1.1.14. Bird-Mukharjee-Dorn equation]({{ '/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_14_Bird-Mukharjee-Dorn_equation/' | relative_url }})

[10.1.1.15. User defined flow stress routine]({{ '/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_15_User_defined_flow_stress_routine/' | relative_url }})
[10.1.1.16. Flow stress database]({{ '/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_16_Flow_stress_database/' | relative_url }})
[10.1.1.17. Material model data conversion utilities]({{ '/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_17_Material_model_data_conversion_utilities/' | relative_url }})

---
lang: en
title: "10.1.1.11. Texture based flow stress model f(strn,strnrt,O,T)"
---

# 10.1.1.11. Texture based flow stress model f(strn,strnrt,O,T)

Flow stress magnitude can be strongly dependent on material microstructure. This flow stress model can be used to consider the effect of crystallographic orientation on the flow stress. This flow stress type should be only used for rigid plastic objects.

  
Before defining this flowstress model, user need to define the basic texture information in texture tab as shown in the below Fig. 10.1.1.11.1. Texture model definition involve defining Crystal type (crystal structure), Texture type (Rodrigues or Euler angles) and Texture mesh type. Euler angles texture type has not been implemented yet.

  
![](../../../../../assets/Images/Pre-Processor/10_Material_Data/10_1_Plastic_Data/10_1_1_Flow_Stress/10_1_1_11_Texture_based_f\(strn,strnrt,O,T\)/10_1_1_11_Image001.jpg)

Texture model definition

  
After defining texture information user has to select the crystallographic orientation flowstress model and define flowstress for each Rodrigues orientation which is based on the texture mesh type selected as a function of strain, strain rate and temperature ( Fig. 10.1.1.11.2.).

![](../../../../../assets/Images/Pre-Processor/10_Material_Data/10_1_Plastic_Data/10_1_1_Flow_Stress/10_1_1_11_Texture_based_f\(strn,strnrt,O,T\)/10_1_1_11_Image002.jpg)

Crystallographic orientation based flowstress window

[10.1.1.1. Tabular data format](/docs/en/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_1_Tabular_data_format/)  
[10.1.1.2. Power Law](/docs/en/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_2_Power_Law/)  
[10.1.1.3. Flow stress for aluminum alloys (Type 1)](/docs/en/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_3_Flow_stress_for_aluminum_alloys_Type_1/)  
[10.1.1.4. Flow stress for aluminum alloys (Type 2)](/docs/en/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_4_Flow_stress_for_aluminum_alloys_Type_2/)  
[10.1.1.5. Linear hardening](/docs/en/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_5_Linear_hardening/)

[10.1.1.6. Tabular data format (Atom)](/docs/en/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_6_Tabular_data_format_2/)

[10.1.1.7. Generalized Johnson and Cook model](/docs/en/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_7_Generalized_Johnson_and_Cook_model/)  
[10.1.1.8. Zerilli-Armstrong model](/docs/en/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_8_Zerilli-Armstrong_model/)  
[10.1.1.9. Norton-Hoff Law model](/docs/en/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_9_Norton-Hoff_Law_model/)  
[10.1.1.10. Microstructure Flow stress model based on dislocation density and burgers vector](/docs/en/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_10_Microstructure_dislocation_density_and_burgers_vector/)  
[10.1.1.12. User defined Tabular data](/docs/en/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_12_User_defined_Tabular_data/)  
[10.1.1.13. User defined Tabular data (Log)](/docs/en/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_13_User_defined_Tabular_data_log/)  
[10.1.1.14. Bird-Mukharjee-Dorn equation](/docs/en/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_14_Bird-Mukharjee-Dorn_equation/)

[10.1.1.15. User defined flow stress routine](/docs/en/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_15_User_defined_flow_stress_routine/)  
[10.1.1.16. Flow stress database](/docs/en/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_16_Flow_stress_database/)  
[10.1.1.17. Material model data conversion utilities](/docs/en/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_17_Material_model_data_conversion_utilities/)

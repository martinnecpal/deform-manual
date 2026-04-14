---
lang: sk
title: "10.1.1.15.User defined flow stress routine"
---

# 10.1.1.15. User defined flow stress routine

Apart from the above flow stress models, DEFORM system allows the flexibility with which user can implement their own flow stress models in to the system using user routines, build their own FEM engine, and use it to run the deformation model. While defining the their own flow stress models, users can have access to all the nodal and element state variables. Depending upon the material model usr_mtr.f fortran file user has to enter User Routine number as shown in Fig. 10.1.1.15.1.

  
![](../../../../../assets/Images/Pre-Processor/10_Material_Data/10_1_Plastic_Data/10_1_1_Flow_Stress/10_1_1_15_User_defined_flow_stress_routine/10_1_1_15_Image001.jpg)

Flow stress User routine window

  
Please refer to [Chapter 56. User Routines](/docs/sk/User_Routines/56_User_Routines_in_DEFORM/56_User_Routines_in_DEFORM/) for a description of how to implement user defined flow stress routines.

[10.1.1.1. Tabular data format](/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_1_Tabular_data_format/)  
[10.1.1.2. Power Law](/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_2_Power_Law/)  
[10.1.1.3. Flow stress for aluminum alloys (Type 1)](/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_3_Flow_stress_for_aluminum_alloys_Type_1/)  
[10.1.1.4. Flow stress for aluminum alloys (Type 2)](/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_4_Flow_stress_for_aluminum_alloys_Type_2/)  
[10.1.1.5. Linear hardening](/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_5_Linear_hardening/)

[10.1.1.6. Tabular data format (Atom)](/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_6_Tabular_data_format_2/)

[10.1.1.7. Generalized Johnson and Cook model](/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_7_Generalized_Johnson_and_Cook_model/)  
[10.1.1.8. Zerilli-Armstrong model](/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_8_Zerilli-Armstrong_model/)  
[10.1.1.9. Norton-Hoff Law model](/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_9_Norton-Hoff_Law_model/)  
[10.1.1.10. Microstructure Flow stress model based on dislocation density and burgers vector](/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_10_Microstructure_dislocation_density_and_burgers_vector/)  
[10.1.1.11. Texture based flow stress model f(strn,strnrt,O,T)](/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_11_Texture_based_flow_stress_model_fstrnstrnrtOT/)  
[10.1.1.12. User defined Tabular data](/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_12_User_defined_Tabular_data/)  
[10.1.1.13. User defined Tabular data (Log)](/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_13_User_defined_Tabular_data_log/)  
[10.1.1.14. Bird-Mukharjee-Dorn equation](/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_14_Bird-Mukharjee-Dorn_equation/)

[10.1.1.16. Flow stress database](/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_16_Flow_stress_database/)  
[10.1.1.17. Material model data conversion utilities](/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_17_Material_model_data_conversion_utilities/)

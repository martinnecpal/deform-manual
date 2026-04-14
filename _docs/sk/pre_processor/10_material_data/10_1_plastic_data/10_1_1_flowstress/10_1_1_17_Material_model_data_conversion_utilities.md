---
lang: sk
title: "10.1.1.17. Material model data conversion utilities"
---

# 10.1.1.17. Material model data conversion utilities

When the material flow stress data is available in the form of data table Fig. 10.1.1.17.1., user can convert this data in to a close form model equation using the ‘Conversion’ utilities. User can select material model from the available list, and fit the model parameters to match the table data points using the curve fitting techniques Fig. 10.1.1.17.2. Once this is done, the system displays both forms of the data for the users to proceed with. Typically solid lines in the graph indicate the original data, and the dashed lines from the flow curve computed based on the fitted model parameters.

![](../../../../../assets/Images/Pre-Processor/10_Material_Data/10_1_Plastic_Data/10_1_1_Flow_Stress/10_1_1_17_Material_model_data_conversion_utilities/10_1_1_17_Image001.JPG)

Material flow stress data in table form in temperature, strain rate and strain dimensions

![](../../../../../assets/Images/Pre-Processor/10_Material_Data/10_1_Plastic_Data/10_1_1_Flow_Stress/10_1_1_17_Material_model_data_conversion_utilities/10_1_1_17_Image002.JPG)

Results from material model data conversion

  
The user should make note that, like any other curve fitting techniques, the nature of original data and initial guess (if user can make one) on the model parameters will greatly influence the quality of the conversion results. This tool also provides options to selectively carry-out the curve fitting needs with control over the individual model parameters. Once user accepts the conversion, the converted model data replaces the original table data.

  
**Loading Measurement Files**

  
Additional functionality has been added to allow users to import multiple measured flow stress data files, each set at a given temperature and strain rate as shown in Fig. 10.1.1.17.3.

![](../../../../../assets/Images/Pre-Processor/10_Material_Data/10_1_Plastic_Data/10_1_1_Flow_Stress/10_1_1_17_Material_model_data_conversion_utilities/10_1_1_17_Image003.jpg)

Utilities to upload the measured flow stress data in to DEFORM system

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

[10.1.1.15. User defined flow stress routine](/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_15_User_defined_flow_stress_routine/)  
[10.1.1.16. Flow stress database](/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_16_Flow_stress_database/)

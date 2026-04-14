---
lang: en
title: "16.2. Thermal Properties"
---

# 16.2. Thermal Properties

16.2.1. Reference temperature (REFTMP)

16.2.2. Truncation temperature (TMPLMT)

16.2.3. Stopping temperature (OTPRNG)

![](../../../assets/Images/Pre-Processor/16_Object_Properties/16_2_Thermal_properties/16_2_Image001.jpg)

2D Thermal Object properties window

![](../../../assets/Images/Pre-Processor/16_Object_Properties/16_2_Thermal_properties/16_2_Image002.jpg)

3D Thermal Object properties window

## Reference temperature (REFTMP) [2D, 3D]

  
For elastic objects, the reference temperature ([REFTMP)](/docs/en/Keyword_Documentation/R/REFTMP/) is the temperature on which thermal expansion calculations are based. The thermal strains are given by: (See Fig. 16.2.1. and Fig. 16.2.2.)

![](../../../assets/Equations/Pre_Processor/16_Object_Properties/EQ_16_2_1.jpg) |   
---|---  
  
For Elasto-plastic objects, instantaneous coefficient of thermal expansion is used.

Coefficient of thermal expansion is set in the Material Properties Elastic menu, also refer section [10.2.4. Material Reference temperature](../10_Material_Data/10_2_Elastic_Data/10_2_Elastic_Data.htm#Material_Reference_Temperature) for difference between the material and object reference temperatures.

## Truncation temperature (TMPLMT) [2D, 3D]

The Truncation Temperature ([TMPLMT](/docs/en/Keyword_Documentation/T/TMPLMT/)) is the maximum nodal temperature allowed at any point in the object. If the calculated temperature exceeds this value, it will be reduced to this value.

## Stopping temperature (OTPRNG) [2D, 3D]

The stopping temperature ([OTPRNG](/docs/en/Keyword_Documentation/O/OTPRNG/)) sets an upper and lower temperature limit which, if exceeded, will stop the simulation. The user has the option of enforcing this limit if any single node exceeds the temperature, only if all nodes exceed the temperature or based on temperature at a specific node. For more information related to Stopping temperature range option, refer [9.3.10. Temperature stopping control](../9_Simulation_Controls/9_3_Stopping_Controls.htm#9.3.10._Temperature_stopping_control)

**Related Topics:**

[16\. Object properties](/docs/en/pre_processor/16_object_properties/16_object_properties/)

[16.1. Deformation properties](/docs/en/pre_processor/16_object_properties/16_1_deformation_properties/)

[16.3. Reference](/docs/en/pre_processor/16_object_properties/16_3_Reference/)

[16.4. Fracture Properties](/docs/en/pre_processor/16_object_properties/16_4_Fracture_properties/)

[16.5. Hardness Properties](/docs/en/pre_processor/16_object_properties/16_5_hardness_properties/)

[16.6. Heating Properties](/docs/en/pre_processor/16_object_properties/16_6_heating_properties/)

[16.7. Symmetry Properties](/docs/en/pre_processor/16_object_properties/16_7_symmetry_properties/)

[16.8. Body Force](/docs/en/pre_processor/16_object_properties/16_8_body_force/)

[16.9. RSE](/docs/en/pre_processor/16_object_properties/16_9_rse/)

[16.10. User](/docs/en/pre_processor/16_object_properties/16_10_user/)

[Difference b/w material and object reference temperature](../10_Material_Data/10_2_Elastic_Data/10_2_Elastic_Data.htm#Material_Reference_Temperature)

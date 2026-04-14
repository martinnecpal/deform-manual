---
lang: sk
title: "16.5. Hardness estimation type"
---

# 16.5. Hardness Estimation type

[2D, 3D]: Material hardness predictions can be based on: (See Fig. 16.5.1. to Fig. 16.5.5.)

  * Volume fraction of various phases
  * Jominy curve data
  * Cooling time
  * Solid solution with precipitation

Hardness data for a material can be defined in the Material Properties of the respective object material and will be estimated based on the estimation type selected under Properties of the respective object, Fig. 16.5.1. shows estimation type options available under Hardness in Object Properties. A description of the hardness prediction method is given there. For more information on defining Hardness in Material Properties, please refer section [10.7. Hardness data.](/docs/sk/pre_processor/10_Material_Data/10_7_Hardness_Data/10_7_Hardness_Data/)

  
**Referenced Start temperature, End temperature** : Upper and lower temperature values for Jominy or cooling time hardness prediction curves. 

![](../../../assets/Images/Pre-Processor/16_Object_Properties/16_5_Hardness_Properties/16_5_Image001.jpg)

Hardness estimation type in Object properties window

  1. "**Use volume fractions** ": Hardness is computed based on the individual phases (Mixture rule) evolving during the quench process at the respective element using the hardness data defined in material properties of the respective phase.

![](../../../assets/Images/Pre-Processor/16_Object_Properties/16_5_Hardness_Properties/16_5_Image003.jpg)

Use jominy curves type Hardness estimation

  1. "**Use jominy curves** ": Referenced Start temperature and End temperature needs to be defined for hardness estimation using Jominy curves which will be used to activate cooling range. Time spent by a material point in the temperature range + the Jominy data provided under material properties will be used for the hardness computations, see Fig. 16.5.3. Time spent by a material point in this temperature range and rate of temperature range is the basis for cooling time and rate computations. 

  1. When the temperature is higher than the referenced high temperature, the hardness flag is set to -2.
  2. When the temperature reaches (equal to or less than) the referenced high temperature, the "Hardness" flag is set to -3, and this instantaneous time is recorded in the "cooling time". This flag and cooling time is set only one time and will be kept for the subsequent steps until the temperature reaches the referenced low temperature, see Fig. 16.5.4.
  3. When the material point is inside the Reference temperature range, cooling time only indicates the time stamp of a material point entering in this temperature range, see Fig. 16.5.4.
  4. When the material point completely cools below the cooling the correct value of hardness is updated, see Fig. 16.5.4.

![](../../../assets/Images/Pre-Processor/16_Object_Properties/16_5_Hardness_Properties/16_5_Image002.jpg)

Use jominy curve type Hardness estimation

![](../../../assets/Images/Pre-Processor/16_Object_Properties/16_5_Hardness_Properties/16_5_Image006.jpg)

Simulation results with Use jominy curve type Hardness estimation

  1. "**Only cooling time** ": Referenced Start temperature and End temperature is used to activate cooling range. Time spent by a material point in this temperature range + the Jominy data provided is the basis for cooling time, see Fig. 16.5.5.. No hardness is computed.

In the element data dialogue,

  1. When the temperature is higher than the referenced high temperature, the hardness flag is set to -2.
  2. When the temperature reaches (equal to or less than) the referenced high temperature, the "Hardness" flag is set to -3, and this instantaneous time is recorded in the "cooling time". This flag and cooling time is set only one time and will be kept for the subsequent steps until the temperature reaches the referenced low temperature.
  3. When the temperature reaches (equal to or less than) the referenced low temperature, the "Hardness" flag is set to -4, the elapse time from reaching the referenced high temperature to reaching the low referenced temperature is recorded in the "Cooling time". This flag and cooling time is set only one time, and will be kept in the subsequent steps. In each simulation step, it is divided into 10 sub-steps, so that the time to reach the referenced temperature can be more accurately determined.

In summary, for the cooling process, when the "Hardness" flag is -3, the "cooling time" means the time to reach the referenced high temperature; when the "Hardness" flag is -4, the "cooling time" means the time interval from the referenced high temperature to the referenced low temperature.

![](../../../assets/Images/Pre-Processor/16_Object_Properties/16_5_Hardness_Properties/16_5_Image003.jpg)

Only cooling time type Hardness estimation

  1. For "**Solid solution with precipitate** ” option, hardness is computed based on the precipitation model, see Fig. 16.5.6..

![](../../../assets/Images/Pre-Processor/16_Object_Properties/16_5_Hardness_Properties/16_5_Image003.jpg)

Solid solution with precipitate type Hardness estimation

**Related Topics:**

[16\. Object properties](/docs/sk/pre_processor/16_object_properties/16_object_properties/)

[16.1. Deformation properties](/docs/sk/pre_processor/16_object_properties/16_1_deformation_properties/)

[16.2. Thermal properties](/docs/sk/pre_processor/16_object_properties/16_2_thermal_properties/)

[16.3. Reference](/docs/sk/pre_processor/16_object_properties/16_3_Reference/)

[16.4. Fracture Properties](/docs/sk/pre_processor/16_object_properties/16_4_Fracture_properties/)

[16.6. Heating Properties](/docs/sk/pre_processor/16_object_properties/16_6_heating_properties/)

[16.7. Symmetry Properties](/docs/sk/pre_processor/16_object_properties/16_7_symmetry_properties/)

[16.8. Body Force](/docs/sk/pre_processor/16_object_properties/16_8_body_force/)

[16.9. RSE](/docs/sk/pre_processor/16_object_properties/16_9_rse/)

[16.10. User](/docs/sk/pre_processor/16_object_properties/16_10_user/)

[Material Hardness properties](/docs/sk/pre_processor/10_Material_Data/10_7_Hardness_Data/10_7_Hardness_Data/)

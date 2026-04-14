---
lang: sk
title: "16.6. Heating Properties"
---

# 16.6. Heating Properties

16.6.1. Current frequency

16.6.2. Volume Charge

16.6.3. Data Definition

[**2D, 3D**]: When Induction heating computations are required, the same needs to be first turned on in the simulation controls before defining the associated object values like current frequency (See Fig. 16.6.1. and Fig. 16.6.2.). CG solver is also an option for solving induction heating models, and is capable of solving models with reasonable size.

See [Fig. 9.1.3.](../9_Simulation_Controls/9_1_Simulation_type_Settings.htm#Fig._9.1.3. Simulation Controls window - Heating) for selecting the Induction heating simulation mode. For Electrical and Magnetic material properties refer section [10.8. Electromagnetic data](/docs/sk/pre_processor/16_object_properties/16_5_hardness_properties/).

DEFORM FEM engine can now handle induction heating models with dual frequency input data for current frequency in both 2D & 3D.

![](../../../assets/Images/Pre-Processor/16_Object_Properties/16_6_Heating_Properties/16_6_Image001.jpg)

Induction Heating Object properties window for Single frequency settings

![](../../../assets/Images/Pre-Processor/16_Object_Properties/16_6_Heating_Properties/16_6_Image002.jpg)

Induction Heating Object properties window for Dual frequency settings

## Current frequency [2D, 3D]

Specifies the frequency of current for heating object. It can be a constant value or a function of time.

## Volume Charge [2D, 3D]

Volume charge can be in three modes:

  * **Current Density** : It is a measure of the density of electrical current. It is defined as a vector whose magnitude is the electric current per cross-sectional area. Current density unit is Amp/mm2 or Amp/inch2 in 2d axi-symmetry model and 3d model. In 2d plane model case, coil cross section will be edge line, and thickness is unit length, so current density unit will be Amp/mm or Amp/inch.
  * **Input power** : The electrical power taken by a power tool from the energy source.
  * **Voltage drop** : It is the reduction in voltage in an electrical circuit between the source and load.

## Data Definition [2D, 3D]

Data definition can be a constant or function of time for a volume charge of Input power, Current Density and Voltage Drop type.

**Related Topics:**

[16\. Object properties](/docs/sk/pre_processor/16_object_properties/16_object_properties/)

[16.1. Deformation properties](/docs/sk/pre_processor/16_object_properties/16_1_deformation_properties/)

[16.2. Thermal properties](/docs/sk/pre_processor/16_object_properties/16_2_thermal_properties/)

[16.3. Reference](/docs/sk/pre_processor/16_object_properties/16_3_Reference/)

[16.4. Fracture Properties](/docs/sk/pre_processor/16_object_properties/16_4_Fracture_properties/)

[16.5. Hardness Properties](/docs/sk/pre_processor/16_object_properties/16_5_hardness_properties/)

[16.7. Symmetry Properties](/docs/sk/pre_processor/16_object_properties/16_7_symmetry_properties/)

[16.8. Body Force](/docs/sk/pre_processor/16_object_properties/16_8_body_force/)

[16.9. RSE](/docs/sk/pre_processor/16_object_properties/16_9_rse/)

[16.10. User](/docs/sk/pre_processor/16_object_properties/16_10_user/)

[Material Electrical and magnetic properties](/docs/sk/pre_processor/10_Material_Data/10_8_Elec_Mag_Data/10_8_Elec_Mag_Data/)

[10\. Material Data](/docs/sk/pre_processor/10_Material_Data/10_Material_Data/)

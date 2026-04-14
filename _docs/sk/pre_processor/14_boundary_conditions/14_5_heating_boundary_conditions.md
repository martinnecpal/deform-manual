---
lang: sk
title: "14.5. Heating Boundary Conditions"
---

# 14.5. Heating Boundary Conditions

14.5.1. Resistance Heating [2D, 3D]

14.5.2. Induction Heating

14.5.3. Induction Heating (BEM)

## Resistance Heating [2D, 3D]

**Voltage BCC**

Specifies a fixed voltage over the nodes or elements bordered by the indicated edges. Units are Volt. This is usually defined for resistance and induction type of problems.

**Current Flux BCC**

Specifies a fixed dominant current flux rate over the elements bordered by the indicated edges. Units are Amp/time.

From V12, PID control option added to Current flux BCC for 2D objects as shown in Fig. 14.5.1. Using this option user can automatically control the Current flux by defining the PID control parameters, target temperature and thermocouple location.

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_5_Heating_Boundary_Conditions/14_5_Image001.jpg)

Current flux PID option [only for 2D]

## Induction Heating 

**[2D]** : Once Induction Heating check box is checked in simulation controls, Induction heating in properties window and Heating tab in Inter object Relations get activated. For more information please refer [16.6. Heating Properties](/docs/sk/pre_processor/16_Object_Properties/16_6_heating_properties/) and [20.3. Interface Resistivity.](/docs/sk/pre_processor/20_Inter-object_Data_Definition/20_3_Interface_Resisitivity/)

**[3D]** : For 3D coil begin and end surface bcc are available (see Fig. 14.5.2.).

**Coil Begin surface [3D]** : Specifies the begin surface of coil.

**Coil End surface [3D]** : Specifies the end surface of coil.

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_5_Heating_Boundary_Conditions/14_5_Image004.jpg)

Induction BCC window for 3D

## Induction Heating (BEM) 

This BCC option is available for Induction BEM process only.

**Heating Surface[2D, 3D]**  
Heating Surface BCC specifies the surface of the coil which heats the workpiece and also the workpiece gets heated by the coil.

**Coil Begin surface [3D]**  
Specifies the begin surface of Coil.

**Coil End surface [3D]**  
Specifies the end surface of Coil. See Fig. 14.5.3. for the induction BEM BCC settings.

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_5_Heating_Boundary_Conditions/14_5_Image002.jpg) ![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_5_Heating_Boundary_Conditions/14_5_Image003.jpg)

(a) (b)

Induction (BEM) BCC window: (a) For 2D and (b) For 3D

**Related Topics:**

[14\. Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/)

[14.1. Symmetry Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_1_symmetry_boundary_conditions/)

[14.2. Deformation Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_2_deformation_boundary_conditions/)

[14.3. Thermal Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_3_thermal_boundary_conditions/)

[14.4. Diffusion Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_4_diffusion_boundary_conditions/)

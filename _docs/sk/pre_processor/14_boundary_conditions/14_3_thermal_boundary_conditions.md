---
lang: sk
title: "14.3. Thermal Boundary Conditions"
---

# 14.3. Thermal Boundary Conditions

14.3.1. Heat exchange with the environment BCC   
14.3.2. Temperature BCC  
14.3.3. Heat flux BCC  
14.3.4. Nodal heat BCC  
14.3.5. Advanced Thermal BCC

## Heat exchange with the environment BCC [2D,3D]

This boundary condition [ECCTMP](/docs/sk/Keyword_Documentation/E/ECCTMP/) specifies that heat exchange between element faces bounded by these nodes and their environment should occur. The contact boundary condition determines whether exchange will occur to the ambient atmosphere or to a contacting object.

Default heat exchange with the environment occurs to the ambient environment as described above. However, heat exchange windows may be specified using the heat exchange windows icon. Heat exchange for nodes within these windows is controlled by the parameters set for each window.

**Heat Exchange windows**

This function allows the user to define heat exchange conditions for local areas on a body by use of three dimensional window. To use heat exchange windows, perform the following actions:

  1. Go to the Boundary Conditions window.
  2. Select the Thermal tab.
  3. Select the Heat exchange windows button.
  4. Note the tools in the top left corner of the display window changes and the new heat exchange window that comes up.
  5. At this point, heat exchange windows can be defined using the tools in the top left corner of the display window. Each window has its own local environmental temperature, convection coefficient, Heat flux and emissivity. See Fig. 14.3.1. of heat exchange window. 
  6. You can define up to 20 independent windows by the method. If two regions share the same space, the lower number window wins.

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_3_Thermal_Boundary_Conditions/14_3_Image003.jpg)

(a)

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_3_Thermal_Boundary_Conditions/14_3_Image001.jpg)

(b)

Heat exchange with Environment window; (a) For 2D and (b) For 3D

## Temperature BCC [2D, 3D]

Specifies a fixed temperature at the given nodes.

##  Heat flux BCC [2D, 3D]

This ([ECHFLX](/docs/sk/Keyword_Documentation/E/ECHFLX/)) Specifies an energy flux per unit area over the face of the element bounded by the nodes. Units are energy/time/area.

## Nodal heat BCC [2D, 3D]

Specifies a heat source at the given nodes. Units are energy/time.

## Advanced Thermal BCC [2D, 3D]

The purpose of this boundary condition definition is to allow the user to have the flexibility to specify all the various types of heat boundary conditions on the same edge. The user can specify either a user-subroutine number or a local heat transfer definition. (See Fig. 14.3.2.) If the user wants to specify a user routine, the User Routine Number should be specified. The User Routine number specified will correspond to the subroutine the boundary condition will correspond to. Refer to User Routines for more information on how to use these user-defined boundary conditions. If the routine number is left zero, the user may then define a local defined boundary condition where the environmental temperature, the convection coefficient, the emissivity and the heat flux needs to be specified the edge. All four of these variables may be defined as either constants or functions. To apply a local user defined boundary condition, set the variables you want, set the local defined number to a unique value, and apply this to a set of element edges. The new keywords for local edge definition are [ECCDEF](/docs/sk/Keyword_Documentation/E/ECCDEF/), [ECTMFN](/docs/sk/Keyword_Documentation/E/ECTMFN/) and [LOCTMP](/docs/sk/Keyword_Documentation/L/LOCTMP/).

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_3_Thermal_Boundary_Conditions/14_3_Image002.jpg)

Advanced Thermal object boundary condition window

**Related Topics:**

[14\. Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/)

[14.1. Symmetry Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_1_symmetry_boundary_conditions/)

[14.2. Deformation Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_2_deformation_boundary_conditions/)

[14.4. Diffusion Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_4_diffusion_boundary_conditions/)

[14.5. Heating Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_5_heating_boundary_conditions/)

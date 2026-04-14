---
lang: sk
title: "14.4. Diffusion Boundary Conditions"
---

# 14.4. Diffusion Boundary Conditions

14.4.1. Diffusion with the environment BCC

14.4.2. Atom content BCC

14.4.3. Atom flux BCC

14.4.4. Advanced Diffusion BCC

## Diffusion with the environment BCC [2D/3D]

Specifies diffusion of the dominant atom through the boundary elements bordered by the indicated nodes. Environment dominant atom content ([ECCATM](/docs/sk/Keyword_Documentation/E/ECCATM/)) and surface reaction rate are specified under the Simulation Controls, Processing Conditions menu. Environment content and reaction rate for various regions of the part may be modified by using diffusion windows.

## Fixed atom content BCC [2D/3D]

Specifies a fixed dominant atom content at the given nodes.

## Atom flux BCC [2D/3D]

Specifies a fixed dominant atom flux rate over the elements bordered by the indicated edges. Atom flux may be defined as a constant or as a function. The keywords for this are [ECCATM](/docs/sk/Keyword_Documentation/E/ECCATM/) and [ECAFLX](/docs/sk/Keyword_Documentation/E/ECAFLX/).

## Advanced Diffusion BCC [2D/3D]

The purpose of this boundary condition definition is to allow the user to have the flexibility to specify all the various types of diffusion boundary conditions on the same edge. The user can specify either a user-subroutine number or a local diffusion definition. (See Fig. 14.4.1.) If the user wants to specify a user routine, the User Routine Number should be specified. The User Routine number specified will correspond to the subroutine the boundary condition will correspond to. Refer to User Routines for more information on how to use these user-defined boundary conditions. If the routine number is left zero, the user may then define a local defined boundary condition where the environmental atom content, the reaction rate coefficient, and the atom flux needs to be specified the edge. All three of these variables may be defined as either constants or functions. To apply a local user defined boundary condition, set the variables you want, set the local defined number to a unique value, and apply this to a set of element edges. The keywords for this are [ECCATM](/docs/sk/Keyword_Documentation/E/ECCATM/) ,[ECAFLX](/docs/sk/Keyword_Documentation/E/ECAFLX/)and [LOCATM](/docs/sk/Keyword_Documentation/L/LOCATM/).

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_4__Diffusion_Boundary_Conditions/14_4_Image001.jpg)

Advanced Diffusion object boundary condition window

From V12, we can define Diffusion BCC options for each Atom type separately, we can observe both types of atoms defined in Simulation controls [Diffusion](../9_Simulation_Controls/9_6_Process_Conditions.htm#9.6.2._Diffusion_) page. (See Fig. 14.4.2.)

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_4__Diffusion_Boundary_Conditions/14_4_Image002.jpg)

Selecting different atom type from pull down menu list

**Related Topics:**

[14\. Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/)

[14.1. Symmetry Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_1_symmetry_boundary_conditions/)

[14.2. Deformation Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_2_deformation_boundary_conditions/)

[14.3. Thermal Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_3_thermal_boundary_conditions/)

[14.5. Heating Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_5_heating_boundary_conditions/)

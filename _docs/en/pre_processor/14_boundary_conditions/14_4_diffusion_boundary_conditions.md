---
lang: en
title: "14.4. Diffusion Boundary Conditions"
---

# 14.4. Diffusion Boundary Conditions

14.4.1. Diffusion with the environment BCC

14.4.2. Atom content BCC

14.4.3. Atom flux BCC

14.4.4. Advanced Diffusion BCC

## Diffusion with the environment BCC [2D/3D]

Specifies diffusion of the dominant atom through the boundary elements bordered by the indicated nodes. Environment dominant atom content ([ECCATM]({{ '/docs/en/keyword_documentation/e/eccatm/' | relative_url }})) and surface reaction rate are specified under the Simulation Controls, Processing Conditions menu. Environment content and reaction rate for various regions of the part may be modified by using diffusion windows.

## Fixed atom content BCC [2D/3D]

Specifies a fixed dominant atom content at the given nodes.

## Atom flux BCC [2D/3D]

Specifies a fixed dominant atom flux rate over the elements bordered by the indicated edges. Atom flux may be defined as a constant or as a function. The keywords for this are [ECCATM]({{ '/docs/en/keyword_documentation/e/eccatm/' | relative_url }}) and [ECAFLX]({{ '/docs/en/keyword_documentation/e/ecaflx/' | relative_url }}).

## Advanced Diffusion BCC [2D/3D]

The purpose of this boundary condition definition is to allow the user to have the flexibility to specify all the various types of diffusion boundary conditions on the same edge. The user can specify either a user-subroutine number or a local diffusion definition. (See Fig. 14.4.1.) If the user wants to specify a user routine, the User Routine Number should be specified. The User Routine number specified will correspond to the subroutine the boundary condition will correspond to. Refer to User Routines for more information on how to use these user-defined boundary conditions. If the routine number is left zero, the user may then define a local defined boundary condition where the environmental atom content, the reaction rate coefficient, and the atom flux needs to be specified the edge. All three of these variables may be defined as either constants or functions. To apply a local user defined boundary condition, set the variables you want, set the local defined number to a unique value, and apply this to a set of element edges. The keywords for this are [ECCATM]({{ '/docs/en/keyword_documentation/e/eccatm/' | relative_url }}) ,[ECAFLX]({{ '/docs/en/keyword_documentation/e/ecaflx/' | relative_url }})and [LOCATM]({{ '/docs/en/keyword_documentation/l/locatm/' | relative_url }}).

![]({{ '/assets/images/pre-processor/14_boundary_conditions/14_4__diffusion_boundary_conditions/14_4_image001.jpg' | relative_url }})

Advanced Diffusion object boundary condition window

From V12, we can define Diffusion BCC options for each Atom type separately, we can observe both types of atoms defined in Simulation controls [Diffusion]({{ '/docs/en/pre_processor/9_simulation_controls/9_6_process_conditions/' | relative_url }}#9.6.2._Diffusion_) page. (See Fig. 14.4.2.)

![]({{ '/assets/images/pre-processor/14_boundary_conditions/14_4__diffusion_boundary_conditions/14_4_image002.jpg' | relative_url }})

Selecting different atom type from pull down menu list

**Related Topics:**

[14\. Boundary Conditions]({{ '/docs/en/pre_processor/14_boundary_conditions/14_boundary_conditions/' | relative_url }})

[14.1. Symmetry Boundary Conditions]({{ '/docs/en/pre_processor/14_boundary_conditions/14_1_symmetry_boundary_conditions/' | relative_url }})

[14.2. Deformation Boundary Conditions]({{ '/docs/en/pre_processor/14_boundary_conditions/14_2_deformation_boundary_conditions/' | relative_url }})

[14.3. Thermal Boundary Conditions]({{ '/docs/en/pre_processor/14_boundary_conditions/14_3_thermal_boundary_conditions/' | relative_url }})

[14.5. Heating Boundary Conditions]({{ '/docs/en/pre_processor/14_boundary_conditions/14_5_heating_boundary_conditions/' | relative_url }})

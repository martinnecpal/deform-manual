---
lang: en
title: "14.2. Deformation Boundary Conditions"
---

# 14.2. Deformation Boundary Conditions

14.2.1. Velocity BCC

  * Free Distortion BCC

14.2.2. Pressure BCC

14.2.3. Force BCC

14.2.4. Movement BCC

14.2.5. Shrink fit BCC

14.2.6. Contact BCC

14.2.7. Beginning surface BCC

14.2.8. Free surface BCC

14.2.9. Rolling BCC

14.2.10. Advanced deformation BCC

## Velocity BCC [2D, 3D]

[2D]: Velocity of each node can be specified independently in the X and Y directions. Velocity boundary conditions are normally set to zero for symmetry conditions, but may also be set to a specified non-zero value for processes such as drawing in which a workpiece is pulled through a die. (See Fig. 14.2.1.)

![]({{ '/assets/images/pre-processor/14_boundary_conditions/14_2_deformation_boundary_conditions/14_2_image001.jpg' | relative_url }})

2D velocity BCC window

[3D]: Velocity of each node can be specified independently in the X, Y, and Z directions. Velocity boundary conditions are normally set to zero for symmetry conditions (Symmetry BCC [3D]), but may also be set to a specified non-zero value for processes such as drawing in which a workpiece is pulled through a die.

Even, we can define Velocity BCC using All direction option for both 2D and 3D, with this option user can assign BCC for all directions at a time.

Note:

If parallel symmetry planes are to be defined, velocity boundary conditions can only be used on one plane. A rigid surface should be defined on the other.

**Free Distortion BCC****[3D]**

The free distortion window can be accessed from the velocity BCC window. (See Fig. 14.2.2.) Free distortion boundary condition is applied where there is a possibility of maximum distortion taking place.

![]({{ '/assets/images/pre-processor/14_boundary_conditions/14_2_deformation_boundary_conditions/14_2_image002.jpg' | relative_url }})

Free Distortion BCC window

**Procedure for applying free distortion boundary condition:**

  1. Fix one node in X, Y, Z direction respectively. This removes the three-degree of freedom in translation. 
  2. Find a point at the same X and Z value but different Y – fix this in Z direction – X-rotation. 
  3. Find a point at the same Y and X value but different Z – fix this in X direction – Y rotation. 
  4. Find a point at the same Z and Y value but different X – fix this in Y direction – Z rotation (See Fig. 14.2.3.)

![]({{ '/assets/images/pre-processor/14_boundary_conditions/14_2_deformation_boundary_conditions/14_2_image003.jpg' | relative_url }})

Fixing of nodes in X, Y and Z direction

A typical example showing how to define free distortion BCC:

  1. User picks a node to fix in X, Y, Z directions as shown in Fig. 14.2.4.

![]({{ '/assets/images/pre-processor/14_boundary_conditions/14_2_deformation_boundary_conditions/14_2_image004.jpg' | relative_url }})

Selection of node to be fixed in XYZ direction

  1. System suggests a node to fix in Z direction. The suggested node has minimum angle to Y axis and is furthest from the XYZ fixed node. (See Fig. 14.2.5.)

![]({{ '/assets/images/pre-processor/14_boundary_conditions/14_2_deformation_boundary_conditions/14_2_image005.jpg' | relative_url }})

Selection of node to be fixed in Z direction

  1. System suggests a node to fix in X direction. The suggested node has minimum angle to Z axis and is furthest from the XYZ fixed node. (See Fig. 14.2.6.)

![]({{ '/assets/images/pre-processor/14_boundary_conditions/14_2_deformation_boundary_conditions/14_2_image006.jpg' | relative_url }})

Selection of node to be fixed in X direction

  1. System suggests a node to fix in Y direction. The suggested node has minimum angle to X axis and is furthest from the XYZ fixed node. User input can also be used while fixing the X, Y, Z nodes. (See Fig. 14.2.7.)

![]({{ '/assets/images/pre-processor/14_boundary_conditions/14_2_deformation_boundary_conditions/14_2_image007.jpg' | relative_url }})

Selection of node to be fixed in Y direction

The defined free distortion BCC is as shown in Fig. 14.2.8.,

![]({{ '/assets/images/pre-processor/14_boundary_conditions/14_2_deformation_boundary_conditions/14_2_image008.jpg' | relative_url }})

Defined free distortion BCC

## Pressure BCC [2D, 3D]

**[2D]** : The pressure boundary conditions specifies a uniform, or linearly varying, force per unit area on the element faces connecting the specified edges. Two values for the normal pressure are required, the first value is the beginning value of pressure from the beginning point where pressure is set, the second value is the value at the end of where the pressure is specified. The pressure is linearly interpolated between the start and the end. The keywords for pressure are [ECCDEF]({{ '/docs/en/Keyword_Documentation/E/ECCDEF/' | relative_url }}) and [ECPRES]({{ '/docs/en/Keyword_Documentation/E/ECPRES/' | relative_url }}). User can define Pressure window as shown in Fig. 14.2.9.

![]({{ '/assets/images/pre-processor/14_boundary_conditions/14_2_deformation_boundary_conditions/14_2_image009.jpg' | relative_url }})

(a)

![]({{ '/assets/images/pre-processor/14_boundary_conditions/14_2_deformation_boundary_conditions/14_2_image010.jpg' | relative_url }})

(b)

2D pressure window definition; (a) For 2D (b) pressure window

**[3D]** : The pressure boundary conditions specifies a uniform, or linearly varying, force per unit area on the element faces connecting the specified nodes. For more information about how to define free distortion BCC please refer Free Distortion BCC [ 3D].

![]({{ '/assets/images/pre-processor/14_boundary_conditions/14_2_deformation_boundary_conditions/14_2_image011.jpg' | relative_url }})

3D pressure window definition

## Force BCC [2D, 3D]

Force boundary conditions specify the force applied on each node. The force is specified in default units. For die stress analysis, the force that the die exerted on the workpiece can be reversed and interpolated onto the dies by using the interpolation function.

**Steps to Define Force interpolation:**

  1. Click on ![]({{ '/assets/icons/pre_icons/mo_interpolate_button.jpg' | relative_url }}) Button, a window will pops up as shown in Fig. 14.2.11.

![]({{ '/assets/images/pre-processor/14_boundary_conditions/14_2_deformation_boundary_conditions/14_2_image012.jpg' | relative_url }})

Database interpolation widow

  1. Click on ![]({{ '/assets/icons/pre_icons/mo_browse_button.jpg' | relative_url }}) select step from the loaded DB at which interpolation of forces needs to be carried over. (See Fig. 14.2.12.)

![]({{ '/assets/images/pre-processor/14_boundary_conditions/14_2_deformation_boundary_conditions/14_2_image013.jpg' | relative_url }})

Database interpolation widow showing step number selection

  1. Select workpiece object from the popup window. System will define tolerance automatically required for interpolation if the tolerance field has 0.00 value. User can specify required tolerance value in error tolerance tab as shown in Fig. 14.2.13. Click on ![]({{ '/assets/icons/pre_icons/mo_interpolate_button2.jpg' | relative_url }}).

![]({{ '/assets/images/pre-processor/14_boundary_conditions/14_2_deformation_boundary_conditions/14_2_image014.jpg' | relative_url }})

Database Interpolation window showing Defining object number and Error tolerance

  1. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) when Force interpolation tolerance window will pop up. (See Fig. 14.2.14)

![]({{ '/assets/images/pre-processor/14_boundary_conditions/14_2_deformation_boundary_conditions/14_2_image015.jpg' | relative_url }})

Force Interpolation window 

The interpolated forces will be displayed under force tab as shown in Fig. 14.2.15.

![]({{ '/assets/images/pre-processor/14_boundary_conditions/14_2_deformation_boundary_conditions/14_2_image016.jpg' | relative_url }})

Force interpolation of 2D Top die 

## Movement BCC [2D, 3D]

The movement of specific nodes on an object can be specified. If the movement boundary condition is specified, object movement controls must also be specified. 

## Shrink fit BCC [2D, 3D]

A specified displacement can be specified in any direction for each node. This is frequently used for specifying shrink fit conditions between a die insert and a shrink ring.

Shrink Fit BCC in 3D used for die stress analysis, This can be defined by following steps,

  * Entering the interference value. 
  * Selecting the Direction (Direction perpendicular to the inner surface of the shrink ring or outer surface of the Die insert)
  * Selecting the inner surface of the shrink ring or outer surface of the Die insert (surface which is contact with the die)

If shrink fit is applied to the inner object, the value should be negative and If shrink fit is applied to the outer object then the value should be positive.

For more information on shrink fit, Please refer [2D Die Stress Analysis Theory]({{ '/docs/en/Operation_Templates/30_Die_Stress/2D_Die_Stress_Analysis_Theory/' | relative_url }}).

## Contact BCC [2D, 3D]

The Contact boundary condition displays inter-object boundary contact conditions on a given object. The user should gain some experience with DEFORM before using this option. The contact conditions are stored in three components to represent the fact that there are three degrees of freedom for any given node.

Contact boundary conditions are applied to nodes of a slave object, and specify contact between those nodes and the surface of a master object (See Fig. 14.2.1.). If a node is specified to be in contact with a particular object, it will be placed on the surface of that object. If this requires changing the position of that node, it will be changed as necessary. Contact boundary conditions are generated under the Inter-object Contact relation ([CNTACT]({{ '/docs/en/Keyword_Documentation/C/CNTACT/' | relative_url }})) section.

Contact boundary conditions can be displayed for a given object using the Objects, Boundary Conditions, Advanced Deformation BCC's icon.

## Beginning surface BCC [3D]

In Extrusion process this specifies the beginning surface of the workpiece.

## Free Surface BCC [3D]

In Extrusion process this specifies the end surface of the workpiece.

## Rolling BCC [3D]

![]({{ '/assets/images/pre-processor/14_boundary_conditions/14_2_deformation_boundary_conditions/14_2_image017.jpg' | relative_url }})

Rolling Boundary condition window 

**Text to be added**

## Advanced deformation BCC [2D, 3D]

The Advanced boundary condition displays inter-object boundary contact conditions on a given object. This is the same information displayed in the Inter-Object BCC's window. There is no physical significance to the X or Y components of contact. Rather, the ``directions'' are dictated by numerical convenience. Contact conditions are first assigned to the Y direction. If that position is occupied by another value, conditions are assigned in the X direction. For more information please refer section [Nodal data- Deform BCC](../17_Object_Data_Initialization/17_1_Node_Data_Window.htm#Deform_BCC) ([BCCDEF]({{ '/docs/en/Keyword_Documentation/B/BCCDEF/' | relative_url }})).

Depending upon the BCC usr_bcc.f fortan file, user has to enter User Routine number. Please refer to [Chapter 56. User Routines]({{ '/docs/en/User_Routines/56_User_Routines_in_DEFORM/56_User_Routines_in_DEFORM/' | relative_url }}) for a description of how to implement user defined BCC routines. (See Fig. 14.2.17.)

![]({{ '/assets/images/pre-processor/14_boundary_conditions/14_2_deformation_boundary_conditions/14_2_image018.jpg' | relative_url }})

(a)

![]({{ '/assets/images/pre-processor/14_boundary_conditions/14_2_deformation_boundary_conditions/14_2_image019.jpg' | relative_url }})

(b)

Advanced Deformation object boundary condition window; (a) For 2D (b) For 3D

**Related Topics:**

[14\. Boundary Conditions]({{ '/docs/en/pre_processor/14_boundary_conditions/14_boundary_conditions/' | relative_url }})

[14.1. Symmetry Boundary Conditions]({{ '/docs/en/pre_processor/14_boundary_conditions/14_1_symmetry_boundary_conditions/' | relative_url }})

[14.3. Thermal Boundary Conditions]({{ '/docs/en/pre_processor/14_boundary_conditions/14_3_thermal_boundary_conditions/' | relative_url }})

[14.4. Diffusion Boundary Conditions]({{ '/docs/en/pre_processor/14_boundary_conditions/14_4_diffusion_boundary_conditions/' | relative_url }})

[14.5. Heating Boundary Conditions]({{ '/docs/en/pre_processor/14_boundary_conditions/14_5_heating_boundary_conditions/' | relative_url }})

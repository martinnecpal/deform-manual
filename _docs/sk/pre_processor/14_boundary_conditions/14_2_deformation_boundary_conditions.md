---
lang: sk
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

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_2_Deformation_Boundary_Conditions/14_2_Image001.jpg)

2D velocity BCC window

[3D]: Velocity of each node can be specified independently in the X, Y, and Z directions. Velocity boundary conditions are normally set to zero for symmetry conditions (Symmetry BCC [3D]), but may also be set to a specified non-zero value for processes such as drawing in which a workpiece is pulled through a die.

Even, we can define Velocity BCC using All direction option for both 2D and 3D, with this option user can assign BCC for all directions at a time.

Note:

If parallel symmetry planes are to be defined, velocity boundary conditions can only be used on one plane. A rigid surface should be defined on the other.

**Free Distortion BCC****[3D]**

The free distortion window can be accessed from the velocity BCC window. (See Fig. 14.2.2.) Free distortion boundary condition is applied where there is a possibility of maximum distortion taking place.

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_2_Deformation_Boundary_Conditions/14_2_Image002.jpg)

Free Distortion BCC window

**Procedure for applying free distortion boundary condition:**

  1. Fix one node in X, Y, Z direction respectively. This removes the three-degree of freedom in translation. 
  2. Find a point at the same X and Z value but different Y – fix this in Z direction – X-rotation. 
  3. Find a point at the same Y and X value but different Z – fix this in X direction – Y rotation. 
  4. Find a point at the same Z and Y value but different X – fix this in Y direction – Z rotation (See Fig. 14.2.3.)

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_2_Deformation_Boundary_Conditions/14_2_Image003.jpg)

Fixing of nodes in X, Y and Z direction

A typical example showing how to define free distortion BCC:

  1. User picks a node to fix in X, Y, Z directions as shown in Fig. 14.2.4.

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_2_Deformation_Boundary_Conditions/14_2_Image004.jpg)

Selection of node to be fixed in XYZ direction

  1. System suggests a node to fix in Z direction. The suggested node has minimum angle to Y axis and is furthest from the XYZ fixed node. (See Fig. 14.2.5.)

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_2_Deformation_Boundary_Conditions/14_2_Image005.jpg)

Selection of node to be fixed in Z direction

  1. System suggests a node to fix in X direction. The suggested node has minimum angle to Z axis and is furthest from the XYZ fixed node. (See Fig. 14.2.6.)

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_2_Deformation_Boundary_Conditions/14_2_Image006.jpg)

Selection of node to be fixed in X direction

  1. System suggests a node to fix in Y direction. The suggested node has minimum angle to X axis and is furthest from the XYZ fixed node. User input can also be used while fixing the X, Y, Z nodes. (See Fig. 14.2.7.)

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_2_Deformation_Boundary_Conditions/14_2_Image007.jpg)

Selection of node to be fixed in Y direction

The defined free distortion BCC is as shown in Fig. 14.2.8.,

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_2_Deformation_Boundary_Conditions/14_2_Image008.jpg)

Defined free distortion BCC

## Pressure BCC [2D, 3D]

**[2D]** : The pressure boundary conditions specifies a uniform, or linearly varying, force per unit area on the element faces connecting the specified edges. Two values for the normal pressure are required, the first value is the beginning value of pressure from the beginning point where pressure is set, the second value is the value at the end of where the pressure is specified. The pressure is linearly interpolated between the start and the end. The keywords for pressure are [ECCDEF](/docs/sk/Keyword_Documentation/E/ECCDEF/) and [ECPRES](/docs/sk/Keyword_Documentation/E/ECPRES/). User can define Pressure window as shown in Fig. 14.2.9.

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_2_Deformation_Boundary_Conditions/14_2_Image009.jpg)

(a)

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_2_Deformation_Boundary_Conditions/14_2_Image010.jpg)

(b)

2D pressure window definition; (a) For 2D (b) pressure window

**[3D]** : The pressure boundary conditions specifies a uniform, or linearly varying, force per unit area on the element faces connecting the specified nodes. For more information about how to define free distortion BCC please refer Free Distortion BCC [ 3D].

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_2_Deformation_Boundary_Conditions/14_2_Image011.jpg)

3D pressure window definition

## Force BCC [2D, 3D]

Force boundary conditions specify the force applied on each node. The force is specified in default units. For die stress analysis, the force that the die exerted on the workpiece can be reversed and interpolated onto the dies by using the interpolation function.

**Steps to Define Force interpolation:**

  1. Click on ![](../../../assets/Icons/Pre_icons/MO_Interpolate_button.jpg) Button, a window will pops up as shown in Fig. 14.2.11.

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_2_Deformation_Boundary_Conditions/14_2_Image012.jpg)

Database interpolation widow

  1. Click on ![](../../../assets/Icons/Pre_icons/MO_Browse_button.jpg) select step from the loaded DB at which interpolation of forces needs to be carried over. (See Fig. 14.2.12.)

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_2_Deformation_Boundary_Conditions/14_2_Image013.jpg)

Database interpolation widow showing step number selection

  1. Select workpiece object from the popup window. System will define tolerance automatically required for interpolation if the tolerance field has 0.00 value. User can specify required tolerance value in error tolerance tab as shown in Fig. 14.2.13. Click on ![](../../../assets/Icons/Pre_icons/MO_Interpolate_button2.jpg).

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_2_Deformation_Boundary_Conditions/14_2_Image014.jpg)

Database Interpolation window showing Defining object number and Error tolerance

  1. Click ![](../../../assets/Icons/Pre_icons/MO_OK_button.jpg) when Force interpolation tolerance window will pop up. (See Fig. 14.2.14)

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_2_Deformation_Boundary_Conditions/14_2_Image015.jpg)

Force Interpolation window 

The interpolated forces will be displayed under force tab as shown in Fig. 14.2.15.

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_2_Deformation_Boundary_Conditions/14_2_Image016.jpg)

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

For more information on shrink fit, Please refer [2D Die Stress Analysis Theory](/docs/sk/Operation_Templates/30_Die_Stress/2D_Die_Stress_Analysis_Theory/).

## Contact BCC [2D, 3D]

The Contact boundary condition displays inter-object boundary contact conditions on a given object. The user should gain some experience with DEFORM before using this option. The contact conditions are stored in three components to represent the fact that there are three degrees of freedom for any given node.

Contact boundary conditions are applied to nodes of a slave object, and specify contact between those nodes and the surface of a master object (See Fig. 14.2.1.). If a node is specified to be in contact with a particular object, it will be placed on the surface of that object. If this requires changing the position of that node, it will be changed as necessary. Contact boundary conditions are generated under the Inter-object Contact relation ([CNTACT](/docs/sk/Keyword_Documentation/C/CNTACT/)) section.

Contact boundary conditions can be displayed for a given object using the Objects, Boundary Conditions, Advanced Deformation BCC's icon.

## Beginning surface BCC [3D]

In Extrusion process this specifies the beginning surface of the workpiece.

## Free Surface BCC [3D]

In Extrusion process this specifies the end surface of the workpiece.

## Rolling BCC [3D]

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_2_Deformation_Boundary_Conditions/14_2_Image017.jpg)

Rolling Boundary condition window 

**Text to be added**

## Advanced deformation BCC [2D, 3D]

The Advanced boundary condition displays inter-object boundary contact conditions on a given object. This is the same information displayed in the Inter-Object BCC's window. There is no physical significance to the X or Y components of contact. Rather, the ``directions'' are dictated by numerical convenience. Contact conditions are first assigned to the Y direction. If that position is occupied by another value, conditions are assigned in the X direction. For more information please refer section [Nodal data- Deform BCC](../17_Object_Data_Initialization/17_1_Node_Data_Window.htm#Deform_BCC) ([BCCDEF](/docs/sk/Keyword_Documentation/B/BCCDEF/)).

Depending upon the BCC usr_bcc.f fortan file, user has to enter User Routine number. Please refer to [Chapter 56. User Routines](/docs/sk/User_Routines/56_User_Routines_in_DEFORM/56_User_Routines_in_DEFORM/) for a description of how to implement user defined BCC routines. (See Fig. 14.2.17.)

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_2_Deformation_Boundary_Conditions/14_2_Image018.jpg)

(a)

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_2_Deformation_Boundary_Conditions/14_2_Image019.jpg)

(b)

Advanced Deformation object boundary condition window; (a) For 2D (b) For 3D

**Related Topics:**

[14\. Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/)

[14.1. Symmetry Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_1_symmetry_boundary_conditions/)

[14.3. Thermal Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_3_thermal_boundary_conditions/)

[14.4. Diffusion Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_4_diffusion_boundary_conditions/)

[14.5. Heating Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_5_heating_boundary_conditions/)

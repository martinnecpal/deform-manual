---
lang: en
title: "15. Movement Controls Settings"
---

# 15\. Movement Controls Settings

15.1. Movement controls Types  
15.1.1. Translation movement  
15.1.2. Rotational movement  
15.1.3. Torsional movement  
15.1.4. Friction Welding movement  
15.2. Assigning movement to Deformable objects  
15.3. Movement controls Tools

15.4. Movement Controls User Routine

Movement controls can be applied to rigid objects and boundary nodes of meshed objects. The surface defined by these nodes can be thought of as a "rigid surface". During the simulation, the constrained nodes will move synchronously in the speed and direction defined by the movement controls. Movement controls windows for 2D and 3D are as shown in Fig. 15.1. and Fig. 15.2. respectively.

![]({{ '/assets/images/pre-processor/15_movement_controls/15_image001.jpg' | relative_url }})

2D Movement controls settings window

![]({{ '/assets/images/pre-processor/15_movement_controls/15_image002.jpg' | relative_url }})

3D Movement controls settings window

## Movement controls Types

For 3D object, movement controls is categorized into Translation movement controls and Rotational movement controls .

For 2D Axisymmetric geometry type, we have Translation movement controls.

For 2D Torsion geometry type, we have Translation and Torsion movement controls. 

For 2D Plane stress and Plane strain geometry type, we have Translation and Rotation movement controls.

For 2.5D Friction welding geometry type, we have Translation and Friction welding movement controls.

### **Translation movement**

During the simulation the constrained nodes will move synchronously in the speed and direction defined by the movement controls. Types of Movement controls that are available in Translation Movement controls are Speed, Force, Hammer, Screw press, Mechanical press, Hydraulic press, Sliding Die and Path. Translation movement for 2D and 3D are as shown in Fig. 15.1. and Fig. 15.2. For more information, please refer [15.1. Speed](/docs/en/pre_processor/15_movement_controls_definition/15_1_speed/), [15.2. Force](/docs/en/pre_processor/15_movement_controls_definition/15_2_force/), [15.3. Hammer](/docs/en/pre_processor/15_movement_controls_definition/15_3_hammer/), [15.4. Screw press](/docs/en/pre_processor/15_movement_controls_definition/15_4_screw_press/), [15.5. Mechanical press](/docs/en/pre_processor/15_movement_controls_definition/15_5_mechanical_press/), [15.6. Hydraulic press](/docs/en/pre_processor/15_movement_controls_definition/15_6_hydraulic_press/), [15.7. Sliding Die](/docs/en/pre_processor/15_movement_controls_definition/15_7_sliding_die/) and [15.8. Path](/docs/en/pre_processor/15_movement_controls_definition/15_8_path/).

### **Rotational movement**

****Rotational movement is defined by an angular velocity/torque about a fixed center of rotation. This movement type causes only rotation. Unless otherwise specified, translation is constrained. The rotational speed is controlled through the Controlling Method option and the point at which the object is rotated about is set through the Center of Rotational Movement. For more information, please refer[15.9. Rotational Movement](/docs/en/pre_processor/15_movement_controls_definition/15_9_rotational_movement/).

### **Torsional movement**

Torsional movement controls are applicable only in the case of torsional formulations. This movement control option is active for DEFORM-2D only. For more information, please refer [15.10. Torsional movement](/docs/en/pre_processor/15_movement_controls_definition/15_10_torsional_movement/).

### **Friction Welding movement**

Friction Welding movement controls are applicable only in the case of 2.5D Frictional welding formulations. This movement control option is active for DEFORM-2D only. For more information, please refer [15.11. Friction Welding movement](/docs/en/pre_processor/15_movement_controls_definition/15_11_friction_welding_movement/).

**Directions [2D, 3D]** : Based on the problem setup user can select the direction of the translation movement. Other direction option is also available for the angular directions selections.

For 2D model X, Y, -X, -Y and Other directions are available. Other direction type needs angle in deg along with the sign, +ve sign indicates upward direction and -ve sign indicates downward direction.

For 3D model X,Y,Z,-X,-Y,-Z and Other directions are available. Other direction type needs the direction vectors with signs along X, Y and Z directions. For example if the die moves in both +ve Y and -ve Z directions then (0,1,-1) must be defined in other direction vectors fields.

## Assigning movement to Deformable objects

[2D, 3D]: In case of coupled dies stress study or other situation where user need to define the translational movement for the deformable objects like, Elastic, Plastic, Elasto plastic and Porous Movement Boundary condition under deformation BCC tree must be defined for that object. The movement Boundary condition defined plane must be the surface not in contact with the other objects where the deformation is intended, because the Movement BCC defined plane wont deform but move with the translational movement defined. (See Fig. 15.3. and Fig. 15.4.)

![]({{ '/assets/images/pre-processor/15_movement_controls/15_image004.jpg' | relative_url }})

2D Movement BCC definition for elastic dies for coupled die stress analysis

![]({{ '/assets/images/pre-processor/15_movement_controls/15_image005.jpg' | relative_url }})

3D Movement BCC definition for elastic dies for coupled die stress analysis

## Movement controls Tools

**Load Movement controls settings** : Using Import movement from a file ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) and Load movement from library ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) options user can import saved movement to object. 

****Save Movement controls settings**** : Using Save movement to a file ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) and Save movement to library ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) options user can save the movement data.

**Movement Preview** ![]({{ '/assets/icons/pre_icons/mo_preview_icon.jpg' | relative_url }}): Clicking the preview button allows the user to see the movement that has been specified for a given object (See Fig. 15.5.). The options in the movement preview dialog allow the user to see the movement of the current object in the display screen. This will only take into account translation and rotational movement but not force or torque control.

![]({{ '/assets/images/pre-processor/15_movement_controls/15_image003.jpg' | relative_url }})

Movement preview window

**Delete Movement controls settings** ![]({{ '/assets/icons/pre_icons/mo_clear_icon.jpg' | relative_url }}): Using this option user can delete the assigned movement data.

## Movement control user subroutines

[2D, 3D]: Complex die movement can be defined using user defined FORTRAN subroutines. USRDSP routine allows the user to calculate the speed of the rigid object that has movement defined as a user model. Please refer [chapter 56.2.3.2 USER ROUTINE USRDSP](../../user_routines/56_user_routines_in_deform/56_2_2d_user_defined_fem_routines.htm#56_2_3_2_User_defined_movement_control_\(USRDSP\)) for 2D and 3D for a description of how to implement user defined subroutines. The defined routine number must be specified in the movement control window as shown in the below Fig. 15.6. and Fig. 15.7.

![]({{ '/assets/images/pre-processor/15_movement_controls/15_image006.jpg' | relative_url }})

2D Force movement control User routine number calling window

![]({{ '/assets/images/pre-processor/15_movement_controls/15_image007.jpg' | relative_url }})

3D Speed movement control User routine number calling window

**Related Topics:**

[15.1. Speed](/docs/en/pre_processor/15_movement_controls_definition/15_1_speed/)

[15.2. Force](/docs/en/pre_processor/15_movement_controls_definition/15_2_force/)

[15.3. Hammer](/docs/en/pre_processor/15_movement_controls_definition/15_3_hammer/)

[15.4. Screw press](/docs/en/pre_processor/15_movement_controls_definition/15_4_screw_press/)

[15.5. Mechanical press](/docs/en/pre_processor/15_movement_controls_definition/15_5_mechanical_press/)

[15.6. Hydraulic press](/docs/en/pre_processor/15_movement_controls_definition/15_6_hydraulic_press/)

[15.7. Sliding Die](/docs/en/pre_processor/15_movement_controls_definition/15_7_sliding_die/)

[15.8. Path](/docs/en/pre_processor/15_movement_controls_definition/15_8_path/)

[15.9. Rotational Movement](/docs/en/pre_processor/15_movement_controls_definition/15_9_rotational_movement/)

[15.10. Torsional movement](/docs/en/pre_processor/15_movement_controls_definition/15_10_torsional_movement/)

[15.11. Friction Welding movement](/docs/en/pre_processor/15_movement_controls_definition/15_11_friction_welding_movement/)

[Primary die selection from simulation controls](../9_simulation_controls/9_2_defining_step.htm#Primary_die_\(PDIE\))

[Step increment control (DSMAX/DTMAX)](../9_simulation_controls/9_2_defining_step.htm#Step_increment_control_\(DSMAX/DTMAX\)) [2D, 3D]

[Selecting time step and number of steps](../9_simulation_controls/9_2_defining_step.htm#Selecting_time_step_and_number_of_steps) [2D, 3D]

[Primary die stopping controls from simulation controls](../9_simulation_controls/9_3_stopping_controls.htm#9.3.2._Primary_Die_Displacement_\(SMAX\))

[Primary die selection from general object data definition window](../11_general_object_data_definition/11_general_object_data_definition.htm#11.5._Primary_Die)

[2D Geometry type selection from Simulation controls](../9_simulation_controls/9_1_simulation_type_settings.htm#9.1.2._Geometry_type_\(GEOTYP\)_\[2D\])

[14\. Boundary Conditions](/docs/en/pre_processor/14_boundary_conditions/14_boundary_conditions/)

[18\. Object Positioning](/docs/en/pre_processor/19_object_positioning/19_object_positioning/)

[Movement-User Routine (USRDSP)](../../user_routines/56_user_routines_in_deform/56_2_2d_user_defined_fem_routines.htm#56_2_3_2_User_defined_movement_control_\(USRDSP\))

[2D Basic Labs](/docs/en/labs/basic_labs/2d_labs/2d_labs/)

[3D Basic Labs](/docs/en/labs/basic_labs/3d_labs/3d_labs/)

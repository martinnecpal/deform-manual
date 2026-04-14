---
lang: en
title: "15.9. Rotational Movement"
---

# 15.9. Rotational Movement

15.9.1. Torque

15.9.2. Angular velocity

  
**[2D, 3D]** : Rotational movement is defined by an angular velocity about a fixed center of rotation. This movement type causes only rotation. Unless otherwise specified, translation is constrained. The rotational speed is controlled through the Controlling Method option and the point at which the object is rotated about is set through the Center of Rotational Movement. See Fig. 15.9.1., Fig. 15.9.2. and Fig. 15.9.3. for 2d and 3d model rotational movement settings.

![]({{ '/assets/images/pre-processor/15_movement_controls/15_9_rotational_movement/15_9_image001.jpg' | relative_url }})

Rotation movement controls window settings for 2D Torque

![]({{ '/assets/images/pre-processor/15_movement_controls/15_9_rotational_movement/15_9_image002.jpg' | relative_url }})

Rotation movement controls window settings for 2D Angular velocity

![]({{ '/assets/images/pre-processor/15_movement_controls/15_9_rotational_movement/15_9_image003.jpg' | relative_url }})

Rotation movement controls window settings for 3D Torque and Angular velocity

Rotational Motion can be applied to simulate rolling or any type of movement where an object will rotate about a fixed axis. Rotational Motion can only be applied to Rigid objects. Rigid objects can have both [Rotational](15_movement_controls_settings.htm#15.1.2._Rotational_movement) and [Translational](15_movement_controls_settings.htm#15.1.1._Translation_movement) movement simultaneously.

**Controlling Method**

The objects rotation can be controlled by an Angular Velocity or a Torque. Select the required control and enter the value for the rotation just below.

## **Torque**

The Torque movement type will apply a rotational motion about the defined axis at a specified torque. The torque can be specified as a constant or as a function of time or angle.

## **Angular Velocity**

Angular Velocity will apply rotational motion about the defined axis at a specified angular velocity in radians per second. The angular velocity can be specified as a constant or as a function of time or angle. Along with axis data, options are available to compute the center and axis from the geometry.

Note:

Idle rolls can be defined by specifying torque control with a very low torque value.

**Axis of Rotation** : is specified by a vector originating at the point center and through the point direction. Rotation direction is defined by the right hand rule. That is, positive rotation is clockwise as viewed from the center point looking towards the direction point.

**Current Angle** : current position of the object.

**Related Topics:**

[15\. Movement Controls Settings](/docs/en/pre_processor/15_movement_controls_definition/15_movement_controls_settings/)

[15.1. Speed](/docs/en/pre_processor/15_movement_controls_definition/15_1_speed/)

[15.2. Force](/docs/en/pre_processor/15_movement_controls_definition/15_2_force/)

[15.3. Hammer](/docs/en/pre_processor/15_movement_controls_definition/15_3_hammer/)

[15.4. Screw press](/docs/en/pre_processor/15_movement_controls_definition/15_4_screw_press/)

[15.5. Mechanical press](/docs/en/pre_processor/15_movement_controls_definition/15_5_mechanical_press/)

[15.6. Hydraulic press](/docs/en/pre_processor/15_movement_controls_definition/15_6_hydraulic_press/)

[15.7. Sliding Die](/docs/en/pre_processor/15_movement_controls_definition/15_7_sliding_die/)

[15.8. Path](/docs/en/pre_processor/15_movement_controls_definition/15_8_path/)

[15.10. Torsional movement](/docs/en/pre_processor/15_movement_controls_definition/15_10_torsional_movement/)

[15.11. Friction Welding movement](/docs/en/pre_processor/15_movement_controls_definition/15_11_friction_welding_movement/)

[Appendix XIV: Rotating Workpiece Simulations](/docs/en/appendices/appendix_xiv_rotating_workpiece_simulations/)

[3D Orbital Movement](/docs/en/applications/55_applications/55_orbital_movement/3d_orbital_movement/)

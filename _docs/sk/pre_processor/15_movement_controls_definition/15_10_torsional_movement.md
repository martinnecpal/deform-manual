---
lang: sk
title: "15.10. Torsional movement"
---

# 15.10. Torsional movement

15.10.1. Angular velocity

15.10.2. Energy

**[2D]** : Torsional movement controls are applicable only in the case of torsional formulations. This movement control option is active for DEFORM-2D only. For these movement settings see Fig. 15.10.1. and Fig. 15.10.2.

![]({{ '/assets/images/pre-processor/15_movement_controls/15_10_torsional_movement/15_10_image001.jpg' | relative_url }})

Torsion movement controls window settings for Angular velocity

![]({{ '/assets/images/pre-processor/15_movement_controls/15_10_torsional_movement/15_10_image002.jpg' | relative_url }})

Torsion movement controls window settings for Energy

**Controlling Method**  
The objects torsion can be controlled by an Angular Velocity or energy. Select the required control and enter the values.

## Angular Velocity

Angular Velocity will apply torsional motion about the defined axis at a specified angular velocity in radians per second. The angular velocity can be specified as a constant or as a function of time or angle. (See Fig. 15.10.1.)

Note:

Idle rolls can be defined by specifying torque control with a very low torque value.

## Energy

Torsional motion is based on Energy, Moment of Inertia, and efficiency values as shown in Fig. 15.10.2.

**Current Angle** : current position of the object.

**Related Topics:**

[15\. Movement Controls Settings](/docs/sk/pre_processor/15_movement_controls_definition/15_movement_controls_settings/)

[15.1. Speed](/docs/sk/pre_processor/15_movement_controls_definition/15_1_speed/)

[15.2. Force](/docs/sk/pre_processor/15_movement_controls_definition/15_2_force/)

[15.3. Hammer](/docs/sk/pre_processor/15_movement_controls_definition/15_3_hammer/)

[15.4. Screw press](/docs/sk/pre_processor/15_movement_controls_definition/15_4_screw_press/)

[15.5. Mechanical press](/docs/sk/pre_processor/15_movement_controls_definition/15_5_mechanical_press/)

[15.6. Hydraulic press](/docs/sk/pre_processor/15_movement_controls_definition/15_6_hydraulic_press/)

[15.7. Sliding Die](/docs/sk/pre_processor/15_movement_controls_definition/15_7_sliding_die/)

[15.8. Path](/docs/sk/pre_processor/15_movement_controls_definition/15_8_path/)

[15.9. Rotational Movement](/docs/sk/pre_processor/15_movement_controls_definition/15_9_rotational_movement/)

[15.11. Friction Welding movement](/docs/sk/pre_processor/15_movement_controls_definition/15_11_friction_welding_movement/)

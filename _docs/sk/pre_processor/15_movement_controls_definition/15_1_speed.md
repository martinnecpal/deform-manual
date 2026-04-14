---
lang: sk
title: "15.1. Speed"
---

# 15.1. Speed

**[2D, 3D]:** This is the default movement control (See Fig. 15.1.1.and Fig. 15.1.2.), which specifies the speed and direction of a object. The speed may be defined in one way of hte following ways.

  * Constant

  * Function of stroke of the primary object

  * Function of time

  * Function of force (load) on the object

  * Proportional to the speed of another object

  * Sinusoidal function

When an object is rigid, the entire object will move at the assigned speed. When the object is elastic, plastic, or porous, each node with a movement boundary condition assigned will maintain the assigned speed. Note that movement boundary conditions should never be assigned for all surface nodes. In general, no more than 1/2 to 2/3 of the boundary nodes on an object should have movement boundary conditions.

Symmetry planes are defined with V=0 boundary conditions perpendicular to the applied surface. Due to limitations of border extraction during remeshing, parallel symmetry planes should be defined using at least one rigid symmetry surface, instead of V=0 boundary conditions on both sides of the object.

Current Force field is added for all movement types and user can observe the current force at different steps. 

![]({{ '/assets/images/pre-processor/15_movement_controls/15_1_speed/15_1_image001.jpg' | relative_url }})

2D Speed movement contros window

![]({{ '/assets/images/pre-processor/15_movement_controls/15_1_speed/15_1_image002.jpg' | relative_url }})

3D Speed movement contros window

Related Topics:

[15\. Movement Controls Settings](/docs/sk/pre_processor/15_movement_controls_definition/15_movement_controls_settings/)

[15.2. Force](/docs/sk/pre_processor/15_movement_controls_definition/15_2_force/)

[15.3. Hammer](/docs/sk/pre_processor/15_movement_controls_definition/15_3_hammer/)

[15.4. Screw press](/docs/sk/pre_processor/15_movement_controls_definition/15_4_screw_press/)

[15.5. Mechanical press](/docs/sk/pre_processor/15_movement_controls_definition/15_5_mechanical_press/)

[15.6. Hydraulic press](/docs/sk/pre_processor/15_movement_controls_definition/15_6_hydraulic_press/)

[15.7. Sliding Die](/docs/sk/pre_processor/15_movement_controls_definition/15_7_sliding_die/)

[15.8. Path](/docs/sk/pre_processor/15_movement_controls_definition/15_8_path/)

[15.9. Rotational Movement](/docs/sk/pre_processor/15_movement_controls_definition/15_9_rotational_movement/)

[15.10. Torsional movement](/docs/sk/pre_processor/15_movement_controls_definition/15_10_torsional_movement/)

[15.11. Friction Welding movement](/docs/sk/pre_processor/15_movement_controls_definition/15_11_friction_welding_movement/).

---
lang: en
title: "15.2. Force"
---

# 15.2. Force

**[2D, 3D]** : For force (load) control (See Fig. 15.2.1. and Fig. 15.2.2.), the speed of the object is constrained such that the specified load on the object is maintained. The force may be defined in one of the following ways.

  * Constant

  * Function of stroke of the primary object

  * Function of time

When the object is rigid, the load is the resultant load applied by all non-rigid objects that contact it. When the object is elastic, plastic, or porous, the load is the sum of the nodal loads of all nodes with movement boundary condition codes defined. This boundary condition adds a degree of freedom to the system of equations to be solved during the simulation. Arbitrary application of this condition can create difficulty in obtaining a converged solution.

![]({{ '/assets/images/pre-processor/15_movement_controls/15_2_force/15_2_image001.jpg' | relative_url }})

2D Force movement controls window

![]({{ '/assets/images/pre-processor/15_movement_controls/15_2_force/15_2_image002.jpg' | relative_url }})

3D Force movement controls window

**Related Topics:**

[15\. Movement Controls Settings](/docs/en/pre_processor/15_movement_controls_definition/15_movement_controls_settings/)

[15.1. Speed](/docs/en/pre_processor/15_movement_controls_definition/15_1_speed/)

[15.3. Hammer](/docs/en/pre_processor/15_movement_controls_definition/15_3_hammer/)

[15.4. Screw press](/docs/en/pre_processor/15_movement_controls_definition/15_4_screw_press/)

[15.5. Mechanical press](/docs/en/pre_processor/15_movement_controls_definition/15_5_mechanical_press/)

[15.6. Hydraulic press](/docs/en/pre_processor/15_movement_controls_definition/15_6_hydraulic_press/)

[15.7. Sliding Die](/docs/en/pre_processor/15_movement_controls_definition/15_7_sliding_die/)

[15.8. Path](/docs/en/pre_processor/15_movement_controls_definition/15_8_path/)

[15.9. Rotational Movement](/docs/en/pre_processor/15_movement_controls_definition/15_9_rotational_movement/)

[15.10. Torsional movement](/docs/en/pre_processor/15_movement_controls_definition/15_10_torsional_movement/)

[15.11. Friction Welding movement](/docs/en/pre_processor/15_movement_controls_definition/15_11_friction_welding_movement/).

---
lang: sk
title: "15.7. Sliding Die"
---

# 15.7. Sliding Die

[2D, 3D]: Defining sliding movement can be done in the movement controls window as seen in Fig. 15.7.1. and Fig. 15.7.2. To use spring-loaded dies, the object should be rigid and should not have any other movement specified.

The following items should be specified for all spring-loaded die cases:

  * Turn spring-loaded die controls to ON.

  * The movement direction should be specified in the direction that compresses the spring. The spring force will be applied opposite the direction of movement.

  * **Stiffness** specifies the stiffness in klb/in (English) or N/mm (SI) units. The stiffness can be either a constant or a function of compression amount.

  * **Preload** specifies the amount of force to overcome before compression occurs in klb (English) or N (SI).
  * **Maximum displacement** is the distance where the spring eventually bottoms out and which cause the spring to not move anymore in the compression direction.
  * **Other end of spring** determines whether the spring is fixed to another rigid object or whether the other end is fixed to a position in space. In the case where the object is fixed to a position in space, the compression direction, the current displacement and maximum displacement determine how much the spring is compressed and whether it is bottomed out. In the case where the spring is attached to another object, the distance between the two objects will determine the amount of compression.
  * **No of Steps before Damping** : **Text to be added**

![]({{ '/assets/images/pre-processor/15_movement_controls/15_7_sliding_die/15_7_image001.jpg' | relative_url }})

2D Sliding die movement controls window

![]({{ '/assets/images/pre-processor/15_movement_controls/15_7_sliding_die/15_7_image002.jpg' | relative_url }})

3D Sliding die movement controls window

**Related Topics:**

[15\. Movement Controls Settings](/docs/sk/pre_processor/15_movement_controls_definition/15_movement_controls_settings/)

[15.1. Speed](/docs/sk/pre_processor/15_movement_controls_definition/15_1_speed/)

[15.2. Force](/docs/sk/pre_processor/15_movement_controls_definition/15_2_force/)

[15.3. Hammer](/docs/sk/pre_processor/15_movement_controls_definition/15_3_hammer/)

[15.4. Screw press](/docs/sk/pre_processor/15_movement_controls_definition/15_4_screw_press/)

[15.5. Mechanical press](/docs/sk/pre_processor/15_movement_controls_definition/15_5_mechanical_press/)

[15.6. Hydraulic press](/docs/sk/pre_processor/15_movement_controls_definition/15_6_hydraulic_press/)

[15.8. Path](/docs/sk/pre_processor/15_movement_controls_definition/15_8_path/)

[15.9. Rotational Movement](/docs/sk/pre_processor/15_movement_controls_definition/15_9_rotational_movement/)

[15.10. Torsional movement](/docs/sk/pre_processor/15_movement_controls_definition/15_10_torsional_movement/)

[15.11. Friction Welding movement](/docs/sk/pre_processor/15_movement_controls_definition/15_11_friction_welding_movement/)

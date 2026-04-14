---
lang: sk
title: "15.6. Hydraulic press"
---

# 15.6. Hydraulic press

15.6.1. Speed  
15.6.2. Average strain rate  
15.6.3. Dwell Controls   
15.6.4. Elastic Losses

**[2D, 3D]:** To use the hydraulic press model the user can control one of two manners.

## Speed [2D, 3D]

The speed of the press may be defined in one of the following ways (See Fig. 15.6.1. and Fig. 15.6.2.).

  * Constant

  * Function of time

  * Function of stroke of the primary object

A power limit curve characterizing the hydraulic press may also be entered as a function of load. See Example [2D Basic lab 10 Hydraulic press.](/docs/sk/labs/basic_labs/2d_labs/lab_10_hydraulic_press/)

Note:

To activate maximum speed control, the power limit must be defined.

![]({{ '/assets/images/pre-processor/15_movement_controls/15_6_hydraulic_press/15_6_image001.jpg' | relative_url }})

2D Hydraulic press speed movement controls settings

![]({{ '/assets/images/pre-processor/15_movement_controls/15_6_hydraulic_press/15_6_image002.jpg' | relative_url }})

3D Hydraulic press speed movement controls settings

## Average strain rate [2D, 3D]

  
The average strain rate control can also used to define the press speed (See Fig. 15.6.3.). Note that the initial billet height needs to be provided and should be a reasonably accurate measurement.

**Allowed maximum strain rate** : This setting can be defined in addition to the controls mentioned above. This will prevent the speed from exceeding a condition where the maximum strain rate in the part would exceed the defined maximum strain rate.

![]({{ '/assets/images/pre-processor/15_movement_controls/15_6_hydraulic_press/15_6_image003.jpg' | relative_url }})

Hydraulic press Average strain rate movement controls settings

## Dwell Controls [2D, 3D]

In hydraulic press, we can stop the simulation based on the load or a minimum velocity stopping criteria. Also we can define Dwell time in Hydraulic press, when stopping criteria reaches Dwell calculation will starts till the defined Total dwell time. Dwell controls options is as shown in  Fig. 15.6. 4.

![]({{ '/assets/images/pre-processor/15_movement_controls/15_6_hydraulic_press/15_6_image004.jpg' | relative_url }})

Hydraulic Press Dwell Controls

## Elastic Losses

The stiffness of a press or a hammer can be defined in this dialog. In the case of a press there can be stretch based on the forging load and the final distance of the press will be less by the amount of the stretch. In the case of a hammer, the compliance accounts for elastic loss of energy.

**Related Topics:**

[15\. Movement Controls Settings](/docs/sk/pre_processor/15_movement_controls_definition/15_movement_controls_settings/)

[15.1. Speed](/docs/sk/pre_processor/15_movement_controls_definition/15_1_speed/)

[15.2. Force](/docs/sk/pre_processor/15_movement_controls_definition/15_2_force/)

[15.3. Hammer](/docs/sk/pre_processor/15_movement_controls_definition/15_3_hammer/)

[15.4. Screw press](/docs/sk/pre_processor/15_movement_controls_definition/15_4_screw_press/)

[15.5. Mechanical press](/docs/sk/pre_processor/15_movement_controls_definition/15_5_mechanical_press/)

[15.7. Sliding Die](/docs/sk/pre_processor/15_movement_controls_definition/15_7_sliding_die/)

[15.8. Path](/docs/sk/pre_processor/15_movement_controls_definition/15_8_path/)

[15.9. Rotational Movement](/docs/sk/pre_processor/15_movement_controls_definition/15_9_rotational_movement/)

[15.10. Torsional movement](/docs/sk/pre_processor/15_movement_controls_definition/15_10_torsional_movement/)

[15.11. Friction Welding movement](/docs/sk/pre_processor/15_movement_controls_definition/15_11_friction_welding_movement/)

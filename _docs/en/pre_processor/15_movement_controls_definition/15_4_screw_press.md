---
lang: en
title: "15.4. Screw press"
---

# 15.4. Screw press

**[2D, 3D]:** The unique characteristic of a screw press is the method of driving it. A motor drives a flywheel which is either directly connected or can be connected to a screw spindle. The screw spindle transmits the rotation through the threads, which have pitch angles usually between 13 and 17 degrees, to a linear movement of the main ram. On contact with the work piece, the complete kinetic energy of the flywheel and the ram is transformed into useful work (work on the work piece) and losses (elastic deformation work in the work piece and the frame of the structure and friction). The elastic deformation work results in a reaction force in all the press parts lying in the force transmission path.

![]({{ '/assets/images/pre-processor/15_movement_controls/15_4_screw_press/15_4_image001.jpg' | relative_url }})

2D Screw Press movement controls window

![]({{ '/assets/images/pre-processor/15_movement_controls/15_4_screw_press/15_4_image002.jpg' | relative_url }})

3D Screw Press movement controls window

The Screw press energy method will mimic the movement of a screw type press on the selected die. In a screw press a flywheel is taken to a given speed and a clutch is engaged. Once the clutch is engaged, the screw press begins to draw energy to drive the screw from the flywheel. Once the flywheel energy is expended the stroke is over and the movement will stop. Screw controlled movement can only be specified for rigid objects or deforming objects with a movement boundary condition applied. Motion of which is controlled by screw press parameters can only be applied in the +X, +Y, +Z, -X, -Y or -Z directions (X, Y, -X, or -Y directions in case of DEFORM-2D).

For Screw press movement settings see Fig. 15.4.1. and Fig. 15.4.2.

The data required to run a screw press driven tool are:

  * **Energy** : The Blow Energy is a measure of the total energy that the flywheel will contain when the desired speed has been reached and prior to engaging the clutch. The units for blow energy in English units are klb-in and in SI units are N-mm. 

  * **Blow Efficiency** : The Blow Efficiency represents the fraction of the total energy that will be converted to deformation energy. The rest of the energy is absorbed through the clutch mechanism, friction, and the machine frame. There are no units for this quantity. 

  * **Moment of Inertia** : The Moment of Inertia is the moment of inertia of the flywheel. The English units of inertia are klb*in*s2 and the SI units are N-mm*s2. The mass moment of inertia for a circular disc with the Z-axis perpendicular to the center is I = 2 ET /ω2 where ET is the total energy of the flywheel, and ω is the angular velocity in radians per second.

  * **Ram Displacement or Lead screw pitch** : The Ram Displacement specifies the distance per revolution of the flywheel that the screw will advance. This helps in determining the linear velocity of the ram. The English units for Ram Displacement are inch/revolution, while the SI units are mm/revolution. If only the pitch angle and diameter of the spindle is known, the Ram Displacement can be calculated using πdsin(θt) where d is the diameter of spindle and θt is the pitch angle of the spindle.

Note:

Multiple pass can be setup for Hammer, Screw press and rolling operations using the tools menu option provided in the menu bar of pre-processor window.

**Related Topics:**

[15\. Movement Controls Settings](/docs/en/pre_processor/15_movement_controls_definition/15_movement_controls_settings/)

[15.1. Speed](/docs/en/pre_processor/15_movement_controls_definition/15_1_speed/)

[15.2. Force](/docs/en/pre_processor/15_movement_controls_definition/15_2_force/)

[15.3. Hammer](/docs/en/pre_processor/15_movement_controls_definition/15_3_hammer/)

[15.5. Mechanical press](/docs/en/pre_processor/15_movement_controls_definition/15_5_mechanical_press/)

[15.6. Hydraulic press](/docs/en/pre_processor/15_movement_controls_definition/15_6_hydraulic_press/)

[15.7. Sliding Die](/docs/en/pre_processor/15_movement_controls_definition/15_7_sliding_die/)

[15.8. Path](/docs/en/pre_processor/15_movement_controls_definition/15_8_path/)

[15.9. Rotational Movement](/docs/en/pre_processor/15_movement_controls_definition/15_9_rotational_movement/)

[15.10. Torsional movement](/docs/en/pre_processor/15_movement_controls_definition/15_10_torsional_movement/)

[15.11. Friction Welding movement](/docs/en/pre_processor/15_movement_controls_definition/15_11_friction_welding_movement/).

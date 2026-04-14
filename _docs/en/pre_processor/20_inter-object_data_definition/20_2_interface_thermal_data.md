---
lang: en
title: "20.2 Interface Thermal Data"
---

# 20.2. Interface Thermal Data

20.2.1. Interface heat transfer coefficient  
20.2.2. Relative rotation

## Interface heat transfer coefficient (IHTCOF)

**[2D, 3D]** : The interface heat transfer coefficient ([IHTCOF](/docs/en/keyword_documentation/i/ihtcof/)) specifies the coefficient of heat transfer between two objects in contact. This can be specified as a constant or a function of time or interface pressure. The interface heat transfer coefficient is generally a complex function determined by the interface pressure, amount of sliding, and interface temperature. If this data is available, it can be entered as a table.

If no data is available, values of 0.004 (English) or 11 (SI) should give reasonable results (See Fig. 20.2.1. and Fig. 20.2.2.).

##  Relative rotation (FRCROT)

**[2D]:** This ([FRCROT](/docs/en/keyword_documentation/f/frcrot/)) specifies the rotation difference between two objects about the axis of symmetry. The units are radians/second. For example, if a top die is rotating while moving downward, the interface between the top die and the billet should have the same angular speed (rad/sec) of the top die applied to it. This enables DEFORM to calculate the heat generation from friction due to rotation for processes such as inertia welding. Relative rotation can be defined as a constant or a function of time.

Modelling inertia welding is possible with DEFORM, but it is recommended to be performed using the torsional element formulation.

![]({{ '/assets/images/pre-processor/20_inter-object_data_definition/20_2_interface_thermal_data/image001.jpg' | relative_url }})

Inter object Thermal window for 2D

![]({{ '/assets/images/pre-processor/20_inter-object_data_definition/20_2_interface_thermal_data/image002.jpg' | relative_url }})

Inter object Thermal window for 3D

**Related Topics:**

[20\. Inter-Object Data Definition](/docs/en/pre_processor/20_inter-object_data_definition/20_1_friction_and_contact_criteria/)

[20.1. Friction and Contact criteria](/docs/en/pre_processor/20_inter-object_data_definition/20_1_friction_and_contact_criteria/)

[20.3. Interface Resisitivity](/docs/en/pre_processor/20_inter-object_data_definition/20_3_interface_resisitivity/)

[20.4. Tool Wear](/docs/en/pre_processor/20_inter-object_data_definition/20_4_tool_wear/)

[20.5. Rigid Contact](/docs/en/pre_processor/20_inter-object_data_definition/20_5_rigid_contact/)

---
lang: sk
title: "16.4. Fracture Properties"
---

# 16.4. Fracture properties

16.4.1. Fracture step (FRCSTP)

16.4.2. Fracture elements (FRCNEL)

16.4.3. Fracture element deletion (FRCNEL)

16.4.4 Fracture element deactivation

  
Ductile fracture of a deforming workpiece can be modelled in DEFORM. If the fracture function is turned on, material separation will be modelled for any elements which exceed a critical damage value specified in the Material Properties ![](../../../assets/Icons/Pre_icons/arrow_front.jpg)Miscellaneous![](../../../assets/Icons/Pre_icons/arrow_front.jpg)[Fracture](/docs/sk/pre_processor/10_Material_Data/10_12_Miscellaneous_Data/10_12_1_Fracture_Models/) tab. This feature is useful for modelling shearing and blanking, machining, fracture of deformable installation fasteners (pop rivets) and other applications.

**[2D]:****Fracture elements deletion** is modelled by deleting any elements which exceed the critical damage value.

Therefore, an extremely fine mesh should be used in any region where fracture is expected to limit volume loss. The FEM simulation is temporarily stopped to perform element deletion. The stopping may be triggered by a given fracture steps (see Fig. 16.4.1.) or whenever the damage value in a specified number of elements exceeds the critical value.

**Fracture element deactivation** is a new method to study crack propagation. It will deactivate an element instead of deleting it when its damage reaches the critical value of its material (See Fig. 16.4.2.).

**[3D]** : To activate fracture elements deletion type, user needs select**Fracture element deletion** type from Fracture pulldown ([FRCNEL](/docs/sk/Keyword_Documentation/F/FRCNEL/)) field (see Fig. 16.4.1.) This will initiate element deletion for elements with fracture value more than critical value defined in material fracture/damage models during remeshing procedures. Damage model and critical damage factor defined in the material data are important data needed to activate this feature. For an overview of fracture, please refer [3D Fracture.](/docs/sk/Applications/55_Applications/55_Fracture/3D_Fracture/)

**Fracture element deactivation** is a new method to study crack propagation. It will deactivate an element instead of deleting it when its damage reaches the critical value of its material (See Fig. 16.4.2.).

![](../../../assets/Images/Pre-Processor/16_Object_Properties/16_4_Fracture_Properties/16_4_Image001.jpg)

Fracture Element deletion type

![](../../../assets/Images/Pre-Processor/16_Object_Properties/16_4_Fracture_Properties/16_4_Image002.jpg)

Fracture element deactivation type

## Fracture step ([FRCSTP](/docs/sk/Keyword_Documentation/F/FRCSTP/)) [2D]

The step (**[FRCSTP](/docs/sk/Keyword_Documentation/F/FRCSTP/))** interval at which the simulation should be stopped to perform element deletion. If no elements are above the critical damage value, none will be deleted.

## Fracture elements deletion ([FRCNEL](/docs/sk/Keyword_Documentation/F/FRCNEL/)) [2D]

The number of elements that must be above the critical damage value for the simulation to be stopped to perform element deletion. A typical value is around 4.

## Fracture element deletion ([FRCNEL](/docs/sk/Keyword_Documentation/F/FRCNEL/)) [3D]

This option will initiate element deletion for elements with fracture value more than critical value defined in material fracture/damage models during remeshing procedures.

Generally, fracture element deletion will be used for crack propagation study in DEFORM system. Due to the difficulty in brick remeshing, fracture element deletion currently does not support 3D brick mesh. 

## Fracture element deactivation [2D, 3D]

Fracture element deactivation is a new method to study crack propagation. It will deactivate an element instead of deleting it when its damage reaches the critical value of its material. It allows simulation to continue without remeshing or with less remeshing in forming processes. Fracture element deactivation can support 3D brick mesh, 3D tetrahedral mesh and 2D mesh to predict crack onset & propagation.

**Related Topics:**

[16\. Object properties](/docs/sk/pre_processor/16_object_properties/16_object_properties/)

[16.1. Deformation properties](/docs/sk/pre_processor/16_object_properties/16_1_deformation_properties/)

[16.2. Thermal properties](/docs/sk/pre_processor/16_object_properties/16_2_thermal_properties/)

[16.3. Reference](/docs/sk/pre_processor/16_object_properties/16_3_Reference/)

[16.5. Hardness Properties](/docs/sk/pre_processor/16_object_properties/16_5_hardness_properties/)

[16.6. Heating Properties](/docs/sk/pre_processor/16_object_properties/16_6_heating_properties/)

[16.7. Symmetry Properties](/docs/sk/pre_processor/16_object_properties/16_7_symmetry_properties/)

[16.8. Body Force](/docs/sk/pre_processor/16_object_properties/16_8_body_force/)

[16.9. RSE](/docs/sk/pre_processor/16_object_properties/16_9_rse/)

[16.10. User](/docs/sk/pre_processor/16_object_properties/16_10_user/)

[Material Fracture/damage models](/docs/sk/pre_processor/10_Material_Data/10_12_Miscellaneous_Data/10_12_1_Fracture_Models/)

[Applications - 3D Fracture](/docs/sk/Applications/55_Applications/55_Fracture/3D_Fracture/)

---
lang: en
title: "16.8. Body Force"
---

# 16.8. Body Force

The influence of gravity can be considered in the solution by activating the gravity body force option. The body force and direction of gravity are specified through the inputs shown in Fig. 16.8.1 and Fig. 16.8.2.

The centrifugal force acting on a rotating body will be considered when the centrifugal force check box is activated.

When running simulations involving a body force, the user must define mass density (Section [10.3.4. Mass density]({{ '/docs/en/pre_processor/10_material_data/10_3_thermal_data/10_3_thermal_data/' | relative_url }}#Mass_Density) )and apply boundary condition constraints. The boundary conditions must sufficiently prevent the part from gross rigid body motion. The free distortion boundary condition feature (Section [14.2.1. Velocity BCC - Free distorsion BCC]({{ '/docs/en/pre_processor/14_boundary_conditions/14_2_deformation_boundary_conditions/' | relative_url }}#Free_Distortion_BCC) ) is designed to assist the user in this task, when necessary.

![]({{ '/assets/images/pre-processor/16_object_properties/16_8_body_force/16_8_image001.jpg' | relative_url }})

2D Body Force Object properties window

![]({{ '/assets/images/pre-processor/16_object_properties/16_8_body_force/16_8_image002.jpg' | relative_url }})

3D Body Force Object properties window

**Related Topics:**

[16\. Object properties]({{ '/docs/en/pre_processor/16_object_properties/16_object_properties/' | relative_url }})

[16.1. Deformation properties]({{ '/docs/en/pre_processor/16_object_properties/16_1_deformation_properties/' | relative_url }})

[16.2. Thermal properties]({{ '/docs/en/pre_processor/16_object_properties/16_2_thermal_properties/' | relative_url }})

[16.3. Reference]({{ '/docs/en/pre_processor/16_object_properties/16_3_Reference/' | relative_url }})

[16.4. Fracture Properties]({{ '/docs/en/pre_processor/16_object_properties/16_4_Fracture_properties/' | relative_url }})

[16.5. Hardness Properties]({{ '/docs/en/pre_processor/16_object_properties/16_5_hardness_properties/' | relative_url }})

[16.6. Heating Properties]({{ '/docs/en/pre_processor/16_object_properties/16_6_heating_properties/' | relative_url }})

[16.7. Symmetry Properties]({{ '/docs/en/pre_processor/16_object_properties/16_7_symmetry_properties/' | relative_url }})

[16.9. RSE]({{ '/docs/en/pre_processor/16_object_properties/16_9_rse/' | relative_url }})

[16.10. User]({{ '/docs/en/pre_processor/16_object_properties/16_10_user/' | relative_url }})

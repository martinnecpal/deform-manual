---
lang: en
title: "16.7. Symmetry Properties"
---

# 16.7. Symmetry Properties

**[3D]** : This boundary condition allows the user to match the velocity of the nodes of any surface of a body to the nodes of any other surface on the same body. The purpose of this is to model the more general case where rotational motion occurs during the forming of a part such as in the case of the forging of a helical gear. The manner in which to setup a rotational symmetry problem is to go to the Object, Properties window for the object and select the Symmetry tab then set the following values: (See Fig. 16.7.1.).

  * **Angle** : The angle of the part simulated in units of degrees. For example, 180 means that only half the part is simulated and 90 means one quarter of the part is simulated.
  * **Centre** : A point on the centreline about which the deformation occurs. The format is in global (x, y, z) coordinates.
  * **Axis** : The vector through which the centreline is parallel to. The format is in (x, y, z) coordinates. For example, if the user wants to specify a vector parallel to the z axis, the value of (0, 0, 1) should be typed in.

The second item the user needs to specify is the surfaces which have the rotational symmetry relationship to one another. The manner in which this is done is to place contact boundary conditions on face which obeys the right-hand rule. The boundary condition can be applied under the Objects, boundary conditions window using the advanced boundary conditions. The user needs to select the face which obeys the right-hand rule and apply self-contact conditions. This will allow the simulation engine to know which faces the rotational symmetry condition applies to.

![](../../../assets/Images/Pre-Processor/16_Object_Properties/16_7_Symmetry_Properties/16_7_Image001.jpg)

Rotational Symmetry Object properties window

**Related Topics:**

[16\. Object properties](/docs/en/pre_processor/16_object_properties/16_object_properties/)

[16.1. Deformation properties](/docs/en/pre_processor/16_object_properties/16_1_deformation_properties/)

[16.2. Thermal properties](/docs/en/pre_processor/16_object_properties/16_2_thermal_properties/)

[16.3. Reference](/docs/en/pre_processor/16_object_properties/16_3_Reference/)

[16.4. Fracture Properties](/docs/en/pre_processor/16_object_properties/16_4_Fracture_properties/)

[16.5. Hardness Properties](/docs/en/pre_processor/16_object_properties/16_5_hardness_properties/)

[16.6. Heating Properties](/docs/en/pre_processor/16_object_properties/16_6_heating_properties/)

[16.8. Body Force](/docs/en/pre_processor/16_object_properties/16_8_body_force/)

[16.9. RSE](/docs/en/pre_processor/16_object_properties/16_9_rse/)

[16.10. User](/docs/en/pre_processor/16_object_properties/16_10_user/)

[3D-Geometry symmetry surface definition](../12_Geometry_Modelling/12_3_3d_geometry_data_defining.htm#Parallel_symmetry_planes)

[3D-Mesh symmetry BCC definition](/docs/en/pre_processor/14_Boundary_Conditions/14_1_symmetry_boundary_conditions/)

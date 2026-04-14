---
lang: sk
title: "1.7. Geometry Representation"
---

# 1.7. Geometry Representation

![]({{ '/assets/images/about_deform/1_7_geometry_representation/1_7_image001.jpg' | relative_url }})

Geometry representation examples; (a) Axisymmetric (b) Torsion (c) Plane stress and Plane strain

DEFORM simulations can be run either as two dimensional (2D) or three dimensional (3D) models. In general, 2D models are smaller, easier to set up, and run more quickly than 3D models. Frequently, the added detail of a 3D model is not worth the additional time required over a 2D simulation if the process can reasonably be represented in 2D.

There are four 2D-geometry representations- axisymmetric, plane strain, torsion and plane stress. Axisymmetric geometries assume that the geometry of every plane radiating out from the centerline is identical. Plane strain and plane stress assumes that there is no material flow in the out of plane direction and that flow in every plane parallel to the section modelled is identical. Torsion models are axisymmetric models characterizing a twist or screw. Fig. 1.7.1. illustrates axisymmetric, torsion, plane strain and plane stress models.

Objects that are closely approximated by axisymmetric or plane strain models can also be modelled in 2D by neglecting minor variations. For example, if the head shape is not critical a hex head bolt can be modelled as axisymmetric by defining a head radius which maintains constant volume (radius = 0.525*(distance across flats)). A gradually tapering part such as a turbine blade can be modelled by modelling several plane strain sections.

![]({{ '/assets/images/about_deform/1_7_geometry_representation/1_7_image002.jpg' | relative_url }})

Buckling

Buckling of cylindrical parts is a fully three dimensional process, and must be modelled as such if such behavior is expected. An axisymmetric simulation will not show buckling, even if it will occur in the actual process (See Fig. 1.7.2.). Parts which cannot be simplified to 2D must be modelled as 3D.

**Related Topics:**

[2D Geometry Types](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#9.1.2._Geometry_type_\(GEOTYP\)_\[2D\])

[2D Plane Strain](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#Plane_strain)

[2D Geo Edit Tool](/docs/sk/pre_processor/12_geometry_modelling/12_2_2d_geometry_editing/)

[3D Geo Tool Manual](/docs/sk/pre_processor/12_geometry_modelling/12_4_3d_geometry_data_editing_geo_tooll/)

[Lab 01 Geometry Manipulation](/docs/sk/labs/basic_labs/2d_labs/lab_01_geometry_manipulation_and_uniform_mesh/)

[Lab 02 Geometry Correction](/docs/sk/labs/basic_labs/2d_labs/lab_02_geometry_correction/)

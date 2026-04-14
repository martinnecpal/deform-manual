---
lang: en
title: "MGUSER (2D)"
---

# MGUSER

|  (Object data - 2D)  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

MGUSER Object, Narea, Ndata, Density, VelocityX, VelocityY, SpdType

Point(1), X(1), Y(1)

: : :

Point(Ndata), X(Ndata), Y(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
Narea |  Index of user defined area (1 to N) |  0.0  
Ndata |  Number of points to define area |  None  
Density |  Mesh Density of ith point in defined area |  0.0  
VelocityX |  X component of window velocity |  0.0  
VelocityY |  Y component of window velocity |  0.0  
SpdType |  Speed type: =******0** or **1** : constant; **-n:** following object **n** |  0.0  
Point(i) |  Index of ith points describing area (1 to Ndata) |  None  
X(i) |  X coordinate of ith point in defined area |  0.0  
Y(i) |  Y coordinate of ith point in defined area |  0.0  
  
DEFINITION  
---  
MGUSER specifies an area in space which will move with and object during deformation. This area has a mesh density definition applied to it and will cause the area to be meshed with an appropriate mesh density.  
  
REMARKS  
---  
MGUSER is can be used to define multiple windows (1 to Narea) which will cause any area of the defined object which falls within the window to be meshed with the defined mesh density Density. Each window is defined by a set of 1 to Ndata X/Y coordinate pairs. The window must be defined in the counter-clockwise direction like all objects in DEFORM®;. The window will have a velocity assigned to it by the variables VelocityX and VelocityY. These will specify a constant velocity in the direction assigned through the velocity. Applicable object types: [Rigid](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.5._Rigid), [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
Mesh: [Mesh density Window](../../pre_processor/13_mesh_generation/13_1_2d_mesh_generation.htm#13.1.6._Mesh_density_windows) Keywords: [MGNELM](/docs/en/keyword_documentation/m/mgnelm/), [MGGRID](/docs/en/keyword_documentation/m/mggrid/), [MGERR](/docs/en/keyword_documentation/m/mgerr/), [MGTELM](/docs/en/keyword_documentation/m/mgtelm/), [MGSIZR](/docs/en/keyword_documentation/m/mgsizr/), [MGWCUV](/docs/en/keyword_documentation/m/mgwcuv/), [MGWTMP](/docs/en/keyword_documentation/m/mgwtmp/), [MGWSTN](/docs/en/keyword_documentation/m/mgwstn/), [MGWSTR](/docs/en/keyword_documentation/m/mgwstr/)

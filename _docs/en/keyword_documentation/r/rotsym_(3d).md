---
lang: en
title: "ROTSYM (3D)"
---

# ROTSYM

|  (Object data - 3D only)  
---|---  
_Update History:_ V11 - Periodic boundary condition has been added. |  Last updated on : 13-08-2013  
  
* * *

ROTSYM Object, Angle 

VectorX, VectorY, VectorZ  
PointX, PointY, PointZ 

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Angle |  Angle of rotational symmetry |  None  
VectorX |  Component of X vector |  None  
VectorY |  Component of Y vector |  None  
VectorZ |  Component of Z vector |  None  
PointX |  X coordinate on rotational axis |  None  
PointY |  Y coordinate on rotational axis |  None  
PointZ |  Z coordinate on rotational axis |  None  
  
DEFINITION  
---  
ROTSYM specifies the conditions for a rotational symmetry condition. Rotational symmetry is a boundary condition in which symmetry is a special case. It is a matching of the velocity on one (master) surface of a body to another (slave) surface on the same body. As a special condition, rotational symmetry condition can be used to specify periodic symmetry condition on the master and slave surfaces. For periodic boundary condition (PBC), it is required to specify a master to slave direction vector with having the point set to (0, 0, 0). The angle is required to set 360 degrees.   
  
REMARKS  
---  
It is recommended that if users use this, that the meshes on the two sides have identical topology. If not, a fine mesh is recommended. Applicable object types: [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous)  
  
RELATED TOPICS  
---  
Geometry: [Symmetry surface](../../pre_processor/12_geometry_modelling/12_3_3d_geometry_data_defining.htm#Specifying_Rotational_Symmetry), Boundary Constraints: [Symmetry BCC](/docs/en/pre_processor/14_boundary_conditions/14_1_symmetry_boundary_conditions/)

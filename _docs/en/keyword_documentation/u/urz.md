---
lang: en
title: "URZ (2D)"
---

# URZ

|  (Object data – 2D)  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

URZ Object, Ndata, DefXVel, DefYVel

Node(1), XSpeed(1), YSpeed(1)

: : :

Node(Ndata), XSpeed(Ndata), YSpeed(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
Ndata |  Number of node/speed data pairs |  None  
DefXSpeed |  Default nodal speed in X of all nodes not listed in the node/speed pairs. |  0  
DefYSpeed |  Default nodal speed in Y of all nodes not listed in the node/speed pairs. |  0  
Node(i) |  Node number of ith data pair |  None  
XSpeed(i) |  Nodal speed in X of ith data pair |  0.0  
YSpeed(i) |  Nodal speed in Y of ith data pair |  0.0  
  
DEFINITION  
---  
URZ specifies the nodal speed of each node.  
  
REMARKS  
---  
The nodal speed is defined in the local coordinate system specified in BCCANG. Typically, the speed constraint is used for limiting translational degrees of freedom along an axis of symmetry. This is achieved by specifying a speed of 0.0 in the direction perpendicular to the axis of symmetry. Most process related object motion, such as die speed, can be specified with movement control constraints (MVOCTL). However, speed constraints are occasionally used for operations which require an object to be pulled through a set of dies, as can be the case with drawing and extrusion processes. Applicable object types: [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
[Boundary Constraints](/docs/en/pre_processor/14_boundary_conditions/14_boundary_conditions/): [Deformation](/docs/en/pre_processor/14_boundary_conditions/14_2_deformation_boundary_conditions/) \- [Velocity](../../pre_processor/14_boundary_conditions/14_2_deformation_boundary_conditions.htm#14.2.1._Velocity_BCC) Keywords: [BCCANG](/docs/en/keyword_documentation/b/bccang/),[BCCDEF(2D)](/docs/en/keyword_documentation/b/bccdef/),[BCCDEF(3D)](/docs/en/keyword_documentation/b/bccdef_3d/), [MOVCTL(2D)](../m/movctl_\(2d\).htm), [MOVCTL(3D)](../m/movctl_\(3d\).htm)

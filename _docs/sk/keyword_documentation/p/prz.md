---
lang: sk
title: "PRZ (2D)"
---

# PRZ

|  (Object data- 2D)  
---|---  
|  Last updated on : 09-08-2013  
  
* * *

PRZ Object, Ndata, DefPressure

Node(1), TanPressure(1) NorPressure(1)

: : :

Node(Ndata), TanPressure(Ndata) NorPressure(NData)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Ndata |  Number of node/traction data pairs |  None  
DefPressure |  Default value of distributed nodal traction of all nodes not listed in the node/traction pairs with deformation boundary constraint code 2. |   
TanPressure |  Tangential Pressure |  None  
NorPressure |  Normal Pressure |  None  
Node(i) |  Node number of ith data pair |  None  
Temp(i) |  Nodal traction of ith data pair |  0.0  
  
DEFINITION  
---  
PRZ maintains a specified normal pressure or shear traction across the face of the elements lying between the selected boundary nodes.  
  
REMARKS  
---  
Pressure is defined as force per unit area. The pressure is assumed to be linear between adjacent nodes. The pressure constraint will be applied to the element faces lying between the selected boundary nodes. The pressure direction may be specified as normal or shear. Positive normal pressure applies tension to the element faces. Positive shear traction is defined by the right hand rule. If no value is specified for DefPressure, it is assumed to be zero. Nodal pressure values may only be applied to nodes which have deformation boundary constraint code 2 (BCCDEF). Nodal pressure may be specified as a function of time with keyword BCCFNC. The Pressure uses the local coordinate system.  
  
RELATED TOPICS  
---  
[Boundary Constraints](/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/): Deformation- Pressure, [Object Nodal Data](/docs/sk/pre_processor/17_object_data_initialization/17_1_node_data_window/): Deformation- Pressure Keywords: [BCCDEF (2D)](/docs/sk/keyword_documentation/b/bccdef/), [BCCDEF (3D)](/docs/sk/keyword_documentation/b/bccdef_3d/), [BCCFNC](/docs/sk/keyword_documentation/b/bccfnc/)

---
lang: sk
title: "BCCANG (2D3D)"
---

# BCCANG

|  (Object Data)  
---|---  
|  Last updated on : 29-07-2013  
  
* * *

BCCANG Object, Ndata, DefAngle  
Node(1), Angle(1)  
: :  
Node(Ndata), Angle(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Ndata |  Number of node/angle pairs |  None  
DefAngle |  Default boundary constraint angle (degrees) of all nodes not listed in the node/angle pairs |  0  
Node(i) |  Node of ith data pair |  None  
Angle(i) |    
Boundary constraint angle (degrees) of ith data pair |  None  
  
DEFINITION  
---  
BCCANG specifies the angle at which nodal and force boundary constraints (URZ and FRZ) will be applied for each node.  
  
REMARKS  
---  
The boundary constraint angle is defined by the angle measured from the X axis of the global coordinate system to the X' axis of the local coordinate system counter clockwise. If no value is specified for DefAngle, it is assumed to be zero. Applicable object types: [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
[Boundary constraints](/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/) Keywords: [URZ (2D)](/docs/sk/keyword_documentation/u/urz/), [FRZ (2D)](/docs/sk/keyword_documentation/f/frz/), [URZ (3D)](/docs/sk/keyword_documentation/u/urz_3d/), [FRZ (3D)](/docs/sk/keyword_documentation/f/frz_3d/),

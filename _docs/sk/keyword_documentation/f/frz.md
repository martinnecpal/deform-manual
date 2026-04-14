---
lang: sk
title: "FRZ (2D)"
---

# FRZ

|  (Object data - 2D)  
---|---  
_Update History:_ (New definition has been introduced in v10.0) |  Last updated on : 06-08-2013  
  
* * *

FRZ Object, Ndata, DefXForce, DefYForce

Node(1), XForce(1), YForce(1)

: : :

Node(Ndata), XForce(Ndata), YForce(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Ndata |  Number of node/force data set |  None  
DefXForce |  Default nodal force in X for all nodes not listed in the node/force sets |  0.0  
DefYForce |  Default nodal force in Y for all nodes not listed in the node/force sets |  0.0  
Node(i) |  Node number of ith data set |  None  
XForce(i) |  Nodal force in X of ith data set |  0.0  
YForce(i) |  Nodal force in Y of ith data set |  0.0  
  
DEFINITION  
---  
FRZ specifies the value of the constant nodal force at individual nodes.  
  
REMARKS  
---  
FRZ can only be applied to nodes which have been specified as having a nodal force boundary constraint code (BCCDEF) and as having a constant function type (BCCDFN). Nodal forces are applied in the local coordinate system specified by BCCANG. If no value is specified for DefXForce and DefYForce, they will be assumed to be zero. Applicable object types: [Rigid](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.5._Rigid), [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
[Boundary constraints](/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/) Keywords: [BCCDEF (2D)](/docs/sk/keyword_documentation/b/bccdef/), [BCCDEF (3D)](/docs/sk/keyword_documentation/b/bccdef_3d/), [BCCDFN (2D)](/docs/sk/keyword_documentation/b/bccdfn/), [BCCDFN (3D)](/docs/sk/keyword_documentation/b/bccdfn_3d/), [BCCFNC](/docs/sk/keyword_documentation/b/bccfnc/), [BCCANG](/docs/sk/keyword_documentation/b/bccang/)

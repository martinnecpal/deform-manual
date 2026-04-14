---
lang: en
title: "BCCDEF (2D)"
---

# BCCDEF

|  (Object Data - 2D)  
---|---  
|  Last updated on : 29-07-2013  
  
* * *

BCCDEF Object, Ndata, Default  
Node(1), BCX(1), BCY(1)  
: : :  
Node(Ndata), BCX(Ndata), BCY(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
Ndata |  Number of node/boundary constraint data sets |  None  
DefBCX |  Default deformation boundary constraint code in X of all nodes not listed in node/boundary constraint data sets |  None  
DefBCY |  Default deformation boundary constraint code in Y of all nodes not listed in node/boundary constraint data sets |  None  
Node(i) |  Node of ith data set |  None  
BCX(i) |  Deformation boundary constraint code in X of ith data set |  None  
BCY(i) |  Deformation boundary constraint code in Y of ith data set |  None  
  
DEFINITION  
---  
BCCDEF specifies the deformation boundary constraint in X and Y.  
  
REMARKS  
---  
The boundary constraint code (bcc) options are: 0 nodal force (This is the Default value for all nodes) 1 nodal velocity 2 nodal traction 3 nodal movement control 4 beginning surface 5 ending surface -n nodal contact with object n For bcc = 0, the value of the nodal force should be specified with keyword FRZ or BCCFNC. For bcc = 1, the value of the nodal velocity should be specified with keyword URZ or BCCFNC. For bcc = 2, the value of the nodal traction should be specified with keyword PRZ or BCCFNC. Nodal traction can only be applied to boundary nodes. For bcc = 0, 1, or 2, keyword BCCDFN is used to specify if the nodal values or specified as a constant or as a function of time. For bcc = 3, the type of movement control should be specified with keyword MOVCTL. For bcc = -n, the node is considered to stick to object n and will move with object n until separation occurs. The contact direction does not matter. Contact boundary constraints are updated by DEFORM during the simulation to account for nodal contact and separation associated with the object's deformation. Contact constraints are only applied to slave objects. The direction of the boundary constraint code (BCX or BCY) refers to X and Y in the local coordinate system defined by BCCANG or the global coordinate system if no local coordinate system has been defined. Each node may only be assigned one deformation boundary constraint code in each direction. If no values are provided for DefBCX and DefBCY, it is assumed that all nodes which are not specified in the node/boundary constraint code pairs have no boundary constraint associated with them. Applicable object types: [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
[Boundary constraints](/docs/en/pre_processor/14_boundary_conditions/14_boundary_conditions/), [Inter-object contact](/docs/en/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/) Keywords: [BCCDFN(2D)](/docs/en/keyword_documentation/b/bccdfn/) [BCCDFN(3D)](/docs/en/keyword_documentation/b/bccdfn_3d/), [BCCFNC](/docs/en/keyword_documentation/b/bccfnc/), [PRZ(2D)](/docs/en/keyword_documentation/p/prz/), [PRZ(3D](/docs/en/keyword_documentation/p/prz_3d/)), [FRZ(2D)](/docs/en/keyword_documentation/f/frz/), [FRZ(3D)](/docs/en/keyword_documentation/f/frz_3d/) [URZ(2D)](/docs/en/keyword_documentation/u/urz/), [URZ(3D)](/docs/en/keyword_documentation/u/urz_3d/), [MOVCTL (2D)](../m/movctl_\(2d\).htm), [MOVCTL (3D)](../m/movctl_\(3d\).htm).

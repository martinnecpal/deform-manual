---
lang: sk
title: "BCCDFN (2D)"
---

# BCCDFN

|  (Object Data - 2D)  
---|---  
|  Last updated on : 29-07-2013  
  
* * *

BCCDFN Object, Ndata, Default  
Node(1), FtypeX(1), FtypeY(1)  
: : :  
Node(Ndata), FtypeX(Ndata), FtypeY(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
Ndata |  Number of node/boundary constraint data sets |  None  
DefFtypeX |  Default function type for deformation boundary constraints in X of all nodes not listed in the Node/Ftype data sets |  0  
DefFtypeY |  Default function type for deformation boundary constraints in Y of all nodes not listed in the Node/Ftype data sets |  0  
Node(i) |  Node of ith data set |  None  
FtypeX(i) |  Function type for deformation boundary constraint in X of ith data set |  None  
FtypeY(i) |  Function type for deformation boundary constraint in Y of ith data set |  None  
  
DEFINITION  
---  
BCCDFN specifies if the value of a deformation boundary constraint (nodal velocity, force, or traction) associated with a particular node is to be specified as a constant or as a set of time/nodal value data.  
  
REMARKS  
---  
The function type (Ftype) options are: 0 no function defined n function number (specified in BCCFNC) The type of deformation constraint (nodal velocity, force, or traction) associated with a particular node is specified with keyword BCCDEF. If Ftype = 1, the function definition should be specified with keyword BCCFNC. If Ftype = 2, the constant nodal value should be specified with URZ, FRZ, or PRZ. The direction of the function type (FtypeX or FtypeY) refers to X and Y in the local coordinate system defined by BCCANG or the global coordinate system if no local coordinate system has been defined. If no values are provided for DefFtypeX and DefFtypeY, it is assumed that all nodes which have deformation boundary constraint codes specified but are not included in the node/Ftype sets are to be specified as a constant. Applicable object types: [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
[Boundary constraints](/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/) Keywords: [BCCFNC](/docs/sk/keyword_documentation/b/bccfnc/), [PRZ(2D)](/docs/sk/keyword_documentation/p/prz/), [PRZ(3D](/docs/sk/keyword_documentation/p/prz_3d/)), [FRZ(2D)](/docs/sk/keyword_documentation/f/frz/), [FRZ(3D)](/docs/sk/keyword_documentation/f/frz_3d/) [URZ(2D)](/docs/sk/keyword_documentation/u/urz/), [URZ(3D),](/docs/sk/keyword_documentation/u/urz_3d/) [BCCDEF(2D),](/docs/sk/keyword_documentation/b/bccdef/) [BCCDEF(3D)](/docs/sk/keyword_documentation/b/bccdef_3d/), [BCCANG](/docs/sk/keyword_documentation/b/bccang/).

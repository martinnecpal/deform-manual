---
lang: sk
title: "BCCFNC (2D3D)"
---

# BCCFNC

|  (Object Data)  
---|---  
|  Last updated on : 29-07-2013  
  
* * *

BCCFNC Object, Fnum, Ndata  
Time(1), Value(1)  
: :  
Time(Ndata), Value(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Fnum |  Function number |  None  
Ndata |  Number of time/nodal value data pairs |  None  
Time |  Time of ith data pair |  0  
Value |  Nodal value of ith data pair |  0  
  
DEFINITION  
---  
BCCFNC is used to specify time/nodal value pairs for nodal boundary constraints. Types of nodal boundary constraints that can be specified as time/nodal value pairs include velocity, force, traction, temperature, heat, and distributed heat flux.  
  
REMARKS  
---  
BCCFNC can only be used when a node's boundary constraint function type, BCCDFN or BCCTFN, has been specified as a time/nodal value type. The type of data being specified by Value is determined by the type of boundary constraint been selected with BCCDEF or BCCTMP. For time dependent boundary constraints, when the process time lies within the time range specified in BCCFNC, linear interpolation is used to determine the corresponding boundary constraint value. When process time lies outside the time range specified in BCCFNC, linear extrapolation is used to determine the corresponding boundary constraint value. Applicable object types: [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
[Boundary constraints](/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/) Keywords: [BCCDEF(2D)](/docs/sk/keyword_documentation/b/bccdef/), [BCCDEF(3D)](/docs/sk/keyword_documentation/b/bccdef_3d/), [BCCDFN(2D)](/docs/sk/keyword_documentation/b/bccdfn/), [BCCDFN(3D)](/docs/sk/keyword_documentation/b/bccdfn_3d/), [BCCTMP](/docs/sk/keyword_documentation/b/bcctmp/), [BCCTFN](/docs/sk/keyword_documentation/b/bcctfn/).

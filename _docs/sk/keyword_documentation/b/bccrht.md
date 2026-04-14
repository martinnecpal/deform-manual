---
lang: sk
title: "BCCRHT (2D3D)"
---

# BCCRHT

|  (Object Data)  
---|---  
|  Last updated on : 29-07-2013  
  
* * *

BCCRHT Object, Ndata, DefBCRht  
Node(1), BCRht(1)  
: :  
Node(Ndata), BCRht(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Ndata |  Number of node/boundary constraint data pairs |  None  
DefBCRht |  Default resistance heating boundary constraint code of all nodes not listed in node/boundary constraint data pairs |  None  
Node(i) |  Node number of ith data pair |  None  
BCRht(i) |  Resistance heating boundary constraint code of ith data pair |  None  
  
DEFINITION  
---  
BCCRHT specifies the resistance heating boundary constraint code for individual nodes.  
  
REMARKS  
---  
The boundary constraint code (bcc) options for DefBCRht and BCRht(i) are: 0 not used 1 prescribed votage in [VOTAGE](/docs/sk/keyword_documentation/v/votage/) 2 not used 3 prescribed current in [RHTFLX](/docs/sk/keyword_documentation/r/rhtflx/) -n node is in contact with object n Applicable object types: [Rigid](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.5._Rigid), [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
[Boundary constraints](/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/), [Inter-object contact](/docs/sk/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/) Keywords: [VOTAGE](/docs/sk/keyword_documentation/v/votage/), [RHTFLX](/docs/sk/keyword_documentation/r/rhtflx/).

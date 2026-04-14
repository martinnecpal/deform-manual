---
lang: en
title: "BCCCRB (2D)"
---

# BCCCRB

|  (Object Data)  
---|---  
|  Last updated on : 23-07-2013  
  
* * *

BCCCRB Object, Ndata, DefBCAtom  
Node(1), BCAtom(1)  
: :  
Node(Ndata), BCAtom(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Ndata |  Number of node/boundary constraint data pairs |  None  
DefBCAtom |  Default diffusion boundary constraint code of all nodes not listed in node/boundary constraint data pairs |  None  
Node(i) |  Node number of ith data pair |  None  
BCAtom(i) |  Diffusion boundary constraint code of ith data pair |  None  
  
DEFINITION  
---  
BCCCRB specifies the diffusion boundary constraint code for individual nodes.  
  
REMARKS  
---  
The boundary constraint code (bcc) options for DefBCAtom and BCAtom(i) are: 0 not used 1 prescribed atom content in [DATOM](/docs/en/keyword_documentation/d/datom/) 2 diffusion with the environment 3 prescribed atom flux in [CRBFLX](/docs/en/keyword_documentation/c/crbflx/) -n node is in contact with object n Applicable object types: [Rigid](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.5._Rigid), [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
[Boundary constraints](/docs/en/pre_processor/14_boundary_conditions/14_boundary_conditions/), [Inter-object contact](/docs/en/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/) Keywords: [DATOM](/docs/en/keyword_documentation/d/datom/), [CRBFLX](/docs/en/keyword_documentation/c/crbflx/)

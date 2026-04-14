---
lang: sk
title: "BCCTFN (2D3D)"
---

# BCCTFN

|  (Object Data)  
---|---  
|  Last updated on : 29-07-2013  
  
* * *

BCCTFN Object, Ndata, DefType  
Node(1), Ftype(1)  
: :  
Node(Ndata), Ftype(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
Ndata |  Number of node/boundary constraint data pairs |  None  
DefFtype |  Default function type for heat transfer boundary constraints of all nodes not listed in the Node/Ftype data pairs |  0  
Node(i) |  Node number of ith data pair |  None  
Ftype(i) |  Function type for heat transfer boundary constraint of ith data pair |  None  
  
DEFINITION  
---  
BCCTFN specifies if the value of a heat transfer boundary constraint (nodal temperature, heat, or heat flux) associated with a particular node is to be specified as a constant or as a set of time/nodal value data pairs.  
  
REMARKS  
---  
The function type (Ftype) options are: 0 no function n function number (specified in BCCFNC) The type of heat transfer boundary constraint (nodal temperature, heat, or heat flux) associated with a particular node is specified with keyword BCCTMP. If Ftype = 1, the function definition should be specified with keyword BCCFNC. If Ftype = 2, the constant nodal value should be specified with NDTMP, NDHEAT, or NDFLUX. If no values are provided for DefFtype, it is assumed that all nodes which have heat transfer boundary constraint codes specified but are not included in the node/Ftype pairs are to be specified as a constant. Applicable object types: Elastic, Plastic, Elastoplastic, and Porous.  
  
RELATED TOPICS  
---  
[Boundary constraints](/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/), [Inter-object contact](/docs/sk/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/) Keywords: [BCCTMP](/docs/sk/keyword_documentation/b/bcctmp/), [BCCFNC](/docs/sk/keyword_documentation/b/bccfnc/), [NDTMP(2D)](/docs/sk/keyword_documentation/n/ndtmp/), [NDTMP(3D)](/docs/sk/keyword_documentation/n/ndtmp_3d/), [NDHEAT](/docs/sk/keyword_documentation/n/ndheat/), [NDFLUX](/docs/sk/keyword_documentation/n/ndflux/)

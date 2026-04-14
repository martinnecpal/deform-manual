---
lang: en
title: "RGDCNT (2D3D)"
---

# RGDCNT

|  (Inter-Object data)  
---|---  
|  Last updated on : 09-08-2013  
  
* * *

RGDCNT Object1, Object2, Method, MstRefNd, SlvRefNd, DistTol

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object1 |  Object number of first object |  None  
Object2 |  Object number of second object |  None  
Method |  Contact calculation method = **0** None = **1 - 4** Distance between reference points less than the tolerance (**1** : Total distance; **2** : X distance; **3** : Y distance; **4** : Z distance) = **5** Automatic detection without reference points (not implemented) |  0  
MstRefNd |  Reference point for the Master object (geometry node #) |   
SlvRefNd |  Reference point for the Slave object (geometry node #) |   
DistTol |  Distance tolerance |   
  
DEFINITION  
---  
RGDCNT specifies the rigid-to-rigid contact method.  
  
REMARKS  
---  
This keyword should be used in conjunction with CNTACT, which specifies the inter-object relationship. Applicable object types: [Rigid](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.5._Rigid).  
  
RELATED TOPICS  
---  
[Inter- Object Data](/docs/en/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/): [Rigid Contact](/docs/en/pre_processor/20_inter-object_data_definition/20_5_rigid_contact/) Keywords: [CNTACT (2D)](/docs/en/keyword_documentation/c/cntact/), [CNTACT (3D)](/docs/en/keyword_documentation/c/cntact_3d/)

---
lang: sk
title: "TXTURE (2D3D)"
---

# TXTURE

|  (Material data)  
---|---  
_Update History:_ V11 - TXTURE has been introduced. |  Last updated on : 24-07-2013  
  
* * *

TXTURE Material, CrystalType, TextureType, TextureMeshType

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Material |  Material Number |  None  
CrystalType  |  Crystal Type = **0** Not defined = **1** Body Centered Cubic (BCC) = **2** Face Centered Cubic (FCC) = **3** Hexagonal Close Packed (HCP) |  0  
TextureType |  Texture Representation Type = **1** Rodrigues space = **2** Euler angles (not implemented) |   
TextureMeshType |  Texture Mesh Type In Rodrigues space:  For BCC and FCC: = 1 Mesh 1 (26 nodes, 36 elements, 7 independent nodes) = 2 Mesh 2 (111 nodes, 288 elements, 50 independent nodes) = 3 Mesh 3 (605 nodes, 2304 elements, 388 independent nodes) = 4 Mesh 4 (3897 nodes, 18432 elements, 3080 independent nodes) For HCP: = 1 Mesh 1 (31 nodes, 56 elements, 10 independent nodes) = 2 Mesh 2 (145 nodes, 448 elements, 76 independent nodes) = 3 Mesh 3 (849 nodes, 3584 elements, 600 independent nodes) = 4 Mesh 4 (5729 nodes, 28672 elements, 4784 independent nodes) |   
  
DEFINITION  
---  
TXTURE specifies the basic information for texture representation of a material.  
  
REMARKS  
---  
Applicable object types: [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic)  
  
RELATED TOPICS  
---  
[Material Data](/docs/sk/pre_processor/10_material_data/10_material_data/) Keywords: [TXTODF](/docs/sk/keyword_documentation/t/txtodf/)

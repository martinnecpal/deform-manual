---
lang: sk
title: "FRCFAI (3D)"
---

# FRCFAI

|  (Inter-object data – 3D)  
---|---  
_Update History:_ V11.1 – FRCFAI is not yet implemented in v11.1 (To be implemented in v11sp1) V12.1.1 – FRCFAI keyword definition has been extended. |  Last updated on : 27-09-2023  
  
* * *

FRCFAI MasterObjNo, SlaveObjNo, AnisoType

Sx, Sy, Sz

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
MasterObjNo |  Object number of master object |  None  
SlaveObjNo |  Object number of salve object |  None  
AnsioType |  Type of coordinate system **0** \- Isotropic **  
1** \- Cartesian (coefficient)**  
2** \- Cylindrical (coefficient)**  
3** \- Cartesian (scale factor)**  
4** \- Cylindrical (scale factor) |   
Sx |  Coefficient (or scale factor) in the x-dir. |  None  
Sy |  Coefficient (or scale factor) in the y-dir. |  None  
Sz |  Coefficient (or scale factor) in the z-dir. |  None  
  
DEFINITION  
---  
FRCFAI specifies anisotropic friction in global coordinate system.  
  
REMARKS  
---  
This keyword allows user to model anisotropic friction behavior for Cartesian or Cylindrical coordinate systems. When the tool surface has a serration/texture which makes a directional friction behavior, this can be modeled by using this keyword.   
  
RELATED TOPICS  
---  
Related keywords: [FRCFAC](/docs/sk/keyword_documentation/f/frcfac/)

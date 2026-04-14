---
lang: en
title: "LATENT (2D3D)"
---

# LATENT

|  (Simulation control)  
---|---  
_Update History:_ V11.1 - LATENT has been re-defined. |  Last updated on : 07-08-2013  
  
* * *

LATENT i

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
i |  Parameter deciding whether solution method for Solid/Liquid phase transformation with latent heat is considered i = **0** Enthalpy method. i = **1** Source Based method. |  0  
  
DEFINITION  
---  
LATENT indicates the solution method applied for Solid/Liquid latent heat calculation during heat transfer calculation.  
  
REMARKS  
---  
Source Based method is not recommended for pure material, which doesn’t has Liquid/Solid mushy zone.  
  
RELATED TOPICS  
---  
[Inter-Material Data](/docs/en/pre_processor/10_material_data/10_9_transformation_data/10_9_transformation_data/): [Latent Heat](../../pre_processor/10_material_data/10_9_transformation_data/10_9_transformation_data.htm#Latent_Heat) Keyword: [LTHEAT](/docs/en/keyword_documentation/l/ltheat/)

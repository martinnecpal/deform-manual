---
lang: en
title: "ELPSOL (2D3D)"
---

# ELPSOL

|  (Object Data)  
---|---  
|  Last updated on : 30-07-2013  
  
* * *

ELPSOL Obj, Type

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Obj |  Object number |  None  
Type |  **0** = Uses rigid-plastic solution for initial guess for every step **1** = Uses elastic solution for initial guess for every step **2** = Uses previous step solution (elasto-plastic) for initial guess for every step except for the first step, which uses rigid-plastic solution for the initial guess. |  None  
  
DEFINITION  
---  
ELPSOL specifies initial guess for elasto-plastic problems.  
  
REMARKS  
---  
Type 0 should be used for objects that will undergo large deformations, while type 1 should be used for objects that undergo small deformations. Type 0 or type 1 should be used when there are many new nodal contacts or separations between objects. Type 2 should be used for small deformation change from step to step. Applicable Simulation Modules: Deformation Applicable Simulation Modes: Deformation Applicable Object Types: [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic)  
  
RELATED TOPICS  
---  
[Object Properties](/docs/en/pre_processor/16_object_properties/16_object_properties/): [Deformation](/docs/en/pre_processor/16_object_properties/16_1_deformation_properties/)

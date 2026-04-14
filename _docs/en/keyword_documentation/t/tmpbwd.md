---
lang: en
title: "TMPBWD (2D3D)"
---

# TMPBWD

|  (Simulation control)  
---|---  
|  Last updated on : 01-08-2013  
  
* * *

TMPBWD Flag

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Flag |  Flag indicating if profile optimization will be performed during heat transfer simulations. = **0** Profile optimization not performed = **1** Profile optimization performed |  0  
  
DEFINITION  
---  
TMPBWD indicates if profile optimization will be performed during a heat transfer simulation.  
  
REMARKS  
---  
Profile optimization is used to reduce the memory storage requirements for the thermal stiffness matrix and increase computational efficiency. If Flag = 1 and the simulation mode is heat transfer, the stiffness matrix will be optimized at the beginning of the simulation. If Flag = 1 and the simulation mode is non-isothermal simulation optimization will be performed at the beginning of the simulation and at each step where there is inter-object nodal contact or separation. Thermal profile optimization is recommended for heat transfer simulations which contain multiple objects. Applicable simulation types: Heat Transfer, Non-Isothermal Deformation  
  
RELATED TOPICS  
---  
[Inter-object contact](/docs/en/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/) Keyword: [DEFBWD](/docs/en/keyword_documentation/d/defbwd/)

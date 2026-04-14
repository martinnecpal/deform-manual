---
lang: en
title: "DEFBWD (2D3D)"
---

# DEFBWD

|  (Simulation control)  
---|---  
|  Last updated on : 29-07-2013  
  
* * *

DEFBWD Flag

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Flag |  Flag indicating if deformation profile optimization is performed = **0** Deformation profile optimization is not performed = **1** Deformation profile optimization is performed |  0  
  
DEFINITION  
---  
DEFBWD specifies if profile optimization is to be performed during a deformation simulation.  
  
REMARKS  
---  
If Flag =1, the profile will be optimized every time a deformation boundary condition is updated (node contact or node separation). Profile optimization should be done in the mesh generator when possible. If the profile cannot be optimized in the mesh generator, deformation profile optimization should be used. If profile optimization has been done in the mesh generator, deformation profile optimization should only be used for problems which contain multiple deforming objects. Applicable simulation types: Isothermal Deformation, Non-Isothermal Deformation  
  
RELATED TOPICS  
---  
[Inter-object contact](/docs/en/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/)

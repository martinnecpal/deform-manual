---
lang: en
title: "LMTSTR (2D3D)"
---

# LMTSTR

|  (Object Data)  
---|---  
|  Last updated on : 27-09-2023  
  
* * *

LMTSTR Object, LimitSrate, Fixed_flag

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
LimitSrate |  Limiting strain rate |  None  
Fixed_flag |  = **0** , Not fixed, changable   
= **1** Fixed, do not change in FEM  |  None  
  
DEFINITION  
---  
LMTSTR specifies a limiting value of effective strain rate under which the material is considered rigid.  
  
REMARKS  
---  
The recommended value for LimitSrate is .1% to 1% of the average strain rate (AVGSTR). If the solution is having difficulty converging at the 1% level, increase LimitSrate up to 10% of the average strain rate. This is recommended for a couple of steps only, then reset. If LimitSrate is too small, the solution may have difficulty converging. If it is too large the accuracy of the solution will be degraded. The value of LimitSrate is updated by DEFORM during the simulation when there is a significant change in the strain rate. Applicable object types: [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
[Deformation iteration](/docs/en/pre_processor/9_simulation_controls/9_5_solver_settings/) Keywords: [AVGSTR](/docs/en/keyword_documentation/a/avgstr/)

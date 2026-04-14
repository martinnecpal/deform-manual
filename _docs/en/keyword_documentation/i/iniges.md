---
lang: en
title: "INIGES (2D3D)"
---

# INIGES (Obsolute)

|  (Simulation control)  
---|---  
|  Last updated on : 04-08-2014  
  
* * *

INIGES i

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
i |  Parameter deciding on initial or continuing run 1 - initial run i = **0** then do not generate initial guess 0 - continuing i = **1** generate initial guess |   
  
DEFINITION  
---  
INIGES indicates whether an initial guess is necessary.  
  
REMARKS  
---  
Initial guess calculation is required when the velocity solution of the current step is expected to be quite different from that of the previous step. Therefore, i = 1 should be used for the initial step solution and for the remeshing run.  
  
RELATED TOPICS  
---  
[Simulation Controls](/docs/en/pre_processor/9_simulation_controls/9_simulation_controls/)

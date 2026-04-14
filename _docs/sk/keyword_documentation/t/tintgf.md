---
lang: sk
title: "TINTGF (2D3D)"
---

# TINTGF

|  (Simulation control)  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

TINTGF TimeFactor

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
TimeFactor |  Time integration factor for heat transfer calculation |  0.75  
  
DEFINITION  
---  
TINTGF specifies the time integration factor used in heat transfer calculations.  
  
REMARKS  
---  
The available stepping methods and their associated TINTGF values are listed below. |  Stepping Method |  TINTGF  
---|---  
Euler |  0.0  
Crank-Nicholson |  0.5  
Galerkin |  0.6667  
Backward Difference |  1.0  
  
The time integration factor is used to average temperature rates such that,

![]({{ '/assets/equations/keyword_documentation/t/tintgf_eq_1.jpg' | relative_url }}) |   
---|---  
  
The default value of 0.75 is appropriate for most applications.

Applicable simulation types: Heat Transfer, Non-Isothermal Deformation  
  
RELATED TOPICS  
---  
Simulation Controls: [Process Conditions](/docs/sk/pre_processor/9_simulation_controls/9_6_process_conditions/) \- [Constants](../../pre_processor/9_simulation_controls/9_6_process_conditions.htm#9.6.4._Constants) Keywords: [TRANS](/docs/sk/keyword_documentation/t/trans/)

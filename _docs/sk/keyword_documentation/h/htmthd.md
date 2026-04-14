---
lang: sk
title: "HTMTHD (2D3D)"
---

# HTMTHD

|  (Simulation control)  
---|---  
|  Last updated on : 07-08-2013  
  
* * *

HTMTHD specifies the heating method. (Simulation control)

  
HTMTHD HeatType

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
HeatType |  Heating method **0** = No heating **1** = Electrical resistance heating **2** = Induction heating **3** = Induction heating (Boundary element method) |  0  
  
DEFINITION  
---  
HTMTHD specifies the heating method.  
  
REMARKS  
---  
The heating method may be specified as an electrical resistance heating, induction heating, or induction heating using boundary element method. Electrical resistance heating is supported both in 2D and 3D. Induction heating option that uses boundary element method is supported from 3D v10.0  
  
RELATED TOPICS  
---  
Simulation Controls: [Modes](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#9.1.4._Type_\(STYPE\))

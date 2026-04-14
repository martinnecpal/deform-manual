---
lang: en
title: "STPINC (2D3D)"
---

# STPINC

|  (Simulation control)  
---|---  
|  Last updated on : 09-08-2013  
  
* * *

STPINC StepInc

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
StepInc |  Increment of solution steps saved to the database |  1  
  
DEFINITION  
---  
STPINC specifies the frequency with which time step solutions are saved to the DEFORM database.  
  
REMARKS  
---  
Only time step solutions which are either multiples of StepInc, remeshing steps, or ending steps will be saved in the database. For example, the recorded step numbers for a simulation that ran a total of 20 steps, was remeshed after step 10 and had StepInc = 3 would be:-1, 3, 6, 9, 10, -11, 12, 15, 18, 20. Applicable simulation types: Isothermal Deformation, Heat Transfer, Non-Isothermal Deformation  
  
RELATED TOPICS  
---  
Step parameters, DEFORM database Keywords: STPDEF, DEMAX, DSMAX, DTMAX, DVMAX, SLDERR

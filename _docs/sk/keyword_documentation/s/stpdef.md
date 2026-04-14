---
lang: sk
title: "STPDEF (2D3D)"
---

# STPDEF

|  (Simulation control)  
---|---  
|  Last updated on : 09-08-2013  
  
* * *

STPDEF StepType

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
StepType |  The type of step saved to the database = **1** User = **2** System = **3** Temperature |  1  
  
DEFINITION  
---  
STPDEF specifies which types of step solutions will be saved to the DEFORM database.  
  
REMARKS  
---  
If StepType is specified as "User", only step solutions based on DTMAX or DSMAX will be recorded in the database. If StepType is specified as "System", solutions of all the step types (DSMAX, DTMAX, DVMAX, DEMAX, SLDERR, and nodal contact) will be recorded in the database. The specified step types will be recorded at STPINC multiples. If StepType is specified as "Temperature", step solutions will then be driven by change in temperature only and not by time or stroke. The keyword DTPMAX sets the criterion governing how a time step definition will behave. Applicable simulation types: Isothermal Deformation Non-Isothermal Deformation  
  
RELATED TOPICS  
---  
Step parameters, DEFORM database Keywords: DSMAX, DTMAX, DVMAX, DEMAX, SLDERR, STPINC, DTPMAX

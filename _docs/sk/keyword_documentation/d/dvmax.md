---
lang: sk
title: "DVMAX (2D3D)"
---

# DVMAX

|  (Simulation control)  
---|---  
|  Last updated on : 30-07-2013  
  
* * *

DVMAX MaxElemVolStep, MaxObjVolStep

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
MaxElemVolStep |  Maximum element volume change per step |  0  
MaxObjVolStep |  Maximum object volume change per step |  0  
  
DEFINITION  
---  
DVMAX limits the amount of volume change that can occur in an individual element or an object during one time step. A new time step will be initiated when the volume change in any element reaches MaxElemVolStep or the volume change in any object reaches MaxObjVolStep.  
  
REMARKS  
---  
DVMAX is one of several parameters used to control the size of time steps. Other keywords which effect time step size include: DSMAX, DTMAX, DEMAX, and SLDERR. A new time step will be generated when the criteria specified in any of these keywords has been satisfied. The MaxElemVolStep represents the maximum allowable volume change for each object (dVe/Ve), and the MaxObjVolStep represents the maximum allowable volume change for the whole object (dV/V). Where Ve is the volume of the element at the beginning of the step, dVe is the amount of volume change at the end of the step. V is the volume of the object at the beginning of the step, dV is the amount of volume change at the end of the step. If MaxElemVolStep = 0, the parameters will not be used as a step size parameter. If MaxObjVolStep = 0, the parameter will not be used as a step size parameter. The time steps initiated by DVMAX will be recorded in the DEFORM database only if STPDEF is specified as "System" mode. For example if only one percent volume loss was wanted after 100 steps, than one would divide the percent volume loss by the number of steps: .01/100. Thus the DVMAX would be 0.0001. Applicable simulation types: Isothermal Deformation, Non-Isothermal Deformation  
  
RELATED TOPICS  
---  
[Step Definition](/docs/sk/pre_processor/9_simulation_controls/9_2_defining_step/) Keywords: [DSMAX](/docs/sk/keyword_documentation/d/dsmax/), [DTMAX](/docs/sk/keyword_documentation/d/dtmax/), [DVMAX](), [SLDERR](/docs/sk/keyword_documentation/s/slderr/), [STPDEF](/docs/sk/keyword_documentation/s/stpdef/)

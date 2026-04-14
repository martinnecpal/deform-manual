---
lang: en
title: "DTMAX (2D3D)"
---

# DTMAX

|  (Simulation control)  
---|---  
|  Last updated on : 30-07-2013  
  
* * *

DTMAX MaxTimeStep, MaxTimeStep2

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
MaxTimeStep |  Maximum elapsed process time per step |  None  
  
DEFINITION  
---  
DTMAX limits the amount of elapsed process time in one time step. A new time step will be initiated when the elapsed process time reaches MaxTimeStep.  
  
REMARKS  
---  
A non-zero value must be assigned to either DTMAX or DSMAX, but values cannot be assigned to both. DTMAX and DSMAX are two of several parameters used to control the size of time steps. Other keywords which effect time step size include: DEMAX, DVMAX, and SLDERR. A new time step will be generated when the criteria specified in any of these keywords has been satisfied. Typically, the value of MaxTimeStep should correspond to an average strain increment of about 0.01, i.e. a one percent height reduction. If MaxTimeStep = 0, DTMAX will not be used as a step size parameter. MaxTimeStep2 is used for complex processes where a different time step is needed for the secondary stage of the process. For example, hydraulic press with a dwell. Applicable simulation types: Isothermal Deformation, Non-Isothermal Deformation, Heat Transfer  
  
RELATED TOPICS  
---  
Step parameters Keywords: [DSMAX](/docs/en/keyword_documentation/d/dsmax/), [DEMAX](/docs/en/keyword_documentation/d/demax/), [DVMAX](/docs/en/keyword_documentation/d/dvmax/), [SLDERR](/docs/en/keyword_documentation/s/slderr/), [STPDEF](/docs/en/keyword_documentation/s/stpdef/)

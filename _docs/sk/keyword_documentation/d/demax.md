---
lang: sk
title: "DEMAX (2D3D)"
---

# DEMAX

|  (Simulation control)  
---|---  
|  Last updated on : 29-07-2013  
  
* * *

DEMAX MaxStrainStep

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
MaxStrainStep |  Maximum strain at an element center per step |  0.1  
  
DEFINITION  
---  
DEMAX limits the amount of strain that can accumulate in any individual element during one time step. A new time step will be initiated when the strain in any element reaches MaxStrainStep.  
  
REMARKS  
---  
DEMAX is one of several parameters used to control the size of time steps. Other keywords which effect time step size include: DSMAX, DTMAX, DVMAX, and SLDERR. A new time step will be generated when the criteria specified in any of these keywords has been satisfied. If MaxStrainStep = 0, DEMAX will not be used as a step size parameter. The time steps initiated by DEMAX will be recorded in the DEFORM database only if STPDEF is specified as "System" mode. This value is typically 0.01 to 0.03. Applicable simulation types: Isothermal Deformation, Non-Isothermal Deformation  
  
RELATED TOPICS  
---  
Step parameters Keywords: [DSMAX](/docs/sk/keyword_documentation/d/dsmax/), [DTMAX](/docs/sk/keyword_documentation/d/dtmax/), [DVMAX](/docs/sk/keyword_documentation/d/dvmax/), [SLDERR](/docs/sk/keyword_documentation/s/slderr/), [STPDEF](/docs/sk/keyword_documentation/s/stpdef/)

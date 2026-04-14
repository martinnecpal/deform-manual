---
lang: en
title: "TMAX (2D3D)"
---

# TMAX

|  (Simulation control)  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

TMAX MaxTime

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
MaxTime |  Maximum process time to be simulated |  0.0  
  
DEFINITION  
---  
TMAX terminates a simulation when the process time reaches MaxTime.  
  
REMARKS  
---  
TMAX is one of several parameters used to control the termination of the simulation. Other keywords which effect simulation termination include: [EMAX](/docs/en/keyword_documentation/e/emax/), LMAX, [NSTEP](/docs/en/keyword_documentation/n/nstep/), [SMAX](/docs/en/keyword_documentation/s/smax/), [VMIN](/docs/en/keyword_documentation/v/vmin/). When the criteria specified in any of these keywords has been met, the simulation will terminate. If MaxTime = 0, [TMAX]() will not be used as a termination condition. Applicable simulation types: Isothermal Deformation, Heat Transfer , Non-Isothermal Deformation  
  
RELATED TOPICS  
---  
[Stopping parameters](/docs/en/pre_processor/9_simulation_controls/9_3_stopping_controls/) Keywords: [EMAX](/docs/en/keyword_documentation/e/emax/), LMAX, [NSTEP](/docs/en/keyword_documentation/n/nstep/), [SMAX](/docs/en/keyword_documentation/s/smax/), [VMIN](/docs/en/keyword_documentation/v/vmin/)

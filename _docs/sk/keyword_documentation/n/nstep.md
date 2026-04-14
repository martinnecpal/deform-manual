---
lang: sk
title: "NSTEP (2D3D)"
---

# NSTEP

|  (Simulation control)  
---|---  
|  Last updated on : 06-08-2014  
  
* * *

NSTEP MaxSteps

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
MaxSteps |  Maximum number of steps simulated |  1  
  
DEFINITION  
---  
NSTEP limits the number of solution steps which can be generated in a simulation. A simulation will terminate when MaxSteps steps have been simulated.  
  
REMARKS  
---  
NSTEP is one of several parameters used to control the termination of the simulation. Other keywords which effect simulation termination include: EMAX, LMAX, SMAX, TMAX, VMIN. When the criteria specified in any of these keywords has been met, the simulation will terminate. MaxSteps must be assigned a positive non-zero value. If you do not want NSTEP to be the constraining termination parameter, assign a high value to MaxSteps. Applicable simulation types: Isothermal Deformation, Heat Transfer, Non-Isothermal Deformation  
  
RELATED TOPICS  
---  
[Termination parameters](/docs/sk/pre_processor/9_simulation_controls/9_3_stopping_controls/) Keywords: [EMAX](/docs/sk/keyword_documentation/e/emax/), [LMAX(2D)](/docs/sk/keyword_documentation/l/lmax/), [LMAX(3D)](/docs/sk/keyword_documentation/l/lmax_3d/), [SMAX](/docs/sk/keyword_documentation/s/smax/), [TMAX](/docs/sk/keyword_documentation/t/tmax/), [VMIN](/docs/sk/keyword_documentation/v/vmin/)

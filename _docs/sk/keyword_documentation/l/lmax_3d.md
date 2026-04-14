---
lang: sk
title: "LMAX (3D)"
---

# LMAX

|  (Simulation control - 3D)  
---|---  
|  Last updated on : 07-08-2013  
  
* * *

LMAX XmaxLoad, YmaxLoad

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
XmaxLoad |  Maximum load of primary object in X direction |  0.0  
YmaxLoad |  Maximum load of primary object in Y direction |  0.0  
  
DEFINITION  
---  
LMAX terminates a simulation when the load of the primary object reaches either XmaxLoad or YmaxLoad.  
  
REMARKS  
---  
LMAX is one of several parameters used to control the termination of the simulation. Other keywords which effect simulation termination include: EMAX, NSTEP, SMAX, TMAX, VMIN. When the criteria specified in any of these keywords has been met, the simulation will terminate. Generally, LMAX is used when the movement control of the primary object is velocity specified. If XmaxLoad = 0 or YmaxLoad = 0, the parameter will not be used as a termination condition. Applicable simulation types: Isothermal Deformation Non-Isothermal Deformation One unit of depth is used for the specification of plain strain conditions, and 360 degrees is used to specify axisymmetrical conditions.  
  
RELATED TOPICS  
---  
Termination parameters, [Primary object](../../pre_processor/9_simulation_controls/9_3_stopping_controls.htm#9.3.2._Primary_Die_Displacement_\(SMAX\)) Keywords: [SMAX](/docs/sk/keyword_documentation/s/smax/), [TMAX](/docs/sk/keyword_documentation/t/tmax/), [EMAX](/docs/sk/keyword_documentation/e/emax/), [NSTEP](/docs/sk/keyword_documentation/n/nstep/), [VMIN](/docs/sk/keyword_documentation/v/vmin/)

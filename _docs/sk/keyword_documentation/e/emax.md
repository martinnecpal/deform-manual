---
lang: sk
title: "EMAX (2D3D)"
---

# EMAX

|  (Simulation control)  
---|---  
|  Last updated on : 30-07-2013  
  
* * *

EMAX MaxStrain

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
MaxStrain |  Maximum accumulated strain at any element center |  0  
  
DEFINITION  
---  
EMAX terminates a simulation when the strain in any element reaches MaxStrain.  
  
REMARKS  
---  
EMAX is one of several parameters used to control the termination of the simulation. Other keywords which effect simulation termination include: LMAX, NSTEP, SMAX, TMAX, VMIN. The simulation will terminate when the criteria specified in any of these keywords has been satisfied. If MaxStrain = 0, EMAX will not be used as a termination condition. Applicable simulation types: Isothermal Deformation Non-Isothermal Deformation  
  
RELATED TOPICS  
---  
Termination parameters Keywords: [SMAX](/docs/sk/keyword_documentation/s/smax/), [TMAX](/docs/sk/keyword_documentation/t/tmax/), [LMAX (2D)](/docs/sk/keyword_documentation/l/lmax/), [LMAX (3D)](/docs/sk/keyword_documentation/l/lmax_3d/), [NSTEP](/docs/sk/keyword_documentation/n/nstep/), [VMIN](/docs/sk/keyword_documentation/v/vmin/)

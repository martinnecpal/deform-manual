---
lang: sk
title: "DTSUB (3D)"
---

# DTSUB

|  (Simulation control – 3D)  
---|---  
|  Last updated on : 13-08-2013  
  
* * *

DTSUB Substepping

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Substepping |  Indicator controlling sub-stepping |  1.0 (for 3-D)  
  
DEFINITION  
---  
After either DSMAX or DTMAX is prescribed, the deformation simulation may be broken into smaller substeps, depending on the assigned value of DTSUB.  
  
REMARKS  
---  
For a default DTSUB = 1.0, the system will not enable contact sub-stepping (DTSUB = 0.01). ??? For DTSUB < 1.0: Assuming a free surface node will contact the die in the time of "dtime" and of all the "dtime" the minimum is "dtmn," if dtmn >= DTMAX, there will be no substepping. However, if "dtmn" is smaller than DTMAX, then a substep will be added in the simulation. Under this situation, not only the the node with "dtime" = "dtmn" becomes a contact node, but also those nodes with (dtime - dtmn)/(dtmn) < DTSUB will be considered contact nodes in this substep. For DTSUB = 1.0: No sub-stepping will be done even "dtmn" is smaller than DTMAX. In addition, if nodal separation occurs, the simulation will not be repeated and the simulation will move to the next step. When DTSUB = 1.0 is taken, the simulation will be sped up due to no sub-stepping, but at the expense of a little greater volume loss. For DTSUB = 2.0: Upon release of nodes, the step will be recomputed to give the most updated stress state for the body. In cases where DTSUB is not equal to zero, the previous contact condition is used to compute the current stress state. Applicable simulation types:Isothermal Deformation, Non-Isothermal Deformation  
  
RELATED TOPICS  
---  
[Step Definition](/docs/sk/pre_processor/9_simulation_controls/9_2_defining_step/) Keywords: [DTMAX](/docs/sk/keyword_documentation/d/dtmax/), [DSMAX](/docs/sk/keyword_documentation/d/dsmax/)

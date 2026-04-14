---
lang: sk
title: "DTSUB (2D)"
---

# DTSUB

|  (Simulation control - 2D)  
---|---  
|  Last updated on : 30-07-2013  
  
* * *

DTSUB Substepping

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Sub-stepping |  Indicator controlling sub-stepping |  0.0 (for 2-D)  
  
DEFINITION  
---  
After either DSMAX or DTMAX is prescribed, the deformation simulation may be broken into smaller substeps, depending on the assigned value of DTSUB.  
  
REMARKS  
---  
For a default DTSUB = 0.0, the system will enable contact sub-stepping. For DTSUB = 1.0, no sub-stepping will be done. Applicable simulation types: Isothermal Deformation, Non-Isothermal Deformation  
  
RELATED TOPICS  
---  
[Step Definition](/docs/sk/pre_processor/9_simulation_controls/9_2_defining_step/) Keywords: [DTMAX](/docs/sk/keyword_documentation/d/dtmax/), [DSMAX](/docs/sk/keyword_documentation/d/dsmax_nstep/)

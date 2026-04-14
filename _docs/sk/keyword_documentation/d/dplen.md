---
lang: sk
title: "DPLEN (3D)"
---

# DPLEN

|  (Simulation control – 3D)  
---|---  
_Update History:_ (New definition has been introduced in v10.0) |  Last updated on : 21-08-2013  
  
* * *

DPLEN edge length %

ACTOUT Type, FileName

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
edge% |  % of edge length of surface |  0.5  
  
DEFINITION  
---  
DPLEN determines whether substepping should occur based on a simple calculation. A time step size is calculated for each surface node by, | ![]({{ '/assets/equations/keyword_documentation/d/dplen_eq_1.jpg' | relative_url }}) |   
---|---  
  
This value is computed for each node and the minimum value is compared to the time step size of the current step. If the current time step size is less than![]({{ '/assets/equations/keyword_documentation/d/delta_tmin.jpg' | relative_url }}) then the simulation proceeds. If the ![]({{ '/assets/equations/keyword_documentation/d/delta_tmin.jpg' | relative_url }}) is less than the current time step, then ![]({{ '/assets/equations/keyword_documentation/d/delta_tmin.jpg' | relative_url }}) is used as the current time step and the remaining time must be computed in that step.  
  
REMARKS  
---  
The default value is of 0.5 is a reasonable value for most forming processes. A value of 0 turns the substepping off.  
  
RELATED TOPICS  
---  
Simulation Controls: [Substepping Control](../../pre_processor/9_simulation_controls/9_2_defining_step.htm#Sub-stepping_Controls) Keywords: [DTSUB(2D)](/docs/sk/keyword_documentation/d/dtsub/), [DTSUB (3D)](/docs/sk/keyword_documentation/d/dtsub_3d/), [DEMAX](/docs/sk/keyword_documentation/d/demax/)

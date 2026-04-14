---
lang: en
title: "DTPMAX (3D)"
---

# DTPMAX

|  (Simulation control - 3D)  
---|---  
|  Last updated on : 30-07-2014  
  
* * *

DTPMAX MaxTempInc, t_TempMin, t_TempMax

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
MaxTempInc |  Maximum increment in temperature per step |  0  
t_TempMin |  Minimum time step allowed for a solution step |  0  
t_TempMax |  Maximum time step allowed for a solution step |  0  
  
DEFINITION  
---  
DTPMAX specifies the time stepping control based on the maximum temperature increment per time step.  
  
REMARKS  
---  
MaxTempInc specifies the maximum temperature increment per time step in heat transfer calculation. The time step calculated by MaxTempInc will control the time step for deformation when STPDEF = 3. If MaxTempInc = 0.0 then this option is ignored. If MaxTempInc ≠ 0.0 and STPDEF ≠ 3 then MaxTempInc controls when a solution will substep. If the temperature change over a time step Δt is greater than MaxTempInc, the simulation will substep. The substepping time (![]({{ '/assets/equations/keyword_documentation/d/t_dtpmax.jpg' | relative_url }})) will be determined by the equation: | ![]({{ '/assets/equations/keyword_documentation/d/dtpmax_eq_1.jpg' | relative_url }}) |   
---|---  
  
The simulation will continue to substep until the original time step Δt has been reached. The substeps ![]({{ '/assets/equations/keyword_documentation/d/t_dtpmax.jpg' | relative_url }}) are bounded by the minimum time step value ![]({{ '/assets/equations/keyword_documentation/d/tmin.jpg' | relative_url }}) and the time step Δt, or

![]({{ '/assets/equations/keyword_documentation/d/dtpmax_eq_2.jpg' | relative_url }}) |   
---|---  
  
If MaxTempInc ≠ 0.0 and STPDEF = 3 (Temperature) then the time steps will be defined solely through temperature changes in the objects. The first time step (Δt) will be defined by DSMAX/DTMAX. Thereafter, each subsequent time step will be defined by the equation:

![]({{ '/assets/equations/keyword_documentation/d/dtpmax_eq_3.jpg' | relative_url }}) |   
---|---  
  
The new time step ![]({{ '/assets/equations/keyword_documentation/d/t_dtpmax.jpg' | relative_url }}) is bounded by the minimum time step ![]({{ '/assets/equations/keyword_documentation/d/tmin.jpg' | relative_url }}) and the maximum time step ![]({{ '/assets/equations/keyword_documentation/d/tmax.jpg' | relative_url }}), or

![]({{ '/assets/equations/keyword_documentation/d/dtpmax_eq_4.jpg' | relative_url }}) |   
---|---  
  
RELATED TOPICS  
---  
[Step Definition](/docs/en/pre_processor/9_simulation_controls/9_2_defining_step/) Keyword: [STPDEF](/docs/en/keyword_documentation/s/stpdef/), [DTMAX](/docs/en/keyword_documentation/d/dtmax/), [DSMAX](/docs/en/keyword_documentation/d/dsmax/)

---
lang: sk
title: "CVGERR (2D)"
---

# CVGERR

|  (Simulation control – 2D)  
---|---  
|  Last updated on : 05-08-2014  
  
* * *

CVGERR Velerr, Forerr

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Velerr |  Velocity convergence error limit |  0.001  
Forerr |  Force convergence error limit |  0.010  
  
DEFINITION  
---  
CVGERR specifies the convergence error limits for deformation simulations.  
  
REMARKS  
---  
Convergence for each step is based on the velocity and force convergence error limits. Convergence is assumed when: | ![]({{ '/assets/equations/keyword_documentation/c/cvgerr_eq_1.jpg' | relative_url }}) |   
---|---  
  
![]({{ '/assets/equations/keyword_documentation/c/cvgerr_eq_2.jpg' | relative_url }}) |   
---|---  
  
A positive non zero value must be assigned to Velerr. If Forerr is assigned a zero value, nodal force will not be checked for convergence.

The default value is recommended for most problems.

Applicable simulation types: Isothermal Deformation, Non-Isothermal Deformation

RELATED TOPICS  
---  
Iteration procedures Keywords: [ITRMTH](/docs/sk/keyword_documentation/i/itrmth/), [ITRMXD](/docs/sk/keyword_documentation/i/itrmxd/), [ITRMXT](/docs/sk/keyword_documentation/i/itrmxt/)

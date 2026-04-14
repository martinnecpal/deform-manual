---
lang: en
title: "CVGERR (3D)"
---

# CVGERR

|  (Simulation control – 3D)  
---|---  
|  Last updated on : 05-08-2013  
  
* * *

CVGERR Velerr, Forerr

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Velerr |  Velocity convergence error limit |  0.005  
Forerr |  Force convergence error limit |  0.050  
  
DEFINITION  
---  
CVGERR specifies the convergence error limits for deformation simulations.  
  
REMARKS  
---  
Convergence for each step is based on the velocity and force convergence error limits. Convergence is assumed when: | ![]({{ '/assets/equations/keyword_documentation/c/cvgerr_eq_1.jpg' | relative_url }}) |   
---|---  
  
---|---  
  
![]({{ '/assets/equations/keyword_documentation/c/cvgerr_eq_2.jpg' | relative_url }}) |   
---|---  
  
  
A positive non zero value must be assigned to Velerr. If Forerr is assigned a zero value, nodal force will not be checked for convergence.

The default value is recommended for most problems.

Applicable simulation types: Isothermal Deformation, Non-Isothermal Deformation

RELATED TOPICS  
---  
Iteration procedures Keywords: [ITRMTH](/docs/en/keyword_documentation/i/itrmth/), [ITRMXD](/docs/en/keyword_documentation/i/itrmxd/), [ITRMXT](/docs/en/keyword_documentation/i/itrmxt/)

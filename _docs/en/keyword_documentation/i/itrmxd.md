---
lang: en
title: "ITRMXD (2D3D)"
---

# ITRMXD

|  (Simulation control)  
---|---  
|  Last updated on : 07-08-2013  
  
* * *

ITRMXD MaxIteration

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
MaxIteration |  Maximum iterations per deformation time step |  200  
  
DEFINITION  
---  
ITRMXD limits the number of iterations per deformation time step.  
  
REMARKS  
---  
When Newton-Raphson iteration is being used, MaxIteration iterations will be performed for each iteration segment (Newton-Raphson/direct iteration/Newton-Raphson/direct iteration) until the solution has converged. At most, 30 iterations will be performed during a Newton-Raphson segment. If the solution does not converge in the specified number of iterations, the simulation will terminate and a message will be written to the ProblemID.MSG file. If direct iteration is specified as the iteration method, MaxIteration iterations will be performed. If the solution has not converged, another MaxIteration will be performed. If the solution still has not converged, the simulation will terminate, and a message will be written to the ProblemID.MSG file. Iteration summaries for each deformation step are recorded in the ProblemID.MSG file. Applicable simulation types: Isothermal Deformation Non-Isothermal Deformation  
  
RELATED TOPICS  
---  
[Iteration procedures](/docs/en/pre_processor/9_simulation_controls/9_5_solver_settings/) Keywords: ,[CVGERR (2D)](/docs/en/keyword_documentation/c/cvgerr/), [CVGERR (3D)](/docs/en/keyword_documentation/c/cvgerr_3d/), [ITRMXD](), [ITRMXT](/docs/en/keyword_documentation/i/itrmxt/), [SOLMTT (2D)](/docs/en/keyword_documentation/s/solmtt/), [SOLMTT (3D)](/docs/en/keyword_documentation/s/solmtt_3d/)

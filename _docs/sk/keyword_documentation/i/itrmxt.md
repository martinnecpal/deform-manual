---
lang: sk
title: "ITRMXT (2D3D)"
---

# ITRMXT

|  (Simulation control)  
---|---  
|  Last updated on : 07-08-2013  
  
* * *

ITRMXT MaxIteration

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
MaxIteration |  Maximum iterations per heat transfer time step |  200  
  
DEFINITION  
---  
ITRMXT limits the number of iterations per heat transfer time step.  
  
REMARKS  
---  
ITRMXT specifies the maximum number of iterations which can be performed during a heat transfer time step. If convergence has not been achieved by MaxIteration the simulation will terminate. Typically heat transfer problems converge in 2-5 iterations. Iteration summaries for each heat transfer step are recorded in the ProblemID.MSG file. Applicable simulation types: Heat Transfer Non-Isothermal Deformation  
  
RELATED TOPICS  
---  
[Iteration procedures](/docs/sk/pre_processor/9_simulation_controls/9_5_solver_settings/) Keywords: ,[CVGERR (2D)](/docs/sk/keyword_documentation/c/cvgerr/), [CVGERR (3D)](/docs/sk/keyword_documentation/c/cvgerr_3d/), [ITRMTH](/docs/sk/keyword_documentation/i/itrmth/), [ITRMXT](), [SOLMTT (2D)](/docs/sk/keyword_documentation/s/solmtt/), [SOLMTT (3D)](/docs/sk/keyword_documentation/s/solmtt_3d/)

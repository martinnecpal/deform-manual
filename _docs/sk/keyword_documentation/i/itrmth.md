---
lang: sk
title: "ITRMTH (2D3D)"
---

# ITRMTH

|  (Simulation control)  
---|---  
|  Last updated on : 16-05-2019  
  
* * *

ITRMTH Itype

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Itype |  Iteration method = **1** Newton-Raphson = **2** Direct iteration |  1  
  
DEFINITION  
---  
ITRMTH specifies the iteration method used to determine nodal velocity and force convergence in deformation simulations.  
  
REMARKS  
---  
The Newton-Raphson iteration method is recommended for most problems because it generally converges in fewer iterations (usually less than 30) than the direct iteration method. However, due to the algorithmic implementation, solutions are more likely to experience convergence difficulties with Newton-Raphson than with direct iteration [3]. To compensate for the risk of solution divergence with the Newton-Raphson method, Newton-Raphson has been paired with the direct iteration method using the sequence Newton-Raphson/direct iteration/Newton-Raphson/direct iteration until convergence is achieved. When a solution has not converged within the maximum number of iterations using Newton-Raphson, the simulation will switch to the direct iteration method for the maximum number of iterations (ITRMXD). If the solution still has not converged, the simulation will switch back to Newton-Raphson for ITRMXD iterations. If the solution still has not converged, the simulation will switch one last time to direct iteration for ITRMXD iterations. A schematic representation of the direct iteration method is shown in Figure A.2. .Direct iteration requires more iterations to achieve convergence than Newton-Raphson, but is less likely to develop convergence problems. The method should only be chosen if it appears that a simulation has been having problems converging using Newton-Raphson. This can be discerned after a simulation run by checking the ProblemID.MSG file. If the file shows that the iteration method switched between Newton-Raphson and direct iteration for many of the time steps, future runs should specify direct iteration as the iteration method. Iteration summaries for each deformation step are recorded in the ProblemID.MSG file. A detailed description of the Newton-Raphson and direct iteration methods can be found in Metal Forming and the Finite-Element Method [1]. Applicable simulation types: Isothermal Deformation Non-Isothermal Deformation  
  
RELATED TOPICS  
---  
[Iteration procedures](/docs/sk/pre_processor/9_simulation_controls/9_5_solver_settings/) Keywords: ,[CVGERR (2D)](/docs/sk/keyword_documentation/c/cvgerr/), [CVGERR (3D)](/docs/sk/keyword_documentation/c/cvgerr_3d/), [ITRMXD](/docs/sk/keyword_documentation/i/itrmxd/), [ITRMXT](/docs/sk/keyword_documentation/i/itrmxt/), [SOLMTT (2D)](/docs/sk/keyword_documentation/s/solmtt/), [SOLMTT (3D)](/docs/sk/keyword_documentation/s/solmtt_3d/)

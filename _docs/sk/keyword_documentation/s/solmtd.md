---
lang: sk
title: "SOLMTD (2D)"
---

# SOLMTD

|  (Simulation control - 2D)  
---|---  
_Update History:_ v11 – MUMPS solver has been added for 2D deformation calculation. |  Last updated on : 29-07-2013  
  
* * *

SOLMTD Solver

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Solver |  Solver type =**1** Skyline =**2** CG (not available in 2D) =**3** Sparse =**4** GMRES (not available in 2D) =**5** MUMPS (new in v11) =**6** Explicit (not available in 2D) |  1  
  
DEFINITION  
---  
SOLMTD specifies the solver type used in deformation simulation.  
  
REMARKS  
---  
The skyline solver uses the skyline storage method in conjunction with Gaussian elimination. The sparse solver is optimized for sparse matrix problems. MUMPS solver is available from DEFORM-3D v11. It is recommended for induction heating simulations in which stiffness matrix is un-symmetric and has a complex value. Applicable simulation types: Isothermal/Non-Isothermal Deformations  
  
RELATED TOPICS  
---  
Keywords: [SOLMTT (2D)](/docs/sk/keyword_documentation/s/solmtt/), [SOLMTT (3D)](/docs/sk/keyword_documentation/s/solmtt_3d/)

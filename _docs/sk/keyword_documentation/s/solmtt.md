---
lang: sk
title: "SOLMTT (2D)"
---

# SOLMTT

|  (Simulation control - 2D)  
---|---  
_Update History:_ v11 – MUMPS solver has been added for 2D thermal calculation |  Last updated on : 30-07-2014  
  
* * *

SOLMTT Solver

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Solver |  Solver type =**1** Sparse =**2** CG (not available in 2D) =**3** Skyline =**4** MUMPS (new in v11) =**5** Explicit (new in v11) |  1  
  
DEFINITION  
---  
SOLMTT specifies the solver type used in heat transfer simulations.  
  
REMARKS  
---  
The skyline solver uses the skyline storage method in conjunction with Gaussian elimination. The skyline solver is recommended for most problems. MUMPS solver is available from DEFORM-2D v11. It is recommended for induction heating simulations in which stiffness matrix is un-symmetric and has a complex value. Applicable simulation types: Heat Transfer, Non-Isothermal Deformation  
  
RELATED TOPICS  
---  
Keyword: [SOLMTD (2D)](/docs/sk/keyword_documentation/s/solmtd/), [SOLMTD (3D)](/docs/sk/keyword_documentation/s/solmtd_3d/)

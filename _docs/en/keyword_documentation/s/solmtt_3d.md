---
lang: en
title: "SOLMTT (3D)"
---

# SOLMTT

|  (Simulation control - 3D)  
---|---  
_Update History:_ v11 – MUMPS solver has been added for 3D thermal calculation v11 – Explicit solver has been added for 3D thermal calculation |  Last updated on : 3-07-2014  
  
* * *

SOLMTT Solver

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Solver |  Solver type =**1** Sparse =**2** CG =**3** Skyline =**4** MUMPS (new in v11) =**5** Explicit (new in v11) |  1  
  
DEFINITION  
---  
SOLMTT specifies the solver type used in heat transfer simulations.  
  
REMARKS  
---  
The skyline solver uses the skyline storage method in conjunction with Gaussian elimination. The skyline solver is recommended for most problems. MUMPS solver is available from DEFORM-3D v11. It is recommended for induction heating simulations in which stiffness matrix is un-symmetric and has a complex value. Applicable simulation types: Heat Transfer, Non-Isothermal Deformation  
  
RELATED TOPICS  
---  
Keyword: [SOLMTD (2D)](/docs/en/keyword_documentation/s/solmtd/), [SOLMTD (3D)](/docs/en/keyword_documentation/s/solmtd_3d/)

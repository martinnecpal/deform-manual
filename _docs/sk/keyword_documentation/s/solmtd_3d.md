---
lang: sk
title: "SOLMTD (3D)"
---

# SOLMTD

|  (Simulation control - 3D)  
---|---  
_Update History:_ v11 – CG-Hybrid, NUMPS and Explicit solvers have been added for 3D deformation calculation. v11.1 – Domain Decomposition, Dual Mesh, DD+DM solvers have been added for 3D deformation calculation |  Last updated on : 29-07-2013  
  
* * *

SOLMTD Solver, Npara

or

SOLMTD Solver, Npara(=4) (for Solver=2, CG-Hybrid)

Par1, Par2, Par3, Par4

or

SOLMTD Solver, Npara(=3) (for Solver=6, Explicit)

Par1, Par2, Par3

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Solver |  Solver type =**1** Sparse =**2** CG-Hybrid (new in v11) =**3** Skyline (obsolete) =**4** GMRES =**5** MUMPS (new in v11) =**6** Explicit (new in v11) =**7** Domain Decomposition (DD) (Rigid plastic only) (new in v11.1) =**8** Dual Mesh (DM) (Rigid plastic only)(new in v11.1) =**9** DD + DM (Elasto-plastic only)(new in v11.1) |  1  
Npara |  Number of control parameters =**0** (for Sparse, Skyline, GMRES, MUMPS) =**4** (for CG-Hybrid) =**3** (for Explicit) |  None  
(for Solver=2, CG-Hybrid)  
Part1  |  CG solver type  = **0** for Old CG =**1** for New CG = **2** for Old and New CG |  2  
Part2  |  Level of fill-in |  4  
Part3  |  Partitioning method |  1  
Part4  |  Direct solver in case of poor convergence = **1** for Sparse = **5** for MUMPS |  1  
(for Solver=6, Explicit)  
Part1  |  Damping  |  None  
Part2  |  Mass Scaling |  None  
Part3  |  Cycle |  None  
  
DEFINITION  
---  
SOLMTD specifies the solver type and associated control parameters used in deformation simulation.  
  
REMARKS  
---  
The skyline solver uses the skyline storage method in conjunction with Gaussian elimination. The sparse solver is optimized for sparse matrix problems. The conjugate gradient solver is recommended when a part is well contacted due to its speed and efficient use of system memory. (For Domain decomposition) \- Domain decomposition method is recommended only for single plastic object with Tet. mesh. \- Domain decomposition method does not allow meshed die(s). (For Dual mesh) \- Dual mesh method is recommended only for single plastic object with Tet. mesh. (For DD + DM) \- DD + DM method is recommended only for single elasto-plastic object with Tet. mesh. \- DD + DM method does not allow meshed die(s). Applicable simulation types: Isothermal/Non-Isothermal Deformations  
  
RELATED TOPICS  
---  
Keywords: [SOLMTT (2D)](/docs/sk/keyword_documentation/s/solmtt/), [SOLMTT (3D)](/docs/sk/keyword_documentation/s/solmtt_3d/)

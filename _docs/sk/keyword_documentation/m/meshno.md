---
lang: sk
title: "MESHNO (2D3D)"
---

# MESHNO

|  (Simulation control)  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

MESHNO MeshNum

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
MeshNum |  Current mesh number |  1  
  
DEFINITION  
---  
MESHNO indicates the cumulative number of object remeshings which have taken place at a specified step number.  
  
REMARKS  
---  
For initial runs MeshNum = 1. The mesh number increases by one for each remeshing of an object. The mesh number value is updated automatically by DEFORM and should not be modified. For example, suppose a database contains step numbers -1, 5, 10, 15, -16, 20, 25, -25, 30, 35 and that remeshings occurred at steps -16 and -25. If step number 35 was read into the Input Preparation utility, the mesh number would be set to "3". Applicable simulation types: Isothermal Deformation Non-Isothermal Deformation  
  
RELATED TOPICS  
---  
Simulation Controls: [Main Controls](/docs/sk/pre_processor/9_simulation_controls/9_2_defining_step/), [Mesh](/docs/sk/pre_processor/13_mesh_generation/13_mesh_generation/)

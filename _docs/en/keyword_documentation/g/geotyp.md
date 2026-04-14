---
lang: en
title: "GEOTYP (2D)"
---

# GEOTYP

|  (Simulation-Control 2D)  
---|---  
_Update History:_ V11.1 – Sub-geometry type (for 2.5D Rolling) has been introduced. |  Last updated on : 27-09-2023  
  
* * *

GEOTYP Gtype, 2.5D_Type, SectionNo

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Gtype |  Type of geometric representation =**1** Axisymmetric geometry = **2** Plane strain geometry = **3** Torsion geometry = **4** Plane stress geometry |  None  
2.5D_Type |  Sub-geometry type = **0** None  
= **1** 2.5D Rolling (Gtype = 2)  
= **2** 2.5D Liner Friction Welding (Gtype = 3)  
= **3** 2.5D Roll Forming (Gtype = 2) |  0  
Section No |  Number of sections in 2.5D FEM (2.5D_Type = 1,3) |  0  
  
DEFINITION  
---  
The geometry type indicates whether the two dimensional mesh represents an axisymmetric geometry or a plane strain geometry  
  
REMARKS  
---  
Applicable simulation types: Heat Transfer Isothermal Deformation Non-Isothermal Deformation  
  
RELATED TOPICS  
---  
Simulation Controls: [Geometry type](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#9.1.2._Geometry_type_\(GEOTYP\)_\[2D\]), [Geometry](/docs/en/pre_processor/12_geometry_modelling/12_2_2d_geometry_editing/)

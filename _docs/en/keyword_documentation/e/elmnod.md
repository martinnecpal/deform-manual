---
lang: en
title: "ELMNOD (2D3D)"
---

# ELMNOD

|  (Simulation control)  
---|---  
_Update History:_ (New) Definition has been extended in v11 |  Last updated on : 23-07-2013  
  
* * *

ELMNOD Ndata(=10)

Var1, Var2, Var3, Var4, Var5, Var6, Var7, Var8, Var9, Var10

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Ndata |  Number of data |  10  
Var1 |  Option for damage variable |  0  
Var2 |  Option for strain variable |  0  
Var3 |  Option for stress variable = **0** SV at element = **2** SV at element and node = **3** SV at integration points (new in v11) |  0  
Var4 |  Option for density variable  = **0** SV at element |  0  
Var5 |  Option for grain variable  = **0** SV at element (for all grain models except Mesoscale) = **1** SV at node (for Mesoscale model) |  0  
Var6 ~ Var10 |  Not used yet |  0  
  
DEFINITION  
---  
ELMNOD specifies state variable output option for stress, strain, and damage when they are saved in the DEFORM database file (*.DB).  
  
REMARKS  
---  
For element output option, state variables (stress, strain, and damage) are saved at the centroid of each element. For element and node output option, the above state variables are saved both at node and element. This will help ensuring simulation accuracy during remeshing. Since remeshing involves data interpolation from old mesh system to new mesh system, a series of remeshings during large deformation may compromise the FEM solution accuracy. It is recommended for sheet forming in which a prediction of springback is important based on the residual stresses produced during sheet forming. Choosing SV at integration point option will increase the size of database file significantly if the FE model size is large especially in 3D simulation. For integration point output option, state variables are saved at Gauss integration points. The number of integration points depends on the element type as below. For 2D quadrilateral element, 4 integration points are used. For 3D brick (hexahedral) element, 8 integration points are used. For 3D tet (Tetrahedral) element, 1 point integration is used. For recrystallization model, output options are pre-determined (They are not accessible through GUI). The mesoscale model always uses nodal output option and all other models use elemental output option. Applicable object types: [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
Keywords:[STRESS (2D)](/docs/en/keyword_documentation/s/stress/), [STRESS (3D)](/docs/en/keyword_documentation/s/stress_3d/) , [STRAIN (2D)](/docs/en/keyword_documentation/s/strain/), [STRAIN (3D)](/docs/en/keyword_documentation/s/strain_3d/), [DAMAGE (2D)](/docs/en/keyword_documentation/d/damage/), [DAMAGE (3D)](/docs/en/keyword_documentation/d/damage_3d/), , [GRNDAT](/docs/en/keyword_documentation/g/grndat/)

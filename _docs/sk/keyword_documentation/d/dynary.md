---
lang: sk
title: "DYNARY (2D3D)"
---

# DYNARY

|  (Object data)  
---|---  
_Update History:_ (New keyword in v11) |  Last updated on : 23-07-2013  
  
* * *

DYNARY Object, ArrayNo, ArrayType, SubType, NumData, NumComps

Num(1), Data(1,1),...,Data(1, Ncomp)

:: :: ::

Num(Ndata), Data(Ndata,1),...,Data(Ndata, Ncomp)

or

(for 1-D state variable, ArrayType = 3, NumData = 1)

DYNARY Object, ArrayNo, ArrayType, SubType, 1, NumComps, Default

Num(1), Data(1,1),...,Data(1, NumComps)

:: :: ::

Num(NumData), Data(NumData,1),...,Data(NumData, NumComps)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
ArrayNo |  Array number |  None  
ArrayType |  Array type = **1** Coordinate = **2** Connectivity = **3** State variable |  1  
SubType |  Sub type (for ArrayType = **2** , Connectivity) = **3** Triangle = **4** Quadrilateral = **5** Tetrahedral = **8** Hexahedral (Brick) (for ArrayType = **3** , State variable) = **100** Damage = **200** Density = **300** Strain = **500** Stress = **600** Temperature = **700** Velocity |  None  
NumData |  Number of data |  0  
NumComps |  Number of components |  0  
Num(i) |  Number of ith variable |  0  
Data(i,j) |  Value of of jth component at ith variable |  0  
Default |  Default value |  0  
  
DEFINITION  
---  
DYNARY allocates dynamic arrays in which FEM can save built-in flownet and Lagrangian mesh definition for ALE simulation.  
  
REMARKS  
---  
The data defined by use of this keyword is not saved in A array or MAR array, but instead it is saved in dynamic array region in the database file. This keyword allocates the space for state variables for nodes as well. (Example 1) 2D coordinates DYNARY 2 1 1 0 1316 2 1 0.0000000000E+000 1.4000000000E+000 2 0.0000000000E+000 1.3481480000E+000 :: 1316 2.4000000000E+000 0.0000000000E+000 (Example 2) 2D connectivity DYNARY 2 2 2 4 1242 4 1 14 15 43 42 2 13 14 42 41 :: 1242 1303 1302 1274 1275 (Example 3) State variables DYNARY 2 3 3 300 0 1 1.2300000000E+000  
  
RELATED TOPICS  
---  
[ALE simulation](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#9.1.5._Simulation_modes_\(SMODE,_TRANS\)), [Built-in flownet](../../pre_processor/13_mesh_generation/13_2_3d_tet_mesh_generation.htm#13_2_9_Built_In_Flownet)

---
lang: sk
title: "LOCDEF (2D)"
---

# LOCDEF

|  (Object data - 2D)  
---|---  
|  Last updated on : 06-08-2014  
  
* * *

LOCDEF Object, LocNum, UsrRtn, PrsType, FricType, FricFuncType

(Followed by Data)

ConstVal / NData

X(1) Y(1)

...

X(NData) Y(NData)

...

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
LocNum |  Local definition number |  None  
UsrRtn |  User routine number |  None  
PrsType |  Type of pressure definition = **0** Constant =**1** Function of time |  None  
FricType |  Friction type = **1** Shear friction = **2** Coulomb friction = **3** Constant Tau |  None  
FricFuncType |  Function type = **0** Constant = **1** f(time) = **2** f(pressure) = **3** f(temperature) = **4** f(surface stretch) = **5** f(pressure, temperature, surface stretch) |  0  
  
DEFINITION  
---  
LOCDEF specifies the local deformation boundary definition for an object. It is also referred to as the "Advanced boundary conditions".  
  
REMARKS  
---  
This keyword works in conjunction with ECCDEF to define the pressure and friction on a specific surface polygon. Note that if the object is rigid, friction defined here has higher priority than the friction defined as inter-object data. If the data is of constant type, only the constant value is given in the data list. If tabular data is used to describe any of the above variables, the number of data sets is listed followed by the data set. Applicable [Simulation Modules](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#9.1.5._Simulation_modes_\(SMODE,_TRANS\)): Deformation Applicable [Object Types](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4._Object_type): ALL except Rigid  
  
RELATED TOPICS  
---  
[Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/): Advanced Deformation Keywords: [ECCDEF (2D)](/docs/sk/keyword_documentation/e/eccdef/), [ECCDEF (3D)](/docs/sk/keyword_documentation/e/eccdef_3d/)

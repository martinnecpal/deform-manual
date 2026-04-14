---
lang: en
title: "OBJSTP (3D)"
---

# OBJSTP

|  (Simulation control - 3D)  
---|---  
|  Last updated on : 13-08-2013  
  
* * *

OBJSTP Object, X, Y, Z, nx, ny, nz

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object  |  Object Number |  None  
X, Y, Z |  X, Y, Z coordinate of a point on stopping plane |   
nx, ny, nz  |  Normal direction vector of the stopping plane |   
  
DEFINITION  
---  
OBJSTP defines a plane in 3D that is used as a simulation stopping plane criterion. When the object passes this plane and is entirely located in a half domain defined by this plane, FEM simulation will stop automatically. (supported from 3D V6.1)  
  
REMARKS  
---  
A plane, used as a simulation stopping criterion, is defined with a point (x,y,z) and its normal direction vector (nx, ny, nz). Applicable object types: [Rigid](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.5._Rigid), [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
Simulation Controls: [Stopping Controls](/docs/en/pre_processor/9_simulation_controls/9_3_stopping_controls/)

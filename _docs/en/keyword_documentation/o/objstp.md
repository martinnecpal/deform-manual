---
lang: en
title: "OBJSTP (2D)"
---

# OBJSTP

|  (Simulation control -2D)  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

OBJSTP Object, X, Y, nx, ny

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
X, Y  |  X, Y coordinate of a point on stopping plane |   
nx, ny |  Normal direction vector of the stopping plane |   
  
DEFINITION  
---  
OBJSTP defines a plane that is used as a simulation stopping plane criterion. When the object passes this plane and is entirely located in a half domain defined by this plane, FEM simulation will stop automatically. (Supported from 2D V9.1)  
  
REMARKS  
---  
A plane, used as a simulation stopping criterion, is defined with a point (x,y) and its normal direction vector (nx, ny).  
  
RELATED TOPICS  
---  
Simulation Controls:[Stopping Controls](/docs/en/pre_processor/9_simulation_controls/9_3_stopping_controls/)

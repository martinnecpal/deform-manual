---
lang: sk
title: "REFPOS (3D)"
---

# REFPOS

|  (Simulation control - 3D)  
---|---  
|  Last updated on : 13-08-2013  
  
* * *

PRZ Object, DefPressureX, DefPressureY, DefPressureZ, Ndata

Node(1), Pressure(1)

: :

Node(Ndata), Pressure(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Method |  Distance tolerance for critical nodes (**0** = None, **1** = coordinate ,**2** = node) |  None  
Var1 |  X coordinate or Node number |  None  
Var2 |  Y coordinate or Blank |  None  
Var3 |  Z coordinate or Blank |  None  
  
DEFINITION  
---  
REFPOS sets reference points for an object.  
  
REMARKS  
---  
REFPOS is to be used in conjunction with MDSOBJ which sets the distance between two objects.  
  
RELATED TOPICS  
---  
Simulation Controls: [Stopping Controls](/docs/sk/pre_processor/9_simulation_controls/9_3_stopping_controls/) Keywords: [MDSOBJ (2D)](/docs/sk/keyword_documentation/m/mdsobj/), [MDSOBJ (3D)](/docs/sk/keyword_documentation/m/mdsobj_3d/)

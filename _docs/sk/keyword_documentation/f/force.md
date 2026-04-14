---
lang: sk
title: "FORCE (2D)"
---

# FORCE

|  (Object data - 2D)  
---|---  
_Update History:_ V11 - FORCE has been introduced. |  Last updated on : 23-07-2013  
  
* * *

FORCE Object, XForce, YForce

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
XForce |  Object force in X |  0  
YForce |  Object force in Y |  0  
  
DEFINITION  
---  
FORCE specifies the current force of objects. These values are saved in the DB step header, same as STROKE in order to support a continuity of force throughout remeshing.  
  
REMARKS  
---  
This keyword saves the current force of objects in the DB step header, same as the current stroke STROKE, in order to support a continuity of force throughout remeshing.  
  
RELATED TOPICS  
---  
Related Keywords: [PDIE](/docs/sk/keyword_documentation/p/pdie/), [MOVCTL (2D)](../m/movctl_\(2d\).htm), [MOVCTL (3D)](../m/movctl_\(3d\).htm)

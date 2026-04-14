---
lang: en
title: "FORCE (3D)"
---

# FORCE

|  (Object data - 3D)  
---|---  
_Update History:_ V11 - FORCE has been introduced. |  Last updated on : 13-08-2013  
  
* * *

FORCE Object, XForce, YForce, ZForce

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
XForce |  Object force in X |  0.0  
YForce |  Object force in Y |  0.0  
ZForce |  Object force in Z |  0.0  
  
DEFINITION  
---  
FORCE specifies the current force of objects. These values are saved in the DB step header, same as STROKE in order to support a continuity of force throughout remeshing.  
  
REMARKS  
---  
This keyword saves the current force of objects in the DB step header, same as the current stroke STROKE, in order to support a continuity of force throughout remeshing. Applicable object types: [Rigid](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.5._Rigid)  
  
RELATED TOPICS  
---  
Related Keywords: [PDIE](/docs/en/keyword_documentation/p/pdie/), [MOVCTL (2D)](../m/movctl_\(2d\).htm), [MOVCTL (3D)](../m/movctl_\(3d\).htm)

---
lang: sk
title: "ANGMOV(3D)"
---

# ANGMOV

|  (Object Data - 3D)  
---|---  
|  Last updated on : 12-08-2013  
  
* * *

ANGMOV Obj, type, ftype, value/npt, Xi, Yi

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Obj |  Object Number |  None  
type |  = **0** Controlled by specific torque  
= **1** Controlled by specific angular velocity in Rad/sec |  None  
ftype |  = **0** Then value is read None  
= **1** Then f(time)  
= **2** Then f(angle) |  None  
  
DEFINITION  
---  
ANGMOV specifies the rotational velocity of an object with the counterclockwise direction having the convention as positive.  
  
REMARKS  
---  
The rotational velocity of an object can be specified by a torque rate or an angular velocity.  Applicable object types: [Rigid](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.5._Rigid)  
  
RELATED TOPICS  
---  
Keywords: [MOVCTL](../m/movctl_\(3d\).htm), [CNTRAX](../c/cntrax\(3d\).htm)

---
lang: en
title: "ANGMO2 (3D)"
---

# ANGMO2

|  (Object Data - 3D)  
---|---  
|  Last updated on : 12-08-2013  
  
* * *

ANGMO2 Obj, type, ftype, value/npt, Xi, Yi 

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Obj |  Object number |  None  
type |  = 0 Controlled by specific torque  
= 1 Controlled by specific angular velocity in Rad/sec |  None  
ftype |  = 0 Then value is read  
= 1 Then f(time)  
= 2 Then f(angle) |  None  
  
DEFINITION  
---  
ANGMO2 specifies the angular movement of the 2nd rotational axis.  
  
REMARKS  
---  
The 2nd rotational velocity of an object can be specified by a torque rate or an angular velocity  Applicable object types: [Rigid](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.5._Rigid)  
  
RELATED TOPICS  
---  
Keywords: [MOVCTL](../m/movctl_\(3d\).htm), [CNTRAX](../c/cntrax\(3d\).htm)

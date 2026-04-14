---
lang: sk
title: "ANGMOV (2D)"
---

# ANGMOV

|  (Object Data - 2D)  
---|---  
|  Last updated on : 29-07-2013  
  
* * *

ANGMOV Object, Rtype, Rdef, RotVelocity/Torque (Rdef = 0)  
or   
ANGMOV Object, Rtype, Rdef, Ndata (Rdef = 1 )  
Time(1) AngVel/Torque(1)  
: :  
Time(Ndata) AngVel/Torque(Ndata)  
or   
ANGMOV Object, Rtype, Rdef, Ndata (Rdef = 2 )  
Angle(1) AngVel/Torque(1)  
: :  
Angle(Ndata) AngVel/Torque(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number | None  
Rtype |  Rotaion type 1 = **0** Torque (force * unit length) = **1** Angular velocity (rad/unit time) |   
Rdef |  Rotational definition method = **0** Constant = **1** f(time) - Angular velocity or torque as a function of time = **2** f(angle) - Angular velocity or torque as a function of angle |   
RotVelocity/Torque |  RotVelocity/Torque |  0  
Ndata |  Number of data points |  0  
Time(i) |  Time of ith data set |  None  
Angle(i) |  Angle of ith data set |  None  
AngVel/Torque(i) |  Angular velocity or torque of ith data set |  None  
  
DEFINITION  
---  
ANGMOV specifies the rotational velocity of an object with the counterclockwise direction having the convention as positive.  
  
REMARKS  
---  
The rotational velocity of an object can be specified by a torque rate or an angular velocity Applicable object types: [Rigid](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.5._Rigid)  
  
RELATED TOPICS  
---  
Keywords: [MOVCTL](../m/movctl_\(2d\).htm), [CNTRAX](/docs/sk/keyword_documentation/c/cntrax/)

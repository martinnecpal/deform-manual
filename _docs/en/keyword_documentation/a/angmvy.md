---
lang: en
title: "ANGMVY (2D)"
---

# ANGMVY

|  (Object Data - 2D)  
---|---  
|  Last updated on : 29-07-2013  
  
* * *

ANGMVY Object, Rtype, Rdef, RotVelocity/Torque, CurAng (Rtype = 0, 1, Rdef = 0)  
or   
ANGMVY Object, Rtype, Rdef, Ndata, CurAng (Rtype = 0, 1, Rdef = 1,2 )  
Time(1) AngVel/Torque(1)  
: :  
Time(Ndata) AngVel/Torque(Ndata)  
or   
ANGMVY Object, Rtype, Energy, Inertia, Efficiency, CurAng (Rtype = 2)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
Rtype |  Rotation type 1  
= **0** Torque (force * unit length)  
= **1** Angular velocity (rad/unit time)  
= **2** Energy |  1  
Rdef |  Rotational definition method  
= **0** Constant  
= **1** f(time) -Angular velocity or torque as a function of time  
= **2** f(angle)-Angular velocity or torque as a function of angle |   
RotVelocity/Torque |  Rotational velocity or torque |  0  
Ndata | Number of data points | 0  
Time(i) | Time of ith data set |  None  
Angle(i) | Angle of ith data set |  None  
AngVel/Torque(i) | Angular velocity or torque of ith data set |  None  
  
DEFINITION  
---  
ANGMVY specifies the torsion rotational movement. Note this is meaningful only for Torsion case (e.g. inertial welding).  
  
RELATED TOPICS  
---  
Applicable Geometry types: [Torsion](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#9.1.2._Geometry_type_\(GEOTYP\)_\[2D\])   
Keywords: [MOVCTL](../m/movctl_\(2d\).htm)

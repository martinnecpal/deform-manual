---
lang: en
title: "MOVCTL (3D)"
---

# MOVCTL

|  (Object data - 3D)  
---|---  
_Update History:_ v11 – New pusher BCC type movement control has been added for Lagrangian rolling [Speed] Speed movement can be defined as a function of force [Screw Press] Efficiency of screw press can be defined as a function of force. Current hammer/screw press efficiency computed by FEM will be written in keyword. |  Last updated on : 13-08-2013  
  
* * *

The movement of an object can be governed by specifying movement type as shown in the table.

v11 |  Movement |  Type No (Mtype)  
---|---|---  
|  Force |  0  
Extended |  Speed |  1  
Extended |  Hammer |  2  
Extended |  Screw press |  3  
|  Mechanical press |  4  
|  Sliding die |  5  
|  Path movement |  6  
|  Hydraulic press with Avg. strain-rate control |  7  
|  Hydraulic press with Speed control |  8  
|  Hydraulic press with Power limit control |  9  
|  Hydraulic press with Maximum strain-rate control (obsolete) |  10  
New in v11 |  Pusher BCC |  11  
  
NOTE: Mtype = 10, Hydraulic Press - Maximum Strain Rate Controlled is obsolete

The keyword data format for each type is documented separately below.

* * *

DEFINITION  
---  
MOVCTL specifies the movement control of an object.  
  
REMARKS  
---  
Movement controls can be applied to rigid objects and boundary nodes of meshed objects. The surface defined by these nodes can be thought of as a "rigid surface". During the simulation, the constrained nodes will move synchronously in the speed and direction defined by the movement controls. The resultant load due to inter-object contact is calculated for all objects with a MOVCTL boundary constraint. If Mtype = 0, the speed of the object is constrained such that the specified load, Load/Speed, is maintained. When the object is rigid, the load is the resultant load applied by a non-rigid object due to the relative motion of the two objects. When the object is elastic, plastic, or porous, the load is the sum of the nodal loads of all nodes with boundary constraint code 3 (BCCDEF). If Mtype = 1, the speed of the object is constrained to match the specified speed, Load/Speed. When the object is rigid, the entire object maintains the specified speed. When the object is elastic, plastic, or porous, each node with deformation boundary constraint code 3 (BCCDEF) maintains the specified speed. The load or speed can be as a constant value, a function of the primary object stroke, or a function of time. The function type is specified by the value of Ftype. If Ftype = 0 use the operand Load/Speed. If Ftype = 1 or Ftype = 2, use the operands Ndata, Stroke/Time(i), Load/Speed(i). When Ftype = 1 or Ftype = 2, each data pair should be provided on a separate line. Hence there should be Ndata lines of Stroke/Time(i), Load/Speed(i). If Ftype = 1, the stroke, Stroke/Time, refers to the stroke of the primary object. MOVCTL (Mtype=3) specifies Hammer movement. Hammer efficiency can be specified either as constant value or function data. Also, counter-blow hammer can be specified. MOVCTL (Mtype=4) specifies Screw Press movement. Screw press efficiency can be defined as a function of force. MOVCTL (Mtype=5) specifies Spring-loaded die controlled movement and this can only be specified for rigid objects. MOVCTL (Mtype=6) specifies Arbitrary path controlled movement. Any path movement data can be provided as a function of time. MOVCTL (Mtype=7~9) specifies the hydraulic press movement data. Hydraulic press (speed control) is the same as the speed controlled (Mtype = 1), except that it is should be used together with speed limit (SPDLMT). It is created for user interface convenience. Hydraulic press (power limit control) means to use the maximum power of the press. Therefore, the speed will be solely determined by the speed limit (SPDLMT). MOVCTL (Mtype=11) specifies the movement control of an object using the specified Pusher BCC. The primary use of this movement type is for providing a virtual pusher object in Lagrangian shape rolling simulation. When workpiece object has deformation boundary code (type=3, nodal movement control in BCCDEF), the pusher bcc movement data will be utilized. Applicable object types: [Rigid](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.5._Rigid), [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
Keywords: [BCCDEF (2D)](/docs/en/keyword_documentation/b/bccdef/), [BCCDEF (3D)](/docs/en/keyword_documentation/b/bccdef_3d/)  
  
Load Controlled (Type=0)

* * *

MOVCTL Object, Mtype(=0), Ftype, VectorX, VectorY, VectorZ, Load

or

MOVCTL Object, Mtype(=0), Ftype, VectorX, VectorY, VectorZ, Ndata

Stroke/Time(1), Load(1)

:: 

Stroke/Time(Ndata), Load(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
Mtype |  Movement type = **0** Load controlled |  1  
Ftype |  Function type of controlled quantity = **0** Constant =**1** Function of stroke = **2** Function of time = **-n** User routine no. n |  0  
Load |  Value of constant load |  None  
Ndata |  Number of data pairs |  None  
VectorX |  Unit direction vector for movement in X direction |  0.0  
VectorY |  Unit direction vector for movement in Y direction |  0.0  
VectorZ |  Unit direction vector for movement in Z direction |  0.0  
Stroke/Time(i) |  Stroke or time of ith data pair |  None  
Load(i) |  Load of ith data pair |  None  
  
Speed Controlled (Type=1)

* * *

MOVCTL Object, Mtype(=1), Ftype, VectorX, VectorY, VectorZ, Speed/SpdRatio

or

MOVCTL Object, Mtype(=1), Ftype, VectorX, VectorY, VectorZ, Ndata

Stroke/Time/Force(1), Speed(1)

:: 

Stroke/Time/Force(Ndata), Speed(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
Mtype |  Movement type = **1** Speed controlled |  1  
Ftype |  Function type of controlled quantity = **0** Constant = **1** Function of stroke = **2** Function of time = **4** Function of force (new in v11) = **1000+n** Speed following object n = **-n** User routine no. n |  0  
Load/Speed |  Value of constant speed |  None  
SpdRatio |  (if Ftype = 1000+n) Speed ratio to object n |  None  
Ndata |  Number of data pairs |  None  
VectorX |  Unit direction vector for movement in X direction |  0.0  
VectorY |  Unit direction vector for movement in Y direction |  0.0  
VectorZ  |  Unit direction vector for movement in Z direction |  0.0  
Stroke/Time/Force(i) |  Stroke or time or Force of ith data pair |  None  
Speed(i) |  Speed of ith data pair |  None  
  
Hammer (Type=2)

* * *

MOVCTL Object, Mtype(=2), VectorX, VectorY, VectorZ

Energy, Efficiency, Mass, CounterObj

or

MOVCTL Object, Mtype(=2), VectorX, VectorY, VectorZ

Energy, Efficiency, Mass, CounterObj, Ftype, Ndata

Force(1), Effy(1)

:: 

Force(Ndata), Effy(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
Mtype |  = **2** Hammer press |  1  
Ftype |  Function type of controlled quantity = **0** Constant = **4** Function of force |  0  
VectorX |  Unit direction vector for movement in X direction |  0.0  
VectorY |  Unit direction vector for movement in Y direction |  0.0  
VectorZ |  Unit direction vector for movement in Z direction |  0.0  
Energy |  Hammer blow energy |  None  
Efficiency |  Hammer blow efficiency |  None  
Mass |  Hammer mass (Moment of inertial) |  None  
CounterObj |  Object No. of the counter blow (0 if not counter blow) |  0  
Ndata |  Number of data pairs |  None  
Force(i) |  Force of ith data pair  |  None  
Effy(i) |  Efficiency of ith data pair |  None  
  
Screw Press (Type=3)

* * *

MOVCTL Object, Mtype(=3), VectorX, VectorY, VectorZ

Energy, Efficiency, Inertia, DispPerRev

or

MOVCTL Object, Mtype(=3), VectorX, VectorY, VectorZ

Energy, Efficiency, Inertia, DispPerRev, Ftype,

Ndata

Force(1), Effy(1)

:: 

Force(Ndata), Effy(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
Mtype |  Movement type = **3** Screw Press |  1  
Ftype |  Function type of controlled quantity = **0** Constant = **4** Function of force (new in v11) |  0  
VectorX |  Unit direction vector for movement in X direction |  0.0  
VectorY |  Unit direction vector for movement in Y direction |  0.0  
VectorZ |  Unit direction vector for movement in Z direction |  0.0  
Energy |  Screw press blow energy |  0.0  
Efficiency |  Screw press blow efficiency |  None  
Inertia |  Screw press moment of inertia |  None  
DispPerRev |  Displacement of ram per revolution of screw press fly wheel. |  None  
Ndata |  Number of data pairs |  None  
Force(i) |  Force of ith data pair |  None  
Effy(i) |  Efficiency of ith data pair |  None  
  
Mechanical Press (Type=4)

* * *

MOVCTL Object, Mtype(=4), VectorX, VectorY, VectorZ

TotalDispl, StrokeFreq, ConnRodLen, Ndata

(if Ndata > 0):

Ang(1), Pos(1)

::

Ang(Ndata), Pos(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
Mtype |  Movement type = **4** Mechanical Press |  1  
VectorX |  Unit direction vector for movement in X direction |  0.0  
VectorY |  Unit direction vector for movement in Y direction |  0.0  
VectorZ |  Unit direction vector for movement in Z direction |  0.0  
TotalDispl |  Total displacement of the die |  None  
StrokeFreq |  Number of strokes per unit of time |  None  
ConnRodLen |  Length of connecting rod (effect ignored if 0) |  None  
Ndata |  Number of position data pairs for specialty press (if Ndata = 0, conventional mechanical press is assumed) |  0  
Ang(i) |  Angle (in degree) of the ith position data pair |   
Pos(i) |  Position of the ith position data pair |   
  
Spring-Loaded Die (Type=5)

* * *

MOVCTL Object, Mtype(=5), VectorX, VectorY, VectorZ

StiffnessTyp(=0), Stiffnes, CurDisp, MaxDisp, PreLoad, MountObj, Reversible

or

MOVCTL Object, Mtype(=5), VectorX, VectorY, VectorZ

StiffnessTyp(=1), NData, CurDisp, MaxDisp, PreLoad, MountObj, Reversible

Displ(1), Force(1)

::

Displ(Ndata), Force(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
Mtype |  Movement type = **5** Spring-loaded die |  1  
VectorX |  Unit direction vector for movement in X direction |  0.0  
VectorY |  Unit direction vector for movement in Y direction |  0.0  
VectorZ |  Unit direction vector for movement in Z direction |  0.0  
StiffnessTyp |  Type of spring stiffness 0 = Constant 1 = Defined function, force-displacement curve |  0  
Stiffness |  Stiffness value (StiffnessTyp=0) |  None  
NData |  Number of data pairs of load-displacement curve |   
CurDisp |  Current spring displacement |  None  
MaxDisp |  Maximum spring displacement |  None  
PreLoad |  Spring preload  |  None  
MountObj |  Spring is mounted with object # (0 if fixed) |  None  
Reversible |  Is spring reversible **0** = Non-reversible **1** = Reversible |  None  
Displ(i) |  Displacement of the ith position data pair |  None  
Force(i) |  Force of the ith position data pair |  None  
  
Arbitrary Path (Type=6)

* * *

MOVCTL Object, Mtype, Ctype(=1), FType, RotFlag, Ndata (if Ctype=1, Global coordinates)

Time/FeedRate(1), X(1), Y(1), Z(1), Angle(1)

::

Time/FeedRate(Ndata), X(Ndata), Y(Ndata), Z(Ndata), Angle(Ndata)

or

MOVCTL Object, Mtype, Ctype(=2), FType, RotFlag, Ndata (if Ctype=2, Local coordinates)

Ox, Oy, Oz

Ux, Uy, Uz, Vx, Vy, Vz

Time/FeedRate(1), U(1), V(1), Angle(1)

::

Time/FeedRate(Ndata), U(Ndata), V(Ndata), Angle(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
Mtype |  Movement type = **6** Arbitrary path controlled |  1  
Ctype |  Coordinate type = **1** Global = **2** Local | 1  
Ftype |  Function type = **1** function of time = **2** profile + feed rate = **-n** user subroutine, n |  1  
RotFlag |  Rotation flag (not yet implemented in FEM) = **0** No rotation =**1** Align head vector to the path |   
Ndata |  Number of data pairs to define path |   
Ox, Oy, Oz |  Origin vector to define local coordinate |   
Ux, Uy, Uz |  U vector to define local coordinate |   
Vx, Vy, Vz |  V vector to define local coordinate |   
Time(i) |  Time of the ith data pair |   
FeedRate(i) |  Feed rate of the ith data pair |   
X(i),Y(i),Z(i) |  Stroke of the ith data pair (global coordinate) |   
U(i),V(i) |  Stroke of the ith data pair (local coordinate) |   
Angle(i) |  Angle of the ith data pair |   
  
Hydraulic Press - Average Strain Rate Control (Type=7)

* * *

MOVCTL Object, Mtype(=7), Ftype(=0), VectorX, VectorY, VectorZ, AvgStnRt, MaxStnRt, CurBilHght

or

MOVCTL Object, Mtype(=7), Ftype, VectorX, VectorY, VectorZ, Ndata, MaxStnRt, CurBilHght

Stroke/Time(1), AvgStnRt(1)

::

Stroke/Time(Ndata), AvgStnRt(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Mtype |  Movement type = **7** Hydraulic press average strain rate controlled |  1  
Ftype |  Function type of controlled quantity = **0** Constant = **1** Primary stroke dependent = **2** Time dependent |  0  
AvgStnRt |  Average strain rate |  None  
Ndata |  Number of data pairs to specify the controlled function |  None  
VectorX |  Unit direction vector for movement in X direction |  0.0  
VectorY |  Unit direction vector for movement in Y direction |  0.0  
VectorZ |  Unit direction vector for movement in Z direction |  0.0  
Stroke/Time(i) |  Stroke or time of the ith data pair |  None  
AvgStnRt(i) |  Average strain rate of the ith data pair |  None  
MaxStnRt |  Maximum strain rate constraint |  None  
CurBilHght |  Current billet height |  0  
  
Hydraulic Press - Speed Control (Type=8)

* * *

MOVCTL Object, Mtype(=8), Ftype(=0), VectorX, VectorY, VectorZ, Speed, MaxStnRt

or

MOVCTL Object, Mtype(=8), Ftype, VectorX, VectorY, VectorZ, Ndata, MaxStnRt

Stroke/Time(1), Speed(1)

::

Stroke/Time(Ndata), Speed(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
Mtype |  Movement type = **8** Hydraulic press speed controlled |  1  
Ftype |  Function type of controlled quantity = **0** Constant = **1** Function of stroke = **2** Function of time |   
Speed |  Constant speed |  None  
Ndata |  Number of data pairs to specify the function |  None  
VectorX |  Unit direction vector for movement in X direction |  0.0  
VectorY |  Unit direction vector for movement in Y direction |  0.0  
VectorZ |  Unit direction vector for movement in Z direction |  0.0  
Stroke/Time(i) |  Stroke or time of the ith data pair |  None  
Speed(i) |  Speed of the ith data pair |  None  
  
Hydraulic Press - Power Limit Controlled (Type =9)

* * *

MOVCTL Object, Mtype(=9), VectorX, VectorY, VectorZ, MaxStnRt

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
Mtype |  Movement type = **9** Hydraulic press power limit controlled |  1  
VectorX |  Unit direction vector for movement in X direction |  0.0  
VectorY |  Unit direction vector for movement in Y direction |  0.0  
VectorZ |  Unit direction vector for movement in Z direction |  0.0  
MaxStnRt |  Maximum strain rate constraint |  0.0  
  
DEFINITION  
---  
MOVCTL (type=7~9) specifies the hydraulic press movement data.  
  
REMARKS  
---  
Hydraulic press (speed control) is the same as the speed controlled (Mtype = 1), except that it is should be used together with speed limit (SPDLMT). It is created for user interface convenience. Hydraulic press (power limit control) means to use the maximum power of the press. Therefore, the speed will be solely determined by the speed limit (SPDLMT).  
  
Pusher BCC (Type=11)

* * *

MOVCTL Object, Mtype(=11), SpeedX, SpeedY, SpeedZ

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
Mtype |  Movement type = **11** Pusher bcc specified movement control |  1  
SpeedX |  Current speed in X direction |  0.0  
SpeedY |  Current speed in Y direction |  0.0  
SpeedZ |  Current speed in Z direction |  0.0

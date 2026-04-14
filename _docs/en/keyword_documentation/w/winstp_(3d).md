---
lang: en
title: "WINSTP (3D)"
---

# WINSTP

|  (Simulation controls - 3D)  
---|---  
_Update History:_ New keyword in v12.1 |  Last updated on : 07-10-2024  
  
* * *

WINSTP Object, WinNo, WinShape, OprStopType, CriticalValueType, VelType   
{Velocity Data} (vx, vy, vz)  
{Window Data} (Coordinates of window control points)  
{Critical Value Data} (Contact area ratio) 

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
WinNo |  None |  1  
WinShape |  shape of the window = 1 Cuboid = 2 Cylinder |  1  
OprStopType |  Type of operation stopping = 0 Undefined = 1 Contact area ratio = 2 Folding |  1  
CriticalValueType |  Critical value function type = 0 Constant = 1 future extension |  0  
VelType {Window Data} |  Velocity of the window  
= 1 Constant < 0 follow object Window velocity/coordinates/etc… |  1  
  
DEFINITION  
---  
WINSTP specifies Stopping criteria for location specific contact area ratio and Fold.  
  
REMARKS  
---  
When "Contact area ratio" is selected, FEM simulation will stop if the workpiece surface area inside the window region reaches the defined contact ratio criteria. When Fold is selected, FEM simulation will stop if fold is detected on the workpiece surface inside the window region..  
  
RELATED TOPICS  
---  
[Stopping controls: 9.3.11 Stopping Window ](../../pre_processor/9_simulation_controls/9_3_stopping_controls.htm#9_3_10_Stopping_Window)

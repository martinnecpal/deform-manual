---
lang: en
title: "CNTRAX (2D)"
---

# CNTRAX

|  (Simulation control)  
---|---  
_Update History:_ V11.1 - XRotAxis and YRotAxis have been introduced for 2.5D rolling |  Last updated on : 25-04-2016  
  
* * *

CNTRAX Object, XCenter, YCenter, CurAngle, XRotAxis, YRotAxis

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
XCenter |  X coordinate of the center of rotational motion |  None  
YCenter |  Y coordinate of the center of rotational motion |  None  
CurAngle |  Current Angle of the Object in radians |  None  
XRotAxis |  X component of rotational axis (2.5D Rolling only) |  0  
YRotAxis |  Y component of rotational axis (2.5D Rolling only)  |  0  
  
DEFINITION  
---  
CNTRAX specifies the center of rotation for objects which move with a rotational velocity.  
  
REMARKS  
---  
Applicable object types: Rigid XRotAxis and YRotAxis are used only for GEOTYP = 5 (2.5D Rolling)  
  
RELATED TOPICS  
---  
Keywords: [ANGMOV(2D)](/docs/en/keyword_documentation/a/angmov/), [ANGMOV(3D)](../a/angmov\(3d\).htm),[MOVCTL (2D)](../m/movctl_\(2d\).htm), [MOVCTL (3D)](../m/movctl_\(3d\).htm), [GEOTYP(2D)](/docs/en/keyword_documentation/g/geotyp/)

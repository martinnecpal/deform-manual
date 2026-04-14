---
lang: en
title: "OBJPOS (3D)"
---

# OBJPOS

|  (Action keyword - 3D)  
---|---  
_**Update History:**_ 3DV6.1 - Drop positioning method (Method = 7,8,9) is supported v11 - Positioning method (methods = 13, 14) have been introduced for cogging application v11.1 - Positioning methods (methods = -1, 1002, 1012, 1102, 1112) have been added v11.1 - Positioning method (= 1) has been obsolete |  Last updated on : 22-10-2016  
  
* * *

OBJPOS Object method var1 var2 var3 var4 var5 var6 var7

or

OBJPOS Object method var1 var2 var3 var4 var5 var6 var7 N

Obj#1, obj#2, … , obj#N

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object  |  Object Number |  None  
Method  |  Positioning Method  **-1** = Offset (don't update stroke always)(new in v11.1) **1** = Offset (stroke will be updated only if mechanical press is defined) (obsolete in v11.1) **2** = Interference (stroke will be updated only if mechanical press is defined) **3** = Rotation **4** = Flip (place holder, not supported yet) **6** = Self-centered Rotation (uses center of the object bounding box) **7** = Drop **8** = Drop (Don’t allow rotation) **9** = Drop (Allow rotation along given axis) **11** = Offset (stroke will be updated always) **12** = Interference (stroke will be updated always) **13** = Reference positioning #1 (new in v11) **14** = Reference positioning #2(new in v11) **102** = same as 1 but don’t move before positioning **112** = same as 12 but don’t move before positioning **1002** = same as 2 but update sliding die current displacement (new in v11.1) **1012** = same as 12 but update sliding die current displacement (new in v11.1) **1102** = same as 102 but update sliding die current displacement (new in v11.1) **1112** = same as 112 but update sliding die current displacement (new in v11.1) |  None  
(if Method =-1 or 11)  
var1, var2, var3  |  X, Y, Z distance |   
(if Method = 2 or 12 or 102 or 112)  
var1  var2, var3, var4  var5 |  Interference Direction (Vx, Vy, Vz) Reference Object |   
(if Method = 3)  
var1, var2, var3 var4, var5, var6 var7 |  A point of rotational axis (X, Y, Z) Rotational axis direction vector (X, Y, Z) Rotational angle (in degrees) |   
(if Method = 6)  
var1, var2, var3  var4 |  Rotational axis direction vector (X, Y, Z) Rotational angle (in degrees) |   
(if Method = 7 or 8)  
var1  var2, var3, var4 |  Interference limit Drop direction (Vx, Vy, Vz) |   
(if Method = 9)  
var1  var2, var3, var4  var5, var6, var7  |  Interference limit Drop direction (Vx, Vy, Vz) Rotational axis direction vector (X, Y, Z) |   
(if Method = 13)  
var1  var2, var3, var4  var5 var6 var7 |  Tolerance Reference Direction (Vx, Vy, Vz) Reference Object Reference Type = **0** Abs distance = **1** Percentage = **2** Node number Distance / Percent / Node number |   
(if Method = 14)  
var1  var2  var3 var4 N |  Second positioning object Reference Object clamp type = **0** Clamp = **1** Unclamp Interference (for clamping) or offset (for unclamping) Number of coupled objects  |   
  
DEFINITION  
---  
OBJPOS positions objects specified by the variables in the keyword.  
  
REMARKS  
---  
OBJPOS is an action keyword that positions objects when it is read in to the Pre-Processor. This keywords main use is for multiple operations. If N is not zero, OBJPOS will perform coupled positioning and read second line which is the list of object numbers. (Supported from 3DV6.1 beta) Positioning method (method = 13) uses the reference object for positioning in cogging simulation. Positioning method (method = 14) has been introduced to handle clamping and unclamping for manipulators using reference object in 3D cogging simulation.  
  
RELATED TOPICS  
---  
[Object Positioning](/docs/en/pre_processor/19_object_positioning/19_object_positioning/)

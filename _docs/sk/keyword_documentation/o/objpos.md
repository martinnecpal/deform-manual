---
lang: sk
title: "OBJPOS (2D)"
---

# OBJPOS

|  (Action Keyword - 2D)  
---|---  
_Update History:_ v11.1 - Positioning methods (methods = -1, 1002, 1012, 1102, 1112) have been added v11.1 - Positioning method (= 1) has been obsolete |  Last updated on : 14-05-2016  
  
* * *

OBJPOS Object method var1 var2 var3 var4

Or

OBJPOS Object method var1 var2 var3 var4 N

Obj#1, obj#2, … , obj#N

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
Method |  Positioning Method **-1** = Offset (don't update stroke always)(new in v11.1) **1** = Offset (stroke will be updated only if mechanical press is defined) (obsolete in v11.1) **2** = Interference (stroke will be updated only if mechanical press is defined) **3** = Rotation **4** = Flip **5**(obsolete) = Move the same distance as previous OBJPOS (Please use coupled positioning instead) **6** = Self-centered Rotation (uses center of the object bounding box) **11** = Offset (stroke will be updated always) **12** = Interference (stroke will be updated always) **102** = same as 1 but don’t move before positioning **112** = same as 12 but don’t move before positioning **1002** = same as 2 but update sliding die current displacement (new in v11.1) **1012** = same as 12 but update sliding die current displacement (new in v11.1) **1102** = same as 102 but update sliding die current displacement (new in v11.1) **1112** = same as 112 but update sliding die current displacement (new in v11.1) |  None  
if Method = -1 or 11:  
var1, var2 |  X, Y distance |   
if Method = 2 or 12 or 102 or 112:  
var1 |  Interference |   
var2 |  Reference Object |   
var3, var4 |  Direction vector (X,Y) |   
if Method = 3:  
var1, var2 |  Rotation center (X, Y) |   
var3 |  Rotation Angle |   
if Method = 4:  
var1, var2 |  Start point X1, Y1 |   
var3, var4 |  End point X2, Y2 |   
if Method = 6:  
var1  |  Rotation angle |   
N  |  Number of coupled objects |  0  
  
DEFINITION  
---  
OBJPOS positions objects specified by the variables in the keyword.  
  
REMARKS  
---  
OBJPOS is an action keyword that positions objects when it is read in to the Pre-Processor. This keywords main use is for multiple operations. For flipping, the object is flipped with respect to a line crossing point (X1, Y1) and (X2, Y2). If N is not zero, OBJPOS will perform coupled positioning and read second line which is the list of object numbers. (supported from 2DV9.1 beta)  
  
RELATED TOPICS  
---  
[Object Positioning](/docs/sk/pre_processor/19_object_positioning/19_object_positioning/)

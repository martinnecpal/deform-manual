---
lang: sk
title: "CSPMTX (3D)"
---

# CSPMTX

|  (Object data - 3D only)  
---|---  
_Update History:_ V6.1 sp3 - CSPMTX was introduced. |  Last updated on : 12-08-2013  
  
* * *

CSPMTX Object, nMode  
1, TranMatrix(1.1),.., TranMatrix(1.4)

: : :

4, TranMatrix(4.1),.., TranMatrix(4.4)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
nMode |  No. of Data Pairs |  1  
TranMatrix(i,j) |  Transformation matrix at (i,j)the location |  None  
  
DEFINITION  
---  
CSPMTX: This keyword is to save the transformation matrix of the sketch plane, usually 2D cross-sectional shape of roll object. (nMode =1 is only available) TranMatrix(4.4) specifies the transformation matrix which is used to recover roll cross-sectional shape in 3D space for shape rolling applications.  
  
REMARKS  
---  
In the shape rolling template, 2D roll cross-sectional geometry is saved in each task folder. When it is saved, [DIEGEO](/docs/sk/keyword_documentation/d/diegeo_3d/), TPLOGY, CSPMTX are saved together in “ShapeRoll2DGeo.KEY” file. Applicable object types: Roll objects in Shape Rolling  
  
RELATED TOPICS  
---  
Keywords: [DIEGEO (2D)](/docs/sk/keyword_documentation/d/diegeo/), [DIEGEO(3D)](/docs/sk/keyword_documentation/d/diegeo_3d/), [TPLOGY(2D)](/docs/sk/keyword_documentation/t/tplogy/)

---
lang: sk
title: "GENSUB (3D)"
---

# GENSUB

|  (Action keyword - 3D only)  
---|---  
_Update History:_ V11 - GENSUB has been introduced. |  Last updated on : 13-08-2013  
  
* * *

GENSUB Object, SubDivision

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
SubDivision |  = **+ve** Edge length; = **-ve** Aspect ratio |   
  
DEFINITION  
---  
GENSUB is applicable to brick mesh only and is used for axial subdivision. Positive value means subdivision will be done if the minimum edge length in X-direction is greater than the given value. Negative value means subdivision will be done if the element aspect ratio in X-direction is greater than the given value.  
  
REMARKS  
---  
GENSUB is an action keyword and is mainly for internal use. It is used in the cogging template for axial subdivision. Applicable simulation types: Cogging  
  
RELATED TOPICS  
---  
Related keywords: GENAXS, EXECMD

---
lang: sk
title: "CURRNT (3D)"
---

# CURRNT

|  (Object data - 3D)  
---|---  
_Update History:_ V11.1 – CURRNT has been introduced for 3D. |  Last updated on : 21-05-2016  
  
* * *

CURRNT Object, Ndata, DefCURRNT

Element(1), CURRNT_x(1), CURRNT_y(1), CURRNT_z(1)

: :

Element(Ndata), CURRNT_x(Ndata), CURRNT_y(Ndata), CURRNT_z(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Ndata |  Number of element/CURRNT pairs |  None  
DefCURRNT |  Default elemental CURRNT of all elements not listed |  0.0  
Element(i) |  Element number of ith data pair |  None  
CURRNT_x(i) |  Electric current flux x component |  0.0  
CURRNT_y(i) |  Electric current flux y component |  0.0  
CURRNT_z(i) |  Electric current flux z component |  0.0  
  
DEFINITION  
---  
CURRNT is the calculated electric current flux at each element center.  
  
REMARKS  
---  
Electric current flux at element center is a vector. This state variable is used in simulations of resistance heating.  
  
RELATED TOPICS  
---  
None

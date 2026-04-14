---
lang: sk
title: "CURRNT (2D)"
---

# CURRNT

|  (Object data - 2D)  
---|---  
|  Last updated on : 29-07-2013  
  
* * *

CURRNT Object, Ndata, DefCURRNT

Element(1), CURRNT_x(1), CURRNT_y(1)

: :

Element(Ndata), CURRNT_x(Ndata), CURRNT_y(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Ndata |  Number of element/CURRNT pairs |  None  
DefCURRNT |  Default elemental CURRNT of all elements not listed in the element/CURRNT pairs |  0  
Element(i) |  Element number of ith data pair |  None  
CURRNT_x(i) |  Electric current flux x component |  0  
CURRNT_y(i) |  Electric current flux y component |  0  
  
DEFINITION  
---  
CURRNT is the calculated electric current flux at each element center.  
  
REMARKS  
---  
Electric current flux at element center is a vector. This state variable is used in simulations of resistance heating.  
  
RELATED TOPICS  
---  
[Simulation Mode](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#9.1.5._Simulation_modes_\(SMODE,_TRANS\)): Heat transfer, Heating, Induction Keywords: [ZEFI](/docs/sk/keyword_documentation/z/zefi/), [ZMFI](/docs/sk/keyword_documentation/z/zmfi/)

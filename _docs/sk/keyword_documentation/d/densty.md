---
lang: sk
title: "DENSTY (2D3D)"
---

# DENSTY

|  (Object data)  
---|---  
|  Last updated on : 29-07-2013  
  
* * *

DENSTY Object, Ndata, DefDensity

Element(1), Density(1)

: :

Element(Ndata), Density(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Ndata |  Number of element/density data pairs |  None  
DefDensity |  Default relative density of all elements not listed in the element/density data pairs. |  1  
Element(i) |  Element number of ith data pair |  None  
Density(i) |  Relative density of ith data pair |  1  
  
DEFINITION  
---  
DENSTY specifies the relative density of the material at each element.  
  
REMARKS  
---  
DENSTY is used when a porous material with relative densities less than 1.0 is being simulated. If no value is specified for DefDensity, it is assumed to be 1.0. The flow stress of porous objects should be specified for the fully dense material. Applicable object types: [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
[Object Elemental Data](/docs/sk/pre_processor/17_object_data_initialization/17_2_element_data_window/)

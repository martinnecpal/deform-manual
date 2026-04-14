---
lang: sk
title: "MTLGRP (2D3D)"
---

# MTLGRP

|  (Object data)  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

MTLGRP Object, Ndata, DefMaterial

Element(1), Material(1)

: :

Element(Ndata), Material(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Ndata |  Number of element/material data pairs |  None  
DefMaterial |  Default material number of all elements not listed in the element/material pairs. |  1  
Element(i) |  Element number of ith data pair |  None  
Material(i) |  Material number of ith data pair |  1  
  
DEFINITION  
---  
MTLGRP specifies the material number associated with each element.  
  
REMARKS  
---  
Each material number represents a set of material properties used to simulate the material behavior. An object may be comprised of elements having different material properties. Applicable Object types: [Rigid](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.5._Rigid), [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
[Material properties](/docs/sk/pre_processor/10_material_data/10_material_data/) Keywords: [EMSVTY](/docs/sk/keyword_documentation/e/emsvty/), [EXPAND](/docs/sk/keyword_documentation/e/expand/), [FRAE2H](/docs/sk/keyword_documentation/f/frae2h/), [FSTRES](/docs/sk/keyword_documentation/f/fstres/), [HEATCP](/docs/sk/keyword_documentation/h/heatcp/), [MTNAME](/docs/sk/keyword_documentation/m/mtname/), [POISON](/docs/sk/keyword_documentation/p/poison/), [YOUNG](/docs/sk/keyword_documentation/y/young/)

---
lang: en
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
Each material number represents a set of material properties used to simulate the material behavior. An object may be comprised of elements having different material properties. Applicable Object types: [Rigid]({{ '/docs/en/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.5._Rigid), [Elastic]({{ '/docs/en/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.2._Elastic), [Plastic]({{ '/docs/en/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.1_Plastic), [Elastoplastic]({{ '/docs/en/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.3._Elasto-plastic), and [Porous]({{ '/docs/en/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.4._Porous).  
  
RELATED TOPICS  
---  
[Material properties]({{ '/docs/en/pre_processor/10_material_data/10_material_data/' | relative_url }}) Keywords: [EMSVTY]({{ '/docs/en/keyword_documentation/e/emsvty/' | relative_url }}), [EXPAND]({{ '/docs/en/keyword_documentation/e/expand/' | relative_url }}), [FRAE2H]({{ '/docs/en/keyword_documentation/f/frae2h/' | relative_url }}), [FSTRES]({{ '/docs/en/keyword_documentation/f/fstres/' | relative_url }}), [HEATCP]({{ '/docs/en/keyword_documentation/h/heatcp/' | relative_url }}), [MTNAME]({{ '/docs/en/keyword_documentation/m/mtname/' | relative_url }}), [POISON]({{ '/docs/en/keyword_documentation/p/poison/' | relative_url }}), [YOUNG]({{ '/docs/en/keyword_documentation/y/young/' | relative_url }})

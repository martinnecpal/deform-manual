---
lang: sk
title: "HDNOBJ (2D3D)"
---

# HDNOBJ

|  (Object data)  
---|---  
|  Last updated on : 13-08-2013  
  
* * *

HDNOBJ Obj# #elem default

1 hardness(1) cool time(1)

. . . . .

. . . . .

n hardness(n) cool time(n)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Obj# |  Object number |  NONE  
#elem |  Number of elements |  NONE  
default |  Default value of hardness |  0.0  
hardness(n) |  Hardness value of element n |  0.0  
cool time(n) |  Cooling time for element n |  0.0  
  
DEFINITION  
---  
HDNOBJ stores the hardness value and cooling time for each element. The manner on which values are used for the estimation of hardness depends on the keyword HDNEST. If hardness calculations are not performed, both the hardness values and cooling times will be written as zero values.  
  
REMARKS  
---  
Applicable Simulation Modules: Microstructure Applicable Simulation Modes: Transformation Applicable object types: ALL Object types  
  
RELATED TOPICS  
---  
[Object Element Data]({{ '/docs/sk/pre_processor/17_object_data_initialization/17_2_element_data_window/' | relative_url }}): Hardness, Material Data: [Hardness]({{ '/docs/sk/pre_processor/10_material_data/10_7_hardness_data/10_7_hardness_data/' | relative_url }}) Keyword: [HDNEST]({{ '/docs/sk/keyword_documentation/h/hdnest/' | relative_url }}), [HDNTIM]({{ '/docs/sk/keyword_documentation/h/hdntim/' | relative_url }}), [JOMINY]({{ '/docs/sk/keyword_documentation/j/jominy/' | relative_url }}), [HDNPHA]({{ '/docs/sk/keyword_documentation/h/hdnpha/' | relative_url }})

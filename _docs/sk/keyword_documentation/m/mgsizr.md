---
lang: sk
title: "MGSIZR (2D3D)"
---

# MGSIZR

|  (Object data)  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

MGSIZR Object, SizeRatio

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
SizeRatio |  Size ratio of largest to the smallest element |  2.0  
  
DEFINITION  
---  
MGSIZR controls the ration of the largest to the smallest element size in areas which are being assigned additional elements based on weighted parameters.  
  
REMARKS  
---  
MGSIZR is one of several keywords used to control the mesh density during AMG mesh generation. If equal sized elements are desired, then SizeRatio = 1. If SizeRatio = 0, the element size ratio will not be a factor in the mesh density distribution. Applicable object types: [Rigid]({{ '/docs/sk/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.5._Rigid), [Elastic]({{ '/docs/sk/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.2._Elastic), [Plastic]({{ '/docs/sk/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.1_Plastic), [Elastoplastic]({{ '/docs/sk/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.3._Elasto-plastic), and [Porous]({{ '/docs/sk/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.4._Porous).  
  
RELATED TOPICS  
---  
Automatic mesh generation, Automatic remeshing Keywords: [MGGRID]({{ '/docs/sk/keyword_documentation/m/mggrid/' | relative_url }}), [MGERR]({{ '/docs/sk/keyword_documentation/m/mgerr/' | relative_url }}), [MGNELM]({{ '/docs/sk/keyword_documentation/m/mgnelm/' | relative_url }}), [MGSIZR](), [MGWCUV]({{ '/docs/sk/keyword_documentation/m/mgwcuv/' | relative_url }}), [MGWTMP]({{ '/docs/sk/keyword_documentation/m/mgwtmp/' | relative_url }}), [MGWSTN]({{ '/docs/sk/keyword_documentation/m/mgwstn/' | relative_url }}), [MGWSTR]({{ '/docs/sk/keyword_documentation/m/mgwstr/' | relative_url }})

---
lang: en
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
MGSIZR is one of several keywords used to control the mesh density during AMG mesh generation. If equal sized elements are desired, then SizeRatio = 1. If SizeRatio = 0, the element size ratio will not be a factor in the mesh density distribution. Applicable object types: [Rigid](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.5._Rigid), [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
Automatic mesh generation, Automatic remeshing Keywords: [MGGRID](/docs/en/keyword_documentation/m/mggrid/), [MGERR](/docs/en/keyword_documentation/m/mgerr/), [MGNELM](/docs/en/keyword_documentation/m/mgnelm/), [MGSIZR](), [MGWCUV](/docs/en/keyword_documentation/m/mgwcuv/), [MGWTMP](/docs/en/keyword_documentation/m/mgwtmp/), [MGWSTN](/docs/en/keyword_documentation/m/mgwstn/), [MGWSTR](/docs/en/keyword_documentation/m/mgwstr/)

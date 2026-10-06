---
lang: en
title: "MGNELM (2D)"
---

# MGNELM

|  (Object data - 2D)  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

MGNELM Object, NumElem

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
NumElem |  Number of elements in new mesh |  500  
  
DEFINITION  
---  
MGNELM specifies the approximate number of elements to be generated when an object is being meshed using AMG.  
  
REMARKS  
---  
MGNELM is one of several keywords used to control the mesh density during automatic remeshing. The error between the number of specified elements and the number of generated elements is typically on the order of ten percent. When the mesh is generated, the specified total number of elements is used in conjunction with the "Point" and "Parameter" controls to determine the mesh density. Applicable object types: [Rigid]({{ '/docs/en/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.5._Rigid), [Elastic]({{ '/docs/en/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.2._Elastic), [Plastic]({{ '/docs/en/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.1_Plastic), [Elastoplastic]({{ '/docs/en/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.3._Elasto-plastic), and [Porous]({{ '/docs/en/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.4._Porous).  
  
RELATED TOPICS  
---  
Automatic mesh generation, Automatic [remeshing]({{ '/docs/en/pre_processor/9_simulation_controls/9_4_remesh_criteria/' | relative_url }}) Keywords: [MGGRID]({{ '/docs/en/keyword_documentation/m/mggrid/' | relative_url }}), [MGERR]({{ '/docs/en/keyword_documentation/m/mgerr/' | relative_url }}), [MGTELM]({{ '/docs/en/keyword_documentation/m/mgtelm/' | relative_url }}), [MGSIZR]({{ '/docs/en/keyword_documentation/m/mgsizr/' | relative_url }}), [MGWCUV]({{ '/docs/en/keyword_documentation/m/mgwcuv/' | relative_url }}), [MGWTMP]({{ '/docs/en/keyword_documentation/m/mgwtmp/' | relative_url }}), [MGWSTN]({{ '/docs/en/keyword_documentation/m/mgwstn/' | relative_url }}), [MGWSTR]({{ '/docs/en/keyword_documentation/m/mgwstr/' | relative_url }})

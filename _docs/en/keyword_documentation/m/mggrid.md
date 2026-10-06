---
lang: en
title: "MGGRID (2D3D)"
---

# MGGRID

|  (Object data)  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

MGGRID Object, XDivision, YDivision

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
XDivision |  Number of grid divisions in X |  25  
YDivision |  Number of grid divisions in Y |   
  
DEFINITION  
---  
MGGRID specifies the spacing of the sampling grids which are used to sample mesh densities.  
  
REMARKS  
---  
MGGRID is one of several keywords used to control the mesh density when AMG mesh generation is being performed. Increasing the value of Xdivision and Ydivision will result in sharper gradients between areas of differing mesh density. Applicable object types: [Rigid](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.5._Rigid), [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
Automatic mesh generation, Automatic [remeshing]({{ '/docs/en/pre_processor/9_simulation_controls/9_4_remesh_criteria/' | relative_url }}). Keywords: [MGERR]({{ '/docs/en/keyword_documentation/m/mgerr/' | relative_url }}), [MGNELM (2D)]({{ '/docs/en/keyword_documentation/m/mgnelm/' | relative_url }}),[MGNELM (3D)]({{ '/docs/en/keyword_documentation/m/mgnelm_3d/' | relative_url }}), [MGTELM]({{ '/docs/en/keyword_documentation/m/mgtelm/' | relative_url }}), [MGSIZR]({{ '/docs/en/keyword_documentation/m/mgsizr/' | relative_url }}), [MGWCUV]({{ '/docs/en/keyword_documentation/m/mgwcuv/' | relative_url }}), [MGWTMP]({{ '/docs/en/keyword_documentation/m/mgwtmp/' | relative_url }}), [MGWSTN]({{ '/docs/en/keyword_documentation/m/mgwstn/' | relative_url }}), [MGWSTR]({{ '/docs/en/keyword_documentation/m/mgwstr/' | relative_url }})

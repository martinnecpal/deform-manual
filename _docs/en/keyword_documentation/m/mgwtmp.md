---
lang: en
title: "MGWTMP (2D3D)"
---

# MGWTMP

|  (Object Data)  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

MGWTMP Object, WtStrain

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
WtTemp |  Weight associated with the nodal temperature when generating a mesh using AMG |  0.0  
  
DEFINITION  
---  
MGWTMP specifies the element density weight to be associated with the nodal temperature values when an object is being meshed using AMG.  
  
REMARKS  
---  
MGWTMP is one of several keywords used to control the mesh density during AMG mesh generation. The values from all the mesh density keywords are combined during the mesh generation process to create a mesh density distribution within the geometric boundary. The keywords [MGWCUV]({{ '/docs/en/keyword_documentation/m/mgwcuv/' | relative_url }}), [MGWSTN]({{ '/docs/en/keyword_documentation/m/mgwstn/' | relative_url }}), [MGWSTR]({{ '/docs/en/keyword_documentation/m/mgwstr/' | relative_url }}), [MGWTMP](), and MGWUSR specify relative mesh density weights to be assigned to the associated keyword parameter (curvature, strain, strain rate, temperature, and user defined area). The value of WtTemp specifies the emphasis to be placed on the nodal temperature gradients as a parameter for determining mesh density during a remeshing. If WtTemp > 0, the mesh density will be allocated so that areas with the highest temperature gradients will receive a higher mesh density than areas with a lower temperature gradients. If WtTemp = 0, nodal temperature will not be used to determine the mesh density. MGWTMP should only be used when a mesh with previous nodal temperature values is being remeshed. Applicable Object types: [Rigid]({{ '/docs/en/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.5._Rigid), [Elastic]({{ '/docs/en/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.2._Elastic), [Plastic]({{ '/docs/en/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.1_Plastic), [Elastoplastic]({{ '/docs/en/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.3._Elasto-plastic), and [Porous]({{ '/docs/en/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.4._Porous).  
  
RELATED TOPICS  
---  
[Mesh]({{ '/docs/en/pre_processor/13_mesh_generation/13_mesh_generation/' | relative_url }}): Mesh weighting factors Keywords: [MGWSTN]({{ '/docs/en/keyword_documentation/m/mgwstn/' | relative_url }}), [MGWSTR]({{ '/docs/en/keyword_documentation/m/mgwstr/' | relative_url }}), [MGWCUV]({{ '/docs/en/keyword_documentation/m/mgwcuv/' | relative_url }}), [MGWUSR]({{ '/docs/en/keyword_documentation/m/mgwusr/' | relative_url }}), [MGNELM]({{ '/docs/en/keyword_documentation/m/mgnelm/' | relative_url }}), [MGGRID]({{ '/docs/en/keyword_documentation/m/mggrid/' | relative_url }}), [MGERR]({{ '/docs/en/keyword_documentation/m/mgerr/' | relative_url }}), [MGTELM]({{ '/docs/en/keyword_documentation/m/mgtelm/' | relative_url }}), [MGSIZR]({{ '/docs/en/keyword_documentation/m/mgsizr/' | relative_url }})

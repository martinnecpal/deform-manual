---
lang: sk
title: "MGWCUV (2D3D)"
---

# MGWCUV

|  (Action keyword)  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

MGWCUV Object, WtCurve

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
WtCurve |  Weight associated with boundary curvature when generating a mesh with AMG |  None  
  
DEFINITION  
---  
MGWCUV specifies the element density weight to be associated with the boundary curvature when an object is being meshed using AMG.  
  
REMARKS  
---  
MGWCUV is one of several keywords used to control the mesh density during AMG mesh generation. The values from all the mesh density keywords are combined during the mesh generation process to create a mesh density distribution within the geometric boundary. The keywords [MGWCUV](), [MGWSTN]({{ '/docs/sk/keyword_documentation/m/mgwstn/' | relative_url }}), [MGWSTR]({{ '/docs/sk/keyword_documentation/m/mgwstr/' | relative_url }}), [MGWTMP]({{ '/docs/sk/keyword_documentation/m/mgwtmp/' | relative_url }}), and MGWUSR specify relative mesh density weights to be assigned to the associated keyword parameter (curvature, strain, strain rate, temperature, and user defined area). If WtCurve > 0, the mesh density will be allocated so that areas with the greatest boundary curvature receive a higher mesh density than areas with lower curvature. If WtCurve < 0, boundary curvature will not be used to determine the mesh density. Applicable object types: [Rigid]({{ '/docs/sk/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.5._Rigid), [Elastic]({{ '/docs/sk/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.2._Elastic), [Plastic]({{ '/docs/sk/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.1_Plastic), [Elastoplastic]({{ '/docs/sk/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.3._Elasto-plastic), and [Porous]({{ '/docs/sk/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.4._Porous).  
  
RELATED TOPICS  
---  
Mesh: Mesh weighting factors Keywords: [MGWTMP]({{ '/docs/sk/keyword_documentation/m/mgwtmp/' | relative_url }}), [MGWSTN]({{ '/docs/sk/keyword_documentation/m/mgwstn/' | relative_url }}), [MGWSTR]({{ '/docs/sk/keyword_documentation/m/mgwstr/' | relative_url }}), [MGWUSR(2D)]({{ '/docs/sk/keyword_documentation/m/mgwusr/' | relative_url }}), [MGWUSR(3D)]({{ '/docs/sk/keyword_documentation/m/mgwusr_3d/' | relative_url }}), [MGNELM(2D)]({{ '/docs/sk/keyword_documentation/m/mgnelm/' | relative_url }}), [MGNELM(3D)]({{ '/docs/sk/keyword_documentation/m/mgnelm_3d/' | relative_url }}), [MGGRID]({{ '/docs/sk/keyword_documentation/m/mggrid/' | relative_url }}), [MGERR]({{ '/docs/sk/keyword_documentation/m/mgerr/' | relative_url }}), [MGTELM]({{ '/docs/sk/keyword_documentation/m/mgtelm/' | relative_url }}), [MGSIZR]({{ '/docs/sk/keyword_documentation/m/mgsizr/' | relative_url }})

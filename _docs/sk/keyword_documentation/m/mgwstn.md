---
lang: sk
title: "MGWSTN (2D3D)"
---

# MGWSTN

|  (Object data)  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

MGWSTN Object, WtStrain

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
WtStrain |  Weight associated with the elemental strain gradient when generating a mesh using AMG |  0.0  
  
DEFINITION  
---  
MGWSTN specifies the element density weight to be associated with the elemental strain values when an object is being meshed using AMG.  
  
REMARKS  
---  
MGWSTN is one of several keywords used to control the mesh density during AMG mesh generation. The values from all the mesh density keywords are combined during the mesh generation process to create a mesh density distribution within the geometric boundary. The keywords [MGWCUV]({{ '/docs/sk/keyword_documentation/m/mgwcuv/' | relative_url }}), [MGWSTN](), [MGWSTR]({{ '/docs/sk/keyword_documentation/m/mgwstr/' | relative_url }}), [MGWTMP]({{ '/docs/sk/keyword_documentation/m/mgwtmp/' | relative_url }}), and MGWUSR specify relative mesh density weights to be assigned to the associated keyword parameter (curvature, strain, strain rate, temperature, and user defined area). When an object is deformed, strain is recorded at the element center. When a remeshing is performed, the value of WtStrain specifies the emphasis to be placed on the elemental strain interpolation error as a parameter for determining mesh density during a remeshing. If WtStrain > 0, the mesh density will be allocated so that areas with the greatest strain gradient will receive a higher mesh density than areas with a lower strain gradient. If WtCurve < 0, elemental strain will not be used to determine the mesh density. Applicable Object types: [Rigid]({{ '/docs/sk/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.5._Rigid), [Elastic]({{ '/docs/sk/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.2._Elastic), [Plastic]({{ '/docs/sk/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.1_Plastic), [Elastoplastic]({{ '/docs/sk/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.3._Elasto-plastic), and [Porous]({{ '/docs/sk/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.4._Porous).  
  
RELATED TOPICS  
---  
[Mesh]({{ '/docs/sk/pre_processor/13_mesh_generation/13_mesh_generation/' | relative_url }}): Mesh weighting factors Keywords: [MGWTMP]({{ '/docs/sk/keyword_documentation/m/mgwtmp/' | relative_url }}), [MGWCUV]({{ '/docs/sk/keyword_documentation/m/mgwcuv/' | relative_url }}), [MGWSTR]({{ '/docs/sk/keyword_documentation/m/mgwstr/' | relative_url }}), [MGWUSR (2D)]({{ '/docs/sk/keyword_documentation/m/mgwusr/' | relative_url }}), [MGWUSR (3D)]({{ '/docs/sk/keyword_documentation/m/mgwusr_3d/' | relative_url }}),[MGNELM (2D)]({{ '/docs/sk/keyword_documentation/m/mgnelm/' | relative_url }}), [MGNELM (3D)]({{ '/docs/sk/keyword_documentation/m/mgnelm_3d/' | relative_url }}) , [MGGRID]({{ '/docs/sk/keyword_documentation/m/mggrid/' | relative_url }}), [MGERR]({{ '/docs/sk/keyword_documentation/m/mgerr/' | relative_url }}), [MGTELM]({{ '/docs/sk/keyword_documentation/m/mgtelm/' | relative_url }}), [MGSIZR]({{ '/docs/sk/keyword_documentation/m/mgsizr/' | relative_url }})

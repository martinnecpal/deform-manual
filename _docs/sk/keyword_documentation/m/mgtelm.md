---
lang: sk
title: "MGTELM (2D3D)"
---

# MGTELM

|  (Object data)  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

MGTELM Object, ElemThick

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
ElemThick |  Number of elements through the geometric thickness of the object. |  4  
  
DEFINITION  
---  
MGTELM specifies the number of elements through the geometric thickness of an object to be generated when an object is being meshed using AMG.  
  
REMARKS  
---  
MGTELM is one of several keywords used to control the mesh density during AMG mesh generation. The thickness direction of an object is perpendicular to the geometry center which is defined by the medial axis. The total number of elements to be generated in a mesh is controlled by the value of NumElem in keyword MGNELM. If the value of ElemThick results in a mesh that contains more than NumElem elements, the value of ElemThick will be scaled down so that the mesh contains approximately NumElem elements. If the value of ElemThick results in a mesh that contains fewer than NumElem elements, the remaining elements will be distributed to other user specified mesh density controls (curvature, strain, strain rate, and temperature). Applicable object types: [Rigid](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.5._Rigid), [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
Automatic mesh generation, Automatic remeshing Keywords: [MGGRID](/docs/sk/keyword_documentation/m/mggrid/), [MGERR](/docs/sk/keyword_documentation/m/mgerr/), [MGNELM](/docs/sk/keyword_documentation/m/mgnelm/), [MGSIZR](/docs/sk/keyword_documentation/m/mgsizr/), [MGWCUV](/docs/sk/keyword_documentation/m/mgwcuv/), [MGWTMP](/docs/sk/keyword_documentation/m/mgwtmp/), [MGWSTN](/docs/sk/keyword_documentation/m/mgwstn/), [MGWSTR](/docs/sk/keyword_documentation/m/mgwstr/)

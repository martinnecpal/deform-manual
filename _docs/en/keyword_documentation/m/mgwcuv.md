---
lang: en
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
MGWCUV is one of several keywords used to control the mesh density during AMG mesh generation. The values from all the mesh density keywords are combined during the mesh generation process to create a mesh density distribution within the geometric boundary. The keywords [MGWCUV](), [MGWSTN](/docs/en/keyword_documentation/m/mgwstn/), [MGWSTR](/docs/en/keyword_documentation/m/mgwstr/), [MGWTMP](/docs/en/keyword_documentation/m/mgwtmp/), and MGWUSR specify relative mesh density weights to be assigned to the associated keyword parameter (curvature, strain, strain rate, temperature, and user defined area). If WtCurve > 0, the mesh density will be allocated so that areas with the greatest boundary curvature receive a higher mesh density than areas with lower curvature. If WtCurve < 0, boundary curvature will not be used to determine the mesh density. Applicable object types: [Rigid](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.5._Rigid), [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
Mesh: Mesh weighting factors Keywords: [MGWTMP](/docs/en/keyword_documentation/m/mgwtmp/), [MGWSTN](/docs/en/keyword_documentation/m/mgwstn/), [MGWSTR](/docs/en/keyword_documentation/m/mgwstr/), [MGWUSR(2D)](/docs/en/keyword_documentation/m/mgwusr/), [MGWUSR(3D)](/docs/en/keyword_documentation/m/mgwusr_3d/), [MGNELM(2D)](/docs/en/keyword_documentation/m/mgnelm/), [MGNELM(3D)](/docs/en/keyword_documentation/m/mgnelm_3d/), [MGGRID](/docs/en/keyword_documentation/m/mggrid/), [MGERR](/docs/en/keyword_documentation/m/mgerr/), [MGTELM](/docs/en/keyword_documentation/m/mgtelm/), [MGSIZR](/docs/en/keyword_documentation/m/mgsizr/)

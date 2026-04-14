---
lang: en
title: "MGERR (2D3D)"
---

# MGERR

|  (Object data)  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

MGERR Object, MaxDistance, MaxAngle

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Distance |  Distance tolerance for critical nodes |  0.01  
Angle |  Angle tolerance for critical nodes |  31.5  
  
DEFINITION  
---  
MGERR specifies the maximum distance and angle error permitted between the object boundary and its associated grid element side.  
  
REMARKS  
---  
MGERR is one of several keywords used to control the mesh density when AMG mesh generation is performed. The distance and angle tolerances are used to capture critical boundary geometry that might otherwise be lost when the mesh is generated. Applicable object types: [Rigid](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.5._Rigid), [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
Automatic mesh generation, Automatic [remeshing](/docs/en/pre_processor/9_simulation_controls/9_4_remesh_criteria/). Keywords: [MGGRID](/docs/en/keyword_documentation/m/mggrid/),[MGNELM (2D)](/docs/en/keyword_documentation/m/mgnelm/),[MGNELM (3D)](/docs/en/keyword_documentation/m/mgnelm_3d/) , [MGTELM](/docs/en/keyword_documentation/m/mgtelm/), [MGSIZR](/docs/en/keyword_documentation/m/mgsizr/), [MGWCUV](/docs/en/keyword_documentation/m/mgwcuv/), [MGWTMP](/docs/en/keyword_documentation/m/mgwtmp/), [MGWSTN](/docs/en/keyword_documentation/m/mgwstn/), [MGWSTR](/docs/en/keyword_documentation/m/mgwstr/)

---
lang: en
title: "MGWUSR (3D)"
---

# MGWUSR

|  (Object Data - 3D)  
---|---  
|  Last updated on : 13-08-2013  
  
* * *

MGWUSR Object, WtUser, DensityVal, SwitchVal 

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
WtUser |  Weight associated with the user defined area |  0.0  
DensityVal |  Global density value |  1.0  
SwitchVal |  Toggle parameter between absolute and relative densities SwitchVal =**0.0** (absolute) SwitchVal = **1.0** (relative) |  1.0  
  
DEFINITION  
---  
MGWUSR specifies the element density weight to be associated with the User Defined Area specified through MGUSER.  
  
REMARKS  
---  
MGWUSR is one of several keywords used to control the mesh density during AMG mesh generation. The values from all the mesh density keywords are combined during the mesh generation process to create a mesh density distribution within the geometric boundary. The keywords MGWCUV, MGWSTN, MGWSTR, MGWTMP, and MGWUSR, specify relative mesh density weights to be assigned to the associated keyword parameter (curvature, strain, strain rate, temperature, and user defined area). When an object is deformed, the user defined area will move according to the velocity component assigned to it. This area will carry the mesh density weight, WtUser, with it throughout the simulation. If WtUser = 0, user defined area weighting will not be used to determine the mesh density. Applicable object types: [Rigid](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.5._Rigid), [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous)..  
  
RELATED TOPICS  
---  
[Mesh](/docs/en/pre_processor/13_mesh_generation/13_mesh_generation/): Mesh weighting factors Keywords: [MGWSTN](/docs/en/keyword_documentation/m/mgwstn/), [MGWSTR](/docs/en/keyword_documentation/m/mgwstr/), [MGWCUV](/docs/en/keyword_documentation/m/mgwcuv/), [MGWTMP](/docs/en/keyword_documentation/m/mgwtmp/), [MGNELM (2D)](/docs/en/keyword_documentation/m/mgnelm/), [MGNELM (3D)](/docs/en/keyword_documentation/m/mgnelm_3d/), [MGGRID](/docs/en/keyword_documentation/m/mggrid/), [MGERR](/docs/en/keyword_documentation/m/mgerr/), [MGTELM](/docs/en/keyword_documentation/m/mgtelm/), [MGSIZR](/docs/en/keyword_documentation/m/mgsizr/)

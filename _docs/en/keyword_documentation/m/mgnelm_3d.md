---
lang: en
title: "MGNELM (3D)"
---

# MGNELM

|  (Object Data – 3D)  
---|---  
|  Last updated on : 13-08-2013  
  
* * *

MGNELM Object, NumSurfElem, NumBodyElem, NumCrcSctElem, PreferredMthd 

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
NumSurfElem |  Number of surface elements in new mesh |  2000  
NumBodyElem |  Number of body elements in new mesh (not currently used) |  8000  
NumCrcSctElem |  Number of cross section elements in new mesh (for brick remeshing) |  100  
PreferredMthd |  Preferred meshing method =**0** : Unstructured tetrahedra =**1** : Brick (refer to WPAXIS definition) =**2** : (obsolete, It will be kept to maintain compatibility with previous versions and will be treated as 1 in mesh generator.) |  0  
  
DEFINITION  
---  
MGNELM specifies the preferred method and approximate number of elements to be generated when an object is being meshed using AMG.  
  
REMARKS  
---  
MGNELM is one of several keywords used to control the mesh density during automatic remeshing. For Brick remeshing, at least one workpiece axis (WPAXIS) needs to be defined. This provides center axis for revolving or direction for extruding. The error between the number of specified elements and the number of generated elements is typically on the order of ten percent. When the mesh is generated, the specified total number of elements is used in conjunction with the "Point" and "Parameter" controls to determine the mesh density. Applicable object types: [Rigid](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.5._Rigid), [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
Automatic mesh generation, Automatic [remeshing](/docs/en/pre_processor/9_simulation_controls/9_4_remesh_criteria/) Keywords: [MGGRID](/docs/en/keyword_documentation/m/mggrid/), [MGERR](/docs/en/keyword_documentation/m/mgerr/), [MGTELM](/docs/en/keyword_documentation/m/mgtelm/), [MGSIZR](/docs/en/keyword_documentation/m/mgsizr/), [MGWCUV](/docs/en/keyword_documentation/m/mgwcuv/), [MGWTMP](/docs/en/keyword_documentation/m/mgwtmp/), [MGWSTN](/docs/en/keyword_documentation/m/mgwstn/), [MGWSTR](/docs/en/keyword_documentation/m/mgwstr/)

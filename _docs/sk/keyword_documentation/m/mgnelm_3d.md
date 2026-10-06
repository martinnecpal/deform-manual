---
lang: sk
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
MGNELM is one of several keywords used to control the mesh density during automatic remeshing. For Brick remeshing, at least one workpiece axis (WPAXIS) needs to be defined. This provides center axis for revolving or direction for extruding. The error between the number of specified elements and the number of generated elements is typically on the order of ten percent. When the mesh is generated, the specified total number of elements is used in conjunction with the "Point" and "Parameter" controls to determine the mesh density. Applicable object types: [Rigid]({{ '/docs/sk/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.5._Rigid), [Elastic]({{ '/docs/sk/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.2._Elastic), [Plastic]({{ '/docs/sk/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.1_Plastic), [Elastoplastic]({{ '/docs/sk/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.3._Elasto-plastic), and [Porous]({{ '/docs/sk/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.4._Porous).  
  
RELATED TOPICS  
---  
Automatic mesh generation, Automatic [remeshing]({{ '/docs/sk/pre_processor/9_simulation_controls/9_4_remesh_criteria/' | relative_url }}) Keywords: [MGGRID]({{ '/docs/sk/keyword_documentation/m/mggrid/' | relative_url }}), [MGERR]({{ '/docs/sk/keyword_documentation/m/mgerr/' | relative_url }}), [MGTELM]({{ '/docs/sk/keyword_documentation/m/mgtelm/' | relative_url }}), [MGSIZR]({{ '/docs/sk/keyword_documentation/m/mgsizr/' | relative_url }}), [MGWCUV]({{ '/docs/sk/keyword_documentation/m/mgwcuv/' | relative_url }}), [MGWTMP]({{ '/docs/sk/keyword_documentation/m/mgwtmp/' | relative_url }}), [MGWSTN]({{ '/docs/sk/keyword_documentation/m/mgwstn/' | relative_url }}), [MGWSTR]({{ '/docs/sk/keyword_documentation/m/mgwstr/' | relative_url }})

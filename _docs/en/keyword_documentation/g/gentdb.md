---
lang: en
title: "GENTDB (2D3D)"
---

# GENTDB

|  (Action keyword)  
---|---  
_Update History:_ V11.1 - GENTDB has been introduced. |  Last updated on : 21-05-2016  
  
* * *

GENTDB Object, Type, HasCorrespondences

Source Keyword File

Correspondence File

Temporary DB

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Type |  Must be 1 |  None  
HasCorrespondence |  Specifies if correspondence file is available 0 - no correspondence file is available 1 - correspondence file is available |  None  
  
DEFINITION  
---  
GENTDB generates a temporary DB by morphing a mesh. This is used by DOE to transfer BCC from nominal run to DOE runs  
  
REMARKS  
---  
GENTDB is used with REMESH action keyword to transfer BCC from a nomimal run to each DOE run. GENTDB morps the surface of the mesh contained in Source Keyword File to the shape of the currently loaded mesh and writes the mesh to Temporary DB. A REMESH action keyword cleans up the internal mesh. If HasCorrespondence is 0, the Correspondence File line should not exist (there will only be 2 lines following the GENTDB keyword). A Correspondence file is required for a morphed 3D object. This file contains a mapping between source object's features to the target object's features.  
  
RELATED TOPICS  
---  
Related keywords: MORP, REMESH

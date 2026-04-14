---
lang: sk
title: "TPLOGY (2D)"
---

# TPLOGY

|  (Object data - 2D)  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

Dataset ID (=99)

[Topology data set id ]

* Geometry Topology Data: Vertex,Edge,Loop,Face [Header information ]

NumVertex, NumEdge, NumLoop, NumFace

* Vertex Data

nCurrVertexID, nNumEdgeUses, dPtCoord[0], dPtCoord[1]

nCurrEdgeUseID (Repeat for as many of nCurrEdgeUseID)

(Repeat the above for every VERTEX)

* Edge Data

nCurrEdgeID, nNumLoopUses, nStartVertID, nEndVertID

nCurrLoopUseID (Repeat as many of nNumLoopUses)

(Repeat the above for every EDGE)

* Loop Data

nCurrLoopID, nNumEdges, nNumFaceUses

nCurrEdgeID (Repeat as many of nNumEdges)

nCurrFaceUseID

(Repeat the above for every LOOP)

* Face Data

nCurrFaceID, nNumLoops, nCurrMatID

nCurrLoopID

(Repeat the above for every FACE)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Dataset ID |  Indicator for Topology data |  99 (Fixed)  
NumVertex  |  Number of vertex |  0  
NumEdge |  Number of edges |  0  
NumLoop |  Number of loops |  0  
NumFaces |  Number of faces  |  0  
(Vertex Data)  
nCurrVertexID |  Current vertex no. |   
nNumEdgeUses |  Number of connected edges |   
dPtCoord[0], dPtCoord[1] |  X,Y coordinates |   
nCurrEdgeUseID |  Edge number(s) that uses the current vertex |   
|  (Repeat as many of nNumEdgeUses) |   
(Edge Data)  
nCurrEdgeID |  Current edge no. |   
nNumLoopUses |  Number of connected loops |   
nStartVertID |  Starting vertex number |   
nEndVertID |  Ending vertex number |   
nCurrLoopUseID |  Loop number(s) that uses the current edge |   
|  (Repeat as many of nNumLoopUses) |   
(Loop Data)  
nCurrLoopID |  Current loop no. |   
nNumEdges |  Number of edges belongs to the current loop |   
nNumFaceUses |  Number of faces connected to the current loop |   
nCurrEdgeID |  Edge number(s) that uses the current loop |   
|  (Repeat as many of nNumEdges) |   
nCurrFaceUseID |  Face number that uses the current loop |   
(Face Data)  
nCurrFaceID |  Current face no. |   
nNumLoops |  Number of loops belongs to the current face |   
nCurrMatID  |  Material group number for the current face |   
nCurrLoopID |  Loop number(s) that belongs to the current face |   
|  (Repeat as many of nNumLoops) |   
  
DEFINITION  
---  
TPLOGY describes how geometrical subsets are connected to represent 2D geometry. It uses vertex, edge, loop and face concepts to build topology data for 2D mesh generation. When geometry boundary(ries) is(are) given in Pre-processor, user is first required to define loop(s) and then region(s) for building a complete topology data. Once topology information is ready, user can assign the different materials in the each region. Mesh generation program can generate mesh systems with different material group id numbers in the different regions. For a given object and when geometry is saved in a keyword file or is exported as a geometry file (*.GEO), geometry as well as the constructed topology data are written together. If the geometry is loaded back to pre-processor, the imported topology data is used to recover the topology settings in a pre-processor.  
  
REMARKS  
---  
Data for keyword TPLOGY is fully automatically generated from pre-processor. For a given object and when geometry is saved in a keyword file or is exported into geometry file format (*.GEO), the constructed topology data is written together. When the data file is loaded back to pre-processor, topology data will be recovered. EXAMPLE OF TPLOGY <E1> ++++++++++++++ \+ [F1][L1] + \+ + \+ <E2> + +++++++++ * ++++++++++ * +++++++++ \+ (P2) (P1) + \+ + \+ [F2][L2] <E3> + ++++++++++++++++++++++++++++++++++ 2 vertex: [P1][P2] 3 edges: [E1][E2][E3] 2 loops: [L1][L2] 2 faces: [F1][F2] with material group ids. #1 and #2 TPLOGY 99  * Geometry Topology Data: Vertex, Edge, Loop, Face  2 3 2 2 * Vertex Data 1 3 7.0000000E+000 5.0000000E+000 1 2 3 2 3 3.0000000E+000 5.0000000E+000  1 2 3 * Edge Data 1 1 1 2  1 2 2 2 1 1 2 3 1 2 1 2 * Loop Data 1 2 1  1 2 1 2 2 1  2  3 2 * Face Data 1 1 1  1 2 1 2 2   
  
RELATED TOPICS  
---  
[Geometry](../../pre_processor/12_geometry_modelling): Topology Keywords: [DIEGEO (2D)](/docs/sk/keyword_documentation/d/diegeo/), [DIEGEO (3D)](/docs/sk/keyword_documentation/d/diegeo_3d/)

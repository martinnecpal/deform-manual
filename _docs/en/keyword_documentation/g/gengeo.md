---
lang: en
title: "GENGEO (2D3D)"
---

# GENGEO

|  (Action keyword)  
---|---  
_Update History:_ V11.1 – GENGEO has been introduced. |  Last updated on : 21-05-2016  
  
* * *

GENGEO Object, SaveToFileFlag, GenerateMethod

GeometryFileName

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
SaveToFileFlag |  Save to Geo File Flag **0** \- Do not save geometry to a Geo file **1** \- Save the geometry to a Geo file |  0  
GenerateMethod |  Geometry generation method **0** \- Generate All **-****1** \- Do not generate **1** \- Generate 2D geometry or 2D cross section only **2** \- Convert 2D cross section to 3D geometry **3** \- generate 2D cross section and convert to 3D geometry **4** \- create 3D geometry directly |  0  
GeometryFileName |  Name go Geo file (This parameter only exists of SaveToFileFlag is 1) |  None  
  
DEFINITION  
---  
GENGEO is an action keyword that generates geometry from parameters defined in a GEOPR2 or GEOPR2 keyword.  
  
REMARKS  
---  
When GenerateMethod is 2 or 3, GENGEO will also create the WPAXIS (type 4) which defines the extrusion or revolve that creates the 3D geometry from it's 2D cross section.  
  
RELATED TOPICS  
---  
Related keywords: GEOPR2, GEOPR3, WPAXIS

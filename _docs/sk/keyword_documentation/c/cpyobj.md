---
lang: sk
title: "CPYOBJ (2D3D)"
---

# CPYOBJ

|  (Action keyword)  
---|---  
_Update History:_ V10.1 - CPYOBJ was introduced. |  Last updated on : 23-07-2013  
  
* * *

CPYOBJ TargetObject, CopyOption, SourceObject

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
TargetObject |  Target object number |  None  
CopyOption |  Coordinate system definition = 0 Entire object data = 1 Mesh settings data = 2 Movement data = 3 Property data |  None  
SourceObject |  Target object number |  None  
  
DEFINITION  
---  
CPYOBJ copies the object data when the object is being split as a result of fracture.  
  
REMARKS  
---  
This is action keyword that copies various object data (BCC, mesh density window and etc.) when an object fracture during simulation creates two objects (the old and new objects).  
  
RELATED TOPICS  
---  
Object Properties: [Fracture](/docs/sk/pre_processor/16_object_properties/16_4_fracture_properties/) Keywords: [FRCMOD](/docs/sk/keyword_documentation/f/frcmod/)

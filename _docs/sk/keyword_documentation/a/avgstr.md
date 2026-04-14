---
lang: sk
title: "AVGSTR (2D3D)"
---

# AVGSTR

|  (Object Data)  
---|---  
|  Last updated on : 29-07-2013  
  
* * *

AVGSTR Object, AvgSrate

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
AvgSrate |  Average strain rate |  None  
  
DEFINITION  
---  
AVGSTR specifies a value of average strain rate to be used during the initial guess generation process.  
  
REMARKS  
---  
A rough estimate of AvgSrate is adequate. The average strain rate can be estimated as, AvgSrate = Velocitymovobj / Initial Heightdefobj  Where,  
Velocitymovobj = Initial velocity of the moving object  
Initial Heightdefobj = Initial height of deforming object  
  
RELATED TOPICS  
---  
Object Properties: [Deformation](/docs/sk/pre_processor/16_object_properties/16_1_deformation_properties/)  
Keywords: [LMTSTR](/docs/sk/keyword_documentation/l/lmtstr/)  
  
#

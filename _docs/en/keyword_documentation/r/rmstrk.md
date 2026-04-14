---
lang: en
title: "RMSTRK (2D3D)"
---

# RMSTRK

|  (Object data)  
---|---  
|  Last updated on : 09-08-2013  
  
* * *

RMSTRK Object, RStroke

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
RStroke |  Stroke increment of primary object at which to initiate an automatic remeshing procedure. |  0  
  
DEFINITION  
---  
RMSTRK controls the initiation of a remeshing procedure based on the stroke of the primary object.  
  
REMARKS  
---  
There are four keywords that control the initiation of a remeshing procedure ([RMDPTH](/docs/en/keyword_documentation/r/rmdpth/), [RMTIME](/docs/en/keyword_documentation/r/rmtime/), [RMSTEP](/docs/en/keyword_documentation/r/rmstep/), [RMSTRK]()) for an object. When the remeshing criteria of any of these keywords has been fulfilled or the mesh becomes unusable (negative Jacobian), the object will be remeshed. RStroke is the stroke increment of the primary object measured from the most recent remeshing. If RStroke = 0, the stroke of the primary object will not be used to determine when the object is remeshed. Applicable object types: [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
Simulation Controls: [Remesh Criteria](/docs/en/pre_processor/9_simulation_controls/9_4_remesh_criteria/) Keywords: [RMTIME](/docs/en/keyword_documentation/r/rmtime/), [RMDPTH](/docs/en/keyword_documentation/r/rmdpth/), [RMSTEP](/docs/en/keyword_documentation/r/rmstep/)

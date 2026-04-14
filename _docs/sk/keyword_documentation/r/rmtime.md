---
lang: sk
title: "RMTIME (2D3D)"
---

# RMTIME

|  (Object data)  
---|---  
|  Last updated on : 09-08-2013  
  
* * *

RMTIME Object, RTime

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
RTime |  Process time increment at which to initiate an automatic remeshing procedure. |  0.0  
  
DEFINITION  
---  
RMTIME controls the initiation of a remeshing procedure based on the process time measured from the last remeshing.  
  
REMARKS  
---  
There are four keywords that control the initiation of a remeshing procedure ([RMDPTH](/docs/sk/keyword_documentation/r/rmdpth/), [RMTIME](), [RMSTEP](/docs/sk/keyword_documentation/r/rmstep/), [RMSTRK](/docs/sk/keyword_documentation/r/rmstrk/)) for an object. When the remeshing criteria of any of these keywords has been fulfilled or the mesh becomes unusable (negative Jacobian), the object will be remeshed. RTime is the value of process time allowed to elapses between remeshings of an object. If RTime = 0, the elapsed process time between remeshings will not be used to determine when the object is remeshed. Applicable object types: [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
Simulation Controls: [Remesh Criteria](/docs/sk/pre_processor/9_simulation_controls/9_4_remesh_criteria/) Keywords: [RMSTRK](/docs/sk/keyword_documentation/r/rmstrk/), [RMDPTH](/docs/sk/keyword_documentation/r/rmdpth/), [RMSTEP](/docs/sk/keyword_documentation/r/rmstep/)

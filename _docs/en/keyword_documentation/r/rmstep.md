---
lang: en
title: "RMSTEP (2D3D)"
---

# RMSTEP

|  (Simulation Control)  
---|---  
|  Last updated on : 09-08-2013  
  
* * *

RMSTEP Object, RStep

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
RStep |  Simulation step increment at which to initiate an automatic remeshing procedure. |  0  
  
DEFINITION  
---  
RMSTEP controls the initiation of a remeshing procedure based on the number of simulation steps measured from the last remeshing.  
  
REMARKS  
---  
There are four keywords that control the initiation of a remeshing procedure ([RMDPTH](/docs/en/keyword_documentation/r/rmdpth/), [RMTIME](/docs/en/keyword_documentation/r/rmtime/), [RMSTEP](), [RMSTRK](/docs/en/keyword_documentation/r/rmstrk/)) for an object. When the remeshing criteria of any of these keywords has been fulfilled or the mesh becomes unusable (negative Jacobian), the object will be remeshed. RStep is the value of simulation steps allowed to elapse between remeshings of the object. If RStep = 0, the number of steps between remeshings will not be used to determine when the object is remeshed. Applicable object types: [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
Simulation Controls: [Remesh Criteria](/docs/en/pre_processor/9_simulation_controls/9_4_remesh_criteria/) Keywords: [RMTIME](/docs/en/keyword_documentation/r/rmtime/), [RMDPTH](/docs/en/keyword_documentation/r/rmdpth/), [RMSTRK](/docs/en/keyword_documentation/r/rmstrk/)

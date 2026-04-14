---
lang: sk
title: "RMDPTH (2D3D)"
---

# RMDPTH

|  (Simulation Control)  
---|---  
|  Last updated on : 09-08-2013  
  
* * *

RMDPTH Object, RDepth

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
RDepth |  Interference depth at which to initiate automatic remeshing procedure. |  0.0  
  
DEFINITION  
---  
RMDPTH controls the initiation of a remeshing procedure based on the depth of interference between a slave object and a master object.  
  
REMARKS  
---  
There are four keywords that control the initiation of a remeshing procedure (RMDPTH, RMTIME, RMSTEP, RMSTRK) for an object. When the remeshing criteria of any of these keywords has been fulfilled or the mesh becomes unusable (negative Jacobian), the object will be remeshed. RMDPTH controls the initiation of a remeshing procedure based on the depth of interference between a slave object and a master object. The depth of interference is the depth an element edge of the slave object is crossing the surface of a master object. The object to be remeshed must be a slave object. If RDepth = 0, the interference depth will not be used to determine when the object is remeshed. Applicable object types: [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
Simulation Controls: [Remesh Criteria](/docs/sk/pre_processor/9_simulation_controls/9_4_remesh_criteria/) Keywords: [RMTIME](/docs/sk/keyword_documentation/r/rmtime/), [RMSTEP](/docs/sk/keyword_documentation/r/rmstep/), [RMSTRK](/docs/sk/keyword_documentation/r/rmstrk/)

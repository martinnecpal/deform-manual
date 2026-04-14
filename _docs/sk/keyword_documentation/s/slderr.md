---
lang: sk
title: "SLDERR (2D3D)"
---

# SLDERR

|  (Simulation control)  
---|---  
|  Last updated on : 09-08-2013  
  
* * *

SLDERR SlideError

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
SlideError |  Maximum normal distance an interface slave node may move from the master object surface per step. |  0.0  
  
DEFINITION  
---  
SLDERR is used to limit the distance an interface node of a slave object can move from the master object surface in a single time step.  
  
REMARKS  
---  
Slave nodes which are in contact with a master surface, tend to slide along that surface as the object is compressed. However, when the slave node approaches a corner on the master surface, the direction of the nodal velocity may cause the node to shoot past the corner during a time step. Once, the node has separated from the master surface, it will continue to move in the direction of its separation velocity until the time step is completed. When a new time step is generated, the node is forced back onto the master surface along the shortest normal. The length of this normal is referred to as the normal distance error, an absolute distance. SLDERR causes a new time step to be generated whenever a slave node's normal distance error exceeds SlideError. The value of SlideError should be between 1% -10% of the smallest side length of the smallest element. If SlideError = 0, the distance error will not be used as a time step parameter. The time steps initiated by SLDERR will be recorded in the DEFORM database only if STPDEF is specified as "System" mode. Applicable simulation types: Isothermal Deformation, Non-Isothermal Deformation  
  
RELATED TOPICS  
---  
Non-Isothermal Deformation, [Inter-object contact](/docs/sk/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/), [Step Parameters](/docs/sk/pre_processor/9_simulation_controls/9_2_defining_step/) Keyword: [STPDEF](/docs/sk/keyword_documentation/s/stpdef/)

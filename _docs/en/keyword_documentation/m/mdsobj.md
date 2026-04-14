---
lang: en
title: "MDSOBJ (2D)"
---

# MDSOBJ

|  (Simulation control - 2D)  
---|---  
|  Last updated on : 04-08-2014  
  
* * *

MDSOBJ RefObj1 RefObj2 Method Distance

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
RefObj1 |  Reference Object 1 |  None  
RefObj2 |  Reference Object 2 |  None  
Method |  Method to calculate distance **0** (**0** = Total distance, **1** = X distance, **2** = Y distance) |   
Distance |  Distance used to stop the simulation |  None  
  
DEFINITION  
---  
MDSOBJ is a stopping criteria when the distance between two objects reaches a specified distance.  
  
REMARKS  
---  
This keyword must be used in conjunction with reference points. It impossible to calculate the distance between two objects with out having two points to use.  
  
RELATED TOPICS  
---  
Simulation Controls: [Stopping Controls](/docs/en/pre_processor/9_simulation_controls/9_3_stopping_controls/) Keywords: [REFPOS (2D)](/docs/en/keyword_documentation/r/refpos/), [REFPOS (3D)](/docs/en/keyword_documentation/r/refpos_3d/)

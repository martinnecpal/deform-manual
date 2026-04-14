---
lang: sk
title: "FPERV (3D)"
---

# FPERV

|  (Material data)  
---|---  
|  Last updated on : 13-08-2013  
  
* * *

FPERV bodyforce

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
bodyforce |  weight of body |  0  
  
DEFINITION  
---  
FPERV allows for the weight of the material to be considered in the sintering simulation for the porous material.  
  
REMARKS  
---  
The following equation is used to calculate the body force for porous materials. FPERV is the value that is entered in the text box in the Materials window. DENSTY is defined under elements. The units for FPERV are force per unit volume. It is integrated with respect to volume.  
  
RELATED TOPICS  
---  
[Step parameters](/docs/sk/pre_processor/9_simulation_controls/9_2_defining_step/) Keyword: [DENSTY](/docs/sk/keyword_documentation/d/densty/)

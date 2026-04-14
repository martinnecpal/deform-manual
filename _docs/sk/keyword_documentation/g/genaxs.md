---
lang: sk
title: "GENAXS (3D)"
---

# GENAXS

|  (Action keyword – 3D only)  
---|---  
_Update History:_ V11 - GENAXS has been introduced. V11.1 - Modified to create WPAXIS of type 7 instead of creating file 'AXIS.DAT' |  Last updated on : 22-10-2016  
  
* * *

GENAXS AxisType, LeftHandover, RightHandover

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
AxisType |  WPAXIS type |  7  
LeftHandover |  Left Handover Distance |  None  
RightHandover |  Right Handover Distance |  None  
  
DEFINITION  
---  
GENAXS creates WPAXIS (type=7) which constrains certain nodes on the billet to prevent it from certain motion.  
  
REMARKS  
---  
GENAXS is an action keyword and is mainly for internal use. It is used in the cogging template to create rigid zones for holding the billet in position. Handover Distance is the distance between manipulators (left/right) and the center of dies within which clamping occurs. Applicable simulation types: [Cogging](/docs/sk/operation_templates/29_cogging/29_introduction_to_cogging/)  
  
RELATED TOPICS  
---  
Related keywords: [GENSUB](/docs/sk/keyword_documentation/g/gensub/), [EXECMD](/docs/sk/keyword_documentation/e/execmd/)

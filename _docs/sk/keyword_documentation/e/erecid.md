---
lang: sk
title: "ERECID (2D3D)"
---

# ERECID

|  (Simulation control)  
---|---  
_Update History:_ V11.1 - ERECID has been introduced. |  Last updated on : 21-05-2016  
  
* * *

ERECID, # of time to record (N), # of control parameters

ID for variable 1, control parameter#1, control parameter #2, ...

ID for variable 2, control parameter#1, control parameter #2, ...

...

ID for variable N, control parameter#1, control parameter #2, ...

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
# of time to record |  Number of rows |  None  
# of control parameters |  Number of columns |  None  
  
DEFINITION  
---  
ERECID defines the state variables in ERECVL. |  NRECID  |  State Variable  
---|---  
**1** |  strain above a temperature  
**2** |  strain belowa temperature  
**3** |  strain above a strain rate  
  
RELATED TOPICS  
---  
Related keywords: [ERECVL](/docs/sk/keyword_documentation/e/erecvl/)

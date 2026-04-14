---
lang: sk
title: "NRECID (2D3D)"
---

# NRECID

|  (Simulation control data)  
---|---  
_Update History:_ V11.1 - NRECID has been introduced. |  Last updated on : 21-05-2016  
  
* * *

NRECID, # of time to record (N), # of control parameters

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
NRECID defines the state variables in NRECVL. |  NRECID |  State Variable  
---|---  
1 |  (Reserved)  
2 |  time between two temperatures  
3 |  cooling/heating rate between two temperature  
4 |  time to reach a temperature during heating  
5 |  time to reach a temperature during cooling  
6 |  time from a temperature to end during heating  
7 |  time from a temperature to end during cooling  
  
RELATED TOPICS  
---  
Related keywords: [NRECVL](/docs/sk/keyword_documentation/n/nrecvl/)

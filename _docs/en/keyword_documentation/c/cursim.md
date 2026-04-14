---
lang: en
title: "CURSIM (2D3D)"
---

# CURSIM

|  (Simulation control)  
---|---  
_Update History:_ (New) Definition has been extended in v11 V11 – Simulation No can increase sequentially across the operations. The second argument, “Process No” in previous release is changed to Operation No. |  Last updated on : 29-07-2013  
  
* * *

CURSIM Simulation_no, Operation_no, Process_type3060

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Simulation_no |  Current simulation number |  None  
Operation_no |  Current operation number |  None  
Process_type |  Process_type |  None  
  
DEFINITION  
---  
CURSIM specifies the current simulation number, operation number, and process type.  
  
REMARKS  
---  
CURSIM is used in multiple operations to determine the position of current simulation in the entire schedule. This allows DEFORM to pick up correct information for further runs. Simulation no increases sequentially after each simulation. Operation no is higher level than the simulation no. Therefore, simulation no will be sequentially increases across operations. (New in v11) For example, a multiple operation Database may have CURSIM growing in following order:  CURSIM 1 1 5 CURSIM 2 1 5 CURSIM 3 1 5 CURSIM 4 2 3 CURSIM 5 2 3 CURSIM is stored in the database. If CURSIM is not set properly, there will be problems. The Multiple Operation Control Program sets CURSIM in the Pre-Processor. The user should not have to worry about setting CURSIM.  
  
RELATED TOPICS  
---  
Keyword: [SIMNAM](/docs/en/keyword_documentation/s/simnam/), [OPRNAM](/docs/en/keyword_documentation/o/oprnam/)

---
lang: en
title: "VFACTR (3D)"
---

# VFACTR

|  (Simulation control - 3D)  
---|---  
_Update History:_ v11 - VFACTR (3D view factor calculation) keyword has been introduced. |  Last updated on : 12-08-2013  
  
* * *

VFACTR SwitchOn

or

VFACTR Switch, NumObject (for NumObject > 0)

Object(1),.. , Object(NumObject)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
SwitchOn |  On/off flag = **0** Off = **1** On |  0  
NumObject |  Total number of objects |  None  
Object(i) |  List of objects |  None  
  
DEFINITION  
---  
VFACTR determines whether inter-object heat transfer by radiation is computed in the simulation. It also specifies the list of objects for view factor calculation in 3D when the object is listed.   
  
REMARKS  
---  
Only when NumObject > 0, the object list can be provided. This keyword was available only in 2D v10.2 release. It becomes available for 3D as well in v11 release.  
  
RELATED TOPICS  
---  
Simulation Controls: [Process conditions](/docs/en/pre_processor/9_simulation_controls/9_6_process_conditions/) \- [Heat transfer](../../pre_processor/9_simulation_controls/9_6_process_conditions.htm#9.6.1._Heat_Transfer) Related keywords: [ENVTMP](/docs/en/keyword_documentation/e/envtmp/), [CNVCOF](/docs/en/keyword_documentation/c/cnvcof/)

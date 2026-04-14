---
lang: en
title: "PRSTRE (2D3D)"
---

# PRSTRE

|  (Object Data)  
---|---  
|  Last updated on : 09-08-2013  
  
* * *

PRSTRE Object, Stiffness, PreLoad, CurStretch

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
Stiffness |  Press stiffness |  0  
Preload |  Pre-load of the press |  None  
CurStretch |  Current stretch of the press |  0  
  
DEFINITION  
---  
PRSTRE This keyword is to incorporate the press stretch (elastic energy loss) into the simulation. With die stretch, the total die displacement within step = current die increment - current stretch increment. The total stoke is increased as usual. And the total strech = current stretch + stretch increment.  
  
REMARKS  
---  
Applicable object types: [Rigid](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.5._Rigid),  
  
RELATED TOPICS  
---  
[Movement Controls](/docs/en/pre_processor/15_movement_controls_definition/15_movement_controls_settings/): Elastic Losses Keywords: [MOVCTL (2D)](../m/movctl_\(2d\).htm), [MOVCTL (3D)](../m/movctl_\(3d\).htm)

---
lang: sk
title: "SMODE (2D3D)"
---

# SMODE

|  (Simulation control)  
---|---  
|  Last updated on : 09-08-2013  
  
* * *

SMODE SimMode

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
SimMode |  Simulation mode = **1** Isothermal Deformation = **2** Heat Transfer = **3** Non-Isothermal Deformation |  3  
  
DEFINITION  
---  
SMODE specifies the type of simulation to be performed. (Note: SMODE is nearly obsolete. Please use TRANS instead.)  
  
REMARKS  
---  
There are three types of FEM analysis that can be performed in DEFORM. Isothermal deformation simulates the deformation of objects with no heat exchange. Heat transfer simulates heat exchange within and between objects. Non-isothermal deformation simulates the combined effects of deformation and heat exchange.  
  
RELATED TOPICS  
---  
Simulation Controls: [Main Controls](/docs/sk/pre_processor/9_simulation_controls/9_1_simulation_type_settings/) \- [Modes](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#9.1.5._Simulation_modes_\(SMODE,_TRANS\)) Related keywords: [TRANS](/docs/sk/keyword_documentation/t/trans/), [STYPE (2D)](/docs/sk/keyword_documentation/s/stype/), [STYPE (3D)](/docs/sk/keyword_documentation/s/stype_3d/)

---
lang: sk
title: "MSTMTR (2D3D)"
---

# MSTMTR

|  (Material data)  
---|---  
|  Last updated on : 24-07-2013  
  
* * *

MSTMTR Material NoPhase

PhaseList(1)

::

PhaseList(NoPhase)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Material |  Material group number |  None  
NoPhase |  Number of dependent phases |  0  
PhaseList(i) |  List of each phase |  None  
  
DEFINITION  
---  
MSTMTR specifies whether a material is a mixture or just a phase. If it is mixture, it specifies the list of each phase in mixture material.  
  
REMARKS  
---  
When material has a list of phases, material type is automatically set as mixture material. For mixture materials, phase transformation kinetic (TTTD) which describes inter-material behavior among the phases should be defined as well. If material is simply a phase, the number of dependent phases will be 0. Applicable simulation types: Non-Isothermal Deformation  
  
RELATED TOPICS  
---  
[Heat treatment](/docs/sk/operation_templates/37_heat_treatment/37_introduction_to_heat_treatment/), Phase transformation Related Keywords: [TTTD](/docs/sk/keyword_documentation/t/tttd/)

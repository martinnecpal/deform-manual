---
lang: en
title: "GBMOBI (2D3D)"
---

# GBMOBI

|  (Material data)  
---|---  
_Update History:_   
V11 - GBMOBI has been introduced. |  Last updated on : 25-07-2013  
  
* * *

GBMOBI Material, M0, Q

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Material |  Material Number |  None  
M0  |  Grain boundary mobility |  None  
Q |  Activation energy of material |  None  
  
DEFINITION  
---  
GBMOBI specifies the grain boundary mobility of a material.  
  
REMARKS  
---  
The movement of high angle grain boundaries (HAGB) has implications for recrystallization and grain growth while subgrain boundary (LAGB) movement strongly influences recovery and the nucleation of recrystallization. A boundary moves due to a pressure acting on it. It is generally assumed that the velocity is directly proportional to the pressure with the constant of proportionality being the mobility of the boundary. The mobility is strongly temperature dependent and often follows an Arrhenius type relationship: | ![]({{ '/assets/equations/keyword_documentation/g/gbmobi_eq_1.jpg' | relative_url }}) |   
---|---  
  
The apparent activation energy (Q) may be related to the thermally activated atomistic processes that occur during boundary movement.  
  
Applicable object types: [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic)

Applicable simulation type: [Heat treatment](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#9.1.5._Simulation_modes_\(SMODE,_TRANS\))

RELATED TOPICS  
---  
Keywords: [GBENGY](/docs/en/keyword_documentation/g/gbengy/), [COARSE](/docs/en/keyword_documentation/c/coarse/), [NUCSIZ](/docs/en/keyword_documentation/n/nucsiz/), [DIFBND](/docs/en/keyword_documentation/d/difbnd/)

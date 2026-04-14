---
lang: en
title: "SIZEMD (2D3D)"
---

# SIZEMD

|  (Material data)  
---|---  
_Update History:_ v11 – Particle size mode has been introduced. |  Last updated on : 09-08-2013  
  
* * *

SIZEMD Material, Mode

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Material |  Material Number |  None  
Mode |  Mode of particle size = **0** None = **1** Spherical particles = **2** Secondary alpha lath = **3** Grain boundary alpha = **4** Side plate alpha = **5** Gamma prime Nickel |  0  
  
DEFINITION  
---  
SIZEMD specifies the mode of particle size.  
  
REMARKS  
---  
Depending on a selection of particle size mode, particle shape at each element of object will be stored in SIZESH. Applicable object types: [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous). Applicable simulation type: [Heat treatment](/docs/en/operation_templates/37_heat_treatment/37_introduction_to_heat_treatment/)  
  
RELATED TOPICS  
---  
Keywords: [SIZESH](/docs/en/keyword_documentation/s/sizesh/)

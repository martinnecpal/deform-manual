---
lang: en
title: "SIZESH (2D3D)"
---

# SIZESH

|  (Object data)  
---|---  
_Update History:_ v11 – Particle shape information has been introduced. |  Last updated on : 09-08-2013  
  
* * *

SIZESH Object, FieldWidth, Nelem, DefSize

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
FieldWidth |  The field width of this state variable |  1  
Nelem |  Number of element |  None  
DefSize |  Default FieldWidth value of all elements not listed in the element data |  0  
  
DEFINITION  
---  
SIZESH specifies the particle shape information.  
  
REMARKS  
---  
Depending on a selection of particle size mode of SIZEMD, SIZESH will store the following particle information at each element in object. 1) SizeMode = Spherical particles \- Particle size 2) SizeMode = Secondary alpha lath \- Thickness of secondary alpha \- Starting temperature \- Starting primary alpha Volume fraction 3) SizeMode = Grain boundary alpha \- Thickness of grain boundary alpha \- Starting temperature of grain boundary alpha 4) SizeMode = Side plate alpha \- Thickness of side plate alpha \- Assumed spacing of grain boundary alpha \- Starting temperature of grain boundary \- Starting temperature of side plate alpha 5) SizeMode = Gamma prime Nickel \- Particle size Applicable object types: [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous). Applicable simulation type: [Heat treatment](/docs/en/operation_templates/37_heat_treatment/37_introduction_to_heat_treatment/)  
  
RELATED TOPICS  
---  
Keywords: [SIZEMD](/docs/en/keyword_documentation/s/sizemd/)

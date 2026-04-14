---
lang: en
title: "NUCSIZ (2D3D)"
---

# NUCSIZ

|  (Material data)  
---|---  
_Update History:_ V11 - NUCSIZ has been introduced. |  Last updated on : 24-07-2013  
  
* * *

NUCSIZ Material, FuncType(=0), Nuclei

or

(For energy as a function of temperature)

NUCSIZ Material, FuncType, Ndata

Temp(1), … , Nuclei(1)

::

Temp(Ndata), … , Nuclei (Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Material |  Material Number |  None  
FuncType |  Energy function type = **0** Constant = **1** Function of temperature |  0  
Nuclei |  Nuclei size |  0  
Ndata |  Number of data pair |   
Temp(i) |  Temperature of ith data pair |   
Nuclei(i) |  Nuclei size of ith data pair |   
  
DEFINITION  
---  
NUCSIZ specifies the size of nuclei during nucleation event.  
  
REMARKS  
---  
The formation of nuclei would be associated with an energy requirement due to the formation of a new interface and energy liberation due to the formation of a new volume of lower energy material. It can be specified as constant or a function of temperature. Applicable object types: [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic) Applicable simulation type: [Heat treatment](/docs/en/operation_templates/37_heat_treatment/37_introduction_to_heat_treatment/)  
  
RELATED TOPICS  
---  
Keywords: [GBMOBI](/docs/en/keyword_documentation/g/gbmobi/), [GBENGY](/docs/en/keyword_documentation/g/gbengy/), [COARSE](/docs/en/keyword_documentation/c/coarse/). [DIFBND](/docs/en/keyword_documentation/d/difbnd/)

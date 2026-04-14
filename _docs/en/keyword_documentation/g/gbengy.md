---
lang: en
title: "GBENGY (2D3D)"
---

# GBENGY

|  (Material data)  
---|---  
_Update History:_ (New keyword in v11) |  Last updated on : 23-07-2013  
  
* * *

GBENGY Material, FuncType, Energy

or

(For energy as a function of temperature)

GBENGY Material, FuncType, Ndata

Temp(1), … , Energy(1)

::

Temp(Ndata), … , Energy(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Material |  Material Number |  0  
FuncType |  Energy function type =**0** Constant = **1** function of temperature |  None  
Energy |  Energy value |  0  
Ndata |  Number of temperature data |  0  
Temp(i) |  Temperature of ith data |  0  
Energy(i) |  Energy of ith data |  0  
  
DEFINITION  
---  
GBENGY specifies the grain boundary energy of a material.  
  
REMARKS  
---  
Grain boundary energy is defined as the excess free energy associated with the presence of a grain boundary, with the perfect lattice as the reference point. A thought experiment provides a means of quantifying GB energy![]({{ '/assets/equations/keyword_documentation/g/gamma.jpg' | relative_url }}). Take a patch of boundary with area A, and increase its area by dA. The grain boundary energy is the proportionality constant between the increment in total system energy and the increment in area. | ![]({{ '/assets/equations/keyword_documentation/g/gbengy_eq_1.jpg' | relative_url }}) |   
---|---  
  
  
As the energy of the boundary increases, the energy per dislocation decreases. Thus there is a driving force to produce fewer, more misoriented boundaries (i.e., grain growth).  
  
Applicable object types: [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic)

Applicable simulation type: [Heat treatment](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#9.1.5._Simulation_modes_\(SMODE,_TRANS\))

RELATED TOPICS  
---  
Keywords: [GBMOBI](/docs/en/keyword_documentation/g/gbmobi/), [COARSE](/docs/en/keyword_documentation/c/coarse/), [NUCSIZ](/docs/en/keyword_documentation/n/nucsiz/), [DIFBND](/docs/en/keyword_documentation/d/difbnd/)

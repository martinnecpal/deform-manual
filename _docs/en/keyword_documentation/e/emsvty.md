---
lang: en
title: "EMSVTY (2D3D)"
---

# EMSVTY

|  (Material data)  
---|---  
|  Last updated on : 30-07-2013  
  
* * *

EMSVTY Mat, Ftype, Emiss or EMSVTY Mat, Ftype, Ndata

Temp(1), Emiss(1)

: :

Temp(Ndata), Emiss(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Mat |  Material number |  None  
Ftype |  Function type: **0** = Constant emissivity **1** = Temperature dependent emissivity |  None  
Emmis |  Emissivity |  None  
Ndata |  Number of temp/emissivity data pairs |  None  
Temp(i) |  Temperature of ith data pair |  None  
Emmis(i) |  Emissivity of ith data pair |  None  
  
DEFINITION  
---  
EMSVTY specifies the emissivity of a particular object.  
  
REMARKS  
---  
The emissivity may be specified as a constant value or as a set of discrete temperature/emissivity data pairs. If Ftype = 1 use the operand Emiss. If Ftype = 2 use the operands Ndata, Temp(i), Emiss(i). Each temperature/emissivity pair should be provided on a separate line. When temperatures lie within the specified data range, linear interpolation is used to determine the corresponding emissivity. When temperatures lie outside the specified data range, linear extrapolation is used to determine the corresponding emissivity. The emissivity is dependent on the material, the surface condition, and the temperature. Its value should be 0 ≤ Emiss ≤ 1. The equation for radiation heat transfer is: | ![]({{ '/assets/equations/keyword_documentation/b/blzman_eq1.jpg' | relative_url }}) |   
---|---  
  
Applicable simulation types: Heat Transfer, Non-Isothermal Deformation  
  
RELATED TOPICS  
---  
Keywords: [BLZMAN](/docs/en/keyword_documentation/b/blzman/), [ENVTMP](/docs/en/keyword_documentation/e/envtmp/)

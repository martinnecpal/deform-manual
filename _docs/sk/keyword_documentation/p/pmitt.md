---
lang: sk
title: "PMITT (2D3D)"
---

# PMITT

|  (Material data)  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

PMITT Material, Ftype, Pmitt/Ndata

if (Ftype = 1 or 2):

Temp/Density(1), Pmitt(1)

Temp/Density(Ndata), Pmitt(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Material |  Material number |  None  
Ftype |  Function type **0** = Constant **1** = Temperature dependent **2** = Density dependent |  None  
Pmitt |  Permitivity |  None  
Ndata |  Number of data pairs |  None  
Temp(i) |  Temperature of ith data pair |  None  
Pmitt(i) |  Permitivity of ith data pair |  None  
Density(i) |  Density of ith data |  None  
  
DEFINITION  
---  
PMITT specifies the magnetic permitivity for a material.  
  
REMARKS  
---  
The Permitivity is used in simulations of induction heating.  
RELATED TOPICS  
---  
Material Data: [Electromagnetic Data](/docs/sk/pre_processor/10_material_data/10_8_elec_mag_data/10_8_elec_mag_data/) Keywords: [ELRST](/docs/sk/keyword_documentation/e/elrst/), [PMEAB](/docs/sk/keyword_documentation/p/pmeab/)

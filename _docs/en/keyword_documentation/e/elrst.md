---
lang: en
title: "ELRST (2D3D)"
---

# ELRST

|  (Material data)  
---|---  
|  Last updated on : 30-07-2013  
  
* * *

ELRST Material, Ftype, ElRst/Ndata/N1, (N2)

if (Ftype = 1, 2, or 3):

Temp/Density/Atom(1), ElRst(1)

Temp/Density/Atom(Ndata), ElRst(Ndata)

else if (Ftype = 4):

Temp(1) .. Temp (N1)

Atom(1) .. Atom (N2)

ElRst(1) .. ElRst(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Material |  Material number |  None  
Ftype |  Function type **0** = Constant **1** = Temperature dependent **2** = Density dependent **3** = Atom dependent **4** = Temperature and Atom dependent |  None  
ElRst |  Electric resistance |  None  
Ndata |  Number of data pairs |  None  
Temp(i) |  Temperature of ith data pair |  None  
ElRst(i) |  Permitivity of ith data pair |  None  
Density(i) |  Density of ith data |   
Atom(i) |  Atom percentage of ith data |   
  
DEFINITION  
---  
ELRST specifies the electric resistance for a material.  
  
REMARKS  
---  
The Electric Resistance is used in simulations of induction heating.  
  
RELATED TOPICS  
---  
Material Data:[ Electromagnetic data](/docs/en/pre_processor/10_material_data/10_8_elec_mag_data/10_8_elec_mag_data/) Keyword: [PMEAB](/docs/en/keyword_documentation/p/pmeab/), [PMITT](/docs/en/keyword_documentation/p/pmitt/)

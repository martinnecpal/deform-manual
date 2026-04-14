---
lang: en
title: "PMEAB (2D3D)"
---

# PMEAB

|  (Material data)  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

PMEAB Material, Ftype, Pmeab/Ndata/N1, (N2)

if (Ftype = 1 or 2):

Temp/Density(1), Pmeab(1)

Temp/Density(Ndata), Pmeab(Ndata)

else if (Ftype = 4):

Temp(1) .. Temp (N1)

MagFI(1) .. MagFI (N2)

Pmeab(1) .. Pmeab(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Material |  Material number |  None  
Ftype |  Function type **0** = Constant **1** = Temperature dependent **2** = Density dependent **3** = (not used) **4** = Temperature and Magnetic field intensity dependent |  None  
Pmeab |  Permeability |  None  
Ndata |  Number of data pairs |  None  
N1 |  Number of temperature data points (method=**4**) |   
N2 |  Number of Magnetic field intensity data points (method=**4**) |   
Temp(i) |  Temperature of ith data pair |  None  
Pmeab(i) |  Permeability of ith data pair |  None  
Density(i) |  Density of ith data |   
MagFI(i) |  Magnetic field intensity of ith data |   
  
DEFINITION  
---  
PMEAB specifies the magnetic permeability for a material.  
  
REMARKS  
---  
The Permeability is used in simulations of induction heating.  
  
RELATED TOPICS  
---  
Material Data: [Electromagnetic Data](../../pre_processor/10_material_data/10_8_elec_mag_data) Keywords:[ ELRST](/docs/en/keyword_documentation/e/elrst/), [PMITT](/docs/en/keyword_documentation/p/pmitt/)

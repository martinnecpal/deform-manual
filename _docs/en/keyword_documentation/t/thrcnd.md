---
lang: en
title: "THRCND (2D3D)"
---

# THRCND

|  (Material data)  
---|---  
|  Last updated on : 09-08-2013  
  
* * *

THRCND Material, Ftype, Conductivity

or

THRCND Material, Ftype, Ndata

Temp(1), Conductivity(1)

::

Temp(Ndata), Conductivity(Ndata)

or 

THRCND Material, Ftype, N1, N2

Temp(1) .. Temp(Ndata)

Atom(1) .. Atom(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Material |  Material number |  None  
Ftype |  Function type: **0** = Constant thermal conductivity **1** = Temperature dependent thermal conductivity **2** = Density dependent thermal conductivity (*) **3** = Atom dependent thermal conductivity (*) **4** = Temperature and Atom dependent thermal conductivity (*) |  None  
Conductivity |  Thermal conductivity |  None  
N1 |  Number of data pairs for the function or temp. data for method = **4** |   
N2 |  Number of atom data for method = **4** |   
Ndata |  Number of temp/thermal conductivity data pairs |  None  
Temp(i) |  Temperature of ith data pair |  None  
Conductivity(i) |  Thermal conductivity of ith data pair |  None  
Density(i) |  Density dependent thermal conductivity |  None  
Atom(i) |  Atom dependent thermal conductivity |  None  
  
DEFINITION  
---  
THRCND specifies the thermal conductivity of a particular material.  
  
REMARKS  
---  
The thermal conductivity may be specified as a constant value as a set of discrete temperature/conductivity data pairs. If Ftype = 0 use the operand Conductivity. If Ftype = 1 use the operands Ndata, Temp(i), Conductivity(i). Each temperature/thermal conductivity pair should be provided on a separate line. When temperatures lie within the specified data range, linear interpolation is used to determine the corresponding thermal conductivity. When temperatures lie outside the specified data range, linear extrapolation is used to determine the corresponding thermal conductivity. If Ftype = 2 use the operands N1 and Density (i). If Ftype = 3 use the operands N1 and Atom(i). It should be noted that the atom variables means the weight percent of solute in the material. If Ftype = 4 use the operands N1, N2, Temp (i), Atom (i). The equation for heat conduction is: | ![]({{ '/assets/equations/keyword_documentation/t/thrcnd_eq_1.jpg' | relative_url }}) |   
---|---  
  
Applicable simulation types:

Deformation Module, Heat Transfer, Non-Isothermal Deformation, Microstructure Module.  
  
RELATED TOPICS  
---  
Material Data: [Thermal Data](/docs/en/pre_processor/10_material_data/10_3_thermal_data/10_3_thermal_data/) Keywords: [HEATCP](/docs/en/keyword_documentation/h/heatcp/), [EMSVTY](/docs/en/keyword_documentation/e/emsvty/), [MASDEN](/docs/en/keyword_documentation/m/masden/)

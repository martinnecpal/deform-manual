---
lang: en
title: "HEATCP (2D3D)"
---

# HEATCP

|  (Material data)  
---|---  
|  Last updated on : 07-08-2013  
  
* * *

HEATCP Material, Ftype, HeatCap or HEATCP Material, Ftype, Ndata, Flag

Temp(1), HeatCap(1)

: :

Temp(Ndata), HeatCap(Ndata)

HEATCP Material, Ftype, N1, N2, Flag

Temp(i)..Temp(Ndata)

Atom(i)..Atom(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Ftype |  Function type: **0** = Constant heat capacity **1** = Temperature dependent heat capacity **2** = Density dependent heat capacity **3** = Atom dependent heat capacity **4** = Temperature and Atom dependent heat capacity |  None None None None None None  
HeatCap |  Heat capacity |  None  
Ndata |  Number of temp/heat capacity data pairs |  None  
N1 |  Number of data pairs for function or temp Data when method = **4** |  None  
N2 |  Number of data pairs for atom when method = 4 |  None  
Temp(i) |  Temperature of ith data pair |  None  
HeatCap(i) |  Heat capacity of ith data pair |  None  
Density(i) |  Density data |  None  
Atom(i) |  Atom data |  None  
Flag |  =**0** or not specified: Heat capacity =**1** : Specific heat |   
  
DEFINITION  
---  
HEATCP specifies the heat capacity of a particular object.  
  
REMARKS  
---  
The heat capacity may be specified as a constant value or as a set of temperature/heat capacity data pairs. If Ftype = 0 use the value HeatCap. If Ftype = 1 use the values Ndata, Temp(i), HeatCap(i). Each temperature/heat capacity pair should be provided on a separate line. When temperatures lie within the specified data range, linear interpolation is used to determine the corresponding heat capacity. When temperatures lie outside the specified data range, linear extrapolation is used to determine the corresponding heat capacity. If Ftype = 2 use the operands N1 and Density(i). If Ftype = 3 use the operands N1 and Atom(i). If Ftype = 4 use the operands N1, N2, Atom(i) and Temp(i). The equation for heat capacity is: | ![]({{ '/assets/equations/keyword_documentation/h/heatcp_eq_1.jpg' | relative_url }}) |   
---|---  
  
Applicable simulation types: Deformation Module

Heat Transfer

Non-Isothermal Deformation

Microstructure Module  
  
RELATED TOPICS  
---  
Material Data: [Thermal](/docs/en/pre_processor/10_material_data/10_3_thermal_data/10_3_thermal_data/) Keywords: [THRCND](/docs/en/keyword_documentation/t/thrcnd/)

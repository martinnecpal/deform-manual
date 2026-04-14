---
lang: sk
title: "EXPAND (2D3D)"
---

# EXPAND

|  (Material data)  
---|---  
|  Last updated on : 30-07-2013  
  
* * *

EXPAND Material, Ftype, Expansion, Temp or EXPAND Material, Ftype, Ndata, Temp

Temp(1), Expansion(1)

: :

Temp(Ndata), Expansion(Ndata)

or EXPAND Material, Ftype, N1, N2

Temp(1) .. Temp (Ndata)

Atom(1) .. Atom (Ndata)

Expansion(1) .. Expansion(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Material |  Material number |  None  
Ftype |  Function type: 0 = Constant thermal expansion coeff 1 = Temperature dependent thermal expansion coeff 2 = Density dependent thermal expansion coeff (*) 3 = Atom dependent thermal expansion coeff (*) 4 = Temperature and Atom dependent thermal coeff (*) |  0  
Expansion |  Thermal expansion coefficient |  None  
Temp |  Material reference temperature |  None  
N1 |  Number of data pairs for the function or temp data When method = **4** is selected |   
N2 |  Number of atom data for method = **4** |   
Ndata |  Number of data |  None  
Temp(i) |  Temperature of ith data pair |  None  
Expansion(i) |  Thermal expansion coefficient of ith data pair |  None  
Density(i) |  Density dependent thermal expansion |  None  
Atom(i) |  Atom dependent thermal expansion |  None  
  
(*) denotes that the function type is used in the Heat Treatment Module only.

DEFINITION  
---  
EXPAND specifies the thermal expansion coefficient of a particular material.  
  
REMARKS  
---  
The thermal expansion coefficient is used to determine the amount an elastic object expands due to temperature change. The temperature change is defined as the difference between nodal temperatures and the specified reference temperature (REFTMP). However, in case of heat treating, the thermal expansion coefficient is derived by using each phase's volume fraction. Therefore, the value is defined as follows: | ![]({{ '/assets/equations/keyword_documentation/e/expand_eq_1.jpg' | relative_url }}) |   
---|---  
  
The thermal expansion coefficient may be specified as a constant value or as a set of temperature/coefficient data pairs. The format is identical to YOUNG and POISON keywords.

If Ftype = 0 use the operand Expansion.

If Ftype = 1 use the operands Ndata, Temp(i), Expansion(i). Each temperature/coefficient pair should be provided on a separate line. When temperatures lie within the specified data range, linear interpolation is used to determine the corresponding thermal expansion coefficient. When temperatures lie outside the specified data range, linear extrapolation is used to determine the corresponding thermal expansion coefficient.

If Ftype = 2 use the operands N1 and Density (i).

If Ftype = 3 use the operands N1, and Atom(i). It should be noted that the atom variable refers to the weight percent of solute in the material.

If Ftype = 4 use the operands N1, N2, Temp (i), Atom (i).

The equation for linear thermal expansion is:  
  
![]({{ '/assets/equations/keyword_documentation/e/expand_eq_2.jpg' | relative_url }}) |   
---|---  
  
Applicable simulation types: Deformation Module, Microstructure Module, Non-Isothermal Deformation, Heat Transfer

RELATED TOPICS  
---  
Material Data: [Elastic Data](/docs/sk/pre_processor/10_material_data/10_2_elastic_data/10_2_elastic_data/) Keywords: [REFTMP](/docs/sk/keyword_documentation/r/reftmp/), [YOUNG](/docs/sk/keyword_documentation/y/young/), [POISON](/docs/sk/keyword_documentation/p/poison/)

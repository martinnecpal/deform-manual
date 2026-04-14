---
lang: en
title: "POISON (2D3D)"
---

# POISON

|  (Material data)  
---|---  
|  Last updated on : 09-08-2013  
  
* * *

POISON Material, Ftype, Poisson or POISON Material, Ftype, Ndata

Temp(1) Poison(1)

Temp(Ndata) Poisson(Ndata)

Or

POISON Material, Ftype, N1, N2, or value Temp (1) .. Temp (Ndata)

Atom (1) .. Atom(Ndata)

Poisson(1) .. Poisson(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Material |  Material number |  None  
Ftype |  Function type: **0** = Constant Poisson's ratio **1** = Temperature dependent Poisson's ratio **2** = Density dependent Poisson’s ratio (*) **3** = Atom dependent Poisson’s ratio (*) **4** = Temperature and Atom dependent Poisson’s ratio (*) |  None  
Poisson |  Poisson's ratio |  None  
N1 |  Number of data pairs for the function or temp data When method=**4** is selected |   
N2 |  Number of atom data for method=**4** |   
Ndata |  Number of data |  None  
Temp(i) |  Temperature of ith data pair |  None  
Poisson(i) |  Poisson's ratio of ith data pair |  None  
Atom(i) |  Atom concentration ith data pair |  None  
Density(i) |  Density of ith data |  None  
(*) denotes that the function type can only be used in the Microstructure Module.  
  
REMARKS  
---  
The Poisson's ratio may be specified as a constant value or specified as a set of temperature/Poisson's ration data pairs. If Ftype = 0 use the operand Poisson. If Ftype = 1 use the operands Ndata, Temp(i), Poisson(i). Each temperature/Poisson's ratio pair should be provided on a separate line. When temperatures lie within the specified data range, linear interpolation is used to determine the corresponding Poisson's ratio. When temperatures lie outside the specified data range, linear extrapolation is used to determine the corresponding Poisson's ratio. If Ftype = 2 use the operands N1 and Density (i). If Ftype = 3 use the operands N1, and Atom(i). It should be noted that the atom variable refers to the weight percent of solute in the material. If Ftype = 4 use the operands N1, N2, Temp (i), Atom (i). Poisson's ratio and Young's modulus are needed to obtain the Lame's constants ![]({{ '/assets/equations/keyword_documentation/p/meu.jpg' | relative_url }}) and ![]({{ '/assets/equations/keyword_documentation/p/lamda.jpg' | relative_url }}). | ![]({{ '/assets/equations/keyword_documentation/p/poison_eq_1_.jpg' | relative_url }}) |   
---|---  
  
Applicable Simulation Modules: Deformation, Microstructure

Applicable [Simulation Modes:](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#9.1.5._Simulation_modes_\(SMODE,_TRANS\)) Deformation

Applicable [object types](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4._Object_type): Elastic, Elastoplastic  
  
RELATED TOPICS  
---  
Keywords: [YOUNG](/docs/en/keyword_documentation/y/young/)

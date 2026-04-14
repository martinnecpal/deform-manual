---
lang: en
title: "YOUNG (2D3D)"
---

# YOUNG

|  (Material Data)  
---|---  
|  Last updated on : 07-08-2013  
  
* * *

YOUNG Material, Ftype, Young

or

YOUNG Material, Ftype, Ndata

Temp(1), Young(1)

::

Temp(Ndata), Young(Ndata)

or

YOUNG Material, Ftype, NI, N2

Temp(1) .. Temp (Ndata)

Atom(1) .. Atom (Ndata)

Young(1) .. Young(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Material |  Material number |  None  
Ftype |  Function type **0** = Constant Young's modulus **1** = Temperature dependent Young's modulus  **2** = Density dependent Young’s modulus (*)  **3** = Atom dependent Young’s modulus (*)  **4** = Temperature and Atom dependent Young’s modulus (*) |  None  
N1 |  Number of data pairs for the function or temp data |   
|  When the method = 4 |   
N2 |  Number of atom pairs for method = 4 |   
Young |  Young's modulus |  None  
Ndata |  Number of data pairs |  None  
Temp(i) |  Temperature of ith data pair |  None  
Young(i) |  Young's modulus of ith data pair |  None  
Atom(i) |  Atom concentration of ith data |  None  
Density(i) |  Density of ith data |   
(*) indicates type used in MICROSTRUCTURE module only  
  
DEFINITION  
---  
YOUNG specifies the Young's modulus for a particular material. The Young's modulus is a measure of the stiffness of a material. It is defined as, | ![]({{ '/assets/equations/keyword_documentation/y/young_eq_1.jpg' | relative_url }}) |   
---|---  
  
It should be noted that the Young's Modulus is only valid in the elastic (or linear) region of the stress-strain diagram.

EXAMPLE:

The following example is for material #1, method #4, with 2 different temperatures (500 and 700), and 2 different atom concentrations (0.1 and 0.2). The user should enter all the operands then enter all the temperature data, followed by the atom concentrations, and lastly by the corresponding Young's Modulus values.

Temperature ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) |  500 |  700  
---|---|---  
Concentration ![]({{ '/assets/icons/pre_icons/arrow_down.jpg' | relative_url }})  
0.1 |  20 |  40  
0.2 |  90 |  160  
  
YOUNG 1 4 2 2

500 700

0.1 0.2

20 40

90 160  
  
REMARKS  
---  
The Young's modulus may be specified as a constant value or as a set of discrete temperature/Young's modulus data pairs in the thermal module. Similarly, in the microstructure module the Young’s modulus can be set as a constant value or varying as a function of density, temperature, and atom content. The variable "atom" is a generic term describing the weight percent of solute in the material. If Ftype = 0 use the operand Young. If Ftype = 1 use the operands Ndata, Temp(i), Young(i). Each temperature/Young's modulus pair should be provided on a separate line. When temperatures lie within the specified data range, linear interpolation is used to determine the corresponding Young's modulus. When temperatures lie outside the specified data range, linear extrapolation is used to determine the corresponding Young's modulus. If Ftype= 2 use the operands N1 and Density(i). The user should be reminded that using Ftype 2 is only significant if the object is porous. (i.e. Porous objects are modeled as having a change in density while all other object types are assumed to have constant density throughout the simulation.) If Ftype= 3 use the operands N1 and Atom(i). If Ftype= 4 use the operands N1, N2, Atom(i), and Temp (i). Poisson's ratio and Young's modulus are needed to obtain the Lame's constants and . | ![]({{ '/assets/equations/keyword_documentation/y/young_eq_2_.jpg' | relative_url }}) |   
---|---  
  
Applicable simulation Modules: Deformation, Microstructure, Thermal  
  
RELATED TOPICS  
---  
Object Type: [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic) Object Keyword: [POISON](/docs/en/keyword_documentation/p/poison/)

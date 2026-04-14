---
lang: sk
title: "PHEQVF (2D3D)"
---

# PHEQVF

|  (Inter-material data)  
---|---  
_Update History:_ (New) Definition has been extended in v11 |  Last updated on : 24-07-2013  
  
* * *

PHEQVF Mat1, Mat2, FuncType(=0 or =4), VolFrac (for constant value)

or

PHEQVF Mat1, Mat2, FuncType(=1 or =5), Ndata (for volume fraction as a function of temperature)

Temp(1), VolFrac(1)

::

Temp(Ndata), VolFrac(Ndata)

or (for Volume fraction as a function of atom)

PHEQVF Mat1, Mat2, FuncType(=2 or =6), Ndata

Atom(1), VolFrac(1)

::

Atom(Ndata), VolFrac(Ndata)

or

PHEQVF Mat1, Mat2, FuncType(=3 or =7), NTemp, NAtom (for volume fraction as a function of temp..and atom)

Temp(1), ...,Temp(NTemp)

Atom(1), ...,Atom(NAtom)

VolFrac(1, 1), ...,VolFrac(NTemp, 1)

: :

VolFrac(1, NAtom), ...,VolFrac(NTemp, NAtom)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Mat1 |  Material 1 |  None  
Mat2 |  Material 2 |  None  
FuncType |  Variant selection model type = **0** or **4** Constant value = **1** or **5** Function of temperature = **2** or **6** Function of atom = **3** or**7** Function of temperature and atom Control of proportional calculation on/off  = Off **0, 1, 2, 3** = On **4, 5, 6, 7** |  0  
Ndata |  Number of temperature or atom pair |  0  
VolFrac(j) |  Volume fraction of ith data pair |  None  
NTemp |  Number of temperature data |  0  
NAtom |  Number of atom data |  0  
Temp(i) |  Temperature of ith data |  0.0  
Atom(i) |  Atom of ith data |  0.0  
VolFrac(i,j) |  Volume fraction of ith and jth data |  0.0  
  
DEFINITION  
---  
PHEQVF specifies the equilibrium volume fraction for precipitation.  
  
REMARKS  
---  
This keyword sets a flag to indicate how to use the equilibrium volume fraction (i.e. proportional calculation on/off) in FEM calculation. Applicable object types: [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic) Applicable [simulation type](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#9.1.4._Type_\(STYPE\)): Microstructure, Heat treatment, Transformation  
  
RELATED TOPICS  
---  
Related keywords: [TTTD](/docs/sk/keyword_documentation/t/tttd/)

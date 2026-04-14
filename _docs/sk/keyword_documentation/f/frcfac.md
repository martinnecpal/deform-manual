---
lang: sk
title: "FRCFAC (2D3D)"
---

# FRCFAC

|  (Inter-Object data)  
---|---  
|  Last updated on : 06-08-2014  
  
* * *

FRCFAC Object1, Object2, FricType(=1~3), FricDefType(=0), Friction

or

FRCFAC Object1, Object2, FricType(=1~3), FricDefType(=-n), Dummy

or

FRCFAC Object1, Object2, FricType(=1~3), FricDefType(=1~4), Ndata

Time/Press/Temp/Stretch(1), Friction(1)

: :

Time/Press/Temp/Stretch (Ndata), Friction(Ndata)

or

FRCFAC Object1, Object2, FricType(=1~3), FricDefType(=5), NPres, NTemp, NStre

Press(1), ..., Press(NPres)

Temp(1), ..., Temp(NTemp)

Stretch(1), ..., Stretch(NStre)

Friction(1, 1, 1), ..., Friction(NPres, 1, 1),

: :

Friction(1, NTemp, NStre), ..., Friction(NPres, NTemp, NStre)

or

FRCFAC Object1, Object2, FricType(=1~3), FricDefType(=6~8), A, B

or

FRCFAC Object1, Object2, FricType(=4)

( Coulomb Friction Data)

FricDefType(=0), Friction

FricDefType(=-n), Dummy

FricDefType(=1~4), Ndata

FricDefType(=5), NPres, NTemp, Nstre

FricDefType(=6~8), A, B

( Shear Friction Data)

FricDefType2(=0), Friction2

FricDefType2(=-n), Dummy

FricDefType2(=1~4), Ndata2

FricDefType2(=5), NPres2, NTemp2, NStre2

FricDefType2(=6~8), A2, B2

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object1 |  Object number of first object |  None  
Object2 |  Object number of second object |  None  
FricType |  Friction model type = **1** Shear friction = **2** Coulomb friction = **3** Constant tau friction (only available in 2D) = **4** Hybrid friction |   
FricDefType |  Function data type = **0** Constant = **1** f(time) = **2** f(pressure) = **3** f(temperature) = **4** f(surface stretch) = **5** f(pressure, temperature, surface stretch ) = **6** Pressure-dependent equation (with two parameters: A1, B1) = **7** Strain rate-dependent equation (with two parameters: A1, B1) = **8** Sliding velocity-dependent equation (with two parameters: A1, B1) = **-n** Friction coefficient is defined by user's routine n |   
Friction |  Friction coefficient (or factor) value |   
Ndata |  Number of friction data points |   
Time/Press/Temp/Stretch(i) |  Time or pressure or temperature or surface stretch of ith data pair |   
Friction(i) |  Friction coefficient (or factor) value of ith data pair for FricDefType=**1~4** |   
A, B |  Two parameters defined in friction equation for FricDefType=**6~8** |   
  
DEFINITION  
---  
FRCFAC specifies the friction coefficient at the interface between two objects.  
  
REMARKS  
---  
The friction coefficient (or factor) may be specified as a constant value or as a function data. (Function data allows defining friction as a function of time or temperature or interface pressure or surface stretch or as a user routine.) If FricDefType = 0, use the operand Friction. If FricDefType = 1~4, each data pair should be provided on a separate line, resulting in Ndata lines of Time/Press/Temperature,Surface stretch (i), Friction(i). If FricDefType = 5, data set should be provided on a specified format shown above; three lines with Ndata points of Press and Temperature and Surface stretch, respectively and Friction(1,1,1) …. Friction(NPres, NTemp, NStre). If FricDefType = 6~8, two friction parameters defined the selected pressure, strain rate, and sliding velocity dependent friction equations should be provided. If FricDefType = -n, the friction factor is specified as user routine and FricDefType specifies the routine number(FricUsrRt). If FricType = 4, hybrid friction model, consisting of Coulomb friction and constant shear friction, is used. In this case, friction data for Coulomb friction portion and constant shear friction portion should be defined together. Constant shear factor friction is generally used to model bulk forming processes while Coulomb friction is usually used to model sheet forming processes. For constant shear factor friction (FricType = 1), 0 < Friction factor < 1\. The contact between plastic (or porous) and plastic (or porous), the frictional stress is calculated using the flow stress of the slave object. If contact occurs between elastic and elastic (or rigid) objects Coulomb friction is used. Applicable object types: [Rigid](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.5._Rigid), [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous)..  
  
RELATED TOPICS  
---  
Inter-Object conditions: Deformation Keyword: [CNTACT (2D)](/docs/sk/keyword_documentation/c/cntact/), [CNTACT (3D)](/docs/sk/keyword_documentation/c/cntact_3d/),[CNTMTH (3D)](/docs/sk/keyword_documentation/c/cntmth/), [SEPRES](/docs/sk/keyword_documentation/s/sepres/), [SEPDEN (2D)](/docs/sk/keyword_documentation/s/sepden/)

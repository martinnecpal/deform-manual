---
lang: sk
title: "ANISO (2D3D)"
---

# ANISO

|  (Material Data)  
---|---  
_Update History:_ (New) Polycrystal Plasticity-based model has been added in v11 |  Last updated on : 29-07-2013  
  
* * *

ANISO specifies the various Hill’s anisotropic yield function (updated in v11) 

ANISO Material, YieldType, NoOfCoef, FuncType (for FuncType = 0)  
1   
0.0, Coef1, Coef2, Coef3, Coef4, Coef5, Coef6  
or   
ANISO Material, YieldType, NoOfCoef, FuncType Ndata, Mdata  
n (for FuncType = 1, 2)  
Temp/Strain(1), Coef1(1), Coef2(1), Coef3(1), Coef4(1), Coef5(1), Coef6(1)  
Temp/Strain(2), Coef1(2), Coef2(2), Coef3(2), Coef4(2), Coef5(2), Coef6(2)  
...   
Temp/Strain(n), Coef1(n), Coef2(n), Coef3(n), Coef4(n), Coef5(n), Coef6(n)  
or   
n, m (for FuncType = 3)  
Strain(1), Strain(2), ... Strain(n)  
Temp(1), Temp(2), ... Temp(m)  
Coef1(1,1), Coef1(2,1), ..., Coef1(n-1, m), Coef1(n, m)  
Coef2(1,1), Coef2(2,1), ..., Coef2(n-1, m), Coef2(n, m)  
Coef3(1,1), Coef3(2,1), ..., Coef3(n-1, m), Coef3(n, m)  
Coef4(1,1), Coef4(2,1), ..., Coef4(n-1, m), Coef4(n, m)  
Coef5(1,1), Coef5(2,1), ..., Coef5(n-1, m), Coef5(n, m)  
Coef6(1,1), Coef6(2,1), ..., Coef6(n-1, m), Coef6(n, m)  
or   
n, m (for FuncType = 4)  
RodOrt(1), RodOrt(2), ... RodOrt(n)  
Temp(1), Temp(2), ... Temp(m)  
Coef2(1,1), Coef2(2,1), ..., Coef2(n-1, m), Coef2(n, m)  
Coef3(1,1), Coef3(2,1), ..., Coef3(n-1, m), Coef3(n, m)  
Coef4(1,1), Coef4(2,1), ..., Coef4(n-1, m), Coef4(n, m)  
Coef5(1,1), Coef5(2,1), ..., Coef5(n-1, m), Coef5(n, m)  
Coef6(1,1), Coef6(2,1), ..., Coef6(n-1, m), Coef6(n, m)  
or   
ANISO Material, YieldType(=-N) (for YieldType =-N)  
(N is the user routine number)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Material |  Material Number |  None  
YieldType |  Anisotropic yield function type  
= **0** None   
= **1** Hill - FGHLMN   
= **2** Hill - R0,R45,R90  
= **3** Lankford \- R value  
= **4** Polycrystal Plasticity (new in v11)  
= **-N** User routine number | 0  
NoOfCoef |  Number of coefficients  
= **6** (when YieldType = 1, 4)  
= **3** (when YieldType = 2)  
= **1** (when YieldType = 3) | None  
FuncType |  Type of function data  
= 1: Function of temperature   
= 2: Function of strain  
= 3: Function of temperature and strain  
= 4: Function of Rodrigues space and temperature (new in v11) |  None  
  
DEFINITION  
---  
ANISO specifies the various Hill’s anisotropic yield function.  
  
REMARKS  
---  
When Hill’s quadratic (Polycrystal Plasticity) anisotropy yield function is selected (YieldType=4), texture information (crystal type, texture type) should be defined in Material dialog. At each material point of an object, orientation distribution functions will be evaluated as explained in keyword [TXTODF](/docs/sk/keyword_documentation/t/txtodf/). Applicable object types: [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), Note: Anisotropy is not available in “Torsion” mode in 2D.  
  
RELATED TOPICS  
---  
[Flow stress](/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_flow_stress_models/), [Plastic object](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic)  
Keywords: [TXTURE](/docs/sk/keyword_documentation/t/txture/), [TXTODF](/docs/sk/keyword_documentation/t/txtodf/)

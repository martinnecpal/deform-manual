---
lang: en
title: "CREEP (2D3D)"
---

# CREEP

|  (Material Data)  
---|---  
_Update History:_ (New) Definition has been extended in v11 V11 – Type = 6 and 7 have been added |  Last updated on : 29-07-2013  
  
* * *

Creep behavior can be defined as one of the 16 types, or as a user subroutine.

Date |  Creep Model |  Type No  
---|---|---  
|  Prezyna model ![]({{ '/assets/equations/keyword_documentation/c/creep_eq_1.jpg' | relative_url }}) | 1  
|  Power law without yielding ![]({{ '/assets/equations/keyword_documentation/c/creep_eq_2.jpg' | relative_url }}) | 2  
|  Baily-Nortons model ![]({{ '/assets/equations/keyword_documentation/c/creep_eq_3.jpg' | relative_url }}) | 3  
|  Soderberg’s model ![]({{ '/assets/equations/keyword_documentation/c/creep_eq_4.jpg' | relative_url }}) | 4  
|  Temperature-stress-strain dependent model ![]({{ '/assets/equations/keyword_documentation/c/creep_eq_6.jpg' | relative_url }}) | 5  
|  Temperature-stress-time dependent model ![]({{ '/assets/equations/keyword_documentation/c/creep_eq_5.jpg' | relative_url }}) | 6  
New in v11 |  Table data with linear interpolation ![]({{ '/assets/equations/keyword_documentation/c/creep_eq_7.jpg' | relative_url }}) : linear interpolation  | 7  
New in v11 |  Table data with linear interpolation ![]({{ '/assets/equations/keyword_documentation/c/creep_eq_7.jpg' | relative_url }}) : log interpolation  | 8  
|  User specified flow stress routine | N  
  
Each creep model is documented separately below.

* * *

DEFINITION  
---  
CREEP specifies the creep model being considered in a simulation.  
  
REMARKS  
---  
Creep is defined as the time-dependent permanent deformation under stress that usually occurs at high temperatures. It is common in applications where the material undergoes cyclic loading. The keyword CREEP must only be used with elasto-plastic objects. In addition, the keyword CREEP must be activated for each object. System Unit: (s-1) Applicable simulation modules: Deformation, Thermal Applicable object types: Elastoplastic  
  
RELATED TOPICS  
---  
FSTRES  
  
Creep model (Type = 1~4)

* * *

CREEP Material, Type (=1~4), Ndata, Ndim  
Temp(1), Parameter a(1), … , Parameter b(1,Ndim)  
::   
Temp(Ndata), Parameter a(Ndata), … , Parameter b (Ndata, Ndim)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Material |  Material group number |  None  
Type |  Type of method = **1** ![]({{ '/assets/equations/keyword_documentation/c/creep_eq_1.jpg' | relative_url }}) Prezyna Model = **2** ![]({{ '/assets/equations/keyword_documentation/c/creep_eq_2.jpg' | relative_url }}) Power law without yielding = **3** ![]({{ '/assets/equations/keyword_documentation/c/creep_eq_3.jpg' | relative_url }}) Baily-Norton’s model = **4** ![]({{ '/assets/equations/keyword_documentation/c/creep_eq_4.jpg' | relative_url }}) Soderberg’s model |   
Ndata |  Number of data points |   
Ndim |  Size of array (fixed for method type) |   
Temp(i) |  Temperature of ith data set |   
Parameter(i) |  Parameter of ith data set |   
  
REMARKS  
---  
Parameters: ![]({{ '/assets/equations/keyword_documentation/c/gamma.jpg' | relative_url }}) = fluidity ![]({{ '/assets/equations/keyword_documentation/c/sigma.jpg' | relative_url }}) = effective stress ![]({{ '/assets/equations/keyword_documentation/c/s.jpg' | relative_url }})= flow stress t = time ![]({{ '/assets/equations/keyword_documentation/c/t.jpg' | relative_url }}) = absolute temperature ![]({{ '/assets/equations/keyword_documentation/c/m.jpg' | relative_url }}),![]({{ '/assets/equations/keyword_documentation/c/n.jpg' | relative_url }}),![]({{ '/assets/equations/keyword_documentation/c/r.jpg' | relative_url }}),![]({{ '/assets/equations/keyword_documentation/c/k.jpg' | relative_url }}),![]({{ '/assets/equations/keyword_documentation/c/q.jpg' | relative_url }}) = material parameters The user must input the fluidity data and make sure that the flow stress is defined properly. Type 1: (![]({{ '/assets/equations/keyword_documentation/c/t.jpg' | relative_url }}),![]({{ '/assets/equations/keyword_documentation/c/gamma.jpg' | relative_url }}),![]({{ '/assets/equations/keyword_documentation/c/m.jpg' | relative_url }})) data triplet’s entry In this method creep will not occur until the effective stress exceeds the yield strength of the material. Type 2: (t,![]({{ '/assets/equations/keyword_documentation/c/gamma.jpg' | relative_url }}),![]({{ '/assets/equations/keyword_documentation/c/m.jpg' | relative_url }})) data triplet’s entry Type 3: ( t,![]({{ '/assets/equations/keyword_documentation/c/k.jpg' | relative_url }}),![]({{ '/assets/equations/keyword_documentation/c/n.jpg' | relative_url }}),![]({{ '/assets/equations/keyword_documentation/c/m.jpg' | relative_url }}),![]({{ '/assets/equations/keyword_documentation/c/q.jpg' | relative_url }}),![]({{ '/assets/equations/keyword_documentation/c/r.jpg' | relative_url }})) data entry The user should make sure that ![]({{ '/assets/equations/keyword_documentation/c/k.jpg' | relative_url }}) and ![]({{ '/assets/equations/keyword_documentation/c/q.jpg' | relative_url }}) are in the proper units so that the strain rate is defined as 1/s. Type 4: (![]({{ '/assets/equations/keyword_documentation/c/t.jpg' | relative_url }}) ,![]({{ '/assets/equations/keyword_documentation/c/k.jpg' | relative_url }}),![]({{ '/assets/equations/keyword_documentation/c/n.jpg' | relative_url }}), ![]({{ '/assets/equations/keyword_documentation/c/c.jpg' | relative_url }}) ) data entry  
  
Creep model (Type = 5, 6)

* * *

CREEP Material, Type (=5,6)  
Nstrain/Ntime, Nstress, Ntemp  
Strain/Time(1), ..., Strain/Time(Nstrain)  
Stress(1), ..., Stress(Nstress)  
Temp(1), ..., Temp(Ntemp)  
Strain-rate (1, 1, 1), ..., Strain-rate (Nstrain/NTime, 1, 1),  
: :  
Strain-rate(1, Nstress, Ntemp), ..., Strain-rate (Nstrain/Ntime, Nstress, Ntemp)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Material |  Material group number |  None  
Type |  Type of method = **5** ![]({{ '/assets/equations/keyword_documentation/c/creep_eq_6.jpg' | relative_url }}) = **6** ![]({{ '/assets/equations/keyword_documentation/c/creep_eq_5.jpg' | relative_url }}) |   
Nstrain/Ntime |  Number of strain or time data |   
Nstress |  Number of strain data |   
Ntemp |  Number of temperature data |   
Strain(i)/Time(i) |  Strain or time of ith data set |   
Stress(i) |  Stress of ith data set |   
Temp(i) |  Temperature of ith data set |   
Strain-rate(i,j,k) |  Strain-rate of (i,j,k)th data set |   
  
Creep model (Type = 7, 8)

* * *

CREEP Material, Type (=7,8)  
NVars   
NdataX1, X1_ID1, X1_ID2  
NdataX2, X2_ID1, X2_ID2  
X1(1), ... ,X1(NdataX1)  
X2(1), …, XN(NdataX2)  
CRP(1,1)   
::   
CRP(NdataX1,1)   
CRP(1, NdataX2)  
::   
CRP(NdataX1, NdataX2)

Note: Examplar format given here is for 2D. For 2D, CRP(X1, X2) is saved in 1D array in DB file.

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Material |  Material number |  None  
Method |  Flow stress type  = **7** ![]({{ '/assets/equations/keyword_documentation/c/creep_eq_7.jpg' | relative_url }}) with linear interpolation =**8** ![]({{ '/assets/equations/keyword_documentation/c/creep_eq_7.jpg' | relative_url }})with log interpolation |   
NVars |  Number of independent variables |   
NdataX1 |  Number of data for 1st variable |   
NdataX2 |  Number of data for 2nd variable |   
X1_ID1 |  1st ID of 1st variable |   
X1_ID2 |  2nd ID of 1st variable |   
X2_ID1 |  1st ID of 2nd variable |   
X2_ID2 |  2nd ID of 2nd variable |   
CRP(i,j) |  Creep function data |

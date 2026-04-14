---
lang: sk
title: "DIFBND (2D3D)"
---

# DIFBND

|  (Material data)  
---|---  
_Update History:_ (New keyword in v11) |  Last updated on : 23-07-2013  
  
* * *

DIFBND Material, FuncType(=0), DiffTime

or

(For diffusion bonding time as a function of temperature & pressure)

DIFBND Material, FuncType, NTemp, NPres

Temp(1), ..., Temp(NTemp)

Press(1), ..., Press(NPres)

DiffTime(1, 1), ..., DiffTime (NTemp, 1)

: :

DiffTime (1, NPres), ..., DiffTime (NTemp, NPres)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Material |  Material Number |  None  
FuncType |  Diffusion bonding data type = **0** Constant =**7** Function of temperature and pressure |  0  
DiffTime  |  Diffusion bonding time value |  0  
NTemp |  Number of temperature data |   
NPres |  Number of pressure data |   
Temp(i) |  Temperature of ith data |   
Pres(i) |  Pressure of ith data |   
DiffTime(i,j) |  Diffusion bonding time of ith and jth data |   
  
DEFINITION  
---  
DIFBND specifies the required time to achieve 100% bonding under certain conditions (temperature, pressure).  
  
REMARKS  
---  
The time to achieve complete bonding is a strong function of temperature and pressure. ![]({{ '/assets/images/keyword_documentation/d/difbnd_image001.jpg' | relative_url }}) Example of experimental and predicted diffusion bonding times (---- Experimental, - - - theoretical) ![]({{ '/assets/images/keyword_documentation/d/difbnd_image002.jpg' | relative_url }}) Time vs Pressure Plot Temperature and pressure are location and time dependent in real process. Thus, simulation uses an effective bonding completion. Applicable object types: [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic) Applicable simulation type: Superplastic forming  
  
RELATED TOPICS  
---  
Keywords: [GBMOBI](/docs/sk/keyword_documentation/g/gbmobi/), [GBENGY](/docs/sk/keyword_documentation/g/gbengy/), [NUCSIZ](/docs/sk/keyword_documentation/n/nucsiz/), [COARSE](/docs/sk/keyword_documentation/c/coarse/)

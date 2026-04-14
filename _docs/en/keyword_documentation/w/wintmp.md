---
lang: en
title: "WINTMP (2D)"
---

# WINTMP

|  (Object data - 2D)  
---|---  
_Update History:_ (New) Definition has been extended and Heat exchange via heat flux was added in v10.0 |  Last updated on : 08-08-2013  
  
* * *

WINTMP Object, Iwin, Ndata, Ttype, Ctype, Rtype, SpdType, Htype

Velx, Vely

X(1), Y(1)

::

X(Ndata), Y(Ndata)

(Environment temperature)

(if Ttype=0)

TempValue

(if Ttype=1)

Ndata

Time Temp(1)

::

Time Temp(Ndata)

(Convection coefficient)

(if Ctype=0)

ConvValue

(if Ctype=1 or 2)

Ndata

Time/Temp(1) Conv(1)

::

Time/Temp(Ndata) Conv(Ndata)

(if Ctype = 3)

NumTim, NumTemp

Time(1) ... Time(NumTim)

Temp(1) ... Temp(NumTemp)

Conv(1) ... Conv(NumTim*NumTemp)

(Emissivity)

(if Rtype=0)

EmsValue

(if Rtype=1 or 2)

Ndata

Time/Temp(1) Ems(1)

::

Time/Temp(Ndata) Ems(Ndata)

(Heat flux)

(if Htype=0)

Heat flux value

(if Htype=1)

Ndata

Time(1) Heat flux(1)

::

Time(Ndata) Heat flux(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Iwin |  Heat exchange window index |  None  
Ndata |  Number of data pairs for window coord. |  None  
Ttype |  Type of temperature definition  
= **0** Constant = 1 Function of time |  0  
Ctype |  Type of convection coefficient definition =**0** Constant  =**1** Function of time  =**2** Function of temperature  =**3** Function of time and temp. (not implemented GUI) |  0  
Rtype |  Type of Radiation view factor =**0** Constant =**1** Function of time =**2** Function of temperature |  0  
Htype |  Type of Heat flux =**0** Constant =**1** Function of time |   
SpdType |  Speed type =**1** Constant  =**2** Function of time  =**-n** Following object n |  1  
Velx, Vely |  Window speed |  None  
  
DEFINITION  
---  
WINTMP specifies the heat exchange window for an object. The keyword should be used if the boundary condition of heat exchange is different at a specific region than the rest of the object.  
  
REMARKS  
---  
The keyword defines the heat exchange information such as temperature, convection coefficient, the radiation view factor, and heat flux. Applicable Simulation Types: Heat Transfer Applicable object types: ALL except Rigid.  
  
RELATED TOPICS  
---  
[Boundary Constraints](/docs/en/pre_processor/14_boundary_conditions/14_boundary_conditions/): [Deformation](/docs/en/pre_processor/14_boundary_conditions/14_2_deformation_boundary_conditions/) \- [Heat exchange windows](../../pre_processor/14_boundary_conditions/14_3_thermal_boundary_conditions.htm#Heat_Exchange_windows) Keywords: [ENVTMP](/docs/en/keyword_documentation/e/envtmp/), [CNVCOF](/docs/en/keyword_documentation/c/cnvcof/), [LOCTMP](/docs/en/keyword_documentation/l/loctmp/)

---
lang: en
title: "WINTMP (3D)"
---

# WINTMP

|  (Object data - 3D)  
---|---  
_Update History:_ v10.0 – Heat exchange via heat flux was added. |  Last updated on : 12-08-2013  
  
* * *

WINTMP Object, Iwin, WindowShape, Ttype, Ctype, Rtype, SpdType, Htype

Velx, Vely, Velz

(if WindowShape = 1, box defined by 8 corners)

Point(1), X(1), Y(1), Z(1)

::

Point(8), X(8), Y(8), Z(8)

(if WindowShape = 2, cylinder)

OriginA_X, OriginA_Y, OriginA_Z

OriginB_X, OriginB_Y, OriginB_Z

inner radius, outer radius

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
WindowShape |  Shape of the heat exchange window  = **1** rectangular = **2** cylindrical. |  None  
Ttype |  Type of temperature definition = **0** constant  = **1** function of time |  0  
Ctype |  Type of convection coefficient definition =**0** constant =**1** function of time =**2** function of temperature =**3** function of time and temp. (not implemented GUI) |  0  
Rtype |  Type of Radiation view factor  = **0** constant = **1** function of time = **2** function of temperature |  0  
Htype |  Type of Heat flux = **0** constant = **1** function of time |  0  
SpdType |  Speed type = **1** constant = **2** function of time =**-n** following object n |  1  
Velx, Vely, Velz |  Window speed |  None  
  
DEFINITION  
---  
WINTMP specifies the heat exchange window for an object. The keyword should be used if the boundary condition of heat exchange is different at a specific region than the rest of the object.  
  
REMARKS  
---  
The keyword defines the heat exchange information such as temperature, convection coefficient, the radiation view factor, and heat flux. Applicable Simulation Types: Heat Transfer Applicable object types: All objects except Rigid object  
  
RELATED TOPICS  
---  
[Boundary Constraints](/docs/en/pre_processor/14_boundary_conditions/14_boundary_conditions/): [Deformation](/docs/en/pre_processor/14_boundary_conditions/14_2_deformation_boundary_conditions/) \- [Heat exchange windows](../../pre_processor/14_boundary_conditions/14_3_thermal_boundary_conditions.htm#Heat_Exchange_windows) Keywords: [ENVTMP](/docs/en/keyword_documentation/e/envtmp/), [CNVCOF](/docs/en/keyword_documentation/c/cnvcof/), [LOCTMP](/docs/en/keyword_documentation/l/loctmp/)

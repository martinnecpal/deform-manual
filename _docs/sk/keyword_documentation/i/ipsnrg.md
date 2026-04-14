---
lang: sk
title: "IPSNRG (2D3D)"
---

# IPSNRG

|  (Inter-material data)  
---|---  
_Update History:_ 3Dv6.1 - IPSNRG was introduced. |  Last updated on : 24-07-2013  
  
* * *

(for constant value)

IPSNRG Material, FuncType(=0), SurfEnergy

(for surface energy as a function of temperature)

IPSNGR Material, FuncType, Ndata

Temp(1), ..., SurfEnergy (1)

: :

Temp(Ndata), ..., SurfEnergy(Ndata)

(for surface energy as a function of misorientation angle)

IPSNGR Material, FuncType, Ndata

Angle(1), ..., SurfEnergy(1)

: :

Angle(Ndata), ..., SurfEnergy (Ndata)

(for surface energy as a function of temperature and misorientation angle)

IPSNGR Material, FuncType, NTemp, NAngle

Temp(1), ..., Temp(NTemp)

Angle(1), ..., Angle(NAngle)

SurfEnergy(1, 1), ..., SurfEnergy(NTemp, 1)

: :

SurfEnergy(1, NAngle), ..., SurfEnergy(NTemp, NAngle)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Material |  Material number |  None  
FuncType |  Surface energy function type = **0** Constant = **1** Function of temperature and pressure = **2** Function of misorientation angle = **3** Function of temperature and misorientation angle |  0  
SurfEnergy |  Surface energy value |  0  
Ndata |  Number of temperature data pair |  0  
SurfEnergy(j) |  Surface energy of ith data pair |  None  
NTemp |  Number of temperature data |  0  
NAngle |  Number of misorientation angle data |  0  
Temp(i) |  Temperature of ith data |  0  
Angle(j) |  Misorientation angle of jth data |  0  
VolFrac(i,j) |  Surface energy of ith and jth data |  0  
  
DEFINITION  
---  
IPSNRG specifies the interface surface energy.  
  
RELATED TOPICS  
---  
Related keywords: [GBMOBI](/docs/sk/keyword_documentation/g/gbmobi/), [GBENGY](/docs/sk/keyword_documentation/g/gbengy/), [COARSE](/docs/sk/keyword_documentation/c/coarse/)

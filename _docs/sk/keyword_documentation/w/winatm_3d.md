---
lang: sk
title: "WINATM (3D)"
---

# WINATM

|  (Object data - 3D)  
---|---  
|  Last updated on : 12-08-2013  
  
* * *

WINATM Object, WinNo, WindowShape, AtmType, SRCtype

Velx, Vely, Velz

window corrdinate data :

{

if WindowShape = 1 (box defined by 8 corners)

Point(1), X(1), Y(1), Z(1)

: : :

Point(8), X(8), Y(8), Z(8)

If WindowShape = 2 (Cylinder)

OriginA_X, OriginA_Y, OriginA_Z

OriginB_X, OriginB_Y, OriginB_Z

inner radius, outer radius

}

Atom content data :

{

If AtmType = 0:

AtmValue

If AtmType = 1:

Ndata

Time(1) Atom(1)

: :

Time(Ndata) Atom(Ndata)

}

Surface reaction coefficient data :

{

If SRCtype=0

SRCvalue

If SRCtype=1 or 2

Ndata

Time/Atom(1) SRC(1)

: :

Time/Atom(Ndata) SRC(Ndata)

If SRCtype = 3

NumTim NumAtm

Time(1) ... Time(NumTim)

Atom(1) ... Atom(NumAtm)

SRC(1) ... SRC(NumTim*NumAtm)

}

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
WinNo  |  Window number |   
WindowShape  |  Shape of window definition  = **1** rectangular = **2** cylindrical |   
AtmType |  Type of atom content definition  =**0** constant =**1** function of time |  None  
SRCtype |  Type of surface reaction coefficient definition =**0** constant =**1** function of time =**2** function of atom content =**3** function of time and atom content |   
  
DEFINITION  
---  
WINATM specifies the diffusion window and window parameters for an object.  
  
REMARKS  
---  
Applicable Simulation Modules: Microstructure Applicable Simulation Mode: Transformation  
  
RELATED TOPICS  
---  
[Boundary Constraints](/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/): [Diffusion windows](../../pre_processor/14_boundary_conditions/14_4_diffusion_boundary_conditions.htm#14.4.1._Diffusion_with_the_environment_BCC_) Keywords: [ENVATM](/docs/sk/keyword_documentation/e/envatm/), [ACVCOF](/docs/sk/keyword_documentation/a/acvcof/), [LOCATM](/docs/sk/keyword_documentation/l/locatm/)

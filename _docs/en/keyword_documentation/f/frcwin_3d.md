---
lang: en
title: "FRCWIN (3D)"
---

# FRCWIN

|  (Inter-Object data - 3D)  
---|---  
|  Last updated on : 06-08-2014  
  
* * *

FRCWIN Object1, Object2, WinNo, WinShape, FricType(=1~3), FricDefType,

Friction/NData, SpdType

VelX, VelY, VelZ

If WinShape = 1, parallelipiped defined by 8 corners

Point(1), X(1), Y(1), Z(1)

: : :

Point(8), X(8), Y(8), Z(8)

Else if WinShape = 2: Cylinder

OriginA_X, OriginA_Y, OriginA_Z

OriginB_X, OriginB_Y, OriginB_Z

Inner radius, Outer radius

if (FricDefType =1~4)

Time/Press/Temp/Stretch(1), Friction(1)

: :

Time/Press/Temp/Stretch (Ndata), Friction(Ndata)

if (FricDefType =5)

NPres, NTemp, NStre

Press(1), ..., Press(NPres)

Temp(1), ..., Temp(NTemp)

Stretch(1), ..., Stretch(NStre)

Friction(1, 1, 1), ..., Friction(NPres, 1, 1)

: :

Friction(1, NTemp, NStre), ..., Friction(NPres, NTemp, NStre)

if (FricDefType =6~8)

A, B

if (FricDefType =-n)

FricUsrRt, Dummy

or (for hybrid friction model)

FRCWIN Object1, Object2, WinNo, WinShape, FricType(=4), Dummy, Dummy2, SpdType

VelX, VelY, VelZ

If WinShape = 1, parallelipiped defined by 8 corners

Point(1), X(1), Y(1), Z(1)

: : :

Point(8), X(8), Y(8), Z(8)

Else if WinShape = 2: Cylinder

OriginA_X, OriginA_Y, OriginA_Z

OriginB_X, OriginB_Y, OriginB_Z

Inner radius, Outer radius

( ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})Coulomb Friction Data)

if (FricDefType =0)

FricDefType, Friction

if (FricDefType =-n)

FricUsrRt, Dummy

if (FricDefType =1~4)

FricDefType, Ndata

Time/Press/Temp/Stretch(1), Friction(1)

: :

Time/Press/Temp/Stretch (Ndata), Friction(Ndata)

if (FricDefType =5)

FricDefType, NPres, NTemp, NStre

Press(1), ..., Press(NPres)

Temp(1), ..., Temp(NTemp)

Stretch(1), ..., Stretch(NStre)

Friction(1, 1, 1), ..., Friction(NPres, 1, 1)

: :

Friction(1, NTemp, NStre), ..., Friction(NPres, NTemp, NStre)

if (FricDefType =6~8)

FricDefType, A, B

( ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})Shear Friction Data)

if (FricDefType2 =0)

FricDefType2, Friction2

if (FricDefType2 =-n)

FricUsrRt2, Dummy

if (FricDefType2 =1~4)

FricDefType2, Ndata2

Time/Press/Temp/Stretch(1), Friction(1)

: :

Time/Press/Temp/Stretch (Ndata2), Friction(Ndata2)

if (FricDefType2 =5)

FricDefType, NPres2, NTemp2, NStre2

Press(1), ..., Press(NPres2)

Temp(1), ..., Temp(NTemp2)

Stretch(1), ..., Stretch(NStre2)

Friction(1, 1, 1), ..., Friction(NPres2, 1, 1)

: :

Friction(1, NTemp2, NStre2), ..., Friction(NPres2, NTemp2, NStre2)

if (FricDefType2 =6~8)

FricDefType2, A2, B2

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object1 |  Object number of first object |  None  
Object2 |  Object number of second object |  None  
WinNo |  Index of current friction window |  None  
WinShape |  Shape of the window: =**1** : box; =**2** : cylinder |  1  
FricType |  Friction type None = **1** Shear friction = **2** Coulomb friction = **3** Constant tau friction (only available in 2D) = **4** Hybrid friction |   
FricDefType |  Function data type =**0** Constant = **1** f(time) = **2** f(pressure) = **3** f(temperature) =**4** f(surface stretch) = **5** f(pressure, temperature, surface stretch ) =**6** Pressure-dependent equation (with two parameters: A1, B1) = **7** Strain rate-dependent equation (with two parameters: A1, B1) = **8** Sliding velocity-dependent equation (with two parameters: A1, B1) = **-n** Friction coefficient is defined by user's routine n |   
Friction |  Friction coefficient (or factor) value when FricDefType = **0** |   
Ndata |  Number of Time/Press friction coefficient data pairs |  None  
SpdTyp |  Speed type: =**1** : contant;**-n** : following object n |  0  
VelX |  X component of window velocity |  0.0  
VelY |  Y component of window velocity |  0.0  
VelZ |  Z component of window velocity |  0.0  
Point(i) |  Index of ith points describing area |  None  
X(i),Y(i),Z(i) |  Coordinate of ith point in defined area |  0.0  
OriginA_X, OriginA_Y, OriginA_Z |  Coordinates of bottom origin of cylinder |  0.0  
OriginB_X, OriginB_Y, OriginB_Z |  Coordinates of top origin of cylinder |  0.0  
inner radius, outer radius |  Inner and outer radii of cylinder |  0.0  
Time/Press/Temp/Stretch(i) |  Time or pressure or temperature or surface stretch of ith data pair |   
Friction(i) |  Friction coefficient (or factor) value of ith data pair for **FricDefType= 1~4** |   
A, B |  Two parameters defined in friction equation for **FricDefType= 6~8** |   
  
DEFINITION  
---  
FRCWIN specifies a user defined friction window. A specific friction model can be defined at any inter-object interfaces inside the window area. A multiple number of friction windows can be created and each individual window can move along with the master objects as the simulation is running.  
  
REMARKS  
---  
The desired window is specified using WinShape 1 or 2, for WinShape=1 8 cornered parallelipiped (X,Y,Z) coordinates are defined and for WinShape=2 Cylinder is defined by Top and Bottom face center coordinates and inner and outer radius. Within this window a friction coefficient is set, which will be used in place of any value set in FRCFAC for the specified object pair. The friction coefficient (or factor) may be specified as a constant value or as a function data. (Function data allows defining friction as a function of time or temperature or interface pressure or surface stretch or as a user routine.) If FricDefType = 0, use the operand Friction. If FricDefType = 1~4, each data pair should be provided on a separate line, resulting in Ndata lines of Time/Press/Temperature,Surface stretch (i), Friction(i). If FricDefType = 5, data set should be provided on a specified format shown above; three lines with Ndata points of Press and Temperature and Surface stretch, respectively and Friction(1,1,1) …. Friction(NPres, NTemp, NStre). If FricDefType = 6~8, two friction parameters defined the selected pressure, strain rate, and sliding velocity dependent friction equations should be provided. If FricDefType = -n, the friction factor is specified as user routine and FricDefType specifies the routine number(FricUsrRt). If FricType = 4, hybrid friction model, consisting of Coulomb friction and constant shear friction, is used. In this case, friction data for Coulomb friction portion and constant shear friction portion should be defined together. Constant shear factor friction is generally used to model bulk forming processes while Coulomb friction is usually used to model sheet forming processes. For constant shear factor friction (FricType = 1), 0 < Friction factor < 1\. The contact between plastic (or porous) and plastic (or porous), the frictional stress is calculated using the flow stress of the slave object. If contact occurs between elastic and elastic (or rigid) objects Coulomb friction is used. Applicable object types: [Rigid](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.5._Rigid), [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).

---
lang: en
title: "ENVTMP (2D3D)"
---

# ENVTMP

|  (Simulation control)  
---|---  
_Update History:_ V11 – Furnace definition (Ftype=10) has been added. |  Last updated on : 30-07-2013  
  
* * *

ENVTMP Ftype, Etemp or ENVTMP Ftype, Ndata (for Ftype =0 or 1)

Time(1), Etemp(1)

: :

Time(Ndata), Time(Ndata)

or

ENVTMP Ftype, Ndata (for Ftype =10)

1, GFDim,Ftype1, Nset1, Ndim1

1, Data1(1,1), Data1(2,1), …, Data1(Ndim1,1)

: :

Nset1, Data1(1,Nset1), Data1(2, Nset1), …, Data1(Ndim1, Nset1)

: :

Ndata, GFDimN, FtypeN, NsetN, NdimN

1, DataN(1,1), DataN(2,1), …, DataN(NdimN,1)

: :

NsetN, DataN(1,NsetN), DataN(2, NsetN), …, DataN(NdimN, NsetN)

(if FtypeN > 0)

Ndata, GFDimN, FtypeN, NsetN, NdimN

DataN(1,1), DataN(2,1), …, DataN(NdimN,1)

::

DataN(1, NsetN), DataN(2, NsetN), …, DataN(NdimN, NsetN)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Ftype |  Function type: **0** = Constant environment temperature **1** = Time dependent environment temperature **10** = Furnace temperature |  0  
Etemp |  Environment temperature |  20C or 68F  
(for Ftype = 1)  
Ndata |  Number of time/temperature data pairs |  None  
Time(i) |  Time of ith data pair |  None  
Etemp(i) |  Environment temperature of ith data pair |  None  
(for Ftype = 10)  
Ndata |  Number of data sections for furnace definition |  20  
GFDimN |  Section function dimension **0** = Reserved **1** = Support NsetN x NdimN data sets DataN(i,j) |  1  
FtypeN |  Function type of section N **0** = Type none, index number starts in each line **1** = Function of time **2** = Function of temperature |  0  
NsetN |  Number of data sets defined in section N |  0  
NdimN |  Dimension of data sets defined in section N |  0  
DataN(i,j) |  Value of the i,jth data defined in section N |   
  
DEFINITION  
---  
The environment temperature is used in radiation and convection heat transfer calculations and represents the room temperature of the area in which the manufacturing process is taking place.  
  
REMARKS  
---  
The environment temperature may be specified as a constant value or as a set of discrete time/temperature pairs, or even calculated by defining furnace parameters. If Ftype = 0 use the operand Etemp. If Ftype = 1 use the operands Ndata, Time(i), Etemp(i). Each time/temperature pair should be provided on a separate line. When process time lies within the specified data range, linear interpolation is used to determine the environment temperature. When process time lies outside the specified data range, linear extrapolation is used to determine the environment temperature. If Ftype = 10 use the operands Ndata, FtypeN, NsetN, NdimN, DataN(i,j). Total Ndata of sections are defined for furnace definition. And each section should be provided in NsetN lines of NdimN data values. Applicable simulation types: Heat Transfer, Non-Isothermal Deformation  
  
RELATED TOPICS  
---  
Keywords: [BLZMAN](/docs/en/keyword_documentation/b/blzman/), [CNVCOF](/docs/en/keyword_documentation/c/cnvcof/), [FRNNAM](/docs/en/keyword_documentation/f/frnnam/)  
  
Followings are the predefined data sections for Furnace:

Section 1 – General

* * *

  * 1, 1, 0, 2, 6

  * 1, IHTSCR, ISVAC, IFSHAP, HINT, FUREF, SCALE

  * 2, NUMOBJ, NUMWAL, NUMLAY, NUMACC, NGRIDS, NTPAIR 

* * *

IHTSCR |  Furnace type  **0** = DT gas-fired **1** = IDT gas-fired **2** = Electric |  2  
---|---|---  
IFSHAP |  Furnace shape **0** = ver_cyl **1** = hor_cyl **2** = box |  1  
ISVAC |  Vacuum furnace flag **1** = vacuum **0** = NOT |  1  
HTINT |  Connected heat input |  0  
FUREF |  Furnace efficiency |  0  
NUMOBJ |  Total number of objects |  0  
NUMWAL |  Total number of walls |  4  
NUMLAY |  Total number of layers |  0  
NUMACC |  Total number of accessories of furnace |  0  
NGRIDS |  Total number of grids of the wall |  0  
NTPAIR |  Total number of data pairs of setting points |  0  
SCALE |  Model scaling factor **0** |  0  
  
Section 2 – Specs

* * *

  * 2, 1, 0, 1, 3

  * 1, ALOAD, AMXTMP, AMNTMP

* * *

ALOAD |  Allowed gross load |  0  
---|---|---  
AMXTMP |  Max. operation temperature |  0  
AMNTMP |  Min. operation temperature |  0  
  
Section 3 – Geometry data of furnace

* * *

  * 3, 1, 0, 1, 6

  * 1, OVH, OVW, OVL, WORKH, WORKW, WORKL

* * *

OVH, OVW, OVL |  Overall furnace height, width, length |  0  
---|---|---  
WORKH,WORKW, WORKL |  Work zone height, width, length |  0  
  
Section 4 – PID parameters

* * *

  * 4, 1, 0, 1, 5

  * 1, IONOFF, PGAIN, IGAIN, SPAN, DAMP

* * *

IONOFF |  On/off flag **0** = Off **1** = On |  0  
---|---|---  
PGAIN |  Proportional gain |  0  
IGAIN |  Integral gain |  0  
SPAN |  Span |  0  
DAMP |  Damping |  0  
  
Section 5 – Combustion parameters

* * *

  * 5, 1, 0, 2, 6

  * 1, IFUEL, HTCNT,COMTMP, EXCAIR, A_G_RATIO, 0.0

  * 2, A11, A12, A13,A21, A22, A23

  * IFUEL Fuel/gas material no. 0

* * *

HTCNT |  Heat content |  0  
---|---|---  
COMTMP |  Temperature of combustion air |  0  
EXCAIR |  Excess air for combustion |  0  
A_G_RATIO |  New Ratio of air to gas |  0  
A11,A12, A13, A21, A22, A23 |  Experiment data for combustion |  0  
  
Section 6 – Cooling system

* * *

  * 6, 1, 0, 2, 3

  * 1, OPENA, FAI, ALT

  * 2, SHCRT, SHCIN, SHCOT

* * *

OPENA |  Opening area |  0  
---|---|---  
FAI |  Given by experience, related to the thickness of furnace wall |  0  
ALT |  Opening rate, 1 for often opened door |  0  
SHCRT |  Cooling water rate |  0  
SHCIN |  Inlet temperature of the shell cooling system |  0  
SHCOT |  Outlet temperature of the shell cooling system |   
  
Section 7 - Fan/blower

* * *

  * 7, 1, 0, 5, 10

  * 1, IFFMTR ,IFFLOC, IFFONFF, FFHP, FFSPD, FFDIA, FFHIGH , 0, 0, 0

  * 2, FFCWRT, FFCWIN, FFCWOT, CONST1, CONST2, 0, 0, 0, 0, 0

  * 3,iFFMAT, FFWGT, Nhrcnd, NHeatcp, NEmsvty, NDensy, 0, IHEATCPFLAG , 0, 0

  * 4,iATMAT, 5, NThrcnd, NHeatcp, NEmsvty, NDensy, 0, IHEATCPFLAG , 0, 0

  * 5, iATMAT,0,NViscsy, 0, 0, 0, 0, 0 , 0, 0

* * *

IFFMTR |  Fan material no. |  0  
---|---|---  
FFHP |  Horse power |  0  
FFSPD |  Speed/velocity |  0  
IFFLOC |  reserved |  0  
IFFONFF |  On/off flag **0** = off **1** = on |  0  
FFDIA |  Diameter of propeller/blade |  0  
FFHIGH |  Height of the propeller/blade |  0  
FFWGT |  Weight of the propeller/blade |  0  
FFCWRT |  Cooling water rate |  0  
FFCWIN |  Inlet water temperature |  0  
FFCWOT |  Outlet water temperature |  0  
CONST1 |  Constant |  520  
CONST2 |  Constant |  460  
iFFMAT |  Material no. of FAN |  0  
iATMAT |  Material no. of Atmosphere |  0  
NThrcnd |  Section number of the material conductivity data |  0  
NHeatcp |  Section number of the material heat capacity data |  0  
NEmsvty |  Section number of the material emissivity data |  0  
NDensy |  Section number of the material density data |  0  
NViscsy |  Section number of the material viscosity data |  0  
IHEATCPFLAG |  **0** \- Heat capacity |  0  
  
Section 8 - Reserved for common blocks for furnace temperature calculation

* * *

  * 8, 1, 0, 10, 5

  * 1, IMAXITR ,DERROR, DPENT, 0.0, 0.0

  * 2, IHYBRID, ISEXPLICIT, ITSOLV_EXPT, 0.0, 0.0

  * 3,IUSURCODE, ICONTACT, DCONTHTC, 0.0, 0.0, 0.0

  * 4,WATER_HEATCP,WATER_DENSY,DENVT,DENVHTC,0.0

  * 5,COEFSUR(1),COEFSUR(2),COEFSUR(3),GASNATRUAL_HTCNT,0.0

  * 6,TMP_AB,TAMB_IN_K,TAMB,0.0, BLZMAN

  * 7,0.0,0.0,0.0,0.0,0.0

  * 8,0.0,0.0,0.0,0.0,0.0

  * 9,0.0,IBASIZE,INOTFIRST,IPRNTFLAG,0.0,

  * 10,CURTIM0,CURTMP0,CURTIM,CURTMP,DTIME

* * *

CURTIM |  Current time |  0  
---|---|---  
  
Section 9 - Energy items

* * *

  * 9, 1, 0, 11, 2

  * 1, Eitem(1), TotEitem(1)

  * …

  * 11, Eitem(11), TotEitem(11)

* * *

Eitem(i) |  Energy items |  0  
---|---|---  
TotEitem(i) |  Total energy consuming at the current step |  0  
  
Section 10 – Reserved for furnace variables

Section 11 – Thermal schedule, time/temperature data pairs:

* * *

  * 11, 1, 1, NTPAIR, 1

  * time(1), Stemp(1)

  * …

  * time(NTPAIR), Stemp(NTPAIR)

* * *

time(j) |  time |  0  
---|---|---  
Stemp(j) |  temperature |  0  
  
Section 12 – Fixture material data section index

* * *

  * 12, 1, 0, NUMFXT, 10

  * 1,,iFxtrMat(i),FxtrWeight(1)NThrcnd(1), NHeatcp(1), NEmsvty(1),

NDensy(1), 0, IHEATCPFLAG(1) , 0, 0

…

  * NUMFXT,iFxtrMat(NUMFXT),FxtrWeight(NUMFXT),NThrcnd(NUMFXT),

NHeatcp(NUMFXT), NEmsvty(NUMFXT), NDensy(NUMFXT), 0,

IHEATCPFLAG (NUMFXT), 0, 0

* * *

iFxtrMat(i) |  Material no. of the ith fixture |  0  
---|---|---  
FxtrWeight(i) |  Weight of the ith fixture |  0  
NThrcnd(j) |  Section number of the ith fixture material conductivity data |  0  
NHeatcp(j) |  Section number of the ith fixture material heat capacity data |  0  
NEmsvty(j) |  Section number of the ith fixture material emissivity data |  0  
NDensy(j) |  Section number of the ith fixture material density data |  0  
  
Section 13 – number of objects in a group with the identical BCCs, and fixture material data section index:

(not in use)

* * *

  * 13, 1, 0, NUMOBJ, 3

  * 1, NumObjs(1), Scale(1), VOLUME(1)

…

  * NUMOBJ, NumObjs(NUMOBJ), Scale(NUMOBJ), VOLUME(NUMOBJ)

* * *

NumObjs(i) |  Number of objects in the ith group |  0  
---|---|---  
Scale(i) |  Scale of the objects in the ith group |  0  
VOLUME(i) |  Volume of the objects in the ith group |  0  
  
Section 14 – Load pattern

* * *

  * 14, 1, 0, 10, 3

  * 1, OBJNO, NPTYPE,0

  * 2, OBJNO_FXT, NPTYPE_FXT,0

  * 3, NRCL(0),NRCL(1),NRCL(2)

  * 4, NRCL_FXT(0),NRCL_FXT(1),NRCL_FXT(2)

  * 5, NSYMOPT(0),NSYMOPT(1),NSYMOPT(2)

  * 6, NSYMOPT_FXT(0),NSYMOPT_FXT(1),NSYMOPT_FXT(2)

  * 7, DOFFSET(0),DOFFSET(1),DOFFSET(2)

  * 8, DOFFSET_FXT(0),DOFFSET_FXT(1),DOFFSET_FXT(2)

  * 9, DINSERTPT(0),DINSERTPT(1),DINSERTPT(2)

  * 10, DINSERTPT_FXT(0),DINSERTPT_FXT(1),DINSERTPT_FXT(2)

* * *

Section 15 – Material number of furnace accessories 

* * *

  * 15, 1, 0, NUMACC, 10

  * 1, iMatNo(1), ACCWeight(1),NThrcnd(1), NHeatcp(1),

NEmsvty(1), NDensy(1), 0, IHEATCPFLAG(1), 0, 0

…

  * NUMACC, iMatNo(NUMACC), ACCWeight(NUMACC),

NThrcnd(NUMACC), NHeatcp(NUMACC), NEmsvty(NUMACC),

NDensy(NUMACC), 0, IHEATCPFLAG(NUMACC), 0, 0 

* * *

iMatNo(j) |  Material number of the ith accessories |  0  
---|---|---  
ACCWeight(j) |  Weight of the ith accessories |  0  
NThrcnd(j) |  Section number of the iMatNo(j) material conductivity data |  0  
NHeatcp(j) |  Section number of the iMatNo(j) material heat capacity data |  0  
NEmsvty(j) |  Section number of the iMatNo(j) material emissivity data |  0  
NDensy(j) |  Section number of the iMatNo(j) material density data |  0  
IHEATCPFLAG(j) |  **0** \- Heat capacity; **1** \- specific heat |  0  
  
Section 16 – Number of layers of furnace wall

* * *

  * 16, 1, 0, NUMWAL, 1

  * 1, nLayers(1)

  * …

  * NUMWAL , nLayers(NUMWAL) 

* * *

nLayers(j) |  Number of layers of the ith wall |  0  
---|---|---  
  
Section 17 – Material number of layers

* * *

  * 17, 1, 0, NUMLAY, 10

  * 1, iLyMatNo(1), LAYThick(1),NThrcnd(1), NHeatcp(1),

NEmsvty(1), NDensy(1), 0, IHEATCPFLAG(1), 0, 0

…

  * NUMLAY, iLyMatNo(NUMLAY), LAYThick(NUMLAY),

NThrcnd(NUMLAY), NHeatcp(NUMLAY), NEmsvty(NUMLAY),

NDensy(NUMLAY), 0, IHEATCPFLAG(NUMACC), 0, 0

* * *

iLyMatNo(j) |  Material number of the ith layer |  0  
---|---|---  
LAYThick(j) |  Thickness of the ith layer |  0  
NThrcnd(j) |  Section number of the iLyMatNo(j) material conductivity data |  0  
NHeatcp(j) |  Section number of the iLyMatNo(j) material heat capacity data |  0  
NEmsvty(j) |  Section number of the iLyMatNo(j) material emissivity data |  0  
NDensy(j) |  Section number of the iLyMatNo(j) material density data |  0  
IHEATCPFLAG(j) |  0 - Heat capacity |  0  
  
Section 18 – Surface grids connections for layers

* * *

  * 18, 1, 0, NUMLAY, 2

  * 1, nGrid_left(1), nGrid_right(1)

  * …

  * NUMLAY, nGrid_left(NUMLAY), nGrid_right(NUMLAY)

* * *

nGrid_left(j) |  Grid number at the left end of the ith layer **0** |  0  
---|---|---  
nGrid_right(j) |  Grid number at the right end of the ith layer |  0  
  
Section 19 – BCC code for surface grids

* * *

  * 19, 1, 0, NUMLAY, 2

  * 1, ITMPBC_left(1), ITMPBC_right(1)

  * …

  * NUMLAY, ITMPBC_left(NUMLAY), ITMPBC_right(NUMLAY)

* * *

ITMPBC_left(j) |  Furnace thermal BCC code of the grid at the left end of the ith layer **1** = innermost surface exposed to the furnace work zone **-n** = contact with the nth layer |  0  
---|---|---  
ITMPBC_right(j) |  Furnace thermal BCC code of the grid at the right end of the ith layer **2** = outermost exposed to the environment **-n** = contact with the nth layer |  0  
  
Section 20 – Grid temperature

* * *

  * 20, 1, 0, NGRIDS, 1

  * nGrid(1), GdTemp(1)

  * …

  * nGrid(NGRIDS) , GdTemp(NGRIDS)

* * *

nGrid(j) |  Grid number |  0  
---|---|---  
GdTemp(j) |  Grid temperature Section NFANThrcnd ~ Section NFANDensy - material data sections for FAN. Section NfxtrThrcnd(1) ~ Section NfxtrDensy(NUMFXT) - material data sections for fixtures. Section NObjThrcnd(1) ~ Section NObjDensy(NUMOBJ) - material density data sections for objects. Section NAccThrcnd(1) ~ Section NAccDensy(NUMACC) - material data sections for furnace accessories. Section NLayThrcnd(1) ~ Section NLayDensy(NUMLAY) - material data sections for furnace layers. |  0

---
lang: sk
title: "FSTRES (2D3D)"
---

# FSTRES

|  (Material data)  
---|---  
_Update History:_ V11 – Types 13, 14, 15, and 16 have been added. V11.1 – Type 17 has been added. |  Last updated on : 25-04-2016  
  
* * *

Flow stress data can be defined as one of the 17 types, or as a user subroutine.

Date |  Flow stress model |  Type No  
---|---|---  
|  CMNY type ![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_1.jpg' | relative_url }}) |  1  
|  Table data ![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_2.jpg' | relative_url }}): log interpolation |  2  
|  Table data ![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_2.jpg' | relative_url }}): linear interpolation |  3  
|  Temp. & Strain-rate dependent I ![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_3.jpg' | relative_url }}) |  4  
|  Temp. & Strain-rate dependent II ![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_4.jpg' | relative_url }}) |  5  
|  Y-H type ![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_5.jpg' | relative_url }}) |  6  
|  Table data ![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_6.jpg' | relative_url }}): log interpolation |  7  
|  Table data ![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_6.jpg' | relative_url }}): linear interpolation |  8  
|  Generalized Johnson & Cook ![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_7.jpg' | relative_url }}) |  9  
|  Zerilli-Armstrong ![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_8.jpg' | relative_url }}) |  10  
New in v11 |  Norton-Hoff ![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_9.jpg' | relative_url }}) |  11  
3Dv6.1 2Dv9.2 |  Microstructure ![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_10.jpg' | relative_url }}) |  12  
New in v11 |  General table data: Log interpolation |  13  
New in v11 |  Bird-Mukherjee-Dorn Equation ![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_11.jpg' | relative_url }}) |  14  
New in v11 |  General table data: Linear interpolation |  15  
New in v11 |  Table data (under development) ![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_12.jpg' | relative_url }}) |  16  
New in v11.1 |  Crystal Plasticity model ![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_13.jpg' | relative_url }}) |  17  
|  User specified flow stress routine |  N  
  
Each flow stress type is documented separately below.

NOTE: Type = 16 has not been fully implemented yet in v11.

Type = 17 has not been fully implemented yet in v11.1; currently only available in Material Suite in v11.1

* * *

CMNY model (Type = 1)

* * *

FSTRES Material, Ftype

c, n, m, y

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Material |  Material number |  None  
Ftype |  Function type = **1** ![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_1.jpg' | relative_url }}) c material constant n strain sensitivity index m strain rate sensitivity index y material constant |  None  
  
DEFINITION  
---  
FSTRES specifies the flow stress for a particular material.  
  
REMARKS  
---  
Flow stress data can be entered as one of 5 flow stress function types, or as a user subroutine. The FSTRES function for Ftype =1 is: | ![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_14.jpg' | relative_url }}) |   
---|---  
  
Applicable simulation types: Isothermal Deformation

Non-Isothermal Deformation

**EXAMPLE**

If the flow stress of material 3 could be expressed as:

![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_15.jpg' | relative_url }}) |   
---|---  
  
The FSTRES keyword representation would be,

FSTRES 3, 1

103.8, 0.22, 0, 0  
  
Table data (Type=2) ![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_2.jpg' | relative_url }}): log interpolation

Table data (Type=3) ![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_2.jpg' | relative_url }}): linear interpolation

* * *

FSTRES Material, Ftype

Nstrain, Nsrate, Ntemp

Strain(1)

:

Strain(Nstrain)

Srate(1)

:

Srate(Nsrate)

Temp(1)

:

Temp(Ntemp)

Stress(i,j,k)

:

Stress(Nstrain, Nsrate, Ntemp) 

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Material |  Material number |  None  
Ftype |  Function type = 2 linear interpolation of data using ![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_16.jpg' | relative_url }}) = 3 linear interpolation of data using  
![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_17.jpg' | relative_url }}) |  None  
Nstrain |  Number of strain sampling points |  None  
Nsrate |  Number of strain rate sampling points |  None  
Ntemp |  Number of temperature sampling points |  None  
Strain(i) |  Strain at ith sampling point |  None  
Srate(j) |  Strain rate at jth sampling point |  None  
Temp(k) |  Temperature at kth sampling point |  None  
Stress(i, j, k) |  Flow stress at ith, jth, kth sampling point (((Stress(i, j, k), i = 1, Nstrain), j = 1, Nsrate), k = 1, Ntemp) |  None  
  
REMARKS  
---  
Flow stress data that is in the form of sampled points can be entered with Ftype =2 or Ftype = 3. The data should contain strain, strain rate, and temperature data for each sampling point. | ![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_18.jpg' | relative_url }}) |   
---|---  
  
If Ftype = 2, the flow stress is linearly interpolated and extrapolated using

![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_16.jpg' | relative_url }}) |   
---|---  
  
If Ftype = 3 the flow stress is linearly interpolated and extrapolated using

![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_17.jpg' | relative_url }}) |   
---|---  
  
Applicable simulation types: Isothermal Deformation, Non-Isothermal Deformation  
  
EXAMPLES  
---  
Suppose the flow stress of material 3 had been measured at the strains, strain rates, and temperatures listed in Tables A.1 and A.2. The FSTRES keyword representation for ln-ln interpolation would be FSTRES 3, 2 3, 4, 2 0.05, 0.30, 0.60 0.10, 1.0, 5.0, 10.0 1800.0, 2000.0 8.3355, 9.9711, 10.6868 14.8227, 17.7313, 19.004 22.1651, 26.5146, 28.4176 26.3589, 31.5313, 33.7944 6.2516, 7.4783 8.0151 11.117, 13.2985, 14.253 16.6238, 19.886, 21.3132 19.7692, 23.6485, 25.3458 Table A.1 Flow stress of material 3 at T = 1800° F |  Strain ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) |  0.05  |  0.30 |  0.60  
---|---|---|---  
Strain rate![]({{ '/assets/icons/pre_icons/arrow_down.jpg' | relative_url }})  
0.10 |  8.34 |  9.97 |  10.67  
1.00 |  14.83 |  17.73 |  19.00  
  
Table A.2 Flow stress of material 3 at T = 2000° F

Strain ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) |  0.05 |  0.3 |  0.6  
---|---|---|---  
Strain Rate![]({{ '/assets/icons/pre_icons/arrow_down.jpg' | relative_url }})  
0.10 |  6.25 |  7.48 |  8.02  
1.00 |  11.12 |  13.30 |  14.25  
5.00 |  16.62 |  19.89 |  21.31  
10.00 |  19.77 |  23.65 |  25.35  
  
Temp. & Strain-rate dependent I (Type=4) ![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_3.jpg' | relative_url }})

* * *

FSTRES Material, Ftype

α, ΔH, A, n, R

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Material |  Material number |  None  
Ftype |  Function type = **4** ![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_3.jpg' | relative_url }}) |  None  
α |  Material constant |  None  
ΔH |  Activation energy |  None  
A |  Material constant |  None  
n |  Strain rate sensitivity index |  None  
R |  Gas constant 8.3144E+03 (N-mm/g-mole/K) Or 1.986 (Btu/lbf-mole/R) |   
  
REMARKS  
---  
The FSTRES function for Ftype =4 is | ![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_19.jpg' | relative_url }}) |   
---|---  
  
This flow stress function is used primarily for aluminum alloys.  
  
Temp. & Strain-rate dependent II (Type=5) ![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_4.jpg' | relative_url }})

* * *

FSTRES Material, Ftype

Δ H, A, n, R

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Material |  Material number |  None  
Ftype |  Function type = 5 ![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_4.jpg' | relative_url }}) |  None  
ΔH |  Activation energy |  None  
A |  Material constant |  None  
n |  Strain rate sensitivity index |  None  
R |  Gas constant **8.3144E+03** (N*mm/g-mole/K) or **1.986** (Btu/lbf-mole/R) |   
  
REMARKS  
---  
The FSTRES function for Ftype =5 is, | ![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_20.jpg' | relative_url }}) |   
---|---  
  
This flow stress function is used primarily for aluminum alloys.  
  
Y-H type (Type=6) ![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_5.jpg' | relative_url }})

* * *

FSTRES Material, Ftype(=6), Y_Ftype (=0), H_Ftype(=0)

Y_ConstValue

H_ConstValue

or

FSTRES Material, Ftype(=6), Y_Ftype (=1), H_Ftype(=2)

Ndata

Temp(1), Y_Value(1)

::

Temp(Ndata), Y_Value(Ndata)

Ndata

Atom(1), H_Value (1)

::

Atom(Ndata), H_Value(Ndata)

or

FSTRES Material, Ftype(=6), Y_Ftype (=3), H_Ftype(=3)

NTemp, NAtom

Temp(1), ..., Temp(NTemp)

Atom(1), ..., Atom(NAtom)

Y_Value(1, 1), ..., Y_Value(NTemp, 1)

: :

Y_Value(1, NAtom), ..., Y_Value(NTemp, NAtom)

NTemp, NAtom

Temp(1), ..., Temp(NTemp)

Atom(1), ..., Atom(NAtom)

H_Value(1, 1), ..., H_Value(NTemp, 1)

: :

H_Value(1, NAtom), ..., H_Value(NTemp, NAtom)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Material |  Material number |  None  
Ftype |  Function type = **6** ![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_5.jpg' | relative_url }}) |  None  
Y_Ftype |  Function type: 0 = Constant Y-value 1 = Temperature dependent Y-value 2 = Atom dependent Y-value 3 = Temperature and Atom dependent Y-value |  None  
H_Ftype |  Function type: 0 = Constant H-value 1 = Temperature dependent H-value 2 = Atom dependent H-value 3 = Temperature and Atom dependent H-value |  None  
Y_ConstValue |  Constant value for Y |  0.0  
H_ConstValue |  Constant value for H |  0.0  
Ndata |  Number of data |  0  
NTemp |  Number of temperature data |  0  
NAtom |  Number of atom data |  0  
Temp(i) |  Temperature of ith data |  0  
Atom(i) |  Atom of ith data |  0.0  
Y_Value(i,j) |  Y_Value function data |  0.0  
H_Value(i,j) |  H_Value function data |  0.0  
  
REMARKS  
---  
In above equations for FSTRES function Ftype =6 | ![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_21.jpg' | relative_url }}) |   
---|---  
  
This flow stress function is used primarily for heat treatment simulations.  
  
Table data (Type=7) : ![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_6.jpg' | relative_url }})log interpolation

Table data (Type=8) : ![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_6.jpg' | relative_url }})linear interpolation

* * *

FSTRES Material, Ftype

Nstrain, Natom, Ntemp

Strain(1)

:

Strain(Nstrain)

Satom(1)

:

Satom(Nsrate)

Temp(1)

:

Temp(Ntemp)

Stress(i,j,k)

:

Stress(Nstrain, Nsrate, Ntemp)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Material |  Material number |  None  
Ftype |  Function type = 7 log interpolation of strain = 8 linear interpolation of strain |  None  
Nstrain |  Number of strain sampling points |  None  
Natom |  Number of atom sampling points |  None  
Ntemp |  Number of temperature sampling points |  None  
Strain(i) |  Strain at ith sampling point |  None  
Satom(j) |  Strain rate at jth sampling point |  None  
Temp(k) |  Temperature at kth sampling point |  None  
Stress(i, j, k) |  Flow stress at ith, jth, kth sampling point (((Stress(i, j, k), i = 1, Nstrain), j = 1, Nsatom), k = 1, Ntemp) |  None  
  
Generalized Johnson & Cook (Type=9)![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_7.jpg' | relative_url }})

* * *

FSTRES Material, Ftype

A,B,X,Δ0, E, n, m,

Alpha, Beta, Eps0, Troom, Tmelt, Tb, k

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Material |  Material number |  None  
Ftype |  Flow stress type = 9 (Generalized Johnson & Cook, usually for machining) |  None  
A |  Material parameter |  0  
B |  Material parameter |  0  
X |  Material parameter |  0  
Δ0 |  Material parameter |  0  
E |  Material parameter |  0  
N |  Material parameter |  0  
M |  Material parameter |  0  
Alpha |  Material parameter |  0  
Beta |  Material parameter |  0  
K |  Material parameter |  0  
Tb |  Material parameter |  0  
Eps0 |  Reference strain rate |  0  
Troom |  Room temperature |  None  
Tmelt |  Melting temperature |  None  
  
REMARKS  
---  
In above equations for FSTRES function Ftype =9 | ![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_22.jpg' | relative_url }}) |   
---|---  
  
This flow stress function is used primarily for machining applications.  
  
Zerilli-Armstrong (Type=10) ![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_8.jpg' | relative_url }})

* * *

FSTRES Material, Ftype

a, c1, c3, c4, c5, n

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Material |  Material number |  None  
Ftype |  Flow stress type = **10** (Zerilli-Armstrong) |  None  
a, c1, c3, c4, c5, n |  Material parameters |   
  
REMARKS  
---  
In above equations for FSTRES function Ftype = 10: This flow stress function is used primarily for machining applications.  
  
Norton-Hoff (Type=11) ![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_9.jpg' | relative_url }})

* * *

FSTRES Material, Ftype

K0, m, n, eps0, beta

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Material |  Material number |  None  
Ftype |  Flow stress type = 11 (Norton-Hoff) |  None  
K0, m, n, eps0, beta |  Material parameters |  0  
  
DEFINITION  
---  
FSTRES specifies the flow stress for a particular material.  
  
REMARKS  
---  
In above equations for FSTRES function Ftype = 11: ![]({{ '/assets/equations/keyword_documentation/f/epsalon_bar_dot.jpg' | relative_url }}): strain rate ![]({{ '/assets/equations/keyword_documentation/f/epsalon_bar.jpg' | relative_url }}): strain Sij : flow stress component T : temperature  
  
Microstructure (Type=12) ![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_10.jpg' | relative_url }})

* * *

FSTRES Material, Ftype(=12), SFuncType(=0), GFuncType(=0)

ConstValue

or

FSTRES Material, Ftype(=12), SFuncType(=1), GFuncType(=0)

Ndata

Temp(1), IniStress(1)

::

Temp(Ndata), IniStress(Ndata)

or

FSTRES Material, Ftype(=12), SFuncType(=2), GFuncType(=0)

Ndata

Strate(1), IniStress(1)

::

Strate(Ndata), IniStress(Ndata)

or

FSTRES Material, Ftype(=12), SFuncType(=3), GFuncType(=0)

NTemp, NStrate

Temp(1), ..., Temp(NTemp)

Strate(1), ..., Strate(NStrate)

IniStress(1, 1), ..., IniStress(NTemp, 1)

: :

IniStress(1, NStrate), ..., IniStress(NTemp, NStrate)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Material |  Material number |  None  
Ftype |  Flow stress type |  None  
SFuncType |  Type of initial stress = **0** Constant =**1** function of temperature = **2** function of strain-rate = **3** function of temperature and strain-rate |   
GFuncType(=0) |  Type of shear modulus (Not used yet) |   
NTemp |  Number of temperature data |  0  
NStrate |  Number of strain-rate atom data |  0  
Temp(i) |  Temperature of ith data |  0  
Strate(i) |  Strain-rate of ith data |  0.0  
IniStress(i,j) |  Initial stress( ) |   
  
REMARKS  
---  
| ![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_23.jpg' | relative_url }}) |   
---|---  
  
General table data: Log interpolation (Type = 13)

General table data: Linear interpolation (Type=15)

* * *

FSTRES Material, Ftype(=13,15)

NVars

NdataX1, X1_ID1, X1_ID2

NdataX2, X2_ID1, X2_ID2

X1(1), ... ,X1(NdataX1)

X2(1), …, XN(NdataX2)

FS(1,1)

::

FS(NdataX1,1)

FS(1, NdataX2)

::

FS(NdataX1, NdataX2)

Note: Format given here is for 2D array. FS=(X1, X2) is saved in 1D array in DB

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Material |  Material number |  None  
Ftype |  Flow stress type  = **13** Linear interpolation = **15** Log interpolation |   
NVars |  Number of independent variables |   
NdataX1 |  Number of data for 1st variable |   
NdataX2 |  Number of data for 2nd variable |   
X1_ID1 |  1st ID of 1st variable |   
X1_ID2 |  2nd ID of 1st variable |   
X2_ID1 |  1st ID of 2nd variable |   
X2_ID2 |  2nd ID of 2nd variable |   
FS(i,j) |  Flow stress function data |   
  
Bird-Mukherjee-Dorn Equation (Type=14) ![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_11.jpg' | relative_url }})

* * *

FSTRES Material, Ftype(=14)

BMD_G, BMD_AD, BMD_b, BMD_p

FuncType(=0), BMD_n

or

FSTRES Material, Ftype(=14)

BMD_G, BMD_AD, BMD_b, BMD_p

FuncType(=6), Ndata

Strate(1), BMD_n(1)

::

Strate (Ndata), BMD_n(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Material |  Material number |  None  
Ftype |  Flow stress type |  None  
FuncType |  Date type of BMD_n = **0** Constant =**6** function of strain-rate |   
BMD_G |  Shear modulus |  0  
BMD_AD |  Grain boundary diffusivity |  0  
BMD_b |  Burgers vector |  0  
BMD_p |  Inverse grain size exponent |  0  
BMD_n |  Stress exponent |  0  
Ndata |  Number of temperature strain rate data pair |  0  
Strate(i) |  Strain-rate of ith data |  0.0  
BMD_n(i) |  Flow stress of ith data |  0.0  
  
REMARKS  
---  
This model specifies the flow stress model that uses Bird-Mukherjee-Dorn generalized constitutive relation. The high temperature deformation of crystalline materials is given by the fol-lowing (Bird–Mukherjee-Dorn) equation: | ![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_24.jpg' | relative_url }}) |   
---|---  
  
![]({{ '/assets/images/keyword_documentation/f/fstres_image001.jpg' | relative_url }})

Fig.1. AD vs 1/T plot for Ti64.1  
  
Table data (Type=16) - under development

* * *

FSTRES Material, Ftype(=16)

::

Not fully implemented Yet as of September 11, 2012

Flow stress function should be able to declare as 4-D…through GUI. 

Flow stress as a function of strain, strain-rate, orientation index in Rodrigues space, temperature.

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Material |  Material number |  None  
Ftype |  Flow stress type = **16** |   
  
REMARKS  
---  
Flow stress as a function of strain, strain-rate, orientation index in Rodrigues space, temperature.  
  
User Routine (Type=N)

* * *

FSTRES Material, Ftype

* * *

DEFINITION  
---  
FSTRES specifies the flow stress for a particular material.  
  
REMARKS  
---  
Flow stress data can be entered as one of 5 flow stress function types, or as a user subroutine. The FSTRES function for Ftype = -n is specified by the user in user subroutine n. The shell of the FORTRAN subroutine for defining flow stress is provided in the file DEF_USR.FOR located in the DEFORM system directory. For additional information about user flow stress subroutines refer to the "Installation" appendix.  
  
RELATED TOPICS  
---  
Material Data: Flow stress Keywords: STRESS, STRAIN  
  
Crystal plasticity model (Type=17)

* * *

FSTRES Material, Ftype(=17)

nHomogen, M, caHCP

ACTFL_1, ACTFL_2, …, ACTFL_M 

DFTYP_1, DFTYP_2, …, DFTYP_M 

nFuncTyp_LH, NT1

LH(1,1,1), LH(1,2,1), …, LH(1,M,1)

...

LH(M,1,1), LH(M,2,1), …, LH(M,M,1)

.

.

LH(1,1,NT1), LH(1,2,NT1), …, LH(1,M,NT1)

...

LH(M,1,NT1), LH(M,2,NT1), …, LH(M,M,NT1)

nFuncTyp_FR, NT2, NYF

T_FR(1), T_FR(2), …, T_FR(NT2)

FRP(1,1), FRP(2,1), …, FRP(NYF,1)

…

FRP(1,NT2), FRP(2,NT2), …, FRP(NYF,NT2)

nHRNo, nFuncTyp_HR, NT3, NYH

T_HR(1), T_HR(2), …, T_HR(NT3)

HRP(1,1,1), …, HRP(NYH,1,1) 

… 

HRP(1,M,1), …, HRP(NYH,M,1)

.

.

HRP(1,1, NT3), …, HRP(NYH,1, NT3) 

… 

HRP(1,M, NT3), …, HRP(NYH,M, NT3)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
nHomogen |  Homogenization scheme (0-Taylor 1-VPSC) |  1  
M |  The number of deformation modes  
(FCC: 1, BCC: 3, HCP: 3. Twinning mode is not implemented yet)  |   
caHCP |  The c/a ratio for HCP crystal |  1.0  
ACTFL_i |  The activation flag for ith deformation mode  
(0: Not activated 1-Activated) |  1  
DFTYP_i |  The deformation type for ith deformation mode  
(0: Bidirectional slip 1-Single direction slip) |  0  
nFuncTyp_LH |  Latent hardening matrix function type  
(0: constants 1-f(Temp.)) |  0  
NT1 |  The number of temperatures for latent hardening function |  0  
T_LH(i) |  The ith temperature for latent hardening function |  0  
LH(k,j,i) |  The latent hardening coefficient contributed from jth deformation mode to kth deformation mode at the ith temperature |  1.0  
nFuncTyp_FR |  Flow rule function type (0: constants 1-f(Temp.)) |  0  
NT2 |  The number of temperatures for flow rule function |  0  
NYF |  The number of parameters in flow rule |  2  
T_FR(i) |  The ith temperature for flow rule function |  0  
FRP(j,i) |  The jth parameter in the flow rule at the ith temperature |   
nHRNo |  The Hardening rule number |  1  
nFuncTyp_HR |  Hardening rule function type (0: constants 1-f(Temp.)) |  0  
NT3 |  The number of temperatures for hardening rule function |  0  
NYH |  The number of parameters in hardening rule |  5  
T_HR(i) |  The ith temperature for hardening rule function |  0  
HRP(k,j,i) |  The kth parameter for jth deformation mode at the ith temperature in the hardening rule |   
  
REMARKS  
---  
(1) Deformation modes and deformation systems The deformation systems are divided into different deformation modes. The number of deformation modes is M.  |  Crystal type |  M |  Deformation systems  
---|---|---  
FCC  |  1 |  12 x {111}<110>  
BCC  |  3 |  12 x {110}<111>, 12 x {112}<111>, 24 x {123}<111>  
HCP  |  3 |  3 x {0001}<11-20>, 3 x {10-10}<11-20>, 6 x {10-11}<11-20>+12 x {10-11}<11-23>)  
  
twinning deformation mode is not implemented yet.

Latent hardening matrix (M X M) is defined between the deformation modes.  
  
(2) The flow rule is described by

![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_25.jpg' | relative_url }}) |   
---|---  
  
(3) Hardening rule 1 is described by

![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_26.jpg' | relative_url }}) |   
---|---  
  
(4) Hardening rule 2 is described by

![]({{ '/assets/equations/keyword_documentation/f/fstres_eq_27.jpg' | relative_url }}) |   
---|---  
  
(5) The data formats for constant parameters

If NT1=0 (Constants for latent hardening matrix), the latent hardening matrix uses the following format:

0, 0

LHC(1,1), LHC(1,2), …, LHC(1,M)

...

LHC(M,1), LHC(M,2), …, LHC(M,M)

Where LHC(k,j) represents the latent hardening coefficient contributed from jth deformation mode to kth deformation mode

If NT2=0 (Constants for flow rule parameters), the flow rule uses the following format:

0, 0, NYF

FRPC(1), FRPC(2), …, FRPC(NYF)

where FRPC(j ) represents the jth parameter in the flow rule.

If NT3=0 (Constants for hardening rule parameters), the hardening rule uses following format:

nHRNo, 0, 0, NYH

HRPC(1,1), …, HRPC(NYH,1) 

… 

HRPC(1,M), …, HRPC(NYH,M)

where HRPC(k,j) represents the kth parameter for the jth deformation mode

EXAMPLES  
---  
_Example 1: All parameters are constants_ FSTRES 2 17 1 3 1.0000000000E+000 1 1 1 0 0 0 0 0 1.0000000E+000 1.0000000E+000 1.0000000E+000 1.0000000E+000 1.0000000E+000 1.0000000E+000 1.0000000E+000 1.0000000E+000 1.0000000E+000 0 0 2 1.0000000E-003 1.0000000E-001 1 0 0 4 7.0000000E+001 1.0000000E+001 2.0000000E+002 1.0000000E+000 7.0000000E+001 1.0000000E+001 2.0000000E+002 1.0000000E+000 7.0000000E+001 1.0000000E+001 2.0000000E+002 1.0000000E+000  
  
_Example 2: All parameters are functions of temperature_

FSTRES 3 17

1 3 1.0000000000E+000

1 1 1

0 0 0

1 2

9.0000000E+002 1.0000000E+003

1.0000000E+000 1.4000000E+000 1.5000000E+000

1.4200000E+000 1.0000000E+000 1.6000000E+000

1.5500000E+000 1.7000000E+000 1.0000000E+000

1.0000000E+000 1.0000000E+000 1.0000000E+000

1.0000000E+000 1.0000000E+000 1.0000000E+000

1.0000000E+000 1.0000000E+000 1.0000000E+000

1 2 2

9.0000000E+002 1.0000000E+003

1.0000000E-003 1.0000000E-001

1.5000000E-003 1.2500000E-001

1 1 2 4

8.5000000E+002 1.0500000E+003

1.5000000E+002 1.0000000E+001 4.4000000E+002 1.0000000E+000

1.5000000E+002 1.0000000E+001 4.4000000E+002 1.0000000E+000

4.5000000E+002 1.0000000E+001 4.4000000E+002 1.0000000E+000

1.0000000E+002 8.0000000E+000 3.3000000E+002 1.0000000E+000

1.0000000E+002 8.0000000E+000 3.3000000E+002 1.0000000E+000

3.0000000E+002 3.0000000E+000 3.3000000E+002 1.0000000E+000

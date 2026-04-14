---
lang: sk
title: "GRNDAT (2D3D)"
---

# GRNDAT

|  (Material data)  
---|---  
_Update History:_ (New) Definition has been extended in v11 |  Last updated on : 07-08-2013  
  
* * *

GRNDAT Material, Model

(please see the each model description for the detail data format)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Material |  Material Number |  None  
Model |  Model Number = **0** None = **1** Avrami model =**2** Mesoscale model(New in v11) = **3** (Not used) = **4** Coarsening model (Not available, it moved to COARSE) = ******5** Texture controlled model (Beta Growth model) (New in v11) = **N** User routine no. N (not implemented in GUI) |  0  
  
DEFINITION  
---  
GRNDAT (Model=1) specifies the grain evolution data, including static, meta-dynamic, dynamic recrystallization and grain growth for a material. GRNDAT (Model=2) specifies the Mesoscale model. For a given initial nodal microstructural parameters and defined recrystallization kinetics, evolving parameters such as grain size, number of grains, dislocatin density and resulting instantaneous flow stress cab ne computed. GRNDAT (Model=5) specifies the Beta grain growth model. (Description please…)  
  
REMARKS  
---  
(Avrami model) The grain size evolution models are specified as following. Static Recrystallization Model Activation Criteria: When strain rate is less than, static recrystallization occurs after deformation. | ![]({{ '/assets/equations/keyword_documentation/g/grndat_eq_1.jpg' | relative_url }}) |   
---|---  
  
Kinetics:

The model for recrystallization kinetics is based on the modified Avrami equation.

![]({{ '/assets/equations/keyword_documentation/g/grndat_eq_2.jpg' | relative_url }}) |   
---|---  
  
where ![]({{ '/assets/equations/keyword_documentation/g/t_0_5.jpg' | relative_url }}) is an empirical time constant for 50% recrystallization:

![]({{ '/assets/equations/keyword_documentation/g/grndat_eq_3.jpg' | relative_url }}) |   
---|---  
  
Grain Size:

The recrystallized grain size is expressed as a function of initial grain size, strain, strain rate, and temperature,

![]({{ '/assets/equations/keyword_documentation/g/grndat_eq_4.jpg' | relative_url }}) |   
---|---  
  
Meta-dynamic Recrystallization Model

Activation Criteria:

When strain rate is greater than (see equation (1)), meta-dynamic recrystallization occurs after deformation.

Kinetics:

The model for recrystallization kinetics is based on the modified Avrami equation.

![]({{ '/assets/equations/keyword_documentation/g/grndat_eq_5.jpg' | relative_url }}) |   
---|---  
  
where ![]({{ '/assets/equations/keyword_documentation/g/t_0_5.jpg' | relative_url }}) is an empirical time constant for 50% recrystallization:

![]({{ '/assets/equations/keyword_documentation/g/grndat_eq_6.jpg' | relative_url }}) |   
---|---  
  
Grain Size:

The recrystallized grain size is expressed as a function of initial grain size, strain, strain rate, and temperature,

![]({{ '/assets/equations/keyword_documentation/g/grndat_eq_7.jpg' | relative_url }}) |   
---|---  
  
Dynamic Recrystallization Model

Activation Criteria:

The onset of DRX usually occurs at a critical stain ![]({{ '/assets/equations/keyword_documentation/g/epsalon_c.jpg' | relative_url }}).

![]({{ '/assets/equations/keyword_documentation/g/grndat_eq_8.jpg' | relative_url }}) |   
---|---  
  
where ![]({{ '/assets/equations/keyword_documentation/g/epsalon_p.jpg' | relative_url }}) denotes the peak stain corresponding to the flow stress maximum:

![]({{ '/assets/equations/keyword_documentation/g/grndat_eq_9.jpg' | relative_url }}) |   
---|---  
  
Kinetics:

The Avrami equation is used to describe the relation between the dynamically recrystallized fraction X and the effective strain.

![]({{ '/assets/equations/keyword_documentation/g/grndat_eq_10.jpg' | relative_url }}) |   
---|---  
  
where ![]({{ '/assets/equations/keyword_documentation/g/epsalon_0_5.jpg' | relative_url }}) denotes the strain for 50% recrystallization:

![]({{ '/assets/equations/keyword_documentation/g/grndat_eq_11.jpg' | relative_url }}) |   
---|---  
  
Grain Size:

The recrystallized grain size is expressed as a function of initial grain size, strain, strain rate, and temperature,

![]({{ '/assets/equations/keyword_documentation/g/grndat_eq_12.jpg' | relative_url }}) |   
---|---  
  
Grain Growth

Following complete recrystallization, the microstructure can be coarsen by crystal growth with kinetics of,

![]({{ '/assets/equations/keyword_documentation/g/grndat_eq_13.jpg' | relative_url }}) |   
---|---  
  
Retained Strain and Grain Size

When there are multiple deformation processes, strain may be reduced during the inter pass period due to recovery, the following equation is used to compute the retained strain at the beginning of the subsequent deformation.

![]({{ '/assets/equations/keyword_documentation/g/grndat_eq_14.jpg' | relative_url }}) |   
---|---  
  
The mixture law was employed to calculate the recrystallized grain size for uncompleted recrystallization,

![]({{ '/assets/equations/keyword_documentation/g/grndat_eq_15.jpg' | relative_url }}) |   
---|---  
  
In addition, if at the beginning of deformation total Xrex is 1.0, the program will reinitialize (e.g. Xrex = 0) in order to compute a new round of recrystallization.

NOMENCLATURE  
  
![]({{ '/assets/equations/keyword_documentation/g/grndat_eq_16.jpg' | relative_url }})

RELATED TOPICS  
---  
Keywords: [GRAIN](/docs/sk/keyword_documentation/g/grain/)  
  
(Model = 1, Avrami model)

* * *

GRNDAT Material, Model

SRB_Flg, NP1

PS_Flg, NP2

SRK_Flg(1), NP3

SRGS_Flg(1), NP4

MRK_Flg, NP5

MRGS_Flg, NP6

DRK_Flg, NP7

DRGS_Flg, NP8

GG_Flg, NP9

SRB_Var(1) A(1), b1(1), b2(1), Q2(1)

… …

SRB_Var(NP1) A(NP1), b1(NP1), b2(NP1), Q2(NP1)

PS_Var(1) a1(1), n1(1), m1(1), Q1(1), c1(1), a2(1)

… …

PS_Var(NP2) a1(NP2), n1(NP2), m1(NP2), Q1(NP2), c1(NP2), a2(NP2)

SRK_Var(1) a3(1), h3(1), n3(1), m3(1), Q3(1), s(1), ks(1)

… …

SRK_Var(NP3) a3(NP3), h3(NP3), n3(NP3), m3(NP3), Q3(NP3), s(NP3), ks(NP3)

SRGS_Var(1) a6(1), h6(1), n6(1), m6(1), Q6(1), c6(1)

… …

SRGS_Var(NP4) a6(NP4), h6(NP4), n6(NP4), m6(NP4), Q6(NP4), c6(NP4)

MRK_Var(1) a4(1), h4(1), n4(1), m4(1), Q4(1,) md(1), kmd(1)

… …

MRK_Var(NP5) a3(NP5), h3(NP5), n3(NP5), m3(NP5), Q3(NP5), md(NP5), kmd(NP5)

MRGS_Var(1) a7(1), h7(1), n7(1), m7(1), Q7(1), c7(1)

… …

MRGS_Var(NP6) a7(NP6), h7(NP6), n7(NP6), m7(NP6), Q7(NP6), c7(NP6)

DRK_Var(1) a5(1), h5(1), n5(1), m5(1), Q5(1), c5(1,) d(1), kd(1), a10(1)

… …

DRK_Var(NP7) a5(NP7), h5(NP7), n5(NP7), m5(NP7), Q5(NP7), c5(NP7), d(NP7), kd(NP7), a10(NP7)

DRGS_Var(1) a8(1), h8(1), n8(1), m8(1), Q8(1), c8(1)

… …

DRGS_Var(NP8) a8(NP8), h8(NP8), n8(NP8), m8(NP8), Q8(NP8), c8(NP8)

GG_Var(1) m(1), a9(1), Q9(1)

…

GG_Var(NP9) m(NP9), a9(NP9), Q9(NP9)

![]({{ '/assets/equations/keyword_documentation/g/lamda.jpg' | relative_url }}), TempNR

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
SRB_Flg |  Flag for Strain Rate Boundary between static and meta-dynamic  = **1** , Computed with equation (1), material data functions of temperature = **2** , Computed with equation (1), material data functions of strain rate |   
SRB_Var(i) |  Temperature or strain rate of the ith sampling point for |   
PS_Flg |  Flag for Peak Strain ep and Critical Strain ec = **1** , Computed with equation (12-13), material data functions of temperature = **2** , Computed with equation (12-13), material data functions of strain rate |   
PS_Var(i) |  Temperature or strain rate of the ith sampling point for Peak Strain ep and Critical Strain ec |   
SRK_Flg |  Flag for Static Recrystallization Kinetics = **1** , Computed with equation (2-4), material data functions of temperature = **2** , Computed with equation (2-4), material data functions of strain rate |   
SRK_Var(i) |  Temperature or strain rate of the ith sampling point for Static Recrystallization Kinetics |   
SRGS_Flg |  Flag for Static Recrystallized Grain Size = **1** , Computed with equation (5-6), material data functions of temperature = **2** , Computed with equation (5-6), material data functions of strain rate |   
SRGS_Var(i) |  Temperature or strain rate of the ith sampling point for Statically Recrystallized Grain Size |   
MRK_Flg |  Flag Meta-dynamic Recrystallization Kinetics = **1** , Computed with equation (7-9), material data functions of temperature = **2** , Computed with equation (7-9), material data functions of strain rate |   
MRK_Var(i) |  Temperature or strain rate of the ith sampling point for Meta-dynamic Recrystallization Kinetics |   
MRGS_Flg |  Flag for Meta-dynamic Recrystallized Grain Size = **1** , Computed with equation (10-11), material data functions of temperature = **2** , Computed with equation (10-11), material data functions of strain rate |   
MRGS_Var(i) |  Temperature or strain rate of the ith sampling point for Meta-dynamically Recrystallized Grain Size |   
DRK_Flg |  Flag Dynamic Recrystallization Kinetics = **1** , Computed with equation (15-17), material data functions of temperature = **2** , Computed with equation (15-17), material data functions of strain rate |   
DRK_Var(i) |  Temperature or strain rate of the ith sampling point for Dynamic Recrystallization Kinetics |   
DRGS_Flg |  Flag for Dynamic Recrystallized Grain Size = **1** , Computed with equation (18-19), material data functions of temperature = **2** , Computed with equation (18-19), material data functions of strain rate |   
DRGS_Var(i) |  Temperature or strain rate of the ith sampling point for Dynamically Recrystallized Grain Size |   
GG_Flg |  Flag for Grain Growth = **1** , Computed with equation (20), material data functions of temperature = **2** , Computed with equation (20), material data functions of strain rate |   
GG_Var(i) |  Temperature or strain rate of the ith sampling point for Grain Growth |   
TempNR |  Recrystallization stop temperature |   
NP1 – 9 |  Number of sampling points for corresponding material data set |   
a1 – 10(i) |  Material data |   
b1 – 2(i) |  Material data |   
c1 – 8(i) |  Material data |   
n1 – 8(i) |  Material data |   
m1 – 8(i) |  Material data |   
Q1 – 8(i) |  Material data |   
bd(i), bmd(i), bs(i) |  Material data |   
kd(i), kmd(i), ks(i) |  Material data |   
l |  Inter-pass strain lost coefficient |   
TempNR |  Cut-off temperature (below which grain model is not computed) |   
  
(Model=2, Mesoscale model)

* * *

GRNDAT Material, Model, PhaseType

(Initial grain MSUs)

(Static Recrystallization MSUs)

(Meta-dyanmic Recrystallization MSUs)

(Dynamic Recrystallization MSUs)

(PSN Recrystallization MSUs)

(Number of User Defined MSUs)

(Initial grain MSUs)

SubBdryVarSize

InitMSU(1), ... , InitMSU(VarSize)

SimPhaseNo, TempLimit

(Nucleation volume: NucVol)

(FuncType=0, Constant value)

FuncType, ConstValue

(FuncType=1, function of temperature)

FuncType, Ndata1

Temp(1), ..., NucVol (1)

::

Temp(Ndata1), ..., NucVol(Ndata1)

(FuncTyp=2, function of angle)

FuncType, Ndata1

Angle(1), ..., NucVol (1)

::

Angle(Ndata1), ..., NucVol(Ndata1)

(FuncType=3, function of temperatur and angle)

FuncType, Ndata1, Ndata2

Temp(1), ..., Temp(Ndata1)

Angle(1), ..., Angle(Ndata2)

NucVol(1, 1), ..., NucVol(Ndata1, 1)

: :

NucVol(1, Ndata2), ..., NucVol(Ndata1, Ndata2)

(Nucleation rate: NucRate)

~ same as above

(Growth rate: Growth)

~ same as above

(Static Recrystallization MSUs)

NoSRXs

SubBdryVarSize

SRXData(1), ... , SRXData(VarSize)

SimPhaseNo, TempLimit

(Nucleation volume: NucVol)

(FuncType=0, Constant value)

FuncType, ConstValue

(FuncType=1, function of temperature)

FuncType, Ndata1

Temp(1), ..., NucVol (1)

::

Temp(Ndata1), ..., NucVol(Ndata1)

(FuncTyp=2, function of angle)

FuncType, Ndata1

Angle(1), ..., NucVol (1)

::

Angle(Ndata1), ..., NucVol(Ndata1)

(FuncType=3, function of temperatur and angle)

FuncType, Ndata1, Ndata2

Temp(1), ..., Temp(Ndata1)

Angle(1), ..., Angle(Ndata2)

NucVol(1, 1), ..., NucVol(Ndata1, 1)

: :

NucVol(1, Ndata2), ..., NucVol(Ndata1, Ndata2)

(Nucleation rate: NucRate)

~ same as above

(Growth rate: Growth)

~ same as above

Note: The same data format is repeated for the remaining data groups.

(Meta-dyanmic Recrystallization MSUs) NoMRXs, MRXData

(Dynamic Recrystallization MSUs) NoDRXs, DRXData

(PSN Recrystallization MSUs) NoPSNs, PSNData

(Number of User Defined MSUs) NoUSR, UserData

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
PhaseType |  Grain boundary energy between matrix grains = **0** Ductile matrix = **1** Hard precipitate |  0 0  
InitMSU |  Initial Grain MSU |  0  
NoSRXs |  Number of Static Recrystallization MSUs |   
SRXData |  Parametsrs of Static Recrystallization MSUs |   
NoMRXs |  Number of Meta-dyanmic Recrystallization MSUs |   
MRXData |  Parametsrs of Meta-dyanmic Recrystallization MSUs |   
NoDRXs |  Number of Dynamic Recrystallization MSUs |   
DRXData |  Parametsrs of Dynamic Recrystallization MSUs |   
NoPSNs |  Number of PSN Recrystallization MSUs |   
PSNData |  Parametsrs of PSN Recrystallization MSUs |   
NoUSRs |  Number of User Defined MSUs |   
UserData |  Parametsrs of User Defined MSUs |   
NucVolFlag |  Nucleation volume (not for initial MSU) =**0** Constant = **1** Function of temperature =**2** Function of misorientation angle =**3** Function of temperature and misorientation angle |   
NucRateFlag |  Nucleation rate (not for initial MSU) = **0** Constant = **1** Function of temperature = **2** Function of misorientation angle = **3** Function of temperature and misorientation angle |   
GrowthFlag |  Grain growth rate =**0** Constant = **1** Function of temperature = **2** Function of misorientation angle = **3** Function of temperature and misorientation angle |   
  
(Model=4, Coarsening model) => Moved to “COARSE“ keyword“

* * *

GRNDAT Material, Model(=4)

FuncType, NTemp, NStrate

Temp(1), ..., Temp(NTemp)

Strate(1), ..., Strate(NStrate)

K-Coeff(1, 1), ..., K-Coeff (NTemp, 1)

: :

K-Coeff (1, NStrate), ..., K-Coeff (NTemp, NStrate)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
FuncType |  Coarsening function type = **0** Constant = **5** Function of temperature and strain-rate |  0  
NTemp |  Number of temperature data |  0  
NStrate |  Number of strain-rate data |  0  
Temp(i) |  Temperature of ith data |   
Strate(i) |  Strain-rate of ith data |   
K_Coeff(i,j) |  K coefficient function data |  0  
  
(Model=5, Texture controlled model)

* * *

GRNDAT Material, Model(=5)

BetaGamma, BetaKappa, BetaK, BetaA, BetaQ, BetaAngle

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
BetaGamma |  Grain boundary energy between matrix grains |  0  
BetaKappa |  Kappa constant |  0  
BetaK |  K constant |  0  
BetaA  |  A |  0  
BetaQ |  Q |  0  
BetaAngle |  Angle between texture grain |  0

---
lang: en
title: "GRAIN (2D3D)"
---

# GRAIN

|  (Object data)  
---|---  
|  Last updated on : 07-08-2013  
  
* * *

GRAIN Object, Nelm, Nvar, Default

Element(1), Pre_StrnR (1), Xrex(1), Avg_GS(1), Init_GS(1), RtnStrn(1), Dm_Time(1),

Dm_StrnR(1), Dm_Temp(1), Pk_Strn(1), Elv_Md(1), Xrex_D(1), Xrex_M(1), Xrex_S(1),

Rex_GS_D(1), Rex_GS_M(1), Rex_GS_S(1)

:::

Element(Nelm), Pre_StrnR(Nelm), Xrex(Nelm), Avg_GS(Nelm), Init_GS(Nelm), RtnStrn(Nelm), Dm_Time(Nelm), Dm_StrnR(Nelm), Dm_Temp(Nelm), Pk_Strn(Nelm), Elv_Md (Nelm),Xrex_D(Nelm), Xrex_M(Nelm), Xrex_S(Nelm), Rex_GS_D(Nelm), Rex_GS_M(Nelm),Rex_GS_S(Nelm)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
Nelm |  Number of elements |  None  
Default |  Default value |  0  
Nvar |  Number of grain-related variables (16 currently) |  None  
NOTE: (i) stands for the ith element below  
Element(i) |  Element number |   
Pre_StrnR(i) |  Previous strain rate (used for determining deformation status) |   
Xrex(i) |  Percentage of recrystallization |   
Avg_GS(i) |  Average grain size |   
Avg_GS(i) |  Average grain size |   
Init_GS(i) |  Initial grain size |   
RtnStrn(i) |  Retained Strain |   
Dm_Time(i) |  Time span of deformation |   
Dm_StrnR(i) |  Average strain rate over deformation period |   
Dm_Temp(i) |  Average temperature over deformation period |   
Pk_Strn(i) |  Peak strain |   
ElvMd(i) |  Grain evolution mode for the ith element =**0** None = **1** Static recrystallization = **2** Meta-dynamic recrystallization = **3** Dynamic recrystallization = **4** Grain growth |   
Xrex_D(i) |  Dynamic recrystallization percentage |   
Xrex_M(i) |  Meta-dynamic recrystallization percentage |   
Xrex_S(i) |  Static recrystallization percentage |   
Rex_GS_D(i) |  Grain size of dynamically recrystallized grains |   
Rex_GS_M(i) |  Grain size of meta-dynamically recrystallized grains |   
Rex_GS_S(i) |  Grain size of statically recrystallized grains |   
  
DEFINITION  
---  
GRAIN provides storage space for calculation results of the grain size models for each element.  
  
REMARKS  
---  
The number of variable can be redefined such that the storage space can be easily expanded or reduced. These variables are tracked through out the simulation and are kept through remeshing.  
  
RELATED TOPICS  
---  
Keywords: [GRNDAT](/docs/en/keyword_documentation/g/grndat/)

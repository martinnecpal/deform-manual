---
lang: en
title: "TIMEID (2D3D)"
---

# TIMEID

|  (Simulation control)  
---|---  
_Update History:_ V11 - TIMEID has been introduced. |  Last updated on : 24-07-2013  
  
* * *

TIMEID NumTime, NumCtrlPara

Time_Id(1), CtrlPara(1,1), … , CtrlPara(NumCtrlPara,1)

: :

Time_Id(NumTime), CtrlPara(1,NumTime), … , CtrlPara(NumCtrlPara,NumTime)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
NumTime |  Total number of Times |  1  
NumCtrlPara |  Total number of control parameters |  0  
Time_Id (i) |  Time Id. = **1** Diffusion bonding time = **2** Time between two temperatures (under development) |  None  
CtrlPara(i,j) |  Control parameter |  0  
  
DEFINITION  
---  
TIMEID specifies how to accumulate time.  
  
REMARKS  
---  
When Time_Id(i) = 1 (for diffusion bonding time), control parameters are not necessary. Thus, CtrlPara(i,j) = 0.0  
  
RELATED TOPICS  
---  
[Simulation Controls](/docs/en/pre_processor/9_simulation_controls/9_simulation_controls/) Keywords: [TIMERC](/docs/en/keyword_documentation/t/timerc/), [DIFBND](/docs/en/keyword_documentation/d/difbnd/)

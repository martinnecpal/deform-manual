---
lang: en
title: "TNOW (2D3D)"
---

# TNOW

|  (Simulation control)  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

TNOW GlobalTime LocalTime FuncTmMd 2ndStgTime

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
GlobalTime  |  Current global time |  0.0  
LocalTime  |  Local time |  0.0  
FuncTmMd  |  Function time method  = **0** Use global time for function = **1** Use local time for function |   
2ndStgTime  |  The second-stage time  |  0.0  
  
DEFINITION  
---  
TNOW specifies the current simulation process time. (2ndStgTime is used for timing the second stage of a simulation, if the simulation contains two stages. For example, in hydraulic forming, a dwell may follow the forming. Thus the clock of the second global time starts when the dwell starts. This is a sort of like multiple operations but in one simulation.)  
  
REMARKS  
---  
For initial runs GlobalTime = 0. For continuing and remeshing runs, GlobalTime indicates the current process time at the specified step number. If GlobalTime, LocalTime or 2ndStgTime is less than -1E20, the input value will be ignored. This is to facilitate updating one of them without changing the other (useful in multiple operations). Applicable simulation types: Isothermal Deformation, Heat Transfer, Non-Isothermal Deformation  
  
RELATED TOPICS  
---  
Keywords: [TMAX](/docs/en/keyword_documentation/t/tmax/), [TLOC](/docs/en/keyword_documentation/t/tloc/), [CURSIM](/docs/en/keyword_documentation/c/cursim/)

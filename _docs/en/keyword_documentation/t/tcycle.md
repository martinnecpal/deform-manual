---
lang: en
title: "TCYCLE (2D3D)"
---

# TCYCLE

|  (Material data)  
---|---  
_Update History:_ V11.1 - TCYCLE has been introduced. |  Last updated on : 21-06-2016  
  
* * *

TCYCLE NumSteps, NumBitesToSkip, CycleTime, DecompTime, DwellTime

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
NumSteps |  Number of simulation steps |  0  
NumBitesToSkip |  Number of cycles to skip |  0  
CycleTime |  Cycle time of the crank press |  0.0  
DecompTime |  Time for decompression (hydraulic press) |  0.0  
DwellTime |  Time for dwell |  0.0  
  
DEFINITION  
---  
TCYCLE calculates remaining cycle time for a crank press and assigns that value to [DTMAX](/docs/en/keyword_documentation/d/dtmax/)  
  
REMARKS  
---  
TCYCLE is an action keyword and is mainly for internal use. It is used in the [cogging](/docs/en/operation_templates/29_cogging/29_introduction_to_cogging/) template to automatically calculate heat transfer time (cycle time left after bite deformation time).

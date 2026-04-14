---
lang: en
title: "ACVCOF (2D3D)"
---

# ACVCOF

|  (Simulation Control)  
---|---  
|  Last updated on : 29-07-2013  
  
* * *

ACVCOF Type, value or (N1)  
Temp(1) ACVCOF(1)  
Temp(Ndata) ACVCOF(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Type |  Defines the function type =**0** Constant atom content =**1** Function of temperature =**2** Function of atom content =**3** Function of time |  None  
Value |  Surface reaction coefficient value |  None  
N1 | Number of data pairs |  None  
  
DEFINITION  
---  
ACVCOF sets the surface reaction coefficient. It is defined at the surface as, | ![]({{ '/assets/equations/keyword_documentation/a/acvcof_eq_1.jpg' | relative_url }}) |   
---|---  
  
  
SYSTEM UNITS: (mm/s) or (in/s)  
  
**EXAMPLE**  
---  
A simple example where k (ACVCOF) is a function of surface temperature for material 1. |  Temperature |  Reaction Rate  
---|---  
400 |  0.1  
500 |  0.2  
600 |  0.3  
  
ACVCOF 1 3

400 0.1

500 0.2

600 0.3  
  
RELATED TOPICS  
---  
Applicable Simulation Modules: Microstructure Applicable Simulation Modes: [Diffusion](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#9.1.5._Simulation_modes_\(SMODE,_TRANS\))

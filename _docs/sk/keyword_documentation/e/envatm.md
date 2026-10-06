---
lang: sk
title: "ENVATM (2D3D)"
---

# ENVATM

|  (Simulation control)  
---|---  
|  Last updated on : 30-07-2013  
  
* * *

ENVATM Type, value (if constant)

t1,C1

tn, CN

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Type |  Environment atom content =**0** Constant =**1** Function of time |  None  
  
DEFINITION  
---  
ENVATM sets the environment atom content for the simulation. EXAMPLE The atom content can be a function of time or constant. Example of atom content as a constant … ENVATM 0 .11 Example of atom content as a function of time … |  TIME(s) |  ATOM %  
---|---  
1 |  0.1  
20 |  0.15  
100 |  0.25  
  
ENVATM 1

1 0.1

20 0.15

100 0.25  
  
REMARKS  
---  
Applicable Simulation Modules: Microstructure Applicable Simulation Modes: Diffusion  
  
RELATED TOPICS  
---  
[Simulation Controls]({{ '/docs/sk/pre_processor/9_simulation_controls/9_simulation_controls/' | relative_url }}): [Process condition]({{ '/docs/sk/pre_processor/9_simulation_controls/9_6_process_conditions/' | relative_url }}) \- Diffusion Keywords: [ACVCOF]({{ '/docs/sk/keyword_documentation/a/acvcof/' | relative_url }}), [ENVTMP]({{ '/docs/sk/keyword_documentation/e/envtmp/' | relative_url }}), [CNVCOF]({{ '/docs/sk/keyword_documentation/c/cnvcof/' | relative_url }})

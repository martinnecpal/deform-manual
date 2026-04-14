---
lang: en
title: "VOLFC (2D3D)"
---

# VOLFC

|  (Object data)  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

VOLFC Iobj, Numel, Nphase

1, f1, f2, f3, .. fnphase

Numel, f1n, f2n, f3n…fnphase

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Iobj |  Object number |  None  
Numel |  Number of element |  None  
Nphase |  Number of material |  None  
  
DEFINITION  
---  
VOLFC specifies initial volume fraction of a phase (material) in an element at the beginning of a simulation. In addition, throughout the simulation, VOLFC stores the volume fraction of all phases in each element per step. EXAMPLE VOLFC 1 585 3 1 0.99 0.01 0 2 0.99 0.01 0 3 0.90 0.10 0 : : : : 585 0.98 0.01 0.01  
  
REMARKS  
---  
The volume fraction is determined from the keyword TTTD, which specifies the model or data used in calculating the volume fraction of each phase. It is important that the user specifies the necessary input for the keyword TTTD or else the volume fraction (VOLF) will not be calculated for the object. The user must input the type of diffusion model and at least two Time-Temperature curves, the beginning of the transformation and the end of the transformation. Applicable Simulation Modules: Microstructure Applicable Simulation Modes: Transformation Applicable object types: ALL except Rigid  
  
RELATED TOPICS  
---  
[Inter-Material Data](/docs/en/pre_processor/10_material_data/10_9_transformation_data/10_9_transformation_data/) Keywords: [VOLFS](/docs/en/keyword_documentation/v/volfs/), VOLFN

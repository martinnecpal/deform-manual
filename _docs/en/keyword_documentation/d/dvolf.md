---
lang: en
title: "DVOLF (2D3D)"
---

# DVOLF

|  (Object data)  
---|---  
|  Last updated on : 30-07-2013  
  
* * *

DVOLF Iobj, Numel, Nphase

1 f1, f2, f3, ...fn

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Iobj |  Object number |  None  
Numel |  Number of Element |  None  
Nphase |  Number of Materials |  None  
  
DEFINITION  
---  
DVOLF specifies the change in volume fraction of all the different phases that resulted from the transformation during each time step. DVOLF of each phase is initially set to zero in a simulation.  
  
REMARKS  
---  
DVOLF is determined by fcurrent - fprevious for each step where f is the volume fraction of a particular phase. DVOLF is used in calculating the latent heat due to transformation and the change in volume of the object. DVOLF can be invaluable in determining the progress of a transformation and aid the user in deciding whether to increase or decrease the time step for a particular transformation. Applicable Simulation Modules: Microstructure Applicable Simulation Modes: Transformation Applicable Object Types: ALL except rigid  
  
RELATED TOPICS  
---  
[Object Element data](/docs/en/pre_processor/17_object_data_initialization/17_2_element_data_window/): Transformation Keywords: [VOLFC](/docs/en/keyword_documentation/v/volfc/), [VOLFS](/docs/en/keyword_documentation/v/volfs/),

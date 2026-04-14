---
lang: en
title: "TRANS (2D3D)"
---

# TRANS

|  (Inter Material Data)  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

TRANS HT DEF TRANS DIFF GRAIN

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
HT |  Heat Transfer off = **0** on = **1** |  NA  
DEF |  Deformation off = **0** on = **1** |  NA  
TRANS  |  Transformation off = **0** on = **1** or **2** = **1** Default scheme = **2** Old additive-rule scheme |  NA  
DIFF |  Diffusion off = **0** on = **1** |  NA  
GRAIN |  Grain off = **0** on = **1** |  NA  
  
DEFINITION  
---  
TRANS enables and disables modes of analysis such as heat transfer and deformation in DEFORM® in the preprocessor. These must be selected in the beginning of the simulation.  
  
REMARKS  
---  
The heat transfer and deformation mode's functions identically to the non-isothermal and isothermal analysis, respectively, those are in the earlier versions of DEFORM. For example, if the user is interested in a thermal analysis such as observing the thermal gradients in a workpiece, then the user should selected heat transfer. Similarly, if the user is interested in a stress-strain analysis or volume changes as a result of a stress, then the user should select deformation mode. The transformation mode should be used when analyzing phase transformations or grain growth phenomenon. The diffusion mode allows the user to analysis the diffusivity of atoms into a material from the environment. In the case of the process of carburization, absorption and diffusion of carbon into steel are carried out in contact with a carbonaceous environment. The grain mode is used to simulate the grain recrystallization and growth. The current default transformation scheme replaces the old additive-rule scheme since 2d v81 and 3d v51. Its major difference from the old scheme are: 1) It handles simultaneous one-to-multiple phase transformation and 2) incubation time TICF and starting volume fraction VOLFN are not used anymore. Applicable Simulation Module's: Deformation, Thermal, Microstructure, Electro-Magnetic.  
  
RELATED TOPICS  
---  
[Inter-Material Data](/docs/en/pre_processor/10_material_data/10_9_transformation_data/10_9_1_transformation_kinetics_models/) Keywords: [SMODE](/docs/en/keyword_documentation/s/smode/), [VOLFS](/docs/en/keyword_documentation/v/volfs/), [VOLFC](/docs/en/keyword_documentation/v/volfc/), [TICF](/docs/en/keyword_documentation/t/ticf/), VOLFN

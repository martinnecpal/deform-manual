---
lang: sk
title: "FRCSTP (2D)"
---

# FRCSTP

|  (Object Data - 2D)  
---|---  
|  Last updated on : 06-08-2013  
  
* * *

FRCSTP Object, steps

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
steps |  number of steps to trigger the fracture program |  None  
  
DEFINITION  
---  
FRCSTP is how often the fracture criteria is checked. If 1 where used, ever step would be checked, which is fine. However, this checking is not done in the FEM engine. This means that ever step would be saved in the database, even if you specified to save ever X number of steps in the Stopping Step Criteria. This keyword takes precedence. It is better not to use this keyword but rather FRCNEL. This is checked in the FEM engine which means it will only exit the FEM engine when the criteria set for FRCNEL is reached. This will reduce the size of the database.  
  
RELATED TOPICS  
---  
[Flow stress](/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_flow_stress_models/), [Fracture](/docs/sk/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/) Keywords: [DAMAGE (2D)](/docs/sk/keyword_documentation/d/damage/), [DAMAGE (3D)](/docs/sk/keyword_documentation/d/damage_3d/), [FRCMOD](/docs/sk/keyword_documentation/f/frcmod/), [FRCNEL (2D)](/docs/sk/keyword_documentation/f/frcnel/), [FRCNEL (3D)](/docs/sk/keyword_documentation/f/frcnel_3d/), [FRCMTH (2D)](/docs/sk/keyword_documentation/f/frcmth/)

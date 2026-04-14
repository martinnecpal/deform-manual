---
lang: en
title: "FRCNEL (2D)"
---

# FRCNEL

|  (Object Data - 2D)  
---|---  
|  Last updated on : 06-08-2013  
  
* * *

FRCNEL Object, nelm

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
nelm |  Number of elements required to meet the fracture criteria before triggering the fracture program. |  None  
  
DEFINITION  
---  
FRCNEL determines the total number of elements that must meet the fracture criteria, before FEM is stopped and the fracture program is started. A good value to use is 4, because in releases after DEFORM®;-2D version 5.0 this may help in the element splitting program. However a value of 1 can be used.  
  
RELATED TOPICS  
---  
[Flow stress](../../pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress), [Fracture](/docs/en/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/) Keywords: [DAMAGE (2D)](/docs/en/keyword_documentation/d/damage/), [DAMAGE (3D)](/docs/en/keyword_documentation/d/damage_3d/), [FRCMOD (2D3D)](/docs/en/keyword_documentation/f/frcmod/), [FRCMTH (2D)](/docs/en/keyword_documentation/f/frcmth/)

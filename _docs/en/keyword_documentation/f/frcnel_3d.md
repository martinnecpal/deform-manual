---
lang: en
title: "FRCNEL (3D)"
---

# FRCNEL

|  (Object Data - 3D)  
---|---  
|  Last updated on : 12-08-2014  
  
* * *

FRCNEL Object, nelm

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
nelm |  Number of elements for triggering element deletion (any non-zero value will trigger element deletion) |  0  
  
DEFINITION  
---  
FRCNEL determines a triggering of element deletion during remeshing procedures. When non-zero value is specified and when FEM goes into remeshing procedures (for any reason), those elements whose damage value is higher than the critical damage value will be deleted. In v11 MO system, a check box (GUI) is used as on/off flag for "3D fracture element deletion".  
  
RELATED TOPICS  
---  
[Flow stress](../../pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress), [Fracture](/docs/en/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/) Keywords: [DAMAGE (2D)](/docs/en/keyword_documentation/d/damage/), [DAMAGE (3D)](/docs/en/keyword_documentation/d/damage_3d/), [FRCMOD (2D3D)](/docs/en/keyword_documentation/f/frcmod/)

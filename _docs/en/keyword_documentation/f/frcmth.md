---
lang: en
title: "FRCMTH (2D)"
---

# FRCMTH

|  (Object Data - 2D)  
---|---  
_Update History:_ v11 - Microvoid (no GUI), Void closure, and Forming limit diagram (FLD) models have been added. |  Last updated on : 06-08-2013  
  
* * *

FRCMTH Object, mode

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
mode |  Method of fracture growth =**0** Element Deletion = **1** Element Separation =**2** Element Splitting |  None  
  
DEFINITION  
---  
FRCMTH determines what type of fracture growth will be used. Element deletion removes elements. Element Separation separates elements along the edges and element splitting splits the elements. In DEFORM®; version 5.0, only the deletion works.  
  
RELATED TOPICS  
---  
[Flow stress](../../pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress), [Fracture](/docs/en/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/) Keywords: [DAMAGE (2D)](/docs/en/keyword_documentation/d/damage/), [DAMAGE (3D)](/docs/en/keyword_documentation/d/damage_3d/), [FRCMOD](/docs/en/keyword_documentation/f/frcmod/), [FRCNEL (2D)](/docs/en/keyword_documentation/f/frcnel/), [FRCNEL (3D)](/docs/en/keyword_documentation/f/frcnel_3d/), [FRCSTP (2D)](/docs/en/keyword_documentation/f/frcstp/)

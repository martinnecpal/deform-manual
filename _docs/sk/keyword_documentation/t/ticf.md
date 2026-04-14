---
lang: sk
title: "TICF (2D3D)"
---

# TICF

|  (Object data)  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

TICF Iobj, Numel, Nphase

1, t1, t2, t3, .. tn

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Iobj |  Object number |  None  
Numel |  Number of element |  None  
Nphase |  Number of material |  None  
  
DEFINITION  
---  
TICF (consumption of incubation time) specifies the fraction of time that has occurred before the transformation has started. It is calculated for diffusion type transformation as follows: ![]({{ '/assets/equations/keyword_documentation/t/ticf_eq_1.jpg' | relative_url }}) The variable ttotal is temperature dependent. If TICF reaches, the transformation starts.  
  
REMARKS  
---  
![]({{ '/assets/images/keyword_documentation/t/ticf_image001.jpg' | relative_url }}) A and B are the phases of the material. The curve defines the boundary between phase A and phase B. Therefore, for the figure shown above, phase B will be present to the right of the curve and phase A will be present to the left of the curve. Along the curve, phase A is transforming into phase B (A![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) B). The incubation time is defined for each phase in an element. The incubation time TICF is only valid for a diffusion or time dependent transformation and should not be used for a diffusionless transformation such as a martensitic transformation. Applicable Simulation Module: Microstructure Applicable [Simulation Modes](/docs/sk/pre_processor/9_simulation_controls/9_1_simulation_type_settings/): Transformation Applicable [object types](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4._Object_type): ALL except Rigid  
  
RELATED TOPICS  
---  
[Inter-Material Data](/docs/sk/pre_processor/10_material_data/10_9_transformation_data/10_9_transformation_data/) Keywords: [TRANS](/docs/sk/keyword_documentation/t/trans/)

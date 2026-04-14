---
lang: en
title: "Appendix IV: Determining &#39;R&#39; coefficients for anisotropy models"
---

# Appendix IV: Determining 'R' Coefficients for anisotropy models

DEFORM® material model allows for anisotropy in sheet metal. Two of the models use “R” ratios for defining anisotropic behavior in rolled sheet.

The R value represents a ratio between orthogonal components of transverse strain in a tension test.

Tension test samples are typically cut at 0°, 45°, and 90° to the rolling direction of the sheet. One can then define

![]({{ '/assets/images/appendices/appendix_iv_determining_r_coefficients/r_theta.jpg' | relative_url }}) as,

![]({{ '/assets/images/appendices/appendix_iv_determining_r_coefficients/eqn1.jpg' | relative_url }}) |  (EQ.1)  
---|---  
  
The measurements are typically taken at an elongation of 15 to 20%, or before the onset of necking on low ductility materials.

In DEFORM, the user may specify ![]({{ '/assets/images/appendices/appendix_iv_determining_r_coefficients/r0.jpg' | relative_url }}), ![]({{ '/assets/images/appendices/appendix_iv_determining_r_coefficients/r45.jpg' | relative_url }}) and ![]({{ '/assets/images/appendices/appendix_iv_determining_r_coefficients/r90.jpg' | relative_url }}) or a single valued ![]({{ '/assets/images/appendices/appendix_iv_determining_r_coefficients/r.jpg' | relative_url }}) may be specified, where is defined as,

![]({{ '/assets/images/appendices/appendix_iv_determining_r_coefficients/eqn2.jpg' | relative_url }}) |  (EQ.2)  
---|---  
  
**Quadratic Hill Criterion (From Wikipedia):**

The [quadratic Hill yield](../pre_processor/10_material_data/10_1_plastic_data/10_1_3_yield_models/10_1_3_2_hill’s_quadratic_\(fghlmn\).htm) criterion [1]. has the form

![]({{ '/assets/images/appendices/appendix_iv_determining_r_coefficients/eqn3.jpg' | relative_url }}) |  (EQ.3)  
---|---  
  
The quadratic Hill yield criterion depends only on the deviatoric/shear stresses and is pressure independent.

It predicts the same yield stress in tension and in compression.

**[edit] Expressions for F, G, H, L, M, N:**

If the axes of material anisotropy are assumed to be orthogonal, we can write,

![]({{ '/assets/images/appendices/appendix_iv_determining_r_coefficients/eqn4.jpg' | relative_url }}) |  (EQ.4)  
---|---  
  
Therefore we have,

![]({{ '/assets/images/appendices/appendix_iv_determining_r_coefficients/eqn5.jpg' | relative_url }}) |  (EQ.5)  
---|---  
  
Similarly, if ![]({{ '/assets/images/appendices/appendix_iv_determining_r_coefficients/tau.jpg' | relative_url }}) are the yield stresses in shear (with respect to the axes of anisotropy), we have,

![]({{ '/assets/images/appendices/appendix_iv_determining_r_coefficients/eqn6.jpg' | relative_url }}) |  (EQ.6)  
---|---  
  
R. Hill. (1948). A theory of the yielding and plastic flow of anisotropic metals. Proc. Roy. Soc. London, 193:281–297.

**Related Topics:**

[Material Properties](/docs/en/pre_processor/10_material_data/10_material_data/)

[Yield function type](/docs/en/pre_processor/10_material_data/10_1_plastic_data/10_1_3_yield_models/10_1_3_yield_models/)

[Hill’s quadratic (R value)](../pre_processor/10_material_data/10_1_plastic_data/10_1_3_yield_models/10_1_3_3_hill’s_quadratic_\(r\).htm)

[Hill’s quadratic (FGHLMN)](../pre_processor/10_material_data/10_1_plastic_data/10_1_3_yield_models/10_1_3_2_hill’s_quadratic_\(fghlmn\).htm)

[Lankford coefficient (R value)](../pre_processor/10_material_data/10_1_plastic_data/10_1_3_yield_models/10_1_3_4_lankford_coefficient_\(r_value\).htm)

---
lang: en
title: "10.1.3.5. Hill’s Quadratic (polycrystalline plasticity model)"
---

# 10.1.3.5. Hill’s Quadratic (Polycrystalline plasticity model)

For Hill’s quadratic (Polycrystal plasticity) anisotropy yield function model (See below Fig. 10.1.3.5.1.), texture information (crystal type, texture type) should be defined in Material dialog. At each material point of an object, orientation distribution functions (ODFs) will be evaluated based on the meshed rodrigues space.

![]({{ '/assets/images/pre-processor/10_material_data/10_1_plastic_data/10_1_3_yield_models/10_1_3_5_hill’s_quadratic_\(polycrystalline\)/10_1_3_5_image001.jpg.jpg' | relative_url }})

Hills quadratic (Polycrystalline plasticity model)

TXTODF specifies ODFs at each material point of an object. If the material has multiple phases, TXTODF lists the ODFs phase by phase, depending on the definition of phase sequence of the material. For single phase material, when Rodrigues space is employed to represent texture, number of ODFs is equal to the independent nodes of meshed Rodrigues space. For multiple-phase material, number of ODFs is equal to the summation of independent nodes of meshed Rodrigues space of all phases.

[10.1.3.1. Von Mises](/docs/en/pre_processor/10_material_data/10_1_plastic_data/10_1_3_yield_models/10_1_3_1_von_mises/)

[10.1.3.2. Hill’s quadratic (FGHLMN)](10_1_3_2_hill’s_quadratic_\(fghlmn\).htm)

[10.1.3.3. Hill’s quadratic (R)](10_1_3_3_hill’s_quadratic_\(r\).htm)

[10.1.3.4. Lankford coefficient (R value)](10_1_3_4_lankford_coefficient_\(r_value\).htm)

[10.1.3.6. User's routine](/docs/en/pre_processor/10_material_data/10_1_plastic_data/10_1_3_yield_models/10_1_3_6_user_s_routine/)

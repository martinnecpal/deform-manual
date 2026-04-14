---
lang: sk
title: "10.2.5. Hyperelastic"
---

# 10.2.5. Hyperelastic

Hyperelastic ([HYPREL](/docs/sk/keyword_documentation/h/hyprel/)) is valid only for hyperelastic objects. From DEFORM v12, two hyperelastic constitutive models are provided to simulate hyperelasticity.  
  
In hyperelastic constitutive models, the work is independent of the load path. There is a strain energy function(w) as a potential for the stress. 

![]({{ '/assets/equations/pre_processor/10_material_data/10_2_elastic_data/eq_10_2_5_1.jpg' | relative_url }}) |   
---|---  
  
  
**Neo-Hookean (CNH) material (extension of the Hooke’s law):**

![]({{ '/assets/equations/pre_processor/10_material_data/10_2_elastic_data/eq_10_2_5_2.jpg' | relative_url }}) |   
---|---  
  
  
**Mooney-Rivlin (MR) model:**

![]({{ '/assets/equations/pre_processor/10_material_data/10_2_elastic_data/eq_10_2_5_3.jpg' | relative_url }}) |   
---|---  
  
[10.2. Elastic Data](/docs/sk/pre_processor/10_material_data/10_2_elastic_data/10_2_elastic_data/)

[10.3 Thermal Data](/docs/sk/pre_processor/10_material_data/10_3_thermal_data/10_3_thermal_data/)

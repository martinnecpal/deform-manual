---
lang: en
title: "10.6.1 Avrami Model"
---

# 10.6.1. Avrami Model

  * Dynamic Recrystallization

  * Static Recrystallization

  * Meta-dynamic Recrystallization

  * Grain Growth

  * NOMENCLATURE

The Avrami equation describes how solids transform from one phase (state of matter) to another at constant temperature. It can specifically describe the kinetics of crystallization. (See Fig. 10.6.1.1.)

![]({{ '/assets/images/pre-processor/10_material_data/10_6_grain_data/10_6_image002.jpg' | relative_url }})

Avrami Grain Material model window

**Definitions:**  
**Dynamic recrystallization:** occurring during deformation and when the strain exceeds critical strain. The driving force is removal of dislocations.  
  
**Static recrystallization:** occurring after deformation and when strain is less than critical strain. The driving force is removal of dislocations. The recrystallization begins in a nuclei-free environment.  
  
**Meta-dynamic recrystallization:** occurring after deformation and when strain is greater than critical strain. The driving force is removal of dislocations. Because the strain has exceeded critical strain, recrystallization nuclei have formed in the material, so the recrystallization behaviors are different from without nuclei (static recrystallization).

  
**Grain Growth:** occurring before recrystallization begins or after recrystallization is completed. The driving force is the reduction of grain boundary energy.

**Strain retaining coefficient** : The strain retaining coefficient is only used when: 

  1. The current step has deformation. 

  2. The previous step has no deformation, i.e, at the beginning step when the operation changes from heat transfer to deformation. 

The equation is as following: 

![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/eq_10_6_1_17.jpg' | relative_url }}) |   
---|---  
  
**Dynamic Recrystallization**

The dynamic recrystallization is a function of strain, strain rate, temperature, and initial grain size, which change in time. It is very difficult to model dynamic recrystallization concurrently during forming. Instead, the dynamic recrystallization is computed in the step immediately after the deformation stops. Average temperatures, strain rate of the deformation period is used as inputs of the equations.

  1. **Activation Criteria**

The onset of DRX usually occurs at a critical strain ![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/epsalon_c.jpg' | relative_url }}) . 

![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/eq_10_6_1_1.jpg' | relative_url }}) |   
---|---  
  
  
Where ![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/epsalon_p.jpg' | relative_url }}) denotes the peak strain corresponding to the flow stress maximum: 

![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/eq_10_6_1_2.jpg' | relative_url }}) |   
---|---  
  
Refer Nomenclature mentioned below for terms explanation.

  1. **Kinetics**

The Avrami equation is use to describe the relation between the dynamically recrystallized fraction ![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/x.jpg' | relative_url }}) and the effective strain. 

![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/eq_10_6_1_3.jpg' | relative_url }}) |   
---|---  
  
  
Where ![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/epsalon_0_5.jpg' | relative_url }}) denotes the strain for 50% recrystallization: 

![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/eq_10_6_1_4.jpg' | relative_url }}) |   
---|---  
  
  
Refer Nomenclature mentioned below for terms explanation.

  1. **Grain Size**

The recrystallized grain size is expressed as a function of initial grain size, strain, strain rate, and temperature, 

![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/eq_10_6_1_5.jpg' | relative_url }}) |   
---|---  
  
  
Refer Nomenclature mentioned below for terms explanation.

**Static Recrystallization**

When deformation stops, the strain rate and critical strain are used to determine whether static or meta-dynamic recrystallization should be activated. The static and meta-dynamic recrystallization is terminated when this element starts to deform again.

  1. **Activation Criteria**

When strain rate is less than![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/epsalon_dot_ss.jpg' | relative_url }}), static recrystallization occurs after deformation. 

![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/eq_10_6_1_6.jpg' | relative_url }}) |   
---|---  
  
  
Refer Nomenclature mentioned below for terms explanation.

  1. **Kinetics**

The model for recrystallization kinetics is based on the modified Avrami equation. 

![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/eq_10_6_1_7.jpg' | relative_url }}) |   
---|---  
  
Where ![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/t_0_5.jpg' | relative_url }}) is an empirical kinetics is based on the modified Avrami equation. 

![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/eq_10_6_1_8.jpg' | relative_url }}) |   
---|---  
  
Refer Nomenclature mentioned below for terms explanation.

  1. **Grain Size**

The recrystallized grain size is expressed as a function of initial grain size, strain, strain rate, and temperature, 

![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/eq_10_6_1_9.jpg' | relative_url }}) |   
---|---  
  
Refer Nomenclature mentioned below for terms explanation.

**Meta-dynamic Recrystallization**

Meta-dynamic recrystallization is similar to static recrystallization but with different activation criteria and material constants.

  1. **Activation Criteria**

When strain rate is greater than ![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/epsalon_dot_ss.jpg' | relative_url }}) (See EQ(10.6.1.3.)), meta-dynamic recrystallization occurs after deformation.

  1. **Kinetics**

The model for recrystallization kinetics is based on the modified Avrami equation. 

![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/eq_10_6_1_10.jpg' | relative_url }}) |   
---|---  
  
  
Where ![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/t_0_5.jpg' | relative_url }}) is an empirical time constant for 50% recrystallization: 

![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/eq_10_6_1_11.jpg' | relative_url }}) |   
---|---  
  
  
Refer Nomenclature mentioned below for terms explanation.

  1. **Grain Size**

The recrystallized grain size is expressed as a function of initial grain size, strain, strain rate, and temperature,

![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/eq_10_6_1_12.jpg' | relative_url }}) |   
---|---  
  
  
Refer Nomenclature mentioned below for terms explanation.

**Grain Growth**

Grain growth takes place before recrystallization start or after recrystallization finishes.  
The kinetics is described by equation:   

![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/eq_10_6_1_13.jpg' | relative_url }}) |   
---|---  
  
  
Refer Nomenclature mentioned below for other terms explanation.  
  
**Retained Strain and Grain Size**  
When there are multiple deformation processes, strain may be reduced during the inter pass period due to recovery.  
  
The following equation is used to compute the retained strain at the beginning of the subsequent deformation. 

![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/eq_10_6_1_14.jpg' | relative_url }}) |   
---|---  
  
  
Refer Nomenclature mentioned below for terms explanation.  
  
**Temperature Limit**  
The temperature limit is the lower bound of all grain evolution mechanisms. Below this temperature, no grain evolution occurs.  
  
**Average Grain Size**  
The mixture law was employed to calculate the recrystallized grain size for uncompleted recrystallization, 

![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/eq_10_6_1_15.jpg' | relative_url }}) |   
---|---  
  
  
In addition, if at the beginning of deformation total ![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/xrex.jpg' | relative_url }}) is 1.0, the program will re-initialize (e.g. ![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/xrex.jpg' | relative_url }}) = 0) in order to compute a new round of recrystallization.  
Refer Nomenclature mentioned below for terms explanation.  
  
**Model Dependency on Temperature and Strain Rate**  
DEFORM allows different constants and coefficients for the equations at different temperatures or strain rates. The data are linearly interpolated.  
**  
****NOMENCLATURE**

![]({{ '/assets/equations/pre_processor/10_material_data/10_6_grain_data/10_6_1_avarami_model/eq_10_6_1_16.jpg' | relative_url }})

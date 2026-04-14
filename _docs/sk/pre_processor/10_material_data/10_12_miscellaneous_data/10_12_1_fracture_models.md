---
lang: sk
title: "10.12.1. Fracture Models"
---

# 10.12.1. Fracture Models

  * Normalized C&L damage model

  * Cockcroft & Latham damage model

  * McClintock damage model

  * Freudenthal damage model

  * Rice & Tracy damage model

  * Oyane damage model

  * Oyane (negative) damage model

  * Ayada damage model

  * Osakada damage model

  * Brozzo damage model

  * Zhoa &Kuhn damage model

  * [Maximum principal stress / ultimate tensile strength damage model](10_12_1_fracture_models.htm#Maximum_principal_stress_/_ultimate_tensile_strength)

  * Void closure damage model

  * FLD damage model

  * User routine damage model

Fracture models available in DEFORM are (see Fig. 10.12.1.1.):

  * Normalized C&L
  * Cockcroft & Latham
  * McClintock
  * Freudenthal
  * Rice & Tracy
  * Oyane
  * Oyane (negative)
  * Ayada
  * Osakada
  * Brozzo
  * Zhoa &Kuhn
  * Maximum principal stress / ultimate tensile strength
  * Void closure
  * FLD
  * User routine

![]({{ '/assets/images/pre-processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/10_12_1_image001.jpg' | relative_url }})

Fracture Models in DEFORM

  * **Normalized C &L damage model**

This model is defined as a function of max. principal stress (![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/sigma_dash.jpg' | relative_url }})) normalized with effective stress (![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/sigma_bar.jpg' | relative_url }})).

![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/eq_10_12_1_1.jpg' | relative_url }}) |   
---|---  
  
  * **Cockcroft & Latham damage model**

This model is defined as a function of max. principal stress (![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/sigma_star.jpg' | relative_url }})).

![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/eq_10_12_1_2.jpg' | relative_url }}) |   
---|---  
  
  * **McClintock damage model**

This model is defined as a function of max. and min. principal stress ( ![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/sigma_a.jpg' | relative_url }}) and ![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/sigma_b.jpg' | relative_url }}) ) and effective stress. is the model coefficient.

![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/eq_10_12_1_3.jpg' | relative_url }}) |   
---|---  
  
  * **Freudenthal damage model**

This model is defined as a function of effective stress (![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/sigma_bar.jpg' | relative_url }}) ).

![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/eq_10_12_1_4.jpg' | relative_url }}) |   
---|---  
  
  * **Rice & Tracy damage model**

This model is defined as a function of mean stress ( ![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/sigma_m.jpg' | relative_url }})) and effective stress ( ![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/sigma_bar.jpg' | relative_url }}) ). ![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/alpha.jpg' | relative_url }}) is the model coefficient.

![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/eq_10_12_1_5.jpg' | relative_url }}) |   
---|---  
  
  * **Oyane damage model**

This model is defined as a function of mean stress ( ![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/sigma_m.jpg' | relative_url }})) and effective stress (![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/sigma_bar.jpg' | relative_url }}) ). ![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/a_not.jpg' | relative_url }}) is the model constant.

The ![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/a_not.jpg' | relative_url }}) material constant has been assumed to be 0.424 in many published works, as determined by Hambli and Reszka.

_Hambli, R.; Reszka, M. Fracture criteria identification using an inverse technique method and blanking experiment. Int. J. Mech. Sci., 2002, 44, 1349–1361. https://doi.org/10.1016/S0020-7403(02)00049-8._

![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/eq_10_12_1_6.jpg' | relative_url }}) |   
---|---  
  
  * **Oyane (negative) damage model**

Accounts for negative terms in the integral to allow damage values to decrease or increase based on the stress state. Including the negative integration term in the above equation EQ(10.12.1.6).

  * **Ayada damage model**

This model is defined as a function of mean stress (![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/sigma_m.jpg' | relative_url }})) and effective stress (![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/sigma_bar.jpg' | relative_url }})).

![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/eq_10_12_1_7.jpg' | relative_url }}) |   
---|---  
  
  * **Ayada (negative) damage model**

Accounts for negative terms in the integral to allow damage values to decrease or increase based on the stress state. Including the negative integration term in the above equation EQ(10.12.1.7).

  * **Osakada damage model**

This model is defined as a function of mean stress and effective strain ![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/small_a.jpg' | relative_url }}) and ![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/small_b.jpg' | relative_url }}) are the model coefficients.

![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/eq_10_12_1_8.jpg' | relative_url }}) |   
---|---  
  
  * **Brozzo damage model**

This model is defined as a function of principal stress (![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/sigma_star.jpg' | relative_url }}) ) and mean stress (![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/sigma_m.jpg' | relative_url }})).

![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/eq_10_12_1_9.jpg' | relative_url }}) |   
---|---  
  
  * **Zhoa & Kuhn damage model**

This model is defined as a function of principal stress (![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/sigma_star.jpg' | relative_url }})) and effective stress (![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/sigma_bar.jpg' | relative_url }})), but it is dependent only on stress state.

![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/eq_10_12_1_10.jpg' | relative_url }}) |   
---|---  
  
  * **Damage based on Maximum principal stress / ultimate tensile strength**

This model is defined as a function of maximum principal stress and ultimate tensile strength (UTS) and is dependent only on stress state. UTS can also be a function of temperature.

![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/eq_10_12_1_11.jpg' | relative_url }}) |   
---|---  
  
  * **Void Closure**

Void closure model estimates “healing factor”, which is a void ratio defined by dividing current void volume by initial void volume. The percent flow stress softening becomes 100% since it is a healing model rather than a fracture model. The internal void closing evaluation index (Q) is computed in FEM simulation using the following definition. (Where 0.0 < Q < 1.0) 

![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/eq_10_12_1_12.jpg' | relative_url }}) |   
---|---  
  
  
User needs to provide Void volume ratio as function of Void Closure Index (Q) as shown in Fig. 10.12.1.2.

![]({{ '/assets/images/pre-processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/10_12_1_image004.jpg' | relative_url }})

Void closure function window

  * **FLD damage model**

Forming limit diagram (FLD) model is introduced as a failure indicator in sheet metal forming simulations. Flow softening can be considered in FLD. This model is available only in MO Environment. The damage factor is defined as a major strain ratio (= current major strain / limit major strain) for a given major and minor strain condition. (See Fig. 10.12.1.3.)

![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/eq_10_12_1_13.jpg' | relative_url }}) |   
---|---  
  
![]({{ '/assets/images/pre-processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/10_12_1_image003.jpg' | relative_url }})

Damage factor Major Strain ratio graph

  
The forming limit diagram (i.e., a minor strain vs. major strain diagram) should be provided by users. User can edit FLD function data as shown in Fig. 10.12.1.4.

![]({{ '/assets/images/pre-processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/10_12_1_image005.jpg' | relative_url }})

Forming Limiting Diagram window

  
By selecting Define Button user can define the FLD (Major strain, Minor strain) as shown in Fig. 10.12.1.5.

![]({{ '/assets/images/pre-processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/10_12_1_image006.jpg' | relative_url }})

Forming Limiting Diagram Function window

  * **Damage user routine**

If the Maximum effective stress / ultimate tensile strength model is selected the ultimate tensile strength ([UTSDAT](/docs/sk/keyword_documentation/u/utsdat/)) has to be defined as a constant or a function of temperature. Additional models on the basic Oyane and Ayada models are also provided to account for negative terms in the integral to allow damage values to decrease or increase based on the stress state. The DAMAGE state variable is used to trigger fracture modeling using either element deletion or continuum damage softening. For element deletion, elements which exceed a defined critical damage value are deleted from the mesh. This is an effective way of modeling crack propagation. Element deletion must be activated for each object under the Object properties dialog. For continuum damage softening, the flow stress value used for element stiffness calculation is reduced to a specified percentage (typically 1 to 5%) of the flow stress calculated for the element. User can create the damage model using the available state variables in usr_dmg.f fortran file. User routine number of usr_dmg.f must be mentioned as shown in Fig. 10.12.1.6. to pick the user defined model for damage calculations.

![]({{ '/assets/images/pre-processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/10_12_1_image002.jpg' | relative_url }})

Damage User routine model window

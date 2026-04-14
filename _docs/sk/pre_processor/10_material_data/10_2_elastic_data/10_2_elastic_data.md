---
lang: sk
title: "10.2. Elastic Data"
---

# 10.2. Elastic Data

10.2.1. Young's modulus

10.2.2. Poisson's ratio

10.2.3. Thermal expansion

10.2.4. Material Reference Temperature

[10.2.5. Hyperelastic](/docs/sk/pre_processor/10_material_data/10_2_elastic_data/10_2_5_hyperelastic/)

Elastic data is required for the deformation analysis of elastic and elasto-plastic materials. The three variables used to describe the properties for elastic deformation are Young's modulus, Poisson's Ratio, Thermal expansion and Hyperelastic as shown in Fig. 10.2.1.

![]({{ '/assets/images/pre-processor/10_material_data/10_2_elastic_data/10_2_image001.jpg' | relative_url }})

Elastic material data window

  
  
Note:   
To activate the reference temperature option, the thermal expansion coefficient must be made a function of temperature.

## Young's modulus 

Young's Modulus ([YOUNG](/docs/sk/keyword_documentation/y/young/)) is used for elastic materials and elasto -plastic materials below the yield point. It can be defined as a constant or as a function of temperature, density (for powder metals), dominant atom content (for example, carbon content) or a function of temperature and atom content.

## Poisson's ratio

Poisson's ratio ([POISON](/docs/sk/keyword_documentation/p/poison/)) is the ratio between axial and transverse strains. It is required for elastic and elasto-plastic materials. It can be defined as a constant or as a function of temperature, density (for powder metals), dominant atom content (for example, carbon content), or a function of temperature and atom content.

## Thermal expansion

The coefficient of thermal expansion ([EXPAND](/docs/sk/keyword_documentation/e/expand/)) defines volumetric strain due to changes in temperature. It can be defined as a constant or as a function of temperature.  
For elastic bodies temperature change is defined as the difference between nodal temperatures and the specified reference temperature ([REFTMP](/docs/sk/keyword_documentation/r/reftmp/)): 

![]({{ '/assets/equations/pre_processor/10_material_data/10_2_elastic_data/eq_10_2_3_1.jpg' | relative_url }}) |   
---|---  
  
  
For elasto-plastic bodies the thermal expansion input in the pre-processor is the average value of thermal expansion and the FEM calculates the instantaneous (tangential) value from the average value.

![]({{ '/assets/equations/pre_processor/10_material_data/10_2_elastic_data/eq_10_2_3_2.jpg' | relative_url }}) |   
---|---  
  
  
Experimental data for thermal expansion and conversion tools are available.  
The user interface now allows either direct entry of the tangent thermal expansion coefficient as a function of temperature, or user can also import instantaneous values if available from the experimental data. (See Fig. 10.2.2.) When importing the instantaneous values, user needs to indicate if the recordings are based on heating or cooling tests and the reference temperature. This instantaneous thermal expansion data can be converted to average data. (Also called secant, which is the data requirement from the model perspective). At any point user can see either native data as imported or converted data or both. This data can also be imported and exported as text files. This table data can also be cut and pasted from and to Excel (on PC systems) data table.

![]({{ '/assets/images/pre-processor/10_material_data/10_2_elastic_data/10_2_3_image001.jpg' | relative_url }})

Data conversion facilities for thermal expansion function data

## Material Reference Temperature

Reference temperature ([REFTMP](/docs/sk/keyword_documentation/r/reftmp/)) is valid only for the Elastic and Elasto plastic objects thermal expansion calculation, this value is used as the reference temperature for thermal expansion calculation. For Elasto-Plastic models or objects, (starting from DEFORM v11) reference temperature defined in material data dialog is always used. For Elastic models or objects, if the thermal expansion is constant object reference temperature will be used (refer Object properties reference Temperature). For Elastic models or objects, if the thermal expansion is a function of temperature reference temperature defined in material data dialog will be used.

[10.2.5. Hyperelastic](/docs/sk/pre_processor/10_material_data/10_2_elastic_data/10_2_5_hyperelastic/)

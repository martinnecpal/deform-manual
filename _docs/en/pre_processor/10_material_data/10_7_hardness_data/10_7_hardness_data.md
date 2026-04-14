---
lang: en
title: "10.7. Hardness Data"
---

# 10.7. Hardness Data

10.7.1. Hardness of each phase (HDNPHA)

10.7.2. Jominy curve (JOMINY)

10.7.3. Cooling time (HDNTIM)

There are two methods by which the hardness of a object can be determined after a cooling operation. The screen where this data is set is shown in Fig. 10.7.1. he first method is by specifying the hardness of each phase (HDNPHA) in a mixture and DEFORM will use the mixture law to determine the hardness of each element. The second method is to use experimental results from the Jominy curve and cooling time vs distance to determine the hardness during cooling. Initial Hardness and cooling type of the object can be added from Object Element window. The method of calculating the hardness can be specified for each object in the Object Properties - Hardness., Both the Jominy Curve and Cooling Time material data inputs are required when “Use Jominy curves” or “Only cooling time” option is selected under [Object properties – Hardness](/docs/en/pre_processor/16_object_properties/16_5_hardness_properties/) tab.

  
Any hardness unit may be used in DEFORM if it is used in conjunction with coefficients that were calibrated to the specific hardness unit. For example, if coefficients were determined based on an experimental HRC data, then the HRC hardness unit must be used in DEFORM simulation that uses those coefficients.  
Brinell and Vickers hardness values can be converted to units of MPa by multiplying the hardness values by the metric standard gravity value (9.80665 m/s^2). If units of KSI are desired, then perform an additional conversion from MPa to KSI.

![]({{ '/assets/images/pre-processor/10_material_data/10_7_hardness_data/10_7_image001.jpg' | relative_url }})

Hardness material data window

## Hardness of each phase (HDNPHA)

The hardness of each phase (material group) can be specified. The hardness of each phase ([HDNPHA](/docs/en/keyword_documentation/h/hdnpha/)) can be defined as constant or as function of atom content or Temperature or Density or Temperature and Atom. The hardness of the object will be calculated based on the volume fraction of each phase in the element and on the hardness of each phase. 

  
From v14.0., hardness can be estimated using Solid solution with precipitate model as shown in Fig. 10.7.2.

![]({{ '/assets/images/pre-processor/10_material_data/10_7_hardness_data/10_7_image002.jpg' | relative_url }})

Solid solution with precipitate option 

## Jominy curve (JOMINY)

The hardness vs. distance for the Jominy test specimen must be specified here as shown in Fig. 10.7.3. The jominy curve is a determination of the hardness in the Jominy specimen at a specific distance from the cool end. Therefore, the Jominy curve is useful in determining the hardenability of a material as a function of the distance from the water-cooled end. 

![]({{ '/assets/images/pre-processor/10_material_data/10_7_hardness_data/10_7_image003.jpg' | relative_url }})

Jominy curve function page 

## Cooling time (HDNTIM)

Using Jominy distance vs. Cooling time option, define the cooling time vs. distance for the Jominy test specimen as shown in Fig. 10.7.4. Using the Jominy curve ([JOMINY](/docs/en/keyword_documentation/j/jominy/)) data and the colling time ([HDNTIM](/docs/en/keyword_documentation/h/hdntim/)) data, DEFORM will estimate the hardness of the object during cooling. 

![]({{ '/assets/images/pre-processor/10_material_data/10_7_hardness_data/10_7_image004.jpg' | relative_url }})

Jominy distance vs. Cooling time

**Related Topics:**

[16.5. Hardness Properties](/docs/en/pre_processor/16_object_properties/16_5_hardness_properties/)

[17.2. Element Data Window](/docs/en/pre_processor/17_object_data_initialization/17_2_element_data_window/)

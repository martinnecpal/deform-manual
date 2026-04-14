---
lang: en
title: "HDNEST (2D3D)"
---

# HDNEST

|  (Object data)  
---|---  
|  Last updated on : 07-08-2013  
  
* * *

HDNEST Obj, Type, Unit, Temph, Templ

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Obj |  Object number |  None  
Type |  Kind of hardness estimation =**0** No estimate =**1** Using Jominy Curve (for quenching process) =**2** Using volume fractions of each phase =**3** Using only cooling time **-n** User routine n |  None  
Temph |  Referenced high temperature |   
Templ |  Referenced low temperature |   
  
DEFINITION  
---  
HDNEST specifies the hardness for a material. SYSTEM UNITS: USER DEFINED  
  
REMARKS  
---  
HDNEST specifies the estimation method of hardness. For Type=1 (Using Jominy Curve), the user must specify the high and low reference temperatures under which the Jominy curve is valid. The hardness is estimated using both the cooling time and Jominy data. The data is specified in the keywords HDNTIM and JOMINY. For Type=2, the weighted average of hardness of each phase (defined in HDNPHA) is used to estimate the hardness. | ![]({{ '/assets/equations/keyword_documentation/h/hdnest_eq_1.jpg' | relative_url }}) |   
---|---  
  
For Type=3 only the cooling versus distance curve is used for the estimation of hardness.

General Guidelines for selecting the hardness estimation method

If the user does not want to spend the time with entering vast amounts of data it is recommended that the user selects estimation method type 2, volume fraction. The disadvantage in using this method is that it may not be as accurate as using the Jominy estimation.

Note: The cooling time is only valid in a given temperature range.

Applicable Simulation Modules: Microstructure

Applicable Simulation Modes: Transformation

Applicable Object Types: ALL except Rigid  
  
RELATED TOPICS  
---  
Material Data: [Hardness](/docs/en/pre_processor/10_material_data/10_7_hardness_data/10_7_hardness_data/) Keyword: [HDNTIM](/docs/en/keyword_documentation/h/hdntim/), [JOMINY](/docs/en/keyword_documentation/j/jominy/), [HDNPHA](/docs/en/keyword_documentation/h/hdnpha/)

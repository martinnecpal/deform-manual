---
lang: en
title: "VARSEL (2D3D)"
---

# VARSEL

|  (Inter-material data)  
---|---  
_Update History:_ v11 – VARSEL has been introduced. |  Last updated on : 24-07-2013  
  
* * *

VARSEL Mat1, Mat2, VarSelType

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Mat1 |  Material 1 |  None  
Mat2 |  Material 2 |  None  
VarSelType |  Variant selection model type = **0** None = **1** Random selection = **2** Matching by kerns numbers = **3** Matching by resolved shear stress |  0  
  
DEFINITION  
---  
VARSEL specifies the variant selection model for texture evolution during phase transformation.  
  
REMARKS  
---  
Phase transformations in alloys often occur with specific orientation relationships between the precursor and transformed phases. This means that a crystallographic texture existing prior to transformation will lead to a specific texture in the transformed material. If during transformation, individual orientations (or variants) occur/evolve more frequently than others, variant selection is said to have taken place, which in steels is usually associated with displacive phase transformation to martensite or bainite. However, in titanium and zirconium alloys variant selection is seen during diffusion phase transformation and the effect can be exacerbated by application of stress during transformation. Scientifically extremely interesting, variant selection in titanium and zirconium alloys is also of great importance for the aerospace and nuclear industry, since this phenomenon affects the texture development during thermomechanical processing of the material and consequently mechanical properties. Applicable object types: [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic) Applicable simulation type: Microstructure, Heat treatment, Transformation  
  
RELATED TOPICS  
---  
Related keywords: [TTTD](/docs/en/keyword_documentation/t/tttd/)

---
lang: en
title: "TRNSFP (2D3D)"
---

# TRNSFP

|  (Inter Material data)  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

TRNSFP Mat1, Mat2, ITYPE, KTYPE, KValue/Npt1,Npt2

Temp/Atm(1) TRNSFP(1)

Temp/Atm(Npt1) TRNSFP(Ndata)

or

Temp(1) ...Temp(Npt1)

Atm(1) ... Atm(Npt2)

TRNSFP(1,1) ... TRNSFP(Npt1,1)

...

TRNSFP(1,Npt2) ... TRNSFP(Npt1,Npt2)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Mat1  |  Material 1 |  None  
Mat2 |  Material 2 |  None  
ITYPE  |  Function type |   
|  =**0** Transformation plasticity not considered |   
|  =**1** with  ![]({{ '/assets/equations/keyword_documentation/t/trnsfp_eq_1.jpg' | relative_url }}) |   
KTYPE |  Type of KIJ |  None  
|  =**0** Constant |   
|  =**1** Function of temperature |   
|  =**2** Function of atom |   
|  =**3** Function of atom and temperature |   
KValue |  Value of K for KTYPE method=**0** |  None  
Npt1,Npt2  |  Number of data pairs if k is a function |   
  
DEFINITION  
---  
TRNSFP defines the transformation plasticity model for a transformation relationship. It is defined between material groups (phases) and it is associated with the object when the material is defined for the object. SYSTEM UNITS: (s-1)  
  
REMARKS  
---  
The phenomenon of transformation plasticity is where the material will plastically deform at lower applied stresses than the yield stress of the material when the applied stress occurs during transformation. Applicable Simulation Modules: Microstructure, Deformation Applicable [Simulation Modes](/docs/en/pre_processor/9_simulation_controls/9_1_simulation_type_settings/): Deformation, Transformation Applicable [object types](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4._Object_type): [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic) and [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic),  
  
RELATED TOPICS  
---  
Inter-Material Data:[ Transformation Plasticity](../../pre_processor/10_material_data/10_9_transformation_data/10_9_transformation_data.htm#Transformation_plasticity_\(TRNSFP\)) Related keywords: [VOLFS](/docs/en/keyword_documentation/v/volfs/), [VOLFC](/docs/en/keyword_documentation/v/volfc/), [STNOUT](/docs/en/keyword_documentation/s/stnout/)

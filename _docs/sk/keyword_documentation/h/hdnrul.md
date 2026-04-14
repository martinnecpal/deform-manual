---
lang: sk
title: "HDNRUL (2D3D)"
---

# HDNRUL

|  (Material data)  
---|---  
|  Last updated on : 07-08-2013  
  
* * *

HDNRUL Mat, Type

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Mat |  Material Number |  None  
Type |  = **0** Isotropic = **1** Kinematic |  None  
  
DEFINITION  
---  
HDNRUL specifies the type of hardening that occurs in the material under an applied load.  
  
REMARKS  
---  
The isotropic hardening rule assumes that the Von Mises yield surface expands uniformly as the material is stressed into the plastic regime. The kinematic hardening rule takes into account the Bauschinger Effect on the Von Mises yield surface that shifts the origin of the Von Mises yield circle. The use of the hardening model can only be used when the object is elasto-plastic (OBJTYP) and the flow stress model is type number 6. ([FSTRES](/docs/sk/keyword_documentation/f/fstres/)). The kinematic hardening model is recommended when running in the transformation mode ([TRANS](/docs/sk/keyword_documentation/t/trans/)). It should be noted that the kinematic hardening model must only be used when the material undergoes small deformations. Flow Stress Model #6 Use Hardening Elasto-Plastic Object Model TRANS KINEMATIC OTHER ISOTROPIC Applicable Simulations Modules: Microstructure Applicable Simulation Modes: Transformation Applicable Object Types: [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic)  
  
RELATED TOPICS  
---  
Material Data: Plastic Keyword: [OBJTYP (2D)](/docs/sk/keyword_documentation/o/objtyp/), [OBJTYP (3D)](/docs/sk/keyword_documentation/o/objtyp_3d/), [FSTRES](/docs/sk/keyword_documentation/f/fstres/), [TRANS](/docs/sk/keyword_documentation/t/trans/)

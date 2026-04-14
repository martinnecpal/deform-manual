---
lang: sk
title: "TRGVOL (2D)"
---

# TRGVOL

|  (Object data – 2D)  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

TRGVOL Object, Flag, Volume

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Flag |  Volume compensation option  = **0** Active in FEM  = **1** Not used  = **2** Not used |  0  
Volume |  Target volume =**0** Volume compensation is not activated **> 0** Volume compensation is activated with target volume |  0.0  
  
DEFINITION  
---  
TRGVOL enables volume compensation during plastic deformation analysis. For 2D, it can be activated for plain strain, axi-symmetry, or torsion geometry but it cannot be used for plane stress geometry.  
  
REMARKS  
---  
If time increment is large or element size is not small enough to describe the geometry, element loses (or gains for rotational dominated process) volume after the geometry is updated at the end of step. Applicable object types: [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous)  
  
RELATED TOPICS  
---  
[Object Properties](/docs/sk/pre_processor/16_object_properties/16_object_properties/): [Deformation](/docs/sk/pre_processor/16_object_properties/16_1_deformation_properties/) \- [Target Volume](../../pre_processor/16_object_properties/16_1_deformation_properties.htm#16_1_3_Target_Volume_\(TRGVOL\)) Related keywords:[GEOTYP(2D)](/docs/sk/keyword_documentation/g/geotyp/) , [OBJTYP(2D)](/docs/sk/keyword_documentation/o/objtyp/), [OBJTYP(3D)](/docs/sk/keyword_documentation/o/objtyp_3d/)

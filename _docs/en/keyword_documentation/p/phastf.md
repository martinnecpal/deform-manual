---
lang: en
title: "PHASTF (2D3D)"
---

# PHASTF

|  (Inter Material data)  
---|---  
|  Last updated on : 06-08-2014  
  
* * *

PHASTF Mat1, Mat2, Itype

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Mat1 |  Material number 1 |  None  
Mat2 |  Material number 2 |  None  
Itype |  Relation type =**0** no relationship =**1**(mat1 ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) mat2) "full" transformation =**2** (mat1 ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) mat2) "partial" transformation |   
  
DEFINITION  
---  
PHASTF defines the phase relationship between two different phases. When the relation is “1”, the parent phase entirely becomes child. (i.e., Austenite->Pearlite) If equilibrium volume fraction for precipitation is turned on in GUI, the relation type “2” is assigned and a part of parents becomes child (precipitation).  
  
RELATED TOPICS  
---  
Applicable Simulation Modules: Microstructure Applicable [Simulation Modes](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#9.1.5._Simulation_modes_\(SMODE,_TRANS\)): Transformation Applicable [object types](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4._Object_type): ALL except Rigid

---
lang: en
title: "PHASVL (2D3D)"
---

# PHASVL

|  (Inter Material data)  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

PHASVL Mat1, Mat2, IType , N1 N2 or Value

Temp(1) PHASVL(1) or Temp(1) …Temp(Ndata)

Temp(Ndata) PHASVL(Ndata) Atom(1) … Atom(Ndata)

PHASVL(1) …PHASVL(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Mat1 |  Material number 1 |  None  
Mat 2 |  Material number 2 |  None  
IType |  Function type =**0** Constant =**1** Function of temperature =**2** Function of atom content =**3** Function of atom content and temperature |  None  
N1 |  Number of data pairs for function or temperature data when method=3 |   
N2 |  Number of data for atom content when method=3 |   
  
DEFINITION  
---  
PHASVL defines the fractional length change that occurs when material 1 transforms into material 2. This is used to determine the amount of volume change that occurs during transformation. SYSTEM UNITS: (unitless)  
  
REMARKS  
---  
Applicable Simulation Modules: Microstructure Applicable [Simulation Modes](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#9.1.5._Simulation_modes_\(SMODE,_TRANS\)): Transformation Applicable [object types](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4._Object_type): ALL except rigid  
  
RELATED TOPICS  
---  
[Inter-Material Data](/docs/en/pre_processor/10_material_data/10_9_transformation_data/10_9_transformation_data/): [Heat/Volume](../../pre_processor/10_material_data/10_9_transformation_data/10_9_transformation_data.htm#Latent_Heat) Keywords: [PHASLH](/docs/en/keyword_documentation/p/phaslh/)

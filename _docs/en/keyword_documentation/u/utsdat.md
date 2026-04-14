---
lang: en
title: "UTSDAT (2D3D)"
---

# UTSDAT

|  (Inter Material data)  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

UTSDAT Matr, Type, value or Npt

Temp(1) UTSDAT(1)

Temp(Ndata) UTSDAT(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Matr |  Material Number |  None  
Type |  =**0** Constant  =**1** Function of temperature |   
Npt |  Number of data pairs |  None  
  
DEFINITION  
---  
UTSDAT defines the ultimate tensile strength for a material. The ultimate tensile strength of a material is the highest stress point in a stress-strain curve. Also, it can be defined as the stress just prior to necking in a specimen. SYSTEM UNITS: (MPa or Ksi) EXAMPLE Simple example for material group 1 UTSDAT 1 1 3 100 50 200 60 300 80  
  
REMARKS  
---  
It should be noted that the keyword can only be used in the fracture method max (eff stress/UTS), which is object specific. Applicable Simulation Module: Deformation Applicable [Simulation Modes](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#9.1.5._Simulation_modes_\(SMODE,_TRANS\)): Deformation Applicable object types: [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic) and [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic)  
  
RELATED TOPICS  
---  
Material Data: [Fracture Models](/docs/en/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/) Keywords: [FRCMOD](/docs/en/keyword_documentation/f/frcmod/)

---
lang: sk
title: "UNIT (2D3D)"
---

# UNIT

|  (Simulation control)  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

UNIT UnitType

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
UnitType |  Unit system for DEFORM default values = 1 SI units = 2 British units |  1  
  
DEFINITION  
---  
UNIT specifies the unit system for DEFORM default values.  
  
REMARKS  
---  
Any system of units can be used in DEFORM as long as all unit specific variables are consistent. The SI and British unit conventions used for all unit specific DEFORM variables are listed below. Applicable simulation types: Isothermal Deformation Heat Transfer Non-Isothermal Deformation  
  
Variable |  SI Unit |  British Unit |  Conversion Factor SI / Factor = British  
---|---|---|---  
Time |  second |  second |  1.0  
Length |  mm |  in |  25.4  
Area |  mm2 |  in2 |  6.4516 x 102  
Volume |  mm3 |  in3 |  1.6387 x 104  
Force |  N |  klbf |  ?  
Mechanical Energy |  N-mm |  klbf-in |  1.13 x 105  
Stress |  Mpa |  ksi |  6.8918  
Heat Energy |  N-mm |  Btu |  1.055 x 106  
Temperature |  C |  F |  C = (F-31)/1.8  
Conductivity |  N/sec/C |  Btu/sec/in/F |  7.4764 x 104  
Heat Flux |  N/mm/sec |  Btu/in2 |  ?  
Heat Capacity |  N/mm2/C |  Btu/in3/F |  1.1589 x 102  
Radiation Coefficient |  N/sec/mm/K4 |  Btu/sec/in2/F |  1.3182 x 104  
Convection Coefficient |  N/sec/mm/C |  Btu/sec/in2/F |  2.943 x 103  
Interface Heat Transfer Coefficient |  N/sec/mm/C |  Btu/sec/in2/F |  2.943 x 103  
  
RELATED TOPICS  
---  
Simulation Controls: Main Controls, Material Data: Unit Converter

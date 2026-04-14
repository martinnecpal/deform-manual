---
lang: en
title: "LOCTMP (2D3D)"
---

# LOCTMP

|  (Object Data)  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

LOCTMP Object, Iwin, UsrRtn, Ttype, Ctype, Etype, Htype, Itype

Followed by Data

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Iwin |  Heat exchange window index |  None  
UsrRtn |  User routine No. |  None  
Etype |  Type of environmental temperature definition =**0** Constant =**1** Function of time |  None  
Rtype |  Type of convection coefficient =**0** Constant =**1** Function of time =**2** Function of temperature |   
Atype |  Type of emmisivity =**0** Constant =**1** Function of time =**2** Function of temperature |   
Htype |  Type of heat flux =**0** Constant =**1** Function of time |   
Itype |  Type of interface heat transfer coefficient =**0** Inactive (use global definitions such as inter-object data) =**1** Constant =**2** Function of time =**3** Function of pressure |   
  
DEFINITION  
---  
LOCTMP specifies the local heat transfer boundary definition for an object. The keyword should be used if the local heat transfer is specified.  
  
REMARKS  
---  
The keyword defines the heat exchange information such as temperature, convection coefficient, and the radiation view factor for a specific boundary. If the data is of constant type, only the constant value is given in the data list. If tabular data is used to describe any of the above variables, the number of data sets is listed followed by the data set. The following example shows how environmental temperature, emissivity and heat flux are constant and the convection coefficient is a function of temperature. Note the use of comments on the keyword describing the contents. LOCTMP 1 1 0 0 2 0 0 % The keyword definition 68 % The environmental temperature 2 % Number of data sets in convection coefficient 68 0.004 % First data set in the convection coefficient 220 0.006 % Second data set in the convection coefficient .7 % Emissivity 10 % Heat flux When Itye is non-zero, the interface heat transfer coefficient is included in the local boundary condition. The value has higher priority than the interface heat transfer coefficient defined in inter-object data (IHTCOF). Applicable Simulation Modules: Thermal Applicable [Simulation Modes](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#9.1.5._Simulation_modes_\(SMODE,_TRANS\)): Heat Transfer Applicable [Object Types](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4._Object_type): ALL except Rigid  
  
RELATED TOPICS  
---  
[Boundary Conditions](/docs/en/pre_processor/14_boundary_conditions/14_boundary_conditions/): Advanced Thermal Keywords: [ENVTMP](/docs/en/keyword_documentation/e/envtmp/), [IHTCOF (2D)](/docs/en/keyword_documentation/i/ihtcof/), [IHTCOF (3D)](/docs/en/keyword_documentation/i/ihtcof_3d/)

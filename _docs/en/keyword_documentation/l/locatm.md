---
lang: en
title: "LOCATM (2D3D)"
---

# LOCATM

|  (Object Data)  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

LOCATM Object, Iwin, UsrRtn, Etype, Rtype, Atype

Followed by Data

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Iwin |  Heat exchange window index |  None  
UsrRtn |  User routine No. |  None  
Etype |  Type of environmental atom content definition = **0** Constant = **1** Function of time |  None  
Rtype |  Type of reaction rate coefficient =**0** Constant = **1** Function of time = **2** Function of temperature = **3** Function of time and atom |   
Atype |  Type of atom flux = **0** Constant = **1** Function of time |   
  
DEFINITION  
---  
LOCATM specifies the local diffusion boundary definition for an object. The keyword is used to specify the local diffusion boundary condition.  
  
REMARKS  
---  
The keyword defines the heat exchange information such as environmental atom constant, reaction rate coefficient, and the atom flux. If the data is of constant type, only the constant value is given in the data list. If tabular data is used to describe any of the above variables, the number of data sets is listed followed by the data set. The following example shows how environmental atom content and atom flux are constant and the reaction rate coefficient is a function of time. Note the use of comments on the keyword describing the contents. LOCATM 1 1 0 0 1 0 % The keyword definition 0.12 % The environmental atom constant 2 % Number of data in the reaction rate coefficient 1.00 % First data set in the reaction rate coefficient 1.20 % Second data set in the reaction rate coefficient 0.001 % Atom flux Applicable Simulation Modules: Diffusion Applicable Simulation Modes: Heat Transfer Applicable Object Types: ALL except Rigid  
  
RELATED TOPICS  
---  
[Boundary Conditions](/docs/en/pre_processor/14_boundary_conditions/14_boundary_conditions/): Advanced Diffusion Keywords: [ENVATM](/docs/en/keyword_documentation/e/envatm/), [ACVCOF](/docs/en/keyword_documentation/a/acvcof/)

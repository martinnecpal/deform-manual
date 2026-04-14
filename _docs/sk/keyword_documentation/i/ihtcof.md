---
lang: sk
title: "IHTCOF (2D)"
---

# IHTCOF

|  (Inter-object data)  
---|---  
|  Last updated on : 07-08-2013  
  
* * *

IHTCOF Object1, Object2, Ftype, HeatCoeff

or

IHTCOF Object1, Object2, Ftype, Ndata

Time/Press(1), HeatCoeff(1)

: :

Time/Press(Ndata), HeatCoeff(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object1 |  Object number of first object |  None  
Object2 |  Object number of second object |  None  
Ftype |  Function type =**-n** User Routine (n) as described in USRBCC2. = **0** Constant interface heat transfer coefficient = **1** Interface heat transfer coefficient is a function of time = **2** Interface heat transfer coefficient is a function of pressure |  None  
HeatCoeff |  Interface heat transfer coefficient when Ftype = 0 |  None  
Ndata |  Number of Time/Press interface heat transfer coefficient data pairs |  None  
Time/Press(i) |  Time (Ftype = 1), or pressure (Ftype = 2) of ith data pair |  None  
HeatCoeff(i) |  Interface heat transfer coefficient of ith data pair |  None  
  
DEFINITION  
---  
IHTCOF specifies the heat transfer coefficient at the interface between two objects.  
  
REMARKS  
---  
The interface heat coefficient may be specified as a constant, a function of time, user routine or a function of interface pressure. If Ftype = 0, use the operand HeatCoeff. If Ftype = 2 or 3, use the operands Ndata, Time/Press, HeatCoeff(i). When Ftype = 2, each data pair should be provided on a separate line, resulting in Ndata lines of Time/Press(i), HeatCoeff(i). In the case of user routine, the value for the function type should be negative to indicate that it is a user routine. The absolute value refers to the subroutine number that the system will run. It is important to compile a new FEM engine for this method to work properly. For more information about the routine refer to the section on USRBCC2. The interface heat transfer coefficient is generally a complex function determined by the interface pressure, amount of sliding, and interface temperature.  
  
RELATED TOPICS  
---  
[Inter-Object Conditions](/docs/sk/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/): Thermal Keywords: [CNTACT (2D)](/docs/sk/keyword_documentation/c/cntact/), [CNTACT (3D)](/docs/sk/keyword_documentation/c/cntact_3d/), [FRCROT(2D)](/docs/sk/keyword_documentation/f/frcrot/)

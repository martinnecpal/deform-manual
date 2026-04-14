---
lang: en
title: "IHTCOF (3D)"
---

# IHTCOF

|  (Inter-object data)  
---|---  
|  Last updated on : 13-08-2013  
  
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
Ftype |  Function type None = **0** Constant interface heat transfer coefficient = **1** Interface heat transfer coefficient is a function of time = **2** Interface heat transfer coefficient is a function of pressure |   
HeatCoeff |  Interface heat transfer coefficient when Ftype = 0 |   
Ndata |  Number of Time/Press interface heat transfer None coefficient data pairs |   
Time/Press(i) |  Time (Ftype = 1), or pressure (Ftype = 2) of ith data pair |  None  
HeatCoeff(i) |  Interface heat transfer coefficient of ith data pair |  None  
  
DEFINITION  
---  
IHTCOF specifies the heat transfer coefficient at the interface between two objects.  
  
REMARKS  
---  
The interface heat coefficient may be specified as a constant, a function of time, or a function of interface pressure. If Ftype = 0, use the operand HeatCoeff. If Ftype = 2 or 3, use the operands Ndata, Time/Press, HeatCoeff(i). When Ftype = 2, each data pair should be provided on a separate line, resulting in Ndata lines of Time/Press(i), HeatCoeff(i). The interface heat transfer coefficient is generally a complex function determined by the interface pressure, amount of sliding, and interface temperature.  
  
RELATED TOPICS  
---  
[Inter-Object Conditions](/docs/en/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/): Thermal Keywords: [CNTACT (2D)](/docs/en/keyword_documentation/c/cntact/), [CNTACT (3D)](/docs/en/keyword_documentation/c/cntact_3d/)

---
lang: en
title: "FRCROT (2D)"
---

# FRCROT

|  (Inter-Object data - 2D)  
---|---  
_Update History:_ (New definition has been introduced in v10.0) |  Last updated on : 06-08-2013  
  
* * *

FRCROT Object1, Object2, DefType, AngVel

or

FRCROT Object1, Object2, DefType, Ndata

Time/Press(1), AngVel(1)

: :

Time/Press(Ndata), AngVel(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object1 |  Object number of first object |  None  
Object2 |  Object number of second object |  None  
DefType |  Function type None =**0** Constant angular velocity = **1** Angular velocity is a function of time = **2** Angular velocity is a function of pressure |   
AngVel |  Angular velocity Ftype = 0 |   
Ndata |  Number of Time/Press angular velocity data pairs |  None  
Time/Press(i) |  Time (Ftype = 1), or pressure (Ftype = 2) of ith data pair |  None  
AngVel(i) |  Relative angular velocity (radians / unit time) of ith data pair |  None  
  
DEFINITION  
---  
FRCROT specifies the relative angular rotation at the interface between two objects. This enables DEFORM to calculate the heat generation from axisymmetric rotation between two objects.  
  
REMARKS  
---  
The angular velocity may be specified as a constant, a function of time, or a function of interface pressure. If Ftype = 0, use the operand AngVel. If DefType = 1 or 2, use the operands Ndata, Time/Press, AngVel(i). When DefType =1, each data pair should be provided on a separate line, resulting in Ndata lines of Time/Press(i), AngVel(i). Applicable object types: [Rigid](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.5._Rigid), [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
[Inter-Object data](/docs/en/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/): Thermal Keywords: [IHTCOF (2D)](/docs/en/keyword_documentation/i/ihtcof/), [IHTCOF (3D)](/docs/en/keyword_documentation/i/ihtcof_3d/)

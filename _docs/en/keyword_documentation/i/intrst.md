---
lang: en
title: "INTRST (2D3D)"
---

# INTRST

|  (Inter-object data)  
---|---  
_Update History:_ v11.1 – FuncTyp 3 has been introduced. |  Last updated on : 14-05-2016  
  
* * *

INTRST Object1, Object2, FuncTyp, ElcRst/Ndata[Ndata2]

Time/Prs(1), ElcRst(1)

: :

Time/Prs(Ndata), ElcRst(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object1 |  Object number of first object  |  None  
Object2 |  Object number of second object |  None  
FuncTyp |  Function type = **0** Constant electric resistance = **1** Electric resistance is a function of temperature = **2** Electric resistance is a function of pressure = **3** electric resistance is a function of temperature and pressure (new in v11.1) |  None  
ElcRst |  Electric resistance when FrictType = 0 |  0.0  
Ndata |  Number of Time/Prs electric resistance data pairs |  None  
Ndata2 |  Number of Prs electric resistance data pairs |  None  
Time/Prs(i) |  Time (Ftype = 1), or pressure (Ftype = 2) of ith data pair |  None  
ElcRst(i) |  Electric resistance of ith data pair |  None  
  
DEFINITION  
---  
INTRST specifies the electric resistance at the interface between two objects.  
  
REMARKS  
---  
Applicable object types: [Rigid](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.5._Rigid), [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic) and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
[Inter-Object Conditions](/docs/en/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/):Heating Keyword: [CNTACT (2D)](/docs/en/keyword_documentation/c/cntact/), [CNTACT (3D)](/docs/en/keyword_documentation/c/cntact_3d/)

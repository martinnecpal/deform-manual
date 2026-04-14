---
lang: en
title: "SYMSUF (3D)"
---

# SYMSUF

|  (Object Data 3D)  
---|---  
|  Last updated on : 12-08-2013  
  
* * *

SYMSUF Object, SymSufNo, Type

OriginX, OriginY, OriginZ

DirX, DirY, DirZ

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object  |  Object Number |  None  
SymSufNo  |  Symmetric plane No. |  None  
Type  |  Symmetric plane type (not used now) |  None  
OriginX, OriginY, OriginZ |  Coordinates of a point on the plane  |  None  
DirX, DirY, DirZ |  Normal of the plane |   
  
DEFINITION  
---  
SYMSUF specifies a symmetric plane used in defining boundary conditions of a object.  
  
REMARKS  
---  
Applicable object types: [Rigid](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.5._Rigid), [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous)  
  
RELATED TOPICS  
---  
Boundary Constraints: [Symmetry Constraints](/docs/en/pre_processor/14_boundary_conditions/14_1_symmetry_boundary_conditions/) Keywords: [ROTSYM](../r/rotsym_\(3d\).htm)

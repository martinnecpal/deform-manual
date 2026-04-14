---
lang: sk
title: "OBJUPD (3D)"
---

# OBJUPD

|  (Object data)  
---|---  
|  Last updated on : 13-08-2013  
  
* * *

OBJUPD Object, Otype

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object  |  Object Number  |  None  
Otype  |  Object type  = **0** Coordinate update = **1** No coordinate update |  0  
  
DEFINITION  
---  
OBJUPD determines the coordinate handling scheme of rigid object in Lagrangian FEM simulation. When (Otype=1) is used, any rigid objects that have an assigned velocity field has does not update its coordinates. (supported from 3D V6.1)  
  
REMARKS  
---  
When (Otype=1) is used in Lagrangian simulation, the object is stationary as if in ALE simulation. It is efficient for modeling a) moving plate in shape rolling simulation and b) roller in ring rolling simulation. Applicable object types: [Rigid](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.5._Rigid)  
  
RELATED TOPICS  
---  
Simulation Controls: [Simulation Type](/docs/sk/pre_processor/9_simulation_controls/9_1_simulation_type_settings/), [Ring Rolling Wizard](/docs/sk/operation_templates/42_ring_rolling/42_introduction_to_ring_rolling/), [Shape Rolling Wizard](/docs/sk/operation_templates/43_shape_rolling/43_introduction_to_shape_rolling/)

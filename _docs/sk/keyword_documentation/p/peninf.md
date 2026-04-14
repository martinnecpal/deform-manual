---
lang: sk
title: "PENINF (2D3D)"
---

# PENINF

|  (Simulation control)  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

PENINF Penalty

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Penalty |  Interface penalty constant |  1.0E+09  
  
DEFINITION  
---  
PENINF is a large positive constant used to penalize the penetration velocity when a boundary node of one object comes into contact with another object [2].  
  
REMARKS  
---  
PENINF is needed to numerically model physical contact between deforming objects. When a slave and master object come into contact, there is a tendency for nodes from the slave object to penetrate the surface of the master object. PENINF reduces the penetration depth by reducing the penetration velocity [2]. velocitypen = contact pressure/Penalty It is recommended that the interface penalty constant be at least 1000 times the volume penalty constant, PENVOL. Generally the default value of Penalty is satisfactory. Applicable simulation types: Isothermal Deformation Non-Isothermal Deformation  
  
RELATED TOPICS  
---  
Node penetration, [Inter-object contact](/docs/sk/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/) Keywords: [PENVOL (2D)](/docs/sk/keyword_documentation/p/penvol/), [PENVOL (3D)](/docs/sk/keyword_documentation/p/penvol_3d/)

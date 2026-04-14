---
lang: sk
title: "CNTACT (2D)"
---

# CNTACT

|  (Inter object data - 2D)  
---|---  
|  Last updated on : 29-07-2013  
  
* * *

CNTACT Object1, Object2, Relation

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object1 |  Object number of first object |  None  
Object2 |  Object number of second object |  None  
Relation |  Contact relationship between Object1 and Object2  = **0** No contact relationship = **1** Object1 is slave to Object2 = **2** Object1 is master to Object2 |  0  
  
DEFINITION  
---  
CNTACT specifies the contact relationship between two objects.  
  
REMARKS  
---  
When a node from one deformable object contacts the surface of another deformable object, a relationship between the two objects must be established to keep the objects from penetrating each other. This relationship is referred to as a master-slave or slave-master relationship. When two objects are contacting each other, the contact nodes move with the master surface as long as the two objects are in contact. The slave nodes are considered to be in contact with the master object as long as the nodal forces indicate a compressive state. When a slave node develops a tensile force, the node is considered to have separated from the master object. It is recommended that the softer material be assigned to the slave object. If two objects have comparable material strength, either can be the slave object. CNTACT should be specified for every pair of deformable objects that may contact each other during the simulation. If Relation = 0, contact between the two objects is ignored. If contact between the two objects occurs, the objects will penetrate each other. If Relation = 1, Object1 is a slave to Object2 If Relation = 2, Object2 is a master to Object2 Applicable object types: [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous)..  
  
RELATED TOPICS  
---  
[Boundary constraints](/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/), [Inter-object contact](/docs/sk/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/) Keywords: [FRCFAC](/docs/sk/keyword_documentation/f/frcfac/), [IHTCOF(2D)](/docs/sk/keyword_documentation/i/ihtcof/), [IHTCOF(3D)](/docs/sk/keyword_documentation/i/ihtcof_3d/),,[FRCWIN(2D)](/docs/sk/keyword_documentation/f/frcwin/), [FRCWIN(3D)](/docs/sk/keyword_documentation/f/frcwin_3d/), [INTRST](/docs/sk/keyword_documentation/i/intrst/), [WMODEL](/docs/sk/keyword_documentation/w/wmodel/)

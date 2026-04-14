---
lang: en
title: "PENVOL (3D)"
---

# PENVOL

|  (Object Data - 3D)  
---|---  
|  Last updated on : 13-08-2013  
  
* * *

PENVOL Object, VolPenalty

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
VolPenalty |  Volume penalty constant |  1.0e6  
  
DEFINITION  
---  
PENVOL specifies a volume penalty constant that is used to enforce the volume constancy of plastic objects. This can be achieved by a constant or variable PENVOL.  
  
REMARKS  
---  
The volume penalty constant can be determined using PENVOL > 1000 * (average flow stress / average strain rate) The average flow stress can be determined by evaluating the flow stress data ([FSTRES](/docs/en/keyword_documentation/f/fstres/)) at the average values of strain, strain rate, and temperature that the object will experience during the simulation. This value should be used as constant unless convergence problems are experienced, then one must use the variable PENVOL. The volume penalty constant is required for plastic objects. Applicable object types: [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic),  
  
RELATED TOPICS  
---  
Keywords: [AVGSTR](/docs/en/keyword_documentation/a/avgstr/)

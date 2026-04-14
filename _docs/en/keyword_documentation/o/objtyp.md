---
lang: en
title: "OBJTYP (2D)"
---

# OBJTYP

|  (Object data-2D)  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

OBJTYP Object, Otype

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
Otype |  Object deformability type = **0** Undefined = **1** Rigid = **2** Rigid plastic or viscoplastic = **3** Porous = **4** Elastic = **5** Elastoplastic = **6** Read from database (multiple operations only) = **7** User-defined |  None  
  
DEFINITION  
---  
OBJTYP specifies the deformability type of an object.  
  
REMARKS  
---  
Rigid objects are treated as non-deformable materials. Elastic objects are treated as elastically deformable objects. The maximum material stress obtainable with an elastic object is the yield stress of the material. Plastic objects are treated as rigid viscoplastic materials. Plastic objects are assumed to be incompressible. Porous objects are treated the same as plastic objects except that the material density is calculated and updated as part of the simulation. Elastoplastic objects are treated as elastic objects until the yield point is reached. Then, any portions of the object that reach the yield point are treated as plastic, while the remainder of the object is treated as elastic. User defined objects require the user to write a subroutine that defines the constitutive relation for the material. For information on this routine, please refer to the user routines section in the user’s manual. Any combination of object types can be used in a DEFORM simulation. Changing OBJTYP to zero will delete it when a database is written. Option 6 means that upon database generation, the information for that object will be obtained from the previous step in the database. This option is used in multiple operations as a means for carrying objects over from one operation to another. When this option is used, only a select group of settings may be changed in the user interface for this object (e.g. movement controls).  Applicable object types: [Rigid](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.5._Rigid), [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
[Object General Definition](/docs/en/pre_processor/11_general_object_data_definition/11_general_object_data_definition/): Object Type Keywords: [OBJNAM](/docs/en/keyword_documentation/o/objnam/), [PDIE](/docs/en/keyword_documentation/p/pdie/)

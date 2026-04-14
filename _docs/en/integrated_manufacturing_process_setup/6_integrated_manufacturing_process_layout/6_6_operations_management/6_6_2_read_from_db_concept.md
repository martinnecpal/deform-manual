---
lang: en
title: "6.6.2. Read from DB concept"
---

# 6.6.2. Read from DB concept

In multiple operations simulation, user may have to pass the objects along with its state variable history to multiple operations as they are simulated sequentially, in such scenario user can "Read from DB" object type. Once the objects are passed across operations a link between the passed objects across operations is displayed in operation editor. Read from DB concept is the basic idea behind Multiple operations setup and simulation in batch mode or single stretch. The Read from DB object type will read the object data from previous operation last step from the Database before generation of new database by .MST file for the next operation simulation, hence it retains the previous operation state variables history. This object type will reduce interruption after every simulation as in earlier versions preprocessor environment.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_6_operations_management/6_6_2_read_from_db_concept/6_6_2_image001.jpg' | relative_url }})

(a)

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_6_operations_management/6_6_2_read_from_db_concept/6_6_2_image002.jpg' | relative_url }})

(b)

Read from DB object type selection from object window; (a) For 2D (b) For 3D

  
Read from DB object type option is available either in object window (See Fig. 6.6.2.1.) or can also be selected from operation editor context menu option "Pass object to Next operation" or "Pass object to All operation" (See  Fig. 6.6.2.2.). As Pass object option will pass to the next operations these objects object type will be Read from DB only. 

  
![]({{ '/assets/images/integrated_manufacturing_process_setup/6_6_operations_management/6_6_2_read_from_db_concept/6_6_2_image003.jpg' | relative_url }})

Read from DB object type selection by passing the objects from operation editor context menu

  
**Note:**

Read from DB option is not available in first operation object types, as there is no DB is available before first operation.

  
For more information on Connecting operations and passing objects refer the chapter [6.6.1.Connecting Operations.](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_6_operations_management/6_6_1_connecting_operations/)

When user wants to pass objects to Forming operation, user has to select the objects to be passed from previous operations as Forming operation is an open environment. But in guided operations like Heat transfer express, Heat treatment, forming express etc opening the operations will automatically add the objects and object type is set to Read from DB.

In case of heat transfer express operations like Heating and Transfer operation only one object is allowed and if these operations are subsequent operations then selecting them will automatically read the object from previous operation and its object type is set to Read from DB as shown in Fig. 6.6.2.3. Similarly Heat transfer Express - Dwell operation will automatically read all objects from previous operation.

  
![]({{ '/assets/images/integrated_manufacturing_process_setup/6_6_operations_management/6_6_2_read_from_db_concept/6_6_2_image004.jpg' | relative_url }})  
(a) 

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_6_operations_management/6_6_2_read_from_db_concept/6_6_2_image005.jpg' | relative_url }})  
  
(b) 

Object type selection in heat transfer operations, (a) Before opening the Heating Express 2nd operation (transfer operation) (b) After opening the Heating Express 2nd operation (transfer operation)

In case of subsequent forming express operation even though all objects object type is set to Red from DB (See Fig. 6.6.2.4.) by default but still user is allowed to change the dies by selecting the define radio button and defining the object data for dies as shown in Fig. 6.6.2.4b.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_6_operations_management/6_6_2_read_from_db_concept/6_6_2_image006.jpg' | relative_url }})   
(a) 

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_6_operations_management/6_6_2_read_from_db_concept/6_6_2_image007.jpg' | relative_url }})

(b)

Object type selection in forming express operation; (a) Before opening the 2nd operation (b) After opening the 2nd operation

**Related Topics:**

[6.1. Integrated Manufacturing Porcess (MO) Pre-processor Layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_1_integrated_manufacturing_process_preprocessor_layout/)

[6.6.1. Connecting Operations](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_6_operations_management/6_6_1_connecting_operations/)

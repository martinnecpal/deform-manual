---
lang: en
title: "35.2. 3D Heat Transfer Operation"
---

# 35.2. 3D Heat Transfer Operation

35.2.1. How to add Heat Transfer operation

35.2.2. Heat transfer type

35.2.3. Process condition

35.2.4. Simulation controls

35.2.5. Material List

35.2.6. Add objects

35.2.7. Workpiece

  * Geometry

  * Object Mesh

  * Object Material

  * Boundary Conditions

  * Movement Controls

  * Property

  * Initialize

35.2.8. Positioning

35.2.9. Scheduled Positioning

35.2.10. Inter-Object relations

35.2.11. Stopping Controls

35.2.12. Step controls

35.2.13. Generate DB

## How to add 3D Heat Transfer operation

Heat Transfer operation is accessible from MO Wizard that can be opened from Main GUI. Heat Transfer Operation can be added in MO wizard, from explorer tab by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button next to 3D Heat Transfer. Also, user can add by drag and drop into the Operation Editor as shown in Fig. 35.2.1. Combination of heat transfer operations based on the process can be setup in batch/scheduled mode. 

![]({{ '/assets/images/operation_templates/35_heat_transfer/35_2_3d_heat_transfer_operation/image001.jpg' | relative_url }})

Added 3D Heat Transfer operation into operation editor

## Heat transfer type

![]({{ '/assets/images/operation_templates/35_heat_transfer/35_1_2d_heat_transfer_operation/image003.jpg' | relative_url }})

Heat transfer type selection window

There are four types of heat transfer operations available (See Fig. 35.2.2.),

  1. **Heat in Furnace** – Heating workpiece in a furnace

  2. **Transfer through Air** – Transferring workpiece from furnace to press

  3. **Rest on die** – Heat loss while resting on die before the deformation is started

  4. **Dwell on die** – Heat loss while dwelling on die after the deformation is completed

  
For more details about these heating types are described in [35\. Introduction to Heat Transfer operation](/docs/en/operation_templates/35_heat_transfer/35_introduction_to_heat_transfer_operations/), refer Heating Types.

## Process condition

Process conditions like Transfer time (Process duration), Environment temperature and Convection coefficient can be defined in this window as shown in Fig. 35.2.3. Depending on the selection of the heat transfer operation, the default process settings for the respective operation can be loaded which can be changed depending on the user requirement.

![]({{ '/assets/images/operation_templates/35_heat_transfer/35_1_2d_heat_transfer_operation/image004.jpg' | relative_url }})

Process condition settings window

## Simulation controls

The DEFORM system solves time dependent non-linear problems by generating a series of FEM solutions at discrete time increments. At each time increment, the velocities, temperatures, and other key variables of each node in the finite element mesh are determined based on boundary conditions, thermo mechanical properties of the work piece materials and possibly solutions at previous steps. Other state variables are derived from these key values, and updated for each time increment. The length of this time step, and number of steps simulated, are determined based on the information specified in the step controls menu.

In Guided mode simulation controls, user can select Simulation mode type and Output type. Fig. 35.2.5. Shows Guided mode simulation controls. Fig. 35.2.4. Shows Expert mode simulation controls where user can define operation step controls and step definition. The basic options required for setting up heat transfer operation are provided here while Expert mode provides more detailed options.

  
![]({{ '/assets/images/operation_templates/35_heat_transfer/35_2_3d_heat_transfer_operation/image002.jpg' | relative_url }})

Expert mode Simulation controls

![]({{ '/assets/images/operation_templates/35_heat_transfer/35_1_2d_heat_transfer_operation/image005.jpg' | relative_url }})

Guided mode Simulation controls

## Material List

Materials required for the process can be loaded either from library using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) or from DB or Key file using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) as shown in Fig. 35.2.6. User can also add new material and define required data from respective tab by clicking ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button. For more information on Material data definition please refer [10\. Material Data.](/docs/en/pre_processor/10_material_data/10_material_data/)

![]({{ '/assets/images/operation_templates/35_heat_transfer/35_1_2d_heat_transfer_operation/image007.jpg' | relative_url }})

Import Material from Library

## Add objects

User can add required number of objects for the simulation by selecting ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button. Fig. 35.2.7. shows three objects added for a simple Heat transfer operation. 

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image007.jpg' | relative_url }})

Objects Window

## Workpiece

In this page user can define required temperature for the object and select type of the object as shown in Fig. 35.2.8. For workpiece by default the object type selected is Plastic and user can also import object from other DB’s or Keyfile’s using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) option and browsing respective file. 

![]({{ '/assets/images/operation_templates/35_heat_transfer/35_2_3d_heat_transfer_operation/image003.jpg' | relative_url }})

Workpiece window

### Geometry

Geometry window is used to define the geometry of an object as shown in Fig. 35.2.9. Only define primitive field will be in active mode rest other options will be in grayed when no geometry is defined. Once after creating geometry all the options will be activated.

  
User can define new geometry using primitives and also can import the geometry from other file using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) or from library using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}), user can also import geometries in other formats such as .STL,.UNV,.PDA,.GEO and .. Primitives are provided for easy definition of basic geometry shapes. For more information on creating 3D geometries please refer to [12.3. 3D Geometry Data Defining](/docs/en/pre_processor/12_geometry_modelling/12_3_3d_geometry_data_defining/)

![]({{ '/assets/images/operation_templates/35_heat_transfer/35_2_3d_heat_transfer_operation/image004.jpg' | relative_url }})

Geometry window

### Object Mesh

Mesh Page provides options to mesh the object. Guided ![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }}) mode provides option to set number of elements only using slider bar to generate mesh. If the object geometry is complex or user would like to control the mesh density over the object, then user has to switch to expert mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}). Expert mode provides various options like weighing factors, Mesh windows and user defined mode to control the mesh density. Meshing options available in expert mode and Guided more are shown in Fig. 35.2.11. and Fig. 35.2.10. For more detail description of these options, please refer [13.2. 3D Tet Mesh Generation](/docs/en/pre_processor/13_mesh_generation/13_2_3d_tet_mesh_generation/). 

![]({{ '/assets/images/operation_templates/35_heat_transfer/35_2_3d_heat_transfer_operation/image005.jpg' | relative_url }})

Guided mode Mesh option

![]({{ '/assets/images/operation_templates/35_heat_transfer/35_2_3d_heat_transfer_operation/image006.jpg' | relative_url }})

Expert mode mesh option

### Object Material

In material page, all the materials added to material list are displayed (as shown in Fig. 35.2.12.) and user can select the required material to assign to respective object from material list. Also user can load the material in Object material page using Import Material data from a File ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) or Using Load form Library option ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}). 

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image029.jpg' | relative_url }})

Material selection Window

### Boundary Conditions

In Boundary conditions page, user can assign various boundary constraints for an object. Boundary conditions specify how the boundary of an object interacts with other objects and with the environment. The most commonly used boundary conditions are heat exchange with the environment for simulations involving heat transfer. Fig. 35.2.13. shows various BCC that can be assigned to an object in Heat transfer operation.

![]({{ '/assets/images/operation_templates/35_heat_transfer/35_2_3d_heat_transfer_operation/image007.jpg' | relative_url }})

Boundary conditions window

For more information about these BCC's please refer [14\. Boundary Conditions](/docs/en/pre_processor/14_boundary_conditions/14_boundary_conditions/).

### Movement Controls

Movement controls are applied to rigid objects when deformation is turned on in simulation control and movement control is not used for Heat transfer operation.  
For more information about these movement controls please refer [15\. Movement Controls Settings.](/docs/en/pre_processor/15_movement_controls_definition/15_movement_controls_settings/)

###   
Property

Miscellaneous object parameters, which affect either thermo-mechanical behavior of the object or numerical solution behavior are specified in the Object-Properties window. (See Fig. 35.2.14.). For more information, please refer [16\. Object properties](/docs/en/pre_processor/16_object_properties/16_object_properties/).

![]({{ '/assets/images/operation_templates/35_heat_transfer/35_2_3d_heat_transfer_operation/image008.jpg' | relative_url }})

Object property window

### Initialize

In Initialize window, few state variables that are commonly used such as Temperature, strain, stress, damage, velocity, Displacement, etc.., are made available for initialization. User can initialize the values for these state variables by clicking on ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}) button. Fig. 35.2.15. shows the various state variables that are available in Initialize window. Depending on the type of state variable, user can also initialize them from Node and Element data windows (see Fig. 35.2.16. and Fig. 35.2.17.). For more information on how to initialize state variables in Node and Element windows, please refer [17.1 Node data Window](/docs/en/pre_processor/17_object_data_initialization/17_1_node_data_window/) and [17.2. Element data Window](/docs/en/pre_processor/17_object_data_initialization/17_2_element_data_window/).

![]({{ '/assets/images/operation_templates/35_heat_transfer/35_2_3d_heat_transfer_operation/image009.jpg' | relative_url }})

Initialize window

![]({{ '/assets/images/operation_templates/35_heat_transfer/35_2_3d_heat_transfer_operation/image010.jpg' | relative_url }})

Node Data window

![]({{ '/assets/images/operation_templates/35_heat_transfer/35_2_3d_heat_transfer_operation/image011.jpg' | relative_url }})

Element Data window

## Positioning

Below Fig. 35.2.18. shows the positioning window.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image037.jpg' | relative_url }})

Positioning window

**Automatic Positioning** ![]({{ '/assets/icons/pre_icons/mo_automatic_positioning_button.jpg' | relative_url }})

By clicking on this button, system automatically Positions the Objects with respect to the top die movement direction, this option works best for simple setup with three objects work piece, top die and bottom die.

**Positioning Objects**![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }})

By clicking on this button, user can position the objects in required directions. Various types of Positioning Options are available such as [Drag](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_1_Drag_Positioning), [Offset](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_2_Offset_Positioning), [Interference](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_3_Interference_positioning), [Flip](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_6_Flip_positioning) and [Rotational](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_4_Rotational_positioning) as shown in Fig. 35.2.19. For more information about these options, please refer [19\. Object Positioning.](/docs/en/pre_processor/19_object_positioning/19_object_positioning/)

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image038.jpg' | relative_url }})

Object positioning window

## Scheduled Positioning

When user is not sure about the location of an object, scheduled positioning will help to position the objects accurately.  
Schedule positioning allows the user to define the positioning for objects in MO setup for successive operations for which DB is not generated so that the objects are positioned before generation of DB while running simulation in Batch mode.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image039.jpg' | relative_url }})

Scheduled Positioning window

## Inter-Object relations

The purpose of inter-object relations is to define how the different objects in a simulation interact with each other. The relations table shows the current inter object relations that have been defined as shown in Fig. 35.2.21. All objects which may come in contact with each other through the course of the simulation must have a contact relation defined.

**System** : By selecting this radio button, system assigns default inter-object relationships. User can modify values by clicking on "Edit" button.

**User** : By default, user radio button will be selected for Heat transfer operation. User can add relationships by clicking on Add button as shown in Fig. 35.2.21.

For more information please refer, [20\. Inter-Object Relations.](/docs/en/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/)

![]({{ '/assets/images/operation_templates/35_heat_transfer/35_2_3d_heat_transfer_operation/image012.jpg' | relative_url }})

Inter-Object definition window

## Stopping Controls

The stopping parameters determine the process time at which the simulation terminates. A simulation can be terminated based on maximum number of time steps simulated or the maximum process time. A simulation will be stopped when the condition of any of the stopping parameters are met. For more information, please refer [Stopping Controls](../33_forming/33_2_3d_forming_setup.htm#33_2_7_Stopping_Controls) in [3D Forming setup](/docs/en/operation_templates/33_forming/33_2_3d_forming_setup/).

## Step controls

**Number of simulation steps (NSTEP)**

The number of simulation steps parameter defines the number of steps to run from the starting step number. The simulation will stop after this number of simulation steps have run, unless stopping control is triggered to stop the simulation or if the simulation runs into a problem. For example, if the starting step number is -35 (NSTART), and 30 steps (NSTEP) are specified, the simulation will stop after the 65th step, unless another stopping control is triggered first.

**Step increment to save (STPINC)**

The step increment (STPINC) to save in the database controls the number of steps that the system will save in the database. When a simulation runs, every step must be computed, but does not necessarily need to be saved in the database. Storing more steps will preserve more information about the process, consequently it will require more storage space.

  
****

**Step increment control (DSMAX/DTMAX)**

Heat transfer operation solution step size can be controlled by time step. The DEFORM system solves time dependent non-linear problems by generating a series of FEM solutions at discrete time increments. At each time increment, the velocities, temperatures and other key variables of each node in the finite element mesh are determined based on boundary conditions, thermo mechanical properties of the work piece materials and possibly solutions at previous steps. Other state variables are derived from these key values and updated for each time increment. The length of this time step and number of steps simulated are determined based on the information specified in the step controls menu. Fig. 35.2.22. shows the Step definition page in guided mode.

![]({{ '/assets/images/operation_templates/35_heat_transfer/35_1_2d_heat_transfer_operation/image013.jpg' | relative_url }})

Guided Mode Step Definition window

  
Options defined under Step definition page control the numerical behavior of the solution. Expert mode simulation control Main controls details with specifying the simulation title, unit system, geometry type, etc.

[Step](/docs/en/pre_processor/9_simulation_controls/9_1_simulation_type_settings/) and [stopping controls](/docs/en/pre_processor/9_simulation_controls/9_3_stopping_controls/) are used to specify the time step, the total number of steps and the criteria used to terminate the simulation. [Processing conditions](/docs/en/pre_processor/9_simulation_controls/9_6_process_conditions/) like the environment temperature, convection coefficient can be specified here.

For more information and description about options in Simulation controls, Please refer [9\. Simulation Controls.](/docs/en/pre_processor/9_simulation_controls/9_simulation_controls/)

## Generate DB

**Check Data**![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }})****

It checks the Data. If Data is correct we can generate DB. But while checking Data if it gives any errors or warnings then it should be corrected before generating Database. Errors will not allow the database to be generated while warnings will allow the DB to be generated.

**Generate Database![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }})**

By clicking on this button, it generated the Database for the setup.(See Fig. 35.2.23.)

**Append Key file**

Any information that is not defined in the wizard but still applicable to the process can be loaded as .key file. This option is also useful in the cases where only few values needs to be changed then those values can be defined as .key file and only .key file can be changed and simulation can be resubmitted.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image048.jpg' | relative_url }})

Generate DB window

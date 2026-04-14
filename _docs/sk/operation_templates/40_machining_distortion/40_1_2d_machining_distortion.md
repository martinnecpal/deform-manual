---
lang: sk
title: "40.1. 2D Machining Distortion"
---

# 40.1. 2D Machining Distortion

40.1.1. How to add 2D Machining Distortion operation

40.1.2. Object window

40.1.3. Workpiece

  * General

  * Boundary Conditions

  * Initialize

40.1.4. Fixtures

  * General

  * Geometry

40.1.5. Pass

  * General

  * Geometry

40.1.6. Positioning

40.1.7. Scheduled Positioning

40.1.8. Contact

40.1.9. Simulation Preview

40.1.10. Simulation controls

40.1.11. Generate DB

## How to add 2D Machining Distortion operation

2D Machining Distortion operation can be setup in Integrated Manufacturing Process environment that can be accessed from GUI Main. 2D Machining Distortion Operation can be added in MO wizard, from explorer tab by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button next to 2D Machining Distortion. Also, user can add by drag and drop into the Operation Editor as shown in Fig. 40.1.1.

![]({{ '/assets/images/operation_templates/40_machining_distortion/40_1_2d_machining_distortion/image001.jpg' | relative_url }})

Adding 2D Machining Distortion Operation to operation editor

## Object window

Along with workpiece, user can add required number of Fixtures and passes for the simulation by defining the Number of Fixtures and Number of Passes in Objects window. Fig. 40.1.2. shows four fixtures and one pass added for a simple 2D Machining Distortion operation. Then Click ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) to add selected objects to the 2D Machining Distortion operation.(See Fig. 40.1.2.)

![]({{ '/assets/images/operation_templates/40_machining_distortion/40_1_2d_machining_distortion/image002.jpg' | relative_url }})

Object window

## Workpiece

### General 

In this window user can change the workpiece name. For workpiece in Machining Distortion user has to import the object from other DB’s or Key file’s using ![]({{ '/assets/icons/pre_icons/mo_import_object.._button.jpg' | relative_url }}) button, hence user do not have any other option to define Workpiece. If user wants to initialize the displacement to the workpiece, then he can turn on the Initialize displacement check box. (see Fig. 40.1.3.)

![]({{ '/assets/images/operation_templates/40_machining_distortion/40_1_2d_machining_distortion/image003.jpg' | relative_url }})

Workpiece window

### Boundary Conditions

In Boundary conditions window, user can assign boundary constraints for an object. Boundary conditions specify how the boundary of an object interacts with other objects and with the environment. Fig. 40.1.4. shows BCC that can be assigned to workpiece in Machining Distortion. Fixing velocity to arrest the workpiece displacement during machining or applying pressure to hold workpiece are most common BCC required for Machining Distortion.

![]({{ '/assets/images/operation_templates/40_machining_distortion/40_1_2d_machining_distortion/image004.jpg' | relative_url }})

Boundary conditions window

### Initialize

In Initialize window, few state variables that are commonly used such as Temperature, strain, stress, damage, velocity, Displacement, etc.., are made available for initialization.

User can initialize the values for these state variables by clicking on ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}) button. Fig. 40.1.5. shows the various state variables that are available in Initialize window. For more information related to initialize option refer [17\. Object Data Initialize](/docs/sk/pre_processor/17_object_data_initialization/17_object_data_initialize/). 

Depending on the type of state variable, user can also initialize them from Node and Element data windows. For more information on how to initialize state variables in Node and Element windows, please refer [17.1 Node node Window](/docs/sk/pre_processor/17_object_data_initialization/17_1_node_data_window/) and [17.2. Element Data Window](/docs/sk/pre_processor/17_object_data_initialization/17_2_element_data_window/).

![]({{ '/assets/images/operation_templates/40_machining_distortion/40_1_2d_machining_distortion/image005.jpg' | relative_url }})

Initialize Window

## Fixtures

###  General

Fixtures that hold workpiece are defined. Fixtures are considered as rigid objects in this operation. In this window user can change the Fixture name. (See Fig. 40.1.6.)

![]({{ '/assets/images/operation_templates/40_machining_distortion/40_1_2d_machining_distortion/image006.jpg' | relative_url }})

Fixture window

### Geometry

User can define the new geometry by using options from geometry window. Geometry window provides basic options for defining geometry (see Fig. 40.1.7.). Geometry can also be imported using Import geometry from a file ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) option or using Import from Library ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) option. User can also import geometries in other formats such as .DXF and .IGES. Primitives are provided for easy definition of basic geometry shapes. For more information on creating and editing 2D geometries please refer to [12.1. 2D Geometry Data Defining](/docs/sk/pre_processor/12_geometry_modelling/12_1_2d_geometry_data_defining/) and [12.2. 2D Geometry Data Editing](/docs/sk/pre_processor/12_geometry_modelling/12_2_2d_geometry_editing/).

![]({{ '/assets/images/operation_templates/40_machining_distortion/40_1_2d_machining_distortion/image007.jpg' | relative_url }})

Geometry Window

## Pass

### General

From the model point of view, the machining pass information is also a geometry data, which when overlapping with the billet, decides the location and the extent of the material set for removal. Hence this is also a geometry data that can be defined/loaded. In this Window user can change the pass name (see Fig. 40.1.8.).

![]({{ '/assets/images/operation_templates/40_machining_distortion/40_1_2d_machining_distortion/image008.jpg' | relative_url }})

Pass window

### Geometry

User can define the new geometry by using options from geometry window. Geometry Window provides basic options for defining geometry (see Fig. 40.1.9.). Geometry can also be imported using Import geometry from a file ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) option or using Import from Library ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) option. User can also import geometries in other formats such as .DXF and .IGES. Primitives are provided for easy definition of basic geometry shapes. For more information on creating and editing 2D geometries please refer to [12.1. 2D Geometry Data Defining](/docs/sk/pre_processor/12_geometry_modelling/12_1_2d_geometry_data_defining/) and [12.2. 2D Geometry Data Editing](/docs/sk/pre_processor/12_geometry_modelling/12_2_2d_geometry_editing/).

![]({{ '/assets/images/operation_templates/40_machining_distortion/40_1_2d_machining_distortion/image007.jpg' | relative_url }})

Geometry Window

## Positioning

Below Fig. 40.1.10. shows the positioning window.

![]({{ '/assets/images/operation_templates/40_machining_distortion/40_1_2d_machining_distortion/image009.jpg' | relative_url }})

Positioning window

**Automatic Positioning![]({{ '/assets/icons/pre_icons/mo_automatic_positioning_button.jpg' | relative_url }}) :** Auto positioning is used by user to position the rigid objects with workpiece, this option works well for the three objects in forming operation however, user has to review the positioned objects after using the auto positioning in Machining Distortion.

**Positioning Objects![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) : **By clicking on this button, user can position the objects in required directions. Various types of Positioning Options are available such as [Drag](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_1_Drag_Positioning), [Offset](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_2_Offset_Positioning), [Interference](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_3_Interference_positioning), [Flip](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_6_Flip_positioning) and [Rotational](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_4_Rotational_positioning) as shown in Fig. 40.1.11. For more information about these options, please refer [19.Object Positioning](/docs/sk/pre_processor/19_object_positioning/19_object_positioning/).

![]({{ '/assets/images/operation_templates/40_machining_distortion/40_1_2d_machining_distortion/image010.jpg' | relative_url }})

Object positioning window

## Scheduled Positioning

When user is not sure about the location of an object as in case of Read From DB objects and Machining Distortion operation is added in batch mode, scheduled positioning will help to position the objects accurately.

Schedule positioning allows the user to define the positioning for objects in MO setup for successive operations for which DB is not generated so that the objects are positioned before generation of DB while running simulation in Batch mode (see Fig. 40.1.12.)

![]({{ '/assets/images/operation_templates/40_machining_distortion/40_1_2d_machining_distortion/image011.jpg' | relative_url }})

Scheduled positioning window

## Contact

The purpose of inter-object relations is to define how different objects, fixture and workpiece, in a simulation interact with each other. The relations table shows the current inter object relations that have been defined as shown in Fig. 40.1.13. All objects which may come in contact with each other through the course of the simulation must have a contact relation defined. It is very important to define these relationships correctly for a simulation to model a Machining Distortion process accurately. User should note that no inter-object relationship is needed between pass object and the workpiece.

**System** : By selecting this radio button, system assigns default inter-object relationships. Also user can add the lubricants if necessary by selecting Add New from pull down menu and clicking on "Edit" button or user can load the required lubricants from the library for the simulation.

**User** : By default, user radio button will be selected for Machining Distortion operation. User can add relationships by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Add) button as shown in Fig. Fig. 40.1.13.

For more information please refer, [20.Inter-Object Data Definition](/docs/sk/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/).

![]({{ '/assets/images/operation_templates/40_machining_distortion/40_1_2d_machining_distortion/image012.jpg' | relative_url }})

Contact window

## Simulation Preview

Simulation Preview provides an overview of the operation to be executed based on the process definition and pass. In Simulation preview window, by clicking the ![]({{ '/assets/icons/pre_icons/mo_simulation_preview_play_button.jpg' | relative_url }}) button animation would be played and shows the preview of the object with material removed after the pass. (See Fig. 40.1.14.)

![]({{ '/assets/images/operation_templates/40_machining_distortion/40_1_2d_machining_distortion/image013.jpg' | relative_url }})

Simulation preview

## Simulation control

**Number of simulation steps :** The number of simulation steps parameter defines the number of steps to run in Pass and Unloading stages from the starting step number. The simulation will stop after this number of simulation steps have run, unless stopping control is triggered to stop the simulation or if the simulation runs into a problem. Machining Distortion simulation is run in 3 stages,

Stage 1 – Load, loads the operation data and

Stage 2 – Pass, Simulates machining pass

Stage 3 – Unload, Removes the fixtures and simulates spring back.

**Step increment to save :** The step increment ([STPINC](/docs/sk/keyword_documentation/s/stpinc/)) to save in the database controls the number of steps that the system will save in the database. Each step must be saved for machining distortion simulation.

**Step increment control :** Solution step size is controlled by time step. Maximum elapsed process time per step can be defined as 1 sec for Machining distortion operations. Fig. 40.1.15. shows the Simulation Controls in Guided mode.

![]({{ '/assets/images/operation_templates/40_machining_distortion/40_1_2d_machining_distortion/image014.jpg' | relative_url }})

Simulation control in Guided mode

For more information and description about options in Simulation controls, Please refer [9\. Simulation Controls](/docs/sk/pre_processor/9_simulation_controls/9_simulation_controls/).

## Generate DB

In Generate DB page, we can observe the Operation Simulation setup summary. (See Fig. 40.1.16.)

**Generate database![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }})** : By clicking on this button, it generates the Database for the setup.

**Append key file** : Any information that is not defined in the wizard but still applicable to the process can be loaded as .key file. This option is also useful in the cases where only few values needs to be changed then those values can be defined as .key file and only .key file can be changed and simulation can be resubmitted.

![]({{ '/assets/images/operation_templates/40_machining_distortion/40_1_2d_machining_distortion/image015.jpg' | relative_url }})

DB generation window

**Related Topics:**

[2D Machining Distortion Lab](/docs/sk/labs/machining_distortion_labs/2d_machining_distortion_lab1/)

[6.1. Integrated Manufacturing Process Pre- Processor Layout](/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_1_integrated_manufacturing_process_preprocessor_layout/)

[6.2. Integrated Manufacturing Process.Simulation layout](/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_2_integrated_manufacturing_process_simulation_layout/)

[6.3. Integrated Manufacturing Process Post - Processor layout](/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_3_integrated_manufacturing_process_post_layout/)

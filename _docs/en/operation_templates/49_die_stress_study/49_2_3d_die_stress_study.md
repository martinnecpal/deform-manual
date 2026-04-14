---
lang: en
title: "49.2. 3D Die Stress Study"
---

# 49.2. 3D Die Stress Study 

49.2.1. How to add Die stress study for 3D setup

49.2.2. Step selection

49.2.3. Objects window

49.2.4. Object Types

49.2.5. Dies

49.2.5.1. General

49.2.5.2. Geometry

49.2.5.3. Object Mesh

49.2.5.4. Object Material

49.2.5.5. Object boundary conditions

49.2.5.6. Initialize

49.2.5.7. Force Interpolation

49.2.5.8. Fixtures

49.2.6. Controls

49.2.7. Contact

49.2.8. Simulation controls

49.2.9. Generate DB

## How to add Die stress study for 3D setup

Die stress study can be added in MO wizard from the menu listed after clicking the ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button in top left corner (See Fig. 49.2.1.), after adding the die stress study, a new tab is added and die stress operation will be automatically added to the operation editor in the new tab, see Fig. 49.2.2. User can also add multiple die stress study tabs to a single MO project at different steps. 

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_2_3d_die_stress_study/image0001.jpg' | relative_url }})

Adding Die stress study

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_2_3d_die_stress_study/image0002.jpg' | relative_url }})

After adding Die stress study

## Step selection

In the step selection window, the user can select the step number at which die stress analysis should be carried over. Step selection window displays step number along with number of simulations, simulation time, die stroke. User can setup the Die stress analysis for whichever step selected in the step selection window, see Fig. 49.2.3. and Fig. 49.2.4.

  1. **One step** – This option should be selected when the user wants to simulate die stress analysis at one selected step, see Fig. 49.2.3.

     1. **Use selected step** – User can turn on this option for single step die stress study to use the current step loaded from database. Current selected step number will be displayed in parentheses.

     2. **Load step from DB** \- User can turn on this option for single step die stress study to load a different step from nominal database than the current loaded step. As the user selects this option, step selection window will be activated with the steps saved in the nominal database, user can select a step from the steps listed.

  1. **Multiple steps** -This option should be selected when the user wants to simulate die stress analysis of multiple steps selected of an operation, see Fig. 49.2.4.. Currently DEFORM® supports multiple steps die stress analysis only for the steps selected of one operation. Users can add additional Die stress study operations for each operation independently. When we use the multiple steps option, we will be setting up Die stress analysis for the first step of the selected steps and for future steps of die stress analysis we will be scheduling interpolation of forces from workpiece. The object data, simulation controls and other settings will be carried on from the first die stress analysis step. 

     1. **Use selected step** – User can turn on this option to use the current step loaded from database to set up the Die stress study. Current selected step number will be displayed in parentheses.

     2. **Load step from DB** \- User can turn on this option to select different steps from nominal database than the current loaded step. As the user selects this option, step selection window will be activated with the steps saved in the nominal database, user can select different steps from the steps listed. Steps selection can be done using selection options displayed in Fig. 49.2.4.

        1. **Auto** – Use the steps that are selected automatically by the system.

        2. **None** – To deselect all the selected steps so that we can select afresh.

        3. **All** – To select all the steps in the database, please note that currently DEFORM® supports multiple steps die stress analysis only for the steps selected of one operation.

        4. **User- Defined** – Select the steps based on the user requirements, user can use either Increment or Number of steps from range to select the steps.

  * **Increment** \- to select the steps based on the increment value defined.

  * **Number of steps** – System selects the defined number of steps such that they are equally spaced.

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_1_2d_die_stress_study/image0021.jpg' | relative_url }})

One step die stress study step selection window.

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_1_2d_die_stress_study/image0003.jpg' | relative_url }})

Multiple steps die stress study step selection window

## Objects window

User can add required number of additional objects for the simulation by clicking ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button. Fig. 49.2.5. shows the objects passed from nominal operation to die stress operation. User can add necessary fixtures and other components based on the setup.

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_2_3d_die_stress_study/image0004.jpg' | relative_url }})

Objects window

## Object Types

Die stress study supports object types of Rigid and Elastic.

  
Die objects on which the stress output is required are considered as elastic objects. These objects will be meshed and forces are interpolated from Workpiece.

  
Fixture objects on which the stress output is not required are considered as Rigid objects. These objects do not require mesh unless heat transfer calculations are required to be carried out.

## Dies

### General Object window

In this window user can set temperature for the object and select type of the object as shown in Fig. 49.2.6. For dies passed on from nominal setup, object type is selected as Elastic by default. If the user does not want to calculate stresses on the object, then user can select the object type as Rigid. From v13.1.1, two new options have been introduced in the object page to position the dies in future steps, see Fig. 49.2.6.

  
**Die positioning in future steps in multi-step die stress study:**

  
In a multiple step die stress study, if the object requires positioning, then the user needs to choose how the object must be positioned in future steps by turning on the Need positioning check box in object page as shown in Fig. 49.2.6.

  * If the object is part of the nominal setup and requires positioning, then user needs to turn on Need positioning check box and select the respective object from the nominal setup as Following object.

  * If the object is not part of the nominal setup but is within the bounding box of the nominal setup object and requires positioning, then user needs to turn on Need positioning check box and select the respective object from the nominal setup within whose bounding box the current object resides as Following object. We should not turn on the Not original object check box so that force interpolation from the nominal setup can be executed onto the current object.

  * If the object is not part of the nominal setup and is not within the bounding box of the any of the nominal setup objects and requires positioning, then user needs to turn on Need positioning check box and select the object from the nominal setup with which the current object makes contact or follow as Following object. We should also turn on the Not original object checkbox. When user turns on the Not original object check box for an object then the force interpolation will not be executed onto that object.

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_2_3d_die_stress_study/image0005.jpg' | relative_url }})

Object page

### Geometry

User can define the new geometry by using the options from geometry window. Geometry window provides basic options for defining geometry (See Fig. 49.2.7.). Geometry can also be imported using Import geometry from file ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) option or using Import from library ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) option. User can also import geometries in other formats such as .key, .DB, .STL, .PDA, .NAS and .UNV. Primitives are provided for easy definition of basic geometry shapes. For more information on creating and editing 3D geometries please refer to [12.3. 3D Geometry Data Defining](/docs/en/pre_processor/12_geometry_modelling/12_3_3d_geometry_data_defining/).

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_2_3d_die_stress_study/image0006.jpg' | relative_url }})

Geometry window

### Object Mesh

Mesh Page provides options to mesh the object. All the dies on which stresses need to be calculated should be meshed. Mesh page provides option to set number of elements using slider bar to generate mesh. Meshing options available in Guided mode mesh window are shown in Fig. 49.2.8. For more information related to Expert mode mesh option, refer [13.2. 3D Tet Mesh Generation](/docs/en/pre_processor/13_mesh_generation/13_2_3d_tet_mesh_generation/) and [13.3. 3D Brick Mesh Generation](/docs/en/pre_processor/13_mesh_generation/13_3_3d_brick_mesh_generation/)

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_2_3d_die_stress_study/image0007.jpg' | relative_url }})

Mesh window

**Target number of Elements** :The number of elements to be generated for an object can be specified merely by adjusting the slider bar and selecting an appropriate value for the current simulation.

**Generate Mesh** :The mesh can be generated by clicking ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}).

**Delete Mesh:** This feature deletes the generated mesh.

### Object Material

In material window, all the materials inherited from the nominal operation are displayed, users can also load the material required for this operation in Object material window using Import Material data from a file ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }})or using Load form Library option ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}), see Fig. 49.2.9.

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_2_3d_die_stress_study/image0008.jpg' | relative_url }})

Material window

### Object boundary conditions

When we interpolate the forces from billet, forces are applied to dies, this makes the dies to displace erratically during simulation.

To prevent erratic displacement of dies, suitable boundary conditions should be assigned. Velocity BCC can be used to arrest the displacement of dies, see Fig. 49.2.10. Velocity BCC is assigned to top edge of the die is shown in the Fig. 49.2.11\. 

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_2_3d_die_stress_study/image0009.jpg' | relative_url }})

Boundary conditions window

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_2_3d_die_stress_study/image0010.jpg' | relative_url }})

Velocity Boundary conditions assigned in Z direction

**Shrink fit:**  
Shrink Fit BCC in 3D used for die stress analysis, shrink fit conditions are defined between a die insert and a shrink ring. This can be defined by following steps,

**For cylindrical method,**

  * Entering the interference value.

  * Selecting the Direction (Direction perpendicular to the inner surface of the shrink ring or outer surface of the Die insert)

  * Selecting the inner surface of the shrink ring or outer surface of the Die insert (surface which is contact with the die)

**For Surface Perpendicular method,**

  * User has to define the interference value, Deform automatically selects the Direction perpendicular to the surface.

  * Entering the interference value.

  * Selecting the inner surface of the shrink ring or outer surface of the Die insert (surface which is contact with the die)

If shrink fit is applied to the inner object, the value should be negative and If shrink fit is applied to the outer object then the value should be positive.

For more information on shrink fit, Please refer [3D Die Stress Analysis.](/docs/en/operation_templates/30_die_stress/3d_die_stress_analysis_theory/) Fig. 49.2.12. & Fig. 49.2.13. shows shrink fit BCC applied to shrink ring.

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_2_3d_die_stress_study/image0011.jpg' | relative_url }})

Shrink Fit BCC window

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_2_3d_die_stress_study/image0012.jpg' | relative_url }})

Shrink Fit Boundary conditions assigned

### Initialize

In Initialize window, few state variables that are commonly used such as Temperature, strain, stress, damage, velocity, Displacement, etc.., are made available for initialization.

User can initialize the values for these state variables by clicking on ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}) button. Fig. 49.2.14. shows the various state variables that are available in Initialize window. Depending on the type of state variable, user can also initialize them from Node and Element data windows. For more information on how to initialize state variables in Node and Element windows, please refer [17.1. Node Data Window](/docs/en/pre_processor/17_object_data_initialization/17_1_node_data_window/) and [17.2. Element Data Window](/docs/en/pre_processor/17_object_data_initialization/17_2_element_data_window/).

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_2_3d_die_stress_study/image0013.jpg' | relative_url }})

Initialize window

###  Force Interpolation

To interpolate the forces from workpiece object to the dies user need to click on ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}) in Force interpolation window, user can also delete the Interpolated force by using ![]({{ '/assets/icons/pre_icons/mo_delete_interpolate_force_button.jpg' | relative_url }}) option (See Fig. 49.2.15. and Fig. 49.2.16.).

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_2_3d_die_stress_study/image0014.jpg' | relative_url }})

Force Interpolation window

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_2_3d_die_stress_study/image0015.jpg' | relative_url }})

Interpolated Forces

### Fixtures

Fixtures that hold dies can be defined in this operation. Fixtures are considered as rigid objects in this operation. The geometry definition and editing for these objects is similar to that of the dies. The objects require mesh, bcc and material definition when thermal calculations are turned on and these variables can be defined in a similar way to that of the dies.

## Controls

Fig. 49.2.17. shows Controls window, user can position the fixtures and die objects that are added using ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) button. The positioning will be applied only for the current selected step and will not be used in future steps. Various positioning options (See Fig. 49.2.18.) are available to position the objects, for more information on these options please refer [19.Object Positioning.](/docs/en/pre_processor/19_object_positioning/19_object_positioning/)

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_2_3d_die_stress_study/image0016.jpg' | relative_url }})

Controls window

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_2_3d_die_stress_study/image0017.jpg' | relative_url }})

Object Positioning window

## Contact

The purpose of inter-object relations is to define how the different objects in a simulation interact with each other.

In Inter-object window, all the possible relations are already present in the list (See Fig. 49.2.19.). User needs to define the type of relation and Friction value for objects that are in contact for the selected relation. For more information related to expert mode contact page refer [20\. Inter-Object Data Definition](/docs/en/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/).

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_2_3d_die_stress_study/image0018.jpg' | relative_url }})

Inter Object relation window

## Simulation control

**Number of simulation steps:** When the stress analysis is being done on only one tool, a one step simulation is sufficient to get accurate stresses. When the stress analysis is being done on die assemblies where there is interaction between the tools, more than one step is typically needed for the die stack to come to a state of equilibrium under the applied load.

User can turn on thermal calculation by turning on Heat Transfer mode from Expert mode and defining respective thermal BCC from object BCC options and Heat Transfer coefficient values from inter-object window.

**Step increment to save :** The step increment to save in the database controls the number of steps that the system will save in the database. When a simulation runs, every step must be computed, but does not necessarily need to be saved in the database. As the steps that will be simulated for die stress analysis is less, user can store each step.

**Step increment control:** Solution step size is controlled by time step. Maximum elapsed process time per step can be defined as 1 sec for Die stress analysis operations. 

Fig. 49.2.20. shows the Simulation Controls window.

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_2_3d_die_stress_study/image0019.jpg' | relative_url }})

Simulation control window

For more information and description about options in Simulation controls, Please refer [9\. Simulation Controls.](/docs/en/pre_processor/9_simulation_controls/9_simulation_controls/)

## Generate DB

**Check data![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) :** It checks the Data. If Data is correct, we can generate DB. But while checking Data if it gives any errors or warnings then they should be corrected before generating Database. Errors will not allow the database to be generated while warnings will allow the DB to be generated.

**Generate database :** By clicking on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button, it generates the Database for the setup.(See Fig. 49.2.21.).

**Append key file:** Any information that is not defined in the wizard but still applicable to the process can be loaded as .key file. This option is also useful in the cases where only few values needs to be changed then those values can be defined as .key file and only .key file can be changed and simulation can be resubmitted.

![]({{ '/assets/images/operation_templates/49_die_stress_study/49_2_3d_die_stress_study/image0020.jpg' | relative_url }})

DB generation window

**Related Topics:**

[49\. Introduction to Die Stress Study](/docs/en/operation_templates/49_die_stress_study/49_introduction_to_die_stress_study/)

[49.1. 2D Die Stress Study](/docs/en/operation_templates/49_die_stress_study/49_1_2d_die_stress_study/)

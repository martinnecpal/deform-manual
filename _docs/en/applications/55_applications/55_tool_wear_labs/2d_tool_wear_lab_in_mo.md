---
lang: en
title: "2D Tool Wear Lab in MO"
---

# 2D Tool Wear lab in MO

1.1. Problem Summary

1.2. Creating New problem

1.3. Adding 2D Forming operations

1.4. Geometry Type

1.5. Assigning Material for Workpiece

1.6. Adding objects

1.7. Workpiece

1.8. Top Die

1.9. Bottom Die

1.10. Controls

1.11. Contact

1.12. Stopping Controls

1.13. Step controls

1.14. Generating Database

1.15. Starting the Simulation

1.16. Post-Processing the Results

1.17. Remarks on tool life evaluations

## Problem Summary

This lab will demonstrate how to set up the model data for tool wear computations in a typical cold extrusion process. The objective is to understand the tool wear behavior of extrusion die. Tool wear is mainly dictated by process conditions and the materials used. This model illustration assumes that the coefficients used have been calibrated under steady wear conditions for a given process involving a set of die and work piece materials. These coefficients should be used with caution and for qualitative evaluation only when applied to any other process or material conditions. Currently DEFORM® system has Archard’s model and Usui’s model apart from the user routine support. Typically Archard’s model is widely used for forming applications and Usui’s model is used for machining applications to compute insert wear.

Archard’s model can be used with either isothermal or non-isothermal runs. On the other hand, Usui’s model can only be used in non-isothermal mode, as it requires interface temperature calculations as well. For both of these models the die (or insert, in case of machining) should be meshed, with appropriate boundary conditions and inter-object relations defined. This lab will glance through the complete problem setup with emphasis on tool wear part of the data and assumes user is familiar with the typical problem setup procedures.

## Creating New problem

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear, as shown below Fig. 2DTWL1.1.)

![]({{ '/assets/images/applications/55_2_arc_welding/image0001.jpg' | relative_url }})

DEFORM GUI main window

Create a new problem either by selecting **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in Fig. 2DTWL1.2. Select " **I****ntegrated Manufacturing Process** " radio button and units system as "**English** " radio button in units field. Define Problem Name as "******Extrusion_Die_Wear**********" and make sure the “**Show option dialog** ” check box is turned on (if we do not turn on the “Show option dialog” check box, then we will not get the New Project dialog). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

Problem type selection window

MO wizard will open along with project naming window, defined problem name is updated as ‘**Extrusion_Die_Wear** ’ as the project name and selected unit system updated. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to add project.

![]({{ '/assets/images/applications/55_tool_wear_labs/2d_tool_wear_lab_in_mo/image0003.jpg' | relative_url }})

Problem Location selection window

## Adding 2D Forming operations

Multiple Operation wizard will opens with new project called **Extrusion_Die_Wear** to setup the problem. Add 2D Forming operations from Operations list in Explorer. Operation can be added by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button next to 2D Forming operation ( see Fig. 2DTWL1.4.) or user can also add the operation by dragging and dropping the operation into Operation Editor region.

![]({{ '/assets/images/applications/55_tool_wear_labs/2d_tool_wear_lab_in_mo/image0004.jpg' | relative_url }})

Added 2D Forming operation into Operation Editor

## Geometry Type

In this lab we will be using Axisymmetric geometries, So select**2D Axisymmetric** radio button from geometry type page and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Material page. (see Fig. 2DTWL1.5.)

![]({{ '/assets/images/applications/55_tool_wear_labs/2d_tool_wear_lab_in_mo/image0005.jpg' | relative_url }})

2D Axisymmetric Geometry type selection

## Assigning Material for Workpiece

In Material list window, Load the materials '**AISI-1035** , **COLD** ' and '**AISI-D2, COLD** ' from DEFORM Material library using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load material data from library) option (see Fig. 2DTWL1.6.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until object page.

![]({{ '/assets/images/applications/55_tool_wear_labs/2d_tool_wear_lab_in_mo/image0006.jpg' | relative_url }})

Material List window

## Adding objects

For this operation we required three objects, Now by default three objects will be added in Object window. If no objects added in Object window, then add three objects by clicking three times on ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) button (see Fig. 2DTWL1.7.) and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/applications/55_tool_wear_labs/2d_tool_wear_lab_in_mo/image0007.jpg' | relative_url }})

Adding Object Window

## Workpiece

In Workpiece window, select Object type as **Plastic** as shown in Fig. 2DTWL1.8. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/applications/55_tool_wear_labs/2d_tool_wear_lab_in_mo/image0008.jpg' | relative_url }})

Workpiece object Window

### Workpiece Geometry

In Geometry window, load **Tool_Wear_Lab1_Workpiece.GEO** geometry file from library using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load geometry from library) option or can also be imported using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Load geometry from a file) option as shown in Fig. 2DTWL1.9., the geometry is located in DEFORM installation folder \2D\LABS directory.

![]({{ '/assets/images/applications/55_tool_wear_labs/2d_tool_wear_lab_in_mo/image0009.jpg' | relative_url }})

Defining the Geometry

### Mesh generation

Define **2000** elements for the mesh settings and Click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) to generate the mesh (see Fig. 2DTWL1.10.).

![]({{ '/assets/images/applications/55_tool_wear_labs/2d_tool_wear_lab_in_mo/image0010.jpg' | relative_url }})

Workpiece Mesh window

### Assigning Workpiece Material

To assign material for workpiece select the material '**AISI-1035, COLD** ' from material window. This can be done as shown in below Fig. 2DTWL1.11. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/applications/55_tool_wear_labs/2d_tool_wear_lab_in_mo/image0011.jpg' | relative_url }})

Assigning Workpiece material

### Workpiece Boundary conditions

In BCC page, check the default assigned Deformation BCC for Left side of the workpiece in X-Direction, default BCC are assigned automatically due to selection of problem type as axisymmetric (see Fig. 2DTWL1.12.). Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top die page.

![]({{ '/assets/images/applications/55_tool_wear_labs/2d_tool_wear_lab_in_mo/image0012.jpg' | relative_url }})

Workpiece BCC page

## Top Die

In Top die page, select Object type as **Rigid** and **Turn****on****Primary****die****check** box as Top die will have movement definition assigned to it ( see Fig. 2DTWL1.13.) , click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/applications/55_tool_wear_labs/2d_tool_wear_lab_in_mo/image0013.jpg' | relative_url }})

Top die page

### Loading Top die Geometry

In Geometry window, load **Tool_Wear_Lab1_Punch.GEO** geometry file from library using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load geometry from library) option or can also be imported using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Load geometry from a file) option as shown in Fig. 2DTWL1.14..The geometry is located in DEFORM installation folder \2D\LABS directory. Check the geometry using ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) option to make sure the geometry is OK. Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top die movement page.

![]({{ '/assets/images/applications/55_tool_wear_labs/2d_tool_wear_lab_in_mo/image0014.jpg' | relative_url }})

Top Die Geometry page

As we are not performing any tool wear computations on the top die, it is not required to have any mesh in this model.

### Assign Movement to Top Die

Define a **speed** of **11.5** in/sec in**-Y** direction for this lab (see Fig. 2DTWL1.15.). Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Bottom Die page.

![]({{ '/assets/images/applications/55_tool_wear_labs/2d_tool_wear_lab_in_mo/image0015.jpg' | relative_url }})

Top die Movement page

## Bottom Die

In Bottom die page select Object type as **Rigid** and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) (see Fig. 2DTWL1.16.).

![]({{ '/assets/images/applications/55_tool_wear_labs/2d_tool_wear_lab_in_mo/image0016.jpg' | relative_url }})

Bottom Die page

### Loading Bottom Die Geometry

In Geometry window, load **Tool_Wear_Lab1_Die.GEO** geometry file from library using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load geometry from library) option or can also be imported using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Load geometry from a file) option. The geometry is located in DEFORM installation folder \2D\LABS directory. Check the geometry using ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) option to make sure the geometry is OK. Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/applications/55_tool_wear_labs/2d_tool_wear_lab_in_mo/image0017.jpg' | relative_url }})

Bottom Die Geometry Page

### Generating mesh for Bottom Die

Set the target number of elements to **1500** and generate mesh by clicking ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button. (see Fig. 2DTWL1.18.)

![]({{ '/assets/images/applications/55_tool_wear_labs/2d_tool_wear_lab_in_mo/image0018.jpg' | relative_url }})

Bottom Die Mesh page

### Assign Material for Bottom Die

Assign AISI-D2 material for Bottom die by selecting **AISI-D2** in Material list as shown in Fig. 2DTWL1.19. then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/applications/55_tool_wear_labs/2d_tool_wear_lab_in_mo/image0019.jpg' | relative_url }})

Bottom Die Material page

### Defining the material hardness

For tool wear analysis material hardness is an important parameter for the Bottom die. Select ![]({{ '/assets/icons/pre_icons/mo_elemental_data_icon.jpg' | relative_url }}) icon to open Element Data page. Select the ‘**Hardness** ’ option and initialize the element hardness data as **55**(see Fig. 2DTWL1.20.). This value is a typical hardness value in Rockwell-C scale for die steel (as hardened condition).

![]({{ '/assets/images/applications/55_tool_wear_labs/2d_tool_wear_lab_in_mo/image0020.jpg' | relative_url }})

Defining Material Hardness

### Bottom die BCC

Check the default assigned Heat exchange with Environment BCC for Bottom Die and make sure that default assigned Heat Exchange with Environment BCC is assigned to the entire outer surface of the Bottom die (see Fig. 2DTWL1.21.). Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Controls page.

![]({{ '/assets/images/applications/55_tool_wear_labs/2d_tool_wear_lab_in_mo/image0021.jpg' | relative_url }})

Bottom Die BCC page

## Controls

Positioning of the objects is not required in this lab as the imported geometries are already in the correct place.

## Contact

In contact page, we will define friction and heat transfer coefficients for a pair of master-slave objects. Click on ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) to generate default inter-object relations. Default relations will be added as shown in Fig. 2DTWL1.22, now select the **Top Die - Workpiece** relation and click on ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) to set the interface **shear** friction as **0.08** and **interface****heat****transfer****coefficient** as **0.002**. Click on![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close Inter-object data definition window and select the option ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) so that same interface conditions are also applied for the Bottom Die and Workpiece relation. Use ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) icon to determine a suitable contact tolerance and click on ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) option to generate the inter object contact relations. Highlighted nodes indicate the contact nodes between objects.   
In this lab, we will be estimating tool wear on Bottom Die, hence select the **Bottom****Die** \- **Workpiece** relation and click on ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) to define Tool wear data for this pair, scroll to the right (beyond the ‘Friction Window’) option and click on ‘**Tool Wear’** tab as shown in the Fig. 2DTWL1.22 below. Select **Archard** ’s model and input coefficients a = 1, b = 1, c = 2 and k = 0.00001. Please note that these are only some typical values that can be obtained from the literature and user is responsible for accuracy of this data (see Fig. 2DTWL1.22). Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close this window and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Stopping controls page.

![]({{ '/assets/images/applications/55_tool_wear_labs/2d_tool_wear_lab_in_mo/image0022.jpg' | relative_url }})

Contact generation

## Stopping Controls

Under stopping controls, define the **Max****primary****die** stroke as **2** in **-Y** direction.(see Fig. 2DTWL1.23.)

![]({{ '/assets/images/applications/55_tool_wear_labs/2d_tool_wear_lab_in_mo/image0023.jpg' | relative_url }})

Defining Stopping Controls

## Step controls

When we enter the step controls, select ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) icon to go to Expert mode. Select ![]({{ '/assets/icons/pre_icons/mo_simulation_step.jpg' | relative_url }}) tab and specify **150** for total **number****of****steps** and **save****every****10** steps as shown in Fig. 2DTWL1.24.)

Select ![]({{ '/assets/icons/pre_icons/mo_step_increment.jpg' | relative_url }}) tab and define punch stroke per step (DSMAX) as **0.02** in/step (see Fig. 2DTWL1.25.).

Select **Remesh** criteria ![]({{ '/assets/icons/pre_icons/mo_remeshing_criteria.jpg' | relative_url }}) tab and Specify ‘**Remesh****Criteria** ’ of **20** steps for the work piece (see Fig. 2DTWL1.26.).

![]({{ '/assets/images/applications/55_tool_wear_labs/2d_tool_wear_lab_in_mo/image0024.jpg' | relative_url }})

Defining Number of steps

![]({{ '/assets/images/applications/55_tool_wear_labs/2d_tool_wear_lab_in_mo/image0025.jpg' | relative_url }})

Defining step Increment

![]({{ '/assets/images/applications/55_tool_wear_labs/2d_tool_wear_lab_in_mo/image0026.jpg' | relative_url }})

Defining Remesh Criteria

## Generating Database

Once the problem has been completely set up, the last step is to generate a database file. The FEM engine (the part of DEFORM that calculates the solution) uses a database file to store the finite element solutions for the problem. When you generate a database in the DEFORM MO Pre-processor, all of the information defined in the Pre-processor (such as the material properties, movement controls, object geometries, etc.) is transferred to the database file.

In Generate DB page. Click the ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) button to have the program check to see if anything was missed in the problem setup. During the checking process:

Messages in the red color signify data that needs to be fixed before a simulation can be run (such as when you forget to define any material data). 

Click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database. When the program is done writing the database, click on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) tab to run simulation.

## Starting the Simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. 2DTWL1.27. Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/applications/55_tool_wear_labs/2d_tool_wear_lab_in_mo/image0027.jpg' | relative_url }})

Run Simulation window

The progress of the simulation can be monitored as it is running by looking at the Simulation Message and Simulation Graphics in Simulation mode. Click the Simulation Message tab to view the Message file. As long as the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked, which is the default setting, the Message file will refresh every couple of seconds.

The Message file provides information about which simulation step the simulation is currently on and also gives information dealing with how well the simulation is running.

## Post-Processing the Results

  
After simulation has been completed, click on ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) tab, MO post processor will open. (See Fig. 2DTWL1.28.)

Tool wear results can be viewed in post processing as follows. Select the last step of the database and click on the state variable ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) icon. select the **Analysis** Icon to open the Tool wear state variables list, from the list of state variables select Tool Wear, and pick ‘**Wear Depth (Total)** ’ and set display option to solid and scaling option to local. Click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) to plot the same. Zoom the region of interface between Die and Workpiece. Right click on the color bar and set the number of significant digits to 6. The plot displays the wear depth (inches) contours at the end of the process for one part (see Fig. 2DTWL1.28.).

![]({{ '/assets/images/applications/55_tool_wear_labs/2d_tool_wear_lab_in_mo/image0028.jpg' | relative_url }})

Post processing Tool wear models

## Remarks on tool life evaluations

Given the criteria for tool life as a specific wear depth (dictated by the allowable variations in the part dimensions), and wear depth simulated for one part, the tool life in terms of total number of parts produced can be computed. It should be noted that the model results are dictated by the coefficients used in the wear model. Hence these wear model (Archard’s) coefficients (see Fig. 2DTWL1.22.) must be accurately calibrated for a given process and set of materials used.

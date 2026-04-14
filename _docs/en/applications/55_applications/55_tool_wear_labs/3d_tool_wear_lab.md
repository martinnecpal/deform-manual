---
lang: en
title: "3D Tool Wear Lab"
---

# 3D Tool Wear Lab Using Archard’s Model

This lab will demonstrate how to set up the model data for tool wear computations in a typical cold extrusion process. The objective is to understand the tool wear behavior of extrusion punch. Tool wear is mainly dictated by process conditions and materials used. This model illustration assumes that the coefficients used have been calibrated under steady wear conditions for a given process involving a set of die and workpiece materials. These coefficients should be used with caution and for qualitative evaluation only when applied to any other process or material conditions.

Currently DEFORM® system has Archard’s model and Usui’s model apart from the user routine support. Typically, Archard’s model is widely used for forming applications and Usui’s model is used for machining applications to compute insert wear. Archard’s model can be used with either isothermal or non-isothermal runs. While Usui’s model can be used only with non-isothermal run as it requires interface temperature calculations as well. For both models, the die (or insert, in case of machining) should be meshed, with appropriate boundary conditions and inter-object relations defined. This lab will glance through the complete problem setup with emphasis on tool wear part of the data and assumes user is familiar with the typical problem setup procedures.

  
1.1. Creating New Problem

1.2. Adding 3D Forming Operation

1.3. Defining Simulation Controls

1.4. Loading material into Material list

1.5. Adding objects for Forming operation

1.6. Defining Workpiece object

1.7. Defining Punch object

1.8. Defining Die object

1.9. Defining Tool wear and contact conditions

1.10. Defining Step controls

1.11. Generate Database

1.12. Running Simulation

1.13. Post-Processing

## Creating New Problem

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear.

![]({{ '/assets/images/applications/55_tool_wear_labs/3d_tool_wear_lab/image0001.jpg' | relative_url }})

New Problem page.

Create a new problem either by selecting **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear. Select "Integrated Manufacturing Process" radio button and unit system as "**English** " in unit field as shown in Fig. 3DTWL1.1. Define Problem Name as “**3D_Tool_wear** " and make sure the “**Show option dialog** ” check box is turned on (if we do not turn on the “Show option dialog” check box, then we will not get the New Project dialog). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new problem using the Deform Integrated Manufacturing Process.  
  
Multiple operation wizard will open with the New Project dialog, user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session (see Fig. 3DTWL1.2.). In this session we will use “**3D_Tool_wear** ” as the project name. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation. MO wizard will open.

![]({{ '/assets/images/applications/55_tool_wear_labs/3d_tool_wear_lab/image0002.jpg' | relative_url }})

MO Wizard New Project Opening Window.

## Adding 3D Forming operation

Multiple Operation wizard will open, add one 3D Forming operation from Explorer Operations list by clicking ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button as shown in Fig. 3DTWL1.3.

![]({{ '/assets/images/applications/55_tool_wear_labs/3d_tool_wear_lab/image0003.jpg' | relative_url }})

Adding 3D Forming operation into Operation Editor. 

## Defining Simulation Controls

As we add new 3D Forming operation, Simulation controls page will be opened in Property editor. In Simulation controls page, we will be using both Heat transfer and Deformation. So, in Simulation controls turn on both Deformation and Heat transfer the check boxes (See Fig. 3DTWL1.4.). Then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Material page.

![]({{ '/assets/images/applications/55_tool_wear_labs/3d_tool_wear_lab/image0004.jpg' | relative_url }})

Defining Simulation control settings.

## Loading material into Material list

In material list window, using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load from Library) load the material **AISI-1010,COLD[70F(20C)]** under **Steel** Catergory. Similarly, load **AISI-H-13** material under **Die_****Material** catergory. This can be done by clicking ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}) button as shown in Fig. 3DTWL1.5. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to objects page.

![]({{ '/assets/images/applications/55_tool_wear_labs/3d_tool_wear_lab/image0005.jpg' | relative_url }})

Loading Material into Material list.

## Adding Objects for Forming operation

For this lab we need 3 objects, by default 3 objects will be added for Forming operation. If not added by default, then add 3 objects to Objects list using ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) button. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Workpiece (See Fig. 3DTWL1.6.)

![]({{ '/assets/images/applications/55_tool_wear_labs/3d_tool_wear_lab/image0006.jpg' | relative_url }})

Adding Objects in Object window.

## Defining Workpiece object

### Workpiece general object definition

In Workpiece object page, we will keep default object name as “**Workpiece** ”, Temperature as **68** °F and set object type as “**Plastic** ” as shown in Fig. 3DTWL1.7. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Geometry page.

![]({{ '/assets/images/applications/55_tool_wear_labs/3d_tool_wear_lab/image0007.jpg' | relative_url }})

Workpiece general object definition.

### Defining Workpiece Geometry

In Geometry page, import the **Workpiece.geo** file from **/3D/LABS/Tool_Wear** folder. The Workpiece geometry looks like as shown in Fig. 3DTWL1.8. In geometry page, click on ![]({{ '/assets/icons/pre_icons/mo_symmetry_planes_label.jpg' | relative_url }}) and assign symmetry plane on the Workpiece’s X and Y plane as shown in Fig. 3DTWL1.9. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Mesh.

![]({{ '/assets/images/applications/55_tool_wear_labs/3d_tool_wear_lab/image0008.jpg' | relative_url }})

Importing Workpiece Geometry.

![]({{ '/assets/images/applications/55_tool_wear_labs/3d_tool_wear_lab/image0009.jpg' | relative_url }})

Assigning symmetry to Workpiece Geometry.

### Generation Mesh for Workpiece

In mesh page general tab, switch to expert mode using ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) and define the Target number of elements to **25000** and set **size****ratio** to **1.** Click ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button to generate mesh and click “**Yes** ” in “Default Boundary Conditions” pop-up during mesh generation to accept default symmetry BCC based on symmetry definition in geometry. Generated mesh looks like as shown in Fig. 3DTWL1.10. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to assign material.

![]({{ '/assets/images/applications/55_tool_wear_labs/3d_tool_wear_lab/image0010.jpg' | relative_url }})

Mesh settings and generated mesh for Workpiece object.

### Assigning Material to Workpiece

Click on the **AISI-1010,COLD[70F(20C)]** in the Material window to assign the material to Workpiece as shown in Fig. 3DTWL1.11. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top Die object page.

![]({{ '/assets/images/applications/55_tool_wear_labs/3d_tool_wear_lab/image0011.jpg' | relative_url }})

Assigning Material to Workpiece.

## Defining Punch Object

### Punch general object definition

In Top Die page, change the object name to **Punch** and keep Temperature as 68°F and object type as “**Rigid** ” (See Fig. 3DTWL1.12.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Geometry page. 

![]({{ '/assets/images/applications/55_tool_wear_labs/3d_tool_wear_lab/image0012.jpg' | relative_url }})

Punch general object definition.

### Defining Punch Geometry

In Geometry page, import**Punch.geo** from \3D\LABS\Tool_Wear folder as shown in Fig. 3DTWL1.13. using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) option. In geometry page, click on ![]({{ '/assets/icons/pre_icons/mo_symmetry_planes_label.jpg' | relative_url }}) and assign symmetry plane on the Punch’s X and Y plane as shown in Fig. 3DTWL1.14. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Material page.

![]({{ '/assets/images/applications/55_tool_wear_labs/3d_tool_wear_lab/image0013.jpg' | relative_url }})

Importing Punch geometry.

![]({{ '/assets/images/applications/55_tool_wear_labs/3d_tool_wear_lab/image0014.jpg' | relative_url }})

Assigning symmetry to Punch.

### Generating Mesh for Punch

In mesh page general tab, define the target number of elements as **40000** and set size ratio to 3.5. Click ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button to generate mesh and click “**Yes** ” in “Default Boundary Conditions” pop-up during mesh generation to accept default symmetry BCC based on symmetry definition in geometry. Generated mesh looks like as shown in Fig. 3DTWL1.15. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to assign material.

![]({{ '/assets/images/applications/55_tool_wear_labs/3d_tool_wear_lab/image0015.jpg' | relative_url }})

Mesh setting and generated mesh for Punch.

### Assigning Material to Punch

In Material page, click on the **AISI-H-13** in the material window to assign the material to Punch as shown in Fig. 3DTWL1.16. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Movement page.

  
![]({{ '/assets/images/applications/55_tool_wear_labs/3d_tool_wear_lab/image0016.jpg' | relative_url }})

Assigning material to Punch 

### Defining Punch Movement 

In Movement page, by default **speed** radio button is selected with movement direction as **-Z**. Define speed as **1** in/sec constant value as shown in Fig. 3DTWL1.17. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Properties page.

![]({{ '/assets/images/applications/55_tool_wear_labs/3d_tool_wear_lab/image0017.jpg' | relative_url }})

Defining movement for Punch.

### Defining the Punch material hardness

For tool wear analysis material hardness is an important parameter for the Top die. Select ![]({{ '/assets/icons/pre_icons/mo_elemental_data_icon.jpg' | relative_url }}) icon to open Element Data page. Select the ‘**Hardness** ’ option and initialize the element hardness data as **55**(see Fig. 3DTWL1.18.). This value is a typical hardness value in Rockwell-C scale for die steel (as hardened condition). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Bottom Die object page.

![]({{ '/assets/images/applications/55_tool_wear_labs/3d_tool_wear_lab/image0029.jpg' | relative_url }})

Defining Material Hardness

## Defining Die object

### Die general object definition

In Bottom Die object page, change the object name to “**Die** ”, keep Temperature as **68** °F and object type as “**Rigid** ” as shown in Fig. 3DTWL1.19. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Geometry page.

![]({{ '/assets/images/applications/55_tool_wear_labs/3d_tool_wear_lab/image0018.jpg' | relative_url }})

Die general object definition.

### Defining Die Geometry

In Geometry page, import the **Die.geo** file from /3D/LABS/Tool_Wear folder. The Die geometry looks like as shown in Fig. 3DTWL1.20. In geometry page, click on ![]({{ '/assets/icons/pre_icons/mo_symmetry_planes_label.jpg' | relative_url }}) and assign symmetry plane on the Die’s X and Y plane as shown in Fig. 3DTWL1.21. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Mesh page.

![]({{ '/assets/images/applications/55_tool_wear_labs/3d_tool_wear_lab/image0019.jpg' | relative_url }})

Importing Die Geometry.

![]({{ '/assets/images/applications/55_tool_wear_labs/3d_tool_wear_lab/image0020.jpg' | relative_url }})

Assigning symmetry to Die.

### Generating Die Mesh

In Mesh page, and Define Target number of elements as **25000** with size ratio as**2**. Click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button and click “**Yes** ” in “Default Boundary Conditions” pop-up during mesh generation to accept default symmetry BCC based on symmetry definition in geometry. Generated mesh looks like as shown in Fig. 3DTWL1.22. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to assign material.

![]({{ '/assets/images/applications/55_tool_wear_labs/3d_tool_wear_lab/image0021.jpg' | relative_url }})

Mesh settings and generated mesh for Die.

### Assigning Material to Die

In Material page, click on the **AISI-H-13** to assign the material to Die as shown in Fig. 3DTWL1.23. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until contact page.

![]({{ '/assets/images/applications/55_tool_wear_labs/3d_tool_wear_lab/image0022.jpg' | relative_url }})

Assigning Material to Die

### Defining the Die material hardness

Select ![]({{ '/assets/icons/pre_icons/mo_elemental_data_icon.jpg' | relative_url }}) icon to open Element Data page. Select the ‘**Hardness** ’ option and initialize the element hardness data as **55**(see Fig. 3DTWL1.24.). This value is a typical hardness value in Rockwell-C scale for die steel (as hardened condition).

![]({{ '/assets/images/applications/55_tool_wear_labs/3d_tool_wear_lab/image0030.jpg' | relative_url }})

Defining Material Hardness

## Defining Tool wear and contact conditions

The next step will be to generate contact between various objects, where the Punch and Die are master to the Workpiece. So, click on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button 2 times to add two relations. In first relation, select **Punch** as **Master** and **Workpiece** as **Slave** and in second relation, select **Die** as **Master** and **Workpiece** as **Slave** as shown in Fig. 3DTWL1.25. Select the first relation and click on ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) Inter-object data window will be opened, set the interface shear friction as 0.12 in Friction tab and interface heat transfer coefficient as 0.004 in Thermal tab as shown in Fig. 3DTWL1.26.

To define tool wear parameters, click on ‘Tool Wear’ tab, select Archard’s model and define model coefficients as a = 1, b = 1, c = 2 and k = 0.000002 as shown in Fig. 3DTWL1.27. Close the Inter-object data window and click on ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) so that same interface conditions are also applied for the Die and Workpiece relation. Click on ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) magic hat to estimate contact tolerance and then click on ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) to generate contact for all the relationships, Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until step controls.

![]({{ '/assets/images/applications/55_tool_wear_labs/3d_tool_wear_lab/image0023.jpg' | relative_url }})

Adding inter-object relations between objects.

![]({{ '/assets/images/applications/55_tool_wear_labs/3d_tool_wear_lab/image0024.jpg' | relative_url }})

Defining Friction and HTC.

![]({{ '/assets/images/applications/55_tool_wear_labs/3d_tool_wear_lab/image0025.jpg' | relative_url }})

Defining Tool wear model and its values.

## Defining Step Controls

Switch to guided mode using ![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }}). In Step page, define **Number of Simulation steps** as **60** , **Step Increment to save** as **5,** **Die displacement** as Solution step definition type and define **0.006** in/step as constant die displacement shown in Fig. 3DTWL1.28. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Generate Database page.

![]({{ '/assets/images/applications/55_tool_wear_labs/3d_tool_wear_lab/image0026.jpg' | relative_url }})

Defining simulation step controls.

## Generate Database

In Generate DB page, click on ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) button to have the program check to see if anything was missed in the problem setup. During the checking process, messages in the red color signify data that needs to be fixed before a simulation can be run (such as when you forget to define any material data). Click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database.

## Running Simulation

Once the database has been generated, switch to the Simulation mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the operation tree. Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. 3DTWL1.29. Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/applications/55_tool_wear_labs/3d_tool_wear_lab/image0027.jpg' | relative_url }})

Run Simulation window.

  
The progress of the simulation can be monitored as it is running by looking at the Simulation Message tab and Simulation Graphics from the Graphics display region in simulation mode. Make sure ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked in Simulation Message tab, which is the default setting, the Message file will refresh automatically.  
  
The Message file provides information about which simulation step the simulation is currently on and information dealing with how well the simulation is running

## Post-Processing

After simulation has been completed, click on ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) tab to open MO post processor.  
  
Tool wear results can be viewed in post processing as follows. Select the last step of the database and click on the state variable ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) icon. Select the Analysis Icon to open the Tool wear state variables list, from the list of state variables select Tool Wear, and pick ‘Wear Depth (Total)’ and set display option to solid and scaling option to local. Click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) button. The plot displays the wear depth (inches) contours at the end of the process for one part. (see Fig. 3DTWL1.30.)

![]({{ '/assets/images/applications/55_tool_wear_labs/3d_tool_wear_lab/image0028.jpg' | relative_url }})

Tool wear depth (Total) distribution.

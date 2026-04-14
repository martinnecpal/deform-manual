---
lang: en
title: "3D Orbital Movement"
---

# Setting up Orbital Forming operation

  
1.1. Creating New Problem

1.2. Adding 3D Forming Operation

1.3. Simulation Controls settings

1.4. Loading materials into Material list

1.5. Adding Objects

1.6. Defining Workpiece

1.6.1. Workpiece object general definition

1.6.2. Defining Workpiece Geometry

1.6.3. Generating Mesh for Workpiece

1.6.4. Assigning material to Workpiece

1.6.5. Defining boundary conditions for Workpiece

1.7. Defining Top Die

1.7.1. Top Die object general definition

1.7.2. Defining Top Die Geometry

1.7.3. Assign Movement to Top Die

1.8. Defining contact condition

1.9. Defining Step controls

1.10. Generate Database

1.11. Running Simulation

1.12. Post-Processing

## Creating New Problem

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear.

![]({{ '/assets/images/applications/55_2_arc_welding/image0002.jpg' | relative_url }})

New Problem dialog. 

Create a new problem either by selecting **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear. Select "**Integrated Manufacturing Process** " radio button and unit system as "**SI** " in Unit field as shown in Fig. 3DOBML1.1. Define problem Name as “**3D_Orbital_Movement** " and make sure the “Show option dialog” check box is turned on (if we do not turn on the “**Show option dialog** ” check box, then we will not get the New Project dialog in MO UI). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Deform Integrated Manufacturing Process.  
  
Multiple operation wizard will open with the New Project dialog, at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session, in this session we will use “**3D_Orbital_Movement** " as the project name (see Fig. 3DOBML1.2.). Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation

![]({{ '/assets/images/applications/55_orbital_movement/3d_orbital_movement/image0002.jpg' | relative_url }})

.

MO Wizard New Project Opening Window.

## Adding 3D Forming operation

Add **3D****Forming****operation** from Operations list of Explorer by clicking ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button as shown in Fig. 3DOBML1.3.

![]({{ '/assets/images/applications/55_orbital_movement/3d_orbital_movement/image0003.jpg' | relative_url }})

Adding 3D Forming operation into Operation Editor.

## Simulation Controls settings

As we add 3D Forming operation, Simulation controls page will be available in property editor region. In Simulation controls, check the **Deformation****check** box as shown in Fig. 3DOBML1.4. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Material list page.

![]({{ '/assets/images/applications/55_orbital_movement/3d_orbital_movement/image0004.jpg' | relative_url }})

Simulation controls settings.

## Loading materials into Material list 

In Material list page, load the material **AISI-1010 COLD [70F(20C)]** material from Library under Steel category using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load from Library) button. This can be done by clicking ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}) button as shown in Fig. 3DOBML1.5. Click to Objects page.

![]({{ '/assets/images/applications/55_orbital_movement/3d_orbital_movement/image0005.jpg' | relative_url }})

Loading material into Material list.

## Objects selection

In Object page, we can observe 3 objects being added by default. For this lab, we will require only two objects, hence, keep Workpiece and Top Die and delete the Bottom Die object (See Fig. 3DOBML1.6.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Workpiece page. 

![]({{ '/assets/images/applications/55_orbital_movement/3d_orbital_movement/image0006.jpg' | relative_url }})

Selecting require objects.

## Defining Workpiece

### Workpiece object general definition

In Workpiece object, we will keep object name as “Workpiece”, Temperature as **20** °C and object type as “**Plastic** ” as shown in Fig. 3DOBML1.7. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Geometry page. 

![]({{ '/assets/images/applications/55_orbital_movement/3d_orbital_movement/image0007.jpg' | relative_url }})

Workpiece object page.

### Defining Workpiece Geometry

In Geometry page, using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) option import **Workpiece.geo** file from /3D/LABS/Orbital_Movement folder as shown in Fig. 3DOBML1.8. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Mesh page.

![]({{ '/assets/images/applications/55_orbital_movement/3d_orbital_movement/image0008.jpg' | relative_url }})

Imported Workpiece Geometry.

### Generating Mesh for Workpiece

Switch to expert mode using ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}). In mesh page general tab, set the **target****number****of****elements** as **20000** and **size****ratio** as **1**. Click ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button to generate mesh as shown Fig. 3DOBML1.9. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to assign material for Workpiece.

![]({{ '/assets/images/applications/55_orbital_movement/3d_orbital_movement/image0009.jpg' | relative_url }})

Mesh settings and generated mesh for Workpiece

### Assigning material to Workpiece

In Material page, click on **AISI-1010,COLD[70F(20C)]** to assign the material to Workpiece as shown in Fig. 3DOBML1.10. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Boundary conditions page.

![]({{ '/assets/images/applications/55_orbital_movement/3d_orbital_movement/image0010.jpg' | relative_url }})

Assigning material to Workpiece.

### Defining boundary conditions for Workpiece

In Boundary conditions page, select **Velocity** from Deformation tree and select bottom surface of the Workpiece with Direction as “**All** ” as shown in Fig. 3DOBML1.11. Keep Velocity as 0 and click on ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) button to assign fixed velocity BCC on bottom surface of the Workpiece. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top Die object page.

![]({{ '/assets/images/applications/55_orbital_movement/3d_orbital_movement/image0011.jpg' | relative_url }})

Assigning Velocity BCC to Workpiece.

## Defining Top Die

### Top Die object general definition

In Top Die object, we will keep object name as “**Top Die** ”, Temperature as **20** °C and object type as “**Rigid** ” as shown in Fig. 3DOBML1.12. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Geometry page. 

![]({{ '/assets/images/applications/55_orbital_movement/3d_orbital_movement/image0012.jpg' | relative_url }})

Top Die object page.

### Defining Top Die Geometry

In Geometry page, using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) option import**Top_Die.geo** file from /3D/LABS/Orbital_Movement folder as shown in Fig. 3DOBML1.13. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Movement page.

![]({{ '/assets/images/applications/55_orbital_movement/3d_orbital_movement/image0013.jpg' | relative_url }})

Imported Top Die geometry.

### Assign Movement to Top Die

We need to define both translation movement and orbital movement for the Top Die. We will be defining orbital movement for the Top Die by using combination of Rotation 1 and Rotation2 while for translation movement we will use speed.

In Translation tab of Movement page, define constant **speed** as **0.42418** mm/sec with **-Z** direction as shown in Fig. 3DOBML1.14.

![]({{ '/assets/images/applications/55_orbital_movement/3d_orbital_movement/image0014.jpg' | relative_url }})

Defining speed movement.

  
To define orbital movement, select Rotation tab and define,

**Rotation 1** : Define constant angular velocity**-1** rad/sec and for rotation Axis, select other radio button and define **X** as **0.08676828998, Y** as **0****** and **Z** as **0.9962285199** as shown in Fig. 3DOBML1.15.

**Rotation 2:** Define constant angular velocity **0.996** rad/sec and select Z as Axis of rotation as shown in Fig. 3DOBML1.15.   
Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button until Contact page.

![]({{ '/assets/images/applications/55_orbital_movement/3d_orbital_movement/image0015.jpg' | relative_url }})

Defining orbital rotation movement.

## Defining contact condition

In Contact page, select contact type as '**User** ' and click on ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) button, a relationship between the Top Die and Workpiece is added.  
Highlight the **Top Die** \- **Workpiece** relationship and click on ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) button to modify the contact conditions, define **Shear****friction** value of **0.12** in Inter-object data window. After modifying the friction value, close the Inter-object data window and click on ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) button to estimate contact tolerance value. Click on ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) to generate contact and generated contact is as shown in the Fig. 3DOBML1.16. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Step controls page.

![]({{ '/assets/images/applications/55_orbital_movement/3d_orbital_movement/image0016.jpg' | relative_url }})

Initial contact generated between Workpiece and Top Die.

## Defining Step controls

In Step controls page, switch to guided mode using ![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }}) and define Number of Simulation steps as 1000 and Step Increment to save as 50. Select Time as Solution step definition type and define constant value of 0.03 sec/step as step definition as shown in Fig. 3DOBML1.17. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button to Generate database page.

![]({{ '/assets/images/applications/55_orbital_movement/3d_orbital_movement/image0017.jpg' | relative_url }})

Defining Step controls for simulation.

## Generate Database

In Generate database page, click on ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) button to have the program check to see if anything was missed in the problem setup. During the checking process, messages in the red color signify data that needs to be fixed before a simulation can be run (such as when you forget to define any material data).  
  
Click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database.

## Running Simulation

Once the database has been generated, switch to the Simulation mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the operation tree. Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. 3DOBML1.18.. Use the default **Continue Run** option to select “**Continue from the last step** ” (from step -1) option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/applications/55_orbital_movement/3d_orbital_movement/image0018.jpg' | relative_url }})

Run Simulation window.

  
The progress of the simulation can be monitored as it is running by looking at the Simulation Message tab and Simulation Graphics from the Graphics display region in Simulation mode. If ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked in Simulation Message tab, which is the default setting, the Message file will refresh automatically.  
  
The Message file provides information about which simulation step the simulation is currently on and information dealing with how well the simulation is running.

## Post-Processing

When the simulation is completed, review the results by switching to Post mode using the ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) button.  
In Step Browser, click on All button to view all saved steps and plot Effective Strain state variable, the Effective Strain distribution looks like as shown in Fig. 3DOBML1.19.

![]({{ '/assets/images/applications/55_orbital_movement/3d_orbital_movement/image0019.jpg' | relative_url }})

Strain Effective distribution at the last step

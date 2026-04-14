---
lang: sk
title: "Friction Stir Welding Lab"
---

# ALE Friction Stir Welding 

In this lab we will demonstrate how to setup simple ALE friction stir welding operation.

  
1.1. Creating a New Problem

1.2. Adding Operation

1.3. Simulation controls

1.4. Material list

1.5. Object

1.5.1. Workpiece

1.5.1.1. Workpiece geometry

1.5.1.2. Workpiece Mesh

1.5.1.3. Assign Material

1.5.1.4. Initialize Volume fraction

1.5.1.5. Workpiece Boundary Condition

1.5.2. Top Die

1.5.2.1. Import Tool Geometry

1.5.2.2. Tool Movement

1.6. Contact

1.7. Stopping controls

1.8. Step controls

1.9. Generate DB

1.10. Running Simulation

1.11. Post Processing

## Creating a New Problem 

On a Windows machine, go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** v1x.x from the menu. The DEFORM GUI Main window will appear, as shown in Fig. FSWL1.1.

![]({{ '/assets/images/applications/55_2_arc_welding/image0001.jpg' | relative_url }})

QT4 GUI Main window

Create a new problem either by selecting **File**![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in Fig. FSWL1.2. Select " **Integrated Manufacturing Process** " radio button and unit system as "**SI** " radio button in unit field. Define Problem Name as " ****ALE_STIR_WELD**** " and make sure the “**Show option dialog** ” check box is turned on (if we do not turn on the “**Show option dialog** ” check box, then we will not get the New Project dialog in MO UI). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/applications/55_additive_manufacturing_labs/image0002.jpg' | relative_url }})

New Problem page

Multiple operation wizard will open with the New Project dialog, at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session we use "**ALE_STIR_WELD** " as the project name. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

##  Adding Operation

Add 3D Forming operation from the Explorer Operations list. Add the operation by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button available next to 3D Forming or can also be added by drag and drop into the Operation editor (See Fig. FSWL1.3.). When we add the 3D Forming operation, process Window will open by default.

![]({{ '/assets/images/applications/55_friction_stir_welding_lab/image0003.jpg' | relative_url }})

Adding 3D Forming operation

## Simulation controls

Switch to Expert mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) button, under Main settings define Operation name as "**ALE Stir Welding** ", select Simulation Type as "**ALE stir Welding** " and check "**Deformation** ", "**Heat Transfer** "and "**Transformation** " mode check box as shown in Fig. FSWL1.4. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to material page.

![]({{ '/assets/images/applications/55_friction_stir_welding_lab/image0004.jpg' | relative_url }})

Simulation controls - Main Setting (Expert mode)

## Material list

Click on Import material from a file ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) and load "**FS_Weld_Material.key** " from the **/3D/ LABS** folder. Select "**ALUMINUM-2024[570-930F(300-500C)]** " and click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) in Material selection popup. **ALUMINUM-2024[570-930F(300-500C)]** material added in Material list as shown in Fig. FSWL1.5. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Object page.

![]({{ '/assets/images/applications/55_friction_stir_welding_lab/image0005.jpg' | relative_url }})

Loaded Material in Material list

## Object

In this lab we need only two object. So, from the list Keep only two objects and delete the other object. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Workpiece page.

### Workpiece

Keep the default Object name as "**Workpiece** ", Object **Temperature** as **20°C** and Object type as **Plastic**. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Geometry page.

#### Workpiece geometry

In Geometry page, using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) button Import **FS_Weld_Workpiece****.****stl** file from /3D/ LABS folder, After importing any geometry. Use ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) action label to check the Geometry and click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to close Check popup and Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Mesh page.

![]({{ '/assets/images/applications/55_friction_stir_welding_lab/image0006.jpg' | relative_url }})

Workpiece Geometry

#### Workpiece Mesh

In General mesh page, Select "**Absolute** " type and define "**Size ratio** " as**4** and **Minimum****element** **size** as **0.4** mm as shown in Fig. FSWL1.7.

![]({{ '/assets/images/applications/55_friction_stir_welding_lab/image0007.jpg' | relative_url }})

General Mesh page

Click on "**Weighting Factor** " tab, with default Weighting factors keep the **Mesh density window** to **1** as shown in Fig. FSWL1.8.

![]({{ '/assets/images/applications/55_friction_stir_welding_lab/image0008.jpg' | relative_url }})

Weighting Factor Mesh page

Click on "**Mesh Windows** " tab, add three Mesh windows in list by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button. For first window select **Cylinder** type window, click on **Workpiece** to add window on workpiece, click on ![]({{ '/assets/icons/pre_icons/mo_edit_window_icon.jpg' | relative_url }}) button and define the value shown in below window (See Fig. FSWL1.9.), Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close Edit window. Define **Element****size** as **0.4** and window **movement** select Follow **Top****die**.

![]({{ '/assets/images/applications/55_friction_stir_welding_lab/image0009.jpg' | relative_url }})

Defining the data for Window 1

For **second****window** select **Cylinder** type window, click on **Workpiece** to add window on workpiece, click on ![]({{ '/assets/icons/pre_icons/mo_edit_window_icon.jpg' | relative_url }}) button and define the value shown in below Window (See Fig. FSWL1.10.), Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close Edit window. Define **Element****size** as **0.5** and window movement select **Follow****Top****die**.

![]({{ '/assets/images/applications/55_friction_stir_welding_lab/image0010.jpg' | relative_url }})

Defining the data for Window 2

For third window select **Box** type window, click on Workpiece to add window on workpiece, click on ![]({{ '/assets/icons/pre_icons/mo_edit_window_icon.jpg' | relative_url }}) button and define the value shown in below Window (See Fig. FSWL1.11.), Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close Edit window. Define **Element****size** as **0.6**.

![]({{ '/assets/images/applications/55_friction_stir_welding_lab/image0011.jpg' | relative_url }})

Editing the Window 3 data 

Click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) to generate Mesh and click ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}) for Default Boundary condition popup. Generated mesh is as shown in Fig. FSWL1.12. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Material page.

![]({{ '/assets/images/applications/55_friction_stir_welding_lab/image0012.jpg' | relative_url }})

Generated Mesh for Workpiece

#### Assign Material

Assign **ALUMINUM-2024[570-930F(300-500C)**] material for Workpiece.

#### Initialize Volume fraction

For half of the workpiece we will define **P1** phase and for other half we will define **P2** in this lab. So, click on ![]({{ '/assets/icons/pre_icons/mo_elemental_data_icon.jpg' | relative_url }}) access to the element dialog to initialize the volume fraction. On the item list window click ‘**Microstructure** ’ ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ‘**Phase** ’. Then choose ‘**P1** ’ and click on ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}) to the ‘Initialize Element Data’. Type in**1** (See Fig. FSWL1.13.), then click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}), then click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) close the window. 

![]({{ '/assets/images/applications/55_friction_stir_welding_lab/image0013.jpg' | relative_url }})

Initialized P1 phase for whole Workpiece

For half of the workpiece we will initialize the defined P1 phase data to define Phase P2 and then we will define the Phase P2 for the initialized region. Now select Phase P1 Click on**-Z** direction, choose ‘**P1** ’ and click on ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}) to the ‘Initialize Element Data’. Select "**Picking** "option, in picking tool select **Box** window, click on Workpiece to add window on workpiece, click on ![]({{ '/assets/icons/pre_icons/mo_edit_window_icon.jpg' | relative_url }}) button and define the value shown in below Fig. FSWL1.14., Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to close Edit window. Define Value as **0** and click on ![]({{ '/assets/icons/pre_icons/mo_close_button2.jpg' | relative_url }}), then close the window. 

![]({{ '/assets/images/applications/55_friction_stir_welding_lab/image0014.jpg' | relative_url }})

Initialized P1 with 0 value for selected region elements

Choose ‘**P2** ’ and click on ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}) to the ‘Initialize Element Data’. Select "**Picking** "option, in picking tool select **Box** window, click on Workpiece to add window on workpiece, click on ![]({{ '/assets/icons/pre_icons/mo_edit_window_icon.jpg' | relative_url }}) button and define the value shown in below Fig. FSWL1.15., click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to close Edit window. Define Value as **1** and click on ![]({{ '/assets/icons/pre_icons/mo_close_button2.jpg' | relative_url }}), then close the window.

![]({{ '/assets/images/applications/55_friction_stir_welding_lab/image0015.jpg' | relative_url }})

Initialized P2 with 1value for selected region elements

Select P1 and click on ![]({{ '/assets/icons/pre_icons/mo_plot_icon.jpg' | relative_url }}) and observe the Assigned P1 Phase volume fraction (See Fig. FSWL1.16.) and similarly select P2 and click on ![]({{ '/assets/icons/pre_icons/mo_plot_icon.jpg' | relative_url }}) and observe the Assigned P2 Phase volume fraction (See Fig. FSWL1.17.). then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the Element data page. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Boundary condition page.

![]({{ '/assets/images/applications/55_friction_stir_welding_lab/image0016.jpg' | relative_url }})

Assigned P1 Phase volume fraction

![]({{ '/assets/images/applications/55_friction_stir_welding_lab/image0017.jpg' | relative_url }})

Assigned P2 Phase volume fraction

Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close Element data.

#### Workpiece Boundary Condition

Define **Vx=0** to the X direction planes as shown in Fig. FSWL1.18. Similar define **Vy=0** to the Y direction plane and **Vz=0** to the Bottom plane of the workpiece.

![]({{ '/assets/images/applications/55_friction_stir_welding_lab/image0018.jpg' | relative_url }})

Assigned X Velocity for the Workpiece (Vx=0)

By default Heat Exchange with Environment BCC will be assigned for whole object, delete the assigned default Heat Exchange with Environment BCC by selecting "**Defined** " and click on ![]({{ '/assets/icons/pre_icons/mo_delete_bcc_button.jpg' | relative_url }}) button. Now select Top and Bottom plane of the workpiece and assign Heat Exchange with Environment BCC as shown in Fig. FSWL1.19. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top Die page.

![]({{ '/assets/images/applications/55_friction_stir_welding_lab/image0019.jpg' | relative_url }})

Assigned Heat Exchange with Environment BCC

### Top Die

Change the Object **name** as "**Tool** ", Obj**e** ct **Temperature** as **200** and Object Type as **Rigid**. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Geometry page. (See Fig. FSWL1.20.)

![]({{ '/assets/images/applications/55_friction_stir_welding_lab/image0020.jpg' | relative_url }})

Tool General page

#### Import Tool Geometry

In Geometry page, using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) button Import**FS_Weld_Tool.stl** file from /3D/ LABS folder, After importing any geometry. Use ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) action label to check the Geometry and click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to close Check popup and Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Movement page.

#### Tool Movement

Select **Speed** as **Function of time** and movement Direction as **+Y** direction as shown in Fig. FSWL1.21. Click on ![]({{ '/assets/icons/pre_icons/mo_define_function.._button.jpg' | relative_url }}) and define the values as shown in Fig. FSWL1.22.

![]({{ '/assets/images/applications/55_friction_stir_welding_lab/image0021.jpg' | relative_url }})

Tool movement page

![]({{ '/assets/images/applications/55_friction_stir_welding_lab/image0022.jpg' | relative_url }})

Speed Function of time window 

Now click on **Rotation** Tab, Select Rotation1 type as **Angular velocity** , Rotation direction as " **+Z** " and define constant value **157** rad/sec as shown in Fig. FSWL1.23. Click on ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) Calculate center and axis from geometry button. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Contact page.

![]({{ '/assets/images/applications/55_friction_stir_welding_lab/image0023.jpg' | relative_url }})

Tool Rotation - Movement page

## Contact

In Contact page, add two relations by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button. In first relation select **Workpiece** as **Master** and **Slave** to define **self****contact** and for Second relation select **Tool** as **Master** and **Workpiece** as **Slave**. By selecting **Tool - Workpiece** relation click on ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) and define **Shear** as **0.7** and **Heat** **Transfer****Coefficient** as **11** (See Fig. FSWL1.24.). Click the ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) to determine an intelligent contact tolerance. Click ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) to generate contact for all the relationships. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Stopping controls page.

![]({{ '/assets/images/applications/55_friction_stir_welding_lab/image0024.jpg' | relative_url }})

Contact page

## Stopping controls

Switch to Guided mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }}) button, Check **Max****die****stroke****check** **box** and define **20** in **Y** field as shown in Fig. FSWL1.25. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Step page.

![]({{ '/assets/images/applications/55_friction_stir_welding_lab/image0025.jpg' | relative_url }})

Stopping controls

## Step controls

Define **Number****of steps** as **10000** , **Step increment to save** as **100** and **Time per step** as **0.01** as shown in Fig. FSWL1.26.

![]({{ '/assets/images/applications/55_friction_stir_welding_lab/image0026.jpg' | relative_url }})

Step page

Switch to Expert mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) icon, under **Step****increment![]({{ '/assets/icons/pre_icons/mo_step_increment.jpg' | relative_url }}) **tab define **Max****polygon****length** as **0** as shown in Fig. FSWL1.27. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to DB Generation page.

![]({{ '/assets/images/applications/55_friction_stir_welding_lab/image0027.jpg' | relative_url }})

Expert mode - Step Increment page

## Generate DB

Click ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) to see if anything was missed in the setup and then click on the ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database. Observe the message in Message tab informing database generation status.

From v13.1, we need to create DEF_ALESTIR.INI file inside the working directory. So, create a file with the name **DEF_ALESTIR.INI** within the project folder at the level where DB is generated as shown in Fig. FSWL1.28., open with Notepad and enter “0.0” in first line and save.

![]({{ '/assets/images/applications/55_friction_stir_welding_lab/image0028.jpg' | relative_url }})

DEF_ALESTIR.INI file information

## Running Simulation

Once the database has been generated and DEF_ALESTIR.INI is created, switch to the Simulation mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the operation tree. Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. FSWL1.29. Use the default **Continue****Run** option to select “**Continue from the last step** ” (from step -1) option and then select the Simulation mode as **Interactive** radio button. Click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

To define MPI settings, click on ![]({{ '/assets/icons/simulator_icons/mo_more_button.jpg' | relative_url }}) button, Run Options window will expand and displays options to define MPI settings for simulation (max number of processors that can be defined depend on your 3D MPI license).

![]({{ '/assets/images/applications/55_friction_stir_welding_lab/image0029.jpg' | relative_url }})

Run Simulation Window

Monitor the progress of the simulation by looking at the Simulation Message and Simulation Log tab, making sure that the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked. User can view the ALE friction stir welding process as the simulation proceeds to the specified Step definition from Simulation graphics.

## Post Processing

When the simulation is completes, review the results by switching to Post mode using the ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) button above the Simulation tool bar.

Click on **Single** **object** mode ![]({{ '/assets/icons/pre_icons/mo_show_single_obj_icon.jpg' | relative_url }}), click on ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) to plot volume fraction, Under **Micro****Structure** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **Volume****Fraction** , select " **P1** " State variable and click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) to plot and play the animation and observe the **P1** distribution.

![]({{ '/assets/images/applications/55_friction_stir_welding_lab/image0030.jpg' | relative_url }})

Volume Fraction P1 distribution at -1 step

![]({{ '/assets/images/applications/55_friction_stir_welding_lab/image0031.jpg' | relative_url }})

Volume Fraction P1 distribution at last step

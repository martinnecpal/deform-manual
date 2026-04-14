---
lang: en
title: "55 Additive Manufacturing Lab"
---

# Additive Manufacturing Lab

In this lab we will demonstrate how to setup Additive manufacturing process with layer scan model.

  
[1.1. Creating a New Problem ](55_additive_manufacturing.htm#Fig_AML1_QT4_GUI_Main_window#1_1_Creating_a_New_Problem)

[1.2. Adding Forming Operation](55_additive_manufacturing.htm#Fig_AML1_QT4_GUI_Main_window#1_2_Adding_Forming_Operation)

[1.3. Simulation Controls](55_additive_manufacturing.htm#Fig_AML1_QT4_GUI_Main_window#1_3_Simulation_Controls)

1.4. Defining Additive Manufacturing process conditions

1.5. Objects

1.6. Workpiece

1.7. Base plate

1.8. Positioning objects

1.9. Contact

1.10. Stopping controls

1.11. Step controls

1.12. Generate Database

1.13. Preparing Dat files for simulation of Additive Manufacturing

1.14. Running Simulation

1.15. Post Processing

## Creating a New Problem 

On a Windows machine, go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** v1x.x from the menu. The DEFORM GUI Main window will appear, as shown in Fig. AML1.1.

![]({{ '/assets/images/applications/55_2_arc_welding/image0001.jpg' | relative_url }})

QT4 GUI Main window

Create a new problem either by selecting **File**![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in Fig. AML1.2. Select " **Integrated Manufacturing Process** " radio button and unit system as "**SI** " radio button in unit field. Define Problem Name as "**AM_CANTI** " and make sure the “Show option dialog” check box is turned on (if we do not turn on the “**Show option dialog** ” check box, then we will not get the New Project dialog in MO UI). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/applications/55_additive_manufacturing_labs/image0002.jpg' | relative_url }})

New Problem page

Multiple operation wizard will open with the New Project dialog, at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session we will use "**AM_CANTI** " as the project name. 3D Forming operation can also be added in "New Project" dialog by selecting "[3D] Forming" in First operation list and by checking First operation check box. In this lab we will add 3D Forming operation from Explorer operation list, so do not check "First operation" check box in "New Project" dialog. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

## Adding Forming Operation

Add 3D Forming operation from the Explorer Operations list. Add the operation by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button available next to [3D] Forming or can also be added by drag and drop into the Operation editor (See Fig. AML1.3.). When we add the Forming operation, process settings window will open by default.

![]({{ '/assets/images/applications/55_additive_manufacturing_labs/image0003.jpg' | relative_url }})

Adding 3D Forming operation from Explorer

## Simulation Controls

Check "**Deformation** " and "**Heat****Transfer** " **Mode** check box as shown in Fig. AML1.4., 

![]({{ '/assets/images/applications/55_additive_manufacturing_labs/image0004.jpg' | relative_url }})

Simulation Controls (Guided mode)

## Defining Additive Manufacturing process conditions

Additive Manufacturing process conditions can be defined in Advanced Process conditions ![]({{ '/assets/icons/pre_icons/mo_advanced_process_conditions.jpg' | relative_url }}) from Simulation controls in expert mode. In this lab, we will use powder bed, layer by layer scanning with voxel mesh. Same model can be used for line scanning with voxel mesh. In Simulation controls page, switch to Expert mode using ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}). Select Advanced Process conditions ![]({{ '/assets/icons/pre_icons/mo_advanced_process_conditions.jpg' | relative_url }}), under**Additive Manufacturing** tab, enter the following data:

Select **Process****type** as "**Powder****Bed** ",

**Activation****size** as **1** , (Activation size is the radius from heat source center, valid only if heat source trajectory is defined, ) for more information refer[ Fig. AML1.5.]()

**Initial****density** as **1.0,**

**Initial****temperature** as **1000** ° C.

**Deposit****size** as **x** = **0.2** , **y** = **0** and **z** = **0.05**. (unit is mm, x -> deposition width, z -> deposition thickness and y -> not use )

Turn on **Use****voxel****mesh****check****box** and define voxel mesh size as **x** = **10** , **y** = **88** and **z** = **60**. (where x, y and z are revolution (number of elements)), for more information refer Fig. AML1.6.

Define Number of layers as 10, Current layer as 1, Start layer as 1 and End layer as 10 as shown in the Fig. AML1.7. Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until ‘Objects’ page.

![]({{ '/assets/images/applications/55_additive_manufacturing_labs/image0021.jpg' | relative_url }})

Activation size

![]({{ '/assets/images/applications/55_additive_manufacturing_labs/image0022.jpg' | relative_url }})

Voxel mesh

![]({{ '/assets/images/applications/55_additive_manufacturing_labs/image0023.jpg' | relative_url }})

Process Condition - Simulation controls

## Objects

From the list, keep only two objects and delete the other object. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Workpiece page.

## Workpiece

In Workpiece object window select object type as "**Elasto-Plastic** ", change the Workpiece name to "**Canti** " and keep the temperature as **20** °C as shown in the Fig. AML1.8. Select "**Mixed (Tet mesh)** " as element type for Elasto-plastic from drop - down menu. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Geometry.

![]({{ '/assets/images/applications/55_additive_manufacturing_labs/image0005.jpg' | relative_url }})

Workpiece Object definition

### Workpiece Geometry

In Geometry page, using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) button import "**AM_LAB_Canti.geo** " from installation path "**/3D/LABS/** " folder. After importing any geometry, use ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) action label to check the Geometry. A perfect geometry should display message as shown in Fig. AML1.9. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to close Check popup and Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Mesh page.

![]({{ '/assets/images/applications/55_additive_manufacturing_labs/image0006.jpg' | relative_url }})

Workpiece Checking popup

### Workpiece Mesh

We will generate initial mesh with default Target number of Elements **32000** with **Relative** mesh type and **size** **ratio** of **2** (See Fig. AML1.10.). Click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) and click ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}) for Default Boundary condition popup. Click on ![]({{ '/assets/icons/pre_icons/mo_boolean_icon.jpg' | relative_url }}) to generate layered Mesh. 

![]({{ '/assets/images/applications/55_additive_manufacturing_labs/image0007.jpg' | relative_url }})

Generated mesh for Workpiece

### Generating layered mesh

Select **Boolean** type as **Slice****layers** , define Number of layers as **10** , **Normal****direction****as**(**0,0,1**) and **Minimum****element****size** as **0.3** with **size****ratio** as **1** for new mesh after slicing and click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) button. Then meshed object will be sliced and a new mesh will be generated with defined mesh settings, after generation is completed click on ![]({{ '/assets/icons/pre_icons/mo_plot_icon.jpg' | relative_url }}) icon to view the sliced layers and click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button to close the Boolean operation page (See Fig. AML1.11.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Material page.

![]({{ '/assets/images/applications/55_additive_manufacturing_labs/image0008.jpg' | relative_url }})

Generated layered mesh

### Assign Material

In Material Window, click on ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) to load material data from Library and load '**I****N718_machining-AMTC** ' material from '**Superalloy** ' category by clicking ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}) button. Select the added material from window to assign it to the workpiece as shown in Fig. AML1.12. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Boundary condition page.

![]({{ '/assets/images/applications/55_additive_manufacturing_labs/image0009.jpg' | relative_url }})

Assign Material for Workpiece

### Workpiece Boundary condition

We will use the Default **Environment****Temperature** of **20** °C. To assign Heat Change with Environment BCC, select Heat Exchange with Environment, select the entire object surface by clicking on ![]({{ '/assets/icons/pre_icons/mo_select_all_icon.jpg' | relative_url }}) from the picking dialog, then click on ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) to finish the assignment (See Fig. AML1.13.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top die page.

![]({{ '/assets/images/applications/55_additive_manufacturing_labs/image0010.jpg' | relative_url }})

Boundary condition definition for workpiece

## Base plate

In Top die definition window change the object name to **"Base Plate** ", change object temperature to **50** °C and keep the object type as "**Rigid** " as shown in Fig. AML1.14. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Geometry page.

![]({{ '/assets/images/applications/55_additive_manufacturing_labs/image0011.jpg' | relative_url }})

Base plate object definition

### Base Plate Geometry

Using ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) create a **Box** Geometry with **Width**(W) **80mm** , **Length**(L) **80mm** and **Height**(H) **20mm** as shown in Fig. AML1.15. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button to close Primitive page and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Mesh page.

![]({{ '/assets/images/applications/55_additive_manufacturing_labs/image0012.jpg' | relative_url }})

Base plate geometry page

### Base plate Mesh

Generate **Tetrahedral** mesh for the Base Plate with default target number of elements (**32000**) with **Relative** mesh **type** of **size****ratio** **2** , click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) (See Fig. AML1.16.). After mesh generation is completed, click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Material page.

![]({{ '/assets/images/applications/55_additive_manufacturing_labs/image0013.jpg' | relative_url }})

Mesh generation for Base Plate

### Assign Material for Base plate

In Material Window, click on ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) to Load material data from Library and load '**DIN-C15[70-2200F(20-1200C)]** ' material from '**Steel** ' category by clicking ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}) button. Select the added material from window to assign it to the Base plate as shown in Fig. AML1.17. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Boundary condition page.

![]({{ '/assets/images/applications/55_additive_manufacturing_labs/image0014.jpg' | relative_url }})

Assigned material for Base plate

### Base plate Boundary Condition

By default, Heat exchange with environment BCC will be assigned to the Base Plate for whole surface, if not defined click on ![]({{ '/assets/icons/pre_icons/mo_select_all_icon.jpg' | relative_url }}) from the picking dialog to pick all surfaces and then click on ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) to finish the assignment. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Positioning page.

## Positioning page

In the **positioning** page, click the ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) icon, select "**Interference** " as the positioning method select "**Base Plate** " as **Positioning****object** and "**Canti** " as the **Reference** select **+Z** **Axis** as the approach direction and click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) and then ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the positioning dialog, click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Contact page.

## Contact

Select '**User** ' type contact and click on ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) button. It will add the relationship between the Base plate and Canti.

Highlight the **Base plate - Canti** relationship and click the ![]({{ '/assets/icons/pre_icons/mo_edit..._2_button.jpg' | relative_url }}) button to modify the contact conditions, enter **Shear****friction** as **1** and **Heat****transfer****Coefficient** as **0.5** and close the dialog. Turn on **Sticking****condition****Check****box** , click on![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) button to calculate default tolerance value and click ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) to generate contact. Click " **Yes** " For Sticking condition Pop-up, generated contact is as shown in the Fig. AML1.18. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Stopping controls page.

![]({{ '/assets/images/applications/55_additive_manufacturing_labs/image0015.jpg' | relative_url }})

Inter-Object data definition window

## Stopping controls

In stopping controls page, we are in Expert mode if not click ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) button to switch to Expert mode. Define '**Process duration** ' as **200** sec (See Fig. AML1.19.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Step page.

![]({{ '/assets/images/applications/55_additive_manufacturing_labs/image0016.jpg' | relative_url }})

Stopping controls - Expert mode

## Step controls

In Step controls, click on ![]({{ '/assets/icons/pre_icons/mo_main_setting.jpg' | relative_url }}) and check '**Deformation** ' and '**Heat****transfer** ' check box are checked and '**Lagrangian****incremental** ' option is selected as shown in the Fig. AML1.20.

![]({{ '/assets/images/applications/55_additive_manufacturing_labs/image0017.jpg' | relative_url }})

Main settings - Simulation controls

Select ![]({{ '/assets/icons/pre_icons/mo_simulation_step.jpg' | relative_url }}), define **Number****of****Simulation****steps** as **250** and **Step****Increment****to****save** as **10** as shown in Fig. AML1.21.

![]({{ '/assets/images/applications/55_additive_manufacturing_labs/image0018.jpg' | relative_url }})

Simulation Steps - Simulation controls

Select ![]({{ '/assets/icons/pre_icons/mo_step_increment.jpg' | relative_url }}), select **Time** as **Solution****step** definition type and define **constant****time****increment** of **1** sec as shown in Fig. AML1.22.

![]({{ '/assets/images/applications/55_additive_manufacturing_labs/image0019.jpg' | relative_url }})

Step Increment - Simulation controls

Select ![]({{ '/assets/icons/pre_icons/mo_solver_settings.jpg' | relative_url }}), In **Deformation** tab select "**Newton-Raphson** " as Iteration method and "**MUMPS** " as the solver as shown in the Fig. AML1.23. Under **Temperature** tab select "**MUMPS** " solver. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Generate DB page.

![]({{ '/assets/images/applications/55_additive_manufacturing_labs/image0020.jpg' | relative_url }})

Solver settings - Simulation controls

## Generate Database

In '**Generate DB** ' page, click ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) to see if anything was missed in the setup and then click on the ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database. Observe the message in Message tab informing database generation status.

## Preparing Dat files for simulation of Additive Manufacturing

We will see dat file content for Layer-by-Layer scanning and Line scanning methods. We can simulate the additive manufacturing process using one of the dat files. For this lab, we will consider heat source scanning at a speed of 750 mm/sec. From **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Folder option **use open working folder. Explorer will open showing the current project folder and we can observe the generated database file. We need to create dat file and place within this folder, the dat file should always be placed in the folder containing the database to be simulated. For more information related to [DEF_ADDMPARM.DAT](../../../appendices/appendix_xvii_data_files.htm#DEF_ADDMPARM_DAT) file, refer section [ Appendix XVII: Data Files](/docs/en/appendices/appendix_xvii_data_files/).

### Dat file for Layer-by-Layer scanning

Create a file named **DEF_ADDMPARM.DAT** to activate **Layer****scan** model. Define the below data in the **DEF_ADDMPARM****.****DAT** file. 

**2** ******750.0 0.0 0.0** **********0** ******0.0 0.0 0.0** **0.0**  
---  
  
1st Line: 2 -> For Layer-by-Layer scan activation.

2nd Line: 750.0 -> Deposit speed 750mm/sec.

3rd Line: 0 -> We will use Initial Temperature defined in Simulation Control (1,000°C).

4th Line: 0,0,0 -> Since we are using Initial Temperature in line 3, Initial Power input (Power, Efficiency, Laser speed) need not be defined.

5th Line: 0 -> There is no resting time between layers.

### Dat File for Line scanning

For **Linescan** type, user can define the below data in**DEF_ADDMPARM.DAT** file.

**4** ******750.0 0.0 0.0** **********0** ******0.0 0.0 0.0** **0.0**  
---  
  
  
1st Line: 4 -> For Line scan activation

2nd Line: 750.0 -> Deposit speed 750mm/sec.

3rd Line: 0 -> We will use Initial Temperature defined in Simulation Control (1,000°C).

4th Line: 0,0,0 -> Since we are using Initial Temperature in line 3, Initial Power input (Power, Efficiency, Laser speed) need not be defined.

5th Line: 0 -> There is no resting time between layers.

## Running Simulation

Once the database has been generated, switch to the Simulation mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the operation tree. Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. AML1.24. Use the default **Continue Run** option to select “**Continue from the last step** ” (from step -1) option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/applications/55_additive_manufacturing_labs/image0028.jpg' | relative_url }})

Run Simulation Window

Monitor the progress of the simulation by looking at the Simulation Message and Simulation Log tab, making sure that the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked.

## Post Processing

When the simulation is completed, review the results by switching to Post mode using the ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) button above the Simulation tool bar.

Play through the steps of the simulation and look how the Canti part formed layer by layer in additive manufacturing process.

![]({{ '/assets/images/applications/55_additive_manufacturing_labs/image0025.jpg' | relative_url }})

Partially formed Canti part after 40 steps

![]({{ '/assets/images/applications/55_additive_manufacturing_labs/image0026.jpg' | relative_url }})

Partially formed Canti part after 100 steps 

![]({{ '/assets/images/applications/55_additive_manufacturing_labs/image0027.jpg' | relative_url }})

Completely formed Canti part after 200 steps

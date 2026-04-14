---
lang: sk
title: "ALE Shape Rolling Lab2"
---

# ALE Shape Rolling Lab2 (using Boolean Mesh)

  
2.1. Creating a New problem

2.2. Adding Shape Rolling operation

2.3. Set process conditions

2.4. Define Workpiece

2.5. Defining Grooves

2.6. Pass Table

2.7. 3D Setup

2.8. Rolling pass operation

2.9. Stand Table

2.10. Defining Contact Relations

2.11. Simulation Controls

2.12. Generate Database

2.13. Running Simulation

2.14. Post Processing

##  Creating a New problem

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear.

Create a new problem either by selecting **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in Fig. ALEL2.1. Select " **Integrated Manufacturing Process** " radio button and Unit system as "**SI** " using radio button. Define Problem Name as Name as "**MO_ALE_LAB2** " and make sure the “Show option dialog” check box is turned on (if we do not turn on the “Show option dialog” check box, then we will not get the New Project dialog in MO UI). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab2/image0001.jpg' | relative_url }})

Problem type selection window

Multiple operation wizard will open with the New Project dialog as shown in (see Fig. ALEL2.2.), at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session we will use ‘**MO_ALE_LAB2** ’ as the project name. 3D Shape Rolling operation can also be added in "New Project" dialog (see Fig. ALEL2.2.), in this lab we will add Shape rolling operation from Explorer operation list, so do not check "First operation" check box and "Shape Rolling" operation in "New Project" dialog. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

## Adding Shape Rolling operation

Add one Shape Rolling operation from the Explorer Operations list. Operation can be added by clicking on Shape Rolling operation ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button or user can also add by drag and drop into the Operation Editor (see Fig. ALEL2.3.)).

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab2/image0002.jpg' | relative_url }})

MO Wizard with new Project opening window

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab2/image0003.jpg' | relative_url }})

Adding Shape Rolling Operation from explorer

## Set process conditions

Select the rolling type as "Steady-State ALE" and symmetry type as "Full" as we will be setting up complete object. As we are not interested in temperature gradient in rolls, select the "**Workpiece only (non-isothermal)** " option. Define the friction coefficient value as **0.7** and heat transfer coefficient value as **11** as shown in Fig. ALEL2.4. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to WP_CrossSection page.

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab2/image0004.jpg' | relative_url }})

Process page

## Define Workpiece

In WP_CrossSection page, keep the object type as ‘Plastic’ and specify workpiece temperature as 100°C (see Fig. ALEL2.5.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab2/image0005.jpg' | relative_url }})

Workpiece Object Definition

### Create Workpiece Geometry

To create a rectangular bar geometry for workpiece, in Geometry page select ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}). From primitive geometry window select **Bar** and define the parameters

Origin Point = (-50, -42.5), Width W = 100mm and Height H = 85mm and click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close. A rectangular bar will create as shown in Fig. ALEL2.6. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Mesh page.

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab2/image0006.jpg' | relative_url }})

Define Primitive

### Generate Workpiece mesh

Generate the workpiece mesh with default number of elements and settings (see Fig. ALEL2.7.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab2/image0007.jpg' | relative_url }})

Workpiece mesh generation

### Assigning Workpiece material

To assign material for workpiece, select the material ‘AISI-1045’ from material window. This can be done as shown in Fig. ALEL2.8. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to until Groove list page.

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab2/image0008.jpg' | relative_url }})

Assigning material for Workpiece

## Defining Grooves

In Groove List page, we can add grooves by clicking on the ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button. Click ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) once to add one groove (see Fig. ALEL2.9.), we will be using same groove for top and bottom roll.

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab2/image0009.jpg' | relative_url }})

Groove list page

### Defining Groove1

Select the First groove and click on ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}), Roll Groove Primitive page will be opened, select Flat rolls. For roll geometry, Define width (W) as 120, radius (r1) as 5 and Roll Radius (RR) as 100 (see Fig. ALEL2.10.). Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Pass page.

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab2/image0010.jpg' | relative_url }})

Groove Geometry defining

## Pass Table

In pass table, we will assign the groove geometries for top roll.

Under Pass1, select the Groove 1 for Top roll, system will copy the top roll geometry for bottom roll bottom roll if asymmetric rolling check box is not checked.

Define the Roll speed (rpm) as 50, Roll gap (mm) as 80 and Environment temperature as 20C. Leave other settings as default. Use Default Number of sections as 20. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to setup 3D objects for workpiece and Rolls.

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab2/image0011.jpg' | relative_url }})

Pass Table

## 3D Setup

3D Rolls and Workpiece geometry and mesh settings are available in this page to setup 3D models. (See Fig. ALEL2.12.).

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab2/image0013.jpg' | relative_url }})

3D Setup page

### 3D Rolls geometry Setup

Select the ![]({{ '/assets/icons/pre_icons/mo_3d_setup_edit_button.jpg' | relative_url }}) button of 3D rolls geometry, 3D roll geometry settings window will open, In 3D rolls Geometry settings window, define the number of layers for rolls as 72 and select the 'Finer geometry from' option as shown in Fig. ALEL2.13. Click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) button to generate rolls with new settings. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button to close the 3D rolls Geometry settings window.

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab2/image0012.jpg' | relative_url }})

3D Roll Geometry settings page

### 3D Workpiece setup using Boolean mesh method

In this lab we will be using boolean method to generate 3D mesh for workpiece, material from workpiece at the intersection of roll and workpiece will be removed.

Select the ![]({{ '/assets/icons/pre_icons/mo_3d_setup_edit_button.jpg' | relative_url }}) button of 3D Workpiece, 3D Workpiece mesh settings window will open. Select the user radio button for Workpiece Length and define the length as 100mm, Select Meshing method as Boolean, define Number of Layers as 36 and select the finer mesh from 0.333 to 0.6667. Then click on ![]({{ '/assets/icons/pre_icons/mo_generate_3d_mesh_button.jpg' | relative_url }}). Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the Workpiece mesh settings window. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab2/image0014.jpg' | relative_url }})

3D Workpiece mesh settings page

Now save the project and select the Rolling Pass operation in operation editor.

## Rolling pass operation

Select the Rolling Pass operation in the operation editor.

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab2/image0015.jpg' | relative_url }})

Rolling pass operation

## Stand Table

As you select the Rolling Pass operation stand table page will appear as shown in figure. In this lab we will not be using Tables and keep 20°C temperature for Rolls. So click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Contact page.

## Defining Contact Relations

In the Contact relations page, master-slave relations will be automatically added. Define the shear friction as 0.7 and interface heat transfer coefficient as 11 (see Fig. ALEL2.16.). Click the ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) to determine an intelligent contact tolerance and click on ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) button to generate contacts between objects. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button. 

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab2/image0016.jpg' | relative_url }})

Contact Relations generation

## Simulation Controls 

In simulation controls page set Time steps as 5000 for this simulation with a step increment to save as 10 and Time per step as 0.001 sec. From DEFORM v12, ALE steady state convergence stopping criteria option has been added in Step controls, user can define ALE steady state stopping criteria for ALE rolling operation. In this lab we will use default values as shown in Fig. ALEL2.17. , click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to generate DB.

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab2/image0017.jpg' | relative_url }})

Simulation controls 

## Generate Database

In the database generation stage user can check the data required for the analysis and proceed to generate the database (see Fig. ALEL2.18.).

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab2/image0018.jpg' | relative_url }})

Database Generation

## Running Simulation

Once the database has been generated switch to the Simulation mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the operation tree. Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. ALEL2.19. Use the default **Continue****Run** option to select “**Continue from the last step** ” (from step -1) option and then select the Simulation mode as **Interactive** radio button. Click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

To define MPI settings, click on ![]({{ '/assets/icons/simulator_icons/mo_more_button.jpg' | relative_url }}) button, Run Options window will expand and displays options to define MPI settings for simulation (max number of processors that can be defined depend on your 3D MPI license).

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab2/image0019.jpg' | relative_url }})

Run Option dialog

Monitor the progress of the simulation by looking at the Simulation Message and Simulation Log tab, making sure that the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked. User can view the process as the simulation proceeds from Simulation graphics

Simulation will stop after reaching steady state with a below message in Message file.

" PROGRAM STOPPED!

CURRENT ROLLING PASS HAS REACHED STEADY-STATE CONDITIONS "

## Post Processing

After the simulation has completed, click on ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) tab, MO post processor will open (See Fig. ALEL2.20.).

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab2/image0020.jpg' | relative_url }})

MO Post mode

Go to last step, Plot Strain - Effective and Stress Max principal state available and observe the state variable distribution (see Fig. ALEL2.21. and Fig. ALEL2.22. ).

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab2/image0021.jpg' | relative_url }})

Strain - Effective Plot

![]({{ '/assets/images/labs/shape_rolling_labs/ale_shape_rolling_lab2/image0022.jpg' | relative_url }})

Stress Max Principal Plot

---
lang: en
title: "Shape Rolling Lab1"
---

# Shape Rolling Lab1(Lagrangian using Brick mesh)

  
1.1. Creating a New problem

1.2. Adding Shape Rolling operation

1.3. Set process conditions

1.4. Define Workpiece

1.5. Defining Grooves

1.6. Pass Table

1.7. 3D Setup

1.8. Simulation controls

1.9. Rolling pass operation

1.10. Stand Table

1.11. Table back

1.12. Pusher object

1.13. Defining Object Positioning

1.14. Defining Contact Relations

1.15. Simulation Controls page

1.16. Generate Database

1.17. Running Simulation

1.18. Post Processing

## Creating a New problem

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear.

Create a new problem either by selecting **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in Fig. L1.1. Select " **Integrated Manufacturing Process** " radio button and Unit system as "**SI** " using radio button. Define Problem Name as "**Shape_Rolling_Lab1** " and make sure the “**Show option dialog** ” check box is turned on (if we do not turn on the “**Show option dialog** ” check box, then we will not get the New Project dialog in MO UI). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0001.jpg' | relative_url }})

Problem type selection window

Multiple operation wizard will open with the New Project dialog as shown in Fig. L1.2., at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session we will use ‘**Shape_Rolling_Lab1** ’ as the project name. 3D Shape Rolling operation can also be added in "New Project" dialog (see Fig. L1.2.), in this lab we will add Shape rolling operation from Explorer operation list, so do not check "First operation" check box and "Shape Rolling" operation in "New Project" dialog. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation. 

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0002.jpg' | relative_url }})

MO Wizard opening window in MO UI

##  Adding Shape Rolling operation

Add one Shape Rolling operation from the Explorer Operations list. Operation can be added by clicking on Shape Rolling operation ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button or user can also add by drag and drop into the Operation Editor.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0003.jpg' | relative_url }})

Adding Shape Rolling Operation

## Set process conditions

Select the rolling type as "**Lagrangian** " and symmetry type as **Full** as we will be setting up complete object. As we are interested in temperature gradient in rolls also, select the "**Workpiece and rolls (non-isothermal)** " option. Define the friction coefficient value as **0.7** and heat transfer coefficient value as **11** as shown in Fig. L1.4.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0004.jpg' | relative_url }})

Process page

## Define Workpiece

In WP_CrossSection window keep the object type as ‘**Plastic** ’ and specify workpiece temperature as 100°C (see Fig. L1.5.). Other option available at this stage are ‘Import Object’ from another keyword file or database. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0005.jpg' | relative_url }})

Workpiece Object Definition

### Create Workpiece Geometry

To create a rectangular bar geometry for workpiece, in Geometry page select Define Primitive. From primitive geometry window select bar and define the parameters as mentioned below. A rectangular bar is created as shown in Fig. L1.6.

**Origin Point** = (-50, -42.5)

**Width** W = 100mm

**Height** H = 85mm

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0006.jpg' | relative_url }})

Define Primitive

### Generate Workpiece mesh

Generate the workpiece mesh with default number of elements and settings.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0007.jpg' | relative_url }})

Workpiece mesh generation

### Assigning Workpiece material

To assign material for workpiece, select the material ‘AISI-1045’ from material window. This can be done as shown in Fig. L1.8. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Groove list page.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0008.jpg' | relative_url }})

Assigning material for Workpiece

## Defining Grooves

In Groove List page, we can add grooves by clicking on the ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button. Click ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) once to add one groove, we will be using same grove for top and bottom roll.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0009.jpg' | relative_url }})

Groove list page

### Defining Groove1

Select the First groove and click on ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}). Roll Groove Primitive page will be opened, select Flat rolls. For roll geometry, Define width as 120, radius (r1) as 5 and Roll Radius RR as 100 as shown in Fig. L1.10.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0010.jpg' | relative_url }})

Groove Geometry defining

## Pass Table

In pass table, we will assign the groove geometries for top roll and bottom roll.

Turn on the 'Show all rolls (for asymmetric rolling)' check box.

Under Pass1, select the Groove 1 for both Top roll and Bottom roll under Pass 1.

Define the Roll speed (rpm) as 50, Roll gap (mm) as 80 and Roll temperature (C) as 40. Leave other settings as default.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0011.jpg' | relative_url }})

Pass Table

### 2.5d Rolling

In pass table page user can preview the rolling process using 2.5 D simulation only for ALE rolling type, so for this lab click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to 3D setup page.

## 3D Setup

From DEFORM v12, in 3D Setup page we have Pusher **object** options for Lagrangian rolling operation in Stand table page. Now we can create Pusher object using **Object** option or we can just assign **Pusher****BCC** without creating pusher object as shown in Fig. L1.12.

**Object** : When we select Object option, default pusher object geometry will be created similar to workpiece cross section and Pusher object will be added in objects list.

**BCC** : When we select BCC option, for workpiece Pusher BCC will be added in BCC Page and movement page will be added for workpiece to define movement value same as that of Pusher. No pusher object will be added in objects list.

**None** : When we select None option, Pusher object / Pusher BCC will not be added to the operation.

**Auto position:** using this option, Workpiece will be interference positioned with Top roll in Movement direction and Pusher will be interference positioned with Workpiece in Movement direction.

In this lab select **Object** option for **Pusher**.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0012.jpg' | relative_url }})

3D Setup page

### 3D Roll geometry setup

Select the ![]({{ '/assets/icons/pre_icons/mo_3d_setup_edit_button.jpg' | relative_url }}) button of 3D Rolls geometry. 3D Rolls geometry settings page will open, in 3D rolls Geometry settings page, define the number of layers as 72 and select the 'Uniform geometry generation'. Then click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button to close the 3D rolls Geometry settings window.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0013.jpg' | relative_url }})

3D Roll Geometry settings page

### 3D Roll mesh settings

Click on ![]({{ '/assets/icons/pre_icons/mo_3d_setup_edit_button.jpg' | relative_url }}) button of 3D roll mesh, 3D roll mesh window will be opened with settings for 3D roll mesh. Define **number of revolved sections** for rolls as **72** using the “**Uniform mesh generation** ” option and import the die material ‘**AISI-H-13** ’ from material library to assign to rolls as shown in Fig. L1.14\. Click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) button to generate mesh for rolls with defined settings and assign material. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button to close the 3D roll mesh window.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0038.jpg' | relative_url }})

3D Roll mesh settings page

### 3D Workpiece setup using Brick mesh

Click on ![]({{ '/assets/icons/pre_icons/mo_3d_setup_edit_button.jpg' | relative_url }}) button of 3D Workpiece mesh, Mesh window with 3D Workpiece mesh settings will be opened. Select user radio button for Workpiece Length and define the length as 600mm, select Birck mesh radio button and define Number of Layers as 120, as shown in the Fig. L1.15. Click on ![]({{ '/assets/icons/pre_icons/mo_generate_3d_mesh_button.jpg' | relative_url }}) to generate 3D Workpiece mesh. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the Mesh window of Workpiece mesh settings after generating the mesh. 

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0014.jpg' | relative_url }})

3D Workpiece mesh settings page

Click on ![]({{ '/assets/icons/pre_icons/mo_generate_all_button_2.jpg' | relative_url }}) button in 3D setup page and click on “Auto position” button to position the Pusher, Rolls and workpiece correctly as shown in below Fig. L1.16. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0015.jpg' | relative_url }})

Positioning the generated objects

## Simulation controls

Accept the default settings in simulation controls page.

Here save the project and select the Rolling Pass operation in operation editor.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0016.jpg' | relative_url }})

Simulation controls page

## Rolling pass operation

Select the Rolling Pass operation in the operation editor.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0017.jpg' | relative_url }})

Rolling pass operation

## Stand Table

As you select the Rolling Pass operation stand table page will appear as shown in figure. We need to use the Table back and Table front in this lab, so turn on the check box as shown in the Fig. L1.19.. As mesh is generated and material is assigned for rolls, click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Table (Back) page 

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0018.jpg' | relative_url }})

Stand Table page

## Table back

In Table back page, accept the default temperature and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0022.jpg' | relative_url }})

Table (back) page

### Defining Table back geometry

In Table back geometry page, select the 'Define primitive' and define the parameters as mentioned below for back Table geometry.

**Origin Point** X= -50mm

**Width** W= 100mm

**Height** H= 5mm

**Length** =750

**Pass****Line** = 2.5mm

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0023.jpg' | relative_url }})

Back Table Geometry creation

### Table back Mesh Generation

Define the Uniform Thickness number of layers as 5 and keep the rest of the settings as default as shown in Fig. L1.22. Click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) to generate mesh for Table.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0024.jpg' | relative_url }})

Back Table mesh generation

### Table Back Material assigning

To assign material for Table back select the material ‘**AISI-H-13** ’ from material window. This can be done as shown in Fig. L1.23. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Table Front page.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0021.jpg' | relative_url }})

Top Roll material Assigning

Similarly define the Table Front as Table back with same settings for the geometry, mesh and material.

## Pusher object

The Pusher object is created automatically using the workpiece dimensions. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to check the created geometry and assigned movement controls.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0026.jpg' | relative_url }})

Pusher page

### Pusher Geometry

Check the default geometry using ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) option as shown in the Fig. L1.25. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Pusher movement page.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0027.jpg' | relative_url }})

Pusher Geometry Defining

### Pusher Movement Defining

Select Speed option. Speed of the pusher should be 50 to 60% of the relative velocity of the rolls and hence assign a constant speed of 340 mm/sec for pusher. (See Fig. L1.26.) The preview of the movement can be seen by clicking on the "Preview Movement" option. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) will take you to Object Positioning page.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0028.jpg' | relative_url }})

Pusher Movement defining

## Defining Object Positioning

The objects are automatically position correctly when we click ![]({{ '/assets/icons/pre_icons/mo_auto_position_button.jpg' | relative_url }}) button in the 3D setup page and the Table front and table back are created at proper position automatically, so no need to position. The objects positioned should appear as shown in Fig. L1.27.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0029.jpg' | relative_url }})

Position of the objects

## Defining Contact Relations

In the Contact relations page, master-slave relations will be automatically added. Define the shear friction as 0.7 and interface heat transfer coefficient as 11 (see Fig. L1.28). Click the ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) to determine an intelligent contact tolerance and click on ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) button to generate contacts between objects (switch to surface patch model to view the contacts generated between the objects). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0030.jpg' | relative_url }})

Contact Relations generation

## Simulation Controls page

In simulation controls page set Time steps as 5000 for this simulation with a step increment to save as 10 and Time per step as 0.001 sec. For stopping criteria select stopping plane and X direction (see Fig. L1.29.). Click on the free end edge of the workpiece for stopping plane stopping controls (i.e. in +X direction) (see Fig. L1.30.)

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0031.jpg' | relative_url }})

Defining Number of Steps and Stopping criteria

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0032.jpg' | relative_url }})

Stopping plane data (Expert mode)

## Generate Database

In the database generation stage user can check the data required for the analysis and proceed to generate the database (see Fig. L1.31.). For First operation of any multiple operations, user is required to generate the database.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0033.jpg' | relative_url }})

Database Generation

## Running Simulation

Once the database has been generated switch to the Simulation mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the operation tree. Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. L1.32. Use the default **Continue****Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** radio button. Click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

To define MPI settings, click on ![]({{ '/assets/icons/simulator_icons/mo_more_button.jpg' | relative_url }}) button, Run Options window will expand and displays options to define MPI settings for simulation (max number of processors that can be defined depend on your 3D MPI license).

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0034.jpg' | relative_url }})

Run Simulation Popup

## Post Processing

In post processor Step list below the graphic area displays step numbers available from the different operations simulated. A set of state variables available from the ‘Post’ menu can be used to review the model response.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0035.jpg' | relative_url }})

Post Processing wizard

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0037.jpg' | relative_url }})

Strain Effective plot

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab1/image0036.jpg' | relative_url }})

Temperature plot

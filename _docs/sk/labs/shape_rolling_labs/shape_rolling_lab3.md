---
lang: sk
title: "Shape Rolling Lab3"
---

# Shape Rolling Lab3 (Lagrangian using Tet mesh)

3.1. Creating a New problem

3.2. Adding Shape Rolling operation

3.3. Set process conditions

3.4. Define Workpiece

3.5. Defining Roll Grooves

3.6. Defining roll pass settings in Pass table

3.7. 3D Setup

3.8. Simulation controls

3.9. Rolling pass operation

3.10. Stand Table

3.11. Defining Tables

3.12. Pusher object

3.13. Defining Object Positioning

3.14. Defining Contact Relations

3.15. Simulation Controls page

3.16. Generate Database

3.17. Running Simulation

3.18. Post Processing

## Creating a New problem

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear.

Create a new problem either by selecting **File********![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ** **New Problem** or by clicking the New Problem icon. The Problem Setup window will appear as shown in Fig. L3.1. Select " **Integrated Manufacturing Process** " radio button and Unit system as "**SI** " using radio button. Define Problem Name as "**SHR_LAG_LAB3** " and make sure the “**Show option dialog** ” check box is turned on (if we do not turn on the “Show option dialog” check box, then we will not get the New Project dialog in MO UI). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0001.jpg' | relative_url }})

Problem type selection window

  
Multiple operation wizard will open with the New Project dialog as shown in Fig. L3.2., at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session we will use ‘**SHR_LAG_LAB3** ’ as the project name. 3D Shape Rolling operation can also be added in "New Project" dialog (see Fig. L3.2.), in this lab we will add Shape rolling operation from Explorer operation list, so do not check "First operation" check box and "Shape Rolling" operation in "New Project" dialog. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0002.jpg' | relative_url }})

MO Wizard opening window in MO UI

## Adding Shape Rolling operation

Add one Shape Rolling operation from the Explorer Operations list. Operation can be added by clicking on Shape Rolling operation ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button or user can also add by drag and drop into the Operation Editor.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0003.jpg' | relative_url }})

Adding Shape Rolling Operation

## Set process conditions

Select the rolling type as "**Lagrangian** " and symmetry type as **Full** as we will be setting up complete object. As we are interested in temperature gradient in rolls also, select the "**Workpiece and rolls (non-isothermal)** " option. Define the friction coefficient value as **0.7** and heat transfer coefficient value as **11** as shown in Fig. L3.4.

  
![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0004.jpg' | relative_url }})

Process page

## Define Workpiece

In WP_CrossSection window keep the object type as ‘**Plastic** ’ and specify workpiece temperature as **100** °C (see Fig. L3.5.). Other option available at this stage are ‘Import Object’ from another keyword file or database. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0005.jpg' | relative_url }})

Workpiece Object Definition

### Create Workpiece Geometry

To create a rectangular bar geometry for workpiece, in Geometry page select Define Primitive. From primitive geometry window select bar and define the parameters as mentioned below. A rectangular bar is created as shown in Fig. L3.6.  
**Origin Point** = (-50, -42.5)  
**Width** W = 100mm  
**Height** H = 85mm

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0006.jpg' | relative_url }})

Workpiece geometry definition in Geometry primitive window

### Generate Workpiece mesh

Generate the workpiece mesh with default number of elements and settings.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0007.jpg' | relative_url }})

Generating Workpiece mesh

### Assigning Workpiece material

To assign material for workpiece, select the material ‘**AISI****-1045** ’ from material window. This can be done as shown in Fig. L3.8. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Groove list page.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0008.jpg' | relative_url }})

Assigning material for Workpiece

## Defining Roll Grooves

In Groove List page, we can add grooves by clicking on the ‘![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }})’ button. Click ‘![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }})’ once to add one groove, we will be using same grove for top and bottom roll.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0009.jpg' | relative_url }})

Groove list page

### Defining Groove1 geometry

Select the First groove and click on ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}). Roll Groove Primitive page will be opened, select Flat rolls. For roll geometry, Define **width** as **120** , **radius**(r1) as **5** and **Roll****Radius****RR** as **100** as shown in Fig. L3.10.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0010.jpg' | relative_url }})

Defining Groove Geometry

## Defining roll pass settings in Pass table

By default, we can observe Pass1 and First HT being added to the Pass table. First HT settings need to be defined if we are simulating the air cooling of the Workpiece before the first Pass. In this lab, we will simulate only rolling pass, hence we will define settings for Pass1.

Turn on the 'Show all rolls (for asymmetric rolling)' check box.

Under Pass1, select Groove 1 from the groove list for both Top roll and Bottom roll.

Define the Roll speed (rpm) as 50, Roll gap (mm) as 80 and Roll temperature (C) as 40. Leave other settings as default and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to 3D setup page.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0011.jpg' | relative_url }})

Pass Table

## 3D Setup

From DEFORM v12, in 3D Setup page we have Pusher **object** options for Lagrangian rolling operation in Stand table page. Now we can create Pusher **object** using Object option or we can just assign **Pusher****BCC** without creating pusher object as shown in Fig. L3.12.

  
**Object** : When we select Object option, default pusher object geometry will be created similar to workpiece cross section and Pusher object will be added in objects list.

**BCC** : When we select BCC option, for workpiece Pusher BCC will be added in BCC Page and movement page will be added for workpiece to define movement value same as that of Pusher. No pusher object will be added in objects list.

**None** : When we select None option, Pusher object / Pusher BCC will not be added to the operation.

**Auto position** : using this option, Workpiece will be interference positioned with Top roll in Movement direction and Pusher will be interference positioned with Workpiece in Movement direction.

In this lab select **Object** option for **Pusher**.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0012.jpg' | relative_url }})

3D Setup page

### 3D Roll geometry setup

Click on ![]({{ '/assets/icons/pre_icons/mo_3d_setup_edit_button.jpg' | relative_url }}) button of 3D rolls geometry to modify the settings of 3D roll object geometry generation, 3D roll geometry settings page will be opened. In 3D rolls Geometry settings page, define the number of layers as 72 and select the 'Uniform geometry generation'. Then click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button to close the 3D rolls Geometry settings window.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0013.jpg' | relative_url }})

3D Roll Geometry settings page

### 3D Roll mesh settings

Click on ![]({{ '/assets/icons/pre_icons/mo_3d_setup_edit_button.jpg' | relative_url }}) button of 3D rolls mesh to modify the mesh settings of the roll, 3D roll mesh window will be opened with settings for 3D roll mesh. Define **number of revolved sections for rolls** as **72** using the “**Uniform****mesh generation** ” option and import the die material ‘AISI-H-13’ from material library to assign to rolls as shown in Fig. L3.14. Click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) button to generate mesh for rolls with defined settings and the material. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button to close the 3D roll mesh window.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0014.jpg' | relative_url }})

3D Roll mesh settings page

### 3D Workpiece setup using Tetrahedral mesh

In this lab, we will use Tetrahedral mesh for the Workpiece. Click on ![]({{ '/assets/icons/pre_icons/mo_3d_setup_edit_button.jpg' | relative_url }}) button of 3D Workpiece mesh, Mesh window with 3D Workpiece mesh settings will be opened. Select user radio button for Workpiece Length and define the length as **600** mm, select **Tetrahedral****mesh** radio button, define Target number of elements as **20000** and Size ratio as **1** , as shown in the Fig. L3.15. Click on ![]({{ '/assets/icons/pre_icons/mo_generate_3d_mesh_button.jpg' | relative_url }}) to generate 3D Workpiece mesh. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the Mesh window of the Workpiece mesh settings after generating the mesh. 

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0015.jpg' | relative_url }})

3D Workpiece mesh settings page

  
  
Click on ![]({{ '/assets/icons/pre_icons/mo_generate_all_button_2.jpg' | relative_url }}) button in 3D setup page and click on “**Auto****position** ” button to position the Pusher, Rolls and workpiece correctly as shown in below Fig. L3.16. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0016.jpg' | relative_url }})

Positioning the 3D objects

## Simulation controls

Accept the default settings in simulation controls page.

Here save the project and select the Rolling Pass operation in operation editor.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0017.jpg' | relative_url }})

Simulation controls page

## Rolling pass operation

Select the Rolling Pass operation in the operation editor.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0018.jpg' | relative_url }})

Rolling pass operation

## Stand Table

As you select the Rolling Pass operation, the Stand table page will appear as shown in figure [Fig. L3.18.]() We will use tables at front and back of the roll stand in this lab, so turn on the **Table back** and **Table****front** check boxes as shown in the Fig. L3.19. As mesh is generated and material is assigned for rolls, click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Table (Back) page.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0019.jpg' | relative_url }})

Stand Table page

## Defining Tables

We need to define tables at front and back of the roll stand. The table at the back is named **Table(Back)** and the table at front is named **Table(Front)**. In **Table(Back)** page, accept the default temperature and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0020.jpg' | relative_url }})

Table (Back) page

### Defining Table(Back) geometry

In Table(Back) geometry page, select the '**Define primitive'** and define the parameters as mentioned below for back Table geometry.

**Origin Point** X= -50mm

**Width** W = 100mm

**Height** H = 5mm

**Length** = 750

**Pass****Line** = 2.5mm

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0021.jpg' | relative_url }})

Geometry settings for Table(Back)

### Generating Mesh for Table(Back) 

Define the Uniform Thickness number of layers as 5 and keep the rest of the settings as default as shown in Fig. L3.22. Click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) to generate mesh for Table.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0022.jpg' | relative_url }})

Mesh settings for Table(Back)

### Assigning material to Table(Back) 

To assign material for Table(Back) select the material ‘**AISI****-H-13** ’ from material window. This can be done as shown in Fig. L3.23. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Table(Front) page.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0023.jpg' | relative_url }})

Assigning material to Table(Back) 

### Defining Table(Front)

Similar to Table(Back), define the Table(Front) with same settings for the geometry, mesh and material.

## Pusher object

The Pusher object is created automatically using the workpiece dimensions and a constant velocity is assigned based on the roll speed. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to check the created geometry and assigned movement controls.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0024.jpg' | relative_url }})

Pusher page

### Pusher Geometry

Check the default geometry using ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) option as shown in the Fig. L3.25. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Pusher movement page.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0025.jpg' | relative_url }})

Defining Pusher Geometry

### Defining Pusher Movement 

Select Speed option. Speed of the pusher should be 50 to 60% of the relative velocity of the rolls and hence assign a constant speed of **340** mm/sec for pusher. (See Fig. L3.26.) The preview of the movement can be seen by clicking on the "Preview Movement" option. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) will take you to Object Positioning page.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0026.jpg' | relative_url }})

Defining Pusher Movement 

## Defining Object Positioning

The objects are automatically position correctly when we click ![]({{ '/assets/icons/pre_icons/mo_auto_position_button.jpg' | relative_url }}) button in the 3D setup page and the Table(Front) and Table(Back) are created at proper position automatically, so no need to position.

The objects positioned should appear as shown in Fig. L3.27.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0027.jpg' | relative_url }})

Position of the objects

## Defining Contact Relations

In the Contact relations page, master-slave relations will be automatically added. Define the **shear** friction as **0.7** and interface heat transfer coefficient as **11**(see Fig. L3.28.). Click the ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) to determine an intelligent contact tolerance and click on ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) button to generate contacts between objects (switch to surface patch model to view the contacts generated between the objects). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0028.jpg' | relative_url }})

Contact Relations settings

## Simulation Controls page

In simulation controls page set Time steps as **5000** for this simulation with a step increment to save as **10** and Time per step as **0.001** sec. For stopping criteria select stopping plane and X direction (see Fig. L3.29.). Click on the free end edge of the workpiece for stopping plane stopping controls (i.e. in +X direction) (see Fig. L3.30.)

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0029.jpg' | relative_url }})

Defining Number of Steps and Stopping criteria

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0030.jpg' | relative_url }})

Stopping plane data (Expert mode)

## Generate Database

In the database generation stage user can check the data required for the analysis and proceed to generate the database (see Fig. L3.31.). For First operation of any multiple operations, user is required to generate the database.

  
![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0031.jpg' | relative_url }})

Database Generation

## Running Simulation

Once the database has been generated switch to the Simulation mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the operation tree. Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. L3.32. Use the default **Continue Run** option to select “**Continue****from the last step** ” option and then select the Simulation mode as **Interactive** radio button. Click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

To define MPI settings, click on ![]({{ '/assets/icons/simulator_icons/mo_more_button.jpg' | relative_url }}) button, Run Options window will expand and displays options to define MPI settings for simulation (max number of processors that can be defined depend on your 3D MPI license).

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0032.jpg' | relative_url }})

Run Simulation Popup

## Post Processing

In post processor Step list below the graphic area displays step numbers available from the different operations simulated. A set of state variables available from the ‘Post’ menu can be used to review the model response.

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0033.jpg' | relative_url }})

Post Processing wizard

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0034.jpg' | relative_url }})

Strain Effective plot

![]({{ '/assets/images/labs/shape_rolling_labs/shape_rolling_lab3/image0035.jpg' | relative_url }})

Temperature plot

---
lang: sk
title: "2D Forming Operation in Guided Mode Lab"
---

# 2D Forming Operation Lab in Guided Mode

This lab will demonstrate how to setup a typical Forming operation after Furnace heating in multiple operation (MO) guided mode. Forming Operation is an open environment where user can setup any Deformation, Heat transfer, Diffusion and Heat treatment problem but for new user, guided mode will guide with simple and basic features for Simulation controls, Mesh Generation, Stopping and Step controls. For detailed study user can use advanced features from expert mode as user become familiar with the DEFORM.

During this lab we will attempt to highlight various guided mode features of the system that user can use for initial studies.

1.1. Creating New Problem and Adding Operations

1.2. Operation1: Heat Transfer Heating Setup

1.3. Operation2: Forming

1.4. Running Simulation

1.5. Post Processing

## Creating New Problem and Adding Operations

### Creating New Problem

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

DEFORM GUI Main Window

Create a new problem either by selecting **File** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear. Select "**Integrated Manufacturing Process** " radio button and unit system as "**English** " radio button in unit field as shown in Fig. 2DFGL1.1.. Define Problem Name as "**Forming_Operation_in_Guided_Mode** " and make sure the “Show option dialog” check box is turned on (if we do not turn on the “**Show option dialog** ” check box, then we will not get the New Project dialog in MO UI). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Deform Integrated Manufacturing Process.

Multiple operation wizard will open with the New Project dialog, at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session we use ‘**Forming_Operation_in_Guided_Mode** ’ as the project name. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation. MO wizard will open (see Fig. 2DFGL1.2.), Select the first operation as 2D Heat transfer operation and check the checkbox to add Heat transfer operation as first operation. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0002.jpg' | relative_url }})

MO Wizard New Project Opening Window

### Adding Forming operation

Multiple Operation wizard will open new project with one 2d Heat transfer operation. Add one Forming operation for Cone Forming after Heat transfer by air for 5 seconds from furnace to dies from Explorer Operations list by clicking ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button as shown in Fig. 2DFGL1.3.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0003.jpg' | relative_url }})

Adding Forming Operation

## Operation1: Heat Transfer Heating Setup

For first heat transfer operation, change the operation name to "**Air Transfer** " by double clicking on Operation name in Operation Editor window as shown in Fig. 2DFGL1.4. and press **Enter** from Keyboard after editing.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0004.jpg' | relative_url }})

Name the first operation as Air Transfer

### Selecting Geometry Type

In this lab we are using Axisymmetric geometries, so activate **2D Axisymmetric** radio button in geometry type window as shown in Fig. 2DFGL1.3., then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

### Selecting Heat Transfer Type

Select "**Transfer through air** " as heat transfer type for Air Transfer operation as shown in Fig. 2DFGL1.5. This will set the default heat transfer settings for heating operation. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0005.jpg' | relative_url }})

Heat transfer type selection for air transfer

### Set Process Conditions

Define Transfer time as 5 sec at 68°F environment temperature and default convection coefficient as shown in Fig. 2DFGL1.6. and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0006.jpg' | relative_url }})

Process Condition settings for air transfer

### Select Simulation Controls for air transfer

Keep only Heat Transfer mode is checked as only heat transfer is modeled as shown in Fig. 2DFGL1.7. When user is in simulation controls window expert mode (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})) will be activated (see Fig. 2DFGL1.7.), user can use this mode for advanced features. As in this lab we are not using any such features, click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0007.jpg' | relative_url }})

Simulation Controls settings for air transfer in guided mode

### Import material for workpiece

In Material window, load the material **AISI-4120** from DEFORM Material library's, from **Steel** category using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load material data from library) option. This can be done as shown in Fig. 2DFGL1.8. by clicking on ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}) button. Material can also be loaded from Materials list in Explorer. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) for Material and Object window.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0008.jpg' | relative_url }})

Importing Workpiece material from DEFORM library

### Define Workpiece

In Workpiece object window keep the object type as ‘**Plastic** ’ and specify workpiece temperature as 1750°F (see Fig. 2DFGL1.9.). Using ‘ Import Object from a file' option we can import object data from keyword file or database and from or 'Import object from library’ option we can import object data from keyword file. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0009.jpg' | relative_url }})

Workpiece Object definition

### Create Workpiece Geometry

In Geometry page, click on ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) action label (see [Fig. 2DFGL1.10.]()) and create a **cylinder** of **radius****0.4** and **height****2.7** as shown in Fig. 2DFGL1.11. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0010.jpg' | relative_url }})

Geometry definition window

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0011.jpg' | relative_url }})

Cylinder geometry creation for workpiece

### Generate Workpiece Mesh

Generate the mesh using 1000 elements using ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button (see Fig. 2DFGL1.12.). Complete range of meshing options are available in expert mode (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})), if user needs to have more control on the mesh generated. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0012.jpg' | relative_url }})

Mesh generation for workpiece

###  Assign Workpiece Material

To assign material for workpiece select the material ‘**AISI-4120** ’ from material window. This can be done as shown in Fig. 2DFGL1.13. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0013.jpg' | relative_url }})

Assigning material for workpiece

### Defining workpiece Boundary Conditions

In BCC page, check the default assigned Heat exchange with Environment BCC to the entire outer surface of the Billet (which does not include the centerline since these nodes are inside the object) by clicking on Defined under Heat exchange with Environment. Default BCC are assigned automatically due to selection of problem type as axisymmetric and simulation mode as heat transfer. (see Fig. 2DFGL1.14.)

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0014.jpg' | relative_url }})

Boundary condition definition for workpiece

Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Step controls window as there is no object positioning and thermal stopping controls definition is required.

### Define Step Controls

Set the **number of simulation steps** as **50** at**0.1** sec each step and saving **every****5** steps (see Fig. 2DFGL1.15.). Advanced Simulation controls settings are available in expert mode (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to proceed to the database generation stage.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0015.jpg' | relative_url }})

Simulation controls settings for air transfer

### Generate Database

At the database generation stage user can check the data required for the analysis and proceed to generate the database (see Fig. 2DFGL1.16.). For the first operation of any multiple operations, user is required to generate the database. For all the subsequent operations we need to setup only the process data and simulation controls. Click on ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) to proceed to the next operation "**Cone****Forming** ".

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0016.jpg' | relative_url }})

Database generation window for first operation

## Operation2: Forming

The Forming operation runs till distance between dies reaches 0.025". As workpiece is coming from air transfer operation with its thermal history, make workpiece as read from DB object and add other three objects for Punch, Bottom die and Ejector to setup the cone forming operation.

Name the operation as "**Cone Forming** " by double clicking on Operation name in Operation Editor and press Enter key from Keyboard to close. Accept the 2D Axisymmetric geometry type and click on![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

### Select Simulation Controls settings for cone forming

In simulation controls check both Deformation and Heat transfer simulation modes as shown in Fig. 2DFGL1.17. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0017.jpg' | relative_url }})

Simulation control settings for cone forming

### Import material for dies

In material window, import the **AISI-H13** material for dies from DEFORM library ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **Die_material** category as shown in Fig. 2DFGL1.18. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until objects window to add objects.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0018.jpg' | relative_url }})

Importing die material from DEFORM library

### Add die objects

In Object window add 4 number of objects as shown in Fig. 2DFGL1.19., as we will be bringing in all three dies at **300°** F for the cone forming operation. We can now see the object tree is expanded to include the dies, details of which will be now be defined now. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0019.jpg' | relative_url }})

Adding objects for cone forming

### Define Workpiece

In workpiece definition window select the object type as "**Read from DB** " as shown in Fig. 2DFGL1.20. Click on Top Die in operation tree to define the Dies.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0020.jpg' | relative_url }})

Workpiece definition window in cone forming

### Define Top die

In Top die definition window, accept the object type as rigid and specify initial temperature as 300°F as shown in Fig. 2DFGL1.21. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0021.jpg' | relative_url }})

Top die definition window in cone forming

### Import and Edit Top die geometry

In Top die Geometry window, click on ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load Geometry from Library) button and import ‘**StubShaft_ConeTools.igs** ' from DEFORM geometry library path /2D/LABS/. As this geometry contains multiple boundaries, system pops up message regarding geometry editing. Click on ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}) button for popup to edit the imported geometry as shown in Fig. 2DFGL1.22.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0022.jpg' | relative_url }})

Importing the multiple boundary geometry for top die

Select the second loop and click on ![]({{ '/assets/icons/pre_icons/mo_delete_loop_button.jpg' | relative_url }}) button to delete loop 2 as shown in Fig. 2DFGL1.23. and click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the geometry editor. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0023.jpg' | relative_url }})

Top die geometry editing

### Meshing Top Die

In mesh generation window generate top die mesh with 1000 elements using ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button as shown in Fig. 2DFGL1.24. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0024.jpg' | relative_url }})

Generating mesh for to die

### Assign material to top die

In top die material window select material **AISI-H13** to assign for top die as shown in Fig. 2DFGL1.25. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0025.jpg' | relative_url }})

Assigning material for top workpiece

### Assigning BCC for top die

In the ‘Define BCC’ window, ‘Heat Exchange with Environment’ BCC automatically assigned to the all edges except axis edge. Click on Defined branch under Heat Exchange with Environment BCC to confirm the BCC definition (see Fig. 2DFGL1.26.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0026.jpg' | relative_url }})

Assigning boundary conditions for top die

### Assigning movement controls for top die

In top die movement controls define the **hydraulic****press** with hydraulic speed as function of time with power limit definition in **-Y** direction as shown in Fig. 2DFGL1.27.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0027.jpg' | relative_url }})

Hydraulic movement definition for top die

Click on ![]({{ '/assets/icons/pre_icons/mo_define_function.._button.jpg' | relative_url }}) button next to speed and define such that from 0 to 0.025 sec press ram speed is 10 in/sec and from 0.02501 to 0.06 sec ram speed is 8 in/sec as shown in Fig. 2DFGL1.28. By default in multiple operations for function of time definitions local time will be considered so in this function time 0 till 0.06 seconds referring to cone forming operation. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to close the definition.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0028.jpg' | relative_url }})

Hydraulic speed defined as function of local time

Click on ![]({{ '/assets/icons/pre_icons/mo_define..._button2.jpg' | relative_url }}) button next to power limit to define the power limit curve as shown in Fig. 2DFGL1.29. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to close the definition and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Bottom die definition window.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0029.jpg' | relative_url }})

Power limit definition for hydraulic press

### Define Bottom Die

In Bottom die definition window accept the object type as rigid and specify initial temperature as 300°F as shown in Fig. 2DFGL1.30. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0030.jpg' | relative_url }})

Bottom die definition window

### Import and Edit Bottom die geometry

In Bottom die Geometry window, click on ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load Geometry from Library) button and import ‘**StubShaft_ConeTools.igs** ' from DEFORM geometry library path /2D/LABS/. As this geometry contains multiple boundaries, system pops up message and asks, want to edit geometry or not. Click on ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}) button for popup to edit the imported geometry as shown in Fig. 2DFGL1.31.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0031.jpg' | relative_url }})

Importing the multiple boundary geometry for bottom die

Select the first loop and click on ![]({{ '/assets/icons/pre_icons/mo_delete_loop_button.jpg' | relative_url }}) button to delete loop 1 as shown in Fig. 2DFGL1.32. and click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the geometry editor. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0032.jpg' | relative_url }})

Bottom die geometry editing

### Meshing Bottom Die

In mesh generation window generate bottom die mesh with 1000 elements using ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button as shown in Fig. 2DFGL1.33. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0033.jpg' | relative_url }})

Generating mesh for bottom die

### Assign material to bottom die

In bottom die material window, select material **AISI-H13** to assign it for bottom die as shown in Fig. 2DFGL1.25. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

### Assigning BCC for bottom die

In the ‘Define BCC’ window, ‘Heat Exchange with Environment’ BCC is automatically assigned to the all sides. Click on Defined branch under Heat Exchange with Environment BCC to confirm the BCC definition (see Fig. 2DFGL1.34.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Object 4 definition window.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0034.jpg' | relative_url }})

Assigning boundary conditions for bottom die

### Define Ejector

In Object 4 definition window change the object name to '**Ejector** " and specify initial temperature as 300°F. By accepting the object type as rigid, click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue. (see Fig. 2DFGL1.35.)

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0035.jpg' | relative_url }})

Ejector die definition window

###  Create Ejector geometry

In Ejector die Geometry window, click on ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}) action label to define geometry points in geometry table as shown in Fig. 2DFGL1.36. After completing the geometry definition click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the geometry editor and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0036.jpg' | relative_url }})

Importing the multiple boundary geometry for ejector die

### Meshing Ejector

In mesh generation window generate ejector mesh with 1000 elements using ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button as shown in Fig. 2DFGL1.37. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0037.jpg' | relative_url }})

Generating mesh for ejector die

### Assign material to ejector die

In ejector die material window, select material AISI-H13 to assign it for ejector as shown in Fig. 2DFGL1.25. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

### Assigning BCC for ejector die

In the ‘Define BCC’ window, ‘Heat Exchange with Environment’ BCC automatically assigned to edges except axis edge. Click on Defined branch under Heat Exchange with Environment BCC to confirm the BCC definition (see Fig. 2DFGL1.38.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until contact window as all objects are correctly positioned by default.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0038.jpg' | relative_url }})

Assigning boundary conditions for ejector die

### Defining Inter-Object relations

Select user type contact and click on ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) button (see Fig. 2DFGL1.40.). It will add the relationship between the Billet, Top Die, Bottom Die and Ejector. As the Dies are Rigid and Billet is plastic, Top, Bottom and ejector Dies are considered as Master and Billet as Slave. In order to predict the fold during deformation, self contact will be assigned for Billet.

Select the **Top Die – Workpiece** relationship and click the ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) button to modify the contact conditions. Under friction tab (see Fig. 2DBL1.39.), there is a pull-down menu that allows the user to choose the appropriate friction conditions of common forming processes.

Since this is warm forming simulation and the dies are steel, use the pull down menu and select **warm forming** from the list. A friction value of **0.25** will be automatically defined. In thermal tab by default heat transfer coefficient assigned is 0.004 which is ok for forming.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0039.jpg' | relative_url }})

Inter-object friction coefficient definition window

Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to go back to Inter-Object window, since the friction conditions are the same for all the object pairs, ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) button can be used to copy the interface properties from the first relationship to all of the others. After this is done, all relationships will have a friction of 0.25 and heat transfer coefficient as 0.004 defined as shown in Fig. 2DFGL1.40. Since the contact will initialize and generate while generating database, turn on initialize and generate check boxes. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0040.jpg' | relative_url }})

Inter-Object relationship definition for cone forming

### Define Stopping controls

In stopping control window, check the Distance between objects stopping control and define it as 0.025". Then from display window pick the point on top die lower edge and bottom die upper edge and select the direction as Y as shown in Fig. 2DFGL1.41. After picking points on dies distance between dies can be observed, in this case it is around **0.5** ". For advanced stopping options please refer Expert mode (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})), as we are not using in this lab click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0041.jpg' | relative_url }})

Distance between dies stopping control for cone forming

### Define Step controls

In step controls window define **number of steps** as **100** , at **0.005** ” per step of die movement, **step increment to save** as **10** for the primary die (which is object number 2 in this simulation) as shown in Fig. 2DFGL1.42. Advanced step controls and simulation controls features are available in Expert mode (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}))

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0042.jpg' | relative_url }})

Step controls settings for cone forming

This completes multiple forming operation setup in MO - Guided mode, as database for cone forming operation will be generated during simulation. To simulate the problem switch to Simulation tab by clicking on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button.

## Running Simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. 2DFGL1.43. Use the default **Continue Run** option to select “**Continue from the last step** ” (from step -1) option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0043.jpg' | relative_url }})

Run Simulation popup window

Monitor the progress of the simulation by looking at the Simulation Graphics, Simulation Message and Simulation Log tab, making sure that the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked. (see Fig. 2DFGL1.44.)

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0044.jpg' | relative_url }})

Simulation mode displaying the cone forming running status

After completion of all operations, simulation log file will display a message as "MULTIPLE OPERATION COMPLETED." and then switch to Post tab to view the simulation results.

## Post Processing

In post processor Step list below the graphic area indicates step numbers available from the different operations simulated. A set of state variables available from the ‘Post’ menu can be used review the model response. Please note that for the first operation only the thermal data for the workpiece is available. And the deformation results can be seen for the Cone forming operation (see Fig. 2DFGL1.45.). Use the ![]({{ '/assets/icons/pre_icons/mo_box_zoom_icon.jpg' | relative_url }}) (zoom by window) icon to zoom the cone portion of the workpiece as shown in Fig. 2DFGL1.45.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0045.jpg' | relative_url }})

MO Post processor with Strain-Effective variable contour at workpiece cone shape

Some important state variables can be selected directly from ‘Post Tools’ window and the rest can be accessed through State Variable dialog by clicking on ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) icon.

Click on ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) Graph (Load-Stroke) and plot Time (sec) vs Load (klb) and also plot Time (sec) Vs Speed (in/sec) for top die. Observe the change in speed as load crosses the power limit curve, speed change from 10 in/sec to 8 in/sec as shown in Fig. 2DFGL1.46.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_guided_mode/image0046.jpg' | relative_url }})

Time vs Load and Time vs Speed plots for primary die (Top die)

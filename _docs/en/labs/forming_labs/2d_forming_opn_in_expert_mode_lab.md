---
lang: en
title: "2D Forming Operation in Expert mode Lab"
---

# 2D Forming Operation in Expert mode Lab

  
This lab will demonstrate how to setup a typical Forming operation after Furnace heating in multiple operation (MO) expert mode. Forming Operation is an open environment where user can setup any Deformation, Heat transfer, Diffusion and Heat treatment problem but for new user, guided mode will guide with simple and basic features for Simulation controls, Mesh Generation, Stopping and Step controls. For detailed study user can go for advanced features using expert mode once become familiar with the DEFORM.

During this lab we will attempt to explore few expert mode features of the system.

## Creating New Problem and Adding Operations

### Creating New Problem

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

New Problem Window

Create a new problem either by selecting **File** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in Fig. 2DFEL1.1.. Select "**Integrated Manufacturing Process** " radio button and unit system as "**English** " radio button in unit field. Define Problem Name as "**Forming_Operation_in_expert_Mode** " and make sure the “Show option dialog” check box is turned on (if we do not turn on the “**Show option dialog** ” check box, then we will not get the New Project dialog in MO UI). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Deform Integrated Manufacturing Process.

Multiple operation wizard will open, at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session we use ‘**Forming_Operation_in_expert_Mode** ’ as the project name. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation. MO wizard will open (see Fig. 2DFEL1.2.), Select the first operation as 2D Heat transfer operation and check the checkbox to add Heat transfer operation as first operation. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0002.jpg' | relative_url }})

MO Wizard New Project Opening Window

###  Adding Forming operation

Multiple Operation wizard will open new project with 2d Heat transfer operation. Add one Forming operation for Cone Forming after Heat transfer by air for 5 seconds from furnace to dies using Explorer Operations list by clicking ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button as shown in Fig. 2DFEL1.3.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0003.jpg' | relative_url }})

Adding Forming Operation

## Operation1: Heat Transfer Heating Setup

For first heat transfer operation, change the operation name to "**Air Transfer** " by double clicking on Operation name in Operation Editor window as shown in Fig. 2DFEL1.4. and press **Enter** key from Keyboard after editing.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0004.jpg' | relative_url }})

Name the first operation as Air Transfer

### Selecting Geometry Type

In this lab we are using Axisymmetric geometries, so activate **2D Axisymmetric** radio button in geometry type window as shown in Fig. 2DFEL1.3., then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

### Selecting Heat Transfer Type

Select "**Transfer through air** " as heat transfer type for Air Transfer operation as shown in Fig. 2DFEL1.5. This will set the default heat transfer settings for heating operation. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0005.jpg' | relative_url }})

Heat transfer type selection for air transfer

### Set Process Conditions

Define **Transfer time** as **5** sec at 68°F environment temperature and default convection coefficient as shown in Fig. 2DFEL1.6. and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0006.jpg' | relative_url }})

Process Condition settings for air transfer

### Select Simulation Controls for air transfer

In simulation controls window expert mode (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})) will be activated (see [Fig. 2DFEL1.7.]()), select the icon in the tool tab to observe the expert mode simulation control options.

Keep only the Heat Transfer mode checked in Main tab as only heat transfer is modeled as shown in Fig. 2DFEL1.7. Also other advanced features like step, stop, solver, process conditions,.. etc are available, we will use some of these features in meshing, stopping and step controls during the later stage of the setup. For more information about simulation controls options refer [Simulation Controls](/docs/en/pre_processor/9_simulation_controls/9_simulation_controls/). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0007.jpg' | relative_url }})

Simulation Controls settings for Furnace Heating in expert mode

### Import material for workpiece

In Material window, load the material **AISI-4120** from DEFORM Material library's, from **Steel** category using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load material data from library) option. This can be done as shown in Fig. 2DFEL1.8. by clicking on ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}) button. Material can also be loaded from Materials list in Explorer. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) for Material and Object window, as only Workpiece heat transfer in air is our interest in air transfer operation.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0008.jpg' | relative_url }})

Importing Workpiece material from DEFORM library

### Define Workpiece

In Workpiece object window keep the object type as ‘**Plastic** ’ and specify workpiece temperature as **1750** °F (see Fig. 2DFEL1.9.). Using ‘Import Object from a file' ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) option we can import object data from keyword file or database and from or 'Import object from library’ option we can import object data from keyword file. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue and import the workpiece geometry.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0009.jpg' | relative_url }})

Workpiece Object definition

### Create Workpiece Geometry

In Geometry page, click on ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) action label (see Fig. 2DFEL1.10.) and create a **cylinder** of radius **0.4** " and height **2.7** " as shown in Fig. 2DFEL1.11.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0010.jpg' | relative_url }})

Geometry definition window

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0011.jpg' | relative_url }})

Cylinder geometry creation for workpiece

### Generate Workpiece Mesh

Complete range of meshing options are available in expert mode (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})), for air transfer operation generate the mesh using **1000** elements and **size ratio** of**3** as shown in Fig. 2DFEL1.12. In the next operation we will use other mesh density window and remeshing options. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue. For more information about expert mode mesh options refer [13.1. 2D Mesh Generation](/docs/en/pre_processor/13_mesh_generation/13_1_2d_mesh_generation/).

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0012.jpg' | relative_url }})

Mesh generation for workpiece

### Assign Workpiece Material

To assign material for workpiece select the material ‘**AISI****-4120** ’ from material window. This can be done as shown in Fig. 2DFEL1.13. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0013.jpg' | relative_url }})

Assigning material for workpiece

### Defining workpiece Boundary Conditions

In BCC page, check the default assigned Heat exchange with Environment BCC to the entire outer surface of the Billet (which does not include the centerline since these nodes are inside the object) by clicking on Defined under Heat exchange with Environment. Default BCC are assigned automatically due to selection of problem type as axisymmetric and simulation mode as heat transfer. (see Fig. 2DFEL1.14.)

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0014.jpg' | relative_url }})

Boundary condition definition for workpiece

Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until stopping controls window as there is no object positioning is required.

### Check Stopping controls

In stopping controls window in expert mode we can observe that Transfer time **5** sec defined in process condition window at the beginning of the setup reflecting here as Process duration stopping control as shown in Fig. 2DFEL1.15. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0015.jpg' | relative_url }})

Air transfer operation stopping control

### Define Step Controls

Set the step definition type as**time increment** of **0.1** sec constant value in step increment tab as shown in Fig. 2DFEL1.16.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0016.jpg' | relative_url }})

Step increment definition for air transfer

Select simulation steps tab to set the **number of simulation steps** as**50** and saving every **5** steps as shown in Fig. 2DFEL1.17., various advanced simulation controls settings are also available in step controls expert mode (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to proceed to the database generation stage.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0017.jpg' | relative_url }})

Simulation steps definition for air transfer

### Generate Database

At the database generation stage user can check the data required for the analysis and proceed to generate the database (see Fig. 2DFEL1.18.). For the first operation of any multiple operations, user is required to generate the database. For all the subsequent operations we need to setup only the process data and simulation controls. Click on ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) to proceed to the next operation ‘**Cone****Forming** ".

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0018.jpg' | relative_url }})

Database generation window for first operation

## Operation2: Forming

The Forming operation runs till distance between dies reaches 0.025". As workpiece is coming from air transfer operation with its thermal history, make workpiece as read from DB object and add other three objects for Punch, Bottom die and Ejector to setup the cone forming operation.

Name the operation as "**Cone Forming** " by double clicking on Operation name in Operation Editor and press Enter key from Keyboard to close. Accept the axi-symmetric geometry type and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

### Select Simulation Controls settings for cone forming

In simulation controls check both **Deformation** and **Heat transfer** simulation modes as shown in Fig. 2DFEL1.19. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0019.jpg' | relative_url }})

Simulation control settings for cone forming

### Import material for dies

In material window, import the **AISI-H13** material for dies from **DEFORM library** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **Die_material** category as shown in Fig. 2DFEL1.20. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until objects window to add objects.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0020.jpg' | relative_url }})

Importing die material from DEFORM library

### Add die objects

In Object window add 4 objects as shown in Fig. 2DFEL1.21., as we will be bringing in all three dies at **300** °F for the cone forming operation. We can now see the object tree is expanded to include the dies, details of which will be defined now. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0021.jpg' | relative_url }})

Adding objects for cone forming

### Define Workpiece

In workpiece definition window select the object type as "**Read from DB** " as shown in Fig. 2DFEL1.22. After defining dies we will define the mesh density window for workpiece at bottom die top inside corner for cone forming, so click on Top Die in operation tree to define the Dies.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0022.jpg' | relative_url }})

Workpiece definition window in cone forming

### Define Top die

In Top die definition window accept the object type as rigid and specify initial temperature as **300** °F as shown in Fig. 2DFEL1.23. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0023.jpg' | relative_url }})

Top die definition window in cone forming

### Import and Edit Top die geometry

In Top die Geometry window, click on ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load Geometry from Library) button and import ‘**StubShaft_ConeTools****.igs'** from DEFORM geometry library path **/2D/LABS/**. As this geometry contains multiple boundaries, system pops up message regarding geometry editing. Click on ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}) button for popup to edit the imported geometry as shown in Fig. 2DFEL1.24.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0024.jpg' | relative_url }})

Importing the multiple boundary geometry for top die

Select the second loop and click on ![]({{ '/assets/icons/pre_icons/mo_delete_loop_button.jpg' | relative_url }}) button to delete **loop 2** as shown in Fig. 2DFEL1.25. and click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the geometry editor. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0025.jpg' | relative_url }})

Top die geometry editing

### Meshing Top Die

In mesh generation window generate top die mesh with default 1000 elements and size ratio 3 using ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button as shown in Fig. 2DFEL1.26. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0026.jpg' | relative_url }})

Generating mesh for to die

### Assign material to top die

In top die material window select material **AISI-H13** to assign for top die as shown in Fig. 2DFEL1.27. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0027.jpg' | relative_url }})

Assigning material for top workpiece

### Assigning BCC for top die

In the ‘Define BCC’ window, ‘Heat Exchange with Environment’ BCC is automatically assigned to all edges except axis edge. Click on Defined branch under Heat Exchange with Environment BCC to confirm the BCC definition (see Fig. 2DFEL1.28.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0028.jpg' | relative_url }})

Assigning boundary conditions for top die

### Assigning movement controls for top die

In top die movement controls define the hydraulic press with hydraulic speed as function of time with power limit definition in**-Y** direction as shown in Fig. 2DFEL1.29.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0029.jpg' | relative_url }})

Hydraulic movement definition for top die

Click on ![]({{ '/assets/icons/pre_icons/mo_define_function..._button2.jpg' | relative_url }}) button next to speed and define it such that from 0 to 0.025 sec ram moves with speed is 10 in/sec and from 0.02501 to 0.06 sec ram moves with speed 8 in/sec, as this operation start after 5 second air transfer operation if user wants to maintain the global time for function definition then in simulation controls Global time must be selected for function definition. Hence in this lab we define the speed as function of global time as shown in Fig. 2DFEL1.30. i.e., from 5 to 5.025 sec ram moves with speed of 10 in/sec and from 5.02501 to 5.06 sec ram moves with speed of 8 in/sec. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to close the definition.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0030.jpg' | relative_url }})

Hydraulic speed definition function of global time

Click on ![]({{ '/assets/icons/pre_icons/mo_define..._button2.jpg' | relative_url }}) button next to power limit to define the power limit curve as shown in Fig. 2DFEL1.31. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to close the definition and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Bottom die definition window.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0031.jpg' | relative_url }})

Power limit definition for hydraulic press

### Define Bottom Die

In Bottom die definition window accept the object type as **Rigid** and specify initial temperature as **300°** F as shown in Fig. 2DFEL1.32. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0032.jpg' | relative_url }})

Bottom die definition window

### Import and Edit Bottom die geometry

In Bottom die Geometry window, click on ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load Geometry from Library) button and import ‘**StubShaft_ConeTools****.igs** ' from DEFORM geometry library path **/2D/LABS/**. As this geometry contains multiple boundaries, system pops up message regarding geometry editing. Click on ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}) button for popup to edit the imported geometry as shown in Fig. 2DFEL1.33.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0033.jpg' | relative_url }})

Importing the multiple boundary geometry for bottom die

Select the first loop and click on ![]({{ '/assets/icons/pre_icons/mo_delete_loop_button.jpg' | relative_url }}) button to delete loop 1 as shown in Fig. 2DFEL1.34. and click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the geometry editor. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0034.jpg' | relative_url }})

Bottom die geometry editing

### Meshing Bottom Die

In mesh generation window generate bottom die mesh with 1000 elements using ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button as shown in Fig. 2DFEL1.35. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0035.jpg' | relative_url }})

Generating mesh for bottom die

### Assign material to bottom die

In bottom die material window, select material **AISI-H13** to assign it for bottom die as shown in Fig. 2DFEL1.27. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

### Assigning BCC for bottom die

In the ‘Define BCC’ window, ‘Heat Exchange with Environment’ BCC is automatically assigned to all edges. Click on Defined branch under Heat Exchange with Environment BCC to confirm the BCC definition (see Fig. 2DFEL1.36.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Object 4 definition window.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0036.jpg' | relative_url }})

Assigning boundary conditions for bottom die

### Define Ejector

In Object 4 definition window change the object name to "**Ejector** " and specify initial temperature as **300** °F. By accepting the object type as **rigid** , click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue. (see Fig. 2DFEL1.37.)

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0037.jpg' | relative_url }})

Ejector die definition window

### Create Ejector geometry

In Ejector die Geometry window, click on ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}) action label to define geometry points in geometry table as shown in Fig. 2DFEL1.38. After completing the geometry points definition, click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the geometry editor and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0038.jpg' | relative_url }})

Importing the multiple boundary geometry for ejector die

### Meshing Ejector

In mesh generation window generate ejector mesh with 1000 elements using ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button as shown in Fig. 2DFEL1.39. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0039.jpg' | relative_url }})

Generating mesh for ejector die

### Assign material to ejector die

In ejector die material window, select material **AISI-H13** to assign it for ejector as shown in Fig. 2DFEL1.27. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

### Assigning BCC for ejector die

In the ‘Define BCC’ window, ‘Heat Exchange with Environment’ BCC automatically assigned to all edges except axis edge. Click on Defined branch under Heat Exchange with Environment BCC to confirm the BCC definition (see Fig. 2DFEL1.40.). Click on **Workpiece Mesh branch** in operation tree to define mesh for cone forming.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0040.jpg' | relative_url }})

Assigning boundary conditions for ejector die

### Define workpiece mesh for cone forming

Near bottom die top inside corner we will add the mesh density window to capture state variable more accurately and also define the forced **remesh** for every **20 steps** to refine the mesh. So check "**Define mesh settings** " so that changes take effect when simulation hits remeshing and also check the "**Perform Remesh Before This Operation** " so that new mesh settings are in effect from the forming operation beginning. Select the "**Weighting Factors** " tab to activate mesh density windows by giving the weight of 0.2 to Mesh windows and set Boundary curvature to 0.4, Strain Distribution to 0.2 and Strain rate distribution to 0.2 as shown in Fig. 2DFEL1.41.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0041.jpg' | relative_url }})

Setting weighting factor for mesh windows

After setting weight for mesh windows, Mesh windows tab is activated as shown in Fig. 2DFEL1.41. Now select Mesh windows tab to add mesh density window, click on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button to add mesh window. By using ![]({{ '/assets/icons/pre_icons/mo_box_zoom_icon.jpg' | relative_url }}) (zoom by window) or ![]({{ '/assets/icons/pre_icons/mo_zoom_icon.jpg' | relative_url }}) (Dynamic zoom) icon, to zoom the bottom die top inside corner near to where we need to add window on workpiece. Using the window definition tools polygon or box, define the window as shown in Fig. 2DFEL1.42. Define the relative mesh element size of 0.00001 for window compared to elements outside window.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0042.jpg' | relative_url }})

Defining mesh density window for workpiece in cone forming

Select remeshing criteria tab and define the **Maximum step increment** as **20** , so simulation hits remesh after every 20 steps in cone forming operation as shown in Fig. 2DFEL1.43. Click on **Contact** in operation tree to define inter-object relations.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0043.jpg' | relative_url }})

Forced remeshing criteria used for cone forming

### Defining Inter-Object relations

Select user type contact and click on ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) button (see Fig. 2DFEL1.45.). It will add the relationship between the Billet, Top Die, Bottom Die and Ejector. As the Dies are Rigid and Billet is plastic, Top, Bottom and ejector Dies are considered as Master and Billet as Slave. In order to predict the fold during deformation, self contact will be assigned for Billet.

Select the **Top Die – Workpeice** relationship and click the ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) button to modify the contact conditions. Under friction tab (see Fig. 2DFEL1.44.), there is a pull-down menu that allows the user to choose the appropriate friction conditions of common forming processes.

Since this is warm forming simulation and the dies are steel, use the pull down menu and select warm forming from the list. A friction value of 0.25 will be automatically defined. In thermal tab by default heat transfer coefficient assigned is 0.004, which is ok for forming.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0044.jpg' | relative_url }})

Inter-object friction coefficient definition window

Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to go back to Inter-Object window, since the friction conditions are the same for all the object pairs, ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) button can be used to copy the interface properties from the first relationships will have a friction value of 0.25 and heat transfer coefficient value of 0.0004 defined as shown in Fig. 2DFEL1.45. Since the contact will initialize and generate while generating database, turn on initialize and generate checkboxes. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0045.jpg' | relative_url }})

Inter-Object relationship definition for cone forming

### Define Stopping controls

In stopping control window select the Die Distance tab to define flash thickness, simulation stops when distance between dies reaches 0.025". So enter the distance **0.025** , select the direction as Y and then from display window pick the point on top die lower edge and bottom die upper edge as shown in Fig. 2DFEL1.46. After picking points on dies, distance between dies can be observed, in this case it is around 0.5". Process parameters like primary die Max. load, Min. velocity and Max. stroke, Max. Strain in element and Process duration can also be used as stopping controls and also stopping plane stopping control is available, which is normally used in rolling operation. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0046.jpg' | relative_url }})

Distance between dies stopping control for cone forming

###  Define Step controls

In step increment tab select step definition as **Die displacement** of **0.005** " as shown in Fig. 2DFEL1.47.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0047.jpg' | relative_url }})

Step controls settings for cone forming operation

Select **simulation steps** tab and set **number of steps** as **100** and**step increment to save** as **10** for the primary die displacement (which is Top die, object number 2 in this simulation) as shown in Fig. 2DFEL1.48.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0048.jpg' | relative_url }})

Simulation steps definition for cone forming

Select **Advanced**![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **Variables** tab to use global time while applying function data (see Fig. 2DFEL1.49.) as we used the global time for hydraulic press speed function definition.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0049.jpg' | relative_url }})

Selecting global time for function data in cone forming

Select the Remeshing criteria tab to observe the workpiece remeshing criteria defined in workpiece mesh window as shown in Fig. 2DFEL1.50.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0050.jpg' | relative_url }})

Cone forming operation remeshing criteria defined for workpiece

This completes the multiple forming operation setup in MO - Expert mode, as database for cone forming operation will be generated during simulation.. To simulate the problem switch to Simulation tab above the object tree by clicking on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button. 

## Running Simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. 2DFEL1.51. Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0054.jpg' | relative_url }})

Run Simulation popup window

Monitor the progress of the simulation by looking at the Simulation Graphics, Simulation Message and Simulation Log tab, making sure that the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked. (see Fig. 2DFEL1.52.) As the simulation progress, observe the mesh density effect during cone forming operation as shown in Fig. 2DFEL1.52.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0051.jpg' | relative_url }})

Simulation mode displaying the cone forming running status

After completion of all operations, Simulation log file will display a message as "MULTIPLE OPERATION COMPLETED.", then switch to Post tab to view the simulation results.

## Post Processing

In post processor Step list below the graphic area indicates step numbers available from the different operations simulated. A set of state variables available from the ‘Post’ menu can be used review the model response. Please note that for the first operation only the thermal data for the workpiece is available. And the deformation results can be seen for the Cone forming operation. Use the ![]({{ '/assets/icons/pre_icons/mo_box_zoom_icon.jpg' | relative_url }}) (zoom by window) icon to zoom the cone portion of the workpiece as shown in Fig. 2DFEL1.53. Also we can see the fine mesh for workpiece at the bottom die top inside corner because of mesh density window definition.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0052.jpg' | relative_url }})

MO Post processor with Strain-Effective variable contour at workpiece cone shape

Some important state variables can be selected directly from ‘Post Tools’ window and the rest can be accessed through State Variable dialog by clicking on ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) icon.

Click on ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) Graph (Load-Stroke) and plot Time (sec) vs Load (klb) and also plot Time (sec) Vs Speed (in/sec) for top die. Observe the change in speed as load crosses the power limit curve, speed changes from 10 in/sec to 8 in/sec as shown in Fig. 2DFEL1.54.

![]({{ '/assets/images/labs/forming_labs/2d_forming_opn_lab_in_expert_mode/image0053.jpg' | relative_url }})

Time vs Load and Time vs Speed plots for primary die (Top die)

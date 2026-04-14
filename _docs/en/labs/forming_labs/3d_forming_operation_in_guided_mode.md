---
lang: en
title: "3D Forming Operation in Guided mode Lab"
---

# 3D Forming Operation in Guided mode

This lab will demonstrate how to setup a typical Forming operation of workpiece after Furnace heating in multiple operation (MO) guided mode. Forming Operation is an open environment where user can setup any Deformation, Heat transfer, Diffusion and Heat treatment problem but for new user guided mode will guide with simple and basic features for Simulation controls, Mesh Generation, Stopping and Step controls. For detailed study user can go for advanced features using expert mode once become familiar with the DEFORM.

During this lab we will attempt to highlight various guided mode features of the system that user can go with for initial studies.

1.1. Creating New Problem and Adding Operations

1.2. Operation1: Heat Transfer Heating Setup

1.3. Operation2: Forming

1.4. Running Simulation

1.5. Post Processing

## Creating New Problem and Adding Operations

### Creating New Problem

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear.

![]({{ '/assets/images/applications/55_2_arc_welding/image0002.jpg' | relative_url }})

New Problem popup

Create a new problem either by selecting **File** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear. Select "**Integrated Manufacturing Process** " radio button and unit system as "**SI** " radio button in unit field as shown in [Fig. 3DFGL1.1.]() Define Problem Name as "**3D_Forming_Operation_in_Guided_Mode** " and make sure the “Show option dialog” check box is turned on (if we do not turn on the “**Show option dialog** ” check box, then we will not get the New Project dialog in MO UI). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Deform Integrated Manufacturing Process.

Multiple operation wizard will open, at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session we use ‘**3D_Forming_Operation_in_Guided_Mode** ’ as the project name. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation. MO wizard will open (see Fig. 3DFGL1.2.), Select the **first operation** as **3D** **Heat** **transfer** operation and **check the checkbox** to add Heat transfer operation as first operation. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0002.jpg' | relative_url }})

MO Wizard New Project Opening Window

### Adding Forming operation

MO wizard will opens new project with one 3d Heat transfer operation. Add **one** **Forming** **operation** for "Steering Link" by clicking ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button as shown in Fig. 3DFGL1.3.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0003.jpg' | relative_url }})

Adding Forming Operation

## Operation1: Heat Transfer Heating Setup

For first heat transfer operation change the operation name as "**Air Transfer** " by double clicking on Operation name in Operation Editor window as shown in Fig. 3DFGL1.4. and press Enter in Keyboard.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0004.jpg' | relative_url }})

Name the first operation as Air Transfer

### Selecting Heat Transfer Type

Select "**Transfer through air** " heat transfer type for Air Transfer operation as shown in Fig. 3DFGL1.3. This will set the default heat transfer settings for heating operation. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

### Set Process Conditions

Define Transfer time as 4 sec at **20** °C environment temperature and default convection coefficient as shown in Fig. 3DFGL1.5. and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0005.jpg' | relative_url }})

Process Condition settings for air transfer

### Select Simulation Controls for air transfer

Keep only Heat Transfer mode checked as only heat transfer is modeling as shown in Fig. 3DFGL1.6. User can use Simulation controls expert mode (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})) for advanced features. As in this lab we are not using any such features click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0006.jpg' | relative_url }})

Simulation Controls settings for air transfer in guided mode

### Import material for workpiece

In Material window, load the material '**DIN-41Cr4[1450-2200F(800-1200)]** ' from DEFORM Material library, from **Steel** category using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load material data from library) option. This can be done as shown in Fig. 3DFGL1.7. by clicking on ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}) button. Material can also be load from Materials list in Explorer. Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) for Material and Object window, as only Workpiece heat transfer in air is our interest in air transfer operation.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0007.jpg' | relative_url }})

Importing Workpiece material from DEFORM library

### Define Workpiece

In Workpiece object window keep the object type as ‘**Plastic** ’ and specify workpiece temperature as **1300** °C (see Fig. 3DFGL1.8.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue and import the workpiece geometry.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0008.jpg' | relative_url }})

Workpiece Object definition

### Create Workpiece Geometry

In Geometry page, using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load Geometry from Library) button import ‘**ids_link_billet.stl** ' from installation path /3D/LABS/ as shown in Fig. 3DFGL1.9. Primitive geometry creation option also available at this stage to create the geometry.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0009.jpg' | relative_url }})

Importing geometry for workpiece

After importing any geometry click on ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) button to check the geometry, geometry checking window will appear which gives a summary of the object’s geometry (see Fig. 3DFGL1.10.). For an object that has a closed volume, there should be 1 surface, 0 free edges, and 0 invalid entities. Objects that are imported as surfaces and not solids will have a free edge but should still only have 1 surface.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0010.jpg' | relative_url }})

Checking the imported 3d geometry

### Generate Workpiece Mesh

Generate the mesh using 32000 elements (see Fig. 3DFGL1.11.). Complete range of meshing options are also available in expert mode (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})), if user needs to have more control on the mesh generated. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0011.jpg' | relative_url }})

Mesh generation for workpiece

### Assign Workpiece Material

To assign material for workpiece select the material ‘**DIN****-41Cr4[1450-2200F(800-1200)]** ’ from material window. This can be done as shown in Fig. 3DFGL1.12. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0012.jpg' | relative_url }})

Assigning material for workpiece

### Defining workpiece Boundary Conditions

In BCC page, check the default assigned Heat exchange with Environment BCC to the entire outer surface of the Billet, but in this lab we are modeled half of the steering link. So to enforce symmetry, we need to define a symmetry plane boundary condition to the +X end of the part and heat exchange with the environment boundary condition to all surfaces except the +x end of the part.

Add the **Symmetry** **BCC** to the **+X** end plane of the part by selecting the plane using selection options on left side BCC tool bar and clicking on ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) (Add BCC) button, after adding select symmetry plane vectors appears under Symmetry Planar as shown in Fig. 3DFGL1.13. to ensure the correct definition of BCC.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0013.jpg' | relative_url }})

Symmetry boundary condition definition for workpiece

Delete the automatically defined heat exchange with environment BCC by selecting the Defined branch under Heat exchange with environment and clicking on ![]({{ '/assets/icons/pre_icons/mo_delete_bcc_button.jpg' | relative_url }}) (Delete BCC) button. Then for heat exchange with environment bcc select the entire object part except symmetry plane using selection options on left side BCC tool bar and clicking on ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) (Add BCC) button. Select the Defined branch to confirm the BCC definition as shown in Fig. 3DFGL1.14.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0014.jpg' | relative_url }})

Boundary condition definition for workpiece

Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Step controls window as there is no object positioning and thermal stopping controls definition is required.

### Define Step Controls

Set the **number of simulation steps** as **50** at **0.1** sec each and **saving every** **5** steps (see Fig. 3DFGL1.15.). Advanced Simulation controls settings are available in expert mode (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to proceed to the database generation stage.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0015.jpg' | relative_url }})

Simulation controls settings for air transfer

### Generate Database

In the database generation stage user can check the data required for the analysis and proceed to generate the database (see Fig. 3DFGL1.16.). First operation of any multiple operations, user is required to generate the database. For all the subsequent operations we only need to setup the process data and simulation controls. Click on ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) to proceed to the next operation ‘Cone Forming".

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0016.jpg' | relative_url }})

Database generation window for first operation

## Operation 2: Steering Link Forming

The Forming operation runs till distance between dies reaches 400.8 mm. As workpiece is coming from air transfer operation with its thermal history, make workpiece as read from DB object and add other two objects for Top and Bottom Die to setup the steering link forming operation.

Name the operation as '**Steering Link** ' by double clicking on Operation name in Operation Editor and press Enter from Keyboard to close.

### Select Simulation Controls settings for forming

In simulation controls check both Deformation and Heat transfer simulation modes as shown in Fig. 3DFGL1.17. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until objects window to add objects as we are not simulating the die's thermal calculations and need not to define any material for dies.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0017.jpg' | relative_url }})

Simulation control settings for forming

### Add die objects

In Object window add number of objects as 3 as shown in Fig. 3DFGL1.18., as we will be bringing in all two dies at 90°C for the forming operation. We can now see the object tree is expanded to include the dies, details for which will be now be defined. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0018.jpg' | relative_url }})

Adding objects for forming

### Define Workpiece

In workpiece definition window select the object type as "**Read from DB** " as shown in Fig. 3DFGL1.19. Click on Top Die in operation tree to define the Dies.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0019.jpg' | relative_url }})

Workpiece definition window in forming

### Define Top Die

In Top die definition window accept the object type as **rigid** and specify initial temperature as **90** °C as shown in Fig. 3DFGL1.20. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0020.jpg' | relative_url }})

Top die definition window in forming

### Import Top Die geometry

In Top die Geometry window, click on ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load Geometry from Library) button and import ‘**Ids_link_top****.stl** ' from DEFORM geometry library path /3D/LABS/ (see Fig. 3DFGL1.21.). Check the imported geometry as explained for workpiece geometry earlier. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until top die movement window.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0021.jpg' | relative_url }})

Importing the multiple boundary geometry for top die

### Assigning movement controls for top die

In top die movement controls define the **hydraulic** **press** with hydraulic **speed** as **function of time**(local time) in **-Z** direction as shown in Fig. 3DFGL1.22.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0022.jpg' | relative_url }})

Hydraulic movement definition for top die

Click on ![]({{ '/assets/icons/pre_icons/mo_define_function..._button2.jpg' | relative_url }}) button next to speed and define such that from 0 to 2.04 sec press runs with speed is 10 mm/sec and from 2.0401 to 4 sec press runs with 8 mm/sec as shown in Fig. 3DFGL1.23. By default in multiple operations for function of time definitions local time will be considered so in this function time 0 till 4 seconds referring to forming operation. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to close the definition and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Bottom die definition window.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0023.jpg' | relative_url }})

Hydraulic speed defined as function of local time

### Define Bottom Die

In Bottom die definition window accept the object type as **rigid** and specify initial temperature as **90** °C as shown in Fig. 3DFGL1.24. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0024.jpg' | relative_url }})

Bottom die definition window

### Import Bottom die geometry

In Bottom die Geometry window, click on ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load Geometry from Library) button and import ‘**ids_link_bottom.stl** ' from DEFORM geometry library path /3D/LABS/ (see Fig. 3DFGL1.25.). Check the imported geometry as explained for workpiece geometry earlier. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until scheduled positioning window.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0025.jpg' | relative_url }})

Importing the multiple boundary geometry for bottom die

### Define Scheduled positioning

The dies by default are in correct position, to make sure they positioned properly define the scheduled position to top and bottom die with respect to workpiece by interference method in -Z and + Z direction respectively as shown in Fig. 3DFGL1.26. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0026.jpg' | relative_url }})

Scheduled positioning for top and bottom dies

### Defining Inter-Object relations

Select **user type** contact and click on ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) button (see Fig. 3DFGL1.29.). It will add the relationship between the Billet, Top Die and Bottom Die. As the Dies are Rigid and Billet is plastic, Top and Bottom Dies are considered as Master and Billet as Slave.

Highlight the **Top****Die – Workpiece** relationship and click the ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) button to modify the contact conditions. In the friction tab (see Fig. 3DFGL1.27.) there is a pull-down menu that allows the user to choose the appropriate friction conditions of common forming processes.

Since this is hot forming simulation and the dies are steel, use the pull down menu and select**Hot forming** from the list. A friction value of **0******.** 3** will automatically be selected.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0027.jpg' | relative_url }})

Inter-object friction coefficient definition for hot forging

In **thermal tab** select the **Forming** type pull down option, it will add the default heat transfer coefficient value **5** for forming as shown in Fig. 3DFGL1.28.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0028.jpg' | relative_url }})

Inter-object heat transfer coefficient definition for forming

Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to go back to Inter-Object window, since the friction conditions and inter-object heat transfer are the same for all the object pairs, the ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) button can be used to copy the interface properties from the first relationship to all of the others. After this is done, all relationships will have a friction factor of 0.3 and heat transfer coefficient of 5 defined as shown in Fig. 3DFGL1.29. Since the contact will initialize and generate while generating database, turn On "Initialize" and "Generate" check boxes. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0029.jpg' | relative_url }})

Inter-Object relationship definition for forming

### Define Stopping controls

In stopping control window check the **Distance between dies** stopping control and define distance value as **11.0** mm. Then from display window pick the point on big end, top and bottom die cavity centers and select the direction as**Z** as shown in Fig. 3DFGL1.30. After picking points on dies distance between dies can be observed, in this case its around 51.8. For advanced stopping options are refer Expert mode (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})), as we are not using in this lab click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0030.jpg' | relative_url }})

Distance between dies stopping control for forming

### Define Step controls

In step controls window define **number of steps** as **500** , at **0.2** mm per step of **die** **movement** , **step** **increment** **to****save** as **10** for the primary die (which is object number 2 in this simulation) as shown in Fig. 3DFGL1.31. Advanced step controls and simulation controls features are available in Expert mode (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})).

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0031.jpg' | relative_url }})

Step controls settings for forming

As database for cone forming operation will generate during simulation, so this completes the multiple forming operation setup in MO - Guided mode. To simulate the problem click on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the object tree (see Fig. 3DFGL1.33.).

## Running Simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. 3DFGL1.32. Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation. 

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0032.jpg' | relative_url }})

Run Simulation popup window

Monitor the progress of the simulation by looking at the Simulation Graphics, Simulation Message and Simulation Log tab by making sure that the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked. (See Fig. 3DFGL1.33.)

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0033.jpg' | relative_url }})

Simulation mode displaying the forming running status

After completion of the all operations in Simulation log file it gives the log message as "MULTIPLE OPERATION COMPLETED.", then switch to Post tab by clicking on ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) to view the simulation results.

## Post Processing

In post processor, Step list below the graphic area indicates step numbers available from the different operations simulated. A set of state variables available from the ‘Post’ menu can be used to review the model response. Please note that for the first operation only the thermal data for the workpiece is available. And the deformation results can be seen for the Steering link forming operation (see Fig. 3DFGL1.34.). Use the ![]({{ '/assets/icons/pre_icons/mo_box_zoom_icon.jpg' | relative_url }}) (zoom by window) icon to zoom the cone portion of the workpiece as shown in Fig. 3DFGL1.34.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0034.jpg' | relative_url }})

Strain-Effective variable contour at workpiece cone shape

Some important state variables can be selected directly from ‘Post Tools’ window and the rest can be accessed through State Variable dialog by clicking on ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) icon.

Click on ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) Graph (Load-Stroke) and plot Time (sec) vs Load (klb) and also plot Time (sec) Vs Speed (in/sec) for top die. Observe for speed change after 20.4 mm deformation from 10 in/sec to 8 in/sec as shown in Fig. 3DFGL1.35.

![]({{ '/assets/images/labs/forming_labs/3d_forming_opn_in_guided_mode/image0035.jpg' | relative_url }})

Time vs Load and Time vs Speed plots for primary die (Top die)

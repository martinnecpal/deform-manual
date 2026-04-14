---
lang: en
title: "3D Forming Operation in Expert mode Lab"
---

# 3D Forming Operation in Expert mode

This lab will demonstrate how to setup a typical Forming operation of workpiece after Furnace heating in multiple operation (MO) expert mode. Forming Operation is an open environment where user can setup any Deformation, Heat transfer, Diffusion and Heat treatment problem but for new user, guided mode will guide with simple and basic features for Simulation controls, Mesh Generation, Stopping and Step controls. For detailed study user can go for advanced features using expert mode once become familiar with the DEFORM.

During this lab we will attempt to highlight few expert mode features of the system to make user to go with expert mode for detailed studies.

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

Create a new problem either by selecting **File** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear. Select "**Integrated Manufacturing Process** " radio button and unit system as "**SI** " radio button in unit field as shown in Fig. 3DFEL1.1. Define Problem Name as "****3D_Forming_Operation_in_Expert_Mode**** " and make sure the “Show option dialog” check box is turned on (if we do not turn on the “**Show option dialog** ” check box, then we will not get the New Project dialog in MO UI). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Deform Integrated Manufacturing Process.

Multiple operation wizard will open with the New Project dialog as shown in [Fig. 3DFEL1.2](), user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session we use ‘****3D_Forming_Operation_in_Expert_Mode**** ’ as the project name. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation. MO wizard will open (see [Fig. 3DFEL1.2.]()), Select the **first operation** as **3D** **Heat** **transfer** operation and **check the checkbox** to add Heat transfer operation as first operation. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0002.jpg' | relative_url }})

MO Wizard New Project Opening Window

### Adding Forming operation

Multiple Operation wizard will opens new project with one 3d Heat transfer operation. Add one Forming operation for "Steering Link" by clicking ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button as shown in Fig. 3DFEL1.3.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0003.jpg' | relative_url }})

Adding Forming Operation

## Operation1: Heat Transfer Heating Setup

For first heat transfer operation change the operation name as "**Air Transfer** " by double clicking on Operation name in Operation Editor window as shown in Fig. 3DFEL1.4. and press Enter in Keyboard.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0004.jpg' | relative_url }})

Name the first operation as Air Transfer

### Selecting Heat Transfer Type

Select "**Transfer through air** " heat transfer type for Air Transfer operation as shown in Fig. 3DFEL1.3. This will set the default heat transfer settings for heating operation. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

### Set Process Conditions

Define **Transfer time** as **4** sec at **20** °C environment temperature and default convection coefficient as shown in Fig. 3DFEL1.5. and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0005.jpg' | relative_url }})

Process Condition settings for air transfer

### Select Simulation Controls for air transfer

In simulation controls window expert mode (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})) gets activate (see Fig. 3DFEL1.6.), select the ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) icon in the tool tab to observe the expert mode simulation control features.

Keep only Heat Transfer mode checked in the Main setting tab as only heat transfer is modeled. The operation name that was changed to "Air Transfer" is shown here as, seen in Fig. 3DFEL1.6. Other advanced features like step, stop, solver, process conditions,. etc. are available here, we will use some of these other features in mesh, stopping and step controls during the later stage of the setup. For more information about simulation controls options refer [Simulation Controls](/docs/en/pre_processor/9_simulation_controls/9_simulation_controls/). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0006.jpg' | relative_url }})

Simulation Controls settings for air transfer in expert mode

### Import material for workpiece

In Material window, load the material '**DIN-41Cr4[1450-2200F(800-1200)]** ' from DEFORM Material library, from **Steel** category using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load material data from library) option. This can be done as shown in Fig. 3DFEL1.7. by clicking on ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}) button. Material can also be loaded from Materials list in Explorer. Click the ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button until the Workpiece window.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0007.jpg' | relative_url }})

Importing Workpiece material from DEFORM library

### Define Workpiece

In Workpiece object window keep the object type as ‘**Plastic** ’ and specify workpiece temperature as **1300** °C (see Fig. 3DFEL1.8.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue and import the workpiece geometry.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0008.jpg' | relative_url }})

Workpiece Object definition

### Create Workpiece Geometry

In Geometry page, using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load Geometry from Library) button import ‘**ids_link_billet.stl** ' from installation path **/3D/LABS/** as shown in Fig. 3DFEL1.9. Primitive geometry creation option also available at this stage to create the geometry.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0009.jpg' | relative_url }})

Importing geometry for workpiece

After importing any geometry click on ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) button to check the geometry, geometry checking window will appear which gives a summary of the object’s geometry (see Fig. 3DFEL1.10.). For an object that has a closed volume, there should be 1 surface, 0 free edges, and 0 invalid entities. Objects that are imported as surfaces and not solids will have a free edge but should still only have 1 surface.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0010.jpg' | relative_url }})

Checking the imported 3d geometry

### Generate Workpiece Mesh

Complete range of meshing options are available in expert mode (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})), for air transfer operation generate the mesh using **Absolute** **mesh** generation type with Minimum element size of 1.3333 mm and **Size** **ratio** of **3** as shown in Fig. 3DFEL1.11. In the next operation we use other mesh density window and forced remeshing options. Click the ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button and select ![]({{ '/assets/icons/pre_icons/mo_no_button.jpg' | relative_url }}) for 'Default Boundary Conditions' popup asking whether to assign default boundary conditions, as we don't want to assing the Heat Exchange with environment bcc to all surfaces. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue. For more information about expert mode mesh options refer [3D Mesh](/docs/en/pre_processor/13_mesh_generation/13_2_3d_tet_mesh_generation/).

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0011.jpg' | relative_url }})

Mesh generation for workpiece

### Assign Workpiece Material

To assign material for workpiece select the material **‘DIN-41Cr4[1450-2200F(800-1200)]** ’ from material window. This can be done as shown in Fig. 3DFEL1.12. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0012.jpg' | relative_url }})

Assigning material for workpiece

### Defining workpiece Boundary Conditions

As we are modeled half of the steering link, to enforce symmetry, we need to define a symmetry plane boundary condition to the +X end of the part and heat exchange with the environment boundary condition to all surfaces except the +x end of the part.

Add the **Symmetry BCC** to the **+X** end plane of the part by selecting the plane using selection options on left side BCC tool bar and clicking on ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) (Add BCC) button, after adding select symmetry plane vectors appears under Symmetry Planar as shown in Fig. 3DFEL1.13. to ensure the correct definition of BCC.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0013.jpg' | relative_url }})

Symmetry boundary condition definition for workpiece

Then add the heat exchange with environment BCC by selecting the symmetry plane using selection options on left side BCC tool bar and clicking on ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) (Add BCC) button. Select the Defined branch to confirm the BCC definition as shown in Fig. 3DFEL1.14.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0014.jpg' | relative_url }})

Boundary condition definition for workpiece

Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Stopping controls window as there is no object positioning and thermal stopping controls definition is required.

### Check Stopping controls

In the stopping controls window in expert mode we can observe that the Transfer time 4 seconds that was defined in the Process condition window at the beginning of the setup is reflected here as Process duration stopping control as shown in Fig. 3DFEL1.15. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0015.jpg' | relative_url }})

Air transfer operation stopping control

### Define Step Controls

Set the step definition type as **time increment** of **0.1** sec constant value in **step increment** tab as shown in Fig. 3DFEL1.16.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0016.jpg' | relative_url }})

Step increment definition for air transfer

Select **simulation steps** tab to set the **number of simulation steps** as **50** at **0.1** sec each and saving **every** **5** steps as shown in Fig. 3DFEL1.17. As informed in simulation controls definition various advanced simulation controls settings are also available in step controls expert mode (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to proceed to the database generation stage.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0017.jpg' | relative_url }})

Simulation steps definition for air transfer

### Generate Database

In the database generation stage user can check the data required for the analysis and proceed to generate the database (see Fig. 3DFEL1.18.). First operation of any multiple operations, user is required to generate the database. For all the subsequent operations we only need to setup the process data and simulation controls. Click on ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) to proceed to the next operation ‘**Steering****link** ".

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0018.jpg' | relative_url }})

Database generation window for first operation

## Operation 2: Steering Link Forming

The Forming operation runs till distance between dies reaches 400.8 mm. As workpiece is coming from air transfer operation with its thermal history, make workpiece as read from DB object and add other two objects for Top and Bottom Die to setup the steering link forming operation.

Name the operation as '**Steering Link'** by double clicking on Operation name in Operation Editor and press Enter from Keyboard to close.

### Select Simulation Controls settings for forming

In simulation controls check both **Deformation** and **Heat****transfer** simulation modes as shown in Fig. 3DFEL1.19. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0019.jpg' | relative_url }})

Simulation control settings for forming

### Add die objects

In Object window add number of objects as 3 as shown in Fig. 3DFEL1.20., as we will be bringing in all two dies at 90°C for the forming operation. We can now see the object tree is expanded to include the dies, details for which will be now be defined. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0020.jpg' | relative_url }})

Adding objects for forming

### Define Workpiece

In workpiece definition window select the object type as "**Read from DB** " as shown in Fig. 3DFEL1.21. After defining dies we will define the mesh density window for workpiece at big end of the symmetric steering link, so click on Top Die in operation tree to define the Dies.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0021.jpg' | relative_url }})

Workpiece definition window in forming

### Define Top Die

In Top die definition window accept the object type as **rigid** and specify initial temperature as **90** °C as shown in Fig. 3DFEL1.22. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0022.jpg' | relative_url }})

Top die definition window in forming

### Import Top Die geometry

In Top die Geometry window, click on ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load Geometry from Library) button and import ‘**Ids_link_top****.stl'** from DEFORM geometry library path **/3D/LABS/**(see Fig. 3DFEL1.23.). Check the imported geometry as explained for workpiece geometry earlier. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until top die movement window.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0023.jpg' | relative_url }})

Importing the multiple boundary geometry for top die

### Assigning movement controls for top die

In top die movement controls define the **hydraulic press** with hydraulic**speed** as **function of time**(local time) in **-Z** direction as shown in Fig. 3DFEL1.24.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0024.jpg' | relative_url }})

Hydraulic movement definition for top die

Click on ![]({{ '/assets/icons/pre_icons/mo_define_function..._button2.jpg' | relative_url }}) button next to speed and define such that from 0 to 2.04 sec press runs with speed is 10 mm/sec and from 2.0401 to 4 sec press runs with 8 mm/sec, as this operation start after 4 second air transfer operation if user wants to maintain the global time for function definition then in simulation controls Global time must be selected for function definition. So in this lab we define the speed function of global time as shown in Fig. 3DFEL1.25. That is from 4 to 6.04 sec press runs with speed is 10 mm/sec and from 6.0401 to 8.0 sec press runs with 8 mm/sec. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the definition and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Bottom die definition window.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0025.jpg' | relative_url }})

Hydraulic speed defined as function of local time

### Define Bottom Die

In Bottom die definition window accept the object type as **rigid** and specify initial **temperature** as **90** °C as shown in Fig. 3DFEL1.26. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0026.jpg' | relative_url }})

Bottom die definition window

### Import Bottom die geometry

In Bottom die Geometry window, click on ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load Geometry from Library) button and import ‘**ids_link_bottom.stl** ' from DEFORM geometry library path /3D/LABS/ (see Fig. 3DFEL1.27.) . Check the imported geometry as explained for workpiece geometry earlier. Click on **workpiece** mesh branch in operation tree to define the mesh window for workpiece.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0027.jpg' | relative_url }})

Importing the multiple boundary geometry for bottom die

### Define Workpiece Mesh for Forming operation

At big end of symmetric steering link, we will add the mesh density window to capture state variable and metal flow more accurately. We will also define the forced remesh for every 50 steps to refine the mesh periodically. To define mesh settings, turn On "**Define mesh settings** " check box in Workpiece Mesh page, also turn On "**Perform Remesh Before This Operation** " check box to have different mesh from the beginning of the Forming operation. Select the "**Weighting Factors** " tab, activate mesh density windows by setting the weighting factor as 0.2 for Mesh windows and set Boundary curvature weighting factor to 0.4, Strain Distribution weighting factor to 0.2 and Strain rate distribution weighting factor to 0.2 as shown in Fig. 3DFEL1.28.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0028.jpg' | relative_url }})

Weighting factor settings for mesh windows

After weighting factor for mesh windows is set, Mesh windows tab is activated as shown in Fig. 3DFEL1.28. Now, select Mesh windows tab to add mesh windows and define mesh windows settings. We need Bottom Die along with Workpiece to position mesh windows, hence select Bottom Die and Workpiece to display using ![]({{ '/assets/icons/pre_icons/mo_show_user_defined_obj_icon.jpg' | relative_url }}) (user defined mode) icon below the object tree. Click on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button in Mesh windows tab to add new mesh window, select Hollow mesh density window type from mesh window types and position window over Bottom Die big end center as shown in Fig. 3DFEL1.29, specify the element size within window as 2.0 compared to elements outside window.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0029.jpg' | relative_url }})

Adding mesh density window for workpiece in forming operation

Again click on ![]({{ '/assets/icons/pre_icons/mo_show_user_defined_obj_icon.jpg' | relative_url }}) (user defined mode) icon to turn on the display of Top die along with Workpiece and Bottom Die, then drag window upward so it covers complete workpiece height as shown in Fig. 3DFEL1.30.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0030.jpg' | relative_url }})

Positioning the mesh density window

Select **remeshing****criteria** tab and define the **Maximum** **step** **increment** as **50** , so simulation hits after every 50 steps in cone forming operation as shown in Fig. 3DFEL1.31. Click on Scheduled positioning in operation tree to continue.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0031.jpg' | relative_url }})

Forced remeshing criteria used in forming

### Define Scheduled positioning

The dies by default are in correct position, to make sure they positioned properly define the scheduled position to top and bottom die with respect to workpiece by interference method in -Z and + Z direction respectively as shown in Fig. 3DFEL1.32. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0032.jpg' | relative_url }})

Scheduled positioning for top and bottom dies

### Defining Inter-Object relations

Select user type contact and click on ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) button (see Fig. 3DFEL1.35.). It will add the relationship between the Billet, Top Die and Bottom Die. As the Dies are Rigid and Billet is plastic, Top and Bottom Dies are considered as Master and Billet as Slave.

Highlight the Top Die – Workpiece relationship and click the ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) button to modify the contact conditions. In the friction tab (see Fig. 3DFEL1.33.) there is a pull-down menu that allows the user to choose the appropriate friction conditions of common forming processes.

Since this is hot forming simulation and the dies are steel, use the pull down menu and select **Hot forging (Lubricated)** from the list. A friction value of**0.3** will automatically be selected.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0033.jpg' | relative_url }})

Inter-object friction coefficient definition for hot forging

In **thermal** tab select the Forming type pull down option, it will add the default heat transfer coefficient value**5** for forming as shown in Fig. 3DFEL1.34.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0034.jpg' | relative_url }})

Inter-object heat transfer coefficient definition for forming

Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to go back to Inter-Object window, since the friction conditions and inter-object heat transfer are the same for all the object pairs, the ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) button can be used to copy the interface properties from the first relationship to all of the others. After this is done, all relationships will have a friction factor of**0.3** and heat transfer coefficient of **5** defined as shown in Fig. 3DFEL1.35. Since the contact will initialize and generate while generating database, turn on "Initialize" and "Generate" check boxes. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0035.jpg' | relative_url }})

Inter-Object relationship definition for forming

### Define Stopping controls

In stopping control window select the **Die Distance** tab to define when distance between dies reaches 11.0 mm. So enter the distance **11.0** , select the direction as **Z** and then from display window pick the point on big end, top and bottom die cavity center as shown in Fig. 3DFEL1.36. After picking points on dies distance between dies can be observed, in this case its around 51.8. Process parameters like primary die Max. load, Min. velocity and Max. stroke, Max. Strain in element and Process duration can also be used as stopping controls and also stopping plane stopping control available, this is normally used in rolling operation. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0036.jpg' | relative_url }})

Distance between dies stopping control for forming

### Define Step controls

In **step** **increment** tab select step definition as **Die** **displacement** of **0.2** mm as shown in Fig. 3DFEL1.37.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0037.jpg' | relative_url }})

Step controls settings for forming operation

Select **simulation** **steps** tab and set **number** **of****steps** as **500** and **step** **increment** **to** **save** as **10** for the primary die displacement (which is Top die, object number 2 in this simulation) as shown in Fig. 3DFEL1.38.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0038.jpg' | relative_url }})

Simulation steps definition for forming

Select **Advanced** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **Variables** tab to select the **global** time to use for function data (see Fig. 3DFEL1.39.) as we used the global time for hydraulic press speed function definition.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0039.jpg' | relative_url }})

Selecting global time for function data in cone forming

Select the **Remeshing** **criteria** tab to observe the workpiece remeshing criteria defined in workpiece mesh window as shown in Fig. 3DFEL1.40.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0040.jpg' | relative_url }})

Forming operation remeshing criteria defined for workpiece

As database for cone forming operation will generate during simulation, so this completes the multiple forming operation setup in MO - Expert mode. To simulate the problem switch to Simulation tab above the object tree. (See Fig. 3DFEL1.42.)

## Running Simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. 3DFEL1.41.Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0041.jpg' | relative_url }})

Run Simulation popup window

Monitor the progress of the simulation by looking at the Simulation Graphics, Simulation Message and Simulation Log tab, making sure that the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked. (See Fig. 3DFEL1.42.)

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0042.jpg' | relative_url }})

Simulation mode displaying the forming running status

After completion of the all multiple operation in Simulation log file it gives the log message as "MULTIPLE OPERATION COMPLETED.", then switch to Post tab to view the simulation results.

## Post Processing

In post processor Step list below the graphic area indicates step numbers available from the different operations simulated. A set of state variables available from the ‘Post’ menu can be used to review the model response. Please note that for the first operation only the thermal data for the workpiece is available. And the deformation results can be seen for the Steering link forming operation (see Fig. 3DFEL1.43.). Use the ![]({{ '/assets/icons/pre_icons/mo_zoom_icon.jpg' | relative_url }}) (zoom by window) icon to zoom the cone portion of the workpiece as shown in Fig. 3DFEL1.43.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0043.jpg' | relative_url }})

Strain-Effective variable contour at workpiece cone shape

Some important state variables can be selected directly from ‘Post Tools’ window and the rest can be accessed through State Variable dialog by clicking on ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) icon.

Click on ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) **Graph** (Load-Stroke) and plot Time (sec) vs Load (klb) and also plot Time (sec) Vs Speed (in/sec) for top die. Observe for speed change after 20.4 mm deformation from 10 in/sec to 8 in/sec as shown in Fig. 3DFEL1.44.

![]({{ '/assets/images/labs/forming_labs/3d_forming_operation_in_expert_mode/image0044.jpg' | relative_url }})

Time vs Load and Time vs Speed plots for primary die (Top die)

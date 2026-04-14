---
lang: sk
title: "3D Hot Forming Lab"
---

# 3D Hot Forming Lab

In this lab we will setup Tee forging operation in Forming Express operation.

Operation 1 : Upsetting Operation

Operation 2 : Finish Forge operation

## : Upsetting operation

### Creating a New Problem

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear, as shown in Fig. 3DHFL1.1.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0001.jpg' | relative_url }})

DEFORM GUI Main window

Create a new problem either by selecting **File** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in Fig. 3DHFL1.2. Select "**Integrated Manufacturing Process** " radio button and unit system as "**English** " radio button in unit field. Define Problem Name as " **Tee** " and make sure the “Show option dialog” check box is turned on (if we do not turn on the “**Show option dialog** ” check box, then we will not get the New Project dialog in MO UI). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

Problem type selection window

Integrated Manufacturing Process will open (see Fig. 3DHFL1.3.), at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session we will use "****Tee**** " as the project name. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0003.jpg' | relative_url }})

Problem location selection window

### Adding 3D Forming Express operation - Bush

Once you click on Finish button, a Multiple Operation wizard will open to setup the problem. **Add****3D Forming Express** operation from Operations list in Explorer. Operation can be add by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button next to 3D Forming express operation (see Fig. 3DHFL1.4.) or user can also add by drag and drop into the Operation Editor.

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0004.jpg' | relative_url }})

Added 3D Forming Express operation into Operation editor

**Change Operation Name**

Change the Operation name to "**Bush** " by double click on Forming field in Operation editor as shown in Fig. 3DHFL1.5.

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0005.jpg' | relative_url }})

Changing Operation name from Operation Editor

### Define Process settings

In **Process page** , select Process type as Hot Forging by selecting **Hot Forging** radio button. For this lab, we will simulate the whole part, by default Whole part will be selected if not select Geometry type as Whole part. The shape complexity and simulation accuracy slider bars influence the mesh settings and number of time steps used in the simulation. This in turn, influences the run time and level of details available in the simulation. For this simulation, we will use a “**Simple** ” geometry and “**Fast** ” calculations, so drag both slider bars all the way to the left as shown in Fig. 3DHFL1.6. then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0006.jpg' | relative_url }})

Process page

### Select Thermal Calculation

For this simulation, we will run with **constant temperature (isothermal)**. This means that an initial workpiece temperature will be assigned, but DEFORM will neglect any changes in temperature during the calculations. Select **Constant temperature (Isothermal)** radio button as shown in Fig. 3DHFL1.7. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0007.jpg' | relative_url }})

Thermal calculation mode selection page

### Select Number of Objects

This simulation will have 1 workpiece and 2 dies, use default selection as shown in Fig L1.8 then click .

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0008.jpg' | relative_url }})

Number of Objects window

### Workpiece General Definition

The workpiece will have an initial temperature of 2250°F, Change the **Workpiece****Temperature** to **2150°F** as shown in Fig. 3DHFL1.9\. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

**Note:** There is an “import object” button on the “object” page. This is for importing complete object data from another object data file.

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0009.jpg' | relative_url }})

Workpiece Object page

#### Import Workpiece Geometry

In Geometry page, click on Load Geometry from Library ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) button, Import **TeeBillet.stl** file as shown in Fig. 3DHFL1.10.

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0010.jpg' | relative_url }})

Import Geometry page

Check the Geometry by clicking on ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) action label. The “Geometry Checking Result” window contains a description of what constitutes a legal geometry as shown in Fig. 3DHFL1.11. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) .

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0011.jpg' | relative_url }})

Check geometry window

#### Workpiece mesh Generation

Generate mesh for the **system** type mesh settings value by click on![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) option as shown in Fig. 3DHFL1.12. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Material page.

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0012.jpg' | relative_url }})

Workpiece Mesh page

#### Assign Material for Workpiece

In Material window, load the material **AISI-316[70-2020F(20-1100C)]** from DEFORM Material library, from **Steel_at_Extended_Temperature** category using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load material data from library) option. This can be done as shown in below Fig. 3DHFL1.13. by clicking ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}) button. Material can also be loaded from Materials list in Explorer. Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top Die page.

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0013.jpg' | relative_url }})

Material window

### Top Die Definition

In Top Die page, use the default Object Temperature (**300** °F) as shown in Fig. 3DHFL1.14., Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0014.jpg' | relative_url }})

Top Die page

#### Import Top Die geometry

Click on Load Geometry from Library ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) button, Import **TeeTop.stl** file as shown in Fig. 3DHFL1.15. Then check the geometry using ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) option. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0015.jpg' | relative_url }})

Import Geometry option

#### Assign Top Die movement

Under the movement options, select speed option. Be sure movement is in the **–Z** direction and enter a **speed** of **10** in/sec as shown in Fig. 3DHFL1.16. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0016.jpg' | relative_url }})

Top Die Movement page

### Bottom Die Definition

In Bottom Die page, use the default Object **Temperature**(**300** °F), Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

#### Import Bottom Die Geometry

Click on Load Geometry from Library ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) button, Import **TeeBottom.stl** file. Then check the geometry using ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }})option. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Object Positioning

We will perform this operation with the workpiece in vertical direction. We will first position the workpiece on the bottom die. To make it easier to see, change to “**User Defined Object Display** ” mode in the control bar at the bottom of the object tree. Select Top Die in Object mode window and uncheck the check box in Visible column as shown in Fig. 3DHFL1.17., then click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0017.jpg' | relative_url }})

Object mode window to Turn of Top die in Display window

Click on ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) option object positioning will open, select ![]({{ '/assets/icons/pre_icons/mo_rotational_radio_button.jpg' | relative_url }}) positioning. Select the workpiece. Use the mouse to pick a point around the center of the workpiece, and then select the “**X** ” axis as the axis of rotation. Enter an angle of **90** degrees, and ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). The workpiece should now be positioned vertical. (See Fig. 3DHFL1.18.)

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0018.jpg' | relative_url }})

Object positioning window

Switch to ![]({{ '/assets/icons/pre_icons/mo_drag_radio_button.jpg' | relative_url }}) positioning. Click on the “**X** ” or “**Y** ” axis and use the mouse to drag the billet to a flat spot on the die, not too close to either the forming cavity or the edge of the die. Use ![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}) positioning to place the billet on the bottom die. (See Fig. 3DHFL1.19.)

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0019.jpg' | relative_url }})

Positioning the billet on the bottom die

Now click on User defined mode ![]({{ '/assets/icons/pre_icons/mo_show_user_defined_obj_icon.jpg' | relative_url }}) and check the **Top Die** visible check box, then position Top die using Interference Positioning on Billet so that it is in contact with the billet. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) and ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Contact (Inter object Relation) Definition

Select **User****defined** \- “**Hot forging (lubricated)** ” for friction condition as shown in Fig. 3DHFL1.20. and click on ![]({{ '/assets/icons/pre_icons/mo_generate_contact_nodes_label.jpg' | relative_url }}). DEFORM will automatically mark the nodes that are initially in contact with the die. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0020.jpg' | relative_url }})

Contact generation page

### Primary Die stroke definition

The primary die stroke is an estimate of the distance the die will travel during forming. This value does not have to be exact (exact stopping criteria will be specified at the next screen).

For this problem, we will upset a 3.300” billet to 1.500”. The primary die stroke is about 1.800”, so define **Total Primary die travel** as **1.8** inches as shown in Fig. 3DHFL1.21. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0021.jpg' | relative_url }})

Primary Die stroke page

### Stopping Controls Definition

We want to stop when the dies are 1.500” apart. So set “Stop Controls” to “Distance between objects". Enter a value of **1.5** ” as shown in Fig. 3DHFL1.22. Turn on shaded mesh, and select a point on the bottom surface of the top die, and a second point on the top surface of the bottom die. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0022.jpg' | relative_url }})

Stopping controls page

### Simulation Controls Definition

The number of simulation steps and step increment are established by the object shape complexity slider bar settings. If you want to change the default values, you can do it at this window. We will accept default values for this lab as shown in Fig. 3DHFL1.23., then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0023.jpg' | relative_url }})

Simulation controls

### Generate Database

In Generate DB page. Click the ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) button to have the program check to see if anything was missed in the problem setup. During the checking process:

Messages in the red color signify data that needs to be fixed before a simulation can be run (such as when you forget to define any material data). 

Click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database. When the program is done writing the database, click on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) tab to run simulation.

### Running simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. 3DHFL1.24. Use the default **Continue Run** option to select “**Continue from the last step** ” (from step -1) option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0024.jpg' | relative_url }})

Run Simulation window

The progress of the simulation can be monitored as it is running by looking at the Simulation Message tab and Simulation Graphics from the Graphics display region in Simulation mode. As long as the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked in Simulation Message tab, which is the default setting, the Message file will refresh automatically.

The Message file provides information about which simulation step the simulation is currently on and also gives information dealing with how well the simulation is running.

When the simulation is finished without any issues, check the messages in Message file, when operation completes we will see messages as ."THE DISTANCE BETWEEN TWO OBJECTS ( 2 3): 1.5000000 HAS REACHED THE SPECIFIED LIMIT 1.5000000 ".

### Post process the upsetting operation

After completion of Simulation, switch to ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) mode for post processing. Click on ![]({{ '/assets/icons/pre_icons/mo_all_button.jpg' | relative_url }}) button in Step Browser to see all saved steps as shown in Fig. 3DHFL1.25.

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0025.jpg' | relative_url }})

MO Post mode

**State Variable:**

From the state variable menu, click on ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) button, select strain effective variable, Display type as **Solid** and click on **![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }})** as shown in Fig. 3DHFL1.26, you can display line or shaded contours. It is also possible to select solid shading, or element shading. Experiment with each of these settings.

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0026.jpg' | relative_url }})

Strain - Effective State variable plot

**Point Tracking:**

Select ![]({{ '/assets/icons/post_icons/mo_point_tracking_icon.jpg' | relative_url }}) **point tracking**. Select few points on the object, and track the points using ![]({{ '/assets/icons/post_icons/mo_track_button.jpg' | relative_url }}) option (see Fig. 3DHFL1.27.). If a state variable is displayed, the values of the variables will be graphed at these points.

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0027.jpg' | relative_url }})

Point tracking

## : Finish Forge operation

After completion of simulation switch to ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}) mode.

### Add and Define 2nd operation

Add another Forming express operation to setup Finish forge operation. In this operation we are positioning the Workpiece over the cavity in Die and simulating the Finish forge operation.

**Select batch mode:**

Select 2nd operation from Operation editor, Setup type popup will appear and click on ![]({{ '/assets/icons/pre_icons/mo_no_batch_setup_button.jpg' | relative_url }}) button (Since we are setting up second operation in Batch mode).

**Change operation name:**

Change operation name to "**Finish Forge** " from Operation editor as shown in Fig. 3DHFL1.28.

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0028.jpg' | relative_url }})

Changing operation name

### Define Process settings for finishing operation

Change the object shape complexity to “**Moderate** ”. Leave accuracy at “**Fast** " as shown in Fig. 3DHFL1.29. and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Scheduled positioning page.

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0029.jpg' | relative_url }})

Process settings for finishing operation

### Scheduled positioning

Add relation by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button, select positioning object as **Workpiece** and select **Offset** option, define the **X** and **Y** value to position the workpiece on Die cavity.

Similarly add relations to position**Top die** on **Workpiece** in **-Z** direction and **Bottom****Die** below **Workpiece** in **+Z** Direction using **Interference** positioning options as shown in Fig. 3DHFL1.30. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0030.jpg' | relative_url }})

Scheduled positioning window

### Contact (Inter object Relation) Definition

Select **User****defined** \- “**Hot forging (lubricated)** ” for friction condition as shown in Fig. 3DHFL1.20. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Defining Primary Die stroke

We will forge from an initial height of 1.500” to a flash height of 0.250”, for a total stroke of 1.250”. Enter **1.25** value as the **primary****die****stroke** value as shown in Fig. 3DHFL1.31. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0031.jpg' | relative_url }})

Primary Die stroke window

### Stopping controls

We are forging to a flash thickness of 0.250". So check the Distance between objects check box, Select points on the bottom of the top die, and the top of the bottom die. Enter a stopping distance of **0.250** and Select **Z** direction as shown in Fig. 3DHFL1.32. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0032.jpg' | relative_url }})

Stopping controls window

### Simulation controls

Use the Default System Step definition values as shown in Fig. 3DHFL1.33. and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0033.jpg' | relative_url }})

Simulation controls window

### Generating DB

When user visit DB generation page, you can see the objects are positioned with respect to Scheduled positioning data, check the position of Workpiece on Die cavity is ok, then check and Generate Database (see Fig. 3DHFL1.34.), after generating Database switch to ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) mode to run the simulation.

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0034.jpg' | relative_url }})

Generate Database page

### Running simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. 3DHFL1.24. Use the default **Continue Run** option to select “**Continue from the last step** ” (from step -1) option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation. As we click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button simulation starts.

When the simulation is finished without any issues, check the messages in Message file, when operation completes we will see messages as,

“PROGRAM STOPPED!

THE DISTANCE BETWEEN TWO OBJECTS ( 2 3): 0.2500000 HAS REACHED THE SPECIFIED LIMIT 0.2500000 “.

After completion of simulation, switch to ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) mode.

### Post processing finishing operation

Play through the simulation. Did the part fill the die cavity? You may want to turn one or the other die off, or use transparency to better visualize the part.

Right click on the workpiece icon in the process tree and turn on display contact. Watch how the contact evolves as the part fills out die, see Fig. 3DHFL1.35.

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0035.jpg' | relative_url }})

Contact display to check the underfill

Plot the**load-stroke** curve as shown in Fig. 3DHFL1.36. Observe how the load increases as the part fills out the die and forms flash.

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0036.jpg' | relative_url }})

Load -Stroke Graph plot

Plot the strain rate during forming as shown in Fig. 3DHFL1.37. Observe what happens in the flash area.

![]({{ '/assets/images/labs/forming_express_labs/3d_hot_forming_lab/image0037.jpg' | relative_url }})

Strain Rate Effective state variable plot

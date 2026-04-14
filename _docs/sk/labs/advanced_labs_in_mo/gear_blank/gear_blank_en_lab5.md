---
lang: sk
title: "Gear Blank EN Lab 5"
---

# Lab 5 3D Non-isothermal Forming operation

Add the **3D****Forming****operation** as 2nd operation from **Explorer** to continue the non-isothermal forming setup. Click on the added forming operation and select ![]({{ '/assets/icons/pre_icons/mo_no_batch_setup_button.jpg' | relative_url }}) from Setup type popup to open and setup the problem in Batch mode. Change the operation name to **Forge**.

Click on **Object** in operation tree to add dies.

### Add objects

Since the workpiece object is passed to forming operation click on ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) (Add object) button twice to add placeholders for the top and bottom dies. After adding object list will display as shown in Fig. L5.1. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab5_image0001.jpg' | relative_url }})

Object list for 3d forming operation

Click on **Workpiece****Property** in operation tree to define target volume.

### Define target volume for workpiece

In Deformation Property tab check **Redefine** : **Target** volume and assign **Target Volume as Active in FEM** only. Click the ![]({{ '/assets/icons/pre_icons/mo_target_volume_icon.jpg' | relative_url }}) (Calculate Volume) button, then click ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}) to accept the recommended volume. Note that it may differ slightly from the value shown in the screen capture Fig. L5.2.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab5_image0002.jpg' | relative_url }})

Target Volume definition for workpiece

Click on **Top****die** branch in operation tree to define the dies.

### Defining Top die object

Confirm that Top Die object type is rigid and set the temperature to **300** °F. Bring in the top die from the second operation of the gear simulation that you ran above (in Project Gear). So click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to go to the Geometry window.

\- Click on ![]({{ '/assets/icons/pre_icons/mo_import_file_icon2.jpg' | relative_url }}) (Import geometry from a file) button

\- Navigate to locate “**G****ear.****DB** ” (In Project **Gear** folder)

\- Select first step (-N) in operation **2** (left column of step list, see Fig. L5.3.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab5_image0003.jpg' | relative_url }})

DB step list display for Import Geometry option

\- Press ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}).

\- Select **Top****die**(See Fig. L5.4.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab5_image0004.jpg' | relative_url }})

Object selection for import geometry option

\- Press ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}).

Click on **Top****die****Movement** branch in operation tree to define movement controls.

Assign a constant **Speed** movement of **3** in/sec in the **–Y** direction.

_Note The position of the imported top die will be corrected in _[section 5.5.](gear_blank_en.htm#5_5_Schedule_position_the_objects)__

Click on **Bottom****die** branch in operation tree to define the bottom die.

### Define Bottom die object

Similar to the Top die object definition define set the Bottom die temperature to **300** °F and import the geometry from **Gear.DB** of previous lab. 

_Note The position of the imported top die will be corrected in[section 5.5.](gear_blank_en.htm#5_5_Schedule_position_the_objects)_

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab5_image0005.jpg' | relative_url }})

Imported Top die and Bottom Die objects

Click on **Scheduled****positioning** branch under **Positioning** to schedule objects positions for forming.

### Schedule position the objects

As workpiece is created from primitive its height direction is Z but imported dies upward direction is Y, so click on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Add) button Rotate the Workpiece 90 degrees about the –X axis keeping center as (0,0,0) as shown in Fig. L5.6. to align all objects upward direction to Y. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the definition.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab5_image0006.jpg' | relative_url }})

Workpiece scheduled rotate definition

Similarly click on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Add) button twice to schedule position the tools to contact the workpiece using Interference positioning.

After adding, the scheduled positioning window lists the added scheduled position details as shown in Fig. L5.7.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab5_image0007.jpg' | relative_url }})

Scheduled positioned details for forge operation

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to the **Contact** page.

### Define inter-object relations

Click ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) button. Edit one of the relationships and apply a constant friction value of **0.3**. Visit the **Thermal****tab** and use the Constant drop down option to select **Forming**(see Fig. L5.8.). Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the definition window and click ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) to apply friction and heat transfer coefficient to other relations.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab5_image0008.jpg' | relative_url }})

Inter-object Thermal settings window

As object workpiece is read from DB object inter-object relations cannot be generated at this stage, so confirm that Scheduled Initialize and Generate contact check boxes are checked as shown in Fig. L5.9. This will initialize previous contacts and generate new contacts while running the simulation.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab5_image0009.jpg' | relative_url }})

Inter-object definition window after adding fiction and HTC

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define the stopping controls.

### Define Stopping and Step controls

Set the flash thickness to **0.2** ” by using Distance between objects option by selecting points on the flash land of top and bottom dies (See lab3 section [3.10. Define Distance between objects Stopping controls](gear_blank_en_lab3.htm#3_10_Define_Distance_between_objects_Stopping_controls)).

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define other simulation controls.

Setup the Step controls in Simulation Controls. Use **300** steps for this operation. Measure the distance between the tools to determine an appropriate die displacement value. Divide the total distance (8.0) by the number of steps (300) to get a die displacement (**0.02667**). (See Fig. L5.10.) **Save** **every****10** steps.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab5_image0010.jpg' | relative_url }})

Guided mode Simulation controls settings

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to generate database.

### Check and generate Database

Observe the schedule positioning preview in display window as shown in Fig. L5.11., if any positioning correction needed go back and correct it in scheduled positioning window. Click on the ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) button and observe the data review information in message file. Confirm that database check don't have any problem. So click on the ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate database and look for Database has been generated message.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab5_image0011.jpg' | relative_url }})

Scheduled positioning preview in DB generation window

Click on the ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode button (above the operation tree) to start the simulation.

### Run a simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog. Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

Watching the simulation graphics provides an initial idea of what to expect when opening the postprocessor. Also monitor simulation from Simulation and log messages. The message file and log file will indicate that the simulation has been completed on the last line, confirming that click on ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode button to review results.

### Review Results

**Play through results**

Use the ![]({{ '/assets/icons/pre_icons/mo_preview_play_button.jpg' | relative_url }}) (Play forward) button to play through the forging operation.

Experiment with all of the different workpiece display options ![]({{ '/assets/icons/pre_icons/mo_display_modes_options.jpg' | relative_url }}) to review the material flow. This includes ![]({{ '/assets/icons/post_icons/mo_slice.jpg' | relative_url }}) (Slicing), ![]({{ '/assets/icons/post_icons/mo_show_cotact_icon.jpg' | relative_url }}) (Contact) and ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) (field variables).

While this lab simulates quickly, the mesh is too coarse and time step is too large to resolve the defect. An indication of the fold can be seen by slicing object at last step in Z plane as shown in Fig. L5.12.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab5_image0012.jpg' | relative_url }})

Fold indication area marked by red circle

**Point tracking**

Click on ![]({{ '/assets/icons/post_icons/mo_point_tracking_icon.jpg' | relative_url }}) icon on post tools and pick two points on the workpiece with step -1 being displayed. Click on ![]({{ '/assets/icons/pre_icons/mo_settings_icon.jpg' | relative_url }}) (Settings) icon and confirm Moving point type option is selected to track the material flow. Click on ![]({{ '/assets/icons/post_icons/mo_track_button.jpg' | relative_url }}) button to start tracking the points and click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close point tracking window. (See Fig. L5.13.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab5_image0013.jpg' | relative_url }})

Point tracking definition for workpiece

Turn on contours of temperature and play the steps and observe the points tracing at center and edge temperatures. (See Fig. L5.14. and Fig. L5.15.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab5_image0014.jpg' | relative_url }})

Point tracking graph at first step

Select the last step of the simulation from the step list or last step icon. The graph tracks the temperature for each point throughout the process as a function of time. The location of these points are tracked through the simulation based on the material flow. The location can be viewed step by step.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab5_image0015.jpg' | relative_url }})

Point tracking graph at last step

Click on [Lab 6. Mechanical Press](/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab6/) to setup Lab6.

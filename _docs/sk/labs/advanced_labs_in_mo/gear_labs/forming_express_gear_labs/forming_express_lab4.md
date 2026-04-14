---
lang: sk
title: "Forming Express Lab4"
---

# Lab 4.Symmetry

### Creating a New Problem

To investigate 3D symmetry in DEFORM, open the new project with **FE_Gear_3D_Thermal_Sym** name and with **English** unit.

This project is the same as the previous **FE_Gear_3D_Thermal** ([Lab 3](/docs/sk/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/forming_express_lab3/)), with the exception that only 45° of the workpiece is modeled. For this 45° sector of the part to deform the same as the full part, symmetry boundary conditions must be used. This lab will go over the differences when setting up a simulation with symmetry.

### Add Operations

Add three operations from the Explorer:

  * [3D] Heat Transfer Express

  * [3D] Heat Transfer Express and

  * [3D] Forming Express

Double-click on the title of the first operation and change it to **Air Transfer**. Change the second operation title to**Rest on Die**. Leave the third Forming title as it is.

Right-click the **Workpiece** and **Pass object to All operations**. Similarly, right-click on the **Top Die** and **Bottom Die** and use **Pass object to Next operation** for both the objects.

### Define Air Transfer

Click on the **Air Transfer** operation. In this lab, we will use **Symmetry**. Verify that the heating type is set to **Transfer**. Leave the **Accuracy** and **Complexity** sliders at **Moderate**. (See Fig. L4.1.). In Objects page keep the **1 Workpiece only** option and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Workpiece page.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab4_image0001.jpg' | relative_url }})

Process Window

#### Define the workpiece General Data

Leave the workpiece temperature at 2250°F. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to geometry page.

#### Create Workpiece geometry from Primitive

Define the geometry as a primitive **cylinder** with a **diameter** of **5** in, **height** of **8.1** in, **Revolve****angle** as **45** degree and **corner****radius** of **0.2** in. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to assign symmetry. (See Fig. L4.2.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab4_image0002.jpg' | relative_url }})

Workpiece Geometry Primitive window

#### Assigning symmetry for Workpiece

Each of the two cut surfaces was added as a Symmetry plane by picking them with the mouse and then clicking ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}). Click each of the entries under Planar Symmetry and observe the surfaces get highlighted (See Fig. L4.3).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab4_image0003.jpg' | relative_url }})

Workpiece Symmetry window

#### Generating mesh for Workpiece

Select **User****defined** radio button and define **Target number of elements** as **10000** and Generate a mesh.

#### Assign Material for Workpiece

Click the ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load material from library) button. Select the **Steel_at_Extended_Temperatures** category, then **AISI-8620[1550-2200F(850 -1200C)]** and click the ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}) button. Click on the **AISI-8620[1550-2200F(850 -1200C)]** in the material window to assign the material to the workpiece. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to BCC page.

#### Workpiece BCC

Confirm that symmetry boundary conditions are defined on the symmetry planes, and that heat exchange with the environment is Defined on all faces except the symmetry planes. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Heat Condition page.

#### Assign Heat Condition

Set the **Transfer****time** as **5** sec, accept the default Environment temperature and Convection coefficient (See [Fig. L3.6.](forming_express_lab3.htm#Fig_L3_6_Heat_condition_window)). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Simulation controls page.

#### Simulation controls

Use default System defined simulation controls, so no changes are needed, Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to generate DB.

#### Generate Database

Click ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), If there are no errors and warnings in message tab, go ahead and click ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}).

Now click on ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) to move to Next operation.

### Rest on Die operation

For the 2nd operation, the heat transfer type will be**Rest on die**. This simulates the heat lost from the workpiece to the tool from the time it is placed on the bottom die until the press is stroked. For this operation, the workpiece should be contacting the bottom die, but the top die should be positioned some distance away from the workpiece.

Note: the Dwell on die is intended for heat transfer after forging, and uses higher heat transfer coefficients corresponding to more complete die contact.

#### Define Temperature Calculation

Use the **Calculate temperature in workpiece only** option. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Objects page.

#### Define Number of Objects

Keep **1 Workpiece + 2 dies** option. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Workpiece page.

#### Define Workpiece for Heat Resting

All workpiece data will be read from the first operation results in the database. Skip over the workpiece and move to the Top Die.

#### Top die General page

Verify that the Top Die temperature is **300** °F. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Top die geometry page.

#### Import Top die geometry

Import the top die geometry STL file “**gear top die.****STL** ” using the ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Import geometry from a file) button by browsing the geometry file path in installation folder V*_* \Tutorials directory. The die comes in oriented along a different axis than the workpiece. We will address that in a later step.

We will use a die distance stopping control when we run the forming simulation, but since the tools are defined in the current operation, reference points must also be defined now. Click on ![]({{ '/assets/icons/pre_icons/mo_define_reference_point_button.jpg' | relative_url }}) and pick a point on the flash land (See [Fig. L3.7.](forming_express_lab3.htm#Fig_L3_7_Top_die_with_the_selected_reference_point)) to select the reference point on the top die. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define bottom die.

#### Bottom die general page

Verify that the Bottom Die temperature is **300** °F. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Bottom die geometry page.

#### Import Bottom die geometry

Import the bottom die geometry STL file “**gear bottom die.****STL** ” using the ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Import geometry from a file) button by browsing the geometry file path in installation folder V*_* \Tutorials directory. The die comes in oriented along a different axis than the workpiece. We will address that in a later step.

Click on ![]({{ '/assets/icons/pre_icons/mo_define_reference_point_button.jpg' | relative_url }}) and pick a point on the flash gutter (See [Fig. L3.8.](forming_express_lab3.htm#Fig_L3_8_Bottom_die_with_the_selected_reference_point)) to select the reference point on the bottom die. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define positioning.

#### Define Positioning for Heat Resting

At this point, the workpiece is oriented along the Z axis, and the tools are oriented along the Y axis as shown in [Fig. L3.9.](forming_express_lab3.htm#Fig_L3_9_Orientation_of_does_and_Workpiece)

Click on ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) button. First, rotate the dies to be oriented along the Z axis. Set Method to **Rotational**. Set the following:

Positioning object : **Top Die**.

Axis : X

Rotation center : User-defined (0,0,0)

Angle : 90 deg.

We want to rotate both dies together, so go to the **Coupled** tab, and check **Bottom****Die**. This will couple any positioning that is done (See [Fig. L3.10.)](forming_express_lab3.htm#Fig_L3_10_Positioning_Top_die_with_Coupled_Bottom_object). Click ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) to rotate the tools to be aligned with the workpiece.

Now the tools and workpiece are all aligned along the Z axis, but the tools are too close together as shown in [Fig. L3.11.](forming_express_lab3.htm#Fig_L3_11_Objects_after_rotation_position) The next step is to move the Top Die into an "up" position away from the workpiece.

Uncheck the coupled positioning, then position the**** Top **Die** using **Offset** by **12** in. in the Z direction.

Finally, we need to make sure that the Bottom Die is contacting properly with the Workpiece. Since the Workpiece will be read from the database at this operation, we can't use regular positioning. However, we can use scheduled positioning that will be completed when the project is running. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close Object positioning dialog and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Scheduled positioning page.

#### Define Scheduled positioning for Heat Resting

Use ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) to add a scheduled positioning operation, and **Interference** position the **Bottom****Die** in the**Z** direction with the **Workpiece**.

Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) and the scheduled positioning page should show this scheduled operation (See [Fig. L3.13.](forming_express_lab3.htm#Fig_L3_13_Scheduled_positioning_window)). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Contact.

#### Define contact settings for Heat Resting

In Contact, use the default **System-defined** coefficients and tolerance settings. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define Heat Condition.

#### Define Heating condition for Heat Resting

The **Resting****time** will be **4** seconds. Accept the default temperature and convection coefficient. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to simulation controls page.

#### Define simulation controls for Heat Resting

Use the **User** define step definition and define the **time per step** as **0.1** sec, **Number of steps** as **40** and **step increment to save** as **5**. With these settings, 10 steps will be used per second, which is appropriate for a heat transfer simulation involving contact conditions. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to generate the DB.

#### DB generation for Heat Resting

Data checking will be executed. You will see a message saying, "Status: DB generation is not required for this operation. It will occur at run time." The database will be generated automatically after the first operation is completed.

### Forming Operation

Click ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) or just click on the Forming tile in the Operation Editor to set up the forming operation.

All objects will be read from the database at the end of the previous Rest on Die operation, so we only need to set:

  * Movement controls

  * Positioning

  * Inter-object relationships

  * Simulation and stopping controls

#### Assign Top die movement

Click on **Top Die Movement** page in Operation tree and set the **Speed** to a constant value of **3** in/sec in the **-Z** direction. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Scheduled Positioning page.

#### Scheduled Positioning

Click ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button and define **Interference** position between the **Top Die** to the Workpiece in the **-Z** direction. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Contact page.

#### Inter-Object relation

The default **system-defined** settings for hot forging will be used, so no changes are needed.

#### Set Primary Die Stroke Controls

In Primary die stroke page, we need to set the total die movement to something appropriate for this forming operation. The height of the billet is 8.1 in. This is a good approximate value to use. Set the **Total primary die stroke** to **8.1** in. (See [Fig. L3.14.](forming_express_lab3.htm#Fig_L3_14_Primary_die_stroke_window)) Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Stopping controls page.

#### Assign Stopping controls

Check the **Distance between objects** stopping criteria to **0.25** in, using the **Top Die** and **Bottom****Die** as the reference objects and **Z** as the direction. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define Simulation controls (See [Fig. L3.15.](forming_express_lab3.htm#Fig_L3_15_Distance_between_objects_stopping_control)).

#### Define simulation control for Forming

Use the **system** define step definition type, which will use the 1.2 times the primary die stroke value as total displacement and divide it by default **number of steps** **100** , so in this case that is, (1.2 x 8.1)/100 = 0.0972 in/step and save every **10** steps in database. (See [Fig. L3.16.](forming_express_lab3.htm#Fig_L3_16_Forming_operation_Simulation_controls_settings))

  
As informed in resting operation, Data checking will be executed and shows if there are any errors otherwise, says database will generate during run time. Save the project.

Click on the MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode button (above the operation tree) to start the simulation.

### Run and monitor a simulation

3D simulations can be made to run faster by taking advantage of multiple processors or multiple cores on one processor. If your computer processors has 4 cores, then Click the ![]({{ '/assets/icons/simulator_icons/mo_run_options_action_lable.jpg' | relative_url }}) label.

set the Simulation Mode to **Interactive** and select **Continue****Run**  
specify the MPI 3D as **4.** (See [Fig. L3.17.](forming_express_lab3.htm#Fig_L3_17_Run_option_window))

Then click on ![]({{ '/assets/icons/pre_icons/mo_save_button.jpg' | relative_url }}) button and then ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}).

As the simulation is running, click the Temperature ![]({{ '/assets/icons/post_icons/mo_temp_sv.jpg' | relative_url }}) button to view temperatures in the graphics window. It is helpful to use **Multi object mode** ![]({{ '/assets/icons/pre_icons/mo_show_multi_obj_icon.jpg' | relative_url }}) to make the dies transparent. 

Once the simulation is completed, click the MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) mode button to review results.

### Review results in Post Mode

Click the 3D Mirroring ![]({{ '/assets/icons/post_icons/mo_3d_mirroring_icon.jpg' | relative_url }}) icon. Confirm that the Add option is selected, and click on a **symmetry****plane** of the object. A mirrored symmetry object will be added. Keep clicking on the symmetry plane until the full object is created. If you make a mistake, the Delete option can be used to delete the added section (See Fig. L4.4.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab4_image0004.jpg' | relative_url }})

3D Mirroring window in MO post

Play through the steps of the simulation. Compare results to the full model. The results should be essentially the same.

Note: When plotting the load vs. stroke curve, the load displayed is only for this 45° section. The Graph ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) dialog has a Scale option that allows you to multiply the load by 8 to get the load to form the full part. (See Fig. L4.5.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab4_image0005.jpg' | relative_url }})

Load Stroke graph with scale

---
lang: en
title: "Gear Blank SI Lab 3"
---

# Lab 3. Sequential 3D Forge operation

This lab explain how to continue sequential 3D operation after converting 2D objects to 3D using 2D to 3D convertor.

### Add 3D forming operation

Click on the ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button next to 3D Forming under Forming operations list from **Explorer** tab as shown in [Fig. L3.1.](gear_blank_si_lab3.htm#Fig_L3_1_Adding_3D_forming_operation_after_2D_to_3D_convertor)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab3_image0001.jpg' | relative_url }})

Adding 3D forming operation after 2D to 3D convertor

Open the 3D forming operation from operation editor by clicking on it and select the ![]({{ '/assets/icons/pre_icons/mo_no_batch_setup_button.jpg' | relative_url }}) button for Setup type popup (see [Fig. L3.2.](gear_blank_si_lab3.htm#Fig_l3_2_Setup_type_popup_for_3rd_operation_3D_Forming)) to setup the problem in batch mode.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab3_image0002.jpg' | relative_url }})

Setup type popup for 3rd operation 3D Forming

Rename the 3D forming operation to **Forge** by clicking on title Forming in operation editor 3D forming operation and press Enter keyboard button to apply.

### Set simulation mode and Add Objects

In Simulation controls, uncheck the Heat transfer mode from simulation control main tab as this is an isothermal simulation. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Objects page.

Continue setup by adding three objects to make the place holders for a workpiece and a top and bottom die required in this operation.

Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to start defining the workpiece object.

### Workpiece object definition

Select the workpiece object type as read from DB as shown in [Fig. L3.3.](gear_blank_si_lab3.htm#Fig_L3_3_Workpiece_object_window_for_3D_forge_operation) Read from DB object will read the all object data from previous operation last step, so it reads the converted 3D object data.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab3_image0003.jpg' | relative_url }})

Workpiece object window for 3D forge operation

Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to change workpiece mesh settings.

### Change the workpiece mesh settings

****Check the**Define mesh settings** check box to change the mesh settings. Define the **size****ratio** as 2 and then select the **Absolute** type ****(see[ Fig. L3.4.](gear_blank_si_lab3.htm#Fig_L3_4_Expert_mode_general_mesh_settings_for_Read_from_DB_object)). This defines the number of elements by defining the smallest element size and a size ratio. The number of elements will increase as the complexity of the geometry increases.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab3_image0004.jpg' | relative_url }})

Expert mode general mesh settings for Read from DB object

Select the **Remesh** tab and change the interference depth to **0.7** **Relative**. (see [Fig. L3.5.](gear_blank_si_lab3.htm#Fig_L3_5_Expert_mode_remesh_criteria_settings_for_Read_from_DB_object))

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab3_image0005.jpg' | relative_url }})

Expert mode remesh criteria settings for Read from DB object

As data like material, boundary conditions are inherited from previous operation, no need to change these data. Select **Property** under workpiece in operation tree to set the target volume.

### Settings target volume to workpiece

In Deformation Property tab check **Redefine** : Target volme and assign **Target Volume as Active in FEM** only. This is the setting that should be used for most forging simulations. Click the ![]({{ '/assets/icons/pre_icons/mo_target_volume_icon.jpg' | relative_url }}) (Calculate Volume) button, then click![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}) to accept the recommended volume. Note that it may differ slightly from the value shown in [Fig. L3.6.](gear_blank_si_lab3.htm#Fig_L3_6_Target_volume_definition_in_deformation_property_window)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab3_image0006.jpg' | relative_url }})

Target volume definition in deformation property window

Click on **Geometry** under**Top die** in operation tree to continue with top die definition.

### Define Top die

Import the geometry “**gear_top_die_SI****.STL”**. Click the ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load geometry from library) button and click on ![]({{ '/assets/icons/pre_icons/mo_open_button.jpg' | relative_url }}) to open (import) the file “**gear_top_die_SI****.****STL** ”. The geometry for Top die is located in DEFORM installation folder \3D\Labs directory.

Check the geometry using ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) button and confirm that invalid edges and orientation, small area's and No. of free edges are 0 and No. of surfaces is 1 from result as shown in [Fig. L3.7.](gear_blank_si_lab3.htm#Fig_L3_7_Top_die_geometry_checking_result) This tells the geometry is clean, so click **Movement** under top die in operation tree to set top die movement controls.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab3_image0007.jpg' | relative_url }})

Top die geometry checking result

In **Movement** window set movement of constant **speed** as **76.2** mm/sec in the **–Y** direction as shown in [Fig. L3.8.](gear_blank_si_lab3.htm#Fig_L3_8_Top_die_movement_window)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab3_image0008.jpg' | relative_url }})

Top die movement window

Click on **Geometry** under **Bottom****die** in operation tree to define bottom die.

### Define Bottom die

Import “**gear_bottom_die_SI****.****STL** ” for the bottom die (object 3) from library. Check the geometry using![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) button and confirm that geometry is clean as explained in [3.6. Top die definition.](gear_blank_si_lab3.htm#3_6_Define_Top_die)

Click on **Scheduled****Positioning** under Controls in operation tree to position the objects.

### Schedule position objects

After importing new dies, they may not be in the correct position. So use Interference positioning to move the Top Die in the –Y direction until it touches the Workpiece and the Bottom Die in the +Y direction until it touches the workpiece. As the workpiece is read from DB object, this can not be position in this operation hence it must be scheduled so as to be positioned during running.

Click on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Add) button and schedule position the **Top die** by interference in **-****Y** direction with respect to **W******orkp** iece **as shown in [Fig. L3.9.](gear_blank_si_lab3.htm#Fig_L3_9_Top_die_scheduled_positioning_settings) Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the definition.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab3_image0009.jpg' | relative_url }})

Top die scheduled positioning settings

Similarly position the **Bottom die** by interference in **+Y** direction with respect to **Workpiece** using ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Add) button. After adding the scheduled positioning window list the added scheduled position details are displayed as shown in [Fig. L3.10.](gear_blank_si_lab3.htm#Fig_L3_10_Scheduled_positioned_details_for_forge_operation) Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to add the Contact.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab3_image0010.jpg' | relative_url }})

Scheduled positioned details for forge operation

### Define Contact

Assign the default inter-object relationships using ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) button. The workpiece should be slave to both the top and bottom die. For 3D simulations, self-contact (workpiece master to itself) is generally not used because it can significantly increase simulation time. Other tools are available to track folding. These will be discussed in a later lab.

Click on the ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) button for one of the relationships. Under the **Friction** ->**Value** box, use the Constant drop down menu to select**Hot forging (lubricated) 0.3**. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to exit the menu. Click on ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) to apply the friction value to the two other relationships. As the object workpiece added in relation is read from DB object inter-object can not be generated now as in lab1, so confirm that Scheduled Initialize and Generate contact check boxes are checked as shown in [Fig. L3.11.](gear_blank_si_lab3.htm#Fig_L3_11_Scheduled_Inter-object_contact_generation_settings) this will initialize previous contacts and generate new contacts while running the simulation.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab3_image0011.jpg' | relative_url }})

Scheduled Inter-object contact generation settings

Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to add stopping controls.

### Define Distance between objects Stopping controls

Select the Guided mode ![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }}), stopping criterion can be established for the flash thickness by checking the**Distance between objects** check box. This selection activates mouse picking, allowing you to pick two reference points. Select the reference points on the flash land. Slice the objects using ![]({{ '/assets/icons/pre_icons/mo_slice.jpg' | relative_url }}) (Slicing) icon along +Z direction to the point (0,0,0.001) and then select ![]({{ '/assets/icons/pre_icons/mo_plus_z_icon.jpg' | relative_url }}) icon before picking the points on flash thickness as shown in [Fig. L3.12.](gear_blank_si_lab3.htm#Fig_L3_12_Distance_between_dies_stopping_controls_definition)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab3_image0012.jpg' | relative_url }})

Distance between dies stopping controls definition

In this case it is important to pick the inside of the flash land. Select Direction**Y** to use the Y distance then enter **5.08** mm in the Die Distance between objects data field. You can visit the slicing menu again to remove the slice.

Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define simulation controls.

### Define Simulation controls

Select the ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) (Switch to expert mode) icon (from header tool bar) to access advanced simulation controls settings. Observe that Operation Number is automatically updated to 3 as shown in [Fig. L3.13.](gear_blank_si_lab3.htm#Fig_L1_13_Top_die_object_window)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab3_image0013.jpg' | relative_url }})

Step control main tab

Go to the **Step increment** tab. Determine the appropriate **Die displacement per step** (DSMAX) and the Number of Simulation Steps that you will need to close the tools. Measure the distance between the top and bottom dies using ![]({{ '/assets/icons/pre_icons/mo_measure_tool_icon.jpg' | relative_url }}) (Measurement tool) icon. When using the measure tool you can right click on the main display to select CAD Style. This will provide a measurement in a defined axis direction (X, Y or Z). Right click on the display again to select the desired axis. The Y distance between the tools is ~48.26 mm. This forging operation should take ~100 steps. Divide the total distance (48.26) by the number of steps to get a die displacement of **0.4826**. (See [Fig. L3.14.](gear_blank_si_lab3.htm#Fig_L1_14_Top_die_Geometry_window))

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab3_image0014.jpg' | relative_url }})

Step increment definition for top die

Select the Steps tab to define the **100** as **number of steps** and to save **every****5** **steps**. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to generate database.

### Check and generate Database

Click on the ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) button and observe the data review information in message file. Confirm that database check don't have any problem. So click on the ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate database and look for Database has been generated message.

Click on the ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) MO Mode button (above the operation tree) to start the simulation.

### Run multiprocessor simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog. Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

To define MPI settings, click on ![]({{ '/assets/icons/simulator_icons/mo_more_button.jpg' | relative_url }}) button, Run Options window will expand and displays options to define MPI settings for simulation (max number of processors that can be defined depend on your 3D MPI license).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab3_image0015.jpg' | relative_url }})

Run options multi processor settings

Click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) to run the simulation.

Observe the simulation graphics window and Simulation message tab to monitor the running job status as shown in [Fig. L3.16.](gear_blank_si_lab3.htm#Fig_l3_16_MO_Simulation_mode_3rd_operation_running_status)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab3_image0016.jpg' | relative_url }})

MO Simulation mode 3rd operation running status

---
lang: sk
title: "Gear Blank SI Lab 4"
---

# Lab 4. 3D Non-isothermal Air transfer operation

Create a new project named **Gear_t** in DEFORM as explained in lab1. This is a two operation simulation. Operation 1 is heat transfer only, representing movement of the workpiece from the heater to the tools. Operation 2 is forging, with temperature calculations enabled.

### Add and name operation

Add the 3D Heat Transfer operation from Explorer tab as shown in [Fig. L4.1.](gear_blank_si_lab4.htm#Fig_L4_1_Adding_3D_Heat_Transfer_operation_and_selecting_process_window_settings)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab4_image0001.jpg' | relative_url }})

Adding 3D Heat Transfer operation and selecting process window settings

Confirm Transfer through Air selected in Heat transfer window. Change the operation name to “**Transfer From Heater** ” in operation editor as shown in [Fig. L4.2.](gear_blank_si_lab4.htm#Fig_L4_2_Naming_operation_as_Transfer_From_Heater) Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab4_image0002.jpg' | relative_url }})

Naming operation as Transfer From Heater

### Define Process Condition

Set **Transfer****time** to **15** seconds (see [Fig. L4.3.](gear_blank_si_lab4.htm#Fig_L4_3_Process_condition_settings_window)), representing a 15 second transfer from the furnace (or induction coils) to the tooling. Keep the default ambient air **Environment temperature** **20** °C and **Convection****coefficient****0.02** N/sec/mm/C values and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until object window. In this operation only one object will be handled, so click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define workpiece.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab4_image0003.jpg' | relative_url }})

Process condition settings window

### Define Workpiece general object data

Set the temperature to**1******232.** 22**°C and confirm that object type is **Plastic** as shown in [Fig. L4.4.](gear_blank_si_lab4.htm#Fig_L4_4_Workpiece_object_general_definition_window) Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to create the geometry from primitive.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab4_image0004.jpg' | relative_url }})

Workpiece object general definition window

### Create 3D primitive geometry

Click on ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) to create a workpiece. Select a **Cylinder** from the icon list on the left. Define the workpiece **Diameter**(2R) as **127** mm and the **Height**(H) as **207.01** mm, with Corner radius (r) of **2.54** mm, Note that the height direction of the primitive is Z. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to create geometry. (See [Fig. L4.5.](gear_blank_si_lab4.htm#Fig_L4_5_3D_geometry_primitive_window)) 

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab4_image0005.jpg' | relative_url }})

3D geometry primitive window

Once the geometry is available geometry tools like Check, Fix, Scale, Reverse, ..etc will be available in geometry window as shown in [Fig. L4.6.](gear_blank_si_lab4.htm#Fig_L4_6_Geometry_window_options)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab4_image0006.jpg' | relative_url }})

Geometry window options

Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until mesh page.

### Generate Mesh for Workpiece

In Mesh page window change the preprocessor setup mode to Expert by using the ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) (Switch to expert mode) icon from the tool bar. Expert mode will provide more options for detailed settings. Define **Target number of Elements** as **20,000** elements and click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button. Select **Absolute** mesh type, define mesh element size as **2.5** as shown in [Fig. L4.7.](gear_blank_si_lab4.htm#Fig_L4_7_Advanced_mesh_settings), so for remeshing it uses Absolute mesh type. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to assign material.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab4_image0007.jpg' | relative_url }})

Advanced mesh settings

### Load and assign material for workpiece

Click the ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load material from library) button as shown in [Fig. L1.16.](gear_blank_si_lab4.htm#Fig_L1_16_Reversing_the_direction_of_the_geometry_orientation) Select the **Steel_at_Extended_Temperatures** category, then **AISI-8620[1550-2200F(850 -1200C)]** and click the ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}) button.

Click on **AISI-8620[1550-2200F(850 -1200C)]** to assign material for workpiece. Confirm the assigning from object tree displaying the material name next to material and in Assigned material information text above the material list as shown in [Fig. L1.11.](gear_blank_si_lab4.htm#Fig_L1_11_Object_Material_Assigning_window) Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define boundary condition.

### Define boundary condition

Define the Heat Exchange with Environment boundary condition for the workpiece. Default BCC's are assigned, If not click on the Heat Exchange with branch. Select the entire surface of the workpiece by clicking the ![]({{ '/assets/icons/pre_icons/mo_select_all_icon.jpg' | relative_url }}) (Select All) button in the Pick nodes window (on the left of the tool bar below explorer). Once you have selected the nodes, click on the ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) (add boundary condition) button. Click on the Defined branch to make sure the boundary condition is defined. (See [Fig. L4.8.](gear_blank_si_lab4.htm#Fig_L4_8_Confirming_boundary_condition_definition_by_selecting_Defined_branch))

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab4_image0008.jpg' | relative_url }})

Confirming boundary condition definition by selecting Defined branch

Click on **Step** branch in operation tree to define Step controls

### Define Step controls

Switch to Guided mode ![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }}), set **Number of Steps** as **60** , **Step****increment** as **5** steps and Solution step definition **Time** as **0.25** **sec** for Heat Transfer operation (see [Fig. L4.9.](gear_blank_si_lab4.htm#Fig_L4_9_Guided_mode_Step_controls)).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab4_image0009.jpg' | relative_url }})

Guided mode Step controls

### Generate DB and Submit to Simulate

Click on ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) and review the data checking information. Confirm no errors in data definition. Click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}). Confirm that Database is generated and run the simulation.

Click on the ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) MO Mode button (above the operation tree) to start the simulation.

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog. Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

Monitor simulation from Simulation graphics and Simulation messages. The message file and log file will indicate that the simulation has been completed on the last line. Click on ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode button to review results.

### Review Air transfer Results

After the simulation is completed, review the temperature loss in the workpiece, especially the corners.

Click on the ![]({{ '/assets/icons/post_icons/mo_temp_sv.jpg' | relative_url }}) (Plot Temperature) state variable icon from post tools. Right click on the mouse with the pointer on top the color bar and select Colorbar type / Temperature for a more realistic color selection as shown in [Fig. L4.10.](gear_blank_si_lab4.htm#Fig_L4_10_Temperature_State_variable_plot_with_color_bar_type_Temperature)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab4_image0010.jpg' | relative_url }})

Temperature State variable plot with color bar type Temperature

Click the **Summary**![]({{ '/assets/icons/post_icons/mo_summary_icon.jpg' | relative_url }}) icon. Go to the ![]({{ '/assets/icons/post_icons/mo_thermal_sv_icon.jpg' | relative_url }}) (Thermal) tab and ![]({{ '/assets/icons/post_icons/mo_plot_button.jpg' | relative_url }}) the max and min thermal values. This plots the highest and lowest temperature anywhere in the workpiece at each step as shown in [Fig. L4.11.](gear_blank_si_lab4.htm#Fig_L4_11_Temperature_summary_plot)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab4_image0011.jpg' | relative_url }})

Temperature summary plot

Click on ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}) mode button to switch to Pre mode to continue with the sequential forming operation in [Lab 5.](gear_blank_si_lab4.htm#Lab5_3D_Non-isothermal_Forming_operation)

Click on [Gear Blank SI Lab 5](/docs/sk/labs/advanced_labs_in_mo/gear_blank/gear_blank_si_lab5/) to continue with the sequential forming operation.

---
lang: en
title: "Gear Blank EN Lab 4"
---

# Lab 4. 3D Non-isothermal Air transfer operation

Create a new project named **Gear_t** in DEFORM as explained in [Lab1.](gear_blank_en.htm#Lab1_2D_upset_operation) This is a two operation simulation. Operation 1 is heat transfer only, representing movement of the workpiece from the heater to the tools. Operation 2 is forging, with temperature calculations enabled.

### Add and name operation

Add the **3D Heat Transfer** operation from Explorer tab as shown in Fig. L4.1.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab4_image0001.jpg' | relative_url }})

Adding 3D Heat Transfer operation and selecting Heat transfer type

Confirm Transfer through Air selected in Heat transfer window. Change the operation name to “**Transfer****From****Heater** ” in operation editor as shown in Fig. L4.2.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab4_image0002.jpg' | relative_url }})

Naming operation as Transfer From Heater

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to go for object window. In this operation only one object will be handled, so click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define workpiece.

### Define Process Condition

Set Transfer time to **15** seconds (See Fig. L4.3.), representing a 15 second transfer from the furnace (or induction coils) to the tooling. Keep the default ambient air **Environment****temperature****68** °F and **Convection****coefficient****7.7e-06** Btu//sec/in^2/F values and Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until object window. In this operation only one object will be handled, so click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define workpiece.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab4_image0003.jpg' | relative_url }})

Process condition settings window

### Define Workpiece general object data

Set the temperature to **2250** ° F and confirm that object type is **Plastic** as shown in Fig. L4.4.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab4_image0004.jpg' | relative_url }})

Workpiece object general definition window

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to create the geometry from primitive.

### Create 3D primitive geometry

Click on ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) to create a workpiece. Select a **Cylinder** from the icon list on the left. Define the workpiece **Diameter**(2R) as **5.00** ” and the **Height**(H) as **8.15** ”, with **Corner****radius**(r) of **0.10** ”. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to create geometry. (See Fig. L4.5.) 

_Note that the height direction of the primitive is**Z**._

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab4_image0005.jpg' | relative_url }})

3D geometry primitive window

Once the geometry is available geometry tools like Check, Fix, Scale, Reverse, ..etc will be available in geometry window as shown in Fig. L4.6.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab4_image0006.jpg' | relative_url }})

Geometry window options

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until mesh page.

### Generate Mesh for Workpiece

In Mesh page window change the preprocessor setup mode to Expert by using the ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) (switch to expert mode) icon from the tool bar. Expert mode will provide more options for detailed settings. Define target number of elements as **20,000** elements and click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button. Select **Absolute****mesh** type, define mesh element **size****ratio** as**2.5** as shown in Fig. L4.7., so for remeshing it uses Absolute mesh type.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab4_image0007.jpg' | relative_url }})

Advanced mesh settings

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to assign material.

### Load and assign material for workpiece

Click the ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load material from library) button as shown in [Fig. L1.6.](gear_blank_en_lab1.htm#Fig_L1_6_Loading_material_from_library) Select the **Steel_at_Extended_Temperatures** category, then **AISI-8620[1550-2200F(850 -1200C)]** and click the ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}) button.

Click on **AISI-8620[1550-2200F(850 -1200C)]** to assign material for workpiece. Confirm the assigning from object tree displaying the material name next to material and in Assigned material information text above the material list as shown in [Fig. L1.11.](gear_blank_en.htm#Fig_L1_11_Object_Material_Assigning_window)

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define boundary condition.

### Define boundary condition

Define the Heat Exchange with Environment boundary condition for the workpiece. Default BCC's are assigned, If not click on the Heat Exchange with branch. Select the entire surface of the workpiece by clicking the ![]({{ '/assets/icons/pre_icons/mo_select_all_icon.jpg' | relative_url }}) (Select All) button in the Pick nodes window (on the left of the tool bar below explorer). Once you have selected the nodes, click on the ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) (add boundary condition) button. Click on the **Defined** branch to make sure the boundary condition is defined. (See Fig. L4.8.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab4_image0008.jpg' | relative_url }})

Confirming boundary condition definition by selecting Defined branch

Click on **Step****branch** in operation tree to define Step controls.

### Define Step controls

Set **Number of Steps** as **60** , **Step****increment** as **5** steps and **Solution****step****definition****Time** as **0.25** sec for **Heat****Transfer****operation**(See Fig. L4.9.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab4_image0009.jpg' | relative_url }})

Guided mode Step controls

### Generate DB and Submit to Simulate

Click on ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) and review the data checking information. Confirm no errors in data definition. Click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}). Confirm that Database is generated and run the simulation.

Click on the ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode button (above the operation tree) to start the simulation.

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog. Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

Monitor simulation from Simulation graphics and Simulation messages. The message file and log file will indicate that the simulation has been completed on the last line. Click on ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode button to review results.

### Review Air transfer Results

After the simulation is completed, review the temperature loss in the workpiece, especially the corners.

Click on the ![]({{ '/assets/icons/post_icons/mo_temp_sv.jpg' | relative_url }}) (Plot Temperature) state variable icon from post tools. Right click on the mouse with the pointer on top the color bar and select Colorbar type / Temperature for a more realistic color selection as shown in Fig. L4.10.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab4_image0010.jpg' | relative_url }})

Temperature State variable plot with color bar type Temperature

Click the Summary ![]({{ '/assets/icons/post_icons/mo_summary_icon.jpg' | relative_url }}) icon. Go to the ![]({{ '/assets/icons/post_icons/mo_thermal_sv_icon.jpg' | relative_url }}) (Thermal) tab and ![]({{ '/assets/icons/post_icons/mo_plot_button.jpg' | relative_url }}) the max and min thermal values. This plots the highest and lowest temperature anywhere in the workpiece at each step as shown in Fig. L4.11.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab4_image0011.jpg' | relative_url }})

Temperature summary plot

Click on ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}) mode button to switch to Pre mode to continue with the sequential forming operation in [Lab 5.](/docs/en/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab5/)

Click on [Lab 5. 3D Non-isothermal Forming operation](/docs/en/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab5/) to setup sequential forming operation.

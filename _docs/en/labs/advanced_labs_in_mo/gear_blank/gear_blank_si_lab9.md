---
lang: en
title: "Gear Blank SI Lab 9"
---

# Lab 9. Hydraulic Press

### Duplicate Project

Start DEFORM and create a new project named **Gear_p**.

Add **3D****Forming** operation and click on ![]({{ '/assets/icons/pre_icons/mo_import_icon.jpg' | relative_url }}) (Import database) in the File menu. Open the “**Gear.DB** ” file. Select the first step of the third (Forge) operation and click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}).

### Define simulation Controls

In this lab we show how to setup Hydraulic press controls for a non-isothermal simulation with heat transfer calculations for both workpiece and dies. So in Simulation controls check **Heat****Transfer** check box status if not turned on, turn on the Heat Transfer checkbox.

### Define Boundary condition for Workpiece

Click on **Workpiece Boundary condition** branch and define **Heat exchange with environment boundary condition** for entire object using ![]({{ '/assets/icons/pre_icons/mo_select_all_icon.jpg' | relative_url }}) (Select all) icon, if system not assigned automatically.

### Define Heat transfer with Top die

Click on Top die branch in operation tree and set temperature to **148.889** **°C**.

We will mesh both tools in order to simulate the temperature of the die. Click on the Top Die **Mesh** branch in operation tree and set **20000** elements. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) and click the ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load material from library) button and select the **Die_material** category, then **AISI-H-13**. Assign the loaded material by selecting it in material list.

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) and define Heat exchange with environment boundary condition for entire object except top surface as shown in [Fig. L9.1.](gear_blank_si_lab9.htm#Fig_L9_1_Top_die_Heat_exchange_with_environment_boundary_condition_surfaces)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab6_image0001.jpg' | relative_url }})

Top die Heat exchange with environment boundary condition surfaces

### Define Hydraulic Press

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to change the movement controls for Top die. Select **Hydraulic** press from the top row of radio buttons. Enter:

\- **Speed**(Constant): **63.5** mm/sec (See [Fig. L9.2.](gear_blank_si_lab9.htm#Fig_L9_2_Hydraulic_press_movement_definition_main_tab))

\- **Check****Power****limit** and enter **data** using**![]({{ '/assets/icons/pre_icons/mo_define..._button2.jpg' | relative_url }}) **button as shown in below [Fig. L9.3.](gear_blank_si_lab9.htm#Fig_L9_3_Power_limit_definition)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab9_image0002.jpg' | relative_url }})

Hydraulic press movement definition main tab

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab9_image0003.jpg' | relative_url }})

Power limit definition

Input a stopping limit (max load of primary die) of **17792880** N in the Y direction. So, select **Dwell** controls tab and define **Maximum****load** as 17792880 N in **Y** data field as shown in [Fig. L9.4.](gear_blank_si_lab9.htm#Fig_L9_4_Hydraulic_press_stopping_load_defined_in_dwell_controls_tab)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab9_image0004.jpg' | relative_url }})

Hydraulic press stopping load defined in dwell controls tab

### Define Heat transfer with Bottom die

Similar to Top die Heat transfer definition define Bottom die initial Temperature to **148.889** ° C and Mesh of **50000** Elements. (See [Section 6.4 Define Heat transfer with Top die](gear_blank_si_lab6.htm#Fig_L6_4_Top_and_bottom_die_contact_with_workpiece))

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) and select **AISI-H-13** from material list to assign material. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define the Heat exchange with environment boundary condition and select all surfaces except bottom surface as shown in [Fig. L9.5.](gear_blank_si_lab9.htm#Fig_L9_5_Bottom_die_Heat_exchange_with_environment_boundary_condition_surfaces)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab6_image0003.jpg' | relative_url }})

Bottom die Heat exchange with environment boundary condition surfaces

Click on **Contact** in operation tree to define inter-object relation ship.

### Define Inter-object relation ship

Click on ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) for any relation and add **heat****transfer****coefficient** of **11** N/s/mm/C. Click on ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) to add for other relationships. Click the ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) (Tolerance) button followed by the ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) button (at bottom of the inter-object window). You should see the contact nodes on the workpiece where contact has been generated. See [Fig. L9.6.](gear_blank_si_lab9.htm#Fig_L9_6_Top_and_bottom_die_contact_with_workpiece) for how the Inter object window looks and contact generation displays in graphics window.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab6_image0004.jpg' | relative_url }})

Top and bottom die contact with workpiece

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define stopping controls.

### Define Stopping and Simulation controls

The Stopping controls maximum load of primary die (**17792880** N) defined in primary die movement controls is reflected in stopping controls. **Uncheck** the **Distance between die** stopping controls imported from DB.

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) and keep the step controls definition imported from DB.

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to check and generate DB.

### Generate Database and Run the simulation

Check and Generate database and click on the ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode button (above the operation tree) to start the simulation.

Run simulation, after completing running click on ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode button to review results.

### Review Results

In the postprocessor, go to the ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) [Graph (load-stroke)] plot, and plot the Top die velocity (Y speed) vs. Stroke.

Plot the Y Load vs. Time.

Note the temperature buildup in the die cavity near the surface. 

* * *

Optional exercise – time permitting

\- Compare the maximum load with the simulation using a constant speed approximation.

\- Compare the process time with the simulation using a constant speed approximation.

\- Rerun the **Gear** problem with meshed tooling and by turning on **Heat transfer** check box option. Use the same inputs for the die mesh, material and temperature. Compare the temperature on the center surface of the bottom die between a constant speed approximation and this case using a hydraulic press model.

\- Export graph data and import into Excel or another program. You can right click on any graph and select **Export graph data** to create a text file output.

* * *

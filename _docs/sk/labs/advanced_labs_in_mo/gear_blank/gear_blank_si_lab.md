---
lang: sk
title: "Gear Blank SI Lab 8"
---

# Lab 8. Screw Press

### Duplicate Project

Start DEFORM and create a new project named **Gear_s**.

Add 3D Forming operation and click on ![]({{ '/assets/icons/post_icons/mo_import_icon.jpg' | relative_url }}) (Import database) in the File menu. Open the “**Gear.DB** ” file. Select the first step of the third (Forge) operation and click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}).

### Define simulation Controls

In this lab we show how to setup Screw press controls for a non-isothermal simulation with heat transfer calculations for both workpiece and dies. So in Simulation controls check Heat Transfer check box status if not turned on, turn on the Heat Transfer checkbox.

### Define Boundary condition for Workpiece

Click on the **Workpiece Boundary condition** branch and define Heat exchange with environment boundary condition for entire object using ![]({{ '/assets/icons/pre_icons/mo_select_all_icon.jpg' | relative_url }}) (Select all) icon, if system not assigned automatically.

### Define Heat transfer with Top die

Click on Top die branch in operation tree and set temperature to **148.889** °C.

We'll mesh both tools in order to simulate the temperature of the die. Click on Top die **Mesh** branch in operation tree and set **20000** elements. Click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}).

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) and click the ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load material from library) button and select the **Die_material** category, then **AISI-H-13**. Assign the loaded material by selecting it in material list.

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) and define Heat exchange with environment boundary condition for entire object except top surface as shown in Fig. L8.1.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab6_image0001.jpg' | relative_url }})

Top die Heat exchange with environment boundary condition surfaces

### Define Screw Press

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to change the movement controls for Top die. Select **Screw press** from the top row of radio buttons. Enter:

\- **Energy** : 209021951.8 N-mm.

\- **Efficiency** : .80 (80%)

\- **Moment of inertia** : 8756325.007 N-mm-s^2

\- **Lead screw pitch** : 381 mm/rev. (See Fig. L8.2.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab8_image0002.jpg' | relative_url }})

Screw press movement definition for top die

### Define Heat transfer with Bottom die

Similar to Top die Heat transfer definition define Bottom die initial Temperature to **148.889** °C and Mesh of **50000** Elements. (See [Section 6.4 Define Heat transfer with Top die](gear_blank_si_lab6.htm#Fig_L6_4_Top_and_bottom_die_contact_with_workpiece))

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) and select **AISI-H-13** from material list to assign material. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define the Heat exchange with environment boundary condition and select all surfaces except bottom surface as shown in Fig. L8.3.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab6_image0003.jpg' | relative_url }})

Bottom die Heat exchange with environment boundary condition surfaces

Click on **Contact** in operation tree to define inter-object relation ship.

### Define Inter-object relation ship

Click on ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) for any relation and add heat transfer coefficient of **11**. Click on ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) to add for other relationships. Click the ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) (Tolerance) button followed by the ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) button (at bottom of the inter-object window). You should see the contact nodes on the workpiece where contact has been generated. See Fig. L8.4. for how the Inter object window looks and contact generation display in graphics window.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_si/lab6_image0004.jpg' | relative_url }})

Top and bottom die contact with workpiece

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define stopping controls.

### Define Stopping and Simulation controls

Keep the Distance between die stopping controls imported from DB.

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) and keep the step controls definition imported from DB.

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to check and generate DB.

### Generate Database and Run the simulation

Check and Generate database and click on the ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode button (above the operation tree) to start the simulation.

Run simulation, after completing running click on ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode button to review results.

### Review Results

In MO postprocessor, go to the [Graph (load-stroke)] plot, and plot the Top die velocity (Y speed) vs. Stroke for the second operation.

Plot the Y Load vs. Time and energy vs. stroke.

Turn on die contact and note the slight unfill as the press runs out of energy.

* * *

Optional exercise – time permitting

\- Compare the maximum load with the simulation using a constant speed approximation.

\- Compare the process time with the simulation using a constant speed approximation.

\- Rerun the **Gear** problem with meshed tooling and by turning on **Heat****transfer** check box option. Use the same inputs for the die mesh, material and temperature. Compare the temperature on the center surface of the bottom die between a constant speed approximation and this case using a screw press model.

\- Export graph data and import into Excel or another program. You can right click on any graph and select Export graph data to create a text file output.

* * *

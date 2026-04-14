---
lang: en
title: "Gear Blank EN Lab 6"
---

# Lab 6 Mechanical Press

### Duplicate Project

Start DEFORM and create a new project named **Gear_m**.

Add 3D Forming operation and click on ![]({{ '/assets/icons/pre_icons/mo_import_icon.jpg' | relative_url }}) (Import database) in the File menu. Open the “**Gear.****DB** ” file. Select the first step of the **third**(forge) operation and click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}).

### Define simulation Controls

In this lab we show how to setup the Mechanical press controls for a non-isothermal simulation with heat transfer calculations for both the workpiece and dies. In Simulation controls by default Heat Transfer check box will be in turned on, if not **turn****on** the **Heat****Transfer** check box.

### Define Boundary condition for Workpiece

Click on the **Workpiece****Boundary****condition** branch and define Heat exchange with environment boundary condition for entire object using ![]({{ '/assets/icons/pre_icons/mo_select_all_icon.jpg' | relative_url }}) (Select all) icon, if the system has not automatically assigned it.

### Define Heat transfer with Top die

Click on **Top****die** branch in operation tree and set temperature to **300** ° F.

We'll mesh both tools in order to simulate the temperature of the die. Click on the **Top****die****Mesh** branch in the operation tree, set **20000** elements and click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}).

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) and click the ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load material from library) button and select the **Die_material** category, then **AISI-H-13**. Assign the loaded material by selecting it in material list.

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) and define Heat exchange with environment boundary condition for entire object except top surface as shown in Fig. L6.1.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab6_image0001.jpg' | relative_url }})

Top die Heat exchange with environment boundary condition surfaces

### Define Mechanical Press

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to change the movement controls for Top die. Select **Mechanical****press** from the top row of radio buttons. Enter:****

**\- Total stroke** : **12.0****** [this represents the total ram stroke from top dead center to bottom dead center]****

**\- Forging****stroke** : **1.575** [this represents the top die stroke form the current position to bottom dead center]

**-****Cycles/sec** : **1.0** [this represents a flywheel rotation of 60 RPM] (See Fig. L6.2.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab6_image0002.jpg' | relative_url }})

Mechanical press movement definition for top die

### Define Heat transfer with Bottom die

Similar to Top die Heat transfer definition define Bottom die initial Temperature to **300** °F and Mesh of **50000** Elements. (See Section 6.4 Define Heat transfer with Top die)

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) and select **AISI-H-13** from material list to assign material. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define the **Heat exchange with environment boundary condition** and select all surfaces except bottom surface as shown in Fig. L6.3.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab6_image0003.jpg' | relative_url }})

Bottom die Heat exchange with environment boundary condition surfaces

Click on **Contact** in operation tree to define inter-object relationship.

### Define Inter-object relation ship

Click on ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) for any relation and add **heat****transfer****coefficient** of **0.004**. Click on![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) to add for other relationships. Click the ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) (Tolerance) button followed by the ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) button (at bottom of the inter-object window). You should see the contact nodes on the workpiece where contact has been generated. See Fig. L6.4. for how the Inter object window looks and contact generation displays in graphics window.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab6_image0004.jpg' | relative_url }})

Top and bottom die contact with workpiece

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define stopping controls.

### Define Stopping and Simulation Step controls

Add a **stopping****criteria** to stop the simulation when the stroke reaches **12** (Max Die Stroke) in **Y** direction field as shown in Fig. L6.5. and **uncheck** the **Distance****between****objects** stopping controls.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab6_image0005.jpg' | relative_url }})

Maximum primary die displacement stopping controls

Keep the **Step****controls** settings imported from DB and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to check and generate DB.

### Generate Database and Run the simulation

Check and Generate database and click on the ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode button (above the operation tree) to start the simulation.

Run simulation, after completing running click on ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode button to review results.

### Review Results

In MO postprocessor, go to the load-stroke ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) plot and plot the punch Velocity (Y speed) vs. Stroke.

Plot the load vs. time for primary die.

* * *

Optional exercise – time permitting

\- Compare the maximum load with the simulation using a constant speed approximation.

\- Compare the process time with the simulation using a constant speed approximation.

Rerun the **Gear** problem with meshed tooling and by turning on **Heat transfer** check box option. Use the same inputs for the die mesh, material and temperature. Compare the temperature on the center surface of the bottom die between a constant speed approximation and this case using a mechanical press model.

\- Export graph data and import into Excel or another program. You can right click on any graph and select Export graph data to create a text file output.

* * *

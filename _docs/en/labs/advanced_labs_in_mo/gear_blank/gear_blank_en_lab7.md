---
lang: en
title: "Gear Blank EN Lab 7"
---

# Lab 7 Hammer

### Duplicate Project

Start DEFORM and create a new project named **Gear_h.**

Add **3D Forming Express** operation and click on ![]({{ '/assets/icons/pre_icons/mo_import_icon.jpg' | relative_url }}) (Import database) in the File menu. Open the “**Gear.****DB** ” file. Select the first step of the **third**(forge) operation and click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}).

### Define process setup

In this lab we show how to setup Hammer controls for a non-isothermal simulation with heat transfer calculations for both workpiece and dies. So select **Hot****forging** as process type (See Fig. L7.1.). This activates the Heat transfer mode.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab7_image0001.jpg' | relative_url }})

Process settings selection window

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) and select **Calculate temperature in workpiece and dies** (See Fig. L7.2.). This adds mesh and Boundary condition windows for dies.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab7_image0002.jpg' | relative_url }})

Temperature calculation settings window

### Define Boundary condition for Workpiece

Click on **Workpiece****Boundary** condition branch and define **Heat exchange with environment boundary condition** for entire object using ![]({{ '/assets/icons/pre_icons/mo_select_all_icon.jpg' | relative_url }}) (Select All) icon, if system not automatically assigned.

### Define Heat transfer with Top die

Click on **Top****die** branch in operation tree and set temperature to **300** °F.

We'll mesh both tools in order to simulate the temperature of the die. Click on **Mesh** branch in operation tree and set **20000****elements** using **User****defined** option. Click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}).

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) and click the ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load material from library) button and select the **Die_material** category, then **AISI-H-13**. Assign the loaded material by selecting it in material list.

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) and define Heat exchange with environment boundary condition for entire object except top surface as shown in Fig. L7.3.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab7_image0003.jpg' | relative_url }})

Top die Heat exchange with environment boundary condition surfaces

### Define Hammer Controls

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to change the movement controls for Top die. Select **Hammer** from the top row of radio buttons. (See Fig. L7.4.) Enter:

\- **Energy** : **500** klb.-in.

\- **Mass** : **0.025** ~ (10,000 lbs)

\- **Efficiency** : **0.85**(85%)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab7_image0004.jpg' | relative_url }})

Mechanical press movement definition for top die

Check **Use blow** table checkbox and click on ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) (Define) button next to use blow table checkbox. Define dwell time as **0.5** sec for Blow 1 and add 4 more hits using **No. Hits** increment button. This adds other 4 blows with same values as shown in Fig. L7.5. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the multiple blows definition.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab7_image0005.jpg' | relative_url }})

Multiple blow definition table

### Define Heat transfer with Bottom die

Similar to Top die Heat transfer definition define Bottom die initial Temperature to **300** °F and Mesh of **50000****Elements**. (See Section 7.4 Define Heat transfer with Top die)

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) and select **AISI-H-13** from material list to assign material. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define the Heat exchange with environment boundary condition and select all surfaces except bottom surface as shown in Fig. L7.6.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab7_image0006.jpg' | relative_url }})

Bottom die Heat exchange with environment boundary condition surfaces

Click on **Contact** in operation tree to define inter-object relationship.

### Define Inter-object relation ship

Select **User defined radio** button and assign **Shear** friction of **0.3** and heat transfer conduction coefficient as **0.004**. Click on ![]({{ '/assets/icons/pre_icons/mo_generate_contact_nodes_label.jpg' | relative_url }}) to generate contact with heat transfer coefficient with friction as shown in Fig. L7.7.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab7_image0007.jpg' | relative_url }})

Forming express contact generation window

You should see the contact nodes on the workpiece where contact has been generated. See Fig. L7.8. how the Inter object window looks and contact generation displays in graphics window. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define Total primary die travel.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab7_image0008.jpg' | relative_url }})

Top and bottom die contact with workpiece

### Define Primary Die travel

Define Primary Die travel as **1.575** in Total primary die travel field and check **Exact****amount****check****box** , then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define stopping controls.

### Define Stopping and Simulation controls

Keep the Distance between die stopping controls imported from DB. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Define Simulation controls

Observe the step controls definition imported from DB. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Generate DB.

### Generate Database and Run the simulation

Check and Generate database and click on the ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode button (above the operation tree) to start the simulation.

Run simulation, after completing running click on ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode button to review results.

### Review Results

In MO post processor, go to the **load-stroke** ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) plot and plot the punch Velocity (Y speed) vs. Stroke for the first, third and ninth operation (select 1, 3 & 9 from combo box in bottom). Plot Energy vs. Time for each of these forming operations as well.

Plot the Y Load vs. Time for the entire process (all operations). Turn on die contact and note the slight underfill.

* * *

Optional exercise – time permitting

\- Compare the maximum load with the simulation using a constant speed approximation.

\- Compare the process time with the simulation using a constant speed approximation.

\- Rerun the **gear** problem with meshed tooling and the **Calculate temperature in workpiece and dies (non-isothermal) temperature calculation** settings. Use the same inputs for the die mesh, material and temperature. Compare the temperature on the center surface of the bottom die between a constant speed approximation and this case using a hammer model.

\- Export graph data and import into Excel or another program. You can right click on any graph and select Export graph data to create a text file output.

* * *

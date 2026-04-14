---
lang: en
title: "Forming Express Lab8"
---

# Lab 8. Hammer Forging

### Creating New Problem

Create a new project called **FE_Gear_Hammer**. Check First operation check box and set it to **[2D] Multi Blow Forging**. The Unit system should be **English**.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab8_image0001.jpg' | relative_url }})

New Problem Window

### Process

On the **Process** page, set the **Energy** to **150** Klb-in. This is the maximum hammer energy. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Blow Table.

### Blow Table

For the Hit 1, set **% Blow** to **50** and the **Efficiency** to**0.7**.

Note: The “No. Hits” field updates the table immediately. It is easy to accidently overwrite previously defined hits if you try typing in the number manually. For this reason, it is recommended to use the up/down arrows to adjust number of hits for this operation.

Increase the No. Hits to 2 using the up arrow. Set the % Blow energy to 100 for hit 2, then click the up arrow to increase the No. Hits to 10. This blow table contains a light first blow then nine full energy blows (see Fig. L8.2.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Geometry Type.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab8_image0002.jpg' | relative_url }})

Blow Table window

At this point, we will import a previously set-up model from a different project. Go to **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Import** and open **FE_Gear_LargerBillet.DB.** Select the **first**(negative) **step** of **Operation****2**. It should be around step **101** , Click **No** for Global/Local Time popup asking "Do you want to use new time definition?" for Global time. This option initialize the global time from the DB to zero. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top die movement page.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab8_image0003.jpg' | relative_url }})

Step selection window

### Top Die Movement

The movement in the dialog should be defined as **Hammer** with an Energy of **150** Klb-in.

Click the Mass calculator ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) icon. Enter a mass of **1000** pounds. The system will convert the mass to DEFORM consistent units. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Generate DB page.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab8_image0004.jpg' | relative_url }})

Hammer movement window

### Generating DB

Go to Generate DB page and generate the database. Click on the MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode button (above the operation tree) to start the simulation.

### Run and monitor a simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog. Use the default **Continue****Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** radio button. Click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

### Review the results

When the simulation is completed, click the MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode button to review results.

Play the steps and note that the dies do not fill and the simulation stops after all the blows are completed. (See Fig. L8.5.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab8_image0005.jpg' | relative_url }})

Last of last blow operation step

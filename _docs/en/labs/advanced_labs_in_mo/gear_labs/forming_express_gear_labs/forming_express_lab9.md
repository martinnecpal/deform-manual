---
lang: en
title: "Forming Express Lab9"
---

# Lab 9. Screw Press

### Create a new Problem

Create a new project called **FE_Gear_Screw** and copy the existing project **FE_Gear_LargerBillet** along with the database. Click on the Upset operation and go to Top Die Movement page.

We will use a **screw****press** with maximum energy 3450 Klb-in., a flywheel moment-of-inertia (MOI) of 250 Klbin-s^2 and a lead screw pitch of 4 in/rev.

We will use reduced energy for the first hit (Upset), and full energy for the 2nd hit (Forming).

### Define Top die movement for Upset

Click on the **Upset** operation tile. Select **Screw****press** type movement for **Top****die** movement, Set the **Energy** to **1000** , the **Moment of inertia** to **250** , the **Lead****screw****pitch** to **4** and the **efficiency** to **0.6**. (See Fig. L9.1.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab9_image0001.jpg' | relative_url }})

Screw press controls for Upset

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Generate DB page.

### Generate DB

Generate the Database and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until next operation Top die movement page.

### Define Top die movement for Forming

Use the same movement defined in first operation (see section 9.2.), except the full **Energy** of **3450**. We will use energy of 3450 klb-in for this operation. (See Fig. L9.2.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab9_image0002.jpg' | relative_url }})

Screw press control for Forming

### Define the Primary die stroke and Step controls

As we defined less energy in 1st operation we will not achieve expected 6.5 in upset, so we will define larger primary die stroke to get the required displacement in 2nd operation. Change the **primary****die****stroke** to **5** in.

Save the project and click on the MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode button (above the operation tree) to start the simulation.

### Run and monitor a simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog. Use the default **Continue****Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** radio button. Click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

Note that Operation 1 ends when the flywheel energy is expended. Operation 2 stops on the predefined stopping control.

### Review the results

When the simulation is completed, click the MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode button to review results.

**Graph**

In the Post-processor, use the Graph ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) tool to plot **Y** -**Speed** vs. Time to review ram speed decay as the part is formed. (See Fig. L9.3.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab9_image0003.jpg' | relative_url }})

Y-Speed vs Time graph plot

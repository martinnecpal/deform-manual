---
lang: sk
title: "Forming Lab 9"
---

# Lab 9. Screw Press

### Create a new Problem

Create a new project called **Gear_Screw** and copy the existing project **Gear_LargerBillet**. Click on the **Upset** operation and go to **Top****Die** Movement page.

### Top die movement

We will use a screw press with maximum energy **3450** Klb-in., a flywheel moment-of-inertia (MOI) of 250 Klbin-s^2 and a lead screw pitch of 4 in/rev.

We will use reduced energy for the first hit, and full energy for the 2nd hit.

Select **Screw****press****type** movement for **Top****die** movement, set the **Energy** to **1000** , the **Moment****of****inertia** to **250** the **Lead****screw****pitch** to **4** as shown in Fig. L9.1. Define the **efficiency** as a **function****of****force** according to this table and Fig. L9.2.

**Force** |  **Screw Press Efficiency**  
---|---  
0 |  0.9  
1.0e3 |  0.8  
1.0e4 |  0.7  
1.0e5 |  0.6  
1.0e6 |  0.5  
1.0e7 |  0.2  
  
![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab9_image0001.jpg' | relative_url }})

Top die Screw press movement window

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab9_image0002.jpg' | relative_url }})

Function of Force Blow efficiency window

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Generate DB page.

### Generate DB

Generate the Database and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Next operation **Top****die****movement** page.

### Forming operation

**Top die movement**

Use the same movement defined in first operation (see section 9.2), except use the full Energy of **3450** Klb-in.

Save the project and click on the MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode button (above the operation tree) to start the simulation.

### Run and monitor a simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog. Use the default **Continue****Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** radio button. Click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

Note that Operation 1 ends when the flywheel energy is expended. Operation 2 stops on the predefined stopping control.

### Review the results

When the simulation is completed, click the MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode button to review results.

**Graph**  
In the Post-processor, use the Graph ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) tool to plot **Y-Speed** vs. **Time** to review ram speed decay as the part is formed. (See Fig. L9.3.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab9_image0003.jpg' | relative_url }})

Y-Speed vs Time graph plot

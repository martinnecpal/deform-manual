---
lang: en
title: "Forming Express Lab7"
---

# Lab 7. Hydraulic Press

There are two ways to model hydraulic press behavior:

  1. Assume press maintains constant speed until it hits maximum load, then dwells at maximum load (two-step method).

  2. Assume press slows gradually as it approaches maximum load (power envelope method).

The two-step method is easier to set up and is useful for force-controlled simulations other than hydraulic presses. The power envelope method is more representative of actual hydraulic press behaviour.

### Two-step method

#### Create a new Problem

Create a new project called **FE_Gear_Hydraulic_Dwell** and copy the existing project **FE_Gear_LargerBillet**. Be sure the **Copy****database****file****option** is **checked**. Click on the **2nd** operation and go to **Top****Die** Movement.

#### Assign Top die movement

Set the movement to **Hydraulic****press** and set the **Speed** to a **constant****2** in/sec. Once the press hits the maximum press load (4000 klb.), we will dwell for 3 seconds. A good rule of thumb is 100 steps per second of dwelling, so we will use 300 steps. We will define the Max load in next step at Stopping controls page.

Set the **Total****dwell** time to **3** seconds as shown in Fig. L7.1. The time will be updated by the system once the dwell load is reached. Click on **Stopping****controls** branch in object tree to define stopping controls.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab7_image0001.jpg' | relative_url }})

Hydraulic movement with dwell controls

#### Define Stopping Controls

**Uncheck****Distance****between****objects** and **check****Max****load**. Set the **load** value to **4000** klb. (See Fig. L7.2.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab7_image0002.jpg' | relative_url }})

Hydraulic press max load to start the dwell

#### Generating DB

Go to **Generate****DB** page and generate the database. Click **Yes** to the Lost Steps popup informing that 2nd operation existing steps will be erased if we generate DB. Click on the MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode button (above the operation tree) to start the simulation.

####  Run and monitor a simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog. Use the default **Continue****Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** radio button. Click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

#### Review the results

When the simulation is completed, click the MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode button to review results.

#### Graph

In the Post-processor, use the Graph tool to plot Y Speed vs. Time. Note that the press moves as constant speed of **2** **in/sec** and then slows down dramatically during the three second dwell time.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab7_image0003.jpg' | relative_url }})

Y-Speed vs Time graph plot with contact

Plot Y Load vs Time. Note that the press load hits a maximum of **4000klb** and then holds this load constant during the dwell.

Use the Contact nodes ![]({{ '/assets/icons/pre_icons/mo_show_cotact_icon.jpg' | relative_url }}) icon to display contact with the dies. View how much contact increases during the dwell phase. This is often the difference between filling and not filling the die in a hydraulic press forging.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab7_image0004.jpg' | relative_url }})

Y-Load vs Time graph plot with contact

### Power Envelope method

#### Creating a New Problem

Create a new project called **FE_Gear_Hydraulic_PowerLimit** and copy the existing project **FE_Gear_LargerBillet**. Be sure the **Copy****database****file** option is **checked**. Click on the **2nd** operation and go to **Top****Die** Movement.

#### Top die movement

Set the movement to **Hydraulic****press** , set the Speed to a **constant****2** in/sec. and **check** the **Power****Limit** option. (See Fig. L7.5.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab7_image0005.jpg' | relative_url }})

Hydraulic movement controls with power limit

Click ![]({{ '/assets/icons/pre_icons/mo_define..._button2.jpg' | relative_url }}) and define the below values into the Power Limit table. This curve defines the maximum speed that the press can maintain at a given forging load (See Fig. L7.6.).

**Force** |  **Speed**  
---|---  
0 |  3  
500 |  3  
1000 |  2.875  
1500 |  2.625  
2000 |  2.375  
2500 |  2  
3000 |  1.4  
3500 |  0.75  
4000 |  0.01  
4500 |  0  
5000 |  0  
  
![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab7_image0006.jpg' | relative_url }})

Power limit window

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Stopping controls.

#### Stopping controls

**Uncheck****Distance****between****objects** and **check****Max****load**. Set the **Max****load** value to **4000** klb.

#### Generating DB

Go to **Generate** DB page and generate the database. Click **Yes** to the Lost Steps popup informing that 2nd operation existing steps will be erased if we generate DB. Click on the MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode button (above the operation tree) to start the simulation.

#### Run and monitor a simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog. Use the default **Continue****Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** radio button. Click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

#### Review the results

When the simulation is completed, click the MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode button to review results.

#### **Graph**

In the Post-processor, use the Graph ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) tool to plot Y-Speed vs. Time. Note that the press moves at constant **speed** of **2** in/sec and then slows down dramatically as shown in Fig. L7.7.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab7_image0007.jpg' | relative_url }})

Y-Speed vs Time plot

Plot Y- Load vs Time. In power limit case, we can observe that when load crosses **2500** klb, speed gradually drops from 2 in/sec. Note that the press load also hits a maximum of 4000klb. (See Fig. L7.8.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab7_image0008.jpg' | relative_url }})

Y-load vs Time graph plot

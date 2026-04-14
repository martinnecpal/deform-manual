---
lang: sk
title: "Forming Lab 7"
---

# Lab 7. Hydraulic Press

There are two ways to model hydraulic press behavior:

  1. Assume press maintains constant speed until it hits maximum load, then dwells at maximum load (two-step method).

  2. Assume press slows gradually as it approaches maximum load (power envelope method).

The two-step method is easier to set up and is useful for force-controlled simulations other than hydraulic presses. The power envelope method is more representative of actual hydraulic press behavior.

### Two-step method

#### Create a new Problem

Create a new project called **Gear_Hydraulic_Dwell** , and copy the existing project **Gear_LargerBillet**. Be sure the **Copy database file** option is checked. Click on the 2nd operation and go to **Top****Die** Movement page.

#### Assign Top die movement

Set the movement to **Hydraulic** press and set the **Speed** to a constant **2** i**n/sec**(See Fig. L7.1.) . Click the **Dwell** controls tab. We will set the maximum press load, the time the press will be held at that load, the number of time steps to dwell, and the stall velocity, after which the press will stop.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab7_image0001.jpg' | relative_url }})

Top die movement window

Once the press hits the maximum press load (4000 klb.), we will dwell for 3 seconds. A good rule of thumb is 100 steps per second of dwelling, so we will use 300 steps.

Set the **Max. load** to **4000** klb, **Min.****velocity** to 0**.005** in/sec, **Total****dwell****time** to **3** seconds and the **No. of steps** to **300**. (See Fig. L7.2.)

Note that the **Current****dwell****time** should always start at **0**. The time will be updated by the system once the dwell load is reached.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab7_image0002.jpg' | relative_url }})

Hydraulic press Dwell tab window

#### Generating DB

Go to **Generate****DB** page and generate the database. Click on the MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode button (above the operation tree) to start the simulation.

#### Run and monitor a simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog. Use the default **Continue****Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** radio button. Click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

#### Review the results

When the simulation is completed, click the MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode button to review results.

#### Graph

In the Post-processor, use the Graph ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) tool to plot Y Speed vs. Time. (See Fig. L7.3.)

_Note that the press holds 2 in/sec and then slows down dramatically during the three second dwell._

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab7_image0003.jpg' | relative_url }})

Y-Speed vs time graph plot with contact

Plot **Y Load** vs **Time**. Note that the press load hits a maximum of **4000** klb and then holds this load constant during the dwell. (See Fig. L7.4.)

Use the Contact nodes ![]({{ '/assets/icons/post_icons/mo_show_cotact_icon.jpg' | relative_url }}) icon to display contact with the dies. View how much contact increases during the dwell phase. This is often the difference between filling and not filling the die in a hydraulic press forging.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab7_image0004.jpg' | relative_url }})

Y-Load vs Time graph plot with contact

### Power Envelope method

#### Creating a New Problem

Create a new project called **Gear_Hydraulic_PowerLimit** and copy the existing project **Gear_LargerBillet**. Be sure the **Copy database file** option is **checked**. Click on the**2 nd operation **and go to **Top****Die** Movement.

#### Top die movement

Set the movement to **Hydraulic****press** , set the Speed to a **constant****2** in/sec. and **check** the **Power****Limit** option as shown in Fig. L7.5.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab7_image0005.jpg' | relative_url }})

Top die movement window

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
  
![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab7_image0006.jpg' | relative_url }})

Power limit window

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Stopping controls.

#### Stopping controls

Set the **Max****load** of primary die to **4000** klb (Y). Go to the **Die****distance****tab** and Initialize ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}) to deactivate. Click ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}) to the popup asking if you want to use these settings.

#### Generating DB

Go to Generate DB page and generate the database. Click on the MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode button (above the operation tree) to start the simulation.

#### Run and monitor a simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog. Use the default **Continue****Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** radio button. Click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

#### Review the results

When the simulation is completed, click the MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode button to review results.

#### Graph

In the Post-processor, use the Graph ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) tool to plot **Y-Speed** vs. **Time**. Note that the press holds 2 in/sec and then slows down dramatically during the three second dwell.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab7_image0007.jpg' | relative_url }})

Y-Speed vs Time plot

In the Post-processor, plot **Y Speed** vs. **Time**.

Note that the press holds 2 in/sec until nearly the end of the simulation, then begins slowing down dramatically as shown in Fig. L7.7.

Plot **Y- Load** vs **Time**. Note that the press load hits a maximum of 4000 klb.(See Fig. L7.8.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab7_image0008.jpg' | relative_url }})

Y-load vs Time graph plot

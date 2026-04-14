---
lang: en
title: "Forming Lab 6"
---

# Lab 6. Mechanical Press

### Background

In multiple operations, interactive mechanical press setup is significantly different than scheduled setup. We will work through both.

Because of the unique kinematics of a mechanical press, we need to know exactly whether the press is in the top-bottom (or front-back) stroke at any time. This means we need knowledge of the starting position.

When defining a mechanical press, there are special terms that should be understood:

**Total stroke** is the total ram movement from Top Dead Center (TDC) to Bottom Dead Center (BDC).

**Forging stroke** is the distance the ram travels from the time it first touches the workpiece until it reaches BDC.

**Strokes/second** is the flywheel speed in cycles/second (matches the press speed on a non- clutch driven press).

For this tutorial, we will use a Total Stroke of 16 in. and a Strokes/second of 1 (i.e. 60 RPM).

### Operation1- Interactive setup

#### Creating New problem

Create a new project called **Gear_Mechanical** and copy the existing project **Gear_LargerBillet**.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab6_image0001.jpg' | relative_url }})

MO New Project window

In an interactive setup, we can start with the Top Die positioned correctly on the workpiece. So, click the first **Upset****operation** tile. Go to **Top** **Die****Movement** page from Operation tree.

#### Top die Movement

Change the movement type to **Mechanical****press**. Set the **Total****stroke** to **16** in. and the **Forging****stroke** to **6.3** in (distance from the current position to BDC). Set the **Cycles/sec** to **1** (See Fig. L6.2.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Stopping controls page

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab6_image0002.jpg' | relative_url }})

Top die movement page

#### Stopping controls

Set the stopping stroke (Primary die displacement) to **16** in. (**Y** direction), which is equal to the total press stroke. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Generate DB page.

#### Generate DB

Generate the Database and click ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) to 2nd operation.

### Operation 2 - scheduled (batch) setup

In a batch setup, we generally do not know where the ram will be relative to BDC when it touches the workpiece. Therefore, we need to start with the ram in a known position, and update the movement controls when the model is run.

We will use the TDC position as a standard reference position, then use scheduled positioning to update the tool position and forging stroke. 

Go to **Positioning** **page** from Operation tree.

#### Object Positioning

  1. Interference position the Top Die down to the Bottom Die

  2. Offset position the Top Die up by the flash gap of 0.2 in

  3. Offset position the Top Die up by the total forging stroke of 16 in. Now the die is at TDC.

Now go back to **Top****die****movement** page.

#### Top die movement

Define Mechanical press with **Cycles/sec** = **1** and define both the **Total****stroke** and **Forging****stroke** to **16** in. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Scheduled positioning page.

#### Scheduled Positioning

Interference positioning the Workpiece down to the Bottom die.

Interference positioning the Top Die down to the Workpiece. Notice how the Update current stroke option is checked and grayed out. The die stroke will be automatically updated when this positioning occurs during the simulation. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Stopping controls page.

#### Stopping controls

Set the **Primary****die****displacement** to **16** in (Y direction) and under **Die****distance****tab** click the ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}) to initialize the Die distance stopping controls data.

When the project runs, the tool will be moved into position in contact with the workpiece (whatever the shape is) and the forging stroke will be updated to reflect the new distance above BDC.

Save the project and click on the MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode button (above the operation tree) to start the simulation.

### Run and monitor a simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog. Use the default **Continue****Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** radio button. Click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

### Review the results

When the simulation is completed, click the MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode button to review results.

Play through all steps. 

**Graph**

Click the ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) tool and plot Y Speed vs. Time graph. Note that the velocity goes to zero at the end of each operation.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab6_image0003.jpg' | relative_url }})

Y-Speed v/s Time graph

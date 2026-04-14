---
lang: sk
title: "Forming Express Lab6"
---

# Lab 6. Mechanical Press

### Background

In multiple operations, interactive mechanical press setup is significantly different than scheduled setup. We will work through both.

Because of the unique kinematics of a mechanical press, we need to know exactly whether the press is in the top-bottom (or front-back) stroke at any time. This means we need knowledge of the starting position.

When defining a mechanical press, there are special terms that should be understood:

**Total stroke** is the total ram movement from Top Dead Center (TDC) to Bottom Dead Center (BDC).

**Forging stroke** is the distance the ram travels from the time it first touches the workpiece until it reaches BDC.

**Strokes/second** is the flywheel speed in cycles/second (matches the press speed on a non- clutch driven press).

For this tutorial, we will use a **Total Stroke of 16 in**. and a **Strokes/second as1 stroke/second** (i.e. 60 RPM).

### Operation1- Interactive setup

#### Creating New problem

Create a new project called **FE_Gear_Mechanical** and copy the existing project **FE_Gear_LargerBillet**.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab6_image0001.jpg' | relative_url }})

MO New Project window

In an interactive setup, we can start with the Top Die positioned correctly on the workpiece. So, click the first **Upset** operation tile. Go to **Top Die Movement** page from Operation tree.

#### Define Top die Movement for Upset

Change the movement type to Mechanical press. Set the **Total****stroke** to **16** in. and the **Stroke/sec** to **1** (See Fig. L6.2.). Leave the **Forming** stroke option as **Exact** **forming****stroke**. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Stopping controls page.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab6_image0002.jpg' | relative_url }})

Top die movement window

#### Define Primary Die stroke for Upset

Set the **total** **primary****die****travel** to **6.5** in (Same as used in [Lab 2](/docs/sk/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/forming_express_lab2/)). (See Fig. L6.3.). If the initial position of the top die is at Top Dead Center or Bottom Dead center, accordingly ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) wizard button can be used for positioning the die and calculate the forming stroke automatically. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define the Stopping controls page.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab6_image0003.jpg' | relative_url }})

Primary die stroke window

#### Check the Stopping controls for Upset

In stopping controls, we can observe that total stroke defined in movement controls is used as Max die stroke. This field will be deactivated as it reads data from mechanical press data of the top die movement controls. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Generate DB window leaving the default step controls settings.

#### Generate DB

Generate the Database and click ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) to 2nd operation.

### Operation 2 - scheduled (batch) setup

In a batch setup, we generally do not know where the ram will be relative to BDC when it touches the workpiece. Therefore, we need to start with the ram in a known position, and update the movement controls when the model is run.

We will use the TDC position as a standard reference position, then use scheduled positioning to update the tool position and forging stroke. 

Go to **Positioning** page from Operation tree.

#### Object Positioning

  1. **Interference** **position** the **Top Die** **down** to the **Bottom****Die**

  2. **Offset****position** the **Top****Die** up in **+Y** direction by the **flash****gap** of **0.2** in

  3. **Offset****position** the **Top****Die** up in +Y direction by the total forging stroke,16 in. Now the die is at **TDC**.

Now go **back** to **Top** **die****movement** page.

#### Define Top die movement for Forming

Define Mechanical press with Strokes/sec = 1 and define the **Total****stroke** as **16** in. Change the **Forming****stroke** option to **Exact****forming****stroke**. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until **Scheduled****positioning** page. (See Fig. L6.4.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab6_image0004.jpg' | relative_url }})

Mechanical press Movement window for Forming

#### Scheduled Positioning

**Interference****positioning** the **Workpiece****down** to the **Bottom****die**.

**Interference****positioning** the **Top****Die** down to the **Workpiece**. Notice how the Update current stroke option is checked and greyed out. The die stroke will be automatically updated when this positioning occurs during the simulation. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Stopping controls page.

#### Define Primary die stroke for Upset

Set the **Primary die displacement** to **16** in (Y direction). As primary die is currently at TDC check the current die position to Top Dead Center Position.

When the project runs, the tool will be moved into position in contact with the workpiece (whatever the shape is) and the forging stroke will be updated to reflect the new distance above BDC.

Save the project and click on the MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) mode button (above the operation tree) to start the simulation.

### Run and monitor a simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog. Use the default **Continue****Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** radio button. Click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

When the simulation ends, you should see the following text at the bottom of the Message file.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab6_image0006.jpg' | relative_url }})

This means that the simulation stopped when the press hit BDC. If you were to look in the Log file, you would see that this is also the reason why the first operation stopped.

### Review the results

Click the MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode button to review results. Play through all steps.

**Graph**  
Click the ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) tool and plot **Y Speed** vs **Time** graph. Note that the velocity goes to zero at the end of each operation.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab6_image0005.jpg' | relative_url }})

Y-Speed v/s Time graph

---
lang: sk
title: "Forming Lab 4"
---

# Lab 4. Symmetry

### Creating a New Problem

To investigate 3D symmetry in DEFORM, open the new project with **Gear_3D_Thermal_Sym** name and with **English** unit.

This project is the same as the previous **Gear_3D_Thermal**(Lab 3), with the exception that only 45° of the workpiece is modeled. For this 45°sector of the part to deform the same as the full part, symmetry boundary conditions must be used. This lab will go over the differences when setting up a simulation with symmetry.

### Add Operations

Add three operations from the Explorer:

  * [3D] Heat Transfer Express

  * [3D] Heat Transfer and

  * [3D] Forming

  
Double-click on the title of the first operation and change it to **Air****Transfer**. Change the second operation title to **Rest****on****Die**. Leave the third Forming title as it is.

Right-click the **Workpiece** and **Pass object to All operations**. Similarly, right-click on the **Top Die** and **Bottom****Die** and use **Pass object to Next operation** for both objects.

### Define Air transfer

Click on the **Air****Transfer** operation in Operation Editor. In this lab, we will use the **Symmetry** part. Verify that the heating type is set to **Transfer**. Select the Symmetry geometry type, leave the **Accuracy** and **Complexity** sliders at **Moderate**(See Fig. L4.1.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Workpiece page.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab4_image0001.jpg' | relative_url }})

Air Transfer operation Process window

### Define Workpiece General data

Leave the workpiece temperature at 2250°F. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to geometry page.

#### Create Workpiece geometry from Primitive

Define the geometry as a primitive **cylinder** with a diameter of **5** in, **height** of **8.1** in, **Revolve****angle** as **45** degree and **corner****radius** of**0.2** in. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to assign symmetry planes in symmetry page.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab4_image0002.jpg' | relative_url }})

Workpiece Geometry Primitive window

#### Assign Symmetry for Workpiece

Select each of the two cut surfaces and add as a **Symmetry****plane** by picking them with the mouse and then clicking ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}). Click each of the entries under Planar Symmetry and observe the surfaces that get highlighted (See Fig. L4.3.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab4_image0003.jpg' | relative_url }})

Workpiece Symmetry window

#### Generating mesh for Workpiece

Select **User****defined** radio button and define target number of elements as **10000** and Generate a mesh. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Material page.

#### Assign Material for Workpiece

Click the ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load material from library) button. Select the **Steel_at_Extended_Temperatures** category, then **AISI-8620[1550-2200F(850 -1200C)]** and click the ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}) button. Click on the **AISI-8620[1550-2200F(850 -1200C)]** in the material window to assign the material to the workpiece. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to BCC page.

#### Workpiece BCC

By default, BCC for Symmetry planes, and Heat exchange with the environment are generated. Confirm that symmetry boundary conditions are defined on the symmetry planes, and that heat exchange with environment is defined on all faces except the symmetry planes. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Heat Condition page.

### Assign Heat Condition

Set the **Transfer****time** as **5** sec, accept the default **Environment temperature** and **Convection****coefficient**. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Simulation controls page.

### Simulation controls

Use default Step definition, Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to generate DB.

### Generate Database

Click ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), If there is no errors and warnings in message tab, go ahead and click![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) .

Now click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to move to Next operation.

### Rest on Die operation

For the 2nd operation, the heat transfer type will be **Rest on die**. This simulates the heat lost from the workpiece to the tool from the time it is placed on the bottom die until the press is stroked. For this operation, the workpiece should be contacting the bottom die, but the top die should be positioned some distance away from the workpiece.

Note: The Dwell on die is intended for heat transfer after forging, and uses higher heat transfer coefficients corresponding to more complete die contact.

### Heat Transfer type

By default, heat transfer type will be **Rest on die**. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Process condition page

### Process condition

The **Resting****time** will be **4** seconds. Accept the **default temperature** and **convection****coefficient**. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Object page.

### Object list

Confirm that 3 objects are present in the table. If not, click the ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) (insert object) button three times to add 3 objects. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Workpiece page.

### Workpiece

All data for workpiece will be read from the first operation results in the database. Skip over the workpiece and move to the Top Die.

### Top die General page

Verify that the Top Die temperature is **300** °F. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Top die geometry page.

#### Import Top die geometry

Import the gear top die geometry from an STLfile. Click the ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Load geometry from a file) button and ![]({{ '/assets/icons/pre_icons/mo_open_button.jpg' | relative_url }}) open (import) the file “**gear top die.STL** ”. The geometry for top die is located in DEFORM installation folder \Tutorials directory. The die comes in oriented along a different axis than the workpiece. We will address that in a later step.

We will use a die distance stopping control when we run the forming simulation, but since the tools are defined in the current operation, reference points must also be defined now. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Properties page.

#### Top die Properties

Select **Properties![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Reference** Use **Coordinate** and pick a point on the flash land (See Fig. L3.7.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Bottom die page.

### Bottom die general page

Verify that the Bottom Die temperature is **300** °F. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Bottom die geometry page.

#### Import Bottom die geometry

Import the bottom die geometry from an STL file. Click the ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load geometry from library) button and ![]({{ '/assets/icons/pre_icons/mo_open_button.jpg' | relative_url }}) open (import) the file “**gear bottom die.STL** ”. This can also be imported using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Load geometry from a file) button by browsing the geometry file path. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Properties page.

#### Bottom die Properties

Select **Properties![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Reference** Use **Coordinate** and pick a point on the flash gutter (See Fig. L3.8.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to positioning page.

### Positioning dies

At this point, the workpiece is oriented along the Z axis, and the tools are oriented along the Y axis.

Click on ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) button.

First, rotate the dies to be oriented along the Z axis. Set Method to **Rotational**. Set the following:

Positioning object: **Top Die**.

Axis: X

Rotation center: User-defined (0,0,0)

Angle: 90 deg.

We want to rotate both dies together, so go to the **Coupled** tab, and check Bottom Die. This will couple any positioning that is done (See [Fig. L3.9.](forming_lab3.htm#Fig_L3_9_Positioning_Top_die_with_Coupled_Bottom_object)). Click ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) to rotate the tools to be aligned with the workpiece.

Now the tools and workpiece are all aligned along the Z axis, but the tools are too close together. The next step is to move the Top Die into an "up" position away from the workpiece. 

**Uncheck** the coupled positioning, then position the Top Die using Offset a distance of **12** in using **Offset** in the **Z** direction.

Finally, we need to make sure that the Bottom Die will properly contact the Workpiece. Since the Workpiece will be read from the database at this operation, we can't use regular positioning. However, we can use scheduled positioning that will be completed when the project is running. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close Object positioning dialog and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Scheduled positioning page.

### Scheduled positioning

Use ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) to add a scheduled positioning operation, and **Interference** position the **Bottom****Die** in the **Z** direction to the **Workpiece**.

Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) and the scheduled positioning page should show this scheduled operation. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Contact page.

### Contact

In Contact, assign default contact relations, and be sure the scheduled contact Initialize and Generate options are checked. Friction doesn’t need to be defined because this operation is strictly heat transfer. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Step controls page.

### Step controls

In Stopping controls, the Process duration is already set to 4 seconds. For heat transfer with contact, run 10 steps per second. So for a 4 second model, run 40 steps with a time step of 0.1 sec. Define **Number of steps** as **40** ,Constant **time per step** as **0.1** sec. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until generate DB page.

### DB generation

Data checking will be executed. You will see a message saying DB will not be generated. The database for this operation will be generated automatically after the first operation simulation is completed.

### Forming operation

Click ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) or just click on the Forming tile in the Operation Editor to set up the forming operation.

All objects will be read from the database at the end of the previous Rest on Die operation, so we only need to set:

  * Movement controls

  * Positioning

  * Inter-object relationships

  * Simulation and stopping controls

### Assign Top die movement

Click on Top Die **Movement** page in Operation tree and set the **Speed** to a constant value of **3** in/sec in the **-Z** direction. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Scheduled Positioning page.

### Scheduled Positioning

Click ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button and define **Interference** position for the **Top****Die** to the **Workpiece** in the **-Z** direction. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Contact page.

### Inter-Object relation

Click on **Contact** and define inter-object relationships with friction 0.3. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Stopping controls page.

### Assign Step and Stopping controls

In Stopping controls, set the **Die****Distance** stopping criteria to 0.25 in., using the **Top Die** and **Bottom****Die** as the reference objects and **Z** as the direction. Save the project. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Step controls page.

Set the **Number of steps** to **100** and the **Step increment to save** to **5**.

Set the step size to a **die displacement** of **0.085** in.

Click on the MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode button (above the operation tree) to start the simulation.

### Run and monitor a simulation

3D simulations can be made to run faster by taking advantage of multiple processors or multiple cores on one processor. If your computer processors has 4 cores, then Click the ![]({{ '/assets/icons/simulator_icons/mo_run_options_action_lable.jpg' | relative_url }}) label.

set the Simulation Mode to **Interactive** and select **Continue****Run**  
specify the Processors Per Job as **4.** Then click on ![]({{ '/assets/icons/pre_icons/mo_save_button.jpg' | relative_url }}) button and then **![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}). (See[ Fig. L3.13.](forming_lab3.htm#Fig_L3_13_Run_option_window)).**

As the simulation is running, click the Temperature ![]({{ '/assets/icons/post_icons/mo_temp_sv.jpg' | relative_url }}) button to view temperatures in the graphics window. It is helpful to use Multi object mode ![]({{ '/assets/icons/pre_icons/mo_show_multi_obj_icon.jpg' | relative_url }}) to make the dies transparent. 

Once the simulation is completed, click the MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode button to review results.

### Review results in Post Mode

Click the 3D Mirroring ![]({{ '/assets/icons/post_icons/mo_3d_mirroring_icon.jpg' | relative_url }}) icon. Confirm that the **Add** option is selected and click on a symmetry plane of the object. A mirrored symmetry object will be added. Keep clicking on the symmetry plane until the full object is created. If you make a mistake, the Delete option can be used to delete the added sections.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab4_image0004.jpg' | relative_url }})

3D Mirroring window in MO post

Play through the steps of the simulation. Compare results to the full model. The results should be essentially the same.

Note: When plotting the load vs. stroke curve, the load displayed is only for this 45° section. The Graph ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) dialog has a Scale option that allows you to multiply the load by 8 to get the load to form the full part.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab4_image0005.jpg' | relative_url }})

Load Stroke graph with scale

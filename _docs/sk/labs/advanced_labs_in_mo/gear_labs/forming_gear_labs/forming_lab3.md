---
lang: sk
title: "Forming Lab 3"
---

# Lab 3. 3D Gear lab with temperature calculations in Forming 

In this lab, we will model forging the same gear blank, but now we will do it with temperature calculations, without the initial upset operation, and in **3D instead of 2D (2D Gear Lab)** .

We will use the multiple operations system to simulate:

  * Removing a heated billet from the furnace, and transferring it in air to the forging tools

  * Resting the billet on the forging tools

  * Forging the billet.

Without the upset operation, a fold develops on the inside of the gear blank. We will use various post-processing tools to examine the fold.

### Creating a New Problem

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear.

Create a new problem either by selecting **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear. Select " **Integrated Manufacturing Process** " radio button and Unit system as "**English** " using radio button. Define Problem Name as "**Gear_3D_Thermal** " and click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Deform Integrated Manufacturing Process.

Multiple operation wizard will open, specify the project name as **Gear_3D_Thermal** and confirm that First operation check box is unchecked as we will add operation later and use the default (home) directory Location as shown in Fig. L3.1. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to add project. This lab will be referenced in future labs so it is important to use the name above.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab3_image0001.jpg' | relative_url }})

New MO project window

### Add Operations

Add three operations from the Explorer:

  1. [3D] Heat Transfer Express

  2. [3D] Heat Transfer and

  3. [3D] Forming

  
Double-click on the title of the first operation and change it to **Air Transfer**. Change the second operation title to **Rest on Die**. Leave the third Forming title as it is (See Fig. L3.2.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab3_image0002.jpg' | relative_url }})

Renamed Operation names in Operation editor

Right-click the **Workpiece** and **Pass object to All operations**. Similarly, right-click on the **Top Die** and **Bottom Die** and use **Pass object to Next operation** for both objects (See Fig. L3.3.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab3_image0003.jpg' | relative_url }})

Operation editor after passing objects to next operations

### Define Air transfer

Click on the **Air****Transfer** operation in Operation Editor. In this lab, we will use the **Whole** part. Verify that the heating type is set to **Transfer**. Leave the **Accuracy** and **Complexity** sliders at **Moderate**(See Fig. L3.4.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Workpiece page.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab3_image0004.jpg' | relative_url }})

Process window

### Define Workpiece General data

Leave the workpiece temperature at **2250** °F. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to geometry page.

#### Create Workpiece geometry from Primitive

Define the geometry as a primitive **cylinder** with a **diameter** of **5** in, **height** of **8.1** in, and **corner****radius** of **0.2** in. Click![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to mesh page.

#### Generating mesh for Workpiece

Generate a mesh using the default setting of **80000** elements.

#### Assign Material for Workpiece.

Click the ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load material from library) button. Select the **Steel_at_Extended_Temperatures** category, then **AISI-8620[1550-2200F(850 -1200C)]** and click the ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}) button. Click on the **AISI-8620[1550-2200F(850 -1200C)]** in the material window to assign the material to the workpiece. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to BCC page.

#### Workpiece BCC

Heat exchange with the environment boundary conditions should be defined automatically. Verify this by clicking the **Defined** in the boundary conditions tree and checking that all surfaces are green as shown in Fig. L3.5\. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Heat Condition page.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab3_image0005.jpg' | relative_url }})

Workpiece BCC window

### Assign Heat Condition

Set the **Transfer****time** as 5 sec, accept the default Environment temperature and Convection coefficient (See Fig. L3.6.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Simulation controls page.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab3_image0006.jpg' | relative_url }})

Heat condition window

### Simulation controls

Use default Step definition, Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to generate DB.

### Generate Database

Click ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}), If there is no errors and warnings in message tab, go ahead and click ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}).

Now click on ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) to move to Next operation.

### Rest on Die operation

For the 2nd operation, the heat transfer type will be **Rest on die**. This simulates the heat lost from the workpiece to the tool from the time it is placed on the bottom die until the press is stroked. For this operation, the workpiece should be contacting the bottom die, but the top die should be positioned some distance away from the workpiece.

Note: The Dwell on die is intended for heat transfer after forging, and uses higher heat transfer coefficients corresponding to more complete die contact.

### Heat Transfer type

By default, heat transfer type will be Rest on die. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Process condition page

### Process condition

The **Resting****time** will be **4** seconds. Accept the default temperature and convection coefficient. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Object page.

### Object list

Confirm that 3 objects are present in the table. If not, click the ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) (insert object) button three times to add 3 objects. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Workpiece page.

### Workpiece

All data for workpiece data will be read from the first operation results in the database. Skip over the workpiece and move to the Top Die.

### Top die General page

Verify that the Top Die temperature is **300** °F. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Top die geometry page.

#### Import Top die geometry

Import the gear top die geometry from an STL file, import the “**gear top die.****STL** ” using the ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Import geometry from a file) button by browsing the geometry file path in installation folder \**Tutorials****** directory. The die comes in oriented along a different axis than the workpiece. We will address that in a later step.

We will use a die distance stopping control when we run the forming simulation, but since the tools are defined in the current operation, reference points must also be defined now. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Properties page.

#### Top die Properties

Select **Properties![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Reference** Use Coordinate and pick a point on the flash land (See Fig. L3.7.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Bottom die page.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab3_image0007.jpg' | relative_url }})

Top die properties window

### Bottom die general page

Verify that the Bottom Die temperature is **300** °F. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Bottom die geometry page.

#### Import Bottom die geometry

Import the gear bottom die geometry from an STL file. Click the ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Load geometry from a file) button and open (import) the file “**gear bottom die.****STL** ”, by browsing the geometry file path in the installation folder \Tutorials directory. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Properties page.

#### Bottom die Properties

Select **Properties![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Reference** Use Coordinate and pick a point on the flash gutter (See Fig. L3.8.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to positioning page.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab3_image0008.jpg' | relative_url }})

Bottom Die Properties window

### Positioning dies

At this point, the workpiece is oriented along the Z axis, and the tools are oriented along the Y axis.

Click on ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) button.

First, rotate the dies to be oriented along the Z axis. Set Method to **Rotational**. Set the following:

Positioning object: **Top Die**.

Axis: X

Rotation center: User-defined (0,0,0)

Angle: 90 deg.

We want to rotate both dies together, so go to the **Coupled** tab, and check Bottom Die. This will couple any positioning that is done (See Fig. L3.9.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab3_image0009.jpg' | relative_url }})

Positioning Top die with Coupled Bottom object

Click ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) to rotate the tools to be aligned with the workpiece.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab3_image0010.jpg' | relative_url }})

Objects after rotation position

Now the tools and workpiece are all aligned along the Z axis, but the tools are too close together as shown in Fig. L3.10. The next step is to move the Top Die into an "up" position away from the workpiece. 

**Uncheck** the **coupled** positioning, then position the **Top****Die** by a distance of **12** in using **Offset** in the **Z** direction.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab3_image0011.jpg' | relative_url }})

Top die after offset position

Finally, we need to make sure that the Bottom Die will properly contact the Workpiece. Since the Workpiece will be read from the database at this operation, we can't use regular positioning. However, we can use scheduled positioning that will be completed when the project is running. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close Object positioning dialog and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Scheduled positioning page.

### Scheduled positioning

Use ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) to add a scheduled positioning operation, and Interference position the **Bottom****Die** in the**Z** direction to the **Workpiece**.

Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) and the scheduled positioning page should show this scheduled operation (See Fig. L3.12.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Contact

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab3_image0012.jpg' | relative_url }})

Scheduled positioning window

### Contact

In Contact, assign default contact relations, and be sure the scheduled contact Initialize and Generate options are checked. Friction doesn’t need to be defined because this operation is strictly heat transfer. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Step controls page.

### Step controls

In Stopping controls, the Process duration is already set to 4 seconds. For heat transfer with contact, run 10 steps per second. So for a 4 second model, run 40 steps with a time step of 0.1 sec. Define **Number****of****steps** as **40** ,Constant **time****per****step** as **0.1** sec. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until generate DB page.

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

Click on **Top****Die****Movement** page in Operation tree and set the **Speed** to a constant value of **3** in/sec in the **-Z** direction. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Scheduled Positioning page.

### Scheduled Positioning

Click ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button and define **Interference****position** for the **Top****Die** to the **Workpiece** in the **-Z** direction. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Contact page.

### Inter-Object relation

Click on **Contact** and define inter-object relationships with friction **0.3**. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Stopping controls page.

### Assign Stopping and Step controls

In Stopping controls, set the **Die****Distance****stopping** criteria to **0.25** in., using the **Top Die** and **Bottom****Die** as the reference objects and **Z** as the direction. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Step controls page.

Set the **Number****of****steps** to **100** and the **Step****increment****to****save** to **5**.

Set the step size to a **die****displacement** of **0.085** in. Save the project.

Click on the MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode button (above the operation tree) to start the simulation.

### Run and monitor a simulation

3D simulations can be made to run faster by taking advantage of multiple processors or multiple cores on one processor. If your computer processors has 4 cores, then Click the ![]({{ '/assets/icons/simulator_icons/mo_run_options_action_lable.jpg' | relative_url }}) label.

set the Simulation Mode to **Interactive** and select **Continue****Run**  
specify the MPI 3D as **4.** (See Fig. L3.13.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab3_image0017.jpg' | relative_url }})

Run option window

Then click on ![]({{ '/assets/icons/pre_icons/mo_save_button.jpg' | relative_url }}) button and then ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}).

As the simulation is running, click the Temperature ![]({{ '/assets/icons/post_icons/mo_temp_sv.jpg' | relative_url }}) button to view temperatures in the graphics window. It is helpful to use Multi object mode ![]({{ '/assets/icons/pre_icons/mo_show_multi_obj_icon.jpg' | relative_url }}) to make the dies transparent. 

Once the simulation is completed, click the MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode button to review results.

### Review results in Post Mode

Play through the steps to observe how the part deforms.

Click the Slicing ![]({{ '/assets/icons/post_icons/mo_slicing_option.jpg' | relative_url }}) icon. The workpiece and tools will be surrounded by a yellow box. Click on a yellow line of the box. The objects will be sliced perpendicular to the line (if the dies don’t get sliced make sure “slice all objects” is selected). Sliding the blue slider bar left or right will move the slicing plane forward or backward.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab3_image0014.jpg' | relative_url }})

Slicing window in MO post

Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the slicing dialog.

Plot Temperature ![]({{ '/assets/icons/post_icons/mo_temp_sv.jpg' | relative_url }}) in the workpiece. Go to the Set Up ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) dialog and set the scaling to User with a Min of **1000** °F and a Max of **2500** °F. Click ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) then ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

Right-click the **Temperature** color bar in the graphics window and select **Colorbar****Type![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Temperature**. The temperatures are now displayed using a more intuitive color scheme.

Click on the Point Tracking ![]({{ '/assets/icons/post_icons/mo_point_tracking_icon.jpg' | relative_url }}) option. Point tracking can track the movement of a point, as well as the evolution of state variables at that point. Pick several points on the sliced section of the workpiece. 

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab3_image0015.jpg' | relative_url }})

Point tracking window in MO post

Click ![]({{ '/assets/icons/post_icons/mo_track_button.jpg' | relative_url }}). The program will take some time to track the temperatures at these points and will then output the result in a graph.

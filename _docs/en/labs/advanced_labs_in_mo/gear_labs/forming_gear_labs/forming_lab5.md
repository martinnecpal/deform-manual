---
lang: en
title: "Forming Lab 5"
---

# Lab 5. 2D to 3D conversion

### Creating a New Problem

Create a new project called **Gear23** and copy the existing project **Gear_LargerBillet**.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab5_image0001.jpg' | relative_url }})

MO New Project window

### Adding operations

Right-click on the 2nd operation tile in operation editor and delete it. Add the following operations:

  * [2D] Heat Transfer Express

  * 2D to 3D Converter (located in Simulation Operator)

  * [3D] Forming Express

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab5_image0002.jpg' | relative_url }})

Operations list in Operation Editor

### Upset Operation

In the initial Upset tile in Operation Editor, right-click on the **Workpiece** and **Pass object to All operations**.

Select **Upset** operation and Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). Go to Simulation controls and **check****Heat****transfer** mode.

**Generating DB**  
Select **Generate****DB** from the operation tree and Generate the Database. Click ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) to Heat Transfer Express operation.

### Heat Transfer Express operation

#### Process

In Process page, select the heating type as **Transfer**. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Object list.

#### Object selection

Select**1 workpiece only** radio button. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Heat condition.

#### Heat Condition

Set the **transfer****time** to **5** seconds and accept the **default temperature** and **convection****coefficient**. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Simulation controls.

#### Simulation Controls

Use the default value and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until 2D to 3D Convertor operation.

### Convert 2D to 3D operation

Verify **Z** is up (consistent with other models) and in 3D parameters start angle and Revolve angle should be 0 and 360 to generate whole workpiece. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Workpiece geometry page.

#### Workpiece Geometry

The **# of sections** sets the number of geometry sections around the circumference. One section per degree of rotation works well, so set the **# of sections** to **360**. click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to workpiece mesh page.

#### Workpiece Mesh

Leave the Mesh at the default **32000** elements. click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to workpiece Material page.

#### Workpiece Material

Leave the Material as (inherited) in Material page. click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Forming express Top die general page.

### 3D Forming Express

#### Top die general

Keep the default **300** °F temperature for Top die, click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Top die geometry page.

#### Top die geometry

Click the ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Load geometry from a file) button and ![]({{ '/assets/icons/pre_icons/mo_open_button.jpg' | relative_url }}) open (import) the file “**gear top die.STL** ”. The geometry for top die is located in DEFORM installation folder \Tutorials directory. Define a reference point on the flash land using ![]({{ '/assets/icons/pre_icons/mo_define_reference_point_button.jpg' | relative_url }}) option. click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Top die movement page.

#### Top die Movement

Set the **Speed** to a constant value of **3** in/sec in the **-Z** direction. click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Bottom die page.

#### Bottom Die general

Keep the default **300** °F temperature for bottom die, click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to bottom die geometry page.

#### Bottom die geometry

Click the ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Load geometry from a file) button and ![]({{ '/assets/icons/pre_icons/mo_open_button.jpg' | relative_url }}) open (import) the file “**gear bottom die.STL** ”. The geometry for gear bottom die is located in DEFORM installation folder \Tutorials directory. Define a reference point on the flash gutter using ![]({{ '/assets/icons/pre_icons/mo_define_reference_point_button.jpg' | relative_url }}) option. click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to positioning page.

#### Positioning dies

Rotate both dies 90° about the X axis so that they line up with the Workpiece. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Scheduled positioning page.

#### Scheduled positioning

Click on ![]({{ '/assets/icons/pre_icons/mo_auto_button.jpg' | relative_url }}) in scheduled positioning page and you can see the positioning scheduled as shown in Fig. L5.3\. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until stopping controls page.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab5_image0003.jpg' | relative_url }})

Scheduled positioning window

#### Stopping controls

Set the Distance between objects to **0.25** in. and set the **Top Die** and **Bottom Die** as reference objects. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to assign Primary die stroke page.

#### Primary die stroke

Define **Primary die stroke** value as **1.5** in input field. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Simulation controls page.

#### Simulation controls

Set **Number of steps** to **1000** , **Step****increment** to **5** , select **User****type** step definition method and define **constant****die****displacement** as **0.02** in.

Save the project and click on the MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode button (above the operation tree) to start the simulation.

### Run and monitor a simulation

3D simulations can be made to run faster by taking advantage of multiple processors or multiple cores on one processor. If your computer processors has 4 cores, then Click the ![]({{ '/assets/icons/simulator_icons/mo_run_options_action_lable.jpg' | relative_url }}) label.

set the Simulation Mode to **Interactive** and select **Continue****Run**  
specify the Processors Per Job as **4.**(**** See ****[Fig. L3. 13.](forming_lab3.htm#Fig_L3_13_Run_option_window))****

****Then click on![]({{ '/assets/icons/pre_icons/mo_save_button.jpg' | relative_url }}) button and then **![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}).**

Once the simulation is completed, click the MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode button to review results.

### Review the results

Play through all steps and observe the object shapes in 2D and 3D operations.

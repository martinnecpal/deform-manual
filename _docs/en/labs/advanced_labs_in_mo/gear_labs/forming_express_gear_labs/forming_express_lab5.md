---
lang: en
title: "Forming Express Lab5"
---

# Lab 5. 2D to 3D conversion

### Creating a New Problem

Create a new project called **FE_Gear23** and copy the existing project **FE_Gear_LargerBillet**. (See Fig. L5.1.) along with the database.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab5_image0001.jpg' | relative_url }})

MO New Project window

### Adding operations

Right-click on the 2nd operation tile in operation editor and delete it. Add the following operations:

  * [2D] Heat Transfer Express

  * 2D to 3D Converter (located under Simulation Operator in explorer tab)

  * [3D] Forming Express

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab5_image0002.jpg' | relative_url }})

Operations list in Operation Editor

In the initial **Upset** tile in Operation Editor, right-click on the **Workpiece** and **Pass object to All operations**. (See Fig. L5.2.)

### Upset Operation

Select Upset operation and click on the Temperature Calculation branch in object tree. Use **Calculate temperature in workpiece only** as shown in Fig. L5.3.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab5_image0003.jpg' | relative_url }})

Temperature calculation window

**Generating DB**

Click on the **Generate DB** branch in operation tree and click ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) and ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) to check and generate database. Click ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) to Heat Transfer Express operation.

### Heat Transfer Express operation

#### Process

In Process page, select the heating type as **Transfer**. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Object list.

#### Object selection

Select **1 workpiece only** radio button and select Heat Condition branch in object tree to define transfer time.

#### Heat Condition

Set the **transfer****time** to**5** seconds and accept the **default temperature and convection coefficient**. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Simulation controls.

#### Simulation Controls

Use the default values and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until 2D to 3D Convertor operation.

### Convert 2D to 3D operation

Verify **Z** is up (consistent with other models) and in 3D parameters enter start angle and **Revolve****angle** as **0** and **360** respectively. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Workpiece geometry page.

#### Workpiece Geometry

Leave the geometry type at the default Solid type. The**# of sections** sets the number of geometry sections around the circumference. One section per degree of rotation works well, so set the **# of sections** to **360**. Click ![]({{ '/assets/icons/pre_icons/mo_3d_preview_button.jpg' | relative_url }}) button to see the 3D geometry preview and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to workpiece mesh page.

#### Workpiece Mesh

Leave the mesh type and **# of elements** at the default **Tetrahedron** and **32000** respectively. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to workpiece Material page.

#### Workpiece Material

Leave the Material as (inherited) in Material page. click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top die general page.

### 3D Forming Express

#### Top die general

Keep the default **300** °F temperature for Top die, click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Top die geometry page.

#### Top die geometry

Import the top die geometry STL file “**gear top die.****STL** ” using the ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Import geometry from a file) button by browsing the geometry file path in installation folder V*_* \Tutorials directory.

Define a reference point on the flash land using ![]({{ '/assets/icons/pre_icons/mo_define_reference_point_button.jpg' | relative_url }}) option. click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Top die movement page.

#### Top die Movement

Set the **Speed** to a constant value of **3** in/sec in the **-Z** direction. click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Bottom die page.

#### Bottom Die general

Keep the default **300** °F temperature for Bottom die, click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Bottom die geometry page.

#### Bottom die geometry

Import the bottom die geometry STL file “**gear bottom die.****STL** ” using the ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Import geometry from a file) button by browsing the geometry file path in installation folder V*_* \Tutorials directory. The die comes in oriented along a different axis than the workpiece. We will address that in a later step. Define a reference point on the flash gutter using ![]({{ '/assets/icons/pre_icons/mo_define_reference_point_button.jpg' | relative_url }}) option. click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to positioning page.

#### Positioning dies

Rotate both dies by **90** ° about the **X** axis so that they line up with the Workpiece. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Scheduled positioning page.

#### Scheduled positioning

Click on ![]({{ '/assets/icons/pre_icons/mo_auto_button.jpg' | relative_url }}) button to generate the following scheduled positioning as shown in Fig. L5.4. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Primary die stroke page.

'

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab5_image0004.jpg' | relative_url }})

Scheduled positioning window

#### Primary die stroke

Define Primary die stroke value as **1.5** in input field. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Stopping controls page.

#### Stopping controls

Set the Distance between objects to **0.25** in. and set the reference objects to Top die and Bottom die. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Simulation controls stroke.

#### Simulation controls

Set **Number of steps** to **1000** , **Step increment** to **5** , we will use **User** type step increment method with constant **die displacement** to **0.02** in.

Save the project and click on the MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode button (above the operation tree) to start the simulation.

### Run and monitor a simulation

3D simulations can be made to run faster by taking advantage of multiple processors or multiple cores on one processor. If your computer processors has 4 cores, then Click the ![]({{ '/assets/icons/simulator_icons/mo_run_options_action_lable.jpg' | relative_url }}) label.

set the Simulation Mode to **Interactive** and select **Continue****Run**  
specify the MPI 3D as **4.** (See [Fig. L3.17.](forming_express_lab3.htm#Fig_L3_17_Run_option_window))

Then click on ![]({{ '/assets/icons/pre_icons/mo_save_button.jpg' | relative_url }}) button and then ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}).

Once the simulation is completed, click the MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) mode button to review results.

### Review the results

Play through all steps and observe the object shapes in 2D and 3D operations.

'![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab5_image0005.jpg' | relative_url }})

Shape of Object workpiece object before converting to 3D and after converting to 3D object

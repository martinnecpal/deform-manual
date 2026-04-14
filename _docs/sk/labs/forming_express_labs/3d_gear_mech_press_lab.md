---
lang: sk
title: "3D Gear-Mech Press Lab"
---

# 3D Gear Mechanical Press Lab

In This we will setup simple Gear blank operation using Mechanical press movement in 3D Forming Express wizard.

## Upset 

### Creating a New problem

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear. Create a new problem either by selecting **File** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear. Select "**3****D Forming Express** " radio button and unit system as "**English** " radio button in unit field as shown in Fig. 3DGML1.1. Define Problem Name as "**3D-****Gear-MechPress** " and click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Integrated Manufacturing Process.

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0001.jpg' | relative_url }})

Problem type selection window

Confirm that a 3D Forming Express operation tile is present in the operation editor. Rename the first operation to “**Upset** ” by double clicking on the operation tile in the operation editor (See Fig. 3DGML1.2.).

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0002.jpg' | relative_url }})

Renaming Operation name in Operation Editor

### Process

In the Process page choose **Symmetry** , **Hot forging** and set both slider bars one notch below moderate to speed up the simulation time (see Fig. 3DGML1.3.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to the temperature calculation page.

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0003.jpg' | relative_url }})

Process Page

### Temperature Calculation

In the Temperature calculation page, select **constant temperature (Isothermal)**. Selecting constant temperature means we are neglecting changes in workpiece temperature during forming. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Objects.

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0004.jpg' | relative_url }})

Temperature Calculation page

### Object Page

In the objects page select **1 workpiece + 2 dies** and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to the workpiece page.

### Workpiece

We will use an object temperature of **2200°F** for our workpiece. Move to the geometry page for the workpiece.

#### Workpiece Geometry

In the geometry page we will define primitive for our workpiece. Click on ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}). Select **Cylinder** type and define the workpiece dimensions to **2.5** in **Radius**(R), **8.267** in **Height**(H), **0.1** in **Corner****Radius**(r), with **Revolve****angle****90** and **Sections****45**(see [Fig. 3DGML1.5.]()) Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to Close. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to proceed to the Symmetry page.

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0005.jpg' | relative_url }})

Defining the Workpiece Geometry

#### Workpiece Symmetry

Define **Planar symmetry** for workpiece on Symmetry surfaces. Select the surfaces as shown in Fig. 3DGML1.6. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Generate Mesh.

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0006.jpg' | relative_url }})

Workpiece Symmetry window

#### Workpiece Mesh

Generate mesh for the **System****type** mesh settings value by click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) option as shown in Fig. 3DGML1.7. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to the material page for the workpiece.

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0007.jpg' | relative_url }})

Workpiece mesh generation

####  Workpiece Material

Click the ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load material from library) button as shown in Fig. 3DGML1.8. Select the **Steel_at_Extended_Temperatures** category, then **AISI-8620[1550-2200F(850 -1200C)]** and click the ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}) button. The material will be added to the material list and selected. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top Die Geometry page.

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0008.jpg' | relative_url }})

Workpiece material selection from Material Library

### Top Die

#### Top Die Geometry

Click on ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) button and import **3d_flat top die.stl** from the 3D\ LABS folder located in the installation directory and Check the geometry. Mark symmetry surfaces using Mark surface as shown in Fig. 3DGML1.9. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0009.jpg' | relative_url }})

Assigning Symmetry plane for Top die using Mark Surface option

#### Top Die Movement page

Here we will define our top die as a **mechanical press**. Select the **mechanical press** radio button and observe the options which that are available (see Fig. 3DGML1.10.).

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0010.jpg' | relative_url }})

Mechanical Press Movement page

Keep the default movement direction of **–Z.** Stiffness and connecting rod length are optional inputs for defining the mechanical press. For the first operation we will use a **total****stroke** of **40** inches and **1** stroke/sec. Select distance between dies and confirm the current stroke = -(total stroke). Click on until ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) bottom die geometry page (see Fig. 3DGML1.11.).

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0011.jpg' | relative_url }})

Top die movement data

### Bottom Die

#### Bottom Die Geometry

In the bottom die geometry page Click on ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}). Select **Cylinder** type and define the Bottom die dimensions to **8** inch **Radius**(R), **4** inch **Height**(H), with **Revolve****angle****90** and **Sections****45** and click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close (See Fig. 3DGML1.12.). Now click on **Mark Surface** and assign symmetry planes as we defined for Top die.

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0012.jpg' | relative_url }})

Bottom Die geometry

Observe the position of the three objects (see Fig. 3DGML1.13.). The top and bottom die are currently positioned inside of the workpiece which will result in excessive remeshing and unrealistic results. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Positioning page.

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0013.jpg' | relative_url }})

Objects Position after creating

### Positioning

In the positioning page, click the ![]({{ '/assets/icons/pre_icons/mo_automatic_positioning_button.jpg' | relative_url }}) button. You should see the top and bottom die position above and below the workpiece. Automatic positioning performs two actions:

  1. Interference position bottom die to workpiece while coupled with top die without updating stroke

  2. Interference position top die to workpiece while updating stroke.

After the dies have been positioned, keep the default contact settings and skip to the stopping controls page.

### Stopping Controls

For the distance between dies method we need to specify a **distance between objects** stopping criteria. Selected points similar to the ones displayed below.

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0014.jpg' | relative_url }})

Distance between objects Stopping controls

For the first operation, we want the top die to travel 6 inches in order to create the correct shape. Input a die distance value of **2.267** inches for distance between objects (see Fig. 3DGML1.14.). Click on ![]({{ '/assets/icons/pre_icons/mo_back_button.jpg' | relative_url }}) to primary die stroke page .

### Primary Die Stroke

Notice the total primary die travel is set to roughly 6 inches. The distance between dies method automatically calculates total primary die travel for the user. **When the exact amount checkbox is checked the value shown in the total primary die travel field is used as the forming stroke** (see Fig. 3DGML1.15.). **In operation 2 we will cover situations where exact amount is unchecked**. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Simulation controls page.

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0015.jpg' | relative_url }})

Primary die stroke

### Simulation Controls

We will be using the default system options (see Fig. 3DGML1.16.) and proceed to the generate DB page.

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0016.jpg' | relative_url }})

Simulation controls page

### Generate DB

In Generate DB page. Click the ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) button to have the program check to see if anything was missed in the problem setup. During the checking process:

Messages in the red color signify data that needs to be fixed before a simulation can be run (such as when you forget to define any material data).

Click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database. When the program is done writing the database, Save the project and click on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) mode to run the simulation.

### Running Simulation - Operation 1

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog. Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0017.jpg' | relative_url }})

Run Simulation window

The progress of the simulation can be monitored as it is running by looking at the Simulation Message tab and Simulation Graphics from the Graphics display region in Simulation mode. As long as the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked in Simulation Message tab, which is the default setting, the Message file will refresh automatically.

### Post process the results - Operation 1

After the simulation is completed, Switch to ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) tab to view the result.

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0018.jpg' | relative_url }})

MO Post processor

Some important state variables can be selected directly from ‘Post Tools’ window and the rest can be accessed through State Variable dialog by clicking on ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) icon.

Click on ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) Graph (Load-Stroke) and plot Time (sec) vs Load (klb) and also plot Time (sec) Vs Speed (in/sec) for top die.

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0019.jpg' | relative_url }})

Strain Effective state variable plot for workpiece at 1st operation last step

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0020.jpg' | relative_url }})

Z -Load v/s Time Graph of Top die in 1st operation

## Gear Finish

### Problem Setup

Add a new 3D Forming Express operation and select ![]({{ '/assets/icons/pre_icons/mo_no_batch_setup_button.jpg' | relative_url }}) as your method of defining the operation.

### Top Die

By default all objects will be passed to the second operation as read from DB objects. Skip to the top die page in the tree. All settings from the previous operation will be passed to operation 2 so there is no need to revisit the earlier pages. For the mechanical press it is best to never use a read from DB top die. Select Define as the object type to define new geometry for top die (see Fig. 3DGML1.21.).

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0021.jpg' | relative_url }})

Top Die page

#### Top Die Geometry

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to go to the geometry page for the top die. Import the geometry **3d_gear top die.stl** from the 3D\ LABS folder located in the installation directory. Mark symmetry surfaces using Mark surfaces as shown in Fig. 3DGML1.22.

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0022.jpg' | relative_url }})

Top die geometry import

#### Top Die Movement

Go to the top die movement page and select exact forming stroke. The previous press settings for total stroke and cycles per second are the same (see Fig. 3DGML1.23.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Bottom Die object page.

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0023.jpg' | relative_url }})

Top die movement data

### Bottom Die

Select **Define** as the object type. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to the geometry page.

#### Bottom Die Geometry

Import **3d_******gear** bottom die.stl** from the 3D\ LABS folder located in the installation directory. Mark Symmetry surfaces using Mark surface as shown in Fig. 3DGML1.24. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until the positioning page.

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0024.jpg' | relative_url }})

Bottom die geometry import

### Positioning

For operation 2 we will use the bottom dead center position action check box to calculate our forming stroke. In order to use this action checkbox the top and bottom die must be positioned at bottom dead center.

Before positioning, take note of the forming stroke value in the top die movement page. In the positioning page**interference position** the top die down to the bottom die in the –Z direction.

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0025.jpg' | relative_url }})

Interference positioning

Then **offset position** the **top die by 0.2 inches** in the Z direction. The dies are now at bottom dead center position. **Switch** to the top die movement page and notice the forming stroke and current stroke that are updated based on the positioning which was applied. **For the mechanical press in Forming Express, forming stroke is always updated when the top die is positioned.**

### Primary Die Stroke

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until the primary die stroke page. Take note that there is no positioning scheduled and the distance between objects stopping criteria is disabled in Stopping Controls page, because exact forming stroke was selected in the top die movement page.

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0026.jpg' | relative_url }})

Primary Die stroke page

As mentioned previously, when exact amount is checked total primary die travel = forming stroke. The forming stroke was recently updated with positioning which explains the negative value seen for total primary die travel. Red text indicates that the value entered for total primary die stroke is outside of the legal range (See Fig. 3DGML1.26.).

It is up to the user to fix illegal total primary die travel value. Check the bottom dead center position check box and observe that the exact amount box is no longer checked as a result.

**When exact amount is unchecked total primary die travel is not equal to forming stroke and is only used to calculate the step size for the simulation. The user is required to input an approximate value for how far the top die is expected to travel.**

In this case the top die needs to travel approximately 2 inches to reach bottom dead center (see Fig. 3DGML1.27.).

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0027.jpg' | relative_url }})

Bottom dead center position checked in Primary die stroke page

The bottom dead center position check box will automatically add scheduled positioning and adjust the forming stroke to zero. Jump to scheduled positioning and the top die movement page to view these changes. The forming stroke value will be updated after scheduled positioning has been executed at DB generation. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Simulation Controls

We will be using the default system options (see Fig. 3DGML1.28.) and proceed to the generate DB page.

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0028.jpg' | relative_url }})

Simulation controls data

### Generate DB

In Generate DB page. click the ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) button and click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database. When the program is done writing the database, save the project and click on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) mode to run the simulation.

### Running Simulation - Operation 2

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog. Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

### Post process the results - Operation 2

After the simulation is completed, switch to ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) tab to view the result.

Some important state variables can be selected directly from ‘Post Tools’ window and the rest can be accessed through State Variable dialog by clicking on ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) icon.

Click on ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) Graph (Load-Stroke) and plot Time (sec) vs Load (klb) and also plot Time (sec) Vs Speed (in/sec) for top die for Operation 2.

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0029.jpg' | relative_url }})

Strain Effective state variable plot for workpiece at 2nd operation last step

![]({{ '/assets/images/labs/forming_express_labs/3d_gear_mech_press_lab/image0030.jpg' | relative_url }})

Z-Load v/s Time Graph of Top die in 2nd Operation

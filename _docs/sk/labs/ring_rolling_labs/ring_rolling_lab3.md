---
lang: sk
title: "Ring Rolling Lab3"
---

# Ring Rolling Lab3

In this lab we will be setting up simple Isothermal Ring Rolling operation.

  
3.1. Creating a New Problem

3.2. Process Page

3.3. Simulation Setup

3.4.Object selection

3.5. Defining Workpiece - Ring

3.5.1. Defining Workpiece - Ring object

3.5.2. Defining Workpiece - Ring 2D cross-section

3.5.3. Defining Workpiece - Ring 2D Mesh

3.5.4. Generating 3D Geometry for Workpiece - Ring

3.5.5. Generating 3D Mesh for Workpiece - Ring

3.5.6. Assign Workpiece-Ring Material

3.6. Defining Driving Roll

3.6.1. Defining Driving Roll Object

3.6.2. Driving roll 2D cross-section Page

3.6.3. Driving Roll 3D Geometry Page

3.6.4. Driving Roll orientation

3.6.5. Driving roll movement

3.7. Defining Pressure Roll

3.7.1. Defining Pressure Roll Object

3.7.2. Pressure roll 2D cross-section Page

3.7.3. Pressure Roll 3D Geometry Page

3.7.4. Pressure Roll orientation

3.7.5. Pressure roll movement

3.8. Contact Page

3.9. Stopping Controls

3.10. Step and Remeshing controls Page

3.11. Generate Database

3.12. Running Simulation

3.13. Post Processing

## Creating a New Problem

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear.

Create a new problem either by selecting **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in Fig. RRL3.1. Select " **Integrated Manufacturing Process** " radio button and Unit system as "**English** " using radio button. Define Problem Name as "**RING_ROLL_LAB3** " and make sure the “Show option dialog” check box is turned on (if we do not turn on the “**Show option dialog** ” check box, then we will not get the New Project dialog in MO UI). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0001.jpg' | relative_url }})

New Problem page

Multiple operation wizard will open with the New Project dialog, at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session, we will use ‘**RING_ROLLING_LAB3** ’ as the project name. 3D Ring Rolling operation can be added in "New Project" dialog buy turning on First operation check band selecting Ring Rolling operation from the drop down menu (see Fig. RRL3.2.) In this lab, we will add Ring rolling operation from Explorer operation list, so do not check "First operation" check box in "New Project" dialog. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to add the operation.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0002.jpg' | relative_url }})

Adding Ring rolling operation from New Project 

  
Add 3D Ring Rolling operation from the Explorer Operations list. Add the operation by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button available next to **3D Ring Rolling** or user can also add by drag and drop into the Operation Editor. When we add the Ring Rolling operation, Process settings page will be opened by default (See Fig. RRL3.3.).

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0003.jpg' | relative_url }})

Adding Ring rolling operation from Explorer

## Process Page

Ring rolling operation template can be used to setup Ring Rolling and Railroad wheel rolling, In Process page, by default **"Ring rolling (default)** " radio button will be selected (See Fig. RRL3.4.), we will retail this selection and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Simulation setup page.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0004.jpg' | relative_url }})

Process page

## Simulation Setup

Select "**Whole** " 3D model type radio button and keep default Thermal calculation type as "**C******o** nstant temperature (isothermal)**" in Simulation setup page as shown in Fig. RRL3.5. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Objects page.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0005.jpg' | relative_url }})

Simulation setup page

## Object selection

In “**Objects** ” page, we will use the current default objects as shown in Fig. RRL3.6., minimum 3 objects are required to setup ring rolling process, they are Workpiece (Ring), Pressure roll (mandrel) and Driving roll. We will not using any axial roll in this lab. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Workpiece - Ring page to define Ring object.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0006.jpg' | relative_url }})

Objects list for Whole model type

## Defining Workpiece - Ring 

### Defining Workpiece - Ring object

In Workpiece - Ring page define the Object temperature as **70** °F as shown in Fig. RRL3.7., click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to 2D Cross-section page.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0007.jpg' | relative_url }})

Workpiece - Ring Object page

### Defining Workpiece - Ring 2D cross-section

In Workpiece 2D cross-section page, click on ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) and select**H******ollo** w** **cylinder** primitive, define the **Outer radius** as “**8** ”, **Inner radius** as "6 ", **H****eight** as “**2** ” and **Corners****radius** as******0.25** at all corners as shown in Fig. RRL3.8. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the Geometry primitive page and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to 2D Mesh page.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0008.jpg' | relative_url }})

Workpiece – Ring 2D cross-section geometry definition

### Defining Workpiece - Ring 2D Mesh

In 2D mesh settings, define Target number of Elements as **100** , click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button and observe the generated mesh in display window (See Fig. RRL3.9.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to 3D Geometry page.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0009.jpg' | relative_url }})

Workpiece-Ring 2D Mesh generation

### Generating 3D Geometry for Workpiece - Ring

In 3D Geometry page, click on "**Revolve from 2D** " option, use the default values in Revolve from 2D page as shown in Fig. RRL3.10., and click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to 3D Mesh page.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0010.jpg' | relative_url }})

Workpiece-Ring 3D Geometry settings

### Generating 3D Mesh for Workpiece - Ring

In 3D Mesh page, select **Revolve with constant cross-section** radio button and with default value of **120** for "**Number of Revolving sections** ", generate 3D mesh by clicking on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). Observe the generated 3D Mesh for workpiece as shown in Fig. RRL3.11. If Ring is of non-uniform shape then user can import the geometry and select Revolve to fit 3D shape to generate non-uniform 3D Ring Mesh. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Material page.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0011.jpg' | relative_url }})

Workpiece-Ring 3D Mesh settings

### Assign Workpiece-Ring Material

In Material page, Click on ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})(Load material from library) icon and load the steel group material "**AISI-1035,COLD[70-400F(20-200C)]** " from material library window. Assign the "**AISI-1035,COLD[70-400F(20-200C)]** " material for Workpiece as shown in Fig. RRL3.12. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Workpiece BCC page.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0012.jpg' | relative_url }})

Workpiece-Ring material Page

## Defining Driving Roll

### Defining Driving Roll Object 

Keep the name as “**Driving Roll** " and temperature as**68°F** unchanged as shown in Fig. RRL3.13. and just click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to go to the 2D cross-section geometry page.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0013.jpg' | relative_url }})

Driving Roll object Page

### Driving roll 2D cross-section Page

In Driving Roll 2D cross-section page, click on ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) and select **H******o** llow cylinder **primitive, define the **Outer radius** as "**19** ", **Inner radius** as “**14** "**and** **height** as “**10** ” as shown in Fig. RRL3.14. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the Geometry primitive page and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to 3D Geometry page.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0014.jpg' | relative_url }})

Defining Driving roll 2D cross section

### Driving Roll 3D Geometry Page

In 3D Geometry page, click on "**Revolve from 2D** " option as shown in Fig. RRL3.15., use the default value of **100** as "**Number of layers in hoop direction** " in Revolve from 2D page as shown in Fig. RRL3.15.. and click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to generate 3D geometry as shown in Fig. RRL3.15.. and close. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Orientation page.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0015.jpg' | relative_url }})

Driving roll 3D Geometry settings

### Driving Roll orientation

In Driving Roll orientation page, select "**Set relative distance between object center** " option and define " **Vertical distance (d)** " as **4** in with "**Current object center's relative location** " as "**-Z** ", click on ![]({{ '/assets/icons/pre_icons/mo_apply_orientation_button.jpg' | relative_url }}) to move the Driving Roll by **2.25** in along the **Z** axis with respect to Ring object center (See Fig. RRL3.16.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Movement page.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0016.jpg' | relative_url }})

Defining Driving Roll Orientation

### Driving roll movement

Select **Angular velocity** in rotation movement controls for the driving roll and define a constant value**2** rad/sec. Notice a green rotation arrow showing rotational direction in the display window (See Fig. RRL3.17.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Object page of Pressure roll.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0017.jpg' | relative_url }})

Driving Roll Movement definition

## Defining Pressure Roll

### Defining Pressure Roll Object 

Keep the name of "**Pressure****Roll** " and temperature as **68°F** as shown in Fig. RRL3.18. and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to go to the 2D cross-section page.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0018.jpg' | relative_url }})

Pressure Roll object page

### Pressure roll 2D cross-section Page

In Pressure roll 2D cross-section page, click on ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) and select **cylinder** primitive define the **R******a** dius **and **Height** as **2** ” and **10** ” respectively as shown in Fig. RRL3.19. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the Geometry primitive page and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to 3D Geometry page.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0019.jpg' | relative_url }})

Defining Pressure Roll 2D Cross-section Geometry

### Pressure Roll 3D Geometry Page

In 3D Geometry page, click on "**Revolve from 2D** " option as shown in Fig. RRL3.20., use the default value of **100** for "**Number of layers in hoop direction** " in Revolve from 2D page in as shown in Fig. RRL3.20. and click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to generate 3D geometry for Pressure Roll as shown in Fig. RRL3.20. and close. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Orientation page.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0020.jpg' | relative_url }})

Pressure Roll 3D geometry settings

### Pressure Roll orientation

Select "**Set relative distance between object centers** " option and define " **Vertical distance (d)** " as **4.5** in with "**Current object center's relative location** " as "**-Z** ", click on ![]({{ '/assets/icons/pre_icons/mo_apply_orientation_button.jpg' | relative_url }}) to move the Pressure Roll down along **Z** axis by **4.5** in (See Fig. RRL3.21.) in Pressure Roll Orientation page. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Movement page.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0021.jpg' | relative_url }})

Pressure Roll Orientation settings

### Pressure roll movement

We will define Pressure Roll movement **Speed** as "**Constant** " as “**0.01** in/sec” while keeping **Torque** at “**0** ” as shown in Fig. RRL3.22. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Contact page.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0022.jpg' | relative_url }})

Pressure Roll movement page

## Contact Page

In Contact page, we will use the default shear friction value of **0.7** as shown in Fig. RRL3.23. and click on ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) to generate contacts between driving roll and the workpiece as well as between pressure roll and the workpiece (See Fig. RRL3.23.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Stopping controls page.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0023.jpg' | relative_url }})

Contact page 

## Stopping Controls

Define **process****duration** as **10** sec as shown in Fig. RRL3.24. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Step and remeshing control page. 

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0024.jpg' | relative_url }})

Stopping control page

## Step and Remeshing controls Page

Keep default **Number****of** **steps** of **10000** , set **Rotation****increment****to** **save** as **90** and **Max****allowed****time****step** as **0.01**. Keep default "**Remeshing control** ” as “**5** revolutions(s)” as shown in Fig. RRL3.25. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Generate DB.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0025.jpg' | relative_url }})

Step and remeshing control page

## Generate Database

In Generate DB page, click on the ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database. Observe the message in Message tab informing database generation status.

## Running Simulation

Once the database has been generated, switch to the Simulation mode by selecting the ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the object tree. Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. RRL3.26. Use the default **Continue Run** option to select “**Continue from the last step** ” (from step -1) option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0026.jpg' | relative_url }})

Run Simulation Window

  
Monitor the progress of the simulation by looking at the Simulation Message and Simulation Log tab, making sure that the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked. User can view the Ring Rolling process as the simulation proceeds to the specified stopping criteria from Simulation graphics.

## Post Processing

When the simulation is completed with ‘normal stop’, review the results by switching to Post mode using the ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) button above the Simulation tool bar.  
Play through the steps of the simulation and look how the workpiece-Ring is formed.  
  
Click on ![]({{ '/assets/icons/pre_icons/mo_show_single_obj_icon.jpg' | relative_url }}) Single object mode by selecting workpiece-Ring and plot Effective Stress of the workpiece-Ring. When we play through the steps, we can observe the increase in strain value. The Effective Stress distribution at the step 163 of the simulation should look like as shown in Fig. RRL3.27. The dimension of the ring at the last step is as shown in Fig. RRL3.28.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0027.jpg' | relative_url }})

Showing effective stress 

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab3/image0028.jpg' | relative_url }})

Dimensions of Ring at end of simulation

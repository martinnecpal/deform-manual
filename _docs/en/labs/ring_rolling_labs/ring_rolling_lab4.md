---
lang: en
title: "Ring Rolling Lab4"
---

# Ring Rolling Lab4

In this Lab we will be setting up simple Ring Rolling operation.

4.1. Creating a New Problem

4.2. Process Page

4.3. Simulation Setup

4.4. Object selection

4.5. Defining Workpiece-Ring Object

4.5.1 Defining Workpiece-Ring Object settings

4.5.2 Defining Workpiece-Ring 2D cross-section

4.5.3 Workpiece-Ring 2D cross section mesh generation

4.5.4 Generating Workpiece-Ring 3D Geometry

4.5.5 Generating Workpiece-Ring 3D Mesh

4.5.6 Assign Workpiece-Ring Material

4.6. Defining Driving Roll Object

4.6.1. Driving roll object settings

4.6.2. Defining Driving roll 2D cross-section

4.6.3. Generating Driving Roll 3D Geometry

4.6.4. Defining Driving Roll orientation

4.6.5. Defining Driving roll movement

4.7. Defining Pressure Roll Object

4.7.1. Defining Pressure Roll Object

4.7.2. Defining Pressure roll 2D cross-section Page

4.7.3. Generating Pressure Roll 3D Geometry Page

4.7.4. Defining Pressure Roll orientation

4.7.5. Defining Pressure roll movement

4.8. Contact Page

4.9. Defining Stopping Controls

4.10. Defining Step and remeshing controls Page

4.11. Generate Database

4.12. Running Simulation

4.13. Post Processing

## Creating a New Problem

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear.

Create a new problem either by selecting **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in [Fig. RRL4.1.]() Select " **Integrated Manufacturing Process** " radio button and Unit system as "**English** " using radio button. Define Problem Name as "**RING_ROLL_LAB4** " and make sure the “Show option dialog” check box is turned on (if we do not turn on the “**Show option dialog** ” check box, then we will not get the New Project dialog in MO UI). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0001.jpg' | relative_url }})

New Problem definition

Multiple operation wizard will open with the New Project dialog, at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session, we will use ‘**RING_ROLLING_LAB4** ’ as the project name. 3D Ring Rolling operation can be added in "New Project" dialog buy turning on First operation check band selecting Ring Rolling operation from the drop down menu (see Fig. RRL4.2.) In this lab, we will add Ring rolling operation from Explorer operation list, so do not check "First operation" check box in "New Project" dialog. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to add the operation.

  
Add 3D Ring Rolling operation from the Explorer Operations list. Add the operation by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button available next to **3D Ring Rolling** or user can also add by drag and drop into the Operation Editor. When we add the Ring Rolling operation, Process settings page will be opened by default (See Fig. RRL4.3.)

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0002.jpg' | relative_url }})

Adding Ring Rolling operation from New Project window

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0003.jpg' | relative_url }})

Adding Ring Rolling operation from Explorer

## Process Page

In Process page, by default "**Ring rolling (default)** " radio button will be selected (See Fig. RRL4.4.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Simulation setup.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0004.jpg' | relative_url }})

Process page

## Simulation Setup

Select "**Whole part** " 3D model type radio button and keep default Thermal calculation type as "**Constant temperature (isothermal)** " in Simulation setup page as shown in Fig. RRL4.5. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Objects page.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0005.jpg' | relative_url }})

Simulation model settings in Simulation setup page

## Object selection

In “**Objects** ” page, we will use the current default objects as shown in Fig. RRL4.6. Minimum of 3 objects workpiece (Ring), Pressure roll (mandrel) and driving roll are required to set up a simple ring rolling operation. In this lab, we will not be using any axial roll. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Workpiece - Ring page to define Ring object.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0006.jpg' | relative_url }})

Objects for ring rolling simulation setup

## Defining Workpiece-Ring Object 

### Defining Workpiece-Ring Object settings

In Workpiece-Ring page define the **Object****temperature** as **70** °F as shown in Fig. RRL4.7., Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to 2D Cross-section page.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0007.jpg' | relative_url }})

Workpiece - Ring Object settings

### Defining Workpiece-Ring 2D cross-section

To define initial ring shape, click on ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) link in Workpiece-Ring 2D cross-section page and select **H****ollow cylinder** primitive, define the **Outer radius** as "**8** ", **Inner radius** as "**6** ", **H****eight** as “**2******” and****and**Corners****radius** as**"****0.25"** at all corners as shown in Fig. RRL4.8. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the Geometry primitive page and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to 2D Mesh page.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0008.jpg' | relative_url }})

Workpiece – Ring 2D cross-section geometry settings

### Workpiece-Ring 2D cross section mesh generation

To generate mesh for 2D cross-section, in 2D mesh settings, define **Target number of Elements** as **100** and click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button and observe the generated mesh in display window (See Fig. RRL4.9.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to 3D Geometry page.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0009.jpg' | relative_url }})

Workpiece 2D Mesh settings

### Generating Workpiece-Ring 3D Geometry

In 3D Geometry page, click on ![]({{ '/assets/icons/pre_icons/mo_revolve_from_2d_label.jpg' | relative_url }}) option, use the defaults values in Revolve from 2D page and click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close (See Fig. RRL4.10.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to 3D Mesh page.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0010.jpg' | relative_url }})

Workpiece 3D geometry and settings

### Generating Workpiece-Ring 3D Mesh

In 3D Mesh page, with default value of **200** for "**Number of Revolving sections** " generate 3D mesh by clicking on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). Observe the generated 3D Mesh for workpiece as shown in Fig. RRL4.11. If Ring is of non-uniform shape, then user can import the geometry and select Revolve to fit 3D shape to generate non-uniform 3D Ring Mesh. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Material page. 

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0011.jpg' | relative_url }})

Workpiece-Ring 3D Mesh settings and generated mesh

###  Assign Workpiece-Ring Material

In Material page, click on ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load material from library) icon and load the **steel** group material "**AISI-1035,COLD[70-400F(20-200C)]** " from material library window. Assign the "**AISI-1035,COLD[70-400F(20-200C)]** " material for Workpiece as shown in Fig. RRL4.12. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Driving Roll object page.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0012.jpg' | relative_url }})

Workpiece-Ring material definition

## Defining Driving Roll Object

### Driving roll object settings

Keep the name of “**Driving********Roll** ” unchanged and temperature as **68** °F as shown in Fig. RRL4.13., click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to go to the 2D cross-section geometry page.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0013.jpg' | relative_url }})

Driving Roll object settings

### Defining Driving roll 2D cross-section

In Driving Roll 2D cross-section page, click on ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) and select **Hollow** **cylinder** primitive, define the **Outer radius** as "**19** ", **Inner radius** as "**14** " and **H****eight** as “**10** ” as shown in Fig. RRL4.14. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the Geometry primitive page and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to 3D Geometry page.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0014.jpg' | relative_url }})

Driving roll 2D cross section definition

### Generating Driving Roll 3D Geometry

In 3D Geometry page, click on ![]({{ '/assets/icons/pre_icons/mo_revolve_from_2d_label.jpg' | relative_url }}) option, use the default value of **100** for "**Number of layers in hoop direction** " in Revolve from 2D page (see Fig. RRL4.15.) and click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Orientation page.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0015.jpg' | relative_url }})

Driving roll 3D geometry and settings

### Defining Driving Roll orientation

In Driving Roll orientation page, select "**Set relative distance between object center** " option and define "**Vertical distance (d)** " as **4** in and "Current object center's relative location as "**-Z** " and click on ![]({{ '/assets/icons/pre_icons/mo_apply_orientation_button.jpg' | relative_url }}) to move the Driving Roll by **2.25** in along the Z axis with respect to Ring object center (See Fig. RRL4.16.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Movement page. 

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0016.jpg' | relative_url }})

Driving Roll Orientation settings

### Defining Driving roll movement

Select **Angular velocity** in rotation movement controls for the driving roll and define a constant value **2** rad/sec. Notice a green rotation arrow showing rotational direction in the display window (See Fig. RRL4.17.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Object page of Pressure roll.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0017.jpg' | relative_url }})

Driving Roll Movement controls

## Defining Pressure Roll Object 

### Defining Pressure Roll Object 

Keep the name of "**Pressure Roll** " and temperature as **68** °**F** as shown in Fig. RRL4.18. and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to go to the 2D cross-section page.

  
![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0018.jpg' | relative_url }})

Pressure Roll object page

### Defining Pressure roll 2D cross-section Page

In Pressure Roll 2D Geometry page, click on ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}) and define the co-ordinates data as shown in below Table and Fig. RRL4.19. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the Edit Window and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to 3D Geometry page.

**X** |  **Y** |  **R**  
---|---|---  
0 |  0 |  0  
2 |  0 |  0  
2 |  4.5 |  0  
2.25 |  4.75 |  0.25  
2.25 |  5.25 |  0.25  
2 |  5.5 |  0  
2 |  10 |  0  
0 |  10 |  0  
0 |  0 |  0  
  
![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0020.jpg' | relative_url }})

Pressure Roll Geometry definition

### Generating Pressure Roll 3D Geometry Page

In 3D Geometry page, click on ![]({{ '/assets/icons/pre_icons/mo_revolve_from_2d_label.jpg' | relative_url }}) option, Use the default value of **100** for "**Number of layers in hoop direction** " in Revolve from 2D page (See Fig. RRL4.20.) and click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Orientation page.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0021.jpg' | relative_url }})

Pressure roll 3D geometry and settings

### Defining Pressure Roll orientation

Select "**Set relative distance between object centers** " option and define " **Vertical distance (d)** " as **4** in and "**Current object center's relative location** " as "**-Z** ", click on ![]({{ '/assets/icons/pre_icons/mo_apply_orientation_button.jpg' | relative_url }}) to move the Pressure Roll down along **Z** axis by **4.5** in (See Fig. RRL4.21.) in Pressure Roll Orientation page. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Movement page.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0022.jpg' | relative_url }})

Pressure Roll Orientation settings

### Defining Pressure roll movement

We will define Pressure Roll movement as "Constant" “**Speed** ” of “**0.01** in/sec” as shown in Fig. RRL4.22. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Contact page.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0023.jpg' | relative_url }})

Pressure Roll movement controls

## Contact Page

In Contact page, use the default shear friction value of**0.7** and click on ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) to generate contacts between driving roll and the workpiece as well as between pressure roll and the workpiece (See Fig. RRL4.23.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Stopping controls page.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0024.jpg' | relative_url }})

Inter-object relation settings 

## Defining Stopping Controls

Define **process****duration** as **10** sec as shown in Fig. RRL4.24. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Step and remeshing control page. 

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0025.jpg' | relative_url }})

Stopping controls

## Defining Step and remeshing controls Page

Keep **Number of steps** as **10000** and define **Rotation** increment to save as **90** and Max allowed time step as 0.01. Keep "Remeshing control” as “5 revolutions(s)” as shown in Fig. RRL4.25. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Generate DB.

  
![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0026.jpg' | relative_url }})

Step and remeshing controls

## Generate Database

In Generate DB page, click on the ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database. Observe the message in Message tab informing database generation status.

## Running Simulation

Once the database has been generated, switch to the Simulation mode by selecting the ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the object tree. Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. RRL4.26. Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0027.jpg' | relative_url }})

Run Simulation settings

  
Monitor the progress of the simulation by looking at the Simulation Message and Simulation Log tab, make sure that the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked. User can view the Ring Rolling process as the simulation proceeds to the specified stopping criteria from Simulation graphics.

## Post Processing

When the simulation is completed with ‘normal stop’, review the results by switching to Post mode using the ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) button above the Simulation tool bar.  
Play through the steps of the simulation and look how the Workpiece-Ring is formed.  
  
Click on ![]({{ '/assets/icons/pre_icons/mo_show_single_obj_icon.jpg' | relative_url }}) Single object mode by selecting Workpiece-Ring and plot Effective Strain of the Workpiece-Ring. When we play through the steps, we can observe the increase in strain value. The Effective Stress value at the end of the simulation should look like as shown in Fig. RRL4.27.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab4/image0028.jpg' | relative_url }})

Effective strain at the end of simulation

---
lang: sk
title: "Ring Rolling Lab1"
---

# Ring Rolling Lab1

In this Lab we will be setting up simple symmetry model type Ring Rolling operation.

1.1 Creating a New Problem

1.2. Process Page

1.3. Simulation Setup

1.4. Object selection

1.4.1. Workpiece-Ring General Page

1.4.2. Driving Roll Object Page

1.4.3. Pressure Roll Object Page

1.5. Contact Page

1.6. Stopping Controls

1.7. Step and Remeshing controls Page

1.8. Simulation controls

1.9. Generate Database

1.10. Running Simulation

1.11. Post Processing

## Creating a New Problem

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear.

Create a new problem either by selecting **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in Fig. RRL1.1. Select " **Integrated Manufacturing Process** " radio button and Unit system as "**English** " using radio button. Define Problem Name as "**RING_ROLL_LAB1** " and make sure the “Show option dialog” check box is turned on (if we do not turn on the “**Show option dialog** ” check box, then we will not get the New Project dialog in MO UI). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

New Problem page

Multiple operation wizard will open with the New Project dialog, at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session we will use ‘**RING_ROLL_LAB1** ’ as the project name. 3D Ring Rolling operation can also be added in "New Project" dialog (see Fig. RRL1.2.), in this lab we will add Ring rolling operation from Explorer operation list, so do not check "First operation" check box and " Ring Rolling" operation in "New Project" dialog. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

Add 3D Ring Rolling operation from the Explorer Operations list. Add the operation by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button available next to 3D Ring Rolling or user can also add by drag and drop into the Operation editor (See Fig. RRL1.3.). When we add the Ring Rolling operation, process settings window will open by default.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0002.jpg' | relative_url }})

Adding Ring rolling operation from New Project

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0003.jpg' | relative_url }})

Adding Ring rolling operation from Explorer

## Process Page

In Process page by default "**Ring rolling (default)** " radio button will be selected (See Fig. RRL1.4.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Simulation setup.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0004.jpg' | relative_url }})

Process page

## Simulation Setup

Select "**Symmetry** " 3D model type radio button and keep default Thermal calculation type as "**Constant temperature (isothermal)** " in Simulation setup page as shown in Fig. RRL1.5. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Objects page.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0005.jpg' | relative_url }})

Simulation setup page

## Object selection

In “**Objects** ” page, we will use the current default objects as shown in Fig. RRL1.6. Minimum of 3 objects workpiece (Ring), Pressure roll (mandrel) and driving roll are required to set up a simple ring rolling operation. In this lab we will not using any axial roll. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Workpiece - Ring page to define Ring object.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0006.jpg' | relative_url }})

Objects list for Symmetry model

### Workpiece-Ring General Page

In Workpiece-Ring page define the Object temperature as 70F as shown in Fig. RRL1.7, the default object type for workpiece (Ring) is plastic. In this lab we will create workpiece hence we will leave the default values as shown in Fig. RRL1.7. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to 2DCross- section page.

#### Extract cross-section from 3D shape

In case user is importing the object from a file then Axis/Center can be calculated using the ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) button and Extract cross-section will be enabled so that user can extract cross-section of the imported object (See Fig. RRL1.8.). From the imported object user can extract single cross-section from a particular layer using “Extract cross-section at layer no” or user can extract multiple cross-section from different layers in case of non-uniform ring and use the average size as cross-section using “Extract Cross-section from Layers and use their average”. 

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0007.jpg' | relative_url }})

Workpiece-Ring page

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0008.jpg' | relative_url }})

Extract cross-section page

#### Workpiece-Ring 2D cross-section Page

In Workpiece 2D cross-section page, click on **![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }})**and define the co-ordinates data as shown in Fig. RRL1.9. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the Edit Window and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to 2D Mesh page. In 2D Geometry page user has also options to import 2D cross-section using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) button from a file or using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) button from library.

**X** |  **Y** |  **R**  
---|---|---  
4 |  3.25 |  0  
4.75 |  3.25 |  0  
4.75 |  4.5 |  0.062  
3.75 |  4.5 |  0.03  
3.75 |  3.25 |  0  
4 |  3.25 |  0  
  
![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0009.jpg' | relative_url }})

Workpiece edit geometry page

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0010.jpg' | relative_url }})

Workpiece 2D Geometry page

#### Workpiece-Ring 2D Mesh Page

In 2D mesh settings, define **Target Number of Elements** as **80** and click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button and observe the generated mesh in Mesh window (See Fig. RRL1.11.). Expert mode is available for the user in case of complex ring geometries to define advanced mesh conditions like mesh windows, change weighing factors,..etc as shown in Fig. RRL1.12. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to 3D Geometry page.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0011.jpg' | relative_url }})

Workpiece 2D Mesh page - Guided mode

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0012.jpg' | relative_url }})

Workpiece 2D Mesh - Expert mode

#### Workpiece-Ring 3D Geometry Page

In 3D Geometry page, click on "**Revolve from 2D** " option (See Fig. RRL1.13.), use the default values in Revolve from 2D page and Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close. If user has loaded a 3D geometry of the workpiece from a file, then Extract cross-section option can be used to extract the cross-section from the 3D Geometry and use it to revolve into 3D Geometry. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to 3D Mesh page.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0013.jpg' | relative_url }})

Workpiece- Ring 3D Geometry page

#### Workpiece-Ring 3D Mesh Page

In 3D Mesh page we have options to create mesh with uniform cross-section or to fit 3D Shape in case of workpiece having non-uniform cross-section. For this lab we will use default value of **120** for " **Number of Revolving sections** " and generate 3D mesh by clicking on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). Observe the generated 3D Mesh for workpiece is should looks like as Fig. RRL1.14. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Workpiece Orientation page. 

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0014.jpg' | relative_url }})

Workpiece-Ring 3D Mesh Page

#### Workpiece Orientation

Workpiece is at 0 angle from object axis to +Z axis, so no need to position the Workpiece (See Fig. RRL1.15.), click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Workpiece Material page.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0015.jpg' | relative_url }})

Workpiece orientation page

#### Assign Workpiece-Ring Material

In Material page, click on ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load material from library) icon and load the material **steel** group material " **AISI-5135H,COLD[70-550F(20-300C)]** " from material library window. Assign the "**AISI-5135H,COLD[70-550F(20-300C)]** " material by selecting it for Workpiece. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Workpiece BCC page.

#### Assign BCC for Workpiece-Ring

Check the default Symmetry BCC assigned for workpiece, default symmetry BCC should be assigned for Symmetry surface as shown in Fig. RRL1.16. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Driving Roll Object page.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0016.jpg' | relative_url }})

Workpiece-Ring Boundary condition page

**Note on Ring Rolling operation added as second operation in batch mode:**

Ring Rolling operation can be added as second operation in batch mode after pre-forming ring using Forming operation or after heat transfer operation. In such case, user can regenerate the ring by checking Regenerate ring check box (see Fig. RRL1.17.). When user checks" Regenerate Ring " check box, "Extract cross-section" page is added and can be accessed using ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button from the workpiece object page. User can extract the cross-section geometry for 2D cross-section mesh using options from extract cross-section page of workpiece object, the options available are shown in Fig. RRL1.18.

User can extract single cross-section using "Extract One cross-section" option from "Constant Cross section" tab. If user wants single cross-section from multiple layers of non-uniform ring then user can extract multiple cross-sections from different layers and use the average size as cross-section using “Extract multiple Cross sections from Layers and use their average” option.

User can extract multiple cross-sections and retain them to generate non-uniform ring using “Extract multiple Cross sections from Layers” option from "Variable Cross-section" tab

When user regenerates Ring in batch mode then the Ring is automatically aligned to Z-axis and the X co-ordinate of its center is moved to ‘0’, if user does not regenerate ring then the Ring will be aligned to Z-axis without modifying Ring center co-ordinates.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0017.jpg' | relative_url }})

Read from DB Workpiece General page

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0018.jpg' | relative_url }})

Read from DB workpiece Extract cross-section page

### Driving Roll Object Page

Keep the name of Driving roll unchanged and just click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to go to the 2D cross-section geometry page.

#### Driving roll 2D cross-section Page

In Driving Roll Geometry page, click on ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}) and define the co-ordinates data as shown in Fig. RRL1.19. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the Edit Window and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to 3D Geometry page.

**X** |  **Y** |  **R**  
---|---|---  
0 |  1.25 |  0  
5 |  1.25 |  0  
5 |  1.9875 |  0.025  
4.66 |  2 |  0.093  
4.66 |  4.5 |  0.093  
5 |  4.525 |  0.025  
5 |  5.25 |  0  
0 |  5.25 |  0  
  
![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0019.jpg' | relative_url }})

Driving Roll 2D Geometry page

#### Driving Roll 3D Geometry Page

In 3D Geometry page, click on "**Revolve from 2D** " option, use the default value of **100** for "**Number of layers in hoop direction** " in Revolve from 2D page and Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Orientation page.

#### Driving Roll orientation

When we visit Orientation page by default Rolls will be in interference position with Workpiece, now the Workpiece and Rolls are in correct position so no need to do position. So, click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Movement page.

The orientation page can be used to position the Driving Roll along the axis by specifying the distance with respect to the object centers or distance between the objects bottom faces, see Fig. RRL1.20.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0020.jpg' | relative_url }})

Driving Roll orientation page

#### Driving roll movement

Select **Angular velocity** in rotation movement controls for the driving roll and define a constant value of **20.943** rad/sec. Notice a green rotation arrow showing rotational direction in the display window (See Fig. RRL1.21.). Click on![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Object page of Pressure roll.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0021.jpg' | relative_url }})

Driving Roll Movement page

### Pressure Roll Object Page

Keep the name "Pressure Roll" unchanged and just click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to go to the 2D cross-section page.

#### Pressure Roll 2D cross-section Page

In Pressure Roll 2D Geometry page, click on ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}) and define the co-ordinates data as shown in Fig. RRL1.22. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the Edit Window and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to 3D Geometry page.

**X** |  **Y** |  **R**  
---|---|---  
0 |  0 |  0  
2 |  0 |  0  
2 |  1.975 |  0.025  
1.62 |  2 |  0.093  
1.62 |  2.75 |  0  
1.75 |  3.25 |  1.5  
1.62 |  3.75 |  0  
1.62 |  4.5 |  0.093  
2 |  4.525 |  0.025  
2 |  6 |  0  
0 |  6 |  0  
  
![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0022.jpg' | relative_url }})

Pressure Roll Geometry page

#### Pressure Roll 3D Geometry Page

In 3D Geometry page, click on "**Revolve from 2D** " option, Use the default value of **100** for "**Number of layers in hoop direction** " in Revolve from 2D page and Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Orientation page.

#### Pressure Roll orientation

Now the Workpiece and Rolls are in correct position so no need to position. So, click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Movement page.

The orientation page can be used to position the Pressure Roll along the axis by specifying the distance with respect to the object centers or distance between the objects bottom faces, see Fig. RRL1.23.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0023.jpg' | relative_url }})

Pressure roll orientation page

#### Pressure roll movement

We will define Pressure Roll movement **Speed** as "**Function of time** " as shown below table and Fig. RRL1.24. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Contact page.

**Time** |  **Speed**  
---|---  
0 |  0.03  
5 |  0.03  
15 |  0.015  
20 |  0.015  
  
![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0024.jpg' | relative_url }})

Pressure Roll Speed as Function of Time Movement

## Contact Page

In Contact page, use the default shear friction value and click on ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) to generate contacts between driving roll and the workpiece as well as between pressure roll and the workpiece (See Fig. RRL1.25.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Stopping controls page.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0025.jpg' | relative_url }})

Contact page

## Stopping Controls

Select Primary die as "**Pressure roll (Mandrel)** "and define the **Y** displacement value as "**0.375** " under Max. primary die displacement as shown in Fig. RRL1.26. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define Step and Remeshing controls page.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0026.jpg' | relative_url }})

Stopping controls page

## Step and Remeshing controls Page

Enter Number of steps as **20000** , Rotation increment to save as **360** and Max allowed time step as **0.02**. Use default Remeshing control as shown in Fig. RRL1.27., user can turn on this option to remesh object after specified number of revolutions to maintain good workpiece shape in case of complex geometries. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Simulation controls.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0027.jpg' | relative_url }})

Step and Remeshing controls page

## Simulation controls

In this page, user can define constraints to the workpiece center as shown in Fig. RRL1.28. checking respective check box.

User can also add a virtual table at top or bottom by checking respective check box and specifying the distance of virtual table location from top / bottom surface.

Using advanced settings from Advanced Control tab, user can define the frequency of steps to verify for node penetration in case user observes heavy penetration into rolls. User can also specify angle for contact search to improve the Solution speed.

If the ring object is not rotating properly then user can check “Enforce to rotate workpiece when it does not rotate well at certain steps” to make small corrections to the ring rotation during the ring rolling process.

The data defined in this page will be written to **DEF_RRE.DAT** file.

In this lab we will use the default settings and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Generate DB page.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0028.jpg' | relative_url }})

a. Stability controls

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0029.jpg' | relative_url }})

b. Advanced controls

Simulation controls

## Generate Database

In Generate DB page, click on the ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database. Observe the message in Message tab informing database generation status.

##  Running Simulation

Once the database has been generated, switch to the Simulation mode by selecting the ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the object tree. Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. RRL1.29. Use the default **Continue Run** option to select “**Continue from the last step** ” (from step -1) option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0035.jpg' | relative_url }})

Run Simulation Window

Monitor the progress of the simulation by looking at the Simulation Message and Simulation Log tab, making sure that the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked. User can view the Ring Rolling process as the simulation proceeds to the specified stopping criteria from Simulation graphics.

##  Post Processing

When the simulation is completed with ‘normal stop’, review the results by switching to Post mode using the ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) button above the Simulation tool bar.

Play through the steps of the simulation and look how the workpiece-Ring is formed.

Click on 3D Mirroring and add symmetry on the symmetry plane of the Workpiece - Ring.

Click on ![]({{ '/assets/icons/pre_icons/mo_show_single_obj_icon.jpg' | relative_url }}) Single object mode by selecting workpiece-Ring and plot Effective Strain and Effective Stress of the workpiece-Ring. When we play through the steps, we can observe the increase in strain value. The Effective strain and Stress value at the end of the simulation should look like as shown in Fig. RRL1.30.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0030.jpg' | relative_url }})

Showing the effective strain and effective stress

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0031.jpg' | relative_url }})

Showing the ring after completion of simulation

The below Fig. RRL1.32. shows the initial and final dimensions of the ring. The user can make out the difference in ring diameter at the end of the simulation.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0032.jpg' | relative_url }})

Initial and Final Dimensions of the ring.

Final Cross section of the ring is as shown in below Fig. RRL1.33. and Fin defect in Ring rolling is as shown in Fig. RRL1.34.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0033.jpg' | relative_url }})

Showing the Cross Section Thickness after completion of simulation at various curvatures.

![]({{ '/assets/images/labs/ring_rolling_labs/ring_rolling_lab1/image0034.jpg' | relative_url }})

Showing Fin Defect in Ring Rolling

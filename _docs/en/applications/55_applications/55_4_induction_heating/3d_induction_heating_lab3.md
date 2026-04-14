---
lang: en
title: "3D Induction Heating Lab3"
---

# Lab 3: Dual Frequency Hot switching type Induction Heating

  
3.1. Creating New Problem

3.2. Adding 3D Forming Operation

3.3. Defining Simulation controls

3.4. Loading material into Material list

3.5. Adding Objects

3.6. Defining Workpiece

3.7. Defining Coil

3.8. Defining Step controls

3.9. Generate Data Base

3.10. Running Simulation

3.11. Post-Processing

## Creating New Problem

On a Windows machine, go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button, select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** v1x.x from the DEFORM v1x.xxx menu. The DEFORM GUI Main window will appear.

![]({{ '/assets/images/applications/55_2_arc_welding/image0002.jpg' | relative_url }})

New Problem dialog.

Create a new problem either by selecting **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****New** **Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear. Select "**Integrated Manufacturing Process"** radio button and unit system as "**SI** " radio button in Unit field as shown in Fig. 3DINDL3.1. Define problem Name as “**3D_Induction_Heating_HotSwitching** " and make sure the “Show option dialog” check box is turned on (if we do not turn on the “**Show option dialog** ” check box, then we will not get the New Project dialog in MO UI). Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Deform Integrated Manufacturing Process.  
  
Multiple operation wizard will open with the New Project dialog, at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session, we will use “**3D_Induction_Heating_HotSwitching** " as the project name (see Fig. 3DINDL3.2.). Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab3/image0002.jpg' | relative_url }})

New Project Window in Multiple Operation Wizard.

## Adding 3D Forming operation

Multiple Operation wizard will open, add one **3D Forming operation** from Operations list in Explorer by clicking ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button as shown in Fig. 3DINDL3.3.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab3/image0003.jpg' | relative_url }})

Adding 3D Forming operation into Operation Editor.

## Defining Simulation Controls

As the 3D forming operation is added, Simulation controls page is displayed in property editor region. In the Simulation controls page, **uncheck** the **Deformation** check box and **check** the **Heating** check box. From drop down menu of **Heating** , select **Induction (BEM)** as shown in Fig. 3DINDL3.4. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Material page.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab3/image0004.jpg' | relative_url }})

Simulation control window.

## Loading material into Material list

In Material list page, using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) option load the material from file **AL 1100 COLD [70F(20C)].****key** available under **/3D/LABS/Induction_Heating/Hot_switching**. Similarly, load the material from file **coil.key.** This can be done as shown in Fig. 3DINDL3.5. by clicking ![]({{ '/assets/icons/pre_icons/mo_open_button.jpg' | relative_url }}) button. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Objects page.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab3/image0005.jpg' | relative_url }})

Loading material into Material list.

## Adding Objects

By default, 3 objects are added into the objects list. We require only two objects for this lab, hence delete the last object “Bottom Die”. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Workpiece page (See Fig. 3DINDL3.6.). 

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab3/image0006.jpg' | relative_url }})

Adding required objects in Object page.

## Defining Workpiece

### Workpiece object general definition

Keep default object name as “**Workpiece** ”, Temperature as **20** °C and object type as “**Plastic** ” as shown in Fig. 3DINDL3.7. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Geometry page. 

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab3/image0007.jpg' | relative_url }})

Workpiece object page.

### Defining Workpiece Geometry

In Geometry page, click on ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) link and create **cylinder** geometry with **Diameter(2R) 200mm** and **Height (H)****300mm** as shown in the Fig. 3DINDL3.8. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button to close the Geometry Primitive page.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab3/image0008.jpg' | relative_url }})

Defining Workpiece Geometry. 

**Brick Mesh settings in Geometry page:**

We will be generating brick mesh for Workpiece. To generate the brick mesh, click on the ![]({{ '/assets/icons/pre_icons/mo_setup_brick_mesh_label.jpg' | relative_url }}) link in the geometry page. Select the "**Revolve** " radio button and select revolve type as “**Full Revolve** ”, accept the default revolve angle as shown in ( Fig. 3DINDL3.9.). Click on the ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button to exit the brick mesh geometry setup. 

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab3/image0009.jpg' | relative_url }})

Defining brick mesh settings in geometry page.

### Generating Mesh for Workpiece

Switch to expert mode using ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) to define brick mesh settings. From General tab of Mesh page, select the "**Brick** **Mesh** " radio button and the "**Uniform****thickness** " radio button, set the "**# of layers** " to **60** as shown in Fig. 3DINDL3.10. In the "**2D Cross Section** " tab, set the **Number of elements** as **200** , **Thickness****elements** as **4** and the **Size****ratio** as **1**. Click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button and click ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}) in Default Boundary conditions popup to assign default BCC as shown Fig. 3DINDL3.11. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to assign material.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab3/image0010.jpg' | relative_url }})

Brick mesh settings in mesh page for Workpiece.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab3/image0011.jpg' | relative_url }})

2D Cross-section mesh settings for Workpiece and mesh generated. 

### Assigning Material to Workpiece

Click on the **AL 1100 COLD[70F(20C)]** in the Material window to assign the material to Workpiece as shown in Fig. 3DINDL3.12. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Boundary conditions page.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab3/image0012.jpg' | relative_url }})

Assigning Material to Workpiece.

### Assigning Boundary Conditions to Workpiece

In Boundary conditions page, check whether the Heat exchange with environment Boundary condition has been assigned to the workpiece surface by default during mesh generation. If it is not applied, then add Heat exchange with environment BCC to all surfaces.   
Click on the **Induction BEM – Heating Surface** , click on ![]({{ '/assets/icons/pre_icons/mo_select_all_icon.jpg' | relative_url }}) so that all surfaces are selected, then assign BCC by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}). Added Induction BEM - Heating surface is as shown in Fig. 3DINDL3.13. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top Die object page.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab3/image0013.jpg' | relative_url }})

Assigning Induction BEM BCC.

## Defining Coil

### Coil general object data definition

In Top Die page, change the object name to Coil. Using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) option, import **Coil_Object.key** from **/3D/LABS/Induction_Heating/****Hot_switching** folder. The imported object is having Coil geometry along with mesh data as shown in Fig. 3DINDL3.14. Since, we don’t need to generate geometry and mesh, we will navigate using ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Material page. 

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab3/image0014.jpg' | relative_url }})

Importing Coil object data.

### Assigning Material to Coil

Click on the **Coil** in the Material page to assign the material to Coil as shown in Fig. 3DINDL3.15. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Boundary conditions page.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab3/image0015.jpg' | relative_url }})

Assigning material to Coil.

### Assigning Boundary Conditions to Coil

In BCC page, under**Induction BEM** from BCC tree, select **Heating Surface** option and select all surfaces of the Coil using ![]({{ '/assets/icons/pre_icons/mo_select_all_icon.jpg' | relative_url }}) and then click on ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) to finish the assignment (See Fig. 3DINDL3.16.).

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab3/image0016.jpg' | relative_url }})

Assigning Heating Surface BCC.

Select **Coil Begin surface** option under Induction BEM BCC, select Coil begin surface and assign using ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) as shown Fig. 3DINDL3.17.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab3/image0017.jpg' | relative_url }})

Assigning Coil Begin Surface BCC.

Similarly, select Coil **End Surface** option under Induction BEM BCC, select Coil End surface and assign using ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) as shown in Fig. 3DINDL3.18. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Properties page.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab3/image0018.jpg' | relative_url }})

Assigning Coil End Surface BCC.

### Defining Coil properties

Select "**Heating** " tab in object “**Properties** ” page, select **Dual** radio button from **Current****frequency** type. Select “**Hot****switching** ” radio button as **Dual****frequency** type and define **frequency** information as,**f1=1000** , **f2=10000** , **w1=0.5** and **w2=0.5** under Dual frequency as shown in Fig. 3DINDL3.19. Select **Volume****charge** type as **Current****density** and define **constant** value **65** under “**Data********Definition** ” tab as shown in Fig. 3DINDL3.19. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Step page.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab3/image0019.jpg' | relative_url }})

Coil Property.

## Defining Step controls

In Step controls page, define **Number of Simulation steps** as **40** and **Step Increment to save** as **1**. Select **Time** as Solution step definition type and define constant**0.1** sec/step as step definition as shown in Fig. 3DINDL3.20. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button to Generate database page. 

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab3/image0020.jpg' | relative_url }})

Defining step controls for simulation.

## Generate Database

In Generate database page, click the ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) button to have the program check to see if anything was missed in the problem setup. During the checking process, messages in the red color signify data that needs to be fixed before a simulation can be run (such as when you forget to define any material data).

  
Click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database.

## Running Simulation

Once the database has been generated, switch to the Simulation mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the operation tree. Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. 3DINDL3.21. Use the default **Continue Run** option to select “**Continue from the last step** ” (from step -1) option and then select the Simulation mode as **Interactive.** Click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab3/image0021.jpg' | relative_url }})

Run Simulation window.

  
The progress of the simulation can be monitored as it is running by looking at the Simulation Message tab and Simulation Graphics from the Graphics display region in Simulation mode. if the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked in Simulation Message tab, which is the default setting, the Message file will refresh automatically.

  
The Message file provides information about which simulation step the simulation is currently on and information dealing with how well the simulation is running.

## Post-Processing

When the simulation is completed, review the results by switching to Post mode using the ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) button above the Simulation tool bar.  
In Step Browser, click on **All** button and plot **Temperature** state variable, observe the temperature distribution at last step which should look like as shown in Fig. 3DINDL3.22.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab3/image0022.jpg' | relative_url }})

Temperature distribution at the last step.

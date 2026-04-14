---
lang: en
title: "3D Induction Heating Lab2"
---

# Lab 2: 3D Combined Dual Frequency type Induction Heating

  
2.1. Creating New Problem

2.2. Adding 2D Operation

2.3. Simulation Controls settings

2.4. Load materials into Material list

2.5. Adding Objects

2.6. Defining Workpiece

2.7. Defining Coil

2.8. Defining Step controls

2.9. Generate Data Base

2.10. Running Simulation

2.11. Post-Processing

## Creating New Problem

On a Windows machine, go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button, select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** v1x.x from the DEFORM-v1x.xxx menu. The DEFORM GUI Main window will appear.

![]({{ '/assets/images/applications/55_2_arc_welding/image0002.jpg' | relative_url }})

New Problem dialog. 

Create a new problem either by selecting **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****New** **Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The New Problem Setup window will appear. Select "**Integrated Manufacturing Process"** radio button and unit system as "**SI** " radio button in Unit field as shown in Fig. 3DINDL2.1. Define problem Name as “**3D_Induction_Heating_Combined** " and make sure the “Show option dialog” check box is turned on (if we do not turn on the “**Show option dialog** ” check box, then we will not get the New Project dialog in MO UI). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Deform Integrated Manufacturing Process.  
  
Multiple operation wizard will open with the New Project dialog, at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session we will use “**3D_Induction_Heating_Combined** " as the project name. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation (see Fig. 3DINDL2.2 ).

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab2/image0002.jpg' | relative_url }})

MO Wizard New Project Opening Window.

## Adding 3D Forming operation

Multiple Operation wizard will open. add **3D Forming****operation** from Operations list of Explorer by clicking ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button as shown in Fig. 3DINDL2.3.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab2/image0003.jpg' | relative_url }})

Adding 3D Forming operation into Operation Editor.

## Simulation Controls settings

We will be using BEM type Induction heating in this lab hence, we will select Induction (BEM) in the Simulation controls page. To do so, in Simulation controls **uncheck** the **Deformation** check box and check the **Heating** check box and select **Induction (BEM)** from pull down below it as shown in Fig. 3DINDL2.4. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Material list page.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab2/image0004.jpg' | relative_url }})

Simulation controls settings.

## Loading materials into Material list 

In Material list page, load the material from file **AL 1100 COLD [70F(20C)].key** available under /3D/LABS/Induction_Heating/Combined. Similarly, load the material from file **coil.key**. This can be done by clicking ![]({{ '/assets/icons/pre_icons/mo_open_button.jpg' | relative_url }}) button as shown in Fig. 3DINDL2.5. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to objects page.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab2/image0005.jpg' | relative_url }})

Loading material into Material list

## Adding Objects

In Object page, we can observe 3 objects being added by default. For this lab, we will require only two objects for this lab hence, keep Workpiece and Top Die and delete the Bottom Die object (See [Fig. 3DINDL2.6.](/docs/en/applications/55_applications/55_4_induction_heating/55_4_induction_heating_labs_main_pg/)). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Workpiece page. 

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab2/image0006.jpg' | relative_url }})

Adding required objects.

## Defining Workpiece

### Workpiece object general definition

Keep object name as “**Workpiece** ”, **Temperature** as **20** °C and object type as “**Plastic** ” as shown in Fig. 3DINDL2.7. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Geometry page. 

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab2/image0007.jpg' | relative_url }})

Workpiece object page.

### Defining Workpiece Geometry

In Geometry page, click on ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) link and create **cylinder** geometry with **Diameter(2R)******20** 0mm **and **Height (H) 300mm** as shown in the Fig. 3DINDL2.8. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button to close Geometry Primitive page.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab2/image0008.jpg' | relative_url }})

Defining Workpiece Geometry.

**Brick mesh settings in Geometry page:**

We will be generating brick mesh for Workpiece. To generate the brick mesh, click on the ![]({{ '/assets/icons/pre_icons/mo_setup_brick_mesh_label.jpg' | relative_url }}) link in the geometry page. Select the "**Revolve** " radio button and select revolve type as “**Full Revolve** ”, accept the default revolve angle as shown in Fig. 3DINDL2.9. Click the ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button to exit the brick mesh geometry setup. 

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab2/image0009.jpg' | relative_url }})

Defining brick mesh settings in geometry page.

### Generating Mesh for Workpiece

Switch to expert mode using ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) to define brick mesh settings. From General tab of Mesh page,, select the "**Brick** **Mesh** " radio button and the "**Uniform****thickness** " radio button, set the "**# of layers** " to **60** as shown in Fig. 3DINDL2.10. In the "**2D Cross Section** " tab, set the **Targe number of elements** as **200** , **Thickness** **elements** as**4** and the **Size** **ratio** as **1**. Click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button and click ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}) in Default Boundary conditions popup to assign default BCC. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to assign material.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab2/image0010.jpg' | relative_url }})

Brick mesh settings in mesh page for Workpiece.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab2/image0011.jpg' | relative_url }})

2D Cross-section mesh settings for Workpiece and mesh generated.

### Assigning material to Workpiece

Click on the **AL 1100 COLD[70F(20C)]** in the material window to assign the material to the Workpiece as shown in Fig. 3DINDL2.12. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Boundary conditions page.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab2/image0012.jpg' | relative_url }})

Assigning material to Workpiece.

### Defining boundary conditions for Workpiece

In Boundary conditions page, check whether the Heat exchange with environment Boundary condition has been assigned to the workpiece surface by default during mesh generation. If it is not applied, then add Heat exchange with environment BCC to the entire outer surface of the object. 

Click on the **Induction BEM – Heating Surface** , click on ![]({{ '/assets/icons/pre_icons/mo_select_all_icon.jpg' | relative_url }}) so that all surfaces are selected and then assign BCC by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}). Added Induction BEM - Heating surface is as shown in Fig. 3DINDL2.13. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top Die object page

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab2/image0013.jpg' | relative_url }})

Assigning Induction BEM BCC.

## Defining Coil

### Coil object definition

In Top Die page, change the Object name to **Coil**. Using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) option, import **Coil_Object.key** from /3D/LABS/Induction_Heating/Combined folder. The imported Coil.key is having Coil geometry along with mesh data as shown in Fig. 3DINDL2.14. Since we don’t need to generate geometry and mesh, we will navigate using ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Material page. 

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab2/image0014.jpg' | relative_url }})

Importing Coil object data.

### Assigning Material to Coil

Click on the **coil** in the material window to assign the material to the Coil as shown in Fig. 3DINDL2.15. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Boundary conditions page.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab2/image0015.jpg' | relative_url }})

Assigning material to Coil.

### Defining boundary conditions for Coil

In BCC page, select Heating Surface option under **Induction BEM** from BCC tree and select all surfaces of the Coil using ![]({{ '/assets/icons/pre_icons/mo_select_all_icon.jpg' | relative_url }}), then click on ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) to finish the assignment (See Fig. 3DINDL2.16.).

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab2/image0016.jpg' | relative_url }})

Assigning Heating Surface BCC.

  
Select **Coil****Begin** **Surface** option under Induction BEM BCC, select Coil begin surface and assign using ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) as shown Fig. 3DINDL2.17.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab2/image0017.jpg' | relative_url }})

Assigning Coil Begin Surface BCC.

Similarly, select**Coil End Surface** option under Induction BEM BCC, select Coil End surface and assign using ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) as shown in Fig. 3DINDL2.18. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Properties page.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab2/image0018.jpg' | relative_url }})

Assigning Coil End Surface BCC.

### Defining Coil properties

Select "**Heating** " tab in object “Properties” page, select **Dual** radio button from **Current****frequency** type. Select “**Combined** ” radio button as **Dual** frequency type and define **frequency** information as, **f1=1000, f2=10000, w1=1 and w2=0.1** under **Dual****frequency** as shown in Fig. 3DINDL2.19. Select Volume charge type as Current **density** and define constant value **65** under “**Data Definition** ” tab as shown in Fig. 3DINDL2.19. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Step page.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab2/image0019.jpg' | relative_url }})

Defining Coil properties

## Defining step controls

In Step controls page, define **Number of Simulation steps** as **40** and **Step Increment to save** as **1**. Select **Time as Solution step definition type** and define constant **0.1** sec/step as step definition as shown in Fig. 3DINDL2.20. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button to navigate to Generate database page.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab2/image0020.jpg' | relative_url }})

Defining step controls for simulation.

## Generate Database

In Generate database page, click the ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) button to have the program check to see if anything was missed in the problem setup. During the checking process, messages in the red color signify data that needs to be fixed before a simulation can be run (such as when you forget to define any material data).  
  
Click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database.

## Running Simulation

Once the database has been generated, switch to the Simulation mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the operation tree. Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. 3DINDL2.21 Use the default **Continue Run** option to select “**Continue from the last step** ” (from step -1) option and then select the Simulation mode as **Interactive.** Click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab2/image0021.jpg' | relative_url }})

Run Simulation window.

  
The progress of the simulation can be monitored as it is running by looking at the Simulation Message tab and Simulation Graphics from the Graphics display region in Simulation mode. if the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked in Simulation Message tab, which is the default setting, the Message file will refresh automatically.  
  
The Message file provides information about which simulation step the simulation is currently on and information dealing with how well the simulation is running.

## Post-Processing

When the simulation is completed, review the results by switching to Post mode using the ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) button above the Simulation tool bar.

In Step Browser, click on **All** button and plot Temperature state variable, observe the temperature distribution at last step which should look like as shown in Fig. 3DINDL2.22.

  
![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab2/image0022.jpg' | relative_url }})

Temperature distribution at the last step

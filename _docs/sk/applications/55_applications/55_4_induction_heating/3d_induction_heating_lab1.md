---
lang: sk
title: "3D Induction Heating Lab1"
---

# Lab 1: Single Frequency type Induction Heating

1.1. Creating New Project

1.2. Adding 3D Forming operation

1.3. Simulation Controls settings

1.4. Load materials into Material list

1.5. Adding Objects

1.6. Defining Workpiece

1.7. Defining Coil

1.8. Defining Air object

1.9. Defining Inter-object relations

1.10. Defining Step controls

1.11. Generate Data Base

1.12. Running Simulation

1.13. Post-Processing

## Creating New Project

On a Windows machine, go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** v1x.x from the menu. The DEFORM GUI Main window will appear.

![]({{ '/assets/images/applications/55_2_arc_welding/image0002.jpg' | relative_url }})

Creating New Project.

Create a new problem either by selecting **File**![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) icon. The Problem Setup window will appear. Select "Integrated Manufacturing Process" radio button and unit system as "**SI** " radio button in unit field as shown in Fig. 3DINDL1.1. Define Problem name as “**3D_Induction_Heating****** " and make sure the “Show option dialog” check box is turned on (if we do not turn on the “**Show option dialog** ” check box, then we will not get the New Project dialog in MO UI). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Deform Integrated Manufacturing Process.  
  
Multiple operation wizard will open with the New Project dialog, at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session we will use “**3D_Induction_Heating** " as the project name. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation. MO wizard will open (see Fig. 3DINDL1.2.).

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab1/image0002.jpg' | relative_url }})

New Project settings from Integrated Manufacturing Process template.

## Adding 3D Forming operation

Multiple Operation wizard will open, induction heating simulation will be set using Forming operation hence, add one **3D Forming operation** from Explorer ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Operations list by clicking ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button as shown in Fig. 3DINDL1.3.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab1/image0003.jpg' | relative_url }})

Adding 3D Forming operation into Operation Editor.

## Simulation Controls settings

As we add 3D forming operation, Simulation controls page will be opened. In Simulation controls page, uncheck the Deformation check box. We have Resistance, Induction and Induction (BEM) types of Heating options, we will be using Induction type heating, hence check the **Heating** check box and select **Induction**(See Fig. 3DINDL1.4.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Material list page.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab1/image0004.jpg' | relative_url }})

Simulation control settings for Induction Heating.

## Loading materials into Material list

In Material list page, load the material from file **AL-1100,COLD[70F(20C)]**.key available under /3D/LABS/Induction_Heating/Induction_Heating_Ex1. Simillarly, load the material from file **coil.key** and **AIR.Key** file. This can be done as shown in Fig. 3DINDL1.5. by clicking ![]({{ '/assets/icons/pre_icons/mo_open_button.jpg' | relative_url }}) button. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Objects page.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab1/image0005.jpg' | relative_url }})

Loading required materials into Material list page.

## Adding Objects

For this lab we need 3 objects, by default 3 objects will be added in list when we add 3D Forming operation. If not added by default, then add 3 objects to objects list using ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) button. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Workpiece object page (See Fig. 3DINDL1.6.).

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab1/image0006.jpg' | relative_url }})

Adding required objects for Induction heating. 

## Defining Workpiece

### Workpiece object definition

We will keep object name as “Workpiece”, object Temperature as 20°C and object type as “**Plastic** ” as shown in Fig. 3DINDL1.7. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Geometry page. 

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab1/image0007.jpg' | relative_url }})

Workpiece object definition. 

### Workpiece Geometry

In Geometry page, click on “![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }})link and create **cylinder** geometry with **Diameter(2R) 200** and **Height (H) 150** as shown in the Fig. 3DINDL1.8. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button to close Geometry Primitive page. 

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab1/image0008.jpg' | relative_url }})

Defining Workpiece Geometry. 

  
**Defining Brick Mesh settings:**

We will be generating brick mesh for Workpiece. To generate the brick mesh, click on the ![]({{ '/assets/icons/pre_icons/mo_setup_brick_mesh_label.jpg' | relative_url }}) link in the geometry page. Select the "**Extrude** " radio button. To define the start surface and end surface to extrude during mesh generation, select the icon "Selection mode" ( ![]({{ '/assets/icons/pre_icons/mo_select_icon.jpg' | relative_url }}) ) in the tool bar, select the Start surface, then pick up a top surface of the Workpiece, and click the button ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) in the “Setup brick mesh” window to accept the definition (See Fig. 3DINDL1.9.). Similarly, define the bottom surface of the Workpiece as End surface. Click the ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button to exit the brick mesh geometry setup. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Mesh page. 

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab1/image0009.jpg' | relative_url }})

Brick mesh settings in geometry page. 

### Generating Workpiece mesh

Switch to expert mode using ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) to define brick mesh settings. From General tab of Mesh page, select the "**Brick Mesh** " radio button and "**Uniform thickness** " radio button to generate uniform layers of mesh, set the "**# of layers** " as **20****** Fig. 3DINDL1.10. In the "**2D Cross Section** " tab, set the **Target number of elements** as **500** , **Thickness****elements** as **4** and the **Size** **ratio** as **1** and then click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button as shown Fig. 3DINDL1.11. Click ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}) for Default Boundary conditions popup to assign default BCC. Once mesh is generated, click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to assign material.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab1/image0010.jpg' | relative_url }})

Brick mesh settings for Workpiece. 

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab1/image0011.jpg' | relative_url }})

2D Cross Section mesh settings for Workpiece. 

### Assigning Material to Workpiece

Click on the **AL-1100 COLD[70F(20C)]** in the material window to assign the material to the Workpiece as shown in Fig. 3DINDL1.12. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top die object page.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab1/image0012.jpg' | relative_url }})

Assigning Material to Workpiece. 

## Defining Coil

### Coil object definition

In Top Die page, change the Object name to Coil. Using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) option, import **Coil_Object.key** from \3D\LABS\Induction_Heating\Induction_Heating_Ex1 folder. The imported COIL.key is having COIL geometry along with mesh data as shown in Fig. 3DINDL1.13. Since, we don’t need to generate geometry and mesh, we will navigate using ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Material page. 

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab1/image0013.jpg' | relative_url }})

Defining Coil object.

### Assigning material to Coil

Click on the **coil** in the material window to assign the material to the Coil as shown in Fig. 3DINDL1.14. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Boundary conditions page.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab1/image0014.jpg' | relative_url }})

Assigning material to Coil.

### Defining Coil BCC

Under Induction from BCC tree, select Coil Begin surface option and select Coil begin surface and assign using ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) as shown Fig. 3DINDL1.15.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab1/image0015.jpg' | relative_url }})

Defining Coil Begin Surface BCC.

Similarly, select Coil End Surface option under Induction BCC and select Coil end surface and assign using ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) as shown in Fig. 3DINDL1.16. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Properties page.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab1/image0016.jpg' | relative_url }})

Defining Coil End Surface BCC.

### Defining Coil properties

In **Property** page under **Heating** tab, select Current frequency type as **Single** , define the current frequency as **2000****Hz** and the Current **density** as **65** A/mm2 constant as shown in Fig. 3DINDL1.17. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Bottom Die page.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab1/image0017.jpg' | relative_url }})

Defining Coil Properties

## Defining Air object

### Air object definition

Change the Object name to “**Air** ”, Object Temperature as **20** °C and Object type “**Rigid** ” as shown in Fig. 3DINDL1.18. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Geometry page.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab1/image0018.jpg' | relative_url }})

Air object definition. 

### Defining Air Geometry

Import the **Air.geo** file from /3D/LABS/Induction_Heating/Induction_Heating_Ex1 folder. The air geometry will be displayed as shown in Fig. 3DINDL1.19.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab1/image0019.jpg' | relative_url }})

Imported Air Geometry.

###  Setup Brick Mesh in geometry page

We will be generating brick mesh for Workpiece. To generate the brick mesh, click on the ![]({{ '/assets/icons/pre_icons/mo_setup_brick_mesh_label.jpg' | relative_url }}) link in the geometry page. We will revolve the 2D cross-section mesh, hence select the "**Revolve** " radio button and “**Full****Revolve** ” to generate full cylinder as shown in Fig. 3DINDL1.20. Click the ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button to exit the brick mesh geometry setup. 

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab1/image0027.jpg' | relative_url }})

Brick mesh settings for Air object in geometry page

### Generating mesh for Air object

Switch to expert mode using ![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }}) to define brick mesh settings. From General tab of Mesh page, select the "**Brick****Mesh** " radio button and "**Uniform****thickness** " radio button, set the "**# of layers** " as **120.** In the "**2D Cross Section** " tab, set the **Target number of elements** as **200** , **Thickness elements** as **4** and the **Size****ratio** as **1**.as shown in Fig. 3DINDL1.21. Click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button and click ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}) in Default Boundary conditions popup to assign default BCC as shown in Fig. 3DINDL1.22. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to assign material.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab1/image0020.jpg' | relative_url }})

Mesh settings for Air object.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab1/image0021.jpg' | relative_url }})

Default Boundary conditions pop-up.

### Assigning Material to Air object

Click on the **AIR** in the material window to assign the material to the Air object as shown in Fig. 3DINDL1.23. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Contact page.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab1/image0022.jpg' | relative_url }})

Assigning material to Air object.

## Defining inter-object relations

The next step will be to generate contact between the various objects, make sure the Air is master to both the Workpiece and the Coil. So, click on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button 2 times to add two relations. In first relation, select **Air** as Master and **Coil** as Slave and in second relation, select **Air** as Master and **Workpiece** as Slave. Click on ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) to auto estimate the tolerance and click on ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) to generate contact for all the relationships, generated contacts between objects are as shown in Fig. 3DINDL1.24. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Step controls page.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab1/image0023.jpg' | relative_url }})

Inter-object relations settings and generated contacts. 

## Defining Step controls 

In Step controls page, define **Number of Simulation steps** as **50** and **Step Increment to save** as **2**. select **Time as Solution step definition** type and define constant **1** sec/step as step definition as shown in Fig. 3DINDL1.25. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button to Generate Database page.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab1/image0024.jpg' | relative_url }})

Defining Step controls for induction heating simulation.

## Generate Database

In Generate DB page, click the ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) button to have the program check to see if anything was missed in the problem setup. During the checking process:  
Messages in the red color signify data that needs to be fixed before a simulation can be run (such as when you forget to define any material data).  
  
Click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database.

## Running Simulation

Once the database has been generated, switch to the Simulation mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the operation tree. Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. 3DINDL1.26. Use the default **Continue Run** option to select “**Continue from the last step** ” (from step -1) option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab1/image0025.jpg' | relative_url }})

Run Simulation settings.

  
The progress of the simulation can be monitored as it is running by looking at the Simulation Message tab and Simulation Graphics from the Graphics display region in Simulation mode. if the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked in Simulation Message tab, which is the default setting, the Message file will refresh automatically.  
  
The Message file provides information about which simulation step the simulation is currently on and information dealing with how well the simulation is running

## Post-Processing

When the simulation is completed, review the results by switching to Post mode using the ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) button above the Simulation tool bar.

In Step Browser, click on All button and plot Temperature state variable, observe the temperature distribution as shown in Fig. 3DINDL1.27.

![]({{ '/assets/images/applications/55_induction_heating/3d_induction_heating_lab1/image0026.jpg' | relative_url }})

Temperature distribution at the last step

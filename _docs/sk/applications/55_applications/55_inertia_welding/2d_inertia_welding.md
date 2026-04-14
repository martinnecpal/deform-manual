---
lang: sk
title: "2D Inertia Welding"
---

# Setting up Inertia Welding simulation in DEFORM

DEFORM ® 2D includes special features to simulate uniform rotation and distortion about the Z axis. The torsional distortion mode uses a different element formulation, which considers out-of-plane shear strains (r,q and z,q) as well as the 3 normal + rz shear strains that are considered in a normal axisymmetric problem.

This lab demonstrates setting up inertia welding simulation in DEFORM® 2D.

1.1. Creating New Problem

1.2. Adding Forming operation

1.3. Defining Simulation Controls

1.4. Loading Material into Material list

1.5. Adding Object for inertia welding

1.6. Defining Punch

1.7. Defining BILLET 2

1.8. Defining BILLET 1

1.9. Defining DIE object

1.10. Positioning objects

1.11. Contact generation

1.12. Defining Step Controls and expert Simulation controls

1.13. Generate Database

1.14. Running Simulation

## Creating New Problem

On a Windows machine, go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** v1x.x from the menu. The DEFORM GUI Main window will appear

![]({{ '/assets/images/applications/55_2_arc_welding/image0002.jpg' | relative_url }})

New Problem dialog.

  
Create a new problem either by selecting **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. New Problem window will appear. Select "**Integrated Manufacturing Process** " radio button and unit system as "**SI** " in unit field as shown in Fig. 2DINWL1.1. Define Problem Name as "**Inertia_Welding** " and make sure the “Show option dialog” check box is turned on (if we do not turn on the “**Show option dialog** ” check box, then we will not get the New Project dialog in MO UI). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Deform Integrated Manufacturing Process.  
  
Multiple operation wizard will open with the New Project dialog, at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session, we will use "**Inertia_Welding** " as the project name (see Fig. 2DINWL1.2.). Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

![]({{ '/assets/images/applications/55_inertia_welding/2d_inertia_welding/image0002.jpg' | relative_url }})

MO Wizard New Project Window.

## Adding Forming operation

Add one 2D Forming operation from Explorer Operations list by clicking ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button as shown in Fig. 2DINWL1.3. As we add 2D forming operation, Geometry type page will be opened. select geometry type as **2D****Torsion** as shown in Fig. 2DINWL1.3. and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Simulation controls page.

![]({{ '/assets/images/applications/55_inertia_welding/2d_inertia_welding/image0003.jpg' | relative_url }})

Added 2D Forming operation and Geometry type selection.

## Defining Simulation Controls

In this lab, we will be using both **Deformation** and **Heat****transfer** hence turn on respective check boxes under Sim Mode in Simulation controls page as shown in Fig. 2DINWL1.4. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Material list page. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Objects page.

![]({{ '/assets/images/applications/55_inertia_welding/2d_inertia_welding/image0004.jpg' | relative_url }})

Simulation control settings.

## Loading Material into Material list

In Material list page, load the material **AISI-4340 [1550-2200F(850-1200C)]** from library under **Steel** category using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load form library) button. This can be done as shown in below by clicking ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}) button as shown in Fig. 2DINWL1.5.

![]({{ '/assets/images/applications/55_inertia_welding/2d_inertia_welding/image0005.jpg' | relative_url }})

Loading material into Material list page.

## Adding Objects for inertia welding

We require four objects to setup inertia welding process, there should be three objects added by default for 2D Forming operation, add the fourth object by clicking the ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) button. After adding fourth object, the object page should look like as shown in Fig. 2DINWL1.6. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Workpiece object page.

![]({{ '/assets/images/applications/55_inertia_welding/2d_inertia_welding/image0006.jpg' | relative_url }})

Object Window showing objects for inertia welding.

## Defining Punch

### Punch general object definition

In Workpiece Object page, change the object name to **Punch** and object type as Rigid and temperature as **20** °C (see Fig. 2DINWL1.7.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Geometry page.

![]({{ '/assets/images/applications/55_inertia_welding/2d_inertia_welding/image0007.jpg' | relative_url }})

Punch general object definition. 

### Defining Punch Geometry

In Geometry page, click on**![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }})** , select **Cylinder** from primitives and define **Radius** as **35.1** , **Height** as **50** as shown in Fig. 2DINWL1.8. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button to accept all the changes and go back to the Geometry definition. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top Die object page.

![]({{ '/assets/images/applications/55_inertia_welding/2d_inertia_welding/image0008.jpg' | relative_url }})

Defining Punch geometry 

## Defining BILLET 2 

### BILLET 2 general object definition

Change the object name from Top Die to **BILLET 2**. Keep temperature as **20** °C and select the object type as **Plastic** as shown in Fig. 2DINWL1.9. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Geometry page.

![]({{ '/assets/images/applications/55_inertia_welding/2d_inertia_welding/image0009.jpg' | relative_url }})

BILLET 2 general object definition.

### Import the geometry for BILLET 2

Click the ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Load geometry from a file) button and import the file "**BILLET2.geo** ” geometry file from /2D/LABS/Inertia_Welding. The imported geometry looks like as shown in Fig. 2DINWL1.10. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Mesh page.

![]({{ '/assets/images/applications/55_inertia_welding/2d_inertia_welding/image0010.jpg' | relative_url }})

Imported BILLET 2 geometry.

### Generating mesh for BILLET 2

We will generate mesh with mesh windows. To generate mesh with mesh windows we need to be in expert mode, click on ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) icon to switch to expert mode. In Mesh page General tab, define Target number of elements as 2000, Thickness elements as 5 and size ratio as 5 (See Fig. 2DINWL1.11.).  
  
Under Weighting Factors tab change the Mesh window weighting factor value to approximately 0.8 and Temperature weighing factor as 0.2, see in Fig. 2DINWL1.12.

Now, select Mesh window tab and add three mesh windows to define mesh transition as shown in Fig. 2DINWL1.13., fine mesh at welding region to capture the deformation and temperature and coarse mesh where we do not have much deformation. 

\- Define Window 1 to cover bottom surface of the BILLET 2 with relative element size 0.033. Define 0.5mm/sec as velocity for Window1.

\- Define Window 2 to cover region above Window1 of the BILLET 2 as shown in Fig. 2DINWL1.13. with relative element size 0.1.

\- Define Window 3 to cover remaining of the BILLET 2 surface with relative element size 1 

Click on Remeshing criteria tab and define Maximum step increment as 50 as shown in Fig. 2DINWL1.14. so that simulation stops for remeshing after every 50 steps. Click on Advanced setting tab and Define 50 value in X and Y division fields as shown in Fig. 2DINWL1.15. Click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button to generate the mesh for BILLET 2. The mesh should look like as shown in Fig. 2DINWL1.15. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Material page. 

![]({{ '/assets/images/applications/55_inertia_welding/2d_inertia_welding/image0011.jpg' | relative_url }})

General mesh settings for BILLET 2.

![]({{ '/assets/images/applications/55_inertia_welding/2d_inertia_welding/image0012.jpg' | relative_url }})

Weighing factors settings for BILLET 2.

![]({{ '/assets/images/applications/55_inertia_welding/2d_inertia_welding/image0013.jpg' | relative_url }})

General mesh settings for BILLET 2.

![]({{ '/assets/images/applications/55_inertia_welding/2d_inertia_welding/image0014.jpg' | relative_url }})

Remeshing criteria settings for BILLET 2.

![]({{ '/assets/images/applications/55_inertia_welding/2d_inertia_welding/image0015.jpg' | relative_url }})

Advanced settings of mesh for BILLET 2 and generated mesh.

### Assigning Material to BILLET 2

Click on the **AISI-4340 [1550-2200F(850-1200C)]** in the material window to assign the material to BILLET 2 as shown in Fig. 2DINWL1.16. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button until Bottom Die object page.

![]({{ '/assets/images/applications/55_inertia_welding/2d_inertia_welding/image0016.jpg' | relative_url }})

Assigning Material to BILLET 2.

## Defining BILLET 1

### BILLET 1 general object definition

Change the object name from Bottom Die to **BILLET****1**. Keep object temperature as **20** °C and select the object type as **Plastic** as shown in Fig. 2DINWL1.17. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button to Geometry page.

![]({{ '/assets/images/applications/55_inertia_welding/2d_inertia_welding/image0017.jpg' | relative_url }})

BILLET 1 general object definition.

### Importing the BILLET 1 geometry

In Geometry page, click on ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Load geometry from a file) button and import the file "**BILLET1.geo** ” geometry file from /2D/LABS/Inertia_Welding. The imported geometry looks like as shown in Fig. 2DINWL1.18. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Mesh page.

![]({{ '/assets/images/applications/55_inertia_welding/2d_inertia_welding/image0018.jpg' | relative_url }})

Imported BILLET 1 geometry.

### Generating mesh for BILLET 1

We will generate mesh with mesh windows. In Mesh page General tab, define Target number of elements as 2000, Thickness elements as 5 and size ratio as 5 (See Fig. 2DINWL1.19.).

Under Weighting Factors tab change the Mesh window weighting factor value to approximately 0.8 and Temperature weighing factor as 0.2, see in Fig. 2DINWL1.20.

Now, select Mesh window tab and add three mesh windows to define mesh transition as shown in Fig. 2DINWL1.21, fine mesh at welding region to capture the deformation and temperature and coarse mesh where we do not have much deformation. 

\- Define Window 1 to cover top surface of the BILLET 1 with relative element size 0.033. Define 0.5mm/sec as velocity for Window1.

\- Define Window 2 to cover region below Window1 of the BILLET 1 as shown in Fig. 2DINWL1.21 with relative element size 0.1.

\- Define Window 3 to cover remaining of the BILLET 1 surface with relative element size 1.

Click on Remeshing criteria tab and define Maximum step increment as 75 as shown in Fig. 2DINWL1.22 so that simulation stops for remeshing after every 75 steps. Click on Advanced setting tab and Define 50 value in X and Y division fields as shown in Fig. 2DINWL1.23. Click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button to generate the mesh for BILLET 1. The mesh should look like as shown in Fig. 2DINWL1.23. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Material page.

![]({{ '/assets/images/applications/55_inertia_welding/2d_inertia_welding/image0019.jpg' | relative_url }})

General mesh settings for BILLET 1.

![]({{ '/assets/images/applications/55_inertia_welding/2d_inertia_welding/image0020.jpg' | relative_url }})

Weighing factors settings for BILLET 1.

![]({{ '/assets/images/applications/55_inertia_welding/2d_inertia_welding/image0021.jpg' | relative_url }})

Mesh Window settings for BILLET 1.

![]({{ '/assets/images/applications/55_inertia_welding/2d_inertia_welding/image0022.jpg' | relative_url }})

Remeshing criteria settings for BILLET 1.

![]({{ '/assets/images/applications/55_inertia_welding/2d_inertia_welding/image0023.jpg' | relative_url }})

Advanced settings of mesh for BILLET 1 and generated mesh.

### Assign Material to BILLET 1

Click on the **AISI-4340 [1550-2200F(850-1200C)]** in the material window to assign the material to BILLET 1 as shown in Fig. 2DINWL1.24. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button until Object 4 object page.

![]({{ '/assets/images/applications/55_inertia_welding/2d_inertia_welding/image0024.jpg' | relative_url }})

Assigning Material to BILLET 1.

## Defining DIE object

### DIE general object definition

Change the object name from Object 4 to **DIE**. Keep object temperature as **20** °C and select the object type as **Rigid** as shown in Fig. 2DINWL1.25. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Geometry page.

![]({{ '/assets/images/applications/55_inertia_welding/2d_inertia_welding/image0025.jpg' | relative_url }})

DIE general object definition. 

### Defining DIE Geometry

In Geometry page, click on ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) and select **Cylinder** from primitives. Define cylinder **Radius** as **32.6** , **Height** as **50** as shown in Fig. 2DINWL1.26. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button to accept all the changes, and go back to the Geometry definition, click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Movement page.

![]({{ '/assets/images/applications/55_inertia_welding/2d_inertia_welding/image0026.jpg' | relative_url }})

Defining geometry for DIE.

### Assigning Movement for DIE

Force will be applied on to the BILLET 1 through DIE. Hence, select Force as movement type and direction as +Y. We will define force as Function of Time, select Function of Time radio button and click on ![]({{ '/assets/icons/pre_icons/mo_define_function.._button.jpg' | relative_url }}) button as shown in Fig. 2DINWL1.27. Define force as shown in Fig. 2DINWL1.28. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to close the table definition page and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Positioning page.

![]({{ '/assets/images/applications/55_inertia_welding/2d_inertia_welding/image0027.jpg' | relative_url }})

Defining force movement for DIE.

**Time** |  **Force**  
---|---  
0 |  0  
0.2 |  171000  
2 |  171000  
2.5 |  556600  
80 |  556600  
80.5 |  1164600  
86 |  1164600  
86.5 | 0  
  
![]({{ '/assets/images/applications/55_inertia_welding/2d_inertia_welding/image0028.jpg' | relative_url }})

Force movement as function of time for DIE

## Positioning objects

In Positioning page, click on ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) label to open Object Positioning window. In Object Positioning window, select Interference option ![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}), select Positioning object as Punch and Reference object as BILLET 2, select Approach direction as -Y direction and click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) to position Punch above BILLET 2 as shown in Fig. 2DINWL1.29. Similarly, position the DIE (Positioning Object) over the BILLET 1 (Reference Object) using interference with an approach direction as +Y. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to accept object positioning and comeback to Positioning page. Objects after positioning looks like as shown in Fig. 2DINWL1.29. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Contact page.

![]({{ '/assets/images/applications/55_inertia_welding/2d_inertia_welding/image0029.jpg' | relative_url }})

Positioning of the objects: Positioning window

## Contact Generation

In Contact page, select **User** as contact type definition and using ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button add relations as shown in Fig. 2DINWL1.30.

![]({{ '/assets/images/applications/55_inertia_welding/2d_inertia_welding/image0030.jpg' | relative_url }})

Contact relations between objects.

Select PUNCH – BILLET 2 relationship and click the ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) button to modify the relationship. In the friction tab, define constant shear friction value 1 as shown in Fig. 2DINWL1.31. Similarly, define constant shear friction of 1 for DIE – BILLET 1 relation.

![]({{ '/assets/images/applications/55_inertia_welding/2d_inertia_welding/image0031.jpg' | relative_url }})

Inter-Object data definition window.

  
Select **BILLET 1– BILLET 2** relationship and click the ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) button to modify the relationship. Define constant shear friction of 0.9 in Friction tab and HTC as 10 in Thermal tab. Use ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) icon to determine a suitable contact tolerance then click on ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) button to generate contact. Generated contacts look like as shown in Fig. 2DINWL1.32. Switch to Message tab or Observe status bar to know about the contacts generated. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Step controls page.

![]({{ '/assets/images/applications/55_inertia_welding/2d_inertia_welding/image0032.jpg' | relative_url }})

Contact generated between objects.

## Defining Step Controls and expert Simulation controls

In Step controls page we have access to expert mode simulation controls as we are in expert mode. Select ![]({{ '/assets/icons/pre_icons/mo_simulation_step.jpg' | relative_url }}), define **Number****of****Simulation****steps** as **2500** and **Step****Increment****to** **save** as **10** as shown in Fig. 2DINWL1.33. and select **DIE** as Primary die.

![]({{ '/assets/images/applications/55_inertia_welding/2d_inertia_welding/image0033.jpg' | relative_url }})

Defining step controls.

  
Select ![]({{ '/assets/icons/pre_icons/mo_step_increment.jpg' | relative_url }}), select **Time** as Solution step definition type and define constant time step as **0.02** Sec/step as shown in Fig. 2DINWL1.34.

![]({{ '/assets/images/applications/55_inertia_welding/2d_inertia_welding/image0034.jpg' | relative_url }})

Defining Solution step definition.

  
Select ![]({{ '/assets/icons/pre_icons/mo_solver_settings.jpg' | relative_url }}), in **Deformation** tab select "**Newton-Raphson** " as Iteration method and Solver as "**Skyline** ". Select **Advanced** tab and Define **350** value in **p****er deformation time step** as shown in the Fig. 2DINWL1.35.

![]({{ '/assets/images/applications/55_inertia_welding/2d_inertia_welding/image0035.jpg' | relative_url }})

Defining Solver settings.

## Generate Database

In Generate Database page, click on ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) button to have the program check to see if anything was missed in the problem setup. During the checking process,  
messages in the red color signify data that needs to be fixed before a simulation can be run (such as when you forget to define any material data).  
  
Click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database.

## Running Simulation

Once the database has been generated, switch to the Simulation mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the operation tree. Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. 2DINWL1.36. Use the default **Continue Run** option to select “**Continue from the last step** ” (from step -1) option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

  
![]({{ '/assets/images/applications/55_inertia_welding/2d_inertia_welding/image0036.jpg' | relative_url }})

Run Simulation window.

  
The progress of the simulation can be monitored as it is running by looking at the Simulation Message tab and Simulation Graphics from the Graphics display region in Simulation mode. If ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked in Simulation Message tab, which is the default setting, the Message file will refresh automatically.  
  
The Message file provides information about which simulation step the simulation is currently on and information dealing with how well the simulation is running.

---
lang: en
title: "Lab02 Square Ring"
---

# Lab2 Square Ring

  
2.1. Introduction

2.2. Creating a New Problem

2.3. Adding Operation

2.4. Adding Objects

2.5. Workpiece

2.6. Top Die

2.7. Inter-Object relationships

2.8. Step Controls

2.9. Database Generation

2.10. Running Simulation

2.11. Post Processing

## Introduction

Symmetry should be taken advantage of whenever possible in simulations. Doing so saves computational time and can increase solution accuracy. Furthermore, the smallest possible section that adequately describes the problem should be modeled.

In this lab, we will simulate the upsetting of a square ring. The square ring has quite a bit of symmetry that can be taken advantage of. This lab will show you that the deformation of the entire ring can be determined by only modeling 1/16 of its full geometry.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0001.jpg' | relative_url }})

Sectioning of Square ring modeled for analysis

## Creating a New Problem

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear as shown below Fig. 3DL2.2.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0001.jpg' | relative_url }})

DEFORM GUI main window

Create a new problem either by selecting **File** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in Fig. 3DL2.3. Select "**Integrated Manufacturing Process** " radio button and unit system as "**English** " radio button in unit field. Define Problem Name as " ******Square_Ring** " and make sure the “**Show option dialog** ” check box is turned on (if we do not turn on the “Show option dialog” check box, then we will not get the New Project dialog). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

Problem type selection window

Multiple operation wizard will open with the New Project dialog (see Fig. 3DL2.4.), at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session we use ‘**Square_Ring** ’ as the project name.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0004.jpg' | relative_url }})

New Project selection window

User can also change the Unit system (File menu selected unit system will be selected by default) and add operation by selecting from First operation pull down list and checkbox (see Fig. 3DL2.5.). Using copy Existing project option we can import previous saved projects as new project. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0005.jpg' | relative_url }})

Assigning problem name

To simulate the forging of this square ring, only a workpiece and a top die are required - the bottom die is not needed due to symmetry.

## Adding Operation

Add 3D Forming operation from the Explorer Operations list. Add the operation by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button available next to 3D Forming or user can also add by drag and drop into the Operation editor. (See Fig. 3DL2.6.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0006.jpg' | relative_url }})

Operation Explorer

In this operation we are setting up simple Isothermal operation so, in Simulation control page Sim Mode tab, **turn****off** the **Heat****transfer****mode** check box. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) .

In Material list window, load the '**AISI-1045, COLD** ' material from DEFORM Material library, **Steel** category using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load material data from library) option. This can be done as shown in below Fig. 3DL2.7. by clicking ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}) button. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0007.jpg' | relative_url }})

Material library window

## Adding Objects

If there aren't already two objects, add the two objects by clicking the insert object ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) button. The two objects will be named as Workpiece and Top Die. If there are three objects, delete the Bottom Die by selecting it and clicking the Delete selected ![]({{ '/assets/icons/pre_icons/mo_delete_object_button.jpg' | relative_url }}) object button (see Fig. 3DL2.8.), then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0008.jpg' | relative_url }})

Object Window

## Workpiece

In Workpiece window, change the Object name to **Billet** and select Object type as **Plastic** and temperature as**68°F** as shown in Fig. 3DL2.9. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0009.jpg' | relative_url }})

Billet object Window

### Loading Billet Geometry

In Geometry window, load **SquareRing_Billet.STL** geometry file from library using (Load geometry from library) option or can also be imported using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load geometry from a file ) option as shown in Fig. 3DL2.10. The geometry is located in DEFORM installation folder \3d\LABS directory. Check the geometry using the ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) and ![]({{ '/assets/icons/pre_icons/mo_show_geometry_normal_vectors_option.jpg' | relative_url }}) options.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0010.jpg' | relative_url }})

Billet Geometry window

Symmetry is being taken advantage of in this simulation and only 1/16 of the square ring is being modeled. Using Planar symmetry option define the symmetry planes to enforce the correct deformation (see Fig. 3DL2.11.). Click on ![]({{ '/assets/icons/pre_icons/mo_symmetry_planes_label.jpg' | relative_url }}), under **Planar Symmetry** select the symmetry plane that is normal to the X-axis (as shown below Fig. 3DL2.12.). The selected plane polygon face on the Plane will get highlighted and the Plane Information will be listed in the Plane area.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0013.jpg' | relative_url }})

Symmetry Plane

Click the ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button to add symmetry boundary conditions. This symmetry plane will now be listed in the Planar symmetry list as (1, 0, 0) which is the normal to the X plane. (See Fig. 3DL2.12.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0028.jpg' | relative_url }})

Assigned Planar symmetry on X Plane

Repeat the above procedure to add the Planar symmetry for the other two symmetry planes. First select the symmetry plane, so that the selected plane get highlighted and then use the ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button to add them. When all three symmetry planes have been added, the planar symmetry area should look like as shown in Fig. 3DL2.13. then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) in Planar symmetry page and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to generate mesh.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0029.jpg' | relative_url }})

Assigned Planar Symmetry data for geometry

### Meshing the Billet

In Mesh window, change the**Target number of elements** to **8000** and click on ![]({{ '/assets/icons/pre_icons/mo_preview_mesh_button2.jpg' | relative_url }}) button. The surface mesh that is created looks good. So click the ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button to finish the meshing process. (See Fig. 3DL2.14.) When meshing is completed, the object should have around 5000 elements. When you are asked "Do you want to assign default boundary conditions?" click ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to material page.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0011.jpg' | relative_url }})

Billet Mesh window

### Assigning Material to the Billet

To assign material for workpiece select the material **AISI-1045 COLD** from material window. This can be done as shown in below Fig. 3DL2.15. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Boundary condition page .

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0012.jpg' | relative_url }})

Billet Material window

### Setting symmetry boundary conditions

In Boundary condition page observe the assigned Symmetry plane data, the Boundary Condition area should look like as shown in Fig. 3DL2.16.

Since it is isothermal setup, delete the default assigned Heat exchange with environment BCC. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until top die object window.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0014.jpg' | relative_url }})

Symmetry boundary conditions

## Top die

In Top die object window, keep the object type as **rigid** and temperature as 68°F, also make sure the primary die check box is checked and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). (See Fig. 3DL2.17.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0016.jpg' | relative_url }})

Top die object window

### Loading Top die Geometry

In Geometry window, load **SquareRing_TopDie.STL** geometry file from library using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load geometry from library) option. The geometry is located in DEFORM installation folder \3d\LABS directory. Check the geometry using the ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) and ![]({{ '/assets/icons/pre_icons/mo_show_geometry_normal_vectors_option.jpg' | relative_url }}) options, then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until the Movement window. Since this is an isothermal problem no mesh nor related data need to be specified.

### Assigning Movement to Top die

Define a **speed** of **1** in/sec in **-Z** direction. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until the Contact window appears as both the Billet and top die are in right position. (See Fig. 3DL2.18.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0017.jpg' | relative_url }})

Top Die Movement window

## Inter-Object relationships

Select **user** type radio button and click on ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) button. It will add the relationship between the Billet and the Top Die as shown in Fig. 3DL2.19.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0018.jpg' | relative_url }})

Inter-Object window

Define the friction for the relationship by clicking the ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) button. Use the pull-down menu to select the friction suitable for **Cold forming (steel dies)**. (See Fig. 3DL2.20.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0019.jpg' | relative_url }})

Inter-Object data definition window

Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to go back to Inter-Object window, use ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) icon to determine a suitable contact tolerance (a value of about 0.00192" will be calculated) and then click ![]({{ '/assets/icons/pre_icons/mo_generate_button.jpg' | relative_url }}) button to generate contact. If you rotate the objects around in graphics window, you will see that contact was generated between the two objects. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Step window as no Stopping controls aren't necessary.

## Step Controls

In Step controls window change the preprocessor setup mode to Expert by using the ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) (Switch to expert mode) icon from the tool bar. Expert mode will provide more options for detailed settings. (See Fig. 3DL2.21.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0020.jpg' | relative_url }})

Step controls Main tab in expert mode

Select the steps tab (![]({{ '/assets/icons/pre_icons/mo_simulation_step.jpg' | relative_url }})), set the **Number of Simulation Steps** to **30** and **Step****Increment****to****Save** to **2**. Set the **Top****Die** as **Primary****Die**. (See Fig. 3DL2.22.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0021.jpg' | relative_url }})

Step controls Simulation Steps tab in expert mode

To determine an appropriate step size, select the ![]({{ '/assets/icons/pre_icons/mo_measure_tool_icon.jpg' | relative_url }}) icon and measure the edge length of a few of the smaller elements in the Billet. An average length of a short edge is around 0.06”. Use a **Constant Die Displacement** per step of **0.02** in/step, which is 1/3 of this small edge length in step increment tab (![]({{ '/assets/icons/pre_icons/mo_step_increment.jpg' | relative_url }})) for step size as die displacement. (See Fig. 3DL2.23.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0022.jpg' | relative_url }})

Simulation controls Step increment tab in expert mode

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) and save a keyword file for the problem by selecting the File menu Export option.

## Database Generation 

Click on ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) action label to check the problem. The only warning should deal with Volume Compensation appear in the console window - ignore this for this lab. Generate a database by clicking ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) action label.

## Running Simulation

Once the database has been generated, switch to the Simulation mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the operation tree.

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

Monitor the progress of the simulation by looking at the Simulation graphics window and Simulation Message and Simulation Log tabs, making sure that the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked (See). Simulation graphics tool bar options can be used to plot basic state variables and contact for objects while simulating the problem.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0023.jpg' | relative_url }})

MO Simulation Mode

## Post Processing

When the simulation is complete, review the results by switching to Post mode using the button above the Simulation tool bar. (See Fig. 3DL2.25.)

In reality this part is a full square ring, so it would be useful to be able to view the entire part in the Post-processor. To create the entire object, the small 1/16 section has to be mirrored about the symmetry planes. Clicking the ![]({{ '/assets/icons/post_icons/mo_3d_mirroring_icon.jpg' | relative_url }}) icon open the 3D Mirroring window. (See Fig. 3DL2.26.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0024.jpg' | relative_url }})

MO Post Mode

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0025.jpg' | relative_url }})

3D Mirroring window

Use the mouse to click on the symmetry planes on the Billet. Each time this is done a mirror image of the billet will be displayed. Repeat the process until the entire billet is shown. This procedure is illustrated below. (See Fig. 3DL2.27.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0026.jpg' | relative_url }})

Symmetry definition

Once the complete part is displayed in the Graphics window, close the Symmetry definition window by clicking OK. Play through the steps to observe how the square ring deforms as it is compressed. Experiment with viewing the different state variables such as effective strain. (See Fig. 3DL2.28.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab02_square_ring/image0027.jpg' | relative_url }})

Strain effective result

When finished viewing the results of the simulation, use the ![]({{ '/assets/icons/pre_icons/mo_quit_icon.jpg' | relative_url }}) icon to return to the GUI Main window.

**Related Topics:**

[1\. Simulation Control](/docs/en/pre_processor/9_simulation_controls/9_simulation_controls/)

[2\. General](/docs/en/pre_processor/11_general_object_data_definition/11_general_object_data_definition/)

[3\. Geometry](/docs/en/pre_processor/12_geometry_modelling/12_3_3d_geometry_data_defining/)

[4\. Movement](/docs/en/pre_processor/15_movement_controls_definition/15_movement_controls_settings/)

[5\. Mesh](/docs/en/pre_processor/13_mesh_generation/13_mesh_generation/)

[6\. Positioning](/docs/en/pre_processor/16_object_properties/16_object_properties/)

[7\. Inter-Object](/docs/en/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/)

[8\. Post - Processor](/docs/en/post_processor/24_introduction_to_post_processor/24_introduction_to_post_processor/)

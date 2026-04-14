---
lang: en
title: "Lab04 Steering Link"
---

# Lab 4. Steering Link

  
4.1. Introduction

4.2. Creating New problem

4.3. Adding Operations and Objects

4.4. Defining Workpiece

4.5. Defining Top Die

4.6. Defining Bottom Die

4.7. Positioning Objects

4.8. Assigning Inter-Object Relation

4.9. Assigning Stopping Controls

4.10. Step Controls

4.11. Database Generation

4.12. Post Processing

## Introduction

The German Forging Industry Association (Industrieverband Deutscher Schmieden or IDS) hosts periodic benchmark tests of forging simulation codes. These are actual industrial parts in which all process data are available for distribution.

In this lab and the next lab, the two parts from the 1999 benchmark will be used to illustrate realistic problem setup. Depending on hardware and system settings, these problems will run anywhere from several hours to a day or two. One of the keys to optimizing simulation performance is mesh definition which will be discussed in depth later in the lab.

Accurately simulating a hammer forging process requires an above normal amount of data about the press, and some additional effort to set up and run the simulation.

## Creating New Problem

Create a new problem either by selecting **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****New Problem** or by clicking the **New Problem**![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear. Select "**Integrated Manufacturing Process** " radio button and units system as "**SI** " radio button in units field. Define Problem Name as "**Steering_Link** " and make sure the “**Show option dialog** ” check box is turned on (if we do not turn on the “Show option dialog” check box, then we will not get the New Project dialog). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new problem using the Deform Integrated Manufacturing Process.

MO wizard will open, at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session we use ‘**Steering_Link** ’ as the project name.

User can also change the Unit system and add operation by selecting from First operation pull down list and checkbox. Using copy Existing project option we can import previous saved projects as new project. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

##  Adding operation and Objects

Add 3D Forming operation from the Explorer Operations list. Add the operation by clicking on 3D Forming ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button or user can also add by drag and drop into the Operation Editor. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Objects page. 

In Objects Page, by default 3 objects will be added if not add objects by selecting ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) button, add three objects as shown in Fig. 3DL4.1. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0001.jpg' | relative_url }})

Adding Objects

## Defining Workpiece

### Assigning Workpiece Temperature

In Workpiece page, enter workpiece temperature as **1300** °C as shown in Fig. 3DL4.2. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) .

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0002.jpg' | relative_url }})

Assigning temperature for Workpiece

### Import Geometry

In Geometry page, click on import geometry from library option ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) and import the **ids_link_billet.stl** file from DEFORM installation folder \3d\LABS directory. Use ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) button to check the Geometry. A Geometry checking popup will appear in Display window as shown in Fig. 3DL4.3. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0003.jpg' | relative_url }})

Geometry checking Window

### Defining Workpiece Mesh

The workpiece mesh has the largest influence of all simulation settings on simulation accuracy and speed. A coarse mesh will allow extremely fast simulation speeds, but surface resolution will be poor. More mesh elements will enhance surface resolution, but will do so at the expense of simulation time.

In general, features and defects which are of the same order of size or smaller than the element size will not be captured.

DEFORM® offers two options for [mesh](/docs/en/pre_processor/13_mesh_generation/13_mesh_generation/) description:

**Absolute mesh** allows the user to specify mesh resolution. The total number of mesh elements will be determined by the system, but resolution will remain constant.

**Relative mesh** allows the user to specify a total number of solid elements. The number of solid elements will remain relatively constant, and surface resolution will change as the simulation progresses.

In general, absolute mesh provides better performance, because for a desired resolution, the simulation uses fewer elements at the start, and adds elements as necessary to maintain resolution. Both mesh descriptions offer adaptive automatic mesh refinement – finer elements are used in areas where more resolution is required.

### Mesh Density Definition for Fine Resolution

It is common to base mesh definition on feature sizes in the tooling. In the case of this part, the critical features are the blend radii leading from the shank into the eyes, and the fillets leading into the flash radius. These fillets are around 2mm. To resolve these, the minimum element size should be about ½ of this size, or 1mm.

Change the preprocessor setup mode to Expert by using the ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) (Switch to expert mode) icon from the tool bar. In Mesh page, select absolute mesh radio button, a **Minimum Element Size** of **1** mm and a **Size****Ratio** of**3** should be entered as mesh parameters for the workpiece as shown in Fig. 3DL4.4.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0004.jpg' | relative_url }})

General Mesh Window

The weighting parameters set the relative influence of surface curvature, strain, strain rate and temperature gradient on mesh definition. Higher weights on curvature will give better **boundary** resolution. Change the weighting to about **0.9** for **Surface Curvature** and **0.1** for both **Strain** and **Strain Rate** as shown in Fig. 3DL4.5.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0005.jpg' | relative_url }})

Mesh Weighing Factors window

First generate a ![]({{ '/assets/icons/pre_icons/mo_surface_mesh_button.jpg' | relative_url }}) and then a ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) for the billet. Click ![]({{ '/assets/icons/pre_icons/mo_no_button.jpg' | relative_url }}) for Default Boundary conditions popup. A mesh with about 76,000 solid elements will be generated. At each remesh, the defined absolute mesh settings will be maintained, so the total number of elements will increase as the geometric complexity of the workpiece increases.

### Importing Material Data

In the Material window, Select **steel** category and load the material **DIN41Cr4** using Load material data from library ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) option as shown in Fig. 3DL4.6.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0006.jpg' | relative_url }})

Material Window

After loading the data, click on ![]({{ '/assets/icons/pre_icons/mo_edit_material_button.jpg' | relative_url }}) button, Material window will open. In that window, view the thermal and plastic data by clicking on the ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) button next to each of the properties. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Assigning Boundary Conditions

Only half of the steering link is being modeled. To enforce symmetry, we need to define a **symmetry plane** boundary condition to the **+X** **end** of the part as shown in Fig. 3DL4.7., and heat exchange with the environment boundary condition to all surfaces except the +X end of the part as shown in Fig. 3DL4.8. and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Properties.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0007.jpg' | relative_url }})

Symmetry BCC Definition

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0008.jpg' | relative_url }})

Heat Exchange with Environment BCC definition

### Activating Volume Compensation

In properties page, click on the **Deformation** button and set the **Target****Volume** to **Active in FEM + meshing**. Click the ![]({{ '/assets/icons/pre_icons/mo_target_volume_icon.jpg' | relative_url }}) button to calculate the volume of the workpiece mesh and geometry. In general, the mesh volume will be slightly smaller than the geometry volume. Using the geometry volume as the target volume will cause DEFORM® to gradually grow the workpiece volume back to the target. Using mesh volume at the target volume will cause DEFORM® to maintain a constant volume.

When asked, use the geometry volume as the target volume by clicking ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}) button as shown in Fig. 3DL4.9.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0009.jpg' | relative_url }})

Target volume popup

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top Die page

## Defining Top Die

###  Assign Temperature

In Top Die page, assign temperature for Top Die as **90** °C s shown in Fig. 3DL4.10. then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0010.jpg' | relative_url }})

Assigning Top Die Temperature

### Import Geometry

In Geometry page, click on import geometry from library option ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) and import the **Ids_link_top.stl** file from DEFORM installation folder \3D\LABS directory. Use ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) button to check the Geometry. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until movement page.

### Assign Movement

For a simplified simulation, we will assign a constant top die velocity of **150** mm/s in the **-Z** direction (see Fig. 3DL4.11.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Bottom die page.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0011.jpg' | relative_url }})

Movement Control Window

## Defining Bottom Die

### Assign Temperature

In Bottom Die page, assign temperature for Bottom Die as **90** °C as shown in Fig. 3DL4.12. then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to geometry page.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0012.jpg' | relative_url }})

Assigning Bottom Die Temperature

### Import Geometry

In Geometry page, click on import geometry from library option ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) and import the **ids_link_bottom.stl** file from DEFORM installation folder \3D\LABS directory. Use ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) button to check the Geometry. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Positioning page.

## Positioning Objects

Click on ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) and select ![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}) radio button. Change the Positioning Object to the **Top Die** and the Reference to the **Workpiece**. Change the Approach Direction to **-Z** and then click ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}).

Again select ![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}) radio button. Change the Positioning Object to the **Bottom****Die** and the Reference to the Workpiece. Change the Approach Direction to **Z** and then click ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until contact page.

## Assigning Inter-Object Relations

In Contact window, click on ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) button, default relations get added as shown in Fig. 3DL4.13.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0013.jpg' | relative_url }})

Inter-Object Window with Default Relations

The workpiece should be slave to both dies. Use a friction value of**0.3** (typical for hot forming), and an interface heat transfer coefficient of **5** (typical for SI units when dies are not meshed).Remember to generate contact boundary conditions.

Highlight the first relationship in the table and click ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}). On the **Deformation** tab, use the friction pull-down menu to select **Hot forging (lubricated)** from the list as shown in [Fig. 3DL3.47](lab03_spike_forging.htm#Fig_3DL3_47_Inter-Object_Data_Deformation_definition_Window) then click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}).

Select **Thermal** Tab and enter an **interface****heat****transfer****coefficient** of **5** (typical for SI units when dies are not meshed) as shown in Fig. 3DL4.14. Then click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0014.jpg' | relative_url }})

Thermal Data Definition window

In Contact window, click on ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) to change the other relationship to these settings as shown in Fig. 3DL4.15.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0015.jpg' | relative_url }})

Inter-Object Window

Use ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) to determine a suitable contact tolerance and then click the ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) button to generate contacts. Contact will be generated between the Billet and both the Top and Bottom Dies. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

## Assigning Stopping Controls

Switch to Guided ![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }}) mode, Select ![]({{ '/assets/icons/pre_icons/mo_show_user_defined_obj_icon.jpg' | relative_url }}) icon, a message pop up appears in Display window, uncheck the workpiece check box in the message popup as shown in Fig. 3DL4.16.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0016.jpg' | relative_url }})

User Define Object mode

In Stopping Controls window, Check the Distance between Objects check box. For Object 1, select **Top Die** and click the button ![]({{ '/assets/icons/pre_icons/mo_mouse_icon.jpg' | relative_url }}). Select a point on the bottom of the Top Die. For Object 2, select **Bottom Die** and click the ![]({{ '/assets/icons/pre_icons/mo_mouse_icon.jpg' | relative_url }}) button. Select a point on the top of the Bottom Die. It calculates the distance and displays it in Display window. Specify a **Z****Distance** of **11.0** mm as the stopping criteria as shown in Fig. 3DL4.17. Click![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) .

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0017.jpg' | relative_url }})

Stopping Controls window

## Step Controls

The total stroke will be approximately 40mm. For a complex flash operation, 200 time steps is reasonable. The selection of this number is not critical, because sub-stepping settings will control the actual step size used in deformation calculations. In Step controls window change the preprocessor setup mode to Expert by using the ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) (Switch to expert mode) icon from the tool bar.

In Step controls, select ![]({{ '/assets/icons/pre_icons/mo_simulation_step.jpg' | relative_url }}) and assign **Number of Simulation steps** as **200** and **step****increment****to****save****10** steps. Set the **Top****Die** as the **primary****die**. (See Fig. 3DL4.18.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0018.jpg' | relative_url }})

Steps Window

Select ![]({{ '/assets/icons/pre_icons/mo_step_increment.jpg' | relative_url }}) assign a stroke/step value of **0.2** mm/step as shown in [Fig. 3DL4.19.](lab03_spike_forging.htm#Fig_3DL3_19_Heat_Transfer_type_selection_page)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0019.jpg' | relative_url }})

Step Controls window

## Database Generation

Save a keyword file for the problem by selecting the **File** menu ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **Export** option.

Click on ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) action label to check the problem. Generate a database by clicking ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) action label.

Once the database has been generated switch to the Simulation mode by selecting the ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the object tree. Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

## Post processing

When the simulation is complete, review the results by switching to Post mode using the ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) button above the Simulation tool bar.

Play through the Steps and plot the Temperature, Stress Effective, Damage and Effective Strain State variables. (See Fig. 3DL4.20. and Fig. 3DL4.21.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0020.jpg' | relative_url }})

Damage State Variable plot

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0021.jpg' | relative_url }})

Stress Effective State Variable Plot

Click on the ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) icon. When the GRAPH window appears, select only Top Die and the X-Axis is set to **Stroke** and the Y-Axis is set to **Z Load**. Click ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) and a transparent Load-Stroke curve will display over the objects in the DISPLAY window as shown in Fig. 3DL4.22.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0022.jpg' | relative_url }})

Load Stroke graph

**Viewing die fill:**

There are several methods of evaluating die fill in the Post-processor.

The nodes which are in contact with dies can be shown by highlighting the workpiece in the Object Tree and clicking ![]({{ '/assets/icons/pre_icons/mo_show_cotact_icon.jpg' | relative_url }}) to view contact. Areas of unfill can be recognized by lack of contact. View the part at various steps to watch the contact evolve.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab04_steering_link/image0023.jpg' | relative_url }})

Area viewing Die fill

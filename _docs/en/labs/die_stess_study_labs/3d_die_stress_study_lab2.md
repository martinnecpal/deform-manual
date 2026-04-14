---
lang: en
title: "3D Die stress study with Shrink Fit Lab"
---

# 3D Die stress study Lab 2

2.1. Introduction

2.2. Opening project file

2.3. Add Die Stress Study

2.4. Adding Objects

2.5. Top Die

2.6. Bottom Die

2.7. Upper Support

2.8. Lower Support

2.9. Define Inter-Object Relation

2.10. Simulation Controls

2.11. Generate Database

2.12. Post Processing

## Introduction

The objective of this lab is to run a die stress analysis. When the stress analysis is being done on only one tool, a one step simulation is sufficient to get accurate stresses. When the stress analysis is being done on die assemblies where there is interaction between the tools, more than one step is typically needed for the die stack to come to a state of equilibrium under the applied load.

In a typical die stress simulation, the workpiece is removed and the forces exerted onto the dies by the workpiece are interpolated onto the tools. In this lab, a shrink fit will also be modeled.

## Opening project file

Open Previously simulated [**Spike_Forging.moproj**](/docs/en/labs/basic_labs/3d_labs/lab03_spike_forging/) file in ![]({{ '/assets/icons/pre_icons/mo_integrated_manufacturing_proc.jpg' | relative_url }}) (DEFORM Integrated Manufacturing Proc.) in [Lab03 Spike Forging](/docs/en/labs/basic_labs/3d_labs/lab03_spike_forging/) as shown in Fig. 3DDSL2.1. Integrated Manufacturing Process user interface will open.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0001.jpg' | relative_url }})

Opening Project file from GUI main

## Add Die Stress Study

At top Left corner of the Display window, Left mouse click on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button and select **Add Die stress Study** operation as shown in Fig. 3DDSL2.2.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0002.jpg' | relative_url }})

Adding Die stress Study

Die stress operation will add automatically to operation editor under new tab as shown in Fig. 3DDSL2.3. To perform Die stress operation, select **step 90** in Step selection page as shown in Fig. 3DDSL2.3. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0003.jpg' | relative_url }})

Adding Die stress Operation From Explorer

## Adding Objects

We need two new objects to analyze the effect of shrink fit on Top Die and provide support to Bottom die. By selecting ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button, add two objects and name them as Upper support and Lower Support respectively, as shown in Fig. 3DDSL2.4. We will accept the object type as Elastic for all objects. As Top Die is already having mesh, click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Top die object page.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0004.jpg' | relative_url }})

Adding Objects

## Top Die

### Top die object definition

By default, the object type of rigid objects from the loaded step will be changed to elastic. Keep the object type as elastic for the Top Die object. From v13.1.1, two new options have been introduced in the object page to position the dies in future steps for Multiple steps die stress analysis, we need not use these options for single step die stress analysis hence, keep the Need positioning check box turned off. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) till Material page.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_with_multiple_step/image0013.jpg' | relative_url }})

Top Die object page

### Assign Material

In material window, select **AISI-H-13** material as shown in Fig. 3DDSL2.6. and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0005.jpg' | relative_url }})

Material Window

### Assigning Boundary Conditions

  1. Select the **Symmetry plane boundary condition** , and then add a boundary condition to each of the Top Die symmetry planes as shown in Fig. 3DDSL2.7.

  2. Apply **Vz = 0** Velocity boundary condition on the top surface of the Top Die. This boundary condition prevents the die from flying off when the forces are applied. (See Fig. 3DDSL2.8.) Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Force interpolation page.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0006.jpg' | relative_url }})

Assigning Symmetry Boundary conditions

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0007.jpg' | relative_url }})

Assigning Velocity BCC

### Interpolate Forces for Top die

In Force interpolation page, click on ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}) action label as shown in Fig. 3DDSL2.9. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Bottom Die page.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0008.jpg' | relative_url }})

Force Interpolation window

## Bottom Die

### Bottom die object definition

We will keep the object type as Elastic for the Bottom Die and turn off Need positioning check box.Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Material page.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_with_multiple_step/image0014.jpg' | relative_url }})

Bottom Die object page

### Assign Material

In material window, select **AISI-H-13** material as shown in Fig. 3DDSL2.6. and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

###  Assigning Boundary Conditions

Select the Symmetry plane boundary condition, and then add a boundary condition to each of the symmetry surfaces as shown in[ Fig. 3DDSL2.11.](3d_die_stress_study_across_multiple_operations.htm#Fig_3DDSL3_11_Interpolated_forces_onto_Punch_from_Billet) We will use Lower support object to prevent Bottom Die from flying off in Z direction. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Force interpolation page.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0010.jpg' | relative_url }})

BCC Window

### Interpolate Forces for Bottom die

In Force interpolation page, click on ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}) action label as shown in Fig. 3DDSL2.12. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Object3 General page.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0009.jpg' | relative_url }})

Force interpolation window

## Upper Support

Change the name of Object 3 to **Upper Support** with **Elastic** object type as shown in Fig. 3DDSL2.13. and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0011.jpg' | relative_url }})

Upper Support Object page

### Import Geometry

In Geometry page, click on import geometry from library option (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})) and import the **UpperSupport.STL** file from installation path \SFTC\DEFORM\v*_*\3d\LABS) . Use ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) button to check the Geometry. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Mesh page.

### Generate Mesh

Enter **Target number of elements** as **12000** as shown in Fig. 3DDSL2.14. then click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Material page.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0012.jpg' | relative_url }})

Mesh Generation Window

### Assign Material

In material window, select **AISI-H-13** material as shown in Fig. 3DDSL2.6. and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Assigning Boundary Conditions

Specify **Symmetry plane boundary conditions** on the **two symmetry surfaces** of the Upper Support as shown in Fig. 3DDSL2.15.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0013.jpg' | relative_url }})

Assigning Symmetry BCC

Apply **Vz = 0** Velocity boundary condition on the **top surface** so that the object does not fly off in the Z-direction as shown in Fig. 3DDSL2.16.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0014.jpg' | relative_url }})

Assigning Velocity BCC

This object also gets a shrink fit applied to it, so select the Shrink Fit boundary condition. Shrink fit is defined radially, so an axis and a point need to be defined. For this analysis, (0, 0, 0) is the point at the center of the dies, and the Z axis is the axis of the objects. If the shrink fit is applied to the inner object, the value should be negative. If the shrink fit is applied to the outer object then the value should be positive. Since we are applying the shrink to the outer object, use a value of 0.004 for the Interference and click on ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) button. When prompted if you want to move the coordinates of the nodes, click ![]({{ '/assets/icons/pre_icons/mo_no_button.jpg' | relative_url }}). (See Fig. 3DDSL2.17.)

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0015.jpg' | relative_url }})

Move object nodal coordinates message

Once the above parameters have been set, Upper support appears as shown in Fig. 3DDSL2.18.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0016.jpg' | relative_url }})

BCC definition Window

For a better look at the applied shrink fit, click on Object Nodes ![]({{ '/assets/icons/pre_icons/mo_nodal_data_icon.jpg' | relative_url }}) icon. Plot Displacement variable vector plot using ![]({{ '/assets/icons/pre_icons/mo_plot_vector_icon.jpg' | relative_url }}) button to view the applied shrink fit on the Upper Support as shown in Fig. 3DDSL2.19.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0017.jpg' | relative_url }})

Node Data window

## Lower Support

Change the name of Object 4 to**Lower Support** with **Elastic** object type as shown in Fig. 3DDSL2.20. and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0018.jpg' | relative_url }})

Lower support Object page

### Import Geometry

In Geometry page, click on import geometry from library option (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})) and import the **LowerSupport.STL** file from installation path \SFTC\DEFORM\v*_*\3d\LABS). Use ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) button to check the Geometry. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Generate Mesh

Enter **T****arget number of Element****s** as **14000** as shown in Fig. 3DDSL2.21., then click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until material page.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0019.jpg' | relative_url }})

Mesh generation window

### Assign Material

In material window, select **AISI-H-13** material as shown in Fig. 3DDSL2.6. and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Assigning Boundary Conditions

Specify **Symmetry plane boundary conditions** on the **two****symmetry****surfaces** of the Lower Support as shown in Fig. 3DDSL2.22.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0020.jpg' | relative_url }})

Assigning Symmetry BCC

Apply **Vz = 0** **Velocity** boundary condition on the **bottom surface** so that the object does not fly off in the Z-direction. (See Fig. 3DDSL2.23.) Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Contact page

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0021.jpg' | relative_url }})

BCC Definition Window

## Define Inter-Object Relation

In Contact page, click on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button twice to add two relations in list. In First relation, select ******Upper support** as **Master** and **Top Die** as **Slave** object with friction value **0.3.** In second relation, select****Lower support**** as **Master** and **Bottom Die****** as **Slave** with friction value **0.3**. Click on ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) button to set a suitable tolerance and click on ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) to generate contacts. (See Fig. 3DDSL2.24.)

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0022.jpg' | relative_url }})

Inter-Object Window

## Simulation Controls

Set **Number of Simulation Steps** to ******6** and the **Step Increment to Save** to **1**. Set the **Max. elapsed process time per step** as **1** sec. (See Fig. 3DDSL2.25.)

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0023.jpg' | relative_url }})

Simulation Controls window

## Generate Database

Click on ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) action label to check the problem. Generate a database by clicking ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) action label.

Once the database has been generated, switch to the Simulation mode by selecting the ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the object tree. Start the simulation by clicking the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label and selecting "Start from last negative step" option. After completion of Simulation, switch to Post mode by selecting ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) button.

## Post Processing

Click the ![]({{ '/assets/icons/pre_icons/mo_show_user_defined_obj_icon.jpg' | relative_url }}) to switch to User-Defined Object Mode, which allows you to change the appearance of the objects. Use ![]({{ '/assets/icons/pre_icons/mo_show_cotact_icon.jpg' | relative_url }}) to turn on contact for both the Top Die and the Bottom Die and make both supports transparent by clicking the ![]({{ '/assets/icons/pre_icons/mo_transparent.jpg' | relative_url }}) icon for each.

This simulation was run with multiple steps so that the contact and stresses could stabilize and come to equilibrium.

Play through the steps and observe how the contact changes. The Top Die contact remains essentially the same throughout the analysis but the contact on the Bottom Die changes quite a bit. The applied load pushes the center of the die downward, causing the OD of the die to raise off of the support. At the end of the simulation, the contact has stabilized and no longer changes much from one step to the next.

Using the State Variable pull-down menu, plot Effective stress and Max Principal stress as shown in Fig. 3DDSL2.26. and Fig. 3DDSL2.27., two of the most important variables in die stress simulation.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0024.jpg' | relative_url }})

Effective Stress state variable plot

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab2/image0025.jpg' | relative_url }})

Stress-Max Principle State variable plot

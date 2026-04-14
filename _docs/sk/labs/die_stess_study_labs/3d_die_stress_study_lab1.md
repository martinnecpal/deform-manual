---
lang: sk
title: "3D Die stress Study with single step Lab1"
---

# 3D Die stress Study Lab1

1.1. Introduction

1.2. Opening project file

1.3. Add Die Stress Study

1.4. Adding Objects

1.5. Top Die

1.6. Bottom Die

1.7. Simulation Controls

1.8. Generate Database

1.9. Post Processing

## Introduction

The objective of this lab is to run a die stress analysis. When the stress analysis is being done on only one tool, a one step simulation is sufficient to get accurate stresses. When the stress analysis is being done on die assemblies where there is interaction between the tools, more than one step is typically needed for the die stack to come to a state of equilibrium under the applied load.

In a typical die stress simulation, the workpiece is removed and the forces exerted onto the dies by the workpiece are interpolated onto the tools. 

## Opening project file

Create a new problem either by selecting **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear. Select "**Integrated Manufacturing Process** " radio button and units system as "**English** " radio button to setup problem in English units system. Define Problem Name as " **Die_stress_Lab1** " and make sure the “Show option dialog” check box is turned on (if we do not turn on the “**Show option dialog** ” check box, then we will not get the New Project dialog in MO UI). Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab1/image0001.jpg' | relative_url }})

Problem defining window

MO wizard will open along with project naming window as shown in Fig. 3DDSL1.1., In the field of project name, set the project name as **Die_stress_Lab1** , select the **copy existing project** radio button as we will be copying the existing project from Labs folder which will be used as the nominal setup. Select the source location browse button and import the **Spike_Forging.moproj** from installation path \SFTC\DEFORM\v*_*\3d\LABS, turn on the **C******o** py Database** check box, click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to close the New project window. Spike_forging simulation will be imported to **Die_stress_Lab1** project. (see Fig. 3DDSL1.2.). After loading the Spike forging operation , Generate Database in Heat transfer operation using ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) option. After generating database, switch to (Simulation) ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) mode and simulate it using ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) option. After completion of simulation, switch to ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}) mode.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab1/image0002.jpg' | relative_url }})

Project imported

We will be executing die stress analysis at the end of First forming operation.

## Add Die Stress Study

At top Left corner of the Display window, Left mouse click on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button and select **Add Die stress Study operation** as shown in Fig. 3DDSL1.3.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab1/image0003.jpg' | relative_url }})

Adding Diestress study

To perform Die stress analysis at the end of first forming operation, select “**Load step from DB** ” and then select last step of the 3rd operation (**step** **90**) in Step selection page as shown in Fig. 3DDSL1.4. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab1/image0004.jpg' | relative_url }})

Step selection page

## Adding Objects

For this lab, we do not require any extra objects. So, keep default Top die and Bottom die as shown in Fig. 3DDSL1.5., click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

Accept object type as Elastic, generate mesh with default number of elements and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top die object page. 

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab1/image0005.jpg' | relative_url }})

Objects page

## Top Die

### Top Die object definition

By default, the object type of rigid objects from the loaded step will be changed to elastic. Keep the object type as elastic for the Top Die object. From v13.1.1, two new options have been introduced in the object page to position the dies in future steps for Multiple steps die stress analysis, we need not use these options for single step die stress analysis hence, keep the Need positioning check box turned off.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_with_multiple_step/image0013.jpg' | relative_url }})

Top Die object page

### Assign Material

In material window, select **AISI-H-13** material inherited from nominal simulation as shown in Fig. 3DDSL1.7. and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab1/image0006.jpg' | relative_url }})

Material Window

### Assigning Boundary Conditions

  1. Select the **Symmetry****plane****boundary****condition** , and then add a boundary condition to each of the Top Die symmetry planes as shown in Fig. 3DDSL1.8.

  2. Apply a **Vz = 0** **Velocity****boundary****condition** on the top surface of the Top Die. This boundary condition prevents the die from flying off when the forces are applied. (See Fig. 3DDSL1.9.)

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab1/image0007.jpg' | relative_url }})

Assigning Symmetry Boundary conditions

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab1/image0008.jpg' | relative_url }})

Assigning Velocity BCC

### Interpolate Forces for Top die

In Force interpolation page, click on ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}) action label and after interpolation, we are able to see force interpolated messages in the property editor page as shown in Fig. 3DDSL1.10. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab1/image0009.jpg' | relative_url }})

Top Die Force Interpolation window

## Bottom Die

### Bottom Die object Definition

We will keep the object type as Elastic for the Bottom Die and turn off Need positioning check box. Generate mesh with default number of elements and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Bottom die material page.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_with_multiple_step/image0014.jpg' | relative_url }})

Bottom Die object page

### Assign Material

In material window, select **AISI-H-13** material as shown in Fig. 3DDSL1.12. and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab1/image0006.jpg' | relative_url }})

Material Window

### Assigning Boundary Conditions

  1. Select the Symmetry plane boundary condition, and then add a boundary condition to each of the symmetry surfaces as shown in Fig. 3DDSL1.13.

  2. Apply a Vz = 0 Velocity boundary condition on the bottom surface of the bottom Die. This boundary condition prevents the die from flying off when the forces are applied. (See Fig. 3DDSL1.14.)

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab1/image0011.jpg' | relative_url }})

Defining symmetry BCC

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab1/image0012.jpg' | relative_url }})

Defining velocity BCC

### Interpolate Forces for Bottom die

In Force interpolation page, click on ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}) action label and after interpolation, we are able to see force interpolated messages in the property editor as shown in Fig. 3DDSL1.15. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab1/image0013.jpg' | relative_url }})

Force interpolation window

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to enter the controls page. There is no need of Positioning in this case. So, click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to enter the Inter-Object Contact page. For this case there is no need of any Inter-Object Contact relations as there are no objects in contact.

## Simulation Controls

By clicking ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) we will enter into Simulation controls page. Keep **number of simulation steps** as **1** , **step increment to save** as **1** and **Max. elapsed process time per step** as **1**. Keep the **Conjugate - Gradient** solver and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to enter the database generation page.

## Generate Database

By selecting the **File** menu ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **Export** option, Save a keyword file for the problem as "**Diestress** ".

Click on ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) action label to check the problem. Generate a database by clicking ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) action label.

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog. Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive.** Click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation. As we click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button, simulation starts.

After completion of Simulation, switch to Post mode by selecting ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) button.

## Post Processing

Using the **State Variable** ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) menu, plot **Effective stress** and **Max Principal stress** as shown in Fig. 3DDSL1.16. and Fig. 3DDSL1.17.

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab1/image0014.jpg' | relative_url }})

Stress effective plot

![]({{ '/assets/images/labs/die_stess_study_labs/3d_die_stress_study_lab1/image0015.jpg' | relative_url }})

Max Principal stress

**Related Topics:**

[2D Die Stress Analysis - Theory](/docs/sk/operation_templates/30_die_stress/2d_die_stress_analysis_theory/)

[3D Die Stress Analysis](/docs/sk/operation_templates/30_die_stress/30_introduction_to_die_stress/)

[Coupled Die Stress analysis](/docs/sk/operation_templates/30_die_stress/coupled_die_stress_analysis/)

[Lab 06 Die Stress](/docs/sk/labs/basic_labs/2d_labs/lab_06_die_stress/)

[Lab 12 Die Stress with Holder](/docs/sk/labs/basic_labs/2d_labs/lab_12_die_stress_with_holder/)

[Lab 13 Die Stress with Shrink Fit](/docs/sk/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/)

[Die Stress study](/docs/sk/operation_templates/49_die_stress_study/49_introduction_to_die_stress_study/)

[49.1. 2D Die Stress Study](/docs/sk/operation_templates/49_die_stress_study/49_1_2d_die_stress_study/)

[49.2. 3D Die Stress Study](/docs/sk/operation_templates/49_die_stress_study/49_2_3d_die_stress_study/)

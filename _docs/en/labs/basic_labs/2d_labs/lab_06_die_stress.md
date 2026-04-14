---
lang: en
title: "Lab 06 Die Stress"
---

# Lab 06 Die Stress

  
6.1. Introduction

6.2. Opening project file

6.3. Add Die stress study

6.4. Step selection

6.5. Top Die Setup

6.6. Bottom Die Setup

6.7. Simulation controls Setup

6.8. Generate Database

6.9. Starting the simulation

6.10. Post processing the results

## Introduction

The objective of this lab is to run a die stress analysis. When the stress analysis is being done on only one tool, a one step simulation is sufficient to get accurate stresses. When the stress analysis is being done on die assemblies where there is interaction between the tools, more than one step is typically needed for the die stack to come to a state of equilibrium under the applied load.

In a typical die stress simulation, the workpiece is removed and the forces exerted onto the dies by the workpiece are interpolated onto the tools. In this lab, we are running die stress analysis for Spike_Nonisothermal project at 50th step.

## Opening project file

Open Previously simulated**Spike_Nonisothermal.moproj** file in DEFORM MO as shown in Fig. L6.1. MO pre- processor will open.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_06_die_stress/2d_mobl6_image0001.jpg' | relative_url }})

DEFORM GUI main window

## Add Die stress study

At top Left corner of the Display window, Left mouse click on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button and select Add Die stress Study operation as shown in Fig. L6.2. A Die stress Study tab is added with Die stress operation in operation editor as shown in Fig. L6.3.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_06_die_stress/2d_mobl6_image0002.jpg' | relative_url }})

Adding Die stress operation

## Step selection

To perform Die stress operation in one step, select "**One step** " as Die stress calculation type and select **step****50** in Step selection page as shown in Fig. L6.3. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Top die page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_06_die_stress/2d_mobl6_image0003.jpg' | relative_url }})

Step selection list

## Top Die Setup

### Top die object definition

By default, the object type of rigid objects from the loaded step will be changed to elastic. Keep the object type as elastic for the Top Die object. From v13.1.1, two new options have been introduced in the object page to position the dies in future steps for Multiple steps die stress analysis, we need not use these options for single step die stress analysis, hence, keep the Need positioning check box turned off. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until BCC page to assign Boundary conditions.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_06_die_stress/2d_mobl6_image0011.jpg' | relative_url }})

Top die object general page

### Assigning Boundary condition

Apply **Vy****= 0** Velocity boundary condition on the top surface of the Top Die. This boundary condition prevents the die from flying off when the forces are applied, see Fig. L6.5. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top Die Force interpolation page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_06_die_stress/2d_mobl6_image0004.jpg' | relative_url }})

Top Die BCC page

### Force interpolation

In Force interpolation page, click on ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}) action label and after force interpolation we can see the Force interpolation report in message list, see Fig. L6.6. Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Bottom die.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_06_die_stress/2d_mobl6_image0005.jpg' | relative_url }})

Top die Force interpolation window

##  Bottom Die Setup

### Bottom Die object definition

We will keep the object type as Elastic for the Bottom Die and turn off Need positioning check box. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until BCC page to assign Boundary conditions.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_06_die_stress/2d_mobl6_image0012.jpg' | relative_url }})

Bottom die object page

### Assigning Boundary condition for Bottom Die

Apply **Vy** = 0 Velocity boundary condition on the Bottom surface of the Bottom Die. This boundary condition prevents the die from flying off when the forces are applied, see Fig. L6.8. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Bottom die Force interpolation page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_06_die_stress/2d_mobl6_image0006.jpg' | relative_url }})

Bottom die BCC page

### Force interpolation

Click on ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}) action label and after force interpolation we can see the Force interpolation report in message list, see Fig. L6.9. Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Simulation controls.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_06_die_stress/2d_mobl6_image0007.jpg' | relative_url }})

Force interpolation window

## Simulation controls Setup

In this operation we will use default Simulation controls data. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Generate DB page.

## Generate Database

Click on ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) action label to check the problem. Generate a database by clicking ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) action label.

## Starting the simulation

Once the database has been generated, switch to the Simulation mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the operation tree. Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

When the simulation is finished without any issues, the following message will be added to the end of the Message file:" Simulation is completed and stopped at the user specified time step".

## Post processing the results

After simulation complete switch to post mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) button. (See Fig. L6.10.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_06_die_stress/2d_mobl6_image0008.jpg' | relative_url }})

MO Post window

#### State Variable

Click on ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) button, plot **Effective stress** and **Max Principal stress** and observe the plot as shown in Fig. L6.11. and Fig. L6.12. These two are the most important variables in die stress simulation.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_06_die_stress/2d_mobl6_image0009.jpg' | relative_url }})

Stress Effective plot in Solid shading display

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_06_die_stress/2d_mobl6_image0010.jpg' | relative_url }})

Max Principal stress plot in Line display

In order to continue with the Die Stress Labs with Holder and with Holder and Shrink Fit do not close the MO project Refer the [Lab 12 Die Stress with Holder](/docs/en/labs/basic_labs/2d_labs/lab_12_die_stress_with_holder/) and [13 Die Stress with Shrink Fit](/docs/en/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/) respectively.

**Related Topics:**

[11\. General Object Data Definition](/docs/en/pre_processor/11_general_object_data_definition/11_general_object_data_definition/)

[14\. Boundary Conditions](/docs/en/pre_processor/14_boundary_conditions/14_boundary_conditions/)

[6.2. Integrated Manufacturing Process Simulation layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_2_integrated_manufacturing_process_simulation_layout/)

[6.3. Integrated Manufacturing Process Post-processor layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_3_integrated_manufacturing_process_post_layout/)

[25\. Post Processor Layout](/docs/en/post_processor/25_post_processor_layout/25_post_processor_layout/)

[2D Die Stress Study with Single step](/docs/en/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/)

[2D Die Stress Study with Multiple Steps](/docs/en/labs/die_stess_study_labs/2d_die_stress_study_with_multiple_steps/)

[49.1. 2D Die Stress Study](/docs/en/operation_templates/49_die_stress_study/49_1_2d_die_stress_study/)

[49.2. 3D Die Stress Study](/docs/en/operation_templates/49_die_stress_study/49_2_3d_die_stress_study/)

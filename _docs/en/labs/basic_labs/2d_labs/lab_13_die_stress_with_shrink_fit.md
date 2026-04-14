---
lang: en
title: "Lab 13 Die Stress with Shrink Fit"
---

# Lab 13 Die Stress with Shrink Fit

In this lab we are doing Die stress study for [Spike_Nonisothermal](/docs/en/labs/basic_labs/2d_labs/lab_05_spike_non-isothermal/) project and we are adding two extra object called Holder to support Bottom die and Shrink fit Rig on Top Die.

13.1. Opening Project File

13.2. Add Die stress study

13.3. Step selection

13.4. Add Objects

13.5. Top Die Setup

13.6. Bottom Die Setup

13.7. Holder Setup

13.8. Ring Setup

13.9. Generating Contact

13.10. Simulation Controls

13.11. Generating Database

13.12. Starting the Simulation

13.13. Post-Processing the Results

## Opening Project File

Open Previously simulated **Spike_NoniSothermal.moproj** file in DEFORM MO as shown in Fig. L13.1. MO pre- processor will open.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_06_die_stress/2d_mobl6_image0001.jpg' | relative_url }})

DEFORM GUI window

## Add Die stress study

If Die Stress Labs 6 and 12 are already done then Die stress Study 1 and Die Stress Study 2 tabs can be noticed as we open the Spike_Nonisothermal project Die stress Study 1 and Die Stress Study 2 tabs can be noticed as shown in Fig. L13.2. At top Left corner of the Display window, Left mouse click on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button and select Add Die stress Study operation as shown in Fig. L13.2.

A Die stress Study tab is added with Die stress operation in operation editor as shown in Fig. L13.3.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0001.jpg' | relative_url }})

Adding Die stress operation

## Step selection

To perform Die stress operation, select **step** **50** in Step selection page as shown in Fig. L13.3. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0002.jpg' | relative_url }})

Step selection list

## Add Objects

Add two object by clicking ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) button in Objects page (see Fig. L13.4.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Top die page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0003.jpg' | relative_url }})

Objects list

## Top Die Setup

### Top die object definition

By default, the object type of rigid objects from the loaded step will be changed to elastic. Keep the object type as elastic for the Top Die object. From v13.1.1, two new options have been introduced in the object page to position the dies in future steps for Multiple steps die stress analysis, we need not use these options for single step die stress analysis, hence, keep the Need positioning check box turned off. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until BCC page to assign Boundary conditions.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0023.jpg' | relative_url }})

Top die object page

### Assigning Boundary condition

Apply Vy = 0 Velocity boundary condition on the top surface of the Top Die. This boundary condition prevents the die from flying off when the forces are applied, see Fig. L13.6. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top Die Force interpolation page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0004.jpg' | relative_url }})

Top Die BCC page

### Force interpolation

In Force interpolation page, click on ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}) action label and after force interpolation we can see the Force interpolation report in message list as shown in Fig. L13.7. Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Bottom die page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0005.jpg' | relative_url }})

Top die Force interpolation window

## Bottom Die Setup

### Bottom die object definition

We will keep the object type as Elastic for the Bottom Die and turn off Need positioning check box. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until BCC page to assign Boundary conditions.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0024.jpg' | relative_url }})

Bottom Die object page

### Bottom Die BCC

In BCC page, check the default assigned Deformation BCC for Left side of the workpiece in X-Direction, default BCC are assigned automatically due to selection of problem type as axisymmetric (see Fig. L13.9.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Force Interpolation page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0006.jpg' | relative_url }})

Bottom Die BCC page

### Force interpolation

Click on ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}) action label and after force interpolation we can see the Force interpolation report in message list as shown Fig. L13.10. Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Object 4 page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0007.jpg' | relative_url }})

Force interpolation window

## Holder Setup

We will select the object type as **Elastic** for the **HOLDER** and turn off Need positioning check box as shown in Fig. L13.11.. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Geometry page to create Geometry.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0008.jpg' | relative_url }})

Holder Object page

### Creating Geometry for Holder

Click on ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}) and create a geometry by enter the following XYR coordinates value in the table 1 (see Fig. L13.12.) and click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

**X** |  **Y** |  **R**  
---|---|---  
4 |  -3 |  0  
4 |  -1 |  0  
1 |  -1 |  0  
1 |  -3 |  0  
  
Geometry XYR coordinates value

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0009.jpg' | relative_url }})

Geometry editing dialog

### Generating Mesh for Holder

Define **Number of Elements** as **150** and generate mesh using ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) (see Fig. L13.13.), then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Material page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0010.jpg' | relative_url }})

Holder Mesh page

### Assigning material for Holder

Assign**AISI-H-13** material for Holder by selecting from Material list (see Fig. L13.14.), then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0011.jpg' | relative_url }})

Assigning Holder material

### Assigning Boundary condition for Holder

Apply Vy = 0 Velocity boundary condition on the Bottom surface of the Holder as shown in Fig. L13.15., then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0012.jpg' | relative_url }})

Holder BCC page

## Ring Setup

Change the**object name** to **Ring** , set initial **temperature** as **250°** F, select the object type as **Elastic** and turn off Need positioning check box****(see Fig. L13.16.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0013.jpg' | relative_url }})

Ring object page

### Creating Geometry for Ring

Click on ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}) and create a geometry by enter the following XYR coordinates value in the table 2 (see Fig. L13.17.) and click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

**X** |  **Y** |  **R**  
---|---|---  
2.2 |  3.2 |  0  
2.2 |  1.2 |  0  
4 |  1.2 |  0  
4 |  3.2 |  0  
  
Geometry XYR coordinates value

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0014.jpg' | relative_url }})

Edit geometry dialog

### Generating Mesh for Ring

Define **Number of Elements** as **150** and generate mesh using ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) (see Fig. L13.18.), then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Material page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0015.jpg' | relative_url }})

Ring Mesh page

### Assigning material for Ring

Assign **AISI-H-13** material for Ring by selecting from Material list, then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Assigning Boundary condition for Ring

Apply Vy = 0 Velocity boundary condition on the Top surface of the Ring as shown in Fig. L13.19.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0016.jpg' | relative_url }})

Velocity BCC for Ring

Apply shrink fit in X direction = 0.008 along inside face, click NO in "Move Object Nodal Coordinates " popup (see Fig. L13.20.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Contact page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0017.jpg' | relative_url }})

Shrink Fit BCC for Ring inner surface

## Generating Contact

In Contact page, add two relations by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button. For first relation , select **Master object** as **Ring** and **Slave object** as **Top Die** and for second relation select **Master object** as **HOLDER** and **Slave object** as **Bottom Die,** define Friction value as **0.12** for both relations. Use ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) icon to determine a suitable contact tolerance (a value of about 0.00136" will be calculated), then click ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) button to generate contact as shown in Fig. L13.21. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Simulation controls page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0018.jpg' | relative_url }})

Contact generation page

## Simulation controls

In Simulation controls, define **Number of Simulation steps** as **5** , **step increment to save** as **1** , **Max elapsed process time per step** as **0.1** sec and use default solver and Iteration method as shown in Fig. L13.22. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to generate Database.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0019.jpg' | relative_url }}).

Simulation controls page

## Generating Database

Click on ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) action label to check the problem. Generate a database by clicking ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) action label.

## Starting the simulation

Once the database has been generated switch to the Simulation mode by selecting the ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the object tree. Start the simulation by clicking the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label and use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

When the simulation is finished without any issues, the following message will be added to the end of the Message file:"NORMAL STOP: Simulation is completed and stopped at the user specified time step".

## Post processing the results

After simulation complete switch to post mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) button as shown in Fig. L13.23.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0020.jpg' | relative_url }})

MO Post

**Examine resulting stress for all objects**

Click on ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) button, plot **Effective stress** and **Max Principal stress** and observe the plot as shown in Fig. L13.24. and Fig. L13.25. This two are the most important variables in die stress simulation.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0021.jpg' | relative_url }})

Stress Effective plot in Solid shading display

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_13_die_stress_with_shrink_fit/2d_mobl13_image0022.jpg' | relative_url }})

Max Principal stress plot in Line display

****

**Related Topics:**

[11\. General Object Data Definition](/docs/en/pre_processor/11_general_object_data_definition/11_general_object_data_definition/)

[14\. Boundary Conditions](/docs/en/pre_processor/14_boundary_conditions/14_boundary_conditions/)

[6.2. Integrated Manufacturing Process Simulation layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_2_integrated_manufacturing_process_simulation_layout/)

[6.3. Integrated Manufacturing Process Post-processor layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_3_integrated_manufacturing_process_post_layout/)

[25\. Post Processor Layout](/docs/en/post_processor/25_post_processor_layout/25_post_processor_layout/)

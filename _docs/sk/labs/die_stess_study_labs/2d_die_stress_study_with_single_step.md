---
lang: sk
title: "2D Die Stress Study with Single step"
---

# Lab 1: 2D Die Stress analysis using Die Stress study at single step 

Die Stress analysis can be setup using Die Stress study or Die Stress operation. Die Stress operation can be used to setup Die Stress analysis in batch mode, the operation picks the last step from the previous operation for analysis.

We will be using Stub Shaft project generated during [Lab 25 Stub Shaft](/docs/sk/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/) in MO Basic Labs, to setup the Die stress study. In this lab, we will be performing Die stress study at a step where we observe maximum load in Cone and Head operations. Since we need to analyse two different steps from two different operations, we will be using Die Stress Study for each of it independently. In a typical die stress simulation, workpiece is removed and then forces exerted onto the dies by the workpiece are interpolated onto the tools. 

1.1. Setup the Nominal project

1.2. Setting up Die Stress Study1

1.2.1. Adding Die Stress study

1.2.2. Step Selection

1.2.3. Objects definition for Die Stress Study1

1.2.4. Defining Punch

1.2.4.1. Punch object definition

1.2.4.2. Generating mesh for Punch

1.2.4.3. Assigning material to Punch

1.2.4.4. Assigning Boundary conditions to Punch

1.2.4.5. Force interpolation from Billet

1.2.5. Defining Bottom Die

1.2.5.1. Bottom Die object Definition

1.2.5.2. Generating mesh for Bottom Die

1.2.5.3. Assigning material for Bottom die

1.2.5.4. Assigning Boundary conditions to Bottom Die

1.2.5.5. Force interpolation from Billet

1.2.6. Defining Simulation Controls

1.2.7. Generating Database

1.2.8. Running simulation

1.2.9. Post-Processing simulation results of Die Stress Study1

1.3. Setting up Die Stress Study2

1.3.1. Adding second Die Stress Study

1.3.2. Step Selection

1.3.3. Objects Definition for Die Stress Study2

1.3.4. Defining Punch

1.3.4.1. Punch object Definition

1.3.4.2. Generating mesh for Punch

1.3.4.3. Assigning material for Punch

1.3.4.4. Assigning Boundary conditions to Punch

1.3.4.5. Force interpolation from Billet

1.3.5. Defining Bottom Die

1.3.5.1. Bottom Die object definition

1.3.5.2. Generating Mesh for Bottom Die

1.3.5.3. Assigning material for Bottom Die

1.3.5.4. Assigning Boundary conditions to Bottom Die

1.3.5.5. Force interpolation from Billet

1.3.6. Defining Simulation Controls

1.3.7. Generating Database

1.3.8. Running simulation

1.3.9. Post-Processing simulation results of Die Stress Study2

## Setup the Nominal project

Setup the[ Lab 25 Stub Shaft](/docs/sk/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/) in MO Basic Labs. Switch to ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) and plot Load-stroke curve, see Fig. 2DDSL1.1, we can observe that Load is maximum at the last step of Cone and Head operations. We will now execute Die Stress analysis at the last step of the Cone operation. Switch to ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}) tab to add Die Stress study operation. 

  
![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0001.jpg' | relative_url }})

Load-stroke graph of Cone and Head operations from Stub Shaft Project.

## Setting up Die Stress Study1

### Adding Die Stress study

At top Left corner of the Display window, click on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button and select Add Die Stress Study operation as shown in Fig. 2DDSL1.2. A Die Stress Study operation tab will be added in display area and Die Stress operation tile will be available in operation editor under new tab as shown in Fig. 2DDSL1.3.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0002.jpg' | relative_url }})

Adding Die stress study operation.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0003.jpg' | relative_url }})

Display of Die Stress Study operation.

###  Step Selection

As we need to analyze die stress only at last step of the Cone operation, select Die stress calculation type as “**One step** ” and select “**Load step from DB** ” radio button to load objects from the selected step. Select last step of Cone operation from Step selection page as shown in Fig. 2DDSL1.4., data of all objects will be loaded into display from the selected step. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0004.jpg' | relative_url }})

Selecting step for Die Stress Study1.

### Objects definition for Die Stress Study1

Since we need to do the Die stress study only on Punch and Bottom Die, we will delete rest of the objects. In the objects page, delete the Ejector object as shown in Fig. 2DDSL1.5. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0005.jpg' | relative_url }})

Deleting unnecessary objects in Objects page.

### Defining Punch

#### Punch object definition

By default, the object type of rigid objects from the loaded step will be changed to elastic. Keep the object type as elastic for the Punch object. From v13.1.1, two new options have been introduced in the object page to position the dies in future steps for Multiple steps die stress analysis, we need not use these options for single step die stress analysis hence, keep the Need positioning check box turned off, see Fig. 2DDSL1.6.. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Mesh page.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0028.jpg' | relative_url }})

Punch object page

#### Generating mesh for Punch

Define target number of elements as 2500 as shown in Fig. 2DDSL1.7. and generate mesh using ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button, then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Material page.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0006.jpg' | relative_url }})

Mesh settings for Punch.

#### Assigning material to Punch

Import material AISI-D3 from the material library. Choose **AISI-D3** from the list to assign the material for Punch as shown in Fig. 2DDSL1.8. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Boundary condition page.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0007.jpg' | relative_url }})

Assigning material to Punch.

#### Assigning Boundary conditions to Punch

We need to apply boundary conditions to Punch so that it does not fly off into space when the forming loads are applied to it. By default, for an axisymmetric product all nodes along x direction at centerline are fixed, if not make sure that the direction of the boundary condition is set to X and then click on centreline using By edge ![]({{ '/assets/icons/pre_icons/mo_bcc_edge_icon.jpg' | relative_url }}) button from picking options. Pick a point on the centerline of the Punch and click on ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) button, you should see that all nodes on centerline are fixed along X direction.

  
Now to set the boundary condition along Y direction, select the top surface of the Punch using ![]({{ '/assets/icons/pre_icons/mo_bcc_edge_icon.jpg' | relative_url }}) button from picking options to fix all those nodes along Y direction and click on ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) button. (See Fig. 2DDSL1.9.) Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Force interpolation page.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0008.jpg' | relative_url }})

Assigning boundary conditions to Punch.

#### Force interpolation from Billet

Click on ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}) to interpolate the forces exerted onto dies by the Billet, once the forces are interpolated, we should be observing a message comparing the forces from the Billet to the new forces on the Punch in Force interpolation page as shown in Fig. 2DDSL1.10. These forces should be relatively close to one another. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define Bottom Die.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0009.jpg' | relative_url }})

Interpolated forces onto Punch from Billet.

### Defining Bottom Die

#### Bottom Die object Definition

We will keep the object type as Elastic for the Bottom Die and turn off Need positioning check box. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Mesh page to generate mesh.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0029.jpg' | relative_url }})

#### Generating mesh for Bottom Die

Define target number of elements as 2500 as shown in Fig. 2DDSL1.11. and Generate mesh, then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Material page.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0010.jpg' | relative_url }})

Mesh Settings for Bottom Die.

#### Assigning material for Bottom die

In Material page, choose **AISI-D3** from the list to assign the material for Bottom Die. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Boundary condition.

#### Assigning Boundary conditions to Bottom Die

We need to apply boundary conditions to the Bottom Die so that it does not fly off into space when the forming loads are applied to it.  
  
Now, set the boundary condition direction to Y, select a point on the bottom surface of the Bottom Die to fix all those nodes along Y direction. (See Fig. 2DDSL1.12.). Since it is an axi-symmetric setup, X direction is already constrained. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Force interpolation page.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0011.jpg' | relative_url }})

Assigning Boundary conditions to Bottom Die.

#### Force interpolation from Billet

Once the mesh is generated, the forming loads from the Billet need to be interpolated onto the Bottom Die. Click on ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}), once the forces are interpolated, we should be observing a message comparing the forces from the Billet to the new forces on the Bottom Die in Force interpolation page as shown in Fig. 2DDSL1.13. These forces should be relatively close to one another. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Simulation controls window.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0012.jpg' | relative_url }})

Interpolated forces onto Bottom Die from Billet.

### Defining Simulation Controls

Define the Number of steps as 2 and keep the rest of the settings as default as shown in Fig. 2DDSL1.14. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0013.jpg' | relative_url }})

Simulation controls settings for Die Stress Study1.

###  Generating Database

In DB Generation page, check the data for any errors in setup and generate database. After generating database, switch to ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) mode to run the simulation.

### Running simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog. Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation. As we click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button, simulation starts. After simulation is completed, switch to ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) tab.

### Post-Processing simulation results of Die Stress Study1

The main variables to look at for a die stress simulation are the Effective stress and the Maximum principal stress.  
  
The Effective stress is used to see whether any location in the die underwent plastic deformation. If any area of the die has an effective stress close to or exceeding the yield stress of the die material, that region is at risk of plastically deforming. (See Fig. 2DDSL1.15.)  
  
The Maximum principal stress is used to see which regions of the die are in a state of compression and which are in a state of tension. Maximum principal stress is extremely important in determining whether a die will experience any cracking due to fatigue. To display the Maximum principal stress, click on the state variable “Set up” button ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) and then select Stress – Max Principal from the list. (See Fig. 2DDSL1.16.)

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0014.jpg' | relative_url }})

Effective Stress distribution at last step in Dies of Cone operation.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0015.jpg' | relative_url }})

Maximum Principal Stress distribution at last step in Dies of Cone operation.

## Setting up Die Stress Study2

After the post processing Die Stress Study1, switch to ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}) tab.

### Adding second Die Stress Study

We will add another Die Stress Study operation to analyze stresses in Die at the end of Head operation. At top Left corner of the Display window, click on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button and select Add Die stress Study operation as shown in Fig. 2DDSL1.17. Second Die Stress Study operation tab will be added in display area and Die Stress operation tile will be available in operation editor of new tab as shown in Fig. 2DDSL1.17.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0016.jpg' | relative_url }})

Adding Second Die stress study operation.

### Step Selection

To perform Die stress operation at the end of Head operation, select “**Load step from DB** ” and then, select last step of second operation in Step selection page as shown in Fig. 2DDSL1.18. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) .

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0017.jpg' | relative_url }})

Step selection for Die Stress Study2.

###  Objects Definition for Die Stress Study2

Since we need to do the die stress study only on Punch and Bottom Die, we will delete the rest of the objects. In the objects page, delete the Ejector object as shown in Fig. 2DDSL1.19. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0018.jpg' | relative_url }})

Deleting unnecessary objects in Objects page.

### Defining Punch

#### Punch object Definition

The Punch object type has been set to Elastic by default, we will keep this selection and turn off “Need positioning” check box as shown in Fig. 2DDSL1.6. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Mesh page.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0028.jpg' | relative_url }})

#### Generating mesh for Punch

Define target number of elements as 2500 as shown in Fig. 2DDSL1.20. and Generate mesh, then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Material page.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0019.jpg' | relative_url }})

Mesh settings for Punch in Head operation.

#### Assigning material for Punch

Import a die material AISI-D3 from the material library. Choose **AISI-D3** from the list to assign the material for Punch. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Boundary conditions page.

#### Assigning Boundary conditions to Punch

We need to apply boundary conditions to the Punch so that it does not fly off into space when the forming loads are applied to it. Click on “By edge” ![]({{ '/assets/icons/pre_icons/mo_bcc_edge_icon.jpg' | relative_url }}) button from picking options and pick a point on the top surface of the Punch to fix all those nodes along Y direction and click on ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) button. Since it is an axi-symmetric setup, X direction is already constrained, if not constrain the X direction similar to Y direction along the centerline of the Punch. (See Fig. 2DDSL1.21.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Force interpolation page.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0020.jpg' | relative_url }})

Punch Boundary conditions.

#### Force interpolation from Billet

Click on ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}), once the forces are interpolated, we should be observing a message comparing the forces from the Billet to the new forces on the Punch in Force interpolation page as shown in Fig. 2DDSL1.22. These forces should be relatively close to one another. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0021.jpg' | relative_url }})

Interpolated forces onto Punch from Billet.

### Defining Bottom Die

#### Bottom Die object definition

By default, the object type of Bottom Die is set to Elastic, we will keep the selection and turn off Need positioning check box. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Mesh page.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0029.jpg' | relative_url }})

#### Generating Mesh for Bottom Die

Define target number of elements as 2500 as shown in Fig. 2DDSL1.23. and Generate mesh, then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Material.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0022.jpg' | relative_url }})

Mesh settings for Bottom Die.

#### Assigning material for Bottom Die

In Material page, choose **AISI-D3** from the list to assign the material for Bottom Die. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Boundary condition page.

####  Assigning Boundary conditions to Bottom Die

We need to apply boundary conditions to the Bottom Die so that it does not fly off into space when the forming loads are applied to it.  
Now set the boundary condition direction to Y, select a point on the bottom surface of the Bottom to fix all those nodes along Y direction and click on ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) button. (See Fig. 2DDSL1.24.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Force interpolation.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0023.jpg' | relative_url }})

Bottom Die Boundary conditions.

#### Force interpolation from Billet

Click on ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}), once the forces are interpolated, we should be observing a message comparing the forces from the Billet to the new forces on the Bottom Die in Force interpolation page as shown in Fig. 2DDSL1.25. These forces should be relatively close to one another. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until simulation controls page.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0024.jpg' | relative_url }})

Forces interpolated onto Bottom Die from Billet.

### Defining Simulation Controls

Define the Number of steps as 2 and keep the rest of the settings as default as shown in Fig. 2DDSL1.26. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0025.jpg' | relative_url }})

Simulation controls settings for Die Stress Study2.

### Generating Database

Check the data and generate the Database. After generating Database switch to ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) mode to run the simulation.

### Running simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog. Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation. As we click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button, simulation starts. After simulation is completed, switch to ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) tab.

### Post-Processing simulation results of Die Stress Study2

The main variables to look at for a die stress simulation are the Effective stress and the Maximum principal stress.

Effective stress distribution in Dies at the last step of Die stress analysis is shown in Fig. 2DDSL1.27.

The Maximum principal stress distribution in Dies at the last step of Die stress analysis is shown in Fig. 2DDSL1.28.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0026.jpg' | relative_url }})

Effective Stress distribution at last step in Dies of Head operation. 

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/image0027.jpg' | relative_url }})

Maximum Principal Stress distribution at last step in Dies of Cone operation.

[2D Die Stress Study with Single step]()

[49.1. 2D Die Stress Study](/docs/sk/operation_templates/49_die_stress_study/49_1_2d_die_stress_study/)

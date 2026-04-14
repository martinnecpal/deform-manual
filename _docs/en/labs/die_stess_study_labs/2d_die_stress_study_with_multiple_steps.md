---
lang: en
title: "2D Die Stress Study with Multiple Steps"
---

# Lab2 : 2D Die Stress study at Multiple steps of an Operation 

2.1. Setup the Nominal project

2.2. Adding Die Stress study

2.3. Step Selection

2.4. Objects definition for Die Stress Study

2.5. Defining Punch

2.5.1. Defining Punch object data

2.5.2. Generating mesh for Punch

2.5.3. Assigning material to Punch

2.5.4. Assigning Boundary conditions to Punch

2.5.5. Interpolating force from Billet and scheduling interpolation

2.6. Defining Bottom Die

2.6.1. Defining Bottom Die object data

2.6.2. Generating mesh for Bottom Die

2.6.3. Assigning material to Bottom Die

2.6.4. Assigning Boundary conditions to Bottom Die

2.6.5. Interpolating force from Billet and scheduling interpolation

2.7. Defining Simulation Controls

2.8. Generating Database

2.9. Running simulation

2.10. Post-Processing simulation results

In this lab we will be using Die Stress Study to analyse stresses on dies at multiple steps of an operation. Currently, multiple steps to analyse stresses should be from same operation. In a typical die stress simulation, the workpiece is removed, and the forces exerted onto the dies by the workpiece are interpolated onto the tools. 

In this lab we will be using Die Stress Study to analyse stresses on dies at multiple steps of an operation. Currently, multiple steps to analyse stresses should be from same operation. In a typical die stress simulation, the workpiece is removed, and the forces exerted onto the dies by the workpiece are interpolated onto the tools.  
When we use the multiple steps option, we will be setting up Die stress analysis for the first step of the selected steps and for future steps of die stress analysis, we will be scheduling interpolation of forces from workpiece. The object data, simulation controls and other settings will be carried on from the first die stress analysis step. From v13.1.1, two new options have been introduced in the object page to position the dies in future steps, see Fig. 2DDSL2.1.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_multiple_steps/image0021.jpg' | relative_url }})

Die positioning options for future steps in die stress study

  
**Die positioning in future steps in multi-step die stress study:**

In a multiple step die stress study, if the object requires positioning, then the user needs to choose how the object must be positioned in future steps by turning on the Need positioning check box in object page as shown in Fig. 2DDSL2.1.

  * If the object is part of the nominal setup and requires positioning, then user needs to turn on Need positioning check box and select the respective object from the nominal setup as Following object.

  * If the object is not part of the nominal setup but is within the bounding box of the nominal setup object and requires positioning, then user needs to turn on Need positioning check box and select the respective object from the nominal setup within whose bounding box the current object resides as Following object. We should not turn on the Not original object check box so that Force interpolation from the nominal setup can be executed onto the current object.

  * If the object is not part of the nominal setup and is not within the bounding box of the any of the nominal setup objects and requires positioning, then user needs to turn on Need positioning check box and select the object from the nominal setup with which the current object makes contact or follow as Following object. We should also turn on the Not original object checkbox. When user turns on the Not original object check box for an object, then the force interpolation will not be executed onto that object.

  
We will be using Stub Shaft project generated during [Lab 25 Stub Shaft](/docs/en/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/) in MO Basic Labs to setup the Die Stress Study at multiple steps.

## Setup the Nominal project

Setup the [Lab 25 Stub Shaft](/docs/en/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/) in MO Basic Labs. After the completion of the simulation, switch to ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}) tab. (See Fig. 2DDSL2.2.)

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_multiple_steps/image0001.jpg' | relative_url }})

Simulation monitor showing the end of Stub Shaft lab simulation.

##  Adding Die Stress study

At top Left corner of the Display window, click on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button and select Add Die stress Study operation as shown in Fig. 2DDSL2.3. A Die Stress Study operation tab will be added in display area and Die Stress operation tile will be available in operation editor under new tab as shown in Fig. 2DDSL2.4.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_multiple_steps/image0002.jpg' | relative_url }})

Adding Die stress study operation.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_multiple_steps/image0003.jpg' | relative_url }})

Display of Die Stress Study operation.

## Step Selection

Since we want analyze stresses at multiple steps of an operation, select “**Multiple steps** ” radio button as Die stress selection type. Select “**Load steps from DB** ” radio button to load the object data from the first step of the selected steps and using “**User defined** ” radio button, select steps 10, 25, 45, 65, 85 and 96 of Cone operation in step selection page to analyze stresses at these steps as shown in Fig. 2DDSL2.5. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_multiple_steps/image0004.jpg' | relative_url }})

Selecting multiple steps of Cone operation to analyse stresses in dies.

## Objects definition for Die Stress Study

Since we need to do the Die stress study only on Punch and Bottom Die, we will delete rest of the objects. In the objects page, delete the Ejector object as shown in Fig. 2DDSL2.6. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_multiple_steps/image0005.jpg' | relative_url }})

Deleting unnecessary objects in Objects page.

## Defining Punch 

### Defining Punch object data

By default, the object type of rigid objects from the loaded step will be changed to elastic. Keep the object type as elastic for the Punch object. Since this object exists in nominal operation and requires positioning in future steps, turn on Need positioning checkbox and select Punch object of nominal operation as Following object from pulldown menu as shown in Fig. 2DDSL2.7 Cick ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Mesh page.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_multiple_steps/image0019.jpg' | relative_url }})

Punch object page

### Generating mesh for Punch

To generate mesh, define target number of elements as 2500 as shown in Fig. 2DDSL2.8. and click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Material page.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_multiple_steps/image0006.jpg' | relative_url }})

Mesh settings for Punch.

### Assigning material to Punch

Import material AISI-D3 from the material library. Choose **AISI-D3** from the list to assign the material for Punch as shown in Fig. 2DDSL2.9. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Boundary conditions page.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_multiple_steps/image0007.jpg' | relative_url }})

Assigning material to Punch.

### Assigning Boundary conditions to Punch

We need to apply boundary conditions to Punch so that it does not fly off into space when the forming loads are applied to it. By default, for an axisymmetric product all nodes along x direction at centerline are fixed, if not make sure that the direction of the boundary condition is set to X and then click on centreline using By edge ![]({{ '/assets/icons/pre_icons/mo_bcc_edge_icon.jpg' | relative_url }}) button from picking options. Using ![]({{ '/assets/icons/pre_icons/mo_bcc_edge_icon.jpg' | relative_url }}) button from picking options, we can add BCC to all nodes/elements on an edge. Pick a point on the centerline of the Punch and click on ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) button, you should see that all nodes on centerline are fixed along X direction. 

  
Now to set the boundary condition along Y direction, select the top surface of the Punch using ![]({{ '/assets/icons/pre_icons/mo_bcc_edge_icon.jpg' | relative_url }}) button from picking options to fix all those nodes along Y direction and click on ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) button. (See Fig. 2DDSL2.10.) Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Force interpolation page.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_multiple_steps/image0008.jpg' | relative_url }})

Assigning boundary conditions to Punch.

### Interpolating force from Billet and scheduling interpolation

Click on ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}) to interpolate the forces exerted onto dies by the Billet, once the forces are interpolated, we should be observing a message comparing the forces from the Billet to the new forces on the Punch in Force interpolation page as shown in Fig. 2DDSL2.11. These forces should be relatively close to one another. 

Since we are simulating for multiple steps, we need to schedule the interpolation of forces from Billet. To do so, turn on checkbox adjacent to “Interpolation force” and keep Tolerance as “0” so that tolerance for interpolation is auto calculated. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define Bottom Die.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_multiple_steps/image0009.jpg' | relative_url }})

Interpolated forces onto Punch from Billet.

## Defining Bottom Die

### Defining Bottom Die object data

We will keep the object type as Elastic for the Bottom Die. Turn ON Need positioning checkbox and select Bottom Die of Nominal database objects from Following object pulldown menu as shown in Fig. 2DDSL2.12. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Mesh page to generate mesh.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_multiple_steps/image0020.jpg' | relative_url }})

Bottom Die Object page

### Generating mesh for Bottom Die

Define target number of elements as 2500 as shown in Fig. 2DDSL2.13. and Generate mesh, then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Material page.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_multiple_steps/image0010.jpg' | relative_url }})

Mesh Settings for Bottom Die.

### Assigning material to Bottom Die

In Material page, choose AISI-D3 from the list to assign the material for Bottom Die. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Boundary conditions page.

###  Assigning Boundary conditions to Bottom Die

Next, we need to apply boundary conditions to the Bottom Die so that it does not fly off into space when the forming loads are applied to it.

Now, set the boundary condition direction to Y, select the bottom edge of the Bottom Die to fix all those nodes along Y direction. (See Fig. 2DDSL2.14.) and click on click on ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) button. Since it is an axi-symmetric setup, X direction is already constrained, if not, constrain the centerline nodes in X direction similar to Y direction on bottom edge. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Force interpolation page.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_multiple_steps/image0011.jpg' | relative_url }})

Assigning Boundary conditions to Bottom Die.

### Interpolating force from Billet and scheduling interpolation

Once the mesh is generated, the forming loads from the Billet need to be interpolated onto the Bottom Die. Click on ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}), once the forces are interpolated, we should be observing a message comparing the forces from the Billet to the new forces on the Bottom Die in Force interpolation page as shown in Fig. 2DDSL2.15. These forces should be relatively close to one another. 

To schedule force interpolation for future steps of die stress analysis, turn on check box adjacent to “Interpolation force” and keep “Tolerance” as “0”. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Simulation controls window.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_multiple_steps/image0012.jpg' | relative_url }})

Interpolated forces onto Bottom Die from Billet 

## Defining Simulation Controls

Define the Number of steps as 2 and keep the rest of the settings as default as shown in Fig. 2DDSL2.16. These settings will be carried on for future die stress analysis steps. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_multiple_steps/image0015.jpg' | relative_url }})

Simulation controls settings for die stress analysis

## Generating Database

In DB Generation page, check the data for any errors in setup and generate database. After generating database, switch to ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) mode to run the simulation.

## Running simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog. Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation. As we click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button, simulation starts.

After simulation of all steps die stress analysis is completed, log file displays message “MULTIPLE OPERATION COMPLETED” as shown in Fig. 2DDSL2.17. Switch to ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) tab to view results.

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_multiple_steps/image0016.jpg' | relative_url }})

Log file displaying end of simulation for all selected steps of die stress analysis

## Post-Processing simulation results

Each selected step will be displayed as separate operation with operation name as From Step XX (XX is selected step number). The main variables to look at for a die stress simulation are the Effective stress and the Maximum principal stress.  
  
The effective stress is used to see whether any location in the die underwent plastic deformation. If any area of the die has an effective stress close to or exceeding the yield stress of the die material, that region is at risk of plastically deforming. (See Fig. 2DDSL2.18.)  
  
The maximum principal stress is used to see which regions of the die are in a state of compression and which are in a state of tension. Maximum principal stress is extremely important in determining whether a die will experience any cracking due to fatigue. To display the maximum principal stress, click the state variable “Set up” button ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) and then select Stress – Max Principal from the list. (See Fig. 2DDSL2.19.)

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_multiple_steps/image0017.jpg' | relative_url }})

Effective Stress distribution at the end of last step of die stress analysis in Cone operation

![]({{ '/assets/images/labs/die_stess_study_labs/2d_die_stress_study_with_multiple_steps/image0018.jpg' | relative_url }})

Maximum Principal Stress distribution at the end of last step of die stress analysis in Cone operation

[2D Die Stress Study with Single step](/docs/en/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/)

[49.1. 2D Die Stress Study](/docs/en/operation_templates/49_die_stress_study/49_1_2d_die_stress_study/)

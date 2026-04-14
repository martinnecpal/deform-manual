---
lang: sk
title: "2D Heat Treatment Wizard Lab1"
---

# 2D Heat Treatment Wizard Lab1

1.1. Introduction

1.2. Starting a New problem

1.3. Process Settings

1.4. Material definition

1.5. Workpiece Object Type

1.5.1. Defining Workpiece Object Data

1.5.2. Import Geometry

1.5.3. Generate Mesh

1.5.4. Assigning Material

1.5.5. Generating Coating Mesh

1.5.6. Assigning Boundary conditions

1.5.7. Workpiece Phase levels initialization

1.6. Medium Definition

1.7. Scheduled Definition

1.8. Simulation controls

1.9. Generate Database

1.10. Starting the Simulation

1.11. Post processing

## Introduction

The Heat Treatment Wizard is a convenient tool to set up complex multiple-operation heat treatment problem. This lab will demonstrate how to use this wizard to prepare a carburization-quench-tempering simulation of a steel part. This lab can also help users understand the capabilities of DEFORM-HT's phase transformation calculation scheme.

##  Starting a New problem

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear

Create a new problem either by selecting **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in [Fig. 2DHTWL1.1.]() Select " **Integrated Manufacturing Process** " radio button and units system as "**SI** " using radio button. Define Problem Name as "**QUENCH** " and make sure the “Show option dialog” check box is turned on (if we do not turn on the “**Show option dialog** ” check box, then we will not get the New Project dialog in MO UI). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image014.jpg' | relative_url }})

Problem type selection window

  
Multiple operation wizard will open with the New Project dialog as shown in Fig. 2DHTWL1.2., at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title. In this lab we will use ‘**QUENCH** ’ as the project name. 

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0002.jpg' | relative_url }})

MO wizard New project

User can also change the Unit system (File menu selected unit system will be selected by default) and add HT operation by selecting it from First operation pull down list and turning on checkbox (See Fig. 2DHTWL1.3.). Using copy Existing project option, we can import previous saved projects as new project. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.  
  
Multiple Operation wizard will open. Add 2D HT Wizard operation from the Explorer Operations list. Add the operation by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button next to 2D HT Wizard or user can also add by drag and drop into the Operation Editor (See Fig. 2DHTWL1.3..). 

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0003.jpg' | relative_url }})

Adding 2D HT Wizard into Operation Editor

## Process Settings

As the operation is added, Process settings page is opened as shown in Fig. 2DHTWL1.4. User can set the simulation mode based on the simulation requirement along with step definition controls.

Turn on "**Deformation** " and "**Phase****Transformation** " as we would like to predict residual stresses and phase transformation calculations during the process. Step definition will be defined in Simulation controls page. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) (See Fig. 2DHTWL1.4.). 

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0004.jpg' | relative_url }})

Defining Process settings in 2D HT Wizard

Initialization page will open, we can observe that Phase transformation and Deformation check boxes are turned on (See Fig. 2DHTWL1.5.), we will leave the settings in Initialization page as it is and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

  
  
![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0005.jpg' | relative_url }})

Initialization Setup window

## Material definition

In Material window, load the material (JIS-S45C (Heat Treatment)) from DEFORM Material library, from Steel category using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load material data from library) option. This can be done as shown in Fig. 2DHTWL1.6. by clicking ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}) button. Material can also be load from Materials list in Explorer. Then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) unitl Workpiece page. 

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0006.jpg' | relative_url }})

Importing Material page

## Defining Workpiece

### Defining Workpiece Object Data

In Workpiece page, change the object type to **Elasto-plastic** type, as we need to predict residual stresses (See Fig. 2DHTWL1.7.). Set object temperature as **900** °C. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

  
![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0007.jpg' | relative_url }})

Workpiece object definition

### Import Geometry

In Geometry page, click on ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (import geometry from library) option and import the **QUENCH_PART.IGS** file from installation path \SFTC\DEFORM\v*_*\2d\LABS as shown in Fig. 2DHTWL1.8. Use ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) action label to check the Geometry. A perfect geometry should display message as shown in Fig. 2DHTWL1.9. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

  
  
![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0008.jpg' | relative_url }})

Importing Geometry for Workpiece

  
![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0009.jpg' | relative_url }})

Output of imported geometry checking

### Generate Mesh

In Mesh page, enter**Target number of elements** as **500** and click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button. After completion of generating mesh, click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button to assign material for workpiece. 

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0010.jpg' | relative_url }})

Mesh settings and mesh generated

### Assigning Material

Select and assign **S45C-JAPAN** Material as shown in Fig. 2DHTWL1.11. Click ![]({{ '/assets/icons/pre_icons/mo_back_button.jpg' | relative_url }}) to generate coating mesh.

  
![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0011.jpg' | relative_url }})

Assigning Material to workpiece

### Generating Coating Mesh

Switch to expert mode by click on ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}). We will be adding coating layers to obtain better information about the phase transformations on surfaces. Select Coating tab and add 2 layers by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_icon.jpg' | relative_url }}) button. Set 500 and 1000 for thickness of layer 1 and 2 respectively as shown in Fig. 2DHTWL1.12., select same material **S45C-JAPAN** and click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button. Click on ![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }}) to change to guided mode. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until boundary conditions page.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0012.jpg' | relative_url }})

Coating mesh settings used in Workpiece mesh generation

### Assigning Boundary conditions

  1. Select X direction and define velocity as 0, pick nodes along axis as shown in Fig. 2DHTWL1.13. to constrain nodal velocity in X direction, as this is an axi-symmetric set up.

  2. Select Y direction and define velocity as 0, pick nodes along bottom surface of the workpiece as shown in Fig. 2DHTWL1.13. to constrain nodal velocity in Y direction of workpiece during quench.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0013.jpg' | relative_url }})

Assigning Velocity BCC

### Workpiece Phase levels initialization

Since we need to calculate phase transformation, we need to initialize initial level of each phase, keep note that sum of all phases at each element should be equal to 1. Since the object temp is 900°C and the material is steel, the material would have changed to Austenite phase completely, we will initialize entire workpiece to Austenite phase. To do so, click on object element data ![]({{ '/assets/icons/pre_icons/mo_elemental_data_icon.jpg' | relative_url }}) and select Phase transformation tab under Microstructure. Initialize Austenite as 1 and zero for the rest by selecting phase and using ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}) (See Fig. 2DHTWL1.14.). In Initialize Element Data window assign value using Range option by defining 1 as value as shown in Fig. 2DHTWL1.15. and then click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) button. Click on ![]({{ '/assets/icons/pre_icons/mo_close_button2.jpg' | relative_url }}) button to close the Initialize Element Data window and click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close Element data dialog. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define the medium details.

  
![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0014.jpg' | relative_url }})

Phase level initialization in object Element Data

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0015.jpg' | relative_url }})

Element Data initialization window

## Medium Definition

The simulation consists of quenching, we need to define required medium for this operation, in this case we require water and air. In page “Medium details”, you will define various media and heat transfer zones associated with them as shown in Fig. 2DHTWL1.16.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0016.jpg' | relative_url }})

Medium Details window

  1. Rename the first medium to “Air” and set the “Default” Heat transfer coefficient (HTC) and convection coefficient to constant 0.05 as shown in Fig. 2DHTWL1.16.

  2. Add a media “Water”. For "Default" HTC, load convection coefficient data from file "WATER_HTC1_si.DAT".

  3. Add one more heat transfer zone under media “Water”. Click on the object boundary to specify the start and end points of the zone. The zone is assigned to the bottom of the workpiece as shown in Fig. 2DHTWL1.17. For Zone #1 HTC, load convection coefficient from file " WATER_HTC2_si. DAT" and click on define function to observe the function data as shown in Fig. 2DHTWL1.18. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define the schedule page.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0017.jpg' | relative_url }})

Medium detail window showing zone allocation

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0018.jpg' | relative_url }})

Function definition window

## Scheduled Definition

In “Schedule” page, input a five-stage quench schedule as shown in Fig. 2DHTWL1.19. by clicking on 'Add' button. A procedure like this is sometimes referred as "Intensive Quenching", which is designed to create a very thin "crust" of Martensite on the part. Such a process can achieve high surface hardness with relative low part distortion. 

1) 20 seconds(20s) cooling in the air at 20C

2) 10 seconds(10s) cooling in the water at 70C

3) 60 seconds(60s) cooling in the air at 20C

4) 5 seconds(10s) cooling in the water at 70C

5) 20 Minutes(1200 s) cooling in the air at 20C

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0019.jpg' | relative_url }})

Heat Treatment Schedule window

The settings for each stage can be set or modified using ![]({{ '/assets/icons/pre_icons/mo_define.._button.jpg' | relative_url }}) button in advanced column. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Simulation controls page.

## Simulation controls

In "Step Definition", select Auto radio button and change "Temp. Change per step" to 5°C and keep other default settings. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to DB generation page. (See Fig. 2DHTWL1.20.)

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0020.jpg' | relative_url }})

Simulation controls window

## Generate Database

Click on ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) action label to check the problem. Generate a database by clicking ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) action label (see Fig. 2DHTWL1.21.). When the program is done writing the database, switch to ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) tab to run simulation.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0021.jpg' | relative_url }})

Generate Database Window

## Starting the Simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. 2DHTWL1.22. Use the default **Continue Run** option to select “**Continue from the last step** ” (from step -1) option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation. As we click on the ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button simulation starts.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0022.jpg' | relative_url }})

Run simulation window

The progress of the simulation can be monitored as it is running by looking at the Simulation Message and process monitor in Simulation mode. Click the Simulation Message tab to view the Message file. If ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked, which is the default setting, the Message file will refresh every couple of seconds.  
  
The Message file provides information about which simulation step the simulation is currently on and gives information dealing with how well the simulation is running.  
When the simulation has finished, the message will be added to the end of the Message file. (See Fig. 2DHTWL1.23.).  
  
Each stage defined will be executed as individual operation and user need to wait until all the stages simulation is completed.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0023.jpg' | relative_url }})

Simulation Message tab

## Post processing

When the simulation has finished, click on ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}). In Step Browser click on ![]({{ '/assets/icons/pre_icons/mo_all_button.jpg' | relative_url }}) button to view all steps. Plot Temperature state variable and observe the temperature distribution at different stages of quenching operation (See Fig. 2DHTWL1.24.). Also plot the volume fraction of each phases at the end of the Quenching process using Volume fraction state variable under microstructure. (See Fig. 2DHTWL1.25.).

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0024.jpg' | relative_url }})

Temperature distribution at different stages of quenching operation.

  
![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/image0025.jpg' | relative_url }})

Volume fraction of each phases at the end of the Quenching process of quenching operation.

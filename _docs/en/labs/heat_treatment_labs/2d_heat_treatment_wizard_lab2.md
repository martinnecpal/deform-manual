---
lang: en
title: "2D Heat Treatment Wizard Lab2"
---

# Lab 2: 2D Heat Treatment Wizard

2.1. Introduction

2.2. Starting a New problem

2.3. Defining Process Settings

2.4. Loading Material definition

2.5. Defining Workpiece

2.5.1. Workpiece General Object

2.5.2. Import Geometry for workpiece

2.5.3. Assigning Material

2.5.4. Generate Mesh

2.5.5. Assigning Boundary conditions

2.5.6. Workpiece initialization

2.6. Medium Definition

2.7. Scheduled Definition

2.8. Simulation controls

2.9. Generate Database

2.10. Starting the Simulation

2.11. Post processing

## Introduction

The Heat Treatment Wizard is a convenient tool to set up complex multiple-operation heat treatment problem. This lab will demonstrate how to use this wizard to prepare a carburization-quench-tempering simulation of a steel part. This lab can also help users understand the capabilities of DEFORM-HT's phase transformation calculation scheme.

## Starting a New problem

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear.

  
Create a new problem either by selecting **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****New Problem** or by clicking the **New Problem** ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in Fig. 2DHTWL2.1. Select " **2D Heat Treat** " radio button and unit system as "**SI** " radio button in Units field. Define problem Name as ‘**Tempering** ’ and make sure the “Show option dialog” check box is turned on (if we do not turn on the “**Show option dialog** ” check box, then we will not get the New Project dialog in MO UI). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0001.jpg' | relative_url }})

Defining New Problem.

  
Multiple operation wizard will open with 2D HT operation as first operation as shown in Fig. 2DHTWL2.2.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0002.jpg' | relative_url }})

New project with 2D HT Operation.

## Defining Process Settings

As the multiple operation wizard opens, Process settings page will be displayed in property editor region as shown in Fig. 2DHTWL2.2. User can set the simulation mode based on the simulation requirement along with step definition controls. For this lab, we will turn on "**Deformation** ", "**Diffusion** " and "**Phase****Transformation** ". Step definition will be defined in Simulation controls page. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Material list page, as we do not need to make any changes in Initialization page.

## Loading material to Material list

In Material list page, click on ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Import material from file) and import material "**Demo_Temper_Steel.KEY** " from installation path \SFTC\DEFORM\v*_*\2d\LABS\HeatTreat directory (See Fig. 2DHTWL2.3.). Click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to material Selection popup dialog, we can observe that material has multiple phases defined and we can observe each phase material properties using ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button to navigate to respective phase. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Workpiece object page.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0003.jpg' | relative_url }})

Importing Material into Material list page.

## Defining Workpiece

### Workpiece general object definition

In Workpiece page, change the object type to **Elasto-plastic** type and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) (See Fig. 2DHTWL2.4.)

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0004.jpg' | relative_url }})

Workpiece general object definition.

### Importing Geometry for Workpiece

In Geometry page, click on ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (import geometry from library) option and import the “**TemperingPart.GEO** ” file from installation path \SFTC\DEFORM\v*_*\2d\LABS\HeatTreat as shown in Fig. 2DHTWL2.5. Use ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) action label to check the imported geometry. If they are any issues with the geometry then geometry will be corrected and message will be displayed as shown in Fig. 2DHTWL2.6. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Material page.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0005.jpg' | relative_url }})

Importing Geometry for Workpiece.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0006.jpg' | relative_url }})

Fixing geometry errors in imported geometry.

### Assigning Material to Workpiece

In Material page, select **Demo.Steel** from material list to assign the material to workpiece as shown in Fig. 2DHTWL2.7. Click ![]({{ '/assets/icons/pre_icons/mo_back_button.jpg' | relative_url }}) to Mesh page.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0009.jpg' | relative_url }})

Assigning Material to workpiece.

### Generating Mesh for Workpiece

In Mesh page, define Target number of mesh elements as **300**. We need to define structured mesh for better prediction of phase distribution and atom content on surface, hence click on ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) to toggle mesh settings into expert mode, select Coating mesh and add 2 layers of coating as shown in Fig. 2DHTWL2.9. Set "**Thickness mode** " to be "**ratio to object overall dimension** " and define **500** **microns** and **1000****microns** as thickness for layer 1 and 2 respectively as shown in See Fig. 2DHTWL2.9. , we will keep default selection of “**Demo.Ste****el** ” as material for coating. Click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). Mesh generated for Workpiece along with structured mesh looks like as shown in Fig. 2DHTWL2.9. Click on ![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }}) to toggle to guided mode. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Boundary condition page.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0007.jpg' | relative_url }})

Defining number of elements for Workpiece mesh.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0008.jpg' | relative_url }})

Coating mesh settings for Workpiece.

### Assigning Boundary conditions to Workpiece

In Boundary conditions page, we will fix nodes in Y direction on bottom edge of the Workpiece as shown in Fig. 2DHTWL2.10.. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Initialization page.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0010.jpg' | relative_url }})

Assigning Velocity BCC to Workpiece.

### Initializing Phase distribution and Atom percentage in Workpiece

In Initialization page, click on “**Microstructure** ” tab and define initial value of “**Pearlite+Bainite** ” as “1” in 3rd column as shown in Fig. 2DHTWL2.11. and then click on ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}) button to initialize the value for entire Workpiece.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0011.jpg' | relative_url }})

Initializing Phase volume fractions of Workpiece.

To initialize atom content, click on **Node****Data![]({{ '/assets/icons/pre_icons/mo_nodal_data_icon.jpg' | relative_url }}) **and select “**Diffusion** ” tab to initialize atom content value as shown in Fig. 2DHTWL2.12. Click on ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}), “Initialize Nodal data” pop-up will open, select “Range” and let range of nodes be default selection of all nodes at Start Node and End Node. Define “Value” as 0.2 and click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) button to initialize value, see Fig. 2DHTWL2.12. Click on ![]({{ '/assets/icons/pre_icons/mo_close_button2.jpg' | relative_url }}) to close the “Initialize Nodal data” and click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close Nodal data dialog. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define Medium details.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0012.jpg' | relative_url }})

Initializing Atom content for Workpiece.

## Medium Definition for heat treatment

In page “**Medium****details** ”, we will define various media and heat transfer zones associated with them,

  
1\. Rename the first medium to “**Furnace** ” and set the “**Default** ” heat transfer coefficient (HTC) to constant **0.1**. Turn on Radiation checkbox as shown in Fig. 2DHTWL2.13.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0013.jpg' | relative_url }})

Defining Furnace Medium.

2\. Add a medium “**Polymer********Solution** ”, turn off Radiation check box and set its "**Default** " zone HTC as a function of temperature. Define the function using ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) button as shown in Table.1. and Fig. 2DHTWL2.14.

Temperature  |  HTC  
---|---  
20 |  3.5  
400 |  8.5  
700 |  15  
900 |  5.2  
  
Polymer solution HTC function.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0014.jpg' | relative_url }})

Defining Polymer solution HTC function.

3\. Add a heat transfer zone to the “**Polymer********Solution** ” medium. Click on the workpiece boundary to specify this zone using the ![]({{ '/assets/icons/pre_icons/mo_bcc_start_and_end_ico.jpg' | relative_url }}) selection mode as shown in Fig. 2DHTWL2.15. Select HTC as a function of temperature and define the values of function using ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) button as shown in Table. 2. and Fig. 2DHTWL2.16.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0015.jpg' | relative_url }})

Defining Zone 1 of Polymer medium.

Temperature  |  HTC  
---|---  
20 |  3.5  
200 | 4.5  
400 |  8.8  
700 |  3.5  
900 |  2.8  
  
HTC function of Polymer solution medium Zone 1.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0016.jpg' | relative_url }})

Defining HTC function of Polymer solution medium Zone 1.

4\. For Zone1 of “Polymer Solution” medium, select the "Diffusion Surface Reaction Rate" as a function of temperature as shown in Table.3. Define the function as shown in Fig. 2DHTWL2.17. and Fig. 2DHTWL2.18.

Temperature  |  RRC  
---|---  
20 |  0.1  
500 | 0.2  
1000 |  0.6  
  
Diffusion Surface Reaction Rate function of Polymer solution medium Zone 1 

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0017.jpg' | relative_url }})

Setting Zone1 Radiation and Diffusion properties.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0018.jpg' | relative_url }})

Defining Surface Reaction Rate function of Polymer solution medium Zone 1

5\. Add one more media, rename it to “Air”. Define “Default” HTC as 0.02 and turn on Radiation checkbox as shown in Fig. 2DHTWL2.19. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to schedule Heat Treatment operations.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0019.jpg' | relative_url }})

Defining Air medium.

## Scheduling heat treatment operations

In this lab we are going to carry out a five stage Heat Treatment process. To do so, in “**Schedule** ” page, input a five-stage schedule as explained below.  
  
1\. One hour (3600 s) of furnace heating. The temperature of the furnace is specified as a function of time. This function can be input by clicking the corresponding "Define" cell in the "Advance" column (See Table.4., Fig. 2DHTWL2.20, Fig. 2DHTWL2.21\. and Fig. 2DHTWL2.22.).

Time(s) |  Temperature  
---|---  
0 |  20  
600 |  660  
1200 |  880  
3600 |  880  
  
Defining Furnace environment temperature function during Furnace heating operation.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0020.jpg' | relative_url }})

Heat Treatment Process scheduling.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0021.jpg' | relative_url }})

Defining Furnace heating window in Advance

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0022.jpg' | relative_url }})

Function definition detail window

2) Schedule second HT operation for10 minutes (600 s) of quenching in the polymer solution. Specify the "Atom" content to be 0.8 at 30C as shown in Fig. 2DHTWL2.23.

3) Schedule third HT operation of tempering as Furnace heating for 30 minutes (1800 s) at temperature 250C as shown in Fig. 2DHTWL2.23.

4) Schedule fourth HT operation of tempering as Furnace heating for 30 minutes (1800 s) at temperature 350C as shown in Fig. 2DHTWL2.23.

5) Schedule fourth HT operation of tempering as cooling in Air for One hour (3600 s) at 20C environment temperature as shown in Fig. 2DHTWL2.23. and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Step page.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0023.jpg' | relative_url }})

Heat Treatment operations schedule.

## Defining Simulation controls

In "**Step** " page, select **Auto** radio button and set "**Temp. Change per step** " to **5°** C, keep Minimum time per step as **0.001** sec and. Maximum time per step as **10** sec. Define **Step increment to save** as **10**. (See Fig. 2DHTWL2.24.)

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0024.jpg' | relative_url }})

Defining step controls for Heat Treatment simulation.

## Generate Database

Click on ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) action label to check for errors and warnings that need to be addressed before generating database. If there are no errors or warnings that would affect the simulation output, generate a database by clicking ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) action label, see Fig. 2DHTWL2.25. When the program is done writing the database, switch to ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) tab to run simulation.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0025.jpg' | relative_url }})

Generating Database

## Starting the Simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. 2DHTWL2.26. Use the default **Continue Run** option to select “**Continue from the last step** ” (from step -1) option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0026.jpg' | relative_url }})

Run simulation window

  
The progress of the simulation can be monitored as it is running by looking at the Simulation Message and process monitor in Simulation mode. Click the Simulation Message tab to view the Message file. As long as the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked, which is the default setting, the Message file will refresh every couple of seconds.  
  
The Message file provides information about which simulation step the simulation is currently on and gives information dealing with how well the simulation is running.  
When the simulation of all Heat Treatment operations is finished, the message will be added as shown in Fig. 2DHTWL2.27. to the end of the Message file.  
  
Each stage defined will be executed as individual operation and user need to wait until all the stages simulation is completed.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0027.jpg' | relative_url }})

Monitoring Heat Treatment Simulation progress.

## Post-Processing

When the simulation has finished, click on ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}). In Step Browser click on ![]({{ '/assets/icons/pre_icons/mo_all_button.jpg' | relative_url }}) button to view all steps. The temperature min-max history should look like the graph below (See Fig. 2DHTWL2.28.).

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0028.jpg' | relative_url }})

Temperature Min-Max history throughout Heat Treatment simulation.

Plot the Volume fraction of each phases at the end of all operations (See Fig. 2DHTWL2.29.).

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0029.jpg' | relative_url }})

Volume Fraction distribution at the end of all operations.

  
Plot Dominant atom from Diffusion and observe the Dominant Atom distribution at different stage of Tempering operation (See Fig. 2DHTWL2.30.).

![]({{ '/assets/images/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab2/image0030.jpg' | relative_url }})

Dominant atom distribution at the end of each operation.

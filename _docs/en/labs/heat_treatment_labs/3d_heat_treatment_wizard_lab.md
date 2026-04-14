---
lang: en
title: "3D Heat Treatment Wizard Lab"
---

# 3D Heat Treatment Wizard Lab

1.1. Introduction

1.2. Starting a New problem

1.3. Process Settings

1.4. Material definition

1.5. Workpiece Object Type

1.6. Workpiece initialization

1.7. Medium Definition

1.8. Scheduled Definition

1.9. Simulation controls

1.10. Generate Database

1.11. Starting the Simulation

1.12. Post processing

## Introduction

The Heat Treatment Wizard is a convenient tool to set up complex multiple-operation heat treatment problem. This lab will demonstrate how to use this wizard to prepare a carburization-quench-tempering simulation of a steel part. This lab can also help users understand the capabilities of DEFORM-HT's phase transformation calculation scheme.

## Starting a New problem

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear as shown in below (see Fig. 3DHTWL1.1.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0001.jpg' | relative_url }})

DEFORM GUI main window

Create a new problem either by selecting **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in Fig. 3DHTWL1.2. Select " **Integrated Manufacturing Process** " radio button and units system as "**SI** " using radio button. Define Problem Name as "**GearHT** " and make sure the “Show option dialog” check box is turned on (if we do not turn on the “**Show option dialog** ” check box, then we will not get the New Project dialog in MO UI). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image014.jpg' | relative_url }})

Problem type selection window

Integrated Manufacturing Process wizard will open (see Fig. 3DHTWL1.3.), at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title. In this lab we will use ‘**GearHT** ’ as the project name.

![]({{ '/assets/images/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/image0003.jpg' | relative_url }})

MO wizard New project

User can also change the Unit system (File menu selected unit system will be selected by default) and add HT operation by selecting it from First operation pull down list and checkbox (see Fig. 3DHTWL1.3.). Using copy Existing project option we can import previous saved projects as new project. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

Multiple Operation wizard will open. Add 3D HT Wizard operation from the Explorer Operations list. Add the operation by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button next to **3D HT Wizard** or user can also add by drag and drop into the Operation Editor (see Fig. 3DHTWL1.4.).

![]({{ '/assets/images/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/image0004.jpg' | relative_url }})

Added 3D HT Wizard into Operation Editor

## Process Settings

As the operation is added, Process settings page opens as shown in Fig. 3DHTWL1.4. User can set the simulation mode based on the simulation requirement along with step definition controls.

Turn on "**Deformation** ", "**Diffusion** ", and "**Phase****Transformation** ". Step definition will be defined in Simulation controls page. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) leave the settings in initialization page as it is (see Fig. 3DHTWL1.5.) and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/image0005.jpg' | relative_url }})

Initialization Setup window

## Material definition

In Material page, click on ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Import material from file) and import material "**Demo_Temper_Steel.KEY** " from installation path \SFTC\DEFORM\v*_*\3d\LABS directory (see Fig. 3DHTWL1.6.). Click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to material Selection popup dialog and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until workpiece object page.

![]({{ '/assets/images/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/image0006.jpg' | relative_url }})

Importing Material

## Workpiece Object Type

In Workpiece page, change the object type to **Elasto-plastic** type and select "**Mixed (Tet mesh)** " as element type for Elasto-plastic from drop - down menu (see in Fig. 3DHTWL1.7.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Geometry page.

**Note** : For almost all 3D heat treat models, (Tet Mesh) or brick mesh element should be used but not "Standard" tet.

![]({{ '/assets/images/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/image0007.jpg' | relative_url }})

Workpiece object page

### Import Geometry

In Geometry page, click on ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (import geometry from library) option and import the **GearTooth.STL** file from installation path \SFTC\DEFORM\v*_*\3d\LABS as shown in Fig. 3DHTWL1.8. Use ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) action label to check the Geometry. A perfect geometry should display message as shown in as shown in Fig. 3DHTWL1.9. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/image0008.jpg' | relative_url }})

Importing Geometry

![]({{ '/assets/images/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/image0009.jpg' | relative_url }})

Check Geometry

### Generate Mesh

In Mesh page, Enter Target number of mesh elements as **16000** or drag the slider bar to 16000 then click on![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) . Mesh is generated and meshed object looks as shown in Fig. 3DHTWL1.10. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/image0010.jpg' | relative_url }})

Generate Mesh Window

### Assigning Material

Select and assign **Demo.Steel** Material as shown in Fig. 3DHTWL1.11. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/image0011.jpg' | relative_url }})

Assigning Material to workpiece

### Assigning Boundary conditions

  1. Assign symmetry surfaces on two sides of workpiece as shown in Fig. 3DHTWL1.12. Note that this geometry represents half a tooth of the gear.

![]({{ '/assets/images/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/image0012.jpg' | relative_url }})

Assigning Symmetry BCC

  1. In addition, as Elasto-plastic deformation will be modeled, some fixed-node boundary conditions need to be specified here. To do so, select a boundary condition item and then assign it to appropriate boundary nodes. For this model, as the symmetric planes provide the constraints in the directions perpendicular to their own plane, we need constraints in the Z direction. Here, we fix a node on the bottom as shown in the Fig. 3DHTWL1.13.

![]({{ '/assets/images/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/image0013.jpg' | relative_url }})

Assigning Velocity BCC

## Workpiece initialization

Click on Object Nodes ![]({{ '/assets/icons/pre_icons/mo_nodal_data_icon.jpg' | relative_url }}) and select **diffusion** then define **atom****percentage** as **0.2** using ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}) button (see Fig. 3DHTWL1.14.), assign using **Range** option by defining **0.2** as value then click on ![]({{ '/assets/icons/pre_icons/mo_close_button2.jpg' | relative_url }}) button. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button to close the Initialization dialog and click to close Nodal data dialog.

![]({{ '/assets/images/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/image0014.jpg' | relative_url }})

Object Node data definition window

Click on Object Elements ![]({{ '/assets/icons/pre_icons/mo_elemental_data_icon.jpg' | relative_url }}) and select **Phase****transformation** tab under **Microstructure**. Initialize **Pearlite+Bainite** as **1** and zero for the rest by selecting each phase and using ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}) (see Fig. 3DHTWL1.15.), assign using Range option by defining 1 as value then click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) button. Click on ![]({{ '/assets/icons/pre_icons/mo_close_button2.jpg' | relative_url }}) button to close the Initialization dialog and click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close Element data dialog. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define the medium details.

![]({{ '/assets/images/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/image0015.jpg' | relative_url }})

Object Element Data definition window

## Medium Definition

In page “**Medium****details** ”, you will define various media and heat transfer zones associated with them as shown in Fig. 3DHTWL1.16.

![]({{ '/assets/images/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/image0016.jpg' | relative_url }})

Medium Details window

  1. Rename the first medium to “Heating Furnace” and set the “default” heat transfer coefficient (HTC) to constant 0.1. Activate Radiation by checking on Radiation button.

  2. Add medium “Carb. Furnace” (Carb. for Carburization). Set the “default” heat transfer coefficient (HTC) to constant 0.05. For “Carb. Furnace”, input 0.0001 for the "Diffusion Surface Reaction Rate". Activate Radiation by checking on Radiation button.

  3. Add a media “Oil”. Deactivate the "Radiation". Input 5.5 for the "default" HTC.

Add a heat transfer zone (Zone #1) to the media “Oil”. Click on the workpiece boundary to specify this zone to the bottom of the workpiece as shown in the Fig. 3DHTWL1.17. Note that you may need to change the picking modes in point selection window in order to specify the zone properly.

![]({{ '/assets/images/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/image0017.jpg' | relative_url }})

Medium detail window showing zone allocation

For Zone #1, define the HTC as a function of temperature as follows, by selecting f(Temp) from pull down menu and using ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) button, (see Fig. 3DHTWL1.18. and Fig. 3DHTWL1.19. )

**Temperature** |  **HTC**  
---|---  
20 |  2.1  
250 |  2.8  
500 |  6.8  
750 |  4.0  
1000 |  2.5  
  
HTC table

![]({{ '/assets/images/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/image0019.jpg' | relative_url }})

Function definition window

  1. Add one more media “Air”. Input 0.02 for the default HTC. Activate Radiation by checking on Radiation button.

## Scheduled Definition

In this lab we are going to carry out a five stage Heat Treatment process. In order to do this, in “Schedule” page, input a five-stage schedule as explained below.(See Fig. 3DHTWL1.20.)

  1. Half an hour (1800 s) of pre-heating at 550C.

  2. Two hours (7200 s) of carburization at 850C. Specify the "Atom" content to be 0.8.

  3. 20 minutes (1200 s) of oil quench with oil temperature 100C.

  4. 30 minutes (1800 s) of tempering at 280C.

  5. One hour (3600 s) cooling in the air.

![]({{ '/assets/images/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/image0020.jpg' | relative_url }})

Heat Treatment Schedule window

The settings for each stage can be set or modified using ![]({{ '/assets/icons/pre_icons/mo_define.._button.jpg' | relative_url }}) button in advanced column. User can start from any stage by setting the Start Operation number based on the stages defined. For this lab we will use 1. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Simulation controls page.

## Simulation controls

In "Step Definition", Select **Auto** radio button and change "Temp. Change per step" to **2** C. Accept other default settings. (See Fig. 3DHTWL1.21.)

![]({{ '/assets/images/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/image0021.jpg' | relative_url }})

Simulation controls window

## Generate Database

Click on ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) action label to check the problem. Generate a database by clicking ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) action label.

![]({{ '/assets/images/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/image0022.jpg' | relative_url }})

Generate Database Window

## Starting the Simulation

Once the database has been generated, switch to the Simulation mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the operation tree. Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. 3DHTWL1.23. Use the default **Continue Run** option to select “**Continue from the last step** ” (from step -1) option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

To define MPI settings, click on ![]({{ '/assets/icons/simulator_icons/mo_more_button.jpg' | relative_url }}) button, Run Options window will expand and displays options to define MPI settings for simulation (max number of processors that can be defined depend on your 3D MPI license).

![]({{ '/assets/images/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/image0023.jpg' | relative_url }})

Run simulation window

The progress of the simulation can be monitored as it is running by looking at the Simulation Message and process monitor in Simulation mode. Click the Simulation Message tab to view the Message file. As long as the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked, which is the default setting, the Message file will refresh every couple of seconds.

The Message file provides information about which simulation step the simulation is currently on and also gives information dealing with how well the simulation is running.

When the simulation has finished, the message will be added to the end of the Message file. (See Fig. 3DHTWL1.24.).

Each stage defined will be executed as individual operation and user need to wait until all the stages simulation is completed.

![]({{ '/assets/images/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/image0024.jpg' | relative_url }})

Simulation Message tab

## Post processing

When the simulation has finished, click on ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}). In Step Browser click on ![]({{ '/assets/icons/pre_icons/mo_all_button.jpg' | relative_url }}) button to view all steps. The temperature min-max history should be like the graph below (see Fig. 3DHTWL1.25.).

![]({{ '/assets/images/labs/heat_treatment_labs/3d_heat_treatment_wizard_lab/image0025.jpg' | relative_url }})

State Variable showing Temperature Min-Max history

In post-processing, we recommend following tasks to be performed:

  1. Examine the state of the workpiece after oil quenching. The state variables of interest may include carbon content, volume fractions of Martensite (M), Ferrite (F), and Perlite + Banite (PB), and the residual stress. Note that at this point, M is as high as 0.797 near tooth surface, and the maximum effective stress is ~128 MPa.

  2. Check the same state variables after tempering. Note that M is reduced to ~0.2 near tooth surface, most of which is transformed into Tempered Ferrite + Cementite (TFC). The maximum effective stress is reduced to ~82 MPa.

  3. In addition, point tracking phase volume fractions at different locations of the work-piece can be helpful for understanding the complex phenomena occurred.

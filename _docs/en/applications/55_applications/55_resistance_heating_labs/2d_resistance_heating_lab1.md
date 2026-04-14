---
lang: en
title: "2D Resistance Heating Lab1"
---

# 2D Resistance Heating Lab1

1.1. Problem Summary

1.2. Creating New problem

1.3. Adding 2D Forming operations

1.4. Geometry Type

1.5. Simulation Controls

1.6. Loading materials data

1.7. Adding Objects

1.8. Contact generation

1.9. Step controls

1.10. Generating Database

1.11. Starting the Simulation

1.12. Post processing

## Problem Summary

This example takes you through the basic steps to setup a simple resistance heating. Existing features of the user interface are referenced here which are constantly improved as we move to higher versions of Deform, to make the setup process more convenient and efficient to use.

This case is a 2d axis-symmetric case involving two plates, 4mm thick and two electrodes. Top plate has a diameter of 300mm, and bottom plate has diameter of 200mm (see Fig. 2DRHL1.1.). The two plates have different thermal electrical resistance properties and the electrodes are subjected to a voltage of 20 v, (grounded on one side, i.e zero voltage) to trigger local heating in the plates (see Fig. 2DRHL1.2.). Please note that the process data used in this example is for illustration purpose only. (3D images indicated here have been documented using 3D Viewer for this axisymmetric analysis).

Sample keyword file available in the release ‘Labs’ folder can be taken as the basis. Only the essential data needed for resistance heating are discussed here and this document assumes user is fairly conversant to the Deform Preprocessor.

![]({{ '/assets/images/applications/55_resistance_heating_labs/image0001.jpg' | relative_url }})

Location of the plates and electrodes

![]({{ '/assets/images/applications/55_resistance_heating_labs/image0002.jpg' | relative_url }})

Local heating due voltage across electrodes

## Creating New problem

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear, as shown below Fig. 2DRHL1.3.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

DEFORM GUI main 

Create a new problem either by selecting **File** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in Fig. 2DRHL1.3. Select "**Integrated Manufacturing Process** " radio button and unit system as "**SI** " radio button in unit field. Define Problem Name as **"Resistance_Heating_lab1"** and make sure the “**Show option dialog** ” check box is turned on (if we do not turn on the “Show option dialog” check box, then we will not get the New Project dialog). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/applications/55_2_arc_welding/image0002.jpg' | relative_url }})

Problem type selection window

Multiple operation wizard will open along with project naming window, defined problem name is updated as ‘**Resistance_Heating_lab1** ’ as the project name and selected unit system updated. Confirm that First operation check box is unchecked as we will add operation later and use the default (home) directory. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to add project.

![]({{ '/assets/images/applications/55_resistance_heating_labs/image0005.jpg' | relative_url }})

MO wizard new Project

## Adding Forming Operation

Multiple Operation wizard will open. Add 2D Forming operation from the Explorer Operations list. Add the operation by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button next to 2D Forming or user can also add by drag and drop into the Operation Editor. (see Fig. 2DRHL1.6.)

![]({{ '/assets/images/applications/55_resistance_heating_labs/image0006.jpg' | relative_url }})

Added 2D Forming operation into operation editor

## Geometry Type

In this lab we will be using Axisymmetric geometries, so select **2D Axisymmetric** radio button from geometry type page, then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). (see Fig. 2DRHL1.7.)

![]({{ '/assets/images/applications/55_resistance_heating_labs/image0007.jpg' | relative_url }})

2D Axisymmetric Geometry type selection

## Simulation Controls

In this lab we will be showing how to setup a resistance heating problem. So we will turn on the **Heating** under **Heat** **transfer** and we will select the **Resistance** in the heating**** pull down menu. Also we have to **turn****off** the **Deformation** check box. (see Fig. 2DRHL1.8.)

![]({{ '/assets/images/applications/55_resistance_heating_labs/image0008.jpg' | relative_url }})

Simulation control window

## Loading materials data

In this lab, we will import the material data from keyfiles. Click on ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Import material data from a file) button and import ‘**New****Material1.key** ’ file from '2D\LABS\Resistance_Heatting' directory. Select "New Material1" in Material selection popup and click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button (See Fig. 2DRHL1.9.). In material list , "New Material1" material will be added as shown in Fig. 2DRHL1.9. Similarly, import material from '**New Material2.key** ' and '**New Material3.key** ' files. After importing the material data from keyfile, Material list will be displayed as shown in Fig. 2DRHL1.9.

Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to go New Material1 Property page, check the Elastic Properties (See Fig. 2DRHL1.10.), Thermal Properties (see  Fig. 2DRHL1.11. ) and Electrical Properties (see Fig. 2DRHL1.12. ). Similarly, check the Elastic properties, Thermal Properties and Elec./Mag. Properties of New Material2 and New Material3 keyfiles. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Object page.

![]({{ '/assets/images/applications/55_resistance_heating_labs/image0009.jpg' | relative_url }})

Importing New Materials

![]({{ '/assets/images/applications/55_resistance_heating_labs/image0010.jpg' | relative_url }})

Elastic Properties of New Material 1 

![]({{ '/assets/images/applications/55_resistance_heating_labs/image0011.jpg' | relative_url }})

Thermal Properties of New Material 1 

![]({{ '/assets/images/applications/55_resistance_heating_labs/image0012.jpg' | relative_url }})

Electrical resisitivity of New Material 1 

## Adding Objects

For this operation we required four objects, for two plates and two electrodes hence in Object window add four objects using ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) button (see Fig. 2DRHL1.13.), then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/applications/55_resistance_heating_labs/image0013.jpg' | relative_url }})

Adding Object Window

### Plate1

In Workpiece window, change the Object name to **Plate1** and select Object type as **Elastic** as shown in Fig. 2DRHL1.14., Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/applications/55_resistance_heating_labs/image0014.jpg' | relative_url }})

Plate1 object window

#### Import Geometry

In Geometry page, click on ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) ( Load Geometry from Library) button and import ‘**resistance_heat_bottom_plate.****GEO** ’ as shown in Fig. 2DRHL1.15. The geometry for Plate1 is located in DEFORM installation folder 2D\LABS\Resistance_Heatting directory.

![]({{ '/assets/images/applications/55_resistance_heating_labs/image0015.jpg' | relative_url }})

Geometry importing

#### Generate Mesh

Generate the mesh using **400** elements (see Fig. 2DRHL1.16.). Complete range of meshing options are also available in expert mode (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})), if user needs to have more control on the mesh generated. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/applications/55_resistance_heating_labs/image0016.jpg' | relative_url }})

Plate1 Mesh generation

#### Assigning Material

To assign the material for the Plate 1 select the **New****Material3** from the material window. This can be done as shown in Fig. 2DRHL1.17. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/applications/55_resistance_heating_labs/image0017.jpg' | relative_url }})

Object material selection window

#### Boundary conditions

In BCC page, check the default assigned Heat exchange with Environment BCC to the entire outer surface of the plate (which does not include the centerline since these nodes are inside the object) by clicking on Defined under Heat exchange with Environment. Default BCC are assigned automatically due to selection of problem type as axisymmetric (see Fig. 2DRHL1.18.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top Die page.

![]({{ '/assets/images/applications/55_resistance_heating_labs/image0018.jpg' | relative_url }})

Boundary conditions window

### Plate2

In Top die window, change the Object Name to **Plate2** and select Object type as **Elastic**. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to geometry page.

#### Import geometry

Similar to the plate1, in Geometry page, click on ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) ( Load Geometry from Library) button and import ‘**resistance_heat_top_plate.****GEO** ’. The geometry for Plate2 is located in DEFORM installation folder 2D\LABS\Resistance_Heatting directory.

#### Mesh Generation

In mesh generation page, generate the mesh for the plate2 with the **400** elements. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to material page.

#### Assigning Material

To assign the material for the Plate2 select the **New Material2** from the material window. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

#### Boundary conditions

In BCC page, check the default assigned Heat exchange with Environment BCC to the entire outer surface of the plate (which does not include the centerline since these nodes are inside the object) by clicking on Defined under Heat exchange with Environment. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until bottom Die page.

### Electrode1

In Bottom die window, change the Object name to **Electrode1** and select Object type as **Elastic**. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

#### Import geometry

Similar to the plate1, in Geometry page, click on ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) ( Load Geometry from Library) button and import ‘**resistance_heat_bottom_electrode.****GEO** ’. The geometry for Electrode1 is located in DEFORM installation folder 2D\LABS\Resistance_Heatting directory.

#### Mesh Generation

In mesh generation page, generate the mesh for the Electrode1 with the **400** elements. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to assign material.

#### Assigning Material

To assign the material for the Electrode1 select the **New** **Material1** from the material window. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

#### Boundary conditions

In BCC page, We need to apply specified edge Voltage BCC for the bottom face, so select the **Voltage****BCC** branch under Heating BCC type, select bottom left corner of the object as start point and bottom right corner of the object as the end point. Nodes/edge will be highlighted. Then input the **Voltage** value of **0** **v** , and click on ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) icon to confirm the selection and apply these boundary conditions. (see Fig. 2DRHL1.19.)

We need to apply specified edge fixed temperature BCC's for the bottom face, so select the Temperature BCC branch under Thermal BCC type, select bottom left corner of the object as start point and bottom right corner of the object as the end point. Nodes/edge will be highlighted. Then input the **Temperature** value as **20 C** and click on ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) icon to confirm the selection and apply these boundary conditions. (see Fig. 2DRHL1.20.) For remaining surface of the object (excluding the axis side) we define ‘Heat Exchange with Environment’ following the same procedures of boundary node selection and BCC application. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until object4 page.

![]({{ '/assets/images/applications/55_resistance_heating_labs/image0019.jpg' | relative_url }})

Defining Voltage BCC

![]({{ '/assets/images/applications/55_resistance_heating_labs/image0020.jpg' | relative_url }})

Defining temperature BCC

![]({{ '/assets/images/applications/55_resistance_heating_labs/image0021.jpg' | relative_url }})

Defining Heat exchange with environment BCC

### Electrode2

In object4 window, change the Object name to **Electrode2** and select Object type as **Elastic**.Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to geometry page.

#### Import geometry

Similar to the plate1, in Geometry page, click on ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) ( Load Geometry from Library) button and import ‘**resistance_heat_top_electrode.****GEO** ’. The geometry for Electrode2 is located in DEFORM installation folder 2D\LABS\Resistance_Heatting directory.

#### Mesh Generation

Similar to the Plate1, in mesh generation page, generate the mesh for the Electrode1 with the **400** elements. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to material page.

#### Assigning Material

To assign the material for the Electrode1 select the **New Material1** from the material window. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

#### Boundary conditions

In BCC page, We need to apply specified edge current flux BCC(ECCRHT=3) for the top face, so select the Current Flux BCC branch under Heating BCC type, select top right corner of the object as start point and top left corner of the object as the end point. Nodes/edge will be highlighted. Then input the **Voltage** value of **20** **v** and click on ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) icon to confirm the selection and apply these boundary conditions. (See Fig. 2DRHL1.22.)

We need to apply specified edge fixed temperature BCC's for the top face, so select the Temperature BCC branch under Thermal BCC type, select top right corner of the object as start point and top left corner of the object as the end point. Nodes/edge will be highlighted. Then input the **Temperature** value as **20C** and click on ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) icon to confirm the selection and apply these boundary conditions. (see Fig. 2DRHL1.23.) Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until contact page. For remaining surface of the object (excluding the axis side) we define ‘Heat Exchange with Environment’ following the same procedures of boundary node selection and BCC application. (See Fig. 2DRHL1.24.)

![]({{ '/assets/images/applications/55_resistance_heating_labs/image0022.jpg' | relative_url }})

Voltage BCC definition

![]({{ '/assets/images/applications/55_resistance_heating_labs/image0023.jpg' | relative_url }})

Temperature BCC Definition

![]({{ '/assets/images/applications/55_resistance_heating_labs/image0024.jpg' | relative_url }})

Defining Heat exchange with environment BCC

## Contact generation

In contact page, add (![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }})) three relation sets. (See Fig. 2DRHL1.25.) Set the bottom plate as master, top plate as slave for the first set, complete the second and third sets with electrodes as masters and plates as slaves. (eg. bottom electrode as master and bottom plate as slave). For the first set of objects specify **0.002** as **interface****heat****transfer****coefficient**(click on ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **thermal**) and **40** as the **interface****resistivity** value (click on ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ‘**Heating** ’), (see Fig. 2DRHL1.26. and Fig. 2DRHL1.27.).

For second and third relation define **0.002** as **interface****heat****transfer****coefficient**(click on ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }})![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**T****hermal**) and **40** as the interface **resistivity** value (click on ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})‘**Heating** ’). Click on ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) to define the contact tolerance and click on ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) button to generate the contact. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until step controls page.

![]({{ '/assets/images/applications/55_resistance_heating_labs/image0025.jpg' | relative_url }})

Contact generation window

![]({{ '/assets/images/applications/55_resistance_heating_labs/image0026.jpg' | relative_url }})

Setting Inter object Heat Transfer coefficient data

![]({{ '/assets/images/applications/55_resistance_heating_labs/image0027.jpg' | relative_url }})

Setting Inter-object Interface resistivity data

## Step controls

Select **Number** **of****simulation****steps** as **100** , and **Step** **increment****to** **save** as **10** , with an equal **time****increment** as **0.05** sec (see Fig. 2DRHL1.28.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/applications/55_resistance_heating_labs/image0028.jpg' | relative_url }})

Step controls window

## Generating Database

Click on ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) action label to check the problem. Generate a database by clicking ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) action label.

Once the database has been generated switch to the Simulation mode by selecting the ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the object tree.

## Starting the Simulation

Once the database has been generated switch to the Simulation mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the operation tree. Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. 2DRHL1.29. Use the default **Continue****Run** option to select “**Continue****from the last step** ” (from step -1) option and then select the Simulation mode as **Interactive** radio button **** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/applications/55_resistance_heating_labs/image0029.jpg' | relative_url }})

Run simulation window

The progress of the simulation can be monitored as it is running by looking at the Simulation Message and process monitor in Simulation mode. Click the Simulation Message tab to view the Message file. As long as the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked, which is the default setting, the Message file will refresh every couple of seconds.

The Message file provides information about which simulation step the simulation is currently on and also gives information dealing with how well the simulation is running.

When the simulation has finished, the message will be added to the end of the Message file.(See Fig. 2DRHL1.30.).

![]({{ '/assets/images/applications/55_resistance_heating_labs/image0030.jpg' | relative_url }})

Simulation tab

## Post processing

When the simulation has finished, click on ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}). In Step Browser click on ![]({{ '/assets/icons/pre_icons/mo_all_button.jpg' | relative_url }}) button to view all steps. Plot the Temperature, Voltage and Elemental current Flux state variables to see the model results of current flux, Temperature distribution and Voltage.

![]({{ '/assets/images/applications/55_resistance_heating_labs/image0031.jpg' | relative_url }})

Elemental Current Flux state variable

![]({{ '/assets/images/applications/55_resistance_heating_labs/image0032.jpg' | relative_url }})

Voltage state variable

![]({{ '/assets/images/applications/55_resistance_heating_labs/image0033.jpg' | relative_url }})

Temperature Distribution in the Plates

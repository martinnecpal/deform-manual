---
lang: en
title: "3D Rayleigh-Benard convection Lab"
---

# 3D Rayleigh-Benard convection Lab

This lab will demonstrate how to use MO to prepare a flow and heat transfer simulation of the developing of the Rayleigh-Benard phenomena.

1.1. Creating a New problem

1.2. Adding 3D Forming operation

1.3. Simulation controls

1.4. Add new material ‘Water'

1.5. Define object

1.5.1. Workpiece Page

1.5.2. Create Geometry

1.5.3. Mesh the Object

1.5.4. Assign Material

1.5.5. Define thermal BCC

1.5.6. Object properties

1.6. Step page

1.7. Generate Database

1.8. Run Simulation

1.9. Post-Processing

## Creating a New problem

On a Windows machine, go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select DEFORM GUI Main v1x.xx. from the menu. The **DEFORM GUI Main** window will appear.

Create a new problem either by selecting **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in Fig. 3DRBL.1. Select " Integrated Manufacturing Process" radio button and units system as "**SI** " radio button in units field. Define Problem Name as "******3D_Rayleigh_Benard******" and and make sure the “Show option dialog” check box is turned on (if we do not turn on the “**Show option dialog** ” check box, then we will not get the New Project dialog in MO UI). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_rayleigh_benard_convection_lab/image0001.jpg' | relative_url }})

Problem type selection window

Multiple operation wizard will open with the New Project dialog, at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session we use ‘**3D_Rayleigh_Benard** ’ as the project name. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

## Adding 3D Forming operation

Add one 3D Forming operation from the Explorer Operations list. Operation can be added by clicking on 3D Forming operation ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button or user can also add by drag and drop into the Operation Editor (see Fig. 3DRBL.2.).

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_rayleigh_benard_convection_lab/image0002.jpg' | relative_url }})

Adding 3D Forming Operation

## Simulation controls

Turn ON ‘**Heat transfer** ’ and ‘**CFD****flow** ’ options and uncheck ‘**Deformation** ’ as shown in Fig. 3DRBL.3., then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_rayleigh_benard_convection_lab/image0003.jpg' | relative_url }})

Simulation controls page

## Add new material ‘Water’

On ‘**Material****list** ’ page, click on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) to add a new material. Double click on the new material name tag, change the material’s name to ‘**Water** ’ (see Fig. 3DRBL.4.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to material page to edit the material parameters.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_rayleigh_benard_convection_lab/image0004.jpg' | relative_url }})

Material List page

First, click on ‘**Elastic** ’ tag, then type the following values as shown on Fig. 3DRBL.5. for elastic parameters.  

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_rayleigh_benard_convection_lab/image0005.jpg' | relative_url }})

Elastic Material page 

Click on ‘**Thermal** ’ tag, then type the values as shown on Fig. 3DRBL.6. for thermal/flow material data.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_rayleigh_benard_convection_lab/image0006.jpg' | relative_url }})

Thermal Material page 

## Define object

This lab only needs one object, so on ‘**Object** ’ list page, removes all objects except ‘**Workpiece** ’ (see Fig. 3DRBL.7.), then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_rayleigh_benard_convection_lab/image0007.jpg' | relative_url }})

Object list page

### Workpiece Page

Choose ‘**Environment - Fluid(CFD)’** as object type with Object temperature as 20°C as shown in Fig. 3DRBL.8. Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_rayleigh_benard_convection_lab/image0008.jpg' | relative_url }})

Workpiece page

### Create Geometry

On '**Geometry** ' page, click on 'Define primitive', on the following page choose '**Box** ', and give 60 as width, 10 as height and 10 as length, see Fig. 3DRBL.9., the object geometry is also previewed at the central graphic window area.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_rayleigh_benard_convection_lab/image0009.jpg' | relative_url }})

Geometry primitive to create the part

  
Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button to accept all the changes, and it will come back to the 'Geometry' definition, click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Mesh page.

### Mesh the Object

Click on Expert mode ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}), select ‘**Brick mesh** ’ then click ‘**2D Cross Section** ’, see Fig. 3DRBL.10.

Put **381** in '**Target number of elements** ', check ‘**Mapped mesh generation** ’ and type **3** in ‘**Thickness elements** ’.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_rayleigh_benard_convection_lab/image0010.jpg' | relative_url }})

2D Cross Section

Click ‘**General** ’, input**24** in ‘**Uniform thick #of layers** ’. Then click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). Click ‘**No** ’ on the pop-up window. 

The mouse icon on the screen turns to busy and then back to normal, which indicating the mesh has been generated, the results are also plotted on the central graphic area, see Fig. 3DRBL.11.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_rayleigh_benard_convection_lab/image0011.jpg' | relative_url }})

Mesh generation

click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) go to the 'Material' page.

### Assign Material

In the object 'Material' selection page, Fig. 3DRBL.12., it shows the material name that has been added to the project. Select '**water** ' for the workpiece, then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to accept it.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_rayleigh_benard_convection_lab/image0012.jpg' | relative_url }})

Material assignment page

### Define thermal BCC

For this lab, only the temperature BCC needs to be specified on top and bottom surface respectively as shown in Fig. 3DRBL.13. and Fig. 3DRBL.14.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_rayleigh_benard_convection_lab/image0013.jpg' | relative_url }})

Bottom surface set to 20.5 Temperature BCC

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_rayleigh_benard_convection_lab/image0014.jpg' | relative_url }})

Top surface set to 20 Temperature BCC

#### Define Wall BCC

The top, bottom and two X surfaces need to be fixed all directions for this simulation as shown in Fig. 3DRBL.15. and Fig. 3DRBL.16.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_rayleigh_benard_convection_lab/image0015.jpg' | relative_url }})

Add Wall BCC in All directions

Fixed two Y surfaces in Y direction, click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Properties page.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_rayleigh_benard_convection_lab/image0016.jpg' | relative_url }})

Add Wall BCC on Y fixed surfaces

### Enable Gravity 

Gravity is needed for this lab, on ‘**Property** ’ page, click on ‘**Body forces** ’, and check ‘**Enable gravity’**. Then type **9820** , and choose ‘**-Z** ’ as direction. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until ‘Step’ page, to define Step control. 

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_rayleigh_benard_convection_lab/image0017.jpg' | relative_url }})

Wall BCC assignment 

## Step Control

Click on Guided mode ![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }}), enter **Number of steps** as **200** , and ‘**Time** ’ of step increment as **2** as shown in Fig. 3DRBL.18.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_rayleigh_benard_convection_lab/image0018.jpg' | relative_url }})

Step control page

Click on **Expert** mode ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}), Under Solver setting - Thermal tab select **MUMPS** solver as shown in Fig. 3DLFL.19. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Generate DB page.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_rayleigh_benard_convection_lab/image0019.jpg' | relative_url }})

Thermal solver selection page 

## Generate Database

Click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), database has been successfully generated.

## Run Simulation

Once the database has been generated, switch to the Simulation mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the operation tree. Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. 3DRBL.20. Use the default **Continue Run** option to select “**Continue from the last step** ” (from step -1) option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_rayleigh_benard_convection_lab/image0024.jpg' | relative_url }})

Run Simulation

## Post-Processing

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_rayleigh_benard_convection_lab/image0021.jpg' | relative_url }})

Velocity profile 

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_rayleigh_benard_convection_lab/image0022.jpg' | relative_url }})

Temperature profile 

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_rayleigh_benard_convection_lab/image0023.jpg' | relative_url }})

Pressure profile

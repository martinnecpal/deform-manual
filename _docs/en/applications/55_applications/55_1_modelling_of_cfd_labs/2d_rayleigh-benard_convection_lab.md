---
lang: en
title: "2D Rayleigh-Benard convection Lab"
---

# 2D Rayleigh-Bernard convection Lab

This lab will demonstrate how to use MO to prepare a flow and heat transfer simulation of the developing of the Rayleigh-Benard phenomena.

1.1. Creating a New problem

1.2. Adding 2D Forming operation

1.3. Geometry type

1.4. Simulation controls

1.5. Add new material ‘Water'

1.6. Define object

1.6.1. Workpiece Page

1.6.2. Create Geometry

1.6.3. Mesh the Object

1.6.4. Assign Material

1.6.5. Define thermal BCC

1.6.6. Object properties

1.7. Step page

1.8. Generate Database

1.9. Run Simulation

1.10. Post-Processing

## Creating a New problem

On a Windows machine, go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select DEFORM GUI Main vx.x. from the menu. The **DEFORM GUI Main** window will appear.

Create a new problem either by selecting **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in Fig. 2DRBCL.1. Select " Integrated Manufacturing Process" radio button and units system as "**SI** " radio button in units field. Define Problem Name as "**2D****_****Rayleigh_Benard** " and make sure the “Show option dialog” check box is turned on (if we do not turn on the “**Show option dialog** ” check box, then we will not get the New Project dialog in MO UI). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_rayleigh-benard_convection_lab/image0001.jpg' | relative_url }})

Problem type selection window

Multiple operation wizard will open with the New Project dialog, at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session we use ‘******2D****_****Rayleigh_Benard******’ as the project name. Click on![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

## Adding 2D Forming operation

Add one 2D Forming operation from the Explorer Operations list. Operation can be added by clicking on 2D Forming operation ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button or user can also add by drag and drop into the Operation Editor (See Fig. 2DRBCL.2.).

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_rayleigh-benard_convection_lab/image0002.jpg' | relative_url }})

Adding 2D Forming Operation

##  Geometry type

Choose '**2D Plane strain** ' on ‘**Geometry type** ’ for this problem, see Fig. 2DRBCL.3. Then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }})

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_rayleigh-benard_convection_lab/image0003.jpg' | relative_url }})

Geometry type page

## Simulation controls

Turn ON ‘**Heat transfer** ’ and ‘**CFD****flow** ’ options and uncheck ‘**Deformation** ’ as shown in Fig. 2DRBCL.4. then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_rayleigh-benard_convection_lab/image0004.jpg' | relative_url }})

Simulation controls page

## Add new material ‘Water'

On ‘**Material****list** ’ page, click on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) to add a new material. Double click on the new material name tag, change the material’s name to ‘**Water** ’ (See Fig. 2DRBCL.5.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to material page to edit the material parameters.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_rayleigh-benard_convection_lab/image0005.jpg' | relative_url }})

Material List page

First, click on ‘**Elastic** ’ tag, then type the following values as shown in Fig. 2DRBCL.6. for elastic parameters.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_rayleigh-benard_convection_lab/image0006.jpg' | relative_url }})

Elastic Material page 

Click on ‘**Thermal** ’ tag, then type the values as shown in Fig. 2DRBCL.7. for thermal/flow material data.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_rayleigh-benard_convection_lab/image0007.jpg' | relative_url }})

Thermal Material page 

## Define object

This lab only needs one object, so on ‘**Object** ’ list page, removes all objects except ‘**Workpiece** ’ (see Fig. 2DRBCL.8.), then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_rayleigh-benard_convection_lab/image0008.jpg' | relative_url }})

Object list page

### Workpiece Page

Choose ‘**Environment - Fluid(CFD)** ’ as object type with Object temperature as 20°C as shown in Fig. 2DRBCL.9. Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_rayleigh-benard_convection_lab/image0009.jpg' | relative_url }})

Workpiece page

### Create Geometry

On '**Geometry** ' page, click on ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}), on the following page choose '**Bar** ', and give 60 as width, and 10 as height, Origin X: as **0** and Y: as **0** as shown in Fig. 2DRBCL.10., the object geometry is also previewed at the central graphic window area. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button to accept all the changes, and it will come back to the 'Geometry' definition, click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to the 'Mesh' page.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_rayleigh-benard_convection_lab/image0010.jpg' | relative_url }})

Geometry primitive to create the part

### Mesh the Object

Click on Expert mode ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}), Put **3000** in 'Number of Elements', check ‘Mapped mesh generation’ check box and type **24** in ‘Thickness element’ then click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). The mouse icon on the screen turns to busy and then back to normal, which indicating the mesh has been generated, the results are also plotted on the central graphic area, see Fig. 2DRBCL.11. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) go to the '**Material** ' page.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_rayleigh-benard_convection_lab/image0011.jpg' | relative_url }})

Mesh generation

### Assign Material

In object 'Material' selection page, (see Fig. 2DRBCL.12.) it shows the material name that has been added to the project. Select '**Water** ' for the workpiece, then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to BCC page.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_rayleigh-benard_convection_lab/image0012.jpg' | relative_url }})

Material assignment page

### Define thermal BCC

For this lab, only the temperature bcc needs to be specified on top and bottom surface respectively. So, delete the default assigned 'Heat Exchange with environment ' BCC and then assign Temperature BCC for Bottom surface with 20.5 as shown in Fig. 2DRBCL.13. and for Top surface with 20 as shown in Fig. 2DRBCL.14.

  
![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_rayleigh-benard_convection_lab/image0013.jpg' | relative_url }})

Temperature BCC assigned for Bottom surface with 20.5C

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_rayleigh-benard_convection_lab/image0014.jpg' | relative_url }})

Temperature BCC assigned for Top surface with 20C

**Define Wall BCC**

****The entire surface needs to be fixed all directions for this simulation. Assign Velocity BCC for all surface in all directions as shown in Fig. 2DRBCL.15. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Object properties to enable gravity. 

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_rayleigh-benard_convection_lab/image0015.jpg' | relative_url }})

Assigned Velocity BCC for all surface in all directions

### Object properties

Gravity is needed for this lab, on ‘**Property** ’ page, click on ‘**Body****forces** ’, and check ‘**Enable****gravity** ’ check box. Then type **9820** , and choose ‘**-Y** ’ as direction as shown in Fig. 2DRBCL.16. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until ‘**Step** ’ page, to define simulation control. 

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_rayleigh-benard_convection_lab/image0016.jpg' | relative_url }})

Wall BCC assignment 

## Step page

Click on Guided mode ![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }}), enter Number of steps as 200, and ‘Time’ of step increment as 2. (see Fig. 2DRBCL.17.)

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_rayleigh-benard_convection_lab/image0017.jpg' | relative_url }})

Step page

## Generate Database

On 'Generate DB' page, click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), database has been successfully generated.

## Run Simulation

Once the database has been generated, switch to the Simulation mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the operation tree. Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. 2DRBCL.18. Use the default **Continue Run** option to select “**Continue from the last step** ” (from step -1) option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_rayleigh-benard_convection_lab/image0018.jpg' | relative_url }})

Run Simulation

## Post-Processing

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_rayleigh-benard_convection_lab/image0019.jpg' | relative_url }})

Velocity profile at last step

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_rayleigh-benard_convection_lab/image0020.jpg' | relative_url }})

Temperature profile at last step

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_rayleigh-benard_convection_lab/image0021.jpg' | relative_url }})

Pressure profile at last step

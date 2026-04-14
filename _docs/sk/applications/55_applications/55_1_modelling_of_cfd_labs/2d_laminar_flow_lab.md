---
lang: sk
title: "2D Laminar Flow Lab"
---

# 2D Laminar Flow Lab

This lab will demonstrate how to use MO to prepare a simulation of laminar flow around a cylinder.

1.1. Creating a New problem

1.2. Adding 2D Forming operation

1.3. Geometry type

1.4. Simulation controls

1.5. Add new material ‘Ideal fluid’

1.6. Define object

1.6.1. Import Object

1.6.2. Assign Material

1.6.3. Review BCC

1.7. Step page

1.8. Generate Database

1.9. Run Simulation

1.10. Post-Processing

## Creating a New problem

On a Windows machine, go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select DEFORM GUI Main v1x.x. from the menu. The **DEFORM GUI Main** window will appear.

Create a new problem either by selecting **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in Fig. 2DLFL.1. Select " Integrated Manufacturing Process" radio button and units system as "**SI** " radio button in units field. Define Problem Name as "**2D****_****Laminar_Flow** " and make sure the “Show option dialog” check box is turned on (if we do not turn on the “**Show option dialog** ” check box, then we will not get the New Project dialog in MO UI). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_laminar_flow_lab/image0001.jpg' | relative_url }})

Problem type selection window

Multiple operation wizard will open, at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session we use ‘**2D_****Laminar_Flow** ’ as the project name. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

## Adding 2D Forming operation

Add one 2D Forming operation from the Explorer Operations list. Operation can be added by clicking on 2D Forming operation ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button or user can also add by drag and drop into the Operation Editor (See Fig. 2DLFL.2.).

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_laminar_flow_lab/image0002.jpg' | relative_url }})

Adding 2D Forming Operation

## Geometry type

Choose '**2D Plane strain** ' on ‘**Geometry type** ’ for this problem, see Fig. 2DLFL.3. Then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).  

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_laminar_flow_lab/image0003.jpg' | relative_url }})

Geometry type page

## Simulation controls

Turn ON ‘**Heat****transfer** ’ and ‘**CFD flow** ’ options and uncheck ‘**Deformation** ’ as shown in Fig. 2DLFL.4., then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_laminar_flow_lab/image0004.jpg' | relative_url }})

Simulation controls page

## Add new material ‘Ideal fluid’

On ‘Material list’ page, click on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) to add a new material. Double click on the new material name tag, change the material’s name to ‘**Ideal fluid** ’ (See Fig. 2DLFL.5.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to material page to edit the material parameters.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_laminar_flow_lab/image0005.jpg' | relative_url }})

Material List page

Click on ‘**Elastic** ’ tab, then type the **Young's modulus** value as**1** as shown in Fig. 2DLFL.6. for elastic material data. 

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_laminar_flow_lab/image0006.jpg' | relative_url }})

Material page, Elastic data

Click on ‘**Thermal** ’ tab, then type the values as shown on Fig. 2DLFL.7. for thermal/flow material data. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Object page.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_laminar_flow_lab/image0007.jpg' | relative_url }})

Material page, thermal data

## Define object

This lab only needs one object, so on ‘**Object** ’ list page, removes all objects except ‘Workpiece’ (see Fig. 2DLFL.8.), then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_laminar_flow_lab/image0008.jpg' | relative_url }})

Object list page

### Import Object

In ‘Workpiece’ page, click on ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) ‘Import Object from a file’ then choose ‘**Flow_cylinder.KEY** ’ from DEFORM installation folder \2D\LABS\ directory folder an select object "**Workpiece** " in object selection page to import. (See Fig. 2DLFL.9.) 

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_laminar_flow_lab/image0009.jpg' | relative_url }})

Import Object

Choose ‘**Environment - Fluid(CFD)** ’ as object type with Object temperature as 200C as shown in Fig. 2DLFL.10. and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Mesh page.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_laminar_flow_lab/image0010.jpg' | relative_url }})

Workpiece Object page

Observe the imported object mesh (See Fig. 2DLFL.11.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to 'Material' page.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_laminar_flow_lab/image0011.jpg' | relative_url }})

View imported Mesh

### Assign Material

In object 'Material' selection page ( Fig. 2DLFL.12.), it shows the material name that has been added to the project. Select '**Idea fluid** ' for the workpiece, then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to accept it.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_laminar_flow_lab/image0012.jpg' | relative_url }})

Material assignment page

### Review BCC

The boundary conditions used in this simulation are shown as below Fig. 2DLFL.13.

  
![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_laminar_flow_lab/image0013.jpg' | relative_url }})

Boundary conditions 

These boundary conditions are already defined in the imported object, see Fig. 2DLFL.14. and Fig. 2DLFL.15. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until ‘Step’ page, to define simulation control. 

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_laminar_flow_lab/image0014.jpg' | relative_url }})

Defined BCC 

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_laminar_flow_lab/image0015.jpg' | relative_url }})

Defined Inlet/Outlet BCC

## Step page

In 'Step' page define the Number of steps as **200** and ‘**Time** ’ of step increment as **0.04** (see Fig. 2DLFL.16.). We need to set "Time integration factor" value under "Constant" tab as 1.0 in Process Conditions. To enable Constant tab, User Type should be of "**Advanced** ". So, under Options ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Environment ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) User Type, select "**Advanced** " as shown in Fig. 2DLFL.17. Now, switch to Expert mode (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})) and under Process conditions ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Constant tab, define "**Time integration factor** " as 1 as shown in Fig. 2DLFL.18. Switch to Solver settings tab and select the Iteration method as “**Direct****iteration** ” as shown in Fig. 2DLFL.19. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Generate DB page. 

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_laminar_flow_lab/image0016.jpg' | relative_url }})

Step controls page

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_laminar_flow_lab/image0017.jpg' | relative_url }})

Environment settings-User type selection option

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_laminar_flow_lab/image0018.jpg' | relative_url }})

Time integration factor data 

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_laminar_flow_lab/image0019.jpg' | relative_url }})

Direct iteration method 

## Generate Database

On 'Generate DB' page, click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}), database has been successfully generated.

## Run Simulation

Once the database has been generated, switch to the Simulation mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the operation tree. Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. 2DLFL.20. Use the default **Continue Run** option to select “**Continue from the last step** ” (from step -1) option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_laminar_flow_lab/image0020.jpg' | relative_url }})

Run Simulation

## Post-Processing

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_laminar_flow_lab/image0021.jpg' | relative_url }})

Velocity profile

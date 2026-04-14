---
lang: sk
title: "2D Turbulent Flow Lab"
---

# 2D Turbulent Flow Lab **– flow over a backward-facing step**

Flow over a backward-facing step (BFS) is a common phenomenon in practical engineering, such as the internal flows in diffusers, turbines, combustors, or pipes, and external flows over aircrafts, around buildings, or over stepped channels. These flows are characterized by flow separation and reattachment induced by sharp expansion of the configuration. 

This lab will demonstrate how to setup a 2D turbulence flow simulation using the backstep example. 

1.1. Creating a New Problem

1.2. Adding Operation

1.3. Geometry Type

1.4. Simulation Controls

1.5. Material List

1.6. Define object

1.6.1. BFS step object

1.6.2. BFS step object geometry

1.6.3. BFS step object mesh

1.6.4. Initialize CFD state variables

1.7. Boundary Conditions

1.8. Step Controls

1.9. Generate Database

1.10. Run Simulation

1.11. Post-Processing

## Creating a New problem

On a Windows machine, go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select DEFORM GUI Main v1x.x. from the menu. The **DEFORM GUI Main** window will appear.

Create a new problem either by selecting **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in Fig. 2DTFL.1. Select " Integrated Manufacturing Process" radio button and units system as "**SI** " radio button in units field. Define Problem Name as "******2D_TurblentFlow_BFS_Lab_SI******" and make sure the “Show option dialog” check box is turned on (if we do not turn on the “**Show option dialog** ” check box, then we will not get the New Project dialog in MO UI). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_turbulent_flow_lab/image0001.jpg' | relative_url }})

Problem type selection window

Multiple operation wizard will open, at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session, we will use ‘**2D_TurblentFlow_BFS_Lab_SI******’ as the project name. Click on![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

## Adding 2D Forming operation

Add one 2D Forming operation from the Explorer Operations list. Operation can be added by clicking on 2D Forming operation ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button or user can also add by drag and drop into the Operation Editor (See Fig. 2DTFL.2.).

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_turbulent_flow_lab/image0002.jpg' | relative_url }})

Adding 2D Forming Operation

## Geometry type

Choose ‘**2D Plane strain** ’ in ‘**Geometry****type** ’ selection page and then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). 

## Simulation controls

‘CFD’ option is available in ‘Simulation controls’ page since version 14, check ‘**CFD flow** ’ and ‘**Heat****transfer** ’ (required for CFD flow simulation) checkboxes. Uncheck ‘**Deformation** ’ checkbox. Change operation name to “**BFS****flow** ” as shown in Fig. 2DTFL.3.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_turbulent_flow_lab/image0003.jpg' | relative_url }})

Simulation controls window, main settings 

Click ![]({{ '/assets/icons/pre_icons/mo_solver_settings.jpg' | relative_url }}), choose “**MUMPS** ” as solver for “**Temperature** ” as shown in Fig. 2DTFL.4., CFD will use the same solver.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_turbulent_flow_lab/image0004.jpg' | relative_url }})

Simulation control window, solver settings

Then click ![]({{ '/assets/icons/pre_icons/mo_process_conditions.jpg' | relative_url }}), switch to “**CFD** ” tab and check the “**Turbulence** ” check box to enable the turbulent flow model. Select **K-Epsilon** as turbulant model as shown in Fig. 2DTFL.5., then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_turbulent_flow_lab/image0005.jpg' | relative_url }})

Simulation control window, process conditions

## Material list

Next, add a new material, name as “**Ideal** ”, and define the material data as listed in table 1.

**Name** |  **Value**  
---|---  
Mass density |  tonne/mm3 |  1.0e-12  
Thermal Conductivity |  N/sec/C |  0.001  
Mass specific heat |  N-mm/tonne-C |  0.001  
Viscosity |  tonne/mm-sec |  1.0e-10  
  
**Ideal material**

‘Elastic’ properties of the material are not required to be defined for the Nitrogen gas for this lab, but still need to set Young’s modulus and Poisson’s ratio to 1 as shown in Fig. 2DTFL.6. and Fig. 2DTFL.7.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_turbulent_flow_lab/image0006.jpg' | relative_url }})

Material window, elastic

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_turbulent_flow_lab/image0007.jpg' | relative_url }})

Material window, thermal

  
Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Object page.

## Define object

In this lab, we need only fluid object. By default, ‘Workpiece’, ‘Top Die’ and ‘Bottom Die’ are added to the operation. Remove ‘Top Die’ and ‘Bottom Die’, so only one object is remained. Rename it to ‘BFS step’ as shown in Fig. 2DTFL.8., then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_turbulent_flow_lab/image0008.jpg' | relative_url }})

Object list page

### BFS step object

Choose ‘**Environment - Fluid(CFD)** ’ as object type with Object temperature as 20°C as shown in Fig. 2DTFL.9. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) go to the ‘Geometry’ page.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_turbulent_flow_lab/image0009.jpg' | relative_url }})

Object list window

### BFS step object geometry

Click on ‘**Edit** ’ And add points in XYR format as shown in Fig. 2DTFL.10. to generate the back step fluid object geometry, then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}).

**X** |  **Y** |  **R**  
---|---|---  
0 |  1000 |  0  
10000 |  1000 |  0  
10000 |  0 |  0  
20000 |  0 |  0  
20000 |  2000 |  0  
0 |  2000 |  0  
0 |  1000 |  0  
  
![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_turbulent_flow_lab/image0010.jpg' | relative_url }})

Geometry editor window

### BFS step object mesh

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to generate mesh for the fluid object. In Mesh page->General tab, type in ‘**10000** ’ in ‘Target number of elements’, leave other fields vaues to their default values. Click Next and assign the Ideal material. Click Back to Mesh page.  
Then click on ![]({{ '/assets/icons/pre_icons/mo_coating_tab.jpg' | relative_url }}), add three coating layers, 10000,10000,20000 respectively and click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) . While mesh is being generated, a ‘Generate Coating Mesh’ pop-up window will appear, click on ‘Yes’ to allow the generation of the coating mesh.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_turbulent_flow_lab/image0011.jpg' | relative_url }})

Mesh generation window

### Initialize CFD state variables

Now click on ![]({{ '/assets/icons/pre_icons/mo_nodal_data_icon.jpg' | relative_url }}) to show the Node data dialog to initialize the CFD state variables. From the list in the Node data dialog, click on ‘CFD flow’, see Fig. 2DTFL.12. We need to define ‘Kinetic energy’ so, click on ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}) to show the ‘Initialize Node Data’ dialog as shown in Fig. 2DTFL.12. and then type in 4570 as value, click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) button and close the Node data dialog.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_turbulent_flow_lab/image0012.jpg' | relative_url }})

Nodal Dialog – Initialization of CFD state variables

Next set ‘Dissipation rate’ to 100 by following the same procedure used for Kinetic energy.

Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) up to the ‘Boundary conditions’ page.

## Boundary Conditions

Default thermal exchange with environment bcc if defined can be removed. Current operation only needs flow related bcc to be defined as shown in Fig. 2DTFL.13.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_turbulent_flow_lab/image0013.jpg' | relative_url }})

Boundary conditions (unit m)

**Inlet BCC**  
Inlet flow velocity is assumed as u = 6000(y/1000-1)(2-y/1000) mm/s, in this Lab.   
To do so, click on ‘Boundary conditions’ ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})‘Deformation’, pick all points on along the left edge and set their ‘Y’ velocity to zero as shown in Fig. 2DTFL.14. Next, pick one by one point along the left edge as shown in Fig. 2DTFL.15., and set its X velocity, which is defined as the function of the point’s Y position, following the definition described above.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_turbulent_flow_lab/image0014.jpg' | relative_url }})

Inlet BCC Y

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_turbulent_flow_lab/image0015.jpg' | relative_url }})

Inlet BCC X

After defining the velocity for the left edge, inlet velocity definition will also be shown on ‘Fluid flow’ ![]({{ '/assets/icons/pre_icons/mo_inlet_outlet_bcc.jpg' | relative_url }}). ‘X’ ‘Y’ box should be checked, for any selected item, make sure ‘Turbulent BCC’ is checked, ‘Kinetic energy’ should already be set to 4570, and 100 for ‘Dissipation rate’. The Inlet BCC definition can be seen in Fig. 2DTFL.16.

* More convenient method is to utilize keyword file and excel. First, select the inlet points and define inlet velocity as a constant value under ![]({{ '/assets/icons/pre_icons/mo_inlet_outlet_bcc.jpg' | relative_url }}), then export the keyword file. Next, copy the lines under keyword ‘URZ’ to a excel file and format text to column. Refer to the first column, the nodal number, to find out the x,y coordinate in ‘Nodal’ ![]({{ '/assets/icons/pre_icons/mo_nodal_data_icon.jpg' | relative_url }}) dialog. In excel file, use MS office’s formula in the second column to calculate the velocity based on the function defined above. They copy the updated lines back to the keyword file and import it to the system. 

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_turbulent_flow_lab/image0016.jpg' | relative_url }})

Inlet BCC

**Wall BCC**  
Next, click on ![]({{ '/assets/icons/pre_icons/mo_wall_bcc.jpg' | relative_url }}), check ‘Noslip wall’, then pick the top and bottom surface as shown in Fig. 2DTFL.17. and click on ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) to assign the wall bcc.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_turbulent_flow_lab/image0017.jpg' | relative_url }})

Noslip wall BCC

## Step Controls

Go to step definition, using the ‘Guide’ mode (click on ![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }})), type 400 into ‘Number of steps’ field, set 10 as ‘Step increment’ and 0.1 sec. the time per step.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_turbulent_flow_lab/image0018.jpg' | relative_url }})

Step Controls (Guide Mode)

Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to ‘Generate DB’ page. 

## Generate Database

In 'Generate DB' page, click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) to generate the database.

## Run Simulation

Click on the menu '**Simulation** ' ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) '**Run****simulation** ', a pop-up window will show up, leave the default setting since the database has been already generated, then click on '**OK** ' button to start the simulation. 

  
Note: Currently CFD simulations cannot be simulated using multiple processors, hence please use Number of processors as 1 when submitting the problem to run.

## Post-Processing

Wait until the simulation has been finished, then open the DB file in the Next generation Post-Processor.

Click on the ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) State variables icon and select ![]({{ '/assets/icons/post_icons/mo_deformation_icon.jpg' | relative_url }}) (Deformation) icon, plot Velocity and Normal Pressure under the state variable list.  
Click on ![]({{ '/assets/icons/post_icons/mo_cfdflow_sv_icon.jpg' | relative_url }}) (CFD Flow) icon, plot Kinetic energy and Dissipation rate variables of CFD as shown in the Fig. 2DTFL.21. and Fig. 2DTFL.22.

  
**Velocity Profiles**

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_turbulent_flow_lab/image0019.jpg' | relative_url }})

Velocity profile 

  
**Pressure**

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_turbulent_flow_lab/image0020.jpg' | relative_url }})

Nodal pressure

  
**Kinetic Energy**

  
![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_turbulent_flow_lab/image0021.jpg' | relative_url }})

Kinetic energy profile 

  
**Dissipation Rate**

  
![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/2d_turbulent_flow_lab/image0022.jpg' | relative_url }})

Dissipation rate

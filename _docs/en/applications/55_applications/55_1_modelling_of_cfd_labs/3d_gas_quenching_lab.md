---
lang: en
title: "3D Gas Quenching Lab"
---

# 3D Gas Quencing Lab 

Gas quenching is a form of quenching that uses gas as a quenching media instead of liquid. Gas quenching typically uses Nitrogen gas, Helium, Argon, Hydrogen, or some mix/blend of these to quickly cool parts from their critical temperature. The metal parts to be quenched can be either alloys or ferrous metals.

Gas Quenching has many advantages：

  * Gas quenched materials are cleaner with no surface residue (this eliminates the need for rinsing and liquid quenching media disposal)

  * Gas quenching facilitates cooling that is more uniform and causes less distortion than liquid quenching

  * Gas quenching can use a medium that is easily produced on-site, such as nitrogen gas produced by an on-site.

This lab will demonstrate how to setup gas quenching simulation. Multiple gear objects load will be modeled, cooling by high pressure Nitrogen gas in a tank. The CFD flow simulation will be conducted first to study the flow and generate the heat transfer coefficient (HTC) profile. Then the calculated HTC will be imported to the second operation, to run the quenching/distortion model. 

Lab 1: Gear Quenching lab

1.1. Creating a New Problem

1.2. Adding Operation

1.3. Simulation Controls

1.4. Material List

1.5. Workpiece

1.6. Boundary Conditions

1.7. Step Controls

1.8. Generate Database

1.9. Run Simulation

1.10. Post-Processing

Lab 2: Gas Quenching Distortion lab

2.1. Adding Operation

2.2. Simulation Controls

2.3. Material List

2.4. Workpiece

2.5. Boundary Conditions

2.6. Object load

2.7. Import HTC

2.8. Stopping Controls

2.9. Step Controls

2.10. Generate Database

2.11. Run Simulation

2.12. Post-Processing

# Lab1: Gear Quenching operation

## Creating a New problem

On a Windows machine, go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button, select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select DEFORM GUI Main v1x.x. from the menu. The **DEFORM GUI Main** window will appear.

Create a new problem either by selecting **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in Fig. 3DGQL.1. Select " Integrated Manufacturing Process" radio button and units system as "**SI** " radio button in units field. Define Problem Name as "******3D_GasQuench_HelicalGear_Lab1******" and make sure the “Show option dialog” check box is turned on (if we do not turn on the “**Show option dialog** ” check box, then we will not get the New Project dialog in MO UI). Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_gas_quenching_lab/image0001.jpg' | relative_url }})

Problem type selection window

Multiple operation wizard will open, at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session, we will use ‘****3D_GasQuench_HelicalGear_Lab1********’ as the project name. Click on![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

## Adding 3D Forming operation

Add one 3D Forming operation from the Explorer Operations list. Operation can be added by clicking on 3D Forming operation ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button or user can also add by drag and drop into the Operation Editor (See Fig. 3DGQL.2.).

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_gas_quenching_lab/image0002.jpg' | relative_url }})

Added 3D Forming Operation into Operation editor

## Simulation Controls

First, set up simulation control data. Gas Quenching, air flow in the quenching tank will be modeled. ‘CFD’ option is available in ‘Simulation controls’ page since version 14, check ‘**CFD flow** ’ and ‘Heat transfer’ (required for CFD flow simulation). Uncheck ‘Deformation for now. Change operation name to “**Gas quenching CFD** ” as shown in Fig. 3DGQL.3.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_gas_quenching_lab/image0003.jpg' | relative_url }})

Simulation control window, main settings

Click![]({{ '/assets/icons/pre_icons/mo_solver_settings.jpg' | relative_url }}) , choose “**MUMPS** ” as solver for the “**Temperature** ” as shown in Fig. 3DGQL.4., CFD will use the same solver.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_gas_quenching_lab/image0004.jpg' | relative_url }})

Simulation control window, solver settings

  
Then click ![]({{ '/assets/icons/pre_icons/mo_process_conditions.jpg' | relative_url }}), switch to “**CFD** ” tab, check ![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_gas_quenching_lab/image0042.jpg' | relative_url }}) to enable turbulent flow model. And select ‘**Wall law** ’ for the ‘Heat transfer coefficient model’ as shown in Fig. 3DGQL.5., then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_gas_quenching_lab/image0005.jpg' | relative_url }})

Simulation control window, process conditions

## Material list

Next, add a new material, name it as “Nitrogen” and define the thermal material properties as listed in table 1.

**Name** |  **Value**  
---|---  
Mass density |  tonne/mm3 |  2.36e-11  
Thermal Conductivity |  N/sec/C |  0.0242  
Mass specific heat |  N-mm/tonne-C |  1.00643e+9  
Viscosity |  tonne/mm-sec |  1.81012e-11  
  
**Nitrogen material**

‘Elastic’ related material data is not required for the Nitrogen gas for this lab, but still need to set Yong’s modulus and Poisson’s ratio to 1 as shown in Fig. 3DGQL.6. and Fig. 3DGQL.7.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_gas_quenching_lab/image0006.jpg' | relative_url }})

Material window, elastic

  
![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_gas_quenching_lab/image0007.jpg' | relative_url }})

Material window, thermal

  
Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Object page.

## Workpiece

In this lab, quench tank and gear objects are required. For the first CFD operation, gear objects will be generated and subtracted from the tank to generate the cavity inside tank geometry.

  
By default, ‘Workpiece’, ‘Top Die’ and ‘Bottom Die’ are added to the operation. Remove ‘Bottom Die’, so only two objects remain in the table. Rename them to ‘Tank’ and ‘Gear’ as shown in Fig. 3DGQL.8.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_gas_quenching_lab/image0008.jpg' | relative_url }})

Object list window

  
**Gear object**

Gear will be generated first. Click on the item tree, ‘Gear’. Leave object type as ‘Rigid’, since gear will be eventually removed for the first operation. Go to next page, import gear geometry file “**helical_gear.geo** ” from \3D\LABS\ by clicking on ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}). After geometry is imported, click on ‘Check’ to make sure that the imported geometry has no issue (only one surface should be there without other geometry errors) as shown in Fig. 3DGQL.9.

  
![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_gas_quenching_lab/image0009.jpg' | relative_url }})

Geometry checking window

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Mesh page to generate the tet mesh for the gear. On mesh![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})General page, leave default values, ‘32000’ in ‘Target number of elements’, type as ‘Relative’, and 2 for the ‘Size ratio’. Click ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) as shown in Fig. 3DGQL.10.

When the ‘Default Boundary Condition’ window ‘Exchange-with-environment will be assigned to all surface…’ is poped-up, click on ‘No’.

Wait until mesh generation is finished, then click on ![]({{ '/assets/icons/pre_icons/mo_save_mesh_button.jpg' | relative_url }}) to save the gear mesh to file ‘**Gear.key** ’, which will be used for the next quenching/distortion simulation.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_gas_quenching_lab/image0010.jpg' | relative_url }})

Mesh generation window

**Object load**

Now a load of 2×2×3 gears model will be generated using ‘Copy object’ function. Right click on ‘Gear’ item, and then click on ![]({{ '/assets/icons/pre_icons/mo_copy_object_option.jpg' | relative_url }}) from the pop-up menu. Increase the total number by setting ‘Row’ to 2, ‘Column’ to 2, and ‘Layer’ to 3. Check ‘Count the original object’, and follow the following figure to finish the load setup. Click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}), the new generated load of gears should look like as shown in Fig. 3DGQL.11.

Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button to confirm and close the Copy object dialog. 

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_gas_quenching_lab/image0011.jpg' | relative_url }})

Object load

**Tank object**

Now it’s time to define ‘Tank’ object. Navigate to tank’s ‘Geometry’ page, click on ![]({{ '/assets/icons/pre_icons/mo_construct_by_substraction_button.jpg' | relative_url }}) as we need to create cavity inside the tank representing the gear objects inside the tank. To create the cavity inside, select all the gear objects from the object list using the mouse as shown in Fig. 3DGQL.12.

Box tank geometry will be generated through ‘Construct by subtraction’ page by defining the parameters for the surrounding box, toggle ![]({{ '/assets/icons/pre_icons/mo_use_box_radio_button.jpg' | relative_url }}), define the size of the box by filling up the respective parameters in the ‘Size’ category, type in the size, 500(W)-500(H)-500(L). Since the gears are centered at (0,0,0), type in -250,-250,0 as ‘Start point’. Construction by subtraction’ page allows user to either ‘Create geometry’ or ‘Generate mesh’. Click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) as shown in Fig. 3DGQL.12.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_gas_quenching_lab/image0012.jpg' | relative_url }})

Construct geometry/mesh by subtraction window

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_gas_quenching_lab/image0013.jpg' | relative_url }})

Construct geometry/mesh by subtraction window

  
As you click on ‘Generate mesh’ page, Mesh settings page will be displayed, type in “# of elements” as 600000, and set size ratio to 4. Then click on ![]({{ '/assets/icons/pre_icons/mo_generate_conforming_mesh_button.jpg' | relative_url }}). Wait untill the mesh generation is done. The final tank mesh will contain the cavity exactly maching with the gears’ surface mesh as shown in Fig. 3DGQL.13. Click on ‘OK’ twice to confirm.

Click on ‘Tank’ object page, then choose ‘Fluid’ as object type under ‘Environment’ catalog. 

Navigate to the Tank Material page and assign Nitrogen material from the ‘Material’ page as shown in Fig. 3DGQL.14.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_gas_quenching_lab/image0014.jpg' | relative_url }})

Assigning material 

For this CFD operation, only ‘Tank’ object is required for flow and heat transfer coefficient calculation. So click on ‘Object’ page, and remove all gear objects.

**Initialize CFD state variables**

Click on the tree in the 'Navigator' window and select the ‘Mesh’ item of the Tank object, then click on ![]({{ '/assets/icons/pre_icons/mo_nodal_data_icon.jpg' | relative_url }}) to open the node dialog and initialize the CFD state variables. From the item list click on ‘CFD flow’, see Fig. 3DGQL.15. First, to define ‘Kinetic energy’, click on ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}) to open ‘Initialize Node Data’ dialog, type in 375000 as shown in Fig. 3DGQL.15., then click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) and close the window.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_gas_quenching_lab/image0015.jpg' | relative_url }})

Nodal Dialog – Initialization of CFD state variables

Following the same procedure, set ‘Dissipation rate’ to 1650098000.

Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until the ‘Boundary conditions’ page.

## Boundary Conditions

Default thermal exchange with environment bcc if defined can be removed. Current operation needs only flow related bcc to be defined.   
**Inlet BCC**  
Constant inlet flow velocity (0,0,10000 mm/s) is assumed in this Lab, to do so, click on ‘Fluid flow’ ![]({{ '/assets/icons/pre_icons/mo_inlet_outlet_bcc.jpg' | relative_url }}). Check ‘X’ ‘Y’ ‘Z’ box, then type in inlet velocity for all the x/y/z components respectively. Make sure ‘Turbulent BCC’ is checked, then type in 375000 for ‘Kinetic energy’, and 1650098000 for ‘Dissipation rate’. Use the mouse, pick the right surface on –z axis, then click on ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) to finish the assignment. The Inlet BCC definition can be seen in Fig. 3DGQL.16.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_gas_quenching_lab/image0016.jpg' | relative_url }})

Inlet BCC

**Wall BCC**  
Tank’s external and the internal surfaces will be defined as wall bcc. First, click on ![]({{ '/assets/icons/pre_icons/mo_wall_bcc.jpg' | relative_url }}), check ‘Noslip wall’ and ‘Wall law’ checkboxes, also type in 0.2 for Y distance. To select the internal surfaces, first select all surfaces by clicking ![]({{ '/assets/icons/pre_icons/mo_select_all_icon.jpg' | relative_url }}) from the picking tools. Then click ![]({{ '/assets/icons/pre_icons/mo_delete_icon.jpg' | relative_url }}) to remove undesired surfaces and pick all the external surfaces, of total 6, to remove them for the selection. Then click on ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) to finish the assignment. The BCC definition can be seen in Fig. 3DGQL.17.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_gas_quenching_lab/image0017.jpg' | relative_url }})

Noslip wall + Wall law BCC

Next, click on ![]({{ '/assets/icons/pre_icons/mo_wall_bcc.jpg' | relative_url }}), check ‘Noslip wall’ checkbox, then use the mouse and pick four external surfaces on X and Y axis. Click on ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) to finish the assignment as shown in Fig. 3DGQL.18.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_gas_quenching_lab/image0018.jpg' | relative_url }})

Noslip wall BCC

## Step Controls

The CFD flow only needs few steps to reach static state. Go to step definition, using the ‘Guide’ mode (clicking on ![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }})), type 4 into ‘Number of steps’ field, set 1 as ‘Step increment’ and 0.01 sec. as the time per step as shown in Fig. 3DGQL.19.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_gas_quenching_lab/image0019.jpg' | relative_url }})

Step Controls (Guide Mode)

  
Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to ‘Generate DB’ page. 

## Generate Database

In 'Generate DB' page, click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) to generate the database as shown in Fig. 3DGQL.20.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_gas_quenching_lab/image0020.jpg' | relative_url }})

DB generation

## Run Simulation

Click on the menu '**Simulation** ' ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) '**Run****simulation** ', a pop-up window will show up, click on '**OK** ' button to start the simulation with the default setting since the database has been already generated.

Note: Currently CFD simulations cannot be simulated using multiple processors, hence please use Number of processors as 1 when submitting the problem to run.

## Post-Processing

Wait until the simulation has been finished, then open the DB file in the next generation post-processor. 

  
**Velocity Profiles**

Velocity profiles can be plotted by selecting **Deformation**![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **Velocity** state variable from the state variable dialog.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_gas_quenching_lab/image0021.jpg' | relative_url }})

Velocity profile (sliced view)

**Calculated Heat transfer coefficient**

Heat transfer coefficient profiles can be plotted by selecting **Thermal**![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **HTC** state variable from the state variable dialog.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_gas_quenching_lab/image0022.jpg' | relative_url }})

Calculated heat transfer coefficient by wall law (sliced view, on cavity)

# Lab 2 : Gas Quenching Distortion operation

Gas quenching CFD simulation has been done, with the generated heat transfer coefficient results now quenching distortion is on the way. Thermal distortion of helical gears load will be modeled. 

## Adding Operation

Add a 3D Forming operation from operation explorer. Click on the newly added operation, and when the ‘Setup Type’ window pops up, click on ‘YES – Interactive Setup’ as shown in Fig. 3DGQL.23.

  
![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_gas_quenching_lab/image0023.jpg' | relative_url }})

Add operations into operation editor

## Simulation Controls

In Simulation control page, using the ‘**Expert** ’ mode (clicking on ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})) check ‘Deformation’ and ‘Heat transfer’ checkboxes, also turn on ‘Transformation’ as shown in Fig. 3DGQL.24.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_gas_quenching_lab/image0024.jpg' | relative_url }})

Simulation control window, main settings

Click ![]({{ '/assets/icons/pre_icons/mo_solver_settings.jpg' | relative_url }}), set “MUMPS” as solver for “Temperature” and ‘Deformation’. For ‘Deformation’, select ‘Newton-Raphson’ as ‘Iteration method’ as shown in Fig. 3DGQL.25., since we will be using elasto-plastic workpiece. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Material page.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_gas_quenching_lab/image0025.jpg' | relative_url }})

Simulation control window, solver settings

## Material List

Import a new material ‘**5140_SI.KEY** ’ available at /3D/LABS/ using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}).

  
![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_gas_quenching_lab/image0026.jpg' | relative_url }})

Import material window

## Workpiece

In this lab, quench tank is no longer required. Load of gears will be created. In ‘Object’ page, click ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) to add one more object and rename it as ‘Gear’ as shown in Fig. 3DGQL.27.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_gas_quenching_lab/image0027.jpg' | relative_url }})

Object list window

  
**Gear object**

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_gas_quenching_lab/image0028.jpg' | relative_url }})

Object page

  
Click on the ‘Gear’ item in object tree and then type in 850 for Temperature and set object type as ‘Elasto-plastic’ as shown in Fig. 3DGQL.28. Since the same gear object was created in the first operation, and mesh has been saved to file, now click on ‘Mesh’ item, and then using ![]({{ '/assets/icons/pre_icons/mo_import_mesh_button.jpg' | relative_url }}) browse the saved file “Gear.key” as shown in the Fig. 3DGQL.29. After mesh has been imported, click on ‘Check Mesh’ and make sure that the mesh is ok. 

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_gas_quenching_lab/image0029.jpg' | relative_url }})

Imported mesh

  
**Material**  
Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Material page of the Gear and assign the material, AISI-5140. Click ![]({{ '/assets/icons/pre_icons/mo_back_button.jpg' | relative_url }}) to Mesh page to define coating mesh.

  
**Coating mesh**

In Mesh page, click on ‘Coating’, then add few coating layers (always recommended for phase transfer) and click on ‘Generate coating’ button as shown in Fig. 3DGQL.30.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_gas_quenching_lab/image0030.jpg' | relative_url }})

Coating layer

**Initialize state variables**

Next, click on ![]({{ '/assets/icons/pre_icons/mo_elemental_data_icon.jpg' | relative_url }}) button to show the elemental dialog to initialize the phase transformation data. From the item list, click ‘Microstructure’![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})’Phase’, see Fig. 3DGQL.31. Click on ‘Austenite’ row, then click on ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}) to ‘Initialize Element Data’, type in 1 as value in Initialize Element Data, then click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) and close the Initialize Element Data window.  

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_gas_quenching_lab/image0031.jpg' | relative_url }})

Elemental Dialog – Initialization of volume fraction 

Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the Elemnt Data dialog and click Next until ‘Boundary conditions’ page.

## Boundary Conditions

**Velocity BCC**

For the distortion analysis, rigid body motion will be prevented, to do so, click on ‘Boundary conditions’![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ‘Deformation’ ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ‘Velocity’ and then click ![]({{ '/assets/icons/pre_icons/mo_assign_free_distortion_bcc_button.jpg' | relative_url }}), Define Free distortion BCC dialog will be displayed.

On central display window, using mouse pick a node on ID, see Fig. 3DGQL.32., then click on ‘Next’ three times to accept the system suggestion for nodes to set the velocity constraint, then click on‘Finish’ to close the Define Free distortion BCC dialog. 

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_gas_quenching_lab/image0032.jpg' | relative_url }})

Define free distortion BCC   

## Object load

Object load has been created in the first operation, but not used in the CFD flow model. Follow the same precedure, see 1.5. Workpiece, Object load ,a load of 2×2×3 gears model will be generated for quenching distortion simulation. Right click on ‘[2] Gear’ item, and ![]({{ '/assets/icons/pre_icons/mo_copy_object_option.jpg' | relative_url }}) on the pop-up menu. Increase the total number by setting ‘Row’ to 2, ‘Column’ to 2, and ‘Layer’ to 3. Check ‘Count the original object’, and follow the following figure to finish the load setup. Click ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}), the new generated load of gears should be displayed as shown in Fig. 3DGQL.33.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_gas_quenching_lab/image0033.jpg' | relative_url }})

Object load 

  
Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button to close the Copy object dialog. 

  
For operation 2, tank is no longer needed. Go to the ‘Object’ page and delete the ‘Tank’ object. 

## Import HTC

Next for gear objects, quenching related parameters is required. Since heat transfer coefficient has been calculated in the first CFD flow simulation, it’s time to introduce them to the gears.

Set single object display mode ![]({{ '/assets/icons/pre_icons/mo_show_single_obj_icon.jpg' | relative_url }}). Click on ‘[2] Gear’ object item, navigate to ‘Boundary conditions’ page, then click on ‘Thermal’![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})’Advanced’, then set ‘Env. Temp’ to 25 and click ![]({{ '/assets/icons/pre_icons/mo_interpolate_button2.jpg' | relative_url }}).   

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_gas_quenching_lab/image0034.jpg' | relative_url }})

Data Interpolation 

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_gas_quenching_lab/image0035.jpg' | relative_url }})

Zone definition 

In ‘**Data********Interpolation** ’ page, select step 4 using the mouse, which is used to imported the heat transfer coefficient from, then click on ‘Next’. ‘Tank’ is the only object in CFD model, and is selected, see Fig. 3DGQL.34., now click on ![]({{ '/assets/icons/pre_icons/mo_interpolate_button2.jpg' | relative_url }}). Heat transfer coefficient is now imported to the present operation, wait until the interpolation finished, as seen Fig. 3DGQL.35. After intepolation is finished, we can observe that imported HTC are automatically divided into 10 zones as default. Results are summarized in Fig. 3DGQL.35.

Now click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to finish the assignment. As seen, defined zone 1 is shown in Fig. 3DGQL.36.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_gas_quenching_lab/image0036.jpg' | relative_url }})

Thermal advanced BCC (zone 1) 

Similarly, import htc to all other gears. Repeat the same procedure, finish assignment of thermal acvanced BCC for all gears by importing the calculated heat transfer coefficient from CFD flow file ‘3D_GasQuench_HelicalGear_Lab1.DB’. 

## Stopping Controls

Next, go to stopping controls definition, set thermal stop setting as shown in Fig. 3DGQL.37. for all gears.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_gas_quenching_lab/image0037.jpg' | relative_url }})

Stopping Controls (Guide Mode)

  
* Stopping controls can also be defined only once before creating the object load, so ‘Copy object’ function will carry this setting to all other objects.

## Step Controls

Next, go to step definition, using the ‘Guided’ mode (click on ![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }}) ), type 999999 into ‘Number of steps’ field. Set 10 as ‘Step increment’. Temperature based step definition will be used as shown in Fig. 3DGQL.38. with small initial time step (Min. time step) which is recommended to benefit the phase transformation simulation.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_gas_quenching_lab/image0038.jpg' | relative_url }})

Step Controls (Guide Mode)

Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to ‘Generate DB’ page. 

## Generate Database

In 'Generate DB' page, click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) to generate the database as shown in Fig. 3DGQL.39.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_gas_quenching_lab/image0039.jpg' | relative_url }})

DB generation

## Run Simulation

Click on the menu 'Simulation' ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) 'Run simulation', a pop-up window will show up, , click on 'OK' button to start the simulation with the default setting since the database has been already generated. 

## Post-Processing

Wait until the simulation has been finished, then open the DB file in the Next generation Post-Processor. Plot Temperature and Effective stress state variable distribution using ![]({{ '/assets/icons/post_icons/mo_temp_sv.jpg' | relative_url }}) button and ![]({{ '/assets/icons/post_icons/mo_eff_stress_sv_icon.jpg' | relative_url }}) button respectively from state variable tool bar.

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_gas_quenching_lab/image0040.jpg' | relative_url }})

Temperature profile (380.954s)

![]({{ '/assets/images/applications/55_1_modelling_of_cfd_labs/3d_gas_quenching_lab/image0041.jpg' | relative_url }})

Effective stress (380.954s)

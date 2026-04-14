---
lang: en
title: "Thermal Distortion Lab"
---

# Thermal Distortion Lab

In this lab we will setup simple Thermal expansion simulation for simple 3D Brick meshed Elasto-Plastic workpiece.

1.1. Creating New problem

1.2. Adding 3D Forming Operation

1.3. Select Simulation Modes

1.4. Add material from Library

1.4.1. Editing Flow stress data

1.5. Adding Objects

1.6. Workpiece

1.6.1. Define Workpiece general object data

1.6.2. Create workpiece geometry from primitive

1.6.3. Generating Brick mesh for Workpiece

1.6.4. Assign Material to Workpiece

1.6.5. Assign BCC for Workpiece

1.6.6. Assign Object properties for Workpiece

1.7. Assign Step controls

1.8. Data checking and database generation

1.9. Run and monitor a simulation

1.10. Review Results

## Creating New problem

On a Windows machine, go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** v1x.x from the menu. The DEFORM GUI Main window will appear.

Create a new problem either by selecting **File**![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in Fig. 3DTHDL1.1. Select " **Integrated Manufacturing Process** " radio button and unit system as "**SI** " radio button in unit field. Define Problem Name as "**BlockHeating** " and make sure the “**Show option dialog** ” check box is turned on (if we do not turn on the “Show option dialog” check box, then we will not get the New Project dialog). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image014.jpg' | relative_url }})

New Problem Setup Window

Multiple operation wizard will open with the New Project dialog, at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session we will use "**BlockHeating** " as the project name. Confirm that First operation check box is unchecked as we will add operation later (See Fig. 3DTHDL1.2.), click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue to open the operation.

![]({{ '/assets/images/applications/55_thermal_distortion/thermal_distortion_lab/image0002.jpg' | relative_url }})

New MO Project window

## Adding 3D Forming Operation

Multiple Operation wizard will open a new project. Add 3D Forming operation from the Explorer Operations list. Operation can be added by clicking on 3D Forming operation ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button (See Fig. 3DTHDL1.3.) or user can also add by drag and drop into the Operation Editor.

![]({{ '/assets/images/applications/55_thermal_distortion/thermal_distortion_lab/image0003.jpg' | relative_url }})

Adding 3D Forming operation from operation explorer

## Select Simulation Modes

In this lab we will be showing how to setup simple Thermal expansion problem, so in Simulation controls page, check the **Deformation** and **Heat****transfer** mode check boxes if not selected by default (See Fig. 3DTHDL1.4.), then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/applications/55_thermal_distortion/thermal_distortion_lab/image0004.jpg' | relative_url }})

Simulation controls window

## Add material from Library

Click the ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load material from library) button. Select the **Aluminum** category, then select **ALUMINUM-2024[70-930F(20-500C)]** and click the ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}) button. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Editing Flow stress data

For improved convergence, click the ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) next to “Flow Stress to edit material data. Under Extrapolate pull down menu select “**Strain****Rate** **–** “(See Fig. 3DTHDL1.5.) and then change first **strain****rate** value to **0** (See Fig. 3DTHDL1.6.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Object list page.

![]({{ '/assets/images/applications/55_thermal_distortion/thermal_distortion_lab/image0005.jpg' | relative_url }})

Extrapolating "Strain rate -" value of Material in Flow stress Edit window

![]({{ '/assets/images/applications/55_thermal_distortion/thermal_distortion_lab/image0006.jpg' | relative_url }})

Editing strain rate value to 0 of Material in Flow stress Edit window

## Adding Objects

The Thermal expansion operation requires only a workpiece for simulation. By default, three objects will be added in Forming operation list. By selecting Top die and Bottom die in list, click on ![]({{ '/assets/icons/pre_icons/mo_delete_object_button.jpg' | relative_url }}) (delete object) button to delete the selected objects. After deleting two objects, Object list window looks as shown in Fig. 3DTHDL1.7. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button.

![]({{ '/assets/images/applications/55_thermal_distortion/thermal_distortion_lab/image0007.jpg' | relative_url }})

Objects list window

## Workpiece

### Define Workpiece general object data

Accept the default object name **Workpiece**. Assign the temperature as 20°C and select the object type as **Elasto-plastic**. (See Fig. 3DTHDL1.8.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button.

![]({{ '/assets/images/applications/55_thermal_distortion/thermal_distortion_lab/image0008.jpg' | relative_url }})

Workpiece object window

### Create workpiece geometry from primitive

Click on the ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) button to create a geometry within DEFORM. Select " Box " type and define **Width**(W) as **50** mm, **Height**(H) as **50** mm and **Length** (L) as **300** mm (See Fig. 3DTHDL1.9.). Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button and then observe the geometry in graphics window.

![]({{ '/assets/images/applications/55_thermal_distortion/thermal_distortion_lab/image0009.jpg' | relative_url }})

Workpiece geometry Primitive window

Now click on ![]({{ '/assets/icons/pre_icons/mo_setup_brick_mesh_label.jpg' | relative_url }}) mesh option, select **Extrude** type radio button and Define Right side end surface as Start surface and Left side end surface as End surface as shown in Fig. 3DTHDL1.10. Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button to close Setup Brick mesh page, click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button until workpiece mesh.

![]({{ '/assets/images/applications/55_thermal_distortion/thermal_distortion_lab/image0010.jpg' | relative_url }})

Setup Brick mesh window

### Generating Brick mesh for Workpiece

We will generate Brick mesh for workpiece so, click on ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) mode icon to switch to expert mode. Select the Brick mesh radio button. In the General tab,define Uniform thickness **# of layers** as **21** , click on 2D Cross section tab and define **Target number of Elements** as **64** , ****the**thickness element** as **8** and turn on **Mapped mesh generation** check box (See Fig. 3DTHDL1.11.). Click the ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button to generate the mesh for workpiece (See Fig. 3DTHDL1.12.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button to assign material for workpiece.

![]({{ '/assets/images/applications/55_thermal_distortion/thermal_distortion_lab/image0011.jpg' | relative_url }})

Brick mesh 2D Cross section window

![]({{ '/assets/images/applications/55_thermal_distortion/thermal_distortion_lab/image0012.jpg' | relative_url }})

3D Brick mesh Window

### Assign Material to Workpiece

Select the **ALUMINUM-2024[70-930F(20-500C)]** in the material window to assign the material to the workpiece. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button to assign the workpiece boundary conditions.

### Assign BCC for Workpiece

**Assign Free Distortion velocity BCC** : This will automatically assign velocity constraints to fix 3 degrees of translation, 3 degrees of rotation, without restricting expansion or bending. To assign this BCC, 

  * Select **Assign Free Distortion BCC** in Velocity page.

  * Pick a node on a bottom corner of the workpiece (See Fig. 3DTHDL1.13.).

  * Click ![]({{ '/assets/icons/pre_icons/mo_bcc_next_button.jpg' | relative_url }}) and accept system selection for next 3 nodes, then click ![]({{ '/assets/icons/pre_icons/mo_finish_button.jpg' | relative_url }}) in Remove **Z** rotation page.

![]({{ '/assets/images/applications/55_thermal_distortion/thermal_distortion_lab/image0013.jpg' | relative_url }})

Picking a node to assign Free distortion BCC

**Assign Heat Exchange with Environment:**

  * Assign Heat Exchange with Environment BCC to all surfaces.

  * Add one Environment window at Bottom of Workpiece with

  * Environment Temperature: 20°C

  * Emissivity : 0.4

  * Convection coefficient :**f(temp**) as shown in Fig. 3DTHDL1.14.

**Temperature (C)** |  **Convection Coefficient**  
---|---  
20 |  0.8  
105 |  0.5  
110 |  1  
150 |  4  
200 |  0.5  
500 |  0.025  
1000 |  0.033333333  
  
  * Assign Advanced (thermal) boundary conditions to the Top surface of workpiece as given below,

  * Environment temperature: 650°C

  * Convection coefficient : 3

  * Emissivity: 0.4 (See Fig. 3DTHDL1.15.)

![]({{ '/assets/images/applications/55_thermal_distortion/thermal_distortion_lab/image0014.jpg' | relative_url }})

Assigning Heat exchange window on bottom surface of workpiece

![]({{ '/assets/images/applications/55_thermal_distortion/thermal_distortion_lab/image0015.jpg' | relative_url }})

Assigning Advanced Thermal BCC on Top surface of Workpiece

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Object properties.

### Assign Object properties for Workpiece

Click on **Thermal** tab to define thermal stopping controls, select**Any node** and define **Max temperature** as **450** °C. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Step page.

## Assign Step controls

In Expert mode Step controls, define **Number of Simulation steps** as **1000** under Simulation controls tab.

Click on **Step increment** tab and select **Temperature** **radio** button and define**Initial time step** as **0.01** , **Max temperature change** as **5** deg, **Min time step** as **0.01** sec and **Max time step** as **5** sec. Click on **Solver settings** tab and select **MUMPS** Solver and **Newton-Rapson** Iteration method under **Deformation** tab. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button to generate DB.

![]({{ '/assets/images/applications/55_thermal_distortion/thermal_distortion_lab/image0016.jpg' | relative_url }})

Expert mode Simulation controls

## Data checking and database generation

Click on the ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) button, the data checking system will confirm that defined data is appropriate for running a simulation.

Red marks indicate missing or incorrect data that will prevent a simulation from running. It is necessary to correct those errors before the database can be generated.

Yellow marks indicate data which may be suspect and should be reviewed. These should be investigated carefully, as they might result in system instability or erroneous (incorrect) results.

Review the data checking information. If there are no yellow or red marks, click the ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button.

You should look for the words: Database has been generated. When you see this, it means that your inputs have been saved to the database and you are now ready to run the simulation.

Click on the MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode button (above the operation tree) to start the simulation.

## Run and monitor a simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog. Use the default **Continue****Run** option to select “**Continue****from the last step** ” option and then select the Simulation mode as **Interactive** radio button **** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

The progress of the simulation can be monitored as it is running by looking at the Simulation Message tab and Simulation Graphics from the Graphics display region in Simulation mode. If ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked in Simulation Message tab, which is the default setting, the Message file will refresh automatically.

The Message file provides information about which simulation step the simulation is currently on and information dealing with how well the simulation is running as shown in Fig. 3DTHDL1.17.

![]({{ '/assets/images/applications/55_thermal_distortion/thermal_distortion_lab/image0017.jpg' | relative_url }})

Running the simulation from MO simulation mode

After completion of simulation, click on ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode button to review results.

## Review Results

Play through the Steps and see the Temperature distribution by plotting the Temperature State variables.

![]({{ '/assets/images/applications/55_thermal_distortion/thermal_distortion_lab/image0018.jpg' | relative_url }})

Temperature distribution in workpiece at last step of simulation.

**Plot Total displacement State variable with Deflection** : Open state variable dialog ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) and plot displacement- total displacement. Click on **Deflection** tab, Select the Use Deflection check box in the “State Variables” dialog. The workpiece with magnified distortion is as shown in Fig. 3DTHDL1.19. Use the slider bar to increase or decrease exaggeration of distortion.

![]({{ '/assets/images/applications/55_thermal_distortion/thermal_distortion_lab/image0019.jpg' | relative_url }})

Total - Displacement state variable plot with Deflection

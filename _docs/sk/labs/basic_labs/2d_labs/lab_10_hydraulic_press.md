---
lang: sk
title: "Lab 10 Hydraulic press"
---

# Lab 10 Hydraulic press

Requirement: To setup this operation, First we have to setup [Lab 03 Spike Isothermal Lab](/docs/sk/labs/basic_labs/2d_labs/lab_03_spike_isothermal/).

This lab will repeat the spike isothermal forging simulation on a 1000 ton hydraulic press. The deformation results will appear similar to the previous spike forging labs, but the velocity will decrease as the press runs out of power during the end of the stroke. An initial die speed of 2”/second will be applied to the top die. As the forming load increases, it will require more power than the press can deliver with subsequent deceleration of the moving die.

10.1. Creating a New Problem

10.2. Adding Operation

10.3. Importing Database

10.4. Assigning Hydraulic movement for Top Die

10.5. Generating Database

10.6. Starting the Simulation

10.7. Post-Processing the Results

## Creating a New Problem

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear.

Create a new problem either by selecting **File** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear. Select "**Integrated Manufacturing Process** " radio button and unit system as "**English** " radio button in unit field. Define Problem Name as " ******Spike_Hydraulic** " and make sure the “**Show option dialog** ” check box is turned on (if we do not turn on the “Show option dialog” check box, then we will not get the New Project dialog). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new problem using the Deform Integrated Manufacturing Process.

Multiple operation wizard will open with the New Project dialog (See Fig. L10.1.), at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this lab we use ‘**Spike_Hydraulic** ’ as the project name.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_10_hydraulic_press/2d_mobl10_image0001.jpg' | relative_url }})

Assigning Project name

User can also change the Unit system, project saving file location and add operation by selecting from First operation pull down list and checkbox (see Fig. L10.1.). Using copy Existing project option we can import previous saved projects as new project. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

## Adding Operation

Multiple Operation wizard will open. Add 2D Forming operation from the Explorer Operations list. Operation can be add by clicking on 2D Forming operation ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button or user can also add by drag and drop into the Operation Editor.

## Importing Database

Using Import option ![]({{ '/assets/icons/pre_icons/mo_import_icon.jpg' | relative_url }}), Load the database of problem **Spike_Isothermal** , select**-1** step in the Step selection window (see Fig. L10.2.), then click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button until Top Die movement page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_10_hydraulic_press/2d_mobl10_image0002.jpg' | relative_url }})

Selecting step in Step Selection window

**Note** :

Two parameters are required to run the hydraulic press model.

1\. A control speed or nominal starting speed should be supplied to the movement control field. If the press is being run at maximum possible speed, then the speed should be identical to the speed at no load. Any controls within the power envelope are possible including speed (or load) as a function of time or stroke.

2\. The power envelope defining the maximum speed available at any load can be described in data pairs. This data is constant for any press configuration. Typically five or more points can adequately define this limit with DEFORM® interpolating data between points. One point at zero load and one at zero force should be included.

Stopping controls such as maximum stroke, maximum load or minimum velocity are all available when using the hydraulic press model.

## Assigning Hydraulic movement for Top Die

Select **Hydraulic****movement** type, define Constant **speed** as **2** in/sec, **check** the **power****limit** check box and click on ![]({{ '/assets/icons/pre_icons/mo_define..._button2.jpg' | relative_url }}) button and define the below power limit curve values in the table (see Fig. L10.3.). Then click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to close the Function window. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Generate DB page.

**Force (Klb-s)** |  **Speed (in/s)**  
---|---  
0 |  2.51  
100 |  2.50  
250 |  2.46  
450 |  2.40  
700 |  2.26  
1000 |  1.98  
1250 |  1.65  
1500 |  1.25  
1750 |  0.75  
2000 |  0.0  
  
Top Die Movement- Power Limit Curve data

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_10_hydraulic_press/2d_mobl10_image0003.jpg' | relative_url }})

Top Die Movement Power limit definition dialog

## Generating Database

Click the ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) button to have the program check to see if anything was missed in the problem setup. During the checking process:

Messages in the red color signify data that needs to be fixed before a simulation can be run (such as when you forget to define any material data). 

Click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database. When the program is done writing the database, click on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) tab to run simulation.

## Starting the Simulation

Click on ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) under the simulation tab, as we click on the Run option, Run simulation dialog will open, use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

The progress of the simulation can be monitored as it is running by looking at the Simulation Message and Simulation Graphics in Simulation mode. Click the Simulation Message tab to view the Message file. As long as the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked, which is the default setting, the Message file will refresh every couple of seconds.

The Message file provides information about which simulation step the simulation is currently on and also gives information dealing with how well the simulation is running.

When the simulation has finished, the following message will be added to the end of the Message file:

"******Message*******

Simulation is completed and stopped at the user specified time step".

## Post-Processing the Results

After simulation has been completed, click on ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) tab, MO post processor will open.

**Load-Stroke Graph:**

Plot **Load-Stroke** and **Speed- Stroke graph** and observe the graph as shown in Fig. L10.4. and Fig. L10.5.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_10_hydraulic_press/2d_mobl10_image0004.jpg' | relative_url }})

Load-Stroke Graph plot

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_10_hydraulic_press/2d_mobl10_image0005.jpg' | relative_url }})

Speed-Stoke Graph plot

****

**Related Topics:**

[15\. Movement Controls Settings](/docs/sk/pre_processor/15_movement_controls_definition/15_movement_controls_settings/)

[6.2. Integrated Manufacturing Process Simulation layout](/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_2_integrated_manufacturing_process_simulation_layout/)

[6.3. Integrated Manufacturing Process Post-processor layout](/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_3_integrated_manufacturing_process_post_layout/)

[25\. Post Processor Layout](/docs/sk/post_processor/25_post_processor_layout/25_post_processor_layout/)

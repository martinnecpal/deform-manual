---
lang: en
title: "Lab 11 Screw press"
---

# Lab 11 Screw press

Requirement: To setup this operation, First we have to setup [Lab 03 Spike Isothermal Lab.](/docs/en/labs/basic_labs/2d_labs/lab_03_spike_isothermal/)

11.1. Creating a New Problem

11.2. Adding Operation

11.3. Importing Database

11.4. Material List

11.5. Assigning Temperature for Billet

11.6. Assigning Screw press movement for Top Die

11.7. Generating Database

11.8. Starting the Simulation

11.9. Post-Processing the Results

## Creating a New Problem

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear.

Create a new problem either by selecting **File** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear. Select "**Integrated Manufacturing Process** " radio button and unit system as "**English** " radio button in unit field. Define Problem Name as " ******Spike_Screwpress** " and make sure the “**Show option dialog** ” check box is turned on (if we do not turn on the “Show option dialog” check box, then we will not get the New Project dialog). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new problem using the Deform Integrated Manufacturing Process.

Multiple operation wizard will open with the New Project dialog (see Fig. L11.1.), at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this lab we use ‘**Spike_Screwpress** ’ as the project name.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_11_screw_press/2d_mobl11_image0001.jpg' | relative_url }})

Assigning Project Name

User can also change the Unit system, project saving file location and add operation by selecting from First operation pull down list and checkbox (see Fig. L11.1.). Using copy Existing project option we can import previous saved projects as new project. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

## Adding Operation

Multiple Operation wizard will open. Add 2D Forming operation from the Explorer Operations list. Operation can be add by clicking on 2D Forming operation ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button or user can also add by drag and drop into the Operation Editor.

## Importing Database

Using Import option ![]({{ '/assets/icons/pre_icons/mo_import_icon.jpg' | relative_url }}), Load the database of problem **Spike_Isothermal** , select**-1** step in the Step selection window, then click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Material page.

## Material List

In material list, delete the AISI-1035,COLD[70-400F(20-200C)] material from the list by highlighting the material click on ![]({{ '/assets/icons/pre_icons/mo_delete_icon2.jpg' | relative_url }}) button (See Fig. L11.2.).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_08_hammer_press/2d_mobl8_image0003.jpg' | relative_url }})

Deleting the Material from the Material list

Load the material **AISI-1045_(20-1100C)** from DEFORM Material library, from **Steel** category using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load material data from library) option. Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Billet page.

## Assigning Temperature for Billet

Assign **Object temperature** as **2250** °F (see Fig. L11.3.) and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top die movement page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_11_screw_press/2d_mobl11_image0002.jpg' | relative_url }})

Billet Object page

## Assigning Screw press movement for Top Die

In Top Die movement page, select **Screw press movement** type, define **Energy** as**75 Klb-in** , **Blow efficiency** as **0.8** , **Movement of Inertia** as **0.25 Klb-in-s^2** and**Lead screw pitch** as **5** **in/rev** (see Fig. L11.4.). Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Generate DB page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_11_screw_press/2d_mobl11_image0003.jpg' | relative_url }})

Top die movement page

## Generating Database

Click the ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) button to have the program check to see if anything was missed in the problem setup. During the checking process:

Messages in the red color signify data that needs to be fixed before a simulation can be run (such as when you forget to define any material data).

Click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database. When the program is done writing the database, click on tab to run simulation.

## Starting the Simulation

Click on ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) under the simulation tab, as we click on the Run option, Run simulation dialog will open, use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

The progress of the simulation can be monitored as it is running by looking at the Simulation Message and Simulation Graphics in Simulation mode. Click the Simulation Message tab to view the Message file. As long as the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked, which is the default setting, the Message file will refresh every couple of seconds.

The Message file provides information about which simulation step the simulation is currently on and also gives information dealing with how well the simulation is running.

When the simulation has finished, the following message will be added to the end of the Message file:

"PROGRAM STOPPED!

***** PRESS ENERGY HAS BEEN FULLY CONSUMED.".

## Post-Processing the Results

After simulation has been completed, click on ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) tab, MO post processor will open.

Plot **Load-Stroke** and **Speed- Stroke graph** and observe the graph as shown in Fig. L11.5. and Fig. L11.6:

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_11_screw_press/2d_mobl11_image0004.jpg' | relative_url }})

Y Load -Stroke graph plot

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_11_screw_press/2d_mobl11_image0005.jpg' | relative_url }})

Y Speed - Stroke graph plot

**Related Topics:**

[15\. Movement Controls Settings](/docs/en/pre_processor/15_movement_controls_definition/15_movement_controls_settings/)

[6.2. Integrated Manufacturing Process Simulation layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_2_integrated_manufacturing_process_simulation_layout/)

[6.3. Integrated Manufacturing Process Post-processor layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_3_integrated_manufacturing_process_post_layout/)

[25\. Post Processor Layout](/docs/en/post_processor/25_post_processor_layout/25_post_processor_layout/)

---
lang: en
title: "Lab 09 Hammer Multiple Operation"
---

# Lab 09 Hammer Multiple Operation

The intent of the lab is to demonstrate to the user how to prepare a multiple-blow simulation in DEFORM for three successive hammer blows using 2D Multi Blow Forging operation. The simulation is performed as a 2D non-isothermal simulation.

9.1. Creating a New Problem

9.2. Adding Operation

9.3. Importing Keyfile

9.4. Setup Process settings

9.5. Editing Blow table

9.6. Generating Inter-object Contact

9.7. Generating Database

9.8. Starting the Simulation

## Creating a New Problem

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear.

Create a new problem either by selecting **File** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear. Select "**Integrated Manufacturing Process** " radio button and unit system as "**English** " radio button in unit field. Define Problem Name as "**HM_FORGE** " and make sure the “**Show option dialog** ” check box is turned on (if we do not turn on the “Show option dialog” check box, then we will not get the New Project dialog). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new problem using the Deform Integrated Manufacturing Process.

Multiple operation wizard will open with the New Project dialog (See Fig. 9.1.), at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this lab we use ‘****HM_FORGE**** ’ as the project name.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_09_hammer_multiple_operation/2d_mobl9_image0001.jpg' | relative_url }})

Assigning project name

User can also change the Unit system, project saving file location and add operation by selecting from First operation pull down list and checkbox (See Fig. 9.1.). Using copy Existing project option we can import previous saved projects as new project. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

## Adding Operation

Multiple Operation wizard will open. Add 2D Multi Blow Forging operation from the Explorer Operations list. Operation can be add by clicking on 2D Multi Blow Forging operation ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button or user can also add by drag and drop into the Operation Editor. (See Fig. 9.2.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_09_hammer_multiple_operation/2d_mobl9_image0002.jpg' | relative_url }})

Added Multi Blow Forging operation into Operation Editor

## Importing Keyfile

Import **HAMMER_LAB.KEY** from DEFORM installation folder \2d\LABS using Import ![]({{ '/assets/icons/pre_icons/mo_import_icon.jpg' | relative_url }}) option.

## Setup Process settings

Energy has been loaded from the Primary Die movement definition. Keep the same energy. Check the Use Workpiece rotation checkbox to flip the workpiece after every blow. Keep the Use Dwell checkbox checked, as no heating is going on between the blows in this lab. Do not check the Use Reheat checkbox. (see Fig. 9.3.) Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to edit Blow table.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_09_hammer_multiple_operation/2d_mobl9_image0003.jpg' | relative_url }})

Process page

## Editing Blow table

In the Blow Table add two more hits in addition to the default blow for a total of three blows. In all three rows change the Dwell time to 1.5 seconds by double clicking on the field. In the first row check the Flip checkbox. In the second row check the Flip checkbox and change the % Blow to 90. In the third row check change the % Blow to 80. (See Fig. 9.4.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until the Contact page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_09_hammer_multiple_operation/2d_mobl9_image0004.jpg' | relative_url }})

Edit Blow table

## Generating Inter-object Contact

In contact page, click on workpiece -workpiece relationship ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) button for define Shear friction value as **0******.2** 5 - Warm forming** from pull down menu list (See Fig. 9.5.), 0.25 value will be added as Shear friction value and define Heat transfer coefficient (HTC) value as **Forming** automatically 0.004 value will be added (See Fig. 9.6.).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_09_hammer_multiple_operation/2d_mobl9_image0005.jpg' | relative_url }})

Deformation Inter-object data definition window

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_09_hammer_multiple_operation/2d_mobl9_image0006.jpg' | relative_url }})

Thermal Inter-object data definition window

Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to go back to Contact window, since the friction conditions are the same for all the object pairs, the ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) button can be used to copy the interface properties from the first relationship to all of the others. After this is done, all relationships will have a friction of 0.25 and HTC of 0.004 defined. Use ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) icon to determine a suitable contact tolerance (a value of about 0.00099" will be calculated), then click ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) button to generate contacts for all relationships (see Fig. 9.7.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Data base generation page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_09_hammer_multiple_operation/2d_mobl9_image0007.jpg' | relative_url }})

Generated contact relationship

## Generating Database

Click the ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) button to have the program check to see if anything was missed in the problem setup. During the checking process:

Messages in the red color signify data that needs to be fixed before a simulation can be run (such as when you forget to define any material data).

Click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database. When the program is done writing the database, click on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) tab to run simulation.

## Starting the Simulation

Click on ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) under the simulation tab, as we click on the Run option, Run simulation dialog will open, use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

The progress of the simulation can be monitored as it is running by looking at the Simulation Message and Simulation Graphics in Simulation mode. Click the Simulation Message tab to view the Message file. As long as the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked, which is the default setting, the Message file will refresh every couple of seconds.

The Message file provides information about which simulation step the simulation is currently on and also gives information dealing with how well the simulation is running.

When the simulation has finished, the following message will be added to the end of the LOG file:

"MULTIPLE OPERATION COMPLETED."

****

**Related Topics:**

[15\. Movement Controls Settings](/docs/en/pre_processor/15_movement_controls_definition/15_movement_controls_settings/)

[6.2. Integrated Manufacturing Process Simulation layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_2_integrated_manufacturing_process_simulation_layout/)

[6.3. Integrated Manufacturing Process Post-processor layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_3_integrated_manufacturing_process_post_layout/)

[25\. Post Processor Layout](/docs/en/post_processor/25_post_processor_layout/25_post_processor_layout/)

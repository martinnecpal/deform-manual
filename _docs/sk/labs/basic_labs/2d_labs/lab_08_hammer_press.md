---
lang: sk
title: "Lab 08 Hammer Press"
---

# Lab 08 Hammer Press

Requirement: To setup this operation, First we have to setup [Lab 03 Spike Isothermal Lab.](/docs/sk/labs/basic_labs/2d_labs/lab_03_spike_isothermal/)

8.1. Creating a New Problem

8.2. Adding Operation

8.3. Importing Database

8.4. Material List

8.5. Assigning Temperature for Billet

8.6. Assigning Hammer Movement for Top Die

8.7. Generating 1st Operation Database

8.8. Simulating 1st Operation

8.9. Post-Processing the 1st operation Results

8.10. Adding 2nd operation

8.11. Adding objects

8.12. Assigning Top Die Movement

8.13. Generate Inter-object Contacts

8.14. Step Controls

8.15. Generating 2nd operation Database

8.16. Simulating 2nd operation

8.17. Post-Processing the 2nd Operation Results

8.18. Closing MO Wizard

## Creating a New Problem

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear.

Create a new problem either by selecting **File** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear. Select "**Integrated Manufacturing Process** " radio button and unit system as "**English** " radio button in unit field. Define Problem Name as " ******Spike_Hammer** " and make sure the “**Show option dialog** ” check box is turned on (if we do not turn on the “Show option dialog” check box, then we will not get the New Project dialog). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new problem using the Deform Integrated Manufacturing Process.

Multiple operation wizard will open with the New Project dialog (See Fig. L8.1.), at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this lab we use ‘**Spike_Hammer** ’ as the project name.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_08_hammer_press/2d_mobl8_image0001.jpg' | relative_url }})

Assigning Project Name

User can also change the Unit system, project saving file location and add operation by selecting from First operation pull down list and checkbox (See Fig. L8.1.). Using copy Existing project option we can import previous saved projects as new project. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

## Adding Operation

Multiple Operation wizard will open. Add 2D Forming operation from the Explorer Operations list. Operation can be add by clicking on 2D Forming operation ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button or user can also add by drag and drop into the Operation Editor.

## Importing Database

Using Import option ![]({{ '/assets/icons/pre_icons/mo_import_icon.jpg' | relative_url }}), load the database of problem **Spike_Isothermal** , select **-1** step in the Step selection window (See Fig. L8.2.), then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_08_hammer_press/2d_mobl8_image0002.jpg' | relative_url }})

Selecting step in Step Selection window

## Material List

In material list, delete the AISI-1035,COLD[70-400F(20-200C)] material from the list by highlighting the material click on ![]({{ '/assets/icons/pre_icons/mo_delete_icon2.jpg' | relative_url }}) button (See Fig. L8.3.).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_08_hammer_press/2d_mobl8_image0003.jpg' | relative_url }})

Deleting the Material from the Material list

Load the material **AISI-1045_(20-1100C)** from DEFORM Material library, from **Steel** category using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load material data from library) option. Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) upto Billet page.

## Assigning Temperature for Billet

Assign **Object****temperature** as **2250** °F (See Fig. L8.4.) and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top die movement page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_08_hammer_press/2d_mobl8_image0004.jpg' | relative_url }})

Billet Object page

## Assigning Hammer Movement for Top Die

In **Top Die movement** page, select **Hammer** movement type, define **Energy** as **250Klb-in** , **Hammer****mass** as **0.265e-3** **Klb-s^2/in** and **Blow****efficiency** as**0.6** (see Fig. L8.5.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Generate DB page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_08_hammer_press/2d_mobl8_image0005.jpg' | relative_url }})

Top die movement page

## Generating 1st Operation Database

Click the ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) button to have the program check to see if anything was missed in the problem setup. During the checking process:

Messages in the red color signify data that needs to be fixed before a simulation can be run (such as when you forget to define any material data).

Click on![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database. When the program is done writing the database, click on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) tab to run simulation.

## Simulating 1st Operation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

The progress of the simulation can be monitored as it is running by looking at the Simulation Message and Simulation Graphics in Simulation mode. Click the Simulation Message tab to view the Message file. As long as the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked, which is the default setting, the Message file will refresh every couple of seconds.

The Message file provides information about which simulation step the simulation is currently on and also gives information dealing with how well the simulation is running.

When the simulation has finished, the following message will be added to the end of the Message file:

"PROGRAM STOPPED!

***** PRESS ENERGY HAS BEEN FULLY CONSUMED.".

## Post-Processing the 1st operation Results

After simulation has been completed, click on ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) tab, MO post processor will open.

#### Load Stroke graph

**Plot Y Load-Stroke graph:**  
Click the ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) icon, the Load Stroke Graph window will open. Select the Top Die in Plot object list, in X-Axis pull down menu select Stroke and in Y-Axis pull down menu select Y Load. Click on options tab and check Step tracer check box, then click on ![]({{ '/assets/icons/post_icons/mo_plot_button.jpg' | relative_url }}). Click on ![]({{ '/assets/icons/pre_icons/mo_all_button.jpg' | relative_url }}) button in Step browser and Play animation (See Fig. L8.6.).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_08_hammer_press/2d_mobl8_image0006.jpg' | relative_url }})

Load Stroke Graph plot

**Plot Y Velocity -Stroke graph:**  
In Y-Axis pull down menu select Y-Speed and click on ![]({{ '/assets/icons/post_icons/mo_plot_button.jpg' | relative_url }}) and see the Graph. (See Fig. L8.7.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_08_hammer_press/2d_mobl8_image0007.jpg' | relative_url }})

Velocity Stroke graph plot

## Adding 2nd operation

After completion of Post processing, click on ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}) button, add another 2D Forming operation. In this operation we are using the same objects and we are doing second blow operation.

Click on second Forming operation in Operation editor, Select Interactive mode type in Setup type popup, then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Object page.

## Adding objects

In interactive mode all previous operation objects are added and their data is loaded from previous operation last step automatically, as shown in Fig. L8.8. As no new objects are required in 2nd operation and all objects data is loaded from previous operation last step select Top die Movement branch from object Tree.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_08_hammer_press/2d_mobl8_image0008.jpg' | relative_url }})

Interactive 2nd operation setup object page

## Assigning Top Die Movement

In Movement page, define **Energy** value as **250** **Klb-in**. Click on Contact branch in object tree.

## Generate Inter-object Contacts

Contact relation ship data has be already copied from previous operation as shown in Fig. L8.9., if not by selecting user type click on ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) button and select appropriate friction coefficient using ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) (Edit) button. After defining the friction coefficient for any relation same values can be copied to other relations using ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) button and use ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) icon to determine a suitable contact tolerance to generate the contacts using ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) button.

For this lab as inter-object relations data and contacts are loaded from previous operation no need to generate the contacts, so click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Step controls window.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_08_hammer_press/2d_mobl8_image0009.jpg' | relative_url }})

Inter-object Contact generation page

## Step Controls

In Step controls page, define Solution step definition with constant **die displacement** as **0.015** in and **number of steps** to **50**(see Fig. L8.10.). Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_08_hammer_press/2d_mobl8_image0010.jpg' | relative_url }})

Simulation controls

## Generating 2nd operation Database

In Generate DB page, click the ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) button to have the program check to see if anything was missed in the problem setup.

Click on the ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database. When the program is done writing the database, click on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) tab to run simulation.

## Simulating 2nd operation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

The progress of the simulation can be monitored as it is running by looking at the Simulation Message and Simulation Graphics in Simulation mode. Click the Simulation Message tab to view the Message file. As long as the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked, which is the default setting, the Message file will refresh every couple of seconds.

The Message file provides information about which simulation step the simulation is currently on and also gives information dealing with how well the simulation is running.

When the simulation has finished, the following message will be added to the end of the Message file:

"PROGRAM STOPPED!

***** PRESS ENERGY HAS BEEN FULLY CONSUMED.".

## Post-Processing the 2nd Operation Results

After simulation has been completed, click on ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) tab, MO post processor will open.

#### Load Stroke graph :

Review LOAD-STROKE and VELOCITY-STROKE plots of 2nd operation as shown in Fig. L8.11. and Fig. L8.12.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_08_hammer_press/2d_mobl8_image0011.jpg' | relative_url }})

Load verses Stroke Graph

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_08_hammer_press/2d_mobl8_image0012.jpg' | relative_url }})

Velocity verses Stroke Graph

## Closing MO Wizard

After completion of Post processing, save the Project and close the MO wizard by clicking Close ![]({{ '/assets/icons/pre_icons/mo_quit_icon.jpg' | relative_url }}) button or selecting Quit option under File menu.

**Related Topics:**

[15\. Movement Controls Settings](/docs/sk/pre_processor/15_movement_controls_definition/15_movement_controls_settings/)

[6.2. Integrated Manufacturing Process Simulation layout](/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_2_integrated_manufacturing_process_simulation_layout/)

[6.3. Integrated Manufacturing Process Post-processor layout](/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_3_integrated_manufacturing_process_post_layout/)

[25\. Post Processor Layout](/docs/sk/post_processor/25_post_processor_layout/25_post_processor_layout/)

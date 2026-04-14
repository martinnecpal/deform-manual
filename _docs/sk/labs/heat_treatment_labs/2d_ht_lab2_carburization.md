---
lang: sk
title: "2D HT Lab 2 Carburization"
---

# 2D HT Lab2 . Modeling of Carburization of a Gear Tooth

  
2.1. Opening Project file

2.2. Adding operation

2.3. Setting Simulation Controls

2.4. Setting Boundary Conditions

2.5. Generating a Database

2.6. Running a Simulation

2.7. Post-Processing the Results

## Opening Project File

The DEFORM GUI MAIN window should already be open. With the **Gear_Blank**.**moproj** file highlighted in the file list, click on ![]({{ '/assets/icons/pre_icons/mo_integrated_manufacturing_proc.jpg' | relative_url }}) as shown in Fig. 2DHTML2.1. Integrated Manufacturing Proc. will open.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab2_carburization/image0001.jpg' | relative_url }})

DEFORM GUI Main Window

## Adding operation

Add 2D Forming operation from Operations list in Explorer. Operation can be added by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button next to **2D****Forming** operation (see Fig. 2DHTML2.2.) or user can also add the operation by dragging and dropping the operation into Operation Editor region.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab2_carburization/image0002.jpg' | relative_url }})

Adding 2D Forming operation into Operation Editor

Select 2nd operation from Operation editor, Setup type popup will appear, click on ![]({{ '/assets/icons/pre_icons/mo_yes_interactive_setup_button.jpg' | relative_url }}) button. (See Fig. 2DHTML2.3.) Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab2_carburization/image0003.jpg' | relative_url }})

Setup type popup window

## Setting Simulation Controls

Select **Main![]({{ '/assets/icons/pre_icons/mo_main_setting.jpg' | relative_url }})** tab, Change the **Operation****Name** to **Carburization**. Turn on **Diffusion****module** and **turn****off** the **Deformation** module. (See Fig. 2DHTML2.4.)

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab2_carburization/image0004.jpg' | relative_url }})

Simulation Controls Main tab in expert mode

Select **Step****Increment**![]({{ '/assets/icons/pre_icons/mo_step_increment.jpg' | relative_url }}) tab, Set **Constant****Time****Increment** to **10** sec.(See Fig. 2DHTML2.5.)

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab2_carburization/image0005.jpg' | relative_url }})

Simulation controls Step increment tab in expert mode

Select **Stopping****Controls**![]({{ '/assets/icons/pre_icons/mo_stopping_criteria.jpg' | relative_url }}) tab, and set **Process****Duration** to **6000** seconds. (See Fig. 2DHTML2.6.)

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab2_carburization/image0006.jpg' | relative_url }})

Stopping control tab in Expert mode

Under **Process****Conditions** /**Diffusion** , set the value of the **reaction** rate **coefficient** to **0.0001** mm/s and the environmental **atom****content** should be set to **1.69** as shown in Fig. 2DHTML2.7. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Workpiece Boundary conditions page.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab2_carburization/image0007.jpg' | relative_url }})

Process Conditions tab in Expert mode

## Setting Boundary Conditions

At this point the user needs to define the boundary over which the carbon-bearing atmosphere is exposed to the workpiece. In this, the entire surface, both the outer surface and the bore surface, will be exposed to a carbon-bearing environment.

Click on Diffusion with the Environment. Select and assign boundary condition for both the bore of the gear and the outer surface of the gear as shown in Fig. 2DHTML2.8. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) till Generate DB page

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab2_carburization/image0008.jpg' | relative_url }})

Gear tooth section with diffusion with environment boundary conditions

## Generating a Database

In Generate DB page, click the ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) button to have the program check to see if anything was missed in the problem setup. During the checking process, messages in the red color signify data that needs to be fixed before a simulation can be run (such as when you forget to define any material data).If there are no errors shown, then the database can be generated.

Click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database (see Fig. 2DHTML2.9.). When the program is done writing the database, switch to ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) tab to run simulation.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab2_carburization/image0009.jpg' | relative_url }})

Generate DB window

## Running a Simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog.[](../tool_life_study_lab/tool_life_study_lab1.htm#Fig_TLSL1_17_Run_Options_Popup) Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

When the simulation is finished without any issues, the following message will be added to the end of the Message file as shown in Fig. 2DHTML2.10.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab2_carburization/image0010.jpg' | relative_url }})

Simulation Message tab

## Post-Processing the Results

After simulation has been completed, switch to ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) tab to view results, MO post processor will open.

The key state variable in this simulation is the Dominant Atom. Go to the last step of the database. Click the State Variables ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) button to open the state variable dialog. Select the variable Dominant Atom under Diffusion and plot the variable as a shaded contour. Click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) (see Fig. 2DHTML2.11.). The user should see the variable having an initial uniform value of 0.14. The value increases at the free boundaries, which indicates that the carbon is absorbed and diffused into the gear tooth.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab2_carburization/image0011.jpg' | relative_url }})

Diffusion Dominant atom plot

After completion of Post processing, Save the Project and close the MO wizard by clicking Quit ![]({{ '/assets/icons/pre_icons/mo_quit_icon.jpg' | relative_url }}) button or selecting Quit option under File menu. If User wants to continue the setup, can switch to pre mode directly and continue the setup by adding operation.

Related Topics:

[2D HT Lab1 Heating](/docs/sk/labs/heat_treatment_labs/2d_ht_lab1_heating/)

[2D HT Lab3 Diffusion](/docs/sk/labs/heat_treatment_labs/2d_ht_lab_3_diffusion/)

[2D HT Lab4 Quenching ](/docs/sk/labs/heat_treatment_labs/2d_ht_lab4_quenching/)

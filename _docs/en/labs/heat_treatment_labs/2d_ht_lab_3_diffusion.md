---
lang: en
title: "2D HT Lab 3 Diffusion"
---

# 2D HT Lab 3 Modeling of Diffusion of a Gear Tooth

  
3.1. Opening Project file

3.2. Adding Operation

3.3. Setting Simulation Controls

3.4. Generating a Database

3.5. Running a Simulation

3.6. Post-Processing the Results

## Opening Project File

The DEFORM GUI MAIN window should already be open. With the **Gear_Blank**.**moproj** file highlighted in the file list, click on ![]({{ '/assets/icons/pre_icons/mo_integrated_manufacturing_proc.jpg' | relative_url }}) as shown in [Fig. 2DHTML2.1.](2d_ht_lab2_carburization.htm#Fig_2DHTML2_1_DEFORM_GUI_Main_Window) Integrated Manufacturing Proc. will open.

## Adding Operation

Add 2D Forming operation from Operations list in Explorer. Operation can be added by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button next to **2D****Forming** operation or user can also add the operation by dragging and dropping the operation into Operation Editor region.

Select 3rd operation from Operation editor, Setup type popup will appear, click on ![]({{ '/assets/icons/pre_icons/mo_yes_interactive_setup_button.jpg' | relative_url }}) button. Select 3rd operation in Operation editor, double mouse click on it and change the name to "**Diffusion** " and press enter from keyboard. (See Fig. 2DHTML3.1.) Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) .

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab3_diffusion/image0001.jpg' | relative_url }})

Changing operation name from Operation Editor

## Setting Simulation Controls

Select **Step****Increment![]({{ '/assets/icons/pre_icons/mo_step_increment.jpg' | relative_url }}) **tab, Set Constant **Time****Increment** to **60** sec as shown in Fig. 2DHTML3.2.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab3_diffusion/image0002.jpg' | relative_url }})

Step Increment tab in expert mode

Select **Stopping****Controls![]({{ '/assets/icons/pre_icons/mo_stopping_criteria.jpg' | relative_url }}) **tab, and set **Process****Duration** to **13200** seconds. as shown in Fig. 2DHTML3.3.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab3_diffusion/image0003.jpg' | relative_url }})

Stopping Controls tab in Expert Mode

Click on the **Process****Conditions![]({{ '/assets/icons/pre_icons/mo_process_conditions.jpg' | relative_url }}) **tab in the Simulations Controls. Select **Diffusion** tab, Set the value of the reaction rate coefficient to **0** mm/s and the environmental atom content should be changed to **0** % atom as shown in Fig. 2DHTML3.4. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Generate DB page.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab3_diffusion/image0004.jpg' | relative_url }})

Process Conditions tab in expert mode

## Generating a Database

In **Generate****DB** page. Click the![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) button to have the program check to see if anything was missed in the problem setup. During the checking process, messages in the red color signify data that needs to be fixed before a simulation can be run (such as when you forget to define any material data).If there are no errors shown, then the database can be generated.

Click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database (see Fig. 2DHTML3.5.). When the program is done writing the database, switch to ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) tab to run simulation.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab3_diffusion/image0005.jpg' | relative_url }})

Generate Database window

## Running a Simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog.[](../tool_life_study_lab/tool_life_study_lab1.htm#Fig_TLSL1_17_Run_Options_Popup) Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation. As we click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) ****button simulation starts.

When the simulation is finished without any issues, the following message will be added to the end of the Message file as shown in Fig. 2DHTML3.6.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab3_diffusion/image0006.jpg' | relative_url }})

Simulation Message tab

## Post-Processing the Results

After simulation has been completed, switch to ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) tab to view results, MO post processor will open.

The key state variable in this simulation is the Dominant Atom. Go to the last step of the database. Click the State Variables ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) button to open the state variable dialog. Select the variable Dominant Atom under Diffusion and plot the variable as a shaded contour. Click on![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) (see Fig. 2DHTML3.7.). The user should see the variable in the similar state as in the end of the Carburization operation. In this simulation, the total amount of carbon holds constant but diffuses throughout the geartooth.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab3_diffusion/image0007.jpg' | relative_url }})

Diffusion Dominant atom plot

After completion of Post processing, Save the Project and close the MO wizard by clicking Quit ![]({{ '/assets/icons/pre_icons/mo_quit_icon.jpg' | relative_url }}) button or selecting Quit option under File menu. If User wants to continue the setup, can switch to pre mode directly and continue the setup by adding operation.

Related Topics:

[2D HT Lab1 Heating](/docs/en/labs/heat_treatment_labs/2d_ht_lab1_heating/)

[2D HT Lab2 Carburization](/docs/en/labs/heat_treatment_labs/2d_ht_lab2_carburization/)

[2D HT Lab4 Quenching ](/docs/en/labs/heat_treatment_labs/2d_ht_lab4_quenching/)

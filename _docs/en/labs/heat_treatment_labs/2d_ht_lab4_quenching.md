---
lang: en
title: "2D HT Lab 4 Quenching"
---

# 2D HT Lab4: Modeling of Quenching of a Gear Tooth

  
4.1. Opening Project file

4.2. Adding operation

4.3. Setting Simulation Controls

4.4. Setting Object Properties

4.5. Generating a Database

4.6. Running a Simulation

4.7. Post-Processing the Results

## Opening Project file

OThe DEFORM GUI MAIN window should already be open. With the **Gear_Blank**.**moproj** file highlighted in the file list, click on ![]({{ '/assets/icons/pre_icons/mo_integrated_manufacturing_proc.jpg' | relative_url }}) as shown in [Fig. 2DHTML2.1.](2d_ht_lab2_carburization.htm#Fig_2DHTML2_1_DEFORM_GUI_Main_Window) Integrated Manufacturing Proc. will open.

## Adding operation

Add 2D Forming operation from Operations list in Explorer. Operation can be added by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button next to **2D****Forming** operation or user can also add the operation by dragging and dropping the operation into Operation Editor region.

Select 4th operation from Operation editor, Setup type popup will appear, click on ![]({{ '/assets/icons/pre_icons/mo_yes_interactive_setup_button.jpg' | relative_url }}) button. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

## Setting Simulation Controls

Select **Main![]({{ '/assets/icons/pre_icons/mo_main_setting.jpg' | relative_url }}) **tab, Change the Operation Name to **Quench**. Turn off **Diffusion** module and turn on the **Deformation** module as shown in Fig. 2DHTML4.1.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab4_quenching/image0001.jpg' | relative_url }})

Simulation controls Main tab in Expert mode

Select **Step****Increment![]({{ '/assets/icons/pre_icons/mo_step_increment.jpg' | relative_url }}) **tab, Set solution Step Definition to Constant **Temperature**. Specify Initial/Minimum time step as 0.01 seconds per step and Max Temperature Change per Step should be set to 5 C. Max Temperature time step to 20 seconds per step. (See Fig. 2DHTML4.2.)

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab4_quenching/image0002.jpg' | relative_url }})

Step Increment tab in Expert mode

Select **Stopping****Controls![]({{ '/assets/icons/pre_icons/mo_stopping_criteria.jpg' | relative_url }}) **tab, and set **Process****Duration** to **13500** seconds as shown in Fig. 2DHTML4.3.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab4_quenching/image0003.jpg' | relative_url }})

Stopping Controls tab in Expert mode

Under Process Conditions,Set the **environment****temperature** to **20** C and change the **convection** **coefficient** to **4.093** as shown in Fig. 2DHTML4.4. This convection coefficient is similar to the convection coefficient of certain quench oil. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Workpiece Property page.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab4_quenching/image0004.jpg' | relative_url }})

Process Conditions window

## Setting Object Properties

At this point the user will set the hardness calculation type to volume fraction method. Click on the workpiece Property tab. Set the **Hardness** estimation type to **Using****Volume****Fractions**.as shown in Fig. 2DHTML4.5.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab4_quenching/image0005.jpg' | relative_url }})

Object property window

## Generating a Database

In Generate DB page. Click the ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) button to have the program check to see if anything was missed in the problem setup. During the checking process, messages in the red color signify data that needs to be fixed before a simulation can be run (such as when you forget to define any material data).If there are no errors shown, then the database can be generated.

Click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database (see Fig. 2DHTML4.6.). When the program is done writing the database, switch to ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) tab to run simulation.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab4_quenching/image0006.jpg' | relative_url }})

Generate Database

## Running a Simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog.[](../tool_life_study_lab/tool_life_study_lab1.htm#Fig_TLSL1_17_Run_Options_Popup) Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation. As we click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) ****button simulation starts.

When the simulation is finished without any issues, the following message will be added to the end of the Message file as shown in Fig. 2DHTML4.7.

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab4_quenching/image0007.jpg' | relative_url }})

Simulation message tab

## Post-Processing the Results

After simulation has been completed, switch to ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) tab to view results, MO post processor will open.

The user may be interested in the state variables Phase Volume Fractions. Go to the last step of the database. Click the State Variables ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) button to open the state variable dialog. Select the variable Volume Fractions(Pearlite) under Microstructure and plot the variables as shaded contours. This gives the prediction of the microstructure of the gear tooth as a function of position. At the end of quench, the material near the surface is mostly Martensite, while the center is mostly Pearlite. In addition, the user may be concerned about the quench distortion and residual stress that are caused by the heterogeneous transformation volume changes and thermal contraction. To examine the distortion, select the variable Total Displacement under Deformation and plot the variables as Deflection plot. You may like to drag the Deflection Scale bar to amplify the deflection. For residual stress, select the Effective Stress and plot the variable as shade contour. ( See Fig. 2DHTML4.8. to Fig. 2DHTML4.10.).

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab4_quenching/image0008.jpg' | relative_url }})

Volume-Fraction Pearlite plot

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab4_quenching/image0009.jpg' | relative_url }})

Volume-Fraction Martensite plot

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab4_quenching/image0010.jpg' | relative_url }})

Volume-Fraction Austenite

Another important state variable in this simulation is the Hardness variable. Select the variable Hardness under Microstructure and plot the variables as shaded contours. You can see that the hardness (in Rockwell C) is high where Martensite is high and low where Pearlite is high.( Fig. 2DHTML4.11.)

![]({{ '/assets/images/labs/heat_treatment_labs/2d_ht_lab4_quenching/image0011.jpg' | relative_url }})

Hardness plot

After completion of Post processing, Save the Project and close the MO wizard by clicking Quit ![]({{ '/assets/icons/pre_icons/mo_quit_icon.jpg' | relative_url }}) button or selecting Quit option under File menu. If User wants to continue the setup, can switch to pre mode directly and continue the setup by adding operation.

Related Topics:

[2D HT Lab1 Heating](/docs/en/labs/heat_treatment_labs/2d_ht_lab1_heating/)

[2D HT Lab2 Carburization](/docs/en/labs/heat_treatment_labs/2d_ht_lab2_carburization/)

[2D HT Lab3 Diffusion](/docs/en/labs/heat_treatment_labs/2d_ht_lab_3_diffusion/)

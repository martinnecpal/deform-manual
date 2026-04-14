---
lang: en
title: "6.2. Integrated Manufacturing Process Simulation layout"
---

# 6.2. Integrated Manufacturing Process (MO) Simulation layout

6.2.1. Simulation Options

  * Run

  * Run Options

  * Stop

  * Continue

  * Refresh

6.2.2. Simulation Jobs tab

6.2.3. Simulation Message tab

6.2.4. Simulation LOG tab

6.2.5. Simulation graphics

  * Simulation graphics tool bar options

  * Right Mouse Button options

6.2.6. Step View and Monitor window

  * Simulation Monitor Window

  * Step View window

MO Simulation mode is used to submit the problem setup to simulate and monitor the simulation progress. Simulation mode GUI layout (See Fig. 6.2.1.) is mainly divided into Simulation Graphics, Simulation Jobs, Message and Log and Simulation running options.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image001.jpg' | relative_url }})

MO Simulation Mode Layout

## Simulation Options

Simulation options are used to start, stop and continue simulation along with refresh simulation display as shown in Fig. 6.2.2.

The main Simulation options Run, Run options, Stop, Continue and Refresh are explained as below,

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image002.jpg' | relative_url }})

Simulation options

**Run**

The simulation can be started by clicking ![]({{ '/assets/icons/simulator_icons/mo_run_icon.jpg' | relative_url }}) (Submit simulation of current project) icon or ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }})action label or Submit Simulation option from Simulation menu (See Fig. 6.2.3.) and selecting an appropriate run simulation options. This initiates a series of actions to run the simulation and generate new meshes as necessary. Run simulation provides three options to run a simulation interactively, those are,

  * **Start from last negative step** : This will start the simulation from the last negative step of the database. To start a simulation negative step is must, any changes made to the setup in preprocessor will be written to the negative step of DB. Now we can run the job in Interactive mode by unchecked Add simulation job to the queue check box and in Batch mode by checked Add simulation job to the queue check box (Fig. 6.2.3.).

  * **Start from beginning (Initial Run)** : Starts the simulation from first step (-1) of the database. (See Fig. 6.2.3.)

  * **Add Simulation job to the Queue** : This will add the job to queue and job will simulate the job in Batch mode using available simulation server. We can add the job in queue using Start from last negative step and Start form beginning (Initial Run) options.

![]({{ '/assets/icons/simulator_icons/run_simulation_mo.jpg' | relative_url }})

Run Simulation options

**********Run Options******

![]({{ '/assets/icons/simulator_icons/mo_run_options_action_lable.jpg' | relative_url }}) action label or Simulation menu Run (options) will provide more advanced options to run the simulation like interactive or batch mode, running with single and multiple (only for 3D) processors and 32 and 64 bit running.

  * **Job Type** : This Indicates type of the running jobs like MO (Multiple operations), DOE (Design of Experiments) or OPT (Optimization).

  * **DB Name/Problem ID** : Displays the current project DB name in case of normal MO operations project. For DOE and OPT it shows the Problem ID as DOE/OPT project name, required DB's to complete DOE/OPT study are generated after submitting the problem to simulate.

  * **Submitted By** : It will display the project location machine name.

  * **Password to Kill Job** : If user used any password to protect simulation in simulation server of DEFORM setup then that password should be entered here before selecting ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) or ![]({{ '/assets/icons/simulator_icons/mo_submit_to_qeue_button.jpg' | relative_url }}) buttons to start the simulation.

  * **Simultaneous Jobs** : User can indicate number of simulations or Jobs that can be run simultaneously and this number should be equal to or less than the maximum number of jobs specified in DEFORMSetup and also based on the license available. This option is available only for DOE/OPT jobs submission in queue.

  * **Simulation Mode** : There are two simulation modes those are,

  
![]({{ '/assets/icons/simulator_icons/mo_interactive_mode_rb.jpg' | relative_url }}) : Using this option, user can run simulations without simulation server by selecting ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button. This option does not require simulation server to be running. (See Fig. 6.2.4.) 

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image003.jpg' | relative_url }})

Run options window for MO job in interactive simulation mode

  
Interactive simulation mode settings are,

**Computer Name:** This will display the name of the Machine

**Type** : This will display whether it is a Single or Multi Processor simulation

**Path on Computer:** This will display the path of the DB and in case of DOE/OPT it indicates the path where DB's would be generated.

**Processors Per Job:** Using this option user can select the number of processors required to be used per job during simulation, currently available only for 3D simulation or job.

**Shared Memory Size:** It displays Shared Memory allocated on the simulation server system for DEFORM simulation.

User can save the settings using ![]({{ '/assets/icons/pre_icons/mo_save_button.jpg' | relative_url }}) button and close the Run options window using ![]({{ '/assets/icons/pre_icons/mo_close_button.jpg' | relative_url }}) button.

![]({{ '/assets/icons/simulator_icons/mo_batch_mode_rb.jpg' | relative_url }}) : Using this option, user can run simulations only in batch mode (See Fig. 6.2.5.). It is essential to select any one of the available simulation servers listed or first available simulation server to simulate batch queue problems and click on ![]({{ '/assets/icons/simulator_icons/mo_submit_to_qeue_button.jpg' | relative_url }}) button to start adding job to the queue. The displayed list contains only simulation servers that are added to the DEFORM Setup.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image004.jpg' | relative_url }})

Run options window for MO job in batch simulation mode

  
In Batch simulation mode selected simulation servers settings can be set by selecting the particular simulation server and clicking on ![]({{ '/assets/icons/simulator_icons/mo_submit_to_qeue_button.jpg' | relative_url }}) button. (See Fig. 6.2.6.)

![]({{ '/assets/icons/simulator_icons/mo_server_settings_button.jpg' | relative_url }}): Using this button user can set the selected simulation server settings like processors to be utilized per job during simulation and shared memory.

**Server Name** : This will display the selected simulation server machine name

**Type** : This will display whether it is a Single or Multi Processor simulation

**Path on Server** : This will display path of the DB if user selected the local machine as simulation server or else will display as "Copied from :<Phisical_DB_existing_Machine_name>"

**Processors Per Job** : Using this user can select the number of processors to be used per 3D simulation or job.

**Shared Memory Size:** It displays Shared Memory allocated on the simulation server  
system for DEFORM simulation.

  
User can save the settings using ![]({{ '/assets/icons/pre_icons/mo_save_button.jpg' | relative_url }}) button and close the Run options window using ![]({{ '/assets/icons/pre_icons/mo_close_button.jpg' | relative_url }}) button.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image005.jpg' | relative_url }})

Batch simulation mode server settings

  
**Simulation Run types:** For normal multiple operations project in both interactive and batch mode user can run the simulation from the initial step or if it is stopped in between or wanted to restart from the mod we can do so by continue options. (See Fig. 6.2.7.)

**Initial Run:** This will start the simulation from the first operation starting step. User can also use this option to restart the simulation from the beginning in case of simulation has stopped in the mid due to some license or network issues.

**Continue Run:** This continue run will provide two options those are, 

  * **Continue from the last step:** This will continue the simulation from the last available negative step. It is useful when user done some corrections to the setup and tries to restart from any stage of the simulation.
  * **Restart from the selected Simulation:** This will restart the simulation from any of the intermediate operation's simulations by selecting that particular operation and its simulation.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image006.jpg' | relative_url }})

Simulation Run types from Run options for normal projects

  * **Run Simulation on** :

DOE or OPT projects has to be simulated only in batch mode, for these projects with multiple DB's to be simulated, user can run all the DB's or Run cases in single or multiple simulation servers.

  * **Single Simulation Server:**

User can run multiple DB's or Run cases in any one of the available simulation servers in the list. User can select the number of simultaneous simulation to simulated up to available number of licenses based on the requirement. (See Fig. 6.2.8.)

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image007.jpg' | relative_url }})

Run options window for DOE job using single sim server

  * **Multiple Simulation Servers:**

From version 11.1 user can run the batch queue jobs using the remote machine simulation servers, using the simulation server other than the local will provide opportunity to reduce the load on the local will provide opportunity to reduce the load on the local simulation servers and also the time required to complete the DOE/OPT project.

To use multiple simulation severs user needs to check the checkbox next to the available simulation servers listed in the table. User can change the simulation severs settings, Multiple processors per job and MPI shared memory as mentioned in the batch simulation mode. In addition to the batch simulation mode settings for DOE and OPT, user needs to set maximum Jobs per simulation server in server settings. (See Fig. 6.2.9.) 

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image008.jpg' | relative_url }})

Run options window for DOE job using multi sim server

  
For DOE and OPT simulations, simulation server settings can be edited by selecting the particular simulation server and clicking on ![]({{ '/assets/icons/simulator_icons/mo_server_settings_button.jpg' | relative_url }}) button. Refer  Server_Settings for most of the server settings.

  
**Max Jobs:** User can indicate maximum number of simulations that can be run simultaneously and this number should be equal to or less than the maximum number of jobs specified in DEFORMSetup for each simulation server and also based on the license available. This option is active only for DOE/OPT jobs submitted in queue. (See [Fig. 6.2.10.](6_2_integrated_manufacturing_process_simulation_layout.htm#Fig._6.2.10._DOE_/_OPT_project_sim_server_settings_window))

User can save the settings using ![]({{ '/assets/icons/pre_icons/mo_save_button.jpg' | relative_url }}) button and close the Run options window using ![]({{ '/assets/icons/pre_icons/mo_close_button.jpg' | relative_url }}) button.

  
![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image009.jpg' | relative_url }})

DOE / OPT project sim server settings window

  
**Files to copy** : Create a new file with name "FILES_TO_COPY" inside the working directory without any extension. The file can be edited with notepad or Wordpad or with any text editor. User can enter the name of the files like *.DAT in [**FILES_TO_COPY**](../../appendices/appendix_xvii_data_files.htm#FILE_TO_COPY) file that are necessary to be copied to the remote system or to Run folders in DOE/OPT in addition to default files that are copied.

**Simulation Run types:** For DOE/OPT projects user can start the simulation from the first operation or if DOE/OPT variables added only from the intermediate operations then user can continue only from those intermediate operations. Even if DOE/OPT simulation stops abnormally then user can restart the incomplete projects from runs where it stopped and also these incomplete runs can be restarted from the intermediate operations. (See [Fig. 6.2.11.](6_2_integrated_manufacturing_process_simulation_layout.htm#Fig._6.2.11._Simulation_Run_types_for_DOE/OPT_projects))

  * **Initial Run:** This initial run will provide two options those are, 

  * **Start from the beginning:** This will start the simulation from the first operation starting step. User can also use this option to restart the simulation from the beginning in case simulation has stopped in the mid due to some license or network issues.

  * **Start from the Selected Simulation:** This will start the simulation from any of the intermediate operation's simulations by selecting that particular operation and its simulation. If user added DOE study only in the intermediate operation then using this option will reduce the total time required to complete DOE study.

  * **Continue Run:** This continue run will provide two options those are,

  * **Continue incomplete DOE study:** This will continue the incomplete DOE study simulations from the last available negative step and complete the DOE/OPT project.

  * **Restart DOE from the selected Simulation:** This will continue the incomplete DOE study runs simulations from any of the intermediate operations simulations by selecting that particular operation and its simulation.

  
Continue does not need to run successfully simulated DOE run cases again to complete the incomplete DOE project.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image010.jpg' | relative_url }})

Simulation Run types for DOE/OPT projects

  * **Simulation Options:**

  * **64bit**

Based on the Operating system user can choose the Run type as 64 bit, if user wont check 64 bit checkbox then the run type will be 32bit. In 64 bit machine we can use either 32 bit or 64 bit option based on the processing speed required. From version 11.1 64bit option is available even for 2D problems.

  * **Partially Parallel FEM**

Option runs only the solver part of the simulation in parallel mode, while the other operations like model stiffness matrix, remeshing and interpolation are run in single CPU on the primary host machine. In PC environment this results in the execution of one DEF_SIM_P4.EXE on each of the processors requested.

  * **Keep the message file**

This prevents the message file from being deleted after each remesh by renaming it to a unique name for each simulation run.

  * **Auto Report**

When Auto Report is turned on system will generate report for the project with default template even though report generation operation is not added in batch mode. 

  * **Parallel meshing** :

Using this option we can reduce remeshing time for large models by distributing the remeshing of independent zones of the solid mesh across multiple processors. Multiple processors defined for running simulations will be used to distributethe zones.

**Surface + Solid:** Parallel meshing will be applied for both surface and solid meshing.

**Solid only:** Parallel meshing will be applied only for solid meshing. 

  * **No automatic remeshing (for no convergence)**

This prevents the simulation from automatic remeshing of an object, if the simulation stops due to convergence problems.

**Stop**

The simulation can be stopped at the current step by using the ![]({{ '/assets/icons/simulator_icons/mo_stop_icon.jpg' | relative_url }}) (Stop) icon or ![]({{ '/assets/icons/simulator_icons/mo_stop_action_label.jpg' | relative_url }}) action label or Simulation menu option Stop Simulation. (See Fig. 6.2.1.) Stopping the simulation changes the status from Running to Aborting in the simulating jobs tab or Process Monitor window. After stopping the current simulation it will take the pending jobs in queue to simulate. If the simulation is performing the remesh then we can not stop the problem, only after completing the remesh we can stop the simulation. In the simulation message tab " *** Simulation Aborted by User ***" message will appear after stopping the simulation.

**Continue**

The stopped simulation can be continued by using the ![]({{ '/assets/icons/simulator_icons/mo_continue_action_label.jpg' | relative_url }}) action label or Continue Simulation option from simulation menu. In background this will automatically generate the database from pre-processor at last step of database, required to start simulation.

**Refresh**

Refresh is used to update the simulating job status and informations like simulation message and log file along with the simulation graphics display.

## Simulation Jobs tab

The Simulation job will display the status of simulation submitted from the current MO project (See Fig. 6.2.12.). The status of job could be Running, Remeshing or Pending (when delay in simulation start or when in queue). Refresh button in the simulation options can be used to refresh the status and even to update the status as and when required. For more information on the jobs user can refer to the Simulation menu Process Monitor option. Refer the chapter [2](/docs/en/simulator/23_deform_simulator/23_4_process_monitor/)[3.4. Process Monitor](/docs/en/simulator/23_deform_simulator/23_4_process_monitor/) for details.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image011.jpg' | relative_url }})  
(a) 

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image012.jpg' | relative_url }})  
(b) 

Simulation jobs tab; (a) FEM running status (b) REMESH running status

## Simulation Message tab

Run-time information will be written to the ProblemId.MSG and ProblemId.LOG files. Execution information, including convergence information for each step and simulation error messages, can be found in the .MSG file. For normal stop it gives the message at the end as "NORMAL STOP: The assigned steps have been completed" and for simulation aborted by user the message will be displayed as " *** Simulation Aborted by User ***".

## Simulation LOG tab

The Information on simulation and remeshing, execution times, fatal errors and type of FEM job running (32-bit or 64-bit simulation) in case of 3D job can be found in the .LOG file. When simulating the Multiple operations project, it even records the DB checking, DB generation, scheduled remesh, positioning and contact generation messages. So it is help full to investigate in case of setup related mistakes.

## Simulation graphics

While the simulation is running, the second most recent saved step can be viewed. Many different variables can be viewed such as plastic strain, plastic strain rate, temperature and many more. (See Fig. 6.2.1.)

**Simulation graphics tool bar options:**

The simulation graphics tool bar contains the state variables window icon ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) and major state variables contour icons ![]({{ '/assets/icons/post_icons/mo_temp_sv.jpg' | relative_url }}) (Temperature),![]({{ '/assets/icons/post_icons/mo_damage_sv_icon.jpg' | relative_url }}) (Damage), ![]({{ '/assets/icons/post_icons/mo_vel_sv_icon.jpg' | relative_url }}) (Velocity), ![]({{ '/assets/icons/post_icons/mo_disp_sv_icon.jpg' | relative_url }}) (Displacement), ![]({{ '/assets/icons/post_icons/mo_eff_stress_sv_icon.jpg' | relative_url }}) (Effective stress), ![]({{ '/assets/icons/post_icons/mo_strain_sv_icon.jpg' | relative_url }}) (Effective strain) and ![]({{ '/assets/icons/post_icons/mo_strain_rate_sv_icon.jpg' | relative_url }}) (Effective strain rate). The plotted state variables can be removed using the ![]({{ '/assets/icons/post_icons/mo_clear_sv_icon.jpg' | relative_url }}) (Clear) icon. For more detailed information about state variables refer to the NG Post mode section [26.6.3](/docs/en/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_3_state_variables/)[. State Variables](/docs/en/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_3_state_variables/).

Other options like Object mode ![]({{ '/assets/icons/post_icons/mo_show_user_defined_obj_icon.jpg' | relative_url }}), Contact display ![]({{ '/assets/icons/post_icons/mo_show_cotact_icon.jpg' | relative_url }}), Contour plot types , Summary ![]({{ '/assets/icons/post_icons/mo_summary_icon.jpg' | relative_url }}) , Load-Stroke graph ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}), Mirror symmetry ![]({{ '/assets/icons/post_icons/mo_3d_mirroring_icon.jpg' | relative_url }}) , Slicing ![]({{ '/assets/icons/post_icons/mo_slicing_option.jpg' | relative_url }}) , Measurement ![]({{ '/assets/icons/post_icons/mo_measure_tool.jpg' | relative_url }}) and 3D view ![]({{ '/assets/icons/post_icons/mo_3d_view_icon.jpg' | relative_url }}) ,3D setup ![]({{ '/assets/icons/post_icons/mo_3d_setup_icon.jpg' | relative_url }}) (only for 2D models) and Display Properties ![]({{ '/assets/icons/post_icons/mo_disp_porp_icon.jpg' | relative_url }}) are also available in Simulation graphics and are explained below,

**![]({{ '/assets/icons/post_icons/mo_show_user_defined_obj_icon.jpg' | relative_url }})Object mode** : User can toggle the object's Display, Geometry, Mesh, Transparency (only for 3D) modes independently. This can be done by turning on/off respective check boxes as shown in [Fig. 6.1.22.](6_1_integrated_manufacturing_process_preprocessor_layout.htm#Fig._6.1.22._User_defined_Object_Mode_window)

![]({{ '/assets/icons/post_icons/mo_show_cotact_icon.jpg' | relative_url }}) **Show Contact Nodes** : Turns on the contact display for the selected object from object tree with all other objects. (See [Fig. 6.1.22.](6_1_integrated_manufacturing_process_preprocessor_layout.htm#Fig._6.1.22._User_defined_Object_Mode_window))

![]({{ '/assets/icons/post_icons/mo_contour_line_icon.jpg' | relative_url }}) **Contour Line** : This plots the state variables in line contour mode. User can change contour plot type, color bar type, label type, its significants etc as shown in Fig. 6.2.13. and Fig. 6.2.14.

![]({{ '/assets/icons/post_icons/mo_contour_smooth_icon.jpg' | relative_url }})**Contour Smooth** : This plots the state variables in smooth shaded contour mode as shown in Fig. 6.2.14.

![]({{ '/assets/icons/post_icons/mo_contour_solid_icon.jpg' | relative_url }}) **Contour Solid** : This plots the state variables in solid contour mode as shown in Fig. 6.2.14.

**![]({{ '/assets/icons/post_icons/mo_contour_vector_icon.jpg' | relative_url }})Contour Vector** : This plots the state variables in vector contour mode.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image013.jpg' | relative_url }})

Line, smooth and solid contour display example

  
**Color bar options:** After plotting different contour types as shown in Fig. 6.2.14., user can right click on the color bar and change its properties (See Fig. 6.2.16.).

  * **Hide colorbar:** This hides the color bar from simulation graphics.

  * **Plot type:** Using this user can plot different contour types (See Fig. 6.2.14.) for objects like Line, Smooth shading, Solid, Elemental shading, Iso surface, Deflection and MinMax. (See Fig. 6.2.14.)

  
![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image015.jpg' | relative_url }}) ![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image014.jpg' | relative_url }})

  
(a) (b)

Contour bar plot type options; (a) For 3D (b) For 2D

  * **Scale type:** Using this user can plot the contours by considering only the current step max and Min values (Local) or All currently available steps max and Min values (Global) or required available range can be set under then user defined type (within the Global). (See Fig. 6.2.15.)

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image016.jpg' | relative_url }})

Contour bar scale type options

  * **Colorbar type** : Using this user can select standard color combination contours or user defined color bar types.(See Fig. 6.2.16.)

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image017.jpg' | relative_url }})

Contour bar colorbar type options

  * **Label type** : Using this user can change the color bar values display types to Float decimal, Float significants, Exponential and Auto. (See Fig. 6.2.17.)

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image018.jpg' | relative_url }})

Contour bar label type options

  * **Significants:** Using this user can change the color bar values number of significants. (See Fig. 6.2.18.)

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image019.jpg' | relative_url }})

Contour bar significants option

  * **Display Min/Max:** Checking this check box will display Min and Max values of the state variable contour at current step.

  * **Change values color:** Using this user can change color of the color bar values.

  * **Change values font:** Using this user can change font type, style and size of the color bar values displaying.

  * **Color Bar Preference:** This provides two options display friendly and print friendly based on the requirement. (See Fig. 6.2.19.)

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image020.jpg' | relative_url }})

Contour bar colorbar Preference

  
**Summary** ![]({{ '/assets/icons/post_icons/mo_summary_icon.jpg' | relative_url }}) : Certain characteristic data, such as press loads, principle die velocities and maximum and minimum values of state variables are stored for every simulation step, whether complete data is stored for that step or not in the respective tabs. This summary data vs time graphs for all the saved steps can be viewed in the graphics window. For more information refer the Section [26.6.6. Summary Graphs](/docs/en/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_6_summary/).

Load/Stroke Graphs ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}): The graphs window is used to generate load, speed, torque, angular velocity, energy and volume vs. time (or stroke) plots for the object. For more information refer the Section [26.6.7. Load Stroke](/docs/en/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_7_load_stroke/) Graphs.

Mirror Symmetry ![]({{ '/assets/icons/post_icons/mo_3d_mirroring_icon.jpg' | relative_url }}) : The purpose of object mirroring and symmetry is to allow the user to visualize the object both sides of the centerline of a part for 2D and in 3D user can visualize the entire part from symmetry model. For more information refer the Section [26.6.15. Mirror Symmetry](/docs/en/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_15_mirror_symmetry/).

  
**Interactive Slicing** ![]({{ '/assets/icons/post_icons/mo_slicing_option.jpg' | relative_url }}) :

[3D]: The slicing dialog allows the user to cut a section into the workpiece. When the section is made, shaded contours can be seen in the cut area. For more information refer the Section [26.6.15.Slicing](/docs/en/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_16_interactive_slicing/).

  
**Delete Slicing**![]({{ '/assets/icons/post_icons/mo_del_slicing_icon.jpg' | relative_url }}) :

**[3D]:** The Sliced plane can be deleted by clicking on this option to see the un-sliced object.

  
**Measurement**![]({{ '/assets/icons/post_icons/mo_measure_tool.jpg' | relative_url }}) : For this option refer the next Section 6.2.5.2. Right Mouse Button options -Measure .

**3D View![]({{ '/assets/icons/post_icons/mo_3d_view_icon.jpg' | relative_url }}) : **[2D]:This is used to view the 2D simulation results by revolving or extruding the objects into 3D.

**3D Setup** ![]({{ '/assets/icons/post_icons/mo_3d_setup_icon.jpg' | relative_url }}) : [2D]: The revolved or extruded 2D simulation results 3D view settings can be controlled by using 3D Setup. For more information on 3D View and Setup refer the [Section 26.6.20. 3D Viewer and Setup](/docs/en/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_20_3d_setup/).

  
For Menu bar and Tool bar options like Axis views, Display rendering modes, View fit, Display Refresh and Display modification options (Zoom, Pan, Rotate) refer the sections [6.4.1.2.Viewport Menu](6_4_main_menu.htm#Viewport_Menu), [6.4.1.3.Display Menu](6_4_main_menu.htm#Display_menu) and [6.4.1.4.Mouse Menu.](6_4_main_menu.htm#Mouse_Menu)

  
**Display Properties** ![]({{ '/assets/icons/post_icons/mo_disp_porp_icon.jpg' | relative_url }}): This option used to define the Define the DB info and Title Labels to display in Graphical Display window. (See Fig. 6.2.20.)

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image021.jpg' | relative_url }})

Display Properties window

**Right Mouse Button options**

DB Info: This by default displays the DB name, while simulating it shows the DB name as "FOR003", after completing it Shows the User Default, actual DB name. DB path, DB folder, Simulation title, Operation Name, Simulation Name can also be set as DB Info in the Simulation Monitor window as shown in Fig. 6.2.21.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image022.jpg' | relative_url }})

DB Info display options

**Title:** Title will by default displays the User Defined, Step number. Process Time, Die Stroke and Remaining Stroke. User can set one of these options as Title in the Simulation Monitor window as shown in Fig. 6.2.22.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image023.jpg' | relative_url }})

Title Display options

**  
Show Dimensions:** This will display the major dimensions for the displaying objects.

**Show current Object Mark:** This will highlight the current selected object by marks at boundary to identify when multiple objects mode is selected.

**Show View Axis:** This will hide or show the axis in graphics display window.

  
**Colorbar:** This will hide or display the state variable contour color bar in graphics display window.

  
**Load and Save Viewport:** The user can move or change the views of the geometries by using display tools such as pan, dynamic zoom and box zoom in the display window. These views can be saved using save option. For more information refer the [Section 6.4.1.2.6. Load and Save viewport](6_4_main_menu.htm#Load_and_Save).

  
**Objects Display mode:** This is used to select the different objects display modes like Single, Multiple and User. Selecting this option will give popup to the user defined object selection window as shown in

Fig. 6.2.23.

  
**Contact display** ![]({{ '/assets/icons/post_icons/mo_show_cotact_icon.jpg' | relative_url }}) : This turns on the contact nodes display of all objects in display window. Contact nodes display types can also be changed to Region, Node and Region, Show Underfill and self contact region as shown in Fig. 6.2.23.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image024.jpg' | relative_url }}) ![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image025.jpg' | relative_url }})

  
(a) (b)

Contact Display RMB options; (a) For 2D (b) For 3D

  
**Display Option:** After turning on the contact display (![]({{ '/assets/icons/post_icons/mo_show_cotact_icon.jpg' | relative_url }})), this option can be used to change the contact display type to point or polygon and the point size as shown in Fig. 6.2.24.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image026.jpg' | relative_url }})

(a) Selected node Display options

  
![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image027.jpg' | relative_url }})  
(b) point size Display options

Display options

  
**Calculate Contact Area: [3D]** This option will calculate the contact area for the deformable object and popup the area information with respective objects as shown in Fig. 6.2.25.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image028.jpg' | relative_url }})

Calculated contact area information popup

  
**Measurement Style****![]({{ '/assets/icons/post_icons/mo_measure_tool.jpg' | relative_url }})**: This tool allows the user to measure any distance between two points by clicking consecutively on both points. The measurement can be plot in either X or Y or XY direction, in 3D Z direction will come into picture, using the CAD style option available which displays the measured values in the selected direction.(See Fig. 6.2.26.) 

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image029.jpg' | relative_url }})  
(a) (b)

Measure RMB options; (a) For 2D (b) For 3D

  
**Measurement options:** This provides to clear previous measurements, modify different font size and backgound color for the measurement display in the graphics display window as shown in Fig. 6.2.27\. 

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image030.jpg' | relative_url }})

Measurement background color option

  
**Background Theme:** Using this option user can select the different background themes available like Navy blue, White, Black and Gray for the graphics window.

**Show title bar:** This option can be used to show the Title bar of simulation graphics window.

  
**Change feature angle:** User can use this option to change the range of selections when selecting the elements/nodes/polygons for adding BCC or editing geometry etc. using surface patch method. It displays the surface patch by treating surfaces within the feature angle as the one surface. A curved surface with smaller feature angle means fewer surface polygons will be picked at a time. Selecting the option Change feature angle pops up the feature angle changing window as shown in Fig. 6.2.28.

  
Also see the Fig. 6.2.29. for the surface patch display for the die geometry with different feature angle.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image031.jpg' | relative_url }})

3D feature angle entry window

  
![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image033.jpg' | relative_url }}) ![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image032.jpg' | relative_url }})

(a) (b)

Surface path display with different feature angle; (a) For angle 10 (b) For angle 20

## Step View and Monitor window

**Simulation Monitor Window**

Simulation Monitor window will be displaying the % of simulation completed using progress bar, % value and the completed number of steps out of defined total number of steps is as shown in Fig. 6.2.30. It also gives a update button by clicking on it will update the DB step in simulation graphics window also we can use auto update check box to update automatically based on selected monitoring type.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image034.jpg' | relative_url }})

Simulation Monitor Window

  
**Monitoring:** This option is used update the graphics display of the current step or Last saved step or to automatically update the steps as simulation running as shown in Fig. 6.2.31.

  * **Auto:** This automatically updates the saved step while simulating in simulation graphics.
  * **Current Step:** This shows the current step in simulation graphics.
  * **Last Saved Step:** This shows the last saved step in simulation graphics.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image035.jpg' | relative_url }})

Monitoring RMB options

DB Info and Title options can be used to view certain useful information related to simulation like DB path, operation name and simulation title, current step, process time, current die stroke and remaining stroke. For more information refer the Section 6.2.5.2. Right_Mouse_Button_options.

**Step View window**

While the Monitoring option in Simulation monitor window will update the simulation step based on selection, any step till the current simulated steps can be reviewed using Step viewer. Step Viewer window tab will be named from "Operation Name and Simulation Title".

  
Step viewer is used to select simulated steps for review, selected step objects will be displayed in the graphics window. Step view window has options for selecting different steps & operations, step tools for quick step selection & playing steps. Step view window also displays information like simulation title, operation name, stroke, time, selected step and operation number. (See Fig. 6.2.32.)

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image036.jpg' | relative_url }})

Step view window

  
There are also four additional ways to monitor a simulation those are,

  1. Use the Process Monitor to determine the current step number.
  2. Read the message file to determine the current step number and iteration information.
  3. Open the simulation in the Post-Processor. During a simulation the database file is renamed to FOR003 and is renamed back to the original database file name upon remeshing and stopping/completion.
  4. Depending up on the frequency of the steps saved in the database, it is recommended to opt for saved steps display rather than the current step.

  
**Related Topics:**

[23.3. Simulation Graphics](/docs/en/simulator/23_deform_simulator/23_3_simulation_graphics/)

[23.4. Process Monitor](/docs/en/simulator/23_deform_simulator/23_4_process_monitor/)

[23.5. Setting up MPICH](/docs/en/simulator/23_deform_simulator/23_5_setting_up_mpich/)

[23.6. Running Shared folder Simulations](/docs/en/simulator/23_deform_simulator/23_6_running_shared_folder_simulations/)

[23.8. Trouble Shooting Simulation Running](/docs/en/simulator/23_deform_simulator/23_8_trouble_shooting_simulation_running/)

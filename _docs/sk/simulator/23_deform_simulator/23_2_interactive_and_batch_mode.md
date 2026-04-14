---
lang: sk
title: "23.2. Interactive and batch mode"
---

# 23.2. Interactive and batch mode

23.2.1. Interactive Mode

23.2.2. Batch Queue Mode

23.2.3. Queuing Simulations

  * Running Batch Queue Server and Simulation Server

  * Computer configuration requirements

  * Simulation Server setup

23.2.4. Run Options dialog features

## Interactive Mode

If batch of problems to be simulated then after completing the previous simulation using the Run option from Integrated GUI or from Run options dialog ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) can be used for submitting simulations interactively one after the other.

## Batch Queue Mode

Interactive submission of simulations requires user monitoring to start simulation one after the other however user can use ![]({{ '/assets/icons/simulator_icons/gui_add_to_queue.jpg' | relative_url }}) option from GUI or from Run options dialog ![]({{ '/assets/icons/simulator_icons/mo_submit_to_qeue_button.jpg' | relative_url }}) to pick automatically each job one after the other or simultaneously based on the simulation server settings.

The problem running status can be monitored from the Process monitor and also for additional options related to executing of interactive and batch mode simulations refer to chapter [23.4. Process Monitor](/docs/sk/simulator/23_deform_simulator/23_4_process_monitor/).

From version 11.0 users can submit jobs for simulation using remote machine Simulation servers in batch mode from Run options dialog. (Refer section [6.2. MO Simulation layout](/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_2_integrated_manufacturing_process_simulation_layout/)) This will temporarily move the jobs to remote simulation server machine for simulation, after completion of simulation it copies back the project, so it reduces the load on the local machine.

## Queuing Simulations

**Running Batch Queue Server and Simulation Server**

****  
(Please refer to[Chapter 23.6. Running Shared folder Simulations](/docs/sk/simulator/23_deform_simulator/23_6_running_shared_folder_simulations/) on how to setup, simulation servers, batch queue servers and handle mapped drives on a network to run DEFORM simulations)

(Installing this Batch Queue and Simulation server services is a part of the default installation process, and the details indicated here are only standby options, if the given system has any issues/restrictions with handling the services)

If you would like to queue up jobs or run jobs on the other machine, please install simulation server.

The installations are easy, just run the provided batch files (at the DEFORM installation directory):

  * InstallBatchQueueServer.bat (example PC path C:\Program Files\SFTC\License Manager\\)

  * InstallSimulationServer.bat (example PC path C:\Program Files\SFTC\DEFORM\Configuration\\)

Then these two programs will also be registered as services just like the license manager. They will start automatically.

**Computer configuration requirements**

****

  * **Si******m** ulation server**: A central computer – presumably high performance – for running FEM calculations.

  * **License server** : A central computer – not necessarily high powered – for managing licenses.

  * **Batch queue server** : A central computer for managing run sequence of jobs. The License and Batch servers will run on the same machine and Simulation server must run on machines from where user submits the jobs to queue.

  * **Pre / Post client(s)** : Computer at which user(s) will pre and post process simulations. Pre and post processor programs are executed on this computer.

  * **DB file location** : The database files should be on a shared network drive accessible from the simulation serer and the pre/post client computer. For optimum simulation performance, the DB files should be on a hard drive physically integrated into the simulation server. In other words, forcing the simulation server to access a database across a network will likely cause longer run times.

**Simulation Server setup**  
On the “Simulation Server” tab, specify the share name or IP address of the simulation server machine. If it is a multi-processor or multi-core machine, specify the number of processors (cores) available and licensed in DEFORM (Processor number) and the maximum number of jobs (normally 1). The user can use simulation and batch queue server as other than local computer by pointing it in DEFORM setup (See Fig. 23.2.1.).

![]({{ '/assets/images/simulator/23_deform_simulator/23_2_interactive_and_batch_mode/image001.jpg' | relative_url }})

DEFORM setup Simulation Server window

**Run (Options) settings**  
After configuration, please use ![]({{ '/assets/icons/simulator_icons/gui_run_options_button.jpg' | relative_url }}) settings from GUI Main to utilize batch queue and simulation server when desired.

**How to add jobs in Queue:**

Pick the DB from GUI Main (from working folder).

From GUI Main open ![]({{ '/assets/icons/simulator_icons/gui_run_options_button.jpg' | relative_url }}).

Initial details are normally picked up from the details provided from DEFORMSetup run.

Check the servers required for batch queue status using Check Server![]({{ '/assets/icons/simulator_icons/mo_check_server_button.jpg' | relative_url }}) button.

From this dialog, click on ![]({{ '/assets/icons/simulator_icons/mo_submit_to_qeue_button.jpg' | relative_url }}) to add the job1 to Queue.

Select job2 click on ![]({{ '/assets/icons/simulator_icons/gui_add_to_queue.jpg' | relative_url }}) under Simulator in GUI main, repeat same for remaining jobs 3 and 4 (See Fig. 23.2.2.).

![]({{ '/assets/images/simulator/23_deform_simulator/23_2_interactive_and_batch_mode/image002.jpg' | relative_url }})

Queuing simulations from Run options

The jobs added to queue can be seen in Process Monitor window under Running and Pending list.

Once a job is finished, it is removed from the Batch Queue list and the next job waiting will take for running.

The user can change the position of the job with the help of "Move UP" ( ![]({{ '/assets/icons/simulator_icons/move_up_button.jpg' | relative_url }}) ) and "Move Down" ( ![]({{ '/assets/icons/simulator_icons/move_down_button.jpg' | relative_url }}) ) buttons and job can be removed from queue using "Terminate or Remove" button ( ![]({{ '/assets/icons/simulator_icons/mo_kill_button.jpg' | relative_url }}) ). (See Fig 23.4.2)

## **Run Options dialog features******

![]({{ '/assets/icons/simulator_icons/run_option_icon.jpg' | relative_url }}) or Simulation menu Run (options) ![]({{ '/assets/icons/simulator_icons/gui_run_options_button.jpg' | relative_url }})will provide more advanced options to run the simulation like interactive or batch mode, running with single and multiple (only for 3D) processors and 32 and 64 bit running.

  * **Job Type** : This Indicates type of the running jobs like MO (Multiple operations), DOE (Design of Experiments) or OPT (Optimization).

  * **DB Name/Problem ID** : Displays the current project DB name in case of normal MO operations project. For DOE and OPT it shows the Problem ID as DOE/OPT project name, required DB's to complete DOE/OPT study are generated after submitting the problem to simulate.

  * **Submitted By** : It will display the project location machine name.

  * **Password to Kill Job** : If user used any password to protect simulation in simulation server of DEFORM setup then that password should be entered here before selecting ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) or ![]({{ '/assets/icons/simulator_icons/mo_submit_to_qeue_button.jpg' | relative_url }}) buttons to start the simulation.

  * **Simultaneous Jobs** : User can indicate number of simulations or Jobs that can be run simultaneously and this number should be equal to or less than the maximum number of jobs specified in DEFORMSetup and also based on the license available. This option is available only for DOE/OPT jobs submission in queue.

  * **Simulation Mode** : There are two simulation modes those are,

  
![]({{ '/assets/icons/simulator_icons/mo_interactive_mode_rb.jpg' | relative_url }}) : Using this option, user can run simulations without simulation server by selecting ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button. This option does not require simulation server to be running. (See Fig. 23.2.3.) 

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image003.jpg' | relative_url }})

Run options window for MO job in interactive simulation mode

  
Interactive simulation mode settings are,

**Computer Name:** This will display the name of the Machine

**Type** : This will display whether it is a Single or Multi Processor simulation

**Path on Computer:** This will display the path of the DB and in case of DOE/OPT it indicates the path where DB's would be generated.

**Processors Per Job:** Using this option user can select the number of processors required to be used per job during simulation, currently available only for 3D simulation or job.

**Shared Memory Size:** It displays Shared Memory allocated on the simulation server system for DEFORM simulation.

User can save the settings using ![]({{ '/assets/icons/pre_icons/mo_save_button.jpg' | relative_url }}) button and close the Run options window using ![]({{ '/assets/icons/pre_icons/mo_close_button.jpg' | relative_url }}) button.

![]({{ '/assets/icons/simulator_icons/mo_batch_mode_rb.jpg' | relative_url }}) : Using this option, user can run simulations only in batch mode (See Fig. 23.2.4.). It is essential to select any one of the available simulation servers listed or first available simulation server to simulate batch queue problems and click on ![]({{ '/assets/icons/simulator_icons/mo_submit_to_qeue_button.jpg' | relative_url }}) button to start adding job to the queue. The displayed list contains only simulation servers that are added to the DEFORM Setup.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image004.jpg' | relative_url }})

Run options window for MO job in batch simulation mode

  
In Batch simulation mode selected simulation servers settings can be set by selecting the particular simulation server and clicking on ![]({{ '/assets/icons/simulator_icons/mo_submit_to_qeue_button.jpg' | relative_url }}) button. (See Fig. 23.2.5.)

![]({{ '/assets/icons/simulator_icons/mo_server_settings_button.jpg' | relative_url }}): Using this button user can set the selected simulation server settings like processors to be utilized per job during simulation and shared memory.

**Server Name** : This will display the selected simulation server machine name

**Type** : This will display whether it is a Single or Multi Processor simulation

**Path on Server** : This will display path of the DB if user selected the local machine  
as simulation server or else will display as "Copied from :<Phisical_DB_existing_Machine_name>"

**Processors Per Job** : Using this user can select the number of processors to be used  
per 3D simulation or job.

**Shared Memory Size:** It displays Shared Memory allocated on the simulation server  
system for DEFORM simulation.

  
User can save the settings using ![]({{ '/assets/icons/pre_icons/mo_save_button.jpg' | relative_url }}) button and close the Run options window using ![]({{ '/assets/icons/pre_icons/mo_close_button.jpg' | relative_url }}) button.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image005.jpg' | relative_url }})

Batch simulation mode server settings

  
**Simulation Run types:** For normal multiple operations project in both interactive and batch mode user can run the simulation from the initial step or if it is stopped in between or wanted to restart from the mod we can do so by continue options. (See Fig. 23.2.6.)

**Initial Run:** This will start the simulation from the first operation starting step. User can also use this option to restart the simulation from the beginning in case of simulation has stopped in the mid due to some license or network issues.

**Continue Run:** This continue run will provide two options those are, 

  * **Continue from the last step:** This will continue the simulation from the last available negative step. It is useful when user done some corrections to the setup and tries to restart from any stage of the simulation.
  * **Restart from the selected Simulation:** This will restart the simulation from any of the intermediate operation's simulations by selecting that particular operation and its simulation.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image006.jpg' | relative_url }})

Simulation Run types from Run options for normal projects

**Related Topics:**

[23.3 Simulation Graphics](/docs/sk/simulator/23_deform_simulator/23_3_simulation_graphics/)

[23.4. Process Monitor](/docs/sk/simulator/23_deform_simulator/23_4_process_monitor/)

[23.5. Setting up MPICH](/docs/sk/simulator/23_deform_simulator/23_5_setting_up_mpich/)

[23.8. Trouble Shooting Simulation Running](/docs/sk/simulator/23_deform_simulator/23_8_trouble_shooting_simulation_running/)

[Pre-Processor](/docs/sk/post_processor/post_processor_mainpg/)

[Integrated Manufacturing Process (MO)](/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_integrated_manufacturing_process_layout/)

[Post -Processor](/docs/sk/post_processor/24_introduction_to_post_processor/24_introduction_to_post_processor/)

---
lang: sk
title: "23.1. Start Stop and Resume Simulations"
---

# 23.1. Start Stop and Resume Simulations

The simulation is started by clicking the ![]({{ '/assets/icons/simulator_icons/gui_run_button.jpg' | relative_url }}) or ![]({{ '/assets/icons/simulator_icons/mo_run_icon.jpg' | relative_url }}) (See Fig. 23.1.1.). This initiates a series of operations to run the simulation and generate new meshes as necessary (See Fig. 23.1.1.).

Run-time information will be written to the ProblemId.MSG and ProblemId.LOG files.

  * Execution information, including convergence information for each step and simulation error messages, can be found in the .MSG file.

  * Information on simulation and remeshing, execution times, fatal errors and type of FEM job running (32-bit or 64-bit simulation) in case of 3D job can be found in the .LOG file or in the command window where DEFORM was executed from.

  * By clicking on ![]({{ '/assets/icons/simulator_icons/open_simulation_graphics_label.jpg' | relative_url }}) link under Preview tab, user can view the Simulation graphics under preview tab.

  * Memo option allows user to enter and save any notes related to the current simulation.

![]({{ '/assets/images/simulator/23_deform_simulator/23_1_start_stop_and_resume_simulations/image001.jpg' | relative_url }})

Main window of DEFORM GUI Main (While running a model)

In Fig. 23.1.1.:

**1- Run** option used to run the job.

**2- Stop** option used to Stop the running job.

**3- Continue** option used to continue the resumed job.

A simulation is stopped by clicking the ![]({{ '/assets/icons/simulator_icons/gui_stop_button.jpg' | relative_url }}) or ![]({{ '/assets/icons/simulator_icons/mo_stop_icon.jpg' | relative_url }}) in the header (See Fig. 23.1.1.). Simulation may also be stopped using the "Kill" or "Stop" buttons from the process monitor (See Fig. 23.1.2.). The simulation will be stopped after the current step is completed for Stop simulation option. For Kill Simulation option simulation stops at the current iteration trial.

**Killing a simulation process**

Another way to stop simulation is killing "DEFORM_RUNNING_JOB_STATUS.TXT" in GUI main. Since the Stop command will only stop a simulation after the current step is completed, substantial time may be required for the simulation to stop. To kill a simulation immediately, the process DEF_SIM.EXE must be killed directly from the operating system.

![]({{ '/assets/images/simulator/23_deform_simulator/23_1_start_stop_and_resume_simulations/image002.jpg' | relative_url }})

**Killing job from Process monitor window**

A simulation is continued or resumed from where we stopped by clicking the ![]({{ '/assets/icons/simulator_icons/gui_continue_button.jpg' | relative_url }}) button (See Fig. 23.1.1.) in the right side Simulator palette or ![]({{ '/assets/icons/simulator_icons/mo_continue_icon.jpg' | relative_url }}) in the header.

**Multiple Processor Simulation**

Processers per Job allows the user to define the multiple processor settings used to solve the problem as well as the number of processors used on each computer. Now correct name of the computer will be displayed in Computer name field. (See. Fig. 23.1.3.)

After selecting the FEM and Machine types click on Start to start the simulation.

**Partially parallel FEM option** runs only the solver part of the simulation in parallel mode, while the other operations like model stiffness matrix, remeshing and interpolation are run in single cpu on the primary host machine. In PC environment this results in the execution of one DEF_SIM.EXE on each of the processors requested.

**Fully parallel FEM** handles the full model in be run in parallel, including the model stiffness matrix, remeshing and interpolation apart from the solution phase. In PC environment fully parallel run results in the execution of one DEF_SIM.EXE on each of the processors requested. With respect to the total simulation time, larger model sizes typically gain from this multiprocessing setup.

![]({{ '/assets/images/simulator/23_deform_simulator/23_1_start_stop_and_resume_simulations/image003.jpg' | relative_url }})

Multiple Processor Set Up window

Note:

  1. Once these options are selected the system saves the information in local files (DEF_MPIenv.DAT and DEF_MPI_p4penv.DAT). FEM looks for these files to start parallel runs.

  2. From the present release, Task Manager will only display multiple MPI instances of DEF_SIM.EXE, instead of DEF_SIM.EXE, DEF_SIM_P4P.EXE or DEF_SIM_P4P.EXE depending on the MPI setting.

  3. Unless Mpich are installed with earlier versions it is now mandatory to install 32 bit Mpich1 v1.2.1 for 32bit machines and additional 64 bit Mpich2 v1.2.1 for 64 bit machines.

**Related Topics:**

[23\. Introduction to Simulator](/docs/sk/simulator/23_deform_simulator/23_introduction_to_deform_simulator/)

[23.2. Interactive and batch modes using Run option](/docs/sk/simulator/23_deform_simulator/23_2_interactive_and_batch_mode/)

[23.3. Simulation Graphics](/docs/sk/simulator/23_deform_simulator/23_3_simulation_graphics/)

[23.4. Process Monitor](/docs/sk/simulator/23_deform_simulator/23_4_process_monitor/)

[23.5. Setting up MPICH](/docs/sk/simulator/23_deform_simulator/23_5_setting_up_mpich/)

[23.6. Running Shared folder Simulations](/docs/sk/simulator/23_deform_simulator/23_6_running_shared_folder_simulations/)

[23.7. Trouble Shooting Simulation Running](/docs/sk/simulator/23_deform_simulator/23_8_trouble_shooting_simulation_running/)

[Post Processor](/docs/sk/post_processor/post_processor_mainpg/)

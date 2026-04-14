---
lang: sk
title: "53.2. Optimization Simulation Running and Monitoring"
---

# 53.2. Optimization Simulation Running and Monitoring

Optimization jobs are submitted to run in batch mode using ![]({{ '/assets/icons/simulator_icons/mo_run_options_action_lable.jpg' | relative_url }}) button, run options are as shown Fig. 53.2.1. Simulations can be run either on "Single simulation server" or "Multiple simulation server" using "Run Simulation on" options. For Single simulation server user needs to select any one available simulation server, for Multiple simulation servers user can select multiple no. of available simulation servers from the list in the table, enter the number of Simultaneous jobs (must be less than the simulation server Max jobs) to be simulated and number of Processors to be utilized per job (for 3D only) based on the licenses available for running, then click on ![]({{ '/assets/icons/simulator_icons/mo_submit_to_qeue_button.jpg' | relative_url }}) to run jobs in queue. To set selected simulation server Max jobs and Processors per job click on ![]({{ '/assets/icons/simulator_icons/mo_server_settings_button.jpg' | relative_url }}) button.

![]({{ '/assets/images/doe_and_optimization/53_optimization_study/53_2_optimization_simulation_running_/image001.jpg' | relative_url }})

Optimization Run options window

**Run Simulation on:**

  * **Single Simulation Server:**

User can run multiple DB's or Run cases by submitting in queue in any one of the available simulation servers listed using single simulation server ( Fig. 53.2.2.). User can select the number of simultaneous simulation servers up to available number of licenses based on the requirement.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image007.jpg' | relative_url }})

Run options window for DOE job using single sim server

  * **Multiple Simulation Servers:**

From version 11.1 users can run the batch queue jobs using the remote machine simulation servers using the simulation server other than the local, it will provide opportunity to use multiple simulation servers at a time to simulate the DOE/OPT multiple run cases or DB's. It reduces the load on the local simulation servers also using the multiple machine simulation server and the time required to complete the DOE/OPT project.

To use a particular available simulation sever, user needs to check the checkbox next to that simulation server from the list in the table. User can change the simulation severs settings like processors per job and MPI shared. In addition to this user can also set Max. Jobs per simulation server for DOE and OPT simulations.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image008.jpg' | relative_url }})

Run options window for DOE job using multi sim server

For DOE and OPT simulations in both single and multi simulation server mode, selected simulation servers settings can be set by selecting the particular simulation server and clicking on ![]({{ '/assets/icons/simulator_icons/mo_server_settings_button.jpg' | relative_url }}) button.

For more details on "Run simulation on" run option refer Chapter [6.2.3. Section Run_Simulation_option](../../integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_2_integrated_manufacturing_process_simulation_layout.htm#Fig._6.2.3._Run_Simulation_options).

**Simulation Run types:** For DOE/OPT projects user can start the simulation from the first operation or if DOE/OPT variables added only from the intermediate operations then user can continue only from those intermediate operations. Even if DOE/OPT simulation stops abnormally then user can restart the simulation from incomplete run where it stopped or from the intermediate operation of the incomplete run.

  * **Initial Run** : This initial run will provide two options those are,

  * **Start from the beginning:** This will start the simulation from the first operation starting step. User can also use this option to restart the simulation from the beginning in case of incomplete DOE run due to some license or network issues.

  * **Start from the Selected Simulation:** This will start the simulation from any of the intermediate operation's simulations by selecting that particular operation and its simulation. If user added DOE study only in the intermediate operation then using this option will reduce the total time required to complete DOE study.

  * **Continue Run:** This continue run will provide two options those are,

  * **Continue incomplete DOE study:** This will continue the incomplete DOE study run from the last available negative step and complete the DOE/OPT project.

  * **Restart DOE from the selected Simulation:** This will continue the incomplete DOE study run from any of the intermediate operation's simulations by selecting that particular operation and its simulation.

Continue does not need to run successfully simulated DOE run cases again to complete the incomplete DOE project.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image010.jpg' | relative_url }})

Simulation Run types for DOE/OPT projects

During running, system generates database for the number of simultaneous simulations within folder **Run** with suffix of number increasing, as the simulation continues DBs are generated up to Maximum number of simulations untill stopping criteria defined is reached. Necessary supporting files will also be generate along with DB under DoeStudies/DoeStudy1/Solutions Problem directory after which simulation starts for number of simultaneous DB's starting with Run_00001 in batch as shown in Fig. 53.2.5. from DEFORM Main GUI. In other empty folders required files and DB's are generated after completing of all simultaneous simulations. DOEStudy1 directory is the directory which contains every details of the Optimization Study Project1.

![]({{ '/assets/images/doe_and_optimization/53_optimization_study/53_2_optimization_simulation_running_/image002.jpg' | relative_url }})

Optimization Problem directory structure

OPT Log tab will display the information regarding Optimization simulations DB generation and adding to queue for running as shown in Fig. 53.2.6

![]({{ '/assets/images/doe_and_optimization/53_optimization_study/53_2_optimization_simulation_running_/image003.jpg' | relative_url }})

OPT Log file messages of DB generation and adding the DB's to queue

The Simulation jobs tab and OPT Log tabs can be used to monitor the OPT runs, see Fig. 53.2.6. Also Process monitor will give more details about the Optimization jobs in queue as shown in Fig. 53.2.7.

![]({{ '/assets/images/doe_and_optimization/53_optimization_study/53_2_optimization_simulation_running_/image004.jpg' | relative_url }})

Process Monitor for Optimization batch jobs running

Optimization jobs submitted in queue that are running and finished will be listed in simulation jobs or Process monitor.

After all simulations running is completed then Optimization results will be prepared automatically and saved as SDB file in DOEStudy1/Output directory. This Optimization results can be post-processed using DOE post. User can select the ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) MO mode button and then select the ![]({{ '/assets/icons/pre_icons/mo_doe_post_button.jpg' | relative_url }}) to access DOE post as shown in Fig. 53.2.8. or can also access from DEFORM Main GUI Post Processor link . User can post process the individual runs by selecting the respective DB's from Database tab in MO Post mode.

![]({{ '/assets/images/doe_and_optimization/53_optimization_study/53_2_optimization_simulation_running_/image005.jpg' | relative_url }})

Optimization Study runs in MO Post

**Related Topics:**

[53\. Introduction to Optimization](/docs/sk/doe_and_optimization/53_optimization_study/53_introduction_to_optimization/)

[53.1. Optimization Setup](/docs/sk/doe_and_optimization/53_optimization_study/53_1_optimization_setup/)

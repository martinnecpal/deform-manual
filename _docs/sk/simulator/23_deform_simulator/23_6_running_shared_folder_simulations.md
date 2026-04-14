---
lang: sk
title: "23.6. Running Shared folder Simulations"
---

# 23.6. Running Shared folder Simulations

This section guides the user on how to set up the Batch Queue Server and Simulation Server on a network. Before doing this setup, we need to set up the network drives. We will be explaining this concept by taking four PCs lmwin11, emerald, tuscan, and puce. Lmwin11 PC is the License Serve, which manages the Deform license, and the Batch Queue Server, which manages the run sequence of jobs. The other three computers are client machines among which emerald is the Simulation Server for running FEM jobs. 

  
First, **create a shared folder on the simulation server** as follows (see Fig. 23.6.1.).

  1. Get into the computer you want to share from, i.e. **Simulation****Server** emerald.

  2. Right-click on the folder you want to share, e.g. folder TEST, go to Properties and select **Sharing**![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**Share**.

  3. Click on the Done button finally. 

![]({{ '/assets/images/simulator/23_deform_simulator/23_6_running_shared_folder_simulations/image001.jpg' | relative_url }})

Share a folder on the simulation server. 

Note that before creating a shared folder, you need to ensure that File and Printer Sharing is enabled on your simulation server by following the steps below.

  1. Go to the Control Panel (or Settings).

  2. Navigate to Network and Sharing Center ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Change advanced sharing settings.

  3. Turn on Network discovery and File and printer sharing.

  
Second, **access the shared folder** as follows.

  1. Go into the computer you want to **access the shared folder** , i.e. a **Client****computer** such as tuscan.

  2. Open File Explorer and type \\\<the name of the simulation server>, i.e. \\\emerald, in the address bar (or click on the Network tab in the left sidebar and double-click on the emerald computer). 

  3. **Right-Click on the shared folder** TEST and select **Map network drive…** , as shown in Fig. 23.6.2. to create your mapped drive with a unique name such as “S:” (see Fig. 23.6.3.)

![]({{ '/assets/images/simulator/23_deform_simulator/23_6_running_shared_folder_simulations/image002.jpg' | relative_url }})

Access the shared folder from the client machine to map a network drive.

  
![]({{ '/assets/images/simulator/23_deform_simulator/23_6_running_shared_folder_simulations/image003.jpg' | relative_url }})

Map a network drive to the shared folder.

Now you can see your mapped drive in **This PC** , shown in Fig. 23.6.4. Note that you can delete the created drive by right-clicking on its name and select Disconnect.

![]({{ '/assets/images/simulator/23_deform_simulator/23_6_running_shared_folder_simulations/image004.jpg' | relative_url }})

Mapped drive in This PC.

Third, **set up the mapped drives in Deform Setup** doing the following steps.

  1. On each client computer, run **Deform Setup** and synchronize to the license server; press OK when you see the message of the license server is running (see Fig. 23.6.5).

  2. As shown in Fig. 23.6.6, in the **Shared Folders** tab, you can create a **New****directory** , which will be the mapped folder \\\emerald\TEST on the simulation server emerald.

  3. **Add shared point** from the client computers to share your project folder and database (see Fig. 23.6.7.). 

  4. Eventually, ensure that you **Save** the last changes in the Deform Setup. Fig. 23.6.8 shows the saved network drives on the client computers tuscan and puce (i.e. S: and R:), mapped to the shared folder on the simulation computer emerald.

![]({{ '/assets/images/simulator/23_deform_simulator/23_6_running_shared_folder_simulations/image005.jpg' | relative_url }})

Synchronize to the license sever in Deform Setup.

![]({{ '/assets/images/simulator/23_deform_simulator/23_6_running_shared_folder_simulations/image006.jpg' | relative_url }})

Create New Directory with the machine name and directory where the shared folder is located (on the simulation server).

![]({{ '/assets/images/simulator/23_deform_simulator/23_6_running_shared_folder_simulations/image007.jpg' | relative_url }})

Add share points from the simulation server and the client computers with the network drive letter. 

![]({{ '/assets/images/simulator/23_deform_simulator/23_6_running_shared_folder_simulations/image008.jpg' | relative_url }})

Save shared drives in Deform Setup.

Now both network drives S: and R: on client computers tuscan and puce can access to the shared folder TEST on the simulation server machine emerald, as can be seen in Fig. 23.6.9. Therefore, users can work on MO project files and databases on their local machines and run them on the simulation server. 

![]({{ '/assets/images/simulator/23_deform_simulator/23_6_running_shared_folder_simulations/image009.jpg' | relative_url }})

Access to the simulation server from the mapped network drive on the client machine.

  
Users can then submit jobs to the simulation server as follows.

  1. Select the network drive from the client machine such as tuscan (Location on local computer will be shown.)

  2. Select the DB to run (Database in remote computer will be shown.)

  3. Open Run options from tuscan, as shown in Fig. 23.6.10.

  4. Select the simulation server emerald under Batch mode (Location on remote computer will be shown.)

  5. Check Server (Dialog box pops up and shows status.)

  6. Submit to Queue (DEF_SIM_64.exe will start on emerald machine.)

![]({{ '/assets/images/simulator/23_deform_simulator/23_6_running_shared_folder_simulations/image010.jpg' | relative_url }})

Submit a job to Batch Queue.

Fig. 23.6.11. illustrates the control flow after the job submission. This image shows how the systems are getting the license from the server machine to perform the given task. We can see that client machines tuscan and puce are getting the licenses from the license server and the batch queue server machine lmwin11 to respectively open Deform applications and add jobs to the batch queue. The simulation server emerald is getting the license from the server machine lmwin11 for running the simulation, and it is also accessing the batch queue server to add the DBs to the list.   
While all these options are going on, we can monitor this ongoing process through the Process Monitor and License Manager Administrator.

![]({{ '/assets/images/simulator/23_deform_simulator/23_6_running_shared_folder_simulations/image011.jpg' | relative_url }})

Control flow after the job submission.

Finally, note that users can alternatively submit jobs for simulation using remote machine simulation servers in batch mode from Run options. This will temporarily move the jobs to the remote simulation server machine for simulation, completes the simulation and copies back the project, so it does not need to map the shared folder of the remote machine folder and reduces the load on the local machine. However, it will be easier if all the simulation files remain on the simulation computer and we access them through network drives. Users may face difficulties during the file transfer and simulation running due to network communications, which will make the remote simulation running more difficult than the shared folder simulation running. 

**Related Topics:**

[23.1. Start, Stop and Resume Simulation](/docs/sk/simulator/23_deform_simulator/23_1_start_stop_and_resume_simulations/)

[23.2. Interactive and batch modes using Run option](/docs/sk/simulator/23_deform_simulator/23_2_interactive_and_batch_mode/)

[23.3. Simulation Graphics](/docs/sk/simulator/23_deform_simulator/23_3_simulation_graphics/)

[23.4. Process Monitor](/docs/sk/simulator/23_deform_simulator/23_4_process_monitor/)

[23.5. Setting up MPICH](/docs/sk/simulator/23_deform_simulator/23_5_setting_up_mpich/)

[23.8. Trouble Shooting Simulation Running](/docs/sk/simulator/23_deform_simulator/23_8_trouble_shooting_simulation_running/)

[Pre-Processor](/docs/sk/post_processor/post_processor_mainpg/)

[Integrated Manufacturing Process (MO)](/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_integrated_manufacturing_process_layout/)

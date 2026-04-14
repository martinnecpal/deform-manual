---
lang: en
title: "3.1. Deform License Setup"
---

# 3.1. DEFORM License Setup

For DEFORM-Integrated 2D3D Version, a new DEFORM license manager has been implemented. We refer this new license manager as License Manager Server, which means this server can reside in a central location in a network serving license to a number of client machines. Batch Queue is running on the same machine as the license manager, and feeds jobs to a simulation server (which can be on a faster computer with sufficient resources to handle FEM jobs). The setup details required is briefly explained in this section. In a simple configuration all the servers can be on the same computer.

3.1.1. Computer configuration requirements

3.1.2. Computer Locations in DEFORM Setup

3.1.3. How to setup the new license configuration

## Computer configuration requirements

**Simulation server:** A central computer – presumably high performance – for running FEM calculations.

**License server** : A central computer – not necessarily high powered – for managing licenses.

**Batch queue server** : A central computer for managing run sequence of jobs. The Batch, License and Simulation servers may all run on the same machine or simulation server can be runned on different machine.

**Pre / Post client(s)** – Computer at which users will pre and post process simulations. Pre and post processor programs are executed on this computer.

## Computer Locations in DEFORM Setup

**Run DEFORM Setup**

In the “Simulation Server” tab user must add the simulation server system on which jobs which are submitted in batch mode would be running. The simulation server system can be local system or any remote high performance system, user can add simulation server by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button, see Fig. 3.1.13. If it is a multi-processor or multi-core machine, specify the number of processors (cores) available and licensed in DEFORM (Processor number) and the maximum number of jobs that user would like to run simultaneously on that articular system based on the performance of the system (default is 1) button. If it is a multi-processor or multi-core machine, specify the number of processors (cores) available and licensed in DEFORM (Processor number) and the maximum number of jobs (default is 1).

**Compared to the previous versions, here are the important changes:**

**Location of the License Manager folder where password file (DEFORM.PWD) needs to be located**

  * Old versions (up to 2DV91 or 3DV61) C:\Program Files\DEFORM License Manager 3.1
  * Current release C:\Program Files\SFTC\License Manager

**Location of the Simulation server and MPICH registration executable**

  * Old versions up to 2DV91 or 3DV61 C:\Program Files\DEFORM License Manager 2.1 and till v10.2.1 in C:\Program Files\SFTC\License Manager
  * Current release C:\Program Files\SFTC\DEFORM\Configuration

After the Sentinel protection driver installation, License Manager installation will start and user will be prompted for the password file. Installer copies the password file to an appropriate location and with a hardware key in place, License Manager server program will validate the password and hardware key combination. During this process, it is important to first uninstall the earlier copy of the programs with the same version number.

**Simulation Server Setup:**

(installing these services is a part of the default installation process and the details indicated here are only standby options, if the given system has any issues/restrictions with handling the services)

As administrator, run the file “InstallBatchQueueServer.bat” on the batch queue server computer. (using default installation path, typical location of this batch file is C:\Program Files\SFTC\License Manager\\)

From v14.0, “InstallBatchQueueServer.bat” is considered as legacy script, instead “InstallServers.bat” is used to add License Server and the Batch Queue Server services.

While executing the script, user can observe below messages indicating the usage of the file:

_“Usage:_

"InstallServers.bat Y" - Set up the License Server and the Batch Queue Server.

"InstallServers.bat N" - Set up the License Server only.

"InstallServers.bat" - Display prompt for whether the Batch Queue Server should be set up or not.

This will install the DEFORM License Server service.

Do you want to install the Batch Queue Server service also? (Yes, No, Quit) [Y,N,Q]?

If we enter “Y”, then it will install both License Server and the Batch Queue Server, if we enter “N”, only License server will be installed and if we enter “Quit”, it will quit the script execution part.

From v11.2, the Windows service "DeformSimServer" is not required.

  1. We do not need to install the "DeformSimServer" Windows service.
  2. If "DeformSimServer" Windows service is already installed, we do not need to run it. It is **NORMAL** to see "DeformSimServer" Windows service is **stopped**.

DEFORM users should use DEFORMSetup (in the "DEFORM Services" tab) to check the status of the DEFORM Simulation Server and other DEFORM services.

**How to run older versions using the new license manager**

**Below 2D V9.1 and 3D V6.1**

Run DLConfig.exe from C:\Program Files (x86)\DEFORM License Manager 2.1 (in 64bit machines) and C:\Program Files\DEFORM License Manager 2.1 (in 32 bit machines) and indicate the new server machine name and 34445 as the port number.

**Above Deform 10.X and Below Deform v11.1**

Install Deform Service Control Program from the Deform Installation program. Run DeformSetup program from C:\Program Files\SFTC\DEFORM\V10.X. Add simulation server system in Simulation Server tab. Select Versions option from the Simulation server tree and add version. Select version added and change it to the old version by selecting old version number from pull down menu and its installation location. After completing it, click on Deform Services tab and select “Open DEFORM service for Local Computer”. Click on update button to update the files in Configuration folder using update button next to the Simulation Server system under Deform Computer. Now system is ready to run older versions of the DEFORM.

## How to setup the new license configuration

  
**Step 1**

Since we are installing License manager in server machine, start DEFORM system Installation and continue till the select components page and choose "Server installation" from pulldown menu as shown in Fig. 3.1.1. Hence DEFORM Installer will install the support codes (Python and Sentinel protection driver) then start the License Manager installation.

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image023.jpg' | relative_url }})

Deform Choose components window (not a required step for official v11.0.2 release)

If old version License Manager is not uninstalled then installer recommends to uninstall the old license manager before installing new license manager as shown in Fig. 3.1.2.

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image022.jpg' | relative_url }})

License manager installation warning (not a required step for official v11.0.2 release)

Turn on Configure windows firewall. Windows firewall needs to be configured to allow License and Batch queue service through windows firewall as shown in Fig. 3.1.3. and then click **Next**.

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image025.jpg' | relative_url }})

Windows Firewall configure page

During the DEFORM License Manager installation the system prompts the user for the DEFORM password (see Fig. 3.1.4), user can browse the location of the DEFORM.PWD file using Browse button. When the user clicks the Next button, the password is copied to the License Manager Folder from the browsed location. Automatic start of the DeformLicenseServer is a part of the installation.

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image024.jpg' | relative_url }})

DEFORM password input window

_**Note:**_

_If the user does not have the password at the time of installation, then password must be manually pasted into the License Manager folder and has to run the license manager batch file to activate the DeformLicenseServer Service._

Turn on Install Batch Queue server. Batch queue is required for queueing the simulations as shown in Fig. 3.1.5. and then click **Next**.

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image028.jpg' | relative_url }})

DEFORM License Manager additional task selection window

Review the License Manager setup selections and click **Install** to start installation. Otherwise go back to change the settings. (See Fig. 3.1.6.)

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image026.jpg' | relative_url }})

DEFORM License Manager installation confirmation window

If the given system has any issues/restrictions with handling the DeformLicenseServer service then as administrator, run the file “InstallServer.bat” on the license server computer (available in installation path, typical location of this batch file is C:\Program Files\SFTC\License Manager) using the command prompt as shown in Fig. 3.1.7. Enter “N” as an option to install only Deform License server.

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image001.jpg' | relative_url }})

Registering and run the license manager server using the batch file

If the given system has any issues/restrictions with handling the DeformBatchQueue service then as administrator run the file “InstallServer.bat” with “Y” option on the license server computer (available in default installation path, typical location of this batch file is C:\Program Files\SFTC\License Manager) using the command prompt as shown in Fig. 3.1.8.

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image002.jpg' | relative_url }})

Registering and running the license manager and batch queue servers using the batch file with “Y” option

**Step 2:**

For any subsequent changes user can open DEFORMSetup dialog (See Fig. 3.1.9.), to indicate the name of the server computer name and port number (34445). Click on ![]({{ '/assets/icons/pre_icons/mo_syncronize_button.jpg' | relative_url }}) to make sure that Success is returned which is an indication of the fact that now a valid combination of License key, password file have been identified by the setup program. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to popup message, this activates other subsequent data tabs (Simulation and Shared folder) and save the settings using ![]({{ '/assets/icons/pre_icons/mo_save_button.jpg' | relative_url }}) button. (See Fig. 3.1.10.). Once user clicks on the save button Deform Services tab will be activated, for subsequent opening of DEFORMSetup dialog Deform Services tab remains activated.

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image003.jpg' | relative_url }})

DEFORM Setup start menu shortcut

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image004.jpg' | relative_url }})

Mandatory input fields to activate the license configuration

After the synchronize button is clicked, if the current computer hasn’t been set up as a Simulation Server with the current version and path then DEFORM Setup will offer to add it as one. (See Fig. 3.1.11.) 

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image009.jpg' | relative_url }})

DEFORM Setup License Server window

If the **Yes** button is clicked to add the Simulation Server, DEFORM Setup will not automatically save the change to the License Server, but will prompt to save the changes. (See Fig. 3.1.12.) Verify the change is correct in the Simulation Server tab before saving the settings. 

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image029.jpg' | relative_url }})

DEFORM Setup reminder to save

**Step 3:**

The Simulation Server tab allows the users to manage the simulation servers connected to the License Server. As shown in Fig. 3.1.13., the top area of the tab shows the defined Simulation Servers. If the local computer isn’t defined as a Simulation Server, click the "Add Simulation Server" button to define it. 

When a Simulation Server is added, by default the local computer name will be captured and added along with some default values for the processor type, number of processors, the maximum number of jobs, and the latest version available in the local system will be set to the current path automatically. 

When the License Manager server is on the same computer as that of DEFORM Setup is being run on, as many Simulation Servers as required can be defined. However, if the License Manager server is on a different computer, then only the local Simulation Server can be defined and edited. 

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image007.jpg' | relative_url }})

DEFORM Setup Simulation Server window 

Within the Simulations tab,

  * ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button can be used to add a simulation server.

  * ![]({{ '/assets/icons/pre_icons/mo_delete_icon2.jpg' | relative_url }}) button can be used to delete the local simulation server.

  * Address shows the name of the computer connected to the current License manger on which the simulation server is running.

  * Versions column shows a list of all versions defined for a given Simulation Server. 

  * Maximum Jobs option allows setting the number of jobs in the queue that can be run simultaneously on the respective simulation server. 

  * Maximum number of processors that can be used, should be same or less than the licensed. 

  * TCP Port on which license server is running.

  * DEFORM versions currently installed on the respective systems.

The lower area shows details about the currently selected Simulation Server. (See Fig. 3.1.14.) In the Versions tab, the disk location for multiple versions can be added using ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button or delete using ![]({{ '/assets/icons/pre_icons/mo_delete_icon2.jpg' | relative_url }}) button, only one path per version is allowed. 

If the Processor Type is defined as a Cluster, the Clusters tab will be enabled and details about the cluster nodes can be defined. After making changes to the Simulation Server tab, click the Save button to save the settings. 

In Windows, user can specify Multiple versions (V12.1, V12.0, V11.3, v11.2, v11.1,v11.0 and v10) installation locations for each simulation server if user would like to use older versions (See Fig. 3.1.14.). Different versions can be added by user using ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button, select the version number from the pull down menu and then specify the installation path information for each version which will be used to run the jobs from the respective version when submitted in Batch Queue. But in Linux/UNIX, user can only specify one version.

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image006.jpg' | relative_url }})

DEFORM Setup Simulation Server window

User should make sure that the Simulation Server service is Running, if it is not running then user can visit DEFORM Services tab and run the local Simulation server by clicking on [Start] button available next to the Simulation server under Deform Computers list. The simulation servers that can be used to run a selected job are listed in Run options dialog as shown in Fig. 3.1.15.

**Note** : Install path information for each version is required to be defined so that the DBs of different versions queued using Batch queue can simulate using respective version.

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image008.jpg' | relative_url }})

Run Options window

**Step 4:**

Go to the “Shared Folders” tab. Each shared folder is represented by a tree identifying its shared names on each machine where it is accessible (See Fig. 3.1.16.).

Click the “New Dir” button (See 1 in Fig. 3.1.16.), and specify the computer name and local path where the shared folder is physically located. For example, the shared folder is C:\Deform\Problem on a computer called “FastServer”. Give “Fast Server” as the computer name, and “C:\Deform\Problem” as the path. Please check your typing. There is currently no automatic checking to ensure that a specified path actually exists.

Now click on the “Add share point” button (See 2 Fig. 3.1.16.). Specify the client computer name and the path name on that computer. Suppose that the path is defined on computer “Client1” as the mapped network drive “Z:”. Then specify other client (See 3 in Fig. 3.1.16. . )computer name as “Client2” and folder name as “Q:” Be sure to include the colon (:).

Now click “Save” (See 4 in Fig. 3.1.16.). This information is all stored on the client and license server machine.

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image027.jpg' | relative_url }})

Shared folders information in DEFORM setup window

**DEFORM Services:**

Deform Services control program is installed along with new installation or can be installed independently from the DEFORM_Service_Control_vx.x.exe installation file if user would like to communicate with new License manager. User can notice a tab Deform Services added in DEFORMSetup program after the installation of Deform Services control program. DEFORM service utility program (DEC_SC.EXE) will be running as a "service" on Windows PC. Deform Service control program communicates with License Manager and can be used to monitor following services,

For Server Computer

License Server

Batch Queue Server

Web-based Service Control (Not available in Linux)

For Client Computer

Simulation Client

Simulation Server

Web-based Simulation Monitoring (Not available in Linux)

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image016.jpg' | relative_url }})

DEFORM Services in DEFORM Setup window

In DEFORM Services tab we have two options to access the computers with DEFORM services (See Fig. 3.1.17. ). User can view the services in a separate window by clicking on **Open in new window button**.

**Open DEFORM Service for local DEFORM computer** : Using this option we can monitor and control the services on Local computer only. If the local computer is a server computer then we can see both DEFORM server Computer and DEFORM Computer list (See Fig. 3.1.18.) but in Client machine we can see only DEFORM Computer list (See Fig. 3.1.19.)

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image011.jpg' | relative_url }})

DEFORM Service for local DEFORM computer window in Server computer

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image012.jpg' | relative_url }})

DEFORM Service for local DEFORM computer window in client computer

**Open DEFORM Service for all DEFORM computers** : Using this option user will be able to view all the clients that are connected to the server to which the local system is connected along with the server system. User must have passcode or user must be an authorized user in order to monitor and control the services of other computers other than the local computer. Services can be started using ![]({{ '/assets/icons/pre_icons/run_action_icon.jpg' | relative_url }}) and stop using ![]({{ '/assets/icons/pre_icons/stop_action_icon.jpg' | relative_url }}) button available next to service, See Fig. 3.1.20. From v14, information of all the computers connected to the License Server will not be synched by default to improve the DEFROM Setup performance, only local computer and server computer information will be synched. Use ![]({{ '/assets/icons/pre_icons/mo_deformsetup_sync_button.jpg' | relative_url }}) button to sync the respective computer information and to sync all computers use ![]({{ '/assets/icons/pre_icons/mo_deformsetup_sync_all_computers_button.jpg' | relative_url }}). (See Fig. 3.1.21.)

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image013.jpg' | relative_url }})

DEFORM Service for all DEFORM computers

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image030.jpg' | relative_url }})

DEFORM Service for all DEFORM computers after sync

**Passcode :** An authorized DEFORM user (See) can create a passcode or change (See Fig. 3.1.22.). With Passcode,

  * User can start and stop the services of the Server computer. (User must have passcode if user would like to stop the services of the Server computer in PC while in Linux you require passcode for both starting and stopping of the services of the Server computer)
  * View Services of any DEFORM computer (other than the authorized computer)
  * View Services of any computer with a web browser (no need to install DEFORM)
  * Update Password file for server computer
  * Update outdated services on any DEFORM Computer

**Note:** A passcode must be shared only among those users who would be controlling the services of all DEFORM Computers as they start and stop any service.

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image014.jpg' | relative_url }})

Creating Passcode in DEFORM Services windows by Authorized user

**Authorized DEFORM user:**

For a DEFORM user, if your user name and computer name is listed in a text file called**authorized_users.txt** then you are called an authorized DEFORM user.

As an authorized DEFORM user, you have full control of the DEFORM services. You can:

  1. Access the DEFORM Services to all DEFORM computers.
  2. Set or change the DEFORM Services passcode
  3. Update the DEFORM license password file (DEFORM.PWD)

The authorized_users.txt is located at DEFORM license folder on the DEFORM server machine.

It has the following format:

  * user_name1@computer_name1
  * user_name2@computer_name2

If the**authorized_users.txt** file does not exist, you can create one with a text editor

Please follow the above format to configure the authorized DEFORM users. Following guidelines can be used while creating authorized users,

  * Please use real user name and computer name in your system
  * Please only list the users who manage the DEFORM system as authorized DEFORM users
  * If you do not have the privilege to edit the authorized_users.txt file, please ask your IT admin for help.

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image015.jpg' | relative_url }})

a. Authorized user DEFORM Services Main window.

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image016.jpg' | relative_url }})

b. Non Authorized user DEFORM Services main window

Showing Authorized user and Non Authorized user DEFORM Services Main window

**Updating Simulation services modules:**

After installing DEFORM Services, if we are observing ![]({{ '/assets/icons/pre_icons/error_status_icon.jpg' | relative_url }}) status then it could be due to the Simulation services files not available or available files are outdated, then we need to update the files by using update button available next to the DEFORM computer which is displaying the error. User requires Passcode to update the services. When we click on ![]({{ '/assets/icons/pre_icons/mo_deform_setup_update_icon.jpg' | relative_url }}) Update button then Simulation Server (SS), Simulation Client (SC), and Web-based Simulation Monitoring server (RS) files are copied to Configuration folder and we can see the message as

“Updating sim_modules on TESTING1 ...

SUCCESS”, TESTING1 is the computer which was showing an error (See Fig. 3.1.24.). 

After successfully updating the Simulation services we can start the services by clicking on ![]({{ '/assets/icons/pre_icons/run_action_icon.jpg' | relative_url }}) button. If the DEFORM system is other than local then we need to enter Username and password of the System else we need not. The services will be run under the Username which is entered while starting the service. In case of local system is Windows, the service will be started automatically under the current active logged username when we click on ![]({{ '/assets/icons/pre_icons/run_action_icon.jpg' | relative_url }}) button (See Fig. 3.1.26.), while local system is Linux Username (default username from deformscd file will be displayed) and password must be entered to start the service.

Before updating Simulation services files, we need to Stop the services that are running and then need to update the files.

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image017.jpg' | relative_url }})

a. When Simulation services are outdated or not available

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image018.jpg' | relative_url }})

b. After updating Simulation services

Updating Simulation services files in DEFORM Services window

**Different status of Simulation server**

\-- | Simulation server not added in Simulation server tab  
---|---  
STOPPED | Simulation server added but not running  
outdated | Simulation server added previously but disconnected now  
RUNNING | Simulation server added and running  
  
**Update License Password file:**

Using Update License Password file button authorized user can update the password file when he receives new license password file (See Fig. 3.1.25.). You must restart the License Server after updating password file.

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image019.jpg' | relative_url }})

Updating License password file from DEFORM Services

**Controlling Services on Server Computer**

We require pass code to stop the services License server, Batch queue server and Web-Based Service Control on server computer in Windows while in Linux we require passcode even to start these services. If we stop the License server service even Batch queue Server service will also be stopped along with all Simulation Server and Simulation Client services on all DEFORM systems connected to that server, see Fig. 3.1.26.

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image021.jpg' | relative_url }})

Prompting to enter Passcode to stop the Batch queue Server Service

![]({{ '/assets/images/starting_up_deform/3_license_manager/3_1_deform_license_setup/3_1_image020.jpg' | relative_url }})

Prompting to enter user name and Password to Start the other user services

**Related Topics:**

[3.2. License Monitoring](/docs/en/starting_up_deform/3_license_manager/3_2_license_monitoring/)

[3.3. Services Monitoring](/docs/en/starting_up_deform/3_license_manager/3_3_services_monitoring/)

[3.4. Trouble Shooting License Issues](/docs/en/starting_up_deform/3_license_manager/3_4_trouble_shooting_license_issues/)

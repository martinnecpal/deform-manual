---
lang: sk
title: "2.1. Installation of DEFORM V14.0.2. in Windows"
---

# 2.1. Installation of DEFORM V14.0.2 in Windows

2.1.1. INTRODUCTION

2.1.2. INSTALLATION REQUIREMENTS

2.1.3. INSTALLING THE SECURITY KEY DEVICE

2.1.4. INSTALLING DEFORM v14.0.2 IN WINDOWS

2.1.5. UPDATING THE DEFORM LICENSE PASSWORD FILE

2.1.6. QUESTIONS / PROBLEMS

2.1.7. COMMAND LINE INSTALLER OPTIONS

2.1.8. WINDOWS START MENU

## INTRODUCTION

The following steps are to be executed in order to install DEFORM v14.0.2 (Subsequent service packs also follow a similar sequence, but install in a different folder and create new short cuts accordingly).   
These steps include:

  * Meeting the minimum system requirements.

  * Installing the DEFORM v14.0.2 program files.

  * License Manager (Installing the Security Key Driver v7.6.9).

  * Support Codes ( MPICH2 v1.2 64-bit and MiKTeX v21.4)

  * v14.0.2 files

  * Troubleshooting, should you run into problems.

Installing DEFORM is started by running **DEFORM_System_Installer_v14.0.2.exe.**  
Running this installer will give the user the option to choose which parts of DEFORM to install.See section 2.1.4. for more details.

**DEFORM_License_Manager_Installer_v14.0.2.exe** installs the DEFORM License Manager and Batch Queue.  
**DEFORM_Core_Installer_v14.0.2.exe** installs the DEFORM system.  
**DEFORM_Service_Control_Installer_v14.0.2.exe** installs the DEFORM Service Control. This is new from v11.2 and allows for managing DEFORM services via the DEFORM Services tab of the DEFORM Setup application.

Unless told otherwise by SFTC support, installation of any part of DEFORM should be handled by running **DEFORM_System_Installer_v14.0.2.exe**.

## INSTALLATION REQUIREMENTS

  * Operating system: Windows 10, and 11 (64-Bit only) (Server Versions are not supported.)

  * Suggested RAM: 16+GB

  * Hard drive space required for installation: ~12GB.

## INSTALLING THE SECURITY KEY DEVICE

The Security Key allows the DEFORM v14.0.2 system to be highly portable while still allowing only one system to be operable as a license server with a valid password at any time. The actual software can be installed on as many computers as you like, but each DEFORM system will only be operable with the Security Key attached or is configured as a client connected to a valid DEFORM license server. The Security Key is a USB key. Plug the Security USB hardware Key into the USB port. 

  
**CAUTION** :  
The Security Key keeps track of the date on your PC. Make sure the date is correct before initially running DEFORM v14.0.2. Changing the date backwards or forwards may make the DEFORM v14.0.2 system inoperable.

  
When uninstalling an earlier version of DEFORM v14.0.2. (alpha or beta versions) then the sentinel security hardware key must be unplugged during uninstallation and plugged back in after uninstallation. 

## INSTALLING DEFORM v14.0.2 IN WINDOWS

The DEFORM v14.0.2 installer is available for download from the DEFORM User Area website (<https://support.deform.com>). All supporting (required and optional) code is included in subfolders.

  
**Before Installation:**

  1. ****Uninstall the previous version of the License Manager and the Sentinel key drivers (If user is uninstalling an earlier version of DEFORM v14.0.2 (alpha or beta) detach the hardware key while uninstalling the sentinel key driver and plug it back in after uninstallation.

  2. Before beginning to install DEFORM v14.0.2 in Windows, it is necessary for the user to be logged in as an Administrator.

  3. Antivirus programs should be temporarily disabled during installation. They can cause substantial delays and/or installation problems.

**Procedure:**

****

  1. Start up Windows (Log in as the Administrator or with Administrator privileges).

  2. Extract the contents of the downloaded zip file into a suitable location with a minimum of 3.5 GB of free space.

  3. Open an Explorer window, go to the extracted folder and double-click the **DEFORM_System_Installer_v14.0.2.exe** file.

  4. Select the setup language like English, Japanese, Italian, Deutsch, etc. and click **OK** as shown in Fig. 2.1.1.

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0001.jpg' | relative_url }})

DEFORM Setup language selection window

  1. The Deform System installer v14.0.2 setup welcome window comes up as shown in Fig. 2.1.2. Click the **Next** button. 

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0002.jpg' | relative_url }})

Deform system installer welcome window 

  1. Accept the DEFORM License (See Fig. 2.1.3.)

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0003.jpg' | relative_url }})

DEFORM License Agreement window

  1. If the default DEFORM Setup installation location needs to be changed then browse to the location and click the **Next** button. (See Fig. 2.1.4.)

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0004.jpg' | relative_url }})

DEFORM installation location selection window 

If any other DEFORM versions are present in the same path then a "Folder Exists" popup asks whether to install to the same folder or not, so click the **Yes** button. (See Fig. 2.1.5.) 

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0005.jpg' | relative_url }})

Folder Exists popup 

  1. Select the features of the DEFORM system installer you wish to install from the list in the Select Components window as shown in Fig. 2.1.6. At the top of the window a menu box can be used to choose between different types of installations, including Client only and Server only. This choice will update the components selected for installation. (See Fig. 2.1.7.) Click the **Next** button to continue.

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0006.jpg' | relative_url }})

DEFORM select components window

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0007.jpg' | relative_url }})

DEFORM select components window combo box

For the initial setup all options should be selected to install the entire DEFORM v14.0.2 system and supporting code. Check the sections that match your license and the appropriate shortcuts will be created in the Windows start menu. The License Manager is a required component of the install pack and if a previous License Manager version is already installed then uninstall before installing the new license manager. If the license manager version is the same then there is no need to install. The Support Code option will launch the installers for MPICH, MiKTeX, and the Microsoft C++ redistributables, though these can be individually (de)selected.

Starting with DEFORM v11.2, the DEFORM Service Control allows for the starting and stopping of DEFORM services on the server and also allows for updating the services programs on DEFORM client computers. Therefore, it is required to install it on all the computers where the DEFORM system is installed regardless of versions.

Starting with DEFORM v12.0, the MiKTeX installer is included as a part of the Support Code.MiKTeX is used with report generation.  
Starting with DEFORM v13.0, the 32-bit MPICH installer has been removed.  
Starting with DEFORM v13.0, the Microsoft C++ 2015 64-bit Redistributable is part of the Support Code.  
Starting with DEFORM v13.1.1, the Microsoft C++ 2008 32-bit and 64-bit Redistributables have been update to v9.0.3.30729.6161.  
Starting with DEFORM v13.1.1, Python 3.12.2 is an optional installation.  
Python is used by the (currently beta) DEFORM API system. The DEFORM API allows users to access DEFORM functionality from Python scripts.  
Python is also needed for the optional Web-based Service Control. Web-based Service Control allows for access to DEFORM services (as seen in the “DEFORM Services” tab of DEFORM Setup) from a web browser

Starting with DEFORM v14.0.1, the MiKTeX installer has been updated to 24.1. 

Click the **Next** button after selecting the products that match your license.

_**DEFORM v14.0.2 and License Manager v14.0.2 Installation Options**_

  1. Select the “Configure Windows Firewall” checkbox to allow the DEFORM programs and the License and batch queue services access through the Windows firewall as shown in Fig. 2.1.8. and then click the **Next** button.

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0008.jpg' | relative_url }})

DEFORM Windows Firewall configuration window

_**DEFORM License Manager v14.0.2 Installation Options**_

  2. If the License Manager v14.0.2 component is selected, the DEFORM installer will present options relating to the License Manager. If the machine is a license server system (where the hardware key is plugged in), the DEFORM license password file supplied by SFTC must be selected. Browse to the password file to select it. Otherwise don't select a password file. Click the **Next** button to continue. (See Fig. 2.1.9.)

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0009.jpg' | relative_url }})

DEFORM License Manager Password browsing window

  1. Select the “Install Batch Queue Server” checkbox, which is required for queuing simulations as shown in Fig. 2.1.10. and then click the **Next** button.

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0010.jpg' | relative_url }})

DEFORM License Manager additional task selection window 

_**DEFORM v14.0.2 Installation Options**_

  1. If the DEFORM v14.0.2 component is selected, the DEFORM installer will present options relating to DEFORM. Starting with DEFORM v13.1, there is a new option to choose the FEM Engine. SFTC recommends using the Intel® Fortran option unless the Absoft Fortran compiler is being used or DEFORM is installed on a computer using a legacy (non-modern) CPU. Please be aware that the Intel Fortran option is compatible with both Intel Core and AMD Ryzen CPUs. Make your FEM engine selection as shown in Fig. 2.1.11. and click the **Next** button. Note that starting with DEFORM v14.0.2, the Absoft Legacy FEM engine is no longer available. 

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0011.jpg' | relative_url }})

DEFORM Setup FEM Engine window 

  1. Confirm the DEFORM Setup settings and click the **Install** button to install the DEFORM files. Otherwise click the **Back** button to change any settings. (See Fig. 2.1.12.)

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0012.jpg' | relative_url }})

DEFORM Setup settings confirmation window

  1. DEFORM setup will proceed to install all the components selected and take several minutes for installation as shown in Fig. 2.1.13.

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0013.jpg' | relative_url }})

DEFORM System installing status window 

Note that the MiKTeX installer will be displayed, but no interaction is required as shown in Fig. 2.1.14.

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0014.jpg' | relative_url }})

MiKTeX installer status window 

  1. Under certain conditions, namely if the Sentinel Key Driver installer is selected, DEFORM will require the computer to be restarted prior to running DEFORM Setup. If the window shown in Fig. 2.1.15. is shown, DEFORM Setup will run at Windows login the next time Windows is rebooted. Click the **Next** button to continue setup as shown in Fig. 2.1.15.

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0015.jpg' | relative_url }})

DEFORM requires reboot window

  1. Click the **Finish** button to end the installation as shown in Fig. 2.1.16.

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0016.jpg' | relative_url }})

DEFORM System Installer setup completion window 

  1. If the DEFORM installer recommends restarting the computer, select the “Yes, restart the computer now” radio button and click the **Finish** button to restart the computer as shown in Fig. 2.1.17.

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0017.jpg' | relative_url }})

DEFORM System Installer setup restart window 

Upon completion of the installation, DEC_SC.EXE, found at "<Installation path>\DEFORM\Configuration\DEF_SC.EXE", will launch.  
This DEFORM service utility program (DEC_SC.EXE) will be run as a "service" on Windows PCs.  
This service communicates with the License Server and, in the DEFORM Setup program, the user can monitor the status of the Simulation Server (SS), Simulation Client (SC), and Web-based Simulation Monitoring server (RS) on any DEFORM computer. As discussed in the next section, the DEFORM Services tab can be used to update them as needed.

  1. The DEFORM Setup application will launch next. Here you can configure the license server location and save those changes.

If the license server is running on a remote machine, select the "On Remote License Server" radio button and enter the remote server machine name or IP address. Click the **Synchronize** button. If the license server is running on the remote machine the user will get a license server running status as shown in Fig. 2.1.18. Otherwise an error popup indicating "Can not connect to license server" is shown.

If the license server is running on this local machine then select the "On Local Computer" radio button and click the **Synchronize** button.

Once synchronization is successful, whether the license server is running on the local computer or a remote computer, click the **Save** button to save the settings. (See Fig. 2.1.18.) 

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0018.jpg' | relative_url }})

DEFORM Setup License Server window 

  
After the synchronize button is clicked, if the current computer hasn’t been set up as a Simulation Server for the current version and path, DEFORM Setup will offer to add it as one (Fig. 2.1.19.)

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0019.jpg' | relative_url }})

DEFORM Setup Simulation Server window

If the Yes button is clicked to add the Simulation Server, DEFORM Setup will not automatically save the change to the License Server, but will prompt to save the changes. (See Fig. 2.1.20.) Verify the change is correct in the Simulation Server tab before saving the settings.

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0020.jpg' | relative_url }})

DEFORM Setup reminder to save

The Simulation Server tab allows for managing computers connected to the License Server. As shown in Fig. 2.1.21., the top area of the tab shows the defined Simulation Servers. If the local computer isn’t defined as a Simulation Server, click the "Add Simulation Server" button to define it.  
When adding a Simulation Server, by default the local computer will be defined, and some values will be set automatically. These defaults include the processor type, the number of processors, the maximum number of jobs, and the latest version will be set to the current path.  
When the License Manager is on the same computer that DEFORM Setup is being run on, as many Simulation Servers as required can be defined. However if the License Manager is on a different computer, only the local Simulation Server can be defined and edited.

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0021.jpg' | relative_url }})

DEFORM Setup Simulation Server window

The **Versions** column shows a list of all versions defined for a given Simulation Server.  
The **Maximum** Jobs option allows setting the number of jobs in the queue that can be run simultaneously on the respective simulation server.  
The lower area shows details about the currently selected Simulation Server. (See  Fig. 2.1.22.)  
In the **Versions** tab, the disk location for multiple versions can be defined. Only one path per version is allowed.  
If the Processor Type is defined as a **Cluster** , the Clusters tab will be enabled and details about the cluster nodes can be defined.  
After making changes to the Simulation Server tab, click the Save button to save the settings.  
_**Note** : ___Install_ path information for each version is required to be defined for the Batch queue to work properly._

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0022.jpg' | relative_url }})

DEFORM Setup Simulation Server window

Running jobs on remote computers can be performed by using the Shared Folders tab. (See Fig. 2.1.23.)  
For more detailed information refer to Chapter [23.6. Running Shared folder Simulations.](/docs/sk/simulator/23_deform_simulator/23_6_running_shared_folder_simulations/)

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0023.jpg' | relative_url }})

DEFORM Setup Shared Folders window

The DEFORM Services tab allows for managing of DEFORM services as shown in Fig. 2.1.24. You have   
two options:

  1. Open DEFORM Services for local DEFORM computer.

  2. Open DEFORM Services for all DEFORM computers.

The first option is available for all DEFORM users, while the second option is only available to “authorized users”, or users who knows the “pass code” created by the authorized users.  
The “authorized users” and “pass code” are introduced to avoid misuse of the new capabilities provided by the DEFORM services tab. For more information, please follow the instructions provided in the DEFORM Setup user interface.

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0024.jpg' | relative_url }})

DEFORM Setup DEFORM Services window

The DEFORM Services tab allows for starting and stopping DEFORM services on the license server computer and DEFORM computers as well as updating the service applications on DEFORM computers. If any of the services are stopped, click the corresponding start button to start the service as shown in Fig. 2.1.25.

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0025.jpg' | relative_url }})

DEFORM Setup DEFORM Services window

When all the DEFORM services are marked as “running”, click the Close button as shown in Fig. 2.1.26.   
The Simulation Client and Simulation Server services should be running on DEFORM computers.   
The Web-based Simulation Monitoring and GeoCAD Server are optional.

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0026.jpg' | relative_url }})

DEFORM Setup DEFORM Services window

## UPDATING THE DEFORM LICENSE PASSWORD FILE

To update the DEFORM license file using DEFORM Setup, switch to the DEFORM Services tab. Click on the “update license password file” button next to the server name as shown in Fig. 2.1.27.

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0027.jpg' | relative_url }})

DEFORM Setup update license password file button

On the Update DEFORM license password file page, click the folder icon and browse to the password file. Then click the “**Update password file”** button as shown in Fig. 2.1.28.

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0028.jpg' | relative_url }})

DEFORM Setup select password file

Click to stop the License Server and click yes in the warning prompt, as shown in Fig. 2.1.29.

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0029.jpg' | relative_url }})

DEFORM Setup stop the License Server

Next, start any stopped Server service as shown in Fig. 2.1.30.

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0030.jpg' | relative_url }})

DEFORM Setup start Server services

  
Next, start any stopped Client service as shown in Fig. 2.1.31.

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0031.jpg' | relative_url }})

DEFORM Setup start Client services

## QUESTIONS / PROBLEMS

If you have any questions, comments, or problems installing DEFORM v14.0.2, contact:

**Scientific Forming Technologies Corporation**

**2545 Farmers Drive, Suite 200**

**Columbus, OH 43235 USA**

**Phone: (614) 451-8330**

**E-mail: support@deform.com**

**Or**

**Visit our website at**

**[http://www.deform.com](http://www.deform.com)**

## COMMAND LINE INSTALLER OPTIONS

Starting in v12.1, the DEFORM System installer allows for command line parameters to be passed to it. This is useful for system administrators in order to do automated installations. For automated installations, all options are optional except /CPUType; either modern or legacy must be specified.

**/LANG** =language

This option specifies the language the installer will use. When a valid /LANG parameter is used, the Select Language dialog will be suppressed. This affects the **Select Setup Language** dialog, as shown in Fig. 2.1.1.

Valid options:  
english, french, german, japanese, russian, spanish, italian, korean, chinesesimplified, chinesetraditional

  
**/DIR** ="path to install DEFORM to"

This option specifies the location to install DEFORM. This affects path in the Select Destination Location window, as shown in Fig. 2.1.4.

Default option: The default installation location is C:\Program Files\SFTC.

  
/ **COMPONENTS** ="comma separated list of component names"

This option specifies which components of DEFORM will be installed. Using this command line parameter causes Setup to automatically select a custom type, meaning all components will be unselected except the one’s passed to this parameter. This affects selected components in the **Select Components** window, as shown in Fig. 2.1.6.

Valid options:

  * LicenseManager

  * Installs the DEFORM License Manager but not the Sentinel Key Driver.

  * *LicenseManager

  * Installs the DEFORM License Manager and the Sentinel Key Driver. Note the asterisk before LicenseManager.

  * LicenseManager\Sentinel

  * Installs the Sentinel Key Driver and the DEFORM License Manager.

  * *SupportCode

  * Installs all the support code. Note the asterisk before SupportCode.

  * SupportCode\MPICH64

  * Installs the 64-bit MPICH.

  * SupportCode\MiKTeX

  * Installs MiKTeX.

  * SupportCode\vc32

  * Installs the 32-bit Microsoft C++ 2008 redistributable.

  * SupportCode\vc64

  * Installs the 64-bit Microsoft C++ 2008 redistributable.

  * SupportCode\vc2015x64

  * Installs the 64-bit Microsoft C++ 2015 redistributable

  * OptionalCodeP\Python

  * Installs Python. (Only required for DEFORM API and Web-based Service Control)

  * DEFORMComponent

  * Installs the DEFORM system.

  * ServiceControl

  * Installs the DEFORM Service Control.

Default option: The default option is to install all components except any optional components.

/**PasswordFile** ="path to DEFORM.PWD file"

This option specifies the location of the DEFORM password file. If the License Manager isn’t being installed, this is ignored. This affects the path in the **DEFORM Password** window, as shown in Fig. 2.1.9.

Default option: no password file specified.

/**BatchQueue** =batch queue option

This option specifies whether the Batch Queue Server should be installed or not. This affects the Install **Batch Queue Server** option in the **DEFORM License Manager** window, as shown in Fig. 2.1.10.

Valid options:

yes, no

Default option: yes

  
/ **Firewall** =firewall option

This option specifies whether to allow DEFORM programs access through the Windows firewall.

This affects the **Configure Windows Firewall** option in the Windows Firewall window, as shown in  Fig. 2.1.8.

Valid options:

yes, no

Default option: yes

/**FEMType** =FEM Fortran type option

New option starting with DEFORM v13.1. This replaces the CPUType option

This option specifies whether the Intel Fortran or Absoft Fortran FEM engine should be installed. This affects the **Intel Fortran (Default)** and **Absoft Fortran** options in the **FEM Engine** window, as shown in Fig. 2.1.11.  
Valid options:  
intel, absoft

Default option: intel

  
/ **SILENT**

Instructs the installer to run in silent mode. When Setup is silent the wizard window is not displayed but the installation progress window is.

There are no options for this parameter.

**/DEFORMSetup** =DEFORM Setup option

New option starting with DEFORM v13.0.1.

This option instructs the installer to launch DEFORM Setup to configure the license server.

Valid options:

yes, no

Default option: yes

  
**/ConfigurationFile** ="path to DEFORM_NLM_CONF file"

New option starting with DEFORM v13.0.1.

This option specifies the location of the License Server configuration file to use. This file is created by DEFORM Setup and is located in the Configuration folder, so run DEFORM Setup on at least one computer first and use it for additional installations.

This is useful for using the same configuration file on multiple computers and works well when setting the DEFORMSetup option to no.  
If an existing DEFORM_NLM_CONF file exists in the Configuration folder, it will be overwritten.

If installing the License Manager (either stand alone or as part of a node locked license) either DEFORM_NLM_CONF or DEFORM_NLM_CONF_SERVER can be used as the source file. In this case the file will also be copied to both the Configuration folder (as DEFORM_NLM_CONF) and the License Manager folder (as DEFORM_NLM_CONF_LMSERVER).

This overrides the LicenseServerName option.

Default option: no License Server configuration file specified.

**/****LicenseServerName** =”License Server name”

New option starting with DEFORM v13.0.1.

This option specifies the server name as shown in Fig. 2.1.18.

This is useful for using the same configuration file on multiple computers and works well when setting the DEFORMSetup option to no.

If an existing DEFORM_NLM_CONF file exists in the Configuration folder it will be overwritten.

This is ignored if the ConfigurationFile option is set.

Default option: no Server name specified

**Examples**

Install Node Locked  
DEFORM_System_Installer_v14.0.2.exe /LANG=english /SILENT

Install Client Installation  
DEFORM_System_Installer_v14.0.2.exe /LANG=english /COMPONENTS="*SupportCode,DEFORMComponent,ServiceControl" /SILENT

Install Server Installation with Password file

DEFORM_System_Installer_v14.0.2.exe /LANG=english /COMPONENTS="*LicenseManager, SupportCode\vc32,ServiceControl" /PasswordFile="C:\DEFORM.PWD" /SILENT

****

**Deprecated Options**

**legacy in /FEMType**  
This option has been deprecated starting with DEFORM v14.0.2. The legacy Absoft FEM engine has been retired.

**ReleaseNotes in /COMPONENTS**  
This option has been deprecated starting with DEFORM v14.0.

**/NodeLocked**  
This option has been deprecated starting with DEFORM v14.0.

**/CAD**  
This option has been deprecated starting with DEFORM v14.0. The GeoCAD Server option has been moved to DEFORM Setup.

**/CPUType**  
This option has been deprecated starting with DEFORM v13.1. The FEMType option supersedes this.

## WINDOWS START MENU

Starting with DEFORM v14.0.2, DEFORM Setup allows for selecting which DEFORM shortcuts appear in the Windows Start menu as shown in Fig. 2.1.32. The installer will include a selection of applications in the Start menu. To change these, applications can be selected in the New **start****menu** column. Clicking the **Update start menu** button will update the Start menu with the selected applications. The **Select all** and **Deselect****all** buttons are used to select and deselect all the optional applications, respectively. The **Refresh** button updates the Current start menu column, which shows the applications that are currently in the Start menu.

_Note that the Start menu tab won’t be displayed if DEFORM Setup is launched from the**DEFORM Setup for License Manager** Start menu item._

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_1_installation_of_deform_v12_0_1_in_windows/image0032.jpg' | relative_url }})

DEFORM Setup Start menu tab

**Related Topics:**

[3\. License Manager](/docs/sk/starting_up_deform/3_license_manager/3_introduction_to_license_manager/)

[3.4. Trouble Shooting License Issues](/docs/sk/starting_up_deform/3_license_manager/3_4_trouble_shooting_license_issues/)

[23.6. Running simulations remotely](../../../assets/images/simulator/23_deform_simulator/23_6_running_shared_folder_simulations)

[23.8. Trouble Shooting Simulation Running](../../../assets/images/simulator/23_deform_simulator/23_8_trouble_shooting_simulation_running)

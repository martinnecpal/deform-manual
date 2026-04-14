---
lang: sk
title: "2.2. Installation of DEFORM V14.0.2. in Unix or Linux"
---

# 2.2. Installation of DEFORM V14.0.2 in Unix or Linux

****

2.2.1. Introduction

2.2.2. Installation Requirements

2.2.3. The Security Key Device

2.2.4. Obtaining DEFORM Software

2.2.5. Installation Notes

2.2.6. LZMA / XZ Utilities installation

2.2.7. Python Installation

2.2.8. Sentinel Key Driver Installation

2.2.9. License Manager Installation

2.2.10. DEFORM Installation

2.2.11. Additional Installation

2.2.12. Setup a user account

2.2.13. DEFORM Setup

2.2.14. System Execution

2.2.15. Questions / Problems

2.2.16. CPU Types

## INTRODUCTION

The following steps are to be executed in order to install DEFORM v14.0.2. (Subsequent service packs also follow a similar sequence, but install in a different folder). These steps include: 

  * Meeting the minimum system requirements. 

  * Installing the DEFORM v14.0.2 program files. 

  * License Manager (Installing the Security Key Driver v7.6.3). 

  * v14.0.2 files 

  * Support Codes (lzma/xz utils, tar, MPICH2 v1.3.1 64-bit, Python, openSCAD, and TeX Live) 

  * Troubleshooting, should you run into problems. 

## INSTALLATION REQUIREMENTS

  * Operating system:

  * CentOS (Red Hat Enterprise Linux) 6.10+ Linux (x86_64)

  * CentOS (Red Hat Enterprise Linux) 7.7+ Linux (x86_64)

  * Red Hat Enterprise Linux (RHEL) 8.8+ (x86_64)

    * Red Hat 8 support is currently in beta

  * Suggested RAM: 16+ GB

  * Hard drive space required for installation: ~8 GB 

  * Supporting Software:

  * LZMA/XZ Utils

  * GNU Tar

## The Security Key Device

The Security Key allows the DEFORM v14.0.2 system to be highly portable while still allowing only one system to be operable as a license server with a valid password at any time. The actual software can be installed on as many computers as you like, but each DEFORM system will only be operable with the Security Key attached or is configured as a client connected to a valid DEFORM license server. The Security Key is a USB key. Plug the Security USB hardware Key into the USB port.

**CAUTION** :

The Security Key keeps track of the date on your PC. Make sure the date is correct before initially running DEFORM v14.0.2. Changing the date backwards or forwards may make the DEFORM v14.0.2 system inoperable.

## Obtaining DEFORM Software

The DEFORM v14.0.2 pack is available for download from the DEFORM User Area website at <https://support.deform.com>.

The DEFORM password file (DEFORM.PWD) is available for download from the DEFORM User Area website at <https://support.deform.com>. or by contacting Ms. Engelbrecht at [mengelbrecht@deform.com](http://mengelbrecht@deform.com).

The Sentinel hardware key driver is available for download from <https://www.deform.com/redirects/sentinel.html>. Driver v7.6.2 installer is also available for download from the DEFORM User Area website at <https://support.deform.com>. 

## Installation Notes

  1. In order to install DEFORM v14.0.2 you need to have root access on the system where you want to install the software. Instructions requiring root access are denoted by beginning with [root].

  2. The user’s system must have the supporting software required to install the DEFORM software.

  3. The examples shown assume installation on CentOS Linux unless otherwise specified. 

## LZMA / XZ Utilities installation 

DEFORM on Linux is distributed as a GNU tar file compressed with LZMA. The installation files must be uncompressed using an LZMA decompression tool; the resulting file must then be unpacked using GNU tar. Direct login as root is required to carry out installation.

  
Check to see if LZMA/XZ is already installed on your system by issuing the following command:  
On CentOS 7 and Red Hat (RHEL)8:

xz --version

On CentOS 6:

lzma --version

If XZ is installed, the response will be similar to:

xz (XZ Utils) 5.5.2

liblzma 5.2.2

If LZMA is installed, the response will be similar to:

LZMA command line tool 4.32.7

LZMA SDK 4.43

If you receive an error with the above command, but you know that LZMA/XZ is installed on your system, modify the system path to include the path to the LZMA/XZ binaries. If LZMA/XZ is installed, running the ‘which  lzma’ or ‘which xz’ command will return the path.

If the LZMA/XZ Utilities are not installed on your system, the easiest way to install LZMA/XZ is through the system’s package manager.

CentOS 7 and Red Hat (RHEL)8:

yum install xz

CentOS 6:

yum install lzma

LZMA is also available in the DEFORM User Area for manual installation. Download the appropriate rpms for your system to a writable directory. Both the lzma-4* and lzma-libs-4* rpms are required. Obtaining the files from the User Area is the easiest method. Precompiled rpm files for CentOS (Red Hat Enterprise Linux Compatible) Linux are available at <https://tukaani.org/lzma>.

Once the rpms are in a writable directory, the lzma-libs-4* rpm needs to be installed first. Some Linux variants (more recent versions of Centos Linux) allow the files to be installed by double clicking on them in the File Browser. If this method is available, a root password will be requested and then the file will be installed. Make sure to install both of the lzma files.

Alternatively, the files can be installed with the following command (issued as root) from the directory containing the files:

rpm –Uvh lzma-4.32.7-1.el4.rf.x86_64.rpm lzma-libs-4.32.7-1.el4.rf.x86_64.rpm

## Python Installation 

  1. Starting with DEFORM v13.1, Python only needs to be installed if using Web-based Service Control or Email notifications. 

  2. [root] On some versions of Linux, the included version of Python may be too old for the DEFORM Services utility to run. If a newer version isn’t available through a repository *yum, zipper), follow these instructions for updating to Python 2.7. 

wget http://www.python.org/ftp/python/2.7.2/Python-2.7.2.tgz 

tar -xzvf Python-2.7.2.tgz

cd Python-2.7.2 

./configure 

make install 

If there are any problems installing Python, gcc might need to be installed first. On CentOS, type _yum install gcc_ . 

## Sentinel Key Driver Installation

  1. The 7.6.2 driver zip (sentinel_protection_installer_7.6.2_linux.zip) is available in   
the installed License Manager at /usr/local/SFTC/LicenseManager/UTILS/. See section 2.2.9. for details on installing the License Manager.

  2. Copy the compressed Sentinel key driver archive file to a writeable directory on the system on which you wish to install it.

  3. [root] Run the following commands to install the driver.

cd /path_to_zip

unzip sentinel_protection_installer_7.6.2_linux.zip

cd sentinel_protection_installer_7.6.2

chmod +x protection_install.sh

./protection_install.sh

  1. Insert the USB key into the computer. In the case of using a cluster, insert the key into the Master node.

  2. [root] Start the driver daemon.

cd /opt/safenet_sentinel/common_files/sentinel_usb_daemon

./load_daemon.sh start

./load_daemon.sh support

  1. [root] Repeating ./load_daemon.sh start a second time should indicate that the daemon is already running. Any subsequent system restart will initiate this service enabling the DEFORM License Manager to communicate with the hardware key and the password file.

  2. Using some versions of this driver (like v7.4 and greater), requires the user to manually maintain compatibility with previous releases for restart/reboot sequence of the machine. (‘./load_daemon.sh support’ is required to be executed manually on each system restart).

  3. DEFORM requires the v7.1 driver or later. With driver v7.1, the default location of the daemon startup script is /opt/sentinel/sud/usb.

## License Manager Installation

The DEFORM License Manager can be run on the same Linux machine that DEFORM is installed on or any other supported Linux machine or PC on the network.

  1. If an earlier version of DEFORM or the License Server is installed, run the following command to stop the existing DEFORM services.

_/etc/init.d/deformscd cleanstop_

  1. Copy the compressed License Manager archive file to a writeable directory on the system on which you wish to install it.

  2. Decompress the tar.lzma file.

  1. On CentOS 6 use unlzma.

unlzma DEFORM_LicenseManager_v14_0_2_CentOS_v6.x_x86_64.tar.lzma

  1. On CentOS 7 use unxz.

unxz DEFORM_LicenseManager_v14_0_2_CentOS_v7.x_x86_64.tar.lzma

  1. [root] Create the installation directory for DEFORM.

mkdir /usr/local/SFTC

  1. [root] Change into the installation directory.

cd /usr/local/SFTC

  1. [root] Untar the uncompressed installation file.

tar –xvf /path_to_file/DEFORM_LicenseManager_v14_0_2_CentOS_v6.x_x86_64.tar

  1. [root] Required System Libraries. Depending on the how the operating system was installed, some 64-bit systems may be missing some required 32-bit system libraries required by DEFORM. Run the commands below to install the most likely missing libraries. This requires access to a valid software repository.  
_cd /usr/local/SFTC/LicenseManager/UTILS  
./DEF_INSTALL_LIBS.sh _

  2. [root] Run the following script to set up the DEFORM services. This will set up deformlmd, deformbqd, and deformscd which are required to start the services for license manager, batch queue server, and services control.

cd /usr/local/SFTC/LicenseManager/UTILS

./DEF_INSTALL_SERVERS.sh

  1. [root] If the License Manager is installed in the default location (/usr/local/SFTC) this step can be skipped.

The deform* scripts in /etc/init.d need to contain the correct paths. Please edit each deform* file and update the paths contained to point to the installation location used.

  1. The Services Control cannot be run as root. The script at /etc/init.d/deformscd assumes that a non-root user named “deform” exists. If there isn’t a non-root user named “deform” adjust the line below to reference an existing, non-root user.

export DEFORM_SIM_USER=deform

The Services Control needs to be started before running DEFORM Setup. Do not launch the service using “service deformscd start”; this will cause problems with report generation. Instead launch it as shown below.

  
_/etc/init.d/deformscd start_

  1. [root] If the DEFORM.PWD has not been downloaded yet, please see section 2.2.4. Obtaining DEFORM Software now. Copy DEFORM.PWD to the directory where the DEFORM License  Manager has been installed. The default installation location is /usr/local/SFTC/LicenseManager. Make sure that this file has read permissions enabled for all users (the chmod command can be used).

cd /usr/local/SFTC/LicenseManager

cp /path_to_file/DEFORM.PWD 

chmod +r DEFORM.PWD

  
NOTE: On a system reboot, the license manager, batch queue, and services control services should get started automatically, and any user login should be able to use these services.

NOTE: Running the License Manager requires that the Sentinel key driver has been installed. After the driver has been installed (following the steps listed above), the License Manager will be started automatically after a reboot in most Linux systems.

NOTE: If a user wants to restart the DEFORM License Manager without rebooting the machine (e.g. if a new DEFORM.PWD file needs to be installed) they can log in as root and run the following commands.

  
/etc/init.d/deformlmd restart

/etc/init.d/deformbqd restart

  1. [root] Start the DEFORM services.

 _/etc/init.d/deformbqd start  
/etc/init.d/deformlmd start  
/etc/init.d/deformscd start_

  1. If DEFORM is going to be installed on this same computer proceed to the next section, 2.2.10. DEFORM Installation. Otherwise skip to section 2.2.11. Additional Installation. 

## DEFORM Installation

  1. If an earlier version of DEFORM or the License Server is installed, run the following command to stop the existing DEFORM services.  
_/etc/init.d/deformscd cleanstop_

  2. Copy the compressed License Manager archive file to a writeable directory on the system on which you wish to install it.

  3. Decompress the tar.lzma file.

  1. On CentOS 6 use unlzma.

unlzma DEFORM _v14_0_2_CentOS_v6.x_x86_64.tar.lzma

  1. On CentOS 7 use unxz.

unxz DEFORM_ v14_0_2_CentOS_v7.x_x86_64.tar.lzma

  1. [root] Create the installation directory for DEFORM.

mkdir /usr/local/SFTC

  1. [root] Change into the installation directory.

cd /usr/local/SFTC

  1. [root] Untar the uncompressed installation file

tar –xvf /path_to_file/DEFORM _v14_0_2_CentOS_v6.x_x86_64.tar

  1. [root] **Required System Libraries**. Depending on the how the operating system was installed, some 64-bit systems may be missing some required 32-bit system libraries required by DEFORM. Run the commands below to install the most likely missing libraries. This requires access to a valid software repository.

cd /usr/local/SFTC/DEFORM/v14.0.2/UTILS  
./DEF_INSTALL_LIBS.sh  

  1. [root] Run the following script to set up the DEFORM services. This will set up deformlmd, deformbqd, and deformscd which are required to start the services for license manager, batch queue server, and services control.

_cd /usr/local/SFTC/DEFORM/v14.0.2/UTILS  
./DEF_INSTALL_SERVERS.sh _

__

  2. [root] If the License Manager is installed in the default location (/usr/local/SFTC) this step can be skipped. 

The deform* scripts in /etc/init.d need to contain the correct paths. Please edit each deform* file and update the paths contained to point to the installation location used.

  1. [root] The Services Control cannot be run as root. The script at /etc/init.d/deformscd assumes that a non-root user named “deform” exists. If there isn’t a non-root user named “deform” adjust the line below to reference an existing, non-root user.

export DEFORM_SIM_USER=deform

The Services Control needs to be started before running DEFORM Setup. Do not launch the service using “service deformscd start”; this will cause problems with report generation. Instead launch it as shown below.

/etc/init.d/deformscd start

  1. [root] **Report Generation Libraries**. Starting with DEFORM v12.0.1 report generation requires the Latex PDF library. Run the commands below to install the Latex libraries.

cd /usr/local/SFTC/DEFORM/v14.0.2/UTILS

./DEF_INSTALL_LATEX.sh

  1. **3D Machining**. Starting with DEFORM v11.1, the 3D machining module is enhanced to include creation of drill bit geometry, which requires the following additional steps.

  1. Copy the openscad-2014.03.x86-32.tar.gz file from

/usr/local/SFTC/DEFORM/v14.0.2/UTILS folder to a writeable folder

  1. unzip this using tar command "_tar -xzvf openscad-2014.03.x86-32.tar.gz_ "

  2. Go to the resulting folder "_cd openscad-2014.03_ "

  3. [root] Install the package "_./install.sh_ ".

  1. [root] **64-bit FEM Engine installation**. Starting with DEFORM v10.2 support for 64-bit 3D FEM engine has been extended to Linux. On these 64-bit operating systems, the 64-bit 3D FEM support includes user routine support as well. From GUI Main, in the Run Options dialog, user can now select to run the model in 32-bit mode or 64-bit mode. Related instructions on the user routine compilation in 64-bit mode are available in the system documentation (please refer to Chapter [56.3. 3D User Defined FEM Routines](/docs/sk/user_routines/56_user_routines_in_deform/56_3_3d_user_defined_fem_routines/) system documentation). Starting with DEFORM v10.2.1 for 64-bit MPI support, the mpich1 library has been updated to mpich2 for 64-bit MPI support (no change for 32-bit MPI support which still uses mpich1). Starting with DEFORM v11.1 the mpich2 library was updated.

Run the following commands to install mpich2 for 64-bit DEFORM.

_cd /usr/local_

_tar -xvf /usr/local/SFTC/DEFORM/v14.0.2/UTILS/mpich2-1.3.1.tar_

In user .cshrc file, add these 2 environment variables.

_setenv DEFORM_MPI MPICH2_

_setenv MPI_ROOT /usr/local/mpich2-1.3.1_

NOTE: The MPI_ROOT definition is only needed if the mpich2 installation is not made in the /usr/local path.

NOTE: Starting with DEFORM v11.1 64-bit support has been also extended to 2D FEM, but has no MPI support.

  1. [root] **64-bit FEM Engine setup**. Starting with DEFORM v13.1.1, there is a new option to choose the FEM Engine. For Centos 7, the Intel® Fortran compiler has been added, and is installed by default. SFTC recommends using this option unless the Absoft Fortran compiler is being used or DEFORM is installed on a computer using a legacy (non-modern) CPU. For Centos 6, the Intel Fortran option is not available, so the Absoft Modern Engine is installed by default. SFTC recommends the modern Absoft Fortran compiler option unless DEFORM is installed on a computer using a legacy (non-modern) CPU. Please be aware that the Intel Fortran option is compatible with both Intel Core and AMD Ryzen CPUs. Note that starting with DEFORM v14.0.2, the Absoft Legact engine is no longer available.

a. In order to change the FEM engine, run the commands below and follow the prompts.

cd /usr/local/SFTC/DEFORM/v14.0.2/UTILS

./DEF_SETUP_FEM.sh

##  Additional Installation

  1. **Permissions**. For simulations being run by a user other than the defined simulation server user, the following minimum permission requirements must be met.

  1. The DEFORM user and Simulation Server users must be in each other’s primary groups.

  2. The DEFORM user and Simulation Server user must have a umask that allows for full permissions for user and group. i.e. umask 007

  3. The DEFORM user’s home directory must be group readable.

  4. Run _/usr/local/SFTC/DEFORM/v14.0.2/UTILS/DEF_CHECK_CONFIG.sh_ from a problem directory to check for these and any other related permission issues. Please have your systems administrator check the output of this check before contacting SFTC Support. Note that some errors may appear depending on when this step is run (for example, if a user account hasn’t been setup yet).

  1. Set the root environment to contain DEF_CFG_DIR by adding the following to root’s shell configuration file (_~/.cshrc_) file:

_setenv DEF_CFG_DIR '/usr/local/SFTC/DEFORM/Configuration'_

  
NOTE: This will also need to be defined in the user’s environment as well as explained in section. 2.2.12. Setup a user account.

  1. **User defined post functionality** **in 64-bit mode**. In order to use user defined post functionality in 64-bit mode.

  1. The system must have Absoft v11.0 (64-bit) compiler installed on the machine.

  2. The user shell configuration file (~/.cshrc) needs to have the following line.

setenv LD_LIBRARY_PATH /opt/absoft11.0/shlib64

  
If the above haven’t been setup you may encounter the following error when loading a 64-bit .SL file to activate user defined post functionality.  
"libaf77math.so: cannot open shared object file : No such file or directory."

  1. [root] The Services Control cannot be run as root. The script at /etc/init.d/deformscd assumes that a non-root user named “deform” exists. If there isn’t a non-root user named “deform” adjust the line below to reference an existing, non-root user.

export DEFORM_SIM_USER=deform

The Services Control needs to be started before running DEFORM Setup. Do not launch the  
service using “service deformscd start”; this will cause problems with report generation. Instead launch it as shown below.

/etc/init.d/deformscd start

## Setup a user account

Some Linux distributions don’t have csh, but instead have tcsh, such as RHEL 8. In this case using tcsh is fine; just replace .cshrc below with .tcshrc.

Make sure the default login shell is "C" shell (csh). Users can determine their default login shell by using

  
cat /etc/passwd | grep ‘user name’

  
and observing the last segment of the system response. If csh is not the default login shell, the chsh command can be used to change this. To check the format of this command, type ‘man chsh’. We will assume the DEFORM user name is "user1" and the login directory is "/home/user1".

  
Log into the user account and edit the “C” shell login command file, ".cshrc", to include the following command lines (based on typical installation location):

  
setenv DEF_CFG_DIR '/usr/local/SFTC/DEFORM/Configuration'

setenv DEFORM23_DIR '/usr/local/SFTC/DEFORM/v14.0.2'

setenv DEFORM_DIR $DEFORM23_DIR/2d

setenv DEFORM3_DIR $DEFORM23_DIR/3d

setenv DEFORM_MPI MPICH2

setenv MPI_ROOT /usr/local/mpich2-1.3.1

source $DEFORM23_DIR/CONFIG.COM

umask 007

  
The first four command lines define the global symbols "DEF_CFG_DIR", “DEFORM23_DIR”, “DEFORM_DIR”, and “DEFORM3_DIR” to be the DEFORM product and license configuration locations. Lines five and six set up 64-bit DEFORM mpich2. The “source” line executes the DEFORM configuration file "CONFIG.COM" to set all the symbols needed (alias) to run the DEFORM system. For the symbols set in the configuration file CONFIG.COM, user should not override these symbols or define them any differently than the original text.

  
**Note** : The settings should be active for all shells, not just interactive shells.

  
User may log out of the system at this time. The next time you log into the system, the above command lines will be executed automatically.

  
If you decide to stay in the system at this time, you need to execute ".cshrc" manually since its contents have changed. To do that, enter ‘source .cshrc’.

  
Run the following commands to verify the environment variables are set correctly.

_echo $DEFORM_DIR_ (should result in 2d installation path)

_echo $DEFORM3_DIR_ (should result in 3d installation path)

_echo $DEFORM23_DIR_ (should result in integrated system installation path)

_echo $DEF_CFG_DIR_ (should result license configuration folder path) 

## DEFORM Setup

The Services Control needs to be started before running DEFORM Setup. Do not launch the service using “service deformscd start”; this will cause problems with report generation. Instead launch it as shown below.

_/etc/init.d/deformscd start_

Execute the setup program to indicate the installation path, and the server details for License Manager and Batch Queue servers.  
(based on the default installation path, change to the v14.0.2 folder and execute the setup)

_cd /usr/local/SFTC/DEFORM/v14.0.2_

_./DEFORMSetup.EXE_

(Appropriate X server settings are required to be set when this action is carried out from a remote machine) 

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_2_installation_of_deform_v12_0_1_in_linux/2_2_image001.jpg' | relative_url }})

DEFORM Setup Window

Once the DEFORMSetup dialog opens, the following basic information needs to be provided:

  * Machine name or IP address of where the license manager is running as identified in the network. 

  * License Manager Server Port to be defined as 34445. Please note that this number cannot be changed.

  * When you click on ‘Synchronize’ it should return a positive running status on the License Manager. If not, check the required components such as the Sentinel key driver daemon status, hardware key, running status on License Manager daemon, and the password file. 

  * Once synchronization is successful, whether the license server is running on the local computer or a remote computer, click the ‘Save’ button to save the settings.

  * Simulation server set up also needs the machine name hosting the service and the port number. In the event of multiple simulation server definitions, it is recommended to first read/synchronize the existing information from the license manager server, correct or add the information and save to the license manager server. Again, this information is only needed if Batch Queue is licensed. Please note that batch queue and simulation server setup is mandatory for running DOE and OPT jobs. Simulation servers can be started in the Simulation Server tab.

  * Please note that when any information is changed and saved in DEFORMSetup, the services could be interrupted while using the same server.

  * Configure the system firewall such that the ports used for DEFORM services (34444 and 34445 (License manager), 34446 (Batch Queue server), 34447 (Simulation server), and 34448 (DEFORM Services, with TCP) are accessible.

  * System ports for 34449+ need to be accessible as well. The number of ports that need to be opened in the range is dependent on the number of simultaneous DOE/OPT jobs that may run at any given time. 

The DEFORM Services tab allows for managing of DEFORM services and is new since v11.2.

You have two options:

  1. Manage the DEFORM Service running on your local computer.
  2. Manage the DEFORM Services running on all computers.

The first option is available for every DEFORM user. The second option is only available to the “authorized users” or users who know the “pass code” created by an authorized user.

![]({{ '/assets/images/starting_up_deform/2_deform_installation/2_2_installation_of_deform_v12_0_1_in_linux/2_2_image002.jpg' | relative_url }})

To set up a user to be an authorized user, you’ll need root access on the computer running the License Manager. In the License Manager folder (usually at

_/usr/local/SFTC/LicenseManager_) create or edit the file “authorized_users.txt”. In this file will be a list of users that are authorized users. The format of the list is: 

_user_name1@computer_name1_

_user_name2@computer_name2_

An authorized user has full control of the DEFORM services.

  * Access the DEFORM Services of all DEFORM computers.
  * Set or change the DEFORM Services pass code.
  * Update the DEFORM license password file (DEFORM.PWD).

The DEFORM Service pass code allows for access to DEFORM Services on all DEFORM computers from:

  * Any DEFORM computer (other than the authorized computer)
  * Any computer with a web browser (no need to install DEFORM)

Only an authorized DEFORM user can create or change the pass code.

The DEFORM Services tab allows for starting and stopping of DEFORM services on server and DEFORM computers as well as updating the service applications on DEFORM computers. If any of the services are stopped, click the corresponding start button to start the service.

## System Execution

The following procedure may be used to run the DEFORM system:

  1. Log into the DEFORM user account from an X-terminal

  2. Run the following commands to invoke the DEFORM system.

DEF_GUI |  Main interface for DEFORM  
---|---  
mo |  Integrated Manufacturing Process (MO)  
mo64 |  64-bit Integrated Manufacturing Process (MO)  
  
  1. A complete list of commands can be found by typing alias. 

## QUESTIONS / PROBLEMS

If you have any questions, comments, or problems installing DEFORM V14.0.2, contact:

**Scientific Forming Technologies Corporation**

**2545 Farmers Drive,****Suite 200**

**Columbus, OH 43235 USA**

**Phone: (614) 451-8330**

**E-mail:[support@deform.com](mailto:support@deform.com)**

**Or**

**Visit our website at<http://www.deform.com>**

## CPU Types

Here are some resources for determining the generation of your Intel CPU.

  
To determine the user CPU, type

cat /proc/cpuinfo | grep "model name"

This Intel site gives an overview of how to determine the generation of your Core-based CPU by comparing it to the detected CPU, as shown above.

<https://www.intel.com/content/www/us/en/processors/processor-numbers.html>

  
If you were unable to determine your Intel CPU generation from the above link, please try the following.

  1. Click on one of the following links (depending on CPU type) and search for your CPU.

For Intel Xeon CPUs:  
<https://en.wikipedia.org/wiki/List_of_Intel_Xeon_microprocessors>

For Intel Core i7 CPUs:

<https://en.wikipedia.org/wiki/List_of_Intel_Core_i7_microprocessors>

For other Intel Core CPUs, look at the “See also” section at the bottom of the Intel Core i7 CPUs page.

  
For example, if the instructions above display the detected CPU as:

model name : Intel(R) Core(TM) i7-6700 CPU @ 3.40GHz

Then search for “6700”.

There will be a link that will take you to Intel’s website with more information.

  1. Click that link.

  2. On the Intel page, the architecture can be found by looking at the code name “Products formerly _______”.

  3. Now you that you know the architecture, you can determine if it is older or newer than Haswell by clicking the following link and searching for the architecture.

<https://en.wikipedia.org/wiki/List_of_Intel_CPU_microarchitectures>

****

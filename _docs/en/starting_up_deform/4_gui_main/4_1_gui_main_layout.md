---
lang: en
title: "4.1. GUI Main layout"
---

# 4.1. GUI Main Layout

4.1.1. Integrated GUI Interface (GUI Main)

  * Pre-Processor

  * Simulator

  * Post-processor

4.1.2. Problem directory

  * Explore Tab

  * Queued Tab

  * Recent tab

4.1.3 Problem Files Section

  * Problem Files tab

  * All Files tab

  * Right mouse button click menu for Problem Files

4.1.4. Menu Bar

  * File Menu

  * Edit

  * View Menu

  * Pre-Processor Menu

  * Simulation Menu

  * Post Processor Menu

  * Tool Menu

  * Options

  * Layout

  * Help

4.1.5. Preview

4.1.6. Message

4.1.7. Log

4.1.8. Summary

4.1.9. Memo

## Integrated GUI Interface (GUI Main)

Integrated GUI Interface (GUI Main) in the DEFORM system guides the user by providing the links to various components of DEFORM under Pre-Processor, Simulator and Post-processor. In classic mode layout the GUI main has multiple sections such as Problem Directory, Problem Files, Preview and File information display (Keyfile, log, message, summary, memo and any text based file) and links under Pre-Processor, Simulator and Post-Processor categories as shown in Fig. 4.1.1. GUI Main is very intuitive, and user can use Layout options to customize the GUI Main display.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image001.jpg' | relative_url }})

DEFORM GUI Main

###    
Pre-Processor

A pre-processor for creating, assembling or modifying the data required to analyse the simulation and for generating the required database file. The DEFORM pre-processor uses a graphical user interface to assemble the data required to run the simulation. Input data includes Object description, Material Data, Inter-objects relations, simulation controls, Inter material Data etc. to setup a problem. Under Pre-Processor, links are provided which can be used to edit the existing setup or create a new setup.

Pre-Processor displays links based on the selection of the File under “Problem Files” tab. For Example, 

  * If a “.moproj” file consisting of Extrusion is selected then link to Extrusion Wizard is displayed

  * If a DB file is selected, then links to Integrated Manufacturing Process and NG Pre are displayed

  * If a keyfile is selected, then links to NG Pre and Text editor are displayed

  * If an empty folder is selected, then links are displayed for creating a New Problem and New Folder.

###    
Simulator

A simulation engine for performing the numerical calculations required to analyse the process and writing the results to the database file. The simulation engine reads the database file, performs the actual solution calculation, and appends the appropriate solution data to the database file. The simulation engine also works seamlessly with the Automatic Mesh Generation (AMG) system to generate a new FEM mesh on the workpiece whenever necessary. While the simulation engine is running, it writes status information, including any error messages, to the message (.MSG) and log (.LOG) files. 

Under simulator we have,  
**Run** : This option is used to start the simulation immediately.   
**Run options** : This option is used to define simulation environment such as MPICH, Simulation server and its settings, message file saving, Initial run or continuing the previous run..etc. Refer for [simulator](/docs/en/simulator/23_deform_simulator/23_introduction_to_deform_simulator/) for more information  
**Add to Queue** : User can select the problem and click on this label to ass the problem to Queue on the selected Simulation Server  
Continue: This option is used to continue the problem that is stopped prematurely.  
**Process Monitor** : Process monitor is used to know the current status of various problems to submitted for simulation on this system or by this system, Refer for [simulator](/docs/en/simulator/23_deform_simulator/23_introduction_to_deform_simulator/) more information.  
**Simulation Graphics** : This option can be used to launch independent “DEFORM Viewer” to monitor the current problems that are simulating.

###   
Post-processor

A post-processor for reading the database file from the simulation engine and displaying the results graphically and for extracting numerical data. The postprocessor is used to view simulation data after the simulation has been run. The post-processor features a graphical user interface to view geometry, field data such as strain, temperature, and stress, and other simulation data such as die loads. The postprocessor can also be used to extract graphic or numerical data for use in other applications.

Under Post-Processor, user can find links to Next Gen Post-Processor, DEFORM Viewer and Material Suite. If the Problem folder consists of DOE/ Optimization study, then link to DOE Post-Processor is displayed.

## Problem directory

Problem Directory section has Explorer, Queued and Recent tabs as shown in Fig. 4.1.2.  
![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) **Browse** : Using Browse option user can mount the selected folder as problem folder under Explorer tab. Also, user can add multiple problem folder under Explorer tab.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image002.jpg' | relative_url }})

Explore Tab

###   
  
Explore Tab

Explore tab as shown in Fig. 4.1.2. shows the list of folders under the selected directory.   
**Mount Folder** : User can mount any folder as “Problem Folder”, to do so user can click on “Browse folder” button and in the “Browse” dialog turn on “Mount as problem folder” check box. The mounted folder can be unmount using RMB on mounted folder and selecting “Unmount problem folder” option (See Fig. 4.1.3.).

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image003.jpg' | relative_url }})

Right mouse button click menu for Mounted Problem folder

**Set as browse location** : User can select any folder and set it as browse location using RMB on folder and selecting “Set as browse location” option.  
**Show in Explorer** : User can select “Show in Explorer” from RMB on a folder to view the folder and its contents in windows explorer.  
**Copy** : User can use this option to copy the folder and paste it in any folder in explorer tab.   
**Duplicate** : User can use this option to from RMB on a folder to duplicate the folder, folder is duplicated with new name at the same location as that of the source directory.   
**Delete**![]({{ '/assets/icons/pre_icons/mo_delete_folder_icon.jpg' | relative_url }}) : User can delete the folder from the system using this option from RMB options on a folder.  
**Rename(F2)** : Folder name can be renamed using this option from RMB options or F2 key on a folder.  
**Database archive** : “Database Archive” dialog can be launched to archive projects in the selected folder, for more information on “Database Archive” please refer [Database Archive](../../integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_4_main_menu.htm#Database_Archive) in**** Chapter 6.4. Main Menu   
**Clean up Files** : This option from RMB options is used to clean up temporary files created by DEFORM during setting up a problem or simulation  
**Clean up running status** : If a simulation is stopped or killed by user and running status is remained then this RMB option can be used to clean up the running status.  
**Move Project** : We can move project folder from one directory to another directory by drag and drop as shown in Fig. 4.1.4.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image004.jpg' | relative_url }})

Moving project by drag and drop

###   
Queued Tab

Queued tab as shown in Fig. 4.1.5. shows the list of Jobs are added to queue to simulate from that system along with the status of queued jobs.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image005.jpg' | relative_url }})

Queued Tab

###   
Recent tab

Recent tab as shown in Fig. 4.1.6. shows the list of recently opened database directories.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image006.jpg' | relative_url }})

Recent Tab

## Problem Files Section

Problem files section has “Problem Files” and “All Files” tabs. “Problem Files” tab displays the files that can be used to link the DEFORM modules in the selected folder and “All Files” displays all the files and folders under selected folder.

###   
Problem Files tab

Problem Files tab as shown in Fig. 4.1.7. shows the .DB, .KEY and Project files.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image007.jpg' | relative_url }})

Problem Files Tab

### All Files tab

All Files tab as shown in Fig. 4.1.8. shows the all files and folders available inside the project folder. Under “All Files” tab user is provided with Filter option to filter files based on the file extension for easier viewing, see Fig. 4.1.9. .

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image008.jpg' | relative_url }})

All Files Tab

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image009.jpg' | relative_url }})

Filter files option under All File tab

###   
  
Right mouse button click menu for Problem Files

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image010.jpg' | relative_url }})

Right mouse button click menu for Problem Files

**Duplicate** : Using the Duplicate option we can make a duplicate copy of a file or folder with new name in the source folder.  
**Delete**![]({{ '/assets/icons/pre_icons/mo_delete_folder_icon.jpg' | relative_url }}) : User can delete the folder or file from the system using this option from RMB options on a folder.  
**Rename(F2)** : Folder or file name can be renamed using this option from RMB options or F2 key on a folder.  
**Edit with Edito****r** : This option is applicable only for keyfile. Using this option user can open the file in text editor to view the file content or edit.

## Menu Bar

Several options are provided under different menus in GUI Main to access project folders, navigated between folders and links to various modules. All menu options are made available using ![]({{ '/assets/icons/pre_icons/mo_menu_bar_icon.jpg' | relative_url }}) icon available in GUI Main, see Fig. 4.1.11.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image011.jpg' | relative_url }})

Menu popup

### File Menu

The below Fig. 4.1.12. shows the options under File menu in GUI Main.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image012.jpg' | relative_url }})

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image013.jpg' | relative_url }})

File menu Options

  
  
**New Problem![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) : **User can create a new problem by either selecting **![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }})** New Problem. New Problem creation option is available from file menu, tool bar, from links under Folder and RMB options on an empty folder.  
When user clicks on New problem, the New Problem window will appear as shown in Fig. 4.1.13.). 

**Create New** : User can use “Create New” to start new problem setup using one of the modules of DEFORM. New Problem dialog shows the lists of modules available in DEFORM when user selects “Create New” option, then user can select wizard like 2D3D Pre / Integrated Manufacturing Proc. or any Template and unit system for the new problem. User can specify the problem location on system in Location field and define problem name in Name field and click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}).

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image014.jpg' | relative_url }})

New problem - Create New category

**Import Template** : User can start new problem setup with saved User Defined Templates (see Fig. 4.1.14.). Location of the templates can be browsed and required template can be selected. User can specify the problem location on system in Location field and define problem name in Name field and click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}). New project will be opened along with the data from user defined template.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image015.jpg' | relative_url }})

New problem - Import Template category

**Import Example** : User can start new problem by copying the data from one of the Example keyfile to the Project folder (see Fig. 4.1.15.). If user check the Open Pre-processor check box and click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), then selected example will be copied to the project folder and will be opened in 2D/3D Pre-Processor.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image016.jpg' | relative_url }})

New problem - Import Example category

  
**New Folder** ![]({{ '/assets/icons/pre_icons/mo_new_folder_icon.jpg' | relative_url }}): Using this option user can create New Sub Folder in the selected folder.  
**Quit (Ctrl +Q)** ![]({{ '/assets/icons/pre_icons/mo_quit_icon.jpg' | relative_url }}): The quit option is used to exit from DEFORM GUI Main.

### Edit

The below Fig. 4.1.16. shows the Edit menu options in GUI.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image017.jpg' | relative_url }})

Edit menu option

**Copy![]({{ '/assets/icons/pre_icons/mo_copy_file_icon.jpg' | relative_url }})** : Using this option user can copy the selected project.  
**Paste![]({{ '/assets/icons/pre_icons/mo_paste_file_icon.jpg' | relative_url }})** : Using this option user can paste the copied project inside the selected Problem Folder.

###   
View Menu

The below Fig. 4.1.17. shows the View menu options in GUI.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image018.jpg' | relative_url }})

View menu option

  
  
**Tool bar:** User can control the display of the tool bars by checking and unchecking under Tool bar as shown in Fig. 4.1.18.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image019.jpg' | relative_url }})

Tool bar option

**Standard** : The user will be provided with some standard option (New problem, Browse folder, Back, Forward, ...etc) under the menu bar. The icons on tool bar are updated based on the folder selected and the project type within it.  
**Layout** : The user will be provided with Toggle buttons to control the display of various sections in GUI Main or change layouts as shown in Fig. 4.1.19. Various options in Layout tool bar are,

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image020.jpg' | relative_url }})

Layout options

**Toggle Folders![]({{ '/assets/icons/pre_icons/mo_toggle_folder_button.jpg' | relative_url }})** : This button is used to Show/Hide the Primary Directory in display.  
**Toggle Files** ![]({{ '/assets/icons/pre_icons/mo_toggle_file_icon.jpg' | relative_url }}): This button is used to Show/Hide the Files window to display.  
**Toggle Properties** ![]({{ '/assets/icons/pre_icons/mo_toggle_properties_icon.jpg' | relative_url }}) : This button is used to activate the Properties window to display.  
**Toggle Actions** ![]({{ '/assets/icons/pre_icons/mo_toggle_action_icon.jpg' | relative_url }}): This button is used to activate the Actions window to display.  
**No split** ![]({{ '/assets/icons/pre_icons/mo_no_split_icon.jpg' | relative_url }}): This button is used not to split the Preview and message tabs.  
**Left right split** ![]({{ '/assets/icons/pre_icons/mo_left_right_split_icon.jpg' | relative_url }}): This button is used to split the Preview and message tabs left and right.  
**Up down split** ![]({{ '/assets/icons/pre_icons/mo_up_down_icon.jpg' | relative_url }}): This button is used to split the Preview and message tabs up and down.  
**Layout Preferences** ![]({{ '/assets/icons/pre_icons/mo_layout_preferences_icon.jpg' | relative_url }}): This button is used to open the layout preferences window.

**Status Bar** : The user can hide and show status bar by unchecking and checking this option under view menu bar.  
**Home![]({{ '/assets/icons/pre_icons/mo_home_icon.jpg' | relative_url }})** : Using this option user can go to Home directory as indicated in Environment settings.  
**Back****(Ctrl +B)![]({{ '/assets/icons/pre_icons/mo_back_icon.jpg' | relative_url }})** : This option is used to navigate back to previously selected path under Explorer tab.  
**Forward (Ctrl +F)** ![]({{ '/assets/icons/pre_icons/mo_forward_icon.jpg' | relative_url }}): This option is used to navigate to problem path under Explorer tab before “Back” option is used.   
**Up (Ctrl +U)** ![]({{ '/assets/icons/pre_icons/mo_up_arrow_iocn.jpg' | relative_url }}): This option is used to navigate to one level above the current selected directory under Explorer tab.  
**Refresh (F5)** : This option is used to Refresh the GUI Main.   
**Scan Subdirectory** ![]({{ '/assets/icons/pre_icons/mo_scan_subdirectory_button.jpg' | relative_url }}): This option is used to display the image files of every problem under the current selected problem directory. User can open the respective problem folder by double click on the image file.

**Rescan problems** option is available when we right click on the image file zone which is used to again scan the respective problem directory and refresh the list of problems as shown in Fig. 4.1.20.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image021.jpg' | relative_url }})

Rescanning the problems

### Pre-Processor Menu

The below Fig. 4.1.21. shows the Pre-Processor menu options which are available at both menu bar and in the toggle actions window under Pre-Processor. The options displayed under “Pre-Processor” depends upon the selected folder and project type within it. For ex., if a forming express project is selected then user is provided with Forming express operation, Integrated Manufacturing Proc. and 2D/3D Pre options. 

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image022.jpg' | relative_url }})

Pre-Processor menu option

###   
Simulation Menu

The below Fig. 4.1.22. shows the simulation menu options which are available at both menu bar and in the toggle actions window under Simulator. Depending upon the selected project folder or empty folder simulator options will be updated.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image023.jpg' | relative_url }})

Simulator menu option

**Run** ![]({{ '/assets/icons/simulator_icons/mo_run_icon.jpg' | relative_url }}): This option is used to run the job   
**Run (options)** ![]({{ '/assets/icons/simulator_icons/run_option_icon.jpg' | relative_url }}): This option is used to open Run option popup for more detailed settings to simulate the selected project.  
**Add to Queue** ![]({{ '/assets/icons/simulator_icons/mo_add_to_queue_icon.jpg' | relative_url }}): It is used to add the selected jobs to queue for simulation.  
**Stop**![]({{ '/assets/icons/simulator_icons/mo_stop_icon.jpg' | relative_url }}) : This option is used to Stop the selected job that is simulating.  
**Continue** ![]({{ '/assets/icons/simulator_icons/mo_continue_icon.jpg' | relative_url }}): This option is used to continue the job that was stopped prematurely.  
**Process Monitor**![]({{ '/assets/icons/simulator_icons/mo_process_monitor_icon.jpg' | relative_url }}) : The process monitor displays the status of all simulations running on the CPU.  
**Simulation Graphics** ![]({{ '/assets/icons/simulator_icons/mo_simulation_graphics_icon.jpg' | relative_url }}): This option is used to monitor the simulating problem.

For more information about these options, please refer [Chapter 23. DEFORM Simulator](/docs/en/simulator/23_deform_simulator/23_introduction_to_deform_simulator/).

###   
Post Processor Menu

The below Fig. 4.1.23. shows the Post Processor menu options which are available at both menu bar and in the toggle actions window under Post Processor depending upon the selected project folder and the project within it. If the selected folder has DOE or Optimization project within it then DOE Post module will be made available.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image024.jpg' | relative_url }})

Post Processor menu option

  
**2D/3D post:** This option is used to open Next gen Post, for more information refer [Post-Poocessor](/docs/en/post_processor/24_introduction_to_post_processor/24_introduction_to_post_processor/).  
**DOE Post** : This option is used to open DOE Post, for more information refer [DOE Post processor](/docs/en/doe_and_optimization/54_doe_post_processor/54_1_doe_post_processor/).  
**DEFORM Viewer** : This option is used to open Deform Viewer, for more information refer DEFORM Viewer.  
**Material Suite:** This option is used to open Material Suite, for more information refer Material Suite.

###   
Tool Menu

The below Fig. 4.1.24. shows the options under Tools menu in GUI Main.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image025.jpg' | relative_url }})

Tool menu option

  
**Database Manager![]({{ '/assets/icons/pre_icons/mo_database_manager_icon.jpg' | relative_url }})**  
Database Manager helps the user to manage the size of the database. In DB manager we can perform Purge, Merge and Convert operation.

**Purge** : Purge can be used to reduce the size of the DB by removing irrelevant saved steps. To purge the database, user must select the required steps from the step list of the selected database![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Click on Purge tab![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Enter the location and name to save the purged database in “ To ” ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) and then click on “ Save Selected Steps ” as shown in Fig. 4.1.25.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image026.jpg' | relative_url }})

Purge Database window

**Merge** : Option used to merge the two databases into one database. For merging database, select .DB files to be merged in “Database 1” and “Database 2” field ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Enter the new location and name for the new DB file in “To” field ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) and then click on “Start Merging” as show in Fig. 4.1.26.

Note:  
For merging, the database should have same mesh number and step number should be continues.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image027.jpg' | relative_url }})

Merge Database window

**Convert** : This option is used to convert the older version database to newer version. To convert select the older version database ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Enter the new location and name for the new DB file in “To” field ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})and then click on “Start Converting” button in converting tab as shown in Fig. 4.1.27.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image028.jpg' | relative_url }})

Convert window

**Database Archive**  
This function is used to get a completed project down to a size to fit on archive media (like a DVD) for backup or distribution, See Fig. 4.1.28. This option is also available in from RMB menu of a folder. User can set “Destination” and “Options” and click on “Archive” to start archiving.  
In “Destination” tab user can enter the location on system in “Location” field and archive name in “Archive Name” field.

This option is used to Archive Project files, project databases and DOE/OPT databases by selecting respective checkboxes. 

**No Purge** : User can archive database without purging the database using this option.

**Save first/last steps** : User can archive database by purging database and retaining only first and last steps of the database.

**Save Operation start/end steps** : User can archive database by purging database and retaining only start and end step of the Operation.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image029.jpg' | relative_url }})

Database Archive

  
**Clean up Files![]({{ '/assets/icons/pre_icons/mo_clean_up_files_icon.jpg' | relative_url }})**

It is used to remove the temporary files in the problem directory which was created while running simulation.

**Clean up Running status![]({{ '/assets/icons/pre_icons/mo_clean_up_running_status_icon.jpg' | relative_url }})**  
It is used to remove the running status files in the problem directory if the running status file retained.

### Options

The user can adjust the DEFORM working environment using environment option. Here the user can make changes in display and graphical settings and can save the settings as for his convenience.(See Fig. 4.1.29.)

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image030.jpg' | relative_url }})

Options menu

**Environment** : The user can adjust the DEFORM working environment using environment option. Here the user can make changes in display and graphical settings and can save the settings as for his convenience. Setting will update from next session onwards.  
****

  * Region:

The user can select the preferred language under Language option and set to English or SI units under Unit option as a Default unit system for a new problem. The user can select the standards for materials under Material Library to be used as a default for importing materials in the problem. (See Fig. 4.1.30.).

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image024.jpg' | relative_url }})

Region options under Environment Settings window

  * User Type:

User Type option under Environment Settings window appears as shown in Fig. 4.1.31. Depending on the user type the default conditions and pop-up windows are activated. 

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image025.jpg' | relative_url }})

User type options under Environment Settings window

  * **Novice** : If the user is new to DEFORM then this option is preferred.
  * I**ntermediate** : This option is for an user who is bit familiar to DEFORM environment. For example, if we select quit option in the GUI, a pop up appears with a message " Do you want to quit", the user can click "Yes" to exit from GUI. 
  * **Advanced:** This option is for an user who is well aware of DEFORM, he can eliminate few pop-ups. For example, if we select quit option in the GUI, Deform will close without a popup warning message.

  * User Directory:

User Directory option under Environment Settings window appears as shown in Fig. 4.1.32. The user can browse for the required location to set it as the working directory under Problem, this directory will be used as a default location to store the generated DB's, key files and working files related to DEFORM. The path under Library root will be used as a default path to store the user data generated in DEFORM.The path under Geometry import will be used as the default path to access the geometries, which can be a problem directory itself. If it is a different location it has to be mentioned under geometry import path separately for 2D and 3D. The temporary files generated while running deform are in the specified path under Temporary Directory.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image026.jpg' | relative_url }})

User directory options under Environment Settings window

  * System Directory:

System Directory option under Environment Settings window appears as shown in Fig. 4.1.33. Only Advanced user type selection (as mentioned in user type section) activates this tab access to user. Using this option user can change the DEFORM material, press and equipment library path under respective fields, this directory will be used as a default location for the material, press and equipment library in DEFORM. By default these are pointed to the DEFORM library available in the installation location, user can changed to user library paths, this path will be called when import material, movement or insert geometries are selected from DEFORM GUI.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image048.jpg' | relative_url }})

System directories options under Environment settings window

  * Simulation Option: 

In DEFORM - V12, default settings to run a Simulation can be set using options under Simulation Option tab in Environment settings. Simulation Options window appears as shown in Fig. 4.1.34. By turning on the Keep Message Files DEFORM saves simulation messages without overwriting even after remesh. User can turn on Parallel meshing and set it as default for all simulations, user can apply the parallel meshing either to Solid or to both Solid+Surface. User can turn on No automatic remeshing as default setting for simulations so that simulation can skip the automatic remesh due to non-convergence. The default settings can be changed for each simulation from Run options dialog.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image027.jpg' | relative_url }})

Simulation Options

  * Multiple Processor:

Multiple processor option under Environment Settings window appears as shown in Fig. 4.1.35. The user can activate the table just by checking next to the Use multiple processor option as shown in the Fig. 4.1.35. The user can specify the computers used to solve the problem as well as the number of processors used on each computer. It is very important that the user enters the correct network name of the computer for the simulation to run. It also provides information about the memory shared between the processors.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image028.jpg' | relative_url }})

Multiple Processor

  * Process:

Process option under Environment Settings window appears as shown in Fig. 4.1.36. User can set the default simulation modes like Deformation, Heat transfer Transformation..etc and control the auto assignment of primary die.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image029.jpg' | relative_url }})

Process options under Environment Settings window

  * Output Control:

The user can set default output type as either Elemental or Elemental+Node for Strain, Stress and Damage variables as shown in Fig. 4.1.37.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image030.jpg' | relative_url }})

Output Controls options under Environment Settings window

  * Email

Email option under Environment Settings window appears as shown in Fig. 4.1.38. This function allows DEFORM to send an email notification at the start of the simulation and with last 25 lines from the Message file and Log file at end of the simulation. Emails are sent via SMTP using StartTLS (or no security). For more information refer [23.7. Email notification of the simulation](/docs/en/simulator/23_deform_simulator/23_7_email_the_results/).

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image031.jpg' | relative_url }})

Email options under Environment Settings window

  * Memory:

The user can set the required memory size depending upon the usage as shown in Fig. 4.1.39. For most part, the default values of these settings can cover wide range of model requirements. For very large size models (with respect to total number of elements and nodes) depending up on the operating system these settings may need to be increased to handle some run time procedures such as remeshing.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image032.jpg' | relative_url }})

Memory options under Environment Settings window

  * Icon/Font:

The user can change the icon and font size depending on the requirement as shown in the [Fig. 4.1.40.](4_1_gui_main_layout.htm#Fig_4_1_40_Icon/Font_options_under_Environment_Settings_window)

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image033.jpg' | relative_url }})

Icon/Font options under Environment Settings window

  * Job Protection:

The user can protect Running job from being terminated by setting password as shown in Fig. 4.1.41.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image034.jpg' | relative_url }})

Job protection options under Environment Settings window

  
In Linux system select the enable protection radio button then enter the password in the password field and click on save button to save the password (see Fig. 4.1.41.).

In windows system select the continue button then use password in setup job password popup window and click as shown in Fig. 4.1.42.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image035.jpg' | relative_url }})

Running Job protection in windows password set up window

  * Report: 

From V12 Auto report generation options are provided under Report option in Environment Settings window, the auto report generation settings appears as shown in Fig. 4.1.43. User can set the default Auto Report option as per the requirement for Normal run, DOE runs and OPT runs by turning on the check box. Depending on the settings DEFORM generates the report automatically at the end of simulation.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image036.jpg' | relative_url }})

Report options under Environment Settings window

### Layout

User can change the GUI layout using Layout scheme option.(See Fig. 4.1.44.)

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image031.jpg' | relative_url }})

Layout Preference page

**Classic**

****This layout is like DEFORM v11.X version GUI Main layout (See Fig. 4.1.1.).

  
**Express**

****Express layout is as shown in Fig. 4.1.45. This layout is a simplified layout. User can open Multiple tabs in Express layout to monitor different projects using "Browse in New tab" option from RMB options on a folder as shown in Fig. 4.1.46. New Tab window added as shown in Fig. 4.1.47.

**Properties** : This window shows the data of the problem folder which is selected in the explorer tab. We can also create the MEMO file in the project folder from this properties window as shown in the Fig. 4.1.48.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image032.jpg' | relative_url }})

Express Layout

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image033.jpg' | relative_url }})

Selecting Browse in New Tab in Right click menu

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image034.jpg' | relative_url }})

Multiple tab opened in Express layout GUI Main

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image035.jpg' | relative_url }})

Properties Window

**Custom Layout**

****Using the Custom layout option user can create own GUI Main layout. Options available for customizing the layout are shown in Fig. 4.1.49. After customizing the layout user can click on Apply for GUI layout to apply custom layout. Customization options are,

**Folders** : Under folders tab user can select or hide Folder properties and folder panel display if only a single problem folder is browsed as show in Fig. 4.1.49.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image036.jpg' | relative_url }})

Custom layout - Folders page

**Files** : Under Files tab user can select or hide the files list and we can also choose file filter type as shown in Fig. 4.1.50.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image037.jpg' | relative_url }})

Custom layout - Files page

**Main View** : User can customize the display of graphics, log and message files. (See Fig. 4.1.51.)

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image038.jpg' | relative_url }})

Custom layout - Main View page

**Actions** : Under Actions tab user can choose to show the action links panels only or action toolbar only or both. (See Fig. 4.1.52.)

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image039.jpg' | relative_url }})

Custom layout - Action page

  
**Tabs** : User can customize the tabbed display using options available in “Tabs”.

**Enable multiple tabbed windows** : User can access different folders in different tab to monitor each project independently

**Restore the tabs on program start** : Restores the multiple tabs on the start of the GUI Main program.

**Show tabs on bottom** : The tabs will be shown at the bottom. (See Fig. 4.1.53.)

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image040.jpg' | relative_url }})

Custom layout - Tabs page

###   
Help

The below Fig. 4.1.54. shows the Help menu options in GUI.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image041.jpg' | relative_url }})

Help menu option

  
**DEFORM Manual**

****Launches DEFORM Manual displays the DEFORM manual through web browser.

**About SFTC**

It displays information about SFTC in a window.

**About**

It displays information about DEFORM-2D/3D(GUI) in a window.  
  
**About FEM Engine:**

It displays information about FEM engine in a window.  
  
**License Information:**

It displays the information about license file, license expiry date and Machine ID in a window. 

## Preview

Under Preview tab user can observe the snapshot of the display from the last access of the problem. User is also provided with a link to open simulation graphics in Preview tab while simulation is running (See Fig. 4.1.55.). Depending on the project type and R status of the database “Preview” tab keeps on updating. If the project type is DOE or Optimization, then DOE cases and snapshot from DOE post is shown. If DOE or Optimization simulation then the preview tab is updated with DOE variable table as shown in Fig. 4.1.56. for each run completed, user can click on the run to view respective run folder in Problem folder.

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image042.jpg' | relative_url }})

Preview tab

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image043.jpg' | relative_url }})

DOE Study Preview tab

## Message

Under Message tab user can observe the Messages of FEM calculation of the problem. Message file is continuously updated as the simulation runs with information about FEM calculations and relevant information depending on the problem type. (See Fig. 4.1.57.)

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image044.jpg' | relative_url }})

Message tab

## Log

Under Log tab user can observe the log file information. Log file displays information about start of the problem, time taken for simulation, remeshing information and multiple operation status. If the problem type is of DOE or Optimization, then DOE Log file is displayed which will display the information about the spawning of databases, DOE running and extraction status.(See Fig. 4.1.58.)

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image045.jpg' | relative_url }})

Log tab

## Summary

Under Summary tab user can observe the Problem summary. This file will be created when we open the Database in NG post. (See Fig. 4.1.59.)

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image046.jpg' | relative_url }})

Summary tab

## Memo

Under Memo tab user can add note. (See Fig. 4.1.60.)

![]({{ '/assets/images/starting_up_deform/4_gui_main/4_1_gui_main_layout/image047.jpg' | relative_url }})

Memo tab

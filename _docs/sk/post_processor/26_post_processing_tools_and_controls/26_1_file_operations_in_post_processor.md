---
lang: sk
title: "26.1. File operations in Post-processor"
---

# 26.1. File operations in Post-processor

26.1.1. Working with DB in PIP mode

The below Fig. 26.1.1. shows the **File menu** options,

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/image001.jpg' | relative_url }})

File menu option in Post - Processor

**New**![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) (Ctrl +N) : It loads database file, This can also be accessed from File Tools menu

**Open**..![]({{ '/assets/icons/pre_icons/mo_open_icon.jpg' | relative_url }}) (Ctrl +O): It loads Database file and saved DEFORM session file, This can also be accessed from File Tools menu

**Save**![]({{ '/assets/icons/pre_icons/mo_save_icon.jpg' | relative_url }}) (Ctrl +S): It saves the session file, This can also be accessed from File Tools menu

**Save as..** : It saves the session file in the selected directory with user specified name.

**Import DB (PIP)**![]({{ '/assets/icons/post_icons/mo_import_database_in_pip_icon.jpg' | relative_url }}) (Ctrl+Shift+D) : Picture in picture feature is helpful to compare two or more databases or within same database at different steps across different state variables. Using this option user can import more than one DB in the same session using (Import database in PIP) icon from header tool bar.

For more details refer 

**Export** : It saves the problem setup in .key file format. 

**Folder option** : It open the working directory of the database in windows explorer.

**Image Setup**(Ctrl + M)**:** It is used to setup the current display window or the work space to the required pixel size and capture images to required location in required format. This can also be accessed from File Tools menu.(See Fig. 26.1.2.)

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/image002.jpg' | relative_url }})

Image Setup popup

**Capture image** ![]({{ '/assets/icons/pre_icons/mo_capture_screen_image_to_file_icon.jpg' | relative_url }}) (Ctrl + I): It writes the current screen image to a file using the specified image format.

**Capture Image to clipboard**![]({{ '/assets/icons/pre_icons/mo_capture_screen_to_clip_board_icon.jpg' | relative_url }}) (Ctrl + Shift+ I): It writes the current screen image to the clipboard. (On PC vista operating system, for some display drivers, this feature works only in 'Windows Vista Basic' mode in the system personalization settings).

**Recent projects** : This option is helpful to open the last ten previously opened Databases.

**Close**(Ctrl+W) : It closes the current working project but does not quit from the pre processor.

**Quit**(Ctrl+Q) : It is used to exit from Post Processor.

For **Viewport menu** and **Windows****menu** options refer chapter [26.2. Viewports and Windows Menu](/docs/sk/post_processor/26_post_processing_tools_and_controls/26_2_handeling_viewports_and_windows_iin_post_processor/).

For **Display****menu** and **Mouse****menu** options refer chapter [26.3. Object Display Controls](/docs/sk/post_processor/26_post_processing_tools_and_controls/26_3_object_display_controls/).

For **Steps****menu** options refer chapter[ 26.4. Simulation Step Display Controls](/docs/sk/post_processor/26_post_processing_tools_and_controls/26_4_simulation_step_display_controls/)

For **Options****menu** options refer chapter [26.5. PostProcessing Options Menu](/docs/sk/post_processor/26_post_processing_tools_and_controls/26_5_post_processing_options/)

For **Tools Menu** options refer chapter [26.6. Post Processing tools](/docs/sk/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_post_processing_tools/)

For **Sections****menu** and **Report****menu** options refer [27\. Introduction to Report Generation](/docs/sk/post_processor/27_introduction_to_report_generation/27_introduction_to_report_generation/)

For **Dock****Widgets****menu** options refer Chapter [25\. Post Processor Layout](/docs/sk/post_processor/25_post_processor_layout/25_post_processor_layout/) section [25.5. Dock Widget menu](../25_post_processor_layout/25_post_processor_layout.htm#25_5_Dock_Widget_menu)

## Working with DB in PIP mode

Picture in picture (PIP) feature is helpful to compare two or more data base results or results of same data base at different steps across different state variables. Using this option user can import more than one DB in the same session by ![]({{ '/assets/icons/post_icons/mo_import_database_in_pip_icon.jpg' | relative_url }}) (Import database in PIP) icon from header tool bar as shown in Fig. 26.1.3.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_1_file_operations_in_post_processor/image003.jpg' | relative_url }})

Import DB in PIP option in tool bar

The imported DB opens in graphics window as a small picture as shown in Fig. 26.1.4., user can maximize, minimize, drag and move this PIP window using control points.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_1_file_operations_in_post_processor/image004.jpg' | relative_url }})

PIP on graphics window

Selecting the PIP window will display border around the image with dots, keeping the cursor within this border gives pan icon, then user can move the PIP window by drag and drop as shown in Fig. 26.1.6. and PIP window can be maximized or minimized by dragging border dots when it shows arrow icon as shown in Fig. 26.1.5.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_1_file_operations_in_post_processor/image005.jpg' | relative_url }})

Maximized PIP window with maximize and minimize drag option

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_1_file_operations_in_post_processor/image006.jpg' | relative_url }})

Moved PIP with pan option

PIP window can also be maximized or minimized by keeping the cursor within the border and scrolling the mouse scroll button.

After selecting the PIP window user can play the steps, plot state variable and graphs and compare the results with the main graphics window DB. (See Fig. 26.1.7. and Fig. 26.1.8.)

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_1_file_operations_in_post_processor/image007.jpg' | relative_url }})

State variable contour plot in both main and PIP DB at different steps For 3D

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_1_file_operations_in_post_processor/image008.jpg' | relative_url }})

State variable contour plot in both main and PIP DB at different steps For 2D

**Order** :

User can arrange the PIP DB’s for better display using the Order option available from RMB options of PIP. The Order menu has options to move back the selected PIP DB or Bring to Front etc. Options available from Order menu are shown in below Fig. 26.1.9.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_1_file_operations_in_post_processor/image009.jpg' | relative_url }})

Order option for PIP DB

**Related Topics:**

[25\. Post Processor Layout](/docs/sk/post_processor/25_post_processor_layout/25_post_processor_layout/)

[26.2. Viewports and Windows Menu](/docs/sk/post_processor/26_post_processing_tools_and_controls/26_2_handeling_viewports_and_windows_iin_post_processor/)

[26.3. Object Display Controls](/docs/sk/post_processor/26_post_processing_tools_and_controls/26_3_object_display_controls/)

[26.4. Simulation Step Display Controls](/docs/sk/post_processor/26_post_processing_tools_and_controls/26_4_simulation_step_display_controls/)

[26.5. PostProcessing Options Menu](/docs/sk/post_processor/26_post_processing_tools_and_controls/26_5_post_processing_options/)

[26.6. Post Processing tools](/docs/sk/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_post_processing_tools/)

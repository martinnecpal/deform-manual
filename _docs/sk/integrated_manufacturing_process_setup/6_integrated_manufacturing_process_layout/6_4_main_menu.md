---
lang: sk
title: "6.4. Main Menu"
---

# 6.4. Main Menu

6.4.1. Pre Mode menu bar options

  * File Menu

  * Viewport Menu

  * Display menu

  * Mouse Menu

  * Tool Menu

  * Options Menu

  * Project Menu

  * Help Menu

6.4.2. Simulation Mode menu bar options

6.4.3. Post Mode menu bar options

6.4.4. Tool bar options

  * Switch to guided mode

  * Switch to expert mode

  * Boolean

  * Data Interpolation

  * Slicing

  * Stop current task

  
The Menu and Tool bar options provides project browsing view manipulation and other utility functions for the object window. Features include add, open and save project, zoom, magnify and pan viewport, measurement utilities, Viewport controls and Rendering type utilities as shown in Fig. 6.4.1.

  
These are grouped under multiple menu's, those are File, Viewport, Display, Mouse, Tool, Project, Simulation and Help. These menu options will available or activate based on the MO modes, like in Pre mode Simulation menu is not available as it is not required and will be available only in Simulation Mode.

## Pre Mode menu bar options

In Pre Mode File, Viewport, Display, Mouse, Tool, Project and Help menu options are available.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image001.jpg' | relative_url }})

(a)

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image002.jpg' | relative_url }})

(b)

MO Pre mode Menu and Tool bar; (a) For 2D (b) For 3D

  
These menu options are explained in below sections,

**File Menu**

Fig. 6.4.2. shows the File menu options using these options or icons in tool bar user can open new project, open the old projects, save the project file, import the setup Keyword/DB file for project setup, export the setup keyword file, open the working directory or recently worked projects, close the project and quit the MO GUI.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image003.jpg' | relative_url }})

File Menu options

  * **New Project (Ctrl+N)** ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }})

New project can be added using this option. This pops up the New Project window (See Fig. 6.4.3.) where Project Name, Title, Location, First operation and Unit system can be selected. By default New Project will give the selected directory as working directory.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image004.jpg' | relative_url }})

MO New Project window

  * **Open Project (Ctrl+O)** ![]({{ '/assets/icons/pre_icons/mo_open_icon.jpg' | relative_url }}) : Previous MO projects can be opened back in MO using this option.

  * **Save (Ctrl+S)** ![]({{ '/assets/icons/pre_icons/mo_save_icon.jpg' | relative_url }}) : Save the MO project file in “moproj” format. This project file is essential to open the MO project. So before closing the MO session it is preferred to save and close or quit the MO project. While closing the Project a File close popup ask whether to save the MO project before closing.

  * **Import (Ctrl+D)** ![]({{ '/assets/icons/pre_icons/mo_import_icon.jpg' | relative_url }}) : Problem setup Keyword or DB file can be imported after adding the operation into the operation editor using this option. In some special operations like Cogging previous versions .MDB files can also be imported to retrieve the old versions data.

  * **Import Keyword File (Ctrl + K) :** User can import a keyword file for the selected operation using Import Key word file option from File menu or using ‘Ctrl + K’ buttons on keyboard

  * **Import User Template :** Saved User MO Template (.motmpl) which was saved using Export User template or Operation Editor Save as Template RMB options can be loaded using Import User Template.

  * **Export :** The problem setup data can be exported to the user readable Keyword file format using this option.

  * **Export User Template :** If user is setting up similar processes and most of the data is identical then user can save the setup including the sequence of operations, process data and object data into a template which can be imported later and modified to suit the new setup with less time involving in setting up the problem. Export User Template option is available under File menu in MO gui and from right click options (right click between two horizontal tiles or between two empty vertical tiles) in Operation Editor. Object data saving into template is optional hence, selected objects data can be saved into template using checkboxes available from the Export user template window (See Fig. 6.4.4.).

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image005.jpg' | relative_url }})

Export user Template window

  * **Folder options :** Using Folder option Open working folder user can open the working directory in windows explorer. (See  Fig. 6.4.5.)

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image006.jpg' | relative_url }})

Folder Open working folder option

  * **Database Archive :** This function is used to get a completed project down to a size to fit on archive media (like a DVD) for backup or distribution.(See Fig. 6.4.6.)

This option is used to Archive Project files, project databases and DOE/OPT databases with No Purge or Save first/last steps or Save Operation start/end steps by selecting respective radio buttons into selected Destination.

This option is also available in Integrated GUI from RMB menu of a folder. 

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image007.jpg' | relative_url }})

Archive window

  * **Image setup (Ctrl+M) :** It is used to setup the current display window or the work space to the required pixel size and capture images to required location in required format as shown in Fig. 6.4.7.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image008.jpg' | relative_url }})

Image setup settings window

  * **Capture image (Ctrl+I)** ![]({{ '/assets/icons/pre_icons/mo_capture_screen_image_to_file_icon.jpg' | relative_url }}) : Writes the current screen image to a file using the specified image format.

  * **Capture Image to clipboard (Ctrl+Shift+I)** ![]({{ '/assets/icons/pre_icons/mo_capture_screen_to_clip_board_icon.jpg' | relative_url }}) : Writes the current screen image to the clipboard.

  * **Recent Projects :** This option is helpful to open the last ten previously worked MO projects.

  * **Close (Ctrl+W) :** MO currently opened project can be closed using this option. After closing the current MO project user can add and work on new project.

  * **Quit (Ctrl+Q)** ![]({{ '/assets/icons/pre_icons/mo_quit_icon.jpg' | relative_url }}) : MO GUI can be closed using this option, before quitting ask whether to save or not to save the changes done to the current project.

**Viewport Menu**

Fig. 6.4.8. shows the Viewport menu options using these options or icons in tool bar user can refresh or fit the view, switch to Iso or any directional view, set the upward axis, save and load the viewports and viewport lighting settings can be varied.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image009.jpg' | relative_url }})

Viewport Menu options

  * **Refresh (F5)** ![]({{ '/assets/icons/pre_icons/mo_refresh_icon.jpg' | relative_url }}) : The refresh icon redraws the screen, removing any measurement marks, and updating any changes made to the color pallet.

  * **Fit View (F3) :** Fits all displayed objects or graphs inside the current viewport.

  * **View back (F4) :** Resets objects to the previously viewed display position.

  * **Iso view** ![]({{ '/assets/icons/pre_icons/mo_iso_view_icon.jpg' | relative_url }}) : This will show the isometric view of the current viewport. This option is not available for 2D systems. This options are not available in 2D mode, as this are not applicable for 2D mode.

  * **Screen upward :****[3D]:** This option shows the isometric view in 3D, such that the selected axis will be pointing in the upward direction. For example, if the user select positive Z-axis from the screen upward option as shown in Fig. 6.4.9. and then select isometric view option, Z-axis will be pointing upwards in the isometric view. This is not applicable for 2D mode.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image010.jpg' | relative_url }})

Screen upward viewport menu options

  * **View point**![]({{ '/assets/icons/pre_icons/mo_plus_x_view_icon.jpg' | relative_url }}) ,![]({{ '/assets/icons/pre_icons/mo_minus_x_view_icon.jpg' | relative_url }}), ![]({{ '/assets/icons/pre_icons/mo_plus_y_view_icon.jpg' | relative_url }}),![]({{ '/assets/icons/pre_icons/mo_minus_y_view_icon.jpg' | relative_url }}) , ![]({{ '/assets/icons/pre_icons/mo_plus_z_icon.jpg' | relative_url }}) , ![]({{ '/assets/icons/pre_icons/mo_minus_z_icon.jpg' | relative_url }}) : **[3D]:** This option allows the user to show the object in the selected direction. For example if we select positive X- direction as a viewpoint from the Fig. 6.4.10., the Deform will show the object from the positive X-direction. These options are not available in 2D mode, as these are not applicable for 2D mode.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image011.jpg' | relative_url }})

Different view selection options

  * **Load and Save :** The user can move or change the views of the geometries by using display tools such as pan, dynamic zoom and box zoom in the display window. These views can be saved using save option provided under viewport tab as shown in Fig. 6.4.11.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image013.jpg' | relative_url }})

Save view port Menu options

If the view is saved as a local viewport, this view gets saved for the current working project only and can be viewed using load option as shown in Fig. 6.4.12. If the view is saved as a global viewport the set views becomes the default views for any project, for global viewports to get activated for the projects, the user has to exit from current project. The user can copy global viewports as a local viewports under load option and local viewports to global viewports under save option.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image012.jpg' | relative_url }})

Load view port Menu options

  * **Lighting :** This allows the user to change the brightness and color of the graphics window lighting, can also add more light switches and control its positions as shown in Fig. 6.4.13. , Fig. 6.4.14. and Fig. 6.4.15.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image014.jpg' | relative_url }})

Lighting General properties window

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image015.jpg' | relative_url }})

Lighting Settings properties window

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image016.jpg' | relative_url }})

Light Advanced Properties window

For More details, please refer Chapter[ 8\. Pre-Processor Layout](/docs/sk/pre_processor/8_pre_processor_layout/8_pre-processor_layout/) section [Set Lighting Property](../../pre_processor/8_pre_processor_layout/8_pre-processor_layout.htm#Set_Lighting_Property).

**Display menu**

Fig. 6.4.16. shows the display menu options using these options or icons in the tool bar user can select the different objects display rendering types like shading, wireframe, shading and wireframe, feature line (surface patch) and adding feature line to any other rendering types. 

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image017.jpg' | relative_url }})

Display Menu options

  * **Shading (F6)** ![]({{ '/assets/icons/pre_icons/mo_shading_mode_icon.jpg' | relative_url }}) : Smoothly shades the objects within viewport.

  * **Wireframe (F7)** ![]({{ '/assets/icons/pre_icons/mo_wirefrane_mode_icon.jpg' | relative_url }}) : Displays mesh of the object within viewport.

  * **Shading and Wireframe (F8)** ![]({{ '/assets/icons/pre_icons/mo_shade_wireframe_icon.jpg' | relative_url }}) : Smoothly shades and display mesh of objects within viewport.

  * **Feature line or Surface patch** ![]({{ '/assets/icons/pre_icons/mo_feature_line_mode_icon.jpg' | relative_url }}) : Displays the surface edges of the object. For 3D mode refer feature angle to vary the surface patches display.

  * **Add feature line** ![]({{ '/assets/icons/pre_icons/mo_add_feature_line_icon.jpg' | relative_url }}) : This feature will combine surface edges with other display modes options. For 3D mode refer feature angle to vary the surface patches display.

**Mouse Menu**

Fig. 6.4.17. shows the Mouse menu options using these options or icons in the tool bar user can select different mouse modes to measure the objects linear distance and change or move the objects view in graphics window like panning, rotate (only for 3D), zoom and magnify.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image018.jpg' | relative_url }})

Mouse menu options

  * Measurement ![]({{ '/assets/icons/pre_icons/mo_measure_tool_icon.jpg' | relative_url }}) : This tool allows the user to measure any distance between two points by clicking consecutively on both points. The measurement can be plot in either X or Y or XY direction, in 3D Z direction will come into picture, using the available CAD style option which displays the measured values in the selected direction. To access the CAD style option user need to right mouse click in the display window when user is in the measurement mode (See Fig. 6.4.18.). The measurement marks are not erased until the viewport is refreshed and as such are also convenient for marking arbitrary reference points on the screen, which will maintain their location through view changes.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image019.jpg' | relative_url }})![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image020.jpg' | relative_url }})  
(a) (b) 

Right mouse button measurement style options; (a) For 3D (b) For 2D

  * Select : The select button is a general pointing utility. It performs several functions which vary with context. It can be used to select a node or an element, to select BCC, stopping controls points on objects and many similar functions. From Right mouse click option menu in graphics window user can change the selected nodes display to point or polygon as shown in Fig. 6.4.19.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image021.jpg' | relative_url }})

Selected node display RMB option on graphics window

  * **Pan (Shift+LMB)** ![]({{ '/assets/icons/pre_icons/mo_pan_icon.jpg' | relative_url }}) : Pan adjusts the region filling the active viewport without changing the size of the displayed object.

  * **Rotate (Ctrl+LMB)**![]({{ '/assets/icons/pre_icons/mo_rotate_icon.jpg' | relative_url }}) : This will allow the mouse pointer to rotate the geometries in the required direction. This can also done by holding the Ctrl key and clicking the left mouse button in the active viewport and rolling the mouse backward or forward to rotate the objects.

  * **Rotate X** ![]({{ '/assets/icons/pre_icons/mo_rotate_x_icon.jpg' | relative_url }}) : This will allow the mouse pointer to rotate the object along X-direction.

  * **Rotate Y**![]({{ '/assets/icons/pre_icons/mo_rotate_y_icon.jpg' | relative_url }}) : This will allow the mouse pointer to rotate the object along Y-direction.

  * **Rotate Z** ![]({{ '/assets/icons/pre_icons/mo_rotate_z_icon.jpg' | relative_url }}) : This will allow the mouse pointer to rotate the object along Z-direction. This option is not available for 2D systems. Even though the user can see this icon while 2D problem setup, if user clicks on it, it will give a notice "This feature is not available in 2D view".

  * **Dynamic zoom (Alt+LMB)** ![]({{ '/assets/icons/pre_icons/mo_zoom_icon.jpg' | relative_url }}) : The dynamic zoom dynamically changes the size of the region of the object which fills the active view port. The view size can be changed by holding Alt key and clicking left mouse button in the active view port and rolling the mouse backward or forward to increase or decrease the size of the object in the display window.

  * **Box Zoom (Ctrl+Alt+LMB)**![]({{ '/assets/icons/pre_icons/mo_box_zoom_icon.jpg' | relative_url }}) : The Box zoom or magnify function allows close up inspection of a small region of the currently display object or graph. The zoom region is selected by holding Ctrl + Alt key and clicking the left mouse button, while dragging the mouse to enclose the selected region with the displayed box. When the mouse button is released the selected region will fill the display window.

**Tool Menu**

Fig. 6.4.20. shows the tool menu options, using these options or icons in the tool bar user can access the tools like object nodes and elements data window and Image capturing tools and its settings.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image022.jpg' | relative_url }})

Tool menu options

  * **Object Nodes** ![]({{ '/assets/icons/pre_icons/mo_nodal_data_icon.jpg' | relative_url }}) : The object node data window displays all available information about object nodes. All information can be modified and many of the variables can be plotted. This option will be activated only when object property windows like object main, geometry and mesh windows are selected. For more information please refer to [section 17.1. Node Datae.](/docs/sk/pre_processor/17_object_data_initialization/17_1_node_data_window/)

  * **Object Elements** ![]({{ '/assets/icons/pre_icons/mo_elemental_data_icon.jpg' | relative_url }}) : The element data window displays all available information about object elements. All information can be modified and many of the variables can be plotted. This option will be activated only when object property windows like object main, geometry and mesh windows are selected. For more information please refer to section [17.2 .Element Data.](/docs/sk/pre_processor/17_object_data_initialization/17_2_element_data_window/)

**Options Menu**

Fig. 6.4.21. shows the Options menu options, using these options user can set the DEFORM working environment different settings.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image023.jpg' | relative_url }})

Options menu options

  1. **Environment:** The user can adjust the DEFORM working environment using environment option. Here the user can make changes in display and graphical settings and can save the settings as for his convenience. Setting will update from next session onwards.

  * Region:

The user can select the preferred language under Language option and set to English or SI units under Unit option as a Default unit system for a new problem. The user can select the standards for materials under Material Library to be used as a default for importing materials in the problem. (See  Fig. 6.4.22.).

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image024.jpg' | relative_url }})

Region options under Environment Settings window

  * User Type:

User Type option under Environment Settings window appears as shown in Fig. 6.4.23. Depending on the user type the default conditions and pop-up windows are activated. 

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image025.jpg' | relative_url }})

User type options under Environment Settings window

  * **Novice** : If the user is new to DEFORM then this option is preferred.
  * **I******n** termediate**: This option is for an user who is bit familiar to DEFORM environment. For example, if we select quit option in the GUI, a pop up appears with a message " Do you want to quit", the user can click "Yes" to exit from GUI. 
  * **Advanced:** This option is for an user who is well aware of DEFORM, he can eliminate few pop-ups. For example, if we select quit option in the GUI, Deform will close without a popup warning message.

  * User Directory:

User Directory option under Environment Settings window appears as shown in Fig. 6.4.24. The user can browse for the required location to set it as the working directory under Problem, this directory will be used as a default location to store the generated DB's, key files and working files related to DEFORM. The path under Library root will be used as a default path to store the user data generated in DEFORM.The path under Geometry import will be used as the default path to access the geometries, which can be a problem directory itself. If it is a different location it has to be mentioned under geometry import path separately for 2D and 3D. The temporary files generated while running deform are in the specified path under Temporary Directory.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image026.jpg' | relative_url }})

User directory options under Environment Settings window

  * System Directory:

System Directory option under Environment Settings window appears as shown in Fig. 6.4.25. Only Advanced user type selection (as mentioned in user type section) activates this tab access to user. Using this option user can change the DEFORM material, press and equipment library path under respective fields, this directory will be used as a default location for the material, press and equipment library in DEFORM. By default these are pointed to the DEFORM library available in the installation location, user can changed to user library paths, this path will be called when import material, movement or insert geometries are selected from DEFORM GUI.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image048.jpg' | relative_url }})

System directories options under Environment settings window

  * Simulation Option: 

In DEFORM - V12, default settings to run a Simulation can be set using options under Simulation Option tab in Environment settings. Simulation Options window appears as shown in Fig. 6.4.26. By turning on the Keep Message Files DEFORM saves simulation messages without overwriting even after remesh. User can turn on Parallel meshing and set it as default for all simulations, user can apply the parallel meshing either to Solid or to both Solid+Surface. User can turn on No automatic remeshing as default setting for simulations so that simulation can skip the automatic remesh due to non-convergence. The default settings can be changed for each simulation from Run options dialog.

(Optional) If user want to use beta mesher binaries in the problem setup then by turning on Use backup 2D mesher and Use backup 3D Mesher check box option/s user can use beta version mesher binaries during meshing/remeshing procedure.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image027.jpg' | relative_url }})

Simulation Options

  * Multiple Processor:

Multiple processor option under Environment Settings window appears as shown in Fig. 6.4.27. The user can activate the table just by checking next to the Use multiple processor option as shown in the Fig. 6.4.27. The user can specify the computers used to solve the problem as well as the number of processors used on each computer. It is very important that the user enters the correct network name of the computer for the simulation to run. It also provides information about the memory shared between the processors.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image028.jpg' | relative_url }})

Multiple Processor

  * Process:

Process option under Environment Settings window appears as shown in Fig. 6.4.28. User can set the default simulation modes like Deformation, Heat transfer Transformation..etc and control the auto assignment of primary die.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image029.jpg' | relative_url }})

Process options under Environment Settings window

  * Output Control:

The user can set default output type as either Elemental or Elemental+Node for Strain, Stress and Damage variables as shown in Fig. 6.4.29.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image030.jpg' | relative_url }})

Output Controls options under Environment Settings window

  * Email

Email option under Environment Settings window appears as shown in Fig. 6.4.30. This function allows DEFORM to send an email notification at the start of the simulation and with last 25 lines from the Message file and Log file at end of the simulation. Emails are sent via SMTP using StartTLS (or no security). For more information refer [23.7. Email notification of the simulation](/docs/sk/simulator/23_deform_simulator/23_7_email_the_results/).

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image031.jpg' | relative_url }})

Email options under Environment Settings window

  * Memory:

The user can set the required memory size depending upon the usage as shown in Fig. 6.4.31. For most part, the default values of these settings can cover wide range of model requirements. For very large size models (with respect to total number of elements and nodes) depending up on the operating system these settings may need to be increased to handle some run time procedures such as remeshing.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image032.jpg' | relative_url }})

Memory options under Environment Settings window

  * Icon/Font:

The user can change the icon and font size depending on the requirement as shown in the[ Fig. 6.4.32.](6_4_main_menu.htm#Fig._6.4.32._Icon/Font_options_under_Environment_Settings_window)

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image033.jpg' | relative_url }})

Icon/Font options under Environment Settings window

  * Job Protection:

The user can protect Running job from being terminated by setting password as shown in Fig. 6.4.33.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image034.jpg' | relative_url }})

Job protection options under Environment Settings window

  
In Linux system select the enable protection radio button then enter the password in the password field and click on save button to save the password (see Fig. 6.4.33.).

In windows system select the continue button then use password in setup job password popup window and click as shown in Fig. 6.4.34.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image035.jpg' | relative_url }})

Running Job protection in windows password set up window

  * Report: 

From V12 Auto report generation options are provided under Report option in Environment Settings window, the auto report generation settings appears as shown in Fig. 6.4.35. User can set the default Auto Report option as per the requirement for Normal run, DOE runs and OPT runs by turning on the check box. Depending on the settings DEFORM generates the report automatically at the end of simulation.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image036.jpg' | relative_url }})

Report options under Environment Settings window

  1. ******Preferences****:** Provides viewing and object type information of the geometries. In this option, the user can modify the display of the objects in the graphic display window.

  * General:

Show object selection mark allows the user to highlight the selected object in the graphical display window of the Pre processor or the Post processor as shown in Fig. 6.4.36. The user can select either of the option as shown in  Fig. 6.4.37. encoding the colors for the objects in pre and post processor depending on the requirement. The user can view back portion of the die geometry from the front view of the object by checking next to the Show back face for dies under Die geometry option.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image037.jpg' | relative_url }})

General options under Preferences window

  * Entity color:

The user can set colors for different entities as shown in the Fig. 6.4.37.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image038.jpg' | relative_url }})

Entity color option under Preferences window

  * Color Bar:

The user can select the type of color bar depending on the requirement as shown in Fig. 6.4.38. If Print friendly is selected, than the Deform adjusts the display to obtain a better image when printed.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image039.jpg' | relative_url }})

Color bar options under Preferences window

  * Object color:

The user can set the color directly for the objects under Object color in Preference as shown in Fig. 6.4.39.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image040.jpg' | relative_url }})

Object color option under Preference window

**Project Menu**

The Project menu options are shown in Fig. 6.4.40., these options can be used to list the normal, DOE , optimization and die stress study projects, add, delete and rename DOE, Optimization and Die stress study projects.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image041.jpg' | relative_url }})

Project Menu options

**Help Menu**

The help menu options are shown in Fig. 6.4.41., these options can be used open the help manual, get the help about icons in the display, to get the SFTC contact information and to get the product brief information.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image042.jpg' | relative_url }})

Help menu options

  * **Deform manual (F1) :** This option open the DEFORM manual through the default web browser. Short cut key for Help document is F1.

  * **What's this? (Shift+F1):** This icon helps in determining the functions of the other icons in the display utilities window. This can be done by clicking the icon and placing it on the icon or field about which the user requires information and then click. ‘Shift+F1’ keys on the Keyboard can be used to activate this function.

  * **About SFTC:** Provides SFTC contact information in a window.

  * **About:** Provides brief information about DEFORM product in a window. For more details on the release note refer the [chapter 1.11. Release Notes.](/docs/sk/about_deform/1_introduction_to_deform/1_11_release_notes/)

## Simulation Mode menu bar options

In Simulation mode except Options and Project menu options and File menu option import DB/Keyword option all other Pre mode menu options (File, Viewport, Display, Mouse, Tool and Help) are available. In addition to the pre mode menu options Simulation menu gets added to the menu bar before help menu as shown in Fig. 6.4.42. For Pre mode File, Viewport, Display, Mouse, Tool and Help menu bar options refer the section Pre mode menu options.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image043.jpg' | relative_url }})  
(a) 

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image044.jpg' | relative_url }})

(b)

MO Simulation mode Menu and Tool bars; (a) For 3D (b) For 2D

**Simulation Menu**

The simulation menu options are shown in Fig. 6.4.43., these options or icons on tool bar can be used to start, stop and continue the simulation running, open the run options for advanced run options and process monitor to monitor the jobs submitted to run.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image045.jpg' | relative_url }})

Simulation Menu bar options

  * **Run (F9) or Submit simulation of the current Project** ![]({{ '/assets/icons/simulator_icons/mo_run_icon.jpg' | relative_url }}) : This is used to run the job. In case of DOE and Optimization study run option opens the run options as these includes the multiple jobs to run. Then user needs to select submit to queue option, this will generate all samples DB’s and submit to simulate based on the number of simultaneous simulations selected, till then all other samples will be pending in queue. For more details on Run options refer [6.2.1 Simulation options](6_2_integrated_manufacturing_process_simulation_layout.htm#6.2.1._Simulation_Options).

  * **Stop (F10)** ![]({{ '/assets/icons/simulator_icons/mo_stop_icon.jpg' | relative_url }}) : This option is used to Stop the running job.

  * **Continue (Ctrl+ F9) :** This option is used to continue the stopped job.

  * **Add to Batch Queue (Ctrl+Shift+A):** It is used to add the jobs in queue for simulation.

  * **Run options :** This provides run options like run normally, run in queue, multiple processors run settings, fem run types.. etc. For more details on Run options refer [6.2.1 Simulation options](6_2_integrated_manufacturing_process_simulation_layout.htm#6.2.1._Simulation_Options).

  * **Process Monitor** : The process monitor displays the status of any simulations running on the CPU and pending jobs in queue for running.

  * **Simulation Job Status - Built In :** This provides simulating jobs status window, which shows status as Running, Pending or Finished next to that particular job. In case of DOE jobs its more useful to observe status of the multiple jobs in simulation tab itself without visiting the process monitor.

## Post Mode menu bar options

In Post mode except Project menu options and File menu option import DB/Keyword option all other Pre mode menu options (File, Viewport, Display, Mouse, Tool and Help) are available.(See Fig. 6.4.44.) There are no additional menu options gets added in post mode, so for Pre mode File, Viewport, Display, Mouse, Tool and Help menu bar options refer the section 6.5.1. Pre mode menu bar options.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image046.jpg' | relative_url }})  
(a) 

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image047.jpg' | relative_url }})  
(b) 

MO Post mode menu and Tool bars; (a) For 3D (b) For 2D.

## Tool bar options

Tool bar below the menu bar contains icons which are the shortcut for the different menu bar options (See Fig. 6.4.1. ).

In MO Pre mode except the data input modes (guided and expert) and advanced object tools Boolean, Data interpolation and Slicing icons all tool bar icons available under different menu bars.

Tool bar icons are listed below,

New Project, Open Project, Save Project and Import DB/Keyword file options functions refer the section File menu.

Capture screen to image file and Capture screen to clipboard options functions refer the section Tool menu.

Measurement tool, Select mode, Explore mode (select, pan, rotate, zoom), Panning, Rotate, Zoom and Box zoom options functions refer the section Mouse Menu.

  
Refresh, Fit View, Iso view, View point (+X View, -X View, +Y View, -Y View, +Z View, -Z View) options functions refer the section Viewport Menu.

  
Display model in shading mode, Display model in wireframe mode, Display model in shading and wireframe mode, Display model in feature line mode and Add feature line display options functions refer the section Display Menu.

Object Nodes and Object Elements options functions refer the section Tool menu..

**Switch to guided mode** ![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }})

Guided data input mode will provide only basic settings in property editor windows, as the name indicates this guides the user without displaying all advanced options.

**Switch to expert mode** ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})

Expert data input mode as the name indicates will provide advanced settings in property editor windows.

For example in forming operation object mesh window in expert mode having all advanced options like number of elements, size ratio, mesh windows, remesh settings..etc unlike only number of elements in guided mode. Similarly for contact and simulation controls property editor windows in forming operation. So this option will activate only when there is a difference between the guided and expert mode settings and also dependent the operation type for which advanced settings are allowed.

**Boolean**![]({{ '/assets/icons/pre_icons/mo_boolean_icon.jpg' | relative_url }})

This capability allows the user to subtract volume from the mesh of an object from the geometry of another object or Boolean with respect to a plane. (option available only for 3D). This will activate only when user selected the object windows like geometry, mesh, boundary conditions..etc. For more information on Boolean option refer [section 18.1. Boolean.](/docs/sk/pre_processor/18_object_manipulation_tools/18_1_boolean/)

**Data Interpolation** ![]({{ '/assets/icons/pre_icons/mo_data_interpolation_icon.jpg' | relative_url }})

While doing the manual remeshing in the preprocessor, user can transfer data from another object from a different database using this dialog. Once the database is selected user can select the object, and step number from where the data needs to be interpolated. For more information on Data interpolation refer section [17.3. Data interpolation](/docs/sk/pre_processor/17_object_data_initialization/17_3_data_interpolation_window/)[.](/docs/sk/pre_processor/17_object_data_initialization/17_3_data_interpolation_window/)

**Slicing**![]({{ '/assets/icons/pre_icons/mo_slicing_option.jpg' | relative_url }})

This utility enables the users to slice an object and save the 2D cross section,either as geometry or as a keyword file including the state variable data from the slicing plane. (option available only for 3D) For more information on Data interpolation refer section [18.2. Slicing.](/docs/sk/pre_processor/18_object_manipulation_tools/18_2_slicing/)

**Stop current task** ![]({{ '/assets/icons/pre_icons/mo_stop_current_task_icon.jpg' | relative_url }})

This utility enables the users to stop the current running tasks like Point tracking, flownet generation etc. It will activate only when such tasks are running.

  
**Related Topics:**

[6.1. Integrated manufacturing process Pre-processor Layout](/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_1_integrated_manufacturing_process_preprocessor_layout/)

[6.2. Integrated manufacturing process Simulation layout](/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_2_integrated_manufacturing_process_simulation_layout/)

[6.3. Integrated manufacturing process Post layout](/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_3_integrated_manufacturing_process_post_layout/)

[6.5. Files Structure](/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_5_files_structure/)

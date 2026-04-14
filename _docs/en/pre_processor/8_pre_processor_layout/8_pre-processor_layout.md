---
lang: en
title: "8. Pre-Processor Layout"
---

# 8\. Pre-Processor Layout

8.1. Graphic Utilities Window

8.1.1. File Menu

8.1.2. Viewport Menu

8.1.3. Display menu

8.1.4. Mouse Menu

8.1.5. Tool Menu

8.1.6. Options Menu

8.1.7. Help

8.2. Operation Tree

8.2.1.Operation Tree Tool bar options

8.2.2.Object Tree Right Mouse button (RMB) options

8.2.3. Right Mouse Button Display Options

8.3. Input options

The Pre-processor window can be accessed from **New Problem** **window** using "2D/3D Pre” link for new problem and for already existing problem the Pre-processor window can be accessed from DEFORM GUI Main using "2D/3D pre” link in the Deform GUI Main window. The below Fig. 8.1. shows the schematic view of Pre-processor layout.

![]({{ '/assets/images/pre-processor/8_pre_processor_layout/8_image001.jpg' | relative_url }})

Pre-Processor Layout

## Graphic Utilities Window

The graphics utilities window provides view manipulation and other utility functions for the object window. Features include zoom and pan, measurement utilities, viewport controls, printing and Rendering type utilities as seen in Fig. 8.1.

### File Menu

The below Fig. 8.2. shows the File menu options,

![]({{ '/assets/images/pre-processor/8_pre_processor_layout/8_image002.jpg' | relative_url }})

File Menu options

  * **New (Ctrl+N)![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }})** : Using this File Menu option we can create New problem. (See Fig. 8.3.)

![]({{ '/assets/images/pre-processor/8_pre_processor_layout/8_image003.jpg' | relative_url }})

New Problem window

  * **Open (Ctrl+O)** ![]({{ '/assets/icons/pre_icons/mo_open_icon.jpg' | relative_url }}) : Using this File Menu option .DB or .KEY file can be imported.
  * **Save (Ctrl+S)** ![]({{ '/assets/icons/pre_icons/mo_save_icon.jpg' | relative_url }}) : Saves the problem setup in .key file format. This can also be accessed from File Tools menu.
  * **Import ... (Ctrl+D)** ![]({{ '/assets/icons/pre_icons/mo_import_icon.jpg' | relative_url }}) : Existing Database file or .DB file can be imported from the selected folder. This can also be accessed from File Tools menu.
  * **Import Keyword (Ctrl+K)** : Saved Keyword file or .KEY file can be imported from the selected folder. This can also be accessed from File Tools menu.
  * **Export:** Using this file menu option we can save the problem setup in .Key format in the selected directory with user specified name.
  * **Folder options** : Using Folder option Open working folder user can open the working directory in windows explorer.
  * **Archive** : This function is used to get a complete project down to a size to fit on archive media (like a DVD) for backup or distribution.
  * **Image setup (Ctrl+M)** : It is used to setup the current display window or the work space to the required pixel size and capture images to required location in required format.
  * **Capture image (Ctrl+I)**![]({{ '/assets/icons/pre_icons/mo_capture_screen_image_to_file_icon.jpg' | relative_url }}) : This writes the current screen image to a file using the specified image format. This can also access from File Tools menu.
  * **Capture Image to clipboard (Ctrl+Shift+I)**![]({{ '/assets/icons/pre_icons/mo_capture_screen_to_clip_board_icon.jpg' | relative_url }}) : This writes the current screen image to the clipboard. This can also be accessed from File Tools menu.
  * **Recent Projects** : Using this file menu option we can open recently opened projects.
  * **Close (Ctrl+W)** : Closes the current working project but does not quit from the Pre-processor. 
  * **Quit (Ctrl+Q)** : The Quit is used to exit from Pre-processor. 

### Viewport Menu

The below Fig. 8.4. shows the Viewport menu options using these options or icons in tool bar user can refresh or fit the view, switch to Iso or any directional view, set the upward axis, save and load the viewports and viewport lighting settings can be varied.

  
![]({{ '/assets/images/pre-processor/8_pre_processor_layout/8_image004.jpg' | relative_url }})

Viewport Menu options

  * **Refresh (F5)****![]({{ '/assets/icons/pre_icons/mo_refresh_icon.jpg' | relative_url }}) : **The refresh icon redraws the screen, removing any measurement marks, and updating any changes made to the color pallet.

  * **Fit**View**(F3)****![]({{ '/assets/icons/pre_icons/mo_view_fit_icon.jpg' | relative_url }}) : ******Fits all displayed objects or graphs inside the current viewport.

  * **View back (F4)** ![]({{ '/assets/icons/pre_icons/mo_view_back_icon.jpg' | relative_url }}) : Resets objects to the previously viewed display position.

  * **Screen upward** : ****[3D]: This option shows the isometric view in 3D, such that the selected axis will be pointing in the upward direction. For example, if the user selects positive Z-axis from the screen upward option as shown in Fig. 8.5. and then select isometric view option, Z-axis will be pointing upwards in the isometric view. This is not applicable for 2D mode.

  
![]({{ '/assets/images/pre-processor/8_pre_processor_layout/8_image005.jpg' | relative_url }})

Screen upward viewport menu options

  * ******Viewport Menu****![]({{ '/assets/icons/pre_icons/mo_plus_x_view_icon.jpg' | relative_url }}) ,**![]({{ '/assets/icons/pre_icons/mo_minus_x_view_icon.jpg' | relative_url }}),![]({{ '/assets/icons/pre_icons/mo_plus_y_view_icon.jpg' | relative_url }}) ,![]({{ '/assets/icons/pre_icons/mo_minus_y_view_icon.jpg' | relative_url }}),![]({{ '/assets/icons/pre_icons/mo_plus_z_icon.jpg' | relative_url }}),![]({{ '/assets/icons/pre_icons/mo_minus_z_icon.jpg' | relative_url }}) : ****The below Fig. 8.6. shows the Viewport menu options using these options or icons in tool bar user can refresh or fit the view, switch to Iso or any directional view, set the upward axis, save and load the viewports and viewport lighting settings can be varied. 

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image011.jpg' | relative_url }})

Different view selection options

  * **Load and Save viewport :** The user can move or change the views of the geometries by using display tools such as pan, dynamic zoom and box zoom in the display window. These views can be saved using save option provided under viewport tab as shown in Fig. 8.7.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image013.jpg' | relative_url }})

Save view port Menu options

If the view is saved as a local viewport, this view gets saved for the current working project only and can be viewed using load option as shown in Fig. 8.8. If the view is saved as a global viewport the set views becomes the default views for any project, for global viewports to get activated for the projects, the user has to exit from current project. The user can copy global viewports as a local viewports under load option and local viewports to global viewports under save option.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image012.jpg' | relative_url }})

Load view port Menu options

  * **Lighting** : This allows the user to change the brightness and color of the graphics window lighting, can also add more light switches and control its positions as shown in Fig. 8.9. , Fig. 8.10. and Fig. 8.11.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image014.jpg' | relative_url }})

Lighting General properties window

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image015.jpg' | relative_url }})

Lighting Settings properties window

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image016.jpg' | relative_url }})

Light Advanced Properties window

**Set Lighting Property**

Positions of light is indicated by dot as shown in Fig. 8.12.

![]({{ '/assets/images/pre-processor/8_pre_processor_layout/8_image006.jpg' | relative_url }})

Positioning of Lighting

For the light settings, we assume the objects are located at (0, 0, 0) and the observer is located at (0, 500, 0). We have four lights,  
Light1: (-400 ~ -200, 0, 500) (left-top light, from left to right adjustable)  
Light2: ( 200 ~ 400, 0 , 500) (right-top light, from left to right adjustable)  
Light3: ( 0, 200 ~ 400, 500) (front light, from near to far adjustable)  
Light4: (0, 0, 0) (ambient color defined by Red, Blue, Green combinations)  
3D, such that the selected axis will be pointing in the upward direction. For example, if the user selects positive Z-axis from the screen upward option as shown in Fig. 8.12. and then select isometric view option, Z-axis will be pointing upwards in the isometric view. This is not applicable for 2D mode.

### Display menu

Fig. 8.13. shows the display menu options using these options or icons in the tool bar user can select the different objects display rendering types like shading, wireframe, shading and wireframe, feature line (surface patch) and adding feature line to any other rendering types. 

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image017.jpg' | relative_url }})

Display Menu options

  * **Shading (F6)** ![]({{ '/assets/icons/pre_icons/mo_shading_mode_icon.jpg' | relative_url }}) : Smoothly shades the objects within viewport.

  * **Wireframe (F7)** ![]({{ '/assets/icons/pre_icons/mo_wirefrane_mode_icon.jpg' | relative_url }}) : Displays mesh of the object within viewport.

  * **Shading and Wireframe (F8)** ![]({{ '/assets/icons/pre_icons/mo_shade_wireframe_icon.jpg' | relative_url }}) : Smoothly shades and display mesh of objects within viewport.

  * **Feature line or Surface patch** ![]({{ '/assets/icons/pre_icons/mo_feature_line_mode_icon.jpg' | relative_url }}) : Displays the surface edges of the object. For 3D mode refer feature angle to vary the surface patches display.

  * **Add feature line** ![]({{ '/assets/icons/pre_icons/mo_add_feature_line_icon.jpg' | relative_url }}) : This feature will combine surface edges with other display modes options. For 3D mode refer feature angle to vary the surface patches display. 

### Mouse Menu

Fig. 8.14. shows the Mouse menu options using these options or icons in the tool bar user can select different mouse modes to measure the objects linear distance and change or move the objects view in graphics window like panning, rotate (only for 3D), zoom and magnify.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image018.jpg' | relative_url }})

Mouse menu options

  * **Measurement**![]({{ '/assets/icons/pre_icons/mo_measure_tool_icon.jpg' | relative_url }}) : This tool allows the user to measure any distance between two points by clicking consecutively on both points. The measurement can be plot in either X or Y or XY direction, in 3D Z direction will come into picture, using the available CAD style option which displays the measured values in the selected direction. To access the CAD style option user need to right mouse click in the display window when user is in the measurement mode (See Fig. 8.15.). The measurement marks are not erased until the viewport is refreshed and as such are also convenient for marking arbitrary reference points on the screen, which will maintain their location through view changes.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image019.jpg' | relative_url }})![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image020.jpg' | relative_url }})  
(a) (b) 

Right mouse button measurement style options; (a) For 3D (b) For 2D

  * **Select :** The select button is a general pointing utility. It performs several functions which vary with context. It can be used to select a node or an element, to select BCC, stopping controls points on objects and many similar functions. From Right mouse click option menu in graphics window user can change the selected nodes display to point or polygon as shown in Fig. 8.16.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image021.jpg' | relative_url }})

Selected node display RMB option on graphics window

  * **Pan (Shift+LMB)** ![]({{ '/assets/icons/pre_icons/mo_pan_icon.jpg' | relative_url }}) : Pan adjusts the region filling the active viewport without changing the size of the displayed object.

  * **Rotate (Ctrl+LMB)** ![]({{ '/assets/icons/pre_icons/mo_rotate_icon.jpg' | relative_url }}) : This will allow the mouse pointer to rotate the geometries in the required direction. This can also done by holding the Ctrl key and clicking the left mouse button in the active viewport and rolling the mouse backward or forward to rotate the objects.

  * **Rotate X** ![]({{ '/assets/icons/pre_icons/mo_rotate_x_icon.jpg' | relative_url }}) : This will allow the mouse pointer to rotate the object along X-direction.

  * **Rotate Y** ![]({{ '/assets/icons/pre_icons/mo_rotate_y_icon.jpg' | relative_url }}) : This will allow the mouse pointer to rotate the object along Y-direction.

  * **Rotate Z** ![]({{ '/assets/icons/pre_icons/mo_rotate_z_icon.jpg' | relative_url }}) : This will allow the mouse pointer to rotate the object along Z-direction. This option is not available for 2D systems. Even though the user can see this icon while 2D problem setup, if user clicks on it, it will give a notice "This feature is not available in 2D view".

  * **Dynamic zoom (Alt+LMB)** ![]({{ '/assets/icons/pre_icons/mo_zoom_icon.jpg' | relative_url }}) : The dynamic zoom dynamically changes the size of the region of the object which fills the active view port. The view size can be changed by holding Alt key and clicking left mouse button in the active view port and rolling the mouse backward or forward to increase or decrease the size of the object in the display window.

  * **Box Zoom (Ctrl+Alt+LMB)**![]({{ '/assets/icons/pre_icons/mo_box_zoom_icon.jpg' | relative_url }}) : The Box zoom or magnify function allows close up inspection of a small region of the currently display object or graph. The zoom region is selected by holding Ctrl + Alt key and clicking the left mouse button, while dragging the mouse to enclose the selected region with the displayed box. When the mouse button is released the selected region will fill the display window. 

###  Tool Menu 

Fig. 8.17. shows the tool menu options, using these options or icons in the tool bar user can access the tools like object nodes and elements data window and Image capturing tools and its settings.

  
  
![]({{ '/assets/images/pre-processor/8_pre_processor_layout/8_image007.jpg' | relative_url }})

Tool menu options

  * **Object Nodes** ![]({{ '/assets/icons/pre_icons/mo_nodal_data_icon.jpg' | relative_url }}) : The object node data window displays all available information about object nodes. All information can be modified and many of the variables can be plotted. This option will be activated only when object property windows like object main, geometry and mesh windows are selected. For more information please refer to section [17.1 Node Data](/docs/en/pre_processor/17_object_data_initialization/17_1_node_data_window/).

  * **Object Elements** ![]({{ '/assets/icons/pre_icons/mo_elemental_data_icon.jpg' | relative_url }}) : The element data window displays all available information about object elements. All information can be modified and many of the variables can be plotted. This option will be activated only when object property windows like object main, geometry and mesh windows are selected. For more information please refer to section [17.2 Element Data](/docs/en/pre_processor/17_object_data_initialization/17_2_element_data_window/).

  * **Boolean**![]({{ '/assets/icons/pre_icons/mo_boolean_icon.jpg' | relative_url }}) : This capability allows the user to subtract volume from the mesh of an object from the geometry of another object or Boolean with respect to a plane (option available only for 3D). For more information please refer to section [18.1 Boolean](/docs/en/pre_processor/18_object_manipulation_tools/18_1_boolean/).

  * **Data Interpolation** ![]({{ '/assets/icons/pre_icons/mo_data_interpolation_icon.jpg' | relative_url }}) : While doing the manual remeshing in the preprocessor, user can transfer data from another object from a different database using this dialog. Once the database is selected user can select the object, and step number from where the data needs to be interpolated. For more information please refer to section [17.3. Data Interpolation](/docs/en/pre_processor/17_object_data_initialization/17_3_data_interpolation_window/).

  * **Convert 2D to 3D** ![]({{ '/assets/icons/pre_icons/convert_2d_to_3d_icon.jpg' | relative_url }}) : Convert 2D to 3D model will convert the 2D axisymmetric/torsion model by revolving about the centerline and 2D plane strain/plane stress model by extruding in the third direction. For more information please refer to section [22\. Convert 2D to 3D.](/docs/en/pre_processor/22_convert_2d_to_3d/22_convert_2d_to_3d/)

### Options Menu

Fig. 8.18. shows the Options menu options, using these options user can set the DEFORM working environment different settings.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image023.jpg' | relative_url }})

Options menu options

  1. **Environment**

The user can adjust the DEFORM working environment using environment option. Here the user can make changes in display and graphical settings and can save the settings as for his convenience. Setting will update from next session onwards.

  * Region:

The user can select the preferred language under Language option and set to English or SI units under Unit option as a Default unit system for a new problem. The user can select the standards for materials under Material Library to be used as a default for importing materials in the problem. (See Fig. 8.19. )

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image024.jpg' | relative_url }})

Region options under Environment Settings window

  * User Type:

User Type option under Environment Settings window appears as shown in Fig. 8.20. Depending on the user type the default conditions and pop-up windows are activated.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image025.jpg' | relative_url }})

User type options under Environment Settings window

  * **Novice** : If the user is new to DEFORM then this option is preferred.
  * **Intermediate** : This option is for an user who is bit familiar to DEFORM environment. For example, if we select quit option in the GUI, a pop up appears with a message " Do you want to quit", the user can click "Yes" to exit from GUI.
  * **Advanced** : This option is for an user who is well aware of DEFORM, he can eliminate few pop-ups. For example, if we select quit option in the GUI, Deform will close without a popup warning message.

  * User Directory:

User Directory option under Environment Settings window appears as shown in Fig. 8.21. The user can browse for the required location to set it as the working directory under Problem, this directory will be used as a default location to store the generated DB's, key files and working files related to DEFORM. The path under Library root will be used as a default path to store the user data generated in DEFORM. The path under Geometry import will be used as the default path to access the geometries, which can be a problem directory itself. If it is a different location it has to be mentioned under geometry import path separately for 2D and 3D. The temporary files generated while running deform are in the specified path under Temporary Directory.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image026.jpg' | relative_url }})

User directory options under Environment Settings window

  * System Directory:

System Directory option under Environment Settings window appears as shown in Fig. 8.22. Only Advanced user type selection (as mentioned in user type section) activates this tab access to user. Using this option user can change the DEFORM material, press and equipment library path under respective fields, this directory will be used as a default location for the material, press and equipment library in DEFORM. By default these are pointed to the DEFORM library available in the installation location, user can change to user library paths, this path will be called when import material, movement or insert geometries are selected from DEFORM GUI.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image048.jpg' | relative_url }})

System directories options under Environment settings window

  * Simulation Option: 

In DEFORM - V12, default settings to run a Simulation can be set using options under Simulation Option tab in Environment settings. Simulation Options window appears as shown in Fig. 8.23. By turning on the Keep Message Files DEFORM saves simulation messages without overwriting even after remesh. User can turn on Parallel meshing and set it as default for all simulations, user can apply the parallel meshing either to Solid or to both Solid+Surface. User can turn on No automatic remeshing as default setting for simulations so that simulation can skip the automatic remesh due to non-convergence. The default settings can be changed for each simulation from Run options dialog.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image027.jpg' | relative_url }})

Simulation Options

  * Multiple Processor:

Multiple processor option under Environment Settings window appears as shown in Fig. 8.24. The user can activate the table just by checking next to the Use multiple processor option as shown in the Fig. 8.24. The user can specify the computers used to solve the problem as well as the number of processors used on each computer. It is very important that the user enters the correct network name of the computer for the simulation to run. It also provides information about the memory shared between the processors.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image028.jpg' | relative_url }})

Multiple Processor

  * Process:

Process option under Environment Settings window appears as shown in Fig. 8.25. User can set the default simulation modes like Deformation, Heat transfer Transformation .etc and control the auto assignment of primary die.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image029.jpg' | relative_url }})

Process options under Environment Settings window

  * Output Control:

The user can set default output type as either Elemental or Elemental+Node for Strain, Stress and Damage variables as shown in Fig. 8.26.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image030.jpg' | relative_url }})

Output Controls options under Environment Settings window

  * Email:

Email option under Environment Settings window appears as shown in Fig. 8.27. This function allows DEFORM to send an email notification at the start of the simulation and with last 25 lines from the Message file and Log file at end of the simulation. Emails are sent via SMTP using StartTLS (or no security). For more information refer [23.7. Email notification of the simulation](/docs/en/simulator/23_deform_simulator/23_7_email_the_results/).

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image031.jpg' | relative_url }})

Email options under Environment Settings window

  * Memory:

The user can set the required memory size depending upon the usage as shown in Fig. 8.28. For most part, the default values of these settings can cover wide range of model requirements. For very large size models (with respect to total number of elements and nodes) depending up on the operating system these settings may need to be increased to handle some run time procedures such as remeshing.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image032.jpg' | relative_url }})

Memory options under Environment Settings window

  * Icon/Font:

The user can change the icon and font size depending on the requirement as shown in the [Fig. 8.29.](8_pre-processor_layout.htm#Fig._8.29._Icon/Font_options_under_Environment_Settings_window)

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image033.jpg' | relative_url }})

Icon/Font options under Environment Settings window

  * Job Protection:

The user can protect Running job from being terminated by setting password as shown in Fig. 8.30.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image034.jpg' | relative_url }})

Job protection options under Environment Settings window

  
In Linux system select the enable protection radio button then enter the password in the password field and click on save button to save the password (see Fig. 8.30.).  
  
In windows system select the continue button then use password in setup job password popup window and click OK as shown in Fig. 8.31.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image035.jpg' | relative_url }})

Running Job protection in windows password set up window

  * Report: 

From V12 Auto report generation options are provided under Report option in Environment Settings window, the auto report generation settings appears as shown in Fig. 8.32. User can set the default Auto Report option as per the requirement for Nominal run, DOE runs and OPT runs by turning on the check box. Depending on the settings DEFORM generates the report automatically at the end of simulation.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image036.jpg' | relative_url }})

Report options under Environment Settings window

  1. ****Preferences********

Provides viewing and object type information of the geometries. In this option, the user can modify the display of the objects in the graphic display window.

  * General:

Show object selection mark allows the user to highlight the selected object in the graphical display window of the Pre processor or the Post processor as shown in Fig. 8.33. The user can select either of the option as shown in Fig. 8.33. encoding the colors for the objects in pre and post processor depending on the requirement. The user can view back portion of the die geometry from the front view of the object by checking next to the Show back face for dies under Die geometry option.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image037.jpg' | relative_url }})

General options under Preferences window

  * Entity color:

The user can set colors for different entities as shown in the Fig. 8.34.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image038.jpg' | relative_url }})

Entity color option under Preferences window

  * Color Bar:

The user can select the type of color bar depending on the requirement as shown in Fig. 8.35. If Print friendly is selected, than the Deform adjusts the display to obtain a better image when printed.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image039.jpg' | relative_url }})

Color bar options under Preferences window

  * Object color:

The user can set the color directly for the objects under Object color in Preference as shown in Fig. 8.36.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_4_main_menu/6_4_image040.jpg' | relative_url }})

Object color option under Preference window

### Help

The below Fig. 8.37. shows the Help menu options.

![]({{ '/assets/images/pre-processor/8_pre_processor_layout/8_image008.jpg' | relative_url }})

Help menu option

  * **Deform manual**(F1) : This option opens the DEFORM manual through the default web browser. Short cut key for Help document is F1.

  * **What's this?**(Shift+F1) : This icon helps in determining the functions of the other icons in the display utilities window. This can be done by clicking the icon and placing it on the icon or field about which the user requires information and then click. ‘Shift+F1’ keys on the Keyboard can be used to activate this function.

  * **About SFTC :** Provides SFTC contact information in a window.

  * **About DEFORM Next-Gen Pre :** Provides brief information about DEFORM product in a window. For more details on the release note refer the chapter [1.11. Release Notes.](/docs/en/about_deform/1_introduction_to_deform/1_11_release_notes/)

## Operation Tree

The purpose of this tree is to provide the user with a systematic list of required data for a given simulation. The data in the list is edited in the setting modification window. The data that is being edited is controlled by the current active position within the operation tree. The structure of the program will progress directly down this list by clicking next in Property Editor region. Alternatively, if any data needs to be modified, clicking on given item in the list will allow that item to be edited in the property editor region.

Operation tree (See Fig. 8.38.) contains list of required data like geometry, mesh, boundary conditions, movement controls of an object, process type and simulation controls etc.  
The tool bar below the object tree is used to switch on or off the object, geometry, mesh and contacts display.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image031.jpg' | relative_url }})

Operation Tree

### **Operation Tree Tool bar options**

**[2D][3D]:**

**Show Object![]({{ '/assets/icons/pre_icons/mo_show_obj_icon.jpg' | relative_url }}) :** Turns on/off the selected object from object tree.

**Show Mesh![]({{ '/assets/icons/pre_icons/mo_show_mesh_icon.jpg' | relative_url }}) :** Shows or hides mesh of the selected object from object tree.

**Show Geometry![]({{ '/assets/icons/pre_icons/mo_show_geo_icon.jpg' | relative_url }}) :** Shows or hides geometry of the selected object geometry from the object tree.

**Show Contact Nodes**![]({{ '/assets/icons/pre_icons/mo_show_cotact_icon.jpg' | relative_url }})**:** Turns on the contact display for the selected object from object tree with all other all object. (See Fig. 8.40.)

  
**[3D]:**

**Make Transparent![]({{ '/assets/icons/pre_icons/mo_transparent.jpg' | relative_url }}) :** Turns on/off transparency of the selected object from the object tree.

**Show Backface![]({{ '/assets/icons/pre_icons/mo_show_backfac_icon.jpg' | relative_url }}) :** Turns on/off the back surface of the object selected object from the object tree, it will be more useful when the object are made transparent. (See Fig. 8.39.)

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image032.jpg' | relative_url }}) ![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image033.jpg' | relative_url }})

Plastic object mesh in shaded rendering type; (a) With Back face off (b) With Back face on

Object Display Modes [2D,3D]: DEFORM has 3 different object display modes as shown in Fig. 8.40.  
Single Object mode ![]({{ '/assets/icons/pre_icons/mo_show_single_obj_icon.jpg' | relative_url }}): Only the selected object from object tree is displayed. All other objects are hidden.  
Multi Object mode ![]({{ '/assets/icons/pre_icons/mo_show_multi_obj_icon.jpg' | relative_url }}): All objects are displayed in graphics window. The selected object from object tree is displayed in solid color and all other objects are transparent in 3d mode. (See Fig. 8.40.)

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image034.jpg' | relative_url }})

Multi object mode when plastic workpiece object get selected

  
**User-defined Object mode![]({{ '/assets/icons/pre_icons/mo_show_user_defined_obj_icon.jpg' | relative_url }})** : User can toggle the object's Display, Geometry, Mesh, Transparency (only for 3D), Slice plane (only for 3D) modes independently. This can be done by checking and unchecking respective check boxes as shown in Fig. 8.41.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image035.jpg' | relative_url }})

User defined Object Mode window

  
Following are the settings we must select based on the objects display requirements,

**Apply Display options**![]({{ '/assets/icons/pre_icons/mo_apply_display_option.jpg' | relative_url }}) : Applies the selected display option for the objects.

**Visible**![]({{ '/assets/icons/pre_icons/mo_visible.jpg' | relative_url }}) : Turns on/off the selected object display.

**Mesh**![]({{ '/assets/icons/pre_icons/mo_mesh_icon.jpg' | relative_url }}) : Shows or hides display of the selected object mesh.

**Geometry**![]({{ '/assets/icons/pre_icons/mo_geometry _icon.jpg' | relative_url }}) : Shows or hides display of the selected object geometry.

**Transparency![]({{ '/assets/icons/pre_icons/mo_transparent.jpg' | relative_url }})** : Turns on/off transparency of the selected object.

**Slice**![]({{ '/assets/icons/pre_icons/mo_slice.jpg' | relative_url }}) : Turns on/off sliced plane for the selected sliced object.

###  **Object Tree Right Mouse button (RMB) options**

By using the RMB on Object or its Geometry branches in object tree user will get few options to export the geometry or control the object display.  
  
By RMB click on the Object any particular object branch (![]({{ '/assets/icons/pre_icons/mo_plastic_workpiece_branch.jpg' | relative_url }})) user can export the geometry, turn on the contact nodes display, make the 3d objects transparent and turn on the 3d objects back face display as shown in Fig. 8.42. below. Geometry inside mark for 2d and Geometry normal vectors for 3d display can be activated by RMB option on ![]({{ '/assets/icons/pre_icons/mo_geometry_branch.jpg' | relative_url }}) (Geometry branch) as shown in Fig. 8.43. For more details on Enable contact nodes and Show back face options refer operation tree tool bar options.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image036.jpg' | relative_url }}) ![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image037.jpg' | relative_url }})

  
(a) (b)

Operation tree Object RMB options; (a) For 2D (b) For 3D

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image038.jpg' | relative_url }}) ![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image039.jpg' | relative_url }})

(a) (b)

Operation tree Geometry RMB options; (a) For 2D (b) For 3D

###  Right Mouse Button Display Options

[2D, 3D]: Right mouse click in display window of pre processor a menu option appears as shown in Fig. 8.44. This option provides a short cut for graphic utilities, object control bar, display modification settings in pre processor. Depending upon the window the RMB options will change. 

![]({{ '/assets/images/pre-processor/8_pre_processor_layout/8_image009.jpg' | relative_url }}) ![]({{ '/assets/images/pre-processor/8_pre_processor_layout/8_image010.jpg' | relative_url }})

  
(a) (b)

Right mouse button display options; (a) For 2D (b) For 3D

  * **DB Info [2D, 3D] :** Display the Database name in display window.

  * **Title [2D, 3D] :** Display the Step number name in display window.

  * **Show Ruler [2D, 3D] :** Using this user can turn on/off the ruler display in the display window.

  * **Show Dimensions [2D, 3D] :** Display the maximum dimensions of the object in X and Y directions in 2D and in X, Y and Z directions in 3D.

  * **Show Center line [ 2D] :** Using this user can turn on/off the Center line display in the display window.

  * **Show Origin Axis [ 3D] :** Using this user can turn on/off the origin axis display in the display window. 

  * **Show Current Object mark [2D, 3D] :** This shows the mark at the top and bottom plane four corners of the 3D object and top and bottom plane two corners of the 2D object in multiple and user object modes indicating that object is the current selected object in the object tree, so for that object user can define the data from the data definition window and also help while positioning the objects by showing these marks for the selected positioning object.

  * **Show view Axis [ 2D, 3D] :** Using this user can turn on/off the view axis display in the display window.

For **Refresh** , **View fit** , **View back** , **Load** and **Save view port** options refer the above section Viewport menu bar options.

  * **Auto fit:** This option is used to automatically fit the view of the object (s) as per the selection. (See Fig. 8.45.)

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image046.jpg' | relative_url }})

Auto fit option

  * **Object display mode:** Using this user can control the object display in graphics window, there are three types of object display modes, those are single, multi and user defined object display modes (See Fig. 8.46.). Refer to Object display mode explanation under Operation Tree for more details.

  * 

![]({{ '/assets/images/pre-processor/8_pre_processor_layout/8_image011.jpg' | relative_url }})

Object display mode

  * **Contact display :** Using this user can turn on/off the inter-object contact nodes display. (See [Fig. 8.47.](8_pre-processor_layout.htm#Fig._8.47._Contact_display_turn_on/off_options))

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image052.jpg' | relative_url }})

Contact display turn on/off options

  * **Calculate contact area :** Using this user can get the contact area data. 

  * **Measurement style :** Using this tool user can measure the distance between two points in the linear (X,Y or Z direction) and angular directions (XYZ direction) in CAD style. (See Fig. 8.48.)

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image054.jpg' | relative_url }}) ![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image053.jpg' | relative_url }})

  
(a) (b)

Right mouse button measurement style options; (a) For 2D (b) For 3D

  * **Measurement options :** Measure option available are clear all, clear last, Change text color, change Line color and Background color options as show in Fig. 8.48.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image055.jpg' | relative_url }})

Right mouse button measurement options

  * **Picking Sensitivity :** Using this user can select the sensitivity of picking the nodes and elements of the object and points on the object or anywhere in the display window. There are five levels of sensitivities Super fine, Fine, Normal, Coarse and Rough. If user wants to pick precisely then Fine picking is preferred otherwise default Normal picking is enough. If the user wants to select the nodes or elements near the picking point on the object then Coarse picking is preferred.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image056.jpg' | relative_url }})

Picking Sensitivity option

  * **Background Theme :** Using this option user can select the different background themes available like Navy blue, White, Black and Gray for the graphics window as shown in Fig. 8.51.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image057.jpg' | relative_url }})

Right mouse button background themes options

  * **Display Options:** Using this option (See Fig. 8.52.) user can select the point or polygon type display of the selected contact node. Also can select point size under Point size list.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image058.jpg' | relative_url }})

Right mouse button selected nodes display options

After turning on the contact display user can select point or polygon type display option, 2d example with point and polygon contact node display is shown in Fig. 8.53.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image059.jpg' | relative_url }})

2D Point and polygon contact nodes display example

  * **Change feature angle [3D] :** User can use this option to change the range of selection when selecting the elements/nodes/polygons for adding BCC or editing geometry etc using surface patch method. It displays the surface patch by treating surfaces within the feature angle as the one surface. A curved surface with smaller feature angle means fewer surface polygons will be picked at a time. Selecting the option Change feature angle pops up the feature angle changing window as shown in Fig. 8.54. Also see the Fig. 8.55. for the surface patch display for the die geometry with different feature angle.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image031.jpg' | relative_url }})

RMB 3D feature angle entry window

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image033.jpg' | relative_url }})![]({{ '/assets/images/integrated_manufacturing_process_setup/6_2_integrated_manufacturing_process_simulation_layout/6_2_image032.jpg' | relative_url }})  
(a) (b)

Surface path display with different feature angle; (a) For angle 10 (b) For angle 20

## Input options

Under Operation tree following options are available to setup problem:

  * **Geometry type [2D]** : This option is available only for 2D where user can select Geometry type as shown in Fig. 8.56. Even in Expert mode Simulation controls page we have these geometry type options.

![]({{ '/assets/images/pre-processor/8_pre_processor_layout/8_image012.jpg' | relative_url }})

Geometry type page

  * **Simulation Controls [2D,3D] :** Options defined under Simulation Controls, control the numerical behaviour of the solution. Please refer to [9\. Simulation Controls](/docs/en/pre_processor/9_simulation_controls/9_simulation_controls/).

  * **Material list [2D,3D] :** For a simulation to achieve a high level of accuracy it is important to understand the material properties required to specify a material used in DEFORM. Please refer to Chapter [10\. Material Properties](/docs/en/pre_processor/10_material_data/10_material_data/).

  * **Object [2D,3D]** : In Object page we will define the number of objects required for the problem setup.

  * **General Definition [2D,3D]** : To define Object Name, Object Temperature and Object types for the object. Please refer to Chapter [11\. General Object Data Definition](/docs/en/pre_processor/11_general_object_data_definition/11_general_object_data_definition/)
  * **Geometry Data [2D,3D]** : To define the geometry data for the object by importing the geometry or by creating geometry using primitive options. Please refer to Chapter [12\. Geometry Modelling](/docs/en/pre_processor/12_geometry_modelling/12_geometry_modelling/).
  * **Mesh Data [2D,3D]** : option to generate mesh for the object geometry using mesh options. Please refer to Chapter [13\. Mesh Generation](/docs/en/pre_processor/13_mesh_generation/13_mesh_generation/).
  * **Material assignment [2D,3D]** : option to assign material for the object by selecting the material in Material list. 
  * **Boundary Conditions [2D,3D]** : option used to assign boundary condition for the object. Please refer to Chapter [14\. Boundary Conditions](/docs/en/pre_processor/14_boundary_conditions/14_boundary_conditions/).
  * **Movement controls [2D,3D]** : option used to define movement for the object. Please refer to Chapter [15\. Movement Controls Settings](/docs/en/pre_processor/15_movement_controls_definition/15_movement_controls_settings/).
  * **Properties [2D,3D]** : option to define object properties for the object. Please refer to Chapter [16\. Object Properties](/docs/en/pre_processor/16_object_properties/16_object_properties/).
  * **Initialize [2D,3D]** : option to initialize the state variable for the object. Please refer to Chapter [17\. Object Data Initialize.](/docs/en/pre_processor/17_object_data_initialization/17_object_data_initialize/)
  * **Built In Flownet [3D]** : option used to generate Built in Flownet for deformable object. 

  * **Positioning [2D,3D]** : Once the object is defined, a variety of positioning features are available to place the objects in the correct position before the process is modelled. It can also be accessed from Pre Tools Menu. Please refer to Chapter [19\. Object positioning](/docs/en/pre_processor/19_object_positioning/19_object_positioning/).

  * **Contact [2D,3D]** : The purpose of inter-object relations is to define how the different objects in a simulation interact with each other. Please refer to Chapter [20\. Inter-Object Definition](/docs/en/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/).

  * **Stopping Controls [2D,3D]** : In Guided mode Stopping controls page, it is having Deformation and Thermal Stopping criteria options as shown in below Fig. 8.57. In Expert mode will have [Simulation controls](/docs/en/pre_processor/9_simulation_controls/9_3_stopping_controls/) options.

![]({{ '/assets/images/pre-processor/8_pre_processor_layout/8_image013.jpg' | relative_url }})

Stopping controls page

  * **Step [2D,3D]** : In guided mode step page, it has solution step definition for defining the Die displacement, Time and Temperature, Number of steps with step increment, starting step number and the selection of the Primary die as shown in below Fig. 8.58. In expert mode step page will have all the simulation controls options.

![]({{ '/assets/images/pre-processor/8_pre_processor_layout/8_image014.jpg' | relative_url }})

Step page

  * ******Generate DB** [2D,3D]**:** The simulation data set entered into the pre-processor can be written as a new database or appended to an existing database file. Please refer to Chapter [21\. Database Generation](/docs/en/pre_processor/21_database_generation/21_database_generation/)

  
**Related Topics:**

[9\. Simulation Controls](/docs/en/pre_processor/9_simulation_controls/9_simulation_controls/)

[10\. Material Properties](/docs/en/pre_processor/10_material_data/10_material_data/)

[11\. General Object Data Definition](/docs/en/pre_processor/11_general_object_data_definition/11_general_object_data_definition/)

[12\. Geometry Modelling](/docs/en/pre_processor/12_geometry_modelling/12_geometry_modelling/)

[13\. Mesh Generation](/docs/en/pre_processor/13_mesh_generation/13_mesh_generation/)

[14\. Boundary Conditions](/docs/en/pre_processor/14_boundary_conditions/14_boundary_conditions/)

[15\. Movement Controls Settings](/docs/en/pre_processor/15_movement_controls_definition/15_movement_controls_settings/)

[16\. Object Properties](/docs/en/pre_processor/16_object_properties/16_object_properties/)

[17\. Object Data Initialize](/docs/en/pre_processor/17_object_data_initialization/17_object_data_initialize/)

[18\. Advanced Object Data Definition](/docs/en/pre_processor/18_object_manipulation_tools/18_object_manipulation_tools/)

[19\. Object positioning](/docs/en/pre_processor/19_object_positioning/19_object_positioning/)

[20\. Inter-Object Definition](/docs/en/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/)

[21\. Database Generation](/docs/en/pre_processor/21_database_generation/21_database_generation/)

[22\. Convert 2D to 3D](/docs/en/pre_processor/22_convert_2d_to_3d/22_convert_2d_to_3d/)

[23\. Simulatior](/docs/en/simulator/23_deform_simulator/23_introduction_to_deform_simulator/)

[24\. Post Processor](/docs/en/post_processor/24_introduction_to_post_processor/24_introduction_to_post_processor/)

[56\. User Routines](/docs/en/user_routines/56_user_routines_in_deform/56_user_routines_in_deform/)

[3\. License Manager](/docs/en/starting_up_deform/3_license_manager/license_manager_mainpg/)

[Appendices](/docs/en/appendices/appendices_list/)

[Keyword Documentation](/docs/en/keyword_documentation/deform_keywords_list/)

  
**Operations:**  
[Integrated Manufacturing Process (MO)](/docs/en/integrated_manufacturing_process_setup/integrated_manufacturing_process_mainpg/)

[Forming operation Manual](/docs/en/operation_templates/33_forming/33_introduction_to_forming/)

[Shape Rolling Manual](/docs/en/operation_templates/43_shape_rolling/43_introduction_to_shape_rolling/)

[Ring Rolling Manual](/docs/en/operation_templates/42_ring_rolling/42_introduction_to_ring_rolling/)

[Extrusion Template Manual](/docs/en/operation_templates/31_extrusion/31_introduction_to_extrusion/)

[Machining Template Manual](/docs/en/operation_templates/39_cutting/39_introduction_to_cutting/)

[Inverse Heat Transfer Manual](/docs/en/inverse_heat/51_introduction_to_inverse_heat/)

[3D Geo Tool](/docs/en/operation_templates/50_3d_geo_tool/50_introduction_to_3d_geo_tool/)

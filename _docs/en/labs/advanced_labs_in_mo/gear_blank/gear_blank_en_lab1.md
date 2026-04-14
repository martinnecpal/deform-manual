---
lang: en
title: "Gear Blank EN Lab 1"
---

# Lab 1.2D upset operation

### Create a new problem

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear.

Create a new problem either by selecting **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in [Fig. L1.1.](gear_blank_en_lab1.htm#Fig_L1_1_New_Problem_setup_window) Select " **Integrated Manufacturing Process** " radio button and Unit system as "**English** " using radio button. Define Problem Name as "**Gear** " and make sure the “Show option dialog” check box is turned on (if we do not turn on the “**Show option dialog** ” check box, then we will not get the New Project dialog in MO UI). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

New Problem setup window

Multiple operation wizard will open, At this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session we will use ‘******Gear** ** **’ as the project name and confirm that First operation check box is unchecked as we will add operation later and use the default (home) directory as shown in [Fig. L1.2.](gear_blank_en_lab1.htm#Fig_L1_2_MO New Project window) Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to continue to open new project. This lab will be referenced in future labs so it is important to use the name above.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0002.jpg' | relative_url }})

MO New Project window

### Open Preprocessor

Add the **2D Forming operation** as first operation from Explorer tab as shown in [Fig. L1.3.](gear_blank_en_lab1.htm#Fig_L1_3_Adding_2D_Forming_operation_from_operation_explorer)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0003.jpg' | relative_url }})

Adding 2D Forming operation from operation explorer

Change the default operation title to "**upset** " from Forming by selecting the title in the operation editor as shown in [Fig. L1.4.](gear_blank_en_lab1.htm#Fig_L1_4_Renaming_operation_title_to_upset) and press **Enter** keyboard button.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0004.jpg' | relative_url }})

Renaming operation title to upset

### Select Geometry type and Simulation Modes

Confirm the geometry type selected is **Axi-symmetric** in Geometry type page, then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

In this lab we will be showing how to setup simple Isothermal problem, so in Simulation controls page, **uncheck** the **Heat transfer mode** check box (See [Fig. L1.5.](gear_blank_en_lab1.htm#Fig_L1_5_Simulation_control_window)). then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0005.jpg' | relative_url }})

Simulation control window

### Add material from Library

Click the ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load material from library) button as shown in [Fig. L1.6.](gear_blank_en_lab1.htm#Fig_L1_6_Loading_material_from_library) Select the **Steel_at_Extended_Temperatures** category, then A**ISI-8620[1550-2200F(850 -1200C)]** and click the ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}) button.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0006.jpg' | relative_url }})

Loading material from library

Material is loaded to material list, click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) for Material list window. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) for Material properties windows as we use the default properties in database for this lab.

### Set number of Objects

The forging operation to be simulated requires a workpiece and a top and bottom die. If there aren't already three objects, add the three objects by clicking the ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) (insert object) button, Workpiece and two dies. Object window looks as shown in [Fig. L1.7.](gear_blank_en_lab1.htm#Fig_L1_7_Objects_window_to_Add_or_Delete_the_objects) Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0007.jpg' | relative_url }})

Objects window to Add or Delete the objects

Before we proceed further, go to **Options**![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **Preferences** menu option and ensure that**Y- axis** is up is the preferred upward axis. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button.

**Graphic Display Icons**

_**Icon**_ |  _**Function**_ |  _**Description**_  
---|---|---  
![]({{ '/assets/icons/pre_icons/mo_shading_mode_icon.jpg' | relative_url }}) |  View shaded objects |  Displays all objects shaded without a mesh  
![]({{ '/assets/icons/pre_icons/mo_wirefrane_mode_icon.jpg' | relative_url }}) |  View mesh only |  Displays all objects unshaded with a mesh  
![]({{ '/assets/icons/pre_icons/mo_shade_wireframe_icon.jpg' | relative_url }}) |  View shaded mesh |  Displays all objects shaded with a mesh  
![]({{ '/assets/icons/pre_icons/mo_feature_line_mode_icon.jpg' | relative_url }}) |  View surface patch |  Only the feature lines of the objects are shown  
![]({{ '/assets/icons/pre_icons/mo_refresh_icon.jpg' | relative_url }}) |  Refresh |  Refreshes the DISPLAY window and clears previous measuring lines  
![]({{ '/assets/icons/pre_icons/mo_fit_all_icon.jpg' | relative_url }}) |  Fit view |  Fits all objects into the DISPLAY window  
![]({{ '/assets/icons/pre_icons/mo_capture_screen_image_to_file_icon.jpg' | relative_url }}) |  Capture image |  Captures the DISPLAY window and saves it to a file  
![]({{ '/assets/icons/pre_icons/mo_capture_screen_to_clip_board_icon.jpg' | relative_url }}) |  Capture image to clipboard |  Captures DISPLAY window and saves in memory clipboard  
  
### Define Workpiece general object data

Accept the default object name Workpiece. Assign the temperature as **2250** °F and confirm the object type selected is **plastic**. (See [Fig. L1.8.](gear_blank_en_lab1.htm#Fig_L1_8_Workpiece_object_window)). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0008.jpg' | relative_url }})

Workpiece object window

Note:

The Import Object button on the General tab is for importing data from a different DEFORM problem keyword or database. In most setups, you will use the “Import Geometry” option on the next tab.

### Create workpiece geometry from primitive

Click on the ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) button to create a geometry within DEFORM. Select **cylinder** type. The workpiece diameter is 5.00", so you will define a radius of **2.50** ", **height** of **8.15** ”, with **corner****radii** of **0.10** ”. Enter a **radius** of 2.50, a **Height** of 8.15, R1 & R2 of 0.10 (see [Fig. L1.9.](gear_blank_en_lab1.htm#Fig_L1_9_2D_axi-symmetric_geometry_primitive_window)). Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button and then observe the geometry in graphics window.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0009.jpg' | relative_url }})

2D axi-symmetric geometry primitive window

**Display Manipulation**

Functions that manipulate the DISPLAY window (such as Pan, Zoom, Magnify, and Rotate) can be activated using icons at the top of the Pre-processor window. These functions also have easy keyboard/mouse combination hotkeys that allow you to quickly perform these functions. Once you have read about these functions, feel free to use them to manipulate the view of the Billet in the DISPLAY window.

**Display Icons**

_**Icon**_ |  _**Function**_ |  _**Description**_  
---|---|---  
![]({{ '/assets/icons/pre_icons/mo_pan_icon.jpg' | relative_url }}) |  Pan |  The objects in the DISPLAY window can be dynamically panned up, down, left, or right by moving the mouse while holding the left mouse button. (Shortcut: Shift + Left Mouse Button)  
![]({{ '/assets/icons/pre_icons/mo_zoom_icon.jpg' | relative_url }}) |  Zoom |  The DISPLAY window can be dynamically zoomed in or out by holding the left mouse button and moving the mouse up or down. (Shortcut: Alt + Left Mouse Button)  
![]({{ '/assets/icons/pre_icons/mo_box_zoom_icon.jpg' | relative_url }}) |  Magnify |  A portion of the DISPLAY window can to be magnified by clicking and holding the left mouse button at one corner of the zoom box and dragging the cursor to create a window encompassing the zoom area. (Shortcut: Ctrl + Alt + Left Mouse Button)  
  
**Point Selection**

Point coordinates and distances between points can be obtained from the current display.

**Point Selection Icons**

_**Icon**_ |  _**Function**_ |  _**Description**_  
---|---|---  
![]({{ '/assets/icons/pre_icons/mo_measure_tool_icon.jpg' | relative_url }}) |  Measure |  Distances between any two points can be measured by clicking the first point and then clicking the second point. The measuring line will remain on the screen until the Refresh button is clicked.  
![]({{ '/assets/icons/pre_icons/mo_select_icon.jpg' | relative_url }}) |  Select |  This is the default display mode and is used to select and get information about nodes and element faces. This is also the mode to be used when measuring.  
  
Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button to generate workpiece mesh.

### Generate Mesh for workpiece

The default target **number of elements** is **1000**. Accept the default number of elements and click the ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button to generate the mesh for workpiece as shown in [Fig. L1.10.](gear_blank_en_lab1.htm#Fig_L1_10_Mesh_generation_window)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0010.jpg' | relative_url }})

Mesh generation window

Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button to assign material for workpiece.

### Assign Material to Workpiece

Click on the **AISI-8620[1550-2200F(850 -1200C)]** in the material window to assign the material to the workpiece as shown in [Fig. L1.11.](gear_blank_en_lab1.htm#Fig_L1_11_Object_Material_Assigning_window)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0011.jpg' | relative_url }})

Object Material Assigning window

Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button to assign the workpiece boundary conditions.

### Assign Workpiece boundary condition

By default Velocity constraint Vx=0 boundary conditions assigned along the centerline as the Geometry type selection is Axi-symmetric. Confirm that the velocity is set to zero and the X direction is selected by selecting the line “X, Fixed” that appears in the Boundary Conditions tree and observing the graphics window (see [Fig. L1.12.](gear_blank_en_lab1.htm#Fig_L1_12_Workpiece_Boundary_Conditions_window)).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0012.jpg' | relative_url }})

Workpiece Boundary Conditions window

If this line is not present, boundary conditions have not been added. In such case use the edge tool ![]({{ '/assets/icons/pre_icons/mo_bcc_edge_icon.jpg' | relative_url }}) and then click on any node on the center line of the workpiece to select all the nodes on that edge, then click on ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) button to apply the settings.

Click on **Top die** in operation tree as there is no Movement, Property and Initialize settings to vary for workpiece object.

### Defining Top die general object data

Keep the Top die default temperature as 68°F and confirm the object type selected is **rigid** and selected as Primary die as shown in [Fig. L1.13.](gear_blank_en_lab1.htm#Fig_L1_13_Top_die_object_window)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0013.jpg' | relative_url }})

Top die object window

Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button to define the top die geometry.

### Import and edit the Top die geometry

Import the top die geometry from an igs file. Click the ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load geometry from library) button and open (import) the file “**Flat_dies_ENG****.****igs** ”. This can also be imported using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Load geometry from a file) button by browsing the geometry file path. The geometry for top die is located in DEFORM installation folder \2D\Labs directory.

Because there is more than one geometry in this file, you will need to select ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}) for popup informing this to open geometry automatically for editing the geometry. (See [Fig. L1.14.](gear_blank_en_lab1.htm#Fig_L1_14_Top_die_Geometry_window))

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0014.jpg' | relative_url }})

Top die Geometry window

Geometry editor will be opened, select the ![]({{ '/assets/icons/pre_icons/mo_xyr_button.jpg' | relative_url }}) button above the geometry table to activate all geometry editing tool bar options. Use ![]({{ '/assets/icons/pre_icons/mo_area select.jpg' | relative_url }}) (Area select) icon, draw a box around the lower geometry to select it. and press Delete keyboard button to keep only upper geometry (See [Fig. L1.15.](gear_blank_en_lab1.htm#Fig_L1_15_Boundary_selection_from_Geometry_editor_for_top_die)). Selected geometry can also be deleted by selecting the boundary to delete using ![]({{ '/assets/icons/pre_icons/mo_delete_selected.jpg' | relative_url }}) (Select deleted) icon.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0015.jpg' | relative_url }})

Boundary selection from Geometry editor for top die

It is necessary to visually check the geometry orientation on the part. Click on the ![]({{ '/assets/icons/pre_icons/mo_show_inside.jpg' | relative_url }}) (Show inside) icon from top geometry tool bar to show the geometry orientation as shown in [Fig. L1.16.](gear_blank_en_lab1.htm#Fig_L1_16_Reversing_the_direction_of_the_geometry_orientation) Also select ![]({{ '/assets/icons/pre_icons/mo_show_vertex_numbers_icon.jpg' | relative_url }}) (Show vertex numbers) icon to observe the direction of geometry boundary creation using numbering order of the geometry vertices, clockwise direction of creation will have the geometry orientation inside. The shading / arrows of geometry orientation should be towards inside of the part. If it is towards outside, use the ![]({{ '/assets/icons/pre_icons/mo_reverse_direction.jpg' | relative_url }}) (Reverse direction) icon and click on the geometry boundary to be reversed as shown in [Fig. L1.16.](gear_blank_en_lab1.htm#Fig_L1_16_Reversing_the_direction_of_the_geometry_orientation) Click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to close the geometry editing.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0016.jpg' | relative_url }})

Reversing the direction of the geometry orientation

Click on the ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) button to open the Check and Correct Geometry menu. Change the Geometry **open/close/auto** type to open and click the ![]({{ '/assets/icons/pre_icons/mo_check_and_correct_geo_button.jpg' | relative_url }}) button. You should receive a message that the geometry is legal as shown in [Fig. L1.17.](gear_blank_en_lab1.htm#Fig_L1_17_Check_and_correct_geometry_window_for_top_die_geometry) Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to exit the menu.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0017.jpg' | relative_url }})

Check and correct geometry window for top die geometry

The geometry checking tool should be used on every 2D geometry you bring into DEFORM, even if the geometry looks legal.

Click on the **Movement** under **Top****die** in operation tree as this is an isothermal simulation there is no need to generate mesh or assign material to top die.

### Assigning movement controls to top die

The default mode is constant **speed**. Input a value of **3** in/sec for the **Constant** value and confirm that the Direction is **-Y** as shown in [Fig. L1.18.](gear_blank_en_lab1.htm#Fig_L1_18_Top_die_movement_controls_window)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0018.jpg' | relative_url }})

Top die movement controls window

Click on the **Bottom****die** in operation tree as there is no changes to do in top die property window.

### Defining Bottom die general object data

Keep the Bottom die default temperature 68°F and confirm its object type is **rigid**. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button to define the bottom die geometry.

### Creating bottom die geometry from geometry editor

Click on the ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}) button to define the bottom die geometry from geometry editor. Make sure **XYR** format is selected in geometry table. To define the geometry, enter the geometry points in table form as shown in [Fig. L1.19.](gear_blank_en_lab1.htm#Fig_L1_19_Bottom_die_geometry_table_with_geometry)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0019.jpg' | relative_url }})

Bottom die geometry table with geometry

These points will trace out the geometry in a counter clockwise fashion to ensure that the geometry orientation is on the inside of the geometry as shown in [Fig. L1.20.](gear_blank_en_lab1.htm#Fig_L1_20_Bottom_die_geometry_orientation)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0020.jpg' | relative_url }})

Bottom die geometry orientation

Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the geometry definition and click on the **Positioning** in operation tree to open the objects positioning window.

### Confirm position and generate contact

**Confirm position**

The geometries should be in the correct position. Confirm that the workpiece is positioned on top of the bottom die and that the top die is positioned against the workpiece as shown in [Fig. L1.21.](gear_blank_en_lab1.htm#Fig_L1_21_Correct_objects_positioning) Further positioning is not required for this operation.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0021.jpg' | relative_url }})

Correct objects positioning

Click on the **Contact** in operation tree to open the Inter-Object window, as there is no need of Scheduled positioning for this operation.

Note:

Scheduled positioning is explained in [lab3](gear_blank_en_lab1.htm#Lab3_Sequential_3D_forge_operation).

**Inter-Object Relationships: Assign Friction; Generate contact**

DEFORM will automatically create default Master-Slave relationships using ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) button create three relationships as shown in [Fig. L1.22.](gear_blank_en_lab1.htm#Fig_L1_22_Inter_object_window_and_Objects_with_inter-object_contacts_display) DEFORM will create three relationships. Two where each tool is the master and the workpiece is the slave. The third relationship will be a (Workpiece – Workpiece) relationship. This relationship will allow self contact of the workpiece if a fold develops.

Click on the Edit button for one of the relationships. Under the **Friction**![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**Value** box, use the Constant drop down menu to select **Hot****forging**(lubricated) **0.3**. If you have experience that suggests that a different friction value would give better results for your process, you can enter that value directly in this field. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to exit the menu. Click ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) to apply the friction value to the two other relationships.

Next, assign contact. Initial contact conditions provide a starting condition for the finite element solver. After the solver calculation starts, contact is automatically updated.

The ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) (Tolerance) button calculates tolerances for contact generation. Click the ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) (Tolerance) button followed by the ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) button (at bottom of the inter-object window). You should see the contact nodes on the workpiece where contact has been generated. See [Fig. L1.22.](gear_blank_en_lab1.htm#Fig_L1_22_Inter_object_window_and_Objects_with_inter-object_contacts_display) for how the Inter object window looks and contact generation is displayed in graphics window.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0022.jpg' | relative_url }})

Inter object window and Objects with inter-object contacts display

Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to set primary die stroke stopping controls.

### Set Primary die stroke

Input stopping criteria that will stop the simulation when the tool has moved **6.25** ’’. Input 6.25 into the **Max****die****stroke**(**Y** direction) field as shown in [Fig. L1.23.](gear_blank_en_lab1.htm#Fig_L1_23_Primary_die_displacement_Max_die_stroke_stopping_controls)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0023.jpg' | relative_url }})

Primary die displacement (Max die stroke) stopping controls

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue with assigning Step controls.

### Assign Step controls

Select the ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) (Switch to expert mode) icon (from header tool bar) to access advanced simulation controls settings because remesh criteria should be defined for this simulation.

Observe the simulation title updated to "**upset** " as renamed in operation editor in Main tab. Go to the **Simulation****Steps** tab.

DEFORM uses a two-step process to establish the total punch movement distance:

On the **Simulation Steps** tab, the number of steps and save interval is defined. On the **Step****Increment** tab, the time or tool movement per time step is defined. If no other stopping controls are defined, total simulation length will be approximately the **step increment** * **number of steps**.

For this operation, the tool needs to move 6.25’’ to produce the desired shape. For a simple upset like this, 75 steps should be sufficient. Change the **Number of Simulation Steps** to **75**. Change the **Step Increment to Save** to **5** as shown in [Fig. L1.24.](gear_blank_en_lab1.htm#Fig_L1_24_Advanced_Step_controls_Simulations_steps_tab)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0024.jpg' | relative_url }})

Advanced Step controls Simulations steps tab

Next, go to **Step****Increment**. The die displacement value is the total distance you want the tool to travel (6.25’’) divided by the number of steps (75). Use the With Die Displacement option to define a die displacement of **0.083** ’’ (6.25 / 75) as shown in [Fig. L1.25.](gear_blank_si.htm#Fig_L1_25_Advanced_Step_controls_Step_increment_tab)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0025.jpg' | relative_url }})

Advanced Step controls Step increment tab

On the **Stop** tab, optional specific stopping control can be specified, which can be based on:

\- forming load on object 2 (the punch or moving die)

\- total movement of object 2

\- reaching a critical distance or measurement between points on two different tools.

Stopping controls reflect the **Primary die displacement** (Y direction) field 6.25’’ defined in stopping controls window earlier in guided mode.

Go to the **Remesh Criteria** Tab. The **Interference Depth** value should be half of a small element edge length. Measure the length of one of the smaller elements, divide by 2 and place the value in the interference depth field (See [Fig. L1.26.](gear_blank_en_lab1.htm#Fig_L1_26_Advanced_Step_controls_Remesh_criteria_tab)). You should get a number around 0.02’’. A remesh will be triggered if one of the tools is able to penetrate into the workpiece by a distance of 0.02’’.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0026.jpg' | relative_url }})

Advanced Step controls Remesh criteria tab

Now click on **Movement** under Top die in operation tree to check the top die movement preview because step and movement definition must be defined before previewing movement.

### Confirm Movement

Click on the ![]({{ '/assets/icons/pre_icons/mo_preview_icon.jpg' | relative_url }}) (Preview object movement) button in the lower right hand corner of the screen (See [Fig. L1.18.](gear_blank_en_lab1.htm#Fig_L1_18_Top_die_movement_controls_window)). Click on the ![]({{ '/assets/icons/pre_icons/mo_movement_play_button.jpg' | relative_url }}) (play) button (See [Fig. L1.27.](gear_blank_en_lab1.htm#Fig_L1_27_Top_die_movement_preview_window)) and watch the top die move through the workpiece. This tool will confirm that your tool is moving in the correct direction and that you have enough steps to complete the stroke.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0027.jpg' | relative_url }})

Top die movement preview window

Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to exit the menu and click on **Generate****DB** in the operation tree to go for DB generation.

### Data checking and database generation

Click on the ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) button as shown in [Fig. L1.28.](gear_blank_en_lab1.htm#Fig_L1_28_DB_generation_window) The data checking system will confirm that all of the data is appropriate for running a simulation.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0028.jpg' | relative_url }})

DB generation window

Red marks indicate missing or incorrect data that will prevent a simulation from running. It is necessary to correct the error before the database can be generated.

Yellow marks indicate data which may be suspect and should be reviewed. These should be investigated carefully, as they might result in system instability or erroneous (incorrect) results.

Review the data checking information. If there are no yellow or red marks, click the ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button.

You should look for the words: **Database has been generated**. When you see this you can be confident that your inputs have been saved to the database and you are now ready to run the simulation.

Click on the ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode button (above the operation tree) to start the simulation.

### Run and monitor a simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog. Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0029.jpg' | relative_url }})

Running the simulation from MO simulation mode

Simulation status update in simulation jobs, simulation and log messages can be observed from other tabs.

The graphics region will display Simulation graphics. In Simulation graphics you can observe the progress of a simulation as it is running, by default it updates the last saved step. To update the current step user has to select the right click option Monitoring Current step.

It is good practice to watch the first few steps of a simulation in simulation graphics mode to confirm that the tool movements and workpiece deformation are proceeding as expected.

Limited view controls are available in the simulation graphics view. In addition, the following zoom controls are available:

\- **ctrl** – **left****mouse** : window zoom

\- **alt** – **left****mouse** : dynamic zoom

\- **shift** – **left****mouse** : pan

User can also change the Hot keys under **Options![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Preferences ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Hot Key.**

These functions can be used to better view details of the workpiece as the simulation is running. When the simulation is completed, the image in the Simulation Graphics viewer will disappear. The message file (default view in main window) and log file will indicate that the simulation has been completed on the last line.

When the simulation is completed, click the ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode button to review results.

### Review results in Post Mode

The graphics window displays the results of the calculation.

The saved steps are listed in a step browser at the bottom of the graphics window as shown in [Fig. L1.30.](gear_blank_en_lab1.htm#Fig_L1_30_Step_browser_for_upset_operation)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0030.jpg' | relative_url }})

Step browser for upset operation

The play controls can be used to:

![]({{ '/assets/icons/pre_icons/mo_preview_play_button.jpg' | relative_url }}) **Play forward** : Displays the steps one by one until the last step is displayed from the current selected step.

![]({{ '/assets/icons/pre_icons/mo_preview_stop_button.jpg' | relative_url }}) **Stop** : Stops the playing (forward or backward) of steps.

**![]({{ '/assets/icons/pre_icons/mo_preview_one step_forward_button.jpg' | relative_url }})Single step forward** : Move to the next saved step in the step list.

![]({{ '/assets/icons/pre_icons/mo_preview_last_step_button.jpg' | relative_url }}) **Jump to the end** : Fast forward to the last saved step in the step list.

![]({{ '/assets/icons/pre_icons/mo_preview_play_back_button.jpg' | relative_url }}) **Play backward** : Displays the steps one by one in reverse order until the first step is displayed from the current selected step.

![]({{ '/assets/icons/pre_icons/mo_preview_one_step_back_button.jpg' | relative_url }}) **Single step backward** : Rewind the step list back to one saved step.

**![]({{ '/assets/icons/pre_icons/mo_preview_last_step_button.jpg' | relative_url }})Jump to the beginning** : Rewind the step list back to the first saved step.

**Play through the simulation.**

**Load – stroke plot**

Click the ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) (load-stroke) icon in the post tools. Plot the Y load vs. Stroke for the top die by selecting ![]({{ '/assets/icons/post_icons/mo_plot_button.jpg' | relative_url }}) button. The graph displays load at any point through the simulation (See [Fig. L1.31.](gear_blank_en_lab1.htm#Fig_L1_31_Velocity_vector_plot_with_Load_stroke_graph_for_top_die)). The vertical step tracer bar indicates the current step. Clicking at any point on the load stroke plot (or any graph in DEFORM) will display the results at that step. The graph may be hidden or removed by right clicking on the graph item at the bottom of the tree.

Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to exit from Load stroke window to plot the state variables.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0031.jpg' | relative_url }})

Velocity vector plot with Load stroke graph for top die

**State variable plots**

  * **Velocity plot**

Select step **75**(or any other intermediate step on the step selection bar). Click the ![]({{ '/assets/icons/post_icons/mo_vel_sv_icon.jpg' | relative_url }}) (Total Velocity) state variable icon in the **Post tools![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})** **State****Variables** short cuts. Click the ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) icon to open the state variable properties dialog. Select the Vector Plot display type and click ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) button to apply the changes. The instantaneous velocities are displayed as vectors at the selected time step. Colors are included to highlight the magnitude of the velocity. (See [Fig. L1.31.](gear_blank_en_lab1.htm#Fig_L1_31_Velocity_vector_plot_with_Load_stroke_graph_for_top_die))

  * **Effective strain plot**

Select **Strain![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Effective****** from state variable dialog ![]({{ '/assets/icons/post_icons/mo_deformation_icon.jpg' | relative_url }}) (Deformation) variables list. This represents the amount of deformation during the simulated process. In cold forming, this is related to work hardening.

Play through the simulation and watch how strain evolves as the part forms. The state variable scales to the maximum value anywhere in the simulation.

Select **Local** scaling and click ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). Play through the simulation. At each step, the state variables rescale to the maximum value at that step.

Select Solid display and click ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). The contour borders become sharp edges (See [Fig. L1.32.](gear_blank_en_lab1.htm#Fig_L1_32_Effective_strain_state_variable_contour_at_local,_global_scale)).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_blank/gear_blank_en/lab1_image0032.jpg' | relative_url }})

Effective strain state variable contour at local, global scale

When you are finished viewing results, click to exit from State variable window. The scale and plot type can also be changed from right click options on contour bar.

Click on ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}) mode button to switch to Pre mode to continue with the Next lab 2.

Click on [Lab 2. 2D to 3D Conversion to sequence 3D operation after 2D operation](/docs/en/labs/advanced_labs_in_mo/gear_blank/gear_blank_en_lab2/) to setup Lab6.

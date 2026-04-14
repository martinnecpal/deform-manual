---
lang: sk
title: "Forming Lab 1"
---

## 2D Gear Lab in Forming operation

### Creating a New problem

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear.

Create a new problem either by selecting **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in Fig. L1.1. Select " **Integrated Manufacturing Process** " radio button and Unit system as "**English** " using radio button. Define Problem Name as "**2DGear** " and make sure the “Show option dialog” check box is turned on (if we do not turn on the “**Show option dialog** ” check box, then we will not get the New Project dialog in MO UI). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

New Problem setup window

Multiple operation wizard will open, at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session we will use "**2DGear** " as the project name. Confirm that First operation check box is unchecked as we will add operation later and use the default (home) directory Location as shown in Fig. L1.2. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to add project. This lab will be referenced in future labs so it is important to use the name above.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0002.jpg' | relative_url }})

New MO project window

### Open Preprocessor

Add the**2D Forming operation** as first operation from **Explorer** tab as shown in Fig. L1.3.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0003.jpg' | relative_url }})

Adding 2D Forming operation from operation explorer

Change the default operation title to "**upset** " from Forming by selecting the title in the operation editor as shown in Fig. L1.4. and press **Enter** keyboard button.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0004.jpg' | relative_url }})

Renaming operation title to upset

### Select Geometry type and Simulation Modes

Confirm the geometry type selected is **Axi-symmetric** in Geometry type page, then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

In this lab we will be showing how to setup simple Isothermal problem, so in Simulation controls page, **uncheck** the **Heat****transfer****mode** check box (See Fig. L1.5.). then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0005.jpg' | relative_url }})

Simulation control window

### Add material from Library

Click the ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load material from library) button as shown in Fig. L1.6. Select the **Steel_at_Extended_Temperatures** category, then **AISI-8620[1550-2200F(850 -1200C)]** and click the ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}) button.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0006.jpg' | relative_url }})

Loading material from library

Material is loaded to material list, click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) for Material list window. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) for Material properties windows as we use the default properties available in database for this lab.

### Set number of Objects

The forging operation to be simulated requires a workpiece and a top and bottom die. Confirm that 3 objects are present in the table. If not, click the ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) (insert object) button three times to add 3 objects, Workpiece and two dies. Object window looks as shown in Fig. L1.7. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0007.jpg' | relative_url }})

Objects window to Add or Delete the objects

Before we proceed further, go to **Options**![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **Preferences** menu option and ensure that **Y- axis** is up is the preferred upward axis. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button.

_**Graphic Display Icons**_

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

Accept the default object name Workpiece. Assign the temperature as **2250** ° F and confirm the object type selected is **plastic**. (See Fig. L1.8.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0008.jpg' | relative_url }})

Workpiece object window

### Create workpiece geometry from primitive

Click on the ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) button to create a geometry within DEFORM. The workpiece diameter is 5.00”, so we will define a width of half the diameter or 2.50”. The length is 7.48”, with corner radii of 0.10”. Enter a **R******adi** us **of **2.50** in, a **Height** of **7.48** in, R1 & R2 of **0.1** (See Fig. L1.9.). Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button and then observe the geometry in graphics window.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0009.jpg' | relative_url }})

2D Axi-symmetric geometry primitive window

_**Display Manipulation**_

Functions that manipulate the DISPLAY window (such as Pan, Zoom, Magnify, and Rotate) can be activated using icons at the top of the Pre-processor window. These functions also have easy keyboard/mouse combination hotkeys that allow you to quickly perform these functions. Once you have read about these functions, feel free to use them to manipulate the view of the Billet in the DISPLAY window.

_**Display Icons**_

_**Icon**_ |  _**Function**_ |  _**Description**_  
---|---|---  
![]({{ '/assets/icons/pre_icons/mo_pan_icon.jpg' | relative_url }}) |  Pan |  The objects in the DISPLAY window can be dynamically panned up, down, left, or right by moving the mouse while holding the left mouse button. (Shortcut: Shift + Left Mouse Button)  
![]({{ '/assets/icons/pre_icons/mo_zoom_icon.jpg' | relative_url }}) |  Zoom |  The DISPLAY window can be dynamically zoomed in or out by holding the left mouse button and moving the mouse up or down. (Shortcut: Alt + Left Mouse Button)  
![]({{ '/assets/icons/pre_icons/mo_box_zoom_icon.jpg' | relative_url }}) |  Magnify |  A portion of the DISPLAY window can to be magnified by clicking and holding the left mouse button at one corner of the zoom box and dragging the cursor to create a window encompassing the zoom area. (Shortcut: Ctrl + Alt + Left Mouse Button)  
  
_**Point Selection**_

Point coordinates and distances between points can be obtained from the current display.

**_Point Selection Icons_**

_**Icon**_ |  _**Function**_ |  _**Description**_  
---|---|---  
![]({{ '/assets/icons/pre_icons/mo_measure_tool_icon.jpg' | relative_url }}) |  Measure |  Distances between any two points can be measured by clicking the first point and then clicking the second point. The measuring line will remain on the screen until the Refresh button is clicked.  
![]({{ '/assets/icons/pre_icons/mo_select_icon.jpg' | relative_url }}) |  Select |  This is the default display mode and is used to select and get information about nodes and element faces. This is also the mode to be used when measuring.  
  
Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button to generate workpiece mesh.

### Generating mesh for workpiece

Set the**target number of elements** as **2000** and click the ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button to generate the mesh for workpiece as shown in Fig. L1.10. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button to assign material for workpiece.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0010.jpg' | relative_url }})

Workpiece mesh window

### Assign Material to Workpiece

Click on the **AISI-8620[1550-2200F(850 -1200C)]** in the material window to assign the material to the workpiece as shown in Fig. L1.11.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0011.jpg' | relative_url }})

Object Material Assigning window

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button to assign the workpiece boundary conditions.

### Assign Workpiece boundary condition

By default, Velocity constraint **Vx=0** boundary conditions assigned along the centerline as the Geometry type selection is Axi-symmetric. Confirm that the velocity is set to zero and the X direction is selected by selecting the line “**X,****Fixed** ” that appears in the Boundary Conditions tree and observing the graphics window (See Fig. L1.12.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0012.jpg' | relative_url }})

Workpiece Boundary Conditions window

If this line is not present, boundary conditions have not been added. In such case use the edge tool ![]({{ '/assets/icons/pre_icons/mo_bcc_edge_icon.jpg' | relative_url }}) and then click on any node on the center line of the workpiece to select all the nodes on that edge, then click on ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) button to apply the settings.

Click on **Top****die** in operation tree as there is no Movement, Property and Initialize settings to vary for workpiece object.

### Defining Top die general object data

Define the Top die temperature as **300** °F and confirm the object type selected is **rigid** and selected as Primary die as shown in Fig. L1.13.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0013.jpg' | relative_url }})

Top die general window

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button to define the top die geometry.

### Import and edit the Top die geometry

Import the flat top die geometry from an igs file. Click the ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Load geometry from a file) button and ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}) open (import) the file “**flat top die.****igs** ”, by browsing the geometry file path. The geometry for top die is located in DEFORM installation folder \Tutorials directory.

It is always good practice to check the geometry to make sure that it is legal. 

Click on the ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) button to open the Check and Correct Geometry dialog. Change the Geometry open/close/auto type to open and click the ![]({{ '/assets/icons/pre_icons/mo_check_and_correct_geo_button.jpg' | relative_url }}) button. You should receive a message that the geometry is legal as shown in Fig. L1.14. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to exit the menu.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0014.jpg' | relative_url }})

Check and correct geometry window for top die geometry

The geometry checking tool should be used on every 2D geometry you bring into DEFORM, even if the geometry looks legal.

Since this is an isothermal simulation, there is no need to generate mesh or assign material for the Top Die, Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top die movement page.

### Assign Top die movement

The default mode is constant **speed**. Input a value of **3** in/sec for the Constant value and confirm that the Direction is **-Y** as shown in Fig. L1.15. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Bottom die page.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0015.jpg' | relative_url }})

Top die movement controls window

### Defining Bottom die general object data

Define the Bottom die temperature as **300** ° F and confirm its object type is **rigid**. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button to define the bottom die geometry page.

### Creating bottom die geometry from geometry editor

Click on the ![]({{ '/assets/icons/pre_icons/mo_xyr_button.jpg' | relative_url }}) button to define the bottom die geometry from geometry editor. Make sure XYR format is selected in geometry table. To define the geometry, enter the geometry points in table as shown in Fig. L1.16.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0016.jpg' | relative_url }})

Bottom die geometry table with geometry

These points will trace out the geometry in a counter clockwise fashion, click on the ![]({{ '/assets/icons/pre_icons/mo_show_inside.jpg' | relative_url }}) (Show inside) icon to ensure that the geometry orientation is on the inside of the geometry as shown in Fig. L1.16. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the geometry definition and click on the **Positioning** in operation tree to open the objects positioning window.

### Position

Use the ![]({{ '/assets/icons/pre_icons/mo_automatic_positioning_button.jpg' | relative_url }}) button to position the tools in contact with the workpiece (in the vertical forming direction). Confirm that the Workpiece is positioned on top of the Bottom Die and that the Top Die is positioned against the Workpiece as shown in Fig. L1.17.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0017.jpg' | relative_url }})

Correct objects positioning

Click on the **Contact** in operation tree to open the Inter-Object window, as there is no need of Scheduled positioning for this operation.

### Contact ( Inter-Object Relationship ) page

DEFORM will automatically create default Master-Slave relationships, using ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) button create three relationships as shown in Fig. L1.18. DEFORM will create three relationships. Two where each tool is the master and the workpiece is the slave. The third relationship will be a (Workpiece – Workpiece) relationship. This relationship will allow self contact of the workpiece if a fold develops.

Click on the ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) button for one of the relationships. Under the **Friction![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Value** box, use the Constant drop down menu to select **Hot****forging**(lubricated) **0.3**. If user have experience that suggests that a different friction value would give better results for user's process, then user can enter that value directly in this field. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to exit the menu. Click ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) to apply the friction value to the two other relationships.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0018.jpg' | relative_url }})

Contact window and Objects with inter-object contacts display

Next, contact among the objects needs to be generated. Click the Default contact tolerance ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) button to calculate a tolerance for contact generation. Click ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) to generate the contact. You should see the contact nodes on the workpiece where contact has been generated.

This initial contact provides a starting condition for the finite element solver. After the simulation starts, contact is automatically updated.

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to set primary die stroke stopping controls.

### Assign Stopping controls

We need to add a stopping criteria that will stop the simulation when the tool has moved 6 in. Check **Max****die****stroke** check box and enter **6** (Y direction) as shown in Fig. L1.19.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0019.jpg' | relative_url }})

Stopping controls window

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue with assigning Step controls.

### Assign Step controls

Select the ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) (Switch to expert mode) icon (from header tool bar) to access advanced simulation controls settings because remesh criteria should be defined for this simulation.

Observe the simulation title updated to "upset" as renamed in operation editor in Main tab. Go to the **Simulation****Steps** tab.

DEFORM uses a two-step process to establish the total punch movement distance:

On the **Simulation****Steps** tab, the number of steps and save interval is defined. On the Step Increment tab, the time or tool movement per time step is defined. If no other stopping controls are defined, total simulation length will be approximately the step increment * number of steps.

For this operation, the tool needs to move 6.0’’ to produce the desired shape. For a simple upset like this, 100 steps should be sufficient. Change the **Number of Simulation Steps** to **100**. Change the **Step****Increment****to****Save** to **5** as shown in Fig. L1.20.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0020.jpg' | relative_url }})

Advanced Step controls Simulations steps tab

Next, go to **Step****Increment**. The die displacement value is the total distance you want the tool to travel (6.0’’) divided by the number of steps (100). Use the With Die Displacement option to define a **die****displacement** of **0.06** ’’ (6.0 / 100) as shown in Fig. L1.21.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0021.jpg' | relative_url }})

Advanced Step controls Step increment tab

Go to the **Remesh****Criteria** Tab. The Interference Depth value should be half of a small element edge length. Measure the length of one of the smaller elements, divide by 2 and place the value in the interference depth field (See Fig. L1.22.). You should get a number around 0.02’’. A remesh will be triggered if one of the tools is able to penetrate the workpiece by a distance of **0.02** ’’.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0022.jpg' | relative_url }})

Advanced Step controls Remesh criteria tab

Now click on **Movement** under Top die in operation tree to check the top die movement preview because step and movement definition must be defined before previewing movement.

### Confirm Movement

Click on the ![]({{ '/assets/icons/pre_icons/mo_preview_icon.jpg' | relative_url }}) (Preview object movement) button in the lower right hand corner of the screen (See Fig. L1.15.). Click on the ![]({{ '/assets/icons/pre_icons/mo_movement_play_button.jpg' | relative_url }}) (play) button (See Fig. L1.23.) and watch the top die move through the workpiece. This tool will confirm that your tool is moving in the correct direction and that you have enough steps to complete the stroke.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0023.jpg' | relative_url }})

Top die movement preview window

Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to exit the menu and click on **Generate****DB** in the operation tree to go for DB generation.

### Data checking and database generation

Click on the ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) button . DEFORM will check all the inputs and verify that all necessary data is defined. The following message should be shown in the Message window.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/image0001.jpg' | relative_url }})

Red marks indicate missing or incorrect data that will prevent a simulation from running. It is necessary to correct the error before the database can be generated.

Yellow marks indicate data which may be suspect and should be reviewed. These should be investigated carefully, as they might result in system instability or erroneous (incorrect) results.

Review the data checking information. If there are no errors, click the ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button.

You should look for the following message in the Message window.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/image0002.jpg' | relative_url }})

When you see this message, it indicates that the simulation setup has been saved to the database and the simulation is ready to be run.

Click on the MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode button (above the operation tree) to start the simulation.

### Run and monitor a simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog. Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0024.jpg' | relative_url }})

Running the simulation from MO simulation mode

In the upper-right, the Status field updates to let you know that the simulation is currently running on a particular computer. (See Fig. L1.24.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/image0003.jpg' | relative_url }})

The Simulation Message and Simulation Log tabs in the lower-right to give you information on how the simulation is running.

The progress of a simulation can be observed in the graphics window as it is running. By default, the graphics update when a new step is saved to the database. 

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/image0004.jpg' | relative_url }})

To have the graphics update more frequently, you can use the Update pull-down menu (bottom right of graphics window) to change the setting to Current Step. This is typically not needed in 2D simulations since they run so fast.

It is good practice to watch the first few steps of a simulation in simulation graphics mode to confirm that the tool movements and workpiece deformation are proceeding as expected.

When the simulation is completed, the image in the graphics window will stop changing and the final deformed shape of the part will be shown. The last lines of the Simulation Message tab will indicate that the simulation has been completed.

"PROGRAM STOPPED!

THE STROKE -6.0000000 HAS EXCEEDED THE SPECIFIED LIMIT 6.0000000 "

### Review results in Post Mode

When the simulation is completed, click the MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode button to review results.

### Step list and play controls

The graphics window displays the results of the simulation. The saved steps are listed in a step browser at the bottom of the graphics window.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0025.jpg' | relative_url }})

Step browser for upset operation

The play controls can be used to:

![]({{ '/assets/icons/pre_icons/mo_preview_play_button.jpg' | relative_url }}) **Play forward** : Displays the steps one by one until the last step is displayed from the current selected step.

![]({{ '/assets/icons/pre_icons/mo_preview_stop_button.jpg' | relative_url }}) **Stop** : Stops the playing (forward or backward) of steps.

**![]({{ '/assets/icons/pre_icons/mo_preview_one step_forward_button.jpg' | relative_url }})Single step forward** : Move to the next saved step in the step list.

![]({{ '/assets/icons/pre_icons/mo_preview_last_step_button.jpg' | relative_url }}) **Jump to the end** : Fast forward to the last saved step in the step list.

![]({{ '/assets/icons/pre_icons/mo_preview_play_back_button.jpg' | relative_url }}) **Play backward** : Displays the steps one by one in reverse order until the first step is displayed from the current selected step.

![]({{ '/assets/icons/pre_icons/mo_preview_one_step_back_button.jpg' | relative_url }}) **Single step backward** : Rewind the step list back to one saved step.

**![]({{ '/assets/icons/pre_icons/mo_preview_last_step_button.jpg' | relative_url }})Jump to the beginning** : Rewind the step list back to the first saved step.

**Load – stroke plot**

Click the ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) (load-stroke) icon in the post tools. Plot the **Y****load**(Y-Axis) vs. **Stroke**(X-Axis) for the top die by selecting ![]({{ '/assets/icons/post_icons/mo_plot_button.jpg' | relative_url }}) button (See Fig. L1.26.). The graph displays the load throughout the simulation. The vertical step tracer bar indicates the current step.

Clicking at any point on the load-stroke plot (or any graph in DEFORM) will display the results at that step. Alternatively, any step in the step list can be selected and the vertical step tracer will jump to that point in the simulation. The graph may be removed by right-clicking on the graph and selecting **Delete**.

Note: By default, graphs open in the same graphics window as the simulation. To achieve a similar look as the image below, go to **Options** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **Preference** and under Graph Display check the box next to New window then hit ![]({{ '/assets/icons/pre_icons/mo_apply_button2.jpg' | relative_url }}). Replot the graph to see the changes.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0026.jpg' | relative_url }})

Load stroke graph for top die

**State variable plots**

  * **Velocity plot**

Select step **75**(or any other intermediate step on the step selection bar). Click the ![]({{ '/assets/icons/post_icons/mo_vel_sv_icon.jpg' | relative_url }}) (Total Velocity) state variable icon in the Post tools State Variables. Click the ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) icon to open the state variable properties dialog. Select the ![]({{ '/assets/icons/post_icons/mo_vector_plot_button.jpg' | relative_url }}) display type. The instantaneous velocities are displayed as vectors at the selected time step. The colors of the arrows denote the magnitude of the velocity. (See Fig. L1.27.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0027.jpg' | relative_url }})

Velocity vector plot with Load stroke graph for top die

  * **Effective strain plot**

In the State Variable dialog, select **Strain**![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **Effective**. Set the **Scaling** to **Global** and click ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). Effective strain represents the amount of deformation during the simulated process. In cold forming, this is related to work hardening.

Play through the simulation and watch how strain evolves as the part forms. With Global scaling, the color bar represents the maximum range of the variable anywhere in the workpiece.

Set the Scaling to **Local** and click ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). Play through the simulation. At each step, the state variables rescale to the maximum value at that step.

Select ![]({{ '/assets/icons/post_icons/mo_solid_plot_button.jpg' | relative_url }}) display and click ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). The contour borders become sharp edges (See Fig. L1.28.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0028.jpg' | relative_url }})

Effective strain state variable contour at local, global scale

When you are finished viewing results, click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to exit from State variable window. The scale and plot type can also be changed from right click options on contour bar.

Click on ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}) MO mode button to switch to Pre mode to continue with the Next lab.

### Add second operation

We will add a finish forging operation to the pancaked part. From the **Explorer** tab on the left side of the user interface, go to **Forming![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Single** and then click the ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button next to**[2D] Forming**. (See Fig. L1.29.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0029.jpg' | relative_url }})

Explorer window

A new operation tile will be added in the Operation Editor. (See Fig. L1.30.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0030.jpg' | relative_url }})

Operations list in Operation Editor window

Click on the **Forming** tile. You will get a pop-up window asking you to select **Interactive** or **Batch** setup. Interactive setup allows more direct control over inputs. However, Batch setup ensures that it will be possible to back up and rerun the full project from the beginning without interruption. _For almost all projects_ , _Batch setup gives greater flexibility_. 

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0031.jpg' | relative_url }})

Setup type popup for 2D Forming operation

Click ![]({{ '/assets/icons/pre_icons/mo_no_batch_setup_button.jpg' | relative_url }}) in this dialog. The 2nd operation will open in the process tree. Notice how the objects in the 1st operation are now linked to the 2nd operation and are shown as Read from DB. All the objects appear red in the 2nd operation, indicating that they are being read from the previous operation in the database.

New dies will be imported for this operation, so dies really won’t be Read from DB like the Workpiece. This is easy to change. When importing the dies below, remember that the geometries are in the DEFORM installation folder \Tutorials directory.

#### Assign Simulation controls

In Simulation controls, **uncheck** the **Heat****Transfer** box. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top die page.

#### Defining Top die general object data

Select **Rigid** type Object, define the Top die temperature as **300°** F and select as Primary die. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Top die geometry page.

#### Define Top die geometry

Import the geometry “**gear top die.****IGS** ”. Click the ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load geometry from a file) button and open (import) the file “gear top die.IGS”. The geometry for billet is located in DEFORM installation folder \Tutorials directory. Use ![]({{ '/assets/icons/pre_icons/mo_check_and_correct_geo_button.jpg' | relative_url }}) to check the geometry and fix the shading so that it is correctly on the inside of the part. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top die Movement page.

#### Assign Top die movement

Make sure the speed is set to **3** in/sec. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Properties page.

#### Define Top die properties

Later in this setup, we will define a stopping criteria based on the spacing of the dies at the flash gap. To define this, we need to define reference points under Property. Go to Reference and use the mouse to pick the bump in the top die corresponding to the flash land, as shown in the Fig. L1.32. (your cursor has to be in Select ![]({{ '/assets/icons/pre_icons/mo_select_icon.jpg' | relative_url }}) mode for this to work).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0032.jpg' | relative_url }})

Reference point on Top die

#### Defining Bottom die general object data

Select **Rigid** type Object, define the Bottom die temperature as **300** ° F. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Bottom die geometry page.

#### Define Bottom die geometry

Import the geometry “**gear bottom die.****IGS** ”. Click the ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Load geometry from a file) button and ![]({{ '/assets/icons/pre_icons/mo_open_button.jpg' | relative_url }}) (import) the file “gear bottom die.IGS”. The geometry for billet is located in DEFORM installation folder \Tutorials directory. Use ![]({{ '/assets/icons/pre_icons/mo_check_and_correct_geo_button.jpg' | relative_url }}) to check the geometry and fix the shading so that it is correctly on the inside of the part. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Bottom die Properties page.

####  Define Bottom die properties

Go to **Reference** and use the mouse to pick and select the point on the bottom die flash land, as shown in the Fig. L1.33. (your cursor has to be in Select ![]({{ '/assets/icons/pre_icons/mo_select_icon.jpg' | relative_url }}) mode for this to work). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Scheduled positioning page.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0033.jpg' | relative_url }})

Reference point selection on Bottom die

#### Scheduled positioning

Because the workpiece is being read from the database after an earlier forming operation, the size and shape may change if the project is rerun from the beginning. For this reason, it is better to allow a flexible positioning of the tools relative to the workpiece, rather than setting a firm position for them.

In DEFORM, there is an option called **Scheduled positioning** which allows the tools to be moved into contact with an arbitrary workpiece shape whenever the workpiece is imported from a prior operation.

Go to **Scheduled****positioning** in the Process Tree and click the ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button to add a positioning operation. 

First, we will schedule the bottom die to move up to the workpiece. Select **Interference** and pick the **Bottom****Die** as the **positioning****object** , and the **Workpiece** as the **Reference****object**. Select the approach direction as **Y** (up). Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). 

Note that the tool does not move at this time, but positioning will be performed when the database is generated for this operation.

Click ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) again to schedule a 2nd positioning. Select **Interference** and position the **Top****Die** down (**-Y**) to the **Workpiece**. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). (See Fig. L1.34.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define contact relation.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0034.jpg' | relative_url }})

Scheduled positioning window

#### Contact (Inter- Object relation) data

Assign the default inter-object relationships using ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) button. The workpiece should be slave to both the top and bottom die. For 3D simulations, self-contact (workpiece master to itself) is generally not used because it can significantly increase simulation time. Other tools are available to track folding. These will be discussed in a later lab.

Click on the ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) button for one of the relationships. Under the **Friction![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****Value****** box, use the Constant drop down menu to select **Hot forging (lubricated)****0.3**. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to exit the menu. Click ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) to apply the friction value to the two other relationships. As the object workpiece added in relation is read from DB object inter-object can not be generated now as in lab1, so confirm that Scheduled **Initialize** and **Generate****contact****check****boxes** are **checked**. this will initialize previous contacts and generate new contacts while running the simulation. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Stopping controls page.

#### Assigning Stopping controls in Expert mode

Rather than measuring the tool movement distance as we did in the first operation, we will stop this process with a fixed distance between tools. In this case we will set the flash thickness to 0.2 in.

The flash distance is measured at the reference points defined on the top and bottom dies.

Click on Stopping controls in the Operation Tree. First, verify that the **Primary****die****displacement** stopping control is set back to **0**. Next, select the **Die****Distance****tab** and set the Reference 1 object to the **Top****Die** and the Reference 2**** object as the **Bottom****Die**. Set the Method to**Y- Distance** and the distance to **0.2** in (See Fig. L1.35.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Step controls page.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0035.jpg' | relative_url }})

Expert mode Stopping controls - Die distance window

#### Assign Step Controls

We want to travel about 1.5 in. in 100 steps, so we will use a **step****increment** of **0.015** in/step. HOWEVER, we do not want the simulation to run out of steps since there is another stopping criteria (die distance) set. Since we want to have flexibility when rerunning this case, we will set the **number****of****simulation****steps** to **1000** , not 100. This will ensure that if we rerun the project with different settings, we will not need to worry about running out of steps. The stopping will always be controlled by the distance between the tools.

Change the **Number of steps** to **1000** , and set the **Step increment** to **5**.

Go to **Step****increment** and select **Die****displacement** per step. Set the Step increment control to **0.015** in/step. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Generate DB page.

#### Generate DB

The system will pause briefly as it executes the scheduled positioning and contact generation. The workpiece color turns from red (Read from DB) to yellow (Plastic object).

Click ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}).

Click on the MO![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode button (above the operation tree) to start the simulation.

#### Run and monitor a simulation

Click the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) button and then uncheck submit job to the simulation queue. Unchecking this option will make the job run on the local computer. Use the default **Start from last negative step** option. Click the ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to start the simulation.

#### Review the results

When the simulation is completed, click the MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode button to review results.

Play through all steps. Note that the part does not completely fill out the die cavity (See Fig. L1.36.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/lab1_image0036.jpg' | relative_url }})

Workpiece shape at last step of second operation

To rerun using a larger billet size, we will create a new project based on the existing project. Please refer [Lab 2. Rerun Sequence with a Larger Bille](/docs/sk/labs/advanced_labs_in_mo/gear_labs/forming_gear_labs/forming_lab2/)t

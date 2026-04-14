---
lang: sk
title: "Forming Express Lab1"
---

# Lab 1. 2D Gear Lab

### Creating a New problem

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear.

Create a new problem either by selecting **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in Fig. L1.1. Select " **Integrated Manufacturing Process** " radio button and Unit system as "**English** " using radio button. Define Problem Name as "**FE_Gear** " and make sure the “Show option dialog” check box is turned on (if we do not turn on the “**Show option dialog** ” check box, then we will not get the New Project dialog in MO UI). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

Problem setup window

MO GUI opens along with New Project window, specify the project name as **FE_Gear** and confirm that **First****operation** check box is **checked** and select the **[2D] Forming Express** operation from the list and use the default (home) directory Location as shown in Fig. L1.2. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to add project. This lab will be referenced in future labs, so it is important to use the name above.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0002.jpg' | relative_url }})

New MO Project window

### Open Preprocessor

Change the default operation name from Forming to "**Upset** " by double-clicking the title in the operation tile. The mouse scroll wheel can be used to zoom in on this operation tile if needed. Press **Enter** to accept the new name.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0003.jpg' | relative_url }})

Changing operation name to Upset

### Process type

Confirm that the Geometry type is **2D Axisymmetric** and Set the Process type to **Hot****forging**.

Forming Express operations use Complexity and Accuracy slider bars to establish meshing and time step parameters for the simulation. As Complexity and Accuracy are set higher, more elements and smaller time steps will be used in the analysis.

Generally, there is a trade-off between resolution and run time. Setting the slider bars all the way to the left (Simple/Fast) will yield faster run times, but there is an increased likelihood of missing important geometry details or defects due to the larger elements.

For this lab, leave the **Complexity** slider at **Moderate** and change the **Accuracy** slide to **Fast** as shown in Fig. L1.4. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0004.jpg' | relative_url }})

Process window

### Thermal Calculation

For this first lab, we will ignore temperature changes that occur during forming, so set the Temperature Calculation to **Constant temperature (Isothermal)**. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Set number of objects

The forging operation to be simulated requires a workpiece and a top and bottom die. So, we will have **1 workpiece + 2 dies**. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Define Workpiece General Object Data

Accept the default object name Workpiece and the temperature of **2******2** 50**°F. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). 

**Note:** The ![]({{ '/assets/icons/pre_icons/mo_import_object.._button.jpg' | relative_url }}) button is for importing data from a different DEFORM problem keyword or database. In most cases, you will use the Import Geometry ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) option on the next page.

### Create workpiece geometry from primitive

Click on the ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) button to create a geometry within DEFORM. The workpiece being modeled has a diameter of 5 in. and a height of 7.48 in., with corner radii of **0.1** in. Axisymmetric simulations model a radial slice of the part, so select **Cylinder** set the Radius to **2.5** in., the **Height** to **7.48** in., and R1 & R2 to **0.1** in (See Fig. L1.5.). Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to accept these part dimensions.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0005.jpg' | relative_url }})

Workpiece geometry Primitive window

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

**Point Selection Icons**

_**Icon**_ |  _**Function**_ |  _**Description**_  
---|---|---  
![]({{ '/assets/icons/pre_icons/mo_measure_tool_icon.jpg' | relative_url }}) |  Measure |  Distances between any two points can be measured by clicking the first point and then clicking the second point. The measuring line will remain on the screen until the Refresh button is clicked.  
![]({{ '/assets/icons/pre_icons/mo_select_icon.jpg' | relative_url }}) |  Select |  This is the default display mode and is used to select and get information about nodes and element faces. This is also the mode to be used when measuring.  
  
Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button to generate workpiece mesh.

### Generate Workpiece Mesh page

The default target number of elements is **2000** for the current slider bar settings. This value is grayed out since the mesh is set to System. Users can change this value or have access to some advanced meshing options using User-defined method. Accept this **System** setting and click the ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button to generate the workpiece mesh. Generated mesh for workpiece is as shown in Fig. L1.6.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0006.jpg' | relative_url }})

Workpiece Mesh window

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
  
Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button to assign material for workpiece.

### Assign Workpiece material

Click the (Load material from library) ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) icon and browse to the **Steel** category. Scroll to find **AISI-8620[1550-2200F(850 -1200C)]** in the material list and click ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}) to assign the material to the workpiece. Users can view or modify the material data using the ![]({{ '/assets/icons/pre_icons/mo_material_edit_button.jpg' | relative_url }}) button. For this lab, no changes are needed so click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to the boundary conditions page.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0007.jpg' | relative_url }})

Material Library window

### Verify Workpiece boundary conditions

Since the geometry type is Axisymmetric, a velocity boundary condition of X, Fixed was automatically assigned along the centerline of the workpiece. Click the "**X, Fixed** " in the boundary condition tree to observe which nodes are being constrained not to move in the X direction. (See Fig. L1.8.)

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0008.jpg' | relative_url }})

Workpiece BCC window

If a user needs to add additional boundary conditions, they can highlight Velocity in the boundary condition tree and then use the tools along the left edge of the screen ![]({{ '/assets/icons/pre_icons/mo_2d_picking_option.jpg' | relative_url }}) to select to appropriate nodes to constrain.

For this lab, we only want the default "X, Fixed" boundary condition on the centerline, so click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to start defining the Top Die.

### Top Die general object data

The Temperature should be set to **300** °F and the Object type will be **Rigid** as shown in Fig. L1.9. These are the defaults for a die, and we will use these settings. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to the Top Die geometry page.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0009.jpg' | relative_url }})

Top die general window

### Import and edit the Top Die geometry

Import the flat top die geometry from an igs file. Click the ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Load geometry from a file) button and ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}) open (import) the file “**flat top die.****igs** ”. The geometry for top die is located in DEFORM installation folder \Tutorials directory.

Note: Make sure you don’t choose FlatTopDieSI.igs.

It is always good practice to check the geometry to make sure that it is legal. 

Click on the ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) button to open the Check and Correct Geometry menu. Change the Geometry open/close/auto type to open and click the ![]({{ '/assets/icons/pre_icons/mo_check_and_correct_geo_button.jpg' | relative_url }}) button. You should receive a message that the geometry is legal as shown in Fig. L1.10. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to exit the menu.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0010.jpg' | relative_url }})

Check and correct geometry window for top die geometry

The geometry checking tool should be used on every 2D geometry you bring into DEFORM, even if the geometry looks legal.

Since this is an isothermal simulation, there is no need to generate mesh or assign material for the Top Die. Therefore these options are not shown in the Operation Tree, Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Top die movement page.

### Assign Top Die movement

This lab will use a constant speed for the Top Die. Verify that Speed is selected and the direction is set to **–Y**. Define the speed as **3** **in** /sec as shown in Fig. L1.11. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to the Bottom Die.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0011.jpg' | relative_url }})

Top die movement window

### Bottom Die general data

The Temperature should be set to **300** °F and the Object type will be **Rigid**. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to geometry page.

### Bottom die Geometry page

Click on the![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) button to define the bottom die geometry from geometry editor. Make sure XYR format is selected in geometry table. To define the geometry, enter the geometry points in table form as shown in Fig. L1.12.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0012.jpg' | relative_url }})

Bottom die Edit geometry window

These points will trace out the geometry in a counter clockwise fashion to ensure that the geometry orientation is on the inside of the geometry as shown in Fig. L1.12. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the geometry definition and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Positioning page.

### Positioning

Use the ![]({{ '/assets/icons/pre_icons/mo_automatic_positioning_button.jpg' | relative_url }}) button to position the tools in contact with the workpiece (in the vertical forming direction). Confirm that the Workpiece is positioned on top of the Bottom Die and that the Top Die is positioned against the Workpiece as shown in Fig. L1.13. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to the contact page.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0013.jpg' | relative_url }})

After positioning the objects using Automatic position option

### Inter-object relationships – friction and contact generation

DEFORM will automatically create inter-object relationships between the workpiece and the dies. The friction settings are set automatically based on the **Process****type** defined at the top of the Process Tree. Since we defined this simulation as **Hot****forging** , the friction coefficient was set to a **System** -**defined** value of**0.3****Shear** as shown in Fig. L1.14.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0014.jpg' | relative_url }})

Contact window

If needed, users can switch to User-defined to define different friction values. Next, contact among the objects needs to be generated. Use the default System-defined contact tolerance and click ![]({{ '/assets/icons/pre_icons/mo_generate_contact_nodes_label.jpg' | relative_url }}). You should see contact highlighted on the nodes on the workpiece where contact has been generated. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Stopping controls page.

### Define Primary die stroke

The Primary die stroke field is an estimate of the total movement of the top die during the forming process. Total primary die stroke is used to establish time step size and other controls. If the exact travel is not known, a best guess value should be used. In this case, the Top Die will travel exactly 6 in. Set the **Total****primary****die****travel** to be **6** in. and check the**Exact Amount** box as shown in Fig. L1.15. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Primary die stroke.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0015.jpg' | relative_url }})

Primary die travel window

### Assign Stopping controls

The Stopping controls dialog sets the exact criteria used for stopping the simulation. For this operation, stop the analysis when the **Max****die****stroke** has **reached****6** in. Check **Max die stroke** check box and enter the value as **6** in as shown in Fig. L1.16. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to simulation controls page.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0016.jpg' | relative_url }})

Stopping controls window

### Assign Simulation controls

For this operation, the tool needs to move 6 in. to produce the desired shape. For a simple upset like this, a**Number of steps** of approximately **100** steps should be sufficient. This is the default value of steps for the slider settings defined in this problem.

Change the **Step Increment** to **5**. This means that every fifth step of the simulation will be saved to the database, and results at these steps will be visible in the Post-processor.

Note that if another stopping method is used, as it is in this case, the number of steps does not need to be precise.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0017.jpg' | relative_url }})

Simulation controls window

### Confirm Movement

Click on **Movement** under Top Die in operation tree to preview movement. Click on the ![]({{ '/assets/icons/pre_icons/mo_preview_icon.jpg' | relative_url }}) (Preview object movement) button in the lower right hand corner of the screen (See Fig. L1.11.). Click on the ![]({{ '/assets/icons/pre_icons/mo_movement_play_button.jpg' | relative_url }}) (play) button (See Fig. L1.18.) and watch the top die move through the workpiece. This tool will confirm that your tool is moving in the correct direction and that you have enough steps to complete the stroke.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0018.jpg' | relative_url }})

Top die movement preview window

Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to exit the menu and click on **Generate****DB** in the operation tree to go for DB generation.

### Data checking and database generation

Click on the ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) button. DEFORM will check all the inputs and verify that all necessary data is defined. The following messages should be shown in the Message window.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/image0001.jpg' | relative_url }})

Red marks indicate missing or incorrect data that will prevent a simulation from running. It is necessary to correct the error before the database can be generated.

Yellow marks indicate data which may be suspect and should be reviewed. These should be investigated carefully, as they might result in system instability or erroneous (incorrect) results.

Review the data checking information. If there are no yellow or red marks, click the ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button.

You should look for the following messages in the Message window.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/image0002.jpg' | relative_url }})

When you see this message, the simulation setup has been saved to the database and the simulation is ready to be run.

Click on the MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode button (above the operation tree) to start the simulation.

### Run and monitor a simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog. Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation. (See Fig. L1.19.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0019.jpg' | relative_url }})

Running the simulation from MO simulation mode

In the upper-right, the Status field updates to let you know that the simulation is currently running on a particular computer.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/image0003.jpg' | relative_url }})

The Simulation Message and Simulation Log tabs in the lower-right will give you information on how the simulation is running.

The progress of a simulation can be observed in the graphics window as it is running. By default, the graphics update when a new step is saved to the database. 

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/image0004.jpg' | relative_url }})

To have the graphics update more frequently, you can use the Update pull-down menu (bottom right of graphics window) to change the setting to Current Step. This is typically not needed in 2D simulations since they run so fast.

It is good practice to watch the first few steps of a simulation in simulation graphics mode to confirm that the tool movements and workpiece deformation are proceeding as expected.

When the simulation is completed, the image in the graphics window will stop changing and the final deformed shape of the part will be shown. The last lines of the **Simulation Message** tab will indicate that the simulation has been completed.

"******Message*******

Simulation is completed and stopped at the user specified time step ".

### Review results in Post Mode

When the simulation is completed, click the MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode button to review results.

### Step list and play controls

The graphics window displays the results of the simulation. The saved steps are listed in a step browser at the bottom of the graphics window as shown in Fig. L1.20.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0020.jpg' | relative_url }})

Step browser for upset operation

The play controls can be used to:

![]({{ '/assets/icons/pre_icons/mo_preview_play_button.jpg' | relative_url }}) **Play forward** : Displays the steps one by one until the last step is displayed from the current selected step.

![]({{ '/assets/icons/pre_icons/mo_preview_stop_button.jpg' | relative_url }}) **Stop** : Stops the playing (forward or backward) of steps.

**![]({{ '/assets/icons/pre_icons/mo_preview_one step_forward_button.jpg' | relative_url }})Single step forward** : Move to the next saved step in the step list.

![]({{ '/assets/icons/pre_icons/mo_preview_last_step_button.jpg' | relative_url }}) **Jump to the end** : Fast forward to the last saved step in the step list.

![]({{ '/assets/icons/pre_icons/mo_preview_play_back_button.jpg' | relative_url }}) **Play backward** : Displays the steps one by one in reverse order until the first step is displayed from the current selected step.

![]({{ '/assets/icons/pre_icons/mo_preview_one_step_back_button.jpg' | relative_url }}) **Single step backward** : Rewind the step list back to one saved step.

**![]({{ '/assets/icons/pre_icons/mo_preview_last_step_button.jpg' | relative_url }})Jump to the beginning** : Rewind the step list back to the first saved step.

_**Load – stroke plot**_

Click the ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) (load-stroke) icon in the post tools. Plot the Y load (Y-Axis) vs. Stroke (X-Axis) for the top die by selecting ![]({{ '/assets/icons/post_icons/mo_plot_button.jpg' | relative_url }}) button (See Fig. L1.21.). The graph displays the load throughout the simulation. The vertical step tracer bar indicates the current step.

Clicking at any point on the load-stroke plot (or any graph in DEFORM) will display the results at that step. Alternatively, any step in the step list can be selected and the vertical step tracer will jump to that point in the simulation. The graph may be removed by right-clicking on the graph and selecting **Delete**.

Note: By default, graphs open in the same graphics window as the simulation. To achieve a similar look as the image below, go to Options ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Preference and under Graph Display check the box next to New window then hit . Replot the graph to see the changes.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0021.jpg' | relative_url }})

Load stroke graph for top die

_**State variable plots**_

  * **Velocity plot**

Select step 75 (or any other intermediate step on the step selection bar). Click the ![]({{ '/assets/icons/post_icons/mo_vel_sv_icon.jpg' | relative_url }}) (Total Velocity) state variable icon in the Post tools State Variables. Click the ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) icon to open the state variable properties dialog. Select the ![]({{ '/assets/icons/post_icons/mo_vector_plot_button.jpg' | relative_url }}) display type. The instantaneous velocities are displayed as vectors at the selected time step. The colors of the arrows denote the magnitude of the velocity. (See Fig. L1.22.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0022.jpg' | relative_url }})

Velocity vector plot with Load stroke graph for top die

  * **Effective strain plot**

In the State Variable dialog, select **Strain**![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **Effective**. Set the Scaling to **Global** and click ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). Effective strain represents the amount of deformation during the simulated process. In cold forming, this is related to work hardening.

Play through the simulation and watch how strain evolves as the part forms. With **Global** scaling, the color bar represents the maximum range of the variable anywhere in the workpiece.

Set the Scaling to **Local** and click ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). Play through the simulation. At each step, the state variables rescale to the maximum value at that step.

Select ![]({{ '/assets/icons/post_icons/mo_solid_plot_button.jpg' | relative_url }}) display and click ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). The contour borders become sharp edges (See Fig. L1.23.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0023.jpg' | relative_url }})

Effective strain state variable contour at local, global scale

When you are finished viewing results, click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to exit from State variable window. The scale and plot type can also be changed from right click options on contour bar.

Click on ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}) MO mode button to switch to Pre mode to continue with the Next lab.

### Finish forge operation

#### Insert new operation

We will add a finisher forging operation to the pancaked part. From the Explorer tab on the left side of the user interface, go to **Forming**![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Single and then click the ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button next to **[2D] Forming Express** as shown in Fig. L1.24.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0024.jpg' | relative_url }})

Adding operation from Explorer

A new operation tile will be added in the Operation Editor (See Fig. L1.25.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0025.jpg' | relative_url }})

Added Forming express operation 

Click on the **Forming** tile. You will get a pop-up window asking you to select Interactive or Batch setup. Interactive setup allows more direct control over inputs. However, Batch setup ensures that it will be possible to back up and rerun the full project from the beginning without interruption. _For almost all projects, Batch setup gives greater flexibility._

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0026.jpg' | relative_url }})

Setup type popup for 2D Forming operation

Click ![]({{ '/assets/icons/pre_icons/mo_no_batch_setup_button.jpg' | relative_url }}) in this dialog as shown in Fig. L1.26. The 2nd operation will open in the process tree. Notice how the objects in the 1st operation are now linked to the 2nd operation and are shown as Read from DB. All the objects appear red in the 2nd operation, indicating that they are being read from the previous operation in the database.

This operation inherits properties from the previous operation, so this operation will also be an isothermal hot forging process.

#### Import dies

New dies will be imported for this operation, so dies really won’t be Read from DB like the Workpiece. This is easy to change. When importing the dies below, remember that the geometries are in DEFORM installation folder \Tutorials directory.

#### Top Die

Click on Top Die in the Operation Tree. Change the object type to **Define** as shown in Fig. L1.27. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Geometry page.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0027.jpg' | relative_url }})

Top die window

#### Top die Geometry

Import the geometry “**gear top die.****IGS** ”. Click the ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Load geometry from a file) button and ![]({{ '/assets/icons/pre_icons/mo_open_button.jpg' | relative_url }}) open (import) the file “gear top die.IGS”. The geometry for Top Die is located in DEFORM installation folder \Tutorials directory. Use ![]({{ '/assets/icons/pre_icons/mo_check_and_correct_geo_button.jpg' | relative_url }}) to check the geometry and fix the shading so that it is correctly on the inside of the part. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Top die Movement page.

Later in this setup, we will define a stopping criteria based on the spacing of the dies at the flash gap. To define this, we need to define reference points on the dies.

In the lower right corner of the geometry page, click ![]({{ '/assets/icons/pre_icons/mo_define_reference_point_button.jpg' | relative_url }}) to turn the button blue.

Use the mouse to pick the bump in the top die corresponding to the flash land, as shown in the Fig. L1.28.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0028.jpg' | relative_url }})

Defining reference point for Top die geometry

#### Assign Top die movement

The speed of **3** in/sec. is already defined from the previous operation so no changes are needed. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Bottom die page.

#### Bottom Die

Change the object type to **Define**. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Geometry page.

#### Bottom die geometry

Import the geometry “**gear bottom die.****IGS** ”. Click the ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Load geometry from a file) button and ![]({{ '/assets/icons/pre_icons/mo_open_button.jpg' | relative_url }}) open (import) the file “gear bottom die.IGS”. The geometry for bottom die is located in DEFORM installation folder \Tutorials directory. Use ![]({{ '/assets/icons/pre_icons/mo_check_and_correct_geo_button.jpg' | relative_url }}) to check the geometry and fix the shading so that it is correctly on the inside of the part. In the lower right corner of the geometry page, click ![]({{ '/assets/icons/pre_icons/mo_define_reference_point_button.jpg' | relative_url }}) to turn the button blue. Use the mouse to pick and select the below point on the bottom die flash land, as shown in the Fig. L1.29.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0029.jpg' | relative_url }})

Defining reference point for Bottom die geometry

#### Scheduled positioning

Because the workpiece is being read from the database after an earlier forming operation, the size and shape may change if the project is rerun from the beginning. For this reason, it is better to allow a flexible positioning of the tools relative to the workpiece, rather than setting a firm position for them.

In DEFORM, there is an operation called Scheduled positioning which allows the tools to be moved into contact with an arbitrary workpiece shape whenever the workpiece is imported from a prior operation. 

Go to**Scheduled positioning** in the Process Tree and click the ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button to add a positioning operation. 

First, we will schedule the bottom die to move up to the workpiece. 

Select **Interference** and pick the **Bottom****Die** as the **Positioning****object** , and the **Workpiece** as the **Reference****object**. Make the approach direction **Y** (up). Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). 

Note that the tool does not move at this time, but positioning will be performed when the database is generated for this operation.

Click ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) again to schedule a second positioning. Select **Interference** and position the **Top****Die** down (**-Y**) to the **Workpiece**. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). (See Fig. L1.30.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Contact page

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0030.jpg' | relative_url }})

Scheduled positioning window

#### Inter-object relationships

In the Contact dialog, the same **System** -**defined** contact of **0.3** Shear will be used as the first operation. So, no changes are needed. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Primary die stroke page

#### Primary die stroke

When defining the above stopping criteria, we saw that the flash gap between the dies was approximately **1.75** in (before the scheduled positioning). A good estimate of how much the Top Die will move in this operation is around 1.5 in. Set the Total primary die travel to 1.5 in. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Stopping controls page (See Fig. L1.31.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0031.jpg' | relative_url }})

Primary die stroke window

#### Stopping controls

Rather than measuring the tool movement distance as we did in the first operation, we will stop this process with a fixed distance between tools. In this case we will set the flash thickness to 0.2 in.

The flash distance is measured at the reference points defined on the top and bottom dies.

Click on Stopping controls in the Process Tree. Check the box for **Distance****between****objects** and define the value as**0.2** in. Select Object 1 as the **Top****Die** and Object 2 as the **Bottom****Die** and select **Y** direction. Once you complete the settings, the reference points and current distance will be shown in the graphics window (See Fig. L1.32.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Simulation controls page.

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0032.jpg' | relative_url }})

Stopping controls window 

#### Simulation controls

Click on Simulation controls. We want to travel about 1.5 in. in 100 steps, so we will use a step increment of 0.015 in/step. HOWEVER, we do not want the simulation to run out of steps since there is another stopping criteria (die distance) set. Since we want to have flexibility when rerunning this case, we will set the number of simulation steps to 1000, not 100. This will ensure that if we rerun the project with different settings, we will not need to worry about running out of steps. The stopping will always be controlled by the distance between the tools.

Change the time stepping from System to **User**. Change the **Number of steps** to **1000** and the **Step increment** to **5** and set the With **constant****die****displacement** to **0.015** in (See Fig. L1.33.).

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0033.jpg' | relative_url }})

Simulation controls window

#### Generate DB

The system will pause briefly as it executes the scheduled positioning and contact generation. The workpiece color turns from red (Read from DB) to yellow (Plastic object).

Click ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}).

Click on the MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode button (above the operation tree) to start the simulation.

#### Run and monitor a simulation

Click the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) button and then uncheck submit job to the simulation queue. Unchecking this option will make the job run on the local computer. Use the default **Start from last negative step** option. Click the ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to start the simulation.

#### Review the results

When the simulation is completed, click the MO ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode button to review results.

Play through all steps. Note that the part does not completely fill out the die cavity (See Fig. L1.34.). 

![]({{ '/assets/images/labs/advanced_labs_in_mo/gear_labs/forming_express_gear_labs/lab1_image0034.jpg' | relative_url }})

Workpiece shape at last step of second operation

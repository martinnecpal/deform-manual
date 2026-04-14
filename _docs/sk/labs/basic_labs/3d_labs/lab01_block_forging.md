---
lang: sk
title: "Lab01 Block Forging"
---

# Lab01 Block Forging

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0000.jpg' | relative_url }})

  
1.1. Creating a New Problem

1.2. Simulation controls

1.3. Setting material properties

1.4. Loading Object Data

1.4.1. Workpiece (Block)

1.4.2. Top Die

1.4.3. Bottom Die

1.5. Positioning

1.6. Inter-Object Relationships

1.7. Setting Steps controls

1.8. Database Generation

1.9. Starting the simulation

1.10. Post-Processing the Results

1.11. Exiting MO Wizard

## Creating a New Problem

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear as shown below Fig. 3DL1.1.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0001.jpg' | relative_url }})

DEFORM GUI main window

Create a new problem either by selecting **File** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in Fig. 3DL1.2. Select "**Integrated Manufacturing Process** " radio button and unit system as "**English** " radio button in unit field. Define Problem Name as " ******Block** " and make sure the “**Show option dialog** ” check box is turned on (if we do not turn on the “Show option dialog” check box, then we will not get the New Project dialog). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new problem using the Deform Integrated Manufacturing Process.

.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

Problem type selection window

Multiple operation wizard will open with the New Project dialog (see Fig. 3DL1.3.), at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session we use ‘**Block** ’ as the project name.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0003.jpg' | relative_url }})

Problem type selection window

User can also change the Unit system (File menu selected unit system will be selected by default) and add **3D Forming operation** by selecting from **First****operation** pull down list and **turn on checkbox** (see Fig. 3DL1.4.). Using copy Existing project option we can import previous saved projects as new project. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0004.jpg' | relative_url }})

Assigning problem name

The Multiple operation wizard (MO wizard) will open (see Fig. 3DL1.5.). The MO wizard is divided into several distinct sections - namely the DISPLAY window, Graphical Utilities, Operation Tree, property Editor, Operation Editor, Explorer and Graphics window.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0005.jpg' | relative_url }})

MO wizard window

## Simulation controls

In this operation we are setting up simple Isothermal operation so,in Simulation control page Sim Mode tab, **turn****off** the **Heat****transfer****mode** check box (see Fig. 3DL1.6.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0006.jpg' | relative_url }})

Simulation controls page

## Setting material properties

When setting up a simulation, material properties have to be specified for the objects. The workpiece has been assigned the material type Plastic, therefore the plastic flow stress needs to be defined. In addition, if the simulation were non-isothermal (temperature varying with time), then the thermal properties would also be required. The material properties of the dies do not have to be specified because their object type is Rigid (and the simulation is isothermal), and therefore do not undergo any deformation upon loading.

Click on the material ![]({{ '/assets/icons/pre_icons/mo_material_icon.jpg' | relative_url }}) icon of the explorer tab, a list of materials which are divided into different categories will appear. For this simulation we need to define the **AISI-1035,****COLD** material for workpiece. so the **Steel** category has to be selected to bring up all the steel materials. Also, there are two different AISI-1035 materials – one for cold forming and one for hot forging. Since this simulation is set for room temperature, select the ‘AISI-1035, COLD’ material.

After selecting the material in the list, click on the ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Add) button to add the selected material to the problem.

Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button to see the properties of the added material (see Fig. 3DL1.7. and Fig. 3DL1.8.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to go to object page.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0007.jpg' | relative_url }})

Material list page

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0008.jpg' | relative_url }})

Material properties page

## Loading Object data

If there aren't already three objects, add the three objects by clicking the insert object button ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}), three objects will be named as Workpiece, Top die and bottom die. Workpiece will get added with plastic object type where as Top die and Bottom die will added with rigid object type (see Fig. 3DL1.9.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button to go to Workpiece page.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0009.jpg' | relative_url }})

Objects adding page

### Workpiece (Block)

As you enter the Workpiece page, change the Object name to **Block** and make sure that the object type is set to **Plastic**. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to go to geometry page and click on ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) load geometry from library option.(See Fig. 3DL1.10.)

The most common type of file for importing geometry into DEFORM-3D is the stereo lithography (.STL) file. The geometry for the Block is located in the file **Block_Billet.STL** in DEFORM installation folder \3D\LABS directory. Once you have found and selected this file, click the ![]({{ '/assets/icons/pre_icons/mo_open_button.jpg' | relative_url }}) button to import the geometry into DEFORM. The geometry of a rectangular block should now be visible in the DISPLAY window.Now geometry has been defined for the block, click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to go to mesh page.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0010.jpg' | relative_url }})

Geometry Definition page

In the **guided****mode** mesh page we are seeing mesh setting options like target number of elements, preview and generate mesh, Click on the ![]({{ '/assets/icons/pre_icons/mo_preview_mesh_button.jpg' | relative_url }}) button to see what the surface mesh looks like when using the default mesh settings. The surface mesh that is created looks good, so click the ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button to finish the meshing process. When you are asked "Do you want to assign default boundary conditions?" click ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}). When the meshing is complete, We can see Number of elements in the Object Tree or in the Summary section of the Meshing controls.(See Fig. 3DL1.11. and Fig. 3DL1.12.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to go to object material page.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0011.jpg' | relative_url }})

Mesh generation page

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0012.jpg' | relative_url }})

Before and After meshing

Again we can see the object material and we can edit material properties by clicking the ![]({{ '/assets/icons/pre_icons/mo_edit_material_button.jpg' | relative_url }}) option. Select the material in the list to add the material to object as shown in Fig. 3DL1.13. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to go to Boundary conditions page.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0013.jpg' | relative_url }})

Object material page

For Object BCC, Default boundary conditions will get defined by MO wizard itself. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to go to movement page.

For movement, since the workpiece has not have any initial movement, so we are not defining any movement for workpiece. Continue until Top die by clicking ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button.

### Top Die

As you enter the Top die page, make sure **rigid** object type is selected for top die. click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to go to Top die geometry page, click on load geometry from library option ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) and import **Block_TopDie.STL** geometry from DEFORM installation folder \3D\LABS directory. The geometry of a rectangular block should now be visible in the Graphic window. It is good practice to check the geometry of an object after it is imported into DEFORM to make sure it doesn’t have any problems. To check the geometry, click the ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) button. A GEOMETRY CHECKING window will appear which gives a summary of the object’s geometry (see Fig. 3DL1.14.). For an object that has a closed volume, there should be 1 surface, 0 free edges, and 0 invalid entities. Objects that are imported as surfaces and not solids will have a free edge but should still only have 1 surface.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0014.jpg' | relative_url }})

Geometry checking results window

In addition to checking whether the imported geometry has problems, the orientation of the geometry should also be checked. If the geometry is a closed volume, the correct orientation is defined when the surface normals are pointing out of the object. When the geometry is not a closed volume but is just a surface, the correct orientation is defined when the normals are pointing toward the workpiece. Click the ![]({{ '/assets/icons/pre_icons/mo_show_geometry_normal_vectors_option.jpg' | relative_url }}) button to view the surface normals, and if the surface normals are not correctly pointing out of the object, click the ![]({{ '/assets/icons/pre_icons/mo_reverse_label.jpg' | relative_url }}) button. continue up to Top die movement page by clicking ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button.

**Top die Movement**

If any of the dies are moving, that movement needs to be defined. In this simulation, the Top Die will be moving downward to compress the Block.

The die will be moving downward at a **constant****speed** of **1** in/sec. In the Movement page go to the Translation tab select the movement Type as Speed. Set the **Speed** field to a Constant value of **1** in/sec. The default Direction of –**Z** is correct for this simulation. Continue up to Bottom Die by clicking ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button.

### Bottom Die

As you enter the Bottom die page, make sure rigid object type is selected for bottom die. Click next to go to Bop die geometry page, click on click on load geometry from library option ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) and import **Block_BottomDie.STL** geometry file from DEFORM installation folder \3D\LABS directory. Use the ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) and ![]({{ '/assets/icons/pre_icons/mo_show_geometry_normal_vectors_option.jpg' | relative_url }}) buttons to check that the geometry doesn’t have any problems and that the surface normals are correctly pointing out of the object. 

At this point, all three objects should be visible in the DISPLAY window.

Continue up to positioning page by clicking ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button.

## Positioning

###  Automatic positioning

For a simple three objects setup with top die as primary die, if we click on the ![]({{ '/assets/icons/pre_icons/mo_automatic_positioning_button.jpg' | relative_url }}) button, the Bottom die will undergo interference positioning with workpiece in +Z direction and Top die will undergo interference positioning with Workpiece in -Z direction. (See Fig. 3DL1.15.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0015.jpg' | relative_url }})

Automatic Positioning

### Position objects

Open the Object positioning window by clicking the position objects button (see Fig. 3DL1.16.). The various positioning methods available within DEFORM-3D are:

![]({{ '/assets/icons/pre_icons/mo_drag_radio_button.jpg' | relative_url }}) |  Objects can be positioned by using the mouse to drag them around the DISPLAY window.  
---|---  
![]({{ '/assets/icons/pre_icons/mo_drop_radio_button.jpg' | relative_url }}) |  Objects can be dropped in a defined direction, and they are allowed to translate and rotate until they come to rest (a state of equilibrium) against the other objects. Drop positioning is especially useful when the starting position of an object is somewhat ill-defined such as an irregularly shaped billet settling into a cavity.  
![]({{ '/assets/icons/pre_icons/mo_offset_radio_button.jpg' | relative_url }}) |  Objects can be moved a defined distance by either specifying a distance vector or by specifying the starting and ending points of the move.  
![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}) |  In Interference positioning, the object being positioned will be moved so that it very slightly overlaps a reference object. Objects can be rotated a defined angle about any axis.  
![]({{ '/assets/icons/pre_icons/mo_rotational_radio_button.jpg' | relative_url }}) |  Objects can be rotated a defined angle about any axis.  
  
![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0016.jpg' | relative_url }})

Object positioning window

### Drag Positioning

Click the ![]({{ '/assets/icons/pre_icons/mo_drag_radio_button.jpg' | relative_url }}) option and select the positioning object to be the **Block**. In the DISPLAY window, click on the +Z arrow and drag the Block upward so that it is no longer sitting on the Bottom Die. Change the Positioning object to the**Top Die** , and use the +Z arrow to move it upward so that it is no longer in contact with the Block, and then use the -Y arrow to place it in the position shown below.(See Fig. 3DL1.17.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0017.jpg' | relative_url }})

Drag positioning

### Drop Positioning

As an example of Drop positioning, let's drop the Block onto the Bottom Die.

Click the ![]({{ '/assets/icons/pre_icons/mo_drop_radio_button.jpg' | relative_url }}) button and change the positioning object to the Block. Change the Direction to -Z and click ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) to perform the drop. (See Fig. 3DL1.18.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0018.jpg' | relative_url }})

Drop positioning

### Offset Positioning

As an example of Offset positioning, let's move the **Top Die** so that it is sitting directly on top of the Bottom Die.

Click the ![]({{ '/assets/icons/pre_icons/mo_offset_radio_button.jpg' | relative_url }}) button and change the positioning object to the Top Die. The two methods of Offset positioning are 1) specifying a distance vector or 2) specifying the starting and ending points of the move. Either of these options can use the mouse to define the distance parameters.

The easiest way to position the Top Die on top of the Bottom Die is to use the Two points option. Select this option and select the points shown below as the Start and End points of the move. Click the ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) button to perform the move. (See Fig. 3DL1.19.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0019.jpg' | relative_url }})

Offset positioning

### Interference Positioning

The Top Die should now be sitting directly on top of the Bottom Die. Let's use Interference positioning to move the Top Die back to its correct position on top of the Block.

Click the ![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}) button. In the positioning dialogue, the Positioning object should already be the **Top Die**. Change the Reference to be the Block if it isn't already. Since the Top Die has to move downward to contact the top of the Block, change the Approach Direction to **-Z**. Click the ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) button to position the Top Die. (See Fig. 3DL1.20. and Fig. 3DL1.21.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0021.jpg' | relative_url }})

Object positioning window

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0020.jpg' | relative_url }})

Object interference

When finished with this positioning, click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to exit the OBJECT POSITIONING window.

Continue up to contact page by clicking on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button.

**Note:**

At any time when in the [Object Positioning](/docs/sk/pre_processor/19_object_positioning/19_object_positioning/) window, the ![]({{ '/assets/icons/pre_icons/mo_cancel_button.jpg' | relative_url }}) button or the ![]({{ '/assets/icons/pre_icons/mo_reset_button.jpg' | relative_url }}) button can be used to return the objects to their positions prior to entering the Object Positioning window.

## Inter-Object Relationships

In contact page, click on the ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) button, two relationships will get added, Relationships within DEFORM are defined in relation to Master and Slave objects. In this simulation, a deforming workpiece is being deformed between two rigid dies. The rigid dies are defined as the Master objects and the deforming workpiece is defined as the Slave object.

Several interface properties (mainly friction and heat transfer coefficient) can be defined for each of these relationships. Since this simulation will not be taking into account any heat transfer, the only interface property that needs to be defined is friction. (See Fig. 3DL1.22.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0022.jpg' | relative_url }})

Contact window

With the first relationship highlighted, click the ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) button to modify the relationship. In the friction section of the screen, there is a pull-down menu that allows the user to choose the appropriate friction conditions of common forming processes. Since this simulation takes place at room temperature, and the dies are steel, use the pull-down menu and select Cold forming (steel dies) from the list (See Fig. 3DL1.23.). A friction value of 0.12 will automatically be selected. Click the ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button to return to the main contact page.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0023.jpg' | relative_url }})

Inter object data definition window

Now that the Top Die - Block relationship has been defined, the relationship between the Bottom Die and the Block needs to be defined. Since the friction conditions are the same between the workpiece and both of the dies, the ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) button can be used to copy the interface properties from the first relationship to all of the others. After this is done, both relationships will have a friction of 0.12 defined. (See Fig. 3DL1.24.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0024.jpg' | relative_url }})

Contact Window

Once the relationships are defined, contact between the objects needs to be generated. When contact is generated, any nodes on the deforming object (Slave) that fall within a specified tolerance of a die (Master) are repositioned onto the die surface.

Before generating contact, we need to determine a reasonable tolerance value. Too large a tolerance will put too many nodes in contact with the die surface, which may cause distortion of the workpiece mesh. Too small a tolerance will mean that too few nodes are found in the contact band and very little contact will be generated. By clicking on the ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) icon in the Tolerance section, DEFORM will determine a reasonable tolerance value. A tolerance of 0.0046" gets calculated and automatically gets input into the program.

Once this tolerance has been set, click the ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) button to generate the contact between the objects. Contact will get generated between the Block and both dies, and this contact is shown in the DISPLAY window as colored dots on the top and bottom surface of the Block.

**Note:**

If too large a tolerance is used when generating contact, and the mesh of the workpiece gets distorted, the ![]({{ '/assets/icons/pre_icons/mo_restore_mesh_button.jpg' | relative_url }}) button can be used to undo the contact generation.

Continue to the Step page by clicking ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button.

## Setting Steps controls

In Step page, set the **Number****of****Simulation****Steps** to **20**. Unless the simulation stops prematurely, the simulation will run 20 steps. Set the **Step****Increment** to **Save** to **2**. Every second step of the simulation will be written to the database. Notice that the Primary Die is shown in this window as well. set the primary die to the Top Die, and it is this die that will be used as a control for many of the stepping and stopping controls.(see Fig. 3DL1.25.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0025.jpg' | relative_url }})

Step control page

An appropriate step size for the simulation now has to be determined. For most simulations, the amount of die stroke per step should be set to about 1/3 of a typical element edge length. The Measure ![]({{ '/assets/icons/pre_icons/mo_measure_tool_icon.jpg' | relative_url }}) tool can be used to determine this value. Click the icon and then measure any edge length on the Block (you may have to click the ![]({{ '/assets/icons/pre_icons/mo_shading_mode_icon.jpg' | relative_url }}) to view the shaded mesh). A typical edge length is about 0.4". One-third of 0.4" is about 0.13". Under Solution Steps Definition, select with Constant Die Displacement radio button and define **0.13** value. click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to go to Database generation page.

## Database Generation

Once the problem has been completely set up, the last step is to generate a database file. The FEM engine (the part of DEFORM® that calculates the solution) uses a database file to store the finite element solutions for the problem. When you generate a database in the DEFORM Pre-processor, all of the information defined in the Pre-processor (such as the material properties, movement controls, object geometries, etc.) is transferred to the database file.

In Generation DB page. Click the ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) button to have the program check to see if anything was missed in the problem setup. During the checking process:

Messages in the red color signify data that needs to be fixed before a simulation can be run (such as when you forget to define any material data). 

Click on the ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database. When the program is done writing the database, click on the ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) tab. 

## Starting the Simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label under the simulation tab (See Fig. 3DL1.26.), Run Options dialog will open as shown in Fig. 3DL1.27. Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0032.jpg' | relative_url }})

Simulation options

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0027.jpg' | relative_url }})

Run simulation window

The progress of the simulation can be monitored as it is running by looking at the Simulation Message and process monitor in Simulation mode. Click the Simulation Message tab to view the Message file. As long as the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked, which is the default setting, the Message file will refresh every couple of seconds.

The Message file provides information about which simulation step the simulation is currently on and also gives information dealing with how well the simulation is running.

When the simulation has finished, the following message will be added to the end of the Message file:NORMAL STOP: The assigned steps have been completed as shown in (see Fig. 3DL1.28.).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0028.jpg' | relative_url }})

Simulation message tab

## Post-Processing the Results

After the simulation has completed, click on ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) tab, MO post processor will open. (See Fig. 3DL1.29.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0029.jpg' | relative_url }})

MO Post Processor window

### Step Tools and Step Selection

To select the step to be viewed, there is a step browser page. click on the ![]({{ '/assets/icons/pre_icons/mo_all_button.jpg' | relative_url }}) button in the step browser, when we click on the all button, all the saved steps will be displayed in the step browser. The ![]({{ '/assets/icons/pre_icons/mo_step_list.jpg' | relative_url }}) icon can be used to bring up the STEP LIST window, which allows the user to define more detailed step settings.

### State Variables

Some of the most commonly used state variables can be viewed in the post tools page. (See Fig. 3DL1.30.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0030.jpg' | relative_url }})

Post Tools page

Select Strain-Effective from post tolls to look at the amount of deformation the workpiece has undergone. Click the ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) icon to bring up the STATE VARIABLE window, and select ![]({{ '/assets/icons/post_icons/mo_local_scaling_radio_button.jpg' | relative_url }}) as the Scaling option. This option will use the Local Min and Max effective strain as the extremes on the color bar. Play through the steps of the simulation to observe the accumulation of strain.

The ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) icon can be used to access all of the state variable options.

### Point Tracking

In DEFORM it is possible to track points in an object through the simulation. Not only can the position of the points be tracked but also the state variables at those locations. To open the Point Tracking window, click the ![]({{ '/assets/icons/post_icons/mo_point_tracking_icon.jpg' | relative_url }}) icon.

We want to define several points on the undeformed geometry and see where they go as the part deforms. To view the undeformed geometry, click the ![]({{ '/assets/icons/pre_icons/mo_preview_first_step_icon.jpg' | relative_url }}) button to view the first step of the simulation. Now click three locations on the workpiece (See Fig. 3DL1.31.) and accept the default Tracking option and click on ![]({{ '/assets/icons/post_icons/mo_track_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0031.jpg' | relative_url }})

Point tracking points

When a state variable is selected from the State Variable pull-down menu, the point tracking graph for the three points will appear in the DISPLAY window.

Click the ![]({{ '/assets/icons/pre_icons/mo_preview_play_button.jpg' | relative_url }}) icon to play the through the steps. You will notice that the corresponding step on the Point Tracking plot also gets highlighted as the steps change. Click the ![]({{ '/assets/icons/pre_icons/mo_preview_stop_button.jpg' | relative_url }}) icon to stop the step playback. Now click anywhere on the Point Tracking graph - the selected step shown in the DISPLAY window should change to match the location selected in the graph. (See Fig. 3DL1.32.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0032.jpg' | relative_url }})

Point Tracking graph

### Slicing Objects

In DEFORM it is possible to slice an object and then view different state variables within the object. Let's first hide the Point Tracking graph by right-clicking the Point Tracking in the Object Tree and selecting the Hide Point Tracking graph option. (See Fig. 3DL1.33.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0033.jpg' | relative_url }})

Point tracking RMB option in Object Tree

Click the ![]({{ '/assets/icons/post_icons/mo_slice.jpg' | relative_url }}) icon to open the Slicing window. The objects can be sliced in several different ways. The objects in the DISPLAY window have a yellow rectangular box surrounding them. By clicking on a vertical edge of the box, a horizontal slicing plane will be created. By clicking on a horizontal edge of the box, a vertical slicing plane will be created. Click the yellow box in several locations to experiment with this slicing option. (See Fig. 3DL1.34.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0034.jpg' | relative_url }})

Slicing objects

The slicing planes are defined by a point on a plane and a normal direction to that plane. These are designated in the SLICING window by P (Point) and N (Normal). 

The objects can also be sliced by selecting the X, Y, or Z coordinate of the Point and then using the slider bar to drag that coordinate up or down. As the slider moves, the objects will be dynamically sliced. Click the X coordinate of the Point as shown in Fig. 3DL1.35., and then drag the slider back and forth to slice the objects.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0035.jpg' | relative_url }})

Slicing window 

Several options are available for determining how the sliced surfaces are displayed. (See Fig. 3DL1.36.) After the completion of slicing click ok for the slicing page.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab01_block_forging/image0036.jpg' | relative_url }})

Slicing surfaces

## Exiting MO Wizard

When you are finished, exit the MO Post-processor by clicking the close ![]({{ '/assets/icons/pre_icons/mo_quit_icon.jpg' | relative_url }}) icon.

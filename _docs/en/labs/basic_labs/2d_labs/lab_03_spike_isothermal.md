---
lang: en
title: "Lab 03 Spike Isothermal"
---

# Lab 03 Spike Isothermal

3.1. Creating a New Problem

3.2. Adding Forming operation - Spike

3.3. Spike Isothermal- Block

3.4. Close MO Wizard

In this lab we will setup 2 operations in interactive mode.

**Operation1** : Spike -Simple Deformation operation.

**Operation2** : Block - Changing Top die.

## Creating a New Problem

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear. as shown below Fig. L3.1.).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0001.jpg' | relative_url }})

DEFORM GUI main window

Create a new problem either by selecting **File****![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in Fig. L3.2. Select " **Integrated Manufacturing Process** " radio button and unit system as "**English** " using radio button. Define Problem Name as "**Spike_Isothermal** " and make sure the “**Show option dialog** ” check box is turned on (if we do not turn on the “Show option dialog” check box, then we will not get the New Project dialog). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

Problem type selection window

Multiple operation wizard will open with the New Project dialog (See Fig. L3.3.), at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session we use ‘**Spike_Isothermal** ’ as the project name.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0001.jpg' | relative_url }})

MO wizard New project

User can also change the Unit system (File menu selected unit system will be selected by default) and add operation by selecting from First operation pull down list and checkbox (See Fig. L3.4.). Using copy Existing project option we can import previous saved projects as new project. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0002.jpg' | relative_url }})

Assigning problem name

## Adding Forming operation - Spike

Multiple Operation wizard will opens with new project called Spike_Isothermal to setup the problem. Add 2D Forming operation from Operations list in Explorer. Operation can be add by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button next to 2D Forming operation (See Fig. L3.5.) or user can also add the operation by dragging and dropping the operation into Operation Editor region.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0003.jpg' | relative_url }})

Added 2D Forming operation into Operation Editor

### Geometry Type

In this lab we will be using Axisymmetric geometries, So select **2D Axisymmetric** radio button from geometry type page as shown in Fig. L3.6., then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) .

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0004.jpg' | relative_url }})

Axisymmetric Geometry type selection

###  Simulation Controls

In this lab we will be showing how to setup simple Isothermal problem. So, in Simulation controls uncheck the Heat transfer mode check box (see Fig. L3.7.). Then Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0005.jpg' | relative_url }})

Simulation control window

### Assigning Material for Workpiece

In material list window load the material '**AISI-1035, COLD** ' from DEFORM Material library, Steel category using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load material data from library) option. This can be done as shown in below by clicking ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}) button as shown in Fig. L3.8.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0006.jpg' | relative_url }})

Material Library Window

Material can also be assigned from Material List in Explorer, by clicking ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button next to AISI-1035,COLD[70-400F(20-200C)] or user can also add drag and drop the material into Material list region (See Fig. L3.9.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Object page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0007.jpg' | relative_url }})

Explorer material list

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0008.jpg' | relative_url }})

Material list page

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0009.jpg' | relative_url }})

Material properties page

### Adding Objects

For this operation we required three objects, if there aren't already three objects, add the three objects by clicking the ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) button. The three objects will be named as Workpiece, Top Die and Bottom Die.(See Fig. L3.12.), then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0010.jpg' | relative_url }})

Adding Object Window

###  Workpiece

In Workpiece window, change the Object Name to **Billet** and select Object type as **Plastic** as shown in Fig. L3.13., Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0011.jpg' | relative_url }})

Billet object Window

#### Loading Billet Geometry

In Geometry window, load **Spike_Billet.IGS** geometry file from library using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load geometry from library) option or can also be imported using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Load geometry from a file) option as shown in Fig. L3.14. The geometry for billet is located in DEFORM installation folder \2D\LABS directory.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0012.jpg' | relative_url }})

Billet Geometry window

The ![]({{ '/assets/icons/pre_icons/mo_show_geometry_inside_mark_radio_button.jpg' | relative_url }})option is to check the orientation of the geometry when we import the geometry from a file. By default the Show geometry inside mark check box will be checked; if not turn on the check box. 

The points defining the imported geometry can be viewed/edited by clicking the ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}) button. When .IGS files are loaded, the data gets imported into DEFORM in Line-Arc format, which defines the geometry in terms of lines and arcs. To view the XYR format of this geometry, user should click on **XYR** button as shown in Fig. L3.15.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0013.jpg' | relative_url }})

Geometry Data

Whenever geometry is imported, it should be checked for its orientation and correctness. Click the ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) button and then click ![]({{ '/assets/icons/pre_icons/mo_check_and_correct_geo_button.jpg' | relative_url }}) button to check and correct the geometry. This not only fixes any problems with the geometry but also corrects the orientation of the geometry, if needed. See Fig. L3.16. where ![]({{ '/assets/icons/pre_icons/mo_check_and_correct_geo_button.jpg' | relative_url }}) is used to correct the orientation, the geometry has changed the orientation from clockwise to counter-clockwise.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0014.jpg' | relative_url }})

Check and correct geometry

#### Generating mesh for Billet

We would like to put an initial mesh on the billet with more elements near the top right corner, where the largest deformation will initially be. You can do this with either mesh windows or user-defined mesh values. For this lab, we will use user-defined values to put the initial mesh on the billet.

If you are in Guided mode, Switch to Expert mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) (Switch to expert mode) icon located in the tool bar at the top of window. Expert mode will provide more options for detailed settings., select ![]({{ '/assets/icons/pre_icons/mo_user_defined_radio_button.jpg' | relative_url }}) in mesh page. We want the upper right corner of the billet to have a mesh that is four times finer than the mesh at the other three corners. To accomplish this, we are going to assign a mesh size of 1 to the upper right corner and a mesh size of 4 to the other corners.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0015.jpg' | relative_url }})

Selecting points for user defined mesh

Set the Element Size to 1 and click the upper right corner of the Billet and then set the Element Size to 4 and click the other three corners (See Fig. L3.17.). Set the Number of Elements to 400 and click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button, around 412 mesh elements is generated for the billet as shown in Fig. L3.18. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0016.jpg' | relative_url }})

Billet Mesh window

As we are using user-defined mesh to define the initial mesh, the Weighting Factors are not considered. The user-defined values, however, can only be used to define the initial mesh. If a remesh is necessary during the simulation, the Weighting Factors are used to define the new mesh.

We want to set one more meshing related parameter. There are several criteria that will trigger a remesh of the billet during a simulation. One of them is called the Interference Depth, which is the distance a tool is allowed to penetrate into the workpiece.

A good value to use for the interference depth is approximately a third of the smallest element size of the deforming object. Zoom in on the upper right corner of the Billet using the ![]({{ '/assets/icons/pre_icons/mo_box_zoom_icon.jpg' | relative_url }}) icon and then use ![]({{ '/assets/icons/pre_icons/mo_measure_tool_icon.jpg' | relative_url }}) to measure a small element edge length. The value for the Interference Depth will be somewhere around 0.013 (0.038 / 3) and this should be set in the Remeshing Criteria tab (See Fig. L3.19.).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0017.jpg' | relative_url }})

Remeshing criteria window

####  Assign Workpiece material

To assign material for workpiece select the material **AISI-1035,COLD[70-400F(20-200C)]** from material window. This can be done as shown in below Fig. L3.20. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0018.jpg' | relative_url }})

Material selection window

#### Workpiece BCC

In BCC page, check the default assigned Deformation BCC for Left side of the workpiece in X-Direction, default BCC are assigned automatically due to selection of problem type as axisymmetric (See Fig. L3.21.). Then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top die page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0019.jpg' | relative_url }})

Billet BCC window

### Top Die

In Top die page ( see Fig. L3.22.) select Object type as **Rigid** and Turn on Primary die check box as Top die will have movement definition assigned to it, click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0020.jpg' | relative_url }})

Top die page

#### Loading Top die Geometry

In Geometry window, load **Spike_TopDie.IGS** geometry file from library using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load geometry from library) option or can also be imported using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Load geometry from a file) option as shown in Fig. L3.23. The geometry is located in DEFORM installation folder \2D\Labs directory. Check the geometry using ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) option to make sure the geometry is OK. Then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top die movement page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0012.jpg' | relative_url }})

Top Die Geometry page

#### Assign Movement to Top Die

Define a **speed** of **2** in/sec in **-Y** direction for this lab (See Fig. L3.24.). Then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Bottom Die page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0021.jpg' | relative_url }})

Top die Movement page

### Bottom Die

In Bottom die page select Object type as **Rigid** and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) (See Fig. L3.25.).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0022.jpg' | relative_url }})

Bottom Die page

#### Loading Bottom Die Geometry

In Geometry window, load **Spike_BottomDie.IGS** geometry file from library using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load geometry from library) option or can also be imported using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }})(Load geometry from a file) option. The geometry is located in DEFORM installation folder \2D\Labs directory. Check the geometry using ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) option to make sure the geometry is OK. Then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Positioning page.

### Positioning

The object can be positioned in Positioning page, two options are available in Positioning page to position objects, Automatic Position and Position Objects option.

**Automatic position** ![]({{ '/assets/icons/pre_icons/mo_automatic_positioning_button.jpg' | relative_url }}): In Automatic positioning, the objects will be positioned automatically with respect to the Positioning direction and the Primary die movement direction. This option can only be used where the operation has only 3 objects: Workpiece, Top die and Bottom die.

**Position objects** ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) : The Positioning methods available are:

![]({{ '/assets/icons/pre_icons/mo_drag_radio_button.jpg' | relative_url }}) |  Objects can be dragged in a certain direction using the mouse.  
---|---  
![]({{ '/assets/icons/pre_icons/mo_offset_radio_button.jpg' | relative_url }}) |  Objects can be moved a defined distance by either specifying a distance vector or by specifying the starting and ending points of the move.  
![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}) |  In Interference positioning, the object being positioned will be moved so that it very slightly overlaps a reference object.  
![]({{ '/assets/icons/pre_icons/mo_rotational_radio_button.jpg' | relative_url }}) |  Objects can be rotated in a defined angle about a defined center point.  
![]({{ '/assets/icons/pre_icons/mo_flip_radio_button.jpg' | relative_url }}) |  Objects can be flipped about the X, Y or any other defined axis.  
  
**Offset Positioning:**

****Let's move the Bottom Die using offset positioning. Select and change the Positioning object to the Bottom Die. Distance components can be entered either by using the keyboard or by selecting the distance with the mouse. We want to position the die so that it moves up and to the right of the Billet. With Distance vector selected, click the Start and End points shown below with the mouse. The corresponding distance will be entered into the Distance vector fields. Click![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) to move the Bottom Die (See Fig. L3.26.).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0023.jpg' | relative_url }})

Offset Positioning

To move the Bottom Die back to its original location, change the Distance vector values from positive to negative and then click ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) again.

**Interference Positioning:**

****Select and change the Positioning object to the Top Die. We want to position the Top Die so that it just barely overlaps the top of the Billet. Since the Top Die has to move downward to contact the top of the Billet, change the Approach Direction to -Y. The default Interference works well in most cases, so click![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). In the Display window, you will notice that Top Die will move down slightly so that it is now touching the Billet (See Fig. L3.27.).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0024.jpg' | relative_url }})

Interference Positioning

**Rotational Positioning:**

Select and change the Positioning object to the Billet. We want to rotate the Billet 45 degrees clockwise about its lower right corner. Select User Defined radio button, click the lower right corner of the Billet with the mouse. The Center field in the Object positioning window will update to the coordinates that were just picked. Change the Angle to -45 (clockwise) and click ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). The Billet will rotate 45 degrees about the picked location. Change the Angle to 45 and to rotate the Billet back to its original location (See Fig. L3.28.).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0025.jpg' | relative_url }})

Rotational Positioning

In this operation setup we will use Automatic position option to position the objects. In Object positioning page select positioning direction as Z (Y) - direction and click on ![]({{ '/assets/icons/pre_icons/mo_automatic_positioning_button.jpg' | relative_url }}) button, it will position the objects as shown in Fig. L3.29. Then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Contact page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0026.jpg' | relative_url }})

Positioned the object using Automatic position option

### Contact Generation

Select user type contact and click on ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) button. It will add the relationship between the Billet, Top Die and Bottom Die as shown in Fig. L3.30. As the Dies are Rigid and Billet is plastic, Top and Bottom Dies are considered as Master and Billet as Slave. In order to predict the fold during deformation, self contact will be assigned for Billet.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0027.jpg' | relative_url }})

Contact Generation page

Highlight the Top Die – Billet relationship and click the ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) button to modify the contact conditions. In the friction section of the screen ( Fig. L3.31.), there is a pull-down menu that allows the user to choose the appropriate friction conditions of common forming processes.

Since this simulation takes place at room temperature and the dies are steel, use the pull down menu and select Cold forming (steel dies) from the list. A friction value of 0.12 will automatically be selected.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0028.jpg' | relative_url }})

Inter-Object data definition window

Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to go back to Inter-Object window, Since the friction conditions are the same for all the object pairs, the ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) button can be used to copy the interface properties from the first relationship to all of the others. After this is done, all relationships will have a friction of 0.12 defined. Use ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) icon to determine a suitable contact tolerance (a value of about 0.00126" will be calculated) , then click ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) button to generate contact. If you rotate the objects around in graphics window, you will see that contact was generated between the two objects. Switch to Message tab or Observe status bar to know about the contacts generated. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Step controls window.

### Step

Change the Operation name as " **Spike** " as shown in Fig. L3.32.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0029.jpg' | relative_url }})

Step Main tab in expert mode

Select the simulations steps tab (![]({{ '/assets/icons/pre_icons/mo_simulation_step.jpg' | relative_url }}) ), set the **Number of Simulation Steps** to **100** and **Step Increment to Save** to **5**. Set the **Top Die** as **Primary Die** if not selected automatically. (See Fig. L3.33.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0030.jpg' | relative_url }})

Simulation controls Simulation Steps tab in expert mode

To determine an appropriate step size, select the icon and measure the edge length of a few of the smaller elements in the Billet. An average length of a short edge is around 0.035”. Use a **Constant** Die Displacement per step of **0.015** in/step, which is 1/3 of this small edge length in step increment tab (![]({{ '/assets/icons/pre_icons/mo_step_increment.jpg' | relative_url }})) for step size as die displacement (See Fig. L3.34.) and leave other settings to default.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0031.jpg' | relative_url }})

Simulation controls Step increment tab in expert mode

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) and save a keyword file for the problem by selecting the File menu Export option.

### Generating Database

Once the problem has been completely set up, the last step is to generate a database file. The FEM engine (the part of DEFORM® that calculates the solution) uses a database file to store the finite element solutions for the problem. When you generate a database in the DEFORM MO Pre-processor, all of the information defined in the Pre-processor (such as the material properties, movement controls, object geometries, etc.) is transferred to the database file. From v12.0.2, In Generate DB file, we can observe the Operation Simulation setup summary as shown in Fig. L3.35.

In Generate DB page. Click the ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) button to have the program check to see if anything was missed in the problem setup. During the checking process, messages in the red color signify data that needs to be fixed before a simulation can be run (such as when you forget to define any material data).

Click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database. When the program is done writing the database, once the database has been generated, switch to the Simulation mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the operation tree.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0040.jpg' | relative_url }})

Generate DB page

### Starting the Simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label under the simulation tab (See Fig. L3.36.), Run Options dialog will open as shown in Fig. L3.37. Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0032.jpg' | relative_url }})

Simulation Options

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0056.jpg' | relative_url }})

Run Simulation window

The progress of the simulation can be monitored as it is running by looking at the Simulation Message tab and Simulation Graphics from the Graphics display region in Simulation mode. As long as the option is checked in Simulation Message tab, which is the default setting, the Message file will refresh automatically.

The Message file provides information about which simulation step the simulation is currently on and also gives information dealing with how well the simulation is running.

When the simulation is finished without any issues, the following message will be added to the end of the Message file:"NORMAL STOP: Simulation is completed and stopped at the user specified time step". (See Fig. L3.38.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0033.jpg' | relative_url }})

Simulation Message tab

### Post-Processing the Results

After simulation has been completed, switch to ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) tab to view results, MO post processor will open. (See Fig. L3.39.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0034.jpg' | relative_url }})

MO Post Processor window

#### Step Tools and Step Selection

To select the step to be viewed, there is a step browser page as shown in Fig. L3.40. Click on the ![]({{ '/assets/icons/pre_icons/mo_all_button.jpg' | relative_url }}) button in the step browser, when we click on the all button, all the saved steps will be displayed in the step browser. The ![]({{ '/assets/icons/post_icons/mo_step_list_icon.jpg' | relative_url }}) icon can be used to bring up the Step List window (See Fig. L3.40.), which allows the user to define more detailed settings for steps display.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0035.jpg' | relative_url }})

Step List window

Some of the most commonly used state variables can be viewed in post tools page. (See Fig. L3.41.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0036.jpg' | relative_url }})

Post Tools Page

#### State Variable

Select Strain-Effective from post tools to look at the amount of deformation the workpiece has undergone. Click the ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) icon to bring up the State Variable window, select **Strain-Effective** state variable, select Solid shading by clicking on Solid display button and select ![]({{ '/assets/icons/post_icons/mo_local_scaling_radio_button.jpg' | relative_url }}) as the Scaling option. This option will use the Local Min and Max effective strain as the extremes on the color bar. Scaling ,Shading and other contour plot setting can also be changed from RMB options on Colorbar. Play through the steps of the simulation to observe the accumulation of strain. (See Fig. L3.42.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0037.jpg' | relative_url }})

Strain-Effective Plot

The ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) icon can be used to access all of the state variables.

The user can change a variable plot from a Solid contour to a Line contour by selecting the Display type. Several other options are also available such as Shaded contours and Elemental contours.

**Vector Plots:**

****For variables that have an associated direction, such as velocity, a vector plot can also be shown. Within the State Variable menu, select ‘**Total Vel** ’ velocity as the variable to plot, and click on **Vector Plot** button. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) . A vector plot of the velocity of the nodes will be displayed for the billet (See Fig. L3.43.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0038.jpg' | relative_url }})

Velocity Vector plot

#### Load - Stroke Graph

The amount of load required to deform an object is an important result that can be obtained from a simulation.

Click the ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) icon, the Load Stroke Graph window will open. Select the **Top Die** in Plot object list, in **X-Axis** pull down menu select **Stroke** and in **Y-Axis** pull down menu select **Y Load**. Click on options tab and check Step tracer check box, then click on ![]({{ '/assets/icons/post_icons/mo_plot_button.jpg' | relative_url }}). The Load Stroke graph will display on the right side of the display window (See Fig. L3.44.). When a different step is selected, the balloon in the Load-Stroke curve will highlight that step and the corresponding load for that step will be shown in the graph. Also, a point on the graph can be picked with the mouse and the displayed step will automatically change to the one corresponding to that point on the graph.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0039.jpg' | relative_url }})

Load-Stroke Plot

After completion of Post processing, switch to ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}) button to add "Block" operation.

## Spike Isothermal- Block

In this operation we will be changing only Top die to check how the fold is developing and we will setup this operation in batch mode.

### Adding Operation

Add 2D forming operation from the Explorer Operation list. Then click on second forming operation to open second forming operation. When we click on second operation we will get Setup type popup, in popup click on **No-Batch mode** button as shown in Fig. L3.45. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Objects page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0041.jpg' | relative_url }})

Setup type popup to setup second operation

### Adding Objects

In Object window, by default previous operation three objects will be added in object list and object data will be transferred, if there aren't already three objects, add the three objects by clicking the ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) button, then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Workpiece

In Workpiece page select Read from DB as an object type, all the data like temperature, mesh and BCC of the Object will be carried over from previous operation (See Fig. L3.46.). The object color changes to Red color and in operation editor we are seeing link is created between the operation for the objects. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) .

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0042.jpg' | relative_url }})

Workpiece window

#### Assigning Workpiece Mesh

It is suspected that a fold will develop during this operation, so if you turn on self contact, the fold will be preserved and you can observe how it develops in the Post- Processor.

In Workpiece mesh page check Define mesh settings check box to modify the existing mesh, when we turn on the Define mesh setting check box all the mesh settings options will get activated. Change the **Number of Elements** as **500** , then click on **Advanced settings** tab and change the **Distance tolerance** to **0.001**. (See Fig. L3.47.)

Since we expect a small fold to develop, we want to make sure that the mesh in the vicinity of the fold will adequately capture the defect. The larger number of elements will be used in the first remeshing operation, increasing the total number of elements automatically from 400 to 500. Also, the "Distance tolerance" setting will help the mesh better to determine the fold in the geometry. 

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0043.jpg' | relative_url }})

Workpiece mesh window

Then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top Die page.

### Top Die

In Top die window select Object type as Rigid and Primary Die check box, click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) .

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0044.jpg' | relative_url }})

Top Die page

#### Create new top die geometry

In Top die geometry page, click on ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}) button. Click the ![]({{ '/assets/icons/pre_icons/mo_delete_loop_button.jpg' | relative_url }}) to remove existing geometry and add the following points in **XYR** format as shown in Fig. L3.49.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0046.jpg' | relative_url }})

Top Die Geometry data

Then click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button to close Edit window, click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until movement page.

#### Assign Movement to Top Die

Define a speed of 2 in/sec in -Y direction and set current stroke value to (0,0). Then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Bottom Die page.

### Bottom Die

In Bottom Die window select object type as Read from DB, then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Scheduled Positioning window.

### Scheduled Positioning the Top Die

In scheduled positioning page, Click on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button and select ![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}) radio button. Change the Positioning Object to the Top Die and the Reference to the Billet. Change the Approach Direction to -Y and then click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). (See Fig. L3.50.) Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Contact page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0045.jpg' | relative_url }})

Scheduled Positioning window

### Contact Page

Select user type contact and click on ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) button. It will add the relationship between the Billet, Top Die and Bottom Die as shown in Fig. L3.51. As the Dies are Rigid and Billet is plastic, Top and Bottom Dies are considered as Master and Billet as Slave. In order to predict the fold during deformation, self contact will be assigned for Billet.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0055.jpg' | relative_url }})

Contact Generation page

Highlight the T**op Die – Billet relationship** and click the ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) button to modify the contact conditions. In the friction section of the screen (See Fig. L3.52.), there is a pull-down menu that allows the user to choose the appropriate friction conditions of common forming processes.

Since this simulation takes place at room temperature, and the dies are steel, use the pull down menu and select Cold forming (steel dies) from the list. A friction value of 0.12 will automatically be selected.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0028.jpg' | relative_url }})

Inter-Object data definition window

Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to go back to Inter-Object window, Since the friction conditions are the same for all the object pairs, the ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) button can be used to copy the interface properties from the first relationship to all of the others. After this is done, all relationships will have a friction of 0.12 defined. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Step page.

### Step

Change the Operation Name to "**Block** ", uncheck the Heat transfer mode check box, Set the **Number of Simulation Steps** to **100** and the **Step Increment to Save** to **5**. Select the Primary Die to Top Die, and under Steps increment, set With **Constant Die Displacement** to **0.01** ". Under **Stop** \- **Process Parameters** tab, define **Primary die displacement** value as (**0** , **0.5**) inch as shown in Fig. L3.53. This will stop the simulation after the top die has moved 0.5" in the -Y direction. Then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0047.jpg' | relative_url }})

Step Controls Stop tab in expert mode

### Generate Database

Save a keyword file for the problem by selecting the File menu Export option.

In Generate DB page. Click the ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) button to have the program check to see if anything was missed in the problem setup.

Click on the ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database. When the program is done writing the database, switch to tab to run simulation.

### Starting the Simulation

Start the simulation by clicking the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label, use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation. When the simulation is finished we can observe that the following message is added to the end of the Message file:

" PROGRAM STOPPED!

THE STROKE -0.5000000 HAS EXCEEDED THE SPECIFIED LIMIT 0.5000000"

### Post processing the results

After simulation complete, Switch to ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) button MO post processor will open (See Fig. L3.54.).

Play through the steps to see whether a fold develops. To see this better, you may need to zoom in on the interface between the top die and the workpiece.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0048.jpg' | relative_url }})

MO Postprocessor window

### Flownet

Now go back to second operation first step, click on ![]({{ '/assets/icons/post_icons/mo_flownet_icon.jpg' | relative_url }}). In Flownet window select **Offset** type flownet (See Fig. L3.55.), then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0049.jpg' | relative_url }})

Flownet window

Use 0.01 in as Offset distance value, then click ![]({{ '/assets/icons/post_icons/mo_preview_button.jpg' | relative_url }}). The Preview will show the offset border of the billet (See Fig. L3.56.), then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0050.jpg' | relative_url }})

Offset window

In Advanced option page, we can save the Starting Flownet pattern, End Flownet pattern and results. Click on ![]({{ '/assets/icons/post_icons/mo_generate_button.jpg' | relative_url }}) button to generate the Flownet (See Fig. L3.57.). Then play the animation by clicking Play button and observe the billet boundary. We can observe that a fold is occurred on the billet closer to the Top die outer edge as shown in Fig. L3.58.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0051.jpg' | relative_url }})

Flownet Generation window

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0052.jpg' | relative_url }})

Last step Billet display

###  Load Stroke-Graph

Go to second operation first step from Step browser and click the ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) icon, the Load Stroke Graph window will open. Select the Top Die in Plot object list, from X-Axis pull down menu select Stroke and Y-Axis pull down menu select Y Load. Click on options tab and check Step tracer check box, then click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). Load-Stroke graph for Block operation is plotted as shown in Fig. L3.59.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0053.jpg' | relative_url }})

Load-Stroke Graph plot

Plot Load Stroke Graph for both the operation by selecting All in Operation pull down list and click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}), Load-Stroke graph will be plot for both the operation as shown in Fig. L3.60.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0054.jpg' | relative_url }})

Load-Stroke Graph plot for all Operation

## Close MO Wizard

After completion of Post processing, Save the Project and close the MO wizard by clicking ![]({{ '/assets/icons/pre_icons/mo_quit_icon.jpg' | relative_url }}) Close button or selecting Quit option under File menu.

**Related Topics:**

[12.1. 2D Geometry Data Defining ](/docs/en/pre_processor/12_geometry_modelling/12_1_2d_geometry_data_defining/)

[12.2. 2D Geometry Data Editing](/docs/en/pre_processor/12_geometry_modelling/12_2_2d_geometry_editing/)

[13.1. 2D Mesh Generation](/docs/en/pre_processor/13_mesh_generation/13_1_2d_mesh_generation/)

[14\. Boundary Conditions](/docs/en/pre_processor/14_boundary_conditions/14_boundary_conditions/)

[15\. Movement Controls Settings](/docs/en/pre_processor/15_movement_controls_definition/15_movement_controls_settings/)

[16\. Object Properties](/docs/en/pre_processor/16_object_properties/16_object_properties/)

[17\. Object Data Initialize](/docs/en/pre_processor/17_object_data_initialization/17_object_data_initialize/)

[19\. Object Positioning](/docs/en/pre_processor/19_object_positioning/19_object_positioning/)

[20\. Inter-Object Data Definition](/docs/en/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/)

[9\. Simulation Controls](/docs/en/pre_processor/9_simulation_controls/9_simulation_controls/)

[6.3. Integrated Manufacturing Process Post-processor layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_3_integrated_manufacturing_process_post_layout/)

[25\. Post Processor Layout](/docs/en/post_processor/25_post_processor_layout/25_post_processor_layout/)

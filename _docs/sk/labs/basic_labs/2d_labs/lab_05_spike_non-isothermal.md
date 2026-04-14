---
lang: sk
title: "Lab 05 Spike Non-Isothermal"
---

# Lab 05 Spike Non-Isothermal

5.1. Creating a New Problem

5.2. Adding Operation

5.3. Geometry type selection

5.4. Loading Materials of Workpiece and Dies

5.5. Adding Objects

5.6. Workpiece Setup

5.7. Top Die Setup

5.8. Bottom Die Setup

5.9. Positioning Controls

5.10. Inter-Object Contact Generation

5.11. Step

5.12. Generating Database

5.13. Starting the Simulation

5.14. Post-Processing the Results

## Creating a New Problem

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear. as shown in below Fig. L5.1.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0001.jpg' | relative_url }})

DEFORM GUI main window

Create a new problem either by selecting **File** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in Fig. L5.2. Select "**Integrated Manufacturing Process** " radio button and unit system as "**English** " radio button in unit field. Define Problem Name as " ******Spike_Nonisothermal** " and make sure the “**Show option dialog** ” check box is turned on (if we do not turn on the “Show option dialog” check box, then we will not get the New Project dialog). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

Problem type selection window

Multiple operation wizard will open with the New Project dialog (see Fig. L5.3.), at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session we use ‘**Spike_Nonisothermal** ’ as the project name.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0001.jpg' | relative_url }})

New Project popup with MO window

User can also change the Unit system (File menu selected unit system will be selected by default) and add operation by selecting from First operation pull down list and checkbox (see Fig. L5.4.), in this lab we will add 2D Forming operation from Explorer operation list, so do not check "First operation" check box and " 2D Forming" operation in "New Project" dialog. Using copy Existing project option we can import previous saved projects as new project. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0002.jpg' | relative_url }})

Selecting First operation in New project dialog

## Adding Operation

Once you click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button, a Multiple Operation wizard will open to setup the problem. Add 2D Forming operation from Operations list in Explorer. Operation can be add by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button next to 2D Forming operation or user can also add the operation by dragging and dropping the operation into Operation Editor region. (See Fig. L5.5.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0003.jpg' | relative_url }})

Add 2D Forming operation into Operation Editor

## Geometry type selection

In this lab we are using Axisymmetric geometries, so select **2D Axisymmetric** radio button in Geometry type ( Fig. L5.6.), then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Material page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0004.jpg' | relative_url }})

Axisymmetric Geometry type selection

## Loading Materials of Workpiece and Dies

In Material list window, load the material **AISI-1025[1800-2200F(1000-1200C)]** from DEFORM Material library, from **Steel category** using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load material data from library) option and load **AISI-H-13** material from **Die_material** category. This can be done as shown in below Fig. L5.7. by clicking ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}) button.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0005.jpg' | relative_url }})

Material Library Window

Material can also be assigned from Material List in Explorer, by clicking ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button next to AISI-1025[1800-2200F(1000-1200C)] or user can also add by drag and drop the material into the Material list region as shown in Fig. L5.8. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until object window.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0006.jpg' | relative_url }})

Explorer material list

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0007.jpg' | relative_url }})

Material Window

## Adding Objects

In Object window, if there aren't already three objects, add the three objects by clicking the ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }})button. The three objects will be named as Workpiece, Top Die and Bottom Die. (See Fig. L5.10.), then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0008.jpg' | relative_url }})

Object window 

## Workpiece Setup

In Workpiece window, change the Object Name to **Billet** , Set the initial billet Temperature as **1800°** F and select Object type as **Plastic** as shown in Fig. L5.11. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }})..

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0009.jpg' | relative_url }})

Billet object Window

### Loading Billet Geometry

In Geometry window, load **Spike_Billet.IGS** geometry file from library using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load geometry from library) option or can also be imported using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Load geometry from a file) option as shown in Fig. L5.12. The geometry is located in DEFORM installation folder \2D\Labs directory.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0010.jpg' | relative_url }})

Billet Geometry window

By default, the ![]({{ '/assets/icons/pre_icons/mo_show_geometry_inside_mark_radio_button.jpg' | relative_url }}) option should be check marked and the shading defining the orientation of the geometry should be visible. When the object is oriented correctly (points ordered counter-clockwise), the shading will appear on the inside of the object.

The points defining this imported geometry can be viewed/edited by clicking the ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}) button. When .IGS files are loaded, the data gets imported into DEFORM in Line-Arc format, which defines the geometry in terms of lines and arcs. To view the XYR format of the geometry, click the **XYR** button. (See Fig. L5.13.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0011.jpg' | relative_url }})

Geometry Data

Whenever geometry is imported, it should be checked. Click the ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) button and then the ![]({{ '/assets/icons/pre_icons/mo_check_and_correct_geo_button.jpg' | relative_url }}) button. This not only fixes any problems with the geometry but also corrects the orientation of the geometry, if needed. Notice how checking this geometry changed the orientation from clockwise to counter-clockwise, which is correct see Fig. L5.14.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0014.jpg' | relative_url }})

Check and correct geometry

### Generating mesh for Billet

Switch to Expert mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) (Switch to expert mode) icon from the tool bar. Expert mode will provide more options for detailed settings.

We would like to put an initial mesh on the billet with more elements near the top right corner, where the largest deformation will initially be. You can do this with either mesh windows or user-defined mesh values. For this lab, we will use user-defined values to put the initial mesh on the billet. 

In Mesh page activate the ![]({{ '/assets/icons/pre_icons/mo_user_defined_radio_button.jpg' | relative_url }}) in Geometry page. We want the upper right corner of the billet to have a mesh that is four times finer than the mesh at the other three corners. To accomplish this, we are going to assign a mesh size of 1 to the upper right corner and a mesh size of 4 to the other corners.

Set the Element Size to 1 and click the upper right corner of the Billet, and then set the Element Size to 4 and click the other three corners. Set the **Number of Elements** to **400** and click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button. The mesh that is generated should look like shown Fig. L5.15. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0012.jpg' | relative_url }})

Billet Mesh window

We are using user-defined mesh to define the initial mesh. When these user-defined values are used, the Weighting Factors are not considered. The user-defined values, however, can only be used to define the initial mesh. If a remesh is necessary during the simulation, the Weighting Factors are used to define the new mesh.

We want to set one more meshing related parameter. There are several criteria that will trigger a remesh of the billet during a simulation. One of them is called the Interference Depth, which is the distance a tool is allowed to penetrate into the workpiece.

A good value to use for the interference depth is approximately a third of the smallest element size of the deforming object. Zoom in on the upper right corner of the Billet using the ![]({{ '/assets/icons/pre_icons/mo_box_zoom_icon.jpg' | relative_url }}) icon and then use ![]({{ '/assets/icons/pre_icons/mo_measure_tool_icon.jpg' | relative_url }}) to measure a small element edge length. The value for the **Interference Depth** will be somewhere around .038 / 3 = **.013** and should be set in the Remesh Criteria tab. (See Fig. L5.16.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0013.jpg' | relative_url }})

Remeshing criteria window

### Assign Workpiece material

To assign material for workpiece select the material **AISI-1025[1800-2200F(1000-1200C)]** from material window. This can be done as shown in below Fig. L5.17., then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0014.jpg' | relative_url }})

Assigning Billet material

### Workpiece BCC

In BCC page, check the default assigned Deformation BCC for Left side of the workpiece in X-Direction and Heat exchange with Environment BCC to the entire outer surface of the Billet (which does not include the centerline since these nodes are inside the object). If the BCC is not assigned, assign manually as shown in below Fig. L5.18. and Fig. L5.19. Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top Die page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0015.jpg' | relative_url }})

Assigned Velocity BCC for Workpiece

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0016.jpg' | relative_url }})

Assigned Heat Exchange with Environment BCC for Workpiece

## Top Die Setup

In Top die page (see Fig. L5.20.) select Object type as **Rigid** and assign object **Temperature** as **300** °F, then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0017.jpg' | relative_url }})

Top die page

###  Loading Top die Geometry

In Geometry window, load **Spike_TopDie.IGS** geometry file from library using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load geometry from library) option or can also be imported using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Load geometry from a file) option as shown in Fig. L5.21.The geometry is located in DEFORM installation folder \2D\Labs directory. Check the geometry using ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) option to make sure the geometry is OK. Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0010.jpg' | relative_url }})

Top Die Geometry page

### Generating mesh for Top die

Set the **number of elements** to **250** and click ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). The Weighting Factors will be used to distribute the 250 elements. The default setting is to weight highly on Surface Curvature. Notice how the curved section of the die has smaller elements than the flat sections. (See Fig. L5.22.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0018.jpg' | relative_url }})

Top Die mesh page

### Assign Material for Top die

Assign **AISI-H-13** material for Top die by selecting **AISI-H-13** in Material list as shown in Fig. L5.23., then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) .

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0019.jpg' | relative_url }})

Assigning Top die material form Material list

### Top Die BCC

Check the default assigned Heat exchange with Environment BCC for Top Die and make sure that default assigned Heat Exchange with Environment BCC is assigned to the entire outer surface of the top die (see Fig. L5.24.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0020.jpg' | relative_url }})

Top Die BCC page

### Assign Movement to Top Die

Define a **speed** of **2** **in/sec** in**-Y** direction (see Fig. L5.25.). Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Bottom die page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0021.jpg' | relative_url }})

Top Die Movement page

##  Bottom Die Setup

In Bottom die page (see Fig. L5.26.) select Object type as **Rigid** and assign object Temperature as **300** °F, then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0022.jpg' | relative_url }})

Bottom Die page

### Loading Bottom Die geometry

In Geometry window, load **Spike_BottomDie.IGS** geometry file from library using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})(Load geometry from library) option or can also be imported using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Load geometry from a file) option. The geometry is located in DEFORM installation folder \2D\Labs directory. Check the geometry using ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) option to make sure the geometry is OK. Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Generating mesh for Bottom Die

Set the **number of elements** to **250** and with default mesh setting generate mesh by clicking ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button (see Fig. L5.27.). Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0023.jpg' | relative_url }})

Bottom Die Mesh page

### Assign Material for Bottom Die

Assign **AISI-H-13** material for Bottom die by selecting AISI-H-13 in Material list as shown in Fig. L5.28., then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0019.jpg' | relative_url }})

Bottom Die Movement page

### Bottom die BCC

Check the default assigned Heat exchange with Environment BCC for Bottom Die and make sure that default assigned Heat Exchange with Environment BCC is assigned to the entire outer surface of the Bottom die (which does not include the centerline since these nodes are inside the die) (see Fig. L5.29.). Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Positioning page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0024.jpg' | relative_url }})

Bottom Die BCC page

## Positioning

In this lab we will position the Top die over the Billet Using position objects Interference option. Click on ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) button, select Interference option![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}), select Positioning object as Top Die and Reference object as Billet, select Approach direction as -Y direction and click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). Top die will position on Billet as shown in Fig. L5.30. Then click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Contact page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0025.jpg' | relative_url }})

Object Positioning page

## Contact

Select **user** type contact and click on ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) button. It will add the relationship between the Billet, Top Die and Bottom Die as shown in Fig. L5.31.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0026.jpg' | relative_url }})

Contact page

Highlight the **Top Die – Billet** relationship and click the ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) button to modify the relationship. In the friction section of the screen (see Fig. L5.32.), there is a pull-down menu that allows the user to choose the appropriate friction conditions of common forming processes.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0027.jpg' | relative_url }})

Inter Object Relation Deformation page

In Friction pull down menu select **Hot forging (lubricated)** from the list, a friction value of **0.3** will be added to the Constant friction field. Under **Thermal tab** select **Forming** type Heat transfer coefficient in List. **0.004** value will be added to Heat transfer coefficient field. (See Fig. L5.33.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0028.jpg' | relative_url }})

Inter Object Relation Thermal page

Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to go back to Inter-Object window, Since the friction conditions are the same for all the object pairs, the ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) button can be used to copy the interface properties from the first relationship to all of the others. After this is done, all relationships will have a friction of 0.3 defined. Use ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) icon to determine a suitable contact tolerance (a value of about 0.0012566" will be calculated) , then click ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) button to generate contact. If you rotate the objects around in graphics window, you will see that contact was generated between the two objects. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Step window.

## Step

Change the Operation name as " **Spike_Nonisothermal** " as shown in Fig. L5.34.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0029.jpg' | relative_url }})

Step controls Main tab in expert mode

Select the simulations steps tab (![]({{ '/assets/icons/pre_icons/mo_simulation_step.jpg' | relative_url }})), set the **Number of Simulation Steps** to **100** and **Step Increment to Save** to **5**. Set the **Top Die** as **Primary****Die**. (See Fig. L5.35.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0030.jpg' | relative_url }})

Step controls Simulation Steps tab in expert mode

To determine an appropriate step size, select the icon and measure the edge length of a few of the smaller elements in the Billet. An average length of a short edge is around 0.035”. Use a Constant**Die Displacement** per step of **0.015** in/step, which is 1/3 of this small edge length in step increment tab ( ![]({{ '/assets/icons/pre_icons/mo_step_increment.jpg' | relative_url }})) for step size as die displacement (see Fig. L5.36.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0031.jpg' | relative_url }})

Step controls Step increment tab in expert mode

Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) and save a keyword file for the problem by selecting the File menu Export option.

## Generating Database

Once the problem has been completely set up, the last step is to generate a database file. The FEM engine (the part of DEFORM® that calculates the solution) uses a database file to store the finite element solutions for the problem. When you generate a database in the DEFORM MO Pre-processor, all of the information defined in the Pre-processor (such as the material properties, movement controls, object geometries, etc.) is transferred to the database file.

In Generate DB page. Click the ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) button to have the program check to see if anything was missed in the problem setup. During the checking process:

Messages in the red color signify data that needs to be fixed before a simulation can be run (such as when you forget to define any material data). 

Click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database. When the program is done writing the database, click on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) tab to run simulation.

## Starting the Simulation

Click on ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) under the simulation tab (See Fig. L5.37.), as we click on the Run option, Run simulation dialog will open (See Fig. L5.38.). Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0032.jpg' | relative_url }})

Simulation Options

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0038.jpg' | relative_url }})

Run Simulation window

The progress of the simulation can be monitored as it is running by looking at the Simulation Message and Simulation Graphics in Simulation mode. Click the Simulation Message tab to view the Message file. As long as the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked, which is the default setting, the Message file will refresh every couple of seconds.

The Message file provides information about which simulation step the simulation is currently on and also gives information dealing with how well the simulation is running.

When the simulation has finished, the following message will be added to the end of the Message file:"NORMAL STOP: Simulation is completed and stopped at the user specified time step". (See Fig. L5.39.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0032.jpg' | relative_url }})

Simulation Message Tab

## Post-Processing the Results

After simulation has been completed, click on ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) tab, MO post processor will open. (See Fig. L5.40.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0033.jpg' | relative_url }})

MO Post Processor window

### State Variable

Click on ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) button, then select **Temperature** from the State Variable Temperature menu, click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) and right-click on the **Color Bar** in the Display window and select **Temperature** as the Color Bar Type. Also, with the Billet selected in the Object Tree, click the ![]({{ '/assets/icons/pre_icons/mo_show_cotact_icon.jpg' | relative_url }}) button to view the contact between the workpiece and the dies. (See Fig. L5.41.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0034.jpg' | relative_url }})

Plot Temperature state variable

Play through the steps. Pay particular attention to the thermal behavior between the billet and the dies. Since the dies are meshed, they are allowed to heat up where they are in contact with the hot billet. Likewise, the billet chills where it is in contact with the cooler dies.

### Flownet

The Post-processor has features that help a user better understand how an object deforms during a simulation. One of these features is called Flow net. A flow net is a pattern that can be applied to the cross-section of an object which will deform with the object. The deformation of the pattern will yield clues to how a particular area deforms.

Click the ![]({{ '/assets/icons/post_icons/mo_flownet_icon.jpg' | relative_url }}) icon to open the Flownet window. We want to define a pattern to the undeformed billet and then watch how the pattern deforms through the simulation. Select Grid type (See Fig. L5.42.) then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0035.jpg' | relative_url }})

Flownet window

Set the **Number of Grids** to **10** in the**X direction** and **20** in the **Y direction**. Click ![]({{ '/assets/icons/post_icons/mo_preview_button.jpg' | relative_url }}) to see this initial grid pattern. (See Fig. L5.43.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0036.jpg' | relative_url }})

Grid Flownet window

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) and then click ![]({{ '/assets/icons/post_icons/mo_generate_button.jpg' | relative_url }}) to generate the flow net. When the flow net is finished generating, click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to close Flownet. Play through the steps to see how the flow net pattern deforms. (See Fig. L5.44.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_05_spike_non_isothermal/2d_mobl5_image0037.jpg' | relative_url }})

Flownet Assigned Billet

In order to continue with the Die Stress lab for this problem do not close the MO project Refer the [Lab 06 Die Stress](/docs/sk/labs/basic_labs/2d_labs/lab_06_die_stress/).

**Related Topics:**

[12.1. 2D Geometry Data Defining ](/docs/sk/pre_processor/12_geometry_modelling/12_1_2d_geometry_data_defining/)

[12.2. 2D Geometry Data Editing](/docs/sk/pre_processor/12_geometry_modelling/12_2_2d_geometry_editing/)

[13.1. 2D Mesh Generation](/docs/sk/pre_processor/13_mesh_generation/13_1_2d_mesh_generation/)

[14\. Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/)

[15\. Movement Controls Settings](/docs/sk/pre_processor/15_movement_controls_definition/15_movement_controls_settings/)

[17\. Object Data Initialize](/docs/sk/pre_processor/17_object_data_initialization/17_object_data_initialize/)

[19\. Object Positioning](/docs/sk/pre_processor/19_object_positioning/19_object_positioning/)

[20\. Inter-Object Data Definition](/docs/sk/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/)

[9\. Simulation Controls](/docs/sk/pre_processor/9_simulation_controls/9_simulation_controls/)

[6.3. Integrated Manufacturing Process Post-processor layout](/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_3_integrated_manufacturing_process_post_layout/)

[25\. Post Processor Layout](/docs/sk/post_processor/25_post_processor_layout/25_post_processor_layout/)

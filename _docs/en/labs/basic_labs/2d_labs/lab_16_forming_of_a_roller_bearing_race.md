---
lang: en
title: "Lab 16 Forming of a Roller Bearing race using a Porous material"
---

# Lab 16 FORMING OF A ROLLER BEARING RACE USING A POROUS MATERIAL

This lab will simulate the forming of the tapered roller bearing race, shown below, using a porous material. Since this part is axisymmetric, only a section of it will be modelled and simulated. The dies will be rigid. For simplicity, the top die/mandrel combination will be modelled as a single object. 

16.1 Creating a New Problem

16.2 Adding Operation

16.3. Geometry type selection

16.4. Simulation Controls

16.5. Loading material for Workpiece

16.6. Adding Objects

16.7. Workpiece

16.8. Top Die

16.9. Bottom Die

16.10. Object Positioning

16.11. Schedule Inter-Object Contact Relationships

16.12. Define Stopping Control

16.13. Define Step Controls for Forming

16.14. Generating Database

16.15. Starting the Simulation

16.16. Post-Processing the Results

## Creating a New Problem

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear. as shown in below Fig. L16.1.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image0001.jpg' | relative_url }})

DEFORM GUI main window

Create a new problem either by selecting **File** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in Fig. L16.2. Select "**Integrated Manufacturing Process** " radio button and unit system as "**English** ". Define Problem Name as "**Porous_Race** " see Fig. L16.2. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image0002.jpg' | relative_url }})

Problem type selection window

## Adding Operation

In Multiple operation wizard, add **2D Forming** operation from the Explorer![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})Operations list. Add the operation by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button available next to 2D Forming Operation or user can also add by drag and drop into the Operation Editor. When we add the 2D Forming operation, process settings window will be opened by default (see Fig. L16.3.).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image0003.jpg' | relative_url }})

Add 2D Forming operation

## Geometry type selection

In this lab we are using Axisymmetric geometries, so select **2D Axisymmetric** radio button in Geometry type ( Fig. L16.4.), then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) .

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image0004.jpg' | relative_url }})

Geometry type selection

## Simulation Controls

In this lab we will be showing how to setup simple Isothermal problem. So, in Simulation controls **uncheck** the **Heat****transfer** mode check box (see Fig. L16.5.) and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image0005.jpg' | relative_url }})

Simulation control window

## Loading material for Workpiece

In material list window, load the material '**AISI-4340 [1550-2200 F]'** from DEFORM Material library, **Steel** category using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})(Load material data from library) option. This can be done as shown in Fig. L16.6. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Object page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image0006.jpg' | relative_url }})

Material Library Window

## Adding Objects

For this operation we need three objects, if there aren't already three objects, add three objects by clicking the ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) button. The three objects will be named as Workpiece, Top Die and Bottom Die. (See Fig. L16.7.), then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image0007.jpg' | relative_url }})

Adding Object Window

## Workpiece

In Workpiece window, change the Object Name to **Race** and change temp to **2000** F and select Object type as Porous (Plastic) as shown in Fig. L16.8. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image0008.jpg' | relative_url }})

Billet object Window

### Loading Billet Geometry

In Geometry window, load **PM_pre.igs** geometry file from library using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load geometry from library) option or can also be imported from DEFORM installation folder \2D\LABS directory using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Load geometry from a file) option as shown in Fig. L16.9.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image0009.jpg' | relative_url }})

Race Geometry window

### Generate Workpiece Mesh

Set number of elements to **1000** and click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button to generate mesh for the Race object (see Fig. L16.10.). Complete range of meshing options are available in expert mode (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})) if user needs to have more control on the mesh generated. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image00010.jpg' | relative_url }})

Mesh page

### Assign Workpiece Material

To assign material for Race, select the material ‘**AISI****-4340** ’ from material window. This can be done as shown in Fig. L16.11. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image00011.jpg' | relative_url }})

Material page

### Workpiece Density initialize

In Initialization page, click on “**Major** ” tab and define **Density** value as “**0.9** ” as shown in Fig. L16.12. and then click on ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}) button to initialize the value for entire Workpiece. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image00012.jpg' | relative_url }})

Initialize page

## Top Die

In Top Die page ( see Fig. L16.13.), select Object type as **Rigid** and Turn on **Primary****die****check****box** as Top die will have movement definition assigned to it, click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image00029.jpg' | relative_url }})

Initialize page

### Loading Top Die Geometry

In Geometry window, load **PM_top.igs** geometry file from library using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load geometry from library) option or can also be imported using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }})(Load geometry from a file) option from DEFORM installation folder \2D\Labs directory as shown in Fig. L16.14. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top Die movement page.

  
![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image00013.jpg' | relative_url }})

Top Die geometry page

### Assign Movement to Top Die

In Top Die Movement page, define **Speed** as **7** in/sec in **-Y** direction for this lab (See Fig. L16.15.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Bottom Die page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image00014.jpg' | relative_url }})

Top Die Movement page

## Bottom Die

In Bottom Die page, select Object type as **Rigid** and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) (See Fig. L16.16.).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image00015.jpg' | relative_url }})

Bottom Die page

### Loading Bottom Die Geometry

In Geometry window, load **PM_btm.igs** geometry file from library using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})(Load geometry from library) option or can also be imported using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }})(Load geometry from a file) option from DEFORM installation folder \2D\Labs directory. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Positioning page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image00016.jpg' | relative_url }})

Bottom Die geometry page

## Object Positioning

We will first move the Top Die and Bottom Die away from the Race so that we can position both the Top Die and Bottom Die correctly with respect to Race object.

To accomplish this first click on ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) button. Select the Top Die, select ‘**Offset’** method and define distance vector as (x=0, y=2). Click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) to move the Top Die away from the Race. (see Fig. L16.18.) Similarly, select the Bottom Die, using “**Offset** ” method and distance vector as (x=0, y=-2) move the Bottom Die away from the Race.

We will position Top Die over the Race using Interference positioning in **-Y** direction. Select the ‘**Interference** ’ method, ‘Positioning object’ as ‘**Top********Die** ’ and Reference object as ‘**Race** ’ as shown in Fig. L16.19. Click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) to position the Top Die. Similarly, position the ‘Bottom Die’ using the interference method in +Y direction. After positioning, the setup should look like as shown in Fig. L16.20. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Contact page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image00017.jpg' | relative_url }})

Offset Object positioning

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image00018.jpg' | relative_url }})

Interference Object positioning

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image00019.jpg' | relative_url }})

After positioning the objects

## Schedule Inter-Object Contact Relationships

In Contact page, select User type contact and click on ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) button. It will add the relationship between the Race, Top Die and Bottom Die (see Fig. L16.21.). As the Dies are Rigid and Race is plastic, Top and Bottom Dies are considered as Master and Billet as Slave.

Highlight the Top **Die – Race** relationship and click the ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) button to modify the contact conditions. In the friction section of the screen (see Fig. L16.21.), there is a pull-down menu that allows the user to choose the appropriate friction conditions of common forming processes.

Since this is hot forming simulation and the dies are steel, use the pull down menu and select **Hot forming (lubricated)** from the list. A friction value of **0.3** will be automatically selected.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image00020.jpg' | relative_url }})

Inter-object friction coefficient definition window

Click on![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to go back Contact page, since the friction conditions are the same for all the object pairs, ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) button can be used to copy the interface properties from the first relationship to all of the others. After this is done, all relationships will have a friction of 0.3 defined as shown in Fig. L16.22. Turn on Initialize and Generate check boxes so that the contact will be initialized and generated while generating database. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define stopping controls.

  
![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image00021.jpg' | relative_url }})

Inter-Object relationship definition for forming operation

## Define Stopping Control

In stopping control window, check the Max. die stroke stopping control and define**primary die displacement** as (0,**0.915**) as shown in Fig. L16.23. Advanced stopping options are available in Expert mode (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) ). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define the step controls.

  
![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image00022.jpg' | relative_url }})

Die stroke stopping control

## Define Step Controls for Forming

In step controls window, define **Number of steps** as **100** , **0.0092** ” as **Die displacement per step** , Step increment to save as **5** , the Top Die selected as Primary die in object page is shown as Primary die in Step page as shown in Fig. L16.24.

  
![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image00023.jpg' | relative_url }})

Step controls settings

## Generating Database 

In Generate DB page, click on ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) button to have the program check to see if anything was missed in the problem setup. During the checking process, messages in the red color signify data that needs to be fixed before a simulation can be run (such as when you forget to define any material data).  
  
Click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database. When the program is done writing the database, switch to the Simulation mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the operation tree.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image00024.jpg' | relative_url }})

Generate DB page

## Starting the Simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label under the simulation tab (See Fig. L16.26.), Run Options dialog will open as shown in Fig. L16.27. Use the default Continue **Run option** →“**Continue****from the last step** ” option, select **Interactive** radio button to run the simulation in interactive mode.Click on button to run the simulation.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image00025.jpg' | relative_url }})

Simulation options

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image00026.jpg' | relative_url }})

Run Simulation window

## Post-Processing the Results

After simulation has been completed, switch to ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) tab to view results, MO post processor will open. (See Fig. L16.28.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image00027.jpg' | relative_url }})

MO Post Processor window

**State Variable**

Click on ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) button and select **Density** from the State Variable Deformation menu, click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). Fig. L16.29. shows density distribution in the Race at the last step of the deformation.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_16_forming_of_a_roller_bearing/2d_mobl16_image00028.jpg' | relative_url }})

Plot Density state variable

**Related Topics:**

[12.1. 2D Geometry Data Defining ](/docs/en/pre_processor/12_geometry_modelling/12_1_2d_geometry_data_defining/)

[12.2. 2D Geometry Data Editing](/docs/en/pre_processor/12_geometry_modelling/12_2_2d_geometry_editing/)

[13.1. 2D Mesh Generation](/docs/en/pre_processor/13_mesh_generation/13_1_2d_mesh_generation/)

[14\. Boundary Conditions](/docs/en/pre_processor/14_boundary_conditions/14_boundary_conditions/)

[15\. Movement Controls Settings](/docs/en/pre_processor/15_movement_controls_definition/15_movement_controls_settings/)

[17\. Object Data Initialize](/docs/en/pre_processor/17_object_data_initialization/17_object_data_initialize/)

[19\. Object Positioning](/docs/en/pre_processor/19_object_positioning/19_object_positioning/)

[20\. Inter-Object Data Definition](/docs/en/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/)

[9\. Simulation Controls](/docs/en/pre_processor/9_simulation_controls/9_simulation_controls/)

[6.3. Integrated Manufacturing Process Post-processor layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_3_integrated_manufacturing_process_post_layout/)

[25\. Post Processor Layout](/docs/en/post_processor/25_post_processor_layout/25_post_processor_layout/)

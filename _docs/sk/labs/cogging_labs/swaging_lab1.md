---
lang: sk
title: "Swaging Lab1"
---

# Swaging Lab1

In this lab for quarter symmetry 3d model **Infeed swaging** operation setup is demonstrated using ICFG example.

1.1. Creating New Problem

1.2. How to add 3D Swaging operation

1.3. Define Swaging Process Settings

1.4. Define pass table data

1.5. Load material

1.6. Define Workpiece Object

1.7. Define Top die Object

1.8. Defining Inter-object relations

1.9 Preview the Swaging pass

1.10. Define Simulation controls

1.11. Check and Generate Database

1.12. Submit to Simulate

1.13. Post process the Results

1.14. Setting up the Swaging Explicit setup

## Creating New Problem

Create a new problem either by selecting **File** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in Fig. 3DSWL1.1. Select "**Integrated Manufacturing Process** " radio button and unit system as "**SI** " radio button in unit field. Define Problem Name as "******Swaging_ICFG_Ex** " and make sure the “Show option dialog” check box is turned on (if we do not turn on the “**Show option dialog** ” check box, then we will not get the New Project dialog in MO UI). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/applications/55_2_arc_welding/image0002.jpg' | relative_url }})

Opening New Problem

Multiple operation wizard will open with the New Project dialog as shown in Fig. 3DSWL1.2., at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In Problem Name popup define Problem Name as "**Swaging_ICFG_Ex** " as the project name as shown in Fig. 3DSWL1.2.

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0002.jpg' | relative_url }})

Add new Project Name and Unit System

## How to add 3D Swaging operation

Add swaging operation from MO explorer by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button next to **Cogging** operation or user can also add by drag and drop into the Operation Editor as shown in Fig. 3DSWL1.3.

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0003.jpg' | relative_url }})

Add Swaging operation from operation explorer

## Define Swaging Process Settings

Select the Swaging process type radio button and enter the stroke value as**1.9** mm as shown in Fig. 3DSWL1.4. User must enter the swaging stroke value so it stops the simulation after each bite if it crosses the stroke of primary die in movement direction.

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0004.jpg' | relative_url }})

Swaging Process window

As this is cold forging operation select temperature calculation as **Cold-Isothermal**. Select **4 dies** and **uncheck****Use****Manipulators** checkbox they are normally used in cogging operation to hold the workpiece.

For symmetric setup select **Use Rotational Symmetry** checkbox this gives the respective geometry primitives and generates the necessary boundary conditions by default. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define the swaging pass data.

## Define pass table data

Swaging entire pass information like Number of bites, Axial die feed per bite, Radial die feed per bite, Die Movement direction, Workpiece rotation per bite, workpiece rotation per pass and die positioning can be entered in pass table. New pass can be added by using the icon similarly added pass can be deleted using icon. Pass information is copied from previous pass whenever a new pass is added and necessary information can be edited based on the process requirement.

Enter **number of bites** as **2500** , Die **Axial feed per bite** **0.027** mm, workpiece **rotation per bite** to **22.56** , leave the Die movement direction as –X and select**Die start positioning****method** as "**3-ofst** " as shown in Fig. 3DSWL1.5.

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to load the material for workpiece.

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0005.jpg' | relative_url }})

Pass table information

## Load material

Load the material “**Steel****16MnCr5** ” from DEFORM installation path \3d\LABS\ folder "**Steel 16MnCr5.key** " file using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (load material from file) option, system popups a dialog with material list and list is the materials available in the keyword file as there is only one material in key file click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) as shown in Fig. 3DSWL1.6.

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0006.jpg' | relative_url }})

Load material from file

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Object window leaving the defaults as axial subdivision is intended for cogging where huge deformation takes place and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to go for Workpiece object window.

## Define Workpiece object

Leave the object name as **Billet** and default object type **Plastic** as it is. Assign the temperature to **20** °C as shown in Fig. 3DSWL1.7. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define the Geometry for billet.

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0007.jpg' | relative_url }})

Billet object window

### Define Billet Geometry

Click on ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) geometry option to define the geometry using primitives as shown in Fig. 3DSWL1.8.

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0008.jpg' | relative_url }})

Geometry window

Enter the **Length****130** mm, **Inner****diameter****24** mm and **Outer****diameter****30** mm to create the symmetric geometry as shown in Fig. 3DSWL1.9. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the Geometry Primitive.

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0009.jpg' | relative_url }})

Billet 3D Geometry

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) for 2D Cross-section window and observe the 2D geometry extracted from the 3D geometry used for brick mesh generation as shown in Fig. 3DSWL1.10.

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0010.jpg' | relative_url }})

Billet 2D extracted geometry

### Define Billet Mesh

Select brick mesh radio button and enter number of **elements** to **390** , **Size ratio** **1** and # of **layers** to **47** and generate the mesh clicking on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button and click ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}) in "Default Boundary conditions" popup.

For 2D cross section geometry as observed in Fig. 3DSWL1.10. system generates **390** mesh elements and revolve about 90 deg in 47 layers as shown in Fig. 3DSWL1.11. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Material page.

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0011.jpg' | relative_url }})

Billet mesh window

### Assign Material for Billet

Select the loaded material “**Steel****16MnCr5** ” from material list to assign it to workpiece as shown in Fig. 3DSWL1.12.

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0012.jpg' | relative_url }})

Assign billet material

### Define Boundary Conditions

Observe the system assigned default rotational symmetry BCC and Fixed velocity at the free end of the billet BCC as shown in Fig. 3DSWL1.13. and Fig. 3DSWL1.14. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top die page to define Top die.

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0013.jpg' | relative_url }})

Rotational Symmetry BCC

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0014.jpg' | relative_url }})

Velocity BCC

## Define Top die Object

Leave the object name as **Top die** and default object type **Rigid** as it is and assign the temperature to **20** °C as shown in Fig. 3DSWL1.15. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0015.jpg' | relative_url }})

Top die object page

### Define Die geometry

Import the Die geometry **Swaging_ICFG_Die_SI.stl** from installation path \3d\LABS\ folder as shown in Fig. 3DSWL1.16.

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0016.jpg' | relative_url }})

Importing Die geometry

For User library popup asking to use the current geometry file browsed location as default library location. By default 3d LABS path will geometry library path, so click ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}).(See Fig. 3DSWL1.17.)

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0017.jpg' | relative_url }})

User Library path update

Observe the imported geometry internal profile showing the Inlet feed angle, Calibration Length and Outlet Run out angle as shown in Fig. 3DSWL1.18.

**Note:** If the Die needs positioning, then user should select the Die positioning method as "3-offset" in Pass Table page. This allows user to position the Die.

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0018.jpg' | relative_url }})

Imported Die geometry

### Define Die movement

Select Advanced radio button type and click on ![]({{ '/assets/icons/pre_icons/mo_define_movement_button.jpg' | relative_url }}) button, define the die movement as constant **Speed** as **200** mm/sec and set the**Current Stroke** as **-1.9** , since the die geometry is imported in its closed position as shown in Fig. 3DSWL1.19. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close Advanced movement page. 

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0019.jpg' | relative_url }})

Die movement window

## Defining Inter-object relations

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Contact page as the swaging operation automatically position dies around the workpiece at equal angles manual position is not needed. Select **System** contact definition type and check scheduled contact Initialize and Generate check boxes and enter small contact **tolerance** value **0.0001** as shown in Fig. 3DSWL1.20. System will generate the contact automatically during database generation. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Simulation preview page. 

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0020.jpg' | relative_url }})

System type Inter-object settings

## Preview the Swaging pass

Observe the Die and workpiece movement and positioning preview by playing with step manipulation options. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Simulation controls controls.

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0021.jpg' | relative_url }})

Swaging preview window

## Define Simulation controls

Enter the **number of steps** to **10000,** **step increment to save** to **1000** and **0.0015** mm stroke/step as shown in Fig. 3DSWL1.22. In addition to this friction coefficient value **0.4** is defined will be used in contact friction calculation. Implicit solver is used to solve this setup. Leave the implicit solver default settings. To know more about RSE and Implicit contact refer and respectively. 

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0022.jpg' | relative_url }})

Simulation control window

## Check and Generate Database

Click on ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) and observe the message tab for DB checking messages, if there is any input errors will be indicated by red color and also display the warning messages. Error message block the user to generate DB. Confirm the DB checking is OK and click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}). (See Fig. 3DSWL1.23.) After generating Database switch to Simulation mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button.

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0023.jpg' | relative_url }})

Generate Database window

## Submit to Simulate

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. 3DSWL1.24. Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0024.jpg' | relative_url }})

Submit to simulate

User can use more processors and run in 64 bit by using the ![]({{ '/assets/icons/simulator_icons/mo_run_options_action_lable.jpg' | relative_url }}). As the simulation starts simulated saved steps will update in simulation graphics window and also Message and LOG files display the status of the current simulation as shown in Fig. 3DSWL1.25.

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0025.jpg' | relative_url }})

Monitor using simulation graphics

Simulation completion or stop will be indicated in the message file. After completion of the simulation click on ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) tab to post process the DB.

## Post process the Results

Play through the Steps and see the Strain distribution by plotting the effective strain State variable. (See Fig. 3DSWL1.26.)

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0026.jpg' | relative_url }})

Strain Distribution

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0027.jpg' | relative_url }})

Workpiece cross section thickness

## Setting up the Swaging Explicit setup

In Explicit solver make workpiece as**Elasto plastic** object by visiting back to Billet object window as shown in Fig. 3DSWL1.28.

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0028.jpg' | relative_url }})

Billet Object selected as Elasto plastic object

After making the billet as Elasto plastic go to workpiece material page, click on ![]({{ '/assets/icons/pre_icons/mo_edit_material_button.jpg' | relative_url }}) define the **Mass****density** as **7.85e-09** under **Thermal** tab as shown in Fig. 3DSWL1.29. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the material edit page.

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0029.jpg' | relative_url }})

Defining Mass density data

Go to **S******im** ulation controls** window and select **Explicit****solver** method radio button as shown in Fig. 3DSWL1.30. Enter the **Damping****coefficient** as **0.5** , **Mass scaling** as **30** and **Contact Frequency** as **1**.

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0030.jpg' | relative_url }})

Simulation controls for Explicit solver method

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to go the Database generation window and check and generate the Database to submit to simulate in Next steps. Similar to the section 1.12. and 1.13. submit the generated DB to simulate and post process using MO post respectively.

Plot Strain Effective at last step for the Simulated Database (See Fig. 3DSWL1.30. and Fig. 3DSWL1.31.)

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0031.jpg' | relative_url }})

Strain effective plot

![]({{ '/assets/images/labs/cogging_labs/swaging_lab1/image0032.jpg' | relative_url }})

Workpiece cross section

**Related Topics:**

[Swaging Setup](/docs/sk/operation_templates/29_cogging/29_2_swaging_setup/)

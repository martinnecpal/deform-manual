---
lang: en
title: "Multipass spinning with Quick Evaluation solver lab"
---

# Multi pass spinning with Quick evaluation Lab 

1.1 Introduction

1.2. Creating a New problem

1.3. Adding Forming operation

1.4. Simulation controls

1.5. Loading Material from library

1.6. Object

1.6.1. Workpiece

1.6.2. Head stock

1.6.3. Mandrel

1.6.4. Roll

1.7. Contact page

1.8. Stopping controls

1.9. Step controls

1.10. Generating database

1.11. Running Simulation

1.12. Post-Processing

## Introduction

From v14.0, “[Partial](../../../pre_processor/9_simulation_controls/9_5_solver_settings.htm#Partial_domain_Solver)[ domain solver](../../../pre_processor/9_simulation_controls/9_5_solver_settings.htm#Partial_domain_Solver)” is available under Special solvers and is currently available only for “Lagrangian incremental” and “ALE spinning” simulation type. Under Partial Domain, we have “Quick evaluation” option which simulates localized deformation and updates axi-symmetrically (neglecting rotational speed). Quick evaluation solver solves one step (per revolution) model for incremental rotary forming and is currently available only for ALE Spinning. Quick Evaluation Method with partial domain solver can improve the computational efficiency and is good for the parametric study for initial check of the processing design.

In this lab we will be setting up simple multi pass ALE spinning operation with Quick evaluation method.

## Creating a New problem

On a Windows machine, go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button, select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** v1x.x from the menu. The DEFORM GUI Main window will appear.

Create a new problem either by selecting **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in [Fig. 3DQEL1.1.]() Select " **Integrated Manufacturing Process** " radio button and "**SI** " radio button in Unit field. Define Problem Name as "******QE_Multipass_spinning******" and make sure the “**Show option dialog** ” check box is turned on (if we do not turn on the “Show option dialog” check box, then we will not get the New Project dialog in MO UI). Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/applications/55_mulitpass_spinning_with_qe_solver/image0001.jpg' | relative_url }})

Problem type selection window

Multiple operation wizard will open with the New Project dialog as shown in Fig. 3DQEL1.2., at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. We will use ‘**QE_Multipass_spinning** ” as the project name in this session. 3D Forming operation can also be added in the "New Project" dialog (see Fig. 3DQEL1.2.), but we will add 3D Forming operation from operations list in Explorer for this lab, so do not check "First operation" check box in "New Project" dialog. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

![]({{ '/assets/images/applications/55_mulitpass_spinning_with_qe_solver/image0002.jpg' | relative_url }})

Adding 3D Forming Operation in MO Wizard from new Project window.

## Adding Forming operation

Add one 3D Forming operation from the Explorer Operations list. Operation can be added by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button adjacent to 3D Forming in Explorer or user can also add by drag and drop into the Operation Editor (See Fig. 3DQEL1.3.). As we add operation, Process page will be opened in the properties area.

![]({{ '/assets/images/applications/55_mulitpass_spinning_with_qe_solver/image0003.jpg' | relative_url }})

Adding 3D Forming Operation from explorer.

## Simulation controls

Switch to Expert mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) button,**** define Operation name as "**Multi pass spinning** " under **Main****settings![]({{ '/assets/icons/pre_icons/mo_main_setting.jpg' | relative_url }})** , select Simulation Type as "**ALE Spinning** " and keep “**Deformation** ” mode in checked status and uncheck the "**Heat****Transfer** " mode check box as shown in Fig. 3DQEL1.4. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to material list page.

![]({{ '/assets/images/applications/55_mulitpass_spinning_with_qe_solver/image0004.jpg' | relative_url }})

Expert mode Simulation controls 

## Loading Material from library

In Material list page, load the material **AISI-1010,COLD[70F(20C)]** from DEFORM Material library's, from **Steel** category using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load material data from library) option. Material is added to Material list as shown in Fig. 3DQEL1.5. ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Object page.

![]({{ '/assets/images/applications/55_mulitpass_spinning_with_qe_solver/image0005.jpg' | relative_url }})

Displaying loaded material in Material list

## Object

We need four objects for this lab. click on ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) button and add 4 objects in list. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Workpiece page. 

### Workpiece

Keep the default object name as "**Workpiece** ", Object **Temperature** as **20** °C and Object type as **Plastic**. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Geometry page.

#### Importing Workpiece geometry 

In Geometry page, using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) button import **QE_Workpiece - blank.stl** file from **/3D/ LABS/QE_Solver** folder. We will generate brick mesh for the imported geometry so, click on ![]({{ '/assets/icons/pre_icons/mo_setup_brick_mesh_label.jpg' | relative_url }}) option and select “**Revolve** ” type and “**Full********Revolve** ” radio button. Define Center as -1, 0, 0 and Axis as 1, 0, 0 as shown in Fig. 3DQEL1.6. Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button to close the Setup brick mesh page. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Mesh page.

![]({{ '/assets/images/applications/55_mulitpass_spinning_with_qe_solver/image0006.jpg' | relative_url }})

Brick mesh setup from the Workpiece Geometry page

#### Generating brick mesh for the workpiece

Select **Brick****mesh** and define **uniform thickness #****of****layers** as **120**. For 2D cross-section mesh, define **number of elements** as **100** , set **thickness****elements** to**2** , **Size****ratio** as**2** and turn on “**Mapped********mesh****generation** ” check box as shown in Fig. 3DQEL1.7. Click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button and click ![]({{ '/assets/icons/pre_icons/mo_no_button.jpg' | relative_url }}) in "**Default Boundary Conditions** " popup. The Mesh should look like as shown in Fig. 3DQEL1.7. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button to Material page.

![]({{ '/assets/images/applications/55_mulitpass_spinning_with_qe_solver/image0007.jpg' | relative_url }})

Workpiece displaying the generated brick mesh 

#### Assign Material

Select the " **AISI-1010, COLD[70F(20C)]** " material in material list which is already available in the material list for Workpiece. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top die page.

![]({{ '/assets/images/applications/55_mulitpass_spinning_with_qe_solver/image0008.jpg' | relative_url }})

Assigned material to Workpiece

### Head stock

In Top die page, change the name of the object to “**Head stock** ” and keep Object **Temperature** as **20** °**C** and Object type as **Rigid** as shown in Fig. 3DQEL1.9. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Geometry page.

![]({{ '/assets/images/applications/55_mulitpass_spinning_with_qe_solver/image0009.jpg' | relative_url }})

Head stock general page.

#### **Importing Head stock geometry**

In Geometry page, click on ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) button to import **QE_Head stock.stl** file from**/3D/ LABS/QE_Solver** folder. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Bottom die page.

### Mandrel 

In Bottom die page, change the Name of the object to “**Mandrel** ” and keep Object **Temperature** as **20** °C and Object type as **Rigid**. click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Geometry page.

#### **Importing Mandrel geometry**

In Geometry page, click on ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) button to import **QE_Mandrel.stl** file from **/3D/ LABS/QE_Solver** folder. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Object 4 die page.

### Roll 

In Object 4 page, change the Name of the object to “**Roll** ” and keep Object **Temperature** as **20** °C and Object type as Rigid. click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Geometry page.

#### Importing Roll geometry

In Geometry page, click on ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) button to import **QE_Roll.stl** file from **/3D/ LABS/QE_Solver** folder. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Movement page.

#### Define path movement for Roll

Select **Path** radio button, and select **Local radio** button and define **U** as 1,0,0, and V as 0,1,0, values as shown in Fig. 3DQEL1.10. Then select “**Function****of time** ” radio button and click on ![]({{ '/assets/icons/pre_icons/mo_define_function..._button2.jpg' | relative_url }}) button and import “**QE_Roll_Path_movement****.****dat** ” file from **/3D/ LABS/QE_Solver** folder using ![]({{ '/assets/icons/pre_icons/mo_load_button_2.jpg' | relative_url }}) button. After importing the file, “Synchronization with path movement” popup will appear, click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button. 

![]({{ '/assets/images/applications/55_mulitpass_spinning_with_qe_solver/image0010.jpg' | relative_url }})

Importing the path movement

  
Imported path movement looks like as shown in Fig. 3DQEL1.11. and click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to close the table and in display, we can observe the path preview of the Roll and its position as shown in Fig. 3DQEL1.12.

![]({{ '/assets/images/applications/55_mulitpass_spinning_with_qe_solver/image0011.jpg' | relative_url }})

Imported path movement data

![]({{ '/assets/images/applications/55_mulitpass_spinning_with_qe_solver/image0012.jpg' | relative_url }})

Roll position and path preview after importing the path movement and synchronization. 

  
**Note: For Quick evaluation method, there is no need to define the rotation movement for the roll/s.**

  
Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Contact page.

## Contact page

In Contact page, select "**User** " type and click on ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) button to populate table with default contact relations between the objects. From the table, we can observe default relations being added. Turn on **sticking contact** check box for Head stock - Workpiece and Mandrel - Workpiece relations as shown in Fig. 3DQEL1.16.

  * Select the **Head stock - Workpiece** relation and click on ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) button. Define a **Coulomb** friction of **0.5**. Switch to the **Friction****Window** tab. Click the ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button to add a new window. Click on the **Solid** cylinder button on toolbar that is along the far-left side of the screen. Click anywhere on the model to place the window. Click on the ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) icon to define the window size as shown in the Fig. 3DQEL1.13., click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the Edit window dialog. Select **Coulomb** friction and set a constant value of **0.5** and select "**Head stock** " as object to follow the window. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the Edit Inter-object data window.

  
  
![]({{ '/assets/images/applications/55_mulitpass_spinning_with_qe_solver/image0013.jpg' | relative_url }})

Head stock - workpiece window definition

  * Select the **Mandrel - workpiece** relation and click on ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}). Define a **Coulomb** friction of**0.3**. Switch to the **Friction****Window** tab. Click the ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button to add a new window. Click on the **Solid****cylinder** button on toolbar that is along the far-left side of the screen. Click anywhere on the model to place the window. Click on the ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) icon to define the window size as shown in the Fig. 3DQEL1.14., click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the Edit window dialog. Select **Coulomb** friction and set a constant value of **0.3** and select "**Mandrel** " as object to follow the window. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the Edit Inter-object data window.

  
  
![]({{ '/assets/images/applications/55_mulitpass_spinning_with_qe_solver/image0014.jpg' | relative_url }})

Mandrel- workpiece window definition

  * Select the **Roll - Workpiece** relation and click on ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) button. Define a **Coulomb** friction of **0.02**. Under **Contact** tab, select **Node coordinate update method** as “**Do not update** ”. Select **Separation criterion as Geometry-based criteria** with “**Absolute distance** ” method, enter **1e-0.5** value as absolute distance tolerance (see Fig. 3DQEL1.15.). 

![]({{ '/assets/images/applications/55_mulitpass_spinning_with_qe_solver/image0016.jpg' | relative_url }})

Roll – Workpiece Contact criteria and separation criteria selection.

Switch to the **Friction****Window** tab, click the ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button to add a new window. Click on the **sold****cylinder** button on toolbar that is along the far-left side of the screen. Click anywhere on the model to place the window. Click on the ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) icon to define the window size as shown in the Fig. 3DQEL1.16., click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the Edit window dialog. Select **Coulomb** friction and set a constant value of **0.02** and select "**Roll** " as object to follow window. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the Edit Inter-object data window.

  
  
![]({{ '/assets/images/applications/55_mulitpass_spinning_with_qe_solver/image0015.jpg' | relative_url }})

Roll - Workpiece window definition

  
Click on ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) button to calculate the default tolerance value and Generate contact by clicking on ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) button and select **Yes** in "**STICKING CONDITION** " popup. Generated contact will look like as shown in Fig. 3DQEL1.17. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Stopping controls page.

![]({{ '/assets/images/applications/55_mulitpass_spinning_with_qe_solver/image0017.jpg' | relative_url }})

Contact page

## Stopping controls

Under the Stopping controls ![]({{ '/assets/icons/pre_icons/mo_stopping_criteria.jpg' | relative_url }}) tab, define Process duration as “**34.5** ” as shown in Fig. 3DQEL1.18. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Step controls page.

![]({{ '/assets/images/applications/55_mulitpass_spinning_with_qe_solver/image0018.jpg' | relative_url }})

Stopping controls – Process condition

## Step controls

Click on Simulation step definition ![]({{ '/assets/icons/pre_icons/mo_simulation_step.jpg' | relative_url }}) and define **Number of Simulation steps** as **400** , **Step Increment to save** as **5** and select**4 - Roll** as Primary die as shown in Fig. 3DQEL1.19.

  
![]({{ '/assets/images/applications/55_mulitpass_spinning_with_qe_solver/image0019.jpg' | relative_url }})

Defining step definition

Click on Step increment definition ![]({{ '/assets/icons/pre_icons/mo_step_increment.jpg' | relative_url }}), select **Time** as Solution step definition type and define constant **time** step as **0.1** Sec/step, define **Max polygon length** as **0** as shown in Fig. 3DQEL1.20.

![]({{ '/assets/images/applications/55_mulitpass_spinning_with_qe_solver/image0020.jpg' | relative_url }})

Defining Solution step definition

Click on ![]({{ '/assets/icons/pre_icons/mo_solver_settings.jpg' | relative_url }}), in **Deformation** tab under Special solver, select "**Partial domain** " and turn on **Quick evaluation solver** check box. Under solver controls, by default **Roll** object is added in the table, define the **Active domain total angle** as **20** degree and **Rotation****axis** as **X** as shown in Fig. 3DQEL1.21. In the table, define 20 as active domain Angle with -10 as Start angle and 10 as End angle. Click on ![]({{ '/assets/icons/pre_icons/mo_preview_button.jpg' | relative_url }}) to observe the active domain region, active domain region will be highlighted in White color in display region as shown in Fig. 3DQEL1.21.

Under Boundary constraints, select method as Bar stiffness and Scaling factor as**0.1**. For more information related on Partial domain solver refer [9.5. Solver settings - Partial domain solver](../../../pre_processor/9_simulation_controls/9_5_solver_settings.htm#Partial_domain_Solver)

![]({{ '/assets/images/applications/55_mulitpass_spinning_with_qe_solver/image0021.jpg' | relative_url }})

Selecting Solver and defining active domain angle

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Generate DB page to generate database.

## Generating database

In Generate database page, click on ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) button to have the program check to see if anything was missed in the problem setup. During the checking process, messages in the red color signify data that needs to be fixed before a simulation can be run (such as when you forget to define any material data). 

Click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database.

## Running Simulation

Once the database has been generated, switch to the Simulation mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the operation tree. Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. 3DQEL1.22. Use the default **Continue Run** option to select “**Continue****from the last step** ” (from step -1) option and then select the Simulation mode as Interactive, click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

  
![]({{ '/assets/images/applications/55_mulitpass_spinning_with_qe_solver/image0023.jpg' | relative_url }})

Run Simulation window.

The progress of the simulation can be monitored as it is running by looking at the Simulation Message tab and Simulation Graphics from the Graphics display region in Simulation mode. If ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked in Simulation Message tab, which is the default setting, the Message file will refresh automatically.

The Message file provides information about which simulation step the simulation is currently on and information dealing with how well the simulation is running.

## Post-Processing

When the simulation is completed, review the results by switching to Post mode using the ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) button. 

In Step Browser, click on ![]({{ '/assets/icons/pre_icons/mo_all_button.jpg' | relative_url }}) button to view all saved steps and play the animation and observe the shape of the workpiece at last step after completion of multi pass spinning (See Fig. 3DQEL1.23.).

![]({{ '/assets/images/applications/55_mulitpass_spinning_with_qe_solver/image0024.jpg' | relative_url }})

Workpiece shape at last step.

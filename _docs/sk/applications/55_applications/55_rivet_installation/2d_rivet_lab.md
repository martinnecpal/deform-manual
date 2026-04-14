---
lang: sk
title: "2D Rivet Lab"
---

# 2D Rivet Lab

In this lab we will setup simple 2D Rivet installation operation in 2D Forming operation.

  
1.1. Creating New problem

1.2. Adding 2D Forming Operation

1.3. Select Geometry type and Simulation Modes

1.4. Add material from Library

1.5. Adding Objects

1.6. Define Rivet general object data

1.6.1. Import the rivet geometry

1.6.2. Generating mesh for Rivet

1.6.3. Assign Material for Rivet

1.7. Define Rivet pin general object data

1.7.1. Import the Rivet pin geometry

1.7.2. Generating mesh for Rivet pin

1.7.3. Assigning BCC for Rivet pin

1.7.4. Assign Movement for Rivet pin

1.7.5. Assign pin Properties

1.8. Define Top sheet general object data

1.8.1. Import the Top sheet geometry

1.9. Define Bottom sheet general object data

1.9.1. Import the Bottom sheet geometry

1.10. Define Anvil general object data

1.10.1. Import the Anvil geometry

1.11. Define Inter-object relations

1.12. Assign Stopping controls

1.13. Assign Step controls

1.14. Data checking and database generation

1.15. Run and monitor a simulation

1.16. Review Results

## Creating New problem

On a Windows machine, go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** v1x.x from the menu. The DEFORM GUI Main window will appear.

Create a new problem either by selecting **File**![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in Fig. 2DRL1.1. Select " **Integrated Manufacturing Process** " radio button and unit system as "**English** " radio button in unit field. Define Problem Name as " **Rivet** " and make sure the “**Show option dialog** ” check box is turned on (if we do not turn on the “Show option dialog” check box, then we will not get the New Project dialog). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

Problem Setup Window

Multiple operation wizard will open with the New Project dialog, at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session we will use "**Rivet** " as the project name. Confirm that First operation check box is unchecked as we will add operation later (See Fig. 2DRL1.2.), click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue to open the operation.

![]({{ '/assets/images/applications/55_rivet_installation/2d_rivet_lab/image0002.jpg' | relative_url }})

New MO Project window

## Adding 2D Forming Operation

Multiple Operation wizard will open new project. Add 2D Forming operation from the Explorer Operations list. Operation can be added by clicking on 2D Forming operation ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button (See Fig. 2DRL1.3.) or user can also add by drag and drop into the Operation Editor.

![]({{ '/assets/images/applications/55_rivet_installation/2d_rivet_lab/image0003.jpg' | relative_url }})

Adding 2D Forming operation from operation explorer

Change the default operation title to "**Rivet** " from Forming by selecting the title in the operation editor as shown in Fig. 2DRL1.4. and press Enter keyboard button after editing is completed.

![]({{ '/assets/images/applications/55_rivet_installation/2d_rivet_lab/image0004.jpg' | relative_url }})

Renaming operation title to Flair

## Select Geometry type and Simulation Modes

Confirm the geometry type selected is **Axi-symmetric** in Geometry type page, then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

In this lab we will be showing how to setup simple Isothermal problem, so in Simulation controls page, **uncheck** the **Heat****transfer** mode check box (See Fig. 2DRL1.5.). then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/applications/55_rivet_installation/2d_rivet_lab/image0005.jpg' | relative_url }})

Simulation control window

## Add material from Library

Click the ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load material data from library) button, select the **Aluminum** category, then **AL-6061-O,COLD[70F(20C)]** and click the ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}) button. Click the ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load material data from library) button,select the **Steel** category, then **AISI-1035,COLD[70-400F(20-200C)]** and click the![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}) button. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Object page.

## Adding Objects

In this Rivet lab we need 5 objects, by default three objects will be added in Forming operation list, if not added click the ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) (insert object) button three times to add 3 objects in list, then add another 2 objects in list using ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) (insert object) button. After adding objects, object window looks as shown in Fig. 2DRL1.6. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button.

![]({{ '/assets/images/applications/55_rivet_installation/2d_rivet_lab/image0006.jpg' | relative_url }})

Objects window to Add or Delete the objects

## Define Rivet general object data

Change the object name to **Rivet**. Assign the **temperature** as **70** °F and select the object type as **Plastic**. (See Fig. 2DRL1.7.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button.

![]({{ '/assets/images/applications/55_rivet_installation/2d_rivet_lab/image0007.jpg' | relative_url }})

Rivet object window

### Import the rivet geometry

Click the ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Load geometry from a file) button and import the file " **Rivet.dxf** ” by browsing the geometry file path located in DEFORM installation folder **\Tutorials** directory. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to mesh page.

### Generating mesh for Rivet

The default **target number of elements** is **1000**. Accept the default number of elements and click the ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button to generate the mesh for Rivet. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Material page to assign material for Rivet.

### Assign Material for Rivet

Select the **AL-6061-O,COLD[70F(20C)]** in the material window to assign the material to the Rivet as shown in Fig. 2DRL1.8. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top die page.

![]({{ '/assets/images/applications/55_rivet_installation/2d_rivet_lab/image0008.jpg' | relative_url }})

Rivet object material window

## Define Rivet pin general object data

Change the object name to **Rivet****pin**. Assign the **temperature** as **70** ° F, select the object type as **Plastic** and check **Primary****die** check box. (See Fig. 2DRL1.9.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button.

![]({{ '/assets/images/applications/55_rivet_installation/2d_rivet_lab/image0009.jpg' | relative_url }})

Rivet pin object window

### Import the Rivet pin geometry

Click the ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Load geometry from a file) button and import the file " **RivetPin.dxf** ” by browsing the geometry file path located in DEFORM installation folder \Tutorials directory. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to mesh page.

### Generating mesh for Rivet pin

We will generate mesh with mesh windows. To generate mesh with mesh windows we need to be in expert mode, click on ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) icon to switch to expert mode. Define **Target number of elements** as **1000** , Under **Weighting****Factors** tab change the **Mesh****window** weighting factor value to **1**. Now select Mesh window tab and add **two****mesh** windows.

Define **Window****1** to cover bottom of pin with **relative****element** size **0.2** and **Window****2** to cover the entire pin with **relative****element** size **1.0** as shown in Fig. 2DRL1.10. Then click the ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button to generate the mesh for Rivet pin. Click on ![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }}) icon to switch to Guided mode

![]({{ '/assets/images/applications/55_rivet_installation/2d_rivet_lab/image0010.jpg' | relative_url }})

Expert mode mesh page.

Select the **AISI-1035,COLD[70-400F(20-200C)]** in the material window to assign the material to the Rivet pin as shown in Fig. 2DRL1.11.

![]({{ '/assets/images/applications/55_rivet_installation/2d_rivet_lab/image0011.jpg' | relative_url }})

Selecting Material for Rivet pin

Click on ![]({{ '/assets/icons/pre_icons/mo_edit_material_button.jpg' | relative_url }}) button to define Fracture data, Click on **Miscellaneous** tab, select **Normalized****C &L Fracture** model click on ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) button and define **Critical****value** as **1** (See Fig. 2DRL1.12.). Now click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) and close the Material Edit window. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to BCC page.

![]({{ '/assets/images/applications/55_rivet_installation/2d_rivet_lab/image0012.jpg' | relative_url }})

Workpiece material Fracture model window

### Assigning BCC for Rivet pin

Assign Movement BCC for roughly top half of the pin as shown in Fig. 2DRL1.13. and retain default velocity BCC on symmetry surface. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Movement BCC page.

![]({{ '/assets/images/applications/55_rivet_installation/2d_rivet_lab/image0013.jpg' | relative_url }})

Movement BCC assigned for Rivet pin

### Assign Movement for Rivet pin

The default mode is constant **speed**. Input a value of **1** in/sec for the Constant value and select the Direction of **+Y** as shown in Fig. 2DRL1.14. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Properties page.

![]({{ '/assets/images/applications/55_rivet_installation/2d_rivet_lab/image0014.jpg' | relative_url }})

Rivet pin movement window

### Assign pin Properties

Click on **Fracture** tab and define **Fracture** **Elements** value as **2**. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Bottom die page.

## Define Top sheet general object data

Change the **object****name** to **Top sheet**. Assign the **temperature** as **70** ° F and select the object type as **Rigid** as shown in Fig. 2DRL1.15. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button.

![]({{ '/assets/images/applications/55_rivet_installation/2d_rivet_lab/image0015.jpg' | relative_url }})

Top pin object window

### Import the Top sheet geometry

Click the ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Load geometry from a file) button and import the file " **RivetTopSheet.DXF** ” by browsing the geometry file path located in DEFORM installation folder **\Tutorials** directory. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Object 4 page.

## Define Bottom sheet general object data

Change the **object****name** to **Bottom** **sheet**. Assign the **temperature** as **70** ° F and select the **object****type** as **Rigid**. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button to assign geometry.

### Import the Bottom sheet geometry

Click the ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Load geometry from a file) button and import the file " **RivetBottomSheet.DXF** ” by browsing the geometry file path located in DEFORM installation folder **\Tutorials** directory. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Object 5 page.

## Define Anvil general object data

Change the **object****name** to **Anvil**. Assign the **temperature** as **70** ° F and select the **object** **type** as **Rigid**. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button to assign geometry.

### Import the Anvil geometry

Click the ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Load geometry from a file) button and import the file "**Anvil.****DXF** ” by browsing the geometry file path located in DEFORM installation folder **\Tutorials** directory. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Contact page.

## Define Inter-object relations

Add four relations in table by clicking on (![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }})) Add relation button, select Rivet Pin as Master and Rivet as slave in first relation, select Top sheet as master and Rivet as slave for second relation, select Bottom sheet as master and Rivet as slave for third relation and select Anvil as master and Rivet as slave for fourth relation. Click on the ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) button for one of the relationships. Select Shear type friction radio button, use the Constant drop down menu and define **0.1** value. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to exit the menu. Click ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) to apply the friction value to the three other relationships (See Fig. 2DRL1.16.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Stopping controls page.

![]({{ '/assets/images/applications/55_rivet_installation/2d_rivet_lab/image0016.jpg' | relative_url }})

Inter-Object relation window

## Assign Stopping controls

Turn on **Max****die****stroke** check box and define **0.5** in **Y** field. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Step controls page.

## Assign Step controls

Define **Number of steps** as **500** , **Step increment** as **10** and define **constant die displacement** as 0.002 in/step as shown in Fig. 2DRL1.17\. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to generate DB.

![]({{ '/assets/images/applications/55_rivet_installation/2d_rivet_lab/image0017.jpg' | relative_url }})

Step controls window

## Data checking and database generation

Click on the ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) button, the data checking system will confirm that defined data is appropriate for running a simulation.

Red marks indicate missing or incorrect data that will prevent a simulation from running. It is necessary to correct those errors before the database can be generated.

Yellow marks indicate data which may be suspect and should be reviewed. These should be investigated carefully, as they might result in system instability or erroneous (incorrect) results.

Review the data checking information. If there are no yellow or red marks, click the ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button.

You should look for the words: Database has been generated. When you see this, it means that your inputs have been saved to the database and you are now ready to run the simulation.

Click on the MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode button (above the operation tree) to start the simulation.

## Run and monitor a simulation

Once the database has been generated switch to the Simulation mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the operation tree. Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog. Use the default **Continue****Run** option to select “**Continue****from the last step** ” option and then select the Simulation mode as **Interactive** radio button **** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

Watching the simulation graphics provides an initial idea of what to expect when opening the postprocessor (See Fig. 2DRL1.18.). Also monitor simulation from Simulation and log messages. The message file and log file will indicate that the simulation has been completed on the last line, confirming that click on ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) Mode button to review results.

![]({{ '/assets/images/applications/55_rivet_installation/2d_rivet_lab/image0018.jpg' | relative_url }})

Running the simulation from MO simulation mode

## Review Results

Play through the Steps and see the Damage distribution by plotting the Damage State variable.

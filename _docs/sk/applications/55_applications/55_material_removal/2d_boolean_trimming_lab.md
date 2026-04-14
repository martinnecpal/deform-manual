---
lang: sk
title: "2D Boolean Trimming Lab"
---

# 2D Boolean and Trimming with Fracture Lab

DEFORM includes many ways of removing material:

  * Boolean

  * Shearing

  * Fracture

Boolean can be performed either as an interactive pre-processing operation, or as an operator between operations. 

In this lab, a Boolean operation will be performed interactively in the preprocessor, followed by a forming operation with fracture.

1.1. Creating New problem

1.2. Adding 2D Forming Operation

1.3. Select Geometry type and Simulation Modes

1.4. Adding Objects

1.5. Loading Workpiece data

1.6. Defining Top die object data

1.6.1. Create Top Die geometry from primitive

1.7. Performing Boolean operation

1.8. Workpiece Mesh page

1.8.1. Defining Fracture data in Material

1.8.2. Assigning Workpiece Fracture properties

1.9. Defining Top die object data for Flash trimming operation

1.9.1. Import the trim punch geometry

1.9.2. Assigning movement controls to trim punch

1.10. Defining Bottom die object data

1.10.1. Import the trim die geometry

1.11. Defining Object 4 object data

1.11.1. Import the trim flash holder geometry

1.11.2. Assigning movement controls to trim flash holder

1.12. Positioning object

1.13. Define Inter-object relations

1.14. Assign Step controls

1.15. Data checking and database generation

1.16. Run and monitor a simulation

1.17. Review Results

## Creating New problem

On a Windows machine, go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** v1x.x from the menu. The DEFORM GUI Main window will appear.

Create a new problem either by selecting **File**![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in Fig. 2DBTL1.1. Select " **Integrated Manufacturing Process** " radio button and unit system as "**English** " radio button in unit field. Define Problem Name as " **Boolean_Trimming** " and make sure the “Show option dialog” check box is turned on (if we do not turn on the “**Show option dialog** ” check box, then we will not get the New Project dialog in MO UI). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

Problem Setup Window

Multiple operation wizard will open with the New Project dialog, at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session we will use "**Boolean_Trimming** " as the project name. Confirm that First operation check box is unchecked as we will add operation later, click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

![]({{ '/assets/images/applications/55_material_removal/2d_boolean_triming_lab/image0002.jpg' | relative_url }})

New MO Project window

## Adding 2D Forming Operation

Multiple Operation wizard will open new project. Add 2D Forming operation from the Explorer Operations list. Operation can be add by clicking on **2D Forming operation** ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button (See [Fig. 2DBTL1.3.](../55_friction_stir_welding/55_friction_stir_welding.htm#Fig_FSWL1_3_Adding_3D_Forming_operation)) or user can also added by drag and drop into the Operation Editor.

![]({{ '/assets/images/applications/55_material_removal/2d_boolean_triming_lab/image0003.jpg' | relative_url }})

Adding 2D Forming operation from operation explorer

## Select Geometry type and Simulation Modes

Confirm the geometry type selected is **Axi-symmetric** in Geometry type page, then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

In this lab we will be showing how to setup trimming operation with Isothermal condition, so in Simulation controls page, Check the **Deformation** **mode** check box, then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Objects page.

## Adding Objects

The forming operation to be simulated requires a workpiece and three dies. By default three objects will be added in Forming operation list, so add another object by clicking the ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) (insert object) button to add 4th object in list, Workpiece and three dies. Object window looks as shown in Fig. 2DBTL1.4. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button.

![]({{ '/assets/images/applications/55_material_removal/2d_boolean_triming_lab/image0004.jpg' | relative_url }})

Adding Objects in list

##  Loading Workpiece data

Click the ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) button and Import the "**gear2.DB** " file from DEFORM installation folder \**Tutorials** directory. Select **Last step** in Step List page (See Fig. 2DBTL1.5.) and Select workpiece in Object selection window. Now the loaded workpiece shape from the database should be like as shown in Fig. 2DBTL1.6. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top die page.

![]({{ '/assets/images/applications/55_material_removal/2d_boolean_triming_lab/image0005.jpg' | relative_url }})

Step selection page popup window

![]({{ '/assets/images/applications/55_material_removal/2d_boolean_triming_lab/image0006.jpg' | relative_url }})

Loaded Workpiece object data from Database

## Defining Top die object data

Change the Object name to "**Trim Geo** ", Keep the Top die default temperature as **68** ° F and confirm the object type selected as **rigid** and Primary die. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Top die geometry page.

### Create Top Die geometry from primitive

Click on the ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) button to create a geometry within DEFORM. The Trim Geo dia is 5.5”, and Height of 3" with Y: -1", so you will define a width of half the diameter. Define **Radius** as **2.75** " and **Height**(H) as **3** " (See Fig. 2DBTL1.7.). Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button to close the Geometry Primitive dialog. Select ![]({{ '/assets/icons/pre_icons/mo_object_positioning_icon.jpg' | relative_url }}), using "**Offset** " positioning move the Top Die object down in -**Y** direction by **-1** ” as shown in Fig. 2DBTL1.8. and observe the geometry in graphics window.

![]({{ '/assets/images/applications/55_material_removal/2d_boolean_triming_lab/image0007.jpg' | relative_url }})

Geometry Primitive window

![]({{ '/assets/images/applications/55_material_removal/2d_boolean_triming_lab/image0015.jpg' | relative_url }})

Positioning the Workpiece using Object Postioning option

## Performing Boolean operation

Now Click on ![]({{ '/assets/icons/pre_icons/mo_show_multi_obj_icon.jpg' | relative_url }}) mode, select Workpiece object from Operation tree and click on Boolean (![]({{ '/assets/icons/pre_icons/mo_boolean_icon.jpg' | relative_url }})) icon on Top line Menu (See Fig. 2DBTL1.9.).

![]({{ '/assets/images/applications/55_material_removal/2d_boolean_triming_lab/image0009.jpg' | relative_url }})

Opening Boolean wizard by clicking on Boolean icon

In Boolean wizard, select **Trim****Geo** from Object to be subtracted list and click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) button. After boolean, the workpiece will be as shown in Fig. 2DBTL1.10.

![]({{ '/assets/images/applications/55_material_removal/2d_boolean_triming_lab/image0008.jpg' | relative_url }})

Workpiece after boolean operation 

Now we will setup Flash trimming operation. Go to **Workpiece****Mesh** page.

## Workpiece Mesh page

Define **Target number of Elements** as **5000** and no need to regenerate mesh. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Material page.

### Defining Fracture data in Material

Click on ![]({{ '/assets/icons/pre_icons/mo_edit_material_button.jpg' | relative_url }}) button to define Fracture data, Click on **Miscellaneous** tab, select **Normalized C &L Fracture** model click on ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) button and define **Critical****value** as **1** (See Fig. 2DBTL1.11.) Now Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) and close the Material Edit window. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Properties page.

![]({{ '/assets/images/applications/55_material_removal/2d_boolean_triming_lab/image0010.jpg' | relative_url }})

Workpiece material Fracture model window

### Assigning Workpiece Fracture properties

Click on **Fracture** tab and select "**Fracture****element****deletion** " from pull down menu and define **Fracture****Elements** value as **2**. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Top die page.

## Defining Top die object data for Flash trimming operation

Change the **Object****name** to "**trim punch** ", Keep the default **temperature** as **68** ° F and confirm the object type selected as **rigid** and **Primary** **die**. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Punch geometry page.

### Import the trim punch geometry

Click the ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Load geometry from a file) button and ![]({{ '/assets/icons/pre_icons/mo_import_button.jpg' | relative_url }}) open (import) the file “**TrimPunch****.****IGS** ” by browsing the geometry file path located in DEFORM installation folder \**Tutorials****** directory. Check the geometry using ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) option to make sure the geometry is OK. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Punch movement page.

### Assigning movement controls to trim punch

The default mode is constant **speed**. Input a value of **3** in/sec for the Constant value and confirm that the Direction is **-Y**. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Bottom die page. 

## Defining Bottom die object data

Change the Object name to "**trim die** ", Keep the **default****temperature** as **68** ° F and confirm that the object type selected is **rigid**. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to trim die geometry page.

### Import the trim die geometry

Click the ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Load geometry from a file) button and ![]({{ '/assets/icons/pre_icons/mo_open_button.jpg' | relative_url }}) open (import) the file “**TrimDie****.****IGS** ” by browsing the geometry file path located in DEFORM installation folder \**Tutorials** directory. Check the geometry using ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) option to make sure the geometry is OK. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Object 4page.

## Defining Object 4 object data

Change the Object name to "**trim flash holder** ", Keep the default temperature as **68** °F and confirm the object type selected is **rigid**. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to geometry page.

### Import the trim flash holder geometry

Click the ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Load geometry from a file) button and ![]({{ '/assets/icons/pre_icons/mo_open_button.jpg' | relative_url }}) open (import) the file “**TrimFlashHolder****.****IGS** ” by browsing the geometry file path located in DEFORM installation folder \**Tutorials** directory. Check the geometry using ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) option to make sure the geometry is OK. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Movement page.

### Assigning movement controls to trim flash holder

Select **Sliding****die** type movement radio button. Input a value of **1** klb/in as **Constant** **Stiffness** , **0.1klb** as **Preload** , **3** " as **Max. disp,** select "**trim punch** " object in **Mounted****on****object** list and **confirm** that the **Direction** is **+Y** (See Fig. 2DBTL1.12.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Positioning page.

![]({{ '/assets/images/applications/55_material_removal/2d_boolean_triming_lab/image0011.jpg' | relative_url }})

Trim Flash holder Movement page

## Positioning object

Using **Interference****method** , position the **Workpiece** on Trim die in **-Y** direction, then position the trim flash holder on Workpiece in -Y direction and trim punch on Workpiece in -Y direction. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Contact page.

## Define Inter-object relations

Assign the default inter-object relationships using ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) button. Click on the ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) button for one of the relationships. Select Shear type friction radio button, use the **Constant** radio button and define**1** value. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to exit the menu. Click ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) to apply the friction value to the three other relationships. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Step controls page.

## Assign Step controls

Define **Number of steps** as **100** , **Step increment** as **10** and define constant **die displacement** as **0.005** in/step as shown in Fig. 2DBTL1.13.

![]({{ '/assets/images/applications/55_material_removal/2d_boolean_triming_lab/image0012.jpg' | relative_url }})

Step controls page

## Data checking and database generation

Click on the ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) button, the data checking system will confirm that all defined data is appropriate for running a simulation.

Red marks indicate missing or incorrect data that will prevent a simulation from running. It is necessary to correct these errors before the database can be generated.

Yellow marks indicate data which may be suspect and should be reviewed. These should be investigated carefully, as they might result in system instability or erroneous (incorrect) results.

Review the data checking information. If there are no yellow or red marks, click the ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button.

You should look for the words: **Database has been generated**. When you see this, it means that your inputs have been saved to the database and you are now ready to run the simulation.

Click on the MO ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) Mode button (above the operation tree) to start the simulation.

## Run and monitor a simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog. Use the default **Continue Run** option to select “**Continue from the last step** ” (from step -1) option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

Watching the simulation graphics provides an initial idea of what to expect when opening the post processor. Also monitor simulation from Simulation and log messages. The message file and log file will indicate that the simulation has been completed on the last line, confirming that click on ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) mode button to review results.

![]({{ '/assets/images/applications/55_material_removal/2d_boolean_triming_lab/image0013.jpg' | relative_url }})

Running the simulation from MO simulation mode

## Review Results

Play through the Steps and see the Damage distribution by plotting the Damage State variable.

![]({{ '/assets/images/applications/55_material_removal/2d_boolean_triming_lab/image0014.jpg' | relative_url }})

Damage distribution at last step

---
lang: sk
title: "Lab03 Spike Forging"
---

# Lab 3. Spike Forging

  
3.1. Spike Forging - Transfer from Furnace to Dies

3.2. Spike Forging - Dwell On Bottom Die

3.3. Spike Forging - Forging Blow1

3.4. Spike Forging - Die Change and Blow2

In four operations, a hot spike forging will be modeled. Since the process is hot, the most accurate simulation will model not only the forging operation but also any heat transfer operations that occur. The entire process will be divided as follows:

  * Heat transfer operation will model a 10 second transfer of the billet from the furnace to the dies. This is solely a heat transfer simulation.

  * Dwelling Operation will model the 2 second dwell period of the billet resting on the bottom die prior to forging. This is also a heat transfer simulation.

  * Forming operation will model the first blow and do a Die change for Second Blow of a two blow forging process.

To perform Die Stress for this setup, please refer to Die Stress Wizard lab 2.

Since the billet and dies are axisymmetric, the process could be modeled in 2D. However, in order to further explore symmetry and other important 3D concepts, the process will be modeled in 3D using 1/4 symmetry for the billet and the dies.

## Spike Forging - Transfer from Furnace to Dies

Create a new problem either by selecting **File** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in Fig. 3DL3.1. Select "**Integrated Manufacturing Process** " radio button and unit system as "**English** " radio button in unit field. Define Problem Name as "**Spike_Forging** " and make sure the “**Show option dialog** ” check box is turned on (if we do not turn on the “Show option dialog” check box, then we will not get the New Project dialog). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new problem using the Deform Integrated Manufacturing Process.

MO wizard will open at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session we use ‘**Spike_Forging** ’ as the project name. User can also change the Unit system (File menu selected unit system will be selected by default) and add operation by selecting from First operation pull down list and checkbox. Using copy Existing project option we can import previous saved projects as new project. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

Assigning problem name

Multiple Operation wizard will open. Add 3D Heat Transfer operation from the Explorer Operations list. Add the operation by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button next to **3D Heat Transfer** or user can also add by drag and drop into the Operation Editor. (See Fig. 3DL3.2.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0002.jpg' | relative_url }})

MO Wizard Window

### Assign Heat transfer Type

Since we are doing Air transfer operation, select the Heat transfer type as **Transfer through Air**. click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Assign Process Condition

Define **heat****transfer****time** as **10** sec and keep rest other fields as it is. (See Fig. 3DL3.3.) . Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Object page.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0003.jpg' | relative_url }})

Assigning Transfer operation Process condition

### Objects

In this initial heat transfer simulation, the billet will be getting transferred from the furnace to the dies. For this operation by default only one object will be added in list, use the default selection and (see Fig. 3DL3.4.) click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0004.jpg' | relative_url }})

Objects window

### Defining Object Temperature

In Workpiece page Define **Object temperature** as **2000** °F as shown in Fig. 3DL3.5. Click on![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0005.jpg' | relative_url }})

Defining Workpiece temperature

### Import Geometry

In Geometry page, click on import geometry from library option (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})) and import the **Spike_Billet.STL** file from DEFORM installed folder \3d\LABS directory as shown in Fig. 3DL3.6. Use ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) action label to check the Geometry. A perfect geometry should display message as shown in Fig. 3DL3.7.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0006.jpg' | relative_url }})

Importing Geometry

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0007.jpg' | relative_url }})

Geometry Checking popup

### Assigning Symmetry Conditions

Click on the ![]({{ '/assets/icons/pre_icons/mo_symmetry_planes_label.jpg' | relative_url }}) option, select one of the symmetry planes of the Workpiece and click the to define planar symmetry as shown in Fig. 3DL3.8. Repeat this for the other symmetry plane then click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0008.jpg' | relative_url }})

Assigning Planar symmetry to the workpiece

### Meshing the Workpiece

Switch to Expert mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) (Switch to expert mode) icon from the tool bar. Expert mode will provide more options for detailed settings.

In Mesh page, Select Absolute type, set the **Min Element Size** to **0.04** and also set the **Size****Ratio** to **3**. After changing these settings, click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) . Click ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}) for Default Boundary condition popup. (See Fig. 3DL3.9.) Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0009.jpg' | relative_url }})

Defining Mesh Data

### Assigning Material to the Workpiece

In Material Window, click on to Load material data from Library ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) and load '**AISI-1025[1800-2200F(1000-1200C)]** ' material from **Steel** category by clicking ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}) button as shown in Fig. 3DL3.10. Select the added material from window to assign it to the workpiece as shown in Fig. 3DL3.11. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0010.jpg' | relative_url }})

Material Window

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0011.jpg' | relative_url }})

Assigning Material to workpiece

### Boundary Conditions

For this lab, Assigned Default Boundary conditions are OK for Workpiece in this setup (see Fig. 3DL3.12.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Step page.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0012.jpg' | relative_url }})

Boundary Conditions Window

### Setting Step Controls

In Step Definition define Set the **Number of Simulation Steps** to **50** , the **Step****Increment** **to** **Save** at **5** and Solution step definition **Time** as **0.2** sec (see Fig. 3DL3.13.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0013.jpg' | relative_url }})

Simulation Step Controls Window

### Generate Database

By selecting the **File** menu ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **Export** option, save a keyword file for the problem as "**Spike_Air_transfer** ".

Click on ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) action label to check the problem. Generate database by clicking ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) action label.

### Running Simulation

Once the database has been generated, switch to the Simulation mode by selecting the ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the object tree. Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label under the simulation tab, Run Options dialog will open as shown in Fig. 3DL3.14.. Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0014.jpg' | relative_url }})

Run Simulation Window

Monitor the progress of the simulation by looking at the Simulation Message and Simulation Log tab, making sure that the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked. (See Fig. 3DL3.15.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0015.jpg' | relative_url }})

Simulation Message File

### Post processing

When the simulation is complete, review the results by switching to Post mode using the ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) button above the Simulation tool bar.

Plot Temperature State variable ![]({{ '/assets/icons/post_icons/mo_temp_sv.jpg' | relative_url }}). Also, right-click on the Color Bar in the DISPLAY window and select **Temperature** as the Color Bar Type. This provides a more intuitive color scheme when viewing temperatures.

Play through the steps of the simulation and look at how the Billet cools down as it is transferred from the furnace to the dies. (See Fig. 3DL3.16.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0016.jpg' | relative_url }})

Post processor window with Temperature plot

Now, select last step in Step browser and click on ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}) button to continue the setup.

## Spike Forging - Dwell On Bottom Die

In earlier operation, workpiece was transferred from the furnace to the dies. Once the workpiece gets to the dies, it will rest on the bottom die for 2 seconds prior to forging operation. This dwell will be modeled in this operation. By selecting Batch mode setup type the dwell operation will be set up.

Add 3D Heat Transfer operation from the Explorer Operations list. Add the operation by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button next to 3D Heat Transfer or can also be added by drag and drop into the Operation editor as shown in Fig. 3DL3.17.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0017.jpg' | relative_url }})

MO wizard with two operations

Select 2nd operation from Operation editor, Setup type popup will appear and click on ![]({{ '/assets/icons/pre_icons/mo_no_batch_setup_button.jpg' | relative_url }}) mode button (since we are setting up Dwell operation in Batch mode). See Fig. 3DL3.18.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0018.jpg' | relative_url }})

Setup type selection popup

In Heat transfer page, by default **Rest on******Die** **Heating type will be selected if not select Rest on Die Heat transfer type. Previous operation settings will be carried over the operation see Fig. 3DL3.19. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0019.jpg' | relative_url }})

Heat Transfer type selection page

### Process condition

Define **Resting****Time** as **2** Sec, as the workpiece will rest on the bottom die for 2 seconds (See Fig. 3DL3.20.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Objects page.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0020.jpg' | relative_url }})

Resting operation Process Condition page

###  Adding Objects

In Object page, by default 3 objects will be added. Depending upon the number of objects required for the simulation, user can add as many dies as needed by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) button. For this lab, we will use 3 objects (workpiece and 2 dies) (see Fig. 3DL3.21.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0021.jpg' | relative_url }})

Objects window

Since we are continuing into heat dwelling operation from Heat transfer operation, Workpiece is automatically considered as read from DB object. As the object is read from DB type, all the data like temperature, mesh and BCC of the Object will be carried over from previous operation (see Fig. 3DL3.22.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top die page

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0022.jpg' | relative_url }})

Workpiece as Read From DB object

### Top Die

In, Top Die page, user can define required object temperature for Top die. For this lab default temperature **300°F** is OK (see Fig. 3DL3.23.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0023.jpg' | relative_url }})

Top die object window

#### Import Geometry

In Geometry page, click on import geometry from library option (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})) and import the **Spike_Topdie1.STL** file from DEFORM installed folder \3D\LABS directory. Use ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) button to check the Geometry. Click on ![]({{ '/assets/icons/pre_icons/mo_symmetry_planes_label.jpg' | relative_url }}) option, define planar symmetry and click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) (see Fig. 3DL3.24.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0024.jpg' | relative_url }})

Assigned Top Die plane Symmetry

#### Generate Mesh

Click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button and select yes in Default Boundary condition popup, a mesh with 28000 elements is generated.

#### Assigning material Data

In Material Window, click on ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) to Load material data from Library and load '**AISI-H-13** ' material from **Die_material** category by clicking ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}) button as shown in Fig. 3DL3.25. Select the added material from window to assign it to Top Die as shown in Fig. 3DL3.26. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0025.jpg' | relative_url }})

Material window

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0026.jpg' | relative_url }})

Assigning Material to Top Die

#### Assigning BCC

Assigned Default Heat Exchange with Environment Boundary conditions for Top die are OK ( see Fig. 3DL3.27.), click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Bottom Die page.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0027.jpg' | relative_url }})

Assigned Heat exchange Boundary conditions for Top Die

### Bottom Die

For this lab, default temperature 300°F is OK for Bottom die (see Fig. 3DL3.28.), click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0028.jpg' | relative_url }})

Bottom Die window

#### Import Geometry

In Geometry page, click on import geometry from library option (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})) and import the **Spike_BottomDie.STL** file from DEFORM installed folder \3d\LABS directory. Use ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) button to check the Geometry. Click on ![]({{ '/assets/icons/pre_icons/mo_symmetry_planes_label.jpg' | relative_url }}) option, define planar symmetry and click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) (see Fig. 3DL3.29.) Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0029.jpg' | relative_url }})

Bottom Die Plane symmetry page

#### Generate Mesh

Click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button, select ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}) in Default Boundary condition popup, a mesh with 30500 elements is generated. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

#### Assigning material Data

Select the **AISI-H-13** material from Material list to assign it to Bottom Die as shown in Fig. 3DL3.26. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

#### Assigning BCC

Assigned Default Heat Exchange with Environment Boundary conditions for Bottom die are OK, see Fig. 3DL3.30. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until scheduled positioning page.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0030.jpg' | relative_url }})

Assigned Heat exchange Boundary conditions for Bottom Die

### Scheduled Positioning

Workpiece needs to be positioned so that it is resting on top of the Bottom Die. Since workpiece is read from DB type, it needs to be positioned by scheduled positioning. To schedule position click on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button and select ![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}). Change the Positioning Object to the **Workpiece** and the Reference to the **Bottom****Die**. Select the Approach Direction to**-Z** as shown in Fig. 3DL3.31. and then click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Defined scheduled positioning will appears as shown in Fig. 3DL3.32. and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0031.jpg' | relative_url }})

Object positioning Window

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0032.jpg' | relative_url }})

Scheduled Positioning window

### Inter-Object relations

Select **user** type contact and click on ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) button. It will add the relationship between the Workpiece, Top Die and Bottom Die as shown in Fig. 3DL3.33.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0033.jpg' | relative_url }})

Inter-object relations window

Highlight the Bottom Die – Workpiece relationship and click the ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) button to modify the relationship. In the friction section of the screen (see Fig. 3DL3.34.), there is a pull-down menu that allows the user to choose the appropriate friction conditions of Heat transfer processes. Under Thermal tab select **Free Resting type** Heat transfer coefficient in List. **0.0002** value will be added to Heat transfer coefficient field.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0034.jpg' | relative_url }})

Inter Object Relation Thermal page

Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to go back to Inter-Object window, since the Problem setup type is Batch mode Contact will generate while generating Database. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Step page.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0035.jpg' | relative_url }})

Inter object relation window

### Setting Simulation Controls

In Step Definition, Set the **Number of steps** to **10** , the **Step Increment** to **5** and **Solution step definition** **Time** to**0.2 sec** (see Fig. 3DL3.36.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0036.jpg' | relative_url }})

Step controls window

### Generate Database

When we visit Generate Database page, objects will be positioned as per defined Scheduled positioning data (see Fig. 3DL3.37.).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0037.jpg' | relative_url }})

Generate Database

By selecting the **File** menu ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **Export****** option, Save the Keyword File as "**Spike_Dwelling** ".

Click on ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) action label to check the problem. Generate database by clicking ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) action label.

Once the database has been generated, switch to the Simulation mode by selecting the ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the object tree. Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label under the simulation tab, Run Options dialog will open as shown in Fig. 3DL3.38.. Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0038.jpg' | relative_url }})

Run Simulation Popup

Monitor the progress of the simulation by looking at the Simulation Message and Simulation Log tab, making sure that the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked.

### Post processing

When the simulation has finished, click on ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}). In Step Browser click ![]({{ '/assets/icons/pre_icons/mo_all_button.jpg' | relative_url }}) on button to view all steps. 

To better view the chilling of the workpiece on the die, select the workpiece in the Object Tree and click the Single object mode ![]({{ '/assets/icons/pre_icons/mo_show_single_obj_icon.jpg' | relative_url }}) icon. Only the workpiece will be shown in the DISPLAY window. Select Temperature (![]({{ '/assets/icons/post_icons/mo_temp_sv.jpg' | relative_url }})) state variable and right-click on the Color Bar and select **Temperature** as the **Color Bar** Type. (See Fig. 3DL3.39.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0039.jpg' | relative_url }})

Temperature state variable plot for workpiece

Play through the steps of the simulation to look at the workpiece temperature. At Step -51, the position of the workpiece will shift downward where it was rested on the bottom die. Note how the base of the workpiece chills from Step -51 to Step 60 where it is in contact with the die. Turn on the Bottom Die and look at it's temperature distribution. Observe how the die heats up during the 2 second dwell. (See Fig. 3DL3.40.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0040.jpg' | relative_url }})

Temperature State variable plot for bottom Die

Now, select last step in Step browser and click on ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}) button to continue the setup.

## Spike Forging - Forging Blow1

In the previous operations, the workpiece underwent furnace transfer and dwell on the bottom die. The last step of the Dwell will be loaded into the Pre-processor mode and the first forging blow will be set up.

Add 3D Forming operation from the Explorer Operations list. Add the operation by clicking on 3D Forming ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button or can also be added by drag and drop into the Operation editor as shown in Fig. 3DL3.41. Select Forming operation from Operation editor, Setup type popup will appear and click on ![]({{ '/assets/icons/pre_icons/mo_no_batch_setup_button.jpg' | relative_url }}) button in Popup. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until objects page.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0041.jpg' | relative_url }})

Adding Forming operation to the Operation Editor

### Add objects

By default the three objects from the previous operation will be displayed. If not, by selecting ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) button, add three objects as shown in Fig. 3DL3.42. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0042.jpg' | relative_url }})

Adding Objects

### Workpiece

In workpiece page, select "**Read from DB** " radio button as shown in Fig. 3DL3.43. Since it is a read from DB object, all the data of this object will be carried over to this operation from previous operations. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top Die page.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0022.jpg' | relative_url }})

Selecting Workpiece as read from DB

### Top Die

In Top Die page, select "**Read from DB** " radio button. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Movement page.

#### **Assigning Die Movement**

****In Movement Page, Set a**Speed** of **2** in/sec in the **-Z** Direction as shown in Fig. 3DL3.44. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Bottom Die page.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0044.jpg' | relative_url }})

Movement control window

### Bottom Die

In Bottom Die page, select "**Read from DB** " radio button. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Scheduled positioning page.

### Scheduled Positioning the Top Die

In Scheduled positioning page, Click on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button and select ![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}) radio button. Change the Positioning Object to the **Top Die** and the Reference to the **workpiece**. Change the Approach Direction to **-Z** and then click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) (see Fig. 3DL3.45.) Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0045.jpg' | relative_url }})

Scheduled positioning window

### Inter-Object relations

In Inter-Object window, click on ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) button. Default relations get added as shown in Fig. 3DL3.46.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0046.jpg' | relative_url }})

Inter-Object window

The Thermal data needs to be modified so that a Forming heat transfer coefficient is used instead of the Free resting coefficient used in the previous operation. The default heat transfer coefficient for hot forming is added automatically which is used in this lab.

Friction needs to be defined between the workpiece and the dies since deformation will now be occurring. Highlight the first relationship in the table and click ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}). On the **Deformation****tab** , use the friction pull-down menu to select **Hot forging (lubricated)** from the list as shown in Fig. 3DL3.47., then click on **Thermal****tab** and Select **Forming** in pull down menu (see Fig. 3DL3.48.), then click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Back in the INTER-OBJECT window, click on ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) to change the other relationship to these settings.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0047.jpg' | relative_url }})

Inter-Object Data Deformation definition Window

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0048.jpg' | relative_url }})

Inter-Object Data Thermal definition Window

Contact will be generated while generating Database, Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Step page.

### Assigning Step Controls

Set the **Number of Simulation Steps** to **30** and the **Step Increment to Save** to **5**. Change the **Primary Die** to the **Top****Die** since it is the Top Die that is moving, and under Solution Steps Definition, set With **Constant Die Displacement** to **0.025** " as shown in Fig. 3DL3.49. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0049.jpg' | relative_url }})

Simulation Step controls window

### Database Generation

By selecting the **File** menu ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **Export** option, Save a keyword file for the problem as "**Spike_Forging_Blow1** ".

Click on ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) action label to check the problem. Generate a database by clicking ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) action label.

### Running Simulations

Once the database has been generated, switch to the Simulation mode by selecting the ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the object tree. Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label under the simulation tab, Run Options dialog will open as shown in Fig. 3DL3.38.. Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

Monitor the progress of the simulation by looking at the Simulation Message and Simulation Log tab, making sure that the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked.

While the simulation is running, the recent saved step can be viewed. Many different variables can be viewed such as plastic strain, plastic strain rate, temperature, etc... from state variables tool bar as shown in Fig. 3DL3.50.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0050.jpg' | relative_url }})

Simulation Graphics window

### Post processing

When the simulation has finished, click on ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}). In Step Browser click on ![]({{ '/assets/icons/pre_icons/mo_all_button.jpg' | relative_url }}) button to view all steps.

Look at both **Temperature** and **Effective****Strain** as shown in Fig. 3DL3.51. and Fig. 3DL3.52. Depending on the variable being viewed, user may want to toggle between the geometry and the mesh on the dies. When viewing Temperature, the mesh/temperature gradient in the dies can be shown by clicking the Show Mesh ![]({{ '/assets/icons/pre_icons/mo_show_mesh_icon.jpg' | relative_url }}) button (and also clicking the Show Geo ![]({{ '/assets/icons/pre_icons/mo_show_geo_icon.jpg' | relative_url }}) button to toggle off the geometry). Likewise, when viewing a variable like Effective Strain that only deforming objects would have, the geometries of the dies should probably be viewed instead of the mesh.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0051.jpg' | relative_url }})

Temperature State variables plot

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0052.jpg' | relative_url }})

Effective stress State variables plot

The amount of load required to deform an object is an important result that can be obtained from a simulation. Click on the ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) icon. When the GRAPH window appears, select only Top Die and the X-Axis is set to **Stroke** and the Y-Axis is set to **Z-Load**. Click ![]({{ '/assets/icons/post_icons/mo_plot_button.jpg' | relative_url }}) and a transparent Load-Stroke curve will display over the objects in the DISPLAY window as shown in Fig. 3DL3.53.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0053.jpg' | relative_url }})

Load Stroke plot

In Load Stroke Graph window, Switch to options tab and check Step tracer check box as shown in Fig. 3DL3.54.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0054.jpg' | relative_url }})

Load Stroke Graph Options window

So that, when a different step is selected, the bar in the Load-Stroke curve will highlight that step and the load for that step will be shown in the graph. Also, a point on the graph can be picked with the mouse and the displayed step will automatically change to the one corresponding to that point on the graph.

Now select last step in Step browser and click on ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}) button to continue the setup.

## Spike Forging - Die Change and Blow2

The first forging blow has been simulated and it is now time to model the second blow which uses a different top die. The new top die geometry will be imported and the second forging operation will be set up.

Add 3D Forming operation from the Explorer Operations list. Add the operation by clicking on 3D Forming ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button or can also be added by drag and drop into the Operation editor. Select Forming operation from Operation editor, Setup type popup will appear and click on NO- Batch mode button in Popup. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until objects page.

### Add objects

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Objects page. By default the three objects from the previous operation will be displayed. If not, by selecting ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) button, add three objects as shown in Fig. 3DL3.42. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Workpiece

In workpiece page, select "**Read from DB** " radio button. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top Die page.

### Changing Top die for Blow2

Both the geometry and mesh of the top die have to be changed. In Top Die page, change Object type to **rigid** and assign temperature as **300** °F then Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

#### Import Geometry

In Geometry page, click on import geometry from library option (![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }})) and import the **Spike_Topdie2.STL** file file from DEFORM installed folder \3d\LABS directory. Use ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) button to check the Geometry. Click on ![]({{ '/assets/icons/pre_icons/mo_symmetry_planes_label.jpg' | relative_url }}) option, define planar symmetry and Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) (see Fig. 3DL3.55.) Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0055.jpg' | relative_url }})

Assigned Plane Symmetry for Top Die

#### Generate Mesh

Click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button, select ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}) in Default Boundary condition popup. A mesh with default number of elements will be generated.

#### Assign Material

Select the material '**AISI-H-13** ' material from material window and assign it to the Top Die. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

#### Assigning BCC

In BCC page, Check the default assigned Heat exchange with Environment BCC for Top Die and make sure that default assigned Heat Exchange with Environment BCC is assigned to the entire outer surface of the top die except the symmetry planes (see Fig. 3DL3.56.).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0056.jpg' | relative_url }})

Assigning Heat Exchange with Environment BCC for Top Die

#### Assigning Die Movement

In Movement Page, Set a **Speed** of **2** in/sec in the -Z Direction. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Bottom Die

In Bottom Die page select "**Read from DB** " radio button. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Scheduled Positioning the Top Die

In Scheduled positioning page, Click on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button and select ![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}) radio button. Change the Positioning Object to the **Top****Die** and the Reference to the **workpiece**. Change the Approach Direction to**-Z** and then click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). 

### Inter-Object relations

In Inter-Object window, click on ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) button. Default relations get added as shown in Fig. 3DL3.47.

Friction needs to be defined between the workpiece and the dies since deformation will now be occurring. Also, the Thermal data needs to be modified so that a Forming heat transfer coefficient is used instead of the Free resting coefficient used in the previous operation.

Highlight the first relationship in the table and click ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}). On the Deformation tab, use the friction pull-down menu to select **Hot forging (lubricated)** from the list as shown in Fig. 3DL3.48. then click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Back in the INTER-OBJECT window, click on ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) to change the other relationship to these settings.

Contact will be generated between the Billet and both the Top and Bottom Dies while generating Database.

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) up to Step controls page.

### Assigning Step Controls

Set the**Number of Simulation Steps** to **10** and the **Step Increment to Save** to **5**. Change the Primary Die to the Top Die since it is the Top Die that is moving, and under Solution Steps Definition, set **With Constant Die Displacement** to **0.025** ". Click![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Database Generation

By selecting the **File****menu** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **Export****** option, Save a keyword file for the problem as "**Spike_Forging_Blow2** ".

Click on ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) action label to check the problem. Generate a database by clicking ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) action label.

Once the database has been generated, switch to the Simulation mode by selecting the ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the object tree. Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label under the simulation tab, Run Options dialog will open. Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

Monitor the progress of the simulation by looking at the Simulation Message and Simulation Log tab, making sure that the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked.

### Post processing

When the simulation has finished, click on ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}). In Step Browser click on ![]({{ '/assets/icons/pre_icons/mo_all_button.jpg' | relative_url }}) button to view all steps.

Play through the steps, focusing especially on the steps for the second forging blow, Steps-90 to 101. Use the ![]({{ '/assets/icons/pre_icons/mo_show_cotact_icon.jpg' | relative_url }}) button to view how the contact evolves through the simulation. Also, investigate temperature, effective strain and load vs. stroke behavior.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab03_spike_forging/image0057.jpg' | relative_url }})

Load-stroke Window with effective strain state variable plot

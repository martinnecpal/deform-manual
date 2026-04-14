---
lang: sk
title: "Lab 25 Stub Shaft Labs"
---

# Lab 25 Stub Shaft Labs

25.1. Stub Shaft Lab in 2D MO Forming

25.2. Tool Stress Analysis

25.3. Adding a Shrink ring to the Die

25.4. Simulating Thermal Effects

25.5. Warm Stub shaft with Mechanical press movement

25.6. Warm Stub shaft with Hydraulic press movement

25.7. Warm Stub shaft with Screw press movement

25.8. Warm Stub shaft with Hammer movement

## Stub Shaft Lab in 2D MO Forming

In this lab we will setup 2 operations :

**Operation1:** Cone Operation.

**Operation2:** Head operation.

**Operation1: Cone Operation**

### Create New Problem

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear as shown below [Fig. L25.1.]()).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0001.jpg' | relative_url }})

DEFORM GUI Main 

Create a new problem either by selecting **File****![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in Fig. L25.2. Select " **Integrated Manufacturing Process** " radio button and unit system as "**English** " using radio button. Define Problem Name as "**Stub_Shaft** " and make sure the “**Show option dialog** ” check box is turned on (if we do not turn on the “Show option dialog” check box, then we will not get the New Project dialog). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

Problem type selection window

Multiple operation wizard will open with the New Project dialog (see Fig. L25.3.), at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session we use ‘**Stub_Shaft** ’ as the project name. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0001.jpg' | relative_url }})

MO wizard New Project

### Adding 2D Forming operations

Multiple Operation wizard will opens with new project called **Stub_Shaft** to setup the problem. Add **two****2D Forming operations** from Operations list in Explorer. Operation can be add by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button next to 2D Forming operation (see Fig. L25.4.) or user can also add the operation by dragging and dropping the operation into Operation Editor region.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0002.jpg' | relative_url }})

Added 2D Forming operation into Operation Editor

### Geometry Type

In this lab we will be using Axisymmetric geometries, so select **2D****Axisymmetric** radio button from geometry type page as shown in Fig. L25.5. and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0003.jpg' | relative_url }})

Axisymmetric Geometry type selection

### Simulation Controls

In this lab we will be showing how to setup simple Isothermal problem. So in Simulation controls **uncheck** the **Heat****transfer****mode** check box (see Fig. L25.6.). Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0004.jpg' | relative_url }})

Simulation control window

### Assigning Material for Workpiece

In Material list window, Load the material '**AISI-4120** ' from DEFORM Material library, **Steel** category using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load material data from library) option. This can be done as shown in below by clicking ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}) button as shown in Fig. L25.7. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Object page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0005.jpg' | relative_url }})

Material List window

### Adding objects

For this operation we required four objects, hence in Object window add four objects by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) button (see Fig. L25.8.) and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0006.jpg' | relative_url }})

Adding Object Window

### Workpiece

In Workpiece window, change the object Name to **Billet** and select object type as **Plastic** as shown in Fig. L25.9. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0007.jpg' | relative_url }})

Billet object Window

#### Billet Geometry

In the Geometry page, select ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) and define a **cylinder** that has a **radius** of **0.4** ” and a **height** of **2.7** ” (see Fig. L25.10.). Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button. Check geometry and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0008.jpg' | relative_url }})

Defining the Geometry

#### Mesh generation

Switch to expert mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}), the default settings are adequate for generating a mesh. Click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) to generate the Mesh (see Fig. L25.11.).

Measure one of the smaller elements in the workpiece – they are in the range of 0.020”. Click the **Remesh criteria** **tab** and set the Interference Depth to ½ of this value, or **0.01** ” This setting prevents excessive overlap between the tools and the workpiece as material flows around corners (See Fig. L25.12.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0009.jpg' | relative_url }})

Billet Mesh window

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0010.jpg' | relative_url }})

Defining Remeshing Criteria

#### Assigning Billet Material

To assign material for workpiece select the material **AISI-4120** from material window. This can be done as shown in below Fig. L25.13. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0011.jpg' | relative_url }})

Material selection window

#### Billet Boundary conditions

In BCC page, check the default assigned Deformation BCC for Left side of the workpiece in X-Direction as shown in Fig. L25.14., default BCC are assigned automatically due to selection of problem type as axisymmetric. Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) up to Top die page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0012.jpg' | relative_url }})

Billet BCC window

### Top Die Definition

In Top Die page, change the name of the top die to **Punch** , Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

#### Import Punch geometry

Import **StubShaft_ConeTools.igs** file using Load Geometry from Library ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) button as shown in Fig. L25.15. Click ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}) for the Multiple boundary popup ( see Fig. L25.16.). When we click 'Yes' for the popup edit geometry will open as shown in Fig. L25.17. **Delete****the Loop 2** by using ![]({{ '/assets/icons/pre_icons/mo_delete_loop_button.jpg' | relative_url }}) (see Fig. L25.18.) and click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Check geometry and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until movement page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0013.jpg' | relative_url }})

Importing Punch Geometry

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0014.jpg' | relative_url }})

Popup to visit edit geometry

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0015.jpg' | relative_url }})

Edit Geometry window

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0016.jpg' | relative_url }})

Deleting the Loop 2 from imported geometry

#### Assign Movement to Top Die

Define a **S****peed** of **10** in/sec in**-Y** direction for this lab. Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Bottom Die page.

### Bottom Die Definition

In Bottom die page accept the Object type as **Rigid** and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) (see Fig. L25.19.).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0017.jpg' | relative_url }})

Bottom Die page

#### Import Bottom Die Geometry

Import **StubShaft_ConeTools.igs** file using Load Geometry from Library ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) button. Click ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}) for the Multiple boundary popup. When we click 'Yes' for the popup edit geometry will open. **Delete****the Loop 1** by using ![]({{ '/assets/icons/pre_icons/mo_delete_loop_button.jpg' | relative_url }}) (see Fig. L25.20.) and click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Check geometry and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Object 4 page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0018.jpg' | relative_url }})

Deleting Loop1 from Imported geometry

### Ejector Definition

In object 4 window, change the Object 4 Name to **Ejector** and select Object type as **Rigid** as shown in Fig. L25.21. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0019.jpg' | relative_url }})

Ejector object window

#### Ejector Geometry

In Ejector geometry window, select the ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}) to visit the edit geometry window and enter the geometry points in the table as shown in Fig. L25.22. and click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Check geometry and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Controls page.

**X** |  **Y** |  **R**  
---|---|---  
0 |  -2 |  0  
0.406 |  -2 |  0  
0.406 |  0 |  0  
0 |  0 |  0  
  
Ejector geometry data

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0020.jpg' | relative_url }})

Ejector geometry defining

### Controls

Confirm that the workpiece is positioned against the ejector, bottom die is positioned to workpiece and the punch is positioned against the workpiece, see Fig. L25.23. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Contact page. 

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0021.jpg' | relative_url }})

Positioning of the objects

### Contact Generation

Select **user** type contact and click on ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) button. It will add the relationship between the Billet, Punch, Bottom Die and Ejector as shown in Fig. L25.24. As the Dies are Rigid and Billet is plastic, Punch, Bottom Die and Ejector are considered as Master and Billet as Slave. In order to predict the fold during deformation, self contact will be assigned for Billet.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0022.jpg' | relative_url }})

Contact Generation page

Highlight the **Punch – Billet** relationship and click the ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) button to modify the contact conditions. In the friction section of the screen (see Fig. L25.25.), there is a pull-down menu that allows the user to choose the appropriate friction conditions of common forming processes.

Since this simulation takes place at room temperature and the dies are steel, use the pull down menu and select**Cold forming (steel dies)** from the list. A friction value of **0.12** will automatically be selected.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0023.jpg' | relative_url }})

Inter-Object data definition window

Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to go back to contact window, Since the friction conditions are the same for all the object pairs, the ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) button can be used to copy the interface properties from the first relationship to all of the others. After this is done, all relationships will have a friction of 0.12 defined. Use ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) icon to determine a suitable contact tolerance (a value of about 0.00040" will be calculated), then click ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) button to generate contact. Switch to Message tab or Observe status bar to know about the contacts generated. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Stopping Controls

We want to stop the simulation when the punch and die are within 0.025” of one another. In the Stopping Controls screen click on ![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }}) guided mode, **check** the **Distance between objects** option. Set the value for this distance to **0.025** ” in the **Y** direction. Click ![]({{ '/assets/icons/pre_icons/mo_mouse_icon.jpg' | relative_url }}) next to **Object 1** and click the bottom of the Punch object in the display. Click ![]({{ '/assets/icons/pre_icons/mo_mouse_icon.jpg' | relative_url }}) next to **Object 2** and click the top of the Bottom Die object in the display (see Fig. L25.26.), click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Step page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0024.jpg' | relative_url }})

Stopping Controls window

### Step Controls

We want the punch to travel 0.5” in **100****steps** , so each step will be 0.5/100 or 0.005”. In the Step Controls enter the Solution Steps Definition to be With Equal **Die****Displacement** of **0.005**.” set the **Number of Simulation Steps** to **100** and **Step Increment to Save** as 5. Set the Punch as Primary Die if not selected automatically (see Fig. L25.27.), click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0025.jpg' | relative_url }})

Step Controls window

### Generate Database

In Generate DB page. Click the ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) button to have the program check to see if anything was missed in the problem setup. During the checking process:

Messages in the red color signify data that needs to be fixed before a simulation can be run (such as when you forget to define any material data).

Click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database. When the program is done writing the database, click on ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) to go to Next operation.

**Operation2: Head operation.**

### Geometry Type

Select **2D****Axisymmetric****radio** button from geometry type page and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Simulation Controls

In Simulation controls **uncheck** the **Heat****transfer****mode** check box. Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Objects page.

### Adding objects

For this operation we required four objects, by default previous operation added four objects are added in object list. if not added objects by default, then add four objects by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) button (see Fig. L25.28.), then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) .

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0026.jpg' | relative_url }})

Adding Object Window

### Workpiece Definition

We will make the Workpiece object as Read Form DB. Select the Read from DB radio button in Workpiece page. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top Die page. (See Fig. L25.29.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0027.jpg' | relative_url }})

Workpiece object page

### Top Die Definition

In Top Die page, change the object type from Read from DB to **Rigid** , Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

#### Import Punch geometry:

Import **StubShaft_HeadTools.igs** file using Load Geometry from Library ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) button as shown in Fig. L25.30. Click ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}) for the Multiple boundary popup. When we click 'yes' for the popup edit geometry will open. **Delete the Loop 1** by using ![]({{ '/assets/icons/pre_icons/mo_delete_loop_button.jpg' | relative_url }}) (see Fig. L25.31.) and click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Check geometry and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until movement page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0028.jpg' | relative_url }})

Load Punch geometry

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0029.jpg' | relative_url }})

Edit Geometry window

#### Assign Movement to Top Die

Define a **speed** of **10** in/sec in**-Y** direction for this lab. Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Bottom Die page.

### Bottom Die Definition

In Bottom die page, change the object type from Read from DB to **Rigid****** and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

#### Import Bottom Die Geometry

Import **StubShaft_HeadTools.igs** file using Load Geometry from Library ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) button. Click ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}) for the Multiple boundary popup. When we click 'yes' for the popup edit geometry will open. **Delete the Loop 2** by using ![]({{ '/assets/icons/pre_icons/mo_delete_loop_button.jpg' | relative_url }}) (see Fig. L25.32.) and click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Check geometry and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Ejector page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0030.jpg' | relative_url }})

Deleting Loop2 from Imported geometry

### Ejector Definition

We will make the Ejector object as Read Form DB. Select the Read from DB radio button in Ejector page. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Positioning page.

### Positioning

In Object positioning page, position the **punch** using **offset****positioning**(x=0, y=2) towards Y direction (see Fig. L25.33.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Scheduled positioning page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0031.jpg' | relative_url }})

Positioning the Punch

### Scheduled Positioning

Using Interference positioning we are positioning the Punch to the Workpiece. In **Scheduled****positioning** page, Click on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button and select ![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}) radio button. Change the **Positioning****Object** to the **Punch** and the **Reference** to the **Billet**. Change the Approach Direction to **-Y** and then click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). (See Fig. L25.34.) Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0032.jpg' | relative_url }})

Scheduled Positioning window

### Contact Generation

Define the contact relations using the same settings which we defined for the first operation, see 25.1.12.Contact Generation. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Stopping Controls

We want to stop the simulation when the punch and billet are within 0.401” of one another. In the Stopping Controls screen, check the **Distance between objects** option. Set the value for this distance to**0.401** ” in the Y direction. Click ![]({{ '/assets/icons/pre_icons/mo_mouse_icon.jpg' | relative_url }}) next to **Object 1** and click the **Punch** object as seen in Fig. L25.35. Click ![]({{ '/assets/icons/pre_icons/mo_mouse_icon.jpg' | relative_url }}) next to **Object 2** and click the **Die** object as seen in Fig. L25.35.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0033.jpg' | relative_url }})

Distance Between Objects stopping control

We will also specify a maximum load for this part. check the **Max load** option. Set the Max load to X = 0, Y = 600 as shown in Fig. L25.36. Now if the press load exceeds 600Klb (300Tons), the simulation will stop, even if the distance between tools has not been reached. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0034.jpg' | relative_url }})

Stop controls page

### Step Controls

Estimate the total punch travel, which will be roughly 1.25”. We will maintain the stroke per step of **0.005** ”, so the simulation will require about 250 steps (1.25/0.005). Set the **Number of Simulation Steps** to **250.** (See Fig. L25.37.) Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0035.jpg' | relative_url }})

Step Controls window

### Generate Database

See the Status in Generate DB page, if we see Input error, check the data missing and complete it, for this lab sequence expect "DB generation is not required for this operation. It will occur at tun time." message.

Save the project and click on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) mode to run the simulation.

### Running simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. L25.38. Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0060.jpg' | relative_url }})

Run Simulation window

The progress of the simulation can be monitored as it is running by looking at the Simulation Message tab and Simulation Graphics from the Graphics display region in Simulation mode. As long as the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked in Simulation Message tab, which is the default setting, the Message file will refresh automatically.

The Message file provides information about which simulation step the simulation is currently on and also gives information dealing with how well the simulation is running.

When the simulation is finished without any issues, check the messages in LOG file, when all operation completes we will see messages in LOG file:"MULTIPLE OPERATION COMPLETED".

### Post process the results

After the simulation is completed, Switch to ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) tab.

#### State variables:

From the State variables list, click the **Effective strain** icon to plot the amount of strain that went into the workpiece. To change the plot settings, you can click on the ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) Set up icon. In this screen, you can display different kinds of contours (line, shaded or solid) as well as change the variable range that is shown on the contour bar. Using the Settings option, the range of the contour bar can be user-defined. Feel free to experiment with the display of the different state variables and plot options.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0036.jpg' | relative_url }})

Strain effective plot

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0037.jpg' | relative_url }})

Stress Effective Plot

#### Flownet

Flownet can be used to create a grid on the starting workpiece shape, the track the distortion of that grid through the simulation.

Click the Flownet ![]({{ '/assets/icons/post_icons/mo_flownet_icon.jpg' | relative_url }}) icon to open the Flownet dialog.

We will start with a **rectangular** Flownet. Select “**Grid** ” and click the ![]({{ '/assets/icons/post_icons/mo_flownet_next_button.jpg' | relative_url }}) button. Assign a “**Spacing** ” of **0.1** in the X direction, and **1** in the Y direction. Click ![]({{ '/assets/icons/post_icons/mo_preview_button.jpg' | relative_url }}) to view the grid. Then click ![]({{ '/assets/icons/post_icons/mo_flownet_next_button.jpg' | relative_url }}). We will not save any data, so click the ![]({{ '/assets/icons/post_icons/mo_generate_button.jpg' | relative_url }}) button. After the Flownet is calculated, play through the simulation to watch the evolution (see Fig. L25.41.).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0038.jpg' | relative_url }})

(a) Grid Flownet at second operation first step. (b) Grid Flownet at second operation last step

## Tool Stress Analysis

### Opening project file

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear.

Create a new problem either by selecting **File****![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear. Select " **Integrated Manufacturing Process** " radio button and unit system as "**English** " using radio button. Define Problem Name as "**StubShaft_ToolStress** " and make sure the “**Show option dialog** ” check box is turned on (if we do not turn on the “Show option dialog” check box, then we will not get the New Project dialog). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new problem using the Deform Integrated Manufacturing Process.

Multiple operation wizard will open with the New Project dialog (see Fig. L25.42.), at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session we use ‘**StubShaft_ToolStress** ’ as the project name. Select the copy existing project radio button, select the source location browse button and import the **Stub_Shaft.moproj** From the previously simulated Stub_shaft Project, **turn on** the **copy****Database** check box, click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) for project naming window. Stub_shaft simulation will get imported to 'StubShaft_ToolStress' project.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0039.jpg' | relative_url }})

Copying Stub_Shaft project using Copy project option

### Add Die stress Operation

Select Die stress 2D operation from the Explorer Operations list and Add the operation by selecting ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button or user can also add by drag and drop into the Operation Editor. Now, in Operation Editor,select the Die stress 2D operation.

### Add Objects 

For this operation we required three objects, hence Keep workpiece, Top Die and Bottom Die objects and delete the Ejector object using ![]({{ '/assets/icons/pre_icons/mo_delete_object_button.jpg' | relative_url }}) button. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Object1

By default for object 1, Workpiece (Read object from DB) radio button is selected. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Top Die

For Top Die, by default for Dies (Elastic) radio button is selected. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Mesh page.

#### Mesh Generation

Generate the mesh with **2000** elements. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Material page.

#### Assign material for Top die

Import a die material **AISI-D3** from the material library. Choose**AISI-D3** from the list to assign the material for Top die. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to BCC page.

#### Assign Boundary condition for Top die

Next we need to apply boundary conditions to the Top die, so that it does not fly off into space when the forming loads are applied to it. Assign Vy=0 boundary condition on the top edge of the Top die. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Force interpolation page.

#### Force Interpolation

Once the mesh is generated, the forming loads from the workpiece need to be interpolated onto the Top die. Interpolate the force by clicking ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}) option. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Bottom Die page.

### Bottom Die

For Bottom Die, by default Dies (Elastic) radio button is selected. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Mesh page. 

#### Mesh Generation

Generate the mesh with **2000** elements. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Material page.

#### Assign material for Bottom Die

Choose**AISI-D3** from the list to assign the material for Bottom Die. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to BCC page.

#### Assign Boundary condition for Bottom Die

Next we need to apply boundary conditions to the Bottom die, so that it does not fly off into space when the forming loads are applied to it.

Assign Vy=0 boundary condition on the bottom Edge of the Bottom Die. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Force interpolation page.

#### Force Interpolation

Once the mesh is generated, the forming loads from the workpiece need to be interpolated onto the Bottom die. Interpolate the force by clicking ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}) option. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Simulation controls.

### Simulation Controls

Define the **Number****of****steps****as** **1** , **step****increment****to****save** as **1** and **time****per****step** as **1**. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Generate Database

Click on ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) action label to check the problem. Generate a database by clicking ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) action label.

### Running simulation

Once the database has been generated, switch to the Simulation mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the operation tree. Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options. Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

### Post Processing

After the simulation is completed, Switch to ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) tab.

Using the State Variable option, plot Effective stress and Max Principal stress.

If the effective stress exceeds the yield stress of the material, plastic deformation of the tools will occur.

If the maximum principal stress is large, it may be a site for fatigue failure initiation.

In carbide tools, positive principal stresses, even if they are of relatively small magnitude, may be indicative of fatigue failure initiation.

Note that in this simulation, effective stress is extremely high.

## Adding a Shrink ring to the Die

After post processing switch back to the Pre- processor mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}) tab.

### Add Die stress Operation

Select Die stress 2D operation from the Explorer Operations list and Add the operation by selecting ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button or user can also add by drag and drop into the Operation Editor.

Now, in Operation Editor select the added Die stress 2D operation.

###  Add Objects

For this operation we required four objects, hence in Object window add another one object by clicking ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) button. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Object 4 page. 

### Defining Ring

In Object4 page, change the object name to **Ring** and accept the**Dies (Elastic)** object type. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

#### Case Geometry definition

Select the ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) and define a **hollow****cylinder** with **Inner****radius** as **1.5** ", **Outer****radius** as **3.5** " and **height** will be **3.25** ”, click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Mesh page.

#### Mesh generation

Generate the mesh with 2000 elements. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). 

#### Assign material for Case

Choose **AISI-D3** from the list to assign the material for Ring. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }})

#### Boundary conditions

Assign Velocity Vy=0 along the bottom edge of the Ring.

Assign a shrink fit of 0.007” along the ID of the Ring. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Positioning page.

### Positioning objects

Using **offset** with **Two points** , make the **Ring** as the **positioning object**. Click on the **bottom inside corner of the ring** , then the**bottom outside corner of the Bottom die**. DEFORM should pick the points From (1.5, 0) To (1.5, -0.75). If these are not the exact values in the object positioning window, edit the values to make them exact. Click the ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) button to move the Ring. Then click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to exit object positioning. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Contact page.

### Contact generation

We will make the Bottom Die as Slave, and the Ring as Master. click on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button to add **Ring** \- **Bottom Die** relation, select **Master object** as **Ring** and **Slave object** as **Bottom Die,** define Friction value as **0.12** and generate contact by click ![]({{ '/assets/icons/pre_icons/mo_generate_button.jpg' | relative_url }}) button. User should see a line of dots along the boundary. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Simulation Controls

Define the Number of steps as 1, step increment to save as 1 and time per step as 1. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to generate Database page. 

### Generate Database

Click on ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) action label to check the problem. Generate a database by clicking ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) action label.

### Running simulation

Once the database has been generated, switch to the Simulation mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the operation tree. Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options. Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

### Post Processing

Compare the stresses in first die stress operation (no shrink ring) with second die stress operation (with shrink ring). Stresses in second die stress operation should be lower, but still quite high. Use the state variable properties and use global rather than local scaling.

Note the stresses in the case are in the order of 1000KSI or higher. Adding a heavier interference fit will likely cause the ring to yield.

## Simulating Thermal Effects

In the next simulation, we will repeat the process as a warm forging. We will simulate transfer from the heat transfer, resting on the die, and the cone-forging blow.

### Transfer in Air

#### Opening project file

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear.

Create a new problem either by selecting **File****![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear. Select " **Integrated Manufacturing Process** " radio button and unit system as "**English** " using radio button. Define Problem Name as "**Stub_shaft_Warm** " and make sure the “**Show option dialog** ” check box is turned on (if we do not turn on the “Show option dialog” check box, then we will not get the New Project dialog). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new problem using the Deform Integrated Manufacturing Process.

MO wizard will open along with project naming window (see Fig. L25.43.). In the field of project name, in this session we use ‘****Stub_shaft_Warm**** ’ as the project name. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0040.jpg' | relative_url }})

Problem defining window

#### Add operations

Add two **2D Heat Transfer** operations and **one****2D Forming** operation from Operation list in Explorer as shown in Fig. L25.44. Operation can be added by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button next to respective operation or user can also add the operation by dragging and dropping the operation into Operation Editor region.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0041.jpg' | relative_url }})

Adding operations

#### Importing the DB

After adding all Three operations, import previously simulated **Stub_Shaft**.**DB** , select the first step and click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) as shown in Fig. L25.46.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0042.jpg' | relative_url }})

Importing DB

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0043.jpg' | relative_url }})

Step selection window

#### Geometry Type

In this lab we will be using Axisymmetric geometries, So select **2D****Axisymmetric** radio button from geometry type page and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). (See Fig. L25.47.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0003.jpg' | relative_url }})

Axisymmetric Geometry type selection

#### Selecting Heat Transfer Type

Select Heat Transfer Type as "**Transfer through air** " for first operation as shown in Fig. L25.48. This will set the default heat transfer settings for heating operation. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0044.jpg' | relative_url }})

Heat transfer type selection for Furnace Heating operation

#### Set Process Conditions

Define **Heating****time** as **5** **sec** at 68F furnace temperature or environment temperature as shown in Fig. L25.49 and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0045.jpg' | relative_url }})

Process condition window

#### Select Simulation Controls

Keep **only Heat Transfer mode** checked as only heat transfer is modelling as shown in Fig. L25.50. and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Billet page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0046.jpg' | relative_url }})

Simulation Controls settings for Furnace Heating

#### Defining Billet

In Billet object window accept the object type as ‘**Plastic** ’ and change the object temperature to **1750°F** as shown in**** Fig. L25.51. We will use the same geometry and mesh from the cold forming simulation. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Punch page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0047.jpg' | relative_url }})

Billet Definition Page

#### Punch Definition

In Punch page define the object temp to **300F** and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Mesh page.

##### Mesh Generation

Generate the mesh for the existing geometry. Generate a mesh with the default number of elements (see Fig. L25.52.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Material page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0048.jpg' | relative_url }})

Punch Mesh generation

##### Assigning Material for the Punch

Import a die material AISI-H-13 from the material library. Choose **AISI-H-13** from the list to assign the material for Punch. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Movement page.

##### Deleting Movement definition

Delete the Punch existing movement by using ![]({{ '/assets/icons/pre_icons/mo_delete_folder_icon.jpg' | relative_url }}) button in the top die movement page. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Bottom Die page.

#### Bottom die Definition

In Bottom die page define the object temp to **300F** and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Mesh page.

##### Mesh Generation

Generate the mesh for the existing geometry. Generate a mesh with the default number of elements. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Material page.

##### Assigning Material for the Bottom die

Choose **AISI-H-13** from the list to assign the material for Bottom die. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Ejector page.

#### Ejector Definition

In Ejector page define the object temp to **300F** and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Mesh page.

##### Mesh Generation

Generate the mesh for the existing geometry. Generate a mesh with the default number of elements. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Material page.

##### Assigning Material for the Ejector

Choose **AISI-H-13** from the list to assign the material for Ejector. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Positioning page.

#### Positioning

Click on ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) button. Use ![]({{ '/assets/icons/pre_icons/mo_offset_radio_button.jpg' | relative_url }}) to move the **Punch****3** inches in the “Y” direction. Also move the **workpiece** **2** inches in the “Y” direction. Click on to ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) exit the positioning menu. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Step controls window.

#### Step control

Set the **number of simulation steps** as **50** at 0.1sec each and saving every **5** steps (See Fig. L25.53.). Advanced Simulation controls settings are available in expert mode (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to proceed to the database generation stage.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0049.jpg' | relative_url }})

Step controls settings

#### Generate Database

In Generate DB page. Click the ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) button to have the program check to see if anything was missed in the problem setup. During the checking process:

Messages in the red color signify data that needs to be fixed before a simulation can be run (such as when you forget to define any material data).

Click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database. When the program is done writing the database, click on ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) to go to Next operation.

### Rest on die

#### Selecting Heat Transfer Type

Select **Rest on die transfer** type for second operation. This will set the default heat transfer settings for heating operation. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

#### Set Process Conditions

Define **Resting time** as **1** second with an environment temperature of 68**°** F as shown in Fig. L25.54. and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0050.jpg' | relative_url }})

Process condition window

#### Select Simulation Controls

Keep only **Heat Transfer mode** **checked** as only heat transfer is modelling and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

#### Defining Objects

By default all the objects will be in Read from DB, accept the default object types and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until scheduled positioning page.

#### Scheduled positioning

click on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Add) button and use ![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}) Positioning option to position the **Billet** against the **Ejector** in " -Y" direction. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

#### Contact Generation

Select **user** type contact and click on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Add relationship) button twice and select **Bottom****die** as **Master** and **Billet** as **Slave** for first relation and for second relation select **Ejector** as Master and **Billet** as Slave as shown in Fig. L25.55.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0051.jpg' | relative_url }})

Inter-object relationship between workpiece and bottom die

Click on **Bottom die- Billet**![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) (Edit) relationship button and select the pull down option "**Free Resting** " in the thermal section to define the inter-object heat transfer coefficient as shown in Fig. L25.56. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the Editing window. Then click on ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) button to copy the interface properties from the first relationship to the other relationships. It will generate the inter-object contact at the beginning of the resting operation while simulating. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until step controls window.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0052.jpg' | relative_url }})

Inter-object Heat transfer coefficient selection for resting

#### Step control

Set the **number of simulation steps** as **50** at **0.1** sec each and saving every **5 steps**. Advanced Simulation controls settings are available in expert mode (![]({{ '/assets/icons/pre_icons/mo_explorer_mode_icon.jpg' | relative_url }})). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to proceed to the database generation stage.

#### Generate Database

See the Status in Generate DB page. If we see Input error, check the data missing and complete it. For this lab sequence we expect to see "DB generation is not required for this operation. It will occur at run time." message. click on ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) to go to Next operation.

###  Form cone Operation

For the forming operation **turn****on** the **Deformation** check box along with **Heat transfer** in Simulation controls page. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

#### Defining the objects

In the Objects page, by default all four objects are added in list. If not, add four objects by using ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) button and make all four objects as Read from DB objects by visiting every object page. (See Fig. L25.57.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0053.jpg' | relative_url }})

Objects page

#### Punch Definition

**Defining the Punch movement**  
Define a **speed** of **10** in/sec in **-Y** direction for the Punch object. Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Scheduled positioning page.

#### Scheduled Positioning

In scheduled Positioning page, click on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Add) button and select the ‘**Positioning****object** ’ as **Punch** , method as ‘**Interference** ’ with respect to ‘**Billet** ’ in the **-Y** direction. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

#### Contact Generation

Select **user** type contact and click on ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) button. It will add the relationship between the Billet, Punch, Bottom Die and Ejector. As the Dies are Rigid and Billet is plastic, Top and Bottom Dies are considered as Master and Billet as Slave.

Highlight the **Punch – Billet** relationship and click the ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) button to modify the contact conditions. In the friction section of the screen (see Fig. L25.58.), there is a pull-down menu that allows the user to choose the appropriate friction conditions of common forming processes.

Since this is hot forming simulation and the dies are steel, use the pull down menu and select **Warm forming** from the list. A friction value of **0.25** will automatically be selected. Switch to **Thermal****tab** and select forming and select the pull down option "**Forming** " to define the inter-object heat transfer coefficient.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0054.jpg' | relative_url }})

Inter-object friction coefficient definition window

Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to go back to Inter-Object window, since the friction conditions are the same for all the object pairs, the ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) button can be used to copy the interface properties from the first relationship to all of the others. After this is done, all relationships will have a friction of **0.25** and Interface heat transfer as **0.004** as shown in Fig. L25.59. Since the contact will initialize and generate while generating database. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0055.jpg' | relative_url }})

Inter-Object relationship definition for forming operation

#### Stopping Controls

Set the stopping controls as explained in the section Stopping controls 25.1.13.

#### Step Controls

Set the step controls as explained in the section Step controls 25.1.14.

#### Generate Database

See the Status in Generate DB page. If we see Input error, check the data missing and complete it. For this lab sequence we expect to see "DB generation is not required for this operation. It will occur at run time." message.

#### Running simulation

Switch to the Simulation mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the operation tree. Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options. Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

#### Post process the results

After the simulation is completed, Switch to ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) tab.

check the load in the post-processor. 

How does the load compare to the cold forming case?

Point track temperature at several points in the head of the part. What happens to the temperature as the part is formed?

## Warm Stub shaft with Mechanical press movement

### Opening project file

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear.

Create a new problem either by selecting **File****![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear. Select " **Integrated Manufacturing Process** " radio button and unit system as "**English** " using radio button. Define Problem Name as "**StubShaft_Mecahical** " and make sure the “**Show option dialog** ” check box is turned on (if we do not turn on the “Show option dialog” check box, then we will not get the New Project dialog). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new problem using the Deform Integrated Manufacturing Process.

MO wizard will open along with project naming window (see Fig. L25.60.). In the field of project name, in this session we use ‘****StubShaft_Mecahical**** ’ as the project name. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0056.jpg' | relative_url }})

Problem defining window

### Add Forming Operation

  
Add 2D Forming operation from the Explorer Operations list. Add the operation by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button or user can also add by drag and drop into the Operation Editor.

### Importing the DB

After adding 2D Forming operation, import previously simulated **Stub_shaft_Warm.DB** , select the **first step of the third operation** and click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Punch Movement page.

### Punch Definition

**Punch Movement Definition**

Select the movement type as **Mechanical press**. The total stroke is the movement of the ram from top dead center to bottom dead center (or back to front, for a horizontal press).

We will specify a**total stroke** of **10** ”.

The forging stroke is the distance the punch travels from the time it contacts the workpiece until it reaches bottom dead center. For this simulation, the**forging stroke** will be **0.5** ”.

The number of Cycles/second is the speed of the flywheel. On a header, or a press without a clutch, it will equal the Cycles/second of the press. On a press with a clutch, it will be Flywheel RPM / 60 rev/sec or cycles/sec.

We will specify **1.1 Cycles / sec**.

We will keep rest of the settings as imported. click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until DB Generation page.

### Generate DB

Check the data and generate the DB. After generating DB switch to ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) mode to run the simulation.

### Running simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options. Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

After simulation complete, switch to ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) tab.

### Post processor

In Step Browser click on ![]({{ '/assets/icons/pre_icons/mo_all_button.jpg' | relative_url }}) button to view all steps. Play through the steps to see the deformation.

Go to the load-stroke ![]({{ '/assets/icons/post_icons/mo_load_stroke_icon.jpg' | relative_url }}) plot and plot the punch velocity vs time. Plot the load vs. time.

User can compare the maximum load using the press model to the maximum load using the constant speed approximation.

## Warm Stub shaft with Hydraulic press movement

### Opening project file

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear.

Create a new problem either by selecting **File****![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear. Select " **Integrated Manufacturing Process** " radio button and unit system as "**English** " using radio button. Define Problem Name as "**StubShaft_Hydraulic** " and make sure the “**Show option dialog** ” check box is turned on (if we do not turn on the “Show option dialog” check box, then we will not get the New Project dialog). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new problem using the Deform Integrated Manufacturing Process.

MO wizard will open along with project naming window (see Fig. L25.61.). In the field of project name, in this session we use ‘****StubShaft_Hydraulic**** ’ as the project name. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0057.jpg' | relative_url }})

Problem defining window

### Add Forming Operation

Add 2D Forming operation from the Explorer Operations list. Add the operation by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button or user can also add by drag and drop into the Operation Editor.

### Importing the DB

After adding 2D Forming operation, import previously simulated **Stub_shaft_Warm.DB** , select the **first step of the third operation** and click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Punch Movement page.

### Punch Movement Definition

Select the movement type as **Hydraulic press**. For this simulation, check the Power limit box, click the ![]({{ '/assets/icons/pre_icons/mo_define..._button2.jpg' | relative_url }}) button, and define the following values.

**Force** |  **Speed**  
---|---  
0 |  1.5  
20 |  1.3  
25 |  1.1  
30 |  0.7  
35 |  0.25  
38 |  0  
  
This means that the max speed of the press – unloaded – is 1.5 in/sec.

The max load of the press is 38 Klb at final step (stall speed.)

At 25 Klb, the press can maintain 1.1 in/sec.

Note that these load values are constructed to illustrate press behavior in this tutorial. The loads are quite small.

Define**constant speed** as **1.5** in/sec

We will keep rest of the settings as imported. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to close the definition then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until the DB Generation page.

### Generate DB

Check the data and generate the DB. After generating DB switch to ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) mode to run the simulation.

### Running simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options. Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

After simulation complete, switch to ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) tab..

### Post processor

In Step Browser click on ![]({{ '/assets/icons/pre_icons/mo_all_button.jpg' | relative_url }}) button to view all steps. Play through the steps to see the deformation.

Go to the load-stroke plot and plot the punch velocity vs time. Plot the load vs. time.

User can compare the maximum load using the press model to the maximum load using the constant speed approximation.

## Warm Stub shaft with Screw press movement

### Opening project file

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear.

Create a new problem either by selecting **File****![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear. Select " **Integrated Manufacturing Process** " radio button and unit system as "**English** " using radio button. Define Problem Name as "**StubShaft_Screw** " and make sure the “**Show option dialog** ” check box is turned on (if we do not turn on the “Show option dialog” check box, then we will not get the New Project dialog). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new problem using the Deform Integrated Manufacturing Process.

MO wizard will open along with project naming window (see Fig. L25.62.). In the field of project name, in this session we use ‘****StubShaft_Screw**** ’ as the project name. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0058.jpg' | relative_url }})

Problem defining window

### Add Forming Operation

Add 2D Forming operation from the Explorer Operations list. Add the operation by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button or user can also add by drag and drop into the Operation Editor.

### Importing the DB

After adding 2D Forming operation, import previously simulated **Stub_shaft_Warm.DB** , select the **f******irs** t step of the third operation** and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Punch Definition

**Punch Movement Definition**

Select the movement type as **Screw press**.

Specify:

**Energy** = **9** Klb-in  
**Moment of inertia** = 0.125 Klb-in-s^2  
**Lead Screw Pitch** = 5 in/rev  
**Efficienc****y** = 0.8  
We will keep rest of the settings as imported. click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until DB Generation page.

### Generate DB

Check the data and generate the DB. After generating DB switch to ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) mode to run the simulation.

### Running simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options. Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

After simulation complete, switch to ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) tab.

### Post processor

In Step Browser click on ![]({{ '/assets/icons/pre_icons/mo_all_button.jpg' | relative_url }}) button to view all steps. Play through the steps to see the deformation.

Go to the load-stroke plot and plot the punch velocity vs time. Plot the load vs. time.

User can rerun the simulation from the beginning with a higher energy.

## Warm Stub shaft with Hammer movement

### Opening project file

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear.

Create a new problem either by selecting **File****![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear. Select " **Integrated Manufacturing Process** " radio button and unit system as "**English** " using radio button. Define Problem Name as "**StubShaft_Hammer** " and make sure the “**Show option dialog** ” check box is turned on (if we do not turn on the “Show option dialog” check box, then we will not get the New Project dialog). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new problem using the Deform Integrated Manufacturing Process.

MO wizard will open along with project naming window (see Fig. L25.63.). In the field of project name, in this session we use ‘****StubShaft_Hammer**** ’ as the project name. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/2d_mobl25_image0059.jpg' | relative_url }})

Problem defining window

### Add Multi Blow Forging Operation

Add **2D Multi Blow Forging** operation from the Explorer Operations list. Add the operation by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button or user can also add by drag and drop into the Operation Editor.

###  Importing the DB

After adding 2D Multi Blow Forging operation, import previously simulated **Stub_shaft_Warm.DB** , select the **first step of the third operation** and click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}).

### Punch Definition

**Punch Movement Definition**  
Select the movement type as **Hammer**.

Specify Hammer controls.

Set:

**Energy** = **6** Klb-in  
**Mass** = **0.03** Klb-s^2/in

### Blow table

In the **Blow table** page, set 0.5 for the efficiency and define the number of hits as 4.

We will keep rest of the settings as imported. click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until DB Generation page.

### Generate DB

Check the data and generate the DB. After generating DB switch to ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) mode to run the simulation.

**Note** : While running the simulation, if the stopping criteria is met then further operations will not simulated.

### Running simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options. Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation. As we click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button simulation starts.

After simulation complete, switch to ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) tab.

### Post processor

In Step Browser click on ![]({{ '/assets/icons/pre_icons/mo_all_button.jpg' | relative_url }}) button to view all steps. Play through the steps to see the deformation.

Go to the load-stroke plot and plot the punch velocity vs time. Plot the load vs. time.

User can rerun the simulation from the beginning with a higher energy.

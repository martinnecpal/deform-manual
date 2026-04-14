---
lang: en
title: "Lab05 Stub Shaft Labs"
---

# Lab 5. Stub Shaft Labs

5.1. Operation1: Cone Operation

5.2. Operation2: Head Operation

5.3. Symmetry/Thermal Operations

5.4. Tool Stress Analysis

5.5. Adding a Shrink ring to the die

5.6. Mechanical Press

## Operation1: Cone Operation

### Creating New Problem

Create a new problem either by selecting **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****New Problem** or by clicking the **New****Problem**![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear. Select "**Integrated Manufacturing Process** " radio button and units system as "**English** " radio button in units field. Define Problem Name as "**Stub_Shaft** " and make sure the “**Show option dialog** ” check box is turned on (if we do not turn on the “Show option dialog” check box, then we will not get the New Project dialog). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new problem using the Deform Integrated Manufacturing Process.

MO wizard will open, at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session we use ‘**Stub_Shaft** ’ as the project name.

User can also change the Unit system and add operation by selecting from First operation pull down list and checkbox. Using copy Existing project option we can import previous saved projects as new project. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

### Adding operations

Add **two****3D****Forming****operations** from the Explorer Operations list. Add the operations by clicking on 3D Forming ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button or user can also add by drag and drop into the Operation Editor.

### Simulation Controls

In this lab we will be showing how to setup simple Isothermal problem. So in Simulation controls **uncheck** the **Heat****transfer** mode check box (see Fig. 3DL5.1.). Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0001.jpg' | relative_url }})

Simulation control window

### Material List

In Material list window, click on load material data from Library ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) option and Load the '**AISI-4120** ' Material from **Steel** category as shown in Fig. 3DL5.2. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Object page.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0002.jpg' | relative_url }})

Material List window

### Adding objects

If there aren't already four objects, add the four objects by clicking the object button ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) button (see Fig. 3DL5.3.), then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0003.jpg' | relative_url }})

Adding Object Window

### Workpiece

In Workpiece window, change the Object name to **Billet** and select Object type as **Plastic** as shown in Fig. 3DL5.4. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to geometry page.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0004.jpg' | relative_url }})

Billet object Window

#### Billet Geometry

In the Geometry page, select ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) and define a **cylinder** that has a **Diameter** of**0.8** ” and a **height** of **2.7** ” (see Fig. 3DL5.5.). Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button. Check geometry and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) till mesh page.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0005.jpg' | relative_url }})

Defining the Workpiece Geometry

#### Mesh generation

The default settings are adequate for generating a mesh. Click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) to generate the mesh. (see Fig. 3DL5.6.) Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0006.jpg' | relative_url }})

Workpiece Mesh generation

#### Assigning Billet Material

To assign material for workpiece select the material **AISI-4120** from material window. This can be done as shown in below Fig. 3DL5.7. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top die page.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0007.jpg' | relative_url }})

Material selection window

### Top Die Definition

In Top Die page, change the name of the top die to **Punch** , Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to geometry page.

#### Import Punch geometry

Import **StubShaft_ConePunch.STL** file using Load Geometry from Library ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) button as shown in Fig. 3DL5.8. Check geometry and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until movement page.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0008.jpg' | relative_url }})

Importing Punch Geometry 

#### Assign Movement to Top Die

Define a speed of **10** in/sec in **-Z** direction for this lab. Then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Bottom Die page.

### Bottom Die Definition

In Bottom die page, accept the Object type as **Rigid** and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) (see Fig. 3DL5.9.).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0009.jpg' | relative_url }})

Bottom Die page

#### Import Bottom Die Geometry

Import **StubShaft_ConeDie.STL** file using Load geometry from Library ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) button as shown in Fig. 3DL5.10. Check geometry and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Object 4 page.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0010.jpg' | relative_url }})

Importing Bottom Die geometry

### Ejector Definition

In object 4 window, change the Object 4 Name to **Ejector** and accept the Object type as **Rigid** as shown in Fig. 3DL5.11., Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0011.jpg' | relative_url }})

Ejector object window

#### Ejector Geometry

In Ejector geometry window, select and define a **cylinder** that has a **Diameter** of **0.817** ” and a height of **1** ” (see Fig. 3DL5.12.), click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button. Check geometry and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Positioning page.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0012.jpg' | relative_url }})

Ejector Geometry Definition

### Positioning

Click on ![]({{ '/assets/icons/pre_icons/mo_auto_position_button.jpg' | relative_url }}) and select ![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}) radio button. Change the Positioning Object to the **Ejector** and the Reference to the **Billet**. Change the Approach Direction to **Z** , Press ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) (see Fig. 3DL5.13.) and then click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Contact page.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0013.jpg' | relative_url }})

Object Positioning window

### Contact Generation

Select **user** type contact and click on ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) button. It will add the relationship between the Billet, Punch, Bottom Die and Ejector as shown in Fig. 3DL5.14. As the Dies are Rigid and Billet is plastic, Punch, Bottom Die and Ejector are considered as Master and Billet as Slave.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0014.jpg' | relative_url }})

Contact Generation page

Highlight the**Punch – Billet** relationship and click the ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) button to modify the contact conditions. In the friction section of the screen (see Fig. 3DL5.15.), there is a pull-down menu that allows the user to choose the appropriate friction conditions of common forming processes.

Since this simulation takes place at room temperature and the dies are steel, use the pull down menu and select **Cold forming (steel dies)** from the list. A friction value of **0.12** will automatically be selected.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0015.jpg' | relative_url }})

Inter-Object data definition window

Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to go back to contact window, Since the friction conditions are the same for all the object pairs, the ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) button can be used to copy the interface properties from the first relationship to all of the others. After this is done, all relationships will have a friction of 0.12 defined. Use ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) icon to determine a suitable contact tolerance (a value of about 0.001" will be calculated), then click ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) button to generate contact. Switch to Message tab or Observe status bar to know about the contacts generated. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Stopping Controls

We want to stop the simulation when the punch and die are within 0.025” of one another. In the Stopping Controls screen, check the**Distance between objects** option and then click points on the bottom of the Punch and on the top of the Bottom Die. Set the value for this distance to **0.025** ” in the**Z** direction.(see Fig. 3DL5.16.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0016.jpg' | relative_url }})

Stopping Controls window

### Step Controls

We want the punch to travel 0.5” in 50 steps, so each step will be 0.5/50 or 0.01”. In the Step Controls, under the **Solution Steps Definition** define the **Die Displacement** as **0.01** ”. Set the **Number of Simulation Steps** to **50** and **Step Increment to Save** to **5**. Set the **Punch** as **Primary Die** if not selected automatically (see Fig. 3DL5.17.) Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0017.jpg' | relative_url }})

Step Controls window

### Generate Database

In Generate DB page. Click the ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) button to have the program check to see if anything was missed in the problem setup. During the checking process:

Messages in the red color signify data that needs to be fixed before a simulation can be run (such as when you forget to define any material data).

Click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database. When the program is done writing the database, click on ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) tab to go to Next operation.

## Operation2: Head operation

### Simulation Controls

In Simulation controls, uncheck the **Heat****transfer** mode check box. Then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Objects page.

###  Adding objects

If there aren't already four objects, add the four objects by clicking the insert object ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) button (see Fig. 3DL5.18.), then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0018.jpg' | relative_url }})

Adding Object Window

### Workpiece Definition

We want to use the workpiece of previous operation last step so, we will make the Workpiece object as Read from DB. Select the **Read from DB** radio button in Workpiece page. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top Die (Punch) page. (see Fig. 3DL5.19.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0019.jpg' | relative_url }})

Workpiece object page

### Top Die Definition

In Top Die (Punch) page, change the Object type to **Rigid**. If the object name isn't Punch change it to Punch, Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

#### Import Punch geometry:

Import **StubShaft_HeadPunch.STL** file using Load Geometry from Library ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) button as shown in Fig. 3DL5.20. Check geometry and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until movement page.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0020.jpg' | relative_url }})

Loading Punch geometry

#### Assign Movement to Punch

Define a speed of **10** in/sec in **-Z** direction for this lab. Then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Bottom Die page.

### Bottom Die Definition

In the Bottom die page change the Object type to **Rigid** and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

#### Import Bottom Die Geometry

Import **StubShaft_HeadDie.STL** file using Load Geometry from Library ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) button. Check geometry and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until object4 (Ejector) page.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0021.jpg' | relative_url }})

Loading Bottom Die Geometry

### Ejector Definition

We will make the Ejector object as Read form DB. Select the Read from DB radio button in Ejector page. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Positioning page.

### Positioning

Click on ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) and change the Positioning Object to the **Punch**. Select ![]({{ '/assets/icons/pre_icons/mo_offset_radio_button.jpg' | relative_url }})radio button and position (x=0, y=0 and **Z** =**2**) towards **Z** direction and click ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) (see Fig. 3DL5.22.) and click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0022.jpg' | relative_url }})

Object Positioning window

### Scheduled Positioning

Using Interference positioning we are positioning the Punch to the Workpiece. In Scheduled positioning page, Click on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button and select ![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}) radio button. Change the Positioning Object to the **Punch** and the Reference to the **Billet**. Change the Approach Direction to **-Z** and then click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). (see Fig. 3DL5.23.) Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0023.jpg' | relative_url }})

Scheduled Positioning window

### Contact Generation

Define the contact relations using the same settings which we defined for the first operation in the section 5.1.11. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Stop Controls

Turn on the Distance between objects option and define the reference points as shown in the Fig. 3DL5.24. Set the stopping distance as **0.375** ” in **Z** direction.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0024.jpg' | relative_url }})

Distance Between Objects stopping control

We will also specify a **maximum****load** for this part. Under the **Deformation** tab, set the Max load to X = 0, Y =0 and Z= **600**. Now if the press load exceeds **600 Klb**(300Tons), the simulation will stop, even if the distance between tools has not been reached (see Fig. 3DL5.25.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0025.jpg' | relative_url }})

Stop controls page

### Step Controls

Estimate the total punch travel, which will be roughly 1.5”. At the end of the simulation we want a gap of 0.375. It’s ok if we overshoot the die travel by a little bit here because we will set a stopping condition to make sure that the tools stop when they are 0.375’’ apart. So we will only subtract 0.3 from 1.5. This will give us a total punch travel of 1.2. For 100 steps, that means that the punch needs to travel 0.012’’ every step.

Set the **Number of Simulation Steps** to **100** , **step increment to save** to **5** and **constant die displacement** as **0.012** ''. (see Fig. 3DL5.26.) Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0026.jpg' | relative_url }})

Step Controls window

### Generate Database

See the Status in Generate DB page, if we see Input error, check the data missing and complete it, for this lab sequence expect "DB generation is not required for this operation. It will occur at run time." message

Save the project and click on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) mode to run the simulation.

### Running simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label under the simulation tab (See Fig. 3DL5.27.), Run Options dialog will open as shown in Fig. 3DL5.28. Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0032.jpg' | relative_url }})

Simulation Options

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0028.jpg' | relative_url }})

Run Simulation window

The progress of the simulation can be monitored as it is running by looking at the Simulation Message tab and Simulation Graphics from the Graphics display region in Simulation mode. As long as the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked in Simulation Message tab, which is the default setting, the Message file will refresh automatically.

The Message file provides information about which simulation step the simulation is currently on and also gives information dealing with how well the simulation is running.

When the simulation is finished without any issues, check the messages in LOG file, when all operation completes we will see messages in LOG file:"MULTIPLE OPERATION COMPLETED".

### Post process the results

After the simulation is completed, Switch to ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) tab.

#### Play through results

Use the ![]({{ '/assets/icons/pre_icons/mo_preview_play_button.jpg' | relative_url }}) function to play through both the cone blow and the heading blow.

Experiment with different part shading options. 

#### Finding folds

Click on the ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) button to open the State Variables window.

Click on **folding****angle** and change scaling mode to “**User**.” Insert values of 270 and 271 for Min and Max respectively. Click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). (See Fig. 3DL5.29.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0029.jpg' | relative_url }})

State Variable Window with fold on workpiece

The fold can now be seen in red. User can play through the time steps and see the fold form. User can also right click on the color bar to experiment with different color bar types. (See Fig. 3DL5.30.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0030.jpg' | relative_url }})

Image showing fold in the workpiece

Use the slicing tool ![]({{ '/assets/icons/pre_icons/mo_slicing_option.jpg' | relative_url }}) to cut the piece vertically. Click on the radio button next to “**Curve + Plane** ” as shown in Fig. 3DL5.31.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0031.jpg' | relative_url }})

Slicing Window

With this view you can easily see the folds. (See Fig. 3DL5.32.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0032.jpg' | relative_url }})

Sliced Object

#### Determining Fill

Press clear ![]({{ '/assets/icons/post_icons/mo_clear_sv_icon.jpg' | relative_url }}) to turn off all the variables. Then turn on show contact nodes ![]({{ '/assets/icons/pre_icons/mo_show_cotact_icon.jpg' | relative_url }}) .

DEFORM places dots where contact has been made with the tool. Places without dots can represent an under fill situation (see Fig. 3DL5.33.). The fill can also be seen by cutting a section through the part.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0033.jpg' | relative_url }})

Determining filling in the object

Turn off contact ![]({{ '/assets/icons/pre_icons/mo_show_cotact_icon.jpg' | relative_url }}). Display all the tools and the workpiece ![]({{ '/assets/icons/pre_icons/mo_show_multi_obj_icon.jpg' | relative_url }}).

Use the slicing tool to slice the objects about the x-y plane (Make the N direction (0,0,1). Pick “**Curve** ” under the ‘Sliced plane display’ option. (See Fig. 3DL5.34.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0034.jpg' | relative_url }})

Slicing window 

Click on the Z coordinate next to the P (point) input. Then use the slider bar to move the slicing plane up and down the Z axis.

Select "+ Z direction" button to view the objects from the +Z direction as shown in Fig. 3DL5.35.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0035.jpg' | relative_url }})

Object in +Z view

User can directly see the gap between the tool and the workpiece. Delete ![]({{ '/assets/icons/pre_icons/mo_delete_symmetry_icon.jpg' | relative_url }}) the slicing plane from the slicing menu.

So far we have used qualitative methods to see under fill. User can also plot the distance between the workpiece and the tooling.

Click on State Variables ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) Icon. Select “**Minimum****distance** ” and press ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}).

Turn off all the tools and display just the workpiece ![]({{ '/assets/icons/pre_icons/mo_show_single_obj_icon.jpg' | relative_url }}). The normal distance between the workpiece and the closest tool will be displayed. User can left mouse click anywhere on the part. This will plot the minimum distance value on the color bar. (See Fig. 3DL5.36.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0036.jpg' | relative_url }})

Image Showing Minimum distance region

## Symmetry/Thermal Operations

### Create a new simulation

Now we are going to perform the Cone_Blow operation, from above, with a heated billet. This involves heating the billet, letting it sit in air for 6 seconds (transfer), letting it sit in the die for 2 seconds (dwell) and then forming it (cone). We will do all of this by simulating 1/12th of the part using symmetry as shown in [Fig. 3DL5.37.](lab05_stub_shaft_labs.htm#FIg_3DL5_37_Workpiece_showing_1/12th_of_the_symmetry)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0037.jpg' | relative_url }})

Workpiece showing 1/12th of the symmetry

Create a new problem either by selecting **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****New Problem** or by clicking the **New****Problem**![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear. Select "**Integrated Manufacturing Process** " radio button and units system as "**English** " radio button in units field. Define Problem Name as "****Stub_shaft_symmetry**** " and make sure the “**Show option dialog** ” check box is turned on (if we do not turn on the “Show option dialog” check box, then we will not get the New Project dialog). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0038.jpg' | relative_url }})

Problem defining window

MO wizard will open along with project naming window as shown in Fig. 3DL5.38. In the field of project name. In the field of project name, set the project name as '**Stub_shaft_symmetry** ' and click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}).

### Add operations

Add **two 3D Heat Transfer operations** and **one 3D Forming operations** from Operation list in Explorer. Operation can be add by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button next to respective operation or user can also add the operation by dragging and dropping the operation into Operation Editor region.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0039.jpg' | relative_url }})

Adding operations

### Importing the DB

After adding all three operations, import previously simulated **Stub_Shaft.DB** , select the **first****step** and click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0040.jpg' | relative_url }})

Importing DB

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0041.jpg' | relative_url }})

Step selection window

### Selecting Heat Transfer Type

Select Transfer through air heat transfer type for first operation as shown in Fig. 3DL5.42. This will set the default heat transfer settings for heating operation. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0042.jpg' | relative_url }})

Heat transfer type selection for Furnace Heating operation

### Set Process Conditions

Define **Heating****time** as **6** sec at **68°F** furnace temperature or environment temperature as shown in Fig. 3DL5.43. and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0043.jpg' | relative_url }})

Process condition window

### Select Simulation Controls

Keep only**Heat Transfer mode** checked as only heat transfer is modelling as shown in Fig. 3DL5.44. and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0044.jpg' | relative_url }})

Simulation Controls settings for Furnace Heating

### Material page

**Delete** the imported**AISI-4120[70-2200F(20-1200C)]** material from the list.

### Objects page

In objects page we are seeing all the objects imported from the stubshaft DB.

### Defining Billet

In Billet object window accept the **object****type** as ‘**Plastic** ’ and change the **object****temperature** to **2100** °**F**. (See Fig. 3DL5.45.) Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0045.jpg' | relative_url }})

Billet Definition Page

#### Billet Geometry

In the Geometry page, select and define a **cylinder** that has a **Diameter** of **0.8** ”, **height** of **2.7** ” and **Revolve****angle** as **30** deg (see Fig. 3DL5.46.). Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button. Check geometry and define the planar symmetry for the two symmetry surfaces (see Fig. 3DL5.47. and Fig. 3DL5.48.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until mesh page.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0046.jpg' | relative_url }})

Defining the Workpiece Geometry

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0047.jpg' | relative_url }})

Geometry page

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0048.jpg' | relative_url }})

Planar symmetry definition

#### Generate Mesh

Generate the mesh using **32000** elements (see Fig. 3DL5.49.). Complete range of meshing options are also available in expert mode (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})), if user needs to have more control on the mesh generated. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0049.jpg' | relative_url }})

Mesh generation window

#### Assign Workpiece Material

Using Load from library ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) option, load **AISI****-8620** material from **Steel** category, to assign material for workpiece select the material ‘**AISI****-8620** ’ from material window. This can be done as shown in Fig. 3DL5.50. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0050.jpg' | relative_url }})

Object material selection window

#### Defining Boundary Conditions

In BCC page, check the default assigned Heat exchange with Environment BCC to the entire outer surface of the Billet except symmetry surfaces. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Punch Movement page.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0051.jpg' | relative_url }})

BCC Definition window

### Punch Movement Definition

In Punch movement page, Change the “constant value” velocity to **0**. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Positioning page.

### Positioning

We will move the tools away from the object so they will not interfere with the cooling process. Click on the ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) button to open the positioning page. Use ![]({{ '/assets/icons/pre_icons/mo_offset.jpg' | relative_url }}) to move the **Punch****2** inches in the “**Z** ” direction. Also move the **Bottom****die** and Ejector **-2** inches in the “**Z** ” direction. Press ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to exit the positioning menu. (See Fig. 3DL5.52.) Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Step controls window

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0052.jpg' | relative_url }})

Objects positioning window

### Define Step Controls

Set the **Number of simulation steps** as **50** at **0.12** sec each and saving every**5** steps (see Fig. 3DL5.53.). Advanced Simulation controls settings are available in expert mode (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to proceed to the database generation stage.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0053.jpg' | relative_url }})

Simulation controls settings for furnace heating operation

### Generate Database

In Generate DB page. Click the ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) button to have the program check to see if anything was missed in the problem setup. During the checking process:

Messages in the red color signify data that needs to be fixed before a simulation can be run (such as when you forget to define any material data).

Click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database. When the program is done writing the database, click on ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) tab to go to Next operation.

### Selecting Heat Transfer Type (2nd Operation)

Select **Rest on die** heat transfer type for second operation as shown in Fig. 3DL5.54. This will set the default heat transfer settings for heating operation. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0054.jpg' | relative_url }})

Heat transfer type selection for Furnace Heating operation

### Set Process Conditions

Define **Resting time** as **2** sec at **68** °F furnace temperature or environment temperature as shown in Fig. 3DL5.55. and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0055.jpg' | relative_url }})

Process condition window

### Select Simulation Controls

Keep only **Heat Transfer mode** checked as only heat transfer is modelling as shown in Fig. 3DL5.56. and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until objects page.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0056.jpg' | relative_url }})

Simulation Controls settings for Furnace Heating

### Defining the objects

When we enter the second operation we are seeing all the objects as Read from DB, accept all the objects as Read from DB objects (see Fig. 3DL5.57.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Scheduled Positioning page.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0057.jpg' | relative_url }})

Objects page

### Scheduled Positioning

Use ![]({{ '/assets/icons/pre_icons/mo_offset_radio_button.jpg' | relative_url }}) Positioning option to move the Bottom die and Ejector **2** inches in the “**Z** ” direction (see Fig. 3DL5.58.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0058.jpg' | relative_url }})

Scheduled Positioning

### Contact Generation

Select **user** type contact and click on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Add relationship) button twice and select **Bottom****die** as Master and **Billet** as Slave for first relation and for second relation select **Ejector** as Master and **Billet** as Slave as shown in Fig. 3DL5.59.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0059.jpg' | relative_url }})

Inter-object relationship between workpiece and bottom die

Click on ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) (Edit) relationship button and select the pull down option "**Free Resting** " in the **thermal** section to define the inter-object heat transfer coefficient as shown in Fig. 3DL5.60. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the Editing window. It will generate the inter-object contact at the beginning of the resting operation while simulating. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until step controls window.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0060.jpg' | relative_url }})

Inter-object Heat transfer coefficient selection for resting

### Define Step Controls

Set the **number of simulation steps** as **20** at **0.1** sec each and saving **every****5** steps (see Fig. 3DL5.61.). Advanced Simulation controls settings are available in expert mode (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to proceed to the database generation stage.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0061.jpg' | relative_url }})

Simulation controls settings for furnace heating operation

### Generate Database

See the Status in Generate DB page, if we see Input error, check the data missing and complete it, for this lab sequence expect "DB generation is not required for this operation. It will occur at run time." message. Save the project and click on ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}).

### Select Simulation Controls( 3rd Operation)

For the forming operation **turn****on** the **Deformation** check box along with **heat****transfer**. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until objects page.

### Defining the objects

If there aren't already four objects, add the four objects by clicking the insert object ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) button (see Fig. 3DL5.62.). All four objects should be defined as Read from DB objects. If they aren't set them that way by visiting every object page.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0062.jpg' | relative_url }})

Objects page

### Defining Workpiece

**Workpiece Properties :**

In Billet Properties page, check "**Redefine : Target volume** " check box and select **Active in Meshing** radio button then click on the ![]({{ '/assets/icons/pre_icons/mo_target_volume_icon.jpg' | relative_url }}) icon. Click ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}) for popup window. (See Fig. 3DL5.63.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0063.jpg' | relative_url }})

Properties page

### Defining the Punch

**Defining the Punch movement :**

Define a speed of **4** in/sec in **-Z** direction for the Punch object. Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Scheduled positioning page.

### Scheduled Positioning

In scheduled Positioning page, click on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button and select the ‘Positioning object’ as **Punch** , method as ‘**Interference** ’ with respect to ‘**Billet** ’ in the **-Z** direction (see Fig. 3DL5.64.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0064.jpg' | relative_url }})

Scheduled Positioning window

### Contact Generation

Select **user** type contact and click on ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) button. It will add the relationship between the Billet, Punch, Bottom Die and Ejector (see Fig. 3DL5.66.). As the Dies are Rigid and Billet is plastic, Top and Bottom Dies are considered as Master and Billet as Slave.

Highlight the **Punch – Billet** relationship and click the ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) button to modify the contact conditions. In the friction section of the screen (see Fig. 3DL5.65.), there is a pull-down menu that allows the user to choose the appropriate friction conditions of common forming processes.

Since this is hot forming simulation and the dies are steel, use the pull down menu and select **Hot forming (lubricated)** from the list. A friction value of **0.3** will automatically be selected. Under **Thermal** tab select "**Forming** " from the list, a Heat transfer coeffecient of " **0.002** " .

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0065.jpg' | relative_url }})

Inter-object friction coefficient definition window

Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to go back to Contact window, Since the friction conditions are the same for all the object pairs, the ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) button can be used to copy the interface properties from the first relationship to all of the others. After this is done, all relationships will have a friction of 0.3 defined as shown in Fig. 3DL5.66. Since the contact will initialize and generate while generating database. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0066.jpg' | relative_url }})

Inter-Object relationship definition for forming operation

### Stopping Controls

We want to stop the simulation when the punch and die are within 0.025” of one another. In the Stopping Controls screen, check the **Distance between objects** option and then click points on the bottom of the punch and on the top of the Bottom Die. Set the value for this distance to **0.02****5** ” in the **Z** direction (see Fig. 3DL5.67.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Step controls page.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0067.jpg' | relative_url }})

Stopping Controls window

### Step Controls

We want the punch to travel 0.5” in 50 steps, so each step will be 0.5/50 or 0.01”. In the Step Controls enter the Solution Steps Definition to be With Equal Die Displacement of 0.01”. Set the **Number of Simulation Steps** to **50** and **Step Increment to Save** to **5**. Set the **Punch** as **Primary****Die** if not selected automatically (see Fig. 3DL5.68.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to DB generation page.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0068.jpg' | relative_url }})

Step Controls window

### Generate Database

See the Status in Generate DB page, if we see Input error, check the data missing and complete it, for this lab sequence expect "DB generation is not required for this operation. It will occur at run time." message.

Save the project and click on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) mode to run the simulation.

### Running simulation

Click on ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) label under the simulation tab (see Fig. 3DL5.70.), as we click on the Run option, use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_03_spike_isothermal/2d_mobl3_image0032.jpg' | relative_url }})

Simulation Options

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0070.jpg' | relative_url }})

Run Simulation window

The progress of the simulation can be monitored as it is running by looking at the Simulation Message tab and Simulation Graphics from the Graphics display region in Simulation mode. As long as the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked in Simulation Message tab, which is the default setting, the Message file will refresh automatically.

The Message file provides information about which simulation step the simulation is currently on and also gives information dealing with how well the simulation is running.

When the simulation is finished without any issues, check the messages in LOG file, when all operation completes we will see messages in LOG file:"MULTIPLE OPERATION COMPLETED".

### Post process the results

After the simulation is completed, Switch to ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) tab.

Click on ![]({{ '/assets/icons/pre_icons/mo_show_single_obj_icon.jpg' | relative_url }}) icon, so that only the workpiece is visible. Click **Temperature** state variable to plot the temperature of the workpiece. Right click on the Temperature scale and Select “**Color****bar type** ” then “**Temperature** ”. (See Fig. 3DL5.71.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0071.jpg' | relative_url }})

Object showing temperature values with Temperature Color Bar type

Click on **Mirror symmetry** ![]({{ '/assets/icons/post_icons/mo_3d_mirroring_icon.jpg' | relative_url }}) icon. Click on the symmetry faces until you can see the whole part. This will take 11 clicks. (See Fig. 3DL5.72.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0072.jpg' | relative_url }})

Mirroring of symmetric faces

## Tool Stress Analysis

### Opening project file

Create a new problem either by selecting **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****New Problem** or by clicking the **New****Problem**![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear. Select "**Integrated Manufacturing Process** " radio button and units system as "**English** " radio button in units field. Define Problem Name as "**StubShaft_ToolStress** " and make sure the “**Show option dialog** ” check box is turned on (if we do not turn on the “Show option dialog” check box, then we will not get the New Project dialog). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new problem using the Deform Integrated Manufacturing Process.

MO wizard will open along with project naming window. In the field of project name, select the **copy existing project** radio button. Select the source location browse button and **import** the **Stub_Shaft.moproj** From the previously simulated Stub_shaft Project, **turn on** the **copy Database check box** , click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) for project naming window. Stub_shaft simulation will get imported to 'StubShaft_ToolStress' project.

### Add Diestress Operation

Select Diestress 3D operation from the Explorer Operations list and Add the operation by selecting ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button or user can also add by drag and drop into the Operation Editor.

Now, in Operation Editor select the Diestress 3D operation

### Add Objects

For this operation we required three objects, hence Keep workpiece, Top Die and Bottom Die objects and delete the Ejector object. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Object 1 page.

### Object1

By default for object 1, Workpiece (Read object from DB) radio button is selected. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Top Die

For Top Die, by default Dies (**Elastic**) radio button is selected. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until mesh generation page.

#### Mesh Generation

Generate the mesh with **40000** elements. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

#### Force Interpolation

Once the mesh is generated, the forming loads from the workpiece need to be interpolated onto the Top die. Interpolate the force by clicking ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}) option. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }})

#### Assign material for Top die

Import a die material AISI-D3 from the material library. Choose **AISI-D3** from the list to assign the material for Top die. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }})

#### Assign Boundary condition for Top die

Next we need to apply boundary conditions to the Top die, so that it does not fly off into space when the forming loads are applied to it.

Assign Vx=Vy=Vz = 0 boundary condition on the top surface of the Top die. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Bottom die page.

### Bottom die

For Bottom Die, by default Dies (Elastic) radio button is selected. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until mesh generation page.

#### Mesh Generation

Generate the mesh with 40000 elements. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }})

#### Force Interpolation

Once the mesh is generated, the forming loads from the workpiece need to be interpolated onto the Bottom die. Interpolate the force by clicking ![]({{ '/assets/icons/pre_icons/mo_interpolate_force_button.jpg' | relative_url }}) option. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }})

#### Assign material for Bottom die

Choose **AISI-D3** from the list to assign the material for Bottom Die. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }})

#### Assign Boundary condition for Bottom die

Next we need to apply boundary conditions to the Bottom die, so that it does not fly off into space when the forming loads are applied to it.

Assign Vx=Vy=Vz = 0 boundary condition on the bottom surface of the Bottom Die. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Simulation controls page

### Simulation Controls

Define the **Number of steps** as **1** , **step increment to save** as **1** and **time per step** as **1**. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Generate Database

Click on ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) action label to check the problem. Generate a database by clicking ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) action label.

Once the database has been generated switch to the Simulation mode by selecting the ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the object tree. Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

### Post Processing

Using the State Variable pull-down menu, plot**Effective stress** and **Max Principal stress.**

If the effective stress exceeds the yield stress of the material, plastic deformation of the tools will occur.

If the maximum principal stress is large, it may be a site for fatigue failure initiation.

In carbide tools, positive principal stresses, even if they are of relatively small magnitude, may be indicative of fatigue failure initiation.

Note that in this simulation, effective stress is extremely high.

## Adding a Shrink ring to the die

After post processing switch back to Pre Mode by clicking ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}) tab.

### Add Die stress study Operation

At top Left corner of the Display window, Left mouse click on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button and select Add Die stress Study operation. A Die stress Study operation get added into operation editor. 

### Step Selection

To perform Die stress operation, select the second operation last step in step selection list. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Add Objects

In this die stress study, we will analyze only Top die and Bottom die with shink ring, hence delete the Ejector object using ![]({{ '/assets/icons/pre_icons/mo_delete_object_button.jpg' | relative_url }}) and add new object to create Ring object by clicking ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) button. 

Follow the instructions from 5.4.5 Top die section to 5.4.6.4 section to generate mesh, assign material,add BCC and interpolate forces over Top die and Bottom die. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Object 4 page.

### Object4

Change object name to **Ring** and accept the Dies (**Elastic**). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

#### Ring Geometry definition

Select the ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) and define a **hollow****cylinder** with **3** ” as**Internal Dia** , **8** ” as **Outer Dia** and **3.25** ” **height**. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

#### Mesh generation

Generate the mesh with **20000** elements. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

#### Assign material for Ring

Choose **AISI-H-13** from the list to assign the material for Ring. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

#### Boundary conditions

Assign Vx=Vy=Vz = 0 velocity boundary condition on the bottom surface of the Ring.

Assign a **shrink****fit** of 0.01” along the **ID** of the **Ring**. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) til positioning page.

### Positioning objects

Right-click in the graphics window and select measurement style > CAD style in Z direction. Select a point on the top surface of the Ring and a point on the top surface of the bottom die and measure the distance; it will be approximately 0.7499. Click the ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) button. Select the ![]({{ '/assets/icons/pre_icons/mo_offset_radio_button.jpg' | relative_url }}) radio button, choose **Ring** as the positioning object and offset it by**0.7499** in the "**-Z** " direction (0,0,-0.7499). Click the ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) button to move the Ring. Then click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to exit object positioning. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Contact generation

click on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Add relationship) button and select **Ring** as Master and ****Bottom****die**** as Slave for relation and click on ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) button. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Simulation Controls

Define the**Number of steps** as **1** , **step increment** **to** **save** as **1** and **time****per****step** as **1**. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Generate Database

Click on ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) action label to check the problem. Generate a database by clicking ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) action label.

Once the database has been generated switch to the Simulation mode by selecting the ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the object tree. Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

### Post Processing

Compare the stresses in first die stress operation (no shrink ring) with second die stress operation (with shrink ring). Stresses in second die stress operation should be lower, but still quite high. Use the state variable properties, and use global rather than local scaling.

Note the stresses in the Ring are in the order of 200KSI or higher. Adding a heavier interference fit will likely cause the ring to yield.

## Mechanical Press

### Opening project file

Open the DEFORM GUI Main window as done in the previous labs. Click the ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon to create a new problem. The New Problem window will appear. Select the **Integrated Manufacturing process** radio button and **English** Units radio button . and make sure the “**Show option dialog** ” check box is turned on (if we do not turn on the “Show option dialog” check box, then we will not get the New Project dialog). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new problem using the Deform Integrated Manufacturing Process.

MO wizard will open along with project naming window. In the field of project name, set the project name as '**StubShaft_Mechanical** ' and click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}).

### Add Forming Operation

Add **3D Forming operation** from the Explorer Operations list. Add the operation by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button or user can also add by drag and drop into the Operation Editor.

### Importing the DB

After adding 3D Forming operation, import previously simulated **Stub_shaft_symmetry.DB** , select the first step of the third operation and click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}). 

#### Punch Movement Definition

Select Punch Movement page from Operation tree, select movement library in the Explorer, select the “mechanical_press_700_Ton_National”. Add the mechanical Press movement by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button which is placed in front of the “**mechanical_press_700_Ton_National** ” movement. (see Fig. 3DL5.73.)

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0073.jpg' | relative_url }})

Mechanical Press Library

### Generate DB

Check the data and generate the DB. After generating DB switch to ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) mode to run the simulation.

### Running simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

After simulation complete, switch to ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) tab.

### Post processor

In Step Browser click on ![]({{ '/assets/icons/pre_icons/mo_all_button.jpg' | relative_url }}) button to view all steps. Play through the steps to see the deformation.

**Point Tracking:**  
Click on the ![]({{ '/assets/icons/post_icons/mo_point_tracking_icon.jpg' | relative_url }}) and select several points on the workpiece as shown in Fig. 3DL5.74. Click on ![]({{ '/assets/icons/post_icons/mo_track_button.jpg' | relative_url }}) and click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) for point tracking window.

Then click Temperature state variable. This will plot the Temperature vs. Time for all the points that you selected.

![]({{ '/assets/images/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/image0074.jpg' | relative_url }})

Point Tracking Graph

---
lang: en
title: "Lab 15 Sliding die lab - Punch Sleeve"
---

# Lab 15 Sliding die lab - Punch Sleeve

This lab will demonstrate how to setup movement controls for a Punch Sleeve loaded with springs, the other end of the springs or mounted onto punch. The Sleeve slides back when load is applied beyond pre-load.

  
15.1. Create New Problem

15.2. Geometry Type

15.3. Simulation Controls

15.4. Loading Material for Workpiece

15.5. Adding objects

15.6. Workpiece

15.7. Punch Definition

15.8. Die Definition

15.9. Sleeve Definition

15.10. Ejector Definition

15.11. Positioning

15.12. Contact Generation

15.13. Stopping Controls

15.14. Step Controls

15.15. Generate Database

15.16. Running Simulation

15.17. Post Processing the Results

## Create New Problem

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear.

Create a new problem either by selecting **File** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear. Select "**Integrated Manufacturing Process** " radio button and unit system as "**English** " radio button in unit field. Define Problem Name as "**Punch_Sleeve** " and make sure the “**Show option dialog** ” check box is turned on (if we do not turn on the “Show option dialog” check box, then we will not get the New Project dialog). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new problem using the Deform Integrated Manufacturing Process.

Multiple operation wizard will open with the New Project dialog, at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session, we use ‘**Punch_Sleeve** ’ as the project name. Add **2d forming operation** as**first operation** by selecting it from First operation pull down list and turning on checkbox as shown in Fig. L15.1. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0001.jpg' | relative_url }})

MO wizard New Project

## Geometry Type

In this lab, we will be using Axisymmetric geometries so, select **2D Axisymmetric** radio button from geometry type page as shown in Fig. L15.2. and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). 

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0002.jpg' | relative_url }})

Axisymmetric Geometry type selection

## Simulation Controls

We will be modelling Non- Isothermal sliding die movement setup in this lab so, in Simulation controls make sure both **Deformation** and **Heat transfer** **modes** are checked as shown in Fig. L15.3. Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0003.jpg' | relative_url }})

Simulation control window

## Loading Material for Workpiece

In Material list window, Load the material '**AISI-1015** ' from DEFORM Material library, **Steel** category using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load material data from library) option. This can be done as shown in below by clicking ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}) button, see Fig. L15.4. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Object page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0004.jpg' | relative_url }})

Material List window

##  Adding objects

For this operation we need five objects, hence in Object window add **five****objects** by clicking ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button (see Fig. L15.5.) and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0005.jpg' | relative_url }})

Adding Object Window

## Workpiece

In Workpiece window select the object type as **Plastic** and keep the temperature as 68°F, see Fig. L15.6. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0006.jpg' | relative_url }})

Workpiece object Window

### Workpiece Geometry

In the Geometry page, select ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) and define a cylinder with **radius** of **0.4** ” and a **height** of **2.7** ” (see Fig. L15.7.). Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button. Check geometry and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Mesh page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0007.jpg' | relative_url }})

Defining the Geometry

### Mesh generation

The default number of elements are adequate for this lab, so keep the **number of elements** as **1000** and click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) to generate the Mesh (see Fig. L15.8.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0008.jpg' | relative_url }})

Workpiece Mesh window

### Assigning Workpiece Material

To assign material for workpiece select the material **AISI-1015** from material window. This can be done by selecting material from the list in the material window as shown in below Fig. L15.9. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0009.jpg' | relative_url }})

Material selection window

### Workpiece Boundary conditions

In BCC page, verify the Deformation BCC assigned to Left side of the workpiece in X-Direction and Heat exchange with Environment BCC to the entire outer surface of the workpiece (which does not include the centerline since these nodes are inside the object) that are assigned by default during meshing. If the BCC’s are not assigned, assign them manually as shown in below Fig. L15.10. and Fig. L15.11. Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top die page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0010.jpg' | relative_url }})

Assigned Velocity BCC for Workpiece

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0011.jpg' | relative_url }})

Assigned Heat Exchange with Environment BCC for Workpiece

## Punch Definition

In Top Die page change the Name to **Punch** , keep the Object type as **Rigid** and Object Temperature 68°F, Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Import Punch geometry

In Geometry window, load **PunchSleeve_Lab_Punch.geo** geometry file from library using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load geometry from library) option as shown in Fig. L15.12., Click **Yes** for the 'User Library' popup asking whether to use the installation labs folder path as default library location. The geometry is located in DEFORM installation folder \2D\Labs directory. Check the geometry using ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) option to make sure the geometry is OK. Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until movement page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0012.jpg' | relative_url }})

Punch Geometry page

### Assign Movement to Punch

Define a **speed** of **10** in/sec in **-Y** direction for this lab (see Fig. L15.13.). Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Bottom Die page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0013.jpg' | relative_url }})

Punch Movement page

## Die Definition

In Bottom Die page change the name to **Die** , keep the object type as **rigid** and temperature 68°F, Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Import Die Geometry

Import **PunchSleeve_Lab_Die.geo** file using Load Geometry from Library ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) button as shown in Fig. L15.14. Check geometry and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) up to object 4 page. 

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0014.jpg' | relative_url }})

Die Geometry page

## Sleeve Definition

In Object 4 page change the Name to **Sleeve** , keep the Object type as **Rigid** and Object Temperature as 68°F, Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Import Die Geometry

Import **PunchSleeve_Lab_Sleeve.geo** file using Load Geometry from Library ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) button as shown in Fig. L15.15. Check geometry and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until movement page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0015.jpg' | relative_url }})

Sleeve object page

### Assign Movement to Sleeve

Select Movement type as **Sliding****die**. Define Sliding movement direction as **Y** with constant **stiffness****10****klb/in** , **Preload****1** **klb** and **Max. displacement****0.5** ". Select other end of spring as mounted on **Punch object** as shown in Fig. L15.16. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until object 5 page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0016.jpg' | relative_url }})

Sleeve Movement Page

## Ejector Definition

In Object 5 page change the Name to **Ejector** , keep the Object type as **Rigid** and Object Temperature 68°F, Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Ejector Geometry

Import **DieSleeve_Lab_Ejector.geo** file using Load Geometry from Library ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) button (see Fig. L15.17.). Check geometry and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Positioning page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0017.jpg' | relative_url }})

Ejector geometry defining

## Positioning

In this lab if objects are created or imported as per instructions then objects will be at correct position (see Fig. L15.18. ). If objects are not positioned correctly, use ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) button to position the objects as shown in Fig. L15.18. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until contact page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0018.jpg' | relative_url }})

Objects position

## Contact Generation

Select **User** type contact and click on ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) button. It will add relationships between the Workpiece, Punch, Die, Sleeve and Ejector as shown in Fig. L15.19.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0019.jpg' | relative_url }})

Default relations in contact Generation page

Highlight the **Punch – Workpiece** relationship and click the ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) button to modify the relationship. In the friction section of the screen (see Fig. L15.20.), there is a pull-down menu that allows the user to choose the appropriate friction conditions for common forming processes.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0020.jpg' | relative_url }})

Inter-Object data definition window

In **F******riction** pull down menu** select **Cold Forming (carbide dies)** from the list, a friction value of **0.08** will be added to the Constant friction field. Under **Thermal****tab** select **Forming** type Heat transfer coefficient from list, **0.002** value will be added to Heat transfer coefficient field. (See Fig. L15.21.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0021.jpg' | relative_url }})

Inter Object Relation Thermal page

Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to go back to contact window, Since the friction conditions are the same for all the object pairs, the ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) button can be used to copy the interface properties from the first relationship to all of the other relationships. After this is done, all relationships will have a friction of 0.08 and Heat transfer coefficient of 0.002 defined.

The sleeve with sliding movement controls is mounted on the punch and moves with the punch as the simulation progresses. The sleeve contacts, and may penetrate, the die, so define a contact relation between the die and the sleeve and make die the master. Click on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button to add a contact relation. Select **Die** as the **master** and **Sleeve**(which has sliding movement controls) as the **slave**. (See Fig. L15.22.)

Use ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) icon to determine a suitable contact tolerance (a value of about 0.000403" will be calculated), then click ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) button to generate contact. (See Fig. L15.22.) Switch to Message tab or Observe status bar to know about the contacts generated. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0022.jpg' | relative_url }})

Contact generated between objects

## Stopping Controls

We will stop the simulation when punch moves by 0.48”. In the Stopping Controls screen, check the **Max Die stroke** option and then define the **Y** stroke value as **0.48** ". (See Fig. L15.23.) Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0023.jpg' | relative_url }})

Stopping Controls window

## Step Controls

In step controls page, define **Number of steps** as **1000** , **Step increment to save** as **5** and **Die displacement per step** as **0.005** ". As we defined more number of steps than required for total primary die displacement, simulation will stop when it reaches the stopping control. Set the punch as Primary Die if not selected automatically, see Fig. L15.24. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0024.jpg' | relative_url }})

Step Controls window

## Generate Database

In Generate DB page, click the ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) button to have the program check to see if anything was missed in the problem setup. During the checking process:

Messages in the red color signify data that needs to be fixed before a simulation can be run (such as when you forget to define any material data).

Click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database.

## Running Simulation

Once the database has been generated, switch to the Simulation mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the operation tree. Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. L15.25. Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0033.jpg' | relative_url }})

Run Simulation window

The progress of the simulation can be monitored as it is running by looking at the Simulation Message tab and Simulation Graphics from the Graphics display region in Simulation mode. As long as the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked in Simulation Message tab, which is the default setting, the Message file will refresh automatically.

The Message file provides information about which simulation step the simulation is currently on and also gives information dealing with how well the simulation is running.

When the simulation has finished, the following message will be displayed at the end of the Message file (See Fig. L15.26.):

"PROGRAM STOPPED!

THE STROKE -0.4800000 HAS EXCEEDED THE SPECIFIED LIMIT 0.4800000".

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0025.jpg' | relative_url }})

Simulation Message file

## Post Processing the Results

After simulation has been completed, click on ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) tab, MO post processor will open. Select Display Stroke from right click options in step list. Play the steps until sleeve starts moving upward when punch stroke is around 0.275". (See Fig. L15.27.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0026.jpg' | relative_url }})

Load-Stroke graph at step sleeve starts sliding up

Plot **Load-stroke** curve and observe the load at this point. We observe that as sleeve experiences load beyond defined Pre-load that is 1 klb, it starts moving upwards. Continue to play animation and stop it when sleeve reverses its movement direction, at this point measure the distance between the Sleeve bottom right corner and Die top right corner and compare it with the Max. Displacement defined in Sleeve sliding movement controls. We can observe that sleeve stopped moving upward once the Max. Displacement defined in Sleeve sliding movement controls is reached. (See Fig. L15.28.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0027.jpg' | relative_url }})

Sleeve load and displacement when it reached max displacement

Continue to play animation to observe material flow and at last step check the total top die displacement using measurement option. (See Fig. L15.29.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0028.jpg' | relative_url }})

Workpiece at last step

####  State variables:

Go to last step and from the **State variables** list, plot important state variables like **Effective strain** , **Effective stress** , **Temperature** and **Damage** as shown in Fig. L15.30. to Fig. L15.33.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0029.jpg' | relative_url }})

Effective Strain state variable plot

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0030.jpg' | relative_url }})

Effective Stress state variable plot

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0031.jpg' | relative_url }})

Temperature state variable plot

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_15__sliding_die_lab__punch_sleeve/2d_mobl15_image0032.jpg' | relative_url }})

Damage state variable plot

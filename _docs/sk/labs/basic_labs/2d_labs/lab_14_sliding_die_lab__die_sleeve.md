---
lang: sk
title: "Lab 14 Sliding die lab - Die Sleeve"
---

# Lab 14 Sliding die lab - Die Sleeve

This lab will demonstrate how to setup movement controls for a sliding die. In the lab, the bottom die is a sliding die loaded on springs fixed at bottom.

  
14.1. Create New Problem

14.2. Geometry Type

14.3. Simulation Controls

14.4. Loading Material for Workpiece

14.5. Adding objects

14.6. Workpiece

14.7. Top Die Definition

14.8. Bottom Die Definition

14.9. Die Pin Definition

14.10. Positioning

14.11. Contact Generation

14.12. Stopping Controls

14.13. Step Controls

14.14. Generate Database

14.15. Running Simulation

14.16. Post Processing the Results

## Create New Problem

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear.

Create a new problem either by selecting **File** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear. Select "**Integrated Manufacturing Process** " radio button and unit system as "**English** " radio button in unit field. Define Problem Name as " ******Die_Sleeve** " and make sure the “**Show option dialog** ” check box is turned on (if we do not turn on the “Show option dialog” check box, then we will not get the New Project dialog). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new problem using the Deform Integrated Manufacturing Process.

Multiple operation wizard will open with the New Project dialog, at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session, we use ‘**Die_Sleeve** ’ as the project name. Add **2d forming operation** as**first operation** by selecting it from First operation pull down list and turning on checkbox as shown in Fig. L14.1. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0001.jpg' | relative_url }})

MO wizard New Project

## Geometry Type

In this lab, we will be using Axisymmetric geometries so, select **2D Axisymmetric** radio button as geometry type from geometry type page as shown in Fig. L14.2. and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0002.jpg' | relative_url }})

Axisymmetric Geometry type selection

## Simulation Controls

In this lab, we will be demonstrating how to setup Non- Isothermal sliding die movement controls so, in Simulation controls make sure both **Deformation** and**Heat transfer** **modes** are checked (see Fig. L14.3.). Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0003.jpg' | relative_url }})

Simulation control window

## Loading Material for Workpiece

In Material list window, Load the material '**AISI-4140** ' from DEFORM Material library, Steel category using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load material data from library) option. This can be done by clicking ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}) button as shown in Fig. L14.4. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Object page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0004.jpg' | relative_url }})

Material List window

## Adding objects

For this operation we need four objects, hence in Object window add four objects by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) button (see Fig. L14.5.) and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0005.jpg' | relative_url }})

Adding Object Window

## Workpiece

In Workpiece window, change the Object temperature to **1850** °F and select Object type as **Plastic** as shown in Fig. L14.6. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0006.jpg' | relative_url }})

Billet object Window

### Create Workpiece Geometry

In the Geometry page, select ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) and define a **cylinder** with **Radius** of **1.5** ” and a **Height** of **4.5** ” (see Fig. L14.7.). Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button. Check geometry and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0007.jpg' | relative_url }})

Defining the Geometry

### Mesh generation

The default number of elements are not adequate to capture the finisher shape, so select the **number of elements** as **2000** and click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) to generate the Mesh (see Fig. L14.8.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0008.jpg' | relative_url }})

Workpiece Mesh page

### Assigning Billet Material

To assign material for workpiece, select the material **AISI-4140** from material window (see Fig. L14.9.) and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0009.jpg' | relative_url }})

Material selection page

### Billet Boundary conditions

In BCC page, verify Velocity BCC under Deformation to the Left side of the workpiece in X-Direction and Heat exchange with Environment BCC to the entire outer surface of the Billet (which does not include the centerline since these nodes are inside the object) that are assigned by default during meshing. If the BCC’s are not assigned, assign them manually as shown in below Fig. L14.10. and Fig. L14.11. Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top die object page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0010.jpg' | relative_url }})

Assigned Velocity BCC for Workpiece

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0011.jpg' | relative_url }})

Assigned Heat Exchange with Environment BCC for Workpiece

## Top Die Definition

In Top Die object page, keep the name as Top Die, object type as **R****igid** and default temperature 68°F. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) .

### Import Top die geometry

In Geometry window, load **DieSleeve_Lab_TopDie.geo** geometry file from library using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load geometry from library) option as shown in Fig. L14.12., Click **Yes** for the 'User Library' popup asking whether to use the installation labs folder path as default library location. The geometry is located in DEFORM installation folder \2D\LABS directory. Check the geometry using ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) option to make sure the geometry is OK. Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until movement page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0012.jpg' | relative_url }})

Top Die Geometry page

### Assign Movement to Top Die

Define a **Speed** of **3** in/sec in **-Y** direction for this lab. Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Bottom Die page. (See Fig. L14.13.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0013.jpg' | relative_url }})

Top Die Movement page

## Bottom Die Definition

In Bottom Die page, keep the name, object type and default temperature as it is, click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Import Bottom Die Geometry

Import **DieSleeve_Lab_BottomDie**.**geo** file using Load Geometry from Library ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) button. Check geometry and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until movement page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0014.jpg' | relative_url }})

Bottom Die Geometry page

### Assign Movement to Bottom Die

Select Movement type as **Sliding Di****e**. Define sliding die movement direction as**-Y** direction with constant **stiffness****500** klb/in, **Preload****2500** klb, **Max. disp**. **2.5** in and select other end of spring as**Fixed** as shown in Fig. L14.15. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until object 4 page. For more information on Sliding Die Movement Controls see Section [15.7. Sliding Die](/docs/sk/pre_processor/15_movement_controls_definition/15_7_sliding_die/).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0015.jpg' | relative_url }})

Bottom Die Movement Page

## Die Pin Definition

In object 4 window, change the Object 4 Name to **Die Pin** and select Object type as **Rigid** and Retain the default temperature as it is, click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) .

### Die Pin Geometry

Import **DieSleeve_Lab_DiePin.geo** file using Load Geometry from Library ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) button (see Fig. L14.16.). Check geometry and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until positioning page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0016.jpg' | relative_url }})

Die Pin geometry defining

## Positioning

Click on ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) button. In object positioning page, select Interference positioning and select the **Positioning object** as **Workpiece** and the **Reference****object** as **Bottom Die**. An approach direction of**–Y** should be used and then click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). The workpiece is positioned over the Bottom Die. Zoom in on the lower right corner of the workpiece, you will see that the default Interference value of 0.0001 was a little too large for these geometries as there is too much overlap between the objects. Add five more zeros to the Interference to make it .000000001 and then ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}). You should see that the workpiece is now positioned in the die with the correct amount of overlap. Position the **Top die** (Position Object) over the **Workpiece** (Reference Object) using interference with an approach direction of **–Y**. (See Fig. L14.17. and Fig. L14.18.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0017.jpg' | relative_url }})

Positioning of the objects : Positioning window

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0018.jpg' | relative_url }})

Positioning of the objects :Objects before and after positioning

## Contact Generation

Select **User** type contact and click on ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) button. It will add relationships between the Workpiece, Top Die, Bottom Die and Die Pin as shown in Fig. L14.19.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0019.jpg' | relative_url }})

Default relations in contact Generation page

Highlight the **Top Die – Workpiece** relationship and click the ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) button to modify the relationship. In the friction section of the screen (See Fig. L14.20.), there is a pull-down menu that allows the user to choose the appropriate friction conditions for common forming processes.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0020.jpg' | relative_url }})

Inter-Object data definition window

In Friction pull down menu select**Hot forging (lubricated)** from the list, a friction value of **0.3** will be added to the Constant friction field. Under **Thermal** tab select **Forming** from type Heat transfer coefficient list, **0.002** value will be added to Heat transfer coefficient field. (See Fig. L14.21.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0021.jpg' | relative_url }})

Inter Object Relation Thermal page

Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to go back to contact window, Since the friction conditions are the same for all the object pairs, the ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) button can be used to copy the interface properties from the selected relationship to all relationships. After this is done, all relationships will have a friction of 0.3 and Heat transfer coefficient of 0.002 defined.

As simulation progress, top die comes down and contacts bottom die and may penetrate Bottom Die hence define the contact relation between top and bottom die to avoid penetration. Click on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button to add contact relation, select **Top die** as **Master** and **Bottom die** which has sliding movement controls defined as **S******lav** e**. (See Fig. L14.22.)

Use ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) icon to determine a suitable contact tolerance (a value of about 0.00067" will be calculated), then click on ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) button to generate contact (see Fig. L14.22.). Switch to Message tab or Observe status bar to know about the contacts generated. Click on **![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }})**.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0022.jpg' | relative_url }})

Contact generated between objects

## Stopping Controls

We want to stop the simulation when the top die moves **4.5** ”. In the Stopping Controls screen, check the **Max Die stroke** option and then define the **Y** stroke value as **4.5** ".as shown in Fig. L14.23. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) .

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0023.jpg' | relative_url }})

Stopping Controls window

## Step Controls

In step controls page, define **Number of steps** as **1000** , **Step increment to save** as **5** and **Die displacement per step** as **0.01** ". Since we defined more number of steps than required for total primary die displacement, simulation will stop when it reaches the stopping control. Set the Top Die as Primary Die if not selected automatically (see Fig. L14.24.) Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0024.jpg' | relative_url }})

Step Controls window

## Generate Database

In Generate DB page, click the ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) button to have the program check to see if anything was missed in the problem setup. During the checking process:

Messages in the red color signify data that needs to be fixed before a simulation can be run (such as when you forget to define any material data).

Click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database.

## Running Simulation

Once the database has been generated, switch to the Simulation mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the operation tree. Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. L14.25. Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0032.jpg' | relative_url }})

Run Simulation window

The progress of the simulation can be monitored as it is running by looking at the Simulation Message tab and Simulation Graphics from the Graphics display region in Simulation mode. if the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked in Simulation Message tab, which is the default setting, the Message file will refresh automatically.

The Message file provides information about which simulation step the simulation is currently on and information dealing with how well the simulation is running.

When the simulation has finished, the following message will be displayed at the end of the Message file (see Fig. L14.26.):

"PROGRAM STOPPED!

THE STROKE -4.5000000 HAS EXCEEDED THE SPECIFIED LIMIT 4.5000000".

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0025.jpg' | relative_url }})

Simulation message file

## Post Processing the Results

After simulation has been completed, click on ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) tab, MO post processor will open. In the **Step Browser,** right-click a step and select **Display****Stroke**. Play the steps and observe the bottom die when top die stroke is around 2.4". We can observe that Bottom Die starts moving downward in the negative Y direction along with the top die. If we plot Load-Stroke plot for bottom die, we can observe that Bottom Die moves downward when its load reaches 2513 klb (see Fig. L14.27.), which is beyond the preload defined in Bottom Die movement controls page

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0026.jpg' | relative_url }})

Load-Stroke graph at step bottom die starts sliding down

As you continue to play animation, observe material flow and at last step check the total displacement of Top Die. (See Fig. L14.28.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0027.jpg' | relative_url }})

Workpiece at last step

#### State variables

Go to last step and from the **State variables** list, plot important state variables like **Effective strain** , **Effective stress** , **Temperature** and **Damage** as shown in Fig. L14.29. to Fig. L14.32.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0028.jpg' | relative_url }})

Effective Strain state variable plot

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0029.jpg' | relative_url }})

Effective Stress state variable plot

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0030.jpg' | relative_url }})

Temperature state variable plot

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_14_sliding_die_lab__die_sleeve/2d_mobl14_image0031.jpg' | relative_url }})

Damage state variable plot

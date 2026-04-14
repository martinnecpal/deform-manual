---
lang: en
title: "2D Radiation Analysis Lab"
---

# 2D Radiation analysis of a plane finned surface

1.1. Creating a New problem

1.2. Operation1: Heat Transfer operation

1.3. Operation2: Steady state heat transfer operation

1.4. Operation3: Transient state heat transfer operation

1.5. Post Processing

## Creating a New problem

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear

Create a new problem either by selecting **File** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in Fig. 2DRAL1.1. Select "**Integrated Manufacturing Process** " radio button and unit system as "**SI** " radio button in unit field. Define Problem Name as "**Fin_Radiation_Analysis** " and make sure the “Show option dialog” check box is turned on (if we do not turn on the “**Show option dialog** ” check box, then we will not get the New Project dialog in MO UI). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/applications/55_2_arc_welding/image0002.jpg' | relative_url }})

Problem Setup window

Multiple operation wizard will open with the New Project dialog, along with project naming window, defined problem name is updated as ‘**Fin_Radiation_Analysis** ’ as the project name and selected unit system updated. Confirm that First operation check box is unchecked as we will add operation later and use the default (home) directory. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to add project. This lab will be referenced in future labs so it is important to use the name above.

![]({{ '/assets/images/applications/55_radiation_analysis_lab/2d_radiation_analysis_lab/image0002.jpg' | relative_url }})

MO New Project window

## Operation1: Heat Transfer operation

Multiple Operation wizard will opens new project. Add 2D Heat transfer operation from the Explorer Operations list. Operation can be add by clicking on 2D Heat transfer operation ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button (see Fig. 2DRAL1.3.) or user can also add by drag and drop into the Operation Editor.

![]({{ '/assets/images/applications/55_radiation_analysis_lab/2d_radiation_analysis_lab/image0003.jpg' | relative_url }})

Added 2D Heat Transfer operation into Operation Editor

### Selecting Geometry Type

In this lab we are using Plane strain geometries, so activate 2D **Plane****strain** radio button in geometry type page as shown in Fig. 2DRAL1.4., then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/applications/55_radiation_analysis_lab/2d_radiation_analysis_lab/image0004.jpg' | relative_url }})

2D Plane strain Geometry type selection

### Selecting Heat transfer type

Select "**Transfer through air** " as heat transfer type for Air Transfer operation as shown in Fig. 2DRAL1.5. This will set the default heat transfer settings for heating operation. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/applications/55_radiation_analysis_lab/2d_radiation_analysis_lab/image0005.jpg' | relative_url }})

Heat Transfer type selection page

### Process condition

In this operation we are heating the Fin bottom surface from External fluid for 1200 sec. So, define **Process****duration** as **1200** sec as shown in Fig. 2DRAL1.6. Use default Environment temperature and Convection coefficient, then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) .

![]({{ '/assets/images/applications/55_radiation_analysis_lab/2d_radiation_analysis_lab/image0006.jpg' | relative_url }})

Process condition page

### Simulation mode selection

In Simulation controls by default only Heat transfer mode will be selected for **Heat****transfer** operation under Sim mode Tab (In guided mode) (see Fig. 2DRAL1.7.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until object page.

![]({{ '/assets/images/applications/55_radiation_analysis_lab/2d_radiation_analysis_lab/image0007.jpg' | relative_url }})

Simulation controls page

### Adding Objects

In Object window now by default one object will be added in list. For this lab we required two objects, so add another object by click on ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) button (see Fig. 2DRAL1.8.), then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/applications/55_radiation_analysis_lab/2d_radiation_analysis_lab/image0008.jpg' | relative_url }})

Adding Object window

### Workpiece

In Workpiece window, change the Object Name to **Fin** and select Object type as **Plastic** and Define Object temperature as **38** °C as shown in Fig. 2DRAL1.9. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/applications/55_radiation_analysis_lab/2d_radiation_analysis_lab/image0009.jpg' | relative_url }})

Workpiece object window

### Importing Fin geometry

In Geometry window, load **Fin_Geometry.geo** geometry file from library using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Load geometry from a file) option. The geometry is located in DEFORM installation folder \2D\LABS\ Radiational_analysis directory. Check the geometry using ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) option to make sure the geometry is OK. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/applications/55_radiation_analysis_lab/2d_radiation_analysis_lab/image0010.jpg' | relative_url }})

Check and Correct Geometry window

### Fin mesh page

Switch to Expert mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) (switch to expert mode) icon from the tool bar. Expert mode will provide more options for detailed settings. Define **Target number of elements** as **3000** , **Thickness****elements** as **2** and **Size****ratio** as **1** , generate the mesh by clicking on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button as shown in Fig. 2DRAL1.11. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/applications/55_radiation_analysis_lab/2d_radiation_analysis_lab/image0011.jpg' | relative_url }})

Workpiece mesh page

### Assigning material for Fin

In Material window, using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }})Import material data from a file option import **Fin_material.key** from DEFORM installation folder \2D\Labs\ Radiational_analysis directory (see Fig. 2DRAL1.12.). Assign Fin_material and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/applications/55_radiation_analysis_lab/2d_radiation_analysis_lab/image0012.jpg' | relative_url }})

Assigning Fin material page

### Defining Boundary condition for Fin

In BCC, assign Heat exchange with Environment to entire surface except right and left sides as shown in Fig. 2DRAL1.13.

![]({{ '/assets/images/applications/55_radiation_analysis_lab/2d_radiation_analysis_lab/image0013.jpg' | relative_url }})

Assigned Heat exchange with Environment for Fin

#### Adding Heat Exchange with Environment BCC windows

From Environment window option we are adding **two** **windows** , one on Top surface of the Fin and one at the bottom surface of Fin. Click on Env. Window button, In Heat Exchange window page click on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button to add first window, **Add window on top surface of Fin** as shown in Fig. 2DRAL1.14. Define Environment temperature as **38** °C and Emissivity as 1, select Convection Coefficient as Function of Temperature, click on ![]({{ '/assets/icons/pre_icons/mo_define..._button2.jpg' | relative_url }}) button and import **Convection_coeffecient_win1.dat** from \2D\Labs\ Radiational_analysis directory using Load button as shown in Fig. 2DRAL1.15. and click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}).

![]({{ '/assets/images/applications/55_radiation_analysis_lab/2d_radiation_analysis_lab/image0014.jpg' | relative_url }})

Assigning first Heat Exchange window for Fin

![]({{ '/assets/images/applications/55_radiation_analysis_lab/2d_radiation_analysis_lab/image0015.jpg' | relative_url }})

Convection coefficient value for first window region

Now click on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button to add second window, Add window on bottom surface of Fin as shown in Fig. 2DRAL1.16., Define **Environment****temperature** as **100** °C and **Emissivity** as **0.8** , select **Convection****Coefficient** as **Function****of****Temperature** , click on Define button and import **Convection_coeffecient_win2.dat** from \2D\LABS\ Radiational_analysis directory using ![]({{ '/assets/icons/pre_icons/mo_load.._button.jpg' | relative_url }}) button as shown in Fig. 2DRAL1.17. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to close Function window. Close Heat Exchange window by click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top die page.

![]({{ '/assets/images/applications/55_radiation_analysis_lab/2d_radiation_analysis_lab/image0016.jpg' | relative_url }})

Assigning second Heat Exchange window for Fin

![]({{ '/assets/images/applications/55_radiation_analysis_lab/2d_radiation_analysis_lab/image0017.jpg' | relative_url }})

Convection coefficient value for second window region

### Top die page

In Top Die page change the Object name to **External_Body** and define Temperature to **38°C** as shown in Fig. 2DRAL1.18. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/applications/55_radiation_analysis_lab/2d_radiation_analysis_lab/image0018.jpg' | relative_url }})

External Body page

### Import External body geometry

In Geometry window, **External_body.geo** geometry file from library using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Load geometry from a file) option. The geometry is located in DEFORM installation folder \2D\Labs\ Radiational_analysis directory. Check the geometry using ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) option to make sure the geometry is OK. Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Generating mesh for External body

Define **Target number of elements** as **100** and **Size ratio** as **1** , generate the mesh by clicking on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button as shown in Fig. 2DRAL1.19. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/applications/55_radiation_analysis_lab/2d_radiation_analysis_lab/image0019.jpg' | relative_url }})

External body mesh page

### Assigning material for External body

In Material window, using Import material data from a file ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) option import **External_Fluid.key** from DEFORM installation folder \2D\Labs\ Radiational_analysis directory (see Fig. 2DRAL1.20.). Assign **External_Fluid** material and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/applications/55_radiation_analysis_lab/2d_radiation_analysis_lab/image0020.jpg' | relative_url }})

Assigning material for External Body

### Defining Boundary condition for External Body 

Delete the default assigned Heat exchange with Environment BCC over the entire outer surface. Then assign the Temperature BCC on Top and Bottom side of External body and assign 38°C as Temperature as shown in Fig. 2DRAL1.21. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Step page.

![]({{ '/assets/images/applications/55_radiation_analysis_lab/2d_radiation_analysis_lab/image0021.jpg' | relative_url }})

Assigned Temperature BCC for External Body

### Assigning Step definition

In Step window, select process condition tab and check **View****factor** calculation check box. Select **Simulation Steps** ![]({{ '/assets/icons/pre_icons/mo_simulation_step.jpg' | relative_url }}) tab and define **Number****of****Simulation****steps** as **6000** and **Step** **increment****to** **save** as **5 sec** (see Fig. 2DRAL1.22.).

![]({{ '/assets/images/applications/55_radiation_analysis_lab/2d_radiation_analysis_lab/image0022.jpg' | relative_url }})

Simulation Steps page

Under **Step increment![]({{ '/assets/icons/pre_icons/mo_step_increment.jpg' | relative_url }}) **tab, select **Temperature** type Solution step definition, Define **Initial time step** and **Min Time step** as **1e-06** and **Max time step** and **Max****temperature****change** as **5** as shown in Fig. 2DRAL1.23. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/applications/55_radiation_analysis_lab/2d_radiation_analysis_lab/image0023.jpg' | relative_url }})

Step increment controls page

### Generate database

Click the ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) button to have the program check to see if anything was missed in the problem setup. During the checking process: Messages in the red color signify data that needs to be fixed before a simulation can be run (such as when you forget to define any material data). 

Click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database. When the program is done writing the database, click on tab to run simulation.

### Run and monitor a simulation

Once the database has been generated switch to the Simulation mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the operation tree. Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options Use the default **Continue****Run** option to select “**Continue****from the last step** ” (from step -1) option and then select the Simulation mode as **Interactive** radio button.

After completion of simulation observe the last messages in Message file. We will observe the message as "

PROGRAM STOPPED!

THE CURRENT TIME 1200.0000000

THE CURRENT LOCAL TIME 1200.0000000 HAS REACHED THE SPECIFIED LIMIT 1200.0000000 "

## Operation2: Steady state heat transfer operation

In this operation we are setting up steady state heat transfer operation with ambient temperature of 800°C for 30 min.

Now go to ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}) mode add another Heat transfer operation. Then click on second Heat transfer operation to open second Heat transfer operation. When we click on second operation we will get Setup type popup, in popup click on Yes -Interactive setup ![]({{ '/assets/icons/pre_icons/mo_yes_interactive_setup_button.jpg' | relative_url }}) button.

### Heat transfer type selection

In Heat transfer type page, select Transfer through air mode and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Define Process Condition

In Process condition page, define **process****duration** as **1800** sec. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Fin BCC page.

### Defining Fin BCC

Click on Env. window button, select **window1** and define Temperature as **800°C** and **Convective coefficient** as **constant****0.01** as shown in Fig. 2DRAL1.24., click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until External body BCC page.

![]({{ '/assets/images/applications/55_radiation_analysis_lab/2d_radiation_analysis_lab/image0024.jpg' | relative_url }})

Fin Heat Exchange Window BCC page

### Defining External Body BCC page

Change the assigned **Temperature****BCC** value to**800°C** from 38°C as shown in Fig. 2DRAL1.25., click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Generate DB page.

![]({{ '/assets/images/applications/55_radiation_analysis_lab/2d_radiation_analysis_lab/image0025.jpg' | relative_url }})

External Body BCC page

### Generating Database

Click the ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) button to have the program check to see if anything was missed in the problem setup. Click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database. When the program is done writing the database, click on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) tab to run simulation.

### Run and monitor a simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options Use the default **Continue****Run** option to select “**Continue****from the last step** ” option and then select the Simulation mode as **Interactive** radio button. 

## Operation3: Transient state heat transfer operation

In this operation we are setting up transient state heat transfer operation with ambient temperature of 38°C for 60 min.

After completion of simulation go to ![]({{ '/assets/icons/pre_icons/mo_pre_mode_button.jpg' | relative_url }}) mode add another Heat transfer operation. Then click on third Heat transfer operation to open the added Heat transfer operation. When we click on operation we will get Setup type popup, in popup click on Yes -Interactive setup ![]({{ '/assets/icons/pre_icons/mo_yes_interactive_setup_button.jpg' | relative_url }}) button.

### Heat transfer type selection

In Heat transfer type page, select **Transfer through air** mode and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Define Process Condition

In Process condition page, define **process****duration** as **3600** sec. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) Fin BCC page.

### Defining Fin BCC

Click on Env. window button, select window1 and define Temperature as **38°C** and select Convection Coefficient as Function of Temperature, click on Define button and import **Convection_coeffecient_win1.dat** from \2D\LABS\ Radiational_analysis directory. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until External body BCC page.

### Defining External Body BCC page

Change the assigned Temperature BCC value to**38°C**. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Generate DB page.

### Generating Database

Click the ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) button to have the program check to see if anything was missed in the problem setup. Click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database. When the program is done writing the database, click on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) tab to run simulation.

### Run and monitor a simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options Use the default **Continue****Run** option to select “**Continue****from the last step** ” option and then select the Simulation mode as **Interactive** radio button **** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.. After completion of simulation go to ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) tab.

## Post Processing

### State variable ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }})

Plot **Temperature****state****variable** for **F** in object and observe temperature distribution in each operation last step (see Fig. 2DRAL1.26.)

![]({{ '/assets/images/applications/55_radiation_analysis_lab/2d_radiation_analysis_lab/image0026.jpg' | relative_url }})

Temperature distribution in each operation last step

### Point tracking ![]({{ '/assets/icons/post_icons/mo_point_tracking_icon.jpg' | relative_url }})

Select **point tracking** add 3 points as explained below (see Fig. 2DRAL1.27.) and click on ![]({{ '/assets/icons/post_icons/mo_track_button.jpg' | relative_url }}).

Point1: On 3rd fin center top surface.

Point2: In between 2nd and 3rd fin top surface.

Point3: Below point 2 on bottom surface.

Now Plot temperature state variable and observe the Point tracking graph (see Fig. 2DRAL1.28.).

![]({{ '/assets/images/applications/55_radiation_analysis_lab/2d_radiation_analysis_lab/image0027.jpg' | relative_url }})

Point selection for Point tracking

![]({{ '/assets/images/applications/55_radiation_analysis_lab/2d_radiation_analysis_lab/image0028.jpg' | relative_url }})

Point Tracking Graph

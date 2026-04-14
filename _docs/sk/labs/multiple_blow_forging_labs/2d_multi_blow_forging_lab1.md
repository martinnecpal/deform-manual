---
lang: sk
title: "2D Multi Blow Forging Lab1"
---

# 2D Multi Blow Forging Lab1

The intent of the lab is to demonstrate to the user how to prepare a multiple-blow simulation in DEFORM for successive hammer blows using 2D Multi Blow Forging operation with adaptive reheat DEFORM feature. The simulation is performed as a 2D non-isothermal simulation.

1.1. Creating New Problem

1.2. Adding Operation

1.3. Define Process settings

1.4. Defining Blow Table

1.5. Geometry type selection

1.6. Simulation Controls

1.7. Loading Material

1.8. Adding Objects

1.9. Define Workpiece

1.10. Defining Top Die

1.11. Defining Bottom Die

1.12. Positioning

1.13. Contact Generation

1.14. Step controls page

1.15. Generating Database

1.16. Starting the Simulation

1.17. Post-Processing the Results

## Creating New Problem

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear as shown in Fig. 2DMBL1.1.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0001.jpg' | relative_url }})

DEFORM GUI main

Create a new problem either by selecting **File** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in Fig. 2DMBL1.2. Select "**Integrated Manufacturing Process** " radio button and units system as "**English** " using radio button. Define Problem Name as "**2D_MB_Forging** " and make sure the “Show option dialog” check box is turned on (if we do not turn on the “**Show option dialog** ” check box, then we will not get the New Project dialog in MO UI). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Deform Integrated Manufacturing Process.

Multiple operation wizard will open with the New Project dialog, at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session we will use "**2D_MB_Forging** " as the project name. To add first operation as 2D Multi Blow Forging operation check the checkbox as shown in Fig. 2DMBL1.2. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0002.jpg' | relative_url }})

MO wizard new project opening window

## Adding Operation

Multiple Operation wizard will open by adding the 2D Multi Blow Forging operation automatically as shown in Fig. 2DMBL1.3. if user selects to use it as first operation. Operation can also be add by clicking on 2D Multi Blow Forging operation ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button or by drag and drop into the Operation Editor.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0003.jpg' | relative_url }})

Adding multi blow operations

## Define Process settings

Define the process settings as below, (see Fig. 2DMBL1.4.)

  * In Process page, define the **Press****energy** as **240****Klb-in**.

  * Make sure energy specification method is **Ratio to max energy** (%).

  * Turn on the **Use****dwell** check box, Define the **Dwell****time** as **1** sec, Time per step as **0.2** and **Heat****transfer****coefficient** as **0.0003**.

  * Turn on **Reheat****check****box** and define the **reheat****temperature** as **2150°** F.

  * Turn on**Use workpiece rotation** to rotate workpiece between blows and **Initialize****strain on reheat** check boxes to initialize strain to zero upon reheat.

  * Turn on **Use heating Simulation** check box, define the **Heating****time** as **800** sec, Heat **Time****step** as **1****sec** , to simulate heat loss during transfer from dies to furnace and vice versa define **Transfer-in-time** as **3** sec, Transfer-out-time as **3** sec and **Transfer time** **step** as **1** sec.

  * Turn on **Use Adaptive reheat** check box so that system automatically identifies when to start reheat based on the billet temperature at the end of the blow, Define the **upper** **limit** as **2150°** F, **lower limit** as **1750°** F and **Temperature** **to****stop****reheat** as **1950°** F. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Blow table.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0004.jpg' | relative_url }})

Process page

## Defining Blow Table

In Blow table, define the **number****of****hits** as **9** and define the rest of the settings as mentioned in the Fig. 2DMBL1.5. Max energy available for that blow is defined below % Blow and also efficiency of each blow is defined below efficiency. Workpiece is flipped at the end of each blow. ![]({{ '/assets/icons/pre_icons/mo_reheat_check_box.jpg' | relative_url }}) under Reheat indicates adaptive reheat is checked and system will decide when to reheat the workpiece. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0005.jpg' | relative_url }})

Define Blow table settings

## Geometry type selection

Select the Geometry type as **2D Axisymmetric**. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0006.jpg' | relative_url }})

Geometry type selection page

## Simulation Controls

In this lab as we are setting up simple non Isothermal problem, in Simulation controls keep both the **Heat****transfer** and **Deformation** modes turn on (see Fig. 2DMBL1.7.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0007.jpg' | relative_url }})

Simulation controls page

## Loading material 

Load the material '**AISI-4340[1550-2200F(850-1200C)]** ' from DEFORM Material library, **Steel** category using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load material data from library) option. This can be done as as shown in below by clicking ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}) button as shown in Fig. 2DMBL1.8. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until object page.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0008.jpg' | relative_url }})

Material library window

## Adding Objects

For this operation we require three objects, hence in Object window keep three objects which are added by default, else add 3 objects using ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) option (see Fig. 2DMBL1.9.) Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0009.jpg' | relative_url }})

Adding objects window

## Define Workpiece

In workpiece page, define the workpiece temperature as **1950** °F and select object type as **Plastic** as shown in Fig. 2DMBL1.10. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0010.jpg' | relative_url }})

Workpiece page

### Loading Workpiece Geometry

In Geometry window, load **MB_Forging_workpiece.geo** geometry file from library using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load geometry from library) option or can also be imported using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Load geometry from a file) option as shown in Fig. 2DMBL1.11. The geometry for billet is located in DEFORM installation folder \2D\LABS directory. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to mesh page.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0011.jpg' | relative_url }})

Workpiece geometry page

### Generating mesh for Workpiece

Define the **Target number of elements** as **400** and click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). A mesh with approximately 400 elements will be generated as shown in Fig. 2DMBL1.12. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to material page.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0012.jpg' | relative_url }})

Workpiece mesh generation

### Assign Workpiece Material

In Material list window, select the '**AISI-4340[1550-2200F(850-1200C)]** ' from the list as shown in Fig. 2DMBL1.13. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Boundary condition page.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0013.jpg' | relative_url }})

Workpiece material selection

### Workpiece BCC

In BCC page, check the default assigned Deformation BCC for Left side of the workpiece in X-Direction, default BCC are assigned automatically due to selection of problem type as axisymmetric (see Fig. 2DMBL1.14.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top die page.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0014.jpg' | relative_url }})

Workpiece BCC page

## Defining Top Die

In Top die page ( Fig. 2DMBL1.15.) select Object type as **Rigid** and keep the temperature as **300** °F, we will not mesh the dies in this lab as we are not interested in dies temperature. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0015.jpg' | relative_url }})

Top die page

### Top die geometry

In Geometry window, load **MB_Forging_Top_die.geo** geometry file from library using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load geometry from library) option or can also be imported using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Load geometry from a file) option as shown in Fig. 2DMBL1.16. The geometry is located in DEFORM installation folder \2D\LABS directory. Check the geometry using ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) option to make sure the geometry is OK. Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top die movement page.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0016.jpg' | relative_url }})

Top die geometry page

### Top Die movement

User can use Multi blow forging template for both hammer and screw presses. In this lab we will be using **hammer** , hence select **hammer****movement** type and define **energy****as****240****Klb-in** and **Mass** as **0.025****Klb-s^2/in** as shown in Fig. 2DMBL1.17. As it is multiple blow simulation constant blow efficiency values for multiple blows definition is allowed in blow table only. If user using blow efficiency as function of force then efficiency function data is allowed to define in movement window. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Bottom Die page

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0017.jpg' | relative_url }})

Top die movement page

## Defining Bottom Die

In Bottom die page select Object type as **Rigid** and define the **temperature** as **300** °F (see Fig. 2DMBL1.18.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to geometry page

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0018.jpg' | relative_url }})

Bottom Die page

### Bottom die geometry definition

In Geometry window, load **MB_Forging_Bottom_die.geo** geometry file from library using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load geometry from library) option. The geometry is located in DEFORM installation folder \2D\LABS directory. Check the geometry using ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) option to make sure the geometry is OK. Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Positioning page.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0019.jpg' | relative_url }})

Bottom Die geometry definition

## Positioning

In this operation setup we will use **Automatic** **position** option to position the objects. In Positioning page select positioning direction as Z (Y) - direction and click on ![]({{ '/assets/icons/pre_icons/mo_automatic_positioning_button.jpg' | relative_url }}) button, it will position the objects as shown in Fig. 2DMBL1.20. Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Contact page.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0020.jpg' | relative_url }})

Positioning the objects

## Contact Generation

Select **user****type** contact and click on ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) button. It will add the relationship between the Billet, Top Die and Bottom Die as shown in Fig. 2DMBL1.21. As the Dies are Rigid and Billet is plastic, Top and Bottom Dies are considered as Master and Billet as Slave. In order to predict the fold during deformation, self contact will be assigned for Billet.

Define the **shear** **friction** value of **0.2** and **Heat****transfer****coefficient** as **0.004** for **Top die** and **workpiece** relation.

Define the **shear****friction** value of **0.25** and **Heat****transfer****coefficient** as **0.004** for **Bottom die** and **workpiece** relation.

Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to go back to Inter-Object window, use ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) icon to determine a suitable contact tolerance (a value of about 0.00123929" will be calculated) and then click on ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) button to generate contact. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Step page as no Stopping controls are necessary to define for this simulation

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0021.jpg' | relative_url }})

Inter object relations

## Step controls page

In Step controls, define the **Number of steps** as **400** , **step****increment** of **10** and **time****increment** of **0.0001** as shown in Fig. 2DMBL1.22. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) for DB generation page.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0022.jpg' | relative_url }})

Step Controls page

## Generating Database

Once the problem has been completely set up, the last step is to generate a database file. The FEM engine (the part of DEFORM® that calculates the solution) uses a database file to store the finite element solutions for the problem. When you generate a database in the DEFORM MO Pre-processor, all of the information defined in the Pre-processor (such as the material properties, movement controls, object geometries, etc.) is transferred to the database file.

In Generate DB page, we can observe the Operation Simulation setup summary. Click the ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) button to have the program check to see if anything was missed in the problem setup. During the checking process, messages in the red color signify data that needs to be fixed before a simulation can be run (such as when you forget to define any material data).

Click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database. When the program is done writing the database, switch to ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) tab to run simulation.

## Starting the Simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. 2DMBL1.23. Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0023.jpg' | relative_url }})

Run Simulation window

The progress of the simulation can be monitored as it is running by looking at the Simulation Message tab and Simulation Graphics from the Graphics display region in Simulation mode. As long as the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked in Simulation Message tab, which is the default setting, the Message file will refresh automatically.

The Message file provides information about which simulation step the simulation is currently on and also gives information dealing with how well the simulation is running.

When the simulation is finished without any issues, the following message will be added to the end of the Message file:PROGRAM STOPPED!

THE CURRENT TIME 41.8737368

THE CURRENT LOCAL TIME 1.0085369 HAS REACHED THE SPECIFIED LIMIT 1.0085369 (see Fig. 2DMBL1.24.)

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0024.jpg' | relative_url }})

Simulation message tab

## Post-Processing the Results

After simulation has been completed, switch to ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) tab to view results, MO post processor will open.

Play the Animation to go through the flipping of the workpiece (Workpiece rotation)..

Directly by clicking on the State variables icons user can plot the important state variables contour plots as shown in below Fig. 2DMBL1.25. and Fig. 2DMBL1.26.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0025.jpg' | relative_url }})

Stress effective plot

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0026.jpg' | relative_url }})

Strain Effective plot

User can go through the multiple blows and reheat operations by selecting particular step from step browser and playing the steps. From step browser operations order we can observe that adaptive reheat triggered after BL5-DWL operation as the object minimum temperature dropped below the adaptive reheat lower limit temperature 1750°F. Also adaptive heat simulation stopped after the workpiece reached the reheat stopping temperature 1950°F has been reached. (see Fig. 2DMBL1.27.)

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0027.jpg' | relative_url }})

Step browser indicating adaptive reheat simulations

Temperature contour of the workpiece before and after the adaptive reheat as shown in Fig. 2DMBL1.28. Note that before adaptive heating is started, the minimum temperature of the billet is 1740°F (specified limit is 1750°F).

![]({{ '/assets/images/labs/multiple_blow_forging_labs/2d_multi_blow_forging_lab1/image0028.jpg' | relative_url }})

Workpiece temperature contour before and after the adaptive reheat after BL5-DWL

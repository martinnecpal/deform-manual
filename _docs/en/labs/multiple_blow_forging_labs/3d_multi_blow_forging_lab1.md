---
lang: en
title: "3D Multi Blow Forging Lab1"
---

# 3D Multi Blow Forging Lab

The intent of the lab is to demonstrate to the user how to prepare a multiple-blow simulation in DEFORM for three successive hammer blows using 3D Multi Blow Forging operation with adaptive reheat DEFORM feature. The simulation is performed as a 3D non-isothermal simulation.

1.1. Creating a New Problem

1.2. Adding Operation

1.3. Defining Process settings

1.4. Defining Blow Table

1.5. Simulation Controls

1.6. Loading Material from library

1.7. Adding Objects

1.8. Defining Workpiece

1.8.1. Defining Workpiece geometry

1.8.2. Generating mesh for Workpiece

1.8.3. Assign Workpiece Material

1.8.4. Assigning BCC

1.9. Defining Top die

1.9.1. Defining Top die geometry

1.9.2. Defining Top Die movement

1.10. Defining Bottom die

1.10.1. Defining Bottom Die geometry

1.11. Positioning

1.12. Contact Generation

1.13. Step controls

1.14. Generating Database

1.15. Starting the Simulation

1.16. Post processing the results

## Creating a New Problem

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

New Problem popup

Create a new problem either by selecting **File** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in [Fig. 3DMBL1.1.]() Select "**Integrated Manufacturing Process** " radio button and units system as "**English** " using radio button. Define Problem Name as "**3D_MB_Forging** " and make sure the “Show option dialog” check box is turned on (if we do not turn on the “**Show option dialog** ” check box, then we will not get the New Project dialog in MO UI). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Deform Integrated Manufacturing Process.

Multiple operation wizard will open with the New Project dialog, at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session we will use "**3****D_MB_Forging** " as the project name. To add first operation as **3D Multi Blow Forging operation****check** the **checkbox** as shown in Fig. 3DMBL1.2. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0002.jpg' | relative_url }})

MO wizard New Project opening window

User can also change the Unit system and project saving file location (see Fig. 3DMBL1.2.). Using copy Existing project option we can import previous saved projects as new project. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

## Adding Operation

Multiple Operation wizard will open by adding the 3D Multi Blow Forging operation automatically, if user selects to use it as first operation as shown in Fig. 3DMBL1.3. Operation can also be add by clicking on 3D Multi Blow Forging operation ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button or user can also add by drag and drop into the Operation Editor.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0003.jpg' | relative_url }})

Added multiple blow forging operation into operation editor

## Defining Process settings

Define the process settings as below, (see Fig. 3DMBL1.4.)

  * In Process page, define the Press **energy** as **240** Klb-in.

  * Turn on the Use dwell check box, Define the **Dwell****time** as **1** sec, **Time per step** as **0.2** and **Heat transfer coefficient** as **0.0003**.

  * **Turn****on** Use **workpiece****rotation** check box.

  * **Turn****on****Reheat** check box and define the **reheat****temperature** as **2150** F.

  * **Turn****on****Use****heating****Simulation** check box, define the **Heating****time** as **800** sec, **Heat****Time****step** as **1** sec, to simulate heat loss during transfer from dies to furnace and vice versa define **Transfer-in-time** as **3** secs, **Transfer-out-time** as **3** secs and **Transfer time step** as **1** sec.

  * **Turn on Use Adaptive reheat** check box so that system automatically identifies when to start reheat based on the billet temperature at the end of the blow, define the **Upper limit** as **2150** F,**Lower limit** as **1750** F and **Temp to stop reheat** as **1950** F.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0004.jpg' | relative_url }})

Process settings window

## Defining Blow Table

In Blow table, define the **number of hits** as**9** and define the rest of the settings as shown in the Fig. 3DMBL1.5.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0005.jpg' | relative_url }})

Blow table settings window

To define the workpiece rotation settings click on button ![]({{ '/assets/icons/pre_icons/mo_target_volume_icon.jpg' | relative_url }}) next to the undefined parameter status and define the upside down rotation movement for workpiece about its center along Z axis as shown in Fig. 3DMBL1.6. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0006.jpg' | relative_url }})

Rotation parameter defining window

## Simulation Controls

In this lab we will be showing how to setup simple non Isothermal problem. So in Simulation controls keep both the Heat transfer and Deformation modes turned on (see Fig. 3DMBL1.7.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) .

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0007.jpg' | relative_url }})

Simulation control window

## Loading Material from library

Load the material '**AISI-4340[1550-2200F(850-1200C)]** ' from DEFORM Material library, **Steel** category using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load material data from library) option. This can be done as shown in below by clicking ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}) button as shown in Fig. 3DMBL1.8. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Object page.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0008.jpg' | relative_url }})

Material library window

##  Adding Objects

For this operation we required three objects, hence in Object window keep the three objects which are added by default, else add 3 objects as shown in Fig. 3DMBL1.9., click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0009.jpg' | relative_url }})

Adding objects window

## Defining Workpiece

In workpiece home page define the workpiece temperature as **1950** F and select Object type as **Plastic** as shown in Fig. 3DMBL1.10. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0010.jpg' | relative_url }})

Workpiece window

### Defining Workpiece geometry

In Geometry window, load **MB_Forging_workpiece.geo** geometry file from library using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) button. Check geometry using ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) and ![]({{ '/assets/icons/pre_icons/mo_show_geometry_normal_vectors_option.jpg' | relative_url }}) options for invalid polygons and no. of surfaces (see Fig. 3DMBL1.11.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to mesh page.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0011.jpg' | relative_url }})

Defining workpiece Geometry

### Generating mesh for Workpiece

Define the target number of elements as **25000** and click ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). A mesh with approximately 22000 elements will be generated (see Fig. 3DMBL1.12.) Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to material page.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0012.jpg' | relative_url }})

Workpiece mesh generation

### Assign Workpiece Material

In Material list window, select the **AISI-4340[1550-2200F(850-1200C)]** from the list as shown in Fig. 3DMBL1.13. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0013.jpg' | relative_url }})

Workpiece material assigning window

### Assigning BCC

In BCC page, check the default assigned Deformation BCC for the workpiece, default BCC is assigned automatically based on the geometry symmetry type (see Fig. 3DMBL1.14.). The default BCC is fine, click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) unitl Top die page.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0014.jpg' | relative_url }})

Workpiece BCC window

## Defining Top die

In Top die page (see Fig. 3DMBL1.15.) select Object type as **Rigid** and keep the temperature as **300F** as we will not mesh the dies in this lab as we are not interested in dies temperature. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0015.jpg' | relative_url }})

Top die object window

### Defining Top die geometry

In Geometry window, load **MB_Forging_Top_die.geo** geometry file from library using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) button. Check geometry using ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) and ![]({{ '/assets/icons/pre_icons/mo_show_geometry_normal_vectors_option.jpg' | relative_url }}) options for invalid polygons and no. of surface (see Fig. 3DMBL1.16.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until top die movement page.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0016.jpg' | relative_url }})

Top die geometry window

### Defining Top Die movement

User can use Multi blow forging template for both hammer and screw presses. In this lab we will be using hammer, hence select hammer movement type and define energy as 240 Klb-in and Mass **0.025** Klb-s^2/in (see Fig. 3DMBL1.17.). As it is multiple blow simulation constant blow efficiency values for multiple blows definition is allowed in blow table only. If user using blow efficiency as function of force then efficiency function data is allowed to define in movement window. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Bottom Die page.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0017.jpg' | relative_url }})

Top die movement window

## Defining Bottom die

In Bottom die page select Object type as **Rigid** and define the temperature as **300** F, (see Fig. 3DMBL1.18.) click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to geometry page.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0018.jpg' | relative_url }})

Bottom die object window

### Defining Bottom Die geometry

In Geometry window, load **MB_Forging_Bottom_die.geo** geometry file from library using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) button. Check geometry using ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) and ![]({{ '/assets/icons/pre_icons/mo_show_geometry_normal_vectors_option.jpg' | relative_url }}) options for invalid polygons and no. of surface. (See Fig. 3DMBL1.19.) Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until positioning page.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0019.jpg' | relative_url }})

Bottom die geometry window

## Positioning

In this operation setup we will use Automatic position option to position the objects. In positioning page select positioning direction as Z - direction and click on ![]({{ '/assets/icons/pre_icons/mo_automatic_positioning_button.jpg' | relative_url }}) button, it will position the objects as shown in Fig. 3DMBL1.20. Then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Contact page.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0020.jpg' | relative_url }})

Object positioning controls window

## Contact Generation

Select **user** type contact and click on ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) button. It will add the relationship between the Billet, Top Die and Bottom Die as shown in Fig. 3DMBL1.21. As the Dies are Rigid and Billet is plastic, Top and Bottom Dies are considered as Master and Billet as Slave. Define the shear friction value of 0.2 and Heat transfer coefficient as 0.004 for Top die and workpiece relation. Define the shear friction value of 0.25 and Heat transfer coefficient as 0.004 for Bottom die and workpiece relation. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to go back to Inter-Object window, use ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) icon to determine a suitable contact tolerance (a value of about 0.00530" will be calculated) and then click ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) button to generate contact. If you rotate the objects around in graphics window, you will see that contact was generated between the two objects. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Step page as no Stopping controls are necessary to define for this simulation.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0021.jpg' | relative_url }})

Inter-object definition window

## Step controls 

In Step controls, define the **Number of steps** as **400** , **step****increment** of **10** and **time****increment** of **0.0001sec**. ( Fig. 3DMBL1.22.) Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) for DB generation window.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0022.jpg' | relative_url }})

Simulation controls window

##  Generating Database

Once the problem has been completely set up, the last step is to generate a database file. The FEM engine (the part of DEFORM® that calculates the solution) uses a database file to store the finite element solutions for the problem. When you generate a database in the DEFORM Integrated Manufacturing Proc., all of the information defined in the Pre-processor (such as the material properties, movement controls, object geometries, etc.) is transferred to the database file.

In Generate DB window, click the ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) button to have the program check to see if anything was missed in the problem setup. During the checking process, messages in the red color signify data that needs to be fixed before a simulation can be run (such as when you forget to define any material data).

Click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database. When the program is done writing the database, switch to ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) tab to run simulation.

## Starting the Simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. 3DMBL1.23. Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0023.jpg' | relative_url }})

Run Simulation window

The progress of the simulation can be monitored as it is running by looking at the Simulation Message tab and Simulation Graphics from the Graphics display region in Simulation mode. As long as the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked in Simulation Message tab, which is the default setting, the Message file will refresh automatically.

The Message file provides information about which simulation step the simulation is currently on and also gives information dealing with how well the simulation is running.

When the simulation is finished without any issues, the following message will be added to the end of the Message file:"NORMAL STOP: Simulation is completed and stopped at the user specified time step". (See Fig. 3DMBL1.24.)

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0024.jpg' | relative_url }})

Simulation message tab

## Post processing the results

After simulation has been completed, switch to ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) tab to view results, MO post processor will open.

Play the Animation to go through the rotation of the workpiece (Workpiece rotation).

Directly by clicking on the State variables icons user can plot the important state variables contour plots as shown in below Fig. 3DMBL1.25\. and Fig. 3DMBL1.26.

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0025.jpg' | relative_url }})

Effective Stress State variable plot

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0026.jpg' | relative_url }})

Effective Strain State variable plot

User can go through the multiple blows and reheat operations by selecting particular step from step browser and playing the steps. In step browser operations order we can observe that adaptive reheat triggered only after BL5-DWL operation onwards as the object minimum temperature dropped below the adaptive reheat lower limit temperature 1750F. Also adaptive heat simulation stopped after the workpiece reached the reheat stopping temperature 1950F has been reached. (See Fig. 3DMBL1.27.)

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0027.jpg' | relative_url }})

Step browser indicating adaptive reheat simulations

Temperature contour of the workpiece before and after the adaptive reheat as shown in blow Fig. 3DMBL1.28\. Note that before adaptive heating is started, the minimum temperature of the billet is 1748.845F (specified limit is 1750F).

![]({{ '/assets/images/labs/multiple_blow_forging_labs/3d_multi_blow_forging_lab1/image0028.jpg' | relative_url }})

Workpiece temperature contour before and after the adaptive reheat after BL3-DWL

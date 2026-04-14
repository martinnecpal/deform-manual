---
lang: sk
title: "Tee Non Isothermal Forging Lab"
---

# Tee Non isothermal Forging Lab

In this lab we will setup simple Tee Non isothermal operation where both Workpiece and Dies are having mesh.

1.1. Creating a New Problem

1.2. Adding 3D Forming Express operation - Tee Forging

1.3. Process

1.4. Thermal Calculation

1.5. Number of Object selection

1.6. Workpiece

1.7. Top Die

1.8. Bottom Die

1.9. Object Positioning

1.10. Contact page

1.11. Primary Die stroke

1.12. Stopping controls

1.13. Simulation controls

1.14. Generate DB

1.15. Running simulation

1.16. Postprocessing

## Creating a New Problem

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear, as shown in Fig. 3DTEEL1.1.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0001.jpg' | relative_url }})

DEFORM GUI Main window

Create a new problem either by selecting **File** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in Fig. 3DTEEL1.2. Select "**Integrated Manufacturing Process** " radio button and unit system as "**English** " radio button in unit field. Define Problem Name as " **TeeNonIso** " and make sure the “Show option dialog” check box is turned on (if we do not turn on the “**Show option dialog** ” check box, then we will not get the New Project dialog in MO UI). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

Problem type selection window

Integrated Manufacturing Process will open (see Fig. 3DTEEL1.3.), at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session we will use "************TeeNonIso**** " as the project name. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0003.jpg' | relative_url }})

Problem location selection window

## Adding 3D Forming Express operation - Tee Forging

Once you click on Finish button, a Multiple Operation wizard will open to setup the problem. Add 3**D Forming Express** operation from Operations list in Explorer. Operation can be added by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button next to 3D Forming express operation or user can also add by drag and drop into the Operation Editor.

**Changing operation name**

Change the Operation name to "**Tee_Forging** " by double click on Forming field in Operation editor as shown in Fig. 3DTEEL1.4.

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0004.jpg' | relative_url }})

Editing Operation Name

## Process

In **Process** page, select Process type as Hot Forging by selecting **Hot Forging** radio button. For this lab, we will simulate the whole part, by default Whole part will be selected if not select Geometry type as Whole part. The shape complexity and simulation accuracy slider bars influence the mesh settings and number of time steps used in the simulation. This in turn, influences the run time and level of details available in the simulation. For this simulation, set Object shape complexity as **Moderate** and Accuracy as **Fast** , as shown in Fig. 3DTEEL1.5. Then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0005.jpg' | relative_url }})

Process page

## Thermal Calculation

In this operation, We will calculate temperature change in the workpiece and dies, so select **Calculate****Temperature****in****Workpiece****and****Dies** radio button (see Fig. 3DTEEL1.6.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0006.jpg' | relative_url }})

Thermal Calculation page

## Number of Object selection

In this lab we will use**1 workpiece and 2 dies** , use default selection as shown in Fig. 3DTEEL1.7. and Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0007.jpg' | relative_url }})

Number of Objects selection page

## Workpiece

The workpiece will have an initial temperature of 2250F, change the Workpiece **Temperature** to **2150** °F. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). (See Fig. 3DTEEL1.8.)

**Note** : there is an ![]({{ '/assets/icons/pre_icons/mo_import_object.._button.jpg' | relative_url }}) button on the “object” page. This is for importing complete object data from another object data file.

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0008.jpg' | relative_url }})

Object page

### Import Workpiece Geometry

Click on Load Geometry from Library ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) button in Geometry page and import **TeeBillet.stl** file.

Check the Geometry by clicking on ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) action label. The “Geometry Checking Result” window contains a description of what constitutes a legal geometry as shown in Fig. 3DTEEL1.9. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0009.jpg' | relative_url }})

Check geometry page

### Generating Mesh for Workpiece

Reduce the number of mesh elements on the workpiece to about 14,000. We will do this to get fast run times during training. Select the **User****defined** type radio button and change the **T******ar** get number of Elements** to **14000** as shown in**** Fig. 3DTEEL1.10. and generate Mesh. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0010.jpg' | relative_url }})

Workpiece mesh page

### Assign Material for Workpiece

In Material window, load the material **AISI-316[70-2020F(20-1100C)]** from DEFORM Material library, from **Stainless_steel** category using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load material data from library) option. This can be done as shown in Fig. 3DTEEL1.11. by clicking ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}) button. Material can also be loaded from Materials list in Explorer. Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0011.jpg' | relative_url }})

Material window

### Workpiece Boundary Condition

In Boundary condition page, check the default assigned Heat exchange with Environment BCC for Workpiece, it should be assigned for whole surface of object as shown in Fig. 3DTEEL1.12., if it is not assigned by default assign manually. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0012.jpg' | relative_url }})

Heat Exchange with environment Boundary condition

## Top Die

In top die page, initialize Temperature of Top die to **300** °F, click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Import Top die geometry

Click on Load Geometry from Library ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) button, import **TeeTop.stl** file. Then check the geometry using ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) option. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Generate Mesh for Top die geometry

Generate mesh for the Top Die using system type mesh settings value by click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) option as shown in Fig. 3DTEEL1.13. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0013.jpg' | relative_url }})

Top die mesh page

### Assign Top die material

Import **AISI-H-13** material from material library and assign to top die as shown in Fig. 3DTEEL1.14. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

**Note** :This mesh is only used for temperature calculations. The geometry is still used for the deformation part of the calculations.

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0014.jpg' | relative_url }})

Top die Material page

### Assign heat Exchange with Environment Boundary condition

In Boundary condition page, check the default assigned Heat exchange with Environment BCC for Top Die, it should be assigned for whole surface of object as shown in Fig. 3DTEEL1.15., if it is not assigned by default assign manually. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0015.jpg' | relative_url }})

Assigned Heat Exchange with Environment BCC for Top die

### Assign Movement for Top die

Under the movement options, select speed option. Be sure movement is in the **–Z** direction and enter a **speed** of **10** in/sec as shown in Fig. 3DTEEL1.16. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0016.jpg' | relative_url }})

Top die movement page

## Bottom Die

In Bottom die page, initialize Temperature of Bottom die to **300** °F, Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Import Bottom Die

Click on Load Geometry from Library ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) button, import **TeeBottom.stl** file. Then check the geometry using ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) option. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Generate mesh

Generate mesh for the system type mesh settings value by click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) option. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to material page.

### Assign Bottom die material

Select the **AISI-H-13** material from Material list to assign it to Bottom Die. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

### Assign Heat Exchange with Environment BCC

In Boundary condition page, check the default assigned Heat exchange with Environment BCC for Bottom Die, it should be assigned for whole surface of object as shown in Fig. 3DTEEL1.17., if it is not assigned by default assign manually. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0017.jpg' | relative_url }})

Assigned Heat Exchange with Environment BCC for Bottom die

## Object Positioning

Click on ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) option object positioning will open, use the mouse to position the billet over the die cavity using both translation and rotation. Then use drop positioning to allow the billet to settle into the die cavity (see Fig. 3DTEEL1.18.), then use interference position to Top die on the Workpiece. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0018.jpg' | relative_url }})

Object positioning page

## Contact page

Select **User****defined** \- “**Hot****forging (lubricated)** ” for friction condition. Click ![]({{ '/assets/icons/pre_icons/mo_generate_contact_nodes_label.jpg' | relative_url }}). DEFORM will automatically mark the nodes that are initially in contact with the die. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

## Primary Die stroke

We will forge to a flash thickness of 0.250”. Measure the current distance between the top and bottom die (see Fig. 3DTEEL1.19.), subtract 0.250, and use this as an estimated primary die stroke.

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0019.jpg' | relative_url }})

Primary Die Stroke page

## Stopping controls

We want to stop when the dies are 0.25 in apart. Check **Distance between objects** check box, Enter a value of **0.25** in. Select a point on the bottom surface of the top die and a second point on the top surface of the bottom die as shown in Fig. 3DTEEL1.20. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0020.jpg' | relative_url }})

Stopping controls page

## Simulation controls

Accept he Default simulation controls as shown in Fig. 3DTEEL1.21., click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0021.jpg' | relative_url }})

Simulation controls page

## Generate DB

In Generate DB page. Click the ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) button to have the program check to see if anything was missed in the problem setup. During the checking process,

Messages in the red color signify data that needs to be fixed before a simulation can be run (such as when you forget to define any material data).

Click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }})button to generate the database. When the program is done writing the database, click on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) tab to run simulation.

## Running simulation

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. 3DTEEL1.22. Use the default **Continue Run** option to select “**Continue from the last step** ” (from step -1) option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation. As we click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button simulation starts.

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0022.jpg' | relative_url }})

Run Simulation window

The progress of the simulation can be monitored as it is running by looking at the Simulation Message tab and Simulation Graphics from the Graphics display region in Simulation mode. As long as the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked in Simulation Message tab, which is the default setting, the Message file will refresh automatically.

The Message file provides information about which simulation step the simulation is currently on and also gives information dealing with how well the simulation is running.

When the simulation is finished without any issues, check the messages in Message file, when operation completes we will see messages as, "THE DISTANCE BETWEEN TWO OBJECTS ( 2 3): 0.25000000 HAS REACHED THE SPECIFIED LIMIT 0.25000000 "

## Post processing

After completion of Simulation, switch to ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) mode for post processing. Click on ![]({{ '/assets/icons/pre_icons/mo_all_button.jpg' | relative_url }}) button in Step Browser to see all saved steps as shown in Fig. 3DTEEL1.23.

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0023.jpg' | relative_url }})

Post mode

Make the dies transparent turn on the ![]({{ '/assets/icons/pre_icons/mo_show_cotact_icon.jpg' | relative_url }}) display contact nodes, play through the simulation and observe the fill pattern as shown in Fig. 3DTEEL1.24.

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0024.jpg' | relative_url }})

Post mode showing objects in transparency mode

**State variable** :

Plot the Temperature and strain variable for Workpiece and observe the plots as shown in Fig. 3DTEEL1.25. and Fig. 3DTEEL1.26.

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0025.jpg' | relative_url }})

Temperature state variable plot

![]({{ '/assets/images/labs/forming_express_labs/3d_tee_non_isothermal_forging_lab/image0026.jpg' | relative_url }})

Strain Effective variable plot

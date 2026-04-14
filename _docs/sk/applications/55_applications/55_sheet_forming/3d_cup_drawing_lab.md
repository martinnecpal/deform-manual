---
lang: sk
title: "3D Cup Drawing Lab"
---

# 3D Cup Drawing Lab

In this Lab we will be setting up 3D Cup Drawing 

[1.1. Creating a New Problem](3d_cup_drawing_lab.htm#1_1_Creating_a_New_Problem)

[1.2. Simulation controls](3d_cup_drawing_lab.htm#1_2_Simulation_controls)

[1.3. Pressure Pad](3d_cup_drawing_lab.htm#1_3_Pressure_Pad)

[1.4. Object](3d_cup_drawing_lab.htm#1_4_Object)

[1.4.1. Workpiece](3d_cup_drawing_lab.htm#1_4_1_Workpiece)

[1.4.2. Punch](3d_cup_drawing_lab.htm#1_4_2_Punch)

[1.4.3. Die](3d_cup_drawing_lab.htm#1_4_3_Die)

[1.4.4. Pressure Pad](3d_cup_drawing_lab.htm#1_4_4_Pressure_Pad)

[1.5. Scheduled Positioning](3d_cup_drawing_lab.htm#1_4_Scheduled_Positioning)

[1.6. Contact](3d_cup_drawing_lab.htm#1_6_Contact)

[1.7. Stopping Controls](3d_cup_drawing_lab.htm#1_7_Stopping_Controls)

[1.8. Step controls Definition](3d_cup_drawing_lab.htm#1_8_Step_controls_Definition)

[1.9. Generate Database](3d_cup_drawing_lab.htm#1_9_Generate_Database)

[1.10. Running Simulation](3d_cup_drawing_lab.htm#1_10_Running_Simulation)

## Creating a New Problem

On a Windows machine, go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select DEFORM GUI Main v1x.x. from the menu. The **DEFORM GUI Main** window will appear as shown in [Fig. 3DCDL1.1.](3d_cup_drawing_lab.htm#Fig_3DCDL1_1_DEFORM_GUI_Main)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0001.jpg' | relative_url }})

DEFORM GUI Main

Create a new problem either by selecting **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in [Fig. 3DCDL1.2.](3d_cup_drawing_lab.htm#Fig_3DCDL1_2_New_Problem_page) Select " **I****ntegrated Manufacturing Process** " radio button and units system as "**English** " radio button in units field. Define Problem Name as "******3DCup******" and make sure the “**Show option dialog** ” check box is turned on (if we do not turn on the “Show option dialog” check box, then we will not get the New Project dialog). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

New Problem page

Multiple operation wizard will open with the New Project dialog, at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session we will use ‘**3DCup** ’ as the project name. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.  
  
Add 3D Forming operation from the Explorer Operations list. Add the operation by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button available next to 3D Forming or user can also add the operation by drag and drop into the Operation Editor (see [Fig. 3DCDL1.3.](3d_cup_drawing_lab.htm#Fig_3DCDL1_3_Opened_3D_Forming_operation)). 

![]({{ '/assets/images/applications/55_3_sheet_forming/3d_cup_drawing_lab/3d_cpdwl1_image002.jpg' | relative_url }})

GUI after adding 3D Forming operation

## Simulation controls

In this operation, we will be setting up simple Isothermal operation hence in Simulation control page Sim Mode tab, turn off the Heat transfer mode check box (see [Fig. 3DCDL1.4.](3d_cup_drawing_lab.htm#Fig_3DCDL1_4_Simulation_control_page)). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button. 

![]({{ '/assets/images/applications/55_3_sheet_forming/3d_cup_drawing_lab/3d_cpdwl1_image003.jpg' | relative_url }})

Simulation control page

## Material list

In Material page, import the material “**steel_cold_70F_20C__e.key** ” from DEFORM installation folder “\2D\Labs\CupDrawing\” directory. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button. 

### **Defining Anisotropy yield model:**

In 3D models, planar anisotropic behaviour can be captured by setting the yield criteria to “**Hill’s quadratic (R value**)” (see [Fig. 3DCDL1.5.](3d_cup_drawing_lab.htm#Fig_3DCDL1_5_Steel,_COLD_\[70F\(20C\)\]_page)) and then defining R0, R45 and R90 parameters. Changing the default values to those shown below will result in earring. To change the values, click on Hill’s quadratic (R value) and define values for R0, R45 and R90 as shown in [Fig. 3DCDL1.6.](3d_cup_drawing_lab.htm#Fig_3DCDL1_6_Hill’s_quadratic_\(R_value\)_page) The R0, R45 and R90 are aligned to X, XY and Y directions in global space by default. 

![]({{ '/assets/images/applications/55_3_sheet_forming/3d_cup_drawing_lab/3d_cpdwl1_image004.jpg' | relative_url }})

Steel, COLD [70F(20C)] page

![]({{ '/assets/images/applications/55_3_sheet_forming/3d_cup_drawing_lab/3d_cpdwl1_image005.jpg' | relative_url }})

Hill’s quadratic (R value) page

## Object

In object page, click on ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) button and add 4 objects in list as shown in [Fig. 3DCDL1.7.](3d_cup_drawing_lab.htm#Fig_3DCDL1__7_Object_page) Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button.

![]({{ '/assets/images/applications/55_3_sheet_forming/3d_cup_drawing_lab/3d_cpdwl1_image006.jpg' | relative_url }})

Object page

### Workpiece

In the Workpiece page, keep the object name as **Workpiece** and object temperature as 68F. Select object type as **Elasto-plastic** (see [Fig. 3DCDL1.8.](3d_cup_drawing_lab.htm#Fig_3DCDL1_8_Workpiece_page)). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Geometry page.

![]({{ '/assets/images/applications/55_3_sheet_forming/3d_cup_drawing_lab/3d_cpdwl1_image007.jpg' | relative_url }})

Workpiece page

#### Create a Workpiece geometry

We will generate workpiece geometry using geometry primitives. Click on ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) label in geometry page and select “**Cylinder** ” from “**Geometry Primitive** ” window. Define the cylinder **Radius (R) as 2.95276** , **Height (H) as 0.118****11,** **Start angle as 90** with **Revolve angle 45** and **Sections as 45** (see [Fig. 3DCDL1.9.](3d_cup_drawing_lab.htm#Fig_3DCDL1_9_Defining_the_Workpiece_geometry)) to create a 45 degree sheet metal blank. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to Close the Geometry Primitive window. 

![]({{ '/assets/images/applications/55_3_sheet_forming/3d_cup_drawing_lab/3d_cpdwl1_image008.jpg' | relative_url }})

Defining the Workpiece geometry

#### Define Planar Symmetry

Since the object is symmetry, we will be defining planar symmetry to the sheet metal blank. Click on ![]({{ '/assets/icons/pre_icons/mo_symmetry_planes_label.jpg' | relative_url }}) label. Select Planar Symmetry and select cut surfaces of the blank as shown in [Fig. 3DCDL1.10.](3d_cup_drawing_lab.htm#Fig_3DCDL1_10_Defining_the_Workpiece_Symmetry) Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button to close the "Symmetry Planes **"** window.

![]({{ '/assets/images/applications/55_3_sheet_forming/3d_cup_drawing_lab/3d_cpdwl1_image009.jpg' | relative_url }})

Defining the Workpiece Symmetry

#### Setup Brick Mesh

Click on ![]({{ '/assets/icons/pre_icons/mo_setup_brick_mesh_label.jpg' | relative_url }}) label from Geometry page. Select Extrude as brick mesh type and then define extrusion “**Start********Surface** ” (bottom face) and click on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}), select extrusion “**End Surface** ” (top face) and click on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}), see [Fig. 3DCDL1.11.](3d_cup_drawing_lab.htm#Fig_3DCDL1_11_Setup_Brick_Mesh) This is necessary for extruded brick mesh generation. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button to close "Setup Brick Mesh" window. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button until Mesh page.

![]({{ '/assets/images/applications/55_3_sheet_forming/3d_cup_drawing_lab/3d_cpdwl1_image010.jpg' | relative_url }})

Setup Brick Mesh

#### Generating Mesh

We will have 3 layers in thickness direction hence in Mesh page, select **Brick mesh** and define **uniform thickness # of layers** as **3** , see [Fig. 3DCDL1.12.](3d_cup_drawing_lab.htm#Fig_3DCDL1_12_Brick_mesh_settings_for_Workpiece) For 2D cross-section mesh, define **number of elements** as **1000** , set **thickness elements** to **1** and **Size ratio** as **1** , see [Fig. 3DCDL1.13.](3d_cup_drawing_lab.htm#Fig_3DCDL1_13_2D_cross_section_mesh_settings_for_Workpiece) Go to “**Advanced settings** ” and reduce the node addition **Distance tolerance** to **1e-05** ,(see [Fig. 3DCDL1.14.](3d_cup_drawing_lab.htm#Fig_3DCDL1_14_2D_mesh_Advanced_settings_for_Workpiece_and_Generated_3D_Mesh)). Click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button and click ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}) in "Default Boundary Conditions" popup. The Mesh should like a shown in [Fig. 3DCDL1.14.](3d_cup_drawing_lab.htm#Fig_3DCDL1_14_2D_mesh_Advanced_settings_for_Workpiece_and_Generated_3D_Mesh) Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button to Material page.

![]({{ '/assets/images/applications/55_3_sheet_forming/3d_cup_drawing_lab/3d_cpdwl1_image011.jpg' | relative_url }})

Brick mesh settings for Workpiece

![]({{ '/assets/images/applications/55_3_sheet_forming/3d_cup_drawing_lab/3d_cpdwl1_image012.jpg' | relative_url }})

2D cross section mesh settings for Workpiece

![]({{ '/assets/images/applications/55_3_sheet_forming/3d_cup_drawing_lab/3d_cpdwl1_image013.jpg' | relative_url }})

2D mesh Advanced settings for Workpiece and Generated 3D Mesh

####  Assign Material

Select the "**Steel,COLD[70F(20C)]** " material in material list which is already available for Workpiece. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button to BCC.

#### Boundary Conditions

Verify symmetry planes defined on the cut faces in Boundary Conditions page, symmetry BCC (see [Fig. 3DCDL1.15.](3d_cup_drawing_lab.htm#Fig_3DCDL1_14_2D_mesh_Advanced_settings_for_Workpiece_and_Generated_3D_Mesh)) are assigned by default during mesh generation as symmetry planes were defined in Geometry page. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button until top die.

![]({{ '/assets/images/applications/55_3_sheet_forming/3d_cup_drawing_lab/3d_cpdwl1_image014.jpg' | relative_url }})

Symmetry Plane

### Punch

In the Top die object page, change the object name to **Punch** and make sure object type is **Rigid**(see [Fig. 3DCDL1.16.](3d_cup_drawing_lab.htm#Fig_3DCDL1_16_Punch_page)). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button to Geometry page.

![]({{ '/assets/images/applications/55_3_sheet_forming/3d_cup_drawing_lab/3d_cpdwl1_image015.jpg' | relative_url }})

Punch page

#### Importing Punch Geometry

In Punch’s Geometry page, click on ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) label and select “**Revolve** ” ![]({{ '/assets/icons/pre_icons/mo_revolve_3d_geometry_primitive.jpg' | relative_url }}) from “Define Primitive” window, import Geometry **cup_draw-op1-punch-english.dxf** from DEFORM installation folder “\2D\Labs\CupDrawing\” directory using "Load Cross section" option. Set the revolve angle to 360 degrees about the Z axis with 120 sections as shown in [Fig. 3DCDL1.17.](3d_cup_drawing_lab.htm#Fig_3DCDL_1_17_Punch_Geometry) The Punch geometry should look like as shown in [Fig. 3DCDL1.17.](3d_cup_drawing_lab.htm#Fig_3DCDL_1_17_Punch_Geometry) Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button to close the primitive window. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button until Movement Page.

![]({{ '/assets/images/applications/55_3_sheet_forming/3d_cup_drawing_lab/3d_cpdwl1_image016.jpg' | relative_url }})

Punch Geometry

#### Assign Movement for Punch

Select “**Speed** ” under the movement options. Be sure movement is in the “**-Z”** direction. Enter a speed of **10** in/sec as shown in[ Fig. 3DCDL1.18.](3d_cup_drawing_lab.htm#Fig_3DCDL1_18_Punch_Movement_page) Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button until Property page.

![]({{ '/assets/images/applications/55_3_sheet_forming/3d_cup_drawing_lab/3d_cpdwl1_image017.jpg' | relative_url }})

Punch Movement page

#### Reference point on Punch 

In property page, select “**Reference** ” tab and enter “**0** ” for X, Y and Z coordinates as shown in [Fig. 3DCDL1.19.](3d_cup_drawing_lab.htm#Fig_3DCDL_1_19_Punch_Property_page) Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button until Bottom Die page.

![]({{ '/assets/images/applications/55_3_sheet_forming/3d_cup_drawing_lab/3d_cpdwl1_image018.jpg' | relative_url }})

Reference point on Punch 

### Die

In the Bottom die object page, change the object name to**Die** and make sure object type is **Rigid**(see [Fig. 3DCDL1.20.](3d_cup_drawing_lab.htm#Fig_3DCDL1_20_Die_page)). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button to Geometry page.

![]({{ '/assets/images/applications/55_3_sheet_forming/3d_cup_drawing_lab/3d_cpdwl1_image019.jpg' | relative_url }})

Die page

#### Importing Die Geometry

In Die’s Geometry page, click on ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) label and select “**Revolve** ” ![]({{ '/assets/icons/pre_icons/mo_revolve_3d_geometry_primitive.jpg' | relative_url }}) from “Define Primitive” window, import **cup_draw-op1-die-english.dxf** from “\2D\Labs\CupDrawing\” folder. Set the **revolve angle** to **360** degrees about the **Z** axis with **120** **sections** as shown in [Fig. 3DCDL1.21.](3d_cup_drawing_lab.htm#Fig_3DCDL1_21_Die_Geometry) The Die geometry should look like as shown in [Fig. 3DCDL1.21.](3d_cup_drawing_lab.htm#Fig_3DCDL1_21_Die_Geometry) Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button to close the primitive window. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button until Property page.

![]({{ '/assets/images/applications/55_3_sheet_forming/3d_cup_drawing_lab/3d_cpdwl1_image020.jpg' | relative_url }})

Die Geometry

#### Reference point on Die

In Die’s property page, select “**Reference** ” tab and enter the values**5** , **5** and **-4** to X, Y and Z coordinates respectively (see [Fig. 3DCDL1.22.](3d_cup_drawing_lab.htm#Fig_3DCDL1_22_Die_property_page)). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button until Object4 object page.

![]({{ '/assets/images/applications/55_3_sheet_forming/3d_cup_drawing_lab/3d_cpdwl1_image021.jpg' | relative_url }})

Reference point on Die

### Pressure Pad

In the Object4 object page, change the object name to **Pressure Pad** and make sure object type is **Rigid**(see [Fig. 3DCDL1.23.](3d_cup_drawing_lab.htm#Fig_3DCDL1_23_Pressure_Pad_page)). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button to Geometry page.

![]({{ '/assets/images/applications/55_3_sheet_forming/3d_cup_drawing_lab/3d_cpdwl1_image022.jpg' | relative_url }})

Pressure Pad page

#### Importing Pressure Pad Geometry

In Pressure Pad’s Geometry page, click on ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) label and select “**Revolve** ” ![]({{ '/assets/icons/pre_icons/mo_revolve_3d_geometry_primitive.jpg' | relative_url }}) from “Define Primitive” window, import **cup_draw-op1-pressure_pad-english.dxf** from “\2D\Labs\CupDrawing\” folder. Set the **revolve****angle** to **360** degrees about the **Z** axis with **120****sections** as shown in [Fig. 3DCDL1.24.](3d_cup_drawing_lab.htm#Fig_3DCDL1_24_Pressure_Pad_Geometry) The Pressure Pad geometry should look like as shown in [Fig. 3DCDL1.24.](3d_cup_drawing_lab.htm#Fig_3DCDL1_24_Pressure_Pad_Geometry)Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button to close the primitive window. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button until Movement page.

![]({{ '/assets/images/applications/55_3_sheet_forming/3d_cup_drawing_lab/3d_cpdwl1_image023.jpg' | relative_url }})

Pressure Pad Geometry

#### Assign Movement for Pressure Pad

In Movement page, select movement type as “**Sliding die** ”. The preload exerted on Pressure Pad is 8 klb, since we are modelling 1/8th symmetry we will define **preload** as **1klb**. Set **Maximum displacement** as **2 in** and movement direction as **+Z****direction** which is a spring compression direction, see [Fig. 3DCDL1.25.](3d_cup_drawing_lab.htm#Fig_3DCDL1_25_Pressure_Pad_Movement_page) Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button until Controls page.

![]({{ '/assets/images/applications/55_3_sheet_forming/3d_cup_drawing_lab/3d_cpdwl1_image024.jpg' | relative_url }})

Pressure Pad Movement settings

## Scheduled Positioning 

Add first schedule position as **interference positioning** of the **punch** to the **workpiece** in the **–Z** direction with **interference tolerance** of **1e-06**. Add second scheduled positioning as **interference positioning** of the **pressure pad** to the **workpiece** in the **–Z** direction with **interference tolerance** of **1e-06** , turn on the “**Update****sliding die current displacement** ” and “**Update****current stroke** ” check boxes. After completing the definition, the scheduled positioning page looks like as shown in [Fig. 3DCDL1.26.](3d_cup_drawing_lab.htm#Fig_3DCDL1_26_Schedule_Positioning_page_after_completion_of_positioning_definition) Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button until Contact page.

![]({{ '/assets/images/applications/55_3_sheet_forming/3d_cup_drawing_lab/3d_cpdwl1_image025.jpg' | relative_url }})

Schedule Positioning page after completion of positioning definition

## Contact

In Contact page, click on ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) to automatically define all relevant contact pairs. Click on ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) for one of the pairs and select **hybrid friction** with **coulomb friction** as **0.05** and **shear friction** as **0.12** as shown in [Fig. 3DCDL1.27.](3d_cup_drawing_lab.htm#Fig_3DCDL1_27_Hybrid_Friction_model_definition) Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button to close the “Inter-Object Data Definition” window. In “Contact” page click on ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) to apply same conditions to all contact pairs. Click on ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) button to calculate default contact tolerance value and Generate contact by clicking on ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) button. Set the **scheduled contact tolerance** to **0.00001** as shown in [Fig. 3DCDL1.28.](3d_cup_drawing_lab.htm#Fig_3DCDL1_28_Contact_page) Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button until Stopping controls page.

![]({{ '/assets/images/applications/55_3_sheet_forming/3d_cup_drawing_lab/3d_cpdwl1_image026.jpg' | relative_url }})

Hybrid Friction model definition

![]({{ '/assets/images/applications/55_3_sheet_forming/3d_cup_drawing_lab/3d_cpdwl1_image027.jpg' | relative_url }})

Contact page

## Stopping Controls

In Stopping Controls page, define a die distance stopping control based on the reference points of the punch and die. Select the **Punch** object for “**Reference 1”** and the **Die** object as “**Reference 2** ”. “**Method** ” should be set to “**Z Distance** ”. Define the stopping distance as **1.375** ” as shown in [Fig. 3DCDL1.29.](3d_cup_drawing_lab.htm#Fig_3DCDL1_29_Stopping_Control_definition)

![]({{ '/assets/images/applications/55_3_sheet_forming/3d_cup_drawing_lab/3d_cpdwl1_image028.jpg' | relative_url }})

Stopping Control definition

## Step controls Definition

In “Step” page under “**Simulation steps** ” ![]({{ '/assets/icons/pre_icons/mo_simulation_step.jpg' | relative_url }})tab, define **number of steps** as **1000** and **step increment to save** as **20**. In “**Step increment** ” ![]({{ '/assets/icons/pre_icons/mo_step_increment.jpg' | relative_url }}) tab, select step definition type as “**die displacement** ” and set the step size to **0.005** in/step. Edit “**Max polygon length** ” to “**0** ” as shown in [Fig. 3DCDL1.30.](3d_cup_drawing_lab.htm#Fig_3DCDL1_30_Step_increment_page)

![]({{ '/assets/images/applications/55_3_sheet_forming/3d_cup_drawing_lab/3d_cpdwl1_image029.jpg' | relative_url }})

Step increment page

  
Select “**Solver settings** ” ![]({{ '/assets/icons/pre_icons/mo_solver_settings.jpg' | relative_url }}) tab, select solver as “**MUMPS** ” and iteration method as “**Newton-Raphson** ”. Set the “**Force error** ” tolerance to **0.005** from Advanced tab in Solver Setting as shown in [Fig. 3DCDL1.31](3d_cup_drawing_lab.htm#Fig_3DCDL1_31_Solver_settings). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button.

![]({{ '/assets/images/applications/55_3_sheet_forming/3d_cup_drawing_lab/3d_cpdwl1_image030.jpg' | relative_url }})

Solver settings

## Generate Database

When we visit Generate DB page, "Apply Scheduled positioning" popup appears since we defined scheduled positioning data. Click on ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}) button in popup to apply scheduled positioning.

The completed setup looks like as shown in [Fig. 3DCDL1.32.](3d_cup_drawing_lab.htm#Fig_3DCDL1_32_Completed_cup_drawing_model_setup) In Generate DB page, click on the ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database. Observe the message in Message tab informing database generation status.

![]({{ '/assets/images/applications/55_3_sheet_forming/3d_cup_drawing_lab/3d_cpdwl1_image031.jpg' | relative_url }})

Completed cup drawing model setup

## Running Simulation

Once the database has been generated switch to the Simulation mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the operation tree. Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. 3DCDL1.33. Use the default **Continue****Run** option to select “**Continue****from the last step** ” option and then select the Simulation mode as **Interactive** radio button **** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation..

![]({{ '/assets/images/applications/55_3_sheet_forming/3d_cup_drawing_lab/3d_cpdwl1_image033.jpg' | relative_url }})

Run simulation window

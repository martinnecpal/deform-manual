---
lang: sk
title: "2D Cup Drawing Lab"
---

# 2D Cup Drawing Lab

1.1. Creating a New Problem

1.2. Geometry type

1.3. Simulation controls

1.4. Material list

1.5. Object

1.5.1. Workpiece

1.5.2. Punch

1.5.3. Die

1.5.4. Pressure Pad

1.6. Schedule Positioning

1.7. Contact

1.8. Stopping Controls

1.9. Step controls Definition

1.10. Generate Database

1.11. Running Simulation

## Creating a New Problem

On a Windows machine, go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select DEFORM GUI Main v1x.x. from the menu. The **DEFORM GUI Main** window will appear as shown in Fig. 2DCDL1.1.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0001.jpg' | relative_url }})

DEFORM GUI Main

Create a new problem either by selecting **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in Fig. 2DCDL1.2. Select " **I****ntegrated Manufacturing Process** " radio button and units system as "**English** " radio button in units field. Define Problem Name as "**2****DCup******" and make sure the “**Show option dialog** ” check box is turned on (if we do not turn on the “Show option dialog” check box, then we will not get the New Project dialog). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

New Problem page

Multiple operation wizard will open with the New Project dialog, at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session we will use ‘**2DCup** ’ as the project name. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.  
  
Add 2D Forming operation from the Explorer Operations list. Add the operation by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button available next to 2D Forming or user can also add the operation by drag and drop into the Operation Editor (see Fig. 2DCDL1.3.). 

![]({{ '/assets/images/applications/55_3_sheet_forming/2d_cup_drawing_lab/2d_cpdwl1_image002.jpg' | relative_url }})

GUI after adding 2D Forming operation

## Geometry type

In this lab we are using Axisymmetric geometries, so select **2D Axisymmetric** radio button in Geometry type (see Fig. 2DCDL1.4.), then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button. 

![]({{ '/assets/images/applications/55_3_sheet_forming/2d_cup_drawing_lab/2d_cpdwl1_image003.jpg' | relative_url }})

Axisymmetric Geometry type selection

## Simulation controls

In this operation, we will be setting up simple Isothermal operation hence in Simulation control page Sim Mode tab,**turn off** the **Heat transfer mode check box** (See Fig. 2DCDL1.5.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button. 

![]({{ '/assets/images/applications/55_3_sheet_forming/3d_cup_drawing_lab/3d_cpdwl1_image003.jpg' | relative_url }})

Simulation control page

## Material list

In Material page, import the material “**steel_cold_70F_20C__e.key** ” from DEFORM installation folder “\2D\Labs\CupDrawing\” directory. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button. 

### **Defining Anisotropy yield model:**

In 3D models, planar anisotropic behaviour can be captured by setting the yield criteria to “**Hill’s quadratic (R value**)” (see Fig. 2DCDL1.6.) and then defining R0, R45 and R90 parameters. Changing the default values to those shown below will result in earring. To change the values, click on Hill’s quadratic (R value) and define values for R0, R45 and R90 as shown in Fig. 2DCDL1.7. The R0, R45 and R90 are aligned to X, XY and Y directions in global space by default. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button. 

![]({{ '/assets/images/applications/55_3_sheet_forming/3d_cup_drawing_lab/3d_cpdwl1_image004.jpg' | relative_url }})

Steel, COLD [70F(20C)] page

![]({{ '/assets/images/applications/55_3_sheet_forming/3d_cup_drawing_lab/3d_cpdwl1_image005.jpg' | relative_url }})

Hill’s quadratic (R value) page

## Object

In object page, click on ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) button and add 4 objects in list as shown in Fig. 2DCDL1.8. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button.

![]({{ '/assets/images/applications/55_3_sheet_forming/3d_cup_drawing_lab/3d_cpdwl1_image006.jpg' | relative_url }})

Object page

### Workpiece

In the Workpiece page, keep the object name as **Workpiece** and object temperature as 68F. Select object type as **Elasto-plastic** (see Fig. 2DCDL1.9.). Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Geometry page.

![]({{ '/assets/images/applications/55_3_sheet_forming/2d_cup_drawing_lab/2d_cpdwl1_image004.jpg' | relative_url }})

Workpiece page

#### Create a Workpiece geometry

We will generate workpiece geometry using geometry primitives. Click on ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) in geometry page and select “**Cylinder** ” from “Geometry Primitive” window. Define the cylinder **Radius** as **2.95276** and **Height**(H) as **0.11811** ( see Fig. 2DCDL1.10.) to create a sheet metal blank. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to Close the Geometry Primitive window. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button to Mesh page.

![]({{ '/assets/images/applications/55_3_sheet_forming/2d_cup_drawing_lab/2d_cpdwl1_image005.jpg' | relative_url }})

Defining the Workpiece geometry

#### Generating Mesh

Define **number of elements** as **300** as shown in Fig. 2DCDL1.11. Click on **weighing Factors** tab and **set all weighing factors to zero** as shown in Fig. 2DCDL1.12. Click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button. The Mesh should like a shown in Fig. 2DCDL1.12. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button to Material page.

![]({{ '/assets/images/applications/55_3_sheet_forming/2d_cup_drawing_lab/2d_cpdwl1_image006.jpg' | relative_url }})

Mesh settings for Workpiece

![]({{ '/assets/images/applications/55_3_sheet_forming/2d_cup_drawing_lab/2d_cpdwl1_image007.jpg' | relative_url }})

Weighing Factors settings for workpiece mesh

####  Assign Material

Select the "**Steel,COLD[70F(20C)]** " material in material list which is already available for Workpiece. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button to BCC.

#### Boundary Conditions

Velocity BCC for the nodes along the axis in X direction are already fixed as shown in Fig. 2DRBCL.13. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button until top die.

![]({{ '/assets/images/applications/55_3_sheet_forming/2d_cup_drawing_lab/2d_cpdwl1_image008.jpg' | relative_url }})

Velocity BCC Definition

### Punch

In the Top die object page, change the **object name** to **Punch** and make sure **object type** is **Rigid**(see Fig. 2DCDL1.14.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button to Geometry page.

![]({{ '/assets/images/applications/55_3_sheet_forming/2d_cup_drawing_lab/2d_cpdwl1_image009.jpg' | relative_url }})

Punch page

#### Importing Punch Geometry

In Punch’s Geometry page, import Geometry **cup_draw-op1-punch-english.dxf** from DEFORM installation folder “\2D\Labs\CupDrawing\” directory. The Punch geometry should look like as shown in Fig. 2DCDL1.15. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Movement Page.

![]({{ '/assets/images/applications/55_3_sheet_forming/2d_cup_drawing_lab/2d_cpdwl1_image010.jpg' | relative_url }})

Punch Geometry

#### Assign Movement for Punch

Select “**Speed** ” under the movement options. Be sure movement is in the “**-Y** ” direction. Enter a speed of **10** in/sec as shown in Fig. 2DCDL1.16. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Property page.

![]({{ '/assets/images/applications/55_3_sheet_forming/2d_cup_drawing_lab/2d_cpdwl1_image011.jpg' | relative_url }})

Punch Movement page

#### Reference Point on Punch

In property page, select “**Reference** ” tab and enter “**0** ” for X and Y coordinates as shown in Fig. 2DCDL1.17. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Bottom die page.

![]({{ '/assets/images/applications/55_3_sheet_forming/2d_cup_drawing_lab/2d_cpdwl1_image012.jpg' | relative_url }})

Reference point on Punch

### Die

In the Bottom die object page, change the **object name** to **Die** and make sure **object type** is **Rigid**(see Fig. 2DCDL1.18.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Geometry page.

![]({{ '/assets/images/applications/55_3_sheet_forming/2d_cup_drawing_lab/2d_cpdwl1_image013.jpg' | relative_url }})

Die page

#### Importing Die Geometry

In Die’s Geometry page, import Geometry **cup_draw-op1-die-english.dxf** from DEFORM installation folder “\2D\Labs\CupDrawing\” directory. The Die geometry should look like as shown in Fig. 2DCDL1.19. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Property page.

![]({{ '/assets/images/applications/55_3_sheet_forming/2d_cup_drawing_lab/2d_cpdwl1_image014.jpg' | relative_url }})

Die Geometry

#### Reference Point on Die

In Die’s property page, select “**Reference** ” tab and enter the values **5** and **-4** to X and Y coordinates respectively (See Fig. 2DCDL1.20.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Object4 page.

![]({{ '/assets/images/applications/55_3_sheet_forming/2d_cup_drawing_lab/2d_cpdwl1_image015.jpg' | relative_url }})

Reference point definition on Die

### Pressure Pad

In the Object4 object page, change the **object name** to **Pressure Pad** and make sure **object type** is **Rigid**(See Fig. 2DCDL1.21.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Geometry page.

![]({{ '/assets/images/applications/55_3_sheet_forming/2d_cup_drawing_lab/2d_cpdwl1_image016.jpg' | relative_url }})

Pressure Pad page

#### Importing Pressure Pad Geometry

In Pressure Pad’s Geometry page, import **cup_draw-op1-Pressure-pad-english.dxf** from DEFORM installation folder “\2D\Labs\CupDrawing\” directory. The Pressure Pad geometry should look like as shown in Fig. 2DCDL1.22. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Movement page.

![]({{ '/assets/images/applications/55_3_sheet_forming/2d_cup_drawing_lab/2d_cpdwl1_image017.jpg' | relative_url }})

Pressure Pad Geometry

#### Assign Movement for Pressure Pad

In Movement page, select movement type as “**Sliding****die** ”. Set **Preload** as**8** klb which is exerted on Pressure Pad. Set**Maximum displacement** as **2** in and **movement direction** as **+Y****direction** which is a spring compression direction as shown in Fig. 2DCDL1.23. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Controls page.

![]({{ '/assets/images/applications/55_3_sheet_forming/2d_cup_drawing_lab/2d_cpdwl1_image018.jpg' | relative_url }})

Pressure Pad Movement settings

## Schedule Positioning 

Add first schedule position as **interference positioning** of the **punch** to the **workpiece** in the **–Y** direction with **interference tolerance** of **1e-06**. Add second scheduled positioning as **interference positioning** of the **pressure pad** to the **workpiece** in the **–Y** direction with **interference tolerance** of **1e-06** , turn on the “**Update****sliding die current displacement** ” and “**Update****current stroke** ” check boxes. After completing the definition, the scheduled positioning page looks like as shown in Fig. 2DCDL1.24. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button to Contact page.

![]({{ '/assets/images/applications/55_3_sheet_forming/2d_cup_drawing_lab/2d_cpdwl1_image019.jpg' | relative_url }})

Schedule Positioning page after completion of positioning definition

## Contact

In Contact page, click on ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) to automatically define all relevant contact pairs. Click on **Punch - workpiece** relation ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) and select **hybrid friction** with **coulomb friction** as **0.05** and **shear friction** as **0.12** as shown in Fig. 2DCDL1.25. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button to close the “Inter-Object Data Definition” window. In “Contact” page click on ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) to apply same conditions to all contact pairs. Click on ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) button to calculate default contact tolerance value and Generate contact by clicking on ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) button. Set the **scheduled contact tolerance** to **0.00001** as shown in Fig. 2DCDL1.26. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button to Stopping controls page.

![]({{ '/assets/images/applications/55_3_sheet_forming/2d_cup_drawing_lab/2d_cpdwl1_image020.jpg' | relative_url }})

Hybrid Friction model definition

![]({{ '/assets/images/applications/55_3_sheet_forming/2d_cup_drawing_lab/2d_cpdwl1_image021.jpg' | relative_url }})

Contact page

## Stopping Controls

In Stopping Controls page, define a die distance stopping control based on the reference points of the punch and die. Select the **Punch** object for “**Reference****1** ” and the **Die** object as “**Reference****2** ”. “**Method** ” should be set to “**Y****Distance** ”. Define the stopping distance as **1.375** ” as shown in Fig. 2DCDL1.27.

![]({{ '/assets/images/applications/55_3_sheet_forming/2d_cup_drawing_lab/2d_cpdwl1_image022.jpg' | relative_url }})

Stopping Control definition

## Step controls Definition

In “**Step** ” page under “**Simulation****steps** ” ![]({{ '/assets/icons/pre_icons/mo_simulation_step.jpg' | relative_url }}) tab, define **number of steps** as **1000** and s**tep increment to save** as **20**. In “**Step****increment** ” ![]({{ '/assets/icons/pre_icons/mo_step_increment.jpg' | relative_url }}) tab, select step definition type as “**die displacement** ” and set the step size to**0.005** in/step as shown in Fig. 2DCDL1.28.

![]({{ '/assets/images/applications/55_3_sheet_forming/2d_cup_drawing_lab/2d_cpdwl1_image023.jpg' | relative_url }})

Step increment page

  
Select “**Solver****settings** ” tab, select solver as “**MUMPS** ” and iteration method as “**Newton-****Raphson** ”. Set the “Force error” tolerance to 0.001 from Advanced tab in Solver Setting as shown in Fig. 2DCDL1.29.

![]({{ '/assets/images/applications/55_3_sheet_forming/2d_cup_drawing_lab/2d_cpdwl1_image024.jpg' | relative_url }})

Solver settings

## Generate Database

When we visit Generate DB page, "Apply Scheduled positioning" popup appears since we defined scheduled positioning data. Click on ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}) button in popup to apply scheduled positioning.

The completed setup looks like as shown in Fig. 2DCDL1.30. In Generate DB page, click on the ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database. Observe the message in Message tab informing database generation status.

![]({{ '/assets/images/applications/55_3_sheet_forming/2d_cup_drawing_lab/2d_cpdwl1_image025.jpg' | relative_url }})

Completed cup drawing model setup

## Running Simulation

Once the database has been generated switch to the Simulation mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the operation tree. Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. 2DCDL1.31 Use the default **Continue****Run** option to select “**Continue****from the last step** ” option and then select the Simulation mode as **Interactive** radio button **** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/applications/55_3_sheet_forming/2d_cup_drawing_lab/2d_cpdwl1_image031.jpg' | relative_url }})

Run simulation window

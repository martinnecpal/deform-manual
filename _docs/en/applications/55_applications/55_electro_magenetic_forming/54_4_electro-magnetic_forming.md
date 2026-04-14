---
lang: en
title: "Electro-Magnetic Forming Lab1"
---

# Electro-Magnetic Forming Lab

In this lab we will demonstrate how to setup a simple Electro-magnetic forming operation.

1.1. Creating a New Problem

1.2. Adding Forming Operation

1.3. Simulation Controls

1.4. Material list

1.5. Objects

1.5.1. Workpiece

1.5.2. Top Die

1.5.3. Bottom Die

1.6. Contact

1.7. Stopping controls

1.8. Step controls

1.9. Generate DB

1.10. Running Simulation

1.11. Post Processing

## Creating a New Problem 

On a Windows machine, go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** v1x.x from the menu. The DEFORM GUI Main window will appear, as shown in Fig. EMFL1.1

![]({{ '/assets/images/applications/55_2_arc_welding/image0001.jpg' | relative_url }})

QT4 GUI Main window

Create a new problem either by selecting **File**![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in Fig. EMFL1.2. Select " **Integrated Manufacturing Process** " radio button and unit system as "**SI** " radio button in unit field. Define Problem Name as " **3D_EMFORMING** " and click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Integrated Manufacturing Process.

![]({{ '/assets/images/applications/55_2_arc_welding/image0002.jpg' | relative_url }})

New Problem page

Multiple operation wizard will open, at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session we will use "**3D_EMFORMING** " as the project name. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

## Adding Forming Operation

Add 3D Forming operation from the Explorer Operations list. Add the operation by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button available next to [3D] Forming or can also be added by drag and drop into the Operation editor (See Fig. EMFL1.3.). When we add the Forming operation, process settings Window will open by default.

![]({{ '/assets/images/applications/55_electro_magenetic_forming_lab/image0003.jpg' | relative_url }})

Adding 3D Forming operation from Explorer

## Simulation Controls

Click on ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) button to switch to Expert mode since advanced settings are required to set up Electro-magnetic forming operation, by default "**Deformation** " and "**Heat****Transfer** " Mode check box would be checked if not, check the "Deformation" and "Heat Transfer" Mode check boxes. Select "**Electro-magnetic forming** " **Simulation****type**(See Fig. EMFL1.4 ), when we select Electro-magnetic forming simulation type by default "**Induction (BEM)** " **type** "**Heating** " will be selected and in **Solver** setting **Explicit****solver** Under Deformation will be selected. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Material page.

![]({{ '/assets/images/applications/55_electro_magenetic_forming_lab/image0004.jpg' | relative_url }})

Simulation controls

## Material list

Using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) button import materials from "**AL-1100,COLD[70F(20C)].key** " and "**coil_material.key** " from /**3D/ LABS/ EM_Forming** folder. Imported materials will be displayed as shown in below Fig. EMFL1.5. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Object page.

![]({{ '/assets/images/applications/55_electro_magenetic_forming_lab/image0005.jpg' | relative_url }})

Material list

##  Objects

In this lab we need three objects, in the list keep all three objects, Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Workpiece page.

### Workpiece

Keep the default **Object****name** as "**Workpiece** ", Object **Temperature** as **20** °C and change Object Type to **Elasto-plastic** as shown in Fig. EMFL1.6. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Geometry page.

![]({{ '/assets/images/applications/55_electro_magenetic_forming_lab/image0006.jpg' | relative_url }})

Workpiece General page

#### Workpiece Geometry

To define tube workpiece geometry for electro-magnetic forming click on ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}), select **Hollow cylinder** type and define **Inside****Radius**(R1) as **6.5** mm, **Outside****Radius**(R2) as**7.5** mm and **Height**(H) as **50** mm as shown in Fig. EMFL1.7. and click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Mesh page.

![]({{ '/assets/images/applications/55_electro_magenetic_forming_lab/image0007.jpg' | relative_url }})

Workpiece geometry primitive

#### Workpiece Mesh

Select type of mesh as **Brick** mesh, under "**2D Cross section** " tab define Target number of elements as **80** , **Thickness** as **2** and **Size****ratio** as ******1** and check the **Mapped mesh generation** check box as shown in below Fig. EMFL1.8.

![]({{ '/assets/images/applications/55_electro_magenetic_forming_lab/image0008.jpg' | relative_url }})

Brick Mesh - 2D Cross section page

Under "**General** " tab, select **Uniform thickness of layers** and define **# of layers** as **52** as shown in Fig. EMFL1.9. and click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) and click **No** for Default Boundary condition popup as we will be defining required BCC. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Material page.

![]({{ '/assets/images/applications/55_electro_magenetic_forming_lab/image0009.jpg' | relative_url }})

Brick Mesh - General page

#### Workpiece Material

Assign "**AL-1100,COLD[70F(20C)]** " for the workpiece as shown in Fig. EMFL1.10. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to BCC page.

![]({{ '/assets/images/applications/55_electro_magenetic_forming_lab/image0010.jpg' | relative_url }})

Workpiece Material page

#### Workpiece Boundary condition

Fix the bottom surface of the workpiece by assigning Vz=0 to the bottom surface (see Fig. EMFL1.11.) and fix both Top surface and Bottom surface of the workpiece in X and Y directions by assigning Vx=0 and Vy=0 to the respective surfaces as shown in Fig. EMFL1.12.

![]({{ '/assets/images/applications/55_electro_magenetic_forming_lab/image0011.jpg' | relative_url }})

Assigned Velocity BCC (Vz=0) for workpiece

![]({{ '/assets/images/applications/55_electro_magenetic_forming_lab/image0012.jpg' | relative_url }})

Assigned Velocity BCC (Vy=0) for workpiece

Under **Induction****BEM** from BCC tree, select **Heating****Surface** option and select **Outer****surface** of the workpiece, then click on ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) to finish the assignment. Defined Heating Surface BCC as shown in below Fig. EMFL1.13. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top die page.

![]({{ '/assets/images/applications/55_electro_magenetic_forming_lab/image0013.jpg' | relative_url }})

Workpiece Heating surface BCC

### Top Die

In Top Die page, change the Object name to **COIL** and using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) option import **COIL.key** from **/3D/ LABS/EM_Forming** folder. The imported COIL.key is having COIL geometry along with Brick mesh data as shown in Fig. EMFL1.14. Since we don’t need to generate geometry and mesh, we will navigate using until Material page.

![]({{ '/assets/images/applications/55_electro_magenetic_forming_lab/image0014.jpg' | relative_url }})

Imported Top die object

#### COIL Material

Assign **coil** Material from list to COIL as shown in Fig. EMFL1.15. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Boundary condition page.

![]({{ '/assets/images/applications/55_electro_magenetic_forming_lab/image0015.jpg' | relative_url }})

COIL Material page

#### COIL Boundary Condition

Under Induction BEM from BCC tree, select Heating Surface option and select all surfaces of the Coil except Coil begin and Coil End surface, then click on ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) to finish the assignment (See Fig. EMFL1.16.).

![]({{ '/assets/images/applications/55_electro_magenetic_forming_lab/image0016.jpg' | relative_url }})

Assigned Heating Surface BCC

Select **Coil****Begin****surface** option under BCC and select COIL begin surface and assign as shown in Fig. EMFL1.17.

![]({{ '/assets/images/applications/55_electro_magenetic_forming_lab/image0017.jpg' | relative_url }})

Assigned Coil Begin Surface BCC

Similarly, select Coil End Surface option under BCC and select COIL End surface and assign as shown in Fig. EMFL1.18. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Properties page.

![]({{ '/assets/images/applications/55_electro_magenetic_forming_lab/image0018.jpg' | relative_url }})

Assigned Coil End Surface BCC

#### COIL Properties

Select "**Heating** " tab in object “**Properties** ” page, select **Current****frequency** type as **Single** , define **Current****frequency** as **Constant** value of **8800** Hz, select **Volume** charge type as "**Current****density** " and define **Current****Density** as **function****of****time** by selecting Function of time type under “**Data****Definition** ” as shown in Fig. EMFL1.19.

![]({{ '/assets/images/applications/55_electro_magenetic_forming_lab/image0019.jpg' | relative_url }})

COIL Properties page

Click on ![]({{ '/assets/icons/pre_icons/mo_define..._button2.jpg' | relative_url }}) and import **volume_charge.dat** file from **/3D/ LABS/EM_Forming** folder and click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), imported file will have data as shown in Fig. EMFL1.20. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Bottom Die page.

![]({{ '/assets/images/applications/55_electro_magenetic_forming_lab/image0020.jpg' | relative_url }})

Imported volume charge file data

### Bottom Die

In Bottom Die page, change the object name to **Mandrel** and keep object type to default "**Rigid** " and object temperature as 20°C as shown in Fig. EMFL1.21. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to object geometry page.

![]({{ '/assets/images/applications/55_electro_magenetic_forming_lab/image0021.jpg' | relative_url }})

Bottom die page

#### Mandrel Geometry

In Geometry page, using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) button import **Mandrel.geo** file from **/3D/ LABS/EM_Forming** folder, after importing any geometry use ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) action label to check the Geometry and click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to close Check popup and Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Contact page.

![]({{ '/assets/images/applications/55_electro_magenetic_forming_lab/image0022.jpg' | relative_url }})

Mandrel geometry page

## Contact

In **Contact** page, add one relation by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button, select **Mandrel** as **Master** and **Workpiece** as **Slave**. Click on ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) and define **Shear** as **0.12**. Click the ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) to determine an intelligent contact tolerance. Click ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) to generate contact. Navigate using ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Stopping controls page.

![]({{ '/assets/images/applications/55_electro_magenetic_forming_lab/image0023.jpg' | relative_url }})

Contact page

## Stopping controls

Define **Process****duration** as **0.0003** as shown in Fig. EMFL1.24., click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Step page

![]({{ '/assets/images/applications/55_electro_magenetic_forming_lab/image0024.jpg' | relative_url }})

Stopping controls

## Step controls

Switch to Guided mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }}), define the **Number of Steps** as **500** , **Step increment** as **1** and **Time per step** as **1e-06** as shown in Fig. EMFL1.25.

![]({{ '/assets/images/applications/55_electro_magenetic_forming_lab/image0025.jpg' | relative_url }})

Step controls -Guided mode

Switch to **Expert****mode** by clicking on ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) button, under **Solver****setting** \- **Deformation** tab we can observe by default **Explicit** solver has been selected when we selected simulation type as Electro-magnetic forming. Define explicit solver settings **Damping****coefficient** as **1** , **Mass****scaling****factor** as **1** and **cycle** as **10**. Select **iteration****method** type as **Newton-Rapson** as shown in Fig. EMFL1.26.

![]({{ '/assets/images/applications/55_electro_magenetic_forming_lab/image0026.jpg' | relative_url }})

Solver settings - Deformation tab

Under Solver setting - **Advanced** tab, **uncheck** the **Deformation** check box within **Bandwidth optimization – deformation solver** tab, Define **maximum****iterations****per****deformation****time** step as **1000** in Maximum iterations- deformation solver tab and **uncheck** the **Temperature check box in Bandwidth optimization - temperature solver** tab, after making these changes the settings should look like as shown in Fig. EMFL1.27.

![]({{ '/assets/images/applications/55_electro_magenetic_forming_lab/image0027.jpg' | relative_url }})

Solver settings - Advanced tab

Under **Process****conditions** \- **Induction** tab, define **Source energy ratio** as **1000** as shown in Fig. EMFL1.28.

![]({{ '/assets/images/applications/55_electro_magenetic_forming_lab/image0028.jpg' | relative_url }})

Process conditions - Induction tab

Under **Advanced****options** \- **Frequency** tab we can define frequency of calculations for **Contact** , **Temperature** and **Database****writing** for explicit solver, for this lab we will use **Auto** as shown in Fig. EMFL1.29. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to DB Generation page.

![]({{ '/assets/images/applications/55_electro_magenetic_forming_lab/image0029.jpg' | relative_url }})

Advanced options - Frequency tab

## Generate DB

Click![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) to see if anything was missed in the setup and then click on the ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database. Observe the message in Message tab informing database generation status.

## Running Simulation

Once the database has been generated, switch to the Simulation mode by selecting the ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the object tree. To start the simulation click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. EMFL1.30.) Use the default  **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/applications/55_electro_magenetic_forming_lab/image0030.jpg' | relative_url }})

Run Simulation Window

Monitor the progress of the simulation by looking at the Simulation Message and Simulation Log tab, making sure that the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked. User can view the Electro- magnetic forming process as the simulation proceeds to the specified Step definition from Simulation graphics.

## Post Processing

When the simulation is completes, review the results by switching to Post mode using the ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) button above the Simulation tool bar.

Play through the steps using animation option and observe the workpiece deformation.

**Slicing:**

Click on ![]({{ '/assets/icons/pre_icons/mo_slice.jpg' | relative_url }}) and slice the object in **X** direction as shown in Fig. EMFL1.31. Play the steps and observe the workpiece deformation.

![]({{ '/assets/images/applications/55_electro_magenetic_forming_lab/image0031.jpg' | relative_url }})

Sliced object using Slicing option

**State variable:**

Select single object mode ![]({{ '/assets/icons/pre_icons/mo_show_single_obj_icon.jpg' | relative_url }}) and plot **Strain-Effective** state variable and observe the strain distribution. (See Fig. EMFL1.32.)

![]({{ '/assets/images/applications/55_electro_magenetic_forming_lab/image0032.jpg' | relative_url }})

Strain - Effective distribution in Workpiece

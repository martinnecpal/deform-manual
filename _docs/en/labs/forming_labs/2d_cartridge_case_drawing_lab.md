---
lang: en
title: "2D Cartridge case drawing lab"
---

# 2D Cartridge case drawing lab

**Problem Summary:**

In this lab, we will be demonstrating about how to use Integrated Manufacturing Process UI (MO) to setup multiple stages of forming process in batch mode. We will be setting up a multi-stage extrusion process to simulate cartridge case forming using [2D]Forming operation from Integrated Manufacturing Process UI. The process involves three stages of extrusion with annealing in between each stage for strain relief. 

We will be setting up all 3 stations at a time in batch mode, Workpiece will be transferred to all operations while changing dies for station 2 and station3. We will be simulating only forming process in this lab and not annealing process, instead we will initialize the strain, damage and velocity of the workpiece in successive forming operations. The dies will be positioned using schedule positioning so that objects are positioned during DB generation. The contact generation also will be scheduled so that the contacts between objects will be generated during DB generation.

[1\. Creating New Problem and Adding Operations](2d_cartridge_case_drawing_lab.htm#1_Creating_New_problem_and_Adding_Operations)

[1.1. Creating New Problem](2d_cartridge_case_drawing_lab.htm#1_1_Creating_a_New_problem)

[1.2. Adding operations to Operation Editor](2d_cartridge_case_drawing_lab.htm#1_2_Adding_operations_to_Operation_Editor)

[2\. Setting up Station 1](2d_cartridge_case_drawing_lab.htm#2_Setting_up_Station1)

[2.1. Select Geometry Type and Simulation Controls](2d_cartridge_case_drawing_lab.htm#2_1_Select_Geometry_Type_and_Simulation_modes)

[2.2. Material List](2d_cartridge_case_drawing_lab.htm#2_2_Material_List)

[2.3. Objects](2d_cartridge_case_drawing_lab.htm#2_3_Objects)

[2.4. Workpiece](2d_cartridge_case_drawing_lab.htm#2_4_Workpiece)

[2.5. Punch](2d_cartridge_case_drawing_lab.htm#2_5_Punch)

[2.6. Die](2d_cartridge_case_drawing_lab.htm#2_6_Die)

[2.7. Ejector](2d_cartridge_case_drawing_lab.htm#2_7_Ejector)

[2.8. Defining Scheduled positioning](2d_cartridge_case_drawing_lab.htm#2_8_Defining_Scheduled_positioning)

[2.9. Defining contact conditions](2d_cartridge_case_drawing_lab.htm#2_9_Defining_contact_conditions)

[2.10. Stopping controls](2d_cartridge_case_drawing_lab.htm#2_10_Stopping_controls)

[2.11. Step Controls](2d_cartridge_case_drawing_lab.htm#2_11_Step_Controls)

[2.12. Generating Database](2d_cartridge_case_drawing_lab.htm#2_12_Generating_Database)

[3\. Setting up Station 2](2d_cartridge_case_drawing_lab.htm#3_Setting_up_Station2)

[3.1. Select Geometry Type and Simulation modes](2d_cartridge_case_drawing_lab.htm#3_1_Select_Geometry_Type_and_Simulation_modes)

[3.2. Workpiece](2d_cartridge_case_drawing_lab.htm#3_2_Workpiece)

[3.3. Punch](2d_cartridge_case_drawing_lab.htm#3_3_Punch)

[3.4. Die](2d_cartridge_case_drawing_lab.htm#3_4_Die)

[3.5. Ejector](2d_cartridge_case_drawing_lab.htm#3_5_Ejector)

[3.6. Scheduled Positioning](2d_cartridge_case_drawing_lab.htm#3_6_Scheduled_Positioning)

[3.7. Defining Contact conditions and scheduling contact generation for Station2](2d_cartridge_case_drawing_lab.htm#3_7_Defining_Contact_conditions_and_scheduling_contact_generation_for_Station2)

[3.8.Stopping controls for Station2](2d_cartridge_case_drawing_lab.htm#3_8_Stopping_controls_for_Station2)

[3.9. Step Controls for Station2](2d_cartridge_case_drawing_lab.htm#3_9_Step_Controls_for_Station2)

[4\. Setting up Station3](2d_cartridge_case_drawing_lab.htm#4_Station3)

[4.1. Select Geometry Type and Simulation modes](2d_cartridge_case_drawing_lab.htm#4_1_Select_Geometry_Type_and_Simulation_modes)

[4.2. Workpiece](2d_cartridge_case_drawing_lab.htm#4_2_Workpiece)

[4.3. Punch](2d_cartridge_case_drawing_lab.htm#4_3_Punch)

[4.4 Die](2d_cartridge_case_drawing_lab.htm#4_4_Die)

[4.5. Ejector](2d_cartridge_case_drawing_lab.htm#4_5_Ejector)

[4.6. Scheduled Positioning](2d_cartridge_case_drawing_lab.htm#4_6_Scheduled_Positioning)

[4.7. Defining Contact Conditions and scheduling contact generation for Station3](2d_cartridge_case_drawing_lab.htm#4_7_Defining_Contact_conditions_and_scheduling_contact_generation_for_Station3)

[4.8. Stopping controls for Station3](2d_cartridge_case_drawing_lab.htm#4_8_Stopping_controls_for_Station3)

[4.9. Step Controls for Station3](2d_cartridge_case_drawing_lab.htm#4_9_Step_Controls_for_Station3)

[5\. Running Simulation](2d_cartridge_case_drawing_lab.htm#5_Running_Simulation)

[6\. Post Processing](2d_cartridge_case_drawing_lab.htm#6_Post_Processing)

## Creating New problem and Adding Operations

### Creating a New problem

On a **Windows machine** , press ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button, select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear.

Create a new problem either by selecting **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear. Select " **Integrated Manufacturing Process** " radio button and unit system as "**English** " using radio button. Define Problem Name as "**Cartridge_Case_Lab** " and make sure the “**Show option dialog** ” check box is turned on (if we do not turn on the “**Show option dialog** ” check box, then we will not get the New Project dialog in MO UI). Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to close the New Problem dialog and open the project in Integrated Manufacturing Process UI.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image001.jpg' | relative_url }})

New problem dialog

### Adding operations to Operation Editor

Multiple Operation wizard will open the new project. Add three 2d forming operations from Operations Explorer list clicking ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image002.jpg' | relative_url }})

Adding operations

## Setting up Station1:

Select first forming operation and change the operation name to "**Station1** " by double clicking on Operation name in Operation Editor window and press Enter in Keyboard.

### Select Geometry Type and Simulation modes

Select the **2D Axisymmetric** radio button in geometry type window as show in [Fig. 2DCCDL1.3.](2d_cartridge_case_drawing_lab.htm#Fig_2DCCDL1_3_Geometry_type_selection) and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue to Simulation controls page. In Simulation controls page, uncheck the Heat transfer mode check box as shown in [Fig. 2DCCDL1.4.](2d_cartridge_case_drawing_lab.htm#Fig_2DCCDL1_4_Simulation_controls_page) and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image003.jpg' | relative_url }})

Geometry type selection

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image004.jpg' | relative_url }})

Simulation controls page

### Material List 

Once the geometry type an simulation modes are set, we will load the materials required for this setup. Using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) button in Material list page, import "**C26000, Cartridge Brass, 70%, annealed [70F(20C)]** " material keyword from /2D/LABS/Cartridge_Lab folder, see [Fig. 2DCCDL1.5.](2d_cartridge_case_drawing_lab.htm#Fig_2DCCDL1_5_Material_List) Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Object page.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image005.jpg' | relative_url }})

Material List

### Objects

We need four objects, Workpiece, Die Punch and Ejector to model for this setup. By default, three objects are added to the object list, we will add one more by clicking on![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) button. The objects will be renamed suitably as we progress through the setup. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Workpiece page.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image006.jpg' | relative_url }})

Objects list page

### Workpiece

#### Workpiece object type definition

Keep the default Object name as "**Workpiece** ", Object Type as **Plastic** and it’s Temperature as **68** °F as shown in [Fig. 2DCCDL1.7.](2d_cartridge_case_drawing_lab.htm#Fig_2DCCDL1_7_Workpiece_object_page) Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Geometry page to define Workpiece geometry.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image007.jpg' | relative_url }})

Workpiece object page

#### Defining Workpiece Geometry

We will define workpiece geometry using primitives. From the Workpiece’s geometry page, click on ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}), select Solid cylinder and define **Diameter** as **0.82** " and **Height** as **0.125** ", see [Fig. 2DCCDL1.8.](2d_cartridge_case_drawing_lab.htm#Fig_2DCCDL1_8_Defining_Workpiece_geometry) Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button in the Primitive window to close the window and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to navigate to Workpiece Mesh page.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image008.jpg' | relative_url }})

Defining Workpiece geometry

#### Generating mesh for Workpiece

In Mesh page, click on ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) to change to expert mode so that we can have access to various options to control mesh. Define the T**arget number of elements** as **1000** , **Thickness** **elements** as **4** and **Size****ratio** as **3** , click the ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button to generate the mesh for workpiece, see [Fig. 2DCCDL1.9.](2d_cartridge_case_drawing_lab.htm#Fig_2DCCDL1_9_Mesh_settings_for_Workpiece) Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button to Material page.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image009.jpg' | relative_url }})

Mesh settings for Workpiece

####  Assigning material to Workpiece

Select the "**C26000, Cartridge Brass, 70%, annealed [70F(20C)]** " in the material window to assign the material to the Workpiece, see [Fig. 2DCCDL1.10.](2d_cartridge_case_drawing_lab.htm#Fig_2DCCDL1_10_Assigning_material_to_Workpiece) Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button to move to Workpiece Boundary conditions page.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image010.jpg' | relative_url }})

Assigning material to Workpiece

#### Boundary conditions for Workpiece

For Axi-symmetric setup by default, velocity in x-direction will be fixed for all the nodes along the axis, we can observe the same in the BCC page for the Workpiece, see [Fig. 2DCCDL1.11.](2d_cartridge_case_drawing_lab.htm#Fig_2DCCDL1_11_Velocity_BCC_for_Workpiece) We do not need any additional BCC, hence click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button to navigate to Workpiece Properties page.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image011.jpg' | relative_url }})

Velocity BCC for Workpiece

#### Setting Limiting strain rate value for Workpiece

In Workpiece Properties page, we will modify the **Limiting** **strain** **rate** value to **0.001** from **Strain** rate tab to capturing the strains more accurately at lower strain rates, see [Fig. 2DCCDL1.12.](2d_cartridge_case_drawing_lab.htm#Fig_2DCCDL1_12_Setting_Limiting_strain_rate_value_for_Workpiece) As we do not need to define anything else for Workpiece we will click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button until we reach Top Die object page or select Punch from Operation tree.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image012.jpg' | relative_url }})

Setting Limiting strain rate value for Workpiece.

### Punch

#### Punch object type definition

Change the object name to "**Punch** ", keep the Object type as **Rigid** and the Temperature as **68** °F. Make sure that the **Primary die** check box is turned on as this is a moving object and the step controls and stopping controls will be applied to this object, see [Fig. 2DCCDL1.13.](2d_cartridge_case_drawing_lab.htm#Fig_2DCCDL1_13_Punch_object_definition) Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Punch Geometry page.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image013.jpg' | relative_url }})

Punch object definition

#### Punch Geometry Definition

We will load the geometry for the Punch from a file stored in \2D\LABS\Cartridge_Lab directory. Click the ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Load geometry from a file) button and import the file “**Punch.geo** ” by browsing the geometry file path located in DEFORM installation folder /2D/LABS/Cartridge_Lab directory, see [Fig. 2DCCDL1.14.](2d_cartridge_case_drawing_lab.htm#Fig_2DCCDL1_14_Loading_Punch_geometry) Check the geometry using ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) option to make sure the geometry is OK. The imported geometry should not have any issues. After defining the geometry for the Punch, we will use ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button to navigate until Movement page. We will not generate mesh for the Punch as the object type is Rigid and we do not intend to calculate temperature distribution.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image014.jpg' | relative_url }})

Loading Punch geometry

#### Defining Movement for Punch

The default mode for Punch movement is Constant speed. Input a value of **10** in/sec for the Constant value and confirm that the Direction is **-Y** , see [Fig. 2DCCDL1.15.](2d_cartridge_case_drawing_lab.htm#Fig_2DCCDL1_15_Movement_controls_for_Punch) As we do not need to define anything else for Punch, we will click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button until we reach Bottom Die object.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image015.jpg' | relative_url }})

Movement controls for Punch

### Die

#### Die object type definition

Change the object name to "**Die** ", keep the Object type as **Rigid** and the Temperature as **68** ° F, see [Fig. 2DCCDL1.16.](2d_cartridge_case_drawing_lab.htm#Fig_2DCCDL1_16_Die_Object_page) Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Die Geometry page.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image016.jpg' | relative_url }})

Die Object page

#### Die Geometry

For Die geometry, we will import the file “**Die.geo** ” by browsing the geometry file path located in DEFORM installation folder \2D\LABS\Cartridge_Lab directory using the ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Load geometry from a file) button in Geometry page, see [Fig. 2DCCDL1.17.](2d_cartridge_case_drawing_lab.htm#Fig_2DCCDL1_17_Loading_Die_geometry) Check the geometry using ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) option to make sure the geometry is OK. We do not need to define mesh or movement controls for Die as the Die is a rigid object, stationary and we are not calculating temperature distribution over the Die, we will click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button until we reach Object 4 page.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image017.jpg' | relative_url }})

Loading Die geometry

### Ejector

#### Ejector object type definition

Change the object name from Object 4 to "**Ejector** ", keep the Object type as **Rigid** and the Temperature as **68** ° F, see [Fig. 2DCCDL1.18.](2d_cartridge_case_drawing_lab.htm#Fig_2DCCDL1_18_Ejector_object_page) Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Ejector Geometry page.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image018.jpg' | relative_url }})

Ejector object page

#### Defining Ejector Geometry

We will import the file “**Ejector.geo** ” for Ejector geometry by browsing the geometry file path located in DEFORM installation folder \2D\LABS\Cartridge_Lab directory using the ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Load geometry from a file) button in Geometry page, see [Fig. 2DCCDL1.19.](2d_cartridge_case_drawing_lab.htm#Fig_2DCCDL1_19_Loading_Ejector_geometry) Check the geometry using ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) option to make sure the geometry is OK. We do not need to define mesh or movement controls for Ejector as the Ejector is a rigid object, stationary and we are not calculating temperature distribution over the Ejector, we will click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button until we reach Scheduled positioning page.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image019.jpg' | relative_url }})

Loading Ejector geometry

### Defining Scheduled positioning

We will be using Scheduled positioning so that the objects are positioned automatically based on the sequence of positioning defined in the Scheduled positioning page before DB is generated in DB generation page. To schedule position for Station1 objects, click on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button to add a positioning item and select ![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}). Change the Positioning object to the **Workpiece** and the Reference object to the **Die** , select the Approach Direction to **-Y.** Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) and we can observe that a positioning step being added based on our definition in the Scheduled positioning page. 

Similarly, position Punch over Workpiece by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button and select ![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}), change the Positioning Object to the **Punch** , the Reference object to the **Workpiece** and select the Approach Direction to **-Y**. We can observe the scheduled positioning sequence as shown in [Fig. 2DCCDL1.20.](2d_cartridge_case_drawing_lab.htm#Fig_2DCCDL1_20_Scheduled_positioning_definition_for_Station) Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to navigate to Contact page to define contact conditions.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image020.jpg' | relative_url }})

Scheduled positioning definition for Station1

### Defining contact conditions

As we are using schedule positioning to position the objects, we need to schedule the contact generation so that contacts between objects can be generated between the objects based on the positioning defined in the Schedule positioning. Turn on the checkboxes Initialize and Generate to initialize contacts and then generate new contacts based on the contact relations defined, see Fig. 2DCCDL1.21\. Assign the default inter-object relationships using ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) button. Click on the ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) button for one of the relationships. An Inter-object data window will open, select **Hybrid** type friction radio button in Deformation tab, define **0.1** value for both Coulomb and Shear. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to exit the Inter-object data window. Click on ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) to apply the same friction conditions defined for the selected relation to all other relations in the list, see [Fig. 2DCCDL1.21.](2d_cartridge_case_drawing_lab.htm#Fig_2DCCDL1_21_Defining_contact_conditions) Since contacts will be generated during DB generation, we will click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to navigate to Stopping controls page to define stopping controls.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image021.jpg' | relative_url }})

Defining contact conditions

### Stopping controls

We will be defining stopping controls so that simulation stops when the Workpiece crosses a plane. In Stopping controls page, click on **Stopping****plane** tab, turn on Defined checkbox and define Origin as (**0,-0.1**) and Vector as (**0,****-1**), see [Fig. 2DCCDL1.22.](2d_cartridge_case_drawing_lab.htm#Fig_2DCCDL1_22_Defining_Stopping_controls_for_Station1) Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to navigate to Step page to define simulation step controls.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image022.jpg' | relative_url }})

Defining Stopping controls for Station1

### Step Controls

We will be defining settings to control the simulation steps in Step page. Define **Number of Steps** for simulation as **10000** , **Step increment to save** steps into database as **10** and **Die displacement per step** as **0.001** , see[ Fig. 2DCCDL1.23.](2d_cartridge_case_drawing_lab.htm#Fig_2DCCDL1_23_Simulation_step_controls_for_Station1) Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Generate DB page.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image023.jpg' | relative_url }})

Simulation step controls for Station1

### Generating Database

In Generate database page, click on the ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) button, the data checking system will confirm that defined data is appropriate for running a simulation.Red marks indicate missing or incorrect data that will prevent a simulation from running. It is necessary to correct those errors before the database can be generated.

  
Yellow marks indicate data which may be suspect and should be reviewed. These should be investigated carefully, as they might result in system instability or erroneous (incorrect) results.  
  
Review the data checking information. If there are no yellow or red marks, click the ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button.  
You should look for the words: Database has been generated in the Message tab. When you see this, it means that your inputs have been saved to the database.

Click on ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) to proceed to set up ‘Station2’.

## Setting up Station2:

Change the operation name to "**Station2** " for the 2nd Forming operation in Operation editor tab as done for first operation by double clicking on the operation name and press Enter in Keyboard after editing the operation name. 

When we navigated to Station2, all objects from Station1 are moved to Station2 as Read from DB objects. In Station2, we will change the Die, Punch and Ejector geometries, and initialize the Strain, Damage and Velocity of the Workpiece to 0 as the Workpiece will undergo strain relaxation between the forming operations.

### Select Geometry Type and Simulation modes

Keep the **2D Axisymmetric** radio button selected as geometry type and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue to Simulation controls page. In Simulation controls page, uncheck the Heat transfer mode check box as shown in [Fig. 2DCCDL1.3.](2d_cartridge_case_drawing_lab.htm#Fig_2DCCDL1_3_Geometry_type_selection) of Station1 and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Workpiece page as we do not need any additional objects to be added to the Objects list for this operation.

### Workpiece 

#### Workpiece object type definition

We can notice that Object type of the Workpiece is Read from DB, the Workpiece object data will be read from the last step of the previous operation. We will keep the Workpiece as Read from DB, see [Fig. 2DCCDL1.24.](2d_cartridge_case_drawing_lab.htm#Fig_2DCCDL1_24_Workpiece_object_page) Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Workpiece Properties page as we will not be redefining the mesh or bcc for the Workpiece.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image024.jpg' | relative_url }})

Workpiece object page

#### Setting Limiting strain rate value for Workpiece

We will change the Limiting Strain rate value to capture the lower strain rates in the Workpiece. We will **turn****on****Redefine Strain rate checkbox** and **Limiting** as ‘**0.001** ’, see [Fig. 2DCCDL1.25.](2d_cartridge_case_drawing_lab.htm#Fig_2DCCDL1_25_Redefining_Limiting_Strain_rate_for_Workpiece) Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Initialize page to initialize Workpiece conditions.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image025.jpg' | relative_url }})

Redefining Limiting Strain rate for Workpiece

#### Initializing Workpiece conditions

In Initialize page, turn on **Strain** , **Damage** and **Velocity** check boxes and define value as ‘**0** ’ so that we can take into account the strain relaxation of the Workpiece, see [Fig. 2DCCDL1.26.](2d_cartridge_case_drawing_lab.htm#Fig_2DCCDL1_26_Initializing_Workpiece_conditions_in_Station2) Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Punch object page.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image026.jpg' | relative_url }})

Initializing Workpiece conditions in Station2

### Punch

#### Punch object type definition

We need to change the Punch geometry for the Station2, hence change the Object type from Read from DB to **Rigid** , see [Fig. 2DCCDL1.27.](2d_cartridge_case_drawing_lab.htm#Fig_2DCCDL1_27_Punch_object_page) Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Punch Geometry page.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image027.jpg' | relative_url }})

Punch object page

#### Changing Punch Geometry

In Punch Geometry page, import the file “**Punch2.geo** ” by browsing the geometry file path located in DEFORM installation folder \2D\LABS\Cartridge_Lab directory, see [Fig. 2DCCDL1.28.](2d_cartridge_case_drawing_lab.htm#Fig_2DCCDL1_28_Punch_geometry_in_Station2) Check the geometry using ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) option to make sure the geometry is OK. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until we reach Punch movement page.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image028.jpg' | relative_url }})

Punch geometry in Station2

#### Assign Movement to Punch in Station2

The default mode is constant speed. Input a value of **10** in/sec for the Constant value and confirm that the Direction is -Y. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Die object page.

### Die

#### Die object type definition

We need to change the Die geometry for the Station2, hence change the Object type from Read from DB to **Rigid**. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Die Geometry page.

#### Changing Die Geometry

Click the ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Load geometry from a file) button and import the file “**Die2.geo** ” by browsing the geometry file path located in DEFORM installation folder \2D\LABS\Cartridge_Lab directory, see [Fig. 2DCCDL1.29.](2d_cartridge_case_drawing_lab.htm#Fig_2DCCDL1_29_Die_geometry_for_Station2) Check the geometry using ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) option to make sure the geometry is OK. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Ejector object page.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image029.jpg' | relative_url }})

Die geometry for Station2

### Ejector

#### Ejector object type definition

We need to change the Ejector geometry for the Station2, hence change the Object type from Read from DB to **Rigid**. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Ejector Geometry page.

#### Changing Ejector Geometry

Click the ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }})(Load geometry from a file) button and import the file “**Ejector2.geo** ” by browsing the geometry file path located in DEFORM installation folder \2D\LABS\Cartridge_Lab directory, see [Fig. 2DCCDL1.30.](2d_cartridge_case_drawing_lab.htm#Fig_2DCCDL1_30_Ejector_geometry_for_Station2) Check the geometry using ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) option to make sure the geometry is OK. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Scheduled positioning page.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image030.jpg' | relative_url }})

Ejector geometry for Station2

### Scheduled Positioning

Currently, we do not have the Workpiece geometry output from Station1 simulation to position the dies as the Station1 is not yet simulated. Hence, we will use schedule positioning method which will position dies during DB generation for Station2 with respect to the Workpiece geometry output from Station1, Workpiece object type is Read from DB. 

To schedule position for Station2 objects, click on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button to add a positioning item and select ![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}). Change the Positioning object to the **Workpiece** and the Reference object to the **Die** , select the Approach Direction to **-Y.** Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) and we can observe that a positioning step being added based on our definition in the Scheduled positioning page. Similarly, position Punch over Workpiece by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button and select ![]({{ '/assets/icons/pre_icons/mo_interference_radio_button.jpg' | relative_url }}), change the Positioning Object to the **Punch** , the Reference object to the **Workpiece** and select the Approach Direction to **-Y**. We can observe the scheduled positioning sequence as shown in [Fig. 2DCCDL1.31.](2d_cartridge_case_drawing_lab.htm#Fig_2DCCDL1_31_Scheduled_positioning_definition_for_Station2) Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to navigate to Contact page to define contact conditions.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image031.jpg' | relative_url }})

Scheduled positioning definition for Station2

### Defining Contact conditions and scheduling contact generation for Station2

We need to schedule the contact generation so that contacts between objects can be generated with between the objects based on the positioning defined in the Schedule positioning. Turn on the check boxes Initialize and Generate to initialize contacts and then generate new contacts based on the contact relations defined, see [Fig. 2DCCDL1.32.](2d_cartridge_case_drawing_lab.htm#Fig_2DCCDl1_32_Defining_contact_conditions_for_Stage_2) Assign the default inter-object relationships using ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) button. Click on the ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button for one of the relationships. Select **Hybrid type** friction radio button in Deformation tab, define **0.1** value for both **Coulomb** and **Shear** in Inter-object data window. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to exit the Inter-object data window. Click on ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) to apply the same friction conditions defined for the selected relation to all other relations in the list, see [Fig. 2DCCDL1.32.](2d_cartridge_case_drawing_lab.htm#Fig_2DCCDl1_32_Defining_contact_conditions_for_Stage_2) Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to navigate to Stopping controls page to define stopping controls.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image032.jpg' | relative_url }})

Defining contact conditions for Stage 2

### Stopping controls for Station2

In Stopping controls page, we will define stopping plane as stopping criteria. Click on **Stopping****plane** tab, turn on Defined checkbox and define origin as (**0** ,**-0.1**) and vector as (**0** ,**-1**) see [Fig. 2DCCDL1.33.](2d_cartridge_case_drawing_lab.htm#Fig2DCCDL1_33_Stopping_plane_stopping_criteria_for_Station2) Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to navigate to Step page to define simulation step controls.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image033.jpg' | relative_url }})

Stopping plane stopping criteria for Station2

### Step Controls for Station2

In Steps page, define **Number of Steps** as **10000** , **Step increment to save** steps into database as **10** and **Die displacement per step** as **0.001**. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Generate DB page, since database will be generated during runtime after completion of the Station1 simulation for a batch mode operation setup, we will click on ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) to setup Station3.

## Station3

Change the operation name to "**Station3** " for the 3rd Forming operation in Operation editor tab as done in previous operations setup by double clicking on the operation name and press Enter in Keyboard after editing the operation name. 

Similar to Station2 for Station3, we will change the Die, Punch and Ejector geometries, and initialize the Strain, Damage and Velocity of the Workpiece to 0 as the Workpiece will undergo strain relaxation between the forming operations.

### Select Geometry Type and Simulation modes

Keep the **2D Axisymmetric** radio button selected as geometry type and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue to Simulation controls page. In Simulation controls page, uncheck the Heat transfer mode check box as shown in Fig. 2DCCDL1.4\. of Station1 and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Workpiece page as we do not need any additional objects to be added to the Objects list for this operation.

### Workpiece 

#### Workpiece object type definition

We can notice that Object type of the Workpiece is Read from DB, the Workpiece object data will be read from the last step of the previous operation. We will keep the Workpiece as Read from DB. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Workpiece Properties page.

#### Setting Limiting strain rate value for Workpiece

We will turn on **Redefine** **Strain****rate** checkbox and **Limiting** as ‘**0.001** ’, see [Fig. 2DCCDL1.34.](2d_cartridge_case_drawing_lab.htm#Fig_2DCCDL1_34_Redefining_Limiting_Strain_rate_for_Workpiece) Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Initialize page to initialize Workpiece conditions.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image034.jpg' | relative_url }})

Redefining Limiting Strain rate for Workpiece

#### Initializing Workpiece conditions

In Initialize page, turn on Strain, Damage, Velocity checkboxes and define value as ‘**0** ’ so that we can take into account the strain relaxation of the Workpiece, see [Fig. 2DCCDL1.35.](2d_cartridge_case_drawing_lab.htm#Fig_2DCCDL1_35_Initializing_Workpiece_conditions_in_Station3) Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Punch object page.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image035.jpg' | relative_url }})

Initializing Workpiece conditions in Station3

### Punch

#### Punch object type definition

We need to change the Punch geometry for the Station3, hence change the Object type from Read from DB to **Rigid** , see [Fig. 2DCCDL1.36.](2d_cartridge_case_drawing_lab.htm#Fig_2DCCDL1_36_Punch_object_page_Station3) Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Punch Geometry page.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image036.jpg' | relative_url }})

Punch object page Station3

#### Changing Punch Geometry

In Punch Geometry page, import the file “**Punch3.geo** ” by browsing the geometry file path located in DEFORM installation folder \2D\LABS\Cartridge_Lab directory, see [Fig. 2DCCDL1.37.](2d_cartridge_case_drawing_lab.htm#Fig_2DCCDL1_37_Punch_geometry_for_Station3) Check the geometry using ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) option to make sure the geometry is OK. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until we reach Punch movement page.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image037.jpg' | relative_url }})

Punch geometry for Station3

#### Assign Movement to Punch in Station2

The default mode is constant speed. Input a value of **10** in/sec for the Constant value and confirm that the Direction is **-Y**. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Die object page.

### Die

#### Die object type definition

We need to change the Die geometry for the **Station3** , hence change the Object type from Read from DB to **Rigid**. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Die Geometry page.

#### Changing Die Geometry

Click the ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Load geometry from a file) button and import the file “**Die3.geo** ” by browsing the geometry file path located in DEFORM installation folder \2D\LABS\Cartridge_Lab directory, see Fig. 2DCCDL1.38\. Check the geometry using ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) option to make sure the geometry is OK. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Ejector object page.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image038.jpg' | relative_url }})

Die geometry for Station3

### Ejector

#### Ejector object type definition

We need to change the Ejector geometry for the Station3, hence change the Object type from Read from DB to **Rigid**. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Ejector Geometry page.

#### Changing Ejector Geometry

Click the ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) (Load geometry from a file) button and import the file “**Ejector3.geo** ” by browsing the geometry file path located in DEFORM installation folder \2D\LABS\Cartridge_Lab directory, see [Fig. 2DCCDL1.39.](2d_cartridge_case_drawing_lab.htm#Fig_2DCCDL1_39_Ejector_geometry_for_Station3) Check the geometry using ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) option to make sure the geometry is OK. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Scheduled positioning page.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image039.jpg' | relative_url }})

Ejector geometry for Station3

### Scheduled Positioning

Similar to Station2, we will use Schedule positioning for Station3. Add schedule positioning of interference for **Workpiece** with **Die** as Reference object in**-Y** direction. Add item of interference positioning **Punch** with **Workpiece** as Reference object in **-Y** direction. We can observe the scheduled positioning sequence as shown in [Fig. 2DCCDL1.40.](2d_cartridge_case_drawing_lab.htm#Fig_2DCCDL1_40_Scheduled_positioning_definition_for_Station3) Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to navigate to Contact page to define contact conditions.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image040.jpg' | relative_url }})

Scheduled positioning definition for Station3

### Defining Contact conditions and scheduling contact generation for Station3

Similar to Station 2, we will schedule the contact generation for Station3, turn on the checkboxes Initialize and Generate to initialize contacts and then generate new contacts, see [Fig. 2DCCDL1.41.](2d_cartridge_case_drawing_lab.htm#Fig_2DCCDL1_41_Defining_contact_conditions_for_Stage_3) ssign the default inter-object relationships using ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) button. Click on the ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) button for one of the relationships. Select **Hybrid** type friction radio button in **Deformation** tab, define **0.1** value for both **Coulomb** and **Shear** in Inter-object data window. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to exit the Inter-object data window. Click on ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) to apply the same friction conditions defined for the selected relation to all other relations in the list, see [Fig. 2DCCDL1.41.](2d_cartridge_case_drawing_lab.htm#Fig_2DCCDL1_41_Defining_contact_conditions_for_Stage_3) Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to navigate to Stopping controls page to define stopping controls.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image046.jpg' | relative_url }})

Defining contact conditions for Stage 3

### Stopping controls for Station3

In Stopping controls page, click on **Stopping****plane** tab, turn on **Defined****checkbox** and define origin as (**0,-0.25**) and vector as (**0** ,**-1**) see [Fig. 2DCCDL1.42.](2d_cartridge_case_drawing_lab.htm#Fig_2DCCDL1_42_Stopping_plane_stopping_criteria_in_3rd_operation) Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to navigate to Step page to define simulation step controls.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image041.jpg' | relative_url }})

Stopping plane stopping criteria in 3rd operation

### Step Controls for Station3

In Steps page, define **Number of Steps** as **10000** , **Step increment to save** steps into database as **10** and **Die displacement** per step as **0.001**. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Generate DB page, since database will be generated during runtime after completion of the Station2 simulation for a batch mode operation setup, we will now run the simulation.

## Running Simulation

Switch to the Simulation mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the operation tree. Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in [Fig. 2DCCDL1.43.](2d_cartridge_case_drawing_lab.htm#Fig_2DCCDL1_43_Run_Simulation_popup_window) Use the default **Continue Run** option to select “**Continue from the last step** ” option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image042.jpg' | relative_url }})

Run Simulation popup window

## Post Processing 

Once the simulation is completed, the DB will be moved to Finished in Simulation tab and in Log file we can observe the message as “Multiple operations completed.”. We can now switch to the **Post mode** by clicking on the ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) button to view the simulation results. In Post, Step browser below the graphic area indicates step numbers available from the different operations simulated see [Fig. 2DCCDL1.44.](2d_cartridge_case_drawing_lab.htm#Fig_2DCCDL1_44_Step_list_page) A set of state variables available from the ‘**Post** ’ menu can be used review the model response, see [Fig. 2DCCDL1.45.](2d_cartridge_case_drawing_lab.htm#Fig_2DCCDL1_45_Damage_results_at_last_step_of_last_operation) shows Damage state variable distribution at the last step of Station 1, Station 2 and Station 3. [Fig. 2DCCDL1.46.](2d_cartridge_case_drawing_lab.htm#Fig_2DCCDL1_46_Strain_effective_results_at_last_step_of_last_operation) shows Effective strain state variable distribution at the last step of Station 1, Station 2 and Station 3. [ Fig. 2DCCDL1.47.](2d_cartridge_case_drawing_lab.htm#Fig_2DCCDL1_47_Stress_effective_results_at_last_step_of_last_operation) shows Effective stress state variable distribution at the last step of Station 1, Station 2 and Station 3.

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image047.jpg' | relative_url }})

Step list in Post processor

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image043.jpg' | relative_url }})

Damage results at last step of last operation

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image044.jpg' | relative_url }})

Strain effective results at last step of last operation

![]({{ '/assets/images/labs/forming_labs/2d_cartridge_case_drawing_lab/image045.jpg' | relative_url }})

Stress effective results at last step of last operation

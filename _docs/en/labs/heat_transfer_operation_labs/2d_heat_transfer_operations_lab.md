---
lang: en
title: "2D Heat Transfer Operations Lab"
---

# 2D Heat Transfer Operations Lab

This lab will demonstrate how to setup a typical multiple operation simulation involving different heat transfer and forging operations. During this lab we will also attempt to highlight various features of the system that user can include in other type of multiple operation situations. These operations can be a set of heat resting operation (see Fig. 2DHTRL1.1.), a set of deformation operations with changing dies between operations, or a combination of both heat transfer and deformation operations (see Fig. 2DHTRL1.1..). The model is 2D axisymmetric and the following 3D images are used for illustration purpose only.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0001.jpg' | relative_url }})

3D illustration of Heat Resting and Forming operations

In this lab, we setup a four operations model involving one ‘Heat Furnace’, ‘Heat Transfer', ‘Heat Resting’ one ‘Deformation’ and Heat Dwelling operations. The part is cylindrical workpiece, which first undergoes a furnace heating operation for one hour at 2000 F, followed by a heat transfer operation for 15 seconds during the transfer from the furnace to the forming station. This operation will be followed by a heat resting operation where the workpiece rests on forming dies for 4 seconds prior to a deformation operation. Deformation operation runs for a specific stroke of (7.25”) the upper die. Finally Dwelling operation for 4 seconds. The entire sequence can be setup using this system and all the operations can be simulated without user intervention in batch mode.

1.1. Creating New Problem and Adding Operations

1.2. Operation1: Furnace Heating Setup

1.3. Operation2: Air Transfer

1.4. Operation3: Heat Resting

1.5. Operation4: Forming

1.6. Operation5: Heat Dwelling

1.7. Simulate problem

1.8. Post Processing

## Creating New Problem and Adding Operations

### Creating New Problem

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2.) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear. 

Create a new problem either by selecting **File** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in Fig. 2DHTRL1.2. Select "**Integrated Manufacturing Process** " radio button and unit system as "**English** " radio button in unit field. Define Problem Name as " ******Heat_Transfer_Operations** " and make sure the “Show option dialog” check box is turned on (if we do not turn on the “**Show option dialog** ” check box, then we will not get the New Project dialog in MO UI). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

New Problem Popup

MO wizard will open, along with project naming window (see Fig. 2DHTRL1.3.), defined problem name is updated as ‘**Heat_Transfer_Operations** ’ as the project name and selected unit system updated. User can also change the Unit system and add operation by selecting from First operation pull down list and checkbox (see Fig. 2DHTRL1.3.). Using Copy Existing project option we can import previous saved projects as new project. Select the **F****irst operation** as **2D Heat transfer** operation and check the check box to add Heat transfer operation as first operation. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0003.jpg' | relative_url }})

MO Wizard New Project Opening Window

### Adding other operations

Multiple Operation wizard will opens new project with one 2d Heat transfer operation. Add two more heat transfer operations for Air transfer and Resting, one Forming operation and heat transfer operation for Dwelling after forming from Explorer Operations list clicking ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button as shown in Fig. 2DHTRL1.4.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0004.jpg' | relative_url }})

Adding Operations

## Operation1: Furnace Heating Setup

For first heat transfer operation change the operation name as "**Furnace Heating** " by double clicking on Operation name in Operation Editor window as shown in Fig. 2DHTRL1.5. and press **Enter** in Keyboard.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0005.jpg' | relative_url }})

Name the first operation as Furnace Heating

### Select Geometry Type

In this lab we are using Axisymmetric geometries, so activate **2D Axisymmetric** radio button in geometry type window as shown in Fig. 2DHTRL1.4., then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

### Select Heat Transfer Type for Furnace Heating

Select **Heat in Furnace** heat transfer type for Furnace heating operation as shown in Fig. 2DHTRL1.6. This will set the default heat transfer settings for heating operation. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0006.jpg' | relative_url }})

Heat transfer type selection for Furnace Heating

### Set Process Conditions for Furnace Heating

Define Heating time as **3600** sec (one hour of heating) at **2000** °F furnace temperature or environment temperature as shown in Fig. 2DHTRL1.7. and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0007.jpg' | relative_url }})

Process Condition settings for Furnace Heating

### Select Simulation Controls for Furnace Heating

Keep only Heat Transfer mode checked as only heat transfer is modeling as shown in Fig. 2DHTRL1.8. and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0008.jpg' | relative_url }})

Simulation Controls settings for Furnace Heating

### Import Workpiece Material

In Material window, load the material **AISI-8620** from DEFORM Material library, from **Steel** category using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load material data from library) option. This can be done as shown in Fig. 2DHTRL1.9. by clicking ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}) button. Material can also be load from Materials list in Explorer. Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) for Material list page.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0009.jpg' | relative_url }})

Importing Workpiece material from DEFORM library

### Check Material properties

In Material **AISI-8620** page to check the thermal material properties, select **Thermal** tab (see Fig. 2DHTRL1.10.) and click on ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) (Define) button next to Thermal Conductivity to observe the Thermal conductivity function of temperature as shown in Fig. 2DHTRL1.11.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0010.jpg' | relative_url }})

Material property definition window for AISI-8620

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0011.jpg' | relative_url }})

Thermal Conductivity function of temperature data for AISI-8620

Similarly click on ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) (Define) button next to Heat capacity and observe the function data as shown in Fig. 2DHTRL1.12.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0012.jpg' | relative_url }})

Heat capacity function of temperature data for AISI-8620

For Emissivity and Mass density constant value is defined as shown in Fig. 2DHTRL1.10. Then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) for Material properties and Object window, as only Workpiece object is enough heating operation.

### Define Workpiece

In Workpiece object window keep the object type as ‘**Plastic** ’ (see Fig. 2DHTRL1.13.). At this stage user can also specify initial temperature of the workpiece as **68°** F. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue and import the workpiece geometry.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0013.jpg' | relative_url }})

Workpiece Object definition

### Import Workpiece Geometry

In Geometry page, click on ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) ( Load Geometry from Library) button and import ‘**Disk_wkp****.****igs** ’ as shown in Fig. 2DHTRL1.14. Other options available at this stage are defining the workpiece from the Primitive geometry and 2D geometry Editor using ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) and ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}) options. Click ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}) If System ask the 2D\LABS\ location to be saved as library location.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0014.jpg' | relative_url }})

Import geometry from DEFORM library

Once the geometry is imported click on ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) option to check and correct the imported geometry if required (see Fig. 2DHTRL1.15.). Depending upon the imported geometry type, after clicking on ‘Check & Correct Geometry’ makes sure that the object boundary mark (shaded region next to the boundary) remains inside the boundary. If the system fails to correct the geometry choose among the options ‘System detects’, ‘Closed’ and ‘Open’ to correct the geometry.

If the geometry orientation is not correct, the system attempts to correct the same during the meshing stage, but it is recommended to check and correct the object geometry as and when we import the same. This procedure remains the same any time we need to import the object geometry. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0015.jpg' | relative_url }})

Geometry checking and correcting

### Generate Workpiece Mesh

Generate the mesh using 2000 elements (see Fig. 2DHTRL1.16.). Complete range of meshing options are also available in expert mode (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})), if user needs to have more control on the mesh generated. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0016.jpg' | relative_url }})

Mesh generation window

### Assign Workpiece Material

To assign material for workpiece select the material ‘**AISI****-8620** ’ from material window. This can be done as shown in Fig. 2DHTRL1.17. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0017.jpg' | relative_url }})

Object material selection window

### Define Workpiece Boundary Conditions

In BCC page, check the default assigned Heat exchange with Environment BCC to the entire outer surface of the Billet (which does not include the centerline since these nodes are inside the object) by clicking on Defined under Heat exchange with Environment. Default BCC are assigned automatically due to selection of problem type as axisymmetric (see Fig. 2DHTRL1.18.).

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0018.jpg' | relative_url }})

Boundary condition definition for Furnace Heating

Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Step controls window as there is no object positioning and Thermal stopping controls definition is required.

### Define Step Controls for Furnace Heating

Set the **number of simulation steps** as **100** at **36** sec each and saving every **10** **steps**(see Fig. 2DHTRL1.19.). Advanced Simulation controls settings are available in expert mode (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to proceed to the database generation stage.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0019.jpg' | relative_url }})

Simulation controls settings for Furnace Heating

### Generate Database

In the database generation stage user can check the data required for the analysis and proceed to generate the database (see Fig. 2DHTRL1.20.). First operation of any multiple operations, user is required to generate the database. For all the subsequent operations we only need to setup the process data and simulation controls. At this stage user also has an option of importing a keyword file, which is particularly useful for the later operations. Functionality of this feature of ‘Append user defined keyword file’ will be discussed in the later sections of this lab. Click on ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) to proceed to the next operation of ‘Air Transfer’.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0020.jpg' | relative_url }})

Database Generation window for first operation

## Operation2: Air Transfer

In this operation we setup a heat transfer to air stage of the operation involving a 15 sec transfer time of the part from furnace to the forming station. During this time the part which is at about 2000°F undergoes some cooling in ambient air.

### Select Heat Transfer Type for Air Transfer

Name the operation as "**Air Transfer** " by double clicking on Operation name in Operation Editor and press Enter from Keyboard to close. Select '**Transfer through air** ' heat transfer type as shown in Fig. 2DHTRL1.21. and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0021.jpg' | relative_url }})

Heat Transfer type selection for Air Transfer

### Set Process Conditions for Air Transfer

Define the process conditions as **transfer time** of **15** sec in a **68** °F environment using the default convection coefficient as shown in Fig. 2DHTRL1.22.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0022.jpg' | relative_url }})

Process condition settings for Air Transfer

Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Workpiece object window and accept object type as ‘Read from DB’ (see Fig. 2DHTRL1.23.). This indicates that workpiece thermal history from the furnace heating operation will be available as a starting data for this operation. Click on Step controls branch in operation tree.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0023.jpg' | relative_url }})

Read from DB object selection for workpiece

### Set Step definition for Air Transfer

In Step Controls window define **15** steps at **1** sec increment and saving at every**5** steps (see Fig. 2DHTRL1.24.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0024.jpg' | relative_url }})

Step controls settings for Air Transfer

Click on ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) to open the Heat resting operation (see Fig. 2DHTRL1.25.), as database will generate for subsequent operations during simulation in batch mode.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0025.jpg' | relative_url }})

Database generation window for subsequent operations in batch mode

**Note** :

At this stage user has an option to bring in additional object or simulation data by opting to ‘Append user defined keyword file’ (see Fig. 2DHTRL1.22.). Please not that, this keyword when defined will be read in by the system before the DB generation of the second operation. However no checking of the user defined data from this keyword file will be done at this stage.

## Operation3: Heat Resting

In this operation we setup a heat transfer where the workpiece rests on forming dies for 4 seconds prior to a deformation operation.

### Select Heat Transfer Type for Heat Resting

Name the operation as "**Heat Resting** " by double clicking on Operation name in Operation Editor and press Enter from Keyboard to close. Select '**Rest on die** ' heat transfer type as shown in Fig. 2DHTRL1.26. and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0026.jpg' | relative_url }})

Heat transfer type selection for heat resting operation

### Set Process Condition for Heat Resting

Set process condition as **resting****time** of **4** sec in a 68°F environment using the default convection coefficient as shown in Fig. 2DHTRL1.27. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0027.jpg' | relative_url }})

Process condition settings for Heat Resting operation

### Add Die Objects

Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Object window and accept the ‘Number of Objects’ as 3 as the total number of objects, as we will be bringing in both the dies at 300°F for the resting operation. We can now see the object tree is expanded to include both the dies, details for which will be now be defined.

### Define Top Die

Click on Top Die in operation tree to define the Dies. Accept the Top Die temperature 300°F and Object type as rigid as shown in Fig. 2DHTRL1.28. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0028.jpg' | relative_url }})

Top die object definition window for heat resting operation

### Import Top Die Geometry

In Top die Geometry window, click on ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load Geometry from Library) button and import ‘**Disk_top****.igs** ' as shown in Fig. 2DHTRL1.29.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0029.jpg' | relative_url }})

Importing the top die geometry from DEFORM Library

### Generate Top Die Mesh

Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) and generate mesh using 600 elements as shown in Fig. 2DHTRL1.30. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to material page.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0030.jpg' | relative_url }})

Generating mesh for Top die

### Import Material for Dies

Load the material **AISI-H13** from DEFORM Material library, from **Die_material** category using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load material data from library) option as shown in Fig. 2DHTRL1.31. Select the loaded material to assign it to the Top Die.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0031.jpg' | relative_url }})

Loading Die material from DEFORM library

### Define Top Die BCC

In the ‘Define BCC’ window, ‘Heat Exchange with Environment’ BCC automatically assigned to the all sides excluding axis side. Click on Defined branch under Heat Exchange with Environment BCC to confirm the BCC definition (see Fig. 2DHTRL1.32.). Click on Bottom Die branch in operation tree to lower die.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0032.jpg' | relative_url }})

Heat exchange with Environment BCC for top die

### Define Bottom Die

For Bottom die also accept 300°F Object temperature and Rigid object type. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

### Import Bottom Die Geometry

In Bottom die geometry window, click on ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load Geometry from Library) button and import ‘**Disk_btm****.igs** ' as shown in Fig. 2DHTRL1.33. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to mesh page.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0033.jpg' | relative_url }})

Loading Bottom die geometry from DEFORM library

### Generate Bottom Die Mesh

Generate mesh using 600 elements as shown in Fig. 2DHTRL1.34.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0034.jpg' | relative_url }})

Generating mesh for bottom die

### Assign Material for Bottom Die

Select **AISI-H13** material from material list to assign it to the Bottom Die. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Boundary condition.

### Define Bottom Die BCC

Confirm the automatically assigned Heat Exchange with Environment BCC to all sides excluding axis side by clicking on Defined under Heat exchange with Environment BCC as shown in Fig. 2DHTRL1.35. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until positioning page.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0035.jpg' | relative_url }})

Heat exchange with Environment BCC for bottom die

### Position Top Die

Now from the ‘Positioning’ enter the ‘Positioning objects’ menu where we first move the top die away from the workpiece so that heat resting accounts for the heat transfer between workpiece and bottom die.

To accomplish this first click on ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) button. Select the top die,‘**Offset** ’ method and distance vector as (x=0, y=4). Click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) will move the top die away from the workpiece. (see Fig. 2DHTRL1.36.)

Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the ‘Object Positioning window. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define scheduled position the bottom die.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0036.jpg' | relative_url }})

Positioning Top die in resting operation

### Schedule Position Bottom Die

As Bottom die we need to position with respect to Read from DB object Workpiece, so we have to schedule position during DB generation. Click on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Add) button and select the ‘Positioning object’ as bottom die, method as ‘Interference’ with respect to ‘Workpiece’ in the **+Y** direction (see Fig. 2DHTRL1.37.). Note that positioning details added in the scheduled positioning will be accounted prior to inter object data generation for this operation. No physical movement of the dies will be seen at this point. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0037.jpg' | relative_url }})

Scheduled positioning Bottom die With respect to workpiece

### Schedule Inter-Object Contact Relationships for Heat Resting

Select **User** type contact and click on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Add relationship) button and select Bottom die as Master and Workpiece as Slave as shown in Fig. 2DHTRL1.38.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0038.jpg' | relative_url }})

Inter-object relationship between workpiece and bottom die

Click on ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) (Edit) relationship button and select the pull down option " **Free Resting** " in the thermal section to define the inter-object heat transfer coefficient as shown in Fig. 2DHTRL1.39. Click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the Editing window. It will generate the inter-object contact at the beginning of the resting operation while simulating. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until step controls window.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0039.jpg' | relative_url }})

Inter-object Heat transfer coefficient selection for resting

### Define Step controls for Heat Resting

In Step Controls window select **number of steps** as **10** , with**0.4** sec each and saving every **second** step (see Fig. 2DHTRL1.40.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Generate DB window and click on ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) from Database generation window to continue defining Forming operation.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0040.jpg' | relative_url }})

Step controls for heat resting operation

## Operation4: Forming

The Forming operation runs for a specific stroke of (7.25”) the upper die. As we are making all objects as read from DB, objects data will come from previous operations, with thermal history. So pass the all objects from Heat resting operation to Forming operation as shown in Fig. 2DHTRL1.41.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0041.jpg' | relative_url }})

Passing objects to read from DB

### Select Simulation Modes for Forming

Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) for Geometry type window and accept the Simulation controls default Simulation modes selected (Deformation and Heat transfer) as shown in Fig. 2DHTRL1.42. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until object window.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0042.jpg' | relative_url }})

Simulation controls settings for Forming operation

In objects page confirm all objects data type as Read from DB and with no movement defined, click on Top Die- Movement branch from operation to define top die movement controls.

### Define Top Die Movement Controls

For the top die assign a constant die movement of **1** in/sec in the negative 'Y’ direction as shown in Fig. 2DHTRL1.43. (Click preview object movement icon to view the movement of the top die, if the Step increment is defined).

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0043.jpg' | relative_url }})

Movement controls for Top die

### Schedule Position Top Die

Click on Scheduled positioning branch in operation tree to define the positioning for Top die. Now click on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Add) button and select the ‘Positioning object’ as top die, method as ‘Interference’ with respect to ‘Workpiece’ in the -Y direction (see Fig. 2DHTRL1.44.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0044.jpg' | relative_url }})

Scheduled positioning for Top die in forming operation

### Schedule Inter-Object Contact Relationships for Forming

Select user type contact and click on ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) button. It will add the relationship between the Billet, Top Die and Bottom Die (see Fig. 2DHTRL1.46.). As the Dies are Rigid and Billet is plastic, Top and Bottom Dies are considered as Master and Billet as Slave. In order to predict the fold during deformation, self contact will be assigned for Billet.

Highlight the **Top Die – Billet** relationship and click the ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) button to modify the contact conditions. In the friction section of the screen (see Fig. 2DHTRL1.45.), there is a pull-down menu that allows the user to choose the appropriate friction conditions of common forming processes.

Since this is hot forming simulation and the dies are steel, use the pull down menu and select **Hot forming (lubricated)** from the list. A friction value of **0.3** will automatically be selected.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0045.jpg' | relative_url }})

Inter-object friction coefficient definition window

Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to go back to Inter-Object window, Since the friction conditions are the same for all the object pairs, the ![]({{ '/assets/icons/pre_icons/mo_apply_to_all_button.jpg' | relative_url }}) button can be used to copy the interface properties from the first relationship to all of the others. After this is done, all relationships will have a friction of 0.3 defined as shown in Fig. 2DHTRL1.46. Since the contact will initialize and generate while generating database. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to continue.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0046.jpg' | relative_url }})

Inter-Object relationship definition for forming operation

### Define Stopping Control for Forming

In stopping control window check the Max. die stroke stopping control and define **primary die displacement** as (0,7.25) as shown in Fig. 2DHTRL1.47. Advanced stopping options are available in Expert mode (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to define the step controls.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0047.jpg' | relative_url }})

Die stroke stopping control for forming operation

### Define Step Controls for Forming

In step controls window define **number of steps** as **100** , at **0.0725** ” per step of die movement, step increment to save as **10** for the primary die (which is object number 2 in this simulation) as shown in Fig. 2DHTRL1.48.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0048.jpg' | relative_url }})

Step controls settings for forming operation

Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) and click on ![]({{ '/assets/icons/pre_icons/mo_next_opr_button.jpg' | relative_url }}) button to continue define the Heat Dwelling operation.

## Operation5: Heat Dwelling

Heat dwelling is nothing but heat transfer after the deformation operation for a particular time and the corresponding time is called heat dwelling time or simply dwell time.

### Select the Heat Transfer Type for Heat Dwelling

Name the Operation as **Heat Dwelling** and select the **Dwell on die** heat transfer type radio button as shown in Fig. 2DHTRL1.49.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0049.jpg' | relative_url }})

Heat transfer type for Heat Dwelling operation

### Set Process Condition for Heat Dwelling

Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) and accept the **Dwell****time** of **4** sec in Environment temperature **68** °F and default Convection coefficient as shown in Fig. 2DHTRL1.50.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0050.jpg' | relative_url }})

Process condition settings for Heat Dwelling operation

The default data is set for all the objects are read from DB (coming from the previous operations, along with thermal history). Accept the default conditions for the objects and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to proceed until Contact (Inter-Object Contact) window.

### Schedule Inter-Object Contact Relationships for Heat Dwelling

Select **user** type contact and click on ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) button. Highlight the **Top Die – Billet** relationship and click the ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) button to modify the contact conditions. Select the pull down option " **Free Resting** " in the thermal section to define the inter-object heat transfer coefficient as shown in Fig. 2DHTRL1.37.

Click on ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) button and click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the Editing window (see Fig. 2DHTRL1.51.). It will generate the inter-object contact during database generation. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until step controls window.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0051.jpg' | relative_url }})

Inter-object contact relationship for heat dwelling operation

### Define Step Controls for Heat Dwelling

In Step Controls window select number of steps as **10** , with **0.4** sec each and saving every **second** step (see Fig. 2DHTRL1.52.). This completes the multiple operations with all heat transfer operations setup, so to simulate the problem switch to Simulation tab above the object tree.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0052.jpg' | relative_url }})

Step controls for heat dwelling operation

## Simulate problem

Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. 2DHTRL1.53. Use the default **Continue Run** option to select “**Continue from the last step** ” (from step -1) option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0053.jpg' | relative_url }})

Run Simulation popup window

Monitor the progress of the simulation by looking at the Simulation Graphics, Simulation Message and Simulation Log tab, making sure that the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked. (see Fig. 2DHTRL1.54.)

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0054.jpg' | relative_url }})

Simulation mode displaying the furnace heating running status

After completion of the all multiple operation in Simulation log file it gives the log message as "MULTIPLE OPERATION COMPLETED.", then switch to Post tab to view the simulation results.

## Post Processing

In post processor Step list below the graphic area indicates step numbers available from the different operations simulated. A set of state variables available from the ‘Post’ menu can be used review the model response. Please note that for the first two operations only the thermal data for the workpiece is available as the dies are introduced from the third operation. And the deformation results can be seen for the Deformation operation (see Fig. 2DHTRL1.55.)

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0055.jpg' | relative_url }})

MO Post processor after simulating all operations

Some important state variables can be selected directly from ‘Post’ and the rest can be accessed through State Variable dialog by clicking on ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) icon. (see Fig. 2DHTRL1.56.)

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0056.jpg' | relative_url }})

Temperature plot for all objects at the end of multiple operations

Plot **Temperature** state variable and play the steps from first operation to observe the heat transfer in workpiece and dies from Furnace heating to Heat dwelling operation as shown in Fig. 2DHTRL1.57.

![]({{ '/assets/images/labs/heat_transfer_operation_labs/2d_heat_transfer_operations_lab/image0057.jpg' | relative_url }})

Hat transfer in objects from furnace heating to heat dwelling operation

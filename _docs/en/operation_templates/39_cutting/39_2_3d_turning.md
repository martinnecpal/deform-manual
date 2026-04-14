---
lang: en
title: "39.2. 3D Turning"
---

# 39.2. 3D Turning

39.2.1. How to add 3D Cutting Operation

39.2.2. System Summary

39.2.3. Adding Turning Operation

39.2.4. Process

39.2.5. Material List

39.2.6. Tool

39.2.6.1. Insert Geometry

39.2.6.2. Tool Holder

39.2.6.3. Coating Material

39.2.6.4. Tool material

39.2.6.5. Tool Mesh

39.2.6.6. Tool BCC

39.2.7. Workpiece

39.2.7.1. Workpiece Geometry

39.2.7.2. Workpiece Material Selection

39.2.7.3. Workpiece Mesh Generation

39.2.7.4. Workpiece BCC

39.2.8. Control

39.2.9. Tool Wear

39.2.10. Contact

39.2.11. Step control

39.2.12. Generate DB

## How to add 3D Cutting Operation

3D Cutting operation can be setup in Integrated Manufacturing Process environment that can be accessed from GUI Main. Create a new problem by either selecting “File ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) New Problem” or by clicking the “New Problem” ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. Select “3D Cutting” radio button under problem type and unit system. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button as shown in Fig. 39.2.1. Integrated Manufacturing Process wizard will open, we can see that 3D Cutting operation is added in Operation editor.

![]({{ '/assets/images/operation_templates/39_cutting/39_2_3d_turning/image0001.jpg' | relative_url }})

Adding 3D Cutting Operation from GUI Main

We can also add “3D Cutting” operation by clicking the “New Problem” ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. Select Integrated Manufacturing Process and unit system. Integrated Manufacturing Process window will be opened with “New Project” popup. In “New Project” popup, we can add “3D Cutting” operation by checking the check box of “First operation” and selecting “3D Cutting” as first operation from pull down list as shown in Fig. 39.2.2. Then click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) in New project window. Integrated Manufacturing Process wizard will open and in “Operation Editor” we can observe “3D Cutting” operation added in Operation editor. Using copy Existing project option, we can import previous saved projects as new project.

![]({{ '/assets/images/operation_templates/39_cutting/39_2_3d_turning/image0002.jpg' | relative_url }})

Assign Project name and First Operation selection in New Project window

  
We can also add “3D Cutting” operation to “Operation Editor” from explorer tab, by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button next to 3D Cutting as shown in Fig. 39.2.3 or by drag and drop 3D Cutting into operation editor window, process selection page will be opened in property settings modification area.

![]({{ '/assets/images/operation_templates/39_cutting/39_2_3d_turning/image0003.jpg' | relative_url }})

Adding operation from Explorer Operation list

#### 3D Cutting Types:

In this operation we are having the 4 different types of cutting models they are

  1. Turning

  2. Milling

  3. Boring

  4. Drilling

## System Summary

3D Cutting template can be used to model the industrial turning process, without any assumptions that are associated with orthogonal cutting conditions. These modeling procedures enable the engineer to study the process response for any change in process conditions. Cutting forces, cutting temperatures, chip shape, tool wear and tool life computations can be performed using this system. The engineer can study the effect of process parameters like, cutting speed, feed rate and depth of cut on the process response. The template simplifies the model definition and uses the same engineering language of process engineer. For turning applications, the rotating work piece, insert and their relation to the analysis domain are shown in Fig. 39.2.4. Typical analysis model generated using the current system is shown in Fig. 39.2.5. The main data requirements to model the machining process are material flow stress data for the work piece material and geometric data for the insert. The material flow stress data should cover the strain rate, strain and temperature range for metal cutting process. For most materials the typical range for strain rate is 0 - ~106/sec, the range for strain is 0 – 5 and the range for temperature is 20 – 1200°C. Special material characterizing techniques are required to address this range of loading conditions. The insert geometry can be made available in STL form, generated from any CAD system.

This document describes process data, loading the materials, inserts and tool holders from the library. By specifying the model specific data, user can generate complete data required for the analysis. This stage of analysis constitutes the initial transient analysis. After executing the simulation and sufficient chip has formed, user can compute the steady state response of the process which includes the prediction of steady state thermal response and chip geometry. From the viewpoint of insert thermal response this stage will significantly reduce the computing time that is normally associated with transient analysis. The results obtained from this stage form important input to the tool wear and tool life computations. The machining template comes with a set of library files for the insert geometry. User can also use any other insert geometry and save it along with the system library for any subsequent use. 

![]({{ '/assets/images/operation_templates/39_cutting/39_2_3d_turning/image0004.jpg' | relative_url }})

Basic components of turning and its relation to analysis domain

![]({{ '/assets/images/operation_templates/39_cutting/39_2_3d_turning/image0005.jpg' | relative_url }})

Simulation model and basic cutting parameters definition

## Adding Turning Operation

To set up Turning process user need to add the 3D cutting template and select “**Turning** ” option in the “Process” page as shown in Fig. 39.2.6.

## Process 

The process parameters that are required to model the turning process will be defined in process page, see Fig. 39.2.6.

  
**Cutting speed:** User can refer to System Summary to define these process parameters.

  * **Cutting speed (v):** It is defined as the speed at which the tool moves. The cutting speed can be defined as mm/sec or m/min in SI and in/sec or ft/min in English units.

  * **Rotation speed:** It defines the rotational speed of tool. The rotation speed can be defined in rpm and radians/sec.

  * **Workpiece diameter (D):** It defines the diameter of the workpiece. This diameter value gets updated in the workpiece geometry primitive page.

  * **Depth of cut (d):** It is the thickness of metal that is removed during machining. The perpendicular distance measured between the machined surface and the uncut surface of the workpiece.

  * **Feed rate (f):** It is defined as the distance the tool travels against the workpiece during one revolution of the workpiece. The tool position is determined by the feed rate. This can be defined as mm/rev or mm/sec in SI and in/rev or in/sec in English units.

![]({{ '/assets/images/operation_templates/39_cutting/39_2_3d_turning/image0006.jpg' | relative_url }})

Turning type process page

  
**Environment heat transfer** : The user can define the Temperature and Convection coeff. Data as shown in the Fig. 39.2.6. We can save and load the convection coefficient from library.

  * **Save to library![]({{ '/assets/icons/pre_icons/mo_save_to_library_button.jpg' | relative_url }})** : User can save the Convection coefficient to the library and can be used later in other simulations. We can also create the new category to save the Convection coefficient as shown in the Fig. 39.2.7.

![]({{ '/assets/images/operation_templates/39_cutting/39_2_3d_turning/image0007.jpg' | relative_url }})

Saving Coolant Coefficient to Library

  * **Load from library**![]({{ '/assets/icons/pre_icons/mo_load_from_library_button.jpg' | relative_url }}) : User can load the already saved Convection coefficient from the selected category as shown in the Fig. 39.2.8. Using the “Delete Category” user can delete the respective category and coolants data within it. If user wants to delete only coolant data, then using “Delete Coolant” the Convection coefficient from any category can be deleted. 

![]({{ '/assets/images/operation_templates/39_cutting/39_2_3d_turning/image0008.jpg' | relative_url }})

Loading Coolant Coefficient from Library

## Material List 

In this Material List page, user can load a material from the library or keyword or database file using the ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}), ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) options as shown in Fig. 39.2.9. The materials loaded here can be assigned to the objects from their respective material page. User can also add a new material using ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button and define its properties. User can use ![]({{ '/assets/icons/pre_icons/mo_delete_icon2.jpg' | relative_url }}) button to delete the loaded material. User can also save the material using ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}), ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}) options.

![]({{ '/assets/images/operation_templates/39_cutting/39_2_3d_turning/image0009.jpg' | relative_url }})

Assigning the Material to Material list

## Tool 

In this Tool page, the user can define the temperature of the tool object. We can import the tool object using the ![]({{ '/assets/icons/pre_icons/mo_import_object_button.jpg' | relative_url }}) button (see Fig. 39.2.10.). If user wants to calculate the thermal data for tool object, select the “**Calculate tool temperature** ” check box and we can observe that mesh options for tool are enabled so that we can mesh the tool to calculate temperature distribution.

![]({{ '/assets/images/operation_templates/39_cutting/39_2_3d_turning/image0010.jpg' | relative_url }})

Tool Page

### Insert Geometry 

In this Insert Geometry page, user can define the tool geometry using the ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) or import the geometry using the Import geometry options. (See Fig. 39.2.11). For more information please refer to [12.3. 3D Geometry Data Defining](/docs/en/pre_processor/12_geometry_modelling/12_3_3d_geometry_data_defining/).

![]({{ '/assets/images/operation_templates/39_cutting/39_2_3d_turning/image0011.jpg' | relative_url }})

Insert Geometry Page

#### Defining Tool Geometry using Define Primitive option

When user clicks on the ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) link in Insert geometry page, “Insert Primitive” window will open with basic tool inserts geometries as shown in the Fig. 39.2.12. Once the insert is identified user can check the basic parameters of this insert, base material and coating material if any, prior to loading the same.

**Parameter tab:** It will provide the geometric parameter data of the selected tool. User can also modify the provided parameters.

**Base Material tab:** It will show the Base material data of the tool selected from the list.

**Coating tab:** It will show the coating materials data of the tool selected from the list.

![]({{ '/assets/images/operation_templates/39_cutting/39_2_3d_turning/image0012.jpg' | relative_url }})

Insert Primitive Page

#### Defining Tool Geometry using Import geometry option

Click on ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) and import tool geometry. Select Cutting Face direction, by default " Y " is selected as shown in Fig. 39.2.13., click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). Now, select reference point as shown in Fig. 39.2.14. and click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). We will observe this cutting face selection template for positioning the insert only in turning process setup.

![]({{ '/assets/images/operation_templates/39_cutting/39_2_3d_turning/image0013.jpg' | relative_url }})

Cutting face axis selection for imported geometry

![]({{ '/assets/images/operation_templates/39_cutting/39_2_3d_turning/image0014.jpg' | relative_url }})

Reference point selection for imported geometry

### Tool Holder 

For the selected insert, the corresponding tool holders can be loaded from the Tool Holder library, or user can define the tool holder by providing basic cutting angles as shown in Fig. 39.2.15. Basic cutting angles that are inherited from the tool holder data are **SCEA**(side cutting edge angle or the lead angle), **BR**(back rake angle) and **SR**(side rake angle). These basic angles and the process data (feed rate and depth of cut) control the correct position of the insert with respect to the work piece.

![]({{ '/assets/images/operation_templates/39_cutting/39_2_3d_turning/image0015.jpg' | relative_url }})

Tool Holder Page

### Coating Material 

User can apply coating to tool insert by defining coating layer and its thickness in “Coating Material” page. User can define the coating layer material and its thickness by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_icon.jpg' | relative_url }}) button as shown in the Fig. 39.2.16. If user wants to delete any layer then user has to select the respective layer and click on ![]({{ '/assets/icons/pre_icons/mo_delete_icon.jpg' | relative_url }}) button.

  
**Extract Coating Info:** After Generating the coating, we can extract the coating info using this button.

**Delete Coating:** We can also delete the Costing layers using this button. 

Using the “**Preserve state variables and boundary conditions** ” check box the user can create the coating layer without losing the state variable and boundary conditions data of the tool.

![]({{ '/assets/images/operation_templates/39_cutting/39_2_3d_turning/image0016.jpg' | relative_url }})

Coating Material Page

### Tool material 

In material page, all the materials added to material list are displayed as shown in Fig. 39.2.17. User can select the required material to assign it to respective object. If the desired material is not available in the list, then the user can load the material in object material page using “Import material” data from a File ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) or using “Load form Library” option ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}). User can also create new material if the material is not available in DEFORM library using ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}). User can delete the material from list using ![]({{ '/assets/icons/pre_icons/mo_delete_icon2.jpg' | relative_url }}) or edit the material data using ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}). Modified / newly defined material can be saved using ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}), ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}). 

![]({{ '/assets/images/operation_templates/39_cutting/39_2_3d_turning/image0017.jpg' | relative_url }})

Assigning the Tool Material

### Tool Mesh 

User can generate mesh for the tool by defining relative or absolute mesh size data as shown in the Fig. 39.2.18. & Fig. 39.2.19. It also provides the preview of the mesh when we click on ![]({{ '/assets/icons/pre_icons/mo_preview_mesh_button.jpg' | relative_url }}) option. Cutting edge information being part of the insert data, the wizard automatically applies finer mesh near the cutting zone. 

####   
**Relative Mesh Method**

  * **Target number of elements:** The number of elements to be generated for an object can be specified merely by adjusting the slider bar and selecting an appropriate value for the current simulation.

  * **Size Ratio:** It is the size ratio between the largest element edge length to smallest element edge length.

![]({{ '/assets/images/operation_templates/39_cutting/39_2_3d_turning/image0018.jpg' | relative_url }})

Tool Mesh Generation using relative mesh size

####   
Absolute Mesh Method

  * **Minimum element size:** Feed rate automatically calculates the minimum element size of the mesh to be generated which calculates the Target number of elements value automatically as shown in the Fig. 39.2.19.

![]({{ '/assets/images/operation_templates/39_cutting/39_2_3d_turning/image0019.jpg' | relative_url }})

Tool Mesh Generation using absolute mesh size

### Tool BCC 

In this BCC Page, the user can define the Thermal BCC like “Heat Exchange with Environment” and “Temperature”. The default BCC are assigned automatically after generating the mesh as shown in the Fig. 39.2.20.

![]({{ '/assets/images/operation_templates/39_cutting/39_2_3d_turning/image0020.jpg' | relative_url }})

Default Heat Exchange BCC

## Workpiece 

In this Workpiece page, the user can define the object type and set its initial temperature. Plastic object type is selected by default, if user is interested to consider the effect of elastic properties then Elasto-plastic object type can be used. We can also import the object data using the ![]({{ '/assets/icons/pre_icons/mo_import_object_button.jpg' | relative_url }}) button.

![]({{ '/assets/images/operation_templates/39_cutting/39_2_3d_turning/image0021.jpg' | relative_url }})

Workpiece Page

### Workpiece Geometry 

In this Workpiece Geometry page, the user can define the workpiece geometry using the ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) The user can also import the geometry using the Import geometry options ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}), ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}).

####   
Defining Workpiece Geometry using Define Primitive option

The ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) will open the ‘Workpiece Geo Primitive’ menu. In this menu we are having different geometry parameters for both simplified and curved mode as shown in the Fig. 39.2.22 and Fig. 39.2.23.

  * **Diameter(D):** For curved mode it will determine the diameter of the workpiece.

  * **Arc angle:** For curved mode it will determine the angle of the workpiece to generated.

  * **Length(L):** For simplified mode it will determine the length of the workpiece.

  * **Feed Amount:** It is defined as the distance the tool travels during one revolution of the workpiece and used to generate the workpiece primitive. The feed rate value which is defined in the process page will be automatically updated in the primitive page and can be modified only from process page.

![]({{ '/assets/images/operation_templates/39_cutting/39_2_3d_turning/image0022.jpg' | relative_url }})

Simplified mode workpiece geometry

![]({{ '/assets/images/operation_templates/39_cutting/39_2_3d_turning/image0023.jpg' | relative_url }})

Curved mode workpiece geometry

### Workpiece Material Selection

In material page, all the materials added to material list are displayed as shown in Fig. 39.2.24\. User can select the required material to assign it to respective object. If the desired material is not available in the list, then the user can load the material in object material page using “Import Material” data from a File ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) or using “Load form Library” option ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}). User can also create new material if the material is not available in DEFORM library using ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}). User can delete the material from list using ![]({{ '/assets/icons/pre_icons/mo_delete_icon2.jpg' | relative_url }}) or edit the material data using ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}). Modified / newly defined material can be saved using ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}),![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}) .

![]({{ '/assets/images/operation_templates/39_cutting/39_2_3d_turning/image0024.jpg' | relative_url }})

Assigning the material for the workpiece

### Workpiece Mesh Generation

The User can generate the mesh by defining relative or absolute mesh size data as shown in the Fig. 39.2.25 & Fig. 39.2.26\. It also provides the preview of the mesh when we click on ![]({{ '/assets/icons/pre_icons/mo_preview_mesh_button.jpg' | relative_url }}) option. For more information related to Expert mode Mesh option refer [13.2. 3D Tet Mesh Generation](/docs/en/pre_processor/13_mesh_generation/13_2_3d_tet_mesh_generation/).

  
**Relative Mesh Method**

  * **Target number of elements:** The number of elements to be generated for an object can be specified merely by adjusting the slider bar and selecting an appropriate value for the current simulation.

  * **Size Ratio:** It is the size ratio between the largest element edge length to smallest element edge length.

![]({{ '/assets/images/operation_templates/39_cutting/39_2_3d_turning/image0025.jpg' | relative_url }})

Workpiece mesh generation using relative mesh size

  
**Absolute Mesh Method**

  * **Define size by percentage of feed:** The percentage of feed will automatically calculate the minimum element size of the mesh.

  * **Minimum element size:** It sets the minimum element size of the mesh to be generated which is calculated from the percentage of feed value.

![]({{ '/assets/images/operation_templates/39_cutting/39_2_3d_turning/image0026.jpg' | relative_url }})

Workpiece mesh generation using absolute mesh size

### Workpiece BCC 

In this BCC Page, the user can define the Deformation and Thermal BCC (like Velocity, Heat Exchange with Environment and Temperature). The default BCC data will be automatically assigned after generating the mesh as shown in the Fig. 39.2.27, Fig. 39.2.28 and Fig. 39.2.29\. The Default BCC data will be same for the both curved and simplified geometries.

![]({{ '/assets/images/operation_templates/39_cutting/39_2_3d_turning/image0027.jpg' | relative_url }})

Velocity BCC data for Simplified geometry

![]({{ '/assets/images/operation_templates/39_cutting/39_2_3d_turning/image0028.jpg' | relative_url }})

Heat Exchange BCC for Curved geometry

![]({{ '/assets/images/operation_templates/39_cutting/39_2_3d_turning/image0029.jpg' | relative_url }})

Temperature BCC for Curved geometry

## Control

Using “Position objects” the tool can be positioned based on the feed rate and workpiece location. Various positioning options are available to position the objects as shown in Fig. 39.2.30, for more information on these options please refer [19\. Object positioning](/docs/en/pre_processor/19_object_positioning/19_object_positioning/). 

![]({{ '/assets/images/operation_templates/39_cutting/39_2_3d_turning/image0030.jpg' | relative_url }})

Object positioning options

## Tool Wear

User can turn on tool wear calculation using “Define model to calculate tool wear” check box. After turning on check box user can select the tool wear model and define its parameters as shown in the Fig. 39.2.31, for more information on these options please refer [20.4.Tool Wear](/docs/en/pre_processor/20_inter-object_data_definition/20_4_tool_wear/). 

![]({{ '/assets/images/operation_templates/39_cutting/39_2_3d_turning/image0031.jpg' | relative_url }})

Tool Wear page

## Contact

By default, user radio button will be selected and default relations also will be defined for 3D Cutting operation as shown in Fig. 39.2.32\. User can modify the value of each relation by selecting it and clicking on ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) button. User can click on ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) button to calculate contact tolerance. User can click on ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) to generate contact relation. User can turn on check box next to contact relation to define sticking contact.  
For more information please refer [20\. Inter-Object Relations](/docs/en/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/).

![]({{ '/assets/images/operation_templates/39_cutting/39_2_3d_turning/image0032.jpg' | relative_url }})

Contact page

## Step control

The user can define the step controls data using the Guided mode (![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }})) as shown in the Fig. 39.2.33\. If user wants to use the advanced simulation controls than we can switch to the Expert mode (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})) as shown in the Fig. 39.2.34\. For more information and description about options in Simulation controls please refer [9.Simulation Controls](/docs/en/pre_processor/9_simulation_controls/9_simulation_controls/).

  
**Starting Step Number** : If a new database is written, the specified step number will be the first step in the database. If data is written to an existing database, the pre-processor data will be appended to this database in proper numerical order, and any steps after the one specified will be overwritten.

**Number of steps (NSTEP) :** Number of steps to be simulated can be defined here. If the simulation stops earlier due to stopping criteria then, next operation starting step will be continuation from previous operation.

**Step increment** : The step increment to save in the database controls the number of steps that the system will save in the database. When a simulation runs, every step must be computed, but does not necessarily need to be saved in the database. Storing more steps will preserve more information about the process, consequently it will require more storage space.  
**Stopping Criteria** :

  * **For Simplified mode geometry** : We need to define the Length of cut so the simulation stops automatically after cutting the defined length.

  * **For Curved mode geometry** : We need to define the Arc angle to cut so the simulation stops automatically after cutting the defined angle.

![]({{ '/assets/images/operation_templates/39_cutting/39_2_3d_turning/image0033.jpg' | relative_url }})

Step controls page in Guided Mode

![]({{ '/assets/images/operation_templates/39_cutting/39_2_3d_turning/image0034.jpg' | relative_url }})

Step controls page in Expert Mode

## Generate DB

**Check Data** ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}): It checks the Data. If Data is correct, we can generate DB. But while checking Data if it gives any errors or warnings then it should be corrected before generating Database. Errors will not allow the database to be generated while warnings will allow the DB to be generated.  
  
**Generate Database**![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) : By clicking on this button, it generates the Database for the setup (See Fig. 39.2.35).  
  
**Append Key file :** Any information that is not defined in the wizard but still applicable to the process can be loaded as .key file. This option is also useful in the cases where only few values needs to be changed then those values can be defined as .key file and only .key file can be changed, and simulation can be resubmitted.

![]({{ '/assets/images/operation_templates/39_cutting/39_2_3d_turning/image0035.jpg' | relative_url }})

Generate DB page

**Related Topics:**

[39 Introduction to Cutting](/docs/en/operation_templates/39_cutting/39_introduction_to_cutting/)

[39.1. 2D Cutting](/docs/en/operation_templates/39_cutting/39_1_2d_cutting/)

[39.3. 3D Milling](/docs/en/operation_templates/39_cutting/39_3_3d_milling/)

[39.4. 3D Drilling](/docs/en/operation_templates/39_cutting/39_4_drilling/)

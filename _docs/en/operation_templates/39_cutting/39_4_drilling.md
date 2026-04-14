---
lang: en
title: "39.4. 3D Drilling"
---

# 39.4. Drilling

39.4.1. System Summary

39.4.2. Adding Drilling Operation

39.4.3. Process

39.4.4. Material List

39.4.5. Tool

39.4.5.1. Insert Geometry

39.4.5.2. Coating Material

39.4.5.3. Tool material

39.4.5.4. Tool Mesh

39.4.5.5. Tool BCC

39.4.6. Workpiece

39.4.6.1. Workpiece Geometry

39.4.6.2. Workpiece Material Selection

39.4.6.3. Workpiece Mesh Generation

39.4.6.4. Workpiece BCC

39.4.7. Control

39.4.8. Tool Wear

39.4.9. Contact

39.4.10. Step Control

39.4.11. Generate DB

## System Summary

Due to the number of revolutions of a drill necessary to establish characteristic behavior, drilling simulations in DEFORM are time consuming. Therefore, every effort should be made to optimize problem size. User can optimize the drilling simulation set up with considerations including keeping the workpiece as small as possible while capturing geometry (both in diameter and thickness), using the largest element which can adequately capture chip geometry, and possibly pre-shaping the workpiece to eliminate the necessity to simulate the transient point penetration before the drill reaches full depth. System provides options to model pre-shape workpiece considering the drill tip geometry.

## Adding Drilling Operation

To set up Drilling process user need to add the 3D cutting template and select “**Drilling** ” option in the “Process” page as shown in Fig. 39.4.1. For more details on how to add problem please refer [39.2.1. How to add 3D Cutting Operation](39_2_3d_turning.htm#39_2_1_How_to_add_3D_Cutting_Operation).

## Process page

The process parameters to setup Drilling process are as shown in Fig. 39.4.1.

**Environment Heat Transfer:** Environment temperature and convection co-efficient are defined under this tab, for more information on defining these parameters refer [39.2.4. Turning Process](39_2_3d_turning.htm#39_2_4_Process_page).

**Cutting speed (v):** It is defined as the speed at which the tool moves. The cutting speed can be defined as mm/sec or m/min in SI and in/sec or ft/min in English units.

**Rotation speed:** It defines the rotational speed of tool. The rotation speed can be defined in rpm and radians/sec.

**Feed rate (f) :** It is defined as the distance the tool travels during one revolution of the workpiece. This can be defined as mm/rev or mm/sec in SI and in/rev or in/sec in English units.

![]({{ '/assets/images/operation_templates/39_cutting/39_4_3d_drilling/image0001.jpg' | relative_url }})

Drilling type process page

## Material List 

In this Material List page, user can load a material from the library or keyword or database file using the ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}), ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) options as shown in Fig. 39.4.2. The materials loaded here can be assigned to the objects from their respective material page. User can also add a new material using ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button and define its properties. User can use ![]({{ '/assets/icons/pre_icons/mo_delete_icon2.jpg' | relative_url }}) button to delete the loaded material. User can also save the material using ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}), ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}) options.

![]({{ '/assets/images/operation_templates/39_cutting/39_4_3d_drilling/image0002.jpg' | relative_url }})

Assigning the Material to Material list

## Tool 

In this Tool page, the user can define the temperature of the tool object. We can import the tool object using the ![]({{ '/assets/icons/pre_icons/mo_import_object_button.jpg' | relative_url }}) button. If user wants to calculate the thermal data for tool object, select the “**Calculate tool temperature** ” check box and we can observe that mesh options for tool are enabled so that we can mesh the tool to calculate temperature distribution. (See Fig. 39.4.3.)

![]({{ '/assets/images/operation_templates/39_cutting/39_4_3d_drilling/image0003.jpg' | relative_url }})

Tool Page

### Insert Geometry 

In this Insert Geometry page (see Fig. 39.4.4.), the user can define the tool geometry using the ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}). The user can also import the geometry using the Import geometry ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}), ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) options. User can use “Advanced” option to define the number of flutes on drill bit tool (see Fig. 39.4.6.), which is used in feed calculations. 

![]({{ '/assets/images/operation_templates/39_cutting/39_4_3d_drilling/image0004.jpg' | relative_url }})

Insert Geometry Page

  
**Defining Tool Geometry using Define Primitive option:**

Define Primitive will lead to the ‘Drillbit Primitive menu’ as shown in Fig. 39.4.5. After defining the geometry parameters of the drill bit user can click on ![]({{ '/assets/icons/pre_icons/mo_generate_2_button.jpg' | relative_url }}) button to create drill bit geometry. 

![]({{ '/assets/images/operation_templates/39_cutting/39_4_3d_drilling/image0005.jpg' | relative_url }})

Drill bit primitive page

![]({{ '/assets/images/operation_templates/39_cutting/39_4_3d_drilling/image0006.jpg' | relative_url }})

Advanced options for Drill bit geometry

### Coating Material 

User can apply coating to tool insert by defining coating layer and its thickness in “**Coating Material** ” page. User can define the coating layer material and its thickness by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_icon.jpg' | relative_url }}) button as shown in the Fig. 39.4.7. If user wants to delete any layer, then user must select the respective layer and click on ![]({{ '/assets/icons/pre_icons/mo_delete_icon.jpg' | relative_url }}) button.

  
**Extract Coating Info** : After Generating the coating, we can extract the coating info using this button.

**Delete Coating** : We can also delete the Costing layers using this button. 

Using the “**Preserve state variables and boundary conditions** ” check box the user can create the coating layer without losing the state variable and boundary conditions data of the tool.

![]({{ '/assets/images/operation_templates/39_cutting/39_4_3d_drilling/image0007.jpg' | relative_url }})

Coating Material Page

### Tool material 

In material page, all the materials added to material list are displayed as shown in Fig. 39.4.8. User can select the required material to assign it to respective object. If the desired material is not available in the list, then the user can load the material in object material page using “Import material” data from a File ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) or using “Load form Library” option ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}). User can also create new material if the material is not available in DEFORM library using ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}). User can delete the material from list using ![]({{ '/assets/icons/pre_icons/mo_delete_icon2.jpg' | relative_url }}) or edit the material data using ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}). Modified / newly defined material can be saved using ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}), ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}). 

![]({{ '/assets/images/operation_templates/39_cutting/39_4_3d_drilling/image0008.jpg' | relative_url }})

Assigning the Tool Material

### Tool Mesh 

User can generate mesh for the tool by defining relative or absolute mesh size data as shown in the Fig. 39.4.9. & Fig. 39.4.10. It also provides the preview of the mesh when we click on “Preview Mesh” option. Cutting edge information being part of the insert data, the wizard automatically applies finer mesh near the cutting zone. See Fig. 39.4.9. to view meshed drill bit.

  
**Relative Mesh Method:**

  * **Target number of elements:** The number of elements to be generated for an object can be specified merely by adjusting the slider bar and selecting an appropriate value for the current simulation.

  * **Size Ratio:** It is the size ratio between the largest element edge length to smallest element edge length.

![]({{ '/assets/images/operation_templates/39_cutting/39_4_3d_drilling/image0009.jpg' | relative_url }})

Tool Mesh Generation using relative mesh size

  
**Absolute Mesh Method :**

  * **Minimum element size:** Feed rate automatically calculates the minimum element size of the mesh to be generated which calculates the Number of elements value automatically as shown in the Fig. 39.4.10.

![]({{ '/assets/images/operation_templates/39_cutting/39_4_3d_drilling/image0010.jpg' | relative_url }})

Tool Mesh Generation using absolute mesh size

### Tool BCC 

In this BCC Page, the user can define the Thermal BCC like “Heat Exchange with Environment” and “Temperature”. The default BCCs are assigned automatically after generating the mesh as shown in the Fig. 39.4.11.

![]({{ '/assets/images/operation_templates/39_cutting/39_4_3d_drilling/image0011.jpg' | relative_url }})

Default Heat exchange BCC

## Workpiece 

In this Workpiece page, the user can define the object type and set its initial temperature. Plastic object type is selected by default as shown in Fig. 39.4.12., if user is interested to consider the effect of elastic properties then Elasto-plastic object type can be used. We can also import the object data using the ![]({{ '/assets/icons/pre_icons/mo_import_object_button.jpg' | relative_url }}) button.

![]({{ '/assets/images/operation_templates/39_cutting/39_4_3d_drilling/image0012.jpg' | relative_url }})

Workpiece Page

### Workpiece Geometry 

In this Workpiece Geometry page, the user can define the workpiece geometry using the ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}). The user can also import the geometry using the Import geometry ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}), ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}), option.

####   
Defining Workpiece Geometry using Define Primitive option

“Define Primitive” will open ‘Workpiece Geo Primitive’ menu as shown in Fig. 39.4.13. Template provides options to create Cylindrical work piece or pre-shaped workpiece based on drill tip geometry. Fig. 39.4.13. and Fig. 39.4.14. shows geometry parameters to create workpiece from drill tip shape and cylindrical workpiece.

![]({{ '/assets/images/operation_templates/39_cutting/39_4_3d_drilling/image0013.jpg' | relative_url }})

Create from drill tip shape workpiece geometry

![]({{ '/assets/images/operation_templates/39_cutting/39_4_3d_drilling/image0014.jpg' | relative_url }})

Cylinder workpiece geometry

### Workpiece Material Selection

In material page, all the materials added to material list are displayed as shown in Fig. 39.4.15. User can select the required material to assign it to respective object. If the desired material is not available in the list, then the user can load the material in object material page using “Import Material” data from a File ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) or using “Load form Library” option ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}). User can also create new material if the material is not available in DEFORM library using ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}). User can delete the material from list using ![]({{ '/assets/icons/pre_icons/mo_delete_icon2.jpg' | relative_url }}) or edit the material data using ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}). Modified / newly defined material can be saved using ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}), ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}) .

![]({{ '/assets/images/operation_templates/39_cutting/39_4_3d_drilling/image0015.jpg' | relative_url }})

Assigning the material for the workpiece

### Workpiece Mesh Generation

The User can generate the mesh by defining relative or absolute mesh size data as shown in the Fig. 39.4.16. & Fig. 39.4.17. It also provides the preview of the mesh when we click on ![]({{ '/assets/icons/pre_icons/mo_preview_mesh_button.jpg' | relative_url }}) option.

**Relative Mesh Method:**

  * **Target number of elements** : The number of elements to be generated for an object can be specified merely by adjusting the slider bar and selecting an appropriate value for the current simulation.

  * **Size Ratio** : It is the size ratio between the largest element edge length to smallest element edge length. Meshed pre-shaped workpiece based on drill tip looks like as shown in Fig. 39.4.16.

![]({{ '/assets/images/operation_templates/39_cutting/39_4_3d_drilling/image0016.jpg' | relative_url }})

Workpiece mesh generation using relative mesh size

  
**Absolute Mesh Method:**

  * **Define size by percentage of feed:** The percentage of feed will automatically calculate the minimum element size of the mesh.

  * **Minimum element size:** It sets the minimum element size of the mesh to be generated which is calculated from the percentage of feed value.

![]({{ '/assets/images/operation_templates/39_cutting/39_4_3d_drilling/image0017.jpg' | relative_url }})

Workpiece mesh generation using absolute mesh size

### Workpiece BCC 

In this BCC Page, the user can define the Deformation and Thermal BCC (like Velocity, Heat Exchange with Environment and Temperature). The BCC data will be automatically assigned by default after generating the mesh as shown in the Fig. 39.4.18. and Fig. 39.4.19.

![]({{ '/assets/images/operation_templates/39_cutting/39_4_3d_drilling/image0018.jpg' | relative_url }})

Velocity BCC data for cylinder geometry

![]({{ '/assets/images/operation_templates/39_cutting/39_4_3d_drilling/image0019.jpg' | relative_url }})

Heat Exchange BCC for Create from drill tip shape geometry

## Control

Using “Position objects” the tool can be positioned based on the feed rate and workpiece location. Various positioning options are available to position the objects as shown in Fig. 39.4.20., for more information on these options please refer [19\. Object Positioning](/docs/en/pre_processor/19_object_positioning/19_object_positioning/).

![]({{ '/assets/images/operation_templates/39_cutting/39_4_3d_drilling/image0020.jpg' | relative_url }})

Object positioning options

## Tool Wear

User can turn on tool wear calculation using “**Define model to calculate tool wear** ” check box. After turning on check box user can select the tool wear model and define its parameters as shown in the Fig. 39.4.21., for more information on these options please refer [20.4. Tool Wear.](/docs/en/pre_processor/20_inter-object_data_definition/20_4_tool_wear/)

![]({{ '/assets/images/operation_templates/39_cutting/39_4_3d_drilling/image0021.jpg' | relative_url }})

Tool Wear page

## Contact

User radio button will be selected and relations also will be defined by default for 3D Cutting operation as shown in Fig. 39.4.22.. User can modify the value of each relation by selecting it and clicking on ![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }}) button. User can click on ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) button to calculate contact tolerance. User can click on ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) to generate contact relation. User can turn on check box next to contact relation to define sticking contact.  
For more information please refer [20\. Inter-Object Relations](/docs/en/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/).

![]({{ '/assets/images/operation_templates/39_cutting/39_4_3d_drilling/image0022.jpg' | relative_url }})

Contact page

## Step Control

The user can define the step controls data using the Guided mode (![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }})) as shown in the Fig. 39.4.23. The user can define the number of steps, step increment and step increment control. The Drill depth is available, so the simulation stops after reaching the defined depth.If user wants to use the advanced simulation controls than we can switch to the Expert mode (![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }})) as shown in the Fig. 39.4.24. For more information and description about options in Simulation controls please refer [9.Simulation Controls](/docs/en/pre_processor/9_simulation_controls/9_simulation_controls/). 

![]({{ '/assets/images/operation_templates/39_cutting/39_4_3d_drilling/image0023.jpg' | relative_url }})

Step controls page in Guided Mode

![]({{ '/assets/images/operation_templates/39_cutting/39_4_3d_drilling/image0024.jpg' | relative_url }})

Step controls page in Expert Mode

## Generate DB

**Check Data** ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}): It checks the Data. If Data is correct, we can generate DB. But while checking Data if it gives any errors or warnings then it should be corrected before generating Database. Errors will not allow the database to be generated while warnings will allow the DB to be generated.  
  
**Generate Database**![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) : By clicking on this button, it generates the Database for the setup (See Fig. 39.4.25.).  
  
**Append Key file :** Any information that is not defined in the wizard but still applicable to the process can be loaded as .key file. This option is also useful in the cases where only few values needs to be changed then those values can be defined as .key file and only .key file can be changed, and simulation can be resubmitted.

![]({{ '/assets/images/operation_templates/39_cutting/39_4_3d_drilling/image0025.jpg' | relative_url }})

Generate DB page

  
**Related Topics:**

[39 Introduction to Cutting](/docs/en/operation_templates/39_cutting/39_introduction_to_cutting/)

[39.1. 2D Cutting](/docs/en/operation_templates/39_cutting/39_1_2d_cutting/)

[39.2. 3D Turning](/docs/en/operation_templates/39_cutting/39_2_3d_turning/)

[39.3. 3D Milling](/docs/en/operation_templates/39_cutting/39_3_3d_milling/)

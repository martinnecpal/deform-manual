---
lang: sk
title: "37.1. 2D Heat Treatment Wizard"
---

# 37.1. 2D Heat Treatment Wizard Manual

37.1.1. How to add 2D Heat Treatment Operation

37.1.2. Process Selection

37.1.3. Initialization

37.1.4. Material selection

37.1.5. Objects

  * Workpiece /Object General

  * Object Geometry

  * Object Mesh

  * Object Material

  * Object Boundary Condition

  * [Object Properties](37_2_3d_heat_treatment_wizard.htm#Object_Property)

  * Initialize

37.1.6. Medium Details

37.1.7. chedule

37.1.8. ontrols

37.1.9. topping controls

37.1.10. Simulation Controls

37.1.11. Generation Database

## How to add Heat Treatment Operation

Heat Treatment operation can be setup in MO environment that can be accessed from GUI Main. Create a new problem by either selecting File ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) New Problem or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. Select " Integrated Manufacturing Process" and unit system. MO window will be opened with New Project popup, in New Project popup Define Project Name, Title and Unit system (File menu selected unit system will be selected). Also we can add 2D HT Wizard operation by selecting from First operation pull down list and check the Check box to add operation as Operation1 in new project (as shown in Fig. 37.1.1.). Then Click ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) in New project window, MO wizard will open and in Operation editor we are seeing 3D Heat Treat wizard added in Operation editor. Using copy Existing project option we can import previous saved projects as new project. 

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_1_2d_heat_treatment_wizard/image001.jpg' | relative_url }})

Assign Project name and First Operation selection in New Project window

We can also add 2D HT Wizard operation to operation editor from explorer tab, by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button next to 2D HT Wizard operation (as shown in Fig. 37.1.2.) or by drag and drop 2D HT Wizard into operation editor window. by default process selection page will be open in property settings modification area.

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_1_2d_heat_treatment_wizard/image002.jpg' | relative_url }})

Adding operation from Explorer Operation list

## Process Selection

In Process page, user can select the Simulation mode as Phase transformation or Diffusion or Deformation or combination of these. If user is interested only to simulate phase transformations during heat treatment then only phase transformation can be turned on, but if user would like to simulate the effect of phase transformation change on geometry then both phase transformation and deformation should be turned on. If user would like to simulate carbon diffusion process only, then only Diffusion can be turned on but if user would like to simulate the diffusion effect on geometry, then both diffusion and Deformation should be turned on.

In this page user can set controls for the duration of the step (See Fig. 37.1.3.). Step Definition can be either User or Auto. When step definition is defined as user mode, user needs to define time per step along with the step increment to write the step into DB.

  
If step definition is Auto mode, then user needs to mention the maximum change in temperature allowed per step along with the minimum and maximum process time per step, also step increment to write the step into DB.

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_1_2d_heat_treatment_wizard/image003.jpg' | relative_url }})

Process page

## Initialization

In Initialization page, user can select the Geometry type either as Axisymmetric or Plane strain using respective radio button. The simulation mode can also be selected here. User can import the Medium details and scheduled data of HT wizard (.HTWZ) of older versions project using Import wizard file option (See Fig. 37.1.4.).

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_1_2d_heat_treatment_wizard/image004.jpg' | relative_url }})

Initialization page

## Material selection

Materials required for the process can be loaded either from library using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) or from DB or Keyfile using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) as shown in Fig. 37.1.5. User can also add new material and define required data from respective tab by clicking ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). For more information on Material data definition please refer [Material data](/docs/sk/pre_processor/10_material_data/10_material_data/). 

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_1_2d_heat_treatment_wizard/image005.jpg' | relative_url }})

Importing Material from Library

## Objects

If user would like to include fixtures and other objects along with the billet then in Objects page, Add the number of Objects required for Heat Treatment operation by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button. By default one object will be added in operation as shown in Fig. 37.1.6.

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_1_2d_heat_treatment_wizard/image006.jpg' | relative_url }})

Objects window

### Workpiece /Object General

In Object general page (See Fig. 37.1.7.), User can select Object type by selecting respective radio button. For more information on object types please refer. By default object type for workpiece will be set as Plastic. User can initialize the object temperature by setting value in Object Temp. field. User can also import object from other DB’s or Keyfile’s using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) option and browsing respective file. 

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_1_2d_heat_treatment_wizard/image007.jpg' | relative_url }})

Object General page

### Object Geometry

User can define new geometry using primitives and also can import the geometry from other file using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) or from library using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}), user can also import geometries in other formats such as .DXF and .IGES. Primitives are provided for easy definition of basic geometry shapes. For more information on creating and editing 2D geometries please refer to [12.1. 2D Geometry Data Defining](/docs/sk/pre_processor/12_geometry_modelling/12_1_2d_geometry_data_defining/) and [12.2. 2D Geometry Data Editing](/docs/sk/pre_processor/12_geometry_modelling/12_2_2d_geometry_editing/).

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_1_2d_heat_treatment_wizard/image008.jpg' | relative_url }})

Object Geometry page

### Object Mesh

Mesh Page provides options to mesh the object. Guided ![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }}) mode provides option to set number of elements only using slider bar to generate mesh. If the object geometry is complex or user would like to control the mesh density over the object, then user has to switch to expert mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}). Expert mode provides various options like weighing factors, Mesh windows and user defined mode to control the mesh density. Meshing options available inexpert mode and Guided more are shown in Fig. 37.1.9. and Fig. 37.1.10. For more detail description of these options, please refer [13.1. 2D Mesh Generation.](/docs/sk/pre_processor/13_mesh_generation/13_1_2d_mesh_generation/)

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_1_2d_heat_treatment_wizard/image009.jpg' | relative_url }})

Guided mode Mesh option

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_1_2d_heat_treatment_wizard/image010.jpg' | relative_url }})

Expert mode mesh option

### Object Material

In material page, all the materials added to material list are displayed (as shown in Fig. 37.1.11.) and user can select the required material to assign it to respective object from material list. Also user can load the material in Object material page using Import Material data from a file ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) or Using Load from Library option ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}). 

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_1_2d_heat_treatment_wizard/image011.jpg' | relative_url }})

Material selection Window

### Object Boundary Condition

System will automatically assign thermal and diffusion BCC depending on the process selection and symmetry conditions based on geometry type. User can review these BCC and can also assign require BCC depending on the process (See Fig. 37.1.12. and Fig. 37.1.13.).

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_1_2d_heat_treatment_wizard/image012.jpg' | relative_url }})

Assigned Velocity BCC for Axisymmetric object

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_1_2d_heat_treatment_wizard/image013.jpg' | relative_url }})

Assigned Velocity BCC for Plane Strain object

### Object Property

Miscellaneous object parameters, which affect either thermo-mechanical behavior of the object or numerical solution behavior are specified in the Object-Properties window. (See Fig. 37.1.14.) For more information, Please refer [16\. Object properties](/docs/sk/pre_processor/16_object_properties/16_object_properties/).

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_1_2d_heat_treatment_wizard/image014.jpg' | relative_url }}) ![]({{ '/assets/images/operation_templates/37_heat_treatment/37_1_2d_heat_treatment_wizard/image015.jpg' | relative_url }})

Property Window: (a) Axi-symmetric/plane Stress/Torsion Geometry type (b) Plane Strain

### Initialize

In Initialize page, user has options to initialize Temperature, Strain, Stress, Damage, Velocity, Displacement, Grain Size, Recrystallization Vol Frac and Density values (as shown in Fig. 37.1.15.).

  
Also user can define Average strain rate and Limiting strain rate value for the object.If the object type is plastic then limiting strain rate defines a limiting value of effective strain rate under which the plastic material is considered rigid. The average strain rate is a characteristic average value of the effective strain rate. An approximation of this value should be given at the start of the simulation. DEFORM automatically maintains the ratio between average strain rate and limiting strain rate. Generally, the value of limiting strain rate should be 0.01.

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_1_2d_heat_treatment_wizard/image016.jpg' | relative_url }})

Initialize page

User should initialize the initial atom percentage for diffusion at nodal level if diffusion process is simulated. For heat treatment user should initialize volume fraction of each phase existing initially at element level and summation of all phases volume fraction should be equal to 1. Nodal values can be accessed by clicking on ![]({{ '/assets/icons/pre_icons/mo_nodal_data_icon.jpg' | relative_url }}) icon from tool bar and initialization can be done using ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}) icon. Similarly element values can be can be accessed by clicking on ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}) icon from tool bar and initialization can be done using ![]({{ '/assets/icons/pre_icons/mo_elemental_data_icon.jpg' | relative_url }}) icon. Node data and Element data options are as shown in Fig. 37.1.16. and Fig. 37.1.17.

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_1_2d_heat_treatment_wizard/image017.jpg' | relative_url }})

Nodal data window

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_1_2d_heat_treatment_wizard/image018.jpg' | relative_url }})

Element data window

## Medium Details

In Medium details page, user can define the media and its Heat transfer coefficients along with the zones associated to that media (See Fig. 37.1.18.)

  
**Media** – Different types of media used in the heat treatment process can be defined here, using ![]({{ '/assets/icons/pre_icons/mo_add_icon.jpg' | relative_url }}) button media can be added and using ![]({{ '/assets/icons/pre_icons/mo_delete_icon.jpg' | relative_url }}) button defined media can be removed. Media can be renamed using ![]({{ '/assets/icons/pre_icons/mo_rename_button.jpg' | relative_url }}) button.  
**Zones** – Zones are the surfaces of the workpiece that are associated to the Media selected under media tab, by default one zone is defined as Default which cannot be deleted. Each zone can be assigned different Heat transfer co-efficients and these co-efficients can be constant or function of temperature or function of time. For the remaining surfaces where no zone is defined, the conditions defined for Default zone is applied. The Heat Transfer co-efficient values for each zone can be stored using button and can be loaded back using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) button.

**Radiation** – User can turn on the Radiation check box if radiation needs to be activated for the respective media.

**Diffusion surface reaction coefficient** \- Diffusion surface reaction co-efficient values associated with the media can be defined here when applicable and these values can be constant or function of temperature or function of atom %.

**Emissivity :** If any particular zone is to be modeled for Radiation then user can turn on Radiation checkbox and define Emssivity value for that zone. Emissivity can be defined as constant or function of temperature or function of time.**  
**

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_1_2d_heat_treatment_wizard/image019.jpg' | relative_url }})

Medium page

## Schedule

In schedule page, user can scheduled the Annealing, Normalizing and Quenching process by defining its process duration, media, Environment temperature and Atom contents as shown in Fig. 37.1.19.

  * User can add an operation using ![]({{ '/assets/icons/pre_icons/mo_add_button.jpg' | relative_url }}) button.

  * User can delete a defined operation using ![]({{ '/assets/icons/pre_icons/mo_delete_button.jpg' | relative_url }}) button.

  * User can delete all the operations defined at a time using![]({{ '/assets/icons/pre_icons/mo_delete_all_button.jpg' | relative_url }}) button.

  * User can insert an operation between two operations using ![]({{ '/assets/icons/pre_icons/mo_insert_button.jpg' | relative_url }}) button.

  * By clicking ![]({{ '/assets/icons/pre_icons/mo_display_button.jpg' | relative_url }}) button we can see the Thermal schedule graph of Time vs. Temperature for all operations as shown in Fig. 37.1.21.

  * User can also define specific environment conditions using advanced option for each operation independently by clicking on ![]({{ '/assets/icons/pre_icons/mo_define.._button.jpg' | relative_url }}) .

  
**Advanced Options:**

User can define Environment Temperature and Atom content in Function of time as shown in Fig. 37.1.20. for a specific operation by turning on the check boxes.  
**Use local time for functions** – When user turns on this option, the local time of the operation is considered to apply the function values defined else by default global time is used. Global time is the accumulation of process time of all the operations, while local time will start when the operation starts and end with operation.  
**Initialize trasf. Incubation** – User can initialize transformation incubation by turning on this check box.  
**User’s .KEY** – user can indicate the path of .KEY file which can be used along with the existing definition by entering the path in this fields.  
**Active Transformation** – All the transformation defined in the material file are displayed here and user can turn on the transformations applicable for the operation by turning on the check the boxes next to transformation.  
User can return to the schedule page by clicking on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button and by clicking on ![]({{ '/assets/icons/pre_icons/mo_cancel_button.jpg' | relative_url }}) button user can come out without applying the changes defined in that session only.

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_1_2d_heat_treatment_wizard/image020.jpg' | relative_url }})

Schedule page

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_1_2d_heat_treatment_wizard/image021.jpg' | relative_url }})

Schedule Advanced options

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_1_2d_heat_treatment_wizard/image022.jpg' | relative_url }})

Schedule Graph

## Positioning

User can position the objects using position objects button. Various positioning options are available to position the objects as shown in Fig. 37.1.22., for more information on these options please refer [19\. Object Positioning](/docs/sk/pre_processor/19_object_positioning/19_object_positioning/).

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_1_2d_heat_treatment_wizard/image023.jpg' | relative_url }})

Object Positioning options

## Stopping controls

Thermal stop controls provides a way that stop the simulation at pre-defined conditions (See Fig. 37.1.23.), like selected temperature for all nodes therefore the heating time can be predicted. They are applied for the object selected from the pull down list of objects.

  * **None** : Applies no thermal stopping controls

  * **Any Node** : Simulation stops when any node in the billet reaches the specified value.

  * **All Nodes** : Simulation stops when all the nodes in the billet reach the specified value.

  * **Selected Node** : Simulation stops when specified node in the billet reaches the specified value.

  * **Average All Nodes** : Simulation stops when average temperature of all the nodes in the billet reaches the specified value.

  * **Average surface Temp +Max. Temp** :Simulation stops when average temperature of all the nodes on the surface of billet + Maximum temperature in the billet reaches the specified value.

**Temperature Range:**

Apart from single value a range of temperature also can be used to stop the simulation.

  * **Stop when temperature is outside range** :Simulation stops when the temperature value is outside the specified range.

  * **Stop when temperature is inside range** : Simulation stops when the temperature value is inside the specified range.

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_1_2d_heat_treatment_wizard/image024.jpg' | relative_url }})

Thermal Stopping Controls

## Simulation Controls

In Simulation controls page ( Fig. 37.1.24.), user can define the Step definition in User or Auto type by selecting respect Radio button.

  
**Auto** – When user selects Auto option, system will automatically control the time step value based on the conditions specified. The conditions used to control time step are,

  * **Temp. change per step** – Maximum change in the temperature allowed per step, whenever it exceeds this value time step is reduced and whenever it reduces than this value time step is increased.

  * **Min/Max Time per step** – It specifies the range of time step within which system can vary the time step value. Minimum allowed value of time step and Maximum allowed value of time step can be set here.

  * **Step Increment to Save** – The step increment (STPINC) to save in the database controls the number of steps that the system will save in the database. When a simulation runs, every step must be computed, but does not necessarily need to be saved in the database. Storing more steps will preserve more information about the process, consequently it will require more storage space.

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_1_2d_heat_treatment_wizard/image025.jpg' | relative_url }})

Simulation Controls

## Generation Database

Once the problem has been completely set up, the last step is to generate a database file. The FEM engine (the part of DEFORM® that calculates the solution) uses a database file to store the finite element solutions for the problem. When you generate a database in the DEFORM MO Pre-processor, all of the information defined in the Pre-processor (such as the material properties, movement controls, object geometries, etc.) is transferred to the database file.

In Generate DB page (See Fig. 37.1.25.). From v12.0.2, we can observe the Operation Simulation setup summary. Click the ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) button to have the program check to see if anything was missed in the problem setup. During the checking process, messages in the red color signify data that needs to be fixed before a simulation can be run (such as when you forget to define any material data). 

Click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database. When the program is done with writing the database, switch to ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) tab to run simulation.

**Append Key file**

Any information that is not defined in the wizard but still applicable to the process can be loaded as .key file. This option is also useful in the cases where only few values needs to be changed then those values can be defined as .key file and only .key file can be changed and simulation can be resubmitted.

![]({{ '/assets/images/operation_templates/37_heat_treatment/37_1_2d_heat_treatment_wizard/image026.jpg' | relative_url }})

Generate database

**Related Topics:**

[6.1. Integrated Manufacturing Process Pre- Processor Layout](/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_1_integrated_manufacturing_process_preprocessor_layout/)

[6.2. Integrated Manufacturing Process.Simulation layout](/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_2_integrated_manufacturing_process_simulation_layout/)

[6.3. Integrated Manufacturing Process Post - Processor layout](/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_3_integrated_manufacturing_process_post_layout/)

[2D Heat Treatment Wizard Lab1](/docs/sk/labs/heat_treatment_labs/2d_heat_treatment_wizard_lab1/)

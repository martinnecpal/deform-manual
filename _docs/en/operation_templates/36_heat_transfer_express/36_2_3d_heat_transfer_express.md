---
lang: en
title: "36.2. 3D Heat Transfer Express"
---

# 36.2. 3D Heat Transfer Express

36.2.1. How to add 3D Heat Transfer Express operation

36.2.2. Process settings definition

36.2.3. Heating Type

36.2.4. Defining Heating operation

  * Object Basic definition

  * Object geometry definition

  * Object Mesh Definition

  * Material Definition

  * Boundary Conditions

  * Heat Condition Definition

  * Stopping controls Definition

  * Simulation controls Definition

  * Generate Database

36.2.5. Defining Heat Transfer Operation

  * Selecting Objects

  * Objects positioning and generating inter object relation

  * Heat condition Definition

36.2.6. Defining Rest on Die Operation

  * Define Thermal Calculations

  * Selecting objects

  * Positioning

  * Schedule Positioning

  * Inter-object Contact Generation

  * Heat Condition Definition

36.2.7. Continue Defining the Forming Operations

  * Defining Dwell on dies Operation

  * Heat Condition Definition

## How to add 3D Heat Transfer Express operation

Heat Transfer Express operation is accessible from MO Wizard that can be opened from Main GUI. Heat Transfer Express Operation can be added in MO wizard, from explorer tab by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button next to 3D Heat Transfer Express. Also, user can add by drag and drop into the Operation Editor as shown in Fig. 36.2.1. Heat Transfer express operation can also be added after the Heat transfer operations interactively after the simulation of preceding operations or in batch/scheduled mode.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_2_3d_heat_transfer_express/image001.jpg' | relative_url }})

Added 3D Heat Transfer Express operation into operation editor

## Process settings definition

In Process window simulation modes such as Geometry Type, Heating Type and Shape Complexity and Accuracy has to set for the heat transfer operation as shown in Fig. 36.2.1.

**Geometry Type**

In Heat Transfer Express 3D Full and Symmetry geometry models can be setup by selecting the respective geometry type radio buttons **Whole** part or **Symmetry**.

  
When the workpiece is asymmetric or need to study any asymmetric behavior during heat transfer and future forming operations then user has to select the Whole part geometry model type.

  
If the workpiece is symmetric then user can select the Symmetric geometry type to setup the symmetric problem model, this adds the symmetry plane selection window after workpiece geometry window. In symmetry window user has to select symmetry planes to fix the velocity along the symmetric plane.

## Heating Type

There are four heating types or heat transfer operations available in both 2D and 3D Heat Transfer Express operation those are (See Fig. 36.2.1.),

  * **Heating**

  * **Transfer**

  * **Rest on die and**

  * **Dwell on die**

Heating workpiece, heat transfer during transferring workpiece form furnace to press, resting workpiece on die (before forming) and workpiece dwell on die after forming operations can be setup easily by using the respective heating type. For more details about these heating types are described in [36\. Introduction to heat transfer express operation](/docs/en/operation_templates/36_heat_transfer_express/36_introduction_to_heat_transfer_express_operations/), refer Heating Types.

For resting and dwelling operation thermal calculation window will activate to give options to select heat transfer with dies and not to calculate heat transfer with dies. These options will be explained further in respective operations explanations.

**Shape Complexity and Accuracy**

The shape complexity and simulation accuracy slider bars (See Fig. 36.2.1.) influence the mesh settings and number of time steps used in the simulation. This in turn influences the run time and level of detail available in the simulation.

**Shape Complexity:**

  * **Simple** : The geometry of the objects are simple in nature. They require minimum number of elements, are easier to solve and takes less time.

  * **Moderate** : The geometry of the objects are moderate (not too complex) in nature.

  * **Complex** : The geometry of the objects are complex in nature.

  
**Shape Accuracy:**

  * **Fast** : Useful for fast evaluation of a process. In exchange for faster run times, there is a higher risk of missing important details.

  * **Moderate** : The simulation uses settings which attempt to balance calculation time and accuracy.

  * **Accurate** : Very detailed analysis of the process is done, which will generally capture minute details. Calculation time and storage requirements are more.

## Defining Heating operation

In heating or heat furnace operation, heating of billet in a furnace is modeled. After selecting the process settings system will gives the customized heating operation windows to guide the user to setup this operation. Only one object is allowed for this operation (See Fig. 36.2.2.) and that object will be added automatically. The default process settings will be added suited to heating operation.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image002.jpg' | relative_url }})

Heating operation object definition window

### Object Basic definition

Object basic definition includes object name, type and temperature. In addition to this object state variable values can be initialized by using Advanced button and object data like geometry, mesh, boundary conditions and material can be imported from DEFORM .DB /.Key file. (See Fig. 36.2.3.)

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image003.jpg' | relative_url }})

Workpiece window

  
**Object Name** : User can define the name for all the objects available in the operation.

  
**Object Type** : The object type ([OBJTYP](/docs/en/keyword_documentation/o/objtyp/)) defines if and how deformation is modeled for each individual object in a DEFORM problem. In Forming Express operation only two object type are available those are Plastic and Rigid and those two are automatically predefined by object number, so workpiece will be plastic and dies will be rigid. More object types are available in Forming operation, for its details refer [11.4. Object Type](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4._Object_type)

  
**Plastic** : Plastic objects are modelled as rigid-plastic or rigid-viscoplastic material depending on characteristics of materials. The formulation assumes that the material stress increases linearly with strain rate until a threshold strain rate, referred to as the limiting strain rate ([LMTSTR](/docs/en/keyword_documentation/l/lmtstr/)). The material deforms plastically beyond the limiting strain rate. The plastic material behaviour of the object is specified with a material flow stress function or flow stress data ([FSTRES](/docs/en/keyword_documentation/f/fstres/)). In heat transfer express workpiece is automatically assigned to Plastic object type.  
**Rigid** : Rigid objects are modelled as non-deformable materials. In the deformation analysis, the object is represented by the geometric profile ([DIEGEO](/docs/en/keyword_documentation/d/diegeo/)). Deformation solution data available for rigid objects include object stroke, load, and velocity. The mesh for the rigid object is used only for thermal, transformation, and diffusion calculations. In heat transfer express dies or tools are automatically assigned to Rigid as they are non-deformable objects.

**Note:**

Should note that object type is predefined by object number in Heat transfer Express operation. For 1st object type will be plastic and for further addition only rigid objects will add.  
There is an Import Object button on the Object page. This is for importing complete object data from another DEFORM file.

  
**Object Temperature** : User can define the object temperature in the Temperature field of the respective object window as shown in Fig. 36.2.3.

**Advanced Object Settings** : The advanced setting Initialization options (See Fig. 36.2.4.) will be useful when user import the object from previously run project or problem or when forming express operation is added after few other operations and if there is need to initialize few important state variables.  
The user can initialize temperature, strain, velocity, damage and displacement that has taken place in the deformable object using the advanced setting options. (See Fig. 36.2.4.)

![]({{ '/assets/images/operation_templates/34_forming_express/34_2_3d_forming_express_setup/image005.jpg' | relative_url }})

Advanced object settings

  
More variables can be initialized in Forming operation, for detail refer [35\. 2D Heat Transfer](/docs/en/operation_templates/35_heat_transfer/35_1_2d_heat_transfer_operation/) operation [Initialize](../35_heat_transfer/35_1_2d_heat_transfer_operation.htm#Initialize).

The average strain rate ([AVGSTR](/docs/en/keyword_documentation/a/avgstr/)) is a characteristic average value of the effective strain rate. An approximation of this value should be given at the start of the simulation.

The limiting strain rate ([LMTSTR](/docs/en/keyword_documentation/l/lmtstr/)) defines a limiting value of effective strain rate below which a plastic or porous material is considered rigid and behaves as Newtonian fluid like material.

![]({{ '/assets/icons/pre_icons/mo_reset_button.jpg' | relative_url }}) : Using this user can rest back the initialized state variables value.

For more Deformation object properties options available in Forming operation refer [16.1. Deformation Properties.](/docs/en/pre_processor/16_object_properties/16_1_deformation_properties/)

### Object geometry definition

Geometry window is used to create the geometry of an object as shown in Fig. 36.2.5. Before creating geometry only Define Primitive Geometry option will be available but after creating geometry Check, Scale, Reverse, Fix and Mark surface geometry options will activate and after generating mesh Extract border option will activate. 

![]({{ '/assets/images/operation_templates/34_forming_express/34_2_3d_forming_express_setup/image006.jpg' | relative_url }})

Geometry definition window

**Define primitive![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }})**

There are three primitive shapes in geometry primitives such as Box, Cylinder and Hollow Cylinder that can be used to generate geometries as shown in Fig. 36.2.6. In each case, the user has to scale appropriately to the problem by defining the dimensions. In addition to these primitives Extrude and Revolve can be used to convert 2D cross-section to 3D. Rotational symmetric objects are created by using the revolve angle option for cylinder, Hollow cylinder and Revolve primitives. 

![]({{ '/assets/images/operation_templates/34_forming_express/34_2_3d_forming_express_setup/image007.jpg' | relative_url }})

Geometry primitive window 

**Check![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) **

Always check geometry. DEFORM has a checking algorithm that checks for number of invalid edges, invalid orientation, polygons with small area and number of surfaces. Every type of error cannot be detected.

Using this Check Geometry option opens the Geometry Checking Results window which gives a summary of the object’s geometry (See Fig. 36.2.7.). For an object that has a closed volume, there should be 1 surface, 0 free edges and 0 invalid entities (as circled below in Fig. 36.2.7.). Objects that are imported as surfaces and not solids will have a free edge but should still only have 1 surface. 

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image011.jpg' | relative_url }})

Geometry Checking Results

**Scale![]({{ '/assets/icons/pre_icons/mo_scale_label.jpg' | relative_url }}) **

Geometry can be scaled in forming operation to accommodate thermal expansion by specifying the scaling factor. (See Fig. 36.2.8.) The scaling factor can be calculated by temperature differential and temperature dependent material data. The scaled geometry can be saved into different Geometry saving formats.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image014.jpg' | relative_url }})

Scale Geo window

  
**Reverse![]({{ '/assets/icons/pre_icons/mo_reverse_label.jpg' | relative_url }}) **

This feature reverses the surface/ normal of the geometry. Always surface/ Normal of the geometry should be outwards.

**Fix![]({{ '/assets/icons/pre_icons/mo_fix_label.jpg' | relative_url }})**

This feature will handle geometric problems where there are either multiple surfaces or open (holes) regions by deleting any extra surfaces and filling holes. For minor or localized problems, this works well. For more troublesome file such as this one, the repair may not produce a desirable result. (See Fig. 36.2.9.) 

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image016.jpg' | relative_url }})

Fixing Geometry of crankshaft Die

**Mark Surface**

Marking any surface takes it out of any contact calculations during the simulation. Even if workpiece comes in contact with that object, normally applied for die/punch surfaces where in practical scenario contacts wont form to avoid the unintended contact calculations.

**Other Geometry options**

**Show geometry inside mark:** Checking this option enables the Geometry orientation display.

**Define reference point** : User can select the geometry reference point by clicking on this button from display window. This reference point is required to define the distance between objects stopping controls stopping controls.

**Import Geometry from a file** ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}): It imports the geometry from a file  
**Load Geometry from Library** ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) :It imports geometry from Library  
**Save the Geometry to a file** ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}) : It saves the Geometry to a file.  
**Save Geometry to Library** ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}) : User can save geometry to the library using this option.  
**Delete Geometry** ![]({{ '/assets/icons/pre_icons/mo_clear_icon.jpg' | relative_url }}): user can delete the geometry.

### Symmetry Plane definition for workpiece

  
Symmetry window comes after the geometry window if symmetry geometry type is selected by user. Symmetry to be defined to fix the velocity of nodes on symmetry planes as shown in Fig. 36.2.10. First user need to select the symmetry plane by left mouse click, the selected plane will turn green and click on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button to add selected plane, for more than one symmetry plane repeat the same steps. For the selected plane system display center and normal as shown in Fig. 36.2.10.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_2_3d_heat_transfer_express/image002.jpg' | relative_url }})

Symmetry plane definition window

### Object Mesh Definition

The Mesh Generation window allows the user to generate a mesh for the current object. Below Fig. 36.2.11. shows the Mesh generation window in system mode. In this mode system automatically sets the number of mesh elements based on the shape complexity and accuracy setting selection in process window.

**System Mode**

Using **![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }})** user has to generate tetrahedron mesh for an objects. User can generate the  
surface mesh or mesh preview quickly before generating the solid mesh required for an object by using ![]({{ '/assets/icons/pre_icons/mo_mesh_preview_button.jpg' | relative_url }}) button. Once the user is satisfied with the preview of surface mesh, the mesh can be generated on an object by clicking **![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }})**.

After generating the mesh ![]({{ '/assets/icons/pre_icons/mo_delete_button.jpg' | relative_url }}) mesh button will get activate, this is useful to delete the current mesh of an object. For varying the auto calculated number of elements and advanced settings user has to go for User Defined Mode.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_2_3d_heat_transfer_express/image003.jpg' | relative_url }})

Mesh settings window in System mode

**User Defined Mode**

For user defined mesh mode option see Fig. 36.2.12., in this mode user can vary number of elements by adjusting the slider bar and use advanced options to change the Size ratio, Minimum elements size, Remesh criteria and Boolean operation. User can generate the surface mesh to observe mesh preview, once the user is satisfied with surface mesh user can generate the solid mesh for 3D object by clicking ![]({{ '/assets/icons/pre_icons/mo_solid_mesh_button.jpg' | relative_url }}) button.

**Number of elements (MGNELM):**

The number of mesh elements represents the approximate number of elements that will be generated by the system. The Automatic Mesh Generator (AMG) takes the value for [MGNELM](/docs/en/keyword_documentation/m/mgnelm/) and generates a mesh that will contain approximately the same number of elements. The number of elements can be specified merely by adjusting the slider bar and selecting an appropriate value for the current simulation.

  
The error between the number of specified elements and the number of generated elements is typically about ten percent.

  
For more mesh settings user has to select ![]({{ '/assets/icons/pre_icons/mo_advanced_button.jpg' | relative_url }}) button.

![]({{ '/assets/images/operation_templates/34_forming_express/34_2_3d_forming_express_setup/image010.jpg' | relative_url }})

User defined mode mesh settings

**Advanced Mesh Options**

  * General Mesh Settings: Within DEFORM, there are two different types of mesh that can be generated for 3D objects.

  * **Relative Mesh:** Using the relative mesh setting, the user specifies the number of solid elements to be generated. No matter how complex the shape of the part gets, the number of elements will remain essentially constant. ( Fig. 36.2.13.)

![]({{ '/assets/images/operation_templates/34_forming_express/34_2_3d_forming_express_setup/image011.jpg' | relative_url }})

Relative mesh settings

  * **Absolute Mesh** : Using the absolute mesh setting, the user specifies the size of the elements and the system determines the total number of elements that are required based on the size of the element specified and geometry. As part complexity increases, the number of elements tends to increase. ( Fig. 36.2.14.)

![]({{ '/assets/images/operation_templates/34_forming_express/34_2_3d_forming_express_setup/image012.jpg' | relative_url }})

Absolute mesh settings

  * **Element size ratio (MGSIZR)** : The maximum size ratio between elements is one of several ways to control the mesh density during automatic mesh generation (AMG) by specifying the ratio of node densities. For a value of 3 for [MGSIZR](/docs/en/keyword_documentation/m/mgsizr/), the largest element edge on an object will be roughly 3 times the size of the smallest element edge on the same object. If equal sized elements are desired, then Size Ratio = 1. If Size Ratio = 0, the element size ratio will not be a factor in the mesh density distribution.

  * **Remeshing criteria :**

Remeshing Criteria (Autoremesh) is the most convenient way to handle the remeshing of objects undergoing large plastic deformation. The Remeshing Criteria Window (See Fig. 36.2.14.) contains a group of parameters that control when and how often the mesh will be regenerated on a meshed object based on assignment of certain triggers. There are four keywords that control the initiation of a remeshing procedure for an object, they are Interference Depth ([RMDPTH](/docs/en/keyword_documentation/r/rmdpth/)), Max. Time Increment ([RMTIME](/docs/en/keyword_documentation/r/rmtime/)), Max. Step Increment ([RMSTEP](/docs/en/keyword_documentation/r/rmstep/)) and Max. Stroke Increment ([RMSTRK](/docs/en/keyword_documentation/r/rmstrk/)). When the remeshing criteria of any of these keywords has been fulfilled or the mesh becomes unusable (negative Jacobian), the object will be remeshed, the solution information from the old mesh is interpolated onto the new mesh and the simulation continues.

  * **Penetration Distance (relative)**

If a negative number (a fraction) is entered, the program will conduct a check on each surface edge that has a contact node on each end. The distance from the middle of the edge to the die surface is calculated and divided by the original length of the edge. If the ratio exceeds the magnitude of the specified value, remeshing will be triggered.

  * **Maximum stroke increment (RMSTRK)**

Anytime the maximum stroke increment ([RMSTRK](/docs/en/keyword_documentation/r/rmstrk/)) is exceeded by the stroke increment of the primary die since the last remeshing step, a new remeshing step will be initiated.

  * **Maximum time increment (RMTIME)**

Anytime the Maximum Time Increment ([RMTIME](/docs/en/keyword_documentation/r/rmtime/)) (Value of Elapsed Time) has elapsed since the last remeshing step, a new remeshing step will be initiated.

  * **Maximum step increment (RMSTEP)**

Anytime the Maximum Step Increment (Number of Steps) has occurred since the last remeshing step, a new remeshing step will be initiated.

**Delete Mesh**![]({{ '/assets/icons/pre_icons/mo_delete_mesh_button.jpg' | relative_url }})

Deletes the mesh generated for the object.

More mesh options like Coating mesh, System mesh density weighting factors, User Mesh Density Window options are not available in Forming express operation unlike in Forming operation, for those mesh options refer chapter [13.2. 3D Tet Mesh Generation](/docs/en/pre_processor/13_mesh_generation/13_2_3d_tet_mesh_generation/).

### Material Definition

Below Fig. 36.2.15. shows the material window. User can add or import material from a keyword file or load from DEFORM material library.

  
After loading system automatically assign the loaded material to an object. User can also edit the material properties using ![]({{ '/assets/icons/pre_icons/mo_material_edit_button.jpg' | relative_url }}) button.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_2_3d_heat_transfer_express/image004.jpg' | relative_url }})

Material window

Once after adding material click on ![]({{ '/assets/icons/pre_icons/mo_material_edit_button.jpg' | relative_url }}) button, material window will open as shown in Fig. 36.2.16.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image022.jpg' | relative_url }})

Material editing window

The properties required are dependent on the physical effects being simulated in DEFORM. The material properties that the user is required to specify is a function of the material types that the user is utilizing in the simulation. In Forming operation user can get access to all material properties for more information refer [10\. Material Data.](/docs/en/pre_processor/10_material_data/10_material_data/)

### Boundary Conditions

In Forming express Boundary conditions window, user can assign only Planar symmetry, Deformation velocity, Thermal Heat exchange with Environment and Temperature boundary constraints for an object. Boundary conditions specify how the boundary of an object interacts with other objects and with the environment. The most commonly used boundary conditions are heat exchange with the environment for simulations involving heat transfer, prescribed symmetry plane for enforcing symmetry in the model. Fig. 36.2.17. shows various BCC that can be assigned to an object.

  
By default planar symmetry planes will be added for workpiece object as per the symmetry plane selection in symmetry window as shown in Fig. 36.2.17. and also heat exchange with environment will be assigned to all surfaces except the symmetric planes for warm and hot forging process as shown in Fig. 36.2.18.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_2_3d_heat_transfer_express/image005.jpg' | relative_url }})

Symmetry boundary condition assigned for workpiece

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_2_3d_heat_transfer_express/image006.jpg' | relative_url }})

Heat exchange with environment boundary condition assigned for workpiece

More BCC’s options under different categories are available in Pre-Processor and Forming Operation such as [Deformation](/docs/en/pre_processor/14_boundary_conditions/14_2_deformation_boundary_conditions/),[Thermal](/docs/en/pre_processor/14_boundary_conditions/14_3_thermal_boundary_conditions/), [Diffusion](/docs/en/pre_processor/14_boundary_conditions/14_4_diffusion_boundary_conditions/) and [Heating](/docs/en/pre_processor/14_boundary_conditions/14_5_heating_boundary_conditions/). For more information about these BCC's please refer [14\. Boundary Conditions.](../../pre_processor/14_boundary_conditions)

### Heat Condition Definition

Heat conditions like Heating time (Process duration), Environment temperature and Convection coefficient has be defined in this window as shown in Fig. 36.2.19. For all heating types system by default define the heating conditions has to input the process settings data by changing the defaults.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image012.jpg' | relative_url }})

Heat condition settings window

### Stopping controls Definition

Only for heating operation heat transfer operation provides the stopping controls to stop the simulation when all nodes of the workpiece are within the specified degree range from the set point temperature or environment temperature as shown in Fig. 36.2.20. In Fig. 36.2.20. simulation stops if all nodes temperatures are within 1199.5 °C to 1200.5 °C.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image013.jpg' | relative_url }})

Heating stopping controls window

### Simulation controls Definition

The DEFORM system solves time dependent non-linear problems by generating a series of FEM solutions at discrete time increments. At each time increment, the velocities, temperatures and other key variables of each node in the finite element mesh are determined based on boundary conditions, thermo mechanical properties of the work piece materials and possibly solutions at previous steps. Other state variables are derived from these key values and updated for each time increment. The length of this time step and number of steps simulated are determined based on the information specified in the step controls menu. Fig. 36.2.21. shows simulation control options.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image014.jpg' | relative_url }})

Simulation controls window in system definition

User needs to specify the time per step (step definition), total number of steps and step increment to save in user and system step definition. In heat transfer express three types of step definitions are available, those are system, user and auto.

**System** type (See Fig. 36.2.21.) step definition auto calculate the step definition based on the heating time defined and accuracy and complexity settings selected. For different accuracy and complexity settings system will vary the object mesh elements and step size by varying number of steps. If user needs to vary the auto calculated step definition then User type allows to change the step definition.

In **User** type user will get the access to change the step definitions as required as shown in Fig. 36.2.22.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image015.jpg' | relative_url }})

User step definition controls

Auto type is temperature based step controls, the DTPMAX settings control the time stepping. The purpose for these controls is to specify the time stepping of a simulation that is driven by thermal-induced deformation. User has to specify the Initial time step (Time per step), Max. Temperature change per step, Min. time per step and Max. time per step as shown in Fig. 36.2.23.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image016.jpg' | relative_url }})

Advanced step definition controls

**Temperature change per step (DTPMAX) [2D, 3D]:**

The maximum temperature change increment limits the amount that the temperature of any node can change during one time step. If a non-zero value is assigned, a new sub step will be initiated when the temperature change at any node reaches the value of DTPMAX. The maximum/minimum time step are the largest and smallest time step allowable with the temperature based sub-stepping.

### Generate Database

**Check Data**![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }})****

It checks the Data. If Data is correct we can generate DB. But while checking Data if it gives any errors or warnings then it should be corrected before generating Database. Errors will not allow the database to be generated while warnings will allow the DB to be generated.

**Generate Database![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }})**

By clicking on this button, it generated the Database for the setup. (See Fig. 36.2.24.)

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image050.jpg' | relative_url }})

Generate Database window

## Defining Heat Transfer Operation

Heat Transfer operation is used to setup the air convection operation normally during the transfer of workpiece from furnace to press. User can add this operation after heating operation or start with heated workpiece heat transfer itself as first operation. In Transfer operation user will be guided by setup windows as in Heating operation except heating Stopping controls as shown in Fig. 36.2.25. For basic object definition, geometry, mesh, material and boundary condition details refer Defining Heating operation. In addition to heating operation options user can add more than one object, so it adds object positioning and inter-object definition options. These options are discussed under this section.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_2_3d_heat_transfer_express/image007.jpg' | relative_url }})

Add Heat transfer operation after furnace heating

### Selecting Objects

In Heat Transfer operation more than one object is allowed. The user can select the number of objects that is required to perform the operation from this window depending on the process set up (See Fig. 36.2.26.). User has to note that we can have only one plastic object in a simulation. A maximum of 100 dies can be added.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_2_3d_heat_transfer_express/image008.jpg' | relative_url }})

Transfer operation object selection settings

### Objects positioning and generating inter object relation

If user selects more than one object then system adds the controls (positioning) and scheduled positioning and contact windows after objects to position the objects and to generate inter object contact if any in the setup. More details about these options refer [Defining Rest on die operation](36_1_2d_heat_transfer_express.htm#36_1_5_Defining_Rest_on_die_Operation) section [Positioning](36_1_2d_heat_transfer_express.htm#Positioning) and [Scheduled Positioning](36_1_2d_heat_transfer_express.htm#Schedule_Positioning).

### Heat condition Definition

Heat conditions like Transfer time (Process duration), Environment temperature and Convection coefficient has be defined in this window as shown in Fig. 36.2.27. For all heating types system by default define the heating conditions, user has to input the process settings data by changing the defaults.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image019.jpg' | relative_url }})

Transfer operation heat conditions

After setting the heat condition user has to define the simulations controls for simulation controls settings details refer Simulation Controls Definition.

Next Database has to be generated in case interactive setup or if the transfer operation is first operation, otherwise database will automatically generate during simulation. For more information on simulation controls and Database generation refer [Simuation controls Definition](36_1_2d_heat_transfer_express.htm#Simulation_controls_Definition) and [Generate Database](36_1_2d_heat_transfer_express.htm#Generate_Database) section.

## Defining Rest on Die Operation

Rest on die or Resting operation is used to setup the hot workpiece heat transfer with environment and with die on which it is resting before forming. User can add this operation after heat transfer operation or can start with heated workpiece resting operation itself as first operation. In Resting operation user will be guided by setup windows as in Heating operation except heating Stopping controls as shown in Fig. 36.2.28\. In addition to heating operation options user can add more than one object, so it adds thermal calculation, object positioning and inter-object definition options. These options are discussed under this section.

By default system will add two die objects and thermal calculations selection option gets added after process window as shown in Fig. 36.2.28.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_2_3d_heat_transfer_express/image009.jpg' | relative_url }})

Adding Resting operation after heat transfer operation

### Define Thermal Calculations

Temperature Calculation (See Fig. 36.2.29.) window gives Non isothermal options to select calculate temperature only in workpiece or workpiece and dies.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image021.jpg' | relative_url }})

Temperature calculation type selection window

**Non-isothermal** : A process in which the temperature of system is not constant. Adding temperature calculations will improve material flow predictions and load predictions, particularly in processes where there are substantial changes in temperature. Calculating temperature in tools further improves workpiece temperature calculation, because evolving tool temperature influences heat loss from the workpiece.

### Selecting objects

The user can select the number of objects that is required to perform the operation from this window depending on the process set up (See Fig. 36.2.30.). User has to note that we can have only one plastic object in a simulation. A maximum of 100 dies can be added.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image022.jpg' | relative_url }})

Objects selection window

For [basic object definition](36_1_2d_heat_transfer_express.htm#Object_Basic_definition), [geometry](36_1_2d_heat_transfer_express.htm#Object_geometry_definition), [mesh](36_1_2d_heat_transfer_express.htm#Object_Mesh_Definition), [material](36_1_2d_heat_transfer_express.htm#Material_Definition) and [boundary condition](36_1_2d_heat_transfer_express.htm#Boundary_Condition_Definition) details refer 36.2.4. Defining Heating operation.

### Positioning

User has to select position objects button to position the objects as per the setup requirements, if objects are not read from DB as shown in Fig. 36.2.31. For more details about positioning options refer [19.Object Positioning](/docs/en/pre_processor/19_object_positioning/19_object_positioning/). If objects are read from DB then those objects positioning must be scheduled.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_2_3d_heat_transfer_express/image010.jpg' | relative_url }})

Positioning Objects window settings for Read from DB and other object types

### Schedule Positioning

When user is not sure about the location of an object as in case of Read From DB objects, scheduled positioning will help to position the objects accurately.

Schedule positioning allows the user to define the positioning for objects in MO setup for successive operations for which DB is not generated so that the objects will position before generation of DB while running simulation in Batch mode. (See Fig. 36.2.32.)

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_2_3d_heat_transfer_express/image011.jpg' | relative_url }})

Schedule position the objects in successive operations

### Inter-object Contact Generation

The purpose of inter-object relations is to define how the different objects in a simulation interact with each other. All objects which may come in contact with each other through the course of the simulation must have a contact relation defined. In Heat transfer express system automatically define the relation between the workpiece and dies and self contact for workpiece then generate contact when user click on as shown in Fig. 36.2.33. Generated contacts message will display in the message tab below the graphics window.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_2_3d_heat_transfer_express/image012.jpg' | relative_url }})

Inter-object contact generation window settings in batch mode

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_2_3d_heat_transfer_express/image013.jpg' | relative_url }})

Inter-object contact generation window settings in interactive mode (or for first  
operation) 

In case if heat transfer express operation is a successive operation then in batch mode system schedule the defining and generating contacts by initializing previous contacts while running, so generate and initialize contact nodes and restore mesh options not available as shown in Fig. 36.2.34. User can select the tolerance value for contact generation by selecting the User defined radio button.

  
Conduction heat transfer coefficient value can be defined by user and also typical values are provided by system those are, (See Fig. 36.2.33.)  
(1 N/sec/mm/C or 0.0003 Btu/sec/in^2/F) for Free Resting  
(1 N/sec/mm/C or 0.0003 Btu/sec/in^2/F) for Dwelling  
(11 N/sec/mm/C or 0.004 Btu/sec/in^2/F) for Forming

### Heat Condition Definition

Heat conditions like Resting time (Process duration), Environment temperature and Convection coefficient has be defined in this window as shown in Fig. 36.2.35. For all heating types system by default define the heating conditions, user has to input the process settings data by changing the defaults.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image027.jpg' | relative_url }})

Heat condition settings window

After setting the heat condition user has to define the simulations controls for simulation controls settings details refer Simulation Control Definition.

  
Next Database has to be generated in case interactive setup or if the transfer operation is first operation, otherwise database will automatically generate during simulation. For more information on simulation controls and Database generation refer [Simuation controls Definition](36_1_2d_heat_transfer_express.htm#Simulation_controls_Definition) and [Generate Database](36_1_2d_heat_transfer_express.htm#Generate_Database) section.

## Continue Defining the Forming Operations

After the Heat transfer express operations user can add the forming operations (See Fig. 36.2.36.) and continue with the non-isothermal deformation setup. Heat transfer operations can also be added between the forming operations, especially after forming operation customized Heat Dwelling heating type available for dwelling simulation explained in the next section Defining dwell on die operation. For more information about forming operations setup refer [3D Forming Setup](/docs/en/operation_templates/33_forming/33_2_3d_forming_setup/) or [3D Forming Express setup](/docs/en/operation_templates/34_forming_express/34_2_3d_forming_express_setup/).

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_2_3d_heat_transfer_express/image014.jpg' | relative_url }})

Adding Forming operation after heat transfer express operation

### Defining Dwell on dies Operation

Dwell on die or Dwelling operation is used to setup the hot workpiece heat transfer with environment and with die after forming and before die retract back from workpiece. User has to add this operation after forming operations as shown in Fig. 36.2.37.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_2_3d_heat_transfer_express/image015.jpg' | relative_url }})

Adding Heat transfer express operation after forming operation for dwelling operation  
setup 

In Dwelling operation user will be guided by setup windows as in Heating operation except heating Stopping controls as shown in Fig. 36.2.20. In addition to heating operation more than one objects are allowed and system automatically pass all the objects from previous operation to this operation. This operation also adds thermal calculation, object positioning and inter-object definition options required to select the thermal calculations for dies, position objects and define and generate the inter-object contact conditions. These additional options other than heating operation options are discussed in 36.2.6. Defining Rest on die Operation.

### Heat Condition Definition

Heat conditions like Dwell time (Process duration), Environment temperature and Convection coefficient has be defined in this window as shown in Fig. 36.2.38. For all heating types system by default define the heating conditions, user has to input the process settings data by changing the defaults.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image030.jpg' | relative_url }})

Heat condition settings window

After setting the heat condition user has to define the simulations controls for simulation controls settings details refer Simulation Control Definition.

  
Next Database has to be generated in case interactive setup or if the transfer operation is first operation, otherwise database will automatically generate during simulation. For more information on simulation controls and Database generation refer [Simuation controls Definition](36_1_2d_heat_transfer_express.htm#Simulation_controls_Definition) and [Generate Database](36_1_2d_heat_transfer_express.htm#Generate_Database) section.

**Related Topics:**

[3D Forming Setup](/docs/en/operation_templates/33_forming/33_2_3d_forming_setup/)

[3D Forming Express Setup](/docs/en/operation_templates/34_forming_express/34_2_3d_forming_express_setup/)

[2D Heat Transfer Express Operation](/docs/en/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/)

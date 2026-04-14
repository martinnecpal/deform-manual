---
lang: en
title: "36.1. 2D Heat Transfer Express"
---

# 36.1. 2D Heat Transfer Express

36.1.1. How to add 2D Heat Transfer Express operation

36.1.2. Process settings definition

36.1.3. Defining Heating operation

  * Object Basic definition

  * Object geometry definition

  * Object Mesh Definition

  * Material Definition

  * Boundary Condition Definition

  * Heat Condition Definition

  * Stopping controls Definition

  * Simulation controls Definition

  * Generate Database

36.1.4. Defining Transfer Operation

  * Selecting Objects

  * Objects positioning and generating inter object relation

  * Heat condition Definition

36.1.5. Defining Rest on die Operation

  * Define Thermal Calculations

  * Selecting objects

  * Positioning

  * Schedule Positioning

  * Inter-object Contact Generation

  * Heat Condition Definition

36.1.6. Continue Defining the Forming Operations

36.1.7. Defining Dwell on die Operation

  * Heat Condition Definition

## How to add 2D Heat Transfer Express operation

Heat Transfer Express operation is accessible from MO Wizard that can be opened from Main GUI. Heat Transfer Express Operation can be added in MO wizard, from explorer tab by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button next to 2D Heat Transfer Express. Also, user can add by drag and drop into the Operation Editor as shown in Fig. 36.1.1. Heat Transfer express operation can also be added after the Heat transfer operations interactively after the simulation of preceding operations or in batch/scheduled mode.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image001.jpg' | relative_url }})

Added 2D Heat Transfer Express operation into operation editor

## Process settings definition

In Process window simulation modes such as Geometry Type, Heating Type and Shape Complexity and Accuracy has to set for the heat transfer operation as shown in Fig. 36.1.1.

**Geometry Type**

In Forming express only two geometry models can be setup, those are Axisymmetric and Plane Strain.

The Axisymmetric models as a cross-section with respect to the central axis. Therefore, the model requires the deforming geometry to be axially symmetric and in the first quadrant and fourth quadrant (i.e. X > 0). In addition, the system assumes that the flow in every radial plane is identical. (See [Fig. 9.1.2.](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#Fig._9.1.2._Example_for_types_of_geometry_model))

The Plane-strain assumes that the geometry to have an unit depth with both front and back faces constrained. The simulation assumes that the objects will behave identically in any given cross-section across the width and height of the object. (See [Fig. 9.1.2.](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#Fig._9.1.2._Example_for_types_of_geometry_model))

Other Geometry types Plane-stress and Torsion are available only in 2D Forming operation, For more information about these geometry types please refer [9.1.2. Geometry type (GEOTYP](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#9.1.2._Geometry_type_\(GEOTYP\)_\[2D\])).

  
**Heating Type**

There are four heating types or heat transfer operations available in both 2D and 3D Heat Transfer Express operation those are (See Fig. 36.1.1.),

  * Heating

  * Transfer

  * Rest on die and

  * Dwell on die

Heating workpiece, heat transfer during transferring workpiece form furnace to press, resting workpiece on die (before forming) and workpiece dwell on die after forming operations can be setup easily by using the respective heating type. For more details about these heating types are described in [36\. Introduction to Heat transfer express operation](/docs/en/operation_templates/36_heat_transfer_express/36_introduction_to_heat_transfer_express_operations/), refer Heating Types.

For resting and dwelling operation thermal calculation window will activate to give options to select heat transfer with dies and not to calculate heat transfer with dies. These options will be explained further in respective operations explanations.

**Shape Complexity and Accuracy**

The shape complexity and simulation accuracy slider bars (See Fig. 36.1.1.) influence the mesh settings and number of time steps used in the simulation. This in turn influences the run time and level of detail available in the simulation.

**Shape Complexity:**

  * **Simple** : The geometry of the objects are simple in nature. They require minimum number of elements, are easier to solve and takes less time.

  * **Moderate** : The geometry of the objects are moderate (not too complex) in nature.

  * **Complex** : The geometry of the objects are complex in nature.

**Shape Accuracy:**

  * **Fast** : Useful for fast evaluation of a process. In exchange for faster run times, there is a higher risk of missing important details.

  * **Moderate** : The simulation uses settings which attempt to balance calculation time and accuracy.

  * **Accurate** : Very detailed analysis of the process is done, which will generally capture minute details. Calculation time and storage requirements are more.

## Defining Heating operation

In heating or heat furnace operation, heating of billet in a furnace is modeled. After selecting the process settings system will gives the customized heating operation windows to guide the user to setup this operation. Only one object is allowed for this operation (See Fig. 36.1.2.) and that object will be added automatically. The default process settings will be added suited to heating operation.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image002.jpg' | relative_url }})

Heating operation object definition window

### Object Basic definition

Object basic definition includes object name, type and temperature. In addition to this object state variable values can be initialized by using Advanced button and object data like geometry, mesh, boundary conditions and material can be imported from DEFORM .DB /.Key file. (See Fig. 36.1.3.)

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image003.jpg' | relative_url }})

Workpiece window

**Object Name** : User can define the name for all the objects available in the operation.

**Object Type** : The object type (OBJTYP) defines if and how deformation is modeled for each individual object in a DEFORM problem. In Forming Express operation only two object type are available those are Plastic and Rigid and those two are automatically predefined by object number, so workpiece will be plastic and dies will be rigid. More object types are available in Forming operation, for its details refer [11.4. Object Type](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4._Object_type)

  
**Plastic** : Plastic objects are modelled as rigid-plastic or rigid-viscoplastic material depending on characteristics of materials. The formulation assumes that the material stress increases linearly with strain rate until a threshold strain rate, referred to as the limiting strain rate ([LMTSTR](/docs/en/keyword_documentation/l/lmtstr/)). The material deforms plastically beyond the limiting strain rate. The plastic material behaviour of the object is specified with a material flow stress function or flow stress data ([FSTRES](/docs/en/keyword_documentation/f/fstres/)). In heat transfer express workpiece is automatically assigned to Plastic object type.  
**Rigid** : Rigid objects are modelled as non-deformable materials. In the deformation analysis, the object is represented by the geometric profile ([DIEGEO](/docs/en/keyword_documentation/d/diegeo/)). Deformation solution data available for rigid objects include object stroke, load, and velocity. The mesh for the rigid object is used only for thermal, transformation, and diffusion calculations. In heat transfer express dies or tools are automatically assigned to Rigid as they are non-deformable objects.

**Note:**

Should note that object type is predefined by object number in Heat transfer Express operation. For 1st object type will be plastic and for further addition only rigid objects will add.  
There is an Import Object button on the Object page. This is for importing complete object data from another DEFORM file.

**Object Temperature** : User can define the object temperature in the Temperature field of the respective object window as shown in Fig. 36.1.3.

Advanced Object Settings: The advanced setting Initialization options (See Fig. 36.1.4.) will be useful when user import the object from previously run project or problem or when forming express operation is added after few other operations and if there is need to initialize few important state variables.

  
The user can initialize temperature, strain, velocity, damage and displacement that has taken place in the deformable object using the advanced setting options. (See Fig. 36.1.4.)

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image004.jpg' | relative_url }})

Advanced object settings

More variables can be initialized in Forming operation, for detail refer [35\. 2D Heat Transfer](/docs/en/operation_templates/35_heat_transfer/35_1_2d_heat_transfer_operation/) operation [Initialize](../35_heat_transfer/35_1_2d_heat_transfer_operation.htm#Initialize).

The average strain rate ([AVGSTR](/docs/en/keyword_documentation/a/avgstr/)) is a characteristic average value of the effective strain rate. An approximation of this value should be given at the start of the simulation.

The limiting strain rate ([LMTSTR](/docs/en/keyword_documentation/l/lmtstr/)) defines a limiting value of effective strain rate below which a plastic or porous material is considered rigid and behaves as Newtonian fluid like material.

![]({{ '/assets/icons/pre_icons/mo_reset_button.jpg' | relative_url }}) : Using this user can rest back the initialized state variables value.

For more Deformation object properties options available in Forming operation refer [16.1. Deformation Properties.](/docs/en/pre_processor/16_object_properties/16_1_deformation_properties/)

### **Object geometry definition**

Geometry window is used to create the geometry of an object as shown in Fig. 36.1.5. Before creating geometry only Define Primitive and Edit Geometry options are available but after creating geometry Check, Scale and Reverse geometry options will activate and after generating mesh Extract border option will activate.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image005.jpg' | relative_url }})

Geometry definition window

**Define primitive![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }})**

  * **For Axisymmetric Type** : There are five primitive shapes in geometry primitive page that can be used to generate geometries as shown in Fig. 36.1.6. In each case, the user has to scale appropriately to the problem by defining the dimensions.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image011.jpg' | relative_url }})

Geometry primitive window for Axisymmetric geometry type

  * **For Plane strain Type** : There are three primitive shapes in geometry primitive page that can be used to generate geometries as shown in Fig. 36.1.7. In each case, the user has to scale appropriately to the problem by defining the dimensions.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image012.jpg' | relative_url }})

Geometry primitive window for Plane strain geometry type

**Check**![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }})

Once the geometry of the object is created, ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) button gets activated. It is necessary to check the orientation of the geometry. This can be done by clicking on the ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) button. Check and correct Geometry window appears as shown in below Fig. 36.1.8. The Geometry gets corrected, if they are any errors, when we click on ![]({{ '/assets/icons/pre_icons/mo_check_and_correct_geo_button.jpg' | relative_url }}) button. A message saying, "Geometry is legal" will appear once the geometry is corrected or does not have any errors and then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) . For more information please refer [12.1. 2D Geometry Data Defining](/docs/en/pre_processor/12_geometry_modelling/12_1_2d_geometry_data_defining/) section [Check Geometry](../../pre_processor/12_geometry_modelling/12_1_2d_geometry_data_defining.htm#Check_Geometry). 

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image006.jpg' | relative_url }})

Check and correct Geometry window

**Scale**![]({{ '/assets/icons/pre_icons/mo_scale_label.jpg' | relative_url }})

Geometry can be scaled in forming operation to accommodate thermal expansion by specifying the scaling factor. (See Fig. 36.1.9.) The scaling factor can be calculated by temperature differential and temperature dependent material data. The scaled geometry can be saved into different Geometry saving formats.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image014.jpg' | relative_url }})

Scale Geo window

**Reverse![]({{ '/assets/icons/pre_icons/mo_reverse_label.jpg' | relative_url }})**

This feature reverses the orientation of the geometry. Orientation of the 2D geometry must be always inside for single loop geometry, for multiple loop geometry the loop which share between the two regions can have the orientation on either side but topology must be defined.

**Extract Border![]({{ '/assets/icons/pre_icons/mo_extract_border_button.jpg' | relative_url }})**

This feature extracts the geometry data from the current database meshed object for all object types except the rigid object.

**Edit![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}) **

The Geometry editing option is used to create geometry for an object or edit the existing geometry. Imported geometry can be modified in Edit Geometry window. In Geometry page click on ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}) label and observe the options available to create and modify the geometry as shown in Fig. 36.1.10.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image007.jpg' | relative_url }})

Edit Geometry Window

Geometry can be created by using the create loop tool or by entering the geometry coordinates in Geometry editor table at right side bottom of the window as shown in Fig. 36.1.10. either in XYR or Line-Arc mode. For more details on 2D geometry editor refer the chapter [12.2. 2D Geometry Data Editing](/docs/en/pre_processor/12_geometry_modelling/12_2_2d_geometry_editing/).

**Other Geometry options:**

**Show geometry inside mark:** Checking this option enables the Geometry orientation display.

**Define reference point** : User can select the geometry reference point by clicking on this button from display window. This reference point is required to define the distance between objects stopping controls stopping controls.

**Import Geometry from a file** ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}): It imports the geometry from a file  
**Load Geometry from Library** ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) :It imports geometry from Library  
**Save the Geometry to a file** ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}) : It saves the Geometry to a file.  
**Save Geometry to Library** ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}) : User can save geometry to the library using this option.  
**Delete Geometry** ![]({{ '/assets/icons/pre_icons/mo_clear_icon.jpg' | relative_url }}): user can delete the geometry.

### Object Mesh Definition

The Mesh Generation window allows the user to generate a mesh for the current object. Below Fig. 36.1.11. shows the Mesh generation window in system mode. In this mode system automatically sets the number of mesh elements based on the shape complexity and accuracy setting selection in process window.

**System****Mode** : Using ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) user has to generate mesh for objects and after generating the mesh **![]({{ '/assets/icons/pre_icons/mo_delete_button.jpg' | relative_url }})** Mesh button will get activate, useful to delete the current mesh of the object.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image008.jpg' | relative_url }})

Mesh settings window in System mode

**User Defined Mode** : For user defined mesh mode option see Fig. 36.1.12., in this mode user can vary number of elements by adjusting the slider bar and use advanced options to change the Size ratio, Thickness elements, Weighting factor and Remesh criteria.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image009.jpg' | relative_url }})

User defined mode mesh settings

**Number of elements (MGNELM)**

The number of mesh elements represents the approximate number of elements that will be generated by the system. The Automatic Mesh Generator (AMG) takes the value for [MGNELM](/docs/en/keyword_documentation/m/mgnelm/) and generates a mesh that will contain approximately the same number of elements.

The error between the number of specified elements and the number of generated elements is typically about ten per-cent. When the mesh is generated, the specified total number of elements is used in conjunction with the "Point" and "Parameter" controls to determine the mesh density.

**Advanced Mesh Options**

**General Settings**

In addition to the Number of elements user can select Thickness elements and Size ratio values to get desired mesh.

  * **Number of thickness elements (MGTELM)**

The max thickness ratio is one of several ways to control the mesh density during automatic mesh generation (AMG). The number of elements in thickness direction represents the approximate number of elements that will be generated by the system across the thickness direction of any region of the part. The Automatic Mesh Generator (AMG) takes the value for [MGTELM](/docs/en/keyword_documentation/m/mgtelm/) and generates a mesh that will have that number of elements across the thinnest portion. For instance, if [MGTELM](/docs/en/keyword_documentation/m/mgtelm/) is set to 4, the AMG will try to have 4 elements across the thickness of the geometry.

The thickness direction of an object is perpendicular to a branched centre line axis for each region of the part. The total number of elements to be generated in a mesh is controlled by the value of number of elements in keyword [MGNELM](/docs/en/keyword_documentation/m/mgnelm/) . If the value of thickness elements results in a mesh that contains more than the value specified in [MGNELM](/docs/en/keyword_documentation/m/mgnelm/) elements, the value of [MGNELM](/docs/en/keyword_documentation/m/mgnelm/) would be scaled down so that the mesh contains approximately [MGNELM](/docs/en/keyword_documentation/m/mgnelm/) elements. If the value of [MGTELM](/docs/en/keyword_documentation/m/mgtelm/) results in a mesh that contains fewer than [MGNELM](/docs/en/keyword_documentation/m/mgnelm/) elements, the remaining elements will be distributed to other user specified mesh density controls (curvature, strain, strain rate, and temperature).

  * **Element size ratio (MGSIZR)**

The maximum size ratio between elements is one of several ways to control the mesh density during automatic mesh generation (AMG) by specifying the ratio of node densities.

For a value of 3 for [MGSIZR](/docs/en/keyword_documentation/m/mgsizr/), the largest element edge on an object will be roughly 3 times the size of the smallest element edge on the same object. If equal sized elements are desired, then Size Ratio = 1. If Size Ratio = 0, the element size ratio will not be a factor in the mesh density distribution.

**Weighing Factors**

The weighting factors or parameters (system defined mesh density) for boundary curvature, temperature, strain and strain rate specify relative mesh density weights to be assigned to the associated parameter. (See Fig. 36.1.13.)

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image018.jpg' | relative_url }})

Weighting factors settings window

Temperature, strain, and strain rate densities are assigned based on gradients in these parameters, not absolute parameter values. That is, a region with a rapid temperature change in a particular direction will receive more elements than a region with a uniform high temperature.

The values from all the mesh density keywords are combined during the mesh generation process to create a mesh density distribution within the geometric boundary. 

Forming operation contains other weighting factor that is, Mesh Density window options using this user can define specific area in space which will move with other objects during deformation with an appropriate mesh density, please refer [13.1.5. Mesh Weighting factors.](../../pre_processor/13_mesh_generation/13_1_2d_mesh_generation.htm#13.1.5._Mesh_weighting_factors)

**Remeshing criteria**

Remeshing Criteria (Autoremesh) is the most convenient way to handle the remeshing of objects undergoing large plastic deformation, so for heat transfer operations this is not applicable.

**Advanced Settings**

Below Fig. 36.1.14. shows the Advanced Settings window.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image020.jpg' | relative_url }})

Advanced mesh settings window

  * **Grid resolution (MGGRID)**

When an object is meshed in 2D, a sampling grid is required to discretize density of the mesh throughout the starting geometry. Grid resolution (MGGRID) specifies the spacing of the sampling grids that are used to sample mesh densities. Increasing the value of X division or Y division will result in sharper gradients between areas of differing mesh density. In the case of blanking, where a very high mesh gradient is required over a narrow region, these values may need to increase to capture high changes in mesh gradient over short distances.

  * **Node addition parameters (MGERR)**

The node addition parameters (MGERR) specify the maximum distance and angle error permitted between the object boundary and its associated grid element side. The distance and angle tolerances are used to capture critical boundary geometry that might otherwise be lost when the mesh is generated. If an object is required to capture very small features, the maximum distance can be decreased or if a node needs to be placed on a shallow angle, the angle error can be decreased as well. Rarely will the user ever have to change these values. For parts that are very small, a value of 0.01% of the object’s bounding box is a good starting number that can be used for MGERR for better handling of mesh resolution.

**Check Mesh![]({{ '/assets/icons/pre_icons/mo_check_mesh_button.jpg' | relative_url }}) **

The mesh can be examined for problems using the Check Mesh function. A perfect mesh will give the popup as shown in the Fig. 36.1.15., when user clicks on check mesh option. 

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_1_2d_mesh_generation/13_1_image003.jpg' | relative_url }})

Check mesh popup window

**Delete Mesh** ![]({{ '/assets/icons/pre_icons/mo_delete_mesh_button.jpg' | relative_url }})

Deletes the mesh generated for the object.

**Show mesh![]({{ '/assets/icons/pre_icons/mo_show_mesh_button.jpg' | relative_url }}) **

When user clicks on show mesh it shows the generated mesh in display window. Show mesh button toggles between display of mesh and geometry of the object.

**Default Setting** ![]({{ '/assets/icons/pre_icons/mo_default_settings_button.jpg' | relative_url }})  
When user clicks on Default settings tab all the settings will be changed to default values, by default Mesh window will be in greyed out mode as no mesh windows are defined. If user wants to activate mesh window, user has to change the weighting factor for mesh density by increasing the sliding bar value to 1.

More mesh options are available in forming operations and Pre-Processor refer [13.1. 2D Mesh Generation.](/docs/en/pre_processor/13_mesh_generation/13_1_2d_mesh_generation/)

### Material Definition

Below Fig. 36.1.16. shows the material window. User can add or import material from a keyword file or load from DEFORM material library.

  
After loading system automatically assign the loaded material to an object. User can also edit the material properties using ![]({{ '/assets/icons/pre_icons/mo_material_edit_button.jpg' | relative_url }}) button.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image010.jpg' | relative_url }})

Material window

Once after adding material click on ![]({{ '/assets/icons/pre_icons/mo_material_edit_button.jpg' | relative_url }}) button, material window will open as shown in Fig. 36.1.17.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image022.jpg' | relative_url }})

Material editing window

The properties required are dependent on the physical effects being simulated in DEFORM. The material properties that the user is required to specify is a function of the material types that the user is utilizing in the simulation. In Forming operation user can get access to all material properties for more information refer [10\. Material Data.](/docs/en/pre_processor/10_material_data/10_material_data/)

### Boundary Condition Definition

In heat transfer express Boundary conditions window, user can assign only Thermal Heat exchange with Environment and Temperature boundary constraints for an object. Boundary conditions specify how the boundary of an object interacts with other objects and with the environment. The most commonly used boundary conditions are heat exchange with the environment for simulations involving heat transfer. Fig. 36.1.18. shows various BCC that can be assigned to an object.

By default heat exchange with environment will be assigned to all surfaces except the symmetric surface (that is centerline) in axisymmetric model and for complete outer surface for plane strain model as shown in Fig. 36.1.18.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image011.jpg' | relative_url }})

Symmetry boundary condition assigned for workpiece

Defined BCC can be initialized first by selecting the BCC type in tree and clicking on ![]({{ '/assets/icons/pre_icons/mo_initialize_button.jpg' | relative_url }}) button. Defined particular BCC can also be deleted by selecting on defined branch from the BCC tree and clicking on ![]({{ '/assets/icons/pre_icons/mo_delete_bcc_button.jpg' | relative_url }}) button. Environment temperature can be varied from the Heat condition window. Environment windows are not allowed for heat exchange with environment BCC in heat transfer operation but available in forming operation, for more details refer Thermal under [14.3 Thermal Boundary Conditions](/docs/en/pre_processor/14_boundary_conditions/14_3_thermal_boundary_conditions/).

More thermal BCC options and other different BCC categories are available in Pre-Processor and Forming Operation such as [Deformation](/docs/en/pre_processor/14_boundary_conditions/14_2_deformation_boundary_conditions/),[Thermal](/docs/en/pre_processor/14_boundary_conditions/14_3_thermal_boundary_conditions/), [Diffusion](/docs/en/pre_processor/14_boundary_conditions/14_4_diffusion_boundary_conditions/) and [Heating](/docs/en/pre_processor/14_boundary_conditions/14_5_heating_boundary_conditions/). For more information about these BCC's please refer [14\. Boundary Conditions.](../../pre_processor/14_boundary_conditions)

### Heat Condition Definition

Heat conditions like Heating time (Process duration), Environment temperature and Convection coefficient has be defined in this window as shown in Fig. 36.1.19. For all heating types system by default define the heating conditions has to input the process settings data by changing the defaults.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image012.jpg' | relative_url }})

Heat condition settings window

### Stopping controls Definition

Only for heating operation heat transfer operation provides the stopping controls to stop the simulation when all nodes of the workpiece are within the specified degree range from the set point temperature or environment temperature as shown in [Fig. 36.1.20.]() In [Fig. 36.1.20.]() simulation stops if all nodes temperatures are within 1199.5 C to 1200.5 C.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image013.jpg' | relative_url }})

Heating stopping controls window

### Simulation controls Definition

The DEFORM system solves time dependent non-linear problems by generating a series of FEM solutions at discrete time increments. At each time increment, the velocities, temperatures and other key variables of each node in the finite element mesh are determined based on boundary conditions, thermo mechanical properties of the work piece materials and possibly solutions at previous steps. Other state variables are derived from these key values and updated for each time increment. The length of this time step and number of steps simulated are determined based on the information specified in the step controls menu. Fig. 36.1.21. shows simulation control options.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image014.jpg' | relative_url }})

Simulation controls window in system definition

User needs to specify the time per step (step definition), total number of steps and step increment to save in user and system step definition. In heat transfer express three types of step definitions are available, those are system, user and auto.

System type (See Fig. 36.1.21. ) step definition auto calculate the step definition based on the heating time defined and accuracy and complexity settings selected. For different accuracy and complexity settings system will vary the object mesh elements and step size by varying number of steps. If user needs to vary the auto calculated step definition then User type allows to change the step definition.

In User type user will get the access to change the step definitions as required as shown in Fig. 36.1.22.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image015.jpg' | relative_url }})

User step definition controls

Auto type is temperature based step controls, the ([DTPMAX)](/docs/en/keyword_documentation/d/dtpmax/) settings control the time stepping. The purpose for these controls is to specify the time stepping of a simulation that is driven by thermal-induced deformation. User has to specify the Initial time step (Time per step), Max. Temperature change per step, Min. time per step and Max. time per step as shown in Fig. 36.1.23.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image016.jpg' | relative_url }})

Advanced step definition controls

**Temperature change per step**(([DTPMAX](/docs/en/keyword_documentation/d/dtpmax/))  
The maximum temperature change increment limits the amount that the temperature of any node can change during one time step. If a non-zero value is assigned, a new sub step will be initiated when the temperature change at any node reaches the value of ([DTPMAX](/docs/en/keyword_documentation/d/dtpmax/). The maximum/minimum time step are the largest and smallest time step allowable with the temperature based sub-stepping.

### Generate Database

**Check Data**![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }})****

It checks the Data. If Data is correct we can generate DB. But while checking Data if it gives any errors or warnings then it should be corrected before generating Database. Errors will not allow the database to be generated while warnings will allow the DB to be generated.

**Generate Database![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }})**

By clicking on this button, it generated the Database for the setup. (See Fig. 36.1.24.)

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image050.jpg' | relative_url }})

Generate Database window

## Defining Transfer Operation

Heat Transfer operation is used to setup the air convection operation normally during the transfer of workpiece from furnace to press. User can add this operation after heating operation or start with heated workpiece heat transfer itself as first operation. In Transfer operation user will be guided by setup windows as in Heating operation except heating Stopping controls as shown in Fig. 36.1.25. For basic object definition, geometry, mesh, material and boundary condition details refer Defining Heating operation. In addition to heating operation options user can add more than one object, so it adds object positioning and inter-object definition options. These options are discussed under this section.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image017.jpg' | relative_url }})

Add Heat transfer operation after furnace heating

### Selecting Objects

In Heat Transfer operation more than one object is allowed. The user can select the number of objects that is required to perform the operation from this window depending on the process set up (See Fig. 36.1.26.). User has to note that we can have only one plastic object in a simulation. A maximum of 100 dies can be added.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image018.jpg' | relative_url }})

Transfer operation object selection settings

### Objects positioning and generating inter object relation

If user selects more than one object then system adds the controls (positioning) and scheduled positioning and contact windows after objects to position the objects and to generate inter object contact if any in the setup. More details about these options refer Defining Rest on die operation section Positioning and Scheduled Positioning.

### Heat condition Definition

Heat conditions like Transfer time (Process duration), Environment temperature and Convection coefficient has be defined in this window as shown in Fig. 36.1.27. For all heating types system by default define the heating conditions, user has to input the process settings data by changing the defaults.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image019.jpg' | relative_url }})

Transfer operation heat conditions

After setting the heat condition user has to define the simulations controls for simulation controls settings details refer Simulation Control Definition.

  
Next Database has to be generated in case interactive setup or if the transfer operation is first operation, otherwise database will automatically generate during simulation. For more information on simulation controls and Database generation refer Simuation controls Definition and Generate Database section .

## Defining Rest on die Operation

Rest on die or Resting operation is used to setup the hot workpiece heat transfer with environment and with die on which it is resting before forming. User can add this operation after heat transfer operation or can start with heated workpiece resting operation itself as first operation. In Resting operation user will be guided by setup windows as in Heating operation except heating Stopping controls as shown in Fig. 36.1.28\. In addition to heating operation options user can add more than one object, so it adds thermal calculation, object positioning and inter-object definition options. These options are discussed under this section.

By default system will add two die objects and thermal calculations selection option gets added after process window as shown in Fig. 36.1.28.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image020.jpg' | relative_url }})

Adding Resting operation after heat transfer operation

### Define Thermal Calculations

Temperature Calculation (See Fig. 36.1.29.) window gives Non isothermal options to select calculate temperature only in workpiece or workpiece and dies.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image021.jpg' | relative_url }})

Temperature calculation type selection window

**Non-isothermal** : A process in which the temperature of system is not constant. Adding temperature calculations will improve material flow predictions and load predictions, particularly in processes where there are substantial changes in temperature. Calculating temperature in tools further improves workpiece temperature calculation, because evolving tool temperature influences heat loss from the workpiece.

### Selecting objects

The user can select the number of objects that is required to perform the operation from this window depending on the process set up (See Fig. 36.1.30.). User has to note that we can have only one plastic object in a simulation. A maximum of 100 dies can be added.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image022.jpg' | relative_url }})

Objects selection window

For basic object definition, geometry, mesh, material and boundary condition details refer 36.1.3. Defining Heating operation.

### Positioning

User has to select position objects button to position the objects as per the setup requirements, if objects are not read from DB as shown in Fig. 36.1.31. For more details about positioning options refer [19.Object Positioning](/docs/en/pre_processor/19_object_positioning/19_object_positioning/). If objects are read from DB then those objects positioning must be scheduled.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image023.jpg' | relative_url }})

Positioning Objects window settings for Read from DB and other object types

### Schedule Positioning

When user is not sure about the location of an object as in case of Read From DB objects, scheduled positioning will help to position the objects accurately.

Schedule positioning allows the user to define the positioning for objects in MO setup for successive operations for which DB is not generated so that the objects will position before generation of DB while running simulation in Batch mode. (See [Fig. 36.1.32.]())

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image024.jpg' | relative_url }})

Schedule position the objects in successive operations

### Inter-object Contact Generation

The purpose of inter-object relations is to define how the different objects in a simulation interact with each other. All objects which may come in contact with each other through the course of the simulation must have a contact relation defined. In Heat transfer express system automatically define the relation between the workpiece and dies and self contact for workpiece then generate contact when user click on as shown in Fig. 36.1.33. Generated contacts message will display in the message tab below the graphics window.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image025.jpg' | relative_url }})

Inter-object contact generation window settings in batch mode

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image026.jpg' | relative_url }})

Inter-object contact generation window settings in interactive mode (or for first operation)

In case if heat transfer express operation is a successive operation then in batch mode system schedule the defining and generating contacts by initializing previous contacts while running, so generate and initialize contact nodes and restore mesh options not available as shown in Fig. 36.1.34. User can select the tolerance value for contact generation by selecting the User defined radio button.

  
Conduction heat transfer coefficient value can be defined by user and also typical values are provided by system those are, (See Fig. 36.1.33.)  
(1 N/sec/mm/C or 0.0003 Btu/sec/in^2/F) for Free Resting  
(1 N/sec/mm/C or 0.0003 Btu/sec/in^2/F) for Dwelling  
(11 N/sec/mm/C or 0.004 Btu/sec/in^2/F) for Forming

### Heat Condition Definition

Heat conditions like Resting time (Process duration), Environment temperature and Convection coefficient has be defined in this window as shown in Fig. 36.1.35. For all heating types system by default define the heating conditions, user has to input the process settings data by changing the defaults.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image027.jpg' | relative_url }})

Heat condition settings window

After setting the heat condition user has to define the simulations controls for simulation controls settings details refer Simulation Control Definition.

  
Next Database has to be generated in case interactive setup or if the transfer operation is first operation, otherwise database will automatically generate during simulation. For more information on simulation controls and Database generation refer Simulation_controls_Definition and Generate Database.

## Continue Defining the Forming Operations

After the Heat transfer express operations user can add the forming operations (See Fig. 36.1.36.) and continue with the non-isothermal deformation setup. Heat transfer operations can also be added between the forming operations, especially after forming operation customized Heat Dwelling heating type available for dwelling simulation explained in the next section 36.1.7. Defining dwell on die operation. For more information about forming operations setup refer [33.1. 2D Forming Setup](/docs/en/operation_templates/33_forming/33_1_2d_forming_setup/) or [34.1. 2D Forming Express Setup](/docs/en/operation_templates/34_forming_express/34_1_2d_forming_express_setup/).

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image028.jpg' | relative_url }})

Adding Forming operation after heat transfer express operation

## Defining Dwell on die Operation

  
Dwell on die or Dwelling operation is used to setup the hot workpiece heat transfer with environment and with die after forming and before die retract back from workpiece. User has to add this operation after forming operations as shown in Fig. 36.1.37.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image029.jpg' | relative_url }})

Adding Heat transfer express operation after forming operation for dwelling operation setup

In Dwelling operation user will be guided by setup windows as in Heating operation except heating Stopping controls as shown in Fig. 36.1.38. In addition to heating operation more than one objects are allowed and system automatically pass all the objects from previous operation to this operation. This operation also adds thermal calculation, object positioning and inter-object definition options required to select the thermal calculations for dies, position objects and define and generate the inter-object contact conditions. These additional options other than heating operation options are discussed in 36.1.5. Defining Rest on die Operation.

### Heat Condition Definition

Heat conditions like Dwell time (Process duration), Environment temperature and Convection coefficient has be defined in this window as shown in Fig. 36.1.38. For all heating types system by default define the heating conditions, user has to input the process settings data by changing the defaults.

![]({{ '/assets/images/operation_templates/36_heat_transfer_express/36_1_2d_heat_transfer_express/image030.jpg' | relative_url }})

Heat condition settings window

After setting the heat condition user has to define the simulations controls for simulation controls settings details refer Simulation Control Definition.

  
Next Database has to be generated in case interactive setup or if the transfer operation is first operation, otherwise database will automatically generate during simulation. For more information on simulation controls and Database generation refer Simulation_controls_Definition and Generate Database.

**Related Topics:**

[33.1. 2D Forming Setup](/docs/en/operation_templates/33_forming/33_1_2d_forming_setup/)

[34.1. 2D Forming Express Setup](/docs/en/operation_templates/34_forming_express/34_1_2d_forming_express_setup/).

[36.2.3D Heat Transfer Express Operation](/docs/en/operation_templates/36_heat_transfer_express/36_2_3d_heat_transfer_express/)

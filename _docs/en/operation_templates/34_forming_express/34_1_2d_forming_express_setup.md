---
lang: en
title: "34.1. 2D Forming Express Setup"
---

# 34.1. 2D Forming Express Setup

34.1.1. How to add 2D Forming Express operation

34.1.2. Process settings definition

34.1.3. Temperature Calculation settings

34.1.4. Select objects

34.1.5. Object Basic definition

34.1.6. Object geometry definition

34.1.7. Object Mesh Definition

34.1.8. Material

34.1.9. Boundary Conditions

34.1.10. Movement Controls

34.1.11. Positioning

34.1.12. Scheduled Positioning

34.1.13. Inter-Object relations

34.1.14. Defining Primary Die Stroke or Total Process Time

34.1.15. Stopping controls

34.1.16. Simulation controls

34.1.17. Generate DB

## How to add 2D Forming Express operation

**Forming Express operation is accessible by two ways** ,

  1. Forming express independent operation.

  2. Forming express MO Wizard Operation.

**For adding Forming express independent operation**

Create a new problem by selecting File ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) New Problem or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in See Fig. 34.1.1. Select the 2D Forming Express radio button. Then Define Problem Name, select Units system radio button in units field in New Problem popup and click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button for opening a new Problem using the Forming Express wizard.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image001.jpg' | relative_url }})

Adding Independent 2D Forming Express operation.

  
Then 2D Forming Express operation will open as shown in the Fig. 34.1.2.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image002.jpg' | relative_url }})

Independent Forming Express wizard

Here you can add or delete express operations and Simulation operators. Heat transfer express operations has been explained in section [36.1 Introduction to Heat Transfer Express](/docs/en/operation_templates/36_heat_transfer_express/36_introduction_to_heat_transfer_express_operations/).

2D to 3D converter operation has been explained in section [44.1. 2D to 3D Convertor](/docs/en/operation_templates/44_2d_to_3d_converter/44_1_2d_to_3d_converter/).

Boolean operations has been explained in section [45.1. Boolean Operator](/docs/en/operation_templates/45_boolean_operation/45_1_boolean_operation/)

Copy/Mirroring operation has been explained in section [46.1. Copy Mirroring](/docs/en/operation_templates/46_copy_mirroring/46_1_copy_mirroring/)

**For Adding Forming Express operation in Integrated Manufacturing Process (MO).**

Create a new problem either by selecting File ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) New Problem or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in Fig. 34.1.3. Select " Integrated Manufacturing Process" radio button and units system radio button in units field. Define Problem Name and click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Deform Integrated Manufacturing Process (MO).

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image003.jpg' | relative_url }})

Opening MO wizard

MO wizard will open, Forming Express Operation can be added in MO wizard from explorer tab by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button next to 2D Forming Express. Also, user can add by drag and drop into the Operation Editor as shown in Fig. 34.1.4. Forming express operation can also be added after the Heat transfer operations interactive or in batch/scheduled mode.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image004.jpg' | relative_url }})

Added 2D Forming Express operation into operation editor

## Process settings definition

In Process window simulation modes such as Geometry Type, Process Type and Shape Complexity and Accuracy has to set for the forming express operation as shown in Fig. 34.1.5.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image005.jpg' | relative_url }})

Process settings window

**Geometry Type**

In Forming express only two geometry models can be setup, those are Axisymmetric and Plane Strain.

The Axisymmetric models as a cross-section with respect to the central axis. Therefore, the model requires the deforming geometry to be axially symmetric and in the first quadrant and fourth quadrant (i.e. X > 0). In addition, the system assumes that the flow in every radial plane is identical. (See [Fig. 9.1.2.](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#Fig._9.1.2._Example_for_types_of_geometry_model))

The Plane-strain assumes that the geometry to have an unit depth with both front and back faces constrained. The simulation assumes that the objects will behave identically in any given cross-section across the width and height of the object. (See [Fig. 9.1.2.](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#Fig._9.1.2._Example_for_types_of_geometry_model))

Other Geometry types Plane-stress and Torsion are available only in 2D Forming operation, for details Refer [2D Forming Setup](/docs/en/operation_templates/33_forming/33_1_2d_forming_setup/).

**Process Type**

Three Process types Cold forming, Warm forming and Hot forging are available in Forming express. In Cold forming operation Heat transfer mode will be off, so no temperature calculation happens during simulation. In Warm and Hot forging types Heat transfer mode will be on and Temperature calculation window will activate. Temperature Calculation (See Fig. 34.1.5.) window gives options to select Isothermal and Non Isothermal setup.

**Shape Complexity and Accuracy**

The shape complexity and simulation accuracy slider bars (See Fig. 34.1.5.) influence the mesh settings and number of time steps used in the simulation. This in turn influences the run time and level of detail available in the simulation.

**Shape Complexity:**

  * **Simple** : The geometry of the objects are simple in nature. They require minimum number of elements, are easier to solve and takes less time.

  * **Moderate** : The geometry of the objects are moderate (not too complex) in nature.

  * **Complex** : The geometry of the objects are complex in nature.

  
**Shape Accuracy:**

  * **Fast** : Useful for fast evaluation of a process. In exchange for faster run times, there is a higher risk of missing important details.

  * **Moderate** : The simulation uses settings which attempt to balance calculation time and accuracy.

  * **Accurate** : Very detailed analysis of the process is done, which will generally capture minute details. Calculation time and storage requirements are more.

## Temperature Calculation settings

Temperature Calculation (See Fig. 34.1.6.) window gives options to select Isothermal and Non Isothermal setup. Isothermal to keep the temperature constant and Non isothermal to calculate temperature in only workpiece or workpiece and dies.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image006.jpg' | relative_url }})

Temperature Calculation type settings window

**Isothermal** : Simulation is treated as constant temperature. Changes in temperature due to deformation, heating or heat exchange with environment are ignored. Appropriate for processes where change in temperature do not significantly influence simulation results. Examples include: most cold forming processes and hot forming processes where the effect of temperature change is neglected for convenience. In this setup dies neither have mesh nor temperature calculation.  
**Non-isothermal** : A process in which the temperature of system is not constant. Adding temperature calculations will improve material flow predictions and load predictions, particularly in processes where there are substantial changes in temperature. Calculating temperature in tools further improves workpiece temperature calculation, because evolving tool temperature influences heat loss from the workpiece.

## Select objects

User can select the number of objects that is required to perform the operation from this window depending on the process set up (See Fig. 34.1.7.). User has to note that we can have only one plastic object in a simulation. A maximum of 100 dies can be added.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image007.jpg' | relative_url }})

Objects selection window

## Object Basic definition

Object basic definition includes object name, type and temperature. In addition to this object state variable values can be initialized by using Advanced button and object data like geometry, mesh, boundary conditions and material can be imported from DEFORM .DB /.Key file. (See Fig. 34.1.8.)

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image008.jpg' | relative_url }})

Workpiece window

  
**Object****Name** : User can define the name for all the objects available in the operation.

**Object****Type** : The object type ([OBJTYP](/docs/en/keyword_documentation/o/objtyp/)) defines if and how deformation is modeled for each individual object in a DEFORM problem. In Forming Express operation only two object type are available those are Plastic and Rigid and those two are automatically predefined by object number, so workpiece will be plastic and dies will be rigid. More object types are explained in chapter 11. General Object Data Definition, for details refer [11.4. Object Type](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4._Object_type).

  * **Plastic** : Plastic objects are modeled as rigid-plastic or rigid-viscoplastic materials depending on characteristics of materials. The formulation assumes that the material stress increases linearly with strain rate until a threshold strain rate, referred to as the limiting strain rate ([LMTSTR](/docs/en/keyword_documentation/l/lmtstr/)). The material deforms plastically beyond the limiting strain rate. The plastic material behavior of the object is specified with a material flow stress function or flow stress data ([FSTRES](/docs/en/keyword_documentation/f/fstres/)). In Forming Express operation workpiece is automatically assigned to Plastic object type.

  * **Rigid** : Rigid objects are modeled as non-deformable materials. In the deformation analysis, the object geometry is represented by a geometric profile ([DIEGEO](/docs/en/keyword_documentation/d/diegeo/)). Deformation solution data available for rigid objects include object stroke, load, and velocity. The geometric profile is used for all deformation analysis and the mesh for the rigid object is used for all thermal, transformation and diffusion calculations. In Forming Express, dies or tools are automatically assigned to Rigid as they are non-deformable objects.

**Note:**

Should note that object type is predefined by object number in Forming Express.

There is an Import Object button on the Object page. This is for importing complete object data from another DEFORM file.

**Object Temperature** : User can define the object temperature in the Temperature field of the respective object window as shown in Fig. 34.1.8.

  
**Advanced Object Settings** : The advanced setting Initialization options (See Fig. 34.1.9.) will be useful when user import the object from previously run project or problem or when forming express operation is added after few other operations and if there is need to initialize few important state variables.

  
The user can initialize temperature, strain, velocity, damage and displacement that has taken place in the deformable object using the advanced setting options. (See Fig. 34.1.9.)

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image009.jpg' | relative_url }})

Advanced object settings

More variables can be initialized in Forming operation, for detail refer [19\. Object Positioning](/docs/en/pre_processor/19_object_positioning/19_object_positioning/).

  
The average strain rate ([AVGSTR](/docs/en/keyword_documentation/a/avgstr/)) is a characteristic average value of the effective strain rate. An approximation of this value should be given at the start of the simulation.

The limiting strain rate ([LMTSTR](/docs/en/keyword_documentation/l/lmtstr/)) defines a limiting value of effective strain rate below which a plastic or porous material is considered rigid and behaves as Newtonian fluid like material.

  
![]({{ '/assets/icons/pre_icons/mo_reset_button.jpg' | relative_url }}) : Using this user can rest back the initialized state variables value.

  
For more Deformation object properties options available in Forming operation refer [16.1. Deformation Properties.](/docs/en/pre_processor/16_object_properties/16_1_deformation_properties/)

## Object geometry definition

Geometry window is used to create the geometry of an object as shown in Fig. 34.1.10. Before creating geometry only Define Primitive and Edit Geometry options are available but after creating geometry Check, Scale and Reverse geometry options will activate and after generating mesh Extract from mesh option will activate.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image010.jpg' | relative_url }})

Geometry definition window

**Define primitive![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }})**

  * **For Axisymmetric Type:** There are five primitive shapes in geometry primitive page that can be used to generate geometries as shown in Fig. 34.1.11. In each case, the user has to scale appropriately to the problem by defining the dimensions.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image011.jpg' | relative_url }})

Geometry primitive window for Axisymmetric geometry type

  * **For Plane strain Type:** There are three primitive shapes in geometry primitive page that can be used to generate geometries as shown in Fig. 34.1.12. In each case, the user has to scale appropriately to the problem by defining the dimensions.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image012.jpg' | relative_url }})

Geometry primitive window for Plane strain geometry type

**Check![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }})**

Once the geometry of the object is created, ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) button gets activated. It is necessary to check the orientation of the geometry. This can be done by clicking on the **![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }})**button. Check and correct Geometry window appears as shown in below Fig. 34.1.13. The Geometry gets corrected, if they are any errors, when we click on ![]({{ '/assets/icons/pre_icons/mo_check_and_correct_geo_button.jpg' | relative_url }}) button. A message saying, "Geometry is legal" will appear once the geometry is corrected or does not have any errors and then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). For more information please refer [Check Geometry](../../pre_processor/12_geometry_modelling/12_1_2d_geometry_data_defining.htm#Check_Geometry) in Chapter [12.1. 2D Geometry Data Defining](/docs/en/pre_processor/12_geometry_modelling/12_1_2d_geometry_data_defining/).

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image013.jpg' | relative_url }})

Check and correct Geometry window

**Scale![]({{ '/assets/icons/pre_icons/mo_scale_label.jpg' | relative_url }}) **

Geometry can be scaled in forming operation to accommodate thermal expansion by specifying the scaling factor. (See Fig. 34.1.14.) The scaling factor can be calculated by temperature differential and temperature dependent material data. The scaled geometry can be saved into different Geometry saving formats.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image014.jpg' | relative_url }})

Scale Geo window

**Reverse![]({{ '/assets/icons/pre_icons/mo_reverse_label.jpg' | relative_url }}) **

This feature reverses the orientation of the geometry. Orientation of the 2D geometry must be always inside for single loop geometry, for multiple loop geometry the loop which share between the two regions can have the orientation on either side but topology must be defined.

**Extract from mesh**![]({{ '/assets/icons/pre_icons/mo_extract_from_mesh.jpg' | relative_url }})****

This feature extracts the geometry data from the current database meshed object for all object types except the rigid object.

**Edit![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }})**

The Geometry editing option is used to create geometry for an object or edit the existing geometry. Imported geometry can be modified in Edit Geometry window. In Geometry page click on ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}) label and observe the options available to create and modify the geometry as shown in Fig. 34.1.15.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image015.jpg' | relative_url }})

Edit Geometry Window

Geometry can be created by using the create loop tool or by entering the geometry coordinates in Geometry editor table at right side bottom of the window as shown in Fig. 34.1.Fig. 34.1.15. either in XYR or Line-Arc mode. For more details on 2D geometry editor refer the chapter [12.2. 2D Geometry Data Editing](/docs/en/pre_processor/12_geometry_modelling/12_2_2d_geometry_editing/).

**Other Geometry options**

  * **Show Geometry inside mark** : Checking this option enables the Geometry orientation display.

  * **Define reference point** : User can select the geometry reference point by clicking on this button from display window. This reference point is required to define the distance between objects stopping controls stopping controls.

  * **Import Geometry from a file** ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) : Using this option user can import the geometry from a file.

  * **Load Geometry from Library** ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) : Using this option user can imports geometry from Library.

  * **Save the Geometry to a file** ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}): It saves the Geometry to a file.

  * **Save Geometry to Library** ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}): Using this option user can save geometry to the library.

  * **Delete Geometry** ![]({{ '/assets/icons/pre_icons/mo_clear_icon.jpg' | relative_url }}) : Using this option user can delete the geometry.

## Object Mesh Definition

The Mesh Generation window allows the user to generate a mesh for the current object. Below Fig. 34.1.16. shows the Mesh generation window in system mode. In this mode system automatically sets the number of mesh elements based on the shape complexity and accuracy setting selection in process window.

**System Mode** : Using **Generate Mesh** user has to generate mesh for objects and after generating the mesh **Delete** Mesh button will get activate, useful to delete the current mesh of the object.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image016.jpg' | relative_url }})

Mesh settings window in System mode

**User Defined Mode** : For user defined mesh mode option see Fig. 34.1.17., in this mode user can vary number of elements by adjusting the slider bar and use advanced options to change the Size ratio, Thickness elements, Weighting factor and Remesh criteria.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image017.jpg' | relative_url }})

User defined mode mesh settings

**Number of elements (MGNELM)**

The number of mesh elements represents the approximate number of elements that will be generated by the system. The Automatic Mesh Generator (AMG) takes the value for [MGNELM](/docs/en/keyword_documentation/m/mgnelm/) and generates a mesh that will contain approximately the same number of elements.

The error between the number of specified elements and the number of generated elements is typically about ten per-cent. When the mesh is generated, the specified total number of elements is used in conjunction with the "Point" and "Parameter" controls to determine the mesh density.

**Advanced Mesh Options**

**General Settings**

In addition to the Number of elements user can select Thickness elements and Size ratio values to get desired mesh.

  * **Number of thickness elements (MGTELM) :** The max thickness ratio is one of several ways to control the mesh density during automatic mesh generation (AMG). The number of elements in thickness direction represents the approximate number of elements that will be generated by the system across the thickness direction of any region of the part. The Automatic Mesh Generator (AMG) takes the value for [MGTELM](/docs/en/keyword_documentation/m/mgtelm/) and generates a mesh that will have that number of elements across the thinnest portion. For instance, if [MGTELM](/docs/en/keyword_documentation/m/mgtelm/) is set to 4, the AMG will try to have 4 elements across the thickness of the geometry.

The thickness direction of an object is perpendicular to a branched centre line axis for each region of the part. The total number of elements to be generated in a mesh is controlled by the value of number of elements in keyword [MGNELM](/docs/en/keyword_documentation/m/mgnelm/) . If the value of thickness elements results in a mesh that contains more than the value specified in [MGNELM](/docs/en/keyword_documentation/m/mgnelm/) elements, the value of [MGNELM](/docs/en/keyword_documentation/m/mgnelm/) would be scaled down so that the mesh contains approximately [MGNELM](/docs/en/keyword_documentation/m/mgnelm/) elements. If the value of [MGNELM](/docs/en/keyword_documentation/m/mgnelm/) results in a mesh that contains fewer than [MGNELM](/docs/en/keyword_documentation/m/mgnelm/) elements, the remaining elements will be distributed to other user specified mesh density controls (curvature, strain, strain rate, and temperature).

  * **Element size ratio (MGSIZR) :** The maximum size ratio between elements is one of several ways to control the mesh density during automatic mesh generation (AMG) by specifying the ratio of node densities.

For a value of 3 for [MGSIZR](/docs/en/keyword_documentation/m/mgsizr/), the largest element edge on an object will be roughly 3 times the size of the smallest element edge on the same object. If equal sized elements are desired, then Size Ratio = 1. If Size Ratio = 0, the element size ratio will not be a factor in the mesh density distribution.

**Weighing Factors**

The weighting factors or parameters (system defined mesh density) for boundary curvature, temperature, strain and strain rate specify relative mesh density weights to be assigned to the associated parameter.(See Fig. 34.1.18.)

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image018.jpg' | relative_url }})

Weighting factors settings window

Temperature, strain, and strain rate densities are assigned based on gradients in these parameters, not absolute parameter values. That is, a region with a rapid temperature change in a particular direction will receive more elements than a region with a uniform high temperature.

The values from all the mesh density keywords are combined during the mesh generation process to create a mesh density distribution within the geometric boundary.

Forming operation contains other weighting factor that is, Mesh Density window options using this user can define specific area in space which will move with other objects during deformation with an appropriate mesh density, please refer chapter [13.1.5. Mesh Weighting factors.](../../pre_processor/13_mesh_generation/13_1_2d_mesh_generation.htm#13.1.5._Mesh_weighting_factors)

**Remeshing criteria**

Remeshing Criteria (Autoremesh) is the most convenient way to handle the remeshing of objects undergoing large plastic deformation. The Remeshing Criteria Window (See Fig. 34.1.19.) contains a group of parameters that control when and how often the mesh will be regenerated on a meshed object based on assignment of certain triggers. There are four keywords that control the initiation of a remeshing procedure for an object, they are Interference Depth ([RMDPTH](/docs/en/keyword_documentation/r/rmdpth/)),Max. Time Increment ([RMTIME](/docs/en/keyword_documentation/r/rmtime/)), Max. Step Increment ([RMSTEP](/docs/en/keyword_documentation/r/rmstep/)) and Max. Stroke Increment ([RMSTRK](/docs/en/keyword_documentation/r/rmstrk/)). When the remeshing criteria of any of these keywords has been fulfilled or the mesh becomes unusable (negative Jacobian), the object will be remeshed. During the simulation, if an object satisfies any of its remeshing criteria, a new mesh is generated, the solution information from the old mesh is interpolated onto the new mesh and the simulation continues. For more information on Remesh Criteria, please refer [13.1.8. Remeshing criteria.](../../pre_processor/13_mesh_generation/13_1_2d_mesh_generation.htm#13.1.8._Remeshing_criteria)

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image019.jpg' | relative_url }})

Remeshing Criteria window

**Advanced Settings**

Below Fig. 34.1.20. shows the Advanced Settings window.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image020.jpg' | relative_url }})

Advanced mesh settings window

  * **Grid resolution ([MGGRID](/docs/en/keyword_documentation/m/mggrid/)) : **When an object is meshed in 2D, a sampling grid is required to discretize density of the mesh throughout the starting geometry. Grid resolution ( [MGGRID](/docs/en/keyword_documentation/m/mggrid/)) specifies the spacing of the sampling grids that are used to sample mesh densities. Increasing the value of X division or Y division will result in sharper gradients between areas of differing mesh density. In the case of blanking, where a very high mesh gradient is required over a narrow region, these values may need to increase to capture high changes in mesh gradient over short distances.

  * **Node addition parameters ([MGERR](/docs/en/keyword_documentation/m/mgerr/)) : **The node addition parameters ([MGERR](/docs/en/keyword_documentation/m/mgerr/)) specify the maximum distance and angle error permitted between the object boundary and its associated grid element side. The distance and angle tolerances are used to capture critical boundary geometry that might otherwise be lost when the mesh is generated. If an object is required to capture very small features, the maximum distance can be decreased or if a node needs to be placed on a shallow angle, the angle error can be decreased as well. Rarely will the user ever have to change these values. For parts that are very small, a value of 0.01% of the object’s bounding box is a good starting number that can be used for [MGERR](/docs/en/keyword_documentation/m/mgerr/)for better handling of mesh resolution.

**Check Mesh![]({{ '/assets/icons/pre_icons/mo_check_mesh_button.jpg' | relative_url }})**

The mesh can be examined for problems using the Check Mesh function. A perfect mesh will give the popup as shown in the Fig. 34.1.21., when user clicks on check mesh option.

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_1_2d_mesh_generation/13_1_image003.jpg' | relative_url }})

Check mesh popup window

**Delete Mesh**![]({{ '/assets/icons/pre_icons/mo_delete_mesh_button.jpg' | relative_url }})   
Deletes the mesh generated for the object.

**Show mesh** ![]({{ '/assets/icons/pre_icons/mo_show_mesh_button.jpg' | relative_url }})

When user clicks on show mesh it shows the generated mesh in display window. Show mesh button toggles between display of mesh and geometry of the object.

**Default Setting![]({{ '/assets/icons/pre_icons/mo_default_settings_button.jpg' | relative_url }})**

When user clicks on Default settings tab all the settings will be changed to default values, by default Mesh window will be in greyed out mode as no mesh windows are defined. If user wants to activate mesh window, user has to change the weighting factor for mesh density by increasing the sliding bar value to 1.

Coating mesh and User Mesh Density Window options are not available in Forming express operation unlike in Forming operation, for these options refer [13.1.7. Coating Mesh](../../pre_processor/13_mesh_generation/13_1_2d_mesh_generation.htm#13.1.7._Coating) and [ 13.1.6. Mesh Density windows](../../pre_processor/13_mesh_generation/13_1_2d_mesh_generation.htm#13.1.6._Mesh_density_windows) respectively.

## Material

Below Fig. 34.1.22. shows the material window. User can add or import material from a keyword file or load from DEFORM material library.

  
After loading system automatically assign the loaded material to an object. User can also edit Plastic and Thermal properties, those are Flow stress, Thermal Conductivity, Heat Capacity, Mass Density and Emissivity using ![]({{ '/assets/icons/pre_icons/mo_material_edit_button.jpg' | relative_url }}) button.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image021.jpg' | relative_url }})

Material window

Once after adding material click on ![]({{ '/assets/icons/pre_icons/mo_material_edit_button.jpg' | relative_url }}) button, material window will open as shown in Fig. 34.1.23.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image022.jpg' | relative_url }})

Material editing window

The properties required are dependent on the physical effects being simulated in DEFORM. The material properties that the user is required to specify is a function of the material types that the user is utilizing in the simulation. In chapter [10\. Material Data](/docs/en/pre_processor/10_material_data/10_material_data/) user can get access to all material properties for more information refer [10\. Material Data](/docs/en/pre_processor/10_material_data/10_material_data/).

## Boundary Conditions

In Forming express Boundary conditions window, user can assign only Deformation velocity and Thermal Heat exchange with Environment and Temperature boundary constraints for an object. Boundary conditions specify how the boundary of an object interacts with other objects and with the environment. The most commonly used boundary conditions are heat exchange with the environment for simulations involving heat transfer, prescribed velocity for enforcing symmetry in the model. Fig. 34.1.24. shows various BCC that can be assigned to an object.

  
By default velocity along the centerline of the workpiece object will be fixed in axisymmetric geometry type as shown inFig. 34.1. Fig. 34.1.24. . and also heat exchange with environment will be assigned to all surfaces except the symmetric surface for warm and hot forging process as shown in Fig. 34.1.25.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image023.jpg' | relative_url }})

Symmetry boundary condition assigned for workpiece

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image024.jpg' | relative_url }})

Heat exchange with environment boundary condition assigned for workpiece

The BCC’s are categorized as [Deformation](/docs/en/pre_processor/14_boundary_conditions/14_2_deformation_boundary_conditions/),[Thermal](/docs/en/pre_processor/14_boundary_conditions/14_3_thermal_boundary_conditions/), [Diffusion](/docs/en/pre_processor/14_boundary_conditions/14_4_diffusion_boundary_conditions/) and [Heating](/docs/en/pre_processor/14_boundary_conditions/14_5_heating_boundary_conditions/). For more information about these BCC's please refer [14\. Boundary Conditions.](../../pre_processor/14_boundary_conditions)

## Movement Controls

Movement controls can be applied to rigid objects and boundary nodes of meshed objects. The surface defined by these nodes can be thought of as a "rigid surface". During the simulation, the constrained nodes will move synchronously in the speed and direction defined by the movement controls. Only translational movement type is available in Forming express out of three types of Movement types available in 2D Environment (Forming operation) those are Translation, Rotation and Torsion.

**Translational Movement:**

During the simulation the constrained nodes will move synchronously in the speed and direction defined by the movement controls. (See Fig. 34.1.26.)

  
In Forming express only six types of Movement controls are available in Translation Movement type, those are [Speed](/docs/en/pre_processor/15_movement_controls_definition/15_1_speed/), [Load](/docs/en/pre_processor/15_movement_controls_definition/15_2_force/), [Hammer](/docs/en/pre_processor/15_movement_controls_definition/15_3_hammer/), [Screw press](/docs/en/pre_processor/15_movement_controls_definition/15_4_screw_press/), [Mechanical press](/docs/en/pre_processor/15_movement_controls_definition/15_5_mechanical_press/), [Hydraulic press](/docs/en/pre_processor/15_movement_controls_definition/15_6_hydraulic_press/). Forming operation contains [Sliding Die](/docs/en/pre_processor/15_movement_controls_definition/15_7_sliding_die/) and [Path](/docs/en/pre_processor/15_movement_controls_definition/15_8_path/) translational movement controls in addition to the forming express and also contains rotational and Torsional movement types, for more information refer [15\. Movement Controls.](/docs/en/pre_processor/15_movement_controls_definition/15_movement_controls_settings/)

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image025.jpg' | relative_url }})

Translational Movement controls window

The lower portion of the movement controls window (See Fig. 34.1.26.) allows the user to import movement specifications from other keyword or database files and to load press information from the library, save the movement controls to a file or movement library, observe the preview and delete the defined the movement definition. User can also load the movement from press library using explorer as shown in Fig. 34.1.26.

**Speed:** This is the default movement control. This specifies the speed and direction of a tool as shown in Fig. 34.1.26.

**Load/Force Control:** For force control, the speed of the object is constrained such that the specified load is maintained. When the object is rigid, the load is the resultant load applied by a non-rigid object due to the relative motion of the two objects. User need to specify the Load magnitude and direction as shown in Fig. 34.1.27.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image026.jpg' | relative_url }})

Load Movement controls settings

**Mechanical Press** : The Mechanical Press type replicates the cyclic motion of a mechanical press (See Fig. 34.1.28.). The "Mechanical Press" option simulates the motion of objects driven by a mechanical press. In Forming express only Mechanical Crank press control is available in addition to this knuckle press control will be available in Forming operation, for knuckle press information refer [15.5.2. Knuckle Press.](../../pre_processor/15_movement_controls_definition/15_5_mechanical_press.htm#15_5_2_Knuckle_or_Wedge_Press)

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image027.jpg' | relative_url }})

Mechanical movement control settings

If user defines the movement type for Primary Die as Mechanical Press then the movement control definitions for all other objects will be deleted and also user cannot define movement controls for other objects.

  
The parameters required to specify the movement of a mechanical press are:

**Total stroke** : The total stroke for the mechanical press represents the total travel of the die from its top position to its lowest position. The unit in English units is inch and in SI units is mm.

**Forming Stroke** : is the distance the primary die travels from operation start to bottom dead center.

**Current Stroke** : is a vector which shows the current distance travelled by the top die and it’s direction along the movement axis.

**Strokes per second** : The Strokes per seconds represents the frequency of the press blows. This is a measure of blows per second or cycles per second.

**Direction** : Direction is used to designate a direction in which the object's stroke will be applied.

**Connecting-Rod Len** gth: As seen in Fig 2.8.19, the connecting rod length can have an influence on the speed of the ram. If the length of the connecting rod is known, it can be input as a field. If it is not known, it can left as zero and its contribution to the ram speed will not be considered.

**Forming Stroke option** : Now Forming Stroke data can be defined in two ways:

**Exact forming stroke** : If the exact forming stroke option is chosen, forming stroke = primary die stroke value.

**Distance between dies** : If the distance between dies option is chosen, forging stroke = (current distance between defined points) – (stopping distance between defined points)

Editable ? | First operation | Next operation | Step Editor  
---|---|---|---  
Top die defined | Top die is Read form DB  
Type | Yes | Yes | Yes | No  
Direction | Yes | Yes | Yes | No  
Total stroke, stroke/sec, stiffness, and connecting rod length | Yes | Yes | Yes | No  
Forming stroke option | Yes | Yes | No* | No  
  
*If the top die is read from DB then the forming stroke option, forming stroke, and current stroke are hidden.

When total stroke is changed the current stroke will be recalculated to maintain the forming stroke value.

When importing a project from an older version the system will default to the exact forming stroke method. If a project with distance between dies stopping criteria is imported the system will switch to distance between dies method.

**Hammer Press :** Hammer forging operation is controlled by energy. During a working stroke, the deformation proceeds until the total kinetic energy is dissipated by plastic deformation of the material and by elastic deformation of ram and anvil when the die and ram faces contact each other.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image029.jpg' | relative_url }})

Hammer movement control settings

During hammer forging operation, only a portion of the kinetic energy of ram is used for the plastic deformation of work piece. The rest of the energy is lost through anvil and machine frame. These values can be set in the movement controls window.

  
There are basically two types of hammer. The first is an [anvil type hammer](../../pre_processor/15_movement_controls_definition/15_3_hammer.htm#15_3_1_Anvil_Type_Hammer) and the other [counter blow hammer](../../pre_processor/15_movement_controls_definition/15_3_hammer.htm#15_3_2_Counterblow_Hammer). The formulations and assumptions used for the two types of hammer forging operations refer [15.3. Hammer Energy.](/docs/en/pre_processor/15_movement_controls_definition/15_3_hammer/)

In an Anvil type hammer, the workpiece, together with the lower die set, is placed on an anvil which is stationary. In a simple gravity drop hammer, the ram is accelerated by gravity and accumulates energy.

A counterblow hammer can be specified for movement by selecting the Counter blow hammer checkbox as seen in Fig. 34.1.29. After this, the other moving hammer object can be specified as well as the mass of the other moving hammer. The mass of the objects do not have to be equal but the total energy is split between the two hammer dies.

Use blow table: Checking this option user can define the multiple hammer blows as shown in Fig. 34.1.30. In this window user has to select the number of hits and blow efficiency for each hit. Along with the blows user can select the reheating temperature after each blow, enter the dwell time and flip the workpiece in 2D. So dwell and transfer after each blow can be designed. The strain can also be initialized with reheat by checking the check box, this initializes the accumulated strain after the dwell with initializing to reheat temperature for workpiece.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image031.jpg' | relative_url }})

Multiple hammer blow settings table

For more details about Hammer press control refer [15.3. Hammer Energy.](/docs/en/pre_processor/15_movement_controls_definition/15_3_hammer/)

**Hydraulic press:** In Forming Express operation hydraulic press model (See Fig. 34.1.31.) have only Speed control. Forming operation contains the average strain rate control in addition to speed control, for its information refer [15.6. Hydraulic Press.](/docs/en/pre_processor/15_movement_controls_definition/15_6_hydraulic_press/). In addition to speed user can enter Power limit, Dwell time and Number of steps for Dwell.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image028.jpg' | relative_url }})

Hydraulic press movement control settings

**Note:**

To activate maximum speed control, the power limit must be defined.

For more details about Hydraulic press control refer to section [15.6. Hydraulic Press.](/docs/en/pre_processor/15_movement_controls_definition/15_6_hydraulic_press/)

**Screw Press**

The unique characteristic of a screw press (See Fig. 34.1.32.) is the method of driving it. A motor drives a flywheel which is either directly connected or can be connected to a screw spindle.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image030.jpg' | relative_url }})

Screw press movement control settings

The data required to run a screw press driven tool are:

**Energy:** The Blow Energy is a measure of the total energy that the flywheel will contain when the desired speed has been reached and prior to engaging the clutch. The units for blow energy in English units are klb-in and in SI units are N-mm.

  
**Blow Efficiency:** The Blow Efficiency represents the fraction of the total energy that will be converted to deformation energy. The rest of the energy is absorbed through the clutch mechanism, friction and the machine frame. There are no units for this quantity. In Forming express only constant value we can use but in forming operation user can also define function of force, for its more information refer [15.4. Screw Press.](/docs/en/pre_processor/15_movement_controls_definition/15_4_screw_press/)

  
**Moment of Inertia:** The Moment of Inertia is the moment of inertia of the flywheel. The English units of inertia are klb*in*s2 and the SI units are N-mm*s2. The mass moment of inertia for a circular disc with the Z-axis perpendicular to the center is I = 2 ET /ω2 where ET is the total energy of the flywheel, and ω is the angular  
velocity in radians per second.

  
**Ram Displacement or Lead screw pitch:** The Ram Displacement specifies the distance per revolution of the flywheel that the screw will advance. This helps in determining the linear velocity of the ram. The English units for Ram Displacement are inch/revolution, while the SI units are mm/revolution. If only the pitch angle and diameter of the spindle is known, the Ram Displacement can be calculated using πdsin(θt) where d is the diameter of spindle and θt is the pitch angle of the spindle.

  
**Use blow table:** Checking this option user can define the multiple blows as shown in Fig. 34.1.33. In this window user has to select the number of hits and blow efficiency for each hit. Along with the blows user can select the reheating after each blow, enter the dwell time and flip the workpiece in 2D. So reheating, transfer  
and dwell after each blow can be designed.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image032.jpg' | relative_url }})

Screw Press multiple blow settings table

For more details about Screw press refer [15.4. Screw Press.](/docs/en/pre_processor/15_movement_controls_definition/15_4_screw_press/)

## Positioning

Below Fig. 34.1.34. shows the positioning window.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image033.jpg' | relative_url }})

Object positioning window

**Automatic Positioning** ![]({{ '/assets/icons/pre_icons/mo_automatic_positioning_button.jpg' | relative_url }})

By clicking on this button, system automatically Positions the Objects with respect to the top die movement direction, this option works best for simple setup with three objects work piece, top die and bottom die.

When mechanical press is used as movement control type for primary die then auto-positioning  
is done in 2 steps:

  1. Interference position bottom die to workpiece while coupled with top die without updating stroke

  2. Interference position top die to workpiece while updating stroke.

System will always update stroke with positioning for the object that has mechanical press defined (top die). Update stroke check box should be hidden in express operations.

**Positioning Objects![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }})**

By clicking on this button, user can position the objects in required directions. Various types of Positioning Options are available such as [Drag](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_1_Drag_Positioning), [Offset](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_2_Offset_Positioning), [Interference](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_3_Interference_positioning), [Flip](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_6_Flip_positioning) and [Rotational](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_4_Rotational_positioning) as shown in Fig. 34.1.35. For more information about these options, please refer [19.Object Positioning.](/docs/en/pre_processor/19_object_positioning/19_object_positioning/)

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image034.jpg' | relative_url }})

Object positioning window

## Scheduled Positioning

When user is not sure about the location of an object as in case of Read From DB objects, scheduled positioning will help to position the objects accurately.

Schedule positioning allows the user to define the positioning for objects in MO setup for successive operations for which DB is not generated so that the objects will position before generation of DB while running simulation in Batch mode. (See Fig. 34.1.36.)

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image035.jpg' | relative_url }})

Scheduled Positioning window

## Inter-Object relations

The purpose of inter-object relations is to define how the different objects in a simulation interact with each other. All objects which may come in contact with each other through the course of the simulation must have a contact relation defined. In Forming express system automatically define the relation between the workpiece and dies and self contact for workpiece then generate contact when user click on ![]({{ '/assets/icons/pre_icons/mo_generate_contact_nodes_label.jpg' | relative_url }}) as shown in Fig. 34.1.37. Generated contacts message will display in the message tab below the graphics window.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image036.jpg' | relative_url }})

Contact generation window

User can select the Shear or Coulomb friction type and define the friction coefficient. The lubricant used on the tooling plays a large role in the amount of friction that exists between the tooling and workpiece. The friction in turn affects the metal flow at contact surfaces.

  
Typical values are provided for shear friction as shown below,

(0.08) for cold forming (carbide dies) processes

(0.12) for cold forming (Steel dies) processes  
(0.25) for warm forming processes  
( 0.3) for lubricated hot forging processes  
(0.7) for un lubricated (dry) hot forging processes  
(0.4) for Aluminium forming processes

Conduction heat transfer coefficient value can be defined by user and also typical values are provided by system those are,  
(1 N/sec/mm/C or 0.0003 Btu/sec/in^2/F) for Free Resting  
(1 N/sec/mm/C or 0.0003 Btu/sec/in^2/F) for Dwelling  
(11 N/sec/mm/C or 0.004 Btu/sec/in^2/F) for Forming

## Defining Primary Die Stroke or Total Process Time

Primary die stroke (See Fig. 34.1.38.) decides the total amount of die travel during an operation. It is an estimate of the total die stroke in an operation. It is used to establish time stepping values.  
Unless the "exact amount" box is checked, the approximate target tool movement will be roughly 125% of the specified value.  
Using the mouse pointer user can define the Primary Die-stroke value by selecting the two points on the objects.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image038.jpg' | relative_url }})

Total primary die stroke definition window

When user uses Load as movement controls then Total Process Time window comes instead of Primary die stroke, this time is used to estimate the stepping values.

**Primary Die stroke for Mechanical Press [Exact Forming stroke method]:**

For mechanical press, a valid range will be shown. (0 ~ ‘Total Stroke’) (See Fig. 34.1.39.)

If the Total primary die travel is 0 or outside of the valid range, then the input is illegal and the range will be displayed in red color.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image039.jpg' | relative_url }}) ![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image040.jpg' | relative_url }})

(a) In First Operation (b) In Next Operation 

Primary die stroke option with Exact Forming stroke method 

There are 3 ways to define exact forming stroke:

  1. User can enter exact forming stroke for Total primary die travel.

  2. User can press **Top dead center position** ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) tool or check Top dead center position in next operation if the current position of the die is at Top dead center. When user presses / checks the Top dead center position ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) tool, Exact amount will become unchecked in next operations. Forming stroke is set equal to total stroke. Automatic positioning is performed or scheduled. In the first operation, primary die travel will update with the correct forming stroke. In next operations forming stroke will update after scheduled positioning is performed.

| First Operation | Next operation | Step Editor  
---|---|---|---  
Top Die is defined | Top die is Read from DB  
**Total Primary die travel** | Displays Calculated Forming stroke | Approximate die travel which will be used to calculate DSMAX | N/A | N/A  
  
If a ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) button is used in the first operation, deactivate ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) buttons for both Top Dead Center and Bottom Dead Center until user revisits page. In next operation, if a wizard check box is selected the system will  
delete any prior scheduled positioning for objects 2 and 3.

  1. User can presses the **Bottom dead center** ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) tool or check Bottom dead center position in next operation if the current position of the die is at Bottom dead center. When user presses / checks the Top dead center position ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) tool, Exact amount will become unchecked in next operations. Forming stroke is set equal to 0. Automatic positioning is performed or scheduled. First operation will update primary die travel value with correct forming stroke. In Next operation will calculate correct forming stroke after scheduled positioning is performed.

| First Operation | Next operation | Step Editor  
---|---|---|---  
Top Die is defined | Top die is Read from DB  
**Total Primary die travel** | Displays Calculated Forming stroke | Approximate die travel which will be used to calculate DSMAX | N/A | N/A  
  
If either of both Top dead center and Bottom dead center ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) button is used in the first operation, both Top dead center and Bottom dead center ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) buttons are deactivated until user revisits page. 

**In Next operations:**

If a check box either for Top dead center and Bottom dead center is selected, the system will delete scheduled positioning for objects 2 and 3.  
If the BDC check box is checked, an error message that there is no interference positioning scheduled for the top die will be displayed.  
If the BDC check box is unchecked, an warning message that there is no interference positioning scheduled for the top die will be displayed.

**Primary Die stroke for Mechanical Press [ Distance between dies method]:**

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image041.jpg' | relative_url }}) ![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image042.jpg' | relative_url }})

(a) In First Operation (b) In Next Operation 

Primary die stroke option with Distance between dies method in First Operation

When user uses Distance between Dies method as forming stroke type then,

In the first operation **Total primary die** travel will be deactivated and defined by the system .

In Next operations the **Exact amount** check box will be unchecked and deactivated. 

In Next operations **Total primary die travel** will be used to calculate system defined step size only.

Precise stopping controls may be set at the next step.

## Stopping controls

The stopping parameters determine the process time at which the simulation terminates. A simulation can be terminated based on maximum number of time steps simulated or maximum stroke or maximum load on the primary die or contact ratio with respect to total surface area or distance between the dies. A simulation will be stopped when the condition of any of the stopping parameters are met. (See Fig. 34.1.41.)

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image043.jpg' | relative_url }})

Stopping controls window

**Max Die Stroke** : Terminates a simulation when the total displacement (SMAX) of the primary die reaches  
the specified value.

**Max Load:** Terminates a simulation when the X or Y load component of the primary die reaches the X or Y value of LMAX. Typically used when the movement control of the primary object is velocity or user specified.

**Contact area ratio:** Contact area ration is the ratio of area which is in contact with the dies to the total surface area of the billet. If this ratio crosses beyond the specified value the simulation stops.

**Distance between Objects:** Terminates a simulation when the distance between reference points (MDSOBJ) on two objects reaches the specified distance. Using the mouse pointer user has to select two points on the objects to mention the distance. If user already defined the reference point for the dies as indicated in Geometry section Other Geometry options then selecting the objects for Object1 and Object2 will highlight the distance in the display. Finally user need to mention the distance value for which simulation to be stopped as shown in Fig. 34.1.42.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image044.jpg' | relative_url }})

Distance between objects stopping controls definition

For Mechanical Press Movement, Max die stroke is always checked, deactivated, and be equal to total stroke (See Fig. 34.1.43.).

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image045.jpg' | relative_url }}) ![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image046.jpg' | relative_url }})

(a) For Exact Forming Stroke Mechanical press option (b) For Distance between dies Mechanical press option

Primary die stroke option with Exact Forming stroke method 

If **Exact forming stroke** was chosen, distance between objects will be unchecked and the deactivated (Fig. 34.1.43 (a).).

  
If **Distance between dies** was chosen, distance between objects will be checked and deactivated (Fig. 34.1.43.(b).)

  
If **Distance between dies** was chosen, the user must define distance between objects and reference points ( Fig. 34.1.43.(b).).

  
For more information about stopping controls refer [9.3.10. Temperature stopping contorls](../../pre_processor/9_simulation_controls/9_3_stopping_controls.htm#9.3.10._Temperature_stopping_control)

## Simulation controls

The DEFORM system solves time dependent non-linear problems by generating a series of FEM solutions at discrete time increments. At each time increment, the velocities, temperatures and other key variables of each node in the finite element mesh are determined based on boundary conditions, thermo mechanical properties of the work piece materials and possibly solutions at previous steps. Other state variables are derived from these key values and updated for each time increment. The length of this time step and number of steps simulated are determined based on the information specified in the step controls menu. Fig. 34.1.44. Shows simulation control options.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image047.jpg' | relative_url }})

Simulation controls window in system mode

User needs to specify the starting step number, the total number of steps, step increment to save and step definition (die displacement or time increment). In Forming express only constant die displacement and constant time increment can be used as step definition. For all movement controls except Load both die displacement and time increment are available as step definition types, for load movement controls only time increment is allowed.

**System type Step Increment constant die displacement:**

Now, for Mechanical press in forming express step size will be calculated from [(Total primary die travel) / (number of steps)]x1.2 regardless of whether exact amount is checked or not.  
For non-mechanical press operations in forming express step size will be calculated as [(Total primary die travel) / (number of steps)], if exact amount is checked (See Fig. 34.1.45.).  
For non-mechanical press operations in forming express step size will be calculated as [(Total primary die travel) / (number of steps)]x1.2, if exact amount is not checked.

**User type Step Increment constant die displacement** : It will allow the users to specify their own step size. User should provide an appropriate step size to meet their stopping condition based on their number of steps.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image048.jpg' | relative_url }})

Simulation controls window in user mode

**Number of simulation steps (NSTEP)**  
The number of simulation steps parameter defines the number of steps to run from the starting step number. The simulation will stop after this number of simulation steps have run, unless stopping control is triggered to stop the simulation or if the simulation runs into a problem. For example, if the starting step number is -35 ([NSTART](/docs/en/keyword_documentation/n/nstart/)) and 30 steps ([NSTEP](/docs/en/keyword_documentation/n/nstep/)) are specified, the simulation will stop after the 65th step, unless another stopping control is triggered first.

**Step increment to save (STPINC)**

The step increment ([STPINC](/docs/en/keyword_documentation/s/stpinc/)) to save in the database controls the number of steps that the system will save in the database. When a simulation runs, every step must be computed, but does not necessarily need to be saved in the database. Storing more steps will preserve more information about the process, consequently it will require more storage space.

**Step increment control ([DSMAX](/docs/en/keyword_documentation/d/dsmax/)/[DTMAX](/docs/en/keyword_documentation/d/dtmax/))**

Solution step size can be controlled by time step or by displacement of the primary die. If stroke per step is specified, the primary die will move the specified amount in each time step. The total movement of the primary die will be the displacement per step multiplied by the total number of steps. If time per step is specified, the time interval per step will be used. The die displacement per step will be the time step times the die velocity.

Stroke per step is frequently more intuitive. However, time per step must be specified for any problem in which there is no die movement (such as heat transfer), or for any problem where force control is used.

In Forming operations enhanced definition of step increment control available to include both the time and stroke dependent step functions. This means, step size (both time per step and stroke per step) can now be defined as a function of time or stroke. This functionality enables finer resolution of saved model information, where it is desired. (typically towards the end of the stroke, where steep changes of die load and cavity filling or flash formation can take place) for more information refer [9.2. Defining step.](/docs/en/pre_processor/9_simulation_controls/9_2_defining_step/)

**Advanced Simulation controls**

Advanced Simulation controls provide options to select the Deformation solvers, this is accessed by ![]({{ '/assets/icons/pre_icons/mo_advanced_button.jpg' | relative_url }}) button. For 2D Forming express only Skyline, MUMPS and Spools Deformation Solvers are available (See Fig. 34.1.46.). By default MUMPS solver will be selected.

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image049.jpg' | relative_url }})

Advanced simulation controls settings

Forming operation gives more simulation controls options in expert mode, for these options details refer [9\. Simulation Controls.](/docs/en/pre_processor/9_simulation_controls/9_simulation_controls/)

## Generate DB

**Check Data** ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }})

It checks the Data. If Data is correct we can generate DB. But while checking Data if it gives any errors or warnings then it should be corrected before generating Database. Errors will not allow the database to be generated while warnings will allow the DB to be generated.

**Generate Database** ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }})

By clicking on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button database gets generate for the setup.(See Fig. 34.1.47.)

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image050.jpg' | relative_url }})

Generate DB window

If user need any of the advanced options which are not available in Forming express then such options can be accessed without loosing the defined data in forming express operation by promoting to forming operation. This option is available in the Right mouse button menu option in operation editor as shown in Fig. 34.1.48. For more details about this upgrading the operation refer to [6.6.4. Upgrading Operations.](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_6_operations_management/6_6_4_upgrading_operations/)

![]({{ '/assets/images/operation_templates/34_forming_express/34_1_2d_forming_express_setup/image051.jpg' | relative_url }})

Promoting forming express to forming operation right menu option

After generating database user has to select the MO Simulation mode tab to submit the problem for simulation, for more information about MO Simulation mode refer [6.2. MO Simulation layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_2_integrated_manufacturing_process_simulation_layout/). Once the Simulation completed message tab indicates it by giving the proper message then from MO Post mode user can review the results, for more information about MO Post mode refer[ 6.3. MO Post layout.](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_3_integrated_manufacturing_process_post_layout/)

**Related Topics:**

[34.2. 3D Forming Express Setup](/docs/en/operation_templates/34_forming_express/34_2_3d_forming_express_setup/)

[Promote Forming Express to Forming operation](../../integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_6_operations_management/6_6_4_upgrading_operations.htm#Fig._6.6.4.4._Forming_express_operation_after_promoting_it_to_forming_operation)

[6.2. MO Simulation layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_2_integrated_manufacturing_process_simulation_layout/)

[6.3. MO Post layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_3_integrated_manufacturing_process_post_layout/)

[33.1. 2D Forming Setup](/docs/en/operation_templates/33_forming/33_1_2d_forming_setup/)

[33.2. 3D Forming Setup](/docs/en/operation_templates/33_forming/33_2_3d_forming_setup/)

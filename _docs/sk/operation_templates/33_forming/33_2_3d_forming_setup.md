---
lang: sk
title: "33.2. 3D Forming Setup"
---

# 33.2. 3D Forming Setup

33.2.1. Material List

33.2.2.Add objects

33.2.3. Workpiece

  * Geometry

  * Mesh

  * Material

  * Boundary Conditions

  * Movement Controls

  * Property

  * Initialize

33.2.4. Positioning

33.2.5. Scheduled Positioning

33.2.6. Contact

33.2.7. Stopping Controls

33.2.8. Simulation controls

33.2.9. Generate DB

Forming 3D operation can be used to setup complex 3D flow problems those cannot be simulated in 2D environment. Buckling of cylindrical parts is a fully three dimensional process, and must be modelled as such if such behavior is expected. An axisymmetric simulation will not show buckling, even if it will occur in the actual process (See Fig. 33.2.1.).

![]({{ '/assets/images/about_deform/1_7_geometry_representation/1_7_image002.jpg' | relative_url }})

Buckling

## Material List

In order for a simulation to achieve a high level of accuracy, it is important to have an understanding of the material properties required to specify a material used in DEFORM.

  
When setting up a simulation, material properties have to be specified for the objects. In MO Forming operation, all the materials required for the operation can be loaded at a time and the required material can be selected later as the problem is setup. User can add material by selecting ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) load material data from library as shown in Fig. 33.2.2. User can select required material from the categories and then click on ![]({{ '/assets/icons/pre_icons/mo_load_button.jpg' | relative_url }}) button as shown in Fig. 33.2.3\. 

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image001.jpg' | relative_url }})

Material List window

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image002.jpg' | relative_url }})

Import material from library window

  
(or) 

Another way of adding material is to click on the material icon of the explorer tab, a list of materials from library that are grouped into different categories will appear as shown in Fig. 33.2.4. Select required material then click on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button. Also, user can add required material by drag and drop into the material window.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image003.jpg' | relative_url }})

Add Material from Explorer material tab

(or)

In material list window, by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button, new material can be added. After adding material click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) and select respective tab to define required data for the simulation as shown in Fig. 33.2.5.

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image005.jpg' | relative_url }})

Add material from material list window

**Import Material data from a file** ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) : It imports the material from a .Key or .DB file.  
**Load Material data from Library** ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) :It imports the material from Library.  
**Save the Material data to a file**![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}) : It saves the material to a file.  
**Save the Material data to Library**![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}) : User can save the material to library using this option and can be loaded back as required in future for other simulations.

**Mixture material**

“Mixture” materials ([MSTMTR](/docs/sk/keyword_documentation/m/mstmtr/)) are used when a phase transformation is to be modeled in the simulation. The transforming material is modeled as a “mixture” of its constituent phases. For example, carbon steel might be modeled as a mixture of Austenite, Pearlite, Bainite, and Martensite. If a mixture material is defined, transformation rules should be defined which govern the transformation of one phase into another.(See Fig. 33.2.6.)

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image004.jpg' | relative_url }})

Adding Mixture Material

**Copy Properties![]({{ '/assets/icons/pre_icons/mo_copy_properties.jpg' | relative_url }})**

It is used to copy the regular material properties like plastic, elastic, thermal etc. from one material to other while creating/defining the material data as shown in Fig. 33.2.7\. In this dialog, source and destination for copying the properties and properties to be copied must be selected.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image005.jpg' | relative_url }})

Copy material properties window

**Convert Units![]({{ '/assets/icons/pre_icons/mo_convert_units_button.jpg' | relative_url }})**

It is used to convert the unit system of current selected material from material list from SI to English or English to SI or user can use any other multiplication factor as shown in Fig. 33.2.8. Selecting the ![]({{ '/assets/icons/pre_icons/mo_si_to_english_button.jpg' | relative_url }}) or ![]({{ '/assets/icons/pre_icons/mo_english_to_si_button.jpg' | relative_url }}) button will display the respective multiplication factors for converting from ![]({{ '/assets/icons/pre_icons/mo_si_to_english_button.jpg' | relative_url }}) and ![]({{ '/assets/icons/pre_icons/mo_english_to_si_button.jpg' | relative_url }}) , then selecting the ![]({{ '/assets/icons/pre_icons/mo_convert_button.jpg' | relative_url }}) button will convert and close the conversion window. This conversion table can be saved using save button and can also be edited by using wordpad/notepad and loaded back UNITCONV.DAT file using load button.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image006.jpg' | relative_url }})

Unit Conversion window

## Add objects

User can add required number of objects for the simulation by selecting ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button. Fig. 33.2.9. shows three objects added for a simple upsetting operation. 

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image007.jpg' | relative_url }})

Objects window

## Workpiece

In this page user can define required temperature for the object and select type of the object as shown in Fig. 33.2.10. For workpiece by default the object type selected is Plastic and user can also import object data from other DB’s or Keyfile’s from user defined library path ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) or from problem directory path ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) and even save the object data to Keyfile in user defined library ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}) or in problem directory path ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }})using respective buttons.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image008.jpg' | relative_url }})

Workpiece window

### **Geometry**

Geometry window is used to define the geometry of an object as shown in Fig. 33.2.11. Only define primitive field will be in active mode rest other options will be in grayed when no geometry is defined. Once after creating geometry all the options will be activated.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image009.jpg' | relative_url }})

Geometry window

**Define Primitive![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}) **

We have three different types of Geometry primitives such as Box, Cylinder and Hollow Cylinder as shown in Fig. 33.2.12. Extrude and Revolve can be used to convert 2D cross-section to 3D.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image010.jpg' | relative_url }})

Geometry primitive window

**Extract Border** ![]({{ '/assets/icons/pre_icons/mo_extract_border_button.jpg' | relative_url }})

This feature extracts the geometry data from the current database meshed object for all object types except the rigid object.

**Check![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }})**

Always check geometry. DEFORM has a checking algorithm that checks for number of invalid edges, invalid orientation, polygons with small area and number of surfaces. Every type of error cannot be detected.

Using this Check Geometry option opens the Geometry Checking Results window which gives a summary of the object’s geometry (See Fig. 33.2.13.). For an object that has a closed volume, there should be 1 surface, 0 free edges and 0 invalid entities (as circled below in Fig. 33.2.13.). Objects that are imported as surfaces and not solids will have a free edge but should still only have 1 surface.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image011.jpg' | relative_url }})

Geometry Checking Results

**Scale![]({{ '/assets/icons/pre_icons/mo_scale_label.jpg' | relative_url }})**

Geometry can be scaled in forming operation to accommodate thermal expansion by specifying the scaling factor. (See Fig. 33.2.14.) The scaling factor can be calculated by temperature differential and temperature dependent material data. The scaled geometry can be saved into different Geometry saving formats.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image012.jpg' | relative_url }})

Scale Geometry window

**Reverse![]({{ '/assets/icons/pre_icons/mo_reverse_label.jpg' | relative_url }})**

This feature reverses the surface/ normal of the geometry. Always surface/ Normal of the geometry should be outwards.

**Find Axis![]({{ '/assets/icons/pre_icons/mo_find_axis_label.jpg' | relative_url }})**

This feature determines the axis of the geometry automatically based on the geometry definition and displays it.

**Setup Brick Mesh**

In order to define Brick mesh, user has to define start surface and End surface for created geometry as shown in Fig. 33.2.15. Brick mesh is used for the geometries of regular or identical cross-section.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image017.jpg' | relative_url }})

Setup Brick Mesh window for Extrusion

Brick mesh can be generated by selecting Extrude or Revolve options based on the geometry. If user selects Extrude radio button the brick mesh will be extruded with respect to start and end point as shown in Fig. 33.2.16.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image013.jpg' | relative_url }})

Brick mesh of Extruded object

If user selects Revolve radio button the brick mesh will be revolved in Z direction as shown in Fig. 33.2.17. and Fig. 33.2.18.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image014.jpg' | relative_url }})

Setup brick mesh window for revolving

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image015.jpg' | relative_url }})

Brick mesh of Revolving object

**Fix![]({{ '/assets/icons/pre_icons/mo_fix_label.jpg' | relative_url }})**

This feature will handle geometric problems where there are either multiple surfaces or open (holes) regions by deleting any extra surfaces and filling holes. For minor or localized problems, this works well. For more troublesome file such as this one, the repair may not produce a desirable result.(See Fig. 33.2.19.)

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image016.jpg' | relative_url }})

Fixing Geometry of crankshaft Die

**Examine**![]({{ '/assets/icons/pre_icons/mo_examine_label.jpg' | relative_url }})

This feature helps to examine the 3D geometry points and polygons. The geometry point’s co-ordinates can also be edited by using points co-ordinates fields and apply button after changing these co-ordinates. The current selection of the point and polygon display is highlighted by sphere or cube shapes using the check boxes at the bottom of the window.(See Fig. 33.2.20.). From DEFORM V12, using ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) ("Detect zones") next to Surface field option we can calculate the number of zones exist in Geometry and for each zone we can assign different material or Layer ID using Assignment option. This option helps the user to model multi-layered composites, voids, inclusions, additive manufacturing,..etc.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image018.jpg' | relative_url }})

Geometry settings of Examine window

**Symmetry Planes![]({{ '/assets/icons/pre_icons/mo_symmetry_planes_label.jpg' | relative_url }})**

Both planar symmetry and rotational symmetry can be defined. In the case of planar symmetry, the simulation will have extra information that allows it to prevent material from flashing around it. In the case of rotational symmetry, meshing will automatically place the proper boundary conditions on the faces. This is meant as a uniform place to apply symmetry boundary conditions for all objects.

**Specifying Planar Symmetry**

To specify planar symmetry, select the symmetry plane on the geometry, then click on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}). The planar symmetry condition will be added to the list of currently specified symmetry. (See Fig. 33.2.21.). When symmetry plane is defined, during mesh generation a pop up appears with a message as shown in Fig. 33.2.22., requesting the user whether to create a default boundary condition, the user can select "No" option, if user would not like to use default BCC assigned by system based on symmetry conditions defined.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image019.jpg' | relative_url }})

Assigning symmetry surfaces

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image020.jpg' | relative_url }})

Default Boundary Conditions popup window

**Note** : Symmetry Popup message appears only when we setup a problem in Expert mode.

**Specifying Rotational Symmetry**

To specify rotational symmetry, specify the point and vector of the rotational axis as well as the degree of symmetry available as shown in Fig. 33.2.23. After this, click on the starting plane and end plane of the geometry in the direction of rotation so that rotational symmetry to be applied. The symmetry condition will be added to the list of currently specified symmetry. For more information about rotational symmetry option refer [Rotational Symmetry.](../../pre_processor/12_geometry_modelling/12_3_3d_geometry_data_defining.htm#Specifying_Rotational_Symmetry)

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image021.jpg' | relative_url }})

Rotational symmetry window

**2D to 3D conversion![]({{ '/assets/icons/pre_icons/mo_2d_to_3d_conversion.jpg' | relative_url }})**

User can define 2D cross section geometry which can be used to generate 3D geometry by checking Use Cross Section check box.

**Define Primitive![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }})**

We have three different types of Geometry primitives such as Bar, Cylinder and Hollow Cylinder as shown in Fig. 33.2.24. This geometry window appears for plane strain type of geometry.

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image007.jpg' | relative_url }})

2D Geometry primitive window for plane strain and plane stress 

The geometry window appears for Axisymmetric type of geometry is shown in Fig. 33.2.25.

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image006.jpg' | relative_url }})

2D Geometry primitive window for Axisymmetric and Torsion

**Check![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }})**

Once the geometry of the object is created, ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) button gets activated. It is necessary to check the orientation of the geometry. This can be done by clicking on the ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) button a popup appears as shown in below Fig. 33.2.26. The Geometry gets corrected, if they are any errors when we click on ![]({{ '/assets/icons/pre_icons/mo_check_and_correct_geo_button.jpg' | relative_url }}) button. A message saying, "Geometry is legal" will appear once the geometry is corrected or does not have any errors and then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). For more information please refer [12.1. 2D Geometry Data Defining](/docs/sk/pre_processor/12_geometry_modelling/12_1_2d_geometry_data_defining/) section [Check Geometry](../../pre_processor/12_geometry_modelling/12_1_2d_geometry_data_defining.htm#Check_Geometry). 

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image022.jpg' | relative_url }})

Check Geometry popup window

**Edit**![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }})

The Geometry editing option is used to create geometry for an object or edit the existing geometry. Imported geometry can be modified in Edit Geometry window. For more information on edit geometry, please refer[ Edit Geometry](33_1_2d_forming_setup.htm#Edit_) in Forming 2D Setup.

**Show geometry inside mark**

Checking this option enables the Geometry orientation display.

**Settings![]({{ '/assets/icons/pre_icons/mo_settings_icon.jpg' | relative_url }})**

After creation of 2D geometry using these settings user can create 3D geometry from 2D geometry.

**Extrude**

The user can import the 2d cross-section or use defined 2D cross-section of the geometry and extrude it in the desired direction. This can also be done while importing the 2d cross-section files from the DB or key file.(See Fig. 33.2.27.) 

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image023.jpg' | relative_url }})

2d cross-section window settings for extrusion

**Revolve**

The user can import the 2d cross-section of the geometry and revolve the geometry based upon the symmetry to get a 3d cross-section. (See Fig. 33.2.28.)

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image024.jpg' | relative_url }})

2D cross-section window settings for Revolving

**Generate 3D![]({{ '/assets/icons/pre_icons/mo_generate_3d_button.jpg' | relative_url }})**

By clicking on this button, created 2D geometry can be extruded or revolved to 3D geometry.

**Show Geometry Normal Vectors**

This feature shows the geometry surface normal vectors. If the geometry is a closed volume, the correct orientation is defined when the surface normals are pointing out of the object. When the geometry is not a closed volume but is just a surface, the correct orientation is defined when the normals are pointing towards the workpiece.(See Fig. 33.2.29.)

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image025.jpg' | relative_url }})

Show Geometry Normal Vectors

**Import Geometry from a file** ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}): It imports the geometry from a file  
**Load Geometry from Library** ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) :It imports geometry from Library  
**Save the Geometry to a file** ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}) : It saves the Geometry to a file.  
**Save Geometry to Library** ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}) : User can save geometry to the library using this option.  
**Delete Geometry** ![]({{ '/assets/icons/pre_icons/mo_clear_icon.jpg' | relative_url }}): It deletes the created geometry.

**Settings**

**2D Import**

Tolerance: Sets the tolerance level for joining two boundary points which are close together when an object is imported in IGS and DXF geometry formats, before transferring the data into DEFORM are defined here. (See Fig. 33.2.30.)

**No. of discretization points:**

Text to be added.

![]({{ '/assets/images/operation_templates/33_forming/33_1_2d_forming_setup/image018.jpg' | relative_url }})

2D Geometry Tolerance settings window

**3D Import**

Tolerance: level for joining two boundary points which close together when an object is imported from STL geometry formats and before transferring the data into DEFORM are defined here. (See Fig. 33.2.30.)

**Scaling Factor** : It will scale the 3D geometry while loading imported geometry. Required scaling factor must be specified before importing the geometry in order to scale the importing geometry. By default the value will be 1 means no scaling, for 0.5 it scales down to half of its original geometry and for 2 it doubles its original geometry. (See Fig. 33.2.30..) 

### Mesh

The below Fig. 33.2.31. shows the mesh generation options in guided mode. In Guided mode, mesh page user can generate Tetrahedral mesh.

The number of elements to be generated for an object can be specified merely by adjusting the slider bar and selecting an appropriate value for the current simulation in Number of Elements field. ![]({{ '/assets/icons/pre_icons/mo_mesh_preview_button.jpg' | relative_url }})option allows the user to preview the surface mesh of the object. Once the user is satisfied with the preview of surface mesh, the mesh can be generated on an object by clicking ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). ![]({{ '/assets/icons/pre_icons/mo_delete_button.jpg' | relative_url }}) feature deletes the generated mesh.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image026.jpg' | relative_url }})

Guided Mode Mesh window options

In order to control the mesh parameters like size, shape, density, type of elements, etc..., user has to switch to expert mode ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) for more advanced mesh options. Below Fig. 33.2.32. shows the mesh options available from Expert mode. We have Tetrahedral mesh and brick mesh option to generate mesh for object. For more information related to Tetrahedral mesh, refer chapter [13.2. 3D Tet Mesh Generation](/docs/sk/pre_processor/13_mesh_generation/13_2_3d_tet_mesh_generation/).

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image027.jpg' | relative_url }})

Expert Mode Mesh window options

The below Fig. 33.2.33. shows the Brick mesh generation options in Expert mode. For more information related to Tetrahedral mesh, refer chapter [13.3. 3D Brick Mesh Generation](/docs/sk/pre_processor/13_mesh_generation/13_3_3d_brick_mesh_generation/)

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image028.jpg' | relative_url }})

Brick Mesh options in Expert mode

###  Material

The below Fig. 33.2.34. shows the material window. User can assign required material from the list or can import from file or library. User can also add new material. For more information on how to assign material, Please refer Material List .

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image029.jpg' | relative_url }})

Material Window

Once after adding material click on ![]({{ '/assets/icons/pre_icons/mo_material_edit_button.jpg' | relative_url }}) button, material window will open as shown in [Fig. 10.9.](../../pre_processor/10_material_data/10_material_data.htm#Fig._10.9._Edit_material_window) The properties required are dependent on the physical effects being simulated in DEFORM. The material properties that the user is required to specify is a function of the material types that the user is utilizing in the simulation. This section describes the material data that may be specified for a DEFORM simulation.

  
The different data sets are:

  * [Plastic ](/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_plastic_data/)
  * [Elastic](/docs/sk/pre_processor/10_material_data/10_2_elastic_data/10_2_elastic_data/)
  * [Thermal ](/docs/sk/pre_processor/10_material_data/10_3_thermal_data/10_3_thermal_data/)
  * [Diffusion ](/docs/sk/pre_processor/10_material_data/10_4_diffusion_data/10_4_diffusion_data/)
  * [Dislocation ](/docs/sk/pre_processor/10_material_data/10_5_dislocation_data/)
  * [Grain ](/docs/sk/pre_processor/10_material_data/10_6_grain_data/10_6_grain_data/)
  * [Hardness ](/docs/sk/pre_processor/10_material_data/10_7_hardness_data/10_7_hardness_data/)
  * [Elec/ Mag ](/docs/sk/pre_processor/10_material_data/10_8_elec_mag_data/10_8_elec_mag_data/)
  * [Transformation](/docs/sk/pre_processor/10_material_data/10_9_transformation_data/10_9_transformation_data/)
  * [Coarsening](/docs/sk/pre_processor/10_material_data/10_10_coarsening_data/)
  * [Texture ](/docs/sk/pre_processor/10_material_data/10_11_texture_data/)
  * [Miscellaneous](/docs/sk/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_miscellaneous_data/)

This section discusses the manner in which to define each data set, and for which type of simulation each of these is required.

The DEFORM material library contains several hundred data sets. Nearly all materials contain Plastic (flow stress), elastic and thermal data. Depending on the intended application, the material data may also include microstructure related data.

The user should confirm that the material selected from the library is appropriate for the process they intend to model. For more information about Material Properties, please refer [10\. Material Data](/docs/sk/pre_processor/10_material_data/10_material_data/).

### Boundary Conditions

In Boundary conditions page, user can assign various boundary constraints for an object. Boundary conditions specify how the boundary of an object interacts with other objects and with the environment. The most commonly used boundary conditions are heat exchange with the environment for simulations involving heat transfer, prescribed velocity for enforcing symmetry or prescribing movement in problems such as drawing where a part is pulled through a die, shrink fit for modelling shrink rings on tooling, prescribed force for die stress analysis and Contact between objects in the model. Fig. 33.2.35. shows various BCC that can be assigned to an object.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image033.jpg' | relative_url }})

Boundary Conditions window

The BCC's are categorized as [Symmetry](/docs/sk/pre_processor/14_boundary_conditions/14_1_symmetry_boundary_conditions/), [Deformation](/docs/sk/pre_processor/14_boundary_conditions/14_2_deformation_boundary_conditions/), [Thermal](/docs/sk/pre_processor/14_boundary_conditions/14_3_thermal_boundary_conditions/), [Diffusion](/docs/sk/pre_processor/14_boundary_conditions/14_4_diffusion_boundary_conditions/) and [Heating](/docs/sk/pre_processor/14_boundary_conditions/14_5_heating_boundary_conditions/). For more information about these BCC's please refer [14\. Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/).

### **Movement Controls**

Movement controls can be applied to rigid objects and boundary nodes of meshed objects. The surface defined by these nodes can be thought of as a "rigid surface". During the simulation, the constrained nodes will move synchronously in the speed and direction defined by the movement controls. Two types of Movement controls are available in 3D Environment.

**Translation Movement**

Various types of Movement controls that are available in Translation Movement controls are [Speed](/docs/sk/pre_processor/15_movement_controls_definition/15_1_speed/), [Force](/docs/sk/pre_processor/15_movement_controls_definition/15_2_force/), [Hammer](/docs/sk/pre_processor/15_movement_controls_definition/15_3_hammer/), [Screw press](/docs/sk/pre_processor/15_movement_controls_definition/15_4_screw_press/), [Mechanical press](/docs/sk/pre_processor/15_movement_controls_definition/15_5_mechanical_press/), [Hydraulic press](/docs/sk/pre_processor/15_movement_controls_definition/15_6_hydraulic_press/), [Sliding Die](/docs/sk/pre_processor/15_movement_controls_definition/15_7_sliding_die/) and [Path](/docs/sk/pre_processor/15_movement_controls_definition/15_8_path/) as shown in Fig. 33.2.36. For more information about these movement controls, please refer [15\. Movement controls settings.](/docs/sk/pre_processor/15_movement_controls_definition/15_movement_controls_settings/)

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image035.jpg' | relative_url }})

Translation Movement Controls window

**Rotational Movement**

Rotational movement is defined by an angular velocity/torque about a fixed center of rotation. Two types of Movement controls that are available in Rotational Movement controls are Torque and Angular Velocity as shown in Fig. 33.2.37. For more information, please refer [15.9. Rotational movement.](/docs/sk/pre_processor/15_movement_controls_definition/15_9_rotational_movement/)

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image034.jpg' | relative_url }})

Rotation Movement Controls window

For more information about these movement controls please refer [15\. Movement Controls Settings.](/docs/sk/pre_processor/15_movement_controls_definition/15_movement_controls_settings/)

### Property

Miscellaneous object parameters, which affect either thermo-mechanical behavior of the object or numerical solution behavior are specified in the Object-Properties window. (See Fig. 33.2.38.) For more information, Please refer [16\. Object properties.](/docs/sk/pre_processor/16_object_properties/16_object_properties/)

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image036.jpg' | relative_url }})

Object property window

### **Initialize**

In Initialize window, few state variables that are commonly used such as Temperature, strain, stress, damage, velocity, Displacement, etc.., are made available for initialization. User can initialize the values for these state variables by defining in the field next to it and clicking on ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}) button. Fig. 33.2.39. shows the various state variables that are available in Initialize window. For state variable like velocity and displacement, provided input fields as many as dimensions, user needs to define the directional values of the variables in respective fields and then clicking on ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}) button will calculate the total velocity and displacement. Depending on the type of state variable, user can also initialize them from Node and Element data windows. For more information on how to initialize state variables in Node and Element windows (See Fig. 33.2.40. and Fig. 33.2.41.), please refer [17.1. Object node variables](/docs/sk/pre_processor/17_object_data_initialization/17_1_node_data_window/) and [17.2. Object element variables.](/docs/sk/pre_processor/17_object_data_initialization/17_2_element_data_window/)

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image030.jpg' | relative_url }})

Initialization window

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image031.jpg' | relative_url }})

Node Data window

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image032.jpg' | relative_url }})

Element Data window

## Positioning

Below Fig. 33.2.42. shows the positioning window.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image037.jpg' | relative_url }})

Positioning window

**Automatic Positioning** ![]({{ '/assets/icons/pre_icons/mo_automatic_positioning_button.jpg' | relative_url }})

By clicking on this button, system automatically Positions the Objects with respect to the top die movement direction, this option works best for simple setup with three objects work piece, top die and bottom die.

**Positioning Objects** ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }})

By clicking on this button, user can position the objects in required directions. Various types of Positioning Options are available such as [Drag](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_1_Drag_Positioning), [Drop](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_5_Drop_positioning), [Offset](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_2_Offset_Positioning), [Interference](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_3_Interference_positioning) and [Rotational](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_4_Rotational_positioning) as shown in Fig. 33.2.43. For more information about these options, please refer [19\. Object Positioning.](/docs/sk/pre_processor/19_object_positioning/19_object_positioning/)

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image038.jpg' | relative_url }})

Object Positioning Window

## Scheduled Positioning

When user is not sure about the location of an object as in case of Read From DB objects, scheduled positioning will help to position the objects accurately.

Schedule positioning allows the user to define the positioning for objects in MO setup for successive operations for which DB is not generated so that the objects are positioned before generation of DB while running simulation in Batch mode.(See Fig. 33.2.44.)

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image039.jpg' | relative_url }})

Scheduled Positioning window

## Contact (Inter-Object Relations)

The purpose of inter-object relations is to define how the different objects in a simulation interact with each other. The relations table shows the current inter object relations that have been defined. All objects which may come in contact with each other through the course of the simulation must have a contact relation defined. This includes an object having a relationship to itself, if self-contact occurs as in case of lap. It is very important to define these relationships correctly for a simulation to model a forming process accurately. The critical variables to be defined between contacting objects are:

  * [Friction factor](../../pre_processor/20_inter-object_data_definition/20_1_friction_and_contact_criteria.htm#20_1_1_Friction_\(FRCFAC\))

  * [Interface heat transfer coefficient](../../pre_processor/20_inter-object_data_definition/20_2_interface_thermal_data.htm#20_2_1_Interface_heat_transfer_coefficient_\(IHTCOF\))

  * [Contact relation](../../pre_processor/20_inter-object_data_definition/20_inter-object_data_definition.htm#20_1_Contact_relation_\(CNTACT\))

  * [Separation criterion](../../pre_processor/20_inter-object_data_definition/20_1_friction_and_contact_criteria.htm#20_1_4_Separation_Type)

Also covered in the inter object controls is generation of inter-object boundary conditions.

Inter-Object relations define what objects can contact each other, and how contacted objects will behave while in contact. Contact relations, Inter-Object boundary conditions, Friction and Heat transfer relations are set here for each object pair ( Fig. 33.2.45.). Simply speaking, the procedure for defining Inter-Object relations is done in the following steps.

  * Define the master-slave combination – In the case of a single deforming object, the deforming object should be the slave object always. In the case of multiple deforming bodies, the object with the finer mesh at the interface of the two objects should be the slave object.

  * Define the parameter for the given master-slave pair – This can be done by clicking the Edit button and setting the appropriate parameters . (See [Fig. 20.2.](../../pre_processor/20_inter-object_data_definition/20_inter-object_data_definition.htm#Fig_20_2_Inter_object_constant_Shear_Friction_options_for__2D) and [Fig. 20.3.](../../pre_processor/20_inter-object_data_definition/20_inter-object_data_definition.htm#Fig_20_3_Inter_object_constant_Shear_Friction_options_for_3D))

  * Generate the contact for all the objects – First click the ![]({{ '/assets/icons/pre_icons/mo_initialize_button.jpg' | relative_url }}) icon and then click the ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) button to generate contact. If contact is not generated where expected check following:

  * The orientation of geometry of the rigid objects. Make sure that the geometry is shaded on the inside of the rigid objects.

  * The mesh in the region of contact. If the mesh is coarse, there may be no nodes in proximity to gain contact.

  * Make sure that the parts are actually within proximity of each other.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image040.jpg' | relative_url }})

Inter-object data definition window

In MO, we have two types of Inter-object relation ships. They are **User** and **System**.

**System** : By selecting this radio button (See Fig. 33.2.46..), system assigns default inter-object relationships. Also user can add the lubricants if necessary (See Fig. 33.2.47.). By clicking on Edit button, user can define the required lubricants for the simulation. (See Fig. 33.2.48.)

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image041.jpg' | relative_url }})

Inter-object window with system selection

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image042.jpg' | relative_url }})

Adding lubricant in Inter-object window

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image043.jpg' | relative_url }})

Adding lubricant from Edit window

**User** : By default, user radio button will be selected for Forming operation. User can add relationships by clicking on Add button as shown in Fig. 33.2.45.

By clicking on edit ****![]({{ '/assets/icons/pre_icons/mo_edit_button.jpg' | relative_url }})**** button user can define the friction and Interface Heat relations. For more information refer, [20\. Inter-object Data Definition](/docs/sk/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/)

For more information about [Deformation](/docs/sk/pre_processor/20_inter-object_data_definition/20_1_friction_and_contact_criteria/), [Thermal](/docs/sk/pre_processor/20_inter-object_data_definition/20_2_interface_thermal_data/), [Heating](/docs/sk/pre_processor/20_inter-object_data_definition/20_3_interface_resisitivity/), [Friction window](../../pre_processor/20_inter-object_data_definition/20_1_friction_and_contact_criteria.htm#20_1_6_Friction_Window), [Tool wear](/docs/sk/pre_processor/20_inter-object_data_definition/20_4_tool_wear/) and [Rigid contact](/docs/sk/pre_processor/20_inter-object_data_definition/20_5_rigid_contact/), refer chapter [20\. Inter-object Data Definition](/docs/sk/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/). 

## Stopping Controls

The stopping parameters determine the process time at which the simulation terminates. A simulation can be terminated based on maximum number of time steps simulated or the maximum accumulated elemental strain or the maximum process time or maximum stroke or minimum velocity or maximum load on the primary object. A simulation will be stopped when the condition of any of the stopping parameters are met.

**Deformation**

The Below Fig. 33.2.49. shows the various types of Deformation Stopping Controls.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image044.jpg' | relative_url }})

Deformation Stopping Controls window

**Max Die Stroke** : Terminates a simulation when the total displacement ([SMAX](/docs/sk/keyword_documentation/s/smax/)) of the primary die reaches the specified value. The stroke value for the object is specified in the Object Movement tab.

**Max Load** :Terminates a simulation when the X or Y or Z load component of the primary die reaches the X or Y or Z value of [LMAX](/docs/sk/keyword_documentation/l/lmax/). Typically used when the movement control of the primary object is velocity or user specified.

**Contact area ratio:** Contact area ration is the ratio of area which is in contact with the dies to the total surface area of the billet. If this ratio crosses beyond the specified value the simulation stops.

**Distance between Objects:** Terminates a simulation when the distance between reference points ([MDSOBJ](/docs/sk/keyword_documentation/m/mdsobj/)) on two objects reaches the specified distance.

**Thermal**

The Below Fig. 33.2.50. shows the various types of Thermal Stopping Controls.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image045.jpg' | relative_url }})

Thermal Stopping Controls window

**Stopping Method**

**None** : Applies no thermal stopping controls

**Any Node:** Simulation stops when any node in the billet reaches the specified value.  
**All Nodes** : Simulation stops when all the nodes in the billet reach the specified value.

**Selected Node** :Simulation stops when specified node in the billet reaches the specified value.  
**Average All Nodes** : Simulation stops when average temperature of all the nodes in the billet reaches the specified value.  
**Average surface Temp +Max. Temp** : Simulation stops when average temperature of all the nodes on the surface of billet + Maximum temperature in the billet reaches the specified value.

**Temperature Range**

Apart from single value a range of temperature also can be used to stop the simulation.

**Stop when temperature is outside range** : Simulation stops when the temperature value is outside the specified range.

**Stop when temperature is inside range** : Simulation stops when the temperature value is inside the specified range.

## Simulation Controls

In Guided mode simulation controls, user can select Simulation mode type and Output type Fig. 33.2.51. shows Guided mode Step page and Fig. 33.2.52. shows guided mode Simulation controls, where user can defined operation step controls and step definition. The basic options required for forming operation are provided here while Expert mode provides more detailed options.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image046.jpg' | relative_url }})

Guided mode Step

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image049.jpg' | relative_url }})

Guided mode Simulation controls

The DEFORM system solves time dependent non-linear problems by generating a series of FEM solutions at discrete time increments. At each time increment, the velocities, temperatures, and other key variables of each node in the finite element mesh are determined based on boundary conditions, thermo mechanical properties of the work piece materials and possibly solutions at previous steps. Other state variables are derived from these key values, and updated for each time increment. The length of this time step, and number of steps simulated, are determined based on the information  
specified in the step controls menu.

**Number of simulation steps (NSTEP)**

The number of simulation steps parameter defines the number of steps to run from the starting step number. The simulation will stop after this number of simulation steps have run, unless stopping control is triggered to stop the simulation or if the simulation runs into a problem. For example, if the starting step number is -35 ([NSTART](/docs/sk/keyword_documentation/n/nstart/)), and 30 steps ([NSTEP](/docs/sk/keyword_documentation/n/nstep/)) are specified, the simulation will stop after the 65th step, unless another stopping control is triggered first.

**Step increment to save (STPINC)**

The step increment ([STPINC](/docs/sk/keyword_documentation/s/stpinc/)) to save in the database controls the number of steps that the system will save in the database. When a simulation runs, every step must be computed, but does not necessarily need to be saved in the database. Storing more steps will preserve more information about the process, consequently it will require more storage space.

**Primary die (PDIE)**

The primary die ([PDIE](/docs/sk/keyword_documentation/p/pdie/)) is the object for which many stopping and stepping criteria are defined. For example, stopping distance based on primary die stroke. When the stroke of the object defined as the primary die reaches the value for primary die displacement, the simulation will be stopped whether or not more steps were specified. The Step by Stroke feature determines step size based on the movement of the primary die. The primary die is usually assigned to the object most closely controlled by the forging machinery. For example, the die attached to the ram of a mechanical press would be designated as the primary object.

**Step increment control ([DSMAX](/docs/sk/keyword_documentation/d/dsmax/)/[DTMAX](/docs/sk/keyword_documentation/d/dtmax/))**

Solution step size can be controlled by time step or by displacement of the primary die. If stroke per step is specified, the primary die will move the specified amount in each time step. The total movement of the primary die will be the displacement per step multiplied by the total number of steps. If time per step is specified, the time interval per step will be used. The die displacement per step will be the time step times the die velocity.

  
Even the temperature based step controls ([DTPMAX](/docs/sk/keyword_documentation/d/dtpmax/)) settings control the time stepping. The purpose for these controls is to specify the time stepping of a simulation that is driven by thermal-induced deformation.

The definition of step increment control have been enhanced to include both the time and stroke dependent step functions,these options are available under Expert mode. This means, step size (both time per step and stroke per step) can now be defined as a function of time or stroke. This functionality enables finer resolution of saved model information, where it is desired. (typically towards the end of the stroke, where steep changes of die load and cavity filling or flash formation can take place)

Stroke per step is frequently more intuitive. However, time per step must be specified for any problem in which there is no die movement (such as heat transfer), or for any problem where force control is used. 

Fig. 33.2.53. shows the Simulation Controls in Expert mode.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image047.jpg' | relative_url }})

Expert mode Simulation controls

Options defined under Simulation Controls (See Fig. 33.2.53.) control the numerical behavior of the solution. Main controls details with specifying the simulation title,unit system, geometry type, etc.

Step and stopping controls are used to specify the time step, the total number of steps and the criteria used to terminate the simulation.  
Processing conditions like the environment temperature, convection coefficient can be specified here.

For more information and description about options in Simulation controls, Please refer [9\. Simulation Controls.](/docs/sk/pre_processor/9_simulation_controls/9_simulation_controls/)

## Generate DB 

**Check Data**![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }})****

It checks the Data. If Data is correct we can generate DB. But while checking Data if it gives any errors or warnings then it should be corrected before generating Database. Errors will not allow the database to be generated while warnings will allow the DB to be generated.

**Generate Database![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }})**

By clicking on this button, it generated the Database for the setup.(See Fig. 33.2.54.)

**Append Key file**

Any information that is not defined in the wizard but still applicable to the process can be loaded as .key file. This option is also useful in the cases where only few values needs to be changed then those values can be defined as .key file and only .key file can be changed and simulation can be resubmitted.

![]({{ '/assets/images/operation_templates/33_forming/33_2_3d_forming_setup/image048.jpg' | relative_url }})

Generate DB window

---
lang: en
title: "22. Convert 2D to 3D"
---

# 22\. Convert 2D to 3D ![]({{ '/assets/icons/pre_icons/convert_2d_to_3d_icon.jpg' | relative_url }})

22.1. Built-in Conversion module Introduction

22.2. Procedure to convert objects from 2D to 3D

22.3. Advanced Geometry Options

The integrated system can handle both 2D DB and 3D DB, one DB can contain either 2D result, 3D result, or hybrid 2D/3D result. Each step will be either 2D or 3D. The Integrated system offers streamlined data flow quick setup of 3D problem from 2D problem, quick setup of 2D problem from 3D problem (under development) and easy comparison between 2D and 3D result

Pre-processor offers dual definitions, unified [simulation controls](/docs/en/pre_processor/9_simulation_controls/9_simulation_controls/), built in conversion module and model conversion from 2D to 3D.

Integrated Database offers unified storage to store/retrieve 2D/3D simulation data. The Integrated DB will have information about dimension and version number for each step, and stores 2D and 3D simulation to a single DB.

Pre-processor has been provided with option to switch between 2D to 3D Mode (See Fig. 22.1.).

**Show 2D Model![]({{ '/assets/icons/pre_icons/show_2d_model.jpg' | relative_url }}) **: Using this button user can switch 2D mode after converting.

**Show 3D Model![]({{ '/assets/icons/pre_icons/show_3d_model.jpg' | relative_url }}) **: Using this button user can switch 3D mode after converting.

![]({{ '/assets/images/pre-processor/22_convert_2d_to_3d/image001.jpg' | relative_url }})

GUI pre processor window highlighted with 2D, 3D mode buttons and convert object button

## Built-in Conversion module Introduction

The built-in conversion module is an enhancement of previous advanced geometry option.

The fast creation of 3D geometry from 2D geometry can be accomplished using Revolution type and extrusion type option provided in the advanced geometry option.

The fast creation of 3D mesh from 2D mesh can be accomplished using the built in conversion module as shown in Fig. 22.2. It can handle both keyword and DB files as input. The user can convert a single object or multiple objects at a time. Conversion axis has been introduced to provide the link between 2D model and 3D model. It will be updated during positioning. The user can control the Revolution and Start angles of the object (See Fig. 22.3.).

![]({{ '/assets/images/pre-processor/22_convert_2d_to_3d/image002.jpg' | relative_url }})

2D to 3D Converter window before conversion

![]({{ '/assets/images/pre-processor/22_convert_2d_to_3d/image003.jpg' | relative_url }})

2D to 3D Converter window after conversion

## Procedure to convert objects from 2D to 3D

  1. **Open the 2D to 3D converter** : Open 2D setup in an Pre-processor. Click on converter (![]({{ '/assets/icons/pre_icons/convert_2d_to_3d_icon.jpg' | relative_url }})) to convert entire setup.

  1. **Object list** : User can select the objects from object list by checking check box next to the objects.

  1. **Co-ordinate system selection** : The axis direction for revolution or extrusion can be selected from Co-ordinate system

  1. **3D parameters** :

  * For rotating a 2D cross-section into 3D,start angle, revolution angle and tolerance can be specified under 3D parameters tab.

  * For extruding a 2D cross-section into 3D, length of extrusion and start location needs to be defined.

  1. **Geometry** : If only geometry needs to be converted, number of sections has to be defined and check output geometry check box to turned on.

  1. **Mesh** : In case of meshed objects, turn on output mesh and select mesh type. Enter number of 3D elements for meshed objects. Advanced button can be used to assign the various 3D mesh parameters. For more information please refer [13.2. 3D Tet Mesh Data Generation](/docs/en/pre_processor/13_mesh_generation/13_2_3d_tet_mesh_generation/) and [13.3. 3D Brick Mesh Generation](/docs/en/pre_processor/13_mesh_generation/13_3_3d_brick_mesh_generation/).

  1. **Preview![]({{ '/assets/icons/pre_icons/converter_preview_button.jpg' | relative_url }}) **: This can be used to preview the objects.

  1. **Convert![]({{ '/assets/icons/pre_icons/converter_convert_button.jpg' | relative_url }}) **: This can be used for Converting objects.

  1. The 3D model settings can be applied by clicking ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}), it switches to the 3D mode showing the converted objects.

![]({{ '/assets/icons/pre_icons/converter_cancel_button.jpg' | relative_url }}) button can be used to exit from converter window without applying changes.

![]({{ '/assets/icons/pre_icons/converter_2d_toggle_button.jpg' | relative_url }}) button can be used to toggle between 2D and 3D after converting.

The user can create object with tetrahedron mesh using the [3D mesh windows](../13_mesh_generation/13_2_3d_tet_mesh_generation.htm#13.2.6._Mesh_density_windows) (See Fig. 22.4.) option and brick mesh using [2D mesh windows](../13_mesh_generation/13_3_3d_brick_mesh_generation.htm#Fig._13.3.6.Mesh_density_windows_for_2D) (See Fig. 22.5.) option with full control for meshing parameters including Weighting factors. 2D mesh density window (poly-line type) will be converted to polygon surface type of mesh density window during conversion. (See Fig. 22.6.)

![]({{ '/assets/images/pre-processor/22_convert_2d_to_3d/image004.jpg' | relative_url }})

Brick mesh model generated using 2D Mesh window

![]({{ '/assets/images/pre-processor/22_convert_2d_to_3d/image005.jpg' | relative_url }})

Tetrahedron mesh model generated using 2D Mesh window

![]({{ '/assets/images/pre-processor/22_convert_2d_to_3d/image006.jpg' | relative_url }})

Mesh density window handling

The user can use interpolation module directly from the built in conversion window to plot the stress, strain, temperature values.

When the model is converted from 2D to 3D the [symmetry plane](../14_boundary_conditions/14_1_symmetry_boundary_conditions.htm#Fig._14.1.1_Symmetry_plane_BCC_for_quarter_symmetry_model), [BCC](/docs/en/pre_processor/14_boundary_conditions/14_boundary_conditions/) assignments and materials are assigned automatically to the respective objects. (See [Fig. 22.7.](22_convert_2d_to_3d.htm#Fig_22_7_Automated_symmetry_plane_assignment_to_die/workpiece_geometry_and_boundary_code_assignment_for_mesh))

![]({{ '/assets/images/pre-processor/22_convert_2d_to_3d/image007.jpg' | relative_url }})

Automated symmetry plane assignment to die/workpiece geometry and boundary code assignment for mesh

##  Advanced Geometry Options

  
**Extrude**  
The user can import or ceate the 2d cross section of the geometry and extrude it in the desired direction in 3D Geometry Primitive page. This can also be done while importing the 2d cross section files from the DB or key file.When we convert the 2D model to 3D model by default it take Z as the Extrude direction (See Fig. 22.8.)

![]({{ '/assets/images/pre-processor/22_convert_2d_to_3d/image008.jpg' | relative_url }})

Extruded object in display window

**Revolve**  
The user can import or create the 2d cross section of the geometry and revolve the geometry based upon the symmetry to get a 3d geometry in 3D Geometry Primitive page. This feature can be used to create 3D geometry from 2D geometry when the geometry is not too complex.

User can controls the Rotation angle, Direction and Revolved sections of the geometry as per the requirement (See Fig. 22.9.).

![]({{ '/assets/images/pre-processor/22_convert_2d_to_3d/image009.jpg' | relative_url }})

The 2D Geo is converted in to 3D Geo by revaluing in Z direction

**Related Topics:**

[2D Geometry Data Defining](/docs/en/pre_processor/12_geometry_modelling/12_1_2d_geometry_data_defining/)

[3D Geometry Data Defining](/docs/en/pre_processor/12_geometry_modelling/12_3_3d_geometry_data_defining/)

[2D Mesh Data Generation](/docs/en/pre_processor/13_mesh_generation/13_1_2d_mesh_generation/)

[3D Tet Mesh Generation](/docs/en/pre_processor/13_mesh_generation/13_2_3d_tet_mesh_generation/)

[3D Brick Mesh Generation](/docs/en/pre_processor/13_mesh_generation/13_3_3d_brick_mesh_generation/)

[Boundary condition](/docs/en/pre_processor/14_boundary_conditions/14_boundary_conditions/)

[Simulation controls](/docs/en/pre_processor/9_simulation_controls/9_simulation_controls/)

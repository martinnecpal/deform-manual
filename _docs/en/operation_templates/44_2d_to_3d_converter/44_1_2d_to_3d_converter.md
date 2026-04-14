---
lang: en
title: "44.1. 2D to 3D Converter"
---

# 44.1. 2D to 3D Converter

44.1.1. Add 2D to 3D Converter operator

44.1.2. Define Configuration settings

44.1.3. Select objects to convert

44.1.4. Defining objects

44.1.5. Define geometry conversion settings

44.1.6. Define Mesh conversion settings

44.1.7. Define Material

44.1.8. Objects Conversion window

44.1.9. Generate DB

44.1.10. Continue 3D problem setup after converter operation

44.1.11. Simulate integrated 2D and 3D setup

44.1.12. Post process the integrated 2D and 3D model in MO Post

##  Add 2D to 3D Converter operator

After completing the 2D operation setup user can add the 2D to 3D converter simulation operator from explorer window as shown in Fig. 44.1.1. Even as first operation we can add 2D to 3D Converter operation then we need to import the 2d Database or 2D keyfile for the conversion.

![]({{ '/assets/images/operation_templates/44_2d_to_3d_converter/44_1_2d_to_3d_converter/image0001.jpg' | relative_url }})

Add 2D to 3D converter

For practicing above example open the MO wizard in English unit system > add 2D Forming operation > import the HAMMER_LAB.KEY keyword file from 2D/LABS folder > go to DB generation window > generate DB > after that add 2D to 3D converter simulation operator from explorer.

In operation editor select the 2D to 3D converter operator to open as shown in [Fig. 44.1.2.](44_1_2d_to_3d_converter.htm#Fig_44_1_2_Configuration_settings_of_converter_for_2D_axisymmetric/torsion_geometry_type)

![]({{ '/assets/images/operation_templates/44_2d_to_3d_converter/44_1_2d_to_3d_converter/image0002.jpg' | relative_url }})

Configuration settings of converter for 2D axisymmetric/torsion geometry type

## Define Configuration settings

User need to select the upward direction for the 3D models by selecting coordinates system selection radio buttons. As indicated if “Z is up” is selected Z direction will be the upward direction, so 2D axisymmetric upward direction Z or plane strain upward direction Y becomes Z direction in 3D model. Similarly for “Y is up” option Y becomes the upward direction in 3D converted model. By default Z direction is selected as upward direction.

User can control the revolution and start angle of the object for 2D axisymmetric geometry type using 3D parameters settings as shown in [Fig. 44.1.2.](44_1_2d_to_3d_converter.htm#Fig_44_1_2_Configuration_settings_of_converter_for_2D_axisymmetric/torsion_geometry_type)

For plane strain/plane stress 2D geometry type conversion user can control extrusion length and start location using 3D parameter settings as shown in [Fig. 44.1.3.](44_1_2d_to_3d_converter.htm#Fig_44_1_3_Configuration_settings_of_converter_for_2D_plane_strain/plane_stress_geometry_type) This can be practiced by importing the Rib_web_SI.KEY 2D Forging example into 2D forming operation similar to the axisymmetric HAMMER_LAB example mentioned in this manual under section 44.1.1.

![]({{ '/assets/images/operation_templates/44_2d_to_3d_converter/44_1_2d_to_3d_converter/image0003.jpg' | relative_url }})

Configuration settings of converter for 2D plane strain/plane stress geometry type

## Select objects to convert

All the objects from the previous operation are automatically passed to the converter operation, if any of the objects not required for further 3D operation then those objects can be deleted by using the ![]({{ '/assets/icons/pre_icons/mo_delete_icon2.jpg' | relative_url }}) button as shown in Fig. 44.1.4. As all the objects from previous operation are passed so all object types are read from DB.

![]({{ '/assets/images/operation_templates/44_2d_to_3d_converter/44_1_2d_to_3d_converter/image0004.jpg' | relative_url }})

Objects selection window

## Defining objects

In objects page if object read from previous operation its object type will be read from DB type. User can also add converter operator as first operation and import the 2D objects from DEFORM DB or keyword file using import object option as shown in Fig. 44.1.5. If user imported any 2D object for conversion then object type will be as in the imported file instead of read from DB.

![]({{ '/assets/images/operation_templates/44_2d_to_3d_converter/44_1_2d_to_3d_converter/image0005.jpg' | relative_url }})

Objects general settings window

##  Define geometry conversion settings

For converting geometry number of sections has to be defined and output geometry check box to be turned on (see Fig. 44.1.7.). As workpiece (Deformable object types) will change for every step as it deforms its geometry normally not converted, so this check box will be unchecked by default for workpiece as shown in Fig. 44.1.6.

![]({{ '/assets/images/operation_templates/44_2d_to_3d_converter/44_1_2d_to_3d_converter/image0006.jpg' | relative_url }})

Geometry conversion settings window for workpiece (Axisymmetric)

For solid objects user geometry type must be Solid and for Hollow user has to select the Hollow option. In case of 2D axisymmetric setup conversion if geometry type is solid then object symmetry edge nodes coordinates are within the tolerance limit from centerline then it will neglect the gap and generates the 3D solid geometry, if the distance exceeds the tolerance limit then system treats the gap and generates the curved surface at the centre. For 3D models conversion less than 360° revolution angle from 2D axisymmetric model symmetry BCC will automatically generate.

Click on ![]({{ '/assets/icons/pre_icons/mo_3d_preview_button.jpg' | relative_url }}) button to observe the preview of the geometry as shown in Fig. 44.1.7.

![]({{ '/assets/images/operation_templates/44_2d_to_3d_converter/44_1_2d_to_3d_converter/image0007.jpg' | relative_url }})

Geometry conversion settings for dies (Axisymmetric)

For Plane strain/Plane stress 2D geometry type user will get only number of sections geometry option along the extrusion length direction as shown in [Fig. 44.1.8.](44_1_2d_to_3d_converter.htm#Fig_44_1_8_Geometry_conversion_window_for_plane_strain/plane_stress)

![]({{ '/assets/images/operation_templates/44_2d_to_3d_converter/44_1_2d_to_3d_converter/image0008.jpg' | relative_url }})

Geometry conversion window for plane strain/plane stress

## Define Mesh conversion settings

In case of meshed objects, turn on output mesh and select mesh type. Enter number of 3D elements for meshed objects as shown in Fig. 44.1.9.

![]({{ '/assets/images/operation_templates/44_2d_to_3d_converter/44_1_2d_to_3d_converter/image0009.jpg' | relative_url }})

Mesh conversion settings

![]({{ '/assets/icons/pre_icons/mo_advanced_button.jpg' | relative_url }}) button can be used to assign the various 3D mesh parameters as shown in Fig. 44.1.10. For more information on general, weighting factors, mesh windows, coating, remesh criteria and advanced settings of tetrahedron and brick/hexahedron mesh please refer [13.2. 3D Tet Mesh Generation](/docs/en/pre_processor/13_mesh_generation/13_2_3d_tet_mesh_generation/) and [13.3. 3D Brick Mesh Generation](/docs/en/pre_processor/13_mesh_generation/13_3_3d_brick_mesh_generation/).

![]({{ '/assets/images/operation_templates/44_2d_to_3d_converter/44_1_2d_to_3d_converter/image0010.jpg' | relative_url }})

Advanced Mesh settings for Tet and Brick mesh

If user setup converter operation in interactive mode after simulation of 2D operation or converter itself as first operation then ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button will be active to convert the mesh.

## Define Material

User can select new material for only workpiece and even edit the material properties by checking the select new material check box as shown in Fig. 44.1.11.

![]({{ '/assets/images/operation_templates/44_2d_to_3d_converter/44_1_2d_to_3d_converter/image0011.jpg' | relative_url }})

New material selection option for workpiece

## Objects Conversion window

User can know the status of the objects geometry and mesh conversion selection and conversion in the convert window as shown in Fig. 44.1.12.

![]({{ '/assets/images/operation_templates/44_2d_to_3d_converter/44_1_2d_to_3d_converter/image0012.jpg' | relative_url }})

Objects convert window in batch mode

In interactive mode (after simulating the 2D operation) or if converter operator itself as first operation both “Force to regenerate for all objects” check box and generate button will be active, so user can generate the all objects mesh and geometry as per the selection forcefully by using by checking this check box. User can also convert mesh and geometry for missing object in interactive mode by using generate button without checking this check box.

For interactive mode 2D plane strain geometry type converter setup the converter window status is as shown in Fig. 44.1.13. In this Fig. 44.1.13. Workpiece and Top die Mesh status is converted but Bottom die mesh is not converted, to convert only not-converted objects user has to select the ![]({{ '/assets/icons/pre_icons/mo_generate_2_button.jpg' | relative_url }}) button. All objects can also forcefully converted in one go by selecting the "Force to regenerate for all objects" check box and selecting the ![]({{ '/assets/icons/pre_icons/mo_generate_2_button.jpg' | relative_url }}) button.

![]({{ '/assets/images/operation_templates/44_2d_to_3d_converter/44_1_2d_to_3d_converter/image0013.jpg' | relative_url }})

Objects convert window in interactive mode

## Generate DB

In batch mode DB generation window will give the status as “DB generation is not required for this operation. It will occur at run time” as shown in Fig. 44.1.14.

In Interactive mode after 2D operation simulation or converter operation itself as first operation case generate Database option will be active and status will be Ready. If the input fields are not defined or objects are not converted in interactive mode then Status will be "Input error".

![]({{ '/assets/images/operation_templates/44_2d_to_3d_converter/44_1_2d_to_3d_converter/image0014.jpg' | relative_url }})

Database generation window for converter operation in batch mode

## Continue 3D problem setup after converter operation

After 2D to 3D Converter operator setup only 3D operations are allowed, so 3D operation added from explorer after converter operator will be linked automatically in operation editor as shown in Fig. 44.1.15.

![]({{ '/assets/images/operation_templates/44_2d_to_3d_converter/44_1_2d_to_3d_converter/image0015.jpg' | relative_url }})

Adding 3D operation after 2D to 3D converter

From operation editor select the 3D operation to continue the 3D operation setup. Based on the 3d operation objects will be passed automatically passed from previous operation. When we select the added 3D Forming operation, all the objects are transferred from previous operation as shown in Fig. 44.1.16.

![]({{ '/assets/images/operation_templates/44_2d_to_3d_converter/44_1_2d_to_3d_converter/image0016.jpg' | relative_url }})

Added objects to 3D Forming operation

Convert will not convert the movement and properties object data and simulation controls data, so user has to define these data in 3D operation. In this example define the same movement controls for top die as in first operation that is select hammer movement controls in -Z direction as shown in Fig. 44.1.17.

![]({{ '/assets/images/operation_templates/44_2d_to_3d_converter/44_1_2d_to_3d_converter/image0017.jpg' | relative_url }})

Movement controls for 3D operation top die object

Go to scheduled positioning window, add and define the interference positioning of workpiece with respect to bottom die in -Z direction, similarly interference position the top die with respect to workpiece in -Z direction as shown in Fig. 44.1.18. If user setup the converter in batch mode it is recommended to add the scheduled positioning of the objects after conversion in 3D operation. Also If user added new objects in the 3D operation along with converted objects scheduled positioning is required.

![]({{ '/assets/images/operation_templates/44_2d_to_3d_converter/44_1_2d_to_3d_converter/image0018.jpg' | relative_url }})

Schedule positioning for objects

Define the default contacts relations and go to Simulation controls to define the step controls as in first operation as shown in Fig. 44.1.19.

![]({{ '/assets/images/operation_templates/44_2d_to_3d_converter/44_1_2d_to_3d_converter/image0019.jpg' | relative_url }})

Simulation controls settings

## Simulate integrated 2D and 3D setup

After completing the problem setup submit the project to Run from MO simulation mode and observe the LOG message tab after the completion of 2D operation for the 2D to 3D conversion messages. Fig. 44.1.20. shows the 2D to 3D conversion messages for the example explained in this manual for one workpiece and two rigid die objects conversion. Beginning of the conversion is indicated by message line "$BGN$" and end of the conversion process will be indicated by message line "$END$". 

![]({{ '/assets/images/operation_templates/44_2d_to_3d_converter/44_1_2d_to_3d_converter/image0020.jpg' | relative_url }})

2D to 3D conversion LOG messages

## Post process the integrated 2D and 3D model in MO Post

From MO Post user can review the 2D and 3D integrated DB, selection of the particular 2D or 3D operation step will load the respective step in respective mode and in 2D to 3D converter will be having only negative step where converted 3D model is available as shown in Fig. 44.1.21.

![]({{ '/assets/images/operation_templates/44_2d_to_3d_converter/44_1_2d_to_3d_converter/image0021.jpg' | relative_url }})

2D to 3D converter operator step in MO post

User can play the animation and plot all state variables and use other post features available in MO post for more option user can select the ![]({{ '/assets/icons/pre_icons/mo_post_label_link.jpg' | relative_url }}) action label to open the DB in Post processor. For information on Post Processor options refer [26\. Post Processor Features](/docs/en/post_processor/26_post_processing_tools_and_controls/26_post_processor_features/).

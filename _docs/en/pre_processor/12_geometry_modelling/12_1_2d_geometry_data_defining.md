---
lang: en
title: "12.1. 2D Geometry Data Defining"
---

# 12.1. Defining 2D Geometry Data

12.1.1. Geometry Rules for 2D

12.1.2. 2D Geometry Tools

12.1.3. 2D Geometry data Importing and Saving

12.1.4 Settings

2D Geometry page is as shown in below Fig. 12.1.1.

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_1_2D_Geometry_Data_Defining/12_1_Image003.jpg)

2D Geometry page

## Geometry Rules for 2D

**Orientation**  
The endpoints of line segments are defined numerically. For all die definitions, all objects should be numbered such that the die block is on the left, and open air (contact zone) on the right as you move along the points in the order. Failure to follow this orientation may cause any of the following problems:

  * Object won't mesh.
  * Mesh distorts when boundary conditions are applied.
  * Object positioning error using interference positioning.

**Direction**

Objects must be defined counter clockwise (CCW). The orientation direction may be checked using the point numbering button in the geometry editing window.

If the current connectivity is clockwise (either after drawing or after importing), it can be reversed. The geometry reverse function reverses the current connectivity of the object by clicking the Reverse button.

**Edges**  
The die starting and stopping point must be away from the contact zone, unless points are on the axis of symmetry. Tooling which crosses the centerline should do so at 90 degrees: other angles may lead to non-convergence. In case of a pointed punch, a very short line segment should be added at the center.

**Blended fillets**

The connectivity between blended fillets is ill-defined in IGES format. To avoid problems, it is helpful to define a very short line segments between arcs. Blended fillets can cause DEFORM-2D to continuously give an incorrect geometry message, even once the geometry has been checked and corrected. To correct this, simply add an extremely small line segment between the two fillets.

**End points**

The radius of the first and last points must be zero.

**Clearance fits**

Tooling with close clearance fits should be drawn to overlap slightly. Failure to overlap tooling may allow nodes to slip between the punch and the die, and cause problems when the mesh regenerates. A "negative jacobian" error in the message file will result.

## 2D Geometry Tools

**Define Primitives** ![](../../../assets/Icons/Pre_icons/MO_Define_Primitive_label.jpg): There are now five primitive shapes in general geometry page that can be used to generate geometries as seen in Fig. 12.1.2. and Fig. 12.1.3. In each case, the user has to scale appropriately to the problem by defining the dimensions.

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_1_2D_Geometry_Data_Defining/12_1_Image004.JPG)

2D Axisymmetric and Torsion Geo Primitive options

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_1_2D_Geometry_Data_Defining/12_1_Image005.JPG)

2D Plane strain and Stress Geo Primitive options

**Scale Geometry**![](../../../assets/Icons/Pre_icons/MO_Scale_label.jpg) **:** Geometry can be scaled in Preprocessor specifying the scaling factor. (See Fig. 12.1.4.) The scaling factor can be calculated by temperature differential and temperature dependent material data and scaled geometry can be saved in the Geometry saving formats.

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_1_2D_Geometry_Data_Defining/12_1_Image001.jpg)

Geometry scaling options

**CAD Interface** ![](../../../assets/Icons/Pre_icons/MO_CAD_Interface_Label.jpg)**:** Using this option user can import CAD geometry file directly for Soildworks directly.

**Construct by Subtract**![](../../../assets/Icons/Pre_icons/MO_Construct_by_substraction_button.jpg) **:** This option is used to create geometry by subtracting geometry of other objects that are already present. Here the starting point, width and height of the object geometry from which other geometries to be subtracted must be specified as shown in Fig. (See Fig. 12.1.5.)

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_1_2D_Geometry_Data_Defining/12_1_Image006.jpg)

Construct by Subtract window

**Check Geometry** ![](../../../assets/Icons/Pre_icons/MO_Check_label.jpg)

Once the geometry of the object is created, Check GEO button gets activated. It is necessary to check the orientation of the geometry. This can be done by clicking on the ![](../../../assets/Icons/Pre_icons/MO_Check_label.jpg)button a popup appears as shown in below Fig. 12.1.6. The Geometry gets corrected when we click on check & correct geometry button.

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_1_2D_Geometry_Data_Defining/12_1_Image002.JPG)

Check Geometry options window in 2D mode

Below are a few common geometric errors in DEFORM 2D and how they are corrected by DEFORM.

**GEOMETRY ERROR** | **RECOMMENDED CORRECTION**  
---|---  
Duplicate points |  Remove the duplicate point  
Adjacent points are collinear |  Remove the collinear point (s)  
Corner radius is so large that at least one of the tangent points lies outside the tangent line defined by the adjacent points  |  Reduce the corner radius so that both tangent points lie within the tangent line segments  
Arc interference at adjacent points: opposite arc orientations |  Adjust the radii of the points so that the common tangent point lies on the line connecting the points  
Arc interference at adjacent points: same arc orientation  |  Adjust the radii so that the common tangent point becomes the intersection point of the two arcs projected on the common tangent line  
Line entity with zero length |  Remove entity  
Arc entity with zero radius |  Remove entity  
Adjacent entities cross  |  Modify entities so that the intersection point becomes the ending point of one entity and the starting point of the other entity  
Unconnected adjacent entities |  Add a line segment to connect the entities  
  
Corrective measures to be taken for DEFORM 2D geometry

**System Defects:** when user checks geometry if there is any misorientation it gets corrected whether it is closed or open Geometry.

**Closed:** It checks the orientation of geometry and closes the geometry. If user creates an open geometry, it get closes by joining start and end points by selecting closed geometry.

**Open Geometry:** If user creates an open geometry, it checks the orientation and keeps the geometry in open.

**Remove collinear points:** When user check remove collinear points check box it removes the collinear points present in the geometry.

**Reverse**![](../../../assets/Icons/Pre_icons/MO_Reverse_label.jpg) : This feature reverses the orientation of the geometry. Orientation of the 2D geometry must be always inside for single loop geometry, for multiple loop geometry the loop which share between the two regions can have the orientation on either side, but topology must be defined.

**Edit**![](../../../assets/Icons/Pre_icons/MO_Edit_lable.jpg) : This feature helps to edit boundary of the 2D object. The Geometry editing window is used to create, modify or view the geometry of a given object. The window appears upon selecting the ![](../../../assets/Icons/Pre_icons/MO_Edit_lable.jpg) in the Geometry window. Refer [Chapter 12.2. 2D Geometry Editing.](/docs/en/pre_processor/12_geometry_modelling/12_2_2d_geometry_editing/)

**Extract Border**![](../../../assets/Icons/Pre_icons/MO_Extract_border_button.jpg) : This feature extracts the geometry data from the current database for all object types except the rigid object.

**Extract from Mesh**![](../../../assets/Icons/Pre_icons/MO_Extract_From_mesh.jpg) : This feature extracts geometry from the mesh.

**Show geometry inside mark** : Checking this option enables the Geometry orientation display.

**Delete geometry :** Using Delete ![](../../../assets/Icons/Pre_icons/MO_clear_icon.jpg) option the object geometry gets deleted.

## 2D Geometry data Loading and Saving 

**Importing Geometry :** Geometry can be imported from a file ![](../../../assets/Icons/Pre_icons/MO_Import_file_icon.jpg) or Load geometry from library ![](../../../assets/Icons/Pre_icons/MO_Load_from_Library_icon.jpg) options, a DEFORM native graphics file (AMGGEO), keyword file, database file or created using the geometry editor. When importing IGES files or dxf files, use the mouse to select the object you wish to import. Click on any line segment in the object. Any segments connected to this object will also be selected and highlighted.

**AMGGEO format input [2D]**

The AMGGEO format is the mesh generators internal format for handling geometries. This format can specify geometry as a set of connect points, the XYR format, the line-arc format, and as a set of boundary nodes.

Note:

It is necessary to use the mouse to select the object to be imported even if there is only a single object in the drawing file.

**Assign the file name to the object name while loading geometry** : When user checks this option while loading or importing geometry file, it assigns the geometry file name to the Object name.

**Save geometry :** Saves geometry to a file ![](../../../assets/Icons/Pre_icons/MO_Save_to_a_file_icon.jpg) or to library uisng ![](../../../assets/Icons/Pre_icons/MO_Save_to_Library_icon.jpg). Saves geometry in IGES, DXF and DEFORM native GEO format for 2D.

## Settings ![](../../../assets/Icons/Pre_icons/MO_Settings_icon.jpg)

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_1_2D_Geometry_Data_Defining/12_1_Image007.jpg)

2D Geometry Settings Window

**Tolerance:** Sets the tolerance level for joining two boundary points which are close together when an object is imported in IGS and DXF geometry formats, and before transferring the data into DEFORM are defined here. ( Fig. 12.1.7.)

**No. of discretization points:**

[12\. Geometry Modelling](/docs/en/pre_processor/12_geometry_modelling/12_geometry_modelling/)

[12.2. 2D Geometry data Editing](/docs/en/pre_processor/12_geometry_modelling/12_2_2d_geometry_editing/)

[12.3. 3D Geometry data Defining](/docs/en/pre_processor/12_geometry_modelling/12_3_3d_geometry_data_defining/)

[12.4. 3D Geometry data Editing (GEO TOOL)](/docs/en/pre_processor/12_geometry_modelling/12_4_3d_geometry_data_Editing_geo_toolL/)

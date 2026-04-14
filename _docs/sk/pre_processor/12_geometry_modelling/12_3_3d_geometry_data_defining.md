---
lang: sk
title: "12.3. 3D Geometry Data Defining"
---

# 12.3. 3D Geometry Data Definition

12.3.1. Geometry rules for 3D

12.3.2. 3D Geometry Tools

12.3.3. 2D Geometry data Importing and Saving

12.3.4. Settings

3D Geometry window is used to define the geometry of an object as shown in Fig. 12.3.1. Only define primitive, CAD interface, Edit and Preform field will be in active mode rest other options will be in grayed when no geometry is defined. Once after creating geometry all the options will be activated.

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_3_3D_Geometry_Data_Definition/12_3_Image001.jpg)

3D Geometry window

## Geometry rules for 3D

There are several conventions that must be followed when defining object surfaces in DEFORM.

**Orientation of Surface****Normals :** ****In DEFORM the surface normals of the closed geometries should point outwards from the geometry. This is how DEFORM defines the exterior of an object. In the case of a surface that isn't closed, the surface normals should point toward the deformable objects and great care should be taken that no nodes see the back of the object. In the case where a rigid plane is used to constrain a workpiece, it is recommended to make the plane sufficiently large such that the nodes cannot see around the plane. In the Geometry window, the direction of the surface normals can be viewed by clicking on the surface normal button in the lower left part of the screen. Failure to follow this convention may cause any of the following problems:

  * Object won't [mesh](/docs/sk/pre_processor/13_Mesh_Generation/13_Mesh_Generation/)
  * Mesh distorts when[ boundary conditions](/docs/sk/pre_processor/14_Boundary_Conditions/14_boundary_conditions/) are applied
  * [Object positioning](/docs/sk/pre_processor/19_Object_Positioning/19_Object_Positioning/) error using interference positioning

**Surface Patches :** In DEFORM a surface patch is defined by a section of a surface that is separated from other portions of the same surface by a 30 degree or greater bend in the surface. For example, a cube would have six surface patches due to the edges between each side having a 90 degree bend in the surface. In order to view the surface patches in DEFORM the user may click on the surface patches button in the geometry window at the lower left section of the screen. Any bend in the surface greater than 30 degrees will appear as a thick red line. The benefit of this feature is that folds in the surface will appear as red slivers in the middle of the geometry. This provides a method for finding where folds may exist.

**Border Extraction** : Border extraction is the process of identifying the deformed part surface geometry from the surface of the finite element mesh. Geometric reasoning is used to identify critical features such as edges, corners, and symmetry planes which should be maintained during remeshing.  
Border extraction can fail for the following reasons:

  * **Folds or crossed elements** [3D]

If a closed forming lap develops in the process, the surface geometry will be ill-defined. If an excessively large time step is used without [polygon length sub stepping](../9_Simulation_Controls/9_2_Defining_Step.htm#Polygon_length_sub_step_\(DPLEN\)), element faces can become crossed, also causing an ill-defined surface. Both of these cases can frequently be identified using the surface patches display in the geometry window.If a legitimate forming lap is developing, the process should be redesigned to eliminate the lap. If the lap is in a region where it is acceptable, it may be necessary to use a CAD system to edit the geometry, then remesh the part and interpolate data.If element faces are crossed, it is generally necessary to revert to the last good step in the database. The situation can be avoided by using a smaller time step, using [polygon length sub stepping](../9_Simulation_Controls/9_2_Defining_Step.htm#Polygon_length_sub_step_\(DPLEN\)), using smaller elements around tight corners, and force remeshing on a fixed step or stroke interval (under remeshing criteria).

**Parallel symmetry planes** : When using symmetry, the user should not specify parallel fixed velocity boundary conditions. (for a comprehensive discussion on symmetry planes, refer to the [Appendix VIII](/docs/sk/Appendices/Appendix_VIII_Preventing_leakage_of_nodes/) on the use of symmetry planes in 3D) In the case where two parallel symmetry planes are necessary, the user can specify one fixed velocity boundary condition and one rigid plane with no friction and a non-separable contact condition (To see how to implement this, please refer to the [Appendix VIII](/docs/sk/Appendices/Appendix_VIII_Preventing_leakage_of_nodes/) on the use of symmetry planes in 3D). If two fixed velocity boundary conditions are set parallel to one another, border extraction will surely fail, causing any remeshing to fail.

If the symmetry plane is not sufficiently large to cover the entire area where symmetry needs to be defined, it is possible that nodes may move around the plane of symmetry and this will also cause border extraction to fail. Since rigid planes, when used to define symmetry planes, need not have relations to any objects other than the workpiece, they may be arbitrarily large. For display reasons, the user is not recommended to make the rigid planes unreasonably large.

## 3D Geometry Tools

**Define Primitive** ![](../../../assets/Icons/Pre_icons/MO_Define_Primitive_label.jpg) : We have three different types of Geometry primitives such as Box, Cylinder and Hollow Cylinder as shown in Fig. 12.3.2. Extrude and Revolve can be used to convert 2D cross-section to 3D.

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_3_3D_Geometry_Data_Definition/12_3_Image002.jpg)

Geometry primitive window

**CAD Interface** ![](../../../assets/Icons/Pre_icons/MO_CAD_Interface_Label.jpg) : Using this option user can import CAD geometry file directly for Soildworks directly.

**Preform**![](../../../assets/Icons/Pre_icons/MO_Preform_label.jpg) :

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_3_3D_Geometry_Data_Definition/12_3_Image020.jpg)

3D Preform window

**Edit**![](../../../assets/Icons/Pre_icons/MO_Edit_lable.jpg) : Using Edit option we can modify the existing geometry in 3D GEO TOOL wizard. Refer Chapter [12.4. 3D Geometry Editing.](/docs/sk/pre_processor/12_geometry_modelling/12_4_3d_geometry_data_Editing_geo_toolL/)

**Extract Border** ![](../../../assets/Icons/Pre_icons/MO_Extract_border_button.jpg) : This feature extracts the geometry data from the current database meshed object for all object types except the rigid object.

**Extract from Mesh** ![](../../../assets/Icons/Pre_icons/MO_Extract_From_mesh.jpg) : This feature extracts geometry from the 3D object mesh.

**Check**![](../../../assets/Icons/Pre_icons/MO_Check_label.jpg) : Always check geometry. DEFORM has a checking algorithm that checks for number of invalid edges, invalid orientation, polygons with small area and number of surfaces. Every type of error cannot be detected.

Using this Check Geometry option opens the Geometry Checking Results window which gives a summary of the object’s geometry (See Fig. 12.3.4.). For an object that has a closed volume, there should be 1 surface, 0 free edges and 0 invalid entities (as circled below in Fig. 12.3.4.). Objects that are imported as surfaces and not solids will have a free edge but should still only have 1 surface.

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_3_3D_Geometry_Data_Definition/12_3_Image004.jpg)

Geometry Checking Results

**GEOMETRY ERROR** | **RECOMMENDED CORRECTION**  
---|---  
Poly with invalid orientation |  Either fix the STL file in the solid modelling package or Find the problematic poly in the Preprocessor and fix the STL file manually.  
Poly with small area |  Increase the error tolerance slightly  
Poly with invalid edge |  Fix the geometry in the solid modelling package  
  
Corrective measures to be taken for DEFORM 3D geometry

  
Note: Correct orientation of the surface normals is NOT checked in geometry checking if all the normals are pointed in a consistent direction. 

**Fix**![](../../../assets/Icons/Pre_icons/MO_Fix_label.jpg) : This feature will handle geometric problems where there are either multiple surfaces or open (holes) regions by deleting any extra surfaces and filling holes. For minor or localized problems, this works well. For more troublesome file such as this one, the repair may not produce a desirable result.(See Fig. 12.3.5.)

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_3_3D_Geometry_Data_Definition/12_3_Image005.jpg)

Fixing Geometry of crankshaft Die

**Scale**![](../../../assets/Icons/Pre_icons/MO_Scale_label.jpg) :Geometry can be scaled in forming operation to accommodate thermal expansion by specifying the scaling factor. (See Fig. 12.3.6.) The scaling factor can be calculated by temperature differential and temperature dependent material data. The scaled geometry can be saved into different Geometry saving formats.

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_1_2D_Geometry_Data_Defining/12_1_Image001.jpg)

Scale Geometry window

**Reverse**![](../../../assets/Icons/Pre_icons/MO_Reverse_label.jpg) : This feature reverses the surface/ normal of the geometry. Always surface/ Normal of the geometry should be outwards.

**Find axis** ![](../../../assets/Icons/Pre_icons/MO_Find_Axis_label.jpg) : This feature determines the axis of the geometry automatically based on the geometry definition and displays it.

**Setup Brick Mesh** ![](../../../assets/Icons/Pre_icons/MO_Setup_brick_mesh_label.jpg) : In order to define Brick mesh, user has to define start surface and End surface for created geometry as shown in Fig. 12.3.7. Brick mesh is used for the geometries of regular or identical cross-section.

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_3_3D_Geometry_Data_Definition/12_3_Image007.jpg)

Setup Brick Mesh window for Extrusion

Brick mesh can be generated by selecting Extrude or Revolve options based on the geometry. If user selects Extrude radio button the brick mesh will be extruded with respect to start and end point as shown in Fig. 12.3.8.

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_3_3D_Geometry_Data_Definition/12_3_Image008.jpg)

Brick mesh of Extruded object

If user selects Revolve radio button the brick mesh will be revolved in Z direction as shown in Fig. 12.3.9. and Fig. 12.3.1.10.

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_3_3D_Geometry_Data_Definition/12_3_Image009.jpg)

Setup brick mesh window for revolving

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_3_3D_Geometry_Data_Definition/12_3_Image010.jpg)

Brick mesh of Revolving object

**Symmetry Planes** ![](../../../assets/Icons/Pre_icons/MO_Symmetry_Planes_label.jpg): Both planar symmetry and rotational symmetry can be defined. In the case of planar symmetry, the simulation will have extra information that allows it to prevent material from flashing around it. In the case of rotational symmetry, meshing will automatically place the proper boundary conditions on the faces. This is meant as a uniform place to apply symmetry boundary conditions for all objects.

  * **Specifying Planar Symmetry** : To specify planar symmetry, select the symmetry plane on the geometry, then click on ![](../../../assets/Icons/Pre_icons/MO_Add_Icon2.jpg). The planar symmetry condition will be added to the list of currently specified symmetry. (See Fig. 12.3.11.) When symmetry plane is defined, during mesh generation a pop up appears with a message as shown in Fig. 12.3.12., requesting the user whether to create a default boundary condition, the user can select "No" option, if user would not like to use default BCC assigned by system based on symmetry conditions defined.

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_3_3D_Geometry_Data_Definition/12_3_Image011.jpg)

Assigning symmetry surfaces

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_3_3D_Geometry_Data_Definition/12_3_Image012.jpg)

Default Boundary Conditions popup window

Note: Symmetry Popup message appears only when we setup a problem in Expert mode.

  * **Specifying Rotational Symmetry** : To specify rotational symmetry, specify the point and vector of the rotational axis as well as the degree of symmetry available as shown in Fig. 12.3.13. After this, click on the starting plane and end plane of the geometry in the direction of rotation so that rotational symmetry to be applied. The symmetry condition will be added to the list of currently specified symmetry. For more information about rotational symmetry option refer to [16.7. ](/docs/sk/pre_processor/16_Object_Properties/16_7_symmetry_properties/)[Rotational Symmetry](/docs/sk/pre_processor/16_Object_Properties/16_7_symmetry_properties/).

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_3_3D_Geometry_Data_Definition/12_3_Image013.jpg)

Rotational symmetry window

**Examine**![](../../../assets/Icons/Pre_icons/MO_Examine_label.jpg) : This feature helps to examine the 3D geometry points and polygons. The geometry point’s co-ordinates can also be edited by using points co-ordinates fields and apply button after changing these co-ordinates. The current selection of the point and polygon display is highlighted by sphere or cube shapes using the check boxes at the bottom of the window.(See Fig. 12.3.14.)

From DEFORM V12, using ![](../../../assets/Icons/Pre_icons/MO_Tolerance_icon.jpg) ("Detect zones") next to Surface field option we can calculate the number of zones exist in Geometry and for each zone we can assign different material or Layer ID using Assignment option. This option helps the user to model multi-layered composites, voids, inclusions,additive manufacturing,..etc.

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_3_3D_Geometry_Data_Definition/12_3_Image006.jpg)

Geometry settings of Examine window

**2D to 3D conversion** ![](../../../assets/Icons/Pre_icons/MO_2D_to_3D_conversion.jpg) : User can define 2D cross section geometry which can be used to generate 3D geometry by checking Use Cross Section check box.

**Define Primitive** ![](../../../assets/Icons/Pre_icons/MO_Define_Primitive_label.jpg) : We have three different types of Geometry primitives such as Bar, Cylinder and Hollow Cylinder as shown in  Fig. 12.3.15. This geometry window appears for plane strain type of geometry.

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_1_2D_Geometry_Data_Defining/12_1_Image005.JPG)

2D Geometry primitive window for plane strain and plane stress Axisymmetric

The geometry window appears for Axisymmetric type of geometry is shown in Fig. 12.3.16.

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_1_2D_Geometry_Data_Defining/12_1_Image004.JPG)

2D Geometry primitive window for Axisymmetric and Torsion

**Check**![](../../../assets/Icons/Pre_icons/MO_Check_label.jpg) : Once the geometry of the object is created, ![](../../../assets/Icons/Pre_icons/MO_Check_label.jpg) button gets activated. It is necessary to check the orientation of the geometry. This can be done by clicking on the ![](../../../assets/Icons/Pre_icons/MO_Check_label.jpg) button a popup appears as shown in below Fig. 12.3.17. The Geometry gets corrected, if they are any errors when we click on ![](../../../assets/Icons/Pre_icons/MO_Check_and_Correct_geo_button.jpg) button. A message saying, "Geometry is legal" will appear once the geometry is corrected or does not have any errors and then click on ![](../../../assets/Icons/Pre_icons/MO_OK_button2.jpg). For more information please refer [Check Geometry](12_1_2d_geometry_data_defining.htm#Check_Geometry)

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_3_3D_Geometry_Data_Definition/12_3_Image014.jpg)

Check Geometry popup window

**Edit**![](../../../assets/Icons/Pre_icons/MO_Edit_lable.jpg) : The Geometry editing option is used to create geometry for an object or edit the existing geometry. Imported geometry can be modified in Edit Geometry window.

For more information on 2D edit geometry, please refer [12.2. 2D Geometry Data Editing](/docs/sk/pre_processor/12_geometry_modelling/12_2_2d_geometry_editing/)

**Show geometry inside mark** : Checking this option enables the Geometry orientation display.

**Settings**![](../../../assets/Icons/Pre_icons/MO_Settings..._button.jpg) : After creation of 2D geometry using these settings user can create 3D geometry from 2D geometry.

**Extrude** : The user can import the 2d cross-section or use defined 2D cross-section of the geometry and extrude it in the desired direction. This can also be done while importing the 2d cross-section files from the DB or key file.(See Fig. 12.3.18.)

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_3_3D_Geometry_Data_Definition/12_3_Image015.jpg)

2d cross-section window settings for extrusion

**Revolve** : The user can import the 2d cross-section of the geometry and revolve the geometry based upon the symmetry to get a 3d cross-section. (See Fig. 12.3.19.)

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_3_3D_Geometry_Data_Definition/12_3_Image016.jpg)

2D cross-section window settings for Revolving

**Generate 3D** ![](../../../assets/Icons/Pre_icons/MO_Generate_3D_button.jpg): By clicking on this button or inside Settings page ![](../../../assets/Icons/Pre_icons/MO_Generate_3D__label.jpg) button, created 2D geometry can be extruded or revolved to 3D geometry.

**Show Geometry Normal Vectors** : This feature shows the geometry surface normal vectors. If the geometry is a closed volume, the correct orientation is defined when the surface normals are pointing out of the object. When the geometry is not a closed volume but is just a surface, the correct orientation is defined when the normals are pointing towards the workpiece.(See Fig. 12.3.20)

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_3_3D_Geometry_Data_Definition/12_3_Image017.jpg)

Show Geometry Normal Vectors

**Transparent** : By checking this check box it will turn on the transparency of the object. (See Fig. 12.3.21.)

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_3_3D_Geometry_Data_Definition/12_3_Image018.jpg)

Transparent check box option

**Delete Geometry**![](../../../assets/Icons/Pre_icons/MO_clear_icon.jpg) : It deletes the created geometry.

## 3D Geometry data Importing and Saving

**Import Geometry :** Geometry can be imported from a file ![](../../../assets/Icons/Pre_icons/MO_Import_file_icon.jpg) or Load geometry from library ![](../../../assets/Icons/Pre_icons/MO_Load_from_Library_icon.jpg) options, a DEFORM native graphics file (AMGGEO), keyword file, database file or created using the geometry editor. When importing STL files or PATRAN files, use the mouse to select the object you wish to import. Click on any line segment in the object. Any segments connected to this object will also be selected and highlighted.

Geometry formats :

  * STL format input (DIEGEO)
  * AMGGEO format input
  * PATRAN format input
  * IDEAS format input
  * NASTRAN format input
  * 2D IGES format input

**STL format input (DIEGEO)**

The STL format ([DIEGEO](/docs/sk/Keyword_Documentation/D/DIEGEO/)) represents a surface by a series of three sided facets. This format may be created from almost all commercial solid modelling packages from a either a solid model or a surface model. For very simple shapes, such as a cube, very few facets may be used to provide an excellent representation of the shape. In the case of an extrusion die where the facets are used to model a curved surface, many facets may be required in order to give the object a smooth representation or to render small details in a geometry. An economy of the number of facets used to represent a geometry is recommended in order to minimize the size of the database file. As more facets are used, the size of each step in the database file will increase. The increase in the time for the contact calculations is negligible with the increase of the number of facets in the die geometries.

Upon inputting an STL file into the Pre-processor, the user is immediately prompted for a error tolerance value. This value is the snapping distance between the points in the STL file. Since the facets are not dependent on each other, the points in which adjacent facets share may not be represented exactly the same way in an STL file. Since they were meant to be the same point, the Preprocessor assumes some error tolerance where the points are merged into representing the same point. The default value of 1e-005 is usually a good starting value. If there are small cracks in the die geometry, they may closed by increasing the error tolerance value and hoping that the cracks are snapped closed. This is not a very controlled manner in which to close any cracks and should be used with extreme caution. After using this method, the geometry should be carefully checked to ensure that no holes are introduced or important features are lost.

The file format for STL files may be either ASCII or binary format. DEFORM can both read and write ASCII and binary versions of the STL file. The facets are all defined independently of each other, so the danger of there being folds, holes, overlapping facets, or invalid facet orientations is possible. After reading an STL file, it is strongly recommended to check the geometry to make sure that there are no folds, holes or other problems. If there are geometry problems in a deforming body, problems may occur upon meshing the object. If there are geometry problems in a rigid die, problems may occur during the simulation where nodes get trapped and severely compromise the integrity of the deforming body. This can be very problematic since problems in die geometries may not occur until well into a simulation. The manner in which to best determine if a die geometry is well defined or not is to try to apply a mesh to it. If a mesh can be generated on geometry, then it is a well defined geometry, however, if the meshing fails, then it is possible that there is a problem with the geometry definition.

**AMGGEO format input**

The AMGGEO format is a DEFORM internal format for handling geometries. This format can specify a surface as a set of connecting triangles or quadrilaterals. If quadrilaterals are used, degenerate elements (i.e. triangles) are not permitted. The patch normals must be out of the element. That is, the points should be numbered counter clockwise when viewed from the outside of the object. The file can be created and edited using a text editor such as vi, emacs, or Notepad.

The file format is  
NUMBER OF VERTEX POINTS

1 X1 Y1 Z1

2 X2 Y2 Z2 

...... N 

XN YN ZN

NUMBER OF

SURFACE PATCHES

1 first patch connectivity 1 2 3 (1/4)

2 second patch connectivity 1 2 3 (1/4) 

......

N Nth patch connectivity 1 2 3 (1/4)

where (1/4) in the connectivity indicates that point 1 is repeated in the 4th position in a triangular patch. All 4 points are used for a quadrilateral patch.

A 1'' by 1'' square patch in the xy plane with normal pointing along the z axis would be defined as follows:

4

1 0. 0. 0.

2 1. 0. 0.

3 1. 1. 0.

4 0. 1. 0.

1

1 1 2 3 4

The square would be defined using two triangles as follows:

4

1 0. 0. 0.

2 1. 0. 0.

3 1. 1. 0.

4 0. 1. 0.

2

1 1 2 3 1

2 1 3 4 1

  
**PATRAN format input [3D]**

The PATRAN neutral file format is an output format from PATRAN. This format specifies a either a surface mesh or a solid mesh which can be used to either represent a geometry. Upon loading a PATRAN neutral file, the user is first prompted whether the neutral file is either a surface mesh or a solid mesh. After the user provides the information on whether the file is a surface or a solid mesh, the user is prompted to provide a conversion factor. This is merely a scaling variable and the user is recommended to just use the default value of 1.

DEFORM®-3D imports .PDA and .PAT 3d geometry files formats.

**IDEAS format input [3D]**

The IDEAS neutral file format is an output format from IDEAS. This format specifies a surface mesh which can be used to either represent a geometry in DEFORM or as a basis for a solid mesh. Upon loading an IDEAS universal file, the user is first prompted to provide a conversion factor. This is merely a scaling variable and the user is recommended to just use the default value of 1.

**NASTRAN format input [3D]**

****DEFORM- 3D imports the NAS 3D geometry format. While importing scaling can be done by using the scaling factor in the options gemetry tab.

**2D IGES format input [3D]**  
3D geometry can also be created by extruding 2D IGS geometry file, using Import Geometry option by specifying extrision length and direction. Fig. 12.3.22. shows the 2d IGES geometry extrusion settings window which pops up while importing geometry using the import geometry option.

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_3_3D_Geometry_Data_Definition/12_3_Image003.jpg)

Extrude Direction and Length window for 2D IGES import in 3D mode

**Assign the file name to the object name while loading geometry :** When user checks this option while loading or importing geometry file, it assigns the geometry file name to the Object name.

**Save Geometry** : Saves geometry to a file ![](../../../assets/Icons/Pre_icons/MO_Save_to_a_file_icon.jpg) or to library ![](../../../assets/Icons/Pre_icons/MO_Save_to_Library_icon.jpg). We can save geometry in STL, PATRAN, UNV and DEFORM native GEO format for 3D.

## Settings ![](../../../assets/Icons/Pre_icons/MO_Settings_icon.jpg)

**2D Import** :

**Tolerance:** Sets the tolerance level for joining two boundary points which are close together when an object is imported in IGS and DXF geometry formats, before transferring the data into DEFORM are defined here. (See Fig. 12.3.23.)

**No. of discretization points:**

![](../../../assets/Images/Pre-Processor/12_Geometry_Modelling/12_3_3D_Geometry_Data_Definition/12_3_Image019.jpg)

3D Geometry Tolerance settings window

**3D Import** :

**Tolerance:** level for joining two boundary points which close together when an object is imported from STL geometry formats and before transferring the data into DEFORM are defined here. (See Fig. 12.3.23.)

**Scaling Factor:** It will scale the 3D geometry while loading imported geometry. Required scaling factor must be specified before importing the geometry in order to scale the importing geometry. By default the value will be 1 means no scaling, for 0.5 it scales down to half of its original geometry and for 2 it doubles its original geometry. (See  Fig. 12.3.23.)

Related Topics:

[12\. Geometry Modelling](/docs/sk/pre_processor/12_geometry_modelling/12_geometry_modelling/)

[12.1. 2D Geometry data Defining](/docs/sk/pre_processor/12_geometry_modelling/12_1_2d_geometry_data_defining/)

[12.2. 2D Geometry data Editing](/docs/sk/pre_processor/12_geometry_modelling/12_2_2d_geometry_editing/)

[12.4. 3D Geometry data Editing (GEO TOOL)](/docs/sk/pre_processor/12_geometry_modelling/12_4_3d_geometry_data_Editing_geo_toolL/)

[13\. Mesh Generation](/docs/sk/pre_processor/13_Mesh_Generation/13_Mesh_Generation/)

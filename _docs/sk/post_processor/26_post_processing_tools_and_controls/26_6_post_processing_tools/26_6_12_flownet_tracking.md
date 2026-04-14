---
lang: sk
title: "26.6.12. Flownet Tracking"
---

# 26.6.12. Flownet Tracking

  * 2D Flownet

  * Rectangular Grid

  * Polygon Pattern

  * Offset Pattern

  * User Defined Flownet****

  * 3D Flownet

  * Cubic Pattern

  * Grid Pattern

  * Polygon Pattern

  * 2D Offset

  * Offset

  * Surface grid pattern

  * User Defined Flownet

  * Flowline tracking

**[2D, 3D]** : The flownet is a post-processing tool that allows the user to place some form (2D or 3D) of a grid onto the object and let the simulation track the deformation of the grid throughout the deformation. As the mesh deforms, so does the pattern, however, unlike the FEM mesh, the pattern remains intact throughout the remeshings. Thus, the flownet is much like physically etching a pattern on a cross section of a workpiece .This is an excellent way in which to visualize any potential irregularities in the grain structure or to view potential surface defects such as folds. It should be noted that flownet patterns can be generated only for deforming objects. The start step list will contain all of the steps in the display window currently loaded by default.

**2D Flownet** :

A flow net region is defined in the graphics window. It can be selected within an object’s border or boundary. In order to define a region, user must add at least three points within the object’s border. Afterwards respective pattern settings must be selected and preview the pattern. Once the pattern has been defined, select generate pattern in the pattern generation \ tracking window.

**Types of grid patterns available in 2D** :

Grid, Polygon, Offset and User defined are the grid pattern types available in 2D.

  * **Rectangular Grid [2D]**

The rectangular grid option will generate a grid composed of perpendicular lines within the desired region. Rectangular patterns are typically used when the material texture is of interest. This pattern is very similar to the grain flow which would be seen if a cross section of the part were etched. If a rectangular pattern is selected, you must specify the grid origin, orientation angle, and line spacing in X and Y.

**Steps to define Grid Pattern:**

  1. Select the type of grid pattern to be used (See Fig. 26.6.12.1.). The Rectangular grid is chosen. Define required number of Boundary points by clicking on workpiece and then Next is clicked. Also user can click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) without defining boundary points. By default system will consider workpiece boundary as boundary points.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image001.jpg' | relative_url }})

Flownet pattern generation

  1. At this time, the density of the grid needs to be specified. In the case of the grid, the number of grid can be set for a regularly spaced grid. By selecting preview the grid can be seen before calculating for all steps. After a desired grid is obtained, click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). (See Fig. 26.6.12.2.)

The grid definition can be controlled by the following parameters:

**Grid Data** :

**Number of Grids** : user can define number of grids in X and Y axis respectively.

**Spacing** :This is the distance (DX and DY) between each grid point in the X and Y directions.

**Number of Sections** : user can define number of sections to be displayed in 3D view.

**Rotation Angle** : This will determine the angle at which the grid will be drawn in degrees.

**Shift** : This is the origin of grid.

**Advanced Options** :

**Boundary** : To include only boundary of the grid.

**Parallel to X line** : To include X-lines of the grid.

**Parallel to Y line** : To include Y-lines of the grid.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image002.jpg' | relative_url }})

Flownet Grid definition Window

  1. At this time, advanced options are available such as saving either the beginning or end pattern (See Fig. 26.6.12.3.). This is useful if a flownet from a different database is to be output to. Click ![]({{ '/assets/icons/post_icons/mo_generate_button.jpg' | relative_url }})when finished and the flownet will be calculated. (See Fig. 26.6.12.4.) 

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image003.jpg' | relative_url }})

Advanced flownet settings window

A pattern can be tracked backwards by selecting a later step in the database as the starting step, then selecting an earlier step as the ending step.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image004.jpg' | relative_url }})

Example of 2D grid flownet

  * **Polygon Patte****rn [2D]:**

The generation of polygon pattern is as shown below. The user can also generate concentric circle flownet for tracing material flow using circular shape. The circular grid can generate a field of circles of a given radius and distance apart within the desired region. Circular patterns are typically used to monitor directional orientation of flow. If a polygon pattern is selected user must specify the grid origin, Diameter, center to center distance between polygons, number of segments in the polygons, and whether clipped circles should be included.

**Steps to define polygon pattern:**

  1. Select polygon type of grid pattern (See Fig. 26.6.12.5.). Define required number of Boundary points by clicking on workpiece and then Next is clicked. Also user can click next without defining boundary points. By default system will consider workpiece boundary as boundary points.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image005.jpg' | relative_url }})

Polygon region definition

  1. At this time, the density of the grid needs to be specified. In the case of the grid, the number of grid can be set for a regularly spaced grid. By selecting preview the grid can be seen before calculating for all steps. After a desired grid is obtained, click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). (See Fig. 26.6.12.6.)

The grid definition can be controlled by the following parameters: ****

**Grid Amount:**

  * **Number of Grids in X dir** : By selecting this radio button user can define no. of grids to be placed in X- direction.

  * **Center to center distance** : Specifies the vertical and horizontal distance between each center of neighboring polygons.

  * **Number of Sections** : It displays the defined number of sections, when user view in 3D mode.

**Diameter** : Specifies the size of each polygon.

**Type** : User can select required type of polygon patterns (circle, triangle, pentagon, diamond,hexagon etc..) to visualize the results.

**Show Clipped** : Includes any partial polygons that were clipped by the region’s boundaries. (default is yes)

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image006.jpg' | relative_url }})

Polygon grid definition

  1. At this time, advanced options are available such as saving either the beginning or end pattern (See Fig. 26.6.12.3.). This is useful if a flownet from a different database is to be output to. Click ![]({{ '/assets/icons/post_icons/mo_generate_button.jpg' | relative_url }}) when finished and the flownet will be calculated. (See Fig. 26.6.12.7.)

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image007.jpg' | relative_url }})

Example of 2D polygon flownet

  * **Offset Pattern [2D]**

The offset will draw an identical surface at a specified distance within the objects border. The border offset pattern is typically used to capture tendencies toward lap formations. If a border offset is selected you must specify the distance the border is offset.

**Steps to define Offset pattern:**

  1. Select Offset type of grid pattern (See Fig. 26.6.12.8.). Define required number of Boundary points by clicking on workpiece and then ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) is clicked. Also user can click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) without defining boundary points. By default system will consider workpiece boundary as boundary points.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image008.jpg' | relative_url }})

2D Offset for 2D problem

  1. The offset curve is controlled through the following parameter.

**Offset Distance** : The offset distance is a positive value specifying how far inside the region the identical border should be positioned.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image009.jpg' | relative_url }})

2D Offset boundary definition

  1. At this time, advanced options are available such as saving either the beginning or end pattern (See Fig. 26.6.12.3. This is useful if a flownet is to be output to a different database. Click ![]({{ '/assets/icons/post_icons/mo_generate_button.jpg' | relative_url }}) when finished and the flownet will be calculated. (See Fig. 26.6.12.10.)

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image010.jpg' | relative_url }})

Example of 2D offset grid pattern

**3D Flownet:**

In 3D flownet user need to define the 3d region boundary by 2d planes or 2d planar boundary based on the type of the flow-net in the graphics window. These boundaries must be within an object's border. Afterwards respective pattern settings must be selected and preview the pattern. Once the pattern has been defined, just select generate pattern in the pattern generation \ tracking window.

**Different types of Grid Patterns available in 3D** :

Cubic, Grid, Polygon, 2D Offset, Offset, Surface net and User defined are available in 3D.

  * **Cubic pattern [3D]**

The generation of cubic grid pattern is as shown below. First the grid region has to be defined as shown in Fig. 26.6.12.11. and then the grid definition has to be defined as shown in Fig. 26.6.12.12. and finally the cubic grid will be generated as shown in Fig. 26.6.12.13.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image011.jpg' | relative_url }}) ![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image012.jpg' | relative_url }})

Region definition for cubic grid pattern

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image013.jpg' | relative_url }})

Grid definition for cubic grid pattern

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image014.jpg' | relative_url }})

Example of Cubic grid pattern

  * **Grid Pattern [3D]**

  1. Select the **grid** type to be used (See Fig. 26.6.12.14.). Either 2D or 3D grids can be used. The 2D grids are less time-consuming for the same grid size since less information is required in two-dimensions. For this example, the grid selection is chosen and ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) is clicked.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image015.jpg' | relative_url }})

Flownet pattern generation

  1. For the 2D grid, a plane has to be defined by using a slicing plane. The plane selection method is similar to the method used by the slicing dialog (See Fig. 26.6.12.15.). After specifying a plane to be used, click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

  1. At this time, the density of the grid needs to be specified. In the case of the grid, the number of grid can be set for a regularly spaced grid. By selecting preview the grid can be seen before calculating for all steps. After a desired grid is obtained, click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). (See Fig. 26.6.12.15.)

The grid definition can be controlled by the following parameters:

Grid Data:

**Number of Grids:** user can define number of grids in X and Y axis respectively.

**Spacing:** This is the distance (DX and DY) between each grid point in the X and Y directions.

**Rotation Angle:** This will determine the angle at which the grid will be drawn in degrees.

  * **Shift** : This is the origin of grid.

**Advanced Options:**

  * **Boundary** : To include only the Boundary points.

  * **Parallel to X line** : To include X-lines of the grid.

  * **Parallel to Y line** : To include Y-lines of the grid.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image016.jpg' | relative_url }}) ![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image017.jpg' | relative_url }})

Flownet pattern generation

  1. 4\. At this time, advanced options are available such as saving either the beginning or end pattern (See Fig. 26.6.12.3.). This is useful if a flownet from a different database is to be output to. Click ![]({{ '/assets/icons/post_icons/mo_generate_button.jpg' | relative_url }}) when finished and the flownet will be calculated. (See Fig. 26.6.12.16.). 

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image018.jpg' | relative_url }})

Example of grid flownet 3D Grid Pattern

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image019.jpg' | relative_url }})

Example of grid flownet Generation of vertical Grid

  * **Polygon pattern [3D]**

The generation of polygon grid pattern is as shown below. First the grid region has to be defined as shown in Fig. 26.6.12.18 and then the grid definition has to be defined as shown in Fig. 26.6.12.19 and finally the polygon grid will be generated as shown in Fig. 26.6.12.20\. 

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image020.jpg' | relative_url }}) ![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image021.jpg' | relative_url }})

Polygon region definition

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image022.jpg' | relative_url }})

Polygon grid definition

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image023.jpg' | relative_url }})

Example of 3D polygon flownet

**Concentric circles** : An example showing the generation of concentric circles flownet is shown in Fig. 26.6.12.21.

**No. of circles** : user can define the no. of circles in this field.

**Maximum radius** : user can define the maximum radius of circle.

**Center position** : user can pick or enter one point to define center position.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image024.jpg' | relative_url }})

Generation of concentric circle flownet pattern

  * **2D Offset [3D]**

The generation of 2D offset pattern is as shown below. First the region has to be defined as shown in Fig. 26.6.12.22. and then the boundary definition has to be defined as shown in Fig. 26.6.12.23. and finally the boundary will be generated as shown in Fig. 26.6.12.24.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image025.jpg' | relative_url }}) ![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image026.jpg' | relative_url }})

Region definition of 2D Offset for 3D problem

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image027.jpg' | relative_url }})

Boundary definition of 2D Offset for 3D problem

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image028.jpg' | relative_url }})

2D offset boundary pattern for 3D problem

  * **Offset [3D]**

The offset will draw an identical surface at a specified distance within the objects border. The border offset pattern is typically used to capture tendencies toward lap formations. If a border offset is selected you must specify the distance the border is offset. The offset curve is controlled through offset distance. The offset distance is a positive value specifying how far inside the region the identical border should be positioned. A rough value of one fourth of the lap distance can be used to define the offset distance. The generation of offset pattern is as shown below.

First the region has to be defined as shown in Fig. 26.6.12.25. and then the boundary definition has to be defined as shown in Fig. 26.6.12.26. and finally the boundary will be generated as shown in Fig. 26.6.12.27.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image029.jpg' | relative_url }}) ![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image030.jpg' | relative_url }})

Offset boundary region definition

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image031.jpg' | relative_url }})

Offset boundary definition

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image032.jpg' | relative_url }})

Example showing Offset boundary Pattern

  * **Surface grid pattern [3D]**

In this option the surface net has been divided in to two options one is parallel and circular. Surface net mode selection is as shown in Fig. 26.6.12.28. The grid definition pattern for parallel and circular is as shown below in Fig. 26.6.12.29., Fig. 26.6.12.30. and Fig. 26.6.12.31. for the linear and circular grid pattern examples.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image033.jpg' | relative_url }})

Surface net mode selection window

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image036.jpg' | relative_url }}) ![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image038.jpg' | relative_url }})

Grid definition for parallel and Circular net

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image037.jpg' | relative_url }})

Examples of parallel grid pattern for Surface net

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image039.jpg' | relative_url }})

Examples of Surface net circular grid pattern

  * ******User Defined Fl****ownet [2D, 3D]**

If you wish to create your own initial pattern or use a previously generated pattern, you may do so by reading in a flow pattern file. A pattern file consists of a list of point coordinates and a list of connectivity sets. The points are points of intersection within the flownet. The type of grid is determined by the connectivity list. This list determines each curve separately as the number of points in a sequential pattern. If the starting and ending point indices are the same, the curve is closed. 

The user defined pattern must be read by a pattern file. The pattern generated can be saved to this file by setting the save option to yes. If the pattern is being saved, the file name must be specified in the pattern File text box.

The material point data format is: 

Numpt

1 X(1) Y(1)

. . .

. . .

Numpt X(Numpt) Y(Numpt)

NumCv

1 CvSz(1) pt(1) pt(CvSz(1))

. . . .

. . . .

NumCv CvSz(NumCv) pt(NumCv) pt(CvSz(NumCv))

Where

**Numpt** : Number of material points 

**Y(i)** : Y coordinate of ith material point

**NumCv** : Number of curve

**CvSz(i)** : Number of points in ith curve

**pt** : Point index of curve (refers to indices in first list)

**Example Case**  
Taking a round billet from the SPIKE.KEY file in the DATA directory and placing a 3x3 rectangular grid on it, will yield an initial flownet that resembles Fig. 26.6.12.32. This flownet is stored as the file seen in Fig. 26.6.12.33. As seen in Fig. 26.6.12.32., the grid points are first stored and the connectivity is stored in the 2nd section. The grid points are seen in as labeled in Fig. 26.6.12.32. and the connectivity curves are labeled as Fig. 26.6.12.33.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image040.jpg' | relative_url }})

The result of placing a 3x3 flownet on a round object; (a) The points are labelled (b) The curves are labelled

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image041.jpg' | relative_url }})

Sample pattern file corresponding to example case. Compare the point connectivity to the figure above

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image042.jpg' | relative_url }})

Merging of different flownet patterns

User can also generate combined (or complicated) patterns like circular-grid, circular-cube and so on. This type of combined grid patterns can be obtained by using Flownet![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})User defined options and is as show as in Fig. 26.6.12.35., Fig. 26.6.12.36. and Fig. 26.6.12.37.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image043.jpg' | relative_url }})

Showing how to generate combined grid pattern

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image044.jpg' | relative_url }})

Shows the complicated flownet pattern

The circular grid pattern on the top of the work piece is created by using Flownet ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})Polygon option and the generated circular grid is as shown below in the Fig. 26.6.12.37.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image045.jpg' | relative_url }})

Circular grid pattern on the top of work piece

**Flowline tracking** :

Flowlines tracking is developed to show metal flow in ALE simulations in Flownet window (See Fig. 26.6.12.38.). This option is applicable for 2D ALE study, 3D ALE Shape Rolling and 3D ALE Extrusion simulations.

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image046.jpg' | relative_url }})

Flownet Tracking window

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image047.jpg' | relative_url }})

Flownet Tracking options

Select Boundary Points: In case of 2D object, Sampling points can be manually picked along workpiece object boundary (see Fig. 26.6.12.40.) or user can use start and end points of the edge on boundary using Define sampling point option (See Fig. 26.6.12.41.).

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image048.jpg' | relative_url }})

Manually picked points for Flowline tracking for 2D

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image049.jpg' | relative_url }})

Selecting points using Start and End point in Point selection window for 2D

In case of 3D object, Sampling points can be manually picked from workpiece object or Sampling points can be defined as rectangular grid with different shapes such as circles, polygons or points on beginning surface using Define sampling point option (See Fig. 26.6.12.42.).

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_12_flownet_tracking/image050.jpg' | relative_url }})

Selecting points on 3D object with different selection options

**Selected point Table** : In Table we can observe the selected points for Flowline Tracking.

**Display type Control** : using this option we can control the thickness of Flowline. Line thickness can be varied by dragging the pointer on the Sliding bar between 1 and 100.

**Animation Control** : We can play the animation of material flow using Animate option and also we can control the animation speed by dragging pointer on Animation Speed sliding bar from slow to fast.

**Auto Update** : Auto update checkbox when turned on flow lines are generated for each selected step automatically. If Auto update is turned off then for each selected step user should use Generate Flowline button to generate flowlines.

**State Variable graph type:** Under State Variable user has options whether to use time or Distance (Start to End surface) as X axis while plotting State variable graph.

**Generate Flowline** : After defining the required options to generate flowline user can click on this button to generate flowlines.

**Save the points to a file** ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}) : We can save the defined points for Flowline tracking using this option for future reference.

**Load Points From a file** ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}): The points defined can be loaded from a file using this option.

**Deleted selected point** : Using this option user can delete unwanted points from the table by selecting respective row in the table.

**Delete all Points** ![]({{ '/assets/icons/pre_icons/mo_clear_icon.jpg' | relative_url }}): Using this option user can delete all the points from the table at once.

**Show/Hide Points** : Using this option we can Show/Hide of Point and Point number in display using " P " and " T " button respectively.

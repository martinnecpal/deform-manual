---
lang: en
title: "12.2. 2D Geometry Data Editing"
---

# 12.2. 2D Geometry Data Editing

12.2.1. 2D Geometry Edit Tools

12.2.2. Display or View Modification options

12.2.3. 2D Geometry Editor Property options

12.2.4. Importing Multiple Boundary Geometries

12.2.5. Defining and Editing Multiple Boundary Geometries

The 2D Geometry editor is used to create geometry for an object or to edit the existing geometry. Imported geometry can be modified in Edit Geometry window. This option can be accessed from Geometry page clicking on ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}) label as shown in Fig. 12.2.1.

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_2_2d_geometry_editing/12_2_image001.jpg' | relative_url }})

2D Geometry Editor option

Observe the options available to create and modify the geometry as shown in below Fig. 12.2.2.

  
![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_2_2d_geometry_editing/12_2_image002.jpg' | relative_url }})

Edit Geometry Window

## 2D Geometry Edit Tools

Various options available for editing 2D geometry are explained below,

**Select**![]({{ '/assets/icons/pre_icons/mo_click_select.jpg' | relative_url }}) :**** Select Tool is used to select the vertex or Edge of the geometry. Using this vertex or edge can be positioned by drag and drop.

**Area select** ![]({{ '/assets/icons/pre_icons/mo_area%20select.jpg' | relative_url }}) : Area Select tool is used to select the geometry more than one entity within a box.

**Create Loop** ![]({{ '/assets/icons/pre_icons/mo_create_loop.jpg' | relative_url }}) : Create Loop tool is used to create the geometry loop by creating points and connecting them. Simple geometry as shown in Fig is created by using create loop in 7 steps as shown in Fig. 12.2. 3.

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_2_2d_geometry_editing/12_2_image003.jpg' | relative_url }})

Simple closed loop with geometry coordinates table

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_2_2d_geometry_editing/12_2_image004.jpg' | relative_url }})

Steps to create the simple geometry using create loop tool

If user not able to figure it out the vertex coordinate with the help of grid lines or grid points (See Fig. 12.2.4.) then geometry points coordinates can be directly entered or changed from the geometry table at right bottom side in geometry tab (See Fig. 12.2.4.). Grid lines can be adjusted to the required dimension by entering the distance between greed lines/points in the field next to grid lines selection.

**Add Point to Loop** ![]({{ '/assets/icons/pre_icons/mo_add_points_to_loop.jpg' | relative_url }}) : Add Point Loop tool is used to add the new points to an existing loop. After adding check and ensure the added points coordinates in geometry tab. If the points coordinates are not accurate then user has to correct by double clicking on respective cell in geometry tab. Typical example of adding points before introducing the fillet is as shown in Fig. 12.2.5.

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_2_2d_geometry_editing/12_2_image005.jpg' | relative_url }})

Adding points to an existing loop

**Delete Point** ![]({{ '/assets/icons/pre_icons/mo_delete%20point.jpg' | relative_url }}) : Delete Point tool is used to delete the point in the loop. For simple example as shown in the Fig. 12.2.6.

  
![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_2_2d_geometry_editing/12_2_image006.jpg' | relative_url }})

Deleting the point from the loop

**Round corner**![]({{ '/assets/icons/pre_icons/mo_round_corner.jpg' | relative_url }}) : Round Corner tool is used to create fillet at selected point. When user selects the corner system shows a field to enter the radius as shown in Fig. 12.2.7.

  
![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_2_2d_geometry_editing/12_2_image007.jpg' | relative_url }})

Round corner creation for the geometry

**Set Angle** ![]({{ '/assets/icons/pre_icons/mo_set_angle.jpg' | relative_url }}) : Set Angle tool is used to change the angle of edge. When user select the edge (Step-1) system display the edge current angle, by clicking on the displaying angle for the Edge will display the Angle field in blue color on display window (Step-2) then change the current angle (Step-3) and press ENTER button to apply as shown in Fig. 12.2.8.

  
![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_2_2d_geometry_editing/12_2_image008.jpg' | relative_url }})

Example to Set angle for an edge

**Move**![]({{ '/assets/icons/pre_icons/mo_move.jpg' | relative_url }}) : Move tool is used to re position the point by dragging it to other location. To move any edge or area first user need to select the edge/area (Step-1), then by selecting Move tool clicking on selected edge/area will display the X,Y coordinates field in blue color on display window (Step-2). The required moving distance along X and Y direction to be entered (Step-3) and press ENTER keyboard button to apply as shown in Fig. 12.2.9.

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_2_2d_geometry_editing/12_2_image009.jpg' | relative_url }})

Example to move edge or area

**Move to centerline** ![]({{ '/assets/icons/pre_icons/mo_move_to_centerline.jpg' | relative_url }}) : Using this tool user can move the loop's nearest and equidistant points to center line as shown in Fig. 12.2.10. User simply needs to select the Move to centerline tool as shown in Fig. 12.2.10.

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_2_2d_geometry_editing/12_2_image010.jpg' | relative_url }})

Example to Move the loop to centerline

**Offset** ![]({{ '/assets/icons/pre_icons/mo_offset.jpg' | relative_url }}) : Offset tool is used to resize the geometry loop. User can decrease or increase the size by entering positive or negative offset distance respectively as shown in Fig. 12.2.11.

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_2_2d_geometry_editing/12_2_image011.jpg' | relative_url }})

Example to offset the loop

**Make First point** ![]({{ '/assets/icons/pre_icons/mo_make_first_point.jpg' | relative_url }}) : Make First Point tool is used to make the selected point as first point in a loop, this will be used for closed loop, we cannot select an arc mid point as first point as shown in Fig. 12.2.12.

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_2_2d_geometry_editing/12_2_image012.jpg' | relative_url }})

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_2_2d_geometry_editing/12_2_image013.jpg' | relative_url }})

Example to show make first point

**Reverse direction** ![]({{ '/assets/icons/pre_icons/mo_reverse_direction.jpg' | relative_url }}) : Reverse direction is used to reverse the direction of loop to change the orientation of the geometry. The geometry should be created in Counter clockwise, if the geometry is created in clockwise, using this option we can change the direction of loop (see Fig. 12.2.13.).

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_2_2d_geometry_editing/12_2_image015.jpg' | relative_url }})

Example to show Reverse Direction

**Close loop**![]({{ '/assets/icons/pre_icons/mo_close_loop.jpg' | relative_url }}) : Closed loop tool is used to close the open loop as shown in Fig. 12.2.14.

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_2_2d_geometry_editing/12_2_image014.jpg' | relative_url }})

Example to show close loop

**Split loop**![]({{ '/assets/icons/pre_icons/mo_split_loop.jpg' | relative_url }}) : Split loop tool is used to split the loop at selected point (see Fig. 12.2.15.).

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_2_2d_geometry_editing/12_2_image016.jpg' | relative_url }})

Example to show slip loop

**Sub loop**![]({{ '/assets/icons/pre_icons/mo_sub_loop.jpg' | relative_url }}) : Sub loop tool is used to select a inner loop as sub loop in case of multi loops topology, by selecting this we can assign the material for a multiple loop geometry (See Fig. 12.2.16.).

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_2_2d_geometry_editing/12_2_image017.jpg' | relative_url }})

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_2_2d_geometry_editing/12_2_image018.jpg' | relative_url }})

Example to show sub loop

**Join loops** ![]({{ '/assets/icons/pre_icons/mo_join_loop.jpg' | relative_url }}) : join loops option is used to merge the 2 loops by selecting the loops to be joined, the end point of first loop will be joined to first point of the second loop (see Fig. 12.2.17.).

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_2_2d_geometry_editing/12_2_image019.jpg' | relative_url }})

Example to show join loops

**Join all loops** ![]({{ '/assets/icons/pre_icons/mo_join_all_loops.jpg' | relative_url }}) : Join all loops tool is used to merge all loops. Example for Join all loops is as shown in Fig. 12.2.18.

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_2_2d_geometry_editing/12_2_image020.jpg' | relative_url }})

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_2_2d_geometry_editing/12_2_image021.jpg' | relative_url }})

Example to show join all loops

**Delete selected** ![]({{ '/assets/icons/pre_icons/mo_delete_selected.jpg' | relative_url }}) : Delete selected is used to delete the selected loops or edges.

**Delete unselected** ![]({{ '/assets/icons/pre_icons/mo_delete_unselected.jpg' | relative_url }}) : Delete unselected is used to delete the unselected loops edges.

## Display or View Modification options

**Show Vertex** ![]({{ '/assets/icons/pre_icons/mo_show_vertex.jpg' | relative_url }}) : is used to display the vertexes of the geometry.

**Show Vertex numbers** ![]({{ '/assets/icons/pre_icons/mo_show_vertex_numbers_icon.jpg' | relative_url }}) : is used to display the vertexes number of the geometry.

**Show Inside**![]({{ '/assets/icons/pre_icons/mo_show_inside.jpg' | relative_url }}) : is used to show the orientation of the geometry.

**Show Edge direction** ![]({{ '/assets/icons/pre_icons/mo_show_edge_direction.jpg' | relative_url }}) : is used to plot the direction of loop created.

**Show Material** ![]({{ '/assets/icons/pre_icons/mo_material_icon.jpg' | relative_url }}) : is used to load and assign the material to the geometry region.

**Grid Lines** : It shows the Grid Lines in Horizontal and Vertical direction in Display window. (See Fig. 12.2.19.)

**Grid Points** : It shows the Grid Points in Horizontal and Vertical direction in Display window.(See Fig. 12.2.19.)

**Grid None** : When this option is selected, the Grid points and Grid Lines in Horizontal and Vertical direction are not displayed in Display window. (See Fig. 12.2.19.)

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_2_2d_geometry_editing/12_2_image022.jpg' | relative_url }})

Grid Definition Window

**Show Axis**![]({{ '/assets/icons/pre_icons/mo_show_axis.jpg' | relative_url }}) : Shows the Axis in the Display window

**Show Centerline**![]({{ '/assets/icons/pre_icons/mo_show_centreline.jpg' | relative_url }}) :Shows the centerline in the Display window

**Fit All** ![]({{ '/assets/icons/pre_icons/mo_fit_all_icon.jpg' | relative_url }}) : Fits all displayed entities into the current viewport.

**Box Zoom** ![]({{ '/assets/icons/pre_icons/mo_box_zoom_icon.jpg' | relative_url }}) : The zoom window function allows close up inspection of a small region of the currently defined entities. The zoom region is selected by holding Ctrl + Alt key and clicking the left mouse button, while dragging the mouse to enclose the selected region with the displayed box. When the mouse button is released the selected region will fill the display window.

**Zoom** ![]({{ '/assets/icons/pre_icons/mo_zoom_icon.jpg' | relative_url }}) : The zoom dynamically changes the size of the region of the object which fills the active view port. The view size can be changed by holding Alt key and clicking left mouse button in the active view port and rolling the mouse backward or forward to increase or decrease the size of the object in the display window.

**Paning**![]({{ '/assets/icons/pre_icons/mo_pan_icon.jpg' | relative_url }}) : Pan adjusts the region filling the active viewport without changing the size of the displayed object.

**Save**![]({{ '/assets/icons/pre_icons/mo_save_icon.jpg' | relative_url }}) :Saves the problem setup in .key file format. This can also be accessed from File Tools menu.

## 2D Geometry Editor Property options

**Geometry tab :** Under Geometry tab, we can enter or modify the geometry entities. Geometry entities can be entered in two methods, in Line-Arc method and XYR methods.

**XYR Method** : The **XYR** format ([DIEGEO]({{ '/docs/en/keyword_documentation/d/diegeo/' | relative_url }})) consists of defining an X coordinate, a Y coordinate and a radius for every point of the geometry defining an object. An arc with the specified radius is drawn connecting the lines that would have intersected at the point defined by the X and Y coordinate. (See Fig. 12.2.20.)

  
The XYR Table appears directly in the Geometry window. This table allows specifying and/or editing an object's geometry through a number of points in the XYR format. X and Y are the x- and y-coordinates of the point and R is the radius of the point (if it is to define a curved line).

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_2_2d_geometry_editing/12_2_image023.jpg' | relative_url }})

2D Geometry Editor with XYR Geo type

**Line-Arc Method :** Line-Arc format ([DIEGEO]({{ '/docs/en/keyword_documentation/d/diegeo/' | relative_url }})) is similar to XYR format in that it can define arcs, but it is more entity oriented. The XYR format defines the connecting points and the connection type, but the Line-Arc format defines the lines and arcs that make up the object, not the connections. The primary reason that the Line-Arc format is used is because IGES files are formatted in the Line-Arc scheme. (See Fig. 12.2.21.)

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_2_2d_geometry_editing/12_2_image024.jpg' | relative_url }})

2D Geometry Editor with Line-Arc Geo type

**Add Loop** ![]({{ '/assets/icons/pre_icons/mo_add_loop_button.jpg' | relative_url }}) : By clicking on this button adds the new loop, this option is required to define topology for multi-boundary objects.(See Fig. 12.2.22.)

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_2_2d_geometry_editing/12_2_image025.jpg' | relative_url }})

Example to show Add loop

**Delete Loop** ![]({{ '/assets/icons/pre_icons/mo_delete_loop_button.jpg' | relative_url }}) : By clicking on this button it deletes the existing loop (see Fig. 12.2.23.).

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_2_2d_geometry_editing/12_2_image026.jpg' | relative_url }})

Example to show Delete Loop

**Add Vertex**![]({{ '/assets/icons/pre_icons/mo_add_vertex_button.jpg' | relative_url }}) : By clicking on this button adds the new vertex to the loop.(See Fig. 12.2.24.)

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_2_2d_geometry_editing/12_2_image027.jpg' | relative_url }})

Example to show Add vertex to loop

**Delete Vertex** ![]({{ '/assets/icons/pre_icons/mo_delete_vertex_button.jpg' | relative_url }}): By clicking on this button it deletes the existing vertex in the loop. (See Fig. 12.2.25.)

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_2_2d_geometry_editing/12_2_image028.jpg' | relative_url }})

Example to show delete vertex in a loop

**Assign to![]({{ '/assets/icons/pre_icons/mo_assign_to_pull_down_button.jpg' | relative_url }}) :**

When multiple boundary geometries (Multiple loops) are available, user can assign each loop geometry to other Objects as shown in Fig. 12.2.26.

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_2_2d_geometry_editing/12_2_image029.jpg' | relative_url }})

Example to show Assign To option

**Objects Tab** : Under Objects tab, we can select the object in list to hide the selected object geometry in graphical display window, when they are more than one objects geometries are displayed. (See Fig. 12.2.27.) 

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_2_2d_geometry_editing/12_2_image030.jpg' | relative_url }})

2D Geometry Editor objects window

**Loops Tab** : Under Loops tab, we can load and assign the material for the selected loops. Also we can see the display of assigned material to the corresponding loop details.(See Fig. 12.2.28.)

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_2_2d_geometry_editing/12_2_image031.jpg' | relative_url }})

2D Geometry Editor materials window

## Importing Multiple Boundary Geometries

In MO, user can import multiple boundary geometries as shown in Fig. 12.2.29.

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_2_2d_geometry_editing/12_2_image032.jpg' | relative_url }})

Example to show multiple boundary geometries

## Defining and Editing Multiple Boundary Geometries

User can create multiple boundary geometries. Fig. 12.2.30. shows the multiple boundary geometries defining and editing the defined geometry.

![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_2_2d_geometry_editing/12_2_image033.jpg' | relative_url }})![]({{ '/assets/images/pre-processor/12_geometry_modelling/12_2_2d_geometry_editing/12_2_image034.jpg' | relative_url }})

Example to show editing and defining multiple boundary geometries

[12\. Geometry Modelling]({{ '/docs/en/pre_processor/12_geometry_modelling/12_geometry_modelling/' | relative_url }})

[12.1. 2D Geometry Data Defining]({{ '/docs/en/pre_processor/12_geometry_modelling/12_1_2d_geometry_data_defining/' | relative_url }})

[12.3. 3D Geometry Data Defining]({{ '/docs/en/pre_processor/12_geometry_modelling/12_3_3d_geometry_data_defining/' | relative_url }})

[12.4. 3D Geometry Editing (GEO TOOL)]({{ '/docs/en/pre_processor/12_geometry_modelling/12_4_3d_geometry_data_Editing_geo_toolL/' | relative_url }})

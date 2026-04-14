---
lang: sk
title: "50.1. 3D Geo Tool"
---

# 50.1.3D Geometry Tool

50.1.1. Geometry Tool Layout

50.1.2. Display window

50.1.3. Object tree

50.1.3.1. Number of Objects

50.1.3.2. Visibility

50.1.3.3. Object color

50.1.3.4. Transparency

50.1.4. Graphical Utilities

50.1.4.1. File Menu

50.1.4.2. Edit Menu

50.1.4.3. Tool Menu

50.1.4.4. Select Menu

50.1.4.5. Display Menu

50.1.4.6. Viewport

50.1.4.7. Window menu

50.1.4.8. Options menu

50.1.4.9. Help menu

50.1.5. Property editor

50.1.5.1. Analysis

50.1.5.2. Measure

50.1.5.3. Slicing

50.1.5.4. Modify

50.1.5.5. Verify

50.1.5.6. Morphing

## Geometry Tool Layout

Geometry tool layout is divided into Display window, Object tree, Graphical Utilities window and Project editor. (See Fig. 50.1.1.).

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0001.jpg' | relative_url }})

3D Geo tool Layout

## Display window

The display window is the graphical display for all imported or created geometries. In Display window, we can see the Geometry as the changes made takes effect.

## Object tree

In object tree we can see the objects imported or created and their viewing information, such as number of objects, Displaying, color of the objects and Transparency information is available in this window.

### Number of Objects

Number of objects (geometry) imported or created can be seen in the object tree as they will be listed out in the Object tree.

###  Visibility

By clicking on the ![]({{ '/assets/icons/pre_icons/mo_visible.jpg' | relative_url }}) icon, user can toggle the visibility of the objects in the display window.

### Object color

User can change the object color by using this option. If user clicks on the box under the object color option for the selected object, a color palette dialog will open and user can select the color to be used for selected object.

### Transparency

User can use this option to toggle the transparency display of the selected object. If user clicks on this option, respective object gets transparent.

## Graphical Utilities

The graphical utilities window provides view manipulation and other utility functions to control the display of the objects in Display window. Features include zoom and pan, Rotate. The graphics utilities window also contains tool bar options for creating geometry and modifying like Geometry Primitive, Translate, Rotate, scale, mirror, Offset, Extrude, Soft move and Boolean and selection options like Pick Shell, Pick Face, Pick Polygon, Pick polygons by box, Pick polygons by cylinder, Pick polygons by window, Pick Polygons by line, Pick Loop, Pick Curve, Pick Slicing Plane, Pick Point and Invent selection.

### File Menu

The below Fig. 50.1.2. Shows the File menu options,

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0002.jpg' | relative_url }})

File Menu options

  * **New Session![]({{ '/assets/icons/pre_icons/geo_tool_new_session.jpg' | relative_url }})** : It opens the new session for creating and modifying geometries in 3D geometry tool.

  * **Open![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) **: It opens 3D geometry of different formats like *.STL, *.GEO, *.PDA, *.UNV, *KEY and *.PBR .

  * **Save![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}) **: It saves the geometry in the current session into *.STl file.

  * **Save as** : Save as saves geometry in the current session into selected format from the available formats in the selected path.

  * **Save All :** Save all option is used save all geometries in one click.

  * **Import :** Using this option user can import the geometries having the formats *.IGS and *.STP .

  * **Export** : Export the geometry in the current session into *.IGS or *.STP .

  * **Close Session** : Close session option is used to close the currently opened session but does not quit the 3D Geo Tool.

  * **Exit** : Exit option is used to close the 3D Geo Tool wizard.

### Edit Menu

  * **Undo** : This option is used to undo the last action.

  * **Redo :** This option is used to redo the action that is deleted using undo.

### Tool Menu

  * **Geometry Primitive![]({{ '/assets/icons/pre_icons/geo_tool_geometry_primitive.jpg' | relative_url }}) : **When we click on the Geometry primitive option, Primitive window will open with options to create a new geometry. (See Fig. 50.1.3.) For more information about the Geometry Primitive options please visit the section [12.3.2. 3D Geometry Tool](../../pre_processor/12_geometry_modelling/12_3_3d_geometry_data_defining.htm#12.3.2._3D_Geometry_Tools) \- [Define Primitive.](../../pre_processor/12_geometry_modelling/12_3_3d_geometry_data_defining.htm#Define_Primitive)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0003.jpg' | relative_url }})

Geometry Primitive window

  * **Translate object![]({{ '/assets/icons/pre_icons/geo_tool_translate_icon.jpg' | relative_url }}) **: Translate object option is used to move the objects for quantified distance in X, Y and Z direction. When we click on this option by selecting an object, a pop-up window will appear to define the distance value in the respective direction to move the object in that direction. (See Fig. 50.1.4.).

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0004.jpg' | relative_url }})

Translate object Dialog

  * **Rotate object![]({{ '/assets/icons/pre_icons/geo_tool_rotate_icon.jpg' | relative_url }}) :** This option is used to rotate the object in specified direction with specified angle. When we click on this option by selecting an object, a pop-up window will appear to define the direction and Angle. Then if we click on the apply button, objects are rotated in the specified direction. (See Fig. 50.1.5.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0005.jpg' | relative_url }})

Rotate Dialog

  * **Scale object** ![]({{ '/assets/icons/pre_icons/geo_tool_scale_icon.jpg' | relative_url }}) : This option is used to scale the Geometry. Geometry can be scaled in Geo tool by specifying the scaling factor. For 0.5 it scales down to half of original geometry and for 2 it doubles original geometry. (See Fig. 50.1.6.) This scaling can be restricted for specified direction. In Scaling dialog, user can uncheck the direction in which scaling is not required.

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0006.jpg' | relative_url }})

Scale Objects dialog

  * **Mirror Object![]({{ '/assets/icons/pre_icons/geo_tool_mirror_icon.jpg' | relative_url }}) : **This option will mirror the objects along the specified axis and won't retain the original objects. (See Fig. 50.1.7.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0007.jpg' | relative_url }})

Mirror Objects dialog

  * **Offset![]({{ '/assets/icons/pre_icons/geo_tool_offset_icon.jpg' | relative_url }}) :** This Option is used to Offset a surface to a specified length. Offsetting the surface can be done using following steps,

  * Select Offset option (Offset dialog will open),

  * Enter offset length or target volume.

  * Turn on Keep original part if the modified geometry should be created as new part, original part geometry is left untouched.

  * Select a surface to be offset by clicking on it (surface will get highlighted)

  * Click on ![]({{ '/assets/icons/pre_icons/apply_button.jpg' | relative_url }}). Surface that we selected is offset to defined length or to target volume. (See Fig. 50.1.8.).

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0008.jpg' | relative_url }})

Offsetting the surface

  * **Extrude![]({{ '/assets/icons/pre_icons/geo_tool_extrude_icon.jpg' | relative_url }}) : **This Option is used to extrude the surface to defined length. Extruding the surface can be done using following steps,

  * Select Extrude option (Extrude dialog will open),

  * Enter extrude length or target volume.

  * Turn on Keep original part if the modified geometry should be created as new part, original part geometry is left untouched.

  * Select a surface to be extruded by clicking on the surface (surface will get highlighted)

  * Define direction or select auto so that system automatically identifies the direction based on the selected surface.

  * Click on ![]({{ '/assets/icons/pre_icons/apply_button.jpg' | relative_url }}).Surface that we selected will Extrude to defined length or to target volume. (See Fig. 50.1.9.).

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0009.jpg' | relative_url }})

Extruding the Surface

  * **Soft move** ![]({{ '/assets/icons/pre_icons/geo_tool_soft_move_icon.jpg' | relative_url }}): This option is used to modify the surface profile. Soft moving the surface can be done using following steps,

  * Select Soft move option (Soft move dialog will open),

  * Select a surface whose profile has to be modified by clicking on the surface (Cylinder will get added, modify the cylinder to select the surface)

  * Select the method of modifying the profile, Around the point or Along the curve

  * Pull the arrow on the cylinder window to define the Profile shape. (See Fig. 50.1.10.)

  * Profile curve shape can be defined using the sliding bar.

  * Click on ![]({{ '/assets/icons/pre_icons/apply_button.jpg' | relative_url }}) and ![]({{ '/assets/icons/pre_icons/ok_button.jpg' | relative_url }}). Surface that we selected will Soft move to defined length. (See Fig. 50.1.11.).

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0010.jpg' | relative_url }})

Creating profile shape for soft move

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0011.jpg' | relative_url }})

Soft moving the surface

  * **Boolean wizard** ![]({{ '/assets/icons/pre_icons/geo_tool_boolean_icon.jpg' | relative_url }}): Boolean wizard guides the user regarding the options need to be used while performing Boolean operations like subtracting the unwanted region in the geometry using another geometry or joining the two geometries. It can be used to create ALE workpiece.

**Step 1 : Start**

Start page is the beginning page to perform the Boolean operations. (See Fig. 50.1.12.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0012.jpg' | relative_url }})

Boolean Wizard Start Page

**Step 2 : Modify objects**

In Modify objects page, we can position the objects using offset positioning to avoid the Overwrap surface. (See Fig. 50.1.13.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0013.jpg' | relative_url }})

Boolean Wizard Modify Page

**Step 3 : Boolean Union**

After modifying the objects user can combine two geometries in to one by selecting the Union option in the modify tab. (See Fig. 50.1.14.). Also  refer 50.1.5.2.

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0014.jpg' | relative_url }})

Boolean Wizard Union page

**Step 4 : Geometry creation**

In geometry Creation page user can create new cylinder geometry by defining the values for Diameter, Height and Position fields. (See Fig. 50.1.15.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0015.jpg' | relative_url }})

Boolean wizard Geometry Creation page

**Step 5 : Boolean Subtract**

In slice page, user can slice the previously Cleaned geometry at required location in desired direction. This slicing creates new geometry from the sliced object, user has an option to retain original geometry (See Fig. 50.1.16.). Also refer Boolean in 50.1.5.2. Measure

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0016.jpg' | relative_url }})

Boolean Wizard Subtract Page

**Step 6 : Clean up**

In clean up page, user can fix the previously combined or subtracted geometry by deleting the illegal shells/polygons and this can be done by using the Analysis tab options. (See Fig. 50.1.17.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0017.jpg' | relative_url }})

Boolean Wizard Clean up page

**Step 7 : Slice**

In slice page, user can slice the previously Cleaned geometry in to required shape and distance with defined direction. This slicing divides the complete geometry in to two separate geometries. (See Fig. 50.1.18.) Also for more information on slicing, please refer 50.1.5.3. Slicing

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0018.jpg' | relative_url }})

Boolean Wizard Slice page

**Step 8 : Extrude**

In extrude page, user can extrude the required surface to defined length and direction. This extends the surface to the defined length. (See Fig. 50.1.19.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0019.jpg' | relative_url }})

Boolean Wizard Extrude page

**Step 9 : Finish**

After getting the Final geometry shape, user can save the geometry by clicking Finish button in the Finish page. (See Fig. 50.1.20.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0020.jpg' | relative_url }})

Boolean Wizard Finish page

### Select Menu

  * **Pick Shell**![]({{ '/assets/icons/pre_icons/geo_tool_pick_shell.jpg' | relative_url }}) : This option is used to select the complete shell of the geometry for editing.

  * **Pick Face**![]({{ '/assets/icons/pre_icons/geo_tool_pick_face.jpg' | relative_url }}) : This option is used to select a geometry face for editing.

  * **Pick Polygon** ![]({{ '/assets/icons/pre_icons/geo_tool_pick_polygon.jpg' | relative_url }}): This option is used to select a polygon for editing.

  * **Pick polygons by box**![]({{ '/assets/icons/pre_icons/geo_tool_pick_polygons_by_box.jpg' | relative_url }}) : This option is used to select the polygons by using box window. Modifying the box length and width picks the polygons which are completely in the box for editing.

  * **Pick polygons by cylinder![]({{ '/assets/icons/pre_icons/geo_tool_pick_polygos_by_cylinder.jpg' | relative_url }}) : **This option is used to select the polygons by using cylinder window. Modifying the cylinder diameter and height picks the polygons which are completely in the cylinder for editing.

  * **Pick polygons by window**![]({{ '/assets/icons/pre_icons/geo_tool_pick_polygons_by_window.jpg' | relative_url }}) : This option is used to select the polygons by using window which is drawn across the polygons.

  * **Pick Polygons by line** ![]({{ '/assets/icons/pre_icons/geo_tool_pick_polygons_by_line.jpg' | relative_url }}): Using this option user can draw a line across the polygons that are to be picked for editing.

  * **Pick Loop** ![]({{ '/assets/icons/pre_icons/geo_tool_pick_loop.jpg' | relative_url }}): Using this option is user can select the open loop to fill.

  * **Pick Curve** ![]({{ '/assets/icons/pre_icons/geo_tool_pick_curve_by_line.jpg' | relative_url }}): This option is used to select the curves in the geometry.

  * **Pick Slicing Plane** ![]({{ '/assets/icons/pre_icons/geo_tool_pick_slicing_curve.jpg' | relative_url }}): This option is used to select the defined slicing plane.

  * **Pick Point** ![]({{ '/assets/icons/pre_icons/geo_tool_pick_point.jpg' | relative_url }}): Pick Point option is used to select points on the geometry.

  * **Invert selection** ![]({{ '/assets/icons/pre_icons/geo_tool_invert_selection.jpg' | relative_url }}): This option is used to toggle the selection between selected and unselected regions of the geometry.

### Display Menu

Display has options for varying the display mode of the geometry. See Fig. 50.1.21.

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0021.jpg' | relative_url }})

Display Menu options

  * **Display Points![]({{ '/assets/icons/pre_icons/geo_tool_display_points.jpg' | relative_url }})** : Shows geometry points on the Display window.

  * **Display Shading** ![]({{ '/assets/icons/pre_icons/mo_shading_mode_icon.jpg' | relative_url }}): Smoothly shades the geometry within viewport.

  * **Display Wireframe** ![]({{ '/assets/icons/pre_icons/mo_wirefrane_mode_icon.jpg' | relative_url }}): Displays Polygons lines of the geometry within viewport.

  * **Display Shading and Wireframe** ![]({{ '/assets/icons/pre_icons/mo_shade_wireframe_icon.jpg' | relative_url }}): Smoothly shades and displays Geometry along with the polygons lines within the viewport.

  * **Display edges** ![]({{ '/assets/icons/pre_icons/geo_tool_display_edge_icon.jpg' | relative_url }}): Displays the surface edges of the geometry.

  * **+Edges**![]({{ '/assets/icons/pre_icons/geo_tool_plus_surface patch_icon.jpg' | relative_url }}) : This feature will display surface edges with other display modes options.

### Viewport

Fig. 50.1.22. Shows the Viewport menu options. Using this option user can place geometry for better visualization.

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0022.jpg' | relative_url }})

Viewport menu

  * **Refresh screen** : The Refresh Screen option redraws the screen, removing any measurement marks.

  * **Fit View** : Fits all displayed geometries inside the current viewport.

  * **Previous view** : Resets objects to previously viewed display position.

  * **Multiple****viewports** : Multiple Viewports can be used by user to visualize geometry from different orientations at a time.

  * **Sync multiple****viewports** : When we select the Sync multiple viewports, it will sync the two windows, if we change the properties in one viewport, it is reflected in other viewports.

  * **Select** : The select button is a general pointing utility. It performs several functions which vary with context. It can be used to report coordinates of an arbitrary point, to select a node or an element, to change the primary viewport, and many similar functions. 

  * **Pan**(Shift+LMB) : Pan adjusts the region filling the active viewport without changing the size of the displayed object.

  * **Dynamic zoom**(Alt+LMB) : The dynamic zoom dynamically changes the size of the region of the object which fills the active view port. The view size can be changed by holding Alt key and clicking left mouse button in the active view port, and rolling the mouse backward or forward to increase or decrease the size of the object in the display window.

  * **Box Zoom Window** (Ctrl+Alt+LMB) : The zoom window function allows close up inspection of a small region of the currently display object or graph. The zoom region is selected by holding Ctrl + Alt key and clicking the left mouse button, while dragging the mouse to enclose the selected region with the displayed box. When the mouse button is released the selected region will fill the display window.

  * **Rotate**(Ctrl+LMB): This will allow the mouse pointer to rotate the geometries in the required direction.

  * **Rotate X** : This will allow the mouse pointer to rotate the object along X-direction.

  * **Rotate Y** : This will allow the mouse pointer to rotate the object along Y-direction.

  * **Rotate Z** : This will allow the mouse pointer to rotate the object along Z-direction. 

### Window menu

  * **Cascade** : If we select Cascade type, each and every time Database opens in new window.

  * **Tile** : Database will fit into the Display window.

  * **Tile Horizontally** : Database will show in Horizontal direction in Display window.

### Options menu

**Environment** : 

The user can adjust the DEFORM working environment using environment option. Here the user can make changes in display and graphical settings. Defined settings will update from next session onwards.

Region: The user can select the preferred language under Language option and set to English or SI units under Unit option as a Default unit system for a new session. (See Fig. 50.1.23.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0023.jpg' | relative_url }})

Environment Region tab

**Directories** : Directories option under Environment Settings window appears as shown in Fig. 50.1.24. User can browse to the required location to set it as working directory, this directory will be used as a default location to store the geometries unless user specifies different location. The temporary files generated while running Geo tool are stored in the specified path under Temporary file location.

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0024.jpg' | relative_url }})

Environment Directories tab

**Feature angle** : User can use this option to change the range of selection when selecting the polygons for editing geometry using surface patch method. It displays the surface patch by treating surfaces within the feature angle as the one surface. A curved surface with smaller feature angle means fewer surface polygons will be picked at a time. The feature tab to change the feature angle is as shown in Fig. 50.1.25.

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0025.jpg' | relative_url }})

Environment Feature Tab

**Icon/Font** : The user can change the icon and font size depending on the requirement as shown in the [Fig. 50.1.26.](50_1_3d_geo_tool.htm#Fig_50_1_26_Icon/Font_options_under_Environment_Settings_window)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0026.jpg' | relative_url }})

Icon/Font options under Environment Settings window

### Help menu

The help menu options are shown in Fig. 50.1.27., these options can be used to open the help manual and view brief information about product.

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0027.jpg' | relative_url }})

Help menu options

**Note** : Help Menu options are not yet functional.

## Property editor

Property editor options (such as Analysis, Measure, Slicing, Modifying, Verifying and Morphing) are the crucial options to Analyze and modify the geometries.

### Analysis

Analysis window shows the details about the geometry imported/created and allows to modifying the geometries using various options.(See Fig. 50.1.28.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0028.jpg' | relative_url }})

Analysis tab options

**Auto Fix** ![]({{ '/assets/icons/pre_icons/geo_tool_auto_fix.jpg' | relative_url }}) : This option automatically fixes the illegal geometry. This option deletes the illegal shells, free loops, free Edges, Noisy shells, free curves, bad edges and makes the geometry water tight geometry.

**Create :** This option is used to create a polygon by selecting the points.

**Delete :** This option deletes the selected part of a geometry or entire geometry selected.

**Flip :** This option flips the surface of the geometry selected.

**Normal :**

  * **Orient Shells Consistently** : This action button will make all the selected geometry polygons continuous by orienting them in one direction. To check this create a primitive cylinder geometry select any polygon > click on Flip > now click on Orient shells consistently, this will make all the polygons which are disoriented to orient consistent with rest of the polygons.(See Fig. 50.1.29.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0029.jpg' | relative_url }})

Example for Orient Shell consistently option

  * **Auto Fix Orientation:** When user uses auto fix orientation option, system corrects polygons orientation towards counterclockwise and orients them consistently towards counter clockwise direction.(see Fig. 50.1.30.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0030.jpg' | relative_url }})

Example for Auto Fix orientation option

**Stitch** : This option is used to fill gaps between polygons that are not connected along the surface. When we click on the Stitch button, existing polygons which are not connected along the surface are edited to connect within the stitching tolerance.(See Fig. 50.1.31.)

  * **Estimate Stitching Tolerance** : When we click on the Estimate Stitching Tolerance, it estimates the tolerance value for stitching the polygons in the geometry.

  * **Auto Stitch** : When this option is used, system automatically estimates the stitching tolerance and connects the polygons of the entire geometry which are within the Stitching tolerance.

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0031.jpg' | relative_url }})

Stitch tab options

**Fill** : The missing surfaces or polygons in the geometry due to which geometry cannot be closed are considered as holes.(See Fig. 50.1.32.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0032.jpg' | relative_url }})

Fill tab Options

  * **Fill Holes** : When we click on the Fill holes, new polygons are created to fill missing surfaces or polygons.

  * **Fill all holes** : When we click on the Fill all holes, all holes in the geometry gets filled with new polygons.

.

  * **Connect two Loops** : This option is used to join two distinct loops. Selecting two loops and clicking on connect two loops option will join the loops.

  * **Auto Fill** : When user uses auto fill option, system automatically identifies the missing surfaces/ polygons in the geometry and fills them with new polygons.

**Shell** : Under Shell tab, information of each shell regarding status, Number of polygons in the shell, Shell Surface Area and volume will be displayed in the table.(See Fig. 50.1.33.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0033.jpg' | relative_url }})

Shell tab Options

  * **Mark Noisy shells** : When user clicks on Mark Noisy Shells button, system will highlight the noisy shells based on the criteria specified in the Noisy Shell Options.

  * **Noisy shell options:** User can use Noisy Shell Options button to specify the criteria to decide whether the shell is a noisy shell or not.

**Triangle** : 

  * **Tool** : Under Tool tab we have a Check button to check the geometry and identify and display the number of polygons with double surface, number of polygons intersecting, number of polygons attached to bad edge and number of polygons duplicated. Under this tab user can specify the criteria like distance, angle and normal direction to identify the double surface polygons.(See Fig. 50.1.34.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0034.jpg' | relative_url }})

Triangle tab options

**Point** : Point tab is used to create new points or duplicate exiting points of 3D geometry.(See Fig. 50.1.35.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0035.jpg' | relative_url }})

Point Tab Options

  * **Tool** : Tool options are used to create new points or duplicate exiting points of 3D geometry.

  * **Property** : Under Property, system displays the point number and co-ordinates of selected point or point to be created.

**Geometry** : Under this tab user can specify the criteria like distance, angle and normal direction to identify the double surface polygons.(See Fig. 50.1.36.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0036.jpg' | relative_url }})

Geometry tab options

  * **Double surface** : Check double surface option is used to check the geometry whether it contains more than one surface based on the specified distance and angle to check the double surface, as DEFORM requires the geometry to have single surface.

  * **Intersecting Triangle** : Check Intersecting Triangle option is used to check the geometry whether it contains any intersecting polygons.

**Advanced** : 

  * **Tool :**

  * **Refine (conformal):** When user clicks on Refine Conformal, system will refine the geometry by reducing the polygon size and thereby increasing the number of polygons.(See Fig. 50.1.37.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0037.jpg' | relative_url }})

Advanced Tab options

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0038.jpg' | relative_url }})

Example for Refining the geometry face

  * **Split (not conformal):**

  * **Fairing** :

  * **Select Contact region** : This is typically used in Lagrangian Extrusion cases. In extrusion where material coming out of different pockets will form self contact, to cleanup these sub-contacted polygons and make the continuous material flow by importing the contact BCC keyword conditions.

  * **Connect one shell** :

  * **Connect all shells** :

### Measure

**Measuring** : In this section, it shows the measuring type when the distance is measured between point to point or between polygon to polygon along with the vector, Length and Label of the measured distance. (See Fig. 50.1.39.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0039.jpg' | relative_url }})

Measure Tab options

**Direction** : Using direction options user can select the direction in which the measurement has to be done between two selected entities.

**Filter** : This section helps to measure the distance between points, edges, Triangle and Face, by turning on the respective check boxes user can measure the distance.

**Information** : This section provides information regarding the polygon over which the cursor is placed or picked. The information includes polygon number, co-ordinates, area and normal direction.

**Delete** : Using Delete button user can delete the last measured distance.

**Delete All** : Using Delete All button user can delete all the measured distances.

### Slicing

Slicing tab can be used to slice the geometry and view. Geometry can be sliced in any direction by turning on the respective check boxes. Position of the slicing plane can be adjusted using the sliding bar.(See Fig. 50.1.40.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0040.jpg' | relative_url }})

Geometry Slicing

**Slicing Objects:** When user clicks on the slicing objects button it creates new object by slicing the exiting object geometry at the specified slicing plane. Original part is retained and holes are filled based on the respective check boxes status.

**Imprint Objects** : Using imprint option user can imprint the geometry of one object on the other, like using cylinder option to make circular groves after splitting the grooved portion, see Fig. 50.1.41.

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0041.jpg' | relative_url }})

Example for using the imprint option to produce projections

### Modify

**Trimming** : Trimming options are used to remove the part of the geometry by defining the trimming line. This can be done by following steps,

  1. Defining the Trimming line on the Geometry. (See Fig. 50.1.42.)

  2. User can see the preview of the trimming geometry. (See Fig. 50.1.43.)

  3. Click Trim button to trim the geometry. (See Fig. 50.1.44.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0042.jpg' | relative_url }})

Defining the trimming line

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0043.jpg' | relative_url }})

Trimming preview

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0044.jpg' | relative_url }})

Geometry after Trimming

User can keep the original object by turning on the Keep original part check box.

**Boolean :** Boolean options are used to join, Subtract and to take out the common of two geometries.

**Union** : Union option is used to combine two geometries into one. Union can be done using following steps,

  1. Create two geometries or import two geometries.

  2. Position the geometries overlapping based on the new geometry requirement.

  3. Shift to Modify property editor page. (See Fig. 50.1.45.)

  4. Select the union button to combine the two geometries, color shades of the geometries to be combined are shown in Modify page. (See Fig. 50.1.46.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0045.jpg' | relative_url }})

Defining two new geometries

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0046.jpg' | relative_url }})

Joining the geometries using Union option

**Subtract :** Subtracting option is used to remove the unwanted area of the Geometry using other object geometry. Subtracting can be done using following steps,

  1. Create two geometries or import two geometries.

  2. Position the geometries to overlap one on another. (See Fig. 50.1.47.)

  3. Shift to Modify property editor page.

  4. Select the subtract option to subtract one geometry from another geometry, color shades of the geometry that is subtracted and geometry from which it is subtracted are shown in Modify page (See Fig. 50.1.48.).

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0047.jpg' | relative_url }})

Defining two new geometries for subtracting

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0048.jpg' | relative_url }})

Subtracting geometry

**Intersect** : This option is used to take out the common part of the two geometries, this can be done by using following steps,

  1. Create two geometries or import two geometries.

  2. Position the geometries to overlap one on another.

  3. Shift to Modify property editor page. (See Fig. 50.1.49.)

  4. Select the Intersect button option to take out the common part of the two geometries, color shades of the geometries from which common geometry will be taken out are shown in Modify page (See Fig. 50.1.50.).

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0049.jpg' | relative_url }})

Creating two geometries

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0050.jpg' | relative_url }})

Taking out the intersecting part

User can keep the original object by turning on the Keep original part check box.

###  Verify

**Quality** : In the quality box, user can analyze the Fold in the geometry based on the specified criteria and also delete the Folds. (See Fig. 50.1.51.)

**Comparison** : Using the comparison;; options, user can compare the two geometries in terms of number of polygons, number of points, Min Length of Polygon, Min Area of Polygon, Number of shells, Number of Noisy shells, Number of Bad edges, Number of Free edges, Volume and Surface Area. (See Fig. 50.1.51.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0051.jpg' | relative_url }})

Verify tab options

### Morphing

Morphing can be used by user to modify the geometry of one object to the other. Morphing is mostly used while setting up optimization problems.(See Fig. 50.1.53.)

**Connect pairs:** Two objects are required to perform morphing. One object is considered as source, the geometry of which needs to be transformed and other object is considered as target, the geometry to be achieved. User can select the surface from source to be transformed and corresponding surface on target and pair them.

In connect pairs page, user can add, remove, import and export the connected pairs. (See Fig. 50.1.52.)

User can calculate the results by clicking on the calculate button.

After calculating the results user can see the preview of the morphed geometry.

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0052.jpg' | relative_url }})

Connect Pairs window

**Preview Morphing Results** : After calculating the results user can see the preview of the various stages of morphing using sliding bar. User can remove the preview of the morphing results using ![]({{ '/assets/icons/pre_icons/mo_clear_icon.jpg' | relative_url }}) icon. (See Fig. 50.1.53.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0053.jpg' | relative_url }})

Preview Morphing Results window

**Save Morphing Results** : User can save the Morphing results by browsing a location and it is saved in *.GEO format. (See Fig. 50.1.54.)

![]({{ '/assets/images/operation_templates/50_3d_geometry_tools/50_1_geometry_tools/image0054.jpg' | relative_url }})

Save morphing results window

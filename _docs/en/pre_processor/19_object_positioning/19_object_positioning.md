---
lang: en
title: "19. Object Positioning"
---

# 19\. Object Positioning

19.1. Drag Positioning

19.2. Offset Positioning

19.3. Interference positioning

19.4. Rotational positioning

19.5. Drop positioning

19.6 Flip positioning

19.7. Coupled positioning

Object positioning dialog can be accessed by clicking on ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) button in Positioning page. (See Fig. 19.1. and Fig. 19.2.)

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image001.jpg' | relative_url }})

2D Object positioning window

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image002.jpg' | relative_url }})

3D Object positioning window

Once the object is defined, a variety of positioning features are available to place the objects in the correct position before the process is modelled. The object can be dragged using mouse, can be dropped in to the die cavity, moved by a specific offset distance, positioned with interference or positioned with rotational movement. A set of components can also be selected and positioned together using coupled positioning.

**Update Current Stroke** : When user checks this check box, "positioning object" current stroke value will update w.r.t. positioned distance.

**Update Windows Following positioning object** : When user checks this check box, defined windows (mesh window or Env. windows) will position with respect to the object positioning methods like Drag, Interference, etc. which are described in below sections 19.1 to 19.7.

**Reset![]({{ '/assets/icons/pre_icons/mo_reset_button.jpg' | relative_url }}) **: using this option user can reset the objects to its initial position. 

## Drag Positioning

**[2D, 3D]:** Objects can be dragged or dynamically rotated using drag option in a certain direction using the mouse. Drag the mouse in the required direction so that we can place as per we required. If you select Translation motion the object will translate based on your dragging direction. If you select Rotation motion the object will rotate based on dragging of your mouse. (See Fig. 19.3., Fig. 19.4. and Fig. 19.5.)

**Mouse driven positioning**

Mouse driven positioning is used to move or rotate the object by allowing the user to select a vector along which to drag or spin any specified object along or about that vector.

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image003.jpg' | relative_url }})

Drag Positioning window for 2D

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image004.jpg' | relative_url }})

Drag Positioning window for 3D

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image005.jpg' | relative_url }})

Example showing usage of drag positioning

## Offset Positioning

**[2D, 3D]:** Offset positioning is used to move the object to position by a given displacement in the chosen direction. The object to be positioned should be highlighted in the Positioning object list table. The displacement in the X, Y, and Z (for 3D) coordinates should be entered in the appropriate fields. ( Fig. 19.6. and Fig. 19.7.)

**Distance Vector****:** using********Distance Vector** **option user need to define the displacement in the X, Y, and Z (for 3D) coordinates should be entered in the appropriate fields.

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image006.jpg' | relative_url }})

Distance vector - Offset Positioning window for 2D

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image007.jpg' | relative_url }})

Distance vector - Offset Positioning window for 3D

**Two points:** using Two point option user can offset by enter the From and To fields values. Even by mouse click on the boundary points user can define the From and To fields values. (See Fig. 19.8., Fig. 19.9. and Fig. 19.10.).

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image008.jpg' | relative_url }})

Two points - Offset Positioning window for 2D

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image009.jpg' | relative_url }})

Two points - Offset Positioning window for 3D

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image010.jpg' | relative_url }})

Example showing usage of offset positioning using two point method

**Centroid of Two objects type Offset Positioning :** The user can offset using the centroid to align positioning object. (See Fig. 19.11.)

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image011.jpg' | relative_url }})

Offset Centroid Positioning example

## Interference positioning

**[2D, 3D]** : Interference positioning moves the object for a given set of "positioning" and "reference" relationship between two objects, the distance between two objects is calculated both from the positioning and reference objects then, the smaller value of this distance is used as an offset value for positioning (See Fig. 19.12., Fig. 19.13. and Fig. 19.14.). During the positioning process, the object being positioned is first moved a large distance away from the reference object, then moved back towards the reference object in the indicated direction, until first contact is made.

For a non-rigid object (plastic, elastic, porous, Elasto-plastic) if the mesh is not existing, object geometry is used for interference positioning.

**Common Question: What is a reasonable value of Interference?**

**Answer** : Interference should be adjusted such that when inter-object boundary conditions are generated, a reasonable number of nodes are in contact with tools. Contact nodes should be generated wherever the object should reasonably be touching the tools.

This may require increasing or decreasing both the interference value and the contact node generation tolerance.

**Do not move object outside bounding box of reference object before positioning** : option for interference positioning is available for DEFORM-2D pre-processor (from v10.2.1), this positioning option is implemented for machining distortion case with undercut surface where interference positioning didn’t work correctly.

It positions the object by interference with respect to the innermost (Internal boundary) boundary of the reference object in the specified direction.

**For example** : In 2d Plane strain for Hollow cylinder or prism top section with internal pressure applying by any object then that object to position against the internal surface we need to use positioning by bounding box.

**For example** : in 3d ring rolling setup, to position the Mandrel with respect to or against workpiece ring inner circle surface then we need to use positioning by bounding box.

**Follow Movement Direction** : When user checks this check box object will position with respect to the movement defined direction.

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image012.jpg' | relative_url }})

Interference Positioning window for 2D

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image013.jpg' | relative_url }})

Interference Positioning window for 3D

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image014.jpg' | relative_url }})

Example showing usage interference positioning

From DEFORM V12.0.2, "First encountered" object positioning option provided in interference object positioning (See Fig. 19.15.). This option allows the user to position the object in such a way that the positioning object will come and position automatically with the object which is going to encounter first along its moving path.

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image026.jpg' | relative_url }})

First encoutered Reference option 

## Rotational positioning

**[2D, 3D]:** Rotation positioning allows the user to rotate any object about a specified axis. The axis of rotation is specified from a point and a direction vector. The specified rotation angle is positive for a right hand rotation about the axis.

In rotational positioning, positioning object can have its own object center as rotation center. Angle (degree) is measured in counter-clock wise direction. (See Fig. 19.16. to Fig. 19.20.)

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image015.jpg' | relative_url }})

Rotational Positioning window for 2D

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image016.jpg' | relative_url }})

Rotational Positioning window for 3D

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image017.jpg' | relative_url }})

2D Example showing usage of rotation positioning

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image018.jpg' | relative_url }})

3D Example 1 showing usage of rotation positioning

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image019.jpg' | relative_url }})

3D Example 2 showing usage of rotation positioning

## Drop positioning

**[3D]:** Drop positioning is used to move an object towards another object by interference or by gravity (See Fig. 19.21. and Fig. 19.22.).

  * **Allow Rotation only about:** User can limit the direction of rotation by dropping the object by checking the check box and the direction mentioned.

  * **Don't allow rotation:** If user don't want to define rotation before dropping an object, by checking this check box user can do drop positioning.

  * **Save Movie File:** By checking this check box user can save the animation of Drop positioning.

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image020.jpg' | relative_url }})

3D Drop Positioning window

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image021.jpg' | relative_url }})

Example showing usage of Drop positioning

  * **Gravity activated** : In the case of gravity activated, the positioned object should be the meshed object. The direction should be the direction that gravity would drive it to fall on the other object. The object can move in 6 degrees of freedom (3 directions of translation and 3 axes of rotation) without any given constraint. Constraint in rotational direction can be added if only one rotational degree of freedom is required. If only one rotational direction is required, the Allow rotation only about box should be selected and the vector about which to rotate should be specified.

  * **Gravity not activated** : In the case where gravity is not activated, this behaves exactly like the interference positioning method.

## Flip positioning

**[2D]** : Flip allows the user to mirror an object about the selected-axis or any line parallel to the selected-axis as shown in Fig. 19.23. and Fig. 19.24.

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image022.jpg' | relative_url }})

2D Flip Positioning window

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image023.jpg' | relative_url }})

Example showing usage of flip positioning

## Coupled positioning

**[2D, 3D]** : This allows several objects to move on the same positioning action (See Fig. 19.25. and Fig. 19.26.). By checking objects in the couple positioning dialog, the objects will be positioned by the exact same amount as the positioned object.

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image024.jpg' | relative_url }})

Coupled Positioning window

![]({{ '/assets/images/pre-processor/19_object_positioning/19_image025.jpg' | relative_url }})

Example showing usage of couple positioning with Drag positioning option

****

**Related Topics:**

[2D-Primitive geometries](../12_geometry_modelling/12_1_2d_geometry_data_defining.htm#Define_Primitives)

[3D-Primitive geometries](../12_geometry_modelling/12_3_3d_geometry_data_defining.htm#Define_Primitive)

[12\. Geometry Modelling](/docs/en/pre_processor/12_geometry_modelling/12_geometry_modelling/)

[13\. Mesh Generation](/docs/en/pre_processor/13_mesh_generation/13_mesh_generation/)

[Selecting the Movement direction of the objects](../15_movement_controls_definition/15_movement_controls_settings.htm#Directions)

[20\. Inter-object Data Definition](/docs/en/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/)

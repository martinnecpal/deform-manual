---
lang: sk
title: "26.6.16. Interactive slicing"
---

# 26.6.16. Slicing

[3D]:The slicing dialog allows the user to cut a section into the workpiece. When the section is made, shaded contours can be seen in the cut area. The dialog appears as shown in Fig. 26.6.16.1. The cut section can be made by clicking on a line of the bounding box of the object. The default mode for a slicing plane is to define it by a point on which the plane lies and a vector that is normal (or perpendicular) to the slicing plane. The normal direction indicates the side of the plane that will be cut away. Once a plane has been selected, the location of point can be changed by selecting the point value that corresponds to the normal direction of the plane and dragging the slider bar.

  
![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_16_interactive_slicing/image001.jpg' | relative_url }})

3D Slicing window

**Modes** : point +Normal: Input a point and normal to determine a slicing plane. (See Fig. 26.6.16.2. and Fig. 26.6.16.3.)

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_16_interactive_slicing/image002.jpg' | relative_url }})

Slicing example using Point + Normal method with single plane

  
![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_16_interactive_slicing/image003.jpg' | relative_url }})

Slicing example using Point + Normal method with two planes

**3 points** : Input three points to determine the slicing plane. (See Fig. 26.6.16.4.)

  
![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_16_interactive_slicing/image004.jpg' | relative_url }})

Slicing example using 3 points method for different values

**Point+Axis+Angle** : Input a point, Axis and Angle to determine a slicing plane. (See Fig. 26.6.16.5.)

  
![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_16_interactive_slicing/image008.jpg' | relative_url }})

Slicing example using point+axis+Angle method

****

**Add![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) **: using this option user can add a slicing plane.

**Delete![]({{ '/assets/icons/pre_icons/mo_delete_icon2.jpg' | relative_url }}) **: using this option user can delete defined slicing plane

**Cutter![]({{ '/assets/icons/pre_icons/mo_cutter_icon.jpg' | relative_url }}) **: using this option user can slice the object.

**Preview![]({{ '/assets/icons/pre_icons/mo_preview_icon.jpg' | relative_url }}) **: using this user can show/hide the slicing plane.

**SV max plot** ![]({{ '/assets/icons/pre_icons/mo_sv_max_point_button.jpg' | relative_url }}) : to slice through the point which has the maximum value of the state variable.

**SV min plo** t ![]({{ '/assets/icons/pre_icons/mo_sv_min_point_button.jpg' | relative_url }}): to slice through the point which has the minimum value of the state variable.

**Duplicate**![]({{ '/assets/icons/pre_icons/mo_duplicate_button.jpg' | relative_url }}) : Make a set of slicing planes parallel to the selected plane. (See Fig. 26.6.16.6.)

**Reverse** : Check to reverse the normal of the selected slicing plane

**Save![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}) **: using this option user can Save 2D slice geometry and/or state variable. 2D Geometry can be saved in .IGS, DXF or in .KEY format.

**Save Slicing planes** ![]({{ '/assets/icons/pre_icons/mo_save_to_library_icon.jpg' | relative_url }}): Using this option user can save the Slicing plane data to a file in .dss file format.

**Load Slicing Planes![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) : **Using this option user can import the saved Slicing plane file.

  
![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_16_interactive_slicing/image005.jpg' | relative_url }})

Slicing plane duplicate example with 3 slicing planes

**Reverse** : Check to reverse the normal of the selected slicing plane. (See Fig. 26.6.16.7.)

  
![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_16_interactive_slicing/image007.jpg' | relative_url }})

Reverse slicing plane example

**Slicing plane display** :

**Curve** : In display it shows only the boundary of the object while slicing an object.

**Plane** : In display it shows only the surface of the object while slicing an object.

**Curve +Plane** : In display it shows both boundary and surface of the object while slicing an object. (See Fig. 26.6.16.8.)

**Slice All Objects**![]({{ '/assets/icons/pre_icons/mo_slice_all_objects_button.jpg' | relative_url }}) : slice all the shown objects using the selected plane.

  
![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_16_interactive_slicing/image008.jpg' | relative_url }})

Slicing plane display options example

**Section Color** : It is sed to turn on and off the color to sliced plane. (See Fig. 26.6.16.9.)

![]({{ '/assets/images/post_processor/26_post_processor_display_controls/26_6_post_processing_tools/26_6_16_interactive_slicing/image009.jpg' | relative_url }})

Slicing plane section color display option

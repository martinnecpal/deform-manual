---
lang: en
title: "25. Post Processor Layout"
---

# 25\. Post-Processor Layout

25.1. Post features settings modifications window

25.2. Object Tree

25.2.1. Operation tree options

25.2.2. Object Tree Right Mouse button (RMB) options

25.3. Graphics window

25.4. Report Generation

25.5. Dock Widget menu

Post-processor provides an intuitive GUI for the user to view simulation output, interpret results and generate report in various formats such as pdf, ppt…etc. PIP feature of Next Gen Post helps the user to compare simulation output across multiple databases.

Post-processor GUI layout (See Fig. 25.1.) can be divided into Step View, Object Tree, Post features settings modifications window and graphics window.

![]({{ '/assets/images/post_processor/25_post_processor_layout/image001.jpg' | relative_url }})

Post-processor layout

**Step View Window** provides options to select and play the simulated steps and also to select the operations and display information related to current operation and step.

**Graphics window** will display graphical representation of objects. The graphics window can be used for displaying the contour plots, graphs, grain flow, etc.

**Post Tools** are used to plot different state variables, point track state variables, study grain flow using flownet, extract data from DB, plot summary graphs, create animation, etc.

**Object Tree** lists the objects and controls their display. Report Tab within object tree window can be used by user for generating report of simulation results.

**Post features** settings modifications window is used to select and modify the post features and its settings for state variables plot, point tracking, flownet, summary graphs, data extraction, load-stroke graphs, symmetry, slicing (only for 3D), region of interest, animation setup, etc.

## Post features settings modifications window

Post features settings modifications window is a region that displays options and settings for selected features of the post processor as shown in Fig. 25.1. The options and settings can be set and modified in this region.

The options and settings for each feature are explained along with the feature further in section Post Features.

## Object Tree

The objects and its display information such as objects visibility, geometry, mesh, transparency, slice plane, point tracking and Flownet information is available in this window as shown in Fig. 25.1.

User can select the object to be visible for display in graphics window using left mouse click on the particular object in the tree and change its display modes. Point tracking and Flownet can be hidden or deleted using RMB click on the Point tracking/Flownet tracking link in the object tree.

### **Operation tree options**

**[2D][3D]:**

**Show Object![]({{ '/assets/icons/pre_icons/mo_show_obj_icon.jpg' | relative_url }}) :** Turns on/off the selected object from object tree.

**Show Mesh![]({{ '/assets/icons/pre_icons/mo_show_mesh_icon.jpg' | relative_url }}) :** Shows or hides mesh of the selected object from object tree.

**Show Geometry![]({{ '/assets/icons/pre_icons/mo_show_geo_icon.jpg' | relative_url }}) :** Shows or hides geometry of the selected object geometry from the object tree.

**Show Contact Nodes:![]({{ '/assets/icons/pre_icons/mo_show_cotact_icon.jpg' | relative_url }}) **Turns on the contact display for the selected object from object tree with all other all object. (See Fig. 25.1. )

  
**[3D]:**

**Make Transparent![]({{ '/assets/icons/pre_icons/mo_transparent.jpg' | relative_url }}) :** Turns on/off transparency of the selected object from the object tree.

**Show Backface![]({{ '/assets/icons/pre_icons/mo_show_backfac_icon.jpg' | relative_url }}) :** Turns on/off the back surface of the object selected object from the object tree, it will be more useful when the object are made transparent. (See  Fig. 25.2.)

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image032.jpg' | relative_url }}) ![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image033.jpg' | relative_url }})

  
(a) (b)

Plastic object mesh in shaded rendering type; (a) With Back face on (b) With Back face off

**[2D][3D]:**  
**Object Display Modes:** DEFORM has 3 different object display modes as shown in Fig. 25.1.

**Single Object mode![]({{ '/assets/icons/pre_icons/mo_show_single_obj_icon.jpg' | relative_url }}) :** Only the selected object from object tree is displayed. All other objects are hidden.

**Multi Object mode**![]({{ '/assets/icons/pre_icons/mo_show_multi_obj_icon.jpg' | relative_url }}) : All objects are displayed in graphics window. The selected object from object tree is displayed in solid color and all other objects are transparent in 3d mode. (See Fig. 25.3.)

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image034.jpg' | relative_url }})

Multi object mode when plastic workpiece object get selected

  
**User Object mode**![]({{ '/assets/icons/pre_icons/mo_show_user_defined_obj_icon.jpg' | relative_url }}) : User can toggle the object's Display, Geometry, Mesh, Transparency (only for 3D), Slice plane (only for 3D) modes independently. This can be done by checking and unchecking respective check boxes as shown in Fig. 25.4.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image035.jpg' | relative_url }})

User defined Object Mode window

  
Following are the settings we have to select based on the objects display requirements,

**Apply Display options**![]({{ '/assets/icons/pre_icons/mo_apply_display_option.jpg' | relative_url }}) : Applies the selected display option for the objects.

**Visible**![]({{ '/assets/icons/pre_icons/mo_visible.jpg' | relative_url }}) : Turns on/off the selected object display.

**Mesh**![]({{ '/assets/icons/pre_icons/mo_mesh_icon.jpg' | relative_url }}) : Shows or hides display of the selected object mesh.

**Geometry**![]({{ '/assets/icons/pre_icons/mo_geometry _icon.jpg' | relative_url }}) : Shows or hides display of the selected object geometry.

**Transparency![]({{ '/assets/icons/pre_icons/mo_transparent.jpg' | relative_url }})** : Turns on/off transparency of the selected object.

**Slice**![]({{ '/assets/icons/pre_icons/mo_slice.jpg' | relative_url }}) : Turns on/off sliced plane for the selected sliced object.

### **Object Tree Right Mouse button (RMB) options**

**Problem Data** [2D, 3D]:   
The Problem Data menu contains the following command as shown in Fig. 25.5. and Fig. 25.6.

**[2D, 3D]:**

**Select All objects** : When user clicks on this option it turns on all the objects Select column check boxes in Operation tree.

**Unselect All objects** : When user clicks on this option it turns off all the objects Select column check boxes in Operation tree.

**Turn on all objects** : When user clicks on this option it turns on all the objects in display window.

**Turn off all objects** : When user clicks on this option it turns off all the objects in display window.

**Turn on all workpieces (not RIGID)** : Turns on any object which is not rigid. (Turns off all rigid objects)

**T******ur** n on all dies (RIGID)**: Turns on any object which is rigid. (Turns off all other objects)

**Turn on contact display for all** : It turns on the contact display of all objects in display window.

**Turn off contact display for all** : It turns off the contact display of all objects in display window.

**Import Object** : User can import object from key file or Database.

**Import Geometry** : User can import geometry from key file, database, IGS, STL, DXF formats.

**[3D]:**

**Turn on transparency for all** : It makes objects transparent in display window.

**Turn off transparency for all** : It turns off the transparency of objects in display window.

**Turn on backface for all:** It shows the back surface of the object, it will be more useful when the objects are made transparent.

**Turn off backface for all** : It turns off the Backface of objects.

![]({{ '/assets/images/post_processor/25_post_processor_layout/image008.jpg' | relative_url }})

RMB menu options on objects in Operation tree for 2D 

![]({{ '/assets/images/post_processor/25_post_processor_layout/image007.jpg' | relative_url }})

RMB menu options on objects in Operation tree for 3D 

**Object Data [2D, 3D]**  
The Object Data menu (See Fig. 25.7., Fig. 25.8. and Fig. 25.9.) contains some or all of the following commands, depending on object type:

**[2D, 3D]:**

**Show Geometry** : It shows the object Geometry

**Change shade color (Geometry)** : Changes the surface facet fill color.

**Change line color (Geometry)** : Changes the color of lines delineating facet edges.

**Export Geometry** : Using this option object geometry data can be saved.

**Show Mesh** : It shows the object Mesh

**Change shade color (Mesh)** : Changes the element fill color.

**Change line color (Mesh)** : Changes the color of the lines delineating element edges.

**Show contact node** : Highlights contact for selected object with any Master object. This is a quick way to display contact. This is a toggle menu selection. Select it once to turn the contact node display on. Select it again to turn the display back off.

**[3D]:**

**Show Geometry and Normal Vecto** r: Turns on the geometry with normal vectors display.

**Use smooth shading (Mesh)** : Renders the mesh shading display to smooth.

**Make Transparent** : It makes objects transparent.

**Change transparency:** Using this option the transparency of the 3D object mesh can be varied.

**Show backface** : It shows the back surface of the object.

**Movement (only For Primary Die)**

**Show translational movement** : It displays the translational movement direction in the display window.

**Show rotational movement** : It displays the rotational movement direction in the display window.

**Load (only For Primary Die)** : It displays the load movement direction in the display window.

**Diff Step (Increment SV)** : User can plot the State variable value at that particular step using Diff Step option  
(See Fig. 25.10.). User can plot the difference in the step that is loaded to the current step (See below Fig. 25.11.).

![]({{ '/assets/images/post_processor/25_post_processor_layout/image003.jpg' | relative_url }}) ![]({{ '/assets/images/post_processor/25_post_processor_layout/image004.jpg' | relative_url }})

(a) (b)

RMB menu options on selected object in Operation tree (a) for 3D and (b) for 3D

![]({{ '/assets/images/post_processor/25_post_processor_layout/image006.jpg' | relative_url }}) ![]({{ '/assets/images/post_processor/25_post_processor_layout/image005.jpg' | relative_url }})

(a) (b)

RMB menu options on Object Mesh in Operation tree (a) for 3D and (b) for 3D

![]({{ '/assets/images/post_processor/25_post_processor_layout/image010.jpg' | relative_url }}) ![]({{ '/assets/images/post_processor/25_post_processor_layout/image009.jpg' | relative_url }})

(a) (b)

RMB menu options on Object Geometry in Operation tree (a) for 3D and (b) for 3D

![]({{ '/assets/images/post_processor/25_post_processor_layout/image011.jpg' | relative_url }})

Plotting Diff step

![]({{ '/assets/images/post_processor/25_post_processor_layout/image012.jpg' | relative_url }})

Plotted Interpolated SV option

**Material Data![]({{ '/assets/icons/pre_icons/mo_material_icon.jpg' | relative_url }}) : [2D, 3D]: **The RMB Material Data buttons allows the user to access the material properties window (See Fig. 25.12.). For more information please refer [Chapter 10. Material Data](/docs/en/pre_processor/10_material_data/10_material_data/)

![]({{ '/assets/images/post_processor/25_post_processor_layout/image013.jpg' | relative_url }})

RMB menu options on material in Operation tree

## Graphics window

Graphics window displays the graphical representation of the objects. This will display state variables contours over objects, graphs, histograms, flownet and die fill (contact nodes). (See Fig. 25.1. )

Right mouse click on the graphics window will provide few options to display the simulation information, set the viewport, measure dimension and change background theme.(See Fig. 25.13.) For more information about these options refer the [Graphics window RMB options.](../../integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_1_integrated_manufacturing_process_preprocessor_layout.htm#Graphics_window_RMB_options)

![]({{ '/assets/images/post_processor/25_post_processor_layout/image014.jpg' | relative_url }}) ![]({{ '/assets/images/post_processor/25_post_processor_layout/image015.jpg' | relative_url }})

(a) (b)

Right mouse button graphics window options; (a) For 2D (b) For 3D

**Show title bar:** It displays the Title bar in display window.

## Report Generation

Report Generation feature provided can be used to generate report in different formats such as ppt and pdf for selected post-processing features like State variables contour, Point tracking, Flownet, Coupons of data extraction, Regions of interest, Summary graphs, Load-stroke graphs and data extraction.

  
For more information on report generation setup refer [Chapter 28. Report Generation](/docs/en/post_processor/27_introduction_to_report_generation/27_introduction_to_report_generation/).

## Dock Widget menu

Using Dock widget menu options, user can turn on/off Step view, Operation tree and Post features settings modifications window. (See Fig. 25.14.)

![]({{ '/assets/images/post_processor/25_post_processor_layout/image002.jpg' | relative_url }})

Post processor Dock widget menu 

**Related Topics:**

[24\. Introduction to Post-Processor](/docs/en/post_processor/24_introduction_to_post_processor/24_introduction_to_post_processor/)

[26\. Post Processor Display controls](/docs/en/post_processor/26_post_processing_tools_and_controls/26_post_processor_features/)

[27\. Post Processing tools](/docs/en/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_post_processing_tools/)

[28\. Report Generation](/docs/en/post_processor/27_introduction_to_report_generation/27_introduction_to_report_generation/)

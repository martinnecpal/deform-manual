---
lang: sk
title: "6.1. Integrated Manufacturing Process Pre-processor layout"
---

# 6.1. Integrated Manufacturing Process Pre-processor layout

6.1.1. Explorer

6.1.2. Operation Editor

  * General options

  * Operation options

  * Object options

6.1.3. Operation Tree

  * Operation Tree Tool bar options

  * Object Tree Right Mouse button (RMB) options

6.1.4. Property Editor

6.1.5. Message tab

6.1.6. Step Editor

6.1.7. Graphics window

6.1.8. Tool Bar Options

Integrated Manufacturing Process Pre-processor (MO) has Pre, Simulation and Post modes in one window. Pre mode GUI layout (See Fig. 6.1.1.) is mainly divided into Object tree, Graphics window, Property editor, Operation Editor and Explorer and Operation Manager regions.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image001.jpg' | relative_url }})

MO Pre GUI layout

**Explorer tab** displays list of different templates/modules, DEFORM material library and Press movement library in MO environment.

User can navigate through **Operation Tree** and **Property Editor** to setup problem.  
**Graphics window** will display graphical representation of objects. The graphic tab can be used for displaying the geometry and mesh information of the simulation objects.  
**Operation Editor** will provide the space to edit and organize the sequence of multiple operations.

**Message tab** will display the information or errors related to the setup.  
Preprocessor data can be changed at any of the simulated step by using the **Step Editor**.

**Operation Manager** list operations, objects, material, equipment's used in the project.

## Explorer

Explorer is having the list of available Operations, Material library and Press library.

Operations explorer lists different operations available in MO. The list of operations available in MO are,

  * Cogging

  * 3D Cogging

  * Die Stress

  * Die Stress 2D
  * Die Stress 3D

  * Extrusion

  * 3D Extrusion

  * Forming
  * **Multiple**

  * 2D Multi Blow Forging
  * 3D Multi Blow Forging

  * **Single**

  * 2D Forming

  * 2D Forming Express

  * 3D Forming

  * 3D Forming Express

  * General

  * 2D General
  * 3D General

  * Heat Transfer

  * 2D Heat Transfer
  * 2D Heat Transfer Express
  * 3D Heat Transfer
  * 3D Heat Transfer Express

  * Heat Treatment

  * 2D HT Wizard
  * 3D HT Wizard
  * 3D HT Furnace

  * Machining

  * 2D Cutting
  * 3D Cutting
  * 2D Machining Distortion
  * 3D machining Distortion

  * Report

  * Report Generation

  * Rolling

  * Ring Rolling
  * Shape Rolling

  * Simulation Operator

  * 2D to 3D Converter
  * Boolean Operator 2D
  * Boolean Operator 3D
  * Copy/Mirroring
  * Cycle

  * Spinning

  * 3D Spinning

  
**Note:**

General pre is converted into Forming operation and Forming operations are converted into Forming express in MO.

Operations can be added in sequence of manufacturing process by clicking the ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button next to the operations name or by dragging and dropping into the operation editor region or by double clicking the operation in the operation explorer (See Fig. 6.1.2.). Depending on requirement of setup, user can filter the operations for easy selection based on 2D, 3D, Express and Advanced modules. Also we can load the saved Template under User tab.

  
![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image002.jpg' | relative_url }}) ![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image006.jpg' | relative_url }})

  
(a)  (b)

Operations Explorer tab; (a) System (b) User

  
Material Explorer provides access to DEFORM material library. Material library has different categories like Aluminum, Steel, Stainless, Super alloys, Titanium, Die material, Tool material etc. Depending on requirement of setup, user can filter materials selection based on Cold Forming, Hot Forming, Heat treatment and Machining. User can create new material or modify the material properties and save them into user library depending on category, these can be accessed from the material explorer user tab (See Fig. 6.1.3.).

  
![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image003.jpg' | relative_url }}) ![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image004.jpg' | relative_url }})

  
(a) (b)

Material Explorer tab; (a) System (b) User

Equipment Explorer provides access to Hammer, Mechanical and Screw press equipment data required for simulation for few standard equipment's standard operating loads as per the industry standards. User can create new equipment or modify existing equipment movement data and store in user library, the user library can be accessed through the user tab (See Fig. 6.1.4.).

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image005.jpg' | relative_url }}) ![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image007.jpg' | relative_url }})

  
(a) (b)

Equipment Explorer tab; (a) System (b) User

## Operation Editor

Operation editor (See Fig. 6.1.5.) is the region where the operations can be added, deleted, selected for editing and arrange sequence of operations. Operations can be reordered by dragging them in the operation editor. Options are provided to transfer required object data across operations.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image011.jpg' | relative_url }})

Operation Editor

User needs to setup the operations sequentially as displaying in the operation editor by using operation tree or property editor. After the setup user can edit any operations properties by selecting the particular operation from the operation editor, selection will highlight the operation by orange outline as shown in Fig. 6.1.5.

  
In Operation Editor right mouse button click will provide options as listed below. (See Fig. 6.1.6.)

  
![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image008.jpg' | relative_url }}) ![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image009.jpg' | relative_url }})

(a) (b)

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image010.jpg' | relative_url }})  
(c) 

Operation editor options; (a) General options (b) Operation options and (c) Object options

**General options**

**Fit View:** Fit the view of the Operations in operation editor. (See Fig. 6.1.7.) 

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image012.jpg' | relative_url }})

(a)

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image013.jpg' | relative_url }})

(b)

Fit view; (a) Before view fit (b) After view fit

  
**Fit Selected** : Fit the view of the selected operation in operation editor. (See Fig. 6.1.8)

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image014.jpg' | relative_url }})

(a)

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image015.jpg' | relative_url }})

  
(b) 

Fit selected operation view; (a) Before view fit (b) After view fit

  
Enable magnifier: Simply keeping the cursor on the operation editor region will magnify that region (See Fig. 6.1.9). By default this magnifier is disabled, this can be disabled by unchecking check box.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image016.jpg' | relative_url }})

Operation Editor magnifier

**Operation options**

**Delete Operation:** Deletes the selected operation from the MO Project (See Fig. 6.1.10). Delete option available in the operations RMB options also.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image017.jpg' | relative_url }})

Delete operation option

  
**Add cycle:** This is used to perform same operations repetitively in cycle. User needs to select the operations to repeat and the number of times to repeat (See Fig. 6.1.11).To add cycle to operation, the first operation in cycle must have read from DB object. To analyze the die stress and temperatures after the multiple components manufacturing is an example where user can use the add number of cycles as components produced.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image018.jpg' | relative_url }})

Extent to use the add cycles

For more details on add cycles refer the chapter[ 6.6.5. Adding Cycles.](/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_6_operations_management/6_6_5_adding_cycles/)

**Copy/Paste operation:** Copy/Paste operation option can be used to eliminate the duplicated input effort to speed up the problem preparation.

  
To do Copy/pasting operation:

  1. Select one or more operations in the operation editor by Clicking in the background of the operation editor and dragging the mouse to select one or more operations or using ctrl + mouse click to select/unselect an operation 
  2. Use mouse to right-click on one of the selected operations, and then click the ‘Copy’ menu item ([ Fig. 6.1.12 a.](6_1_integrated_manufacturing_process_preprocessor_layout.htm#Fig._6.1.12.a_Select_copy_option_to_copy_the_selected_operation/s)).Use mouse to right-click on an operation and the click the ‘Paste’ menu item. The copied operations will be pasted after this operation[ Fig. 6.1.12\. b](6_1_integrated_manufacturing_process_preprocessor_layout.htm#Fig._6.1.12.b_Select_paste_to_paste_the_copied_operation/s),  Fig. 6.1.12\. c ).

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image019.jpg' | relative_url }})

  
(a) Select copy option to copy the selected operation/s

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image020.jpg' | relative_url }})

  
(b) Select paste to paste the copied operation/s

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image021.jpg' | relative_url }})

(c) copied operations added in operation list.

Copy/Paste operation

**Breakpoint** : Using Breakpoint option user can add Breakpoint to stop the simulation before the selected operation by selecting Breakpoint option as shown in Fig. 6.1.13.This will help the user to view simulation behaviour until that operation before proceeding with other operations

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image022.jpg' | relative_url }})

(a) adding Breakpoint operation using before this operation option

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image023.jpg' | relative_url }})  
(b) added Breakpoint operation using before this operation option

Adding Breakpoint Operation

  
**Delete Breakpoint:** Added Breakpoint operation can be deleted by unchecking the Breakpoint check box.

**No. 1** : Display’s the operation number.

**Type** : Display’s the type of the selected Operation.

**Folder (Open task folder)** : Using this option user can open the selected operation task folder which consists files related to the selected operation (See Fig. 6.1.14.).

  
![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image024.jpg' | relative_url }})

Operation Editor options

**Object options**

Pass Object To Next Operation: Using this option object data can be transferred to the next operation. (See  Fig. 6.1.15.)

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image025.jpg' | relative_url }})

(a)

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image026.jpg' | relative_url }})

(b)

Pass object to next operation option; (a) Before passing and (b) After passing

**Pass Object To All Operations:** Using this option object data can be transferred to all operations. (See Fig. 6.1.16.)

  
![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image027.jpg' | relative_url }})

(a)

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image028.jpg' | relative_url }})  
(b) 

Pass object to all operation option; (a) Before passing and (b) After passing

**Pass All objects to Next operation** : Using this option All objects and their data can be transferred to the next operation.

**Pass All objects to All operations** : Using this option All objects and their data can be transferred to all operations.

  
**Delete Object:** Using this option user can delete the selected object in any particular operation. (See  Fig. 6.1.17.)

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image029.jpg' | relative_url }})

Delete object option

  
For more details on connecting operations and passing objects across operation refer the [6.1.1. Connecting Operations.](/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_6_operations_management/6_6_1_connecting_operations/)

**Set As Primary Die** : Using this user can set object as Primary die.

After setting the object as primary die, user can see an arrow mark before the object name in operation editor for particular operation as shown in Fig. 6.1.18.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image030.jpg' | relative_url }})

Set as primary Die

## Operation Tree

The purpose of this tree is to provide the user with a systematic list of required data for a given simulation. The data in the list is edited in the setting modification window. The data that is being edited is controlled by the current active position within the operation tree. The structure of the program will progress directly down this list by clicking next in Property Editor region. Alternatively, if any data needs to be modified, clicking on given item in the list will allow that item to be edited in the property editor region. 

Operation tree (See Fig. 6.1.19.) contains list of required data like geometry, mesh, boundary conditions, movement controls of an object, process type and simulation controls etc. The tool bar below the object tree is used to switch on or off the object, geometry, mesh and contacts display.

  
![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image031.jpg' | relative_url }})

Operation Tree

**Operation Tree Tool bar options**

**[2D][3D]:**

**Show Object![]({{ '/assets/icons/pre_icons/mo_show_obj_icon.jpg' | relative_url }}) :** Turns on/off the selected object from object tree.

**Show Mesh![]({{ '/assets/icons/pre_icons/mo_show_mesh_icon.jpg' | relative_url }}) :** Shows or hides mesh of the selected object from object tree.

**Show Geometry![]({{ '/assets/icons/pre_icons/mo_show_geo_icon.jpg' | relative_url }}) :** Shows or hides geometry of the selected object geometry from the object tree.

**Show Contact Nodes:![]({{ '/assets/icons/pre_icons/mo_show_cotact_icon.jpg' | relative_url }}) **Turns on the contact display for the selected object from object tree with all other all object. (See Fig. 6.1.21.)

  
**[3D]:**

**Make Transparent![]({{ '/assets/icons/pre_icons/mo_transparent.jpg' | relative_url }}) :** Turns on/off transparency of the selected object from the object tree.

**Show Backface![]({{ '/assets/icons/pre_icons/mo_show_backfac_icon.jpg' | relative_url }}) :** Turns on/off the back surface of the object selected object from the object tree, it will be more useful when the object are made transparent. (See  Fig. 6.1.20.)

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image032.jpg' | relative_url }}) ![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image033.jpg' | relative_url }})

  
(a) (b)

Plastic object mesh in shaded rendering type; (a) With Back face on (b) With Back face off

**[2D][3D]:**  
**Object Display Modes:** DEFORM has 3 different object display modes as shown in Fig. 6.1.19.

**Single Object mode![]({{ '/assets/icons/pre_icons/mo_show_single_obj_icon.jpg' | relative_url }}) :** Only the selected object from object tree is displayed. All other objects are hidden.

**Multi Object mode**![]({{ '/assets/icons/pre_icons/mo_show_multi_obj_icon.jpg' | relative_url }}) : All objects are displayed in graphics window. The selected object from object tree is displayed in solid color and all other objects are transparent in 3d mode. (See Fig. 6.1.21.)

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image034.jpg' | relative_url }})

Multi object mode when plastic workpiece object get selected

  
**User Object mode**![]({{ '/assets/icons/pre_icons/mo_show_user_defined_obj_icon.jpg' | relative_url }}) : User can toggle the object's Display, Geometry, Mesh, Transparency (only for 3D), Slice plane (only for 3D) modes independently. This can be done by checking and unchecking respective check boxes as shown in Fig. 6.1.22.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image035.jpg' | relative_url }})

User defined Object Mode window

  
Following are the settings we have to select based on the objects display requirements,

**Apply Display options**![]({{ '/assets/icons/pre_icons/mo_apply_display_option.jpg' | relative_url }}) : Applies the selected display option for the objects.

**Visible**![]({{ '/assets/icons/pre_icons/mo_visible.jpg' | relative_url }}) : Turns on/off the selected object display.

**Mesh**![]({{ '/assets/icons/pre_icons/mo_mesh_icon.jpg' | relative_url }}) : Shows or hides display of the selected object mesh.

**Geometry**![]({{ '/assets/icons/pre_icons/mo_geometry _icon.jpg' | relative_url }}) : Shows or hides display of the selected object geometry.

**Transparency![]({{ '/assets/icons/pre_icons/mo_transparent.jpg' | relative_url }})** : Turns on/off transparency of the selected object.

**Slice**![]({{ '/assets/icons/pre_icons/mo_slice.jpg' | relative_url }}) : Turns on/off sliced plane for the selected sliced object.

**Object Tree Right Mouse button (RMB) options**

By using the RMB on Object or its Geometry branches in object tree user will get few options to export the geometry or control the object display.

By RMB click on the Object any particular object branch (![]({{ '/assets/icons/pre_icons/mo_plastic_workpiece_branch.jpg' | relative_url }})) user can export the geometry, turn on the contact nodes display, make the 3d objects transparent and turn on the 3d objects back face display as shown in Fig. 6.1.23. below. Geometry inside mark for 2d and Geometry normal vectors for 3d display can be activated by RMB option on ![]({{ '/assets/icons/pre_icons/mo_geometry_branch.jpg' | relative_url }})(Geometry branch) as shown in Fig. 6.1.24. For more details on Enable contact nodes and Show backface options refer operation tree tool bar options.

  
![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image036.jpg' | relative_url }}) ![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image037.jpg' | relative_url }})

  
(a) (b)

Operation tree Object RMB options; (a) For 2D (b) For 3D

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image038.jpg' | relative_url }})![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image039.jpg' | relative_url }})  
  
(a) (b)

Operation tree Geometry RMB options; (a) For 2D (b) For 3D

## Property Editor

As the project is being constructed most of the information is specified in the Property Editor (See Fig. 6.1.1.) like Geometry, Mesh , Boundary conditions, Material, Simulation control etc. By clicking ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) in the window, it allows user to traverse the project list in order. Each window will have an effect on how the simulation performs so, care must be taken on each window. For detail information on editing varies properties of an object and operation setup, please refer [Basic forming operation setup](/docs/sk/operation_templates/33_forming/33_introduction_to_forming/).

## Message tab

In Pre mode message tab display the preprocessing setup (data definitions) information related to geometry checking output, mesh generation, mesh checking, Database check and generation messages. (See Fig. 6.1.25.)

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image040.jpg' | relative_url }})

MO Pre Mode Message tab

## Step Editor

Step editor is used after the simulation of project to modify operation setup from any of the intermediate saved steps and continue the simulation from there on. It displays all saved steps in the database. User can select the step at which operation needs to be edited., database needs to be generated and simulate to reflect the modifications. (See Fig. 6.1.26.)

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image041.jpg' | relative_url }})

Step editor tab

  
User can use the below listed step selection options for selecting the step easily,

![]({{ '/assets/icons/pre_icons/mo_outline_button.jpg' | relative_url }}) : When selected displays only the first and last step of the operations in the step editor

![]({{ '/assets/icons/pre_icons/mo_auto_button.jpg' | relative_url }}): When selected displays only first, last and one intermediate saved step of the operations in the step editor.

![]({{ '/assets/icons/pre_icons/mo_brief_button.jpg' | relative_url }}): When selected displays steps that are selected by system automatically for display in the step list.

![]({{ '/assets/icons/pre_icons/mo_all_button.jpg' | relative_url }}) : When selected displays all saved steps of the all operations in the step editor.

![]({{ '/assets/icons/pre_icons/mo_step_list.jpg' | relative_url }}) : This will provide more detailed information of all saved steps like Simulation  
number, Mesh number, Time, Stroke of primary die, Dimension, Version number and Fold (for 3D). It also list the operations sequence on the left side window and provides more step selection option on right side window.

It provides user defined step selection option in addition to the all above listed step selection options, selecting this will activates few advanced step selection types style and range. (See Fig. 6.1.27.).

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image042.jpg' | relative_url }})

Step List step selection options

  
**Style options:**

The selection method for the step list to be displayed in the Post-Processor.

  * **All Steps**

All steps will be selected for use in the Post-Processor.

  * **None**

No steps are selected for use in the Post-Processor.

  * **Operation Start /End Step**

Selects the starting and the end step of the increment range when no other steps are selected.

  * **Remeshing**

Toggle Remeshing will select/deselect the remeshing steps from the step list for use in the Post-Processor.

  * **Start Step**

The starting step for the increment range.

  * **End Step**

The ending step for the increment range.

**Range options:**

  * **Increment:** This will select saved steps for display, but the increment will be across the saved steps. For example: An Increment value of 5 in Increment Saved mode will select 1 step for every 5 saved steps between the starting and ending step for inclusion into the Post-Processor display.

  * **Number of steps:** The number of steps specified here will be used for the saved step Increment selection. Depending upon the no. of steps specified, the saved steps to be displayed or highlighted.

Huge database can be purged into small one based on the user requirement using Database purge tab. It is necessary that user must select all the negative steps (operation starting steps and remeshing steps), first step and last step of simulation in addition to the important steps to purge. (See Fig. 6.1.28.)

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image043.jpg' | relative_url }})

Database purging window

## Graphics window

Graphics window displays the graphical representation of the objects. It can be used for displaying the geometry and mesh information of the simulation objects in pre mode. (See Fig. 6.1.1.)

**Graphics window RMB options** : Right mouse click in pre mode graphics window will provide options as shown in Fig. 6.1.29.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image044.jpg' | relative_url }}) ![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image045.jpg' | relative_url }})

(a) (b)

Right mouse button graphics window options; (a) For 2D (b) For 3D

**DB Info** : It display the name of the database at the top left corner in the graphics window.

**Title** : It display the current operation name at the top left corner in the graphics window.

**Show Ruler** : Using this user can turn on/off the ruler display in the display window.

**Show Dimensions :** Display the maximum dimensions of the object in X and Y directions in 2D and in X, Y and Z directions in 3D.

**Show Center line [2D]:** It display the center axis line for Axisymmetric or Torsion geometry type in the graphics window.

**Show Origin Axis [3D]:** Using this user can turn on/off the origin axis display in the display window.

**Show current object mark** : This shows the mark in graphics display at the top and bottom corners for the **selected objects from object tree**. This will be more helpful in multiple object mode display when there are many objects in a setup. (See Fig. 6.1.21.)

**Show Current Object mark** : This shows the mark at the top and bottom plane four corners of the 3D object and top and bottom plane two corners of the 2D object in multiple and user object modes indicating that object is the current selected object in the object tree, so for that object user can define the data from the data definition window and also help while positing the objects by showing these marks for the selected positioning object.

**Show View Axis:** It display the 2D or 3D axis at right bottom corner in the graphics window as shown in Fig. 6.1.30.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image047.jpg' | relative_url }}) ![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image049.jpg' | relative_url }}) ![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image048.jpg' | relative_url }})

(a) (b) (b)

Axis display in graphics window; (a) For 2D Plane strain and plane stress (b) For 2D Axisymmetric and Torsion mode (c) For 3D

**Refresh** : Refreshes the Graphical Display Area.

**Fit View** : Fits all displayed objects or graphs inside the current View port.

**View Back** : Resets objects to the previously viewed display position.

**Auto fit** : This option is used to automatically fit the view of the object (s) as per the selection.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image046.jpg' | relative_url }})

Auto fit options

**Load and Save Viewport** : The user can move or change the views of the geometries by using display tools such as pan, dynamic zoom and box zoom in the display window. These views can be saved using save option (See Fig. 6.1.32a) provided under viewport tab. If the view is saved as a local viewport, this view gets saved for the current working project only and can be viewed using load option as shown in Fig. 6.1.32b.  
If the view is saved as a global viewport the set views are available for any database or a key file, for global viewports to get activated for the projects, the user has to exit from current project.

The user can copy global viewports as a local viewports under load option and local viewports to global viewports under save option.

  
![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image050.jpg' | relative_url }}) ![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image051.jpg' | relative_url }})

(a) (b)

Load and Save viewport options; (a) Lod viewport (b) Save viewport

  
**Object display mode** : Using this user can control the object display in graphics window, there are three types of object display modes, those are single Multi and user defined object display modes. Refer to Object display mode explanation under Operation Tree for more details.

**Contact display:** Using this user can turn on/off the inter-object contact nodes display. (See[ Fig. 6.1.33.](6_1_integrated_manufacturing_process_preprocessor_layout.htm#Fig._6.1.33._Contact_display_turn_on/off_options))

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image052.jpg' | relative_url }})

Contact display turn on/off options

**Calculate Contact Area** : Shows the contact objects contact area information.  
**Measurement style:** This option gets activate only when ![]({{ '/assets/icons/pre_icons/mo_measure_tool_icon.jpg' | relative_url }}) icon (Measurement tool) is selected. Using this tool user can measure the distance between two points in the linear (X,Y or Z direction) and angular directions (XYZ direction) in CAD style. (See Fig. 6.1.34.)

  
![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image053.jpg' | relative_url }}) ![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image054.jpg' | relative_url }})

  
(a) (b)

Right mouse button measurement style options; (a) For 2D (b) For 3D

  
**Measurement options:** Measure option available are clear, to clear last , Change color text , change Line color and Background color options as show in Fig. 6.1.35.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image055.jpg' | relative_url }})

Right mouse button measurement options

  
**Picking Sensitivity:** Using this user can select the sensitivity of picking the nodes and elements of the object and points on the object or anywhere in the display window. There are five levels of sensitivities Super fine Fine, Normal, Coarse and Rough (See Fig. 6.1.36.). If user wants to pick precisely then Fine picking is preferred otherwise default Normal picking is enough. If the user wants to select the nodes or elements near the picking point on the object then Coarse picking is preferred.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image056.jpg' | relative_url }})

Picking Sensitivity option

  
**Background Theme** : Using this option user can select the different background themes available like Navy blue, White, Black and Gray for the graphics window as shown in Fig. 6.1.37.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image057.jpg' | relative_url }})

Right mouse button background themes options

**Display Options** : Using this option (See Fig. 6.1.38.) user can select the point or polygon type display of the selected contact node. Also can select point size under Point size list.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image058.jpg' | relative_url }})

Right mouse button selected nodes display options

After turning on the contact display user can select point or polygon type display option, 2d example with point and polygon contact node display is shown in Fig. 6.1.39.

![]({{ '/assets/images/integrated_manufacturing_process_setup/6_1_integrated_manufacturing_process_preprocessor_layout/6_1_image059.jpg' | relative_url }})

2D Point and polygon contact nodes display example

  
**Feature Angle (3D)** : User can use this option to change the range of selection when selecting the elements/nodes/polygons for adding BCC or editing geometry etc using surface patch method. It displays the surface patch by treating surfaces within the feature angle as the one surface. A curved surface with smaller feature angle means fewer surface polygons will be picked at a time. For more information refer 8. Pre-processor [Feature Angle](../../pre_processor/8_pre_processor_layout/8_pre-processor_layout.htm#Change_feature_angle)

## Tool Bar Options

Tool bar options has been explained in [section 6.4.4. Tool bar options](6_4_main_menu.htm#Tool_bar_options), hence please refer that section for more details.

**Related Topics:**

[Material data](/docs/sk/pre_processor/10_material_data/10_material_data/)

[Expert mode Simulation Controls settings](/docs/sk/pre_processor/9_simulation_controls/9_simulation_controls/)

[Geometry Definition](/docs/sk/pre_processor/12_geometry_modelling/12_geometry_modelling/)

[Mesh definition](/docs/sk/pre_processor/13_mesh_generation/13_mesh_generation/)

[Boundary condition definitions](/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/)

[Movement controls](/docs/sk/pre_processor/15_movement_controls_definition/15_movement_controls_settings/)

[Object properties definitions](/docs/sk/pre_processor/16_object_properties/16_object_properties/)

[Object Positioning](/docs/sk/pre_processor/19_object_positioning/19_object_positioning/)

[Inter-Object data definitions](/docs/sk/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/)

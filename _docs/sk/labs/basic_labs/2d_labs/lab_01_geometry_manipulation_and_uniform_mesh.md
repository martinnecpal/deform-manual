---
lang: sk
title: "Lab 01 Geometry Manipulation and Uniform mesh"
---

# Lab 01 Geometry Manipulation and Uniform mesh

  
1.1. Creating a New problem

1.2. Adding Forming operation

1.3. Selecting Geometry Type

1.4. Adding Object

1.5. Workpiece

1.6. Creating Workpiece geometry

1.7. Workpiece mesh page

## Creating a New problem

On a **Windows machine** , go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** vxx.xx from the menu. The DEFORM GUI Main window will appear, as shown below.(See Fig. L1.1.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0001.jpg' | relative_url }})

DEFORM GUI main window

Create a new problem either by selecting **File** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})**New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in Fig. L1.2. Select "**Integrated Manufacturing Process** " radio button and unit system as "**English** " radio button in unit field. Define Problem Name as " **Mesh** " and make sure the “**Show option dialog** ” check box is turned on (if we do not turn on the “Show option dialog” check box, then we will not get the New Project dialog). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0002.jpg' | relative_url }})

Problem type selection window

Multiple operation wizard will open with the New Project dialog (See Fig. L1.3.), at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session we use ‘**Mesh** ’ as the project name.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0003.jpg' | relative_url }})

MO wizard New project

User can also change the Unit system and add operation by selecting from First operation pull down list and checkbox (See Fig. L1.4.). Using copy Existing project option we can import previous saved projects as new project. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation. 

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0004.jpg' | relative_url }})

New project window settings

## Adding Forming operation

Multiple Operation wizard will opens new project. Add 2D Forming operation from the Explorer Operations list. Operation can be add by clicking on 2D Forming operation ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button (See Fig. L1.5.) or user can also add by drag and drop into the Operation Editor.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0005.jpg' | relative_url }})

Added 2D Forming operation into Operation Editor

## Selecting Geometry Type

In this lab we are using Axisymmetric geometries, so activate 2D Axisymmetric radio button in geometry type page, then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Object page.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0006.jpg' | relative_url }})

Axisymmetric Geometry type selection

## Adding Object

In this lab we need only one object, if already there are three objects in object list, then delete the last two objects by clicking ![]({{ '/assets/icons/pre_icons/mo_delete_object_button.jpg' | relative_url }}) object button and keep only Workpiece object in list (See Fig. L1.7.), then click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0007.jpg' | relative_url }})

Adding Object Window

## Workpiece

In Workpiece window, change the Object name to **Billet** and select Object type as **Plastic** as shown in Fig. L1.8., Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0008.jpg' | relative_url }})

Billet object Window

## Creating Workpiece geometry

In DEFORM-2D, the surface definition of an object is referred to as it's geometry. An object's geometry can either be created within DEFORM or it can be imported as a .dxf or .igs file. In this lab, the geometry of the billet will be created within DEFORM.

In Geometry page click on ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}) label and observe the options available to create and modify the geometry (See Fig. L1.9.),

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0009.jpg' | relative_url }})

Edit Geometry window

**Select**![]({{ '/assets/icons/pre_icons/mo_click_select.jpg' | relative_url }}) :**** Select Tool is used to select the vertex or Edge of the geometry. Using this vertex or edge can be positioned by drag and drop.

**Area select** ![]({{ '/assets/icons/pre_icons/mo_area select.jpg' | relative_url }}) : Area Select tool is used to select the geometry more than one entity within a box.

**Create Loop** ![]({{ '/assets/icons/pre_icons/mo_create_loop.jpg' | relative_url }}) : Create Loop tool is used to create the geometry loop by creating points and connecting them. 

**Add Point to Loop** ![]({{ '/assets/icons/pre_icons/mo_add_points_to_loop.jpg' | relative_url }}) : Add Point Loop tool is used to add the new points to an existing loop.

**Delete Point** ![]({{ '/assets/icons/pre_icons/mo_delete point.jpg' | relative_url }}) : Delete Point tool is used to delete the point in the loop.

**Round corner**![]({{ '/assets/icons/pre_icons/mo_round_corner.jpg' | relative_url }}) : Round Corner tool is used to create fillet at selected point.

**Set angle** ![]({{ '/assets/icons/pre_icons/mo_set_angle.jpg' | relative_url }}): is used to change the angle of edge.

**Move**![]({{ '/assets/icons/pre_icons/mo_move.jpg' | relative_url }}) : is used to move the point.

**Move to centerline![]({{ '/assets/icons/pre_icons/mo_move_to_centerline.jpg' | relative_url }}) **: is used to move the loop nearest point to centerline

**Offset** ![]({{ '/assets/icons/pre_icons/mo_offset.jpg' | relative_url }}) : Offset tool is used to resize the geometry loop.

**Make First point** ![]({{ '/assets/icons/pre_icons/mo_make_first_point.jpg' | relative_url }}) : Make First Point tool is used to make the selected point as first point in a loop, this will be used for closed loop and we cannot make an arc mid point as first point.

**Reverse direction** ![]({{ '/assets/icons/pre_icons/mo_reverse_direction.jpg' | relative_url }}) : Reverse direction is used to reverse the direction of loop to change the orientation of the geometry. The geometry should be create in Counter clockwise, if the geometry is created in clockwise, using this option we can change the direction of loop.

**Close loop**![]({{ '/assets/icons/pre_icons/mo_close_loop.jpg' | relative_url }}) : Closed loop tool is used to close the open loop

**Split loop**![]({{ '/assets/icons/pre_icons/mo_split_loop.jpg' | relative_url }}) : Split loop tool is used to split the loop at selected point

**Sub loop**![]({{ '/assets/icons/pre_icons/mo_sub_loop.jpg' | relative_url }}) : Sub loop tool is used to select a inner loop as sub loop in case of multi loops topology, by selecting this we can assign the material for a multiple loop geometry

**Join loops** ![]({{ '/assets/icons/pre_icons/mo_join_loop.jpg' | relative_url }}) : join loops option is used to merge the 2 loops by selecting the loops to be joined, the end point of first loop will be joined to first point of the second loop

**Join all loops** ![]({{ '/assets/icons/pre_icons/mo_join_all_loops.jpg' | relative_url }}) : Join all loops tool is used to merge all loops.

**Delete selected** ![]({{ '/assets/icons/pre_icons/mo_delete_selected.jpg' | relative_url }}) : Delete selected is used to delete the selected loops or edges.

**Delete unselected** ![]({{ '/assets/icons/pre_icons/mo_delete_unselected.jpg' | relative_url }}) : Delete unselected is used to delete the unselected loops edges.

**Show Vertex** ![]({{ '/assets/icons/pre_icons/mo_show_vertex.jpg' | relative_url }}) : is used to display the vertexes of the geometry.

**Show Vertex numbers** ![]({{ '/assets/icons/pre_icons/mo_show_vertex_numbers_icon.jpg' | relative_url }}) : is used to display the vertexes number of the geometry.

**Show Inside**![]({{ '/assets/icons/pre_icons/mo_show_inside.jpg' | relative_url }}) : is used to show the orientation of the geometry.

**Show Edge direction** ![]({{ '/assets/icons/pre_icons/mo_show_edge_direction.jpg' | relative_url }}) : is used to plot the direction of loop created.

**Show Material** ![]({{ '/assets/icons/pre_icons/mo_material_icon.jpg' | relative_url }}) : is used to load and assign the material to the geometry region.

**Grid Lines** : It shows the Grid Lines in Horizontal and Vertical direction in Display window. 

**Grid Points** : It shows the Grid Points in Horizontal and Vertical direction in Display window.

**Grid None** : When this option is selected, the Grid points and Grid Lines in Horizontal and Vertical direction are not displayed in Display window.

Under **Objects** tab, we can select the object in list to hide the selected object geometry in graphical display window.

Under **Geometry** tab, we can enter or modify the geometry entities. Geometry entities can be enter in two methods, in Line-Arc method and XYR methods.

Under the **l****oop** tab, we can load and assign the material to the selected loops. Also we can see the assigned material to the corresponding loop details.

in this lab we will create a geometry by enter the following XYR coordinates value in the Table.1. (see Fig. L1.10.) and click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}).

X |  Y |  R  
---|---|---  
0 |  0 |  0  
1.5 |  0 |  0.12  
1.5 |  4 |  0.12  
0 |  4 |  0  
  
Geometry XYR coordinates value

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0010.jpg' | relative_url }})

2D Edit Geometry page

Then click on ![]({{ '/assets/icons/pre_icons/mo_check_label.jpg' | relative_url }}) button, Use the default checking parameters and click ![]({{ '/assets/icons/pre_icons/mo_check_and_correct_geo_button.jpg' | relative_url }}) as shown in Fig. L1.11. A message saying, "Geometry is legal" will appear. then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) and click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0011.jpg' | relative_url }})

Check and Correct Geometry window

## Workpiece mesh page

Switch to Expert mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) (Switch to expert mode) icon. Expert mode will provide more options for detailed settings.

### Generating mesh for Default settings

Using default mesh settings, (Size ratio 3 and Number of elements 1000), generate the mesh by clicking on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button as shown in Fig. L1.12.

The Size Ratio determines the difference between the smallest and largest element. A ratio of 3 allows the smallest element to be 1/3 the size of the largest element. The Weighting Factors determine where the small and large elements are placed in the object.

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0012.jpg' | relative_url }})

Mesh generated for Size ratio 3

### Generating uniform mesh

To create a uniform mesh on an object, where all the elements are the same size, set the Size Ratio to 1 and click ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) again. (See Fig. L1.13.)

![]({{ '/assets/images/labs/basic_labs/2d_labs/lab_01_geometry_manipulation/image0013.jpg' | relative_url }})

Mesh generated for Size ratio 1

**Note** : It is important to know that all information about the old mesh will be lost when a new mesh is generate.

**Related Topics:**

[12.2. 2D Geometry Data Editing](/docs/sk/pre_processor/12_geometry_modelling/12_2_2d_geometry_editing/)

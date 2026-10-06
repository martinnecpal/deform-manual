---
lang: en
title: "14. Boundary Conditions"
---

# 14\. Boundary Conditions [BCC]

Boundary conditions specify how the boundary of an object interacts with other objects and with the environment. The most commonly used boundary conditions are heat exchange with the environment for simulations involving heat transfer, prescribed velocity for enforcing symmetry or prescribing movement in problems such as drawing where a part is pulled through a die, shrink fit for modelling shrink rings on tooling, prescribed force, for die stress analysis and Contact between objects in the model. Some of the boundary condition definitions have been changed from a node based definition to an element edge-based definition. 

![]({{ '/assets/images/pre-processor/14_boundary_conditions/14_image001.jpg' | relative_url }})

(a)

![]({{ '/assets/images/pre-processor/14_boundary_conditions/14_image002.jpg' | relative_url }})

(b)

Object boundary condition window; (a) For 2D (b) For 3D

The purpose for changing from a node-based definition to an edge-based definition is to reduce ambiguity at corners. If heat exchange with environment is defined on an edge and heat flux is set to zero at an adjacent edge there is an ambiguity at the corner. If the corner node is set to heat exchange with the environment, then the definition at the edge with one heat exchange BC and one heat flux BC is not clearly defined. The purpose of the edge definition is to eliminate this problem in any case where the boundary condition acts over the length of an element edge such as pressure, heat flux and atomic diffusion from the environment.

**Defining object boundary conditions**

Boundary conditions are specified and enforced at nodes or element edges in the finite element mesh. The basic procedure for setting any boundary condition except Contact is the same:

  1. Select the appropriate condition type.
  2. Select the direction (where applicable).
  3. Select the nodes to which boundary conditions will be applied using one of the selection tools in the lower left button bar. (See Fig. 14.1.)
  4. Apply the boundary conditions

The selected nodes will be highlighted. To apply the boundary conditions click the ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) button. Colored markers will highlight the nodes to which boundary conditions have been applied. To delete specific boundary conditions, select the start and end nodes, and click the ![]({{ '/assets/icons/pre_icons/mo_delete_bcc_button.jpg' | relative_url }}) button. To delete all boundary conditions of the specified type and direction, click the ![]({{ '/assets/icons/pre_icons/mo_initialize_button.jpg' | relative_url }}) button.

Note :

You can either select faces of the surface by using the surface patches feature or use the node button to select individual nodes.

**Picking option for 2D object are:**

**Start & end point **![]({{ '/assets/icons/pre_icons/mo_bcc_start_and_end_ico.jpg' | relative_url }}) : By selecting two consecutive points, the first being the starting point and the second being the ending point, a counter-clockwise set of boundary nodes are selected.

**By edge****![]({{ '/assets/icons/pre_icons/mo_bcc_edge_icon.jpg' | relative_url }})** : By using this option, various edges are selected on the two-dimensional shape. If the shape is sufficiently curved, the entire boundary is selected.

**One by one**![]({{ '/assets/icons/pre_icons/mo_bcc_one_by_one_icon.jpg' | relative_url }}) : Clicking this icon will select individual nodes.

**Window** : Below are the 2D windows options are used to select the region by defining windows.

**Polygon**![]({{ '/assets/icons/pre_icons/mo_2d_polygon_window_icon.jpg' | relative_url }}) , **Rectangle**![]({{ '/assets/icons/pre_icons/mo_2d_rectangle_window_icon.jpg' | relative_url }}) and **Circle**![]({{ '/assets/icons/pre_icons/mo_2d_circle_window_icon.jpg' | relative_url }}) **[2D]** options are used for to select BCC region for 2D.

**Add****a****point**![]({{ '/assets/icons/pre_icons/mo_2d_add_point_button.jpg' | relative_url }}) : Using this option user can add points to define BCC window.

**Delete****a****point**![]({{ '/assets/icons/pre_icons/mo_2d_delete_point_button.jpg' | relative_url }}) : Using this option user can delete points of a defined BCC window.

**Relocate****point**![]({{ '/assets/icons/pre_icons/mo_2d_relocate_point_button.jpg' | relative_url }}) : Using this option user can relocate points of a defined BCC window.

**Modify**![]({{ '/assets/icons/pre_icons/mo_edit_window_icon.jpg' | relative_url }}) : Using this option user can modify the previously defined BCC window.

**Select All**![]({{ '/assets/icons/pre_icons/mo_select_all_icon.jpg' | relative_url }}) : Clicking this icon will select every node on the boundary of the part.

**Deselect All** :![]({{ '/assets/icons/pre_icons/mo_clear_icon.jpg' | relative_url }}) Clicking this icon will deselect every node on the boundary of the part.

**Picking option for 3D object are:**

**S******u** rface Patch **![]({{ '/assets/icons/pre_icons/mo_bcc_surface_patch_icon.jpg' | relative_url }}): This option is used to select the surface patch of the object.

**Plane![]({{ '/assets/icons/pre_icons/mo_bcc_plane_icon.jpg' | relative_url }})** : This option selects the plane of the object.

**One by one** ![]({{ '/assets/icons/pre_icons/mo_bcc_one_by_one_icon.jpg' | relative_url }}): Clicking this icon will select individual nodes.

**Window** : Below Windows options are used to select the region by defining windows.

**Box![]({{ '/assets/icons/pre_icons/mo_box_window_icon.jpg' | relative_url }})** , **Cylinder![]({{ '/assets/icons/pre_icons/mo_cylinder_window_icon.jpg' | relative_url }})** , **Ring![]({{ '/assets/icons/pre_icons/mo_hollow_cylinder_icon.jpg' | relative_url }}) **and **Polygon![]({{ '/assets/icons/pre_icons/mo_polygon_window_icon.jpg' | relative_url }}) [3D] **window options are used to select BCC region for 3D. 

**Modify**![]({{ '/assets/icons/pre_icons/mo_edit_window_icon.jpg' | relative_url }}) : Using this option user can modify the previously defined BCC window.

![]({{ '/assets/icons/pre_icons/mo_add_icon.jpg' | relative_url }}), ![]({{ '/assets/icons/pre_icons/mo_delete_icon.jpg' | relative_url }}), ![]({{ '/assets/icons/pre_icons/mo_toggle_button.jpg' | relative_url }}), ![]({{ '/assets/icons/pre_icons/mo_assign_button.jpg' | relative_url }}) are add, delete, toggle and assign window options respectively.

**Select All**![]({{ '/assets/icons/pre_icons/mo_select_all_icon.jpg' | relative_url }}) : Clicking this icon will select every node on the boundary of the part.

**Deselect All** :![]({{ '/assets/icons/pre_icons/mo_clear_icon.jpg' | relative_url }}) Clicking this icon will deselect every node on the boundary of the part.

To apply the boundary conditions click the ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}) button. Colored markers will highlight the edges to which boundary conditions have been applied. To delete specific boundary conditions, select the start and end nodes, and click the ![]({{ '/assets/icons/pre_icons/mo_delete_bcc_button.jpg' | relative_url }}) button. To delete all boundary conditions of the specified type and direction, click the ![]({{ '/assets/icons/pre_icons/mo_initialize_button.jpg' | relative_url }}) button.

Note:

If parallel symmetry planes are to be defined, velocity boundary conditions can only be used on one plane. A rigid surface should be defined on the other.

**The**Boundary conditions** are categorized as**:

  * **Symmetry Boundary conditions****[3D]** : where Symmetry BCC options are available for 3D object. For more information related to Symmetry Boundary conditions options refer section [14.1. Symmetry Boundary Conditions]({{ '/docs/en/pre_processor/14_boundary_conditions/14_1_symmetry_boundary_conditions/' | relative_url }})
  * **Deformation**Boundary conditions**[2D, 3D]**: where Velocity BCC, Pressure BCC, Force BCC, Movement ****BCC, Contact BCC, Beginning surface****BCC, Free surface BCC, Rolling BCC and Advanced Deformation BCC options are available. For more information related to Deformation Boundary conditions options******** refer section [14.2. Deformation Boundary Conditions]({{ '/docs/en/pre_processor/14_boundary_conditions/14_2_deformation_boundary_conditions/' | relative_url }})
  * **Thermal**Boundary conditions**[2D, 3D]**: where Heat exchange with Environment BCC, Temperature BCC, Heat BCC, Heat flux BCC and Advanced Thermal BCC options are available. For more information related to Thermal Boundary conditions options refer section [14.3. Thermal Boundary Conditions]({{ '/docs/en/pre_processor/14_boundary_conditions/14_3_thermal_boundary_conditions/' | relative_url }})
  * **Diffusion**Boundary conditions**[2D, 3D]: **where Diffusion with Environment BCC, Atom content BCC, Atom flux BCC and Advanced Diffusion BCC options are available. For more information related to Diffusion Boundary conditions options refer section [14.4. Diffusion Boundary Conditions]({{ '/docs/en/pre_processor/14_boundary_conditions/14_4_diffusion_boundary_conditions/' | relative_url }})
  * **Heating**Boundary conditions** [2D, 3D]: **where Voltage BCC, Current flux BCC, Atom content BCC, Atom flux BCC, Start Surface, End surface BCC and Heating surface BCC options are available. For more information related to Heating Boundary conditions options refer section [14.5. Diffusion Boundary Conditions]({{ '/docs/en/pre_processor/14_boundary_conditions/14_5_heating_boundary_conditions/' | relative_url }})

**Related Topics:**

[14.1. Symmetry Boundary Conditions]({{ '/docs/en/pre_processor/14_boundary_conditions/14_1_symmetry_boundary_conditions/' | relative_url }})

[14.2. Deformation Boundary Conditions]({{ '/docs/en/pre_processor/14_boundary_conditions/14_2_deformation_boundary_conditions/' | relative_url }})

[14.3. Thermal Boundary Conditions]({{ '/docs/en/pre_processor/14_boundary_conditions/14_3_thermal_boundary_conditions/' | relative_url }})

[14.4. Diffusion Boundary Conditions]({{ '/docs/en/pre_processor/14_boundary_conditions/14_4_diffusion_boundary_conditions/' | relative_url }})

[14.5. Heating Boundary Conditions]({{ '/docs/en/pre_processor/14_boundary_conditions/14_5_heating_boundary_conditions/' | relative_url }})

[2D-Geometry type selection from Simulation controls](../9_Simulation_Controls/9_1_Simulation_type_Settings.htm#9.1.2._Geometry_type_\(GEOTYP\)_\[2D\])  
[Simulations modes selections from Simulation controls](../9_Simulation_Controls/9_1_Simulation_type_Settings.htm#9.1.5._Simulation_modes_\(SMODE,_TRANS\))  
[Process conditions selection from Simulation controls](../9_Simulation_Controls/9_6_Process_Conditions.htm#Process_Conditions)  
[Object type selection from object data definition window](../11_General_Object_Data_Definition/11_General_Object_Data_Definition.htm#11.4._Object_type)  
[Assigning movement to deformable objects with Movement BCC](14_2_deformation_boundary_conditions.htm#14.2.4._Movement_BCC)  
[19\. Inter-object Data Definition]({{ '/docs/en/pre_processor/20_Inter-object_Data_Definition/20_Inter-Object_Data_Definition/' | relative_url }})  
[BCC- User routines -USRBCC](../../User_Routines/56_User_Routines_in_DEFORM/56_2_2D_User_Defined_FEM_Routines.htm#56_2_3_6_User_defined_nodal_boundary_conditions_\(USRBCC\))  
[2D Labs]({{ '/docs/en/Labs/Basic_labs/2D_Labs/2D_LABS/' | relative_url }})  
[3D Labs]({{ '/docs/en/Labs/Basic_labs/3D_Labs/3D_LABS/' | relative_url }})

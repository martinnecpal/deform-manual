---
lang: en
title: "14. Boundary Conditions"
---

# 14\. Boundary Conditions [BCC]

Boundary conditions specify how the boundary of an object interacts with other objects and with the environment. The most commonly used boundary conditions are heat exchange with the environment for simulations involving heat transfer, prescribed velocity for enforcing symmetry or prescribing movement in problems such as drawing where a part is pulled through a die, shrink fit for modelling shrink rings on tooling, prescribed force, for die stress analysis and Contact between objects in the model. Some of the boundary condition definitions have been changed from a node based definition to an element edge-based definition. 

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_Image001.jpg)

(a)

![](../../../assets/Images/Pre-Processor/14_Boundary_Conditions/14_Image002.jpg)

(b)

Object boundary condition window; (a) For 2D (b) For 3D

The purpose for changing from a node-based definition to an edge-based definition is to reduce ambiguity at corners. If heat exchange with environment is defined on an edge and heat flux is set to zero at an adjacent edge there is an ambiguity at the corner. If the corner node is set to heat exchange with the environment, then the definition at the edge with one heat exchange BC and one heat flux BC is not clearly defined. The purpose of the edge definition is to eliminate this problem in any case where the boundary condition acts over the length of an element edge such as pressure, heat flux and atomic diffusion from the environment.

**Defining object boundary conditions**

Boundary conditions are specified and enforced at nodes or element edges in the finite element mesh. The basic procedure for setting any boundary condition except Contact is the same:

  1. Select the appropriate condition type.
  2. Select the direction (where applicable).
  3. Select the nodes to which boundary conditions will be applied using one of the selection tools in the lower left button bar. (See Fig. 14.1.)
  4. Apply the boundary conditions

The selected nodes will be highlighted. To apply the boundary conditions click the ![](../../../assets/Icons/Pre_icons/MO_Add_BCC_button.jpg) button. Colored markers will highlight the nodes to which boundary conditions have been applied. To delete specific boundary conditions, select the start and end nodes, and click the ![](../../../assets/Icons/Pre_icons/MO_delete_BCC_button.jpg) button. To delete all boundary conditions of the specified type and direction, click the ![](../../../assets/Icons/Pre_icons/MO_initialize_button.jpg) button.

Note :

You can either select faces of the surface by using the surface patches feature or use the node button to select individual nodes.

**Picking option for 2D object are:**

**Start & end point **![](../../../assets/Icons/Pre_icons/MO_Bcc_start_and_end_ico.jpg) : By selecting two consecutive points, the first being the starting point and the second being the ending point, a counter-clockwise set of boundary nodes are selected.

**By edge****![](../../../assets/Icons/Pre_icons/MO_Bcc_edge_icon.jpg)** : By using this option, various edges are selected on the two-dimensional shape. If the shape is sufficiently curved, the entire boundary is selected.

**One by one**![](../../../assets/Icons/Pre_icons/MO_Bcc_one_by_one_icon.jpg) : Clicking this icon will select individual nodes.

**Window** : Below are the 2D windows options are used to select the region by defining windows.

**Polygon**![](../../../assets/Icons/Pre_icons/MO_2D_Polygon_Window_icon.jpg) , **Rectangle**![](../../../assets/Icons/Pre_icons/MO_2D_Rectangle_Window_icon.jpg) and **Circle**![](../../../assets/Icons/Pre_icons/MO_2D_Circle_Window_icon.jpg) **[2D]** options are used for to select BCC region for 2D.

**Add****a****point**![](../../../assets/Icons/Pre_icons/MO_2D_Add_point_button.jpg) : Using this option user can add points to define BCC window.

**Delete****a****point**![](../../../assets/Icons/Pre_icons/MO_2D_Delete_point_button.jpg) : Using this option user can delete points of a defined BCC window.

**Relocate****point**![](../../../assets/Icons/Pre_icons/MO_2D_Relocate_point_button.jpg) : Using this option user can relocate points of a defined BCC window.

**Modify**![](../../../assets/Icons/Pre_icons/MO_Edit_window_icon.jpg) : Using this option user can modify the previously defined BCC window.

**Select All**![](../../../assets/Icons/Pre_icons/MO_Select_all_icon.jpg) : Clicking this icon will select every node on the boundary of the part.

**Deselect All** :![](../../../assets/Icons/Pre_icons/MO_clear_icon.jpg) Clicking this icon will deselect every node on the boundary of the part.

**Picking option for 3D object are:**

**S******u** rface Patch **![](../../../assets/Icons/Pre_icons/MO_Bcc_surface_patch_icon.jpg): This option is used to select the surface patch of the object.

**Plane![](../../../assets/Icons/Pre_icons/MO_Bcc_plane_icon.jpg)** : This option selects the plane of the object.

**One by one** ![](../../../assets/Icons/Pre_icons/MO_Bcc_one_by_one_icon.jpg): Clicking this icon will select individual nodes.

**Window** : Below Windows options are used to select the region by defining windows.

**Box![](../../../assets/Icons/Pre_icons/MO_Box_window_icon.jpg)** , **Cylinder![](../../../assets/Icons/Pre_icons/MO_Cylinder_window_icon.jpg)** , **Ring![](../../../assets/Icons/Pre_icons/MO_Hollow_Cylinder_icon.jpg) **and **Polygon![](../../../assets/Icons/Pre_icons/MO_Polygon_window_icon.jpg) [3D] **window options are used to select BCC region for 3D. 

**Modify**![](../../../assets/Icons/Pre_icons/MO_Edit_window_icon.jpg) : Using this option user can modify the previously defined BCC window.

![](../../../assets/Icons/Pre_icons/MO_Add_icon.jpg), ![](../../../assets/Icons/Pre_icons/MO_Delete_icon.jpg), ![](../../../assets/Icons/Pre_icons/MO_Toggle_button.jpg), ![](../../../assets/Icons/Pre_icons/MO_Assign_button.jpg) are add, delete, toggle and assign window options respectively.

**Select All**![](../../../assets/Icons/Pre_icons/MO_Select_all_icon.jpg) : Clicking this icon will select every node on the boundary of the part.

**Deselect All** :![](../../../assets/Icons/Pre_icons/MO_clear_icon.jpg) Clicking this icon will deselect every node on the boundary of the part.

To apply the boundary conditions click the ![](../../../assets/Icons/Pre_icons/MO_Add_BCC_button.jpg) button. Colored markers will highlight the edges to which boundary conditions have been applied. To delete specific boundary conditions, select the start and end nodes, and click the ![](../../../assets/Icons/Pre_icons/MO_delete_BCC_button.jpg) button. To delete all boundary conditions of the specified type and direction, click the ![](../../../assets/Icons/Pre_icons/MO_initialize_button.jpg) button.

Note:

If parallel symmetry planes are to be defined, velocity boundary conditions can only be used on one plane. A rigid surface should be defined on the other.

**The**Boundary conditions** are categorized as**:

  * **Symmetry Boundary conditions****[3D]** : where Symmetry BCC options are available for 3D object. For more information related to Symmetry Boundary conditions options refer section [14.1. Symmetry Boundary Conditions](/docs/en/pre_processor/14_boundary_conditions/14_1_symmetry_boundary_conditions/)
  * **Deformation**Boundary conditions**[2D, 3D]**: where Velocity BCC, Pressure BCC, Force BCC, Movement ****BCC, Contact BCC, Beginning surface****BCC, Free surface BCC, Rolling BCC and Advanced Deformation BCC options are available. For more information related to Deformation Boundary conditions options******** refer section [14.2. Deformation Boundary Conditions](/docs/en/pre_processor/14_boundary_conditions/14_2_deformation_boundary_conditions/)
  * **Thermal**Boundary conditions**[2D, 3D]**: where Heat exchange with Environment BCC, Temperature BCC, Heat BCC, Heat flux BCC and Advanced Thermal BCC options are available. For more information related to Thermal Boundary conditions options refer section [14.3. Thermal Boundary Conditions](/docs/en/pre_processor/14_boundary_conditions/14_3_thermal_boundary_conditions/)
  * **Diffusion**Boundary conditions**[2D, 3D]: **where Diffusion with Environment BCC, Atom content BCC, Atom flux BCC and Advanced Diffusion BCC options are available. For more information related to Diffusion Boundary conditions options refer section [14.4. Diffusion Boundary Conditions](/docs/en/pre_processor/14_boundary_conditions/14_4_diffusion_boundary_conditions/)
  * **Heating**Boundary conditions** [2D, 3D]: **where Voltage BCC, Current flux BCC, Atom content BCC, Atom flux BCC, Start Surface, End surface BCC and Heating surface BCC options are available. For more information related to Heating Boundary conditions options refer section [14.5. Diffusion Boundary Conditions](/docs/en/pre_processor/14_boundary_conditions/14_5_heating_boundary_conditions/)

**Related Topics:**

[14.1. Symmetry Boundary Conditions](/docs/en/pre_processor/14_boundary_conditions/14_1_symmetry_boundary_conditions/)

[14.2. Deformation Boundary Conditions](/docs/en/pre_processor/14_boundary_conditions/14_2_deformation_boundary_conditions/)

[14.3. Thermal Boundary Conditions](/docs/en/pre_processor/14_boundary_conditions/14_3_thermal_boundary_conditions/)

[14.4. Diffusion Boundary Conditions](/docs/en/pre_processor/14_boundary_conditions/14_4_diffusion_boundary_conditions/)

[14.5. Heating Boundary Conditions](/docs/en/pre_processor/14_boundary_conditions/14_5_heating_boundary_conditions/)

[2D-Geometry type selection from Simulation controls](../9_Simulation_Controls/9_1_Simulation_type_Settings.htm#9.1.2._Geometry_type_\(GEOTYP\)_\[2D\])  
[Simulations modes selections from Simulation controls](../9_Simulation_Controls/9_1_Simulation_type_Settings.htm#9.1.5._Simulation_modes_\(SMODE,_TRANS\))  
[Process conditions selection from Simulation controls](../9_Simulation_Controls/9_6_Process_Conditions.htm#Process_Conditions)  
[Object type selection from object data definition window](../11_General_Object_Data_Definition/11_General_Object_Data_Definition.htm#11.4._Object_type)  
[Assigning movement to deformable objects with Movement BCC](14_2_deformation_boundary_conditions.htm#14.2.4._Movement_BCC)  
[19\. Inter-object Data Definition](/docs/en/pre_processor/20_Inter-object_Data_Definition/20_Inter-Object_Data_Definition/)  
[BCC- User routines -USRBCC](../../User_Routines/56_User_Routines_in_DEFORM/56_2_2D_User_Defined_FEM_Routines.htm#56_2_3_6_User_defined_nodal_boundary_conditions_\(USRBCC\))  
[2D Labs](/docs/en/Labs/Basic_labs/2D_Labs/2D_LABS/)  
[3D Labs](/docs/en/Labs/Basic_labs/3D_Labs/3D_LABS/)

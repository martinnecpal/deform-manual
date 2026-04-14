---
lang: en
title: "17.1. Node Data Window"
---

# 17.1. Node Data Window ![]({{ '/assets/icons/pre_icons/mo_nodal_data_icon.jpg' | relative_url }})

17.1.1. Features of the display window include in Node Data window

17.1.2. Nodal Data initializing

17.1.3. Deformation Tab

  * General Tab

  * Displacement

  * Velocity

  * Force

  * Pressure

  * Deform BCC

  * Function BCC

  * Strain(Nodal)

  * Damage(Nodal)

  * Stress(Nodal) Tab

17.1.4. Thermal Tab

  * Node Temperature

  * Heat

  * Heat flux

  * Thermal BCC

  * Boundary condition function

  * Diffusion bonding

17.1.5. Diffusion Tab

  * Atom Percentage

  * Diffusion Flux

  * Diffusion BCC

17.1.6. Electric Heating Tab

  * Electric field intensity

  * Resistance BCC

  * Current Flux

17.1.7. User Tab

17.1.8. Thermomechanical variable Tab

17.1.9. Additive Manufacturing Tab

[**2D,3D**]: The node data window displays all available information about nodes. All information can be modified and many of the variables can be plotted as shown in Fig. 17.1.1. and Fig. 17.1.2.

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_1_node_data_window/17_1_image001.jpg' | relative_url }})

2D Node Deformation - General data window

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_1_node_data_window/17_1_image002.jpg' | relative_url }})

3D Node Deformation - General data window

## Features of the display window include in Node Data window

**Node Number** : The number of the node for which information is being displayed. A node may be selected either by keying in the value or by using the select icon and mouse-picking a node.

**Highlight Node** : To highlight the selected Node in graphic display. 

**Initialize values** :![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}) icon initializes the specified variable value on nodes in the object for,

  * a particular node 
  * range of nodes 
  * Picking the nodes using pick tools (See Fig. 17.1.3. and Fig. 17.1.4.)
  * interpolation method

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_1_node_data_window/17_1_image003.jpg' | relative_url }})

Picking tools for selecting Node for 2D

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_1_node_data_window/17_1_image004.jpg' | relative_url }})

Picking tools for selecting Node for 3D

**Plot variable** :

![]({{ '/assets/icons/pre_icons/mo_preview_icon.jpg' | relative_url }}) Plots selected node state variable in shaded contour.

![]({{ '/assets/icons/pre_icons/mo_plot_vector_icon.jpg' | relative_url }}) Plots selected node state variable Vector plot.

Plot type can be changed by right mouse click option on contour bar in display window.

**Node Coordinate** :

The coordinates of the node are displayed next to the node number. The values can be modified to slightly adjust the position of nodes where boundary conditions were not properly enforced. This should be done with EXTREME caution. For features such as boundary extraction and mesh generation, the database must be saved, and the newly saved step read into the pre-processor before the adjusted coordinates can be used.

## Nodal Data initializing

We can initialize the data using two methods, Assign and Interpolation methods.

We have another two options:

**Range** : Using Range option user can define the Start node number and End node number and the variable value. After defining the parameters when user clicks on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) button the data will be initialize to the selected nodes.

**Picking** : Using picking option user can select the nodes to initialize the value. 

Related to picking options refer 14. Boundary Condition [Picking options for 2D](../14_boundary_conditions/14_boundary_conditions.htm#Picking_option_for_2D) and [Picking options for 3D](../14_boundary_conditions/14_boundary_conditions.htm#Picking_option_for_3D).

**Assign method** : ****

**Interpolation method:**

## Deformation Tab [2D, 3D]

**General Tab**

  * **Displacement (DRZ) :** Displacement ([DRZ](/docs/en/keyword_documentation/d/drz/)) stores the displacement of each node since the last remeshing. For elastic objects, a displacement may be specified for interference fits. The elastic recover of the object will cause the appropriate stress values to be developed.

  * **Velocity (URZ) :**[URZ](/docs/en/keyword_documentation/u/urz/) is the velocity components of each node.

  * **Force (FRZ) :**[FRZ](/docs/en/keyword_documentation/f/frz/) specifies the value of the constant nodal force at individual nodes.

  * **Pressure (PRZ) :**[PRZ](/docs/en/keyword_documentation/p/prz/) maintains a specified normal pressure or shear traction across the face of the elements lying between the selected boundary nodes.

  * **Deform BCC (BCCDEF) :**[BCCDEF](/docs/en/keyword_documentation/b/bccdef/) specifies the deformation boundary condition in X and Y directions.

The code values are:

**0** Node force specified

**1** X, Y, or Z component of node velocity constrained, corresponding to the X, Y or Z component of [BCCDEF](/docs/en/keyword_documentation/b/bccdef/)

**2** Constrained node tractions specified by PRZ

**3** Node movement control defined

**-n** Node is in contact with object number N.

**Note** : There is no significance to the X, Y, or Z component of contact. Contact values are stored in the first free component, starting with Z, then Y, then X.

  * **Function BCC (BCCDFN)** : [BCCDFN](/docs/en/keyword_documentation/b/bccdfn/) specifies if the value of a deformation boundary constraint (nodal velocity, force, or traction) associated with a particular node is to be specified as a constant or as a set of time/nodal value data.

  * **Strain(Nodal)** : Strain (nodal) specifies the value of the Strain at individual nodes.

  * **Damage(Nodal)** : Strain (nodal) specifies the value of the Strain at individual nodes.

**Note** :

To activate Strain(Nodal), Damage(Nodal) and Stress (nodal) data, we have to activate Damage Element+Node output radio button, Strain Element+Node output radio button and Stress Element+Node output radio button under Simulation control [Advanced output](../9_simulation_controls/9_7_advanced_options.htm#9.7.4._Output_Control) tab.

  
******Stress(Nodal) Tab**  
Stress stores the stress for each node since the last remeshing. The stress values can be initialized here for a particular node or set of nodes. Values for X/R, Y/Z, Z/Theta, XY/RZ are entered by clicking on initialize button to calculate Max.principal stress and Min.principal stress for a particular node. This is more useful once the simulation as completed, so that principal stress can be checked for each node either by selecting the node number or just clicking on a particular node of the object as shown in Fig. 17.1.5. and Fig. 17.1.6.

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_1_node_data_window/17_1_image005.jpg' | relative_url }})

Nodal Deformation Stress data window for 2D 

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_1_node_data_window/17_1_image006.jpg' | relative_url }})

Nodal Deformation Stress data window for 3D 

## Thermal Tab

**[2D, 3D]** : All the nodal thermal data of the model can be examined, defined or initialized from this dialog. (See Fig. 17.1.7.)

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_1_node_data_window/17_1_image007.jpg' | relative_url }})

2D Nodal Thermal data window

  * **Node Temperature (NDTMP) :**[NDTMP](/docs/en/keyword_documentation/n/ndtmp/) specifies the nodal temperature to be applied to individual nodes.

  * **Heat (NDHEAT) :**[NDHEAT](/docs/en/keyword_documentation/n/ndheat/) specifies the nodal heat to be applied to individual nodes.

  * **Heat flux (NDFLUX) :**[NDFLUX](/docs/en/keyword_documentation/n/ndflux/) specifies the distributed nodal heat flux to be applied to individual nodes. The heat flux constraint will be applied to the element faces lying between the selected boundary nodes.

  * **Thermal BCC (BCCTMP) :**[BCCTMP](/docs/en/keyword_documentation/b/bcctmp/) specifies the heat transfer boundary constraint code for individual nodes.

  1. Constant nodal temperature is specified
  2. Heat transfer with environment boundary condition
  3. Specified nodal heat flux

  * **Boundary condition function (BCCTFN) :** [BCCFNC](/docs/en/keyword_documentation/b/bccfnc/) is used to specify time/nodal value pairs for nodal boundary constraints. Types of nodal boundary constraints that can be specified as time/nodal value pairs include velocity, force, traction, temperature, heat, and distributed heat flux. [BCCFNC](/docs/en/keyword_documentation/b/bccfnc/) can only be used when a node's boundary constraint function type, [BCCDFN](/docs/en/keyword_documentation/b/bccdfn/) or [BCCTFN](/docs/en/keyword_documentation/b/bcctfn/), has been specified as a time/nodal value type.

  * **Diffusion bonding :**

## Diffusion Tab

**[2D, 3D]** For all the model with diffusion turned in the simulation controls, the nodal diffusion data for the object can be examined, defined or initialized in this dialog. (See Fig. 17.1.8. and Fig. 17.1.9.)

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_1_node_data_window/17_1_image008.jpg' | relative_url }})

Nodal Diffusion data window for 2D 

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_1_node_data_window/17_1_image009.jpg' | relative_url }})

Nodal Diffusion data window for 2D 

  * **Atom Percentage (DATOM) :**[DATOM](/docs/en/keyword_documentation/d/datom/) specifies atom content at a node.

  * **Diffusion Flux (CRBFLX)** : [CRBFLX](/docs/en/keyword_documentation/c/crbflx/) specifies "carbon flux" or atom flux for the surface of a workpiece.

  * **Diffusion BCC (BCCCRB)** : [BCCCRB](/docs/en/keyword_documentation/b/bcccrb/) specifies the atom transfer boundary constraint code for individual nodes.

## Electric Heating Tab

**[2D, 3D]** Electric Heating Nodal data dialog is as shown in Fig. 17.1.10.

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_1_node_data_window/17_1_image010.jpg' | relative_url }})

Nodal Electric Heating data window

  * **Electric field intensity** **(VOTAGE)** : Electric field intensity ([VOTAGE](/docs/en/keyword_documentation/v/votage/)) specifies amount of voltage supplied to heat the object.

  * **Resistance BCC** **(BCCRHT)** : Resistance BCC ([BCCRHT](/docs/en/keyword_documentation/b/bccrht/)) specifies if the value of a resistance boundary constraint (nodal velocity, force, or traction) associated with a particular node is to be specified as a constant or as a set of time/nodal value data.

  * **Current Flux (RHTFLX)** :**** Rate of flow of current ([RHTFLX](/docs/en/keyword_documentation/r/rhtflx/)) supplied to heat the object.

## User Tab

**[2D,3D]** The data for User node variables ([USRNOD](/docs/en/keyword_documentation/u/usrnod/)) can be initialized, defined or examined here.

User node variable values can be defined using FORTRAN subroutines. Refer to a [Chapter 56 section USRUPD subroutines](../../user_routines/56_user_routines_in_deform/56_2_2d_user_defined_fem_routines.htm#56_2_3_3_User_defined_node_and_element_value_\(USRUPD\)). Each node value may accept both a name and a value (See Fig. 17.1.11.). Also, an infinite number of variables may be defined. A minimum of 2 user node variables will be defined by default, however, the user may increase this to as large number as wished. User needs to be cautious that a large number of variables defined can lead to a large database file.

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_1_node_data_window/17_1_image011.jpg' | relative_url }})

User Nodal variables data window

## Thermomechanical variable Tab

**[2D, 3D]** Under Simulation controls - [Thermomechanical](/docs/en/pre_processor/9_simulation_controls/9_9_thermomechanical_variables/) variable page, added variables related to Nodal data will be listed under Thermomechanical variable ( [NRECID](/docs/en/keyword_documentation/n/nrecid/)) tab in Node data window as shown in Fig. 17.1.12. Thermomechanical variable value can be initialized or examined here. 

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_1_node_data_window/17_1_image012.jpg' | relative_url }})

Nodal Thermomechanical variables data window

## Additive Manufacturing Tab

**[3D]** Under Additive manufacturing ([NODDEN](/docs/en/keyword_documentation/n/nodden/)) tab user can define the node density value of the object used for Additive manufacturing process. (See Fig. 17.1.13.) 

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_1_node_data_window/17_1_image013.jpg' | relative_url }})

3D Nodal Additive Manufacturing variables data window

**Related Topics:**

[17\. Object Data Initialize](/docs/en/pre_processor/17_object_data_initialization/17_object_data_initialize/)

[17.2. Element Data Window](/docs/en/pre_processor/17_object_data_initialization/17_2_element_data_window/)

[17.3. Data Interpolation Window](/docs/en/pre_processor/17_object_data_initialization/17_3_data_interpolation_window/)

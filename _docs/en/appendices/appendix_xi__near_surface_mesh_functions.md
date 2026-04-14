---
lang: en
title: "Appendix XI: Near surface mesh functions"
---

# Appendix XI: Near surface mesh functions

_*From QT3 interface_

Near surface mesh functions are generated to provide or simulate the intricate details of the surface . The user can generate, extract and delete the near - surface information for both Tet mesh and brick mesh using the [coating](../pre_processor/13_mesh_generation/13_3_3d_brick_mesh_generation.htm#13.3.5_Coating_Mesh) window option in mesh generation page: (See [Fig. AXI.1.](), Fig. AXI.2. and Fig. AXI.3.)

![]({{ '/assets/images/appendices/appendix_xi_near_surface_mesh_functions/image0001.jpg' | relative_url }})

Generation of near - surface mesh (brick)

![]({{ '/assets/images/appendices/appendix_xi_near_surface_mesh_functions/image0002.jpg' | relative_url }})

Extraction of near - surface mesh (brick)

![]({{ '/assets/images/appendices/appendix_xi_near_surface_mesh_functions/image0003.jpg' | relative_url }})

Deletion of near - surface mesh (brick)

The user can assign residual stress via near-surface mesh using the Element + Node definition for stress

( Simulation Control / Advanced / [Output Control](../pre_processor/9_simulation_controls/9_7_advanced_options.htm#9.7.4._Output_Control) ), which is accessible in node data dialog. (See Fig. AXI.4. and Fig. AXI.5.)

![]({{ '/assets/images/appendices/appendix_xi_near_surface_mesh_functions/image0004.jpg' | relative_url }})

Node Data window

![]({{ '/assets/images/appendices/appendix_xi_near_surface_mesh_functions/image0005.jpg' | relative_url }})

Defining residual stress as a function of depth

Pick surface nodes in specified area and assign the residual stress via near-surface mesh layers. (See Fig. AXI.6.)

![]({{ '/assets/images/appendices/appendix_xi_near_surface_mesh_functions/image0006.jpg' | relative_url }})

Picking surface node to assign residual stress

This shows the stress assigned using the Post-processor function ([SV between two points](/docs/en/post_processor/26_post_processing_tools_and_controls/26_6_post_processing_tools/26_6_8_state_variables_between_2_points/)) as shown in Fig. AXI.7.

![]({{ '/assets/images/appendices/appendix_xi_near_surface_mesh_functions/image0007.jpg' | relative_url }})

Assigned stress via near surface mesh in Post processor

**Problem faced to move nodes onto reference surface:**

  * For CMM measurement of distortion results, it is common to analyze the results using the deviation form a best fit surface

  * The distortion value is generally small

  * The starting mesh surface is generally not on the perfect surface due to discretization error

  * The discretization errors of the mesh surface may overwhelm the distortion values

  * In order to compare the simulation results to the CMM measurement results directly, it is necessary to move certain nodes onto a reference surface

The function is accessible in the [node data](/docs/en/pre_processor/17_object_data_initialization/17_1_node_data_window/) dialog as shown in below Fig. AXI.8.

![]({{ '/assets/images/appendices/appendix_xi_near_surface_mesh_functions/image0008.jpg' | relative_url }})

Node data window

Define the reference surface (either planar or cylindrical surface) by best fit to selected nodes or user input the surface definition. Then, the selected nodes are moved onto the reference surface (See Fig. AXI.9.)

![]({{ '/assets/images/appendices/appendix_xi_near_surface_mesh_functions/image0009.jpg' | relative_url }})

Projecting the selected nodes onto the surface

**Related Topics:**

[13\. Mesh Generation](/docs/en/pre_processor/13_mesh_generation/13_mesh_generation/)

[17.1. Node Data Window](/docs/en/pre_processor/17_object_data_initialization/17_1_node_data_window/)

---
lang: sk
title: "13.3. 3D Brick Mesh Generation"
---

# 13.3. 3D Brick Mesh Generation

13.3.1. General Settings for Brick mesh  
13.3.2. 2D Cross section for Brick mesh  
13.3.3. Mesh Weighing Factors  
13.3.4. Mesh Density Window for Brick mesh  
13.3.5. Coating Mesh  
13.3.6. Remeshing Criteria  
13.3.7. Advanced Settings

The below Fig. 13.3.1. shows the Brick mesh generation options in Expert mode.

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_3_3d_brick_mesh_generation/13_3_image001.jpg' | relative_url }})

Expert mode Brick mesh generation

## General Settings for Brick mesh

**Uniform Thickness of Layers** : When this option is selected, a mesh with layers of uniform thickness is generated based on the number of layers defined. 

**Finer mesh Areas** :User can define the finer mesh areas by defining number of layers required within specified area as shown in Fig. 13.3.2.

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_3_3d_brick_mesh_generation/13_3_image003.jpg' | relative_url }})

Finer Mesh Areas Definition

The density of mesh layers can be controlled by using Fine Mesh areas option. User can control the number of mesh layers within area by selecting the start point and end point of the area. Fig. 13.3.3. shows the object with variable mesh density.

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_3_3d_brick_mesh_generation/13_3_image002.jpg' | relative_url }})

Example showing Finer Mesh Areas definition

**Sheet application:**

Sheet application option activates projection-based remeshing for sheet-shaped objects that have been constructed with brick elements. The setting only applies to an object that was initially generated as 2D mesh and then extruded into 3D mesh.

When sheet application option is deactivated (default), the object is meshed with tet elements during any subsequent remeshing.

With the setting activated, brick remeshing will be attempted using projection techniques. The remesher will fall back to tet elements if the deformed shape significantly deviates from a sheet shape, since such a condition may cause the sheet brick remesher to fail. (See Fig. 13.3.4.)

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_3_3d_brick_mesh_generation/13_3_image009.jpg' | relative_url }})

Sheet application option selelcted 

## 2D Cross section for Brick mesh

In order to generate a brick mesh a 2D cross-section is defined which is meshed and either extruded or revolved with specified number of layers depending on the 3D geometry requirement.

**Mapped Mesh Generation** : Mapped meshing can be used at the initial stages of forming process. As the geometry of the workpiece takes a complex shape during forming, mesh is subjected to several remeshings and mapped meshing may not be able to survive such changes to geometry and remeshing may fail. Mapped mesh generation can been seen in the Fig. 13.3.5.

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_3_3d_brick_mesh_generation/13_3_image004.jpg' | relative_url }})

Mapped Mesh Generation for 2D Cross-section

**Use coarse internal mesh:** User can generate coarse mesh inside region as shown in Fig. 13.3.6.

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_3_3d_brick_mesh_generation/13_3_image005.jpg' | relative_url }})

Coarse internal mesh generation for 2D Cross-section

## Mesh Weighing Factors

The weighting factors or parameters (system defined mesh density) for boundary curvature, temperature, strain and strain rate specify relative mesh density weights to be assigned to the associated parameter. For more information Refer [13.2.5. Mesh weighting factors.](13_2_3d_tet_mesh_generation.htm#13.2.5._Mesh_weighting_factors)

## **Mesh Density Window for Brick mesh**

The Mesh density window (See Fig. 13.3.7.) concept is similar to a user defined mesh density. The mesh density specified for a given window is applied to any geometry point (node or STL vertex) inside the window. However, the mesh density window is used during remeshing as well as initial mesh generation, whereas user defined mesh densities are used only during initial generation. It can also be assigned a velocity, or follow another object's movement and it can be defined in an area where the workpiece has not yet been deformed through.

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_3_3d_brick_mesh_generation/13_3_image006.jpg' | relative_url }})

Mesh density windows for 2D

## Coating Mesh

The user can add coating layers using this option and generate mesh for the same. Coating mesh is a thin layer of elements along the object boundary with specific characteristics. For added coating layers user can assign material. For further information on the usage of coating mesh please refer to [Appendix XI](/docs/sk/appendices/appendix_xi__near_surface_mesh_functions/).

## Remeshing Criteria

Remeshing Criteria (Autoremesh) is the most convenient way to handle the remeshing of objects undergoing large plastic deformation. The Remeshing Criteria Window (See Fig. 13.3.8.) contains a group of parameters that control when and how often the mesh will be regenerated on a meshed object based on assignment of certain triggers. There are four keywords that control the initiation of a remeshing procedure for an object, they are Interference Depth ([RMDPTH](/docs/sk/keyword_documentation/r/rmdpth/)),Max. Time Increment ([RMTIME](/docs/sk/keyword_documentation/r/rmtime/)), Max. Step Increment ([RMSTEP](/docs/sk/keyword_documentation/r/rmstep/)) and Max. Stroke Increment ([RMSTRK](/docs/sk/keyword_documentation/r/rmstrk/)). When the remeshing criteria of any of these keywords has been fulfilled or the mesh becomes unusable (negative Jacobian), the object will be remeshed. During the simulation, if an object satisfies any of its remeshing criteria, a new mesh is generated, the solution information from the old mesh is interpolated onto the new mesh and the simulation continues.

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_3_3d_brick_mesh_generation/13_3_image007.jpg' | relative_url }})

Remesh criteria option for Brick mesh

  
For details about Maximum interference depth (RMDPTH), Maximum stroke increment (RMSTRK), Maximum time increment (RMTIME), Maximum step increment (RMSTEP) and Purpose of Criteria please refer [13.2.8. Remeshing criteria.](13_2_3d_tet_mesh_generation.htm#13.2.8._Remeshing_criteria)

## Advanced Settings

  
Below Fig. 13.3.9. shows the Advanced Settings window for 3D Brick mesh.

![]({{ '/assets/images/pre-processor/13_mesh_generation/13_3_3d_brick_mesh_generation/13_3_image008.jpg' | relative_url }})

Advanced settings window for Brick mesh 

**Grid resolution**(**MGGRID**)

When an object is meshed in 2D, a sampling grid is required to discretize density of the mesh throughout the starting geometry. Grid resolution ([MGGRID](/docs/sk/keyword_documentation/m/mggrid/)) specifies the spacing of the sampling grids that are used to sample mesh densities. Increasing the value of X division or Y division will result in sharper gradients between areas of differing mesh density. In the case of blanking, where a very high mesh gradient is required over a narrow region, these values may need to increase to capture high changes in mesh gradient over short distances.

**Node addition parameters** (**MGERR**)  
The node addition parameters ([MGERR](/docs/sk/keyword_documentation/m/mgerr/)) specify the maximum distance and angle error permitted between the object boundary and its associated grid element side. The distance and angle tolerances are used to capture critical boundary geometry that might otherwise be lost when the mesh is generated. If an object is required to capture very small features, the maximum distance can be decreased or if a node needs to be placed on a shallow angle, the angle error can be decreased as well. Rarely will the user ever have to change these values. For parts that are very small, a value of 0.01% of the object’s bounding box is a good starting number that can be used for [MGERR](/docs/sk/keyword_documentation/m/mgerr/) for better handling of mesh resolution.

Related Topics:

[13\. Mesh Generation](/docs/sk/pre_processor/13_mesh_generation/13_mesh_generation/)

[13.1. 2D Mesh Generation](/docs/sk/pre_processor/13_mesh_generation/13_1_2d_mesh_generation/)

[13.2. 3D Tet Mesh Generation](/docs/sk/pre_processor/13_mesh_generation/13_2_3d_tet_mesh_generation/)

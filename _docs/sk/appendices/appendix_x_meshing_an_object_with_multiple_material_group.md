---
lang: sk
title: "Appendix X: Meshing an object with multiple material group"
---

# Appendix X: 2D Topology definition and Multiple Material Groups

_*From QT3 interface_

  
AX.1. 2D Topology Definition

AX.2. User Interface for Topology Building

AX.3. Summary

AX.4. Applications of Multiple Material Groups

AX.5. Two examples from the references

New topology concepts have been implemented which enable multiple material group definition within a single object. From the geometry point of view this forms a single set of data that can be conveniently defined, with each region (and the associated mesh) having it's own material assignment. Coating mesh or internal voids can be special cases of this new data set as explained in the following examples. And this topology data can be retained across remesh steps. In summary the following section gives specific details on,

  * Development of 2D topology definition and multiple material groups.

  * Example applications of multiple material groups in 2D.

One object, one mesh, multiple material groups as shown in Fig. AX.1.

![]({{ '/assets/images/appendices/appendix_x_meshing_an_object_with_mmg/image001.jpg' | relative_url }})

One object with multiple materials group

## 2D Topology Definition

Introduce Vertex, Edge, Loop, Region topology entities to the data structure. (See Fig. AX.2.)

![]({{ '/assets/images/appendices/appendix_x_meshing_an_object_with_mmg/image002.jpg' | relative_url }})

Defining the region topology entities

Material can be defined on geometry (topological regions).

Basic boundaries represented by Edge 1(open), Edge 2(open), Edge 3(open) and Edge 4 (closed) can be either imported from files (.GEO, .IGES, .DXF) or created interactively.

![]({{ '/assets/images/appendices/appendix_x_meshing_an_object_with_mmg/image003.jpg' | relative_url }})

Adding loops to Region

  * (Loop 1, Loop 2, and Loop 3) can be generated automatically (by default) or interactively. (See Fig. AX.3.)

  * (Region 1 and Region 2) can be generated interactively. The region is generated automatically when only one loop exists.

  * As a default, Loops and regions are automatically generated for most common cases when only one region exists. If there are more than two loops, user needs to define regions interactively.

## User Interface for Topology Building

![]({{ '/assets/images/appendices/appendix_x_meshing_an_object_with_mmg/image004.jpg' | relative_url }})

Building Region and assigning Materials

**Topology Building Example–Open Boundary:**

![]({{ '/assets/images/appendices/appendix_x_meshing_an_object_with_mmg/image005.jpg' | relative_url }})

Topology Building for open Boundary region and assigning Materials

**Topology Building Example–Closed Boundary:**

![]({{ '/assets/images/appendices/appendix_x_meshing_an_object_with_mmg/image006.jpg' | relative_url }})

Topology Building for closed Boundary region and assigning Materials

![]({{ '/assets/images/appendices/appendix_x_meshing_an_object_with_mmg/image007.jpg' | relative_url }})

Topology Building with Internal void

**Handling Multiple Material Groups with Coating:**

![]({{ '/assets/images/appendices/appendix_x_meshing_an_object_with_mmg/image008.jpg' | relative_url }})

Handling the multiple material group with Coating

**Extracting Geometry and Topology from Existing Mesh:**

![]({{ '/assets/images/appendices/appendix_x_meshing_an_object_with_mmg/image009.jpg' | relative_url }})

Extracting Geometry and Topology from Existing Mesh.

**Topology Saving and Loading –Geo and Keyword File:**

![]({{ '/assets/images/appendices/appendix_x_meshing_an_object_with_mmg/image010.jpg' | relative_url }})

Saving and Loading the Topology geometry

## Summary

  * New topology definition for 2D geometry.

  * Material defined on geometry (topological regions).

  * Auto loop construction of both manifold and non-manifold geometry.

  * Automatic region construction when only one loop exists or extracting geometry from mesh.

  * Interactive region construction when more than one loop exists (not well defined).

  * Related display/picking, topology editing UI, etc.

  * Topology data saving/loading (keyword file, GEO file).

  * Multiple material mesh with coating mesh.

  * Geometry/topology extraction from multiple material group mesh.

  * Functionality available for all other 2D and 3D applications - currently available in Regular Pre 2D, MO2 and Shape Rolling template.

## Applications of Multiple Material Groups

  * Rolling and extrusion are commonly used to produce bimetallic products such as wire or sheet and plate, as well as other simple geometries from shape rolling.

  * Forming of bimetallic material involves non-uniformity caused by different material properties of bimetal components.

  * Properly designed bimetallic products and optimal process parameters exhibit an desired mechanical properties without any defects

## Two examples from the references

**_Co-extrusion ~ extrusion of bimetallic tubes_**

Wojciech Z. Misiolek (Lehigh University), Vinod K. Sikka(Oak Ridge Natrional Lab.)

“Physical and Numerical Analysis of Extrusion Process for Production of Bimetallic Tubes”

Final Technical Report (2006) available at US. Dept. of Energy, http://www.osti.gov/bridge

**_Asymmetric rolling ~ rolling of bimetallic plates_**

D. Rydz et al, “The Prediction of Curvature of Bimetallic Plate Au-Cu during Asymmetrical Cold Rolling”

METALUGIJA 42 (2003) 4, 261-264

**Related Topics:**

[Geometry Data](/docs/sk/pre_processor/12_geometry_modelling/12_geometry_modelling/)

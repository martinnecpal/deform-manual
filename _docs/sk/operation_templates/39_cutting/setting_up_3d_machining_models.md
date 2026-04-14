---
lang: sk
title: "Setting up 3D Machining Models"
---

# Setting up 3D Machining Models

Mesh definition is the most critical factor in simulation performance. The goal is to adoptively refine the mesh to maintain small elements in areas where they are necessary to maintain geometry or state variables. At the same time, we wish to keep the total number of elements in the simulation to a minimum.

The most significant enhancement of DEFORM is local remeshing – rather than completely regenerating the mesh, as was done in earlier versions of DEFORM, elements are simply split or merged to improve quality and match local element size requirements. Elements which meet local size and quality requirements are not changed.

Major advantages of this new feature are that the problem of element deletion due to the chip touching the edge of a workpiece has been nearly (if not completely) eliminated, and the changing shape of sharp curves such as the nose radius feature has been substantially reduced.

A new interpolation scheme has been implemented which uses a least squares fit of surrounding elements, and reduces state variable smoothing during repeated remeshings. Because mesh element size definition is based on these state variables (particularly strain), mesh generation behavior is also changed.

Different approaches to mesh generation are appropriate depending on whether the user’s primary interest is the chip or the workpiece. Both approaches are described below.

_**A) For capturing chip geometry**_

  * these settings will give good resolution in the chip, but will tend to loose or smooth out temperature, residual stress, and microstructure information in the workpiece.

  * There is no need for mesh windows. In nearly every case, properly defined adaptive meshing will consistently provide a good quality mesh with substantially fewer elements than can be achieved with mesh windows.

  * Use Absolute Element Size. Set the minimum element size to about 1/3 or ¼ of the uncut chip thickness. ¼ will give better results, but run time will be significantly longer. 

  * Set the size ratio between 10 and 15.

  * Use Local Remeshing: under Mesh![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})Remesh Criteria![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})Remeshing Method ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) select “Local solid”

  * Set the mesh weighting factor slider bars to 50% strain, 50% strain rate, all other values = 0.

  * The mesh generator normally determines mesh refinement based on the gradient of state variables. In other words, a region where state variables (strain or strain rate) are changing quickly will get relatively fine elements, but regions which have high constant values will get a relatively coarse mesh. For machining we want fine elements in the chip (high constant strain), and in the primary shear zone (high strain rate). To trigger the mesh generator to do this, Under Weighting factor tab, check the Strain distribution - Use Gradient check box and Strain rate distribution - Use Gradient check box.

**Summary** : (these settings will maintain chip geometry, but will tend to loose state variables in the workpiece)

  * Absolute element size – minimum size 1/3 to ¼ of uncut chip thickness. Size ratio 10 to 15.

  * Local Solid

  * Slider bar weighting 50% strain, 50% strain rate

  * Under Weighting factor tab, check the Strain distribution - Use Gradient check box and Strain rate distribution - Use Gradient check box.

**B) For capturing workpiece properties**

For simulations where workpiece surface properties (residual stress, microstructure, temperature) are of interest, but chip geometry is not. For these simulations, a mesh window may be helpful to maintain mesh size on the cut surface. Strain based meshing may also be adequate. The user may wish to experiment with both approaches to find which gives better results.

**With mesh windows:**

  * Use absolute element size. Use a size ratio of 1, and set the global element size to be about 5 x larger than the expected surface layer thickness. Windows will be used to refine the mesh in the surface layer.

  * Define a mesh window from slightly in front of the tool edge, and extending backward. Define window movement to follow the cutting tool. The window can extend substantially behind the workpiece, such that it covers more and more of the workpiece surface as the tool advances.

  * Assign element size in window to be roughly 30-70% of the size of the expected surface layer effect. In other words, if the residual stress variations are over a depth of 0.01mm, the minimum element size should be around 0.005mm. Note that there will always be a difficult balance between adequate resolution and acceptable run times.

  * The size ratio between elements in the window and elements outside the window should not exceed about 5:1. If necessary, nested windows should be used with 5:1 ratio maintained between adjacent windows. The smallest elements (innermost window) should be first in the list of windows.

  * Slider bars should be weighted either fully to mesh windows, or roughly 80% mesh windows, 20% divided between strain & strain rate.

  * Local remeshing will do a better job of maintaining state variables. Use Local Remeshing: under Mesh![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})Remesh Criteria![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})Remeshing Method select “Local Solid”.

**Without mesh windows:**

  * Use absolute element size, with the minimum element size 30-70% of the expected surface layer effect thickness.

  * Use a size ratio of 10

  * Use Local Solid

  * The new interpolation scheme will do a good job of maintaining strain in the cut surface of the workpiece, so this can be used as a key meshing parameter. Set slider bars to 80% strain, 20% strain rate.

  * Check the Strain distribution - Use Gradient check box. This will cause the mesh generator to maintain a fine mesh in regions where the strain is high (i.e. the cut surface). The contents of the file are arbitrary.

**Related Topics:**

[Object Mesh Data](/docs/sk/pre_processor/13_mesh_generation/13_mesh_generation/)

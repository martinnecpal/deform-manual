---
lang: sk
title: "Appendix XV: The Double Concave Corner Constraint"
---

# Appendix XV: The Double Concave Corner Constraint

This feature is available under the **Simulation Controls** ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **Control Files** menu in the preprocessor. Any given node in an FEM mesh has three degrees of freedom (DOF). In a Cartesian coordinate system they can be the X, Y and Z directions. In a cylindrical system, they can be the radial, axial and hoop directions. In any case, no matter what coordinate system one selects, there are no more and no less than three degrees of freedom for any node. In the boundary condition dialog (as seen in Fig. AXV.1.), the DOF for the nodes are defined through contact, through velocity control and other conditions. The way in which a DOF is defined for a node in contact is to not allow the node to penetrate into the object as well as do not allow separation if the tensile separation criteria is not exceeded (usually a small nominal value). Three contact conditions, completely specify the motion of a given node.

![]({{ '/assets/images/appendices/appendix_xv_the_double_concave_corner/image0001.jpg' | relative_url }})

The boundary condition dialog

There is a specific case where more than one degree of freedom is required for a given node. Consider the case where a node resides in the corner of a die cavity (See Fig. AXV.2.). Note that nodes 1,2,3 are in contact with the die surface and their vertical motion should follow the die surface. Note also that nodes 3,4,5 are in contact with the die surface and their horizontal motion should follow the die surface. The problem comes for node 3. It should have two boundary condition codes to restrict its motion in two DOF. These two degrees of freedom can be seen as the directions of the red arrows in Fig. AXV.2. However, if it only has one, it is only restricted in one direction and can thus penetrate the other direction.

![]({{ '/assets/images/appendices/appendix_xv_the_double_concave_corner/image0002.jpg' | relative_url }})

A set of nodes lying on a die surface

Note that as shown in Fig. AXV.2. nodes 1,2,3 should be constrained in the vertical direction and nodes 3,4,5 should be constrained in the horizontal direction.

For this reason, there is a new functionality to let nodes in convex corners be applied with 2 contact conditions. In order to specify which nodes should be given this constraint, two angles are to be given for this consideration. As seen in Fig. AXV.3., angle a is the minimum angle value and angle b is the maximum. Between these two angles, nodes will be specified with a double contact constraint. Fig. AXV.4. indicates the corresponding settings in the simulation controls. ([Control Files](/docs/sk/pre_processor/9_simulation_controls/9_8_control_files/) : [Category 1](../pre_processor/9_simulation_controls/9_8_control_files.htm#9.8.1._Category_1))

![]({{ '/assets/images/appendices/appendix_xv_the_double_concave_corner/image0003.jpg' | relative_url }})

The two angles that are specified in the double concave corner constraint

![]({{ '/assets/images/appendices/appendix_xv_the_double_concave_corner/image0004.jpg' | relative_url }})

The two angles that are specified in the double concave corner constraint

**Related Topics:**

[Simulation Controls](/docs/sk/pre_processor/9_simulation_controls/9_simulation_controls/)

[Object Boundary Condition](/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/)

---
lang: sk
title: "Appendix IX: Generating a Circular Geometry With a Hole"
---

# Appendix IX: Generating a Circular Geometry With a Hole

_*From QT3 interface_

This case involves the two features of generating a circular geometry and adding an internal hole. To create a circular geometry, go to the geometry window of the desired object.

  1. Click the Edit tab and select the Line-Arc format radio button as seen in Fig. AIX.1.

  2. Set the type to Arc.

  3. The first point X1, Y1 is the start of the arc. The second point X2, Y2 is the center of the arc. The angle is the amount of sweep of the arc. Input the following values: (1,0) for X1, Y1; (0,0) for X2, Y2; and 360 for the angle.

![]({{ '/assets/images/appendices/appendix_ix_generating_a_circular_geometry_with_a_hole/image0001.jpg' | relative_url }})

Setting the geometry type to Line-Arc

This will yield the result seen in Fig. AIX.2.

![]({{ '/assets/images/appendices/appendix_ix_generating_a_circular_geometry_with_a_hole/image0002.jpg' | relative_url }})

Generating a circular geometry

  1. Increment the boundary number in the geometry window and select the second boundary (See Fig. AIX.3.).

![]({{ '/assets/images/appendices/appendix_ix_generating_a_circular_geometry_with_a_hole/image0003.jpg' | relative_url }})

Incriminating the boundary number and selecting the second boundary

  1. Set the geometry type to Arc and set the curve as follows (0.5,0) for the first point; (0,0) for the second point; and –360 as the angle.

At this point a mesh can be generated which will have a hole in the middle (See Fig. AIX.4.).

**Note** :

The exterior boundary was counter-clockwise while the interior boundary was clockwise.

![]({{ '/assets/images/appendices/appendix_ix_generating_a_circular_geometry_with_a_hole/image0004.jpg' | relative_url }})

A circular result with a hole

**Related Topics:**

[12\. Geometry Modelling](/docs/sk/pre_processor/12_geometry_modelling/12_geometry_modelling/)

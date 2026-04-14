---
lang: sk
title: "40. Introduction to Machining Distortion"
---

# 40\. Introduction to Machining Distortion

Machining distortion operation can set up the model data and simulate a machining pass on a component with deformation and residual stress history. Machining Distortion will model and simulate machining operation with fixtures and elastic spring back after the fixtures are removed.

The Machining distortion Operations can be used to prepare the data required for the simulation. To use this operation, user needs the result from a DEFORM simulation model that includes residual stress in the part. Typical models include elasto-plastic deformation process or heat treat process model. Apart from this object input data, machining distortion process model requires details on the fixtures, their location and details on machining pass.

The order of operations in which we will be modeling is as follows:

  1. Machine the part.

  2. Allow the part to spring back with tools to constrain.

  3. Allow part to spring back free from tools.

All of these operations can be accomplished in the Machining distortion Operation. Of these stages,

only the data related to machining is defined in the template, while the system procedures automatically compute the subsequent spring back stage on removing the fixtures. Post processor will allow the user to view the results (stress state and spring back/distortions) after machining and fixture removal. This process can be repeated for the subsequent passes, which may also include object flipping and fixture repositioning prior to machining.

**Related Topics:**

[40.1. 2D Machining Distortion](/docs/sk/operation_templates/40_machining_distortion/40_1_2d_machining_distortion/)

[40.2. 3D Machining Distortion](/docs/sk/operation_templates/40_machining_distortion/40_2_3d_machining_distortion/)

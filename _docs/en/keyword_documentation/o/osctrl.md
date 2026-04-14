---
lang: en
title: "OSCTRL (2D)"
---

# OSCTRL

|  (Simulation control - 2D)  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

OSCTRL Noscil, Nstep

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Noscil |  Total number of oscillations before a node is locked |  0  
Nstep |  Total number of sub-steps that the node should be locked at the corner prior to releasing. |  0  
  
DEFINITION  
---  
OSCTRL is used to control and avoid nodal oscillation.  
  
REMARKS  
---  
The default values for both arguments are 0, that is, oscillation control is not activated. The following example gives an illustration of nodal oscillation. ![]({{ '/assets/images/keyword_documentation/o/osctrl_image001.jpg' | relative_url }}) (a) A node moves from segment 1 to 2 (b) The node moves back to segment 1, constituting the first oscillation, (c) The node moves back to segment 2, constituting the second oscillation.  
  
RELATED TOPICS  
---  
[Object Nodal Data](/docs/en/pre_processor/17_object_data_initialization/17_1_node_data_window/) Keywords: [RZ (2D)](/docs/en/keyword_documentation/r/rz/), [RZ (3D)](/docs/en/keyword_documentation/r/rz_3d/)

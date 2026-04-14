---
lang: sk
title: "PDIE (2D3D)"
---

# PDIE

|  (Simulation Control)  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

PDIE Primary Die Primary Object

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
PrimaryDie |  Object number of the primary Die |  None  
PrimaryObject |  Object number of the primary object |  None  
  
DEFINITION  
---  
PDIE specifies the primary die and primary object for simulation.  
  
REMARKS  
---  
Characteristics of the primary die can be used to control various aspects of a simulation including

  * Simulation time step size (DSMAX)
  * Object movement (MOVCTL)
  * Simulation termination criteria (SMAX, VMIN, LMAX)

The primary die is usually assigned to the object most closely controlled by the forming machinery. For example, the die attached to the ram of a mechanical press would be designated as the primary object. If the primary die characteristics are not needed for controlling the time step size, object movement, or termination criteria, the object number assigned to be the primary die is immaterial. The primary workpiece is the object in which filling is determined for. If all the nodes are contacted on the surface of this object, the simulation will stop. Applicable simulation types: Isothermal Deformation Non-Isothermal Deformation  
  
RELATED TOPICS  
---  
[Primary object](../../pre_processor/9_simulation_controls/9_2_defining_step.htm#Primary_die_\(PDIE\)), [Movement control](/docs/sk/pre_processor/15_movement_controls_definition/15_movement_controls_settings/), [Termination parameters](/docs/sk/pre_processor/9_simulation_controls/9_3_stopping_controls/), [Step parameters](/docs/sk/pre_processor/9_simulation_controls/9_2_defining_step/). Keywords: [SMAX](/docs/sk/keyword_documentation/s/smax/), [VMIN](/docs/sk/keyword_documentation/v/vmin/), [LMAX (2D)](/docs/sk/keyword_documentation/l/lmax/), [LMAX (3D)](/docs/sk/keyword_documentation/l/lmax_3d/), [MOVCTL (2D)](../m/movctl_\(2d\).htm), [MOVCTL (3D)](../m/movctl_\(3d\).htm), [DSMAX](/docs/sk/keyword_documentation/d/dsmax/)

---
lang: sk
title: "STROKE (3D)"
---

# STROKE

|  (Object data - 3D)  
---|---  
_Update History:_ (New definition has been introduced in v10.0) |  Last updated on : 12-08-2013  
  
* * *

STROKE Object, XStroke, YStroke, Zstroke

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
XStroke |  Object stroke in X |  0.0  
YStroke |  Object stroke in Y |  0.0  
ZStroke |  Object stroke in Z |  0.0  
  
DEFINITION  
---  
STROKE specifies the stroke of objects with a movement control boundary constraint (MOVCTL).  
  
REMARKS  
---  
STROKE is the measurement of displacement of objects. The stroke of the primary object ([PDIE](/docs/sk/keyword_documentation/p/pdie/)) can be used to define movement control simulation time step size ([DSMAX](/docs/sk/keyword_documentation/d/dsmax/)) object movement (MOVCTL) simulation termination criteria ([SMAX](/docs/sk/keyword_documentation/s/smax/), [VMIN](/docs/sk/keyword_documentation/v/vmin/), LMAX) Applicable object types: [Rigid](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.5._Rigid), [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
Stroke Keywords: [PDIE](/docs/sk/keyword_documentation/p/pdie/), [MOVCTL (2D)](../m/movctl_\(2d\).htm), [MOVCTL (3D)](../m/movctl_\(3d\).htm) , [DSMAX](/docs/sk/keyword_documentation/d/dsmax/), [SMAX](/docs/sk/keyword_documentation/s/smax/), [VMIN](/docs/sk/keyword_documentation/v/vmin/), [LMAX (2D)](/docs/sk/keyword_documentation/l/lmax/), [LMAX (3D)](/docs/sk/keyword_documentation/l/lmax_3d/)

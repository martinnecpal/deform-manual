---
lang: en
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
STROKE is the measurement of displacement of objects. The stroke of the primary object ([PDIE]({{ '/docs/en/keyword_documentation/p/pdie/' | relative_url }})) can be used to define movement control simulation time step size ([DSMAX]({{ '/docs/en/keyword_documentation/d/dsmax/' | relative_url }})) object movement (MOVCTL) simulation termination criteria ([SMAX]({{ '/docs/en/keyword_documentation/s/smax/' | relative_url }}), [VMIN]({{ '/docs/en/keyword_documentation/v/vmin/' | relative_url }}), LMAX) Applicable object types: [Rigid]({{ '/docs/en/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.5._Rigid), [Elastic]({{ '/docs/en/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.2._Elastic), [Plastic]({{ '/docs/en/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.1_Plastic), [Elastoplastic]({{ '/docs/en/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.3._Elasto-plastic), and [Porous]({{ '/docs/en/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.4._Porous).  
  
RELATED TOPICS  
---  
Stroke Keywords: [PDIE]({{ '/docs/en/keyword_documentation/p/pdie/' | relative_url }}), [MOVCTL (2D)]({{ '/docs/en/keyword_documentation/m/movctl_(2d)/' | relative_url }}), [MOVCTL (3D)]({{ '/docs/en/keyword_documentation/m/movctl_(3d)/' | relative_url }}) , [DSMAX]({{ '/docs/en/keyword_documentation/d/dsmax/' | relative_url }}), [SMAX]({{ '/docs/en/keyword_documentation/s/smax/' | relative_url }}), [VMIN]({{ '/docs/en/keyword_documentation/v/vmin/' | relative_url }}), [LMAX (2D)]({{ '/docs/en/keyword_documentation/l/lmax/' | relative_url }}), [LMAX (3D)]({{ '/docs/en/keyword_documentation/l/lmax_3d/' | relative_url }})

---
lang: en
title: "WINRSE (2D3D)"
---

# WINRSE

|  (Object data)  
---|---  
_Update History:_ V11 - WINRSE has been introduced. |  Last updated on : 12-08-2013  
  
* * *

WINRSE Object, WinNo, WinShape

Point(1), X(1), Y(1), Z(1)

: : :

Point(8), X(8), Y(8), Z(8)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
WinNo |  Index of current RSE window |  None  
WinShape |  Shape of RSE window  =**1** Cubical shape (Box)  =**2** Cylinder (not implemented yet) |  1  
Point(i) |  Index of ith points describing window region |  None  
X(i),Y(i),Z(i) |  Coordinate of ith point in defined area |  0.0  
  
DEFINITION  
---  
WINRSE specifies the rigid window which defines a specific region where plastic deformation is not expected. This rigid window is optional input for RSE solver. Multiple rigid windows can be defined per object.  
  
REMARKS  
---  
If only some portion of deforming object undergoes plastic deformation often found in [Cogging](/docs/en/operation_templates/29_cogging/29_introduction_to_cogging/) simulation, using the rigid window can help RSE to improve the computational efficiency by reducing the effort in searching a plastically deforming zone. Applicable object types: [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic)  
  
RELATED TOPICS  
---  
Keywords: [SOLMTD(2D)](/docs/en/keyword_documentation/s/solmtd/), [SOLMTD(3D)](/docs/en/keyword_documentation/s/solmtd_3d/) , [RSEDEF(3D)](/docs/en/keyword_documentation/r/rsedef/)

---
lang: en
title: "STRESS (3D)"
---

# STRESS

|  (Object data - 3D)  
---|---  
_Update History:_ v11 - Stress tensor at 8 integration points has been added for 3D brick element. |  Last updated on : 13-08-2013  
  
* * *

STRESS Object, Ndata, DefStress, Nnode, DefNodeStress

or

(If “Integration Point” stress is requested for output, ELMNOD=3)

STRESS Object, Ndata, 0.0, Nnode, 0.0, NIntPts

(If “element” stress is requested for output, ELMNOD=0)

Element(1), X1(1), X2(1), X3(1), X4(1), X5(1), X6(1)

::

Element(Ndata), X1(Ndata), X2(Ndata),X3(Ndata),X4(Ndata),X5(Ndata),X6(Ndata)

(If dual “element + nodal” stress is requested for output, ELMNOD=2)

Element(1), X1(1), X2(1), X3(1), X4(1), X5(1), X6(1)

::

Element(Ndata), X1(Ndata), X2(Ndata),X3(Ndata),X4(Ndata),X5(Ndata),X6(Ndata)

Node(1), X1(1), X2(1), X3(1), X4(1), X5(1), X6(1)

::

Node(Nnode), X1(Nnode), X2(Nnode), X3(Nnode), X4(Nnode), X5(Nnode), X6(Nnode)

(Only for brick element with eight integration points, NIntPts=8)

(If “Integration Point” stress is requested for output, ELMNOD=3)

Element(1)

X1(1,1), X2(1,1), X3(1,1), X4(1,1), X5(1,1), X6(1,1)

::

X1(NIntPts,1), X2(NIntPts,1), X3(NIntPts,1), X4(NIntPts ,1), X5(NIntPts,1), X6(NIntPts,1)

::

Element(Ndata)

X1(1,Ndata), X2(1,Ndata), X3(1,Ndata), X4(1,Ndata), X5(1,Ndata), X6(1,Ndata )

::

X1(NIntPts,Ndata), X2(NIntPts,Ndata), X3(NIntPts,Ndata), X4(NIntPts,Ndata),

X5(NIntPts,Ndata), X6(NIntPts,Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
Ndata |  Number of elements |  None  
DefStress |  Default elemental stress value |  0.0  
Nnode |  Number of nodes |  None  
DefNodeStress  |  Default nodal stress value |   
NIntPts |  Number of integration points per element = **8** Brick element = **1** Tet element (same as elemental output option) |  8  
X1(i) |  Sigma X of ith data set |  None  
X2(i) |  Sigma Y of ith data set |  None  
X3(i) |  Sigma Z of ith data set |  None  
X4(i) |  Tau XY of ith data set |  None  
X5(i) |  Tau YZ of ith data set |  None  
X6(i) |  Tau XZ of ith data set |  None  
  
DEFINITION  
---  
STRESS defines the stress tensors of each element of an object.   
  
REMARKS  
---  
X1 is the value of Sigma X(![]({{ '/assets/images/keyword_documentation/s/sigmax.jpg' | relative_url }})), X2 is Sigma Y(![]({{ '/assets/images/keyword_documentation/s/sigma_y.jpg' | relative_url }})), X3 is Sigma Z(![]({{ '/assets/images/keyword_documentation/s/sigma_z.jpg' | relative_url }})), X4 is Tau XY(![]({{ '/assets/images/keyword_documentation/s/tau_xy.jpg' | relative_url }})), X5 is Tau YZ(![]({{ '/assets/images/keyword_documentation/s/tau_yz.jpg' | relative_url }})) and X6 is Tau XZ(![]({{ '/assets/images/keyword_documentation/s/tau_xz.jpg' | relative_url }})). The keyword format varies depending on stress output selection made at ELMNOD. For element output (ELMNOD = 0) option, stress at the centroid of each element is written. For dual output (ELMNOD = 2) option, stress at the centroid of element and at node are written. For brick element case with integration point (ELMNOD = 3) option, stress at eight integration points in element are written. The stress tensor,![]({{ '/assets/images/keyword_documentation/s/sij.jpg' | relative_url }}) , of the object is represented by the matrix: ![]({{ '/assets/images/keyword_documentation/s/stress_3d_image002.jpg' | relative_url }}) ![]({{ '/assets/images/keyword_documentation/s/stress_3d_image001.jpg' | relative_url }}) Note: This integration point option is valid only for brick element whose stress values are evaluated at 8 integration points per element during FEM calculation. For Tetrahedral element, integration point output option is same as elemental output option.  Applicable [object types](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4._Object_type): [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), Elastoplastic, [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous)  
  
RELATED TOPICS  
---  
Related keywords: ELMN[ELMNOD (2D3D)](/docs/en/keyword_documentation/e/elmnod/)OD

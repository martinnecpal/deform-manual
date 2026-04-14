---
lang: sk
title: "STRESS (2D)"
---

# STRESS

|  (Object data - 2D)  
---|---  
_Update History:_ v11 - Stress tensor at 4 integration points has been added for 2D Quad element. |  Last updated on : 09-08-2013  
  
* * *

STRESS Object, Ndata, DefStress, FieldWidth, Nnode, DefNodeStress

(If “Integration Point” stress is requested for output, ELMNOD=3)

STRESS Object, Ndata, 0.0, FieldWidth, Nnode, 0.0, NIntPts

(If “element” stress is requested for output, ELMNOD=0)

Element(1), X1(1), X2(1), X3(1), X4(1)

::

Element(Ndata), X1(Ndata), X2(Ndata),X3(Ndata),X4(Ndata)

(If dual “element + nodal” stress is requested for output, ELMNOD=2)

Element(1), X1(1), X2(1), X3(1), X4(1)

::

Element(Ndata), X1(Ndata), X2(Ndata),X3(Ndata),X4(Ndata)

Node(1), X1(1), X2(1), X3(1), X4(1)

::

Node(Nnode), X1(Nnode), X2(Nnode), X3(Nnode), X4(Nnode)

(If “Integration Point” stress is requested for output, ELMNOD=3)

Element(1)

X1(1,1), X2(1,1), X3(1,1), X4(1,1)

::

X1(NIntPts,1), X2(NIntPts,1), X3(NIntPts,1), X4(NIntPts ,1)

::

Element(Ndata)

X1(1,Ndata), X2(1,Ndata), X3(1,Ndata), X4(1,Ndata)

::

X1(NIntPts,Ndata), X2(NIntPts,Ndata), X3(NIntPts,Ndata), X4(NIntPts,Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
Ndata |  Number of elements |  None  
DefStress |  Default elemental stress value |  0.0  
Nnode |  Number of nodes |  None  
DefNodeStress |  Default nodal stress value |   
FieldWidth |  Variable field width = **4** for Axisymmetry, Plane strain, Plane stress = **6** for Torsion |   
NIntPts |  Number of integration points (for ELMNOD=3) = **4** Quadrilateral element |  4  
X1(i) |  Sigma X(R) of ith data set |  None  
X2(i) |  Sigma Y(Z) of ith data set |  None  
X3(i) |  Sigma Z(Theta) of ith data set |  None  
X4(i) |  Tau XY(RZ) of ith data set |  None  
  
DEFINITION  
---  
STRESS defines the stress tensors of each element of an object.   
  
REMARKS  
---  
X1 is the value of Sigma X(sx), X2 is Sigma Y(sy), X3 is Sigma Z(sz), and X4 is Tau XY(txy). In Axisymmetric mode, X1 is the value of Sigma R(sr), X2 is Sigma Z (sz), X3 is Sigma Theta(sTheta), and X4 is Tau RZ (trz). The keyword format varies depending on stress output selection made at ELMNOD. For element output (ELMNOD = 0) option, stress at the centroid of each element is written. For dual output (ELMNOD = 2) option, stress at the centroid of element and at node are written. For integration point (ELMNOD = 3) option, stress at four integration points in element are written. For torsion mode, stress tensor have six components same as 3D definition. The stress tensor, Sij, of the object is represented by the matrix: ![]({{ '/assets/images/keyword_documentation/s/stress_2d_image001.jpg' | relative_url }}) | ![]({{ '/assets/equations/keyword_documentation/s/stress_eq_1.jpg' | relative_url }}) |   
---|---  
  
Applicable object types: [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), Elastoplastic, and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
  
Keyword: [ELMNOD](/docs/sk/keyword_documentation/e/elmnod/)

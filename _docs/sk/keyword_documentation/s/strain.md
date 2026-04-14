---
lang: sk
title: "STRAIN (2D)"
---

# STRAIN

|  (Object data - 2D)  
---|---  
_Update History:_ v11 – Effective strain at 4 integration points has been added for 2D Quad element. |  Last updated on : 09-08-2013  
  
* * *

STRAIN Object, Ndata, DefStrain, Nnode, DefNodeStrain

or

(If “Integration Point” stress is requested for output, ELMNOD=3)

STRAIN Object, Ndata, 0.0, Nnode, 0.0, NIntPts

(If “element” stress is requested for output, ELMNOD=0)

Element(1), Strain(1)

::

Element(Ndata), Strain(1)

(If dual “element + nodal” stress is requested for output, ELMNOD=2)

Element(1), Strain(1)

::

Element(Ndata), Strain(1)

Node(1), StrainNode(1)

::

Node(Nnode), StrainNode(Nnode)

(If “Integration Point” stress is requested for output, ELMNOD=3)

Element(1)

Strain(1,1)

::

Strain(NIntPts,1)

::

Element(Ndata)

Strain(1,Ndata)

::

Strain(NIntPts,Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
Ndata |  Number of elements |  None  
DefStrain |  Default elemental stress value |  0.0  
Nnode |  Number of nodes |  None  
DefNodeStrain |  Default nodal stress value |   
NIntPts |  Number of integration points per element = **4** Quadrilateral |  4  
Strain(i) |  Average effective strain at ith element |  None  
Strain(i,j) |  Effective strain at ith integration point of jth element |  None  
StrainNode(i) |  Effective strain at ith node |  None  
  
DEFINITION  
---  
STRAIN defines the effective strain of each element of an object.   
  
REMARKS  
---  
The keyword format varies depending on strain output selection made at ELMNOD. For element output (ELMNOD = 0) option, effective strain at the centroid of each element is written. For dual output (ELMNOD = 2) option, effective strain at the centroid of element and at node are written. For integration point (ELMNOD = 3) option, effective strain values at four integration points in element are written. Applicable object types: Plastic, Elastoplastic, and Porous  
  
RELATED TOPICS  
---  
Related keywords: ELMNOD

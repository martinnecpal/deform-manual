---
lang: sk
title: "STRAIN (3D)"
---

# STRAIN

|  (Object data - 3D)  
---|---  
_Update History:_ v11 – Effective strain at 8 integration points has been added for 3D brick element. |  Last updated on : 13-08-2013  
  
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

(Only for brick element with eight integration points, NIntPts=8)

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
Nnode |  Number of nodes None |   
DefNodeStrain  |  Default nodal stress value |   
NIntPts |  Number of integration points per element = **8** Brick element = **1** Tet element (same as elemental output option) |  8  
Strain(i) |  Average effective strain at ith element |  None  
Strain(i,j) |  Effective strain at ith integration point of jth element |  None  
StrainNode(i) |  Average effective strain at ith node |  None  
  
DEFINITION  
---  
STRAIN defines the effective strain of each element of an object.  
  
REMARKS  
---  
The keyword format varies depending on strain output selection made at [ELMNOD](/docs/sk/keyword_documentation/e/elmnod/). For element output ([ELMNOD](/docs/sk/keyword_documentation/e/elmnod/) = 0) option, effective strain at the centroid of each element is written. For dual output ([ELMNOD](/docs/sk/keyword_documentation/e/elmnod/) = 2) option, effective strain at the centroid of element and at node are written. For brick element case with integration point ([ELMNOD](/docs/sk/keyword_documentation/e/elmnod/) = 3) option, effective strain values at eight integration points in element are written. Note: This integration point option is valid only for brick element whose strain values are evaluated at 8 integration points per element during FEM calculation. For Tetrahedral element, integration point output option is same as elemental output option.  Applicable object types:[Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous)  
  
RELATED TOPICS  
---  
Related keywords: [ELMNOD (2D3D)](/docs/sk/keyword_documentation/e/elmnod/)

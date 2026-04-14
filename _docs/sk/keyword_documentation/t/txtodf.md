---
lang: sk
title: "TXTODF (2D3D)"
---

# TXTODF

|  (Object data)  
---|---  
_Update History:_ V11 - TXTODF has been introduced. |  Last updated on : 24-07-2013  
  
* * *

TXTODF Object, NElem, 0, NData, DefaultValue (For elemental definition)

Elem(1), ODF(1,1), ... , ODF(NData,1)

::

Elem(NElem), ODF(1, NElem), ... , ODF(NData, NElem)

or

TXTODF Object, 0, NNode, NData, DefaultValue (For nodal definition, not implemented yet)

Node(1), ODF(1,1), ... , ODF(NData,1)

::

Node(NNode), ODF(1, NNode), ... , ODF(NData, NNode)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object  |  Object Number |  None  
Elem |  Element Number |  None  
Node |  Node Number |  None  
NElem |  Number of elements = **0** For nodal output |  0  
NNode |  Number of nodes = **0** For element output |  0  
NData |  Number of ODFs (Orientation distribution functions) at each element (or node) |  0  
DefaultValues |  Default values  |  0  
  
DEFINITION  
---  
TXTODF specifies ODFs (orientation distribution functions) at each material point of an object.   
  
REMARKS  
---  
If the material has multiple phases, TXTODF lists the ODFs phase by phase, depending on the definition of phase sequence of the material. For single phase material, when Rodrigues space is employed to represent texture, NData is equal to the independent nodes of meshed Rodrigues space. For multiple-phase material, NData is equal to the summation of independent nodes of meshed Rodrigues space of all phases.  
  
RELATED TOPICS  
---  
Keywords: [TXTURE](/docs/sk/keyword_documentation/t/txture/)

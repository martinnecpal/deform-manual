---
lang: en
title: "YLDS (3D)"
---

# YLDS

|  (Object data - 3D)  
---|---  
|  Last updated on : 12-08-2013  
  
* * *

YLDS Object, Ndata, DefYLDS

Element(1), YLDS(1)(1), ..., YLDS(1)(6)

: :

Element(Ndata), YLDS(Ndata)(1), ..., YLDS(Ndata)(6)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object  |  Object number |  None  
Ndata  |  Number of element/YLDS pairs |  None  
DefYLDS |  Default elemental YLDS of all elements not listed in the element/YLDS pairs |  0.0  
Element(i)  |  Element number of ith data pair |  None  
YLDS(i)(j) |  Yield surface translation tensor for the ith data pair jth component  |  0.0  
  
DEFINITION  
---  
YLDS specifies the yield surface translation tensor.  
  
RELATED TOPICS  
---  
Keyword: [STRESS (2D)](/docs/en/keyword_documentation/s/stress/), [STRESS (3D)](/docs/en/keyword_documentation/s/stress_3d/)

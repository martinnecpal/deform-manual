---
lang: sk
title: "MATAXI (2D3D)"
---

# MATAXI

|  (Object data)  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

MATAXI Object, Ndata, FieldWidth

Element(1), MATAXI(1)(1), ..., MATAXI(1)(FieldWidth)

: :

Element(Ndata), MATAXI(Ndata)(1), ..., MATAXI(Ndata)(FieldWidth)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Ndata |  Number of element/MATAXI pairs |  None  
FieldWidth |  Number of variables for each element =**1** for 2D; = **9** for 3D |  None  
Element(i) |  Element number of ith data pair |  None  
MATAXI(i)(j) |  jth component of material axis data for the ith data pair (see below) |   
  
DEFINITION  
---  
MATAXI specifies the material axis at each element. In 2D, it has one component, which is the angle. In 3D, it has nine components, which are the vectors for material axis x, y, and z, in the global coordinate system. By default, they are (1,0,0), (0,1,0), and (0,0,1), respectively.  
  
REMARKS  
---  
These state variables are computed only when the material is anisotropic. Related keyword: [ANISO](/docs/sk/keyword_documentation/a/aniso/).  
  
RELATED TOPICS  
---  
[Object Element Data](/docs/sk/pre_processor/17_object_data_initialization/17_2_element_data_window/): Deformation- General Keywords: [ANISO](/docs/sk/keyword_documentation/a/aniso/)

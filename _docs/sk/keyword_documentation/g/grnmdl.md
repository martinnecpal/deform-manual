---
lang: sk
title: "GRNMDL (2D3D)"
---

# GRNMDL 

|  (Inter Material data)  
---|---  
(Obsolute) |  Last updated on : 04-08-2014  
  
* * *

GRNMDL Matr, Method, npt, ndim

Temp(1) N1(1) N2(1) K(1) N3(1) …

Temp(Ndata) N1(Ndata) N2(Ndata) K(Ndata) N3(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Matr |  Material Number |  None  
Method |  Method type = **0** Not predicted = **1![]({{ '/assets/equations/keyword_documentation/g/grnmdl_eq_1.jpg' | relative_url }})** |  None None  
Npt |  Number of temperature points |  None  
Ndim |  Dimension=**5** (# of columns) 5 |   
  
DEFINITION  
---  
The grain diameter changes as a function of temperature and can be approximately calculated with ![]({{ '/assets/equations/keyword_documentation/g/grnmdl_eq_1.jpg' | relative_url }}). This feature has not yet been implemented in the latest release of DEFORM-HT.  
  
EXAMPLES

An example of the grain model as a function of temperature.

Temperature |  n1 |  n2 |  k |  n3  
---|---|---|---|---  
500 |  2 |  4 |  5 |  4  
600 |  3 |  4 |  3 |  2  
700 |  5 |  6 |  7 |  8  
  
GRNMDL 1 1 3 5

500 2 4 5 4

600 3 4 3 2

700 5 6 7 8

REMARKS  
---  
If Ftype = 1 use the operands Npt, and Ndim. The typical values for N in metals are between 2-4. Applicable simulation types: Microstructure Module  
  
RELATED TOPICS  
---  
[DEFORM-HT](/docs/sk/operation_templates/37_heat_treatment/37_introduction_to_heat_treatment/) Keywords: [GRNDAT](/docs/sk/keyword_documentation/g/grndat/), [GRAIN](/docs/sk/keyword_documentation/g/grain/)

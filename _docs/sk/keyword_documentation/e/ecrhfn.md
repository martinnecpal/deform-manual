---
lang: sk
title: "ECRHFN (2D)"
---

# ECRHFN

|  (Object Data - 2D)  
---|---  
|  Last updated on : 30-07-2013  
  
* * *

ECRHFN Object, Ndata, Default

Num(1), node1(1) node2(1) BCfuncNum(1)

: : :

Num(Ndata), node1(Ndata) node2(Ndata) BCfuncNum(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
Ndata |  Number of edge constraint data sets |  None  
Default |  Default value for function number |  None  
Num(i) |  ith data set |  0  
node1(i) |  1st node defining edge i |  None  
node2(i) |  2nd node defining edge i |  None  
BCfuncNum(i) |  Function type for resistance heating boundary constraint in ith data set |  None  
  
DEFINITION  
---  
ECRHFN specifies whether a resistance heating edge boundary condition function is defined as a function or through a user subroutine.  
  
REMARKS  
---  
The function type (Ftype) options are: < 0 user routine number > 0 function number (specified in BCCFNC) The user should be aware that the edge definition function shares the function structure with the nodal boundary condition function keyword (BCCFNC). Applicable object types: Elastic, Plastic, Elastoplastic, and Porous.  
  
RELATED TOPICS  
---  
Object Edge data: Electric Heating, Boundary Constraints: Heating Keywords: ECCRHT, ECRHFN, BCCFNC

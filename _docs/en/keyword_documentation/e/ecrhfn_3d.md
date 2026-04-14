---
lang: en
title: "ECRHFN (3D)"
---

# ECRHFN

|  (Object data – 3D)  
---|---  
|  Last updated on : 13-08-2013  
  
* * *

ECRHFN Object, Ndata, Default

Num(1), node1(1) node2(1) node3(1) node4(1) BCfuncNum(1)

: : :

Num(Ndata), node1(Ndata) node2(Ndata) node3(Ndata) node4(Ndata) BCfuncNum(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
Ndata |  Number of face constraint data sets |  None  
Default |  Default value for function number |  0  
Num(i) |  ith data set |  None  
node1(i) |  1st node defining face i |   
node2(i) |  2nd node defining face i |   
node3(i) |  3rd node defining face i |   
node4(i) |  4th node defining face i |   
BCfuncNum(i) |  Function type for resistance heating boundary constraint in ith data set |  None  
  
DEFINITION  
---  
ECRHFN specifies whether a resistance heating face boundary condition function is defined as a function or through a user subroutine.  
  
REMARKS  
---  
The function type (Ftype) options are: < 0 user routine number > 0 function number (specified in BCCFNC) The user should be aware that the face definition function shares the function structure with the nodal boundary condition function keyword (BCCFNC). Applicable object types: Elastic, Plastic, Elastoplastic, Porous  
  
RELATED TOPICS  
---  
Object Edge data: Electric Heating, Boundary Constraints: Heating Keywords: ECCRHT, ECRHFN, BCCFNC

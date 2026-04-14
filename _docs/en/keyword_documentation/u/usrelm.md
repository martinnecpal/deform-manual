---
lang: en
title: "USRELM (2D3D)"
---

# USRELM

|  (Object data)  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

USRELM Object, Nelm, Default, Nvar

Element(1), ElmData(1,1) … ElmData(1,Nvar)

: : :

Element(Nelm), ElmData(Nelm,Nvar) …ElmData(Nelm,Nvar)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
Nelm |  Number of elements |  None  
Default |  Default value |  0  
Nvar |  Number of user element variables |  None  
Element(i) |  Element number for ith data set |  None  
ElmData(i, j) |  jth User data value for ith element |  None  
  
DEFINITION  
---  
USRELM provides storage space for calculation results that the user may want for each element. The storage area is used to provide extra state variables for elements, which the user can track. These variables are tracked through out the simulation and are kept through remeshing.  
  
REMARKS  
---  
To take advantage of these extra state variables, a subroutine in the $DEFORM_DIR directory must be edited. The subroutine is located in the file DEF_USR.FOR and is called USRUPD. This subroutine is well commented. For more details about the subroutine, read the detailed comments. Once the subroutine has been altered, it must be compiled and linked. If you have difficulties with this subroutine or any other aspects of implementation, please refer to the DEFORM User’s Manual section on user routines.  
  
RELATED TOPICS  
---  
[Object Elemental Data](/docs/en/pre_processor/17_object_data_initialization/17_2_element_data_window/): User Element variable Keywords: [USRNOD](/docs/en/keyword_documentation/u/usrnod/), [UENAME](/docs/en/keyword_documentation/u/uename/), [UNNAME](/docs/en/keyword_documentation/u/unname/)

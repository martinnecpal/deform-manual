---
lang: sk
title: "ZEFI (2D3D)"
---

# ZEFI

|  (Object data)  
---|---  
|  Last updated on : 07-08-2013  
  
* * *

ZEFI Object, Ndata, DefZEFI

Element(1), ZEFI(1), ZEFI_i(1)

: :

Element(Ndata), ZEFI(Ndata), ZEFI_i(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Ndata |  Number of element/ZEFI pairs |  None  
DefZEFI |  Default elemental ZEFI of all elements not listed in the element/ZEFI pairs |  0.0  
Element(i) |  Element number of ith data pair |  None  
ZEFI(i)  |  Real part of elemental electric field intensity of ith data pair |  0.0  
ZEFI_i(i) |  Imaginary part of elemental electric field intensity of ith data pair |  0.0  
  
DEFINITION  
---  
ZEFI specifies the electric field intensity at each element.  
  
REMARKS  
---  
The electric field intensity is a complex number. This state variable is used in simulations of induction heating.

---
lang: en
title: "ZMFI (2D3D)"
---

# ZMFI

|  (Object data)  
---|---  
_Update History:_ V11 - ZMFI has been introduced. |  Last updated on : 24-07-2013  
  
* * *

ZMFI Object, Ndata, DefZMFI

Element(1), ZMFI(1), ZMFI_i(1)

: :

Element(Ndata), ZMFI(Ndata), ZMFI_i(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
Ndata |  Number of element/ZMFI pairs |  None  
DefZMFI |  Default elemental ZMFI of all elements not listed in the element/ZMFI pairs |  0  
Element(i) |  Element number of ith data pair |  None  
ZMFI(i) |  Real part of magnetic intensity of ith data pair |  0  
ZMFI_i(i) |  Imaginary part of magnetic intensity of ith data pair |  0  
  
DEFINITION  
---  
ZMFI specifies the magnetic field intensity at each element.  
  
REMARKS  
---  
The magnetic field intensity is complex number. This state variable is used in simulations of electric resistance heating.  
  
RELATED TOPICS  
---  
Keywords: [ZEFI](/docs/en/keyword_documentation/z/zefi/), [CURRNT(2D)](/docs/en/keyword_documentation/c/currnt/), [CURRNT(3D)](/docs/en/keyword_documentation/c/currnt_3d/)

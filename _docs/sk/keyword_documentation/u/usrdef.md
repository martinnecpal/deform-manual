---
lang: sk
title: "USRDEF (2D3D)"
---

# USRDEF

|  (Simulation control)  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

USRDEF NumLines

Line(1)

:

Line(NumLines)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
NumLines |  Number of lines |  None  
Line(i) |  Character string with up to 80 characters |  None  
  
DEFINITION  
---  
USRDEF provides storage space for user data. Typically the storage area is used to provide data for a user defined subroutine or to store comments.  
  
REMARKS  
---  
Up to ten lines of data can be stored in the storage region. Each line of data is stored as an element in the character array IUSRVL. The IUSRVL array is defined in the common block IUSR. The data can be accessed from a user subroutine with read or write statements addressing the IUSRVL array. For example, if the first two lines of USRDEF were specified as: 3, 0.1, 1.0E10 Variables for flow stress definition (N, A, B) 10.0, 3.14159 Variables for movement control (X, Y) These USRDEF values could be accessed from a user subroutine using the following FORTRAN code: CHARACTER*80 IUSRVL COMMON /IUSR/ ISURVL (10) ................................................. ................................................. READ(IUSRVL(1),*) N, A, B READ(IUSRVL(2),*) X, Y Applicable simulation types: Isothermal Deformation, Heat Transfer, Non-Isothermal Deformation  
  
RELATED TOPICS  
---  
[User Sub Routines](/docs/sk/user_routines/56_user_routines_in_deform/56_user_routines_in_deform/) Keywords: [USRSUB](/docs/sk/keyword_documentation/u/usrsub/)

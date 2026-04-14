---
lang: en
title: "USRSUB (2D3D)"
---

# USRSUB

|  (Object data)  
---|---  
|  Last updated on : 24-07-2013  
  
* * *

USRSUB Object, Subroutine

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
Subroutine |  Subroutine Number |  none  
  
DEFINITION  
---  
USRSUB allows the user to store the flag value for user routines in the keyword file. This flag value is taken as an argument to the user routine as the variable NPTRTN. Based on this variable, the user routine will branch accordingly to various subroutines.  
  
REMARKS  
---  
The user routine FORTRAN file is called DEF_USR.FOR and is located in the DEFORM directory.  
  
RELATED TOPICS  
---  
[User Sub Routines](/docs/en/user_routines/56_user_routines_in_deform/56_user_routines_in_deform/) Keywords: [USRDEF](/docs/en/keyword_documentation/u/usrdef/)

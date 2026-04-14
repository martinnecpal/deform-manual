---
lang: en
title: "USRNOD (2D3D)"
---

# USRNOD

|  (Object data)  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

USRNOD Object, Nnode, Default, Nvar

Num(1), NodeData(1,1) … NodeData(Nnode,1)

: : :

Num(Ndata), NodeData(1,Ndata) … NodeData(Nnode,Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
Nnode |  Number of nodes |  None  
Nvar |  Number of user node variables |  None  
Default |  Default value |  0  
Num |  Data index |  None  
NodeData |  Data value for ith user node |  None  
  
DEFINITION  
---  
USRNOD provides storage space for information that can be calculated for specific purposes. The storage area is used to provide extra state variables for nodes, which the user can track. These variables are tracked through out the simulation and are kept through remeshing.  
  
REMARKS  
---  
To take advantage of these extra state variables, a subroutine in the $DEFORM_DIR directory must be edited. The subroutine is located in the file DEF_USR.FOR and is called USRUPD. This subroutine is well commented. For more details about the subroutine, read the detailed comments. Once the subroutine has been altered, it must be compiled and linked. If you have difficulties with this subroutine or any other aspects of implementation, please refer to the DEFORM User’s Manual section on user routines.  
  
RELATED TOPICS  
---  
Keywords: [USRELM](/docs/en/keyword_documentation/u/usrelm/), [UNNAME](/docs/en/keyword_documentation/u/unname/), [UENAME](/docs/en/keyword_documentation/u/uename/)

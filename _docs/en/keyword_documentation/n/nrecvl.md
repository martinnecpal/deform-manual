---
lang: en
title: "NRECVL (2D3D)"
---

# NRECVL

|  (Object data)  
---|---  
_Update History:_ V11.1 - NRECVL has been introduced. |  Last updated on : 21-05-2016  
  
* * *

NRECVL OBJ#, #Node, type(=0), Width(M), Default value

Node1, data11, data12, data13, ..., data1M

Node2, data21, data22, data23, ..., data2M

...

NodeN, dataN1, dataN2, dataN3, ..., dataNM

(For Type 1)

NRECVL, OBJ#, #Node, type(=1), Width(M)

1, 0, 1, 1 ... (0: leave alone; 1: initialize)

1.2, 0.0, 0.1, 0.2 ... (initial value for each column)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
OBJ# |  Object number |  None  
#Node |  Number of nodes |  None  
Type |  Definition type =**0** initial setup =**1** modify existing data |  None  
Width |  width (number of columns) of data |  None  
Default value |  default value |  None  
  
DEFINITION  
---  
NRECVL is the state variable for nodal record values.  
  
RELATED TOPICS  
---  
Related keywords: [NRECID](/docs/en/keyword_documentation/n/nrecid/)

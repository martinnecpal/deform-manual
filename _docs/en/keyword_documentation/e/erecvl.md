---
lang: en
title: "ERECVL (2D3D)"
---

# ERECVL

|  (Object data)  
---|---  
_Update History:_ V11.1 - ERECVL has been introduced. |  Last updated on : 21-05-2016  
  
* * *

ERECVL OBJ#, #Elem, type(0), Width(M), Default value

Elem1, data11, data12, data13, ..., data1M

Elem2, data21, data22, data23, ..., data2M

...

ElemN, dataN1, dataN2, dataN3, ..., dataNM

(For type 1)

ERECVL, OBJ#, #Elem, type(1), Width(M)

1, 0, 1, 1 ... (0: leave alone; 1: initialize)

1.2, 0.0, 0.1, 0.2 ... (initial value for each column)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
OBJ# |  Object number |  None  
#Elem |  Number of elements |  None  
Type |  Definition type =**0** initial setup =**1** modify existing data |  None  
Width |  width (number of columns) of data |  None  
Default value |  default value |  None  
  
DEFINITION  
---  
ERECVL is the state variable for element record values.  
  
RELATED TOPICS  
---  
Related keywords: [ERECID](/docs/en/keyword_documentation/e/erecid/)

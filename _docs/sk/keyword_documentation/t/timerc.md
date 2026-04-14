---
lang: sk
title: "TIMERC (2D3D)"
---

# TIMERC

|  (Object data)  
---|---  
_Update History:_ V11 - TIMERC has been introduced. |  Last updated on : 24-07-2013  
  
* * *

TIMERC Object, Ndata, Type, FieldWidth, DefTime

Node(1), Time(1,1), ... , Time(FieldWidth,1)

:: :: ::

Node(Ndata), Time(1,Ndata), .... , Time (FieldWidth, Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number  |  None  
Ndata |  Number of nodes |  None  
Type |  Data Type = **1** Default (for current use) = **2** Not defined yet (for future use) |  1  
FieldWidth |  Variable field width |  1  
DefTime |  Default time value |  0  
Node(i) |  Node number |  None  
Time(i,j)  |  Time value at (i,j)th location |  None  
  
DEFINITION  
---  
TIMERC specifies the nodal state variable to record the accumulated time for certain condition.  
  
REMARKS  
---  
This keyword represents nodal state variable that store time information with a specified field width.  
  
RELATED TOPICS  
---  
Keywords: [TIMEID](/docs/sk/keyword_documentation/t/timeid/), [DIFBND](/docs/sk/keyword_documentation/d/difbnd/)

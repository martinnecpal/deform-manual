---
lang: sk
title: "OTPRNG (2D3D)"
---

# OTPRNG

|  (Object Data)  
---|---  
_Update History:_ v11 – StopType 4 and 5 have been introduced for cogging simulation. |  Last updated on : 08-08-2013  
  
* * *

OTPRNG ObjNo, StopType, MinTemp, MaxTemp, TempStpCrit

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
ObjNo |  Object Number |  None  
StopType:  
|  Type of stopping = **0** Not activated = **1** Any nodal temperature = **2** All nodal temperatures = **4** Average of surface nodal temperatures or Max. nodal temperature (new in v11) = **5** Average of all nodal temperatures (new in v11) = **-n** Selected nodal temperature |   
Min Temp |  Lower bound of the temperature range |   
Max Temp |  Upper bound of the temperature range |   
TempStpCrit |  Type of temperature range = **0** Outside = **1** Inside  
|   
  
DEFINITION  
---  
OTPRNG specifies stopping criteria which stops the FEM simulation when temperature of the object meets the specified conditions established by StopType and TempStpCrit.  
  
REMARKS  
---  
TempStpCrit specifies the type of temperature range which works for this stopping criterion. For TempStpCrit=0, simulation stops if temperature is outside the range defined by minimum and maximum temperatures. For TempStpCrit=1, simulation stops if temperature is inside the range defined by minimum and maximum temperatures. For StopType=4, if average of surface temperatures drops below the lower bound or maximum temperature increases above the upper bound, then simulation stops. It is special thermal stopping condition for cogging reheat operation.  
  
RELATED TOPICS  
---  
Keywords: OPSTOP

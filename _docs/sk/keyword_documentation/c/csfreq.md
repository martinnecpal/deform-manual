---
lang: sk
title: "CSFREQ (2D3D)"
---

# CSFREQ

|  (Object Data)  
---|---  
|  Last updated on : 29-07-2013  
  
* * *

CSFREQ Object, Type(1 or 2), Value/NData

Time(1) Value(1)

...

Time(NData) Value(NData)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |   
Type |  Induction heating current source frequency type = **0** Constant = **1** f(time) = **2** Dual frequency, type = hot switching = **3** Dual frequency, type = combined |   
Value |  Frequency value if constant |   
NData |  Number of data for f(time) or**2** for dual frequency |   
CSFREQ Object, Type (=2 or 3), 2 Frequency 1, Weight 1 Frequency 2, Weight 2  
  
DEFINITION  
---  
CSFREQ specifies the induction heating current source frequency of an object. For single frequency case, Type=1 (or 2). For dual frequency case, Type=2 (or 3), and two sets of frequency/weight data are saved.  
  
RELATED TOPICS  
---  
Simulation Mode: Heat transfer, Heating, Induction Object Properties: [Induction Heating](/docs/sk/pre_processor/16_object_properties/16_6_heating_properties/) Keywords: [VOLCRG](/docs/sk/keyword_documentation/v/volcrg/)

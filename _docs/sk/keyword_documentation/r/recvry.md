---
lang: sk
title: "RECVRY (2D3D)"
---

# RECVRY

|  (Material Data)  
---|---  
|  Last updated on : 18-08-2014  
  
* * *

RECVRY Material, Ftype(=0), Recvry

or

RECVRY Material, Ftype(=1,2), Ndata

Temp/Strate(1), Recvry(1)

::

Temp/Strate(Ndata), Recvry(Ndata)

or

RECVRY Material, Ftype(=3), N1, N2

Temp(1) .. Temp(N1)

Strate(1) .. Strate(N2)

Recvry(1,1)

::

Recvry(N1, N2)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Material |  Material number |  None  
Ftype |  Function type **0** = Constant value **1** = f(temperature) **2******= f(strain-rate) **3** = f(temperature, strain-rate) |  None  
NumDis |  Constant Number of recovery factor value |  0.0  
N1 |  Number of data pairs for the function |  None  
N2 |  Number of data pairs for the function |  None  
Temp |  Temperature of (i)th data pair |  None  
Strate |  Strain-rate of (i)th data pair |  None  
Recvry(i) |  Number of recovery factor at (i)th data pair |  None  
Recvry(i,j) |  Number of recovery factor at (i,j)th data pair |  None  
  
DEFINITION  
---  
RECVRY specifies the recovery factor in the recovering term of the differential of dislocation density.  
  
REMARKS  
---  
The differential in dislocation density (increase or decrease) is given by, | ![]({{ '/assets/equations/keyword_documentation/n/ndisfm_eq_1.jpg' | relative_url }}) |   
---|---  
  
The recovering term is given in

![]({{ '/assets/equations/keyword_documentation/r/recvry_eq_2.jpg' | relative_url }}) |   
---|---  
  
[1] "A model of continuous dynamic recrystallization"; S. Gourdet, F. Montheillet. Acta Materialia 51 (2003) 2685–2699.  
  
Applicable object types: [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic)

RELATED TOPICS  
---  
Keywords:ALPHA, [BURGRS](/docs/sk/keyword_documentation/b/burgrs/), [NDISFM](/docs/sk/keyword_documentation/n/ndisfm/), [GBMOBI](/docs/sk/keyword_documentation/g/gbmobi/)

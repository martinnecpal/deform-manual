---
lang: sk
title: "NDISFM (2D3D)"
---

# NDISFM

|  (Material Data)  
---|---  
|  Last updated on : 18-08-2014  
  
* * *

NDISFM Material, Ftype(=0), NumDis

or

NDISFM Material, Ftype(=1,2), Ndata

Temp/Strate(1), NumDis(1)

::

Temp/Strate(Ndata), NumDis(Ndata)

or

NDISFM Material, Ftype(=3), N1, N2

Temp(1) .. Temp(N1)

Strate(1) .. Strate(N2)

NumDis(1,1)

::

NumDis(N1, N2)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Material |  Material number |  None  
Ftype |  Function type **0** = Constant value **1** = f(temperature) **2** = f(strain-rate) **3** = f(temperature, strain-rate) |  None  
NumDis |  Constant Number of dislocation families value |  0.0  
N1 |  Number of data pairs for the function |  None  
N2 |  Number of data pairs for the function |  None  
Temp |  Temperature of (i)th data pair |  None  
Strate |  Strain-rate of (i)th data pair |  None  
Alpha(i) |  Number of dislocation families at (i)th data pair |  None  
Alpha(i,j) |  Number of dislocation families at (i,j)th data pair |  None  
  
DEFINITION  
---  
NDISFM defines the "no. of dislocations" which specifies the number of "dislocation families" [1]  
  
REMARKS  
---  
The differential in dislocation density (increase or decrease) is given by, | ![]({{ '/assets/equations/keyword_documentation/n/ndisfm_eq_1.jpg' | relative_url }}) |   
---|---  
  
The hardening term is given in

![]({{ '/assets/equations/keyword_documentation/n/ndisfm_eq_2.jpg' | relative_url }}) |   
---|---  
  
[1] "A model of continuous dynamic recrystallization"; S. Gourdet, F. Montheillet. Acta Materialia 51 (2003) 2685–2699.

Applicable object types: Elasto plastic  
  
RELATED TOPICS  
---  
Keywords:ALPHA, [BURGRS](/docs/sk/keyword_documentation/b/burgrs/), [RECVRY](/docs/sk/keyword_documentation/r/recvry/), [GBMOBI](/docs/sk/keyword_documentation/g/gbmobi/)

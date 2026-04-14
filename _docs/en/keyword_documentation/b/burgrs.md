---
lang: en
title: "BURGRS (2D3D)"
---

# BURGRS

|  (Material Data)  
---|---  
|  Last updated on : 18-08-2014  
  
* * *

BURGRS Material, Ftype(=0), Burgrs

or

BURGRS Material, Ftype(=1,2,3), Ndata  
Temp/Stress/Concent(1), Burgrs(1)  
::   
Temp/Stress/Concent(Ndata), Burgrs(Ndata)

or

BURGRS Material, Ftype(=4,5,6), N1, N2  
Temp/Temp/Stress(1) .. Temp/Temp/Stress(N1)  
Stress/Concent/Concent(1) .. Stress/Concent/Concent(N2)  
Burgrs(1,1)   
::   
Burgrs(N1, N2)

or  
  
BURGRS Material, Ftype(=7)  
N1, N2, N3  
Temp(1) .. Temp(N1)  
Stress(1) .. Stress(N2)  
Concent(1) .. Concent(N3)  
Burgrs(1,1,1)   
::   
Burgrs(N1, N2, N3)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Material |  Material number |  None  
Ftype |  Function type **0** = Constant value **1** = f(temperature) **2** = f(stress) **3** = f(concentration) **4** = f(temperature, stress) **5** = f(temperature, concentration) **6** = f(stress, concentration) **7** = f(temperature, stress, concentration) |  None  
Burgrs |  Constant Burgers value | 0.0  
N1 |  Number of data pairs for the function |  None  
N2 |  Number of data pairs for the function |  None  
M3 |  Number of data pairs for the function |  None  
Temp |  Temperature of (i)th data pair |  None  
Stress |  Stress of (i)th data pair |  None  
Concent |  Concentration of (i)th data pair |  None  
Burgrs(i) |  Burgers value of (i)th data pair |  None  
Burgrs(i,j) |  Burgers value of (i,j)th data pair |  None  
Burgrs(i,j,k) |  Burgers value of (i,j,k)th data pair |  None  
  
DEFINITION  
---  
BURGRS defines the BURGERS vector, which represents the magnitude and direction of the lattice distortion resulting from a dislocation in a crystal lattice.  
  
REMARKS  
---  
The energy per dislocation can be defined as, | ![]({{ '/assets/equations/keyword_documentation/a/alpha_eq_1.jpg' | relative_url }}) |   
---|---  
  
[1] "A model of continuous dynamic recrystallization"; S. Gourdet, F. Montheillet. Acta Materialia 51 (2003) 2685–2699.

  
Applicable object types: Elastoplastic  
  
RELATED TOPICS  
---  
Keywords: [ALPHA](/docs/en/keyword_documentation/a/alpha/), [NDISFM](/docs/en/keyword_documentation/n/ndisfm/), [GBMOBI](/docs/en/keyword_documentation/g/gbmobi/), [RECVRY](/docs/en/keyword_documentation/r/recvry/)

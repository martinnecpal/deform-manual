---
lang: sk
title: "ALPHA (2D3D)"
---

# ALPHA

|  (Material Data)  
---|---  
|  Last updated on : 18-08-2014  
  
* * *

ALPHA Material, Ftype(=0), Alpha or ALPHA Material, Ftype(=1,2), Ndata  
Temp/Strate(1), Alpha(1)  
::   
Temp/Strate(Ndata), Alpha(Ndata) or ALPHA Material, Ftype(=3), N1, N2  
Temp(1) .. Temp(N1)  
Strate(1) .. Strate(N2)  
Alpha(1,1)   
::   
Alpha(N1, N2)

* * *  
  
---  
  
OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Type |  Output file type |  10  
FileName |  File name of converted 3D model |  M23_OUTPUT.KEY  
  
DEFINITION  
---  
**ACTOUT** specifies the type and name of the file that stores the converted 3D model after 2D to 3D object data conversion is complete.  
  
REMARKS  
---  
The energy per dislocation can be defined as, | ![]({{ '/assets/equations/keyword_documentation/a/alpha_eq_1.jpg' | relative_url }}) |   
---|---  
  
  
[1] "A model of continuous dynamic recrystallization"; S. Gourdet, F. Montheillet. Acta Materialia 51 (2003) 2685–2699.

Applicable object types: Elastoplastic  
  
RELATED TOPICS  
---  
Keywords: [BURGRS](/docs/sk/keyword_documentation/b/burgrs/), [NDISFM](/docs/sk/keyword_documentation/n/ndisfm/), [GBMOBI](/docs/sk/keyword_documentation/g/gbmobi/), [RECVRY](/docs/sk/keyword_documentation/r/recvry/)

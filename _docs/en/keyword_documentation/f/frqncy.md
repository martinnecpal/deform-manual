---
lang: en
title: "FRQNCY (2D3D)"
---

# FRQNCY

|  (Simulation control)  
---|---  
_Update History:_ (V11 - FRQNCY has been introduced.) |  Last updated on : 23-07-2013  
  
* * *

FRQNCY nRows, nCols

Freq_CNT(1), .. , Freq_CNT(nCols)

Freq_TMP(1), .. , Freq_TMP(nCols)

Freq_DBW(1), .. , Freq_DBW(nCols)

Freq_MXW(1), .. , Freq_MXW(nCols)

Freq_VEW(1), .. , Freq_VEW(nCols)

Freq_YLD(1), .. , Freq_YLD(nCols)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
nRows |  Row size of frequency data |   
nCols |  Column size of frequency data (=1) |   
Freq_CNT(i) |  Frequency of contact calculation = **-1** Contact search defined by Friction window = **n** Contact calculation at every nth step |   
Freq_TMP(i) |  Frequency of temperature calculation |   
Freq_DBW(i) |  Frequency of DB writing |   
Freq_MXW(i) |  Frequency of Maxwell equation solving |   
Freq_VEW(i) |  Frequency of view factor calculation |   
Freq_YLD(i) |  Frequency of yield surface calculation |   
  
DEFINITION  
---  
FRQNCY specifies the frequency of specific FEM computation.  
  
REMARKS  
---  
Freq_CNT is for contact calculation frequency for explicit FEM. When “-1” is specified, contact search will be executed at every step but its search area is limited within the area defined by friction window (3D only). Freq_TMP is for calculation frequency for temperature in explicit FEM (3D only). Freq_DBW is for calculation frequency for DB writing in explicit FEM (3D only). Freq_MXW is for calculation frequency for Maxwell equation solver in induction heating simulation. (2D and 3D) Freq_VEW is for calculation frequency for radiation view factor in thermal calculation. Freq_YLD is for calculation frequency for coupling between ODF (orientation distribution function) and Yield surface. The size of nCols is fixed as “1” as of v11 release. Thus, only one set of frequency values is allowed to define.  
  
RELATED TOPICS  
---  
Keywords: [SOLMTD (2D)](/docs/en/keyword_documentation/s/solmtd/), [SOLMTD (3D)](/docs/en/keyword_documentation/s/solmtd_3d/), [VFACTR (2D)](/docs/en/keyword_documentation/v/vfactr/), [VFACTR (3D)](/docs/en/keyword_documentation/v/vfactr_3d/) , [TXTODF](/docs/en/keyword_documentation/t/txtodf/), [ANISO](/docs/en/keyword_documentation/a/aniso/)

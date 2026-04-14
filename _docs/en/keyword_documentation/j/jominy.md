---
lang: en
title: "JOMINY (2D3D)"
---

# JOMINY

|  (Material data)  
---|---  
|  Last updated on : 07-08-2013  
  
* * *

JOMINY Matr, Itype, N1, N2

Atom(1) …Atom(Ndata)

Distance(1) … Distance( Ndata)

JOMINY(1) …JOMINY(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Matr |  Material Group |  None  
Itype |  Type of Curve =**1** Data Entry 1 |   
N1 |  Number of distance |  None  
N2 |  Number of atom content |  None  
  
DEFINITION  
---  
JOMINY defines the jominy curve for a mixture material group. The jominy curve is a determination of the hardness in the Jominy specimen at a specific distance from the cool end. Therefore, the jominy curve is useful in determining the hardenability of a material as a function of the distance from the water-cooled end. The hardenability of the material is estimated by using the data specified in HDNTIM and cooling time calculated in the heat transfer analysis. SYSTEM UNITS: JOMINY(ARBITRARY), DISTANCE (ARBITRARY), ATOM(WT%) Note: The units for Jominy and Distance are arbitrary but should be self-consist. The distance units in the cooling curve HDNTIM and the Jominy curve must match. EXAMPLE |  ATOM(%)/DISTANCE |  1 |  2 |  3  
---|---|---|---  
0.1 |  50 |  60 |  70  
0.2 |  80 |  90 |  100  
0.3 |  110 |  120 |  130  
  
JOMINY 1 1 3 3

0.1 0.2 0.3

1 2 3

50 80 110

60 90 120

70 100 130  
  
REMARKS  
---  
Applicable Simulation Types: Microstructure Module  
  
RELATED TOPICS  
---  
Material Data: [Hardness](/docs/en/pre_processor/10_material_data/10_7_hardness_data/10_7_hardness_data/) Keywords: [HDNEST](/docs/en/keyword_documentation/h/hdnest/), [HDNTIM](/docs/en/keyword_documentation/h/hdntim/),[HDNPHA](/docs/en/keyword_documentation/h/hdnpha/)

---
lang: sk
title: "HDNPHA (2D3D)"
---

# HDNPHA

|  (Material data)  
---|---  
|  Last updated on : 07-08-2013  
  
* * *

HDNPHA Mat, Type, N1 or Value, N2

if (Type=1,2,3)

Atom(1), Hardness(1)

Atom(N1), Hardness(N1)

else if (Type = 4)

Temp(1) .. Temp (N1)

Atom(1) .. Atom (N2)

Hardness(1) .. Hardness(N1xN2)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Mat |  Material Group Number |  None  
Type |  Kind of hardness of each phase =**0** Constant hardness =**1** Function of atom content =**2** Function of temperature =**3** Function of density =**4** Function of temperature and atom |  None  
  
DEFINITION  
---  
HDNPHA specifies the hardness of a material (or phase). The system units are dependent on the user. It should be reminded that the units used should be consist throughout the simulation for accurate interpretation of the results.  
  
REMARKS  
---  
Users should distinguish the hardness as a material property and the hardness as an object state variable. The hardness as an object state variable is defined by keyword HDNOBJ, which stores the output of the Hardness calculation module. HDNEST defines the computation method used in the Hardness calculation module. Note that the hardness of the object may not be related to the hardness of the material when, for example, the cooling time is used for estimating hardness. Applicable Simulation Modules: Microstructure Applicable Simulation Modes: Transformation Applicable Object Types: ALL Object types  
  
RELATED TOPICS  
---  
Material Data: [Hardness](/docs/sk/pre_processor/10_material_data/10_7_hardness_data/10_7_hardness_data/) Keyword: [HDNOBJ](/docs/sk/keyword_documentation/h/hdnobj/), [HDNEST](/docs/sk/keyword_documentation/h/hdnest/), [HDNTIM](/docs/sk/keyword_documentation/h/hdntim/), [JOMINY](/docs/sk/keyword_documentation/j/jominy/)

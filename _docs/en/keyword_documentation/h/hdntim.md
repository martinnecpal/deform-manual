---
lang: en
title: "HDNTIM (2D3D)"
---

# HDNTIM

|  (Material data)  
---|---  
|  Last updated on : 07-08-2013  
  
* * *

HDNTIM Matr, Npt,

Cooling Time(1) Distance(1)

: :

Cooling Time(Ndata) Distance(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Matr |  Material Number |  None  
Npt |  Number data for cooling time |  None  
  
DEFINITION  
---  
HDNTIM specifies the relation between cooling time and the distance from the water-cooling end of the specimen. It should be noted that the cooling time versus distance is only valid for a specific temperature difference (high-low temperature). DEFORM® does not interpolate the data if the user puts different data then the operation parameters, the resulting solution might be inaccurate. The distance is measured in terms of absolute length and not in terms of Jominy distance unit which is defined as 1/16 inch. EXAMPLE For material group #1 with 4 data pairs HDNTIM 1 4 0.0 0.2 1.0 0.5 2.0 0.7 3.0 0.8  
  
REMARKS  
---  
Applicable [simulation types](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#9.1.5._Simulation_modes_\(SMODE,_TRANS\)): Microstructure Module.  
  
RELATED TOPICS  
---  
Material Data: [Hardness](/docs/en/pre_processor/10_material_data/10_7_hardness_data/10_7_hardness_data/) Keyword: [HDNOBJ](/docs/en/keyword_documentation/h/hdnobj/), [HDNEST](/docs/en/keyword_documentation/h/hdnest/), [JOMINY](/docs/en/keyword_documentation/j/jominy/)

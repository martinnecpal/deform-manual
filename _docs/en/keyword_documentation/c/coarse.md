---
lang: en
title: "COARSE (2D3D)"
---

# COARSE

|  (Material data)  
---|---  
_Update History:_ (New keyword in v11) |  Last updated on : 29-07-2013  
  
* * *

COARSE Material, CoarsenType(=0) (for undefined)  
or   
COARSE Material, CoarsenType(=1) (for coarsening as a constant value)  
FuncType, CoarseFactor  
or   
COARSE Material, CoarsenType(=1) (for coarsening as a function of temp. & strain-rate)  
FuncType, NTemp, NStrate  
Temp(1), ..., Temp(NTemp)  
Strate(1), ..., Strate(NStrate)  
Factor(1, 1), ..., Factor(NTemp, 1)  
: :  
Factor(1, NStrate), ..., Factor(NTemp, NStrate)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Material |  Material number |  None  
CoarsenType |  Coarsening model type  =**0** None = **1** Static/dynamic coarsening |  0  
FuncType |  Coarsening function type  = **0** Constant = **5** Function of temperature and strain-rate |  0  
CoarseFactor |  Coarsening factor value |  0  
NTemp |  Number of temperature data |   
NStrate |  Number of strain-rate data |   
Temp(i) |  Temperature of ith data |   
Strate(i) |  Strain-rate of ith data |   
Factor(i,j) |  Coarsening factor of ith and jth data |   
  
DEFINITION  
---  
COARSE specifies the static/dynamic coarsening behavior of particle.  
  
REMARKS  
---  
In superplastic forming, superplastic materials (Aluminum and Titanium alloys) can withstand large amount of elongation (mostly by grain boundary sliding) well beyond necking points of conventional alloys. Since SPF processing is usually under high temperatures and has long processing time, alpha particles usually undergo significant coarsening. There is a driving force for coarsening of the precipitates. The reason for this is that smaller particles have a higher solubility than larger particles. Due to the concurrent deformation, it’s called dynamic coarsening and different than the static coarsening. The dynamic coarsening is much faster than static coarsening because of the diffusion through dislocations. The mechanism for coarsening is diffusion, hence the kinetics follow an Arrhenius law. The dynamic coarsening follows cube rule. The unit for coarsening factor K is micron^3/hour for SI system. Applicable object types: [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic) Applicable simulation type: Superplastic forming  
  
RELATED TOPICS  
---  
Keywords: [GBMOBI](/docs/en/keyword_documentation/g/gbmobi/), [GBENGY](/docs/en/keyword_documentation/g/gbengy/)

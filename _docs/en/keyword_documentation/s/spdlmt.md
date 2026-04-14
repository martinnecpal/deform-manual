---
lang: en
title: "SPDLMT (2D3D)"
---

# SPDLMT

|  (Object Data)  
---|---  
|  Last updated on : 09-08-2013  
  
* * *

SPDLMT Object, Ndata, AcclCoef, DwellTime

Force(1), Speed(1)

: : :

Force(Ndata), Speed(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
NData |  No. of Data Pairs |  None  
Force(i) |  Force of ith data set |  None  
Speed(i) |  Speed of ith data set |  None  
AcclCoef |  Acceleration coefficient |  0  
DwellTime |  Dwell time after maximum load is reached |  0  
  
DEFINITION  
---  
SPDLMT This keyword is to incorporate the press limit into the simulation. The keyword is represented by a Force-Speed curve that is used as an upper bound of the die speed with the given die force. Acclcoef specifies the acceleration coefficient of the die. It is zero by default, meaning that the press will never increase speed. DwellTime specifies the dwell time after the maximum load is reached. The simulation is load-controled during dwell, when workpiece may deform due to creep.  
  
REMARKS  
---  
This keyword is intended as a Control Modifier for the primary die movement control. For example: when the specified speed exceeds the capacity of the press (typically for hydraulic presses), this control will take over and represent the actual velocity degradation seen in production. When this keyword is used, the [VMIN](/docs/en/keyword_documentation/v/vmin/) or LMAX can be used to stop the simulation at "stall off". Applicable object types: [Rigid](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.5._Rigid).  
  
RELATED TOPICS  
---  
Movement Controls: [Hydraulic Press](/docs/en/pre_processor/15_movement_controls_definition/15_6_hydraulic_press/) Related keywords: [MOVCTL (2D)](../m/movctl_\(2d\).htm),[MOVCTL (3D)](../m/movctl_\(3d\).htm) , [VMIN](/docs/en/keyword_documentation/v/vmin/), [LMAX (2D)](/docs/en/keyword_documentation/l/lmax/), [LMAX (3D)](/docs/en/keyword_documentation/l/lmax_3d/)

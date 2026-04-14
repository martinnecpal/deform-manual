---
lang: en
title: "CNVCOF (2D3D)"
---

# CNVCOF

|  (Simulation control)  
---|---  
|  Last updated on : 29-07-2013  
  
* * *

CNVCOF Ftype, Cnvcof or CNVCOF Ftype, Ndata  
Temp(1), Cnvcof(1)  
: :  
Temp(Ndata), Cnvcof(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Ftype |  Function type: **0** = Constant convection coefficient **1** = Temperature dependent convection coefficient |  0  
Cnvcof |  Convection coefficient |  0.02 (N/sec/mm/C) Or  0.77E-05 (Btu/sec/in2/F)  
Ndata |  Number of temp/convection coeff data pairs |  None  
Temp(i) |  Temperature of ith data pair |  None  
Cnvcof(i) |  Convection coefficient of ith data pair |  None  
  
DEFINITION  
---  
CNVCOF specifies the convection coefficient that is used in determining convection heat transfer.  
  
REMARKS  
---  
The convection coefficient may be specified as a constant value or as a set of discrete temperature/coefficient data pairs. If Ftype = 1 use the operand Cnvcof. If Ftype = 2 use the operands Ndata, Temp(i), Cnvcof(i). Each temperature/coefficient pair should be provided on a separate line. When temperatures lie within the specified data range, linear interpolation is used to determine the convection coefficient. When temperatures lie outside the specified data range, linear extrapolation is used to determine the convection coefficient. The default values represent free air convection. Free air and forced air convection coefficient ranges are listed below [2].  
  
Mode |  Btu/sec/in2/F |  N/sec/mm/C  
---|---|---  
Free air convection |  1.93 x 10-6 ~ 9.645 x 10-6 |  5 x 10-3 ~ 25 x 10-3  
Forced air convection |  3.86 x 10-6 ~ 192.9 x 10-6 |  10 x 10-3 ~ 500 x 10-3  
  
The equation for convection heat transfer is: 

![]({{ '/assets/equations/keyword_documentation/c/cnvcof_eq_1.jpg' | relative_url }}) |   
---|---  
  
Applicable simulation types: Heat Transfer

Non-Isothermal Deformation

RELATED TOPICS  
---  
Keywords: [ENVTMP](/docs/en/keyword_documentation/e/envtmp/)

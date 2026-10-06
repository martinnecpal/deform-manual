---
lang: sk
title: "SMAX (2D3D)"
---

# SMAX

|  (Simulation control)  
---|---  
|  Last updated on : 09-08-2013  
  
* * *

SMAX MaxStroke

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
MaxStroke |  Maximum stroke of the primary object |  0.0  
  
DEFINITION  
---  
SMAX terminates a simulation when the stroke of the primary object reaches MaxStroke.  
  
REMARKS  
---  
SMAX is one of several parameters used to control the termination of the simulation. Other keywords which effect simulation termination include: EMAX, LMAX, NSTEP, TMAX, VMIN. When the criteria specified in any of these keywords has been met, the simulation will terminate. If MaxStroke = 0, SMAX will not be used as a termination condition. Applicable simulation types: Isothermal Deformation Non-Isothermal Deformation  
  
RELATED TOPICS  
---  
[Stopping Controls]({{ '/docs/sk/pre_processor/9_simulation_controls/9_3_stopping_controls/' | relative_url }}) Keywords: [EMAX]({{ '/docs/sk/keyword_documentation/e/emax/' | relative_url }}), [LMAX (2D)]({{ '/docs/sk/keyword_documentation/l/lmax/' | relative_url }}), [LMAX (3D)]({{ '/docs/sk/keyword_documentation/l/lmax_3d/' | relative_url }}) , [NSTEP]({{ '/docs/sk/keyword_documentation/n/nstep/' | relative_url }}), [TMAX]({{ '/docs/sk/keyword_documentation/t/tmax/' | relative_url }}), [VMIN]({{ '/docs/sk/keyword_documentation/v/vmin/' | relative_url }})

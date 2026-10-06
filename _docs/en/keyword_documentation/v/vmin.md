---
lang: en
title: "VMIN (2D3D)"
---

# VMIN

|  (Simulation control  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

VMIN MinVel

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
MinVel |  Minimum primary object velocity |  0.0  
  
DEFINITION  
---  
VMIN terminates a simulation when the velocity of the primary object reaches MinVel.  
  
REMARKS  
---  
VMIN is one of several parameters used to control the termination of the simulation. Other keywords which effect simulation termination include: [EMAX]({{ '/docs/en/keyword_documentation/e/emax/' | relative_url }}), LMAX, [NSTEP]({{ '/docs/en/keyword_documentation/n/nstep/' | relative_url }}), [SMAX]({{ '/docs/en/keyword_documentation/s/smax/' | relative_url }}), [TMAX]({{ '/docs/en/keyword_documentation/t/tmax/' | relative_url }}). When the criteria specified in any of these keywords has been met, the simulation will terminate. Generally, VMIN is used when the movement control of the primary object is stroke or load specified. If MinVel = 0, VMIN will not be used as a termination condition. Applicable simulation types: Isothermal Deformation Non-Isothermal Deformation  
  
RELATED TOPICS  
---  
[Stopping parameters]({{ '/docs/en/pre_processor/9_simulation_controls/9_3_stopping_controls/' | relative_url }}),[ Movement controls]({{ '/docs/en/pre_processor/15_movement_controls_definition/15_movement_controls_settings/' | relative_url }}), [Primary object]({{ '/docs/en/pre_processor/9_simulation_controls/9_2_defining_step/' | relative_url }}#Primary_die_\(PDIE\)) Keywords: [EMAX]({{ '/docs/en/keyword_documentation/e/emax/' | relative_url }}), LMAX, [NSTEP]({{ '/docs/en/keyword_documentation/n/nstep/' | relative_url }}), [SMAX]({{ '/docs/en/keyword_documentation/s/smax/' | relative_url }}), [TMAX]({{ '/docs/en/keyword_documentation/t/tmax/' | relative_url }}).

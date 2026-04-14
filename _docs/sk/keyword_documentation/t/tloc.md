---
lang: sk
title: "TLOC (2D3D)"
---

# TLOC

|  (Action keyword)  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

TLOC Local Time

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Local Time |  Incremental time span for next simulation |  0.0 (initial run)  
  
DEFINITION  
---  
TLOC is an action keyword which specifies the time span next simulation should last. It actually assign the sum of current time and next simulation time span to TMAX (global time stopping criteria): TMAX = TNOW + TLOC. This is very useful in multiple simulations.  
  
REMARKS  
---  
Applicable simulation types: Isothermal Deformation, Heat Transfer, Non-Isothermal Deformation  
  
RELATED TOPICS  
---  
Keywords: [TMAX](/docs/sk/keyword_documentation/t/tmax/), [TNOW](/docs/sk/keyword_documentation/t/tnow/)

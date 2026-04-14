---
lang: sk
title: "TMPLIQ (2D3D)"
---

# TMPLIQ

|  (Inter Material data)  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

TMPLIQ n, tmpliq

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
n |  Material number |  None  
tmpliq |  Temperature at which phase transformation is completed when material temperature increases. |  None  
  
DEFINITION  
---  
TMPLIQ is used to describe the temperature at which phase transformation is completed.  
  
REMARKS  
---  
When a material is heated, then phase transformation starts at tmpsol (see keyword [TMPSOL](/docs/sk/keyword_documentation/t/tmpsol/)) and it is completed at tmpliq. Here, it is assumed that tmpsol < tmpliq. If [LATENT](/docs/sk/keyword_documentation/l/latent/) is set to zero, then this keyword is ignored.  
  
RELATED TOPICS  
---  
[Inter-Material Data](/docs/sk/pre_processor/10_material_data/10_9_transformation_data/10_9_transformation_data/) Keywords: [TMPSOL](/docs/sk/keyword_documentation/t/tmpsol/),[LATENT](/docs/sk/keyword_documentation/l/latent/), [TRANS](/docs/sk/keyword_documentation/t/trans/)

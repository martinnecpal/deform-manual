---
lang: sk
title: "TMPSOL (2D3D)"
---

# TMPSOL

|  (Inter Material data)  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

TMPSOL n, tmpsol

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
n |  Material number |  None  
tmpsol |  Temperature at which phase transformation starts when material temperature increases. |  None  
  
DEFINITION  
---  
TMPSOL is used to describe the temperature at which phase transformation starts when material temperature increases.  
  
REMARKS  
---  
When a material is heated, then phase transformation starts at tmpsol and it is completed at tmpliq. Here, it is assumed that tmpsol < tmpliq. If [LATENT]({{ '/docs/sk/keyword_documentation/l/latent/' | relative_url }}) is set to zero, then this keyword is ignored.  
  
RELATED TOPICS  
---  
[Inter-Material Data]({{ '/docs/sk/pre_processor/10_material_data/10_9_transformation_data/10_9_transformation_data/' | relative_url }}) Keywords: [TMPLIQ]({{ '/docs/sk/keyword_documentation/t/tmpliq/' | relative_url }}), [LATENT]({{ '/docs/sk/keyword_documentation/l/latent/' | relative_url }}), [TRANS]({{ '/docs/sk/keyword_documentation/t/trans/' | relative_url }})

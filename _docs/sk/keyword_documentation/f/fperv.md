---
lang: sk
title: "FPERV (2D)"
---

# FPERV

|  (Material data)  
---|---  
|  Last updated on : 05-08-2013  
  
* * *

FPERV Material, BodyFor(Ndata1), CentFor(Ndata2), Ftype

(if Ftype = 1)

Time(1), BodyFor(1)

::

Time(Ndata1), BodyFor(Ndata1)

(if Ftype = 2)

Time(1), CentFor(1)

::

Time(Ndata2), CentFor(Ndata2)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Material |  Material group number |   
BodyFor |  Body force = Constant value = Ndata |   
CentFor |  Centrifugal force = Constant value = Ndata |   
Ftype |  Type of data = **0** Constant values = **1** Function data for Body force = **2** Function data for Centrifugal force = **3** Function data Body & Centrifugal forces |   
  
DEFINITION  
---  
BodyFor allows for the weight of the material to be considered in the sintering simulation for the porous material. CentFor makes possible to consider the effect of centrifugal force when centrifugal loading problem such as in rotating annular disc.  
  
REMARKS  
---  
The following equation is used to calculate the body force for porous materials. | ![]({{ '/assets/equations/keyword_documentation/f/fperv_eq_1.jpg' | relative_url }}) |   
---|---  
  
DENSTY is defined under elements.

User has to assign ![]({{ '/assets/equations/keyword_documentation/f/rho_g.jpg' | relative_url }}) for the body force term and ![]({{ '/assets/equations/keyword_documentation/f/rho_omega_square.jpg' | relative_url }}) for the centrifugal force term.  
  
RELATED TOPICS  
---  
Step parameters Keyword: DENSTY

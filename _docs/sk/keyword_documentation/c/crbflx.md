---
lang: sk
title: "CRBFLX (2D3D)"
---

# CRBFLX

|  (Simulation Control)  
---|---  
|  Last updated on : 29-07-2013  
  
* * *

CRBFLX Object, Ndata, DefFlux

Node(1), Flux(1)

: :

Node(Ndata), Flux(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Ndata |  Number of node/flux pairs |  None  
DefFlux |  Default distributed nodal atom flux of all nodes not listed in the node/flux pairs with diffusion boundary constraint code 3 |  0  
Node(i) |  Node number of ith data pair |  None  
Flux(i) |  Distributed nodal atom flux of ith data pair |  0  
  
DEFINITION  
---  
CRBFLX specifies "carbon flux" or atom flux for the surface of work.  
  
REMARKS  
---  
Applicable object types: Rigid, Elastic, Plastic, Elastoplastic, and Porous.  
  
RELATED TOPICS  
---  
Boundary constraints, Inter-object contact Keywords: [DATOM](/docs/sk/keyword_documentation/d/datom/), [BCCCRB(2D)](/docs/sk/keyword_documentation/b/bcccrb/), .[BCCCRB(3D)](/docs/sk/keyword_documentation/b/bcccrb_3d/)

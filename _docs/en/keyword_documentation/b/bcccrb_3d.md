---
lang: en
title: "BCCCRB (3D)"
---

# BCCCRB

|  (Object Data)  
---|---  
|  Last updated on : 12-08-2013  
  
* * *

BCCCRB Object, Ndata, DefBCAtom  
Node(1), BCAtom(1)  
: :  
Node(Ndata), BCAtom(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Ndata |  Number of node/boundary constraint data pairs |  None  
DefBCAtom |  Default diffusion boundary constraint code of all nodes not listed in node/boundary constraint data pairs |  None  
Node(i) |  Node number of ith data pair |  None  
BCAtom(i) |  Diffusion boundary constraint code of ith data pair |  None  
  
DEFINITION  
---  
BCCCRB specifies the prescribed atom content for the surface of the workpiece.  
  
REMARKS  
---  
BCCCRB specifies the atom content at the surface for the entire simulation. Therefore, BCCCRB is identical to setting the environment atom content. The advantage of using the prescribed atom content is that it is easy and quicker to set the boundary condition for a particular object. If a user specifies the BCCCRB then it is not necessary to define the environment conditions in regards to atom content. It should be noted that the surface nodes should be only selected when using this keyword. An example of implementation of the process is shown below. If the surface nodes are specified with an atom content of 0.3 and D is the distance in an object then: Applicable Simulation Modules: Microstructure Applicable Simulation Modes: Diffusion Applicable object types: ALL except Rigid  
  
RELATED TOPICS  
---  
[Boundary constraints](/docs/en/pre_processor/14_boundary_conditions/14_boundary_conditions/), [Inter-object contact](/docs/en/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/) Keywords: [DATOM](/docs/en/keyword_documentation/d/datom/), [CRBFLX](/docs/en/keyword_documentation/c/crbflx/)

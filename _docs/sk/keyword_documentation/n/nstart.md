---
lang: sk
title: "NSTART (2D3D)"
---

# NSTART

|  (Simulation control)  
---|---  
|  Last updated on : 08-08-2013  
  
* * *

NSTART Step#

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Step# |  Starting step number |  -1 (initial run)  
  
DEFINITION  
---  
NSTART specifies the current simulation step number. When a database is run, NSTART will be the starting step number of the simulation.  
  
REMARKS  
---  
In DEFORM a negative step number designates that the step number is used as input for a simulation run. Step# must always be a negative number. For initial runs Step# = -1. For remeshing runs, Step# should be the negative value of the next step following the remeshed step. For example, if a problem had run 42 steps and was then remeshed, Step# = -43. For continuing runs, Step# should be the negative of the next sequential step. For example if a problem had run 26 steps and was resubmitted as a continuing run, Step# = -27. Applicable simulation types: Isothermal Deformation, Heat Transfer, Non-Isothermal Deformation  
  
RELATED TOPICS  
---  
[DEFORM database](/docs/sk/pre_processor/21_database_generation/21_database_generation/)

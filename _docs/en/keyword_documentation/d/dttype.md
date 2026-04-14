---
lang: en
title: "DTTYPE (2D3D)"
---

# DTTYPE

|  (Simulation control)  
---|---  
|  Last updated on : 30-07-2013  
  
* * *

DTTYPE Ftype (=0), Ndata (=0)

or

DTTYPE Ftype (=1), Ndata

Time(1), DSMax(1)

::

Time(Ndata), DSMax(Ndata)

or

DTTYPE Ftype (=2), Ndata

Stroke(1), DSMax(1)

::

Stroke(Ndata), DSMax(Ndata)

or

DTTYPE Ftype (=3), Ndata

Time(1), DTMax(1)

::

Time(Ndata), DSMax(Ndata)

or

DTTYPE Ftype (=4), Ndata

Stroke(1), DTMax(1)

::

Stroke(Ndata), DTMax(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Ftype |  Function type of DTTYPE = **0** Constant - DSMAX or DTMAX will be used = **1** Function of time for variable DSMAX = **2** Function of stroke for variable DSMAX = **3** Function of time for variable DTMAX = **4** Function of stroke for variable DTMAX |  0  
  
DEFINITION  
---  
DTTYPE allows a user defining an analysis step size in FEM as a function of “time” or “stroke”. Since the step definition available in DEFORM 2D are time increment and displacement increment, four different combinations are possible for a user-defined time stepping technique.  
  
REMARKS  
---  
During a forging type of simulation, as height of the billet reduces, a constant time step (or stroke increment) may become too large relatively to properly describe the deformation behavior (i.e., a rapid flash formation) toward the end of operation. The user-defined time stepping provides flexibility in discretizing finite element model over the time space. If user is already familiar with the process and clearly knows the specific time period where higher simulation accuracy is mandatory, he can setup function data for the most desirable time stepping. This will help reducing CPU time and maintaining good simulation accuracy.  
  
RELATED TOPICS  
---  
[Step Definition](/docs/en/pre_processor/9_simulation_controls/9_2_defining_step/) Keyword: [STEPDEF](/docs/en/keyword_documentation/s/stpdef/), [DTMAX](/docs/en/keyword_documentation/d/dtmax/), [DSMAX](/docs/en/keyword_documentation/d/dsmax/)

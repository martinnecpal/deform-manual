---
lang: en
title: "HITSRC (3D)"
---

# HITSRC

|  (Simulation Control )  
---|---  
_Update History:_ V11.1 - HITSRC has been introduced. |  Last updated on : 21-05-2016  
  
* * *

HITSRC Heat#, HeatType, TrajectoryType, OrientationType, MagnitudeType

{Trajectory Data} (Function of time or Object number)

{Orientation Data} (Constant or Function of time)

{Magnitude Data} (Constant or Function of time)

{Heat source parameters}

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Heat# |  Heat source number |  None  
HeatType |  Heat source type =**1:** 2D surface Gaussian  =**2** : 3D conical Gaussian =**3** : Double ellipsoid |  None  
TrajectoryType |  Trajectory type =**1** Function of time  =**2** Follow object |  None  
OrientationType |  Orientation type =**0** Constant =**1** Function of time |  None  
MagnitudeType |  Magnitude type =**0** Constant =**1** Function of time |  None  
{Trajectory Data} |  Data for the trajectory if TrajectoryType is **1** : function data if TrajectoryType is **2** : object number |  None  
{Orientation Data} |  Data for the trajectory if TrajectoryType is **0** : Vx, Vy Vz if TrajectoryType is **1** : function data |  None  
{Magnitude Data} |  Data for the magnitude if TrajectoryType is **0** : Magnitude if TrajectoryType is **1** : function data |  None  
{Heat source parameters} |  Parameters for the heat source if HeatType is 1: Par1, Par2 if HeatType is 2: Par1, Par2, Par3, Par4, Par5 if HeatType is 3: Par1, Par2, Par3, Par4, Par5, Par6 |  None  
  
DEFINITION  
---  
HITSRC specifies heat source information.  
  
REMARKS  
---  
The heat source is still under development.  
  
RELATED TOPICS  
---  
None

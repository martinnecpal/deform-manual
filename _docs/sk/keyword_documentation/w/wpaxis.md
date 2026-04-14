---
lang: sk
title: "WPAXIS (2D)"
---

# WPAXIS

|  (Object data - 2D)  
---|---  
_Update History:_ (New) Definition has been extended in v11 |  Last updated on : 24-07-2013  
  
* * *

(AxisType = 5, Gravity)

WPAXIS Object, AxisNo, AxisType(=5) 

Direction_X, Direction_Y

Gravity

(AxisType = 6, Centrifugal force)

WPAXIS Object, AxisNo, AxisType(=6)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
AxisNo |  Axis number |  None  
AxisType |  Axis type = **5** Gravity (new in v11) = **6** Centrifugal force - “On” (new in v11) |   
Direction_X |  Direction of gravity in X |   
Direction_Y |  Direction of gravity in Y |   
Gravity |  (AxiType = 5) Acceleration of gravity  |  0  
  
DEFINITION  
---  
WPAXIS specifies the gravity and centrifugal force during deformation analysis. When translational or rotational movement is specified, the effect of gravity or centrifugal force will be considered in the simulation.  
  
REMARKS  
---  
A corresponding material data keyword [MASDEN](/docs/sk/keyword_documentation/m/masden/), introduced in v10.2 release, which defines mass density, is used together in FEM calculation.  
  
RELATED TOPICS  
---  
Related keywords: [MASDEN](/docs/sk/keyword_documentation/m/masden/), [FPERV(3D)](/docs/sk/keyword_documentation/f/fperv_3d/)

---
lang: en
title: "WPAXIS (3D)"
---

# WPAXIS

|  (Object data - 3D)  
---|---  
_Update History:_ (V11 - WPAXIS has been introduced. V11.1 - WPAXIS has been extended to include brick meshing (Type =9) and object positioning (Type =8). |  Last updated on : 12-10-2023  
  
* * *

The workpiece axis property can be governed by specifying various axis type as shown in the table.

**v11** |  **Axis Type** |  **No (Axis Type)**  
---|---|---  
|  Revolving (3D only) |  0  
|  Extruding (3D only) |  1  
|  Rotation sweeping (3D only) |  2  
|  Axis Reference Point (3D only) |  3  
|  2D to 3D Conversion (3D only) |  4  
New in v11 |  Gravity (both 2D, 3D) |  5  
New in v11 |  Centrifugal Force (both 2D, 3D) |  6  
New in v11 |  Enforce Rigid Zone around a given axis (in cogging) This is to replace the use of AXIS.DAT |  7  
New in v11 |  Object positioning (3D only) |  8  
New in v11 |  Brick remeshing ( 3D only) |  9  
  
* * *

DEFINITION  
---  
WPAXIS specifies the object axis property information for various usages.  
  
REMARKS  
---  
WPAXIS AxisType =0 (or =2) specifies the revolving mesh information used in ring rolling, shape rolling, flow forming, and cogging. WPAXIS AxisType =1 specifies the extrusion mesh information used in extrusion, shape rolling, and cogging. WPAXIS AxisType =3 specifies two points on the workpiece that deform with the workpiece and is used during stopping criteria checks with manipulator positions during cogging. WPAXIS AxisType =4 specifies the 2D to 3D model conversion related information. WPAXIS AxisType = 5 specifies the gravity during deformation analysis. When translational movement is specified, the effect of gravity will be considered in the simulation if WPAXIS type=5 presents in the object data. A corresponding material data keyword MASDEN, introduced in v10.2 release, which defines mass density, is used together in FEM calculation. WPAXIS AxisType = 6 specifies the centrifugal force during deformation analysis. When rotational movement is specified, the effect of centrifugal force will be considered in the simulation if WPAXIS type=5 presents in the object data. A corresponding material data keyword MASDEN, introduced in v10.2 release, which defines mass density, is used together in FEM calculation. WPAXIS Axistype =7 is to enforce a rigid zone around a given axis which is used during cogging. Manipulator numbers required for coupling the velocities and also during spring calculations. This is also used to replace the use of AXIS.DAT file with flag (=9) - enforce rigid zone around a given axis.  
  
RELATED TOPICS  
---  
Related keywords: [MASDEN](/docs/en/keyword_documentation/m/masden/), [FPERV (3D)](/docs/en/keyword_documentation/f/fperv_3d/)  
  
Revolving / Rotation Sweep (AxisType = 0, 2)

* * *

WPAXIS Object, AxisNo, AxisType(=0,2), RotType 

CenterX, CenterY, CenterZ

AxisX, AxisY, AxisZ

Radius, AngVel, Spd1, Spd2

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
AxisNo |  Axis number |  None  
AxisType |  Axis type =**0** Revolving = **2** Rotation Sweep |  None  
RotType |  Rotation type (when AxisType = 0) =**0** Controlled angular velocity (when AxisType = 0) =**1** Free rotation (when AxisType = 0) |  None  
CenterX |  Rotation Center in X |  0.0  
CenterY |  Rotation Center in Y |  0.0  
CenterZ |  Rotation Center in Z |  0.0  
AxisX |  Direction of Axis in X |  0.0  
AxisY |  Direction of Axis in Y |  0.0  
AxisZ |  Direction of Axis in Z |  0.0  
Radius |  Radius |  0.0  
AngVel |  Angular Velocity |  0.0  
Spd1 |  Speed of Start Point |  0.0  
Spd2 |  Speed of End Point |  0.0  
  
Extrusion (AxisType = 1)

* * *

WPAXIS Object, AxisNo, AxisType(=1), RotType 

StartX, StartY, StartZ

EndX, EndY, EndZ

Radius, AngVel, Spd1, Spd2

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
AxisNo |  Axis number |  None  
AxisType |  Axis type = **1** Extrusion |  None  
RotType |  Rotation type |  None  
StartX |  Start Position in X |  0.0  
StartY |  Start Position in Y |  0.0  
StartZ |  Start Position in Z |  0.0  
EndX |  End Position in X |  0.0  
EndY |  End Position in Y |  0.0  
EndZ |  End Position in Z |  0.0  
Radius |  Radius |  0.0  
AngVel |  Angular Velocity |  0.0  
Spd1 |  Speed of Start Point |  0.0  
Spd2 |  Speed of End Point |  0.0  
  
Axial Reference Point (AxisType = 3)

* * *

WPAXIS Object, AxisNo, AxisType(=3), AxialRefPointNo 

StartX, StartY, StartZ

EndX, EndY, EndZ

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
AxisNo |  Axis number |  None  
AxisType |  Axis type =3 Axial Reference Position |  None  
AxialRefPointNo |  Axial Reference Point No |  0  
StartX |  Start Position in X |  0.0  
StartY |  Start Position in Y |  0.0  
StartZ |  Start Position in Z |  0.0  
EndX |  End Position in X |  0.0  
EndY |  End Position in Y |  0.0  
EndZ |  End Position in Z |  0.0  
  
Conversion (2D to 3D) (AxisType = 4) (Extrude type)

* * *

WPAXIS Object, AxisNo, AxisType(=4) , ModelType(=2), DensityFlag, CrossSectionPlane, ErrorDist

StartX, StartY, StartZ

EndX, EndY, EndZ

Dummy, Dummy, Dummy

Dummy, Dummy, ExtrudeLayers

Ftype, Ndata

Distance(1), Density(1)

::

Distance(Ndata), Density(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
AxisNo |  Axis number |  None  
AxisType |  Axis type =**4** 2D to 3D Conversion |  None  
ModelType |  Model type (**0** \- Partial revolve) (**1** \- Full Revolve) **2** \- Extrude |  2  
DensityFlag |  Density flag 0 - Variable density data (not available) 1 - Variable density data (available) |  1  
CrossSectionPlane |  Cross section plane  **1** \- XY plane **2** \- YZ plane **3** \- ZX plane |  1  
ErrorDist |  Digitization error distance |  0.0  
StartX |  Start position in X |   
StartY |  Start position in Y |   
StartZ |  Start position in Z |   
EndX |  End position in X |   
EndY |  End position in Y |   
EndZ |  End position in Z |   
ExtrudeLayers |  Number of Extruded layers |   
Ftype |  Function type **0** \- Uniform **1** \- Finer |   
Ndata |  Number of data pairs |   
Distance(i) |  Normalized distance of ith data pair |   
Density(i) |  Number of layers of ith data pair |   
  
Conversion (2D to 3D) (AxisType = 4) (Revolve type) 

* * *

WPAXIS Object, AxisNo, AxisType(=4) , ModelType(=0,1), DensityFlag, CrossSectionPlane, ErrorDist

R-VectorX, R-VectorY, R-VectorZ

Z-VectorX, Z-VectorY, Z-VectorZ

O-CoordX, O-CoordY, O-CoordZ

RotationAngle, StartAngle, RevolveSections

Ftype, Ndata

(For Ftype > 0)

Angle(1), Density(1)

::

Angle(Ndata), Density(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
AxisNo |  Axis number |  None  
AxisType |  Axis type =**4** 2D to 3D Conversion |  None  
ModelType |  Model Type (= 0 or 1) **0** \- Partial revolve **1** \- Full revolve (**2** \- Extrude) |  0  
DensityFlag |  Density Flag 0 - Variables density data (not available) 1 - Variable density data (available) |  1  
CrossSectionPlane |  Cross Section Plane  **1** \- XY plane **2** \- YZ plane **3** \- ZX plane |  1  
ErrorDist |  Digitization Error Distance |  0.0  
R-Vector |  Reference vector  |   
Z-Vector |  Revolve vector, where angle = 0 |   
O-Coord |  Revolve origin |   
RotationAngle |  Revolve angle |   
StartAngle |  Revolve start angle |   
**RevolveSections** |  Number of revolved sections |   
**Ftype** |  Function type **0** \- Uniform **1** \- Finer |   
**Ndata** |  Number of data pairs |   
**Angle(i)** |  Normalized angle of ith data pair |   
**Density(i)** |  Number of sections of ith data pair |   
  
Gravity / Centrifugal Force (AxisType = 5, 6)

* * *

(AxisType = 5, Gravity)

WPAXIS Object, AxisNo, AxisType(=5) 

Direction_X, Direction_Y,

Gravity

(AxisType = 6, Centrifugal force)

WPAXIS Object, AxisNo, AxisType(=6)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
AxisNo |  Axis number |  None  
AxisType |  Axis type =**5** Gravity (new in v11) =**6** Centrifugal force - “On” (new in v11) |  None  
Direction_X |  Direction of gravity in X |  0.0  
Direction_Y |  Direction of gravity in Y |  0.0  
Direction_Z |  Direction of gravity in Z |  0.0  
Gravity |  (AxiType=5) Acceleration of gravity  |  0.0  
  
Enforcing Rigid Zone (AxisType = 7)

* * *

WPAXIS Object, AxisNo, AxisType(=7)

AxiDirX, AixDirY, AxiDirZ

AxiOriX, AxiOriY, AxiOriZ

Radius, ManipObjNo1, ManipObjNo2, StartAxialPos, EndAxialPos

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
AxisNo |  Axis number |  None  
AxisType |  Axis type =**7** Enforcing Rigid Zone (new in v11) |  None  
AxiDirX |  Direction of Axis in X |  1.0  
AxiDirY |  Direction of Axis in Y |  0.0  
AxiDirZ |  Direction of Axis in Z |  0.0  
AxiOriX |  Origin of Axis in X |  0.0  
AxiOriY |  Origin of Axis in Y |  0.0  
AxiOriZ |  Origin of Axis in Z |  0.0  
Radius |  Radius |  0.0  
ManipObjNo1 |  Object no. of Manipulator 1  |  0.0  
ManipObjNo2 |  Object no. of Manipulator 2 |  0.0  
StartAxialPos |  Start Axial Position |  0.0  
EndAxialPos |  End Axial Position |  0.0  
  
REMARKS  
---  
The starting and ending axial positions StartAxialPos, EndAxialPos is used to apply constraint.  
  
( AxisType=8 , Object Positioning ) 

* * *

WPAXIS Object, AxisNo, AxisType(=8) 

O-VectorX, O-VectorY, O-VectorZ

X-VectorX, X-VectorY, X-VectorZ

Y-VectorX, Y-VectorY, Y-VectorZ

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
AxisNo |  Axis number |  None  
AxisType |  Axis type |  None  
O-Vector |  The translation of the origin point None |  None  
X-Vector |  The rotated X-Axis |  None  
Y-Vector |  The rotated Y-Axis |  None  
  
DEFINITION  
---  
This WPAXIS type stores the parameters used position objects from their created position. If multiple positionings were done, this contains the concatination of all positionsings.  
  
REMARKS  
---  
The O-Vector represents the translation of the object. The X-Vector and Y-Vector represent rotated X and Y axis for the object. A rotated Z-Vector cen be computed from the cross product of the X-Vector and Y-Vector.  
  
RELATED TOPICS  
---  
Related keywords: [OBJPOS (3D)](/docs/en/keyword_documentation/o/objpos_3d/)  
  
(AxisType = 9, Brick Mesh) (Extrude type)

* * *

WPAXIS Object, AxisNo, AxisType(=9) , ModelType (2), DensityFlag, CrossSectionPlane, ErrorDist

StartX, StartY, StartZ

EndX, EndY, EndZ

Dummy, Dummy, Dummy

Dummy, Dummy, ExtrudeLayers, SheetFlag

Ftype, Ndata

Distance(1), Density(1)

::

Distance(Ndata), Density(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
AxisNo |  Axis number |  None  
AxisType |  Axis type = 9 Brick remeshing |  None  
ModelType |  Model type (**0** \- Partial revolve) (**1** \- Full revolve) **2** \- Extrude |  2  
Density Flag |  Density flag **0** \- Variable density data (not available) **1** \- Variable density data (available) |  1  
CrossSectionPlane |  Cross Section Plane **1** \- XY Plane **2** \- YZ Plane **3** \- ZX Plane |  1  
StartX |  Start position in X |   
StartY |  Start position in Y |   
StartZ |  Start position in Z |   
EndX |  End position in X |   
EndY |  End position in Y |   
EndZ |  End position in Z |   
ExtrudeLayers |  Number of extruded layers |   
SheetFlag |  Sheet remeshing flag |   
Ftype |  Function type **0** \- Uniform **1** \- Finer |   
Ndata |  Number of data pairs |   
Distance(i) |  Normalized distance of ith data pair |   
Density(i) |  Number of layers of ith data pair |   
  
(AxisType = 9, Brick Mesh) (Revolve type)

* * *

WPAXIS Object, AxisNo, AxisType(=9) , ModelType (=0,1), DensityFlag, CrossSectionPlane

R-VectorX, R-VectorY, R-VectorZ

Z-VectorX, Z-VectorY, Z-VectorZ

O-CoordX, O-CoordY, O-CoordZ

RotationAngle, StartAngle, RevolveSections, SheetFlag

Ftype, Ndata

(For Ftype > 0)

Angle(1), Density(1)

::

Angle(Ndata), Density(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
AxisNo |  Axis number |  None  
AxisType |  Axis type = 9 Brick Remeshing |  None  
ModelType |  Model Type (=0 or 1) **0** \- Partial revolve **1** \- Full revolve (**2** \- Extrude) |  0  
Density Flag |  Density flag **0** \- Variable density data (not available) **1** \- Variable density data (available) |  1  
CrossSectionPlane |  Cross section plane **1** \- XY Plane **2** \- YZ Plane **3** \- ZX Plane |  1  
R-Vector |  Reference vector |   
Z-Vector |  Revolve vector, where angle = 0 |   
O-Coord |  Revolve origin |   
RotationAngle |  Revolve angle |   
StartAngle |  Revolve Start Angle |   
RevolveSections |  Number of revolved sections |   
SheetFlag |  Sheet remeshing flag |   
Ftype |  Function type **0** \- Uniform **1** \- Finer |   
Ndata |  Number of data pairs |   
Angle(i) |  Normalized angle of ith data pair |   
Density(i) |  Number of sections of ith data pair |   
  
DEFINITION  
---  
This WPAXIS type stores the parameters used to generate brick meshes.  
  
RELATED TOPICS  
---  
Related keywords: [DEFAMG](/docs/en/keyword_documentation/d/defamg/), [REMESH](/docs/en/keyword_documentation/r/remesh/)

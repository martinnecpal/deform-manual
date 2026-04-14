---
lang: en
title: "DIEGEO (2D)"
---

# DIEGEO

|  (Object Data -2D)  
---|---  
|  Last updated on : 29-07-2013  
  
* * *

DIEGEO Object, Gtype, Ndata

Point(1), X(1), Y(1), Radius(1)

: : : :

Point(Ndata), X(Ndata), Y(Ndata), Radius(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Gtype |  Geometry type = **1** Point description |  None  
Ndata |  Number of points describing the geometry |  None  
Point(i) |  Point number of ith data point |  None  
X(i) |  X coordinate of ith data point |  None  
Y(i) |  Y coordinate of ith data point |  None  
Radius(i) |  Corner radius of ith data point |  None  
  
DEFINITION  
---  
DIEGEO specifies the boundary geometry of an object.  
  
REMARKS  
---  
DIEGEO boundary geometry may be used to specify a geometric profile of a rigid object or to define the object geometry for automatic mesh generation. DIEGEO information can be described by points or entities (lines and arcs). The remarks presented in this section refer to the point description geometry type. Radius(i) is the radius which will be placed at the intersection of the lines formed by the Point(i) and Point(i-1) and Point(i) and Point(i+1). The profile geometry must be continuous, but does not need to represent a closed curve. If the geometry is a closed curve, the data should be ordered counterclockwise. If the geometry is not a closed curve, the geometry should be ordered counterclockwise such that the rigid object interior lies to the left of the profile geometry as would be the case if the entire closed shape had been drawn. Lines of symmetry should lie on either the global X or Y axis. If the geometry represents a closed curved, then X(1) = X(Ndata), Y(1) = Y(Ndata), and Radius(1) = 0 and Radius(Ndata) must be a non-zero value. If the geometry does not represent a closed curve, then Radius(1) = Radius(Ndata) = 0. If a point other than an end point contains a zero radius, it will be treated as a straight line segment connecting the previously defined point. Applicable object types: Rigid, Elastic, Plastic, Elastoplastic, Porous  
  
WARNINGS  
---  
If Line/Arc is read from Keyword File the geometry must be checked each time.  
  
* * *

DIEGEO Line/Arc Format |  (Object Data -2D)  
---|---  
|  Last updated on : 29-07-2013  
  
* * *

DIEGEO Object, Gtype, Ndata

Entity(1), XStart(1), YStart(1), XEnd(1), YEnd(1), Angle(1)

: : : : : :

Entity(Ndata), XStart(Ndata), YStart(Ndata), XEnd(Ndata), YEnd(Ndata), Angle(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Gtype |  Geometry type = **2** Entity description |  None  
Ndata |  Number of entities describing the geometry |   
Entity(i) |  Entity number of ith data point |   
XStart(i) |  Starting X coordinate of ith data point |   
YStart(i) |  Starting Y coordinate of ith data point |   
XEnd(I) |  Ending X coordinate of ith data point(Line) or X coordinate of arc center (Arc) |  None  
YEnd(i) |  Ending Y coordinate of ith data point (Line) or Y coordinate of arc center (Arc) |  None  
Angle(i) |  Sweeping angle (degrees) in counterclockwise direction (Arc) |  None  
  
DEFINITION  
---  
DIEGEO specifies the geometric data of a rigid object.  
  
REMARKS  
---  
DIEGEO information can be described by points (Gtype = 1) or entities (lines and arcs, Gtype = 2). The remarks presented in this section refer to the entity description geometry type. Entities can contain geometric information for lines or arcs. XStart(i) and Ystart(i) refer to the coordinates of either the starting point of a line or the starting point of an arc. XEnd(i) and YEnd(i) refer to the coordinates of either the ending point of a line or the center point of an arc. The profile geometry must be continuous, but does not need to represent a closed curve. If the geometry is a closed curve, the data should be ordered counterclockwise. If the geometry is not a closed curve, the geometry should be ordered counterclockwise such that the rigid object interior lies to the left of the profile geometry as would be the case if the entire closed shape had been drawn. Lines of symmetry should lie on either the global X or Y axis. Applicable object types: Rigid  
  
RELATED TOPICS  
---  
[Geometry](/docs/en/pre_processor/12_geometry_modelling/12_geometry_modelling/) Keyword: [GEOTYP(2D)](/docs/en/keyword_documentation/g/geotyp/)

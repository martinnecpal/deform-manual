---
lang: sk
title: "STNCMP (3D)"
---

# STNCMP

|  (Object Data - 3D)  
---|---  
|  Last updated on : 13-08-2013  
  
* * *

STNCMP Object, Ndata, FieldWidth, DefSTNCMP

Element(1), STNCMP(1)(1), ..., STNCMP(1)(FieldWihth)

: :

Element(Ndata), STNCMP(Ndata)(1), ..., STNCMP(1)(FieldWihth)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object  |  Object number  |  None  
Ndata  |  Number of element/STNCMP pairs |  None  
DefSTNCMP  |  Default elemental STNCMP of all elements not listed in the element/STNCMP pairs |  0.0  
FieldWihth  |  Field width of strain components stored (determined by STNOUT) |  6  
Element(i) |  Element number of ith data pair |  None  
STNCMP(i)(j) |  Elemental STNCMP of ith data pair |  0.0  
  
DEFINITION  
---  
STNCMP specifies the value of strain components at the centroid of each element.  
  
REMARKS  
---  
The field width of strain components is determined by strain component storage flags specified by STNOUT. The possible components include Plastic, Elastic, Creep, Transformation plasticity, Thermal, Transformation volumetric, and Total. Elemental strain components are interpolated between meshes during remeshing procedures. Applicable object types: Plastic, Elastoplastic, Porous  
  
RELATED TOPICS  
---  
Object Elemental Data: Deformation - Strain Components Keywords: STNOUT

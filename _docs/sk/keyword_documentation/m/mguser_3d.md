---
lang: sk
title: "MGUSER (3D)"
---

# MGUSER

|  (Object Data – 3D)  
---|---  
|  Last updated on : 27-09-2023  
  
* * *

MGUSER Object, WinNo, Density, VelocityX, VelocityY, VelocityZ, WindowType, SpdTyp, AxisType, Remesh  
If WindowType = 1, parallelipiped defined by 8 corners  
Point(1), X(1), Y(1), Z(1)  
: : :  
Point(8), X(8), Y(8), Z(8)  
If WindowTyp = 2: Cylinder  
OriginA_X, OriginA_Y, OriginA_Z  
OriginB_X, OriginB_Y, OriginB_Z   
inner radius, outer radius

If WindowTyp = 3: Polygon  
Node   
Point(1), X(1), Y(1), Z(1)  
::   
Point(Node), X(Node), Y(Node), Z(Node)  
NElem   
Element(1), Nd1(1), Nd2(1), Nd3(1), Nd4(1)  
::   
Element(NElem), Nd1(NElem), Nd2(NElem), Nd3(NElem), Nd4(NElem)

If WindowTyp = 11: 3-D planar polygon  
Ndata   
Point(1), X(1), Y(1), Z(1)  
::   
Point(Ndata), X(Ndata), Y(Ndata), Z(Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number |  None  
WinNo |  Index of user defined mesh window (1 to N) |  None  
Density |  Mesh Density of ith point in defined area |   
VelocityX |  X component of window velocity |  0.0  
VelocityY |  Y component of window velocity |  0.0  
VelocityZ |  Z component of window velocity |  0.0  
WindowTyp |  Shape type of the window: =**1** : box;  =**2** : cylinder;  =**3** : polygon;  =**4** : 3-D planar polygon |  1  
SpdTyp |  Speed type: =**0** or **1** : constant;  = **2** : f(time); = **-n** : following object n |  0  
Point(i) |  Index of ith points describing area (1 to Ndata) |  None  
AxisType |  Axis information type = **0** brought from WPAXIS;  = **1** not defined |  1  
Remesh |  = 0 regular mesh window  
= 1 local remesh window |   
X(i),Y(i),Z(i) |  coordinate of ith point in defined area |  0.0  
OriginA_X, OriginA_Y, OriginA_Z |  coordinates of bottom origin of cylinder |  0.0  
OriginB_X, OriginB_Y, OriginB_Z |  coordinates of top origin of cylinder |  0.0  
inner radius, outer radius |  inner and outer radii of cylinder |  0.0  
Nd1(i), Nd2(i), Nd3(i), Nd4(i) |  elemental connectivity |   
  
DEFINITION  
---  
MGUSER specifies an area in space, which will move with and object during deformation. This area has a mesh density definition applied to it and will cause the area to be meshed with an appropriate mesh density Density. Polygon window (type 3) allows user to import any window shapes defined in a DEOFRM geometry format file (*.GEO). (Supported for 3dv6.1)    
3-D planar window (type 11) allows user to define a planar polygon window in 3D space to control 2D cross-section mesh of 3D object. As an example, in the ring rolling or shape rolling (3D template), 3D planar mesh window can be used for mesh density control on 2D cross-section of the workpiece before generate 3D mesh with brick elements. (Supported for 3dv10.0)  
  
REMARKS  
---  
Applicable object types: [Rigid](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.5._Rigid), [Elastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.2._Elastic), [Plastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.1_Plastic), [Elastoplastic](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.3._Elasto-plastic), and [Porous](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4.4._Porous).  
  
RELATED TOPICS  
---  
Mesh: [Mesh density Window](../../pre_processor/13_mesh_generation/13_2_3d_tet_mesh_generation.htm#13.2.6._Mesh_density_windows) Keywords: [MGNELM](/docs/sk/keyword_documentation/m/mgnelm/), [MGGRID](/docs/sk/keyword_documentation/m/mggrid/), [MGERR](/docs/sk/keyword_documentation/m/mgerr/), [MGTELM](/docs/sk/keyword_documentation/m/mgtelm/), [MGSIZR](/docs/sk/keyword_documentation/m/mgsizr/), [MGWCUV](/docs/sk/keyword_documentation/m/mgwcuv/), [MGWTMP](/docs/sk/keyword_documentation/m/mgwtmp/), [MGWSTN](/docs/sk/keyword_documentation/m/mgwstn/), [MGWSTR](/docs/sk/keyword_documentation/m/mgwstr/)

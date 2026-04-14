---
lang: sk
title: "GEOPR3"
---

# GEOPR3

|  (Object data)  
---|---  
_Update History:_ V11.1 – GEOPR3 has been introduced. |  Last updated on : 21-05-2016  
  
* * *

GEOPR3 Object, GeoParamType, NumSections

SectionType1 NumParams1

ParamName1

ParamValue1

...

ParamNameN

ParamValueN

...

SectionTypeM NumParamsM

ParamName1

ParamValue1

...

ParamNameN

ParamValueN

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
GeoParamType |  Parametric Geometry Type -1 - Imported File 0 - Undefined 1 - DEFORM Primitive 2 - CAD Geometry 3 - Preform Generation |  None  
NumSections (M) |  Number of Parameter Sections 1 - General Parameters (values are either strings or integers) 2 - Geometry Parameters (values are doubles) 3 - CAD Export Options (values are doubles) |  None  
NumParamsM (N) |  Number of Parameters in a section |  None  
ParamNameN |  Name of a Parameter |  None  
ParamValueN |  Value of a Parameter |  None  
  
DEFINITION  
---  
GEOPR3 specifies parameters used to define geometry.  
  
REMARKS  
---  
This keyword stores geometry parameters a name-value pairs. Each parameter name is followed by its value. The parameters are grouped into sections to allow one level of organization. The general parameters section is used to store information about the geometry type. For DEFORM primitives, the primitive type is stored here. For, imported files and CAD geometry, the file format, file name, and CAD system name are stored here. Table 1 lists the recognized parameters used in this section. This section is not used for preform generation.  
  
Parameter Name |  Description |  Applicable GeoParamType  
---|---|---  
FileName |  The name of the imported file |  -1  
CadProgram |  The name of the CAD program |  2  
CadFilePath |  The name of the CAD file |  2  
GeoType |  The basic geometry type1 |  1  
SymType |  Symmetry type 0 - Full Symmetry 1 - Half Vertical Symmetry 2 - Half Horizontal Symmetry 3 - Quarter Symmetry |  1  
PrimType  |  The primitive type2 |  1  
  
1 \- A list of supported shapes in shown in Table 2

2 \- A list of supported primitives is shown in Table 3. Note that different primitives may use the same basis geometry shape.

Table 1 - Recognized Section 1 Parameters

Geometry Shape |  ID  
---|---  
Box |  3001  
Revolved Cylinder |  3002  
Extruded Cylinder |  3003  
Hollow Cylinder |  3004  
Octagonal Bar |  3005  
  
Table 2 - Supported Geometry Shapes.

Primitive Type |  ID |  Appropriate Geometry Shape ID  
---|---|---  
Box |  0 |  3001  
Cylinder |  1 |  3002 or 3003  
Hollow Cylinder |  2 |  3004  
  
Table 3 - Primitive Types

The geometry parameters section stores the actual geometry parameters. For CAD geometry, this stores the named parameters define on the geometry by the CAD system. For DEFORM primitives, imported geometry and Preform geometry, this stores the named parameters used by the DEFORM system.

The CAD Export Options section is only used for CAD geometry (GeoParamType = 2). This will store options used to export the CAD file to a format that can be read by DEFORM (usually STL).

The action keyword, GENGEO can be used to create geometry defined by GEOPR3.

RELATED TOPICS  
---  
Related keywords: [GEOPR2](/docs/sk/keyword_documentation/g/geopr2/), [GENGEO](/docs/sk/keyword_documentation/g/gengeo/), [WPAXIS (2D)](/docs/sk/keyword_documentation/w/wpaxis/), [WPAXIS (3D)](/docs/sk/keyword_documentation/w/wpaxis_3d/)

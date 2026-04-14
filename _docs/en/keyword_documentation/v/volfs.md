---
lang: en
title: "VOLFS (2D3D)"
---

# VOLFS

|  (Object data)  
---|---  
|  Last updated on : 05-08-2014  
  
* * *

VOLFS Iobj, Numel, Nphase

1 f1, f2, f3, .. fn

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Iobj |  Object number |  None  
Numel |  Number of element |  None  
Nphase |  Number of materials |  None  
  
DEFINITION  
---  
VOLFS specifies the volume fraction limit of a phase in an element of an object. VOLFN is only stored in the database at the beginning of a new phase transformation, ex. Austenite Pearlite or Austenite Martensite. The intent of VOLFN is to assure that the volume fraction amount transformed from Austenite Pearlite does not exceed the volume fraction of Austenite prior to transformation.  
  
REMARKS  
---  
Example of implementation of VOLFN A: Austenite P: Pearlite B: Bainite M: Martensite Step 1 A: 1 P:0 B:0 M:0 (VOLFN stored into database) A P Step 2 A: 0.9 P:0.1 B:0 M:0 Step 3 A:0.8 P:0.2 B:0 M:0 (VOLFN stored into database) A B (phase P complete) Step 4 A:0.7 P:0.2 B:0.1 M:0 It should be noted that VOLFC is different than VOLFN in that VOLFC stores the volume fraction of the phases every step. Typically, the user will only be concerned with inputting volume fractions for VOLFN at the beginning of the simulation. Applicable Simulation Modules: Microstructure Applicable Simulation Modes: Transformation Applicable object types: ALL except Rigid  
  
RELATED TOPICS  
---  
[Inter-Material Data](/docs/en/pre_processor/10_material_data/10_9_transformation_data/10_9_transformation_data/) Keywords: [VOLFS](), VOLFC

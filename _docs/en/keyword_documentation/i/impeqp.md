---
lang: en
title: "IMPEQP (2D3D)"
---

# IMPEQP

|  (Action keyword)  
---|---  
_Update History:_ V11 - IMPEQP has been introduced. |  Last updated on : 24-07-2013  
  
* * *

IMPEQP Object, FilePath

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object Number  |  None  
FilePath |  Path to the equipment data file |  None  
  
DEFINITION  
---  
IMPEQP loads equipment data for a specific object. The content of keyword file will be loaded to the object as the object’s movement data.  
  
REMARKS  
---  
This keyword is intended as a convenient way to load movement for an object. Applicable object types: [Rigid]({{ '/docs/en/pre_processor/11_general_object_data_definition/11_general_object_data_definition/' | relative_url }}#11.4.5._Rigid)  
  
RELATED TOPICS  
---  
[Movement Controls]({{ '/docs/en/pre_processor/15_movement_controls_definition/15_movement_controls_settings/' | relative_url }}) Keywords: [MOVCTL (2D)]({{ '/docs/en/keyword_documentation/m/movctl_(2d)/' | relative_url }}), [MOVCTL (3D)]({{ '/docs/en/keyword_documentation/m/movctl_(3d)/' | relative_url }}),[ANGMOV (2D)]({{ '/docs/en/keyword_documentation/a/angmov/' | relative_url }}), [ANGMOV(3D)]({{ '/docs/en/keyword_documentation/a/angmov(3d)/' | relative_url }}) , [ANGMVY(2D)]({{ '/docs/en/keyword_documentation/a/angmvy/' | relative_url }})

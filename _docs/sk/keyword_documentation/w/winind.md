---
lang: sk
title: "WININD (3D)"
---

# WININD

|  (Simulation control data)  
---|---  
_Update History:_ V11.1 - WININD has been introduced only for 3D. |  Last updated on : 21-05-2016  
  
* * *

WININD Win#, Window_shape, Velocity type

{Vx, Vy, Vz} or {velocity function data}

{Window coordinates}

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Win# |  Window number |  None  
Window_shape |  Window shape =**1** rectangular =**2** cylindrical |  None  
Velocity type |  Velocity type =**1** constant =**2** function of time =**-n** follow Object#n |  None  
velocity function data |  Function data that defines the velocity |  None  
Vx |  Unit direction vector for gravity in X dir. |  None  
Vy |  Unit direction vector for gravity in Y dir. |  None  
Vz |  Unit direction vector for gravity in Z dir. |  None  
Window coordinates |  Coordinates of points that define the window |  None  
  
DEFINITION  
---  
WININD specifies the window for induction heating calculation.  
  
REMARKS  
---  
WININD is only for 3D. If WININD is defined, the induction heating calculation is carried out only inside the window area. This will save computation time.  
  
RELATED TOPICS  
---  
Similar keywords: [WINATM(2D)]({{ '/docs/sk/keyword_documentation/w/winatm/' | relative_url }}), [WINATM(3D)]({{ '/docs/sk/keyword_documentation/w/winatm_3d/' | relative_url }}) , [WINPRS(2D)]({{ '/docs/sk/keyword_documentation/w/winprs/' | relative_url }}), [WINPRS(3D)]({{ '/docs/sk/keyword_documentation/w/winprs_3d/' | relative_url }}), [WINRSE]({{ '/docs/sk/keyword_documentation/w/winrse/' | relative_url }}), [WINTMP (2D)]({{ '/docs/sk/keyword_documentation/w/wintmp/' | relative_url }}). [WINTMP(3D)]({{ '/docs/sk/keyword_documentation/w/wintmp_3d/' | relative_url }})

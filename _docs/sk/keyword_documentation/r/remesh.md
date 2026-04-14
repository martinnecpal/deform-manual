---
lang: sk
title: "REMESH (2D3D)"
---

# REMESH

|  (Action keyword)  
---|---  
_Update History:_ V11 - REMESH has been introduced. V11.1 - Adde UseDB option to support BCC transfer in DOE. |  Last updated on : 24-07-2013  
  
* * *

REMESH Object

DbFile

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
UseDB |  Use another DB **0** \- Use the <problemid>.DB **1** \- Use DB file specified on the following line |  0  
  
DEFINITION  
---  
REMESH specifies the object number for remeshing By default, REMESH remeshes the open DB. the UseDB option allows for the specification of another DB file.  
  
REMARKS  
---  
This is action keyword that executes remeshing procedure.  
  
RELATED TOPICS  
---  
Text-based PRE, Shape optimization, [Multiple operations](/docs/sk/integrated_manufacturing_process_setup/5_introduction_to_integrated_manufacturinghtm/) Keywords: [BRDEXT](/docs/sk/keyword_documentation/b/brdext/), [DEFINT](/docs/sk/keyword_documentation/d/defint/), [DEFAMG](/docs/sk/keyword_documentation/d/defamg/)

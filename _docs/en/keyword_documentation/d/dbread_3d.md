---
lang: en
title: "DBREAD (3D)"
---

# DBREAD

|  (Action keyword)  
---|---  
|  Last updated on : 12-08-2013  
  
* * *

DBREAD step#

Filename

DBREAD 1 1 -1

Filename

(Obsolete : read the last step)

DBREAD 1 0 step#

Filename

(Obsolete : read step#) 

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Step# |  = 0 Read the last step Otherwise, read specific step number |   
Filename |  specific file name |   
  
DEFINITION  
---  
DBREAD allows the user to input an arbitrary database step into the preprocessor.  
  
REMARKS  
---  
It is an action keyword placed in Keyword and Master files that directs the preprocessor to read a database file. Any redundant information read will clobber current states in the Preprocessor. For example, if the preprocessor has a value for NSTEP stored in it before a DBREAD command is processed, this value will be overwritten by the value stored in the database that this read from.  
  
RELATED TOPICS  
---  
[Preprocessor](/docs/en/pre_processor/7_introduction_to_pre-processor/), [Multiple Operations](/docs/en/integrated_manufacturing_process_setup/5_introduction_to_integrated_manufacturinghtm/)

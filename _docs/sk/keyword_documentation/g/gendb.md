---
lang: sk
title: "GENDB (2D3D)"
---

# GENDB

|  (Action keyword)  
---|---  
|  Last updated on : 22-10-2016  
  
* * *

GENDB Arg1 Arg2 Arg3

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Arg1 |  = 1 Generate old database = 2 Generate new database = 0 (or not-specified) System define |   
Arg2 |  Whether to use DB checking = 0, 1 (or not-specified) Use DB checking = 2 Skip DB checking |   
Arg3 |  Whether to keep positive step # = 0: generate negative step # always = 1: keep positive step # = 2: Cogging step (allow repeated negative steps) |  0  
DbFilename |  Database file name to be generated |   
  
DEFINITION  
---  
GENDB generates a database.  
  
REMARKS  
---  
GENDB is an action keyword placed in Keyword files that drives the Preprocessor to generate a database. (Example usage of GENDB) * generate new DB GENDB 2 <ProblemId>.DB * generate old DB (with DB checking) GENDB 1 <ProblemId>.DB * generate old DB, WITHOUT DB checking (no DB checking for DB conversion or 2Dto3D conversion) GENDB 1 2 <ProblemId>.DB * system defined - if no DB, generate new DB otherwise generate old DB GENDB or GENDB 0 <ProblemId>.DB * generate old DB, WITHOUT DB checking, keep positive step number (good for purging) GENDB 1 2 1 <ProblemId>.DB * generate old DB, with DB checking, allow repeated negative steps (initially added for cogging but good for general MO procedure) GENDB 1 1 2 <ProblemId>.DB * make purged DB (keep -1 and the last step only) DBREAD -1 <ProblemId>.DB GENDB 2 0 <ProblemId>_PUR.DB DBREAD 0 <ProblemId>.DB GENDB 0 2 1 <ProblemId>_PUR.DB  
  
RELATED TOPICS  
---  
[Preprocessor](/docs/sk/pre_processor/7_introduction_to_pre-processor/): [Database Generation](/docs/sk/pre_processor/21_database_generation/21_database_generation/) Keywords: [PROBID](/docs/sk/keyword_documentation/p/probid/), [DBREAD](/docs/sk/keyword_documentation/d/dbread/), [KFREAD](/docs/sk/keyword_documentation/k/kfread/), [KFWRIT](/docs/sk/keyword_documentation/k/kfwrit/)

---
lang: sk
title: "KFREAD (2D3D)"
---

# KFREAD

|  (Action keyword)  
---|---  
|  Last updated on : 27-09-2023  
  
* * *

KFREAD number

filename

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
number |  = 0, 1 (or not-specified): Read keyword in append mode   
= 2: Global time will be kept intact after reading (v12sp1) |  None  
filename |  Filename of keyword file to load |  None  
  
DEFINITION  
---  
KFREAD loads a keyword file automatically into the preprocessor during a multiple operations run.  
  
REMARKS  
---  
  
It is an action keyword placed in either an automatic script file or in a Master file. The purpose of KFREAD is to load a keyword file to be converted into a database or to load information into the Preprocessor to overwrite current information. For example, if during a multiple operations run the user wants to change the geometry of an object from a previous run, the user can load the database using a [DBREAD](/docs/sk/keyword_documentation/d/dbread/) keyword and then load in the new geometry data using the KFREAD keyword. 

RELATED TOPICS  
---  
[Multiple Operations](/docs/sk/integrated_manufacturing_process_setup/5_introduction_to_integrated_manufacturinghtm/) Keywords: [DBREAD](/docs/sk/keyword_documentation/d/dbread/), [KFWRIT](/docs/sk/keyword_documentation/k/kfwrit/)

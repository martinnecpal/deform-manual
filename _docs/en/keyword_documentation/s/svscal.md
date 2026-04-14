---
lang: en
title: "SVSCAL (2D3D)"
---

# SVSCAL

|  (Action keyword)  
---|---  
|  Last updated on : 17-08-2017  
  
* * *

SVSCAL Object, Type, Ndata

Strain(1), Strain(1)

: :

Strain (Ndata), Strain (Ndata)

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Object |  Object number |  None  
Type |  Type of state variable **1** = Effective strain **2** = Not yet defined **3** = Not yet defined |  1  
Ndata |  Number of data points |   
  
DEFINITION  
---  
SVSCAL scales (or initializes) the elemental and nodal (if specified) values of the selected state variable in the object according to user-defined function data. (Supported from 3D V6.1)  
  
REMARKS  
---  
SVSCAL is an action keyword that scales the values of state variable when it is read in to the Pre-Processor. The main use of this keyword is for multiple operations as well as Shape Roll. For example, in rolling, this action keyword is to re-compute the effective strain in order to include the effect of recrystallization in FEM simulation. A user needs to prepare function data required for scaling from experiments.  
  
RELATED TOPICS  
---  
[Object Nodal Data](/docs/en/pre_processor/17_object_data_initialization/17_1_node_data_window/), [Object Elemental Data](/docs/en/pre_processor/17_object_data_initialization/17_2_element_data_window/)

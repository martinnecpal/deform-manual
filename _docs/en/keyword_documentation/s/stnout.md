---
lang: en
title: "STNOUT (2D3D)"
---

# STNOUT

|  (Simulation control - 2D)  
---|---  
_Update History:_ V11.1 - Added the flag for strain partitioning for multiphase textured material for keyword STNOUT |  Last updated on : 12-08-2014  
  
* * *

STNOUT PlasticOn, ElasticOn, CreepOn, TransOn, TotalOn, ThmVolOn, TrnsfVolOn, PartitionOn

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
PlasticOn |  Plastic strain flag |  0  
ElasticOn |  Elastic strain flag |  0  
CreepOn |  Creep strain flag |  0  
TransOn |  Transformation plasticity strain flag |  0  
TotalOn |  Total strain flag |  1  
ThmVolOn |  Thermal volumetric strain flag |  0  
TrnsfVolOn |  Transformation volumetric strain flag |  0  
|  (=0: Not stored, =1: Stored) |   
PartitionOn |  Effective strain partitioning flag for multiphase textured material |  0  
|  (=0: Not stored, =1: Stored) |   
  
DEFINITION  
---  
STNOUT specifies strain component storage flags.  
  
REMARKS  
---  
Strain may consist of several components: Plastic, Elastic, Creep, Transformation plasticity, Thermal, and Transformation volumetric. These components can be stored separately in Database. Keyword STNOUT specifies which ones of them are stored. Notice this keyword will affect the field width of strain component (STNCMP) Plastic, elastic, creep, trans. plasticity and total strain each has six components. Thermal and transformation volumetric each has one component. Thus, for example, if plastic and thermal strain are turned on, the field width of STNCMP will be 6+1=7. (New in v11.1) For multiphase textured material, the overall effective strain can be partitioned among child phases. The partitioned strains are specified in keyword STNPAT.  
  
RELATED TOPICS  
---  
Simulation Controls: Advanced Output Controls, Object Elemental Data: Deformation - Strain Components Keywords: STNCMP

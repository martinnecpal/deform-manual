---
lang: en
title: "DOESCL (2D3D)"
---

# DOESCL

|  (Action keyword)  
---|---  
_Update History:_ (New keyword in v11) |  Last updated on : 23-07-2013  
  
* * *

DOESEL Scale, (Type) (for Object initial temperature)

“NDTMP” , Object

or

DOESEL Scale, (Type) (for Flow stress data)

“FSTRES” , Material

or

DOESEL Scale, (Type) (for Young’s modulus)

“YOUNG” , Material

or

DOESEL Scale, (Type) (for Advanced thermal BCC)

“LOCTMP” , Object, Window, Flag1, Flag2, Flag3, Flag4, Flag5 

or

DOESEL Scale, (Type) (for Body force and Centrifugal force)

“FPERV”, Material, Flag1, Flag 2

or

DOESEL Scale, (Type) (for Movement type)

“MOVCTL” , Object 

* * *

OPERAND |  DESCRIPTION |  DEFAULT  
---|---|---  
Scale |  Scaling factor  |  None  
Type |  (reserved for future use) |  None  
Object |  Object number |   
Material |  Material number |   
Window |  Window Number |   
(for Advanced Thermal BCC)  
Flag1 |  = **1** scaling for environment temperature |  0  
Flag2 |  = **1** scaling for convection coefficient |  0  
Flag3 |  = **1** scaling for emissivity |  0  
Flag4 |  = **1** scaling for heat flux |  0  
Flag5 |  = **1** scaling for interface heat transfer coefficient |  0  
(for Body and Centrifugal force)  
Flag1 |  = **1** scaling for body force |  0  
Flag2 |  = **1** scaling for centrifugal force |  0  
  
DEFINITION  
---  
DOESCL specifies the scaling of the design of experiments (DOE) variable used in each FEM simulation run. For DOE study, the following input data can be used as design variable in v11. \- Material data (Flow stress, Young’s modulus, Body force, Centrifugal force) \- Initial object temperature \- Advanced thermal bcc (Env. Temp., Convection coefficient, Emissivity, Heat flux, Heat transfer coefficient) \- Movement data (Force, Speed, Hammer energy, Screw energy, Hydraulic press with speed control) This keyword is written in DEF_MULTI.INI file which becomes input to text-based pre-processor (DEF_PRE.EXE) for DOE simulation run.  
  
REMARKS  
---  
Design of Experiments (DOE) simulation technique enables industrial designers to identify simultaneously the individual and interactive effects of many (input) design factors that could affect the simulation results (output). DOE simulation technique can provide a full insight of interaction between design variables. Therefore, DOE simulation environment in DEFORM v11 system can help to pin point the sensitive areas in process/product designs that cause problems in final product. Designers are then able to review and fix these problems and produce robust and near optimal process and product designs before going into mass production. In order to investigate the sensitivity of certain design variable to manufacturing process or product quality variation, the value of design variable needs to be adjusted by (+/-)% from its nominal value. The new action keyword DOESCL serves to generate a series of DOE simulation run. Applicable simulation type: DOE simulation Example of the use of DOESCL in DEF_MULTI.INI: KFREAD Disk-HT.KEY DOESCL 1.15 NDTMP 1 DOESCL 1.25 LOCTMP 1 1 0 1 0 0 0 DOESCL 1.25 LOCTMP 1 2 0 1 0 0 0 DOESCL 1.05 FSTRES 1 DOESCL 1.05 YOUNG 1 DOESCL 1.1 FPERV 1 0 1 KRWRIT Disk-HT-NDTMP-LOCTMP.KEY GENDB Disk-HT-NDTMP-LOCTMP.DB  
  
RELATED TOPICS  
---  
Keywords: [NDTMP(2D)](/docs/en/keyword_documentation/n/ndtmp/), [NDTMP (3D)](/docs/en/keyword_documentation/n/ndtmp_3d/), [FSTRES](/docs/en/keyword_documentation/f/fstres/), [YOUNG](/docs/en/keyword_documentation/y/young/), [LOCTMP](/docs/en/keyword_documentation/l/loctmp/), FPERV, [MOVCTL(2D)](../m/movctl_\(2d\).htm), [MOVCTL (3D)](../m/movctl_\(3d\).htm)  
  
,

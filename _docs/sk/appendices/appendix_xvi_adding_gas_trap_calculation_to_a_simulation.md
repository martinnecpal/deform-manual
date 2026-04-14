---
lang: sk
title: "Appendix XVI: Adding Gas Trap Calculation to a Simulation"
---

# Appendix XVI: Adding Gas Trap Calculation to a Simulation

In 2D, gas trapping can be predicted if the file [DEF_GAS.DAT](appendix_xvii_data_files.htm#DEF_GAS_DAT) is added to the directory where a simulation is running. The contents of the file [DEF_GAS.DAT](appendix_xvii_data_files.htm#DEF_GAS_DAT) is unimportant in that the file is merely a flag to indicate that gas trapping is to be performed.

The gas trapping is modeled as a perfect law for any time a boundary of a deformable object traps a region of a rigid object. When a volume is closed off by contact with a single body (See Fig. AXVI.1.), a pressure is applied to the surface of the body which increases as a perfect gas law. At the end, slight underfill can be noted in the workpiece when you highlight the contact nodes (See Fig. AXVI.2.). In the case that the boundary of the deformable traps a split between two objects, there will be no trapping even if the two objects are flush or overlapped.

If a gas trap simulation is run, delete the files [DEF_GAS.DAT](appendix_xvii_data_files.htm#DEF_GAS_DAT) and DEF_GAS.INI in the case of running a simulation that does not use gas trapping. The file [DEF_GAS.DAT](appendix_xvii_data_files.htm#DEF_GAS_DAT) is a flag used activate gas trapping. The file DEF_GAS.INI is a file output by the program and should not be changed during a simulation.

  
![]({{ '/assets/images/appendices/appendix_xvi_adding_gas_trap_calculation_to_a_simulation/image0001.jpg' | relative_url }})

A trapped volume under compression

In Fig. AXVI.1. red circle shows where the air is trapped as the workpiece is being extruded.

![]({{ '/assets/images/appendices/appendix_xvi_adding_gas_trap_calculation_to_a_simulation/image0002.jpg' | relative_url }})

The final trapped volume with slight underfill

The final volume is small but it can be easily seen as slight underfill by the highlighted contact nodes as shown in Fig. AXVI.2.

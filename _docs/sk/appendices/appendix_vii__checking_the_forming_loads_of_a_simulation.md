---
lang: sk
title: "Appendix VII: Checking the Forming loads of a simulation"
---

# Appendix VII: Checking the Forming loads of a simulation

There are several factors that affect the forming loads and tool stresses of a simulation. This appendix will try to give the reader a cursory introduction into understanding what is required for a simulation in order to give accurate results. It is the presupposition of this document that DEFORM will yield an accurate result given that the inputs properly reflect the actual case being modeled. It has been verified many times that DEFORM is a leader in accurate results for the correct input.

The outline of this appendix is to first discuss some guidelines for obtaining proper load results. Since these loads are transmitted as forces onto the dies, it is imperative that these results be accurate in order for the stresses in the dies to be accurate.

**Guideline 1: Check the flow stress data and make sure that it is representative of your actual stock.**

This is a very obvious rule that sounds simple at first but tends to be overlooked very frequently. Some people perform testing on their material to make sure that the data they have matches the materials they are using. Often some data is meant for different processes or has had slightly different processing conditions or has a different chemistry. If testing is not an option, often one can try to correlate load results over several simulated processes and try to determine the suitability of material data. 

**Guideline 2: Make sure that the material data covers the process condition range.**

The required material data for a simulation can be only flow stress data for a rigid-plastic material at isothermal conditions. In the case of a non-isothermal elasto-plastic simulation, elastic, plastic and thermal data should be specified. All the required data should be specified for the range of temperature, strain and strain rate that the process exists at. If any extrapolation occurs, the results can become inaccurate. 

**Guideline 3: Check that the mesh resolution of workpiece is reasonable to capture the shape of the dies.**

The number of required elements in a simulation can vary depending on the process and the desired results. In the case of a simple upset of a round bar, the deformation gradient is not large and the only region that can require a fine mesh is at the contact areas if a hot workpiece is contacting a cold tool. However, in the case of a forging of a complex shape such as a crankshaft, many elements are required to capture the many details of the final shape.

**Guideline 4: Make sure that if the process is hot or warm that correct die speed is considered along with transfer times.**

In the case of hot forming and some warm forming cases, the materials tend to be sensitive to forming rate. In this case, the speed of the moving tool can impact the results greatly. The impact of the forming rate can be seen directly in the flow stress data. By checking how much the flow stress data changes at a given temperature based on the forming rate can show very large changes in the stress of the material (thus the forming load of the part) versus the forming rate.

Also, in cases where a part is very hot, small periods of time between transfers can add up to a non-negligible amount of heat loss. This is important to consider since many materials can have their properties changes very quickly at hot temperatures.

****

**Guideline 5: Check at the end of the simulation that the flash thickness is correct. (or that the tool travel distance is correct)**

This should be of no surprise to anyone who designs tools are works in the metal forming industry. As a part fills all the crevices of a die, the load will tend to increase rather quickly. If the simulation is overstroked or understroked, the results will behave just like real life. The results will tend to over or underestimate loads respectively.

**Guideline 6: Make sure that the friction value is consistent with the actual process.**

**Related Topics:**

[Material Properties](/docs/sk/pre_processor/10_material_data/10_material_data/)

[Object Mesh](/docs/sk/pre_processor/13_mesh_generation/13_mesh_generation/)

[Simulation Controls](/docs/sk/pre_processor/9_simulation_controls/9_simulation_controls/)

[Contact relations](/docs/sk/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/)

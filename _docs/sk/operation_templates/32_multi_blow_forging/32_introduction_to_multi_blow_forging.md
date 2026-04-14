---
lang: sk
title: "32. Introduction to Multi Blow Hammer"
---

# 32\. Introduction to Multi Blow Forging

A forging system comprises all the input variables such as the billet or blank (geometry and material), the tooling (geometry and material), the conditions at the tool/material interface, the mechanics of plastic deformation, the equipment used, the characteristics of the final product, and the finally the plant environment where the process is being conducted.

Multi blow forging operation is used to setup the problem which is having successive blows by either hammer or screw press. In this operation user is able to setup the Forging problem without having manually restart each pass and in blow table user is allowed to define the number of blows. For every blow we are able to define the percentage of blow, energy, reheating and separate dwelling time. In V11.0 New MO, advanced features like, Adaptive process controls, Blow efficiency can be defined as function, All simulation models are available (transformation, carburization, recrystallization etc).

  
**How to add Multi blow Forging operation**

Multi blow Forging operation is accessible from MO Wizard that can be opened from Main GUI. Multi blow Forging Operation can be added in MO wizard, from explorer tab by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button next to 2D Multi blow Forging. Also, user can add by drag and drop into the Operation Editor as shown in Fig. 32.1.

  
![]({{ '/assets/images/operation_templates/32_multi_blow_forging/32_introduction_to_multi_blow_forging/image001.jpg' | relative_url }})

Added 2D Multi blow Forging operation into Operation Editor

Following are the steps to Setup Multi blow forging operation in MO wizard:

  * Define Process Details

  * Define Blow Table

  * Geometry type

  * Simulation controls

  * Load Object material

  * Add Number of Objects

  * Create object geometry and Generate Mesh for the objects

  * Assign Material and Boundary conditions

  * Define the movement for top die (number of blows)

  * Stopping controls and Step Controls

  * Generate Database

  * Running the simulation.

**Related Topics:**

[6.1. Integrated Manufacturing Process Pre- Processor Layout](/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_1_integrated_manufacturing_process_preprocessor_layout/)

[6.2. Integrated Manufacturing Process.Simulation layout](/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_2_integrated_manufacturing_process_simulation_layout/)

[6.3. Integrated Manufacturing Proces Post - Processor layout](/docs/sk/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_3_integrated_manufacturing_process_post_layout/)

[32.1. 2D Multi Blow Forging](/docs/sk/operation_templates/32_multi_blow_forging/32_1_2d_multi_blow_forging_setup/)

[32.2. 3D Multi Blow Forging setup](/docs/sk/operation_templates/32_multi_blow_forging/32_2_3d_multi_blow_forging_setup/)

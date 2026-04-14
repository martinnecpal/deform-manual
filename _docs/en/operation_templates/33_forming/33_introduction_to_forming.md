---
lang: en
title: "33. Introduction to Forming"
---

# 33\. Introduction to Forming

Forming is a manufacturing process involving the shaping of metal using localized compressive forces.

  
A forging system comprises all the input variables such as the billet or blank (geometry and material), the tooling (geometry and material), the conditions at the tool/material interface, the mechanics of plastic deformation, the equipment used, the characteristics of the final product, and finally the plant environment where the process is being conducted.

Forming operation is used to understand the direction of metal flow, the magnitude of deformation, and the temperature distribution. In forming operation, defects such as cracks and folds can be tracked while running simulation. 

## How to add Forming operation

Forming operation is accessible from Integrated Manufacturing Process (MO) Wizard that can be opened from Main GUI. Forming Operation can be added in MO wizard from explorer tab by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button next to 2D or 3D Forming as shown in Fig. 33.1. Also, user can add by drag and drop into the Operation Editor. 

![]({{ '/assets/images/operation_templates/33_forming/33_introduction_to_forming/image001.jpg' | relative_url }})

Added 3D Forming operation into Operation Editor

  
The Integrated Manufacturing Process (MO) is divided into several distinct sections - namely the DISPLAY window, Graphical Utilities, Operation Tree, property Editor, Operation Editor, Explorer and Graphics window. For more information, please refer [6.1. Integrated Manufacturing Process Pre- Processor Layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_1_integrated_manufacturing_process_preprocessor_layout/)

There are three modes in Integrated Manufacturing process (MO). The [Pre-Processor](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_1_integrated_manufacturing_process_preprocessor_layout/), the [Simulator](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_2_integrated_manufacturing_process_simulation_layout/) and the [Post-Processor](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_3_integrated_manufacturing_process_post_layout/). These three modes can be selected among each other through a tab selection. The Pre-Processor is used to setup problem for simulation, the simulation can be run from Simulator section and the results are viewed in the Post-Processor. Each time a change is desired for a simulation, the change should be made in the Pre-Processor. The Simulator is where the simulation is run and monitored. The Post-Processor has many tools for viewing and interpreting the results of a simulation.

## Objective of Forming operation

Simple Forming operations can be set using guided mode while complex operations and advanced options can be set using expert mode . User can setup complex problems such as rolling, heat transfer, dwelling, grain, phase transformation, extrusion etc... by selecting expert mode.

  
Forming operation in MO is similar to Pre processor, where user can setup any type of problem.(See Fig. 33.2. and Fig. 33.3.)

  
![]({{ '/assets/images/operation_templates/33_forming/33_introduction_to_forming/image002.jpg' | relative_url }})

Example of 2D successive operation setup

  
![]({{ '/assets/images/operation_templates/33_forming/33_introduction_to_forming/image003.jpg' | relative_url }})

Example of 3D successive operation setup

**Related Topics:**

[6.1. Integrated Manufacturing Process Pre- Processor Layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_1_integrated_manufacturing_process_preprocessor_layout/)

[6.2. Integrated Manufacturing Process.Simulation layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_2_integrated_manufacturing_process_simulation_layout/)

[6.3. Integrated Manufacturing Process Post - Processor layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_3_integrated_manufacturing_process_post_layout/)

[33.1. 2D Forming Setup](/docs/en/operation_templates/33_forming/33_1_2d_forming_setup/)

[33.2. 3D Forming Setup](/docs/en/operation_templates/33_forming/33_2_3d_forming_setup/)

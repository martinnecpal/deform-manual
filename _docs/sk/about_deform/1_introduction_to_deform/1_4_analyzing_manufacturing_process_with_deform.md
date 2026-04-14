---
lang: sk
title: "1.4. Analyzing Manufacturing Process with DEFORM"
---

# 1.4. Analyzing Manufacturing Process with DEFORM

DEFORM can be used to analyze most thermo-mechanical forming processes, and many heat treatment processes. The general approach is to define the geometry and materials of the initial workpiece in DEFORM, and then sequentially simulate each process that is to be applied to the workpiece.

The recommended sequence for designing a manufacturing process using DEFORM is:

  * Define your proposed process.

  * Final forged part geometry
  * Material
  * Tool progressions
  * Starting workpiece/billet geometry
  * Processing temperatures, reheats, etc.

  1. Gather required data.

  * Material data

  * Processing condition data.
  * Using the DEFORM pre-processor, input the problem definition for the first operation.
  * Using the DEFORM MO Interface input the problem definition to construct successive operations initially and simulate all operations in sequence without user interaction. Fig. 1.4.1. explains process flow in MO environment.
  * Submit the data for simulation.
  * Using the DEFORM post-processor, review the results.
  * Using Next gen post processor, review the results and generate Report for desired state variables/ graphs.
  * Repeat the pre-process-simulate-review sequence for each operation in the process.
  * If the results are unacceptable, use your engineering experience and judgment to modify the process and repeat the simulation sequence.

![]({{ '/assets/images/about_deform/1_4_analyzing_manufacturing_process_with_deform/1_4_image001.jpg' | relative_url }})

Process Flow in MO ENVIRONMENT

**Related Topics:**

[PRE-PROCESSOR](/docs/sk/pre_processor/7_introduction_to_pre-processor/)

[POST-PROCESSOR](/docs/sk/post_processor/24_introduction_to_post_processor/24_introduction_to_post_processor/)

[Integrated Manufacturing Process](/docs/sk/integrated_manufacturing_process_setup/5_introduction_to_integrated_manufacturinghtm/) (MO)

[Material Data Definition](/docs/sk/pre_processor/10_material_data/10_material_data/)

[Geometry Data](/docs/sk/pre_processor/12_geometry_modelling/12_1_2d_geometry_data_defining/)

[Movement Control Definition](/docs/sk/pre_processor/15_movement_controls_definition/15_movement_controls_settings/)

[Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/)

[Inter-object Data definition](/docs/sk/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/)

[Appendix V: The elasto-plastic model](/docs/sk/appendices/appendix_v__the_elasto-plastic_model/)

[Appendix VII: Checking the forming loads results of a simulation](/docs/sk/appendices/appendix_vii__checking_the_forming_loads_of_a_simulation/)

---
lang: en
title: "9.8. Control Files"
---

# 9.8. Control files ![]({{ '/assets/icons/pre_icons/mo_control_files.jpg' | relative_url }})

9.8.1. Category 1

  * Double corner constraints

  * Solver switch control

**[3D]** : There are many different specialized features within DEFORM - Preprocessor that are controlled through data files. The purpose for this type of implementation is that these functions are used in only a few rare instances and if they find popular use, they can be incorporated into DEFORM keywords. When these data files are used, the functionality is available if the data file is located in the same directory as the current problem running. Since they are not contained within neither in database nor the keyword files, the control file has to be moved with the database or the keyword to run the problem with the same functionality if a different directory or computer is used to run a simulation. When one of these control files are used, a warning is automatically posted in the message file heading letting the user know that one of these files exists. 

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_8_control_files/9_8_image001.jpg' | relative_url }})

Control files category1 settings

From version 6.0, these data files can be specified through the graphical interface in the Control File window. (See Fig. 9.8.1.)

## Category 1

**Double corner constraints**

This defines two angles where if a node is contacting a die corner an angle between these values, the node will be given a double contact condition. This is further explained in the [Appendix XV: The Double Concave Corner Constraint.](/docs/en/appendices/appendix_xv_the_double_concave_corner_constraint/)

**Solver switch control**

This defines a number of elements where the switch to sparse solver is blocked. The purpose of this is to prevent the sparse solver from being activated in cases where the problem is too large.

Related Topics:

[9.1. Simulation type Settings](/docs/en/pre_processor/9_simulation_controls/9_1_simulation_type_settings/)   
[9.2. Defining Step](/docs/en/pre_processor/9_simulation_controls/9_2_defining_step/)   
[9.3. Stopping Controls](/docs/en/pre_processor/9_simulation_controls/9_3_stopping_controls/)   
[9.4. Remesh Criteria](/docs/en/pre_processor/9_simulation_controls/9_4_remesh_criteria/)   
[9.5. Solver Settings](/docs/en/pre_processor/9_simulation_controls/9_5_solver_settings/)   
[9.6. Process Conditions](/docs/en/pre_processor/9_simulation_controls/9_6_process_conditions/)   
[9.7. Advanced Options](/docs/en/pre_processor/9_simulation_controls/9_7_advanced_options/)   
[9.9. Thermomechanical variables](/docs/en/pre_processor/9_simulation_controls/9_9_thermomechanical_variables/)

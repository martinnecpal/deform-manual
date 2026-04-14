---
lang: en
title: "21. Database Generation"
---

# 21\. Database Generation

**[2D, 3D]:** The simulation data set entered into the pre-processor can be written as a new database or appended to an existing database file. The information will be written as a negative step, indicating that it was written from the pre-processor and not the simulation engine. In an existing database, any steps higher than the current step will be overwritten at this time. The simulation database will be checked as it is written.

When the Status is "Ready to generate DB", we can generate the DB file. If the Status is "Input error", then we can observe the Error message in Message file related to Setup (in problem setup what data is missing or not correct). 

From v12.0.2, In Generate DB file, we can observe the Operation Simulation setup summary as shown in Fig. 21.1.. 

The simulation database will be checked when either the ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) or ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) buttons are clicked as shown in Fig. 21.1.

![]({{ '/assets/images/pre-processor/21_database_generation/image001.jpg' | relative_url }})

Database Generation window

**Data errors**

Errors are serious problems with the data set that will prevent the simulation from running. These errors are marked with red flags in data checking and must be resolved before the database can be written.

**Data warnings**

Warnings are conditions which may cause undesirable solution behavior but will not prevent the simulation from running. Warnings are marked with yellow flags. If warnings exist, each one should be carefully checked and the source identified.

Some warnings represent unusual, but valid, data situations. If this is the case, they can be ignored and the simulation can be run.

**The Benefits of Integrated DB**  
In the integrated DB we can store the 2D and 3D simulation and streamlined animation. There is No DB version compatibility issue any more. Fig. 21.2. demonstrating integrated DB structure.

![]({{ '/assets/images/pre-processor/21_database_generation/image002.jpg' | relative_url }})

Database Step Selection window

**Related Topics:**

[DEFORM Basic file system](/docs/en/about_deform/1_introduction_to_deform/1_10_basic_file_system/)

[Primary Die selection from simulation control](../9_simulation_controls/9_2_defining_step.htm#Primary_die_\(PDIE\))

[Primary Die selection from Object general definition window](../11_general_object_data_definition/11_general_object_data_definition.htm#11.5._Primary_Die)

[Step definition in the simulation control](/docs/en/pre_processor/9_simulation_controls/9_2_defining_step/)

[Max. Interference depth for remesh settings](../13_mesh_generation/13_2_3d_tet_mesh_generation.htm#13.2.8._Remeshing_criteria)

[Volume compensation selection from Object properties window](../16_object_properties/16_1_deformation_properties.htm#16_1_3_Target_Volume_\(TRGVOL\))

[Inter-Object data definition window](/docs/en/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/)

[23.1. Start, Stop and Resume Simulation](/docs/en/simulator/23_deform_simulator/23_1_start_stop_and_resume_simulations/)

[23.2. Interactive and batch modes using Run option](/docs/en/simulator/23_deform_simulator/23_2_interactive_and_batch_mode/)

[23.3. Simulation Graphics](/docs/en/simulator/23_deform_simulator/23_3_simulation_graphics/)

[23.4. Process Monitor](/docs/en/simulator/23_deform_simulator/23_4_process_monitor/)

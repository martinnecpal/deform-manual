---
lang: en
title: "9.1. Simulation type Settings"
---

# 9.1. Simulation type Settings

9.1.1. Simulation Information

9.1.2. Geometry type

9.1.3. Units

9.1.4. Type

9.1.5. Simulation modes

Main Settings options are as shown in Fig. 9.1.1. for 2D and 3D.

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_simulation_controls/9_image001.jpg' | relative_url }})

(a)

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_simulation_controls/9_image002.jpg' | relative_url }})

(b)

Main Settings window; (a) For 2D and (b) For 3D

## Simulation Information

  * **Simulation title (TITLE) [2D, 3D]** : The simulation title ([TITLE](/docs/en/keyword_documentation/t/title/)) allows you to title the problem (up to 80 characters) for reference purposes.

  * **Operation name (OPRNAM) [2D, 3D]** : The Operation name (OPRNAM) allows you to title the specific operation (up to 64 characters) for reference purposes.

  * **Simulation name (SIMNAM) [2D, 3D]** : The simulation name ([SIMNAM](/docs/en/keyword_documentation/s/simnam/)) allows you to title the specific operation (up to 64 characters) for reference purposes.

  * **Oper****ation number (CURSIM) [2D, 3D]** : Allows the specification of a new operation number ([SIMNAM](/docs/en/keyword_documentation/s/simnam/)) for each operation in the database. If operations numbers are specified, the post-processor displays each operation with its number in the step list.

  * **Simulation number (CURSIM) [2D, 3D]** : Allows the specification of a new simulation number ([SIMNAM](/docs/en/keyword_documentation/s/simnam/)) for each simulation in the database. If simulation numbers are specified, the post-processor displays each simulation with its number in the step list.

  * **Mesh number (MESHNO) [2D, 3D] :** This variable records the current mesh based on the number of remeshings ([MESHNO](/docs/en/keyword_documentation/m/meshno/)) that occur between the initial mesh and the current mesh. This variable should not be changed.

##  Geometry type (GEOTYP) [2D]

In DEFORM seven types of geometry models ([GEOTYP](/docs/en/keyword_documentation/g/geotyp/)) can be setup currently:

  * **Axisymmetric** : The Axisymmetric models as a cross-section with respect to the central axis. Therefore, the model requires the deforming geometry to be axially symmetric and in the first quadrant and fourth quadrant (i.e. X > 0). In addition, the system assumes that the flow in every radial plane is identical. (See Fig. 9.1.2.)

  * **Plane strain :** The Plane-strain assumes that the geometry to have an unit depth with both front and back faces constrained. The simulation assumes that the objects will behave identically in any given cross-section across the width and height of the object. (See Fig. 9.1.2.)

  * **Torsion :** Torsion models are axisymmetric models. The notion of torsion is a manner of characterizing a twist or screw. (See Fig. 9.1.2.). Typical application is in modelling inertia welding, where in one part with torsional movement with an axial force is pressed against a stationary part with computations extending to hoop direction.

  * **Plane stress** : The Plane stress model assumes unit dimension of z- directional thickness. The simulation assumes that the objects will behave identically in any given cross-section across the width and height of the object. The Plane stress model supports Plastic, Elastic, and Elasto - Plastic Objects. (See Fig. 9.1.2.)

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_1_simulation_type_settings/9_1_image001.jpg' | relative_url }})

Example for types of geometry model

  * **2.5D Friction Welding** : In DEFORM-V12 2.5D Friction welding geometry type option has been added, using this option user can setup 2.5D Linear Friction welding operation.

  * **2.5D Rolling** : In DEFORM-V12 2.5D Rolling geometry type option has been added, using this option user can setup 2.5D Rolling operation with # of section data.

  * **2.5D Roll Forming** : In DEFORM-V12 2.5D Roll Forming geometry type option has been added, using this option user can setup 2.5D Roll Forming operation with # of section data.

## Units (UNIT) [2D, 3D]

The DEFORM unit system ([UNIT](/docs/en/keyword_documentation/u/unit/)) can be defined as English or Metric (SI). (See Fig. 9.1.1.) All information in DEFORM should be expressed in consistent units. The unit system should be selected at the beginning of the problem setup procedure, and should not be changed during a simulation or after an operation. (See [Table 1.9.1](../../about_deform/1_introduction_to_deform/1_9_units.htm#Table_DEFORM_unit_system) for more information of variables units in DEFORM

##  Type (STYPE)

The different types of simulations ([STYPE](/docs/en/keyword_documentation/s/stype/)) that can be run are:

  * **Lagrangian Incremental [2D, 3D**]: To be used for all the conventional [forming](/docs/en/operation_templates/33_forming/33_introduction_to_forming/),[ heat transfer](/docs/en/operation_templates/35_heat_transfer/35_introduction_to_heat_transfer_operations/) and [heat-treat](/docs/en/operation_templates/37_heat_treatment/37_introduction_to_heat_treatment/) applications (See Fig. 9.1.1.). Transient phase of the processes like rolling, [machining](/docs/en/operation_templates/39_cutting/39_introduction_to_cutting/), [extrusion](/docs/en/operation_templates/31_extrusion/31_introduction_to_extrusion/), drawing, [cogging](/docs/en/operation_templates/29_cogging/29_introduction_to_cogging/) etc. also can be modelled in this general framework.

  * **ALE Rolling [3D]** : ALE model for rolling process can be generated using the ‘[Shape](/docs/en/operation_templates/43_shape_rolling/43_introduction_to_shape_rolling/)[ Rolling template](/docs/en/operation_templates/43_shape_rolling/43_introduction_to_shape_rolling/)’ (See Fig. 9.1.1b.). When the model is generated using this template, automatically generates the necessary boundary conditions for the entry surface for the billet (indicated in the interface as the Beginning surface, nodes are assigned [BCCDEF](/docs/en/keyword_documentation/b/bccdef/)=4), and the exit surface (indicated in the interface as Free surface, nodes are assigned [BCCDEF](/docs/en/keyword_documentation/b/bccdef/)=5). Template automatically sets the analysis type as ‘ALE Rolling’. When the rolling model is setup using the regular pre-processor, user needs to set this analysis type and proper boundary conditions to be able to run the ALE model for rolling. From 3DV6.1 this functionality has been also improved with automatic stopping criteria once steady state conditions are detected.

  * **Steady-State machining [2D, 3D]** : 2D/3D machining model for turning applications can be generated using the ‘[Machining](/docs/en/operation_templates/39_cutting/39_introduction_to_cutting/)[ ](/docs/en/operation_templates/39_cutting/39_introduction_to_cutting/) [Template](/docs/en/operation_templates/39_cutting/39_introduction_to_cutting/)’ in which the initial model can be set up for Lagrangian Incremental run. (See Fig. 9.1.1.) When sufficient chip has formed the template can be used to generate an additional operation to switch the analysis mode to Steady State. In this stage template can be used to generate the required boundary conditions for the steady state run, which includes defining end surface of the chip (indicated as free surface, with [BCCDEF](/docs/en/keyword_documentation/b/bccdef/)code set as 5 for those nodes). Template automatically sets the analysis type as ‘Steady-State Machining’. When the machining model is setup using the regular pre-processor, user needs to set this analysis type and proper free surface and thermal boundary conditions to be able to run the Steady State model for machining.

  * **Ring Rolling [3D]** : From 3D-V6.1, simulation engine has been enhanced to handle the non isothermal modelling of [ring rolling](/docs/en/operation_templates/42_ring_rolling/42_introduction_to_ring_rolling/) process. (See Fig. 9.1.1b.) This development includes a special ALE technique that does not depend on any expensive computing resources, nor involves very long modelling times. From 3D-v10.0 this special ALE solver has been further improve to take advantage of parallel environments (solver part).

  * **Steady-State extrusion [3D]** : If user would like to understand the displacement and other state variables after reaching steady state in Extrusion then user can select this option. This option is available even in [Extrusion](/docs/en/operation_templates/31_extrusion/31_introduction_to_extrusion/) operation under explorer in DEFORM MO Environment. User can simulate for only 5 to 10 steps depending on the extrusion geometry complexity.

  * **ALE Extrusion [3D]** : If user wishes to setup the ALE Extrusion model in Preprocessor, then he has to select ALE Extrusion radio button as shown in Fig. 9.1.1b. Even ALE Extrusion operation can be setup using Extrusion operation under explorer in DEFORM MO GUI.

  * **ALE stir Welding [3D]** : In DEFORM-V12, if an user wishes to setup the ALE Stir welding model in Preprocessor, then he has to select ALE Stir welding model radio button.

  * **ALE Spinning [3D]** : In DEFORM-V12, if an user wishes to setup the ALE spinning model in Preprocessor, then he has to select ALE Spinning model radio button. ALE [spinning](/docs/en/operation_templates/48_spinning/48_introduction_to_spinning/) operation can be setup even using 3D Spinning operation available under explorer in DEFORM MO GUI.

  * **Electro-magnetic forming****[3D]** : In DEFORM-V12, if an user wishes to setup the Electro-magnetic forming model in Preprocessor, then he has to select Electro-magnetic forming radio button.

  * **ALE Spinning (express) [3D]** : In DEFORM-v12.1, user can select ALE express solver to accelerate the simulation speed of ALE spinning simulation.  
When this solver is selected the roll must have hole at the center and Non separable criteria must be defined between Head stock/Tail stock and workpiece.

  * **ALE Tube piercing [3D]:** In DEFORMv12.1.1, if user wishes to setup the Tube piercing model in Preprocessor, then user should select ALE Tube piercing model radio button. ALE Tube piercing operation can be setup even using 3D Spinning operation available under explorer in Deform MO GUI.

## Simulation modes (SMODE, TRANS)

[2D, 3D]: DEFORM features a group of simulation modes that may be turned on or off individually, or used in various combinations.(See Fig. 9.1.3.) For backward compatibility with old keywords and databases, before version 3.0, the Keyword [SMODE](/docs/en/keyword_documentation/s/smode/) (old style isothermal, non-isothermal, heat transfer) is read and the Corresponding keyword TRANS mode switches are set in the pre-processor. 

  * **Deformation :** Simulates deformation due to mechanical, thermal, or phase transformation effects. 

  * **Heat transfer :** Simulates thermal effects within the simulation, including heat transfer between objects and the environment, and heat generation due to deformation or phase transformation, where applicable.

  * **CFD flow** : User can simulate fluid flow phenomena based on the conservation laws governing fluid motion using this option. For 2D, only Plane strain geometry type will be supported.

  * **Transformation** : Simulates transformation between phases due to thermo mechanical and time effects.

  * **Diffusion** : Simulates diffusion of carbon atoms within the material, due to carbon content gradients.

  * **Grain** : Simulates grain size calculation and recrystallization calculations.

  * **Heating** : Simulates heat generation due to resistance or induction heating. Induction heating, Induction-BEM heating (Boundary Element Method) and Resistance heating (available from DEFORM v11.0) can be used for Simulation of various Heating Processes. 3D FEM engine from DEFORM v11.0 can now handle induction heating models with dual frequency input data for current frequency. For examples of heating cases refer to the DATA folder heating examples.

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_1_simulation_type_settings/9_1_image002.jpg' | relative_url }})

Simulation Controls window - Heating

**Related Topics:**

[9.2. Defining Step](/docs/en/pre_processor/9_simulation_controls/9_2_defining_step/)   
[9.3. Stopping Controls](/docs/en/pre_processor/9_simulation_controls/9_3_stopping_controls/)   
[9.4. Remesh Criteria](/docs/en/pre_processor/9_simulation_controls/9_4_remesh_criteria/)   
[9.5. Solver Settings](/docs/en/pre_processor/9_simulation_controls/9_5_solver_settings/)   
[9.6. Process Conditions](/docs/en/pre_processor/9_simulation_controls/9_6_process_conditions/)   
[9.7. Advanced Options](/docs/en/pre_processor/9_simulation_controls/9_7_advanced_options/)   
[9.8. Control Files](/docs/en/pre_processor/9_simulation_controls/9_8_control_files/)   
[9.9. Thermomechanical variables](/docs/en/pre_processor/9_simulation_controls/9_9_thermomechanical_variables/)

[9.10. Output controls](/docs/en/pre_processor/9_simulation_controls/9_10_output_controls/)

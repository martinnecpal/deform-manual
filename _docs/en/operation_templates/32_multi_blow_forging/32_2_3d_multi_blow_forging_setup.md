---
lang: en
title: "32.2. 3D Multi Blow Forging setup"
---

# 32.2. 3D Multi Blow Forging setup

32.2.1. Process Details

32.2.2. Blow table

32.2.3. Simulation Controls

32.2.4. Material List

32.2.5. Add objects

32.2.6. Workpiece

  * Geometry

  * Object Mesh

  * Object Material

  * Boundary conditions

32.2.7. Top Die

32.2.8. Bottom Die

32.2.9. Positioning

32.2.10. Scheduled Positioning

32.2.11. Contact

32.2.12. Stopping Controls

32.2.13. Step controls

32.2.14. Generate DB

## Process Details

In this process page, user can define the Hammer energy and method of energy specification along with the process controls like Reheat and Dwell. User can define Reheat conditions and its controls along with the Dwell conditions. User also has options to specify if object is rotated between blows and also can Initialize strain on Reheat. (See Fig. 32.2.1.)

![]({{ '/assets/images/operation_templates/32_multi_blow_forging/32_2_3d_multi_blow_forging_setup/image001.jpg' | relative_url }})

Process window

**Press** : User can define Hammer name and energy details. Using Load movement from file ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) and Load movement from Library ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) user can load the hammer data. 

**Note** : At this moment press data cannot be loaded from explorer tab equipment library.

**Energy specification Method:**

  * **Absolute** : Energy will be consumed with respect to the defined energy value.

  * **Ratio to Max Energy(%)** : Energy will be consumed in terms of percentage value.

  
**Dwell** : Using this user can set the time that workpiece rests on the die before the starting of the next Blow. User can also specify Simulation time step and Heat Transfer Co-efficient to be used during dwell process simulation.

**Workpiece Rotation** : By turning on this option, user can specify rotation for workpiece between blows in specified directions.

**Use Reheat** : During hammer forging process involving multiple blows, the workpiece temperature drops and may require reheating. User can schedule reheat process between blows by turning on this option. 

**Reheat Temperature** : Reheat Temperature is the temperature to which the workpiece temperature will be raised. If only Reheat Temperature is turned on without Heating Simulations, then the temperature at all nodes of the workpiece is simply initialized to the reheating temperature.

**Heating Simulations** : When Heating Simulations is turned on, an simulation of workpiece heating is carried on at the specified time between the blows. It includes, heating time, Transfer In time, Transfer Out Time, along with specific simulation time step for heat time and Transfer Time.

**Adaptive Reheat:** By turning on Adaptive Reheat, system will decide and schedule reheating of the workpiece based on the nodal temperatures of the workpiece and adaptive reheat controls. If it is off, user has to schedule reheating manually. If the nodal temperature of the workpiece drops below the Lower limit, reheating process will be scheduled automatically. During non-deformation simulation, simulation stops if nodal temperature of the workpiece is out of range specified in upper limit and lower limit. Simulation stops during reheating if all the nodes reach the temperature specified in Temperature to stop reheat.

**Initialize Strain on Reheat:** Buy turning on this, user can initialize strain in the workpiece after reheating.

**Heating Simulations** : It includes, heating time, heat time per step, Transfer In time, Transfer Out Time, Transfer Time Step.

## Blow table

In hammer forging process multiple blows are used and blow table helps the user to define number of blows and schedule work piece rotation, Dwelling and Reheating.

**Energy** : The Blow Energy is a measure of the total energy that the flywheel will contain when the desired speed has been reached and prior to engaging the clutch. The units for blow energy in English units are klb-in and in SI units are N-mm. (See Fig. 32.2.2.)

**No.Hits** : User can specify number of hits/blows required for the process. Once the user enters the hits/blows number, we can see equal number of rows are added to the table with default values. User can control each blow’s efficiency and the energy to be utilized. User can also schedule Reheating and Flip of workpiece after each blow by turning on respective boxes. User can also define different dwell times for different blows if required. An example of blow table is shown in below Fig. 32.2.2.

![]({{ '/assets/images/operation_templates/32_multi_blow_forging/32_2_3d_multi_blow_forging_setup/image002.jpg' | relative_url }})

Blow Table window

## Simulation Controls

In Guided mode simulation controls, user can select Simulation mode type and Output type (See Fig. 32.2.3.). The basic options required for forming operation are provided here while Expert mode provides more detailed options. For more information on Export mode simulation options, please refer [9\. Simulation Controls](/docs/en/pre_processor/9_simulation_controls/9_simulation_controls/)

![]({{ '/assets/images/operation_templates/32_multi_blow_forging/32_1_2d_multi_blow_forging_setup/image004.jpg' | relative_url }})

Guided mode Simulation controls

## Material List

Materials required for the process can be loaded either from library using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) or from DB or Key file using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) as shown in Fig. 32.2.4. User can also add new material and define required data from respective tab by clicking ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). For more information on Material data definition please refer Material List

![]({{ '/assets/images/operation_templates/32_multi_blow_forging/32_1_2d_multi_blow_forging_setup/image005.jpg' | relative_url }})

Import Material from Library

## Add objects

User can add required number of objects for the simulation by selecting ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button. Fig. 32.2.5. shows three objects added for a simple upsetting operation. 

![]({{ '/assets/images/operation_templates/32_multi_blow_forging/32_1_2d_multi_blow_forging_setup/image006.jpg' | relative_url }})

Objects Window

## Workpiece

In this page user can define required temperature for the object and select type of the object as shown in Fig. 32.2.6. For workpiece by default the object type selected is Plastic and user can also import object from other DB’s or Keyfile’s using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) button and browsing respective file. 

![]({{ '/assets/images/operation_templates/32_multi_blow_forging/32_2_3d_multi_blow_forging_setup/image003.jpg' | relative_url }})

Workpiece window

**Geometry**

Geometry window is used to define the geometry of an object as shown in Fig. 32.2.7. Only define primitive field will be in active mode rest other options will be in greyed when no geometry is defined. Once after creating geometry all the options will be activated.

  
User can define new geometry using primitives and also can import the geometry from other file using or from library using , user can also import geometries in other formats such as .STL,.UNV,.PDA,.GEO and .. Primitives are provided for easy definition of basic geometry shapes. For more information on creating and editing 2D geometries please refer [12.1. 2D Geometry Data Defining.](/docs/en/pre_processor/12_geometry_modelling/12_1_2d_geometry_data_defining/)

![]({{ '/assets/images/operation_templates/32_multi_blow_forging/32_2_3d_multi_blow_forging_setup/image004.jpg' | relative_url }})

Geometry window

  
**Object Mesh**

Mesh Page provides options to mesh the object. Guided ![]({{ '/assets/icons/pre_icons/mo_guided_mode.jpg' | relative_url }}) mode provides option to set number of elements only using slider bar to generate mesh. If the object geometry is complex or user would like to control the mesh density over the object, then user has to switch to expert mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}). Expert mode provides various options like weighing factors, Mesh windows and user defined mode to control the mesh density. Meshing options available in expert mode and Guided more are shown in Fig. 32.2.8. and Fig. 32.2.9. For more detail description of these options, please refer [13\. Mesh Generation.](/docs/en/pre_processor/13_mesh_generation/13_mesh_generation/)

![]({{ '/assets/images/operation_templates/32_multi_blow_forging/32_2_3d_multi_blow_forging_setup/image005.jpg' | relative_url }})

Guided mode Mesh option

![]({{ '/assets/images/operation_templates/32_multi_blow_forging/32_2_3d_multi_blow_forging_setup/image006.jpg' | relative_url }})

Expert mode mesh option

**Object Material**

In material page, all the materials added to material list are displayed (as shown in Fig. 32.2.10.) and user can select the required material to assign to respective object from material list. Also user can load the material in Object material page using Import Material data from a File ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) or Using Load form Library option ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) .

![]({{ '/assets/images/operation_templates/30_die_stress/30_1_2d_die_stress_setup/image011.jpg' | relative_url }})

Material selection Window

  
**Boundary conditions**

In Boundary conditions page, user can assign various boundary constraints for an object. Boundary conditions specify how the boundary of an object interacts with other objects and with the environment. The most commonly used boundary conditions are heat exchange with the environment for simulations involving heat transfer, prescribed velocity for enforcing symmetry or prescribing movement in problems such as drawing where a part is pulled through a die, shrink fit for modelling shrink rings on tooling, prescribed force for die stress analysis and Contact between objects in the model. Fig. 32.2.11. shows various BCC that can be assigned to an object.

![]({{ '/assets/images/operation_templates/32_multi_blow_forging/32_2_3d_multi_blow_forging_setup/image007.jpg' | relative_url }})

Boundary conditions window

The BCC’s are categorized as [Deformation](/docs/en/pre_processor/14_boundary_conditions/14_2_deformation_boundary_conditions/),[Thermal](/docs/en/pre_processor/14_boundary_conditions/14_3_thermal_boundary_conditions/), [Diffusion](/docs/en/pre_processor/14_boundary_conditions/14_4_diffusion_boundary_conditions/) and [Heating](/docs/en/pre_processor/14_boundary_conditions/14_5_heating_boundary_conditions/). For more information about these BCC's please refer [14\. Boundary Conditions](/docs/en/pre_processor/14_boundary_conditions/14_boundary_conditions/).

## Top Die

For Top Die, user can define all the required details like Geometry, mesh, Material and BCC as explained for the workpiece object.   
But Top die Movement we have to define it separately for top die.

**Top Die movement**

**Hammer Press**

Hammer forging operation is controlled by energy. During a working stroke, the deformation proceeds until the total kinetic energy is dissipated by plastic deformation of the material and by elastic deformation of ram and anvil when the die and ram faces contact each other.(See Fig. 32.2.12.)

![]({{ '/assets/images/operation_templates/32_multi_blow_forging/32_2_3d_multi_blow_forging_setup/image008.jpg' | relative_url }})

Hammer movement control settings

  
During hammer forging operation, only a portion of the kinetic energy of ram is used for the plastic deformation of work piece. The rest of the energy is lost through anvil and machine frame. These values can be set in the movement controls window.

There are basically two types of hammer. The first is an [anvil type hammer](../../pre_processor/15_movement_controls_definition/15_3_hammer.htm#15_3_1_Anvil_Type_Hammer) and the other c[ounter blow hammer](../../pre_processor/15_movement_controls_definition/15_3_hammer.htm#15_3_2_Counterblow_Hammer). For the formulations and assumptions used for the two types of hammer forging operations please refer [15.3. Hammer](/docs/en/pre_processor/15_movement_controls_definition/15_3_hammer/)

In an **Anvil type hammer** , the workpiece, together with the lower die set, is placed on an anvil which is stationary. In a simple gravity drop hammer, the ram is accelerated by gravity and accumulates energy.

A **counterblow hammer** can be specified for movement by selecting the Counter blow hammer check box as seen in Fig 6.7.5.3.12. After this, the other moving hammer object can be specified as well as the mass of the other moving hammer. The mass of the objects do not have to be equal but the total energy is split between the two hammer dies.

**Screw Press**

The unique characteristic of a screw press (See Fig. 32.2.13.) is the method of driving it. A motor drives a flywheel which is either directly connected or can be connected to a screw spindle.

![]({{ '/assets/images/operation_templates/32_multi_blow_forging/32_2_3d_multi_blow_forging_setup/image009.jpg' | relative_url }})

Screw press movement control settings

  
**The data required to run a screw press driven tool are:**

  * **Energy** : The Blow Energy is a measure of the total energy that the flywheel will contain when the desired speed has been reached and prior to engaging the clutch. The units for blow energy in English units are klb-in and in SI units are N-mm.

  * **Blow Efficiency** : The Blow Efficiency represents the fraction of the total energy that will be converted to deformation energy. The rest of the energy is absorbed through the clutch mechanism, friction and the machine frame. There are no units for this quantity. In Forming express only constant value we can use but in forming operation user can also define function of force, for more information refer [15.4. Screw Press.](/docs/en/pre_processor/15_movement_controls_definition/15_4_screw_press/)

  * **Moment****of****Inertia** : The Moment of Inertia is the moment of inertia of the flywheel. The English units of inertia are klb*in*s2 and the SI units are N-mm*s2. The mass moment of inertia for a circular disc with the Z-axis perpendicular to the center is I = 2 ET /ω2 where ET is the total energy of the flywheel, and ω is the angular velocity in radians per second.

  * **Ram****Displacement****or Lead screw pitch** : The Ram Displacement specifies the distance per revolution of the flywheel that the screw will advance. This helps in determining the linear velocity of the ram. The English units for Ram Displacement are inch/revolution, while the SI units are mm/revolution. If only the pitch angle and diameter of the spindle is known, the Ram Displacement can be calculated using πdsin(θt) where d is the diameter of spindle and θt is the pitch angle of the spindle

  
For more details about Screw press refer [15.4. Screw Press.](/docs/en/pre_processor/15_movement_controls_definition/15_4_screw_press/)

## Bottom Die

For Bottom Die, user can define all the required details like Geometry, mesh, Material and BCC as explained for the workpiece object.

## Positioning

Below Fig. 32.2.14. shows the positioning window.

![]({{ '/assets/images/operation_templates/32_multi_blow_forging/32_2_3d_multi_blow_forging_setup/image010.jpg' | relative_url }})

Positioning window

**Automatic Positioning![]({{ '/assets/icons/pre_icons/mo_automatic_positioning_button.jpg' | relative_url }})**

By clicking on this button, system automatically Positions the Objects with respect to the top die movement direction, this option works best for simple setup with three objects work piece, top die and bottom die.

**Positioning Objects![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) **

By clicking on this button, user can position the objects in required directions.Various types of Positioning Options are available such as [Drag](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_1_Drag_Positioning), [Offset](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_2_Offset_Positioning), [Interference](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_3_Interference_positioning), [Flip](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_6_Flip_positioning) and [Rotational](../../pre_processor/19_object_positioning/19_object_positioning.htm#19_4_Rotational_positioning) as shown in Fig. 32.2.15. For more information about these options, please refer [19\. Object Positioning](/docs/en/pre_processor/19_object_positioning/19_object_positioning/)

![]({{ '/assets/images/operation_templates/32_multi_blow_forging/32_2_3d_multi_blow_forging_setup/image011.jpg' | relative_url }})

Object positioning window

## Scheduled Positioning

When user is not sure about the location of an object, scheduled positioning will help to position the objects accurately.

  
Schedule positioning allows the user to define the positioning for objects in MO setup for successive operations for which DB is not generated so that the objects are positioned before generation of DB while running simulation in Batch mode.

## Contact

The purpose of inter-object relations is to define how the different objects in a simulation interact with each other. All objects which may come in contact with each other through the course of the simulation must have a contact relation defined. 

  
Inter-Object relations define what objects can contact each other, and how contacted objects will behave while in contact. Contact relations, Inter-Object boundary conditions, Friction and Heat transfer relations are set here for each object pair.(See Fig. 32.2.16.) Generated contacts message will display in the message tab below the graphics window.

![]({{ '/assets/images/operation_templates/32_multi_blow_forging/32_1_2d_multi_blow_forging_setup/image015.jpg' | relative_url }})

Contact generation window

  
User can select the Shear or Coulomb friction type and define the friction coefficient. The lubricant used on the tooling plays a large role in the amount of friction that exists between the tooling and workpiece. The friction in turn affects the metal flow at contact surfaces.

  
Typical values are provided for shear friction as shown below,  
(0.08) for cold forming (carbide dies) processes

(0.12) for cold forming (Steel dies) processes

(0.25) for warm forming processes

( 0.3) for lubricated hot forging processes

(0.7) for un lubricated (dry) hot forging processes

(0.4) for Aluminium forming processes

Conduction heat transfer coefficient value can be defined by user and also typical values are provided by system those are,

(1 N/sec/mm/C or 0.0003 Btu/sec/in^2/F) for Free Resting

(1 N/sec/mm/C or 0.0003 Btu/sec/in^2/F) for Dwelling

(11 N/sec/mm/C or 0.004 Btu/sec/in^2/F) for Forming

## Stopping Controls

The stopping parameters determine the process time at which the simulation terminates. A simulation can be terminated based on maximum number of time steps simulated or the maximum accumulated elemental strain or the maximum process time or maximum stroke or minimum velocity or maximum load on the primary object. A simulation will be stopped when the condition of any of the stopping parameters are met.(See Fig. 32.2.17.)

![]({{ '/assets/images/operation_templates/32_multi_blow_forging/32_2_3d_multi_blow_forging_setup/image012.jpg' | relative_url }})

Stopping controls window

For more information, please refer [Stopping Controls in Forming 3D setup](../33_forming/33_2_3d_forming_setup.htm#33_2_7_Stopping_Controls).

## Step controls

The DEFORM system solves time dependent non-linear problems by generating a series of FEM solutions at discrete time increments. At each time increment, the velocities, temperatures, and other key variables of each node in the finite element mesh are determined based on boundary conditions, thermo mechanical properties of the work piece materials and possibly solutions at previous steps. Other state variables are derived from these key values, and updated for each time increment. The length of this time step, and number of steps simulated, are determined based on the information specified in the step controls menu. Fig. 32.2.18. Shows simulation control options in Guided mode, the basic options required for forming operation are provided here while Expert mode provides more detailed options.

![]({{ '/assets/images/operation_templates/32_multi_blow_forging/32_1_2d_multi_blow_forging_setup/image017.jpg' | relative_url }})

Guided mode Step controls window

**Number of simulation steps (NSTEP)**

The number of simulation steps parameter defines the number of steps to run from the starting step number. The simulation will stop after this number of simulation steps have run, unless stopping control is triggered to stop the simulation or if the simulation runs into a problem. For example, if the starting step number is -35 ([NSTART](/docs/en/keyword_documentation/n/nstart/)), and 30 steps ([NSTEP](/docs/en/keyword_documentation/n/nstep/)) are specified, the simulation will stop after the 65th step, unless another stopping control is triggered first. In case of reheating process it could be Temp. to stop reheating.

For more information, please refer [Stopping Controls.](/docs/en/pre_processor/9_simulation_controls/9_3_stopping_controls/)

  
**Step increment to save (STPINC)**

The step increment ([STPINC](/docs/en/keyword_documentation/s/stpinc/)) to save in the database controls the number of steps that the system will save in the database. When a simulation runs, every step must be computed, but does not necessarily need to be saved in the database. Storing more steps will preserve more information about the process, consequently it will require more storage space.

  
**Primary die (PDIE)**

The primary die ([PDIE](/docs/en/keyword_documentation/p/pdie/)) is the object for which many stopping and stepping criteria are defined. For example, stopping distance based on primary die stroke. When the stroke of the object defined as the primary die reaches the value for primary die displacement, the simulation will be stopped whether or not more steps were specified. The Step by Stroke feature determines step size based on the movement of the primary die. The primary die is usually assigned to the object most closely controlled by the forging machinery. For example, the die attached to the ram of a mechanical press would be designated as the primary object. The primary die is usually assigned to Top Die in case of Hammer / Screw Press.

**Step increment control ([DSMAX](/docs/en/keyword_documentation/d/dsmax/)/[DTMAX](/docs/en/keyword_documentation/d/dtmax/))**

Solution step size can be controlled by time step or by displacement of the primary die. If stroke per step is specified, the primary die will move the specified amount in each time step. The total movement of the primary die will be the displacement per step multiplied by the total number of steps. If time per step is specified, the time interval per step will be used. The die displacement per step will be the time step times the die velocity.

The definition of step increment control have been enhanced to include both the time and stroke dependent step functions,these options are available under Expert mode. This means, step size (both time per step and stroke per step) can now be defined as a function of time or stroke. This functionality enables finer resolution of saved model information, where it is desired. (typically towards the end of the stroke, where steep changes of die load and cavity filling or flash formation can take place)

  
Stroke per step is frequently more intuitive. However, time per step must be specified for any problem in which there is no die movement (such as heat transfer), or for any problem where force control is used.

Fig. 32.2.19.. shows the Simulation Controls in Expert mode.

![]({{ '/assets/images/operation_templates/32_multi_blow_forging/32_2_3d_multi_blow_forging_setup/image013.jpg' | relative_url }})

Expert mode Simulation controls window

  
Options defined under Simulation Controls (See Fig. 32.2.19.) control the numerical behavior of the solution. Main controls details with specifying the simulation title, unit system, geometry type, etc.

  
Step and stopping controls are used to specify the time step, the total number of steps and the criteria used to terminate the simulation.

  
Processing conditions like the environment temperature, convection coefficient can be specified here.

For more information and description about options in Simulation controls, Please refer [9\. Simulation Controls.](/docs/en/pre_processor/9_simulation_controls/9_simulation_controls/)

## Generate DB

**Check Data![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) **

It checks the Data. If Data is correct we can generate DB. But while checking Data if it gives any errors or warnings then it should be corrected before generating Database. Errors will not allow the database to be generated while warnings will allow the DB to be generated.

**Generate Database![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }})**

By clicking on this button, it generated the Database for the setup.(See Fig. 32.2.20.)

**Append Key file**

Any information that is not defined in the wizard but still applicable to the process can be loaded as .key file. This option is also useful in the cases where only few values needs to be changed then those values can be defined as .key file and only .key file can be changed and simulation can be resubmitted.

  
![]({{ '/assets/images/operation_templates/30_die_stress/30_1_2d_die_stress_setup/image024.jpg' | relative_url }})

Generate DB window

**Related Topics:**

[6.1. Integrated Manufacturing Process Pre- Processor Layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_1_integrated_manufacturing_process_preprocessor_layout/)

[6.2. Integrated Manufacturing Process.Simulation layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_2_integrated_manufacturing_process_simulation_layout/)

[6.3. Integrated Manufacturing Process Post - Processor layout](/docs/en/integrated_manufacturing_process_setup/6_integrated_manufacturing_process_layout/6_3_integrated_manufacturing_process_post_layout/)

[32.1. 2D Multi Blow Forging](/docs/en/operation_templates/32_multi_blow_forging/32_1_2d_multi_blow_forging_setup/)

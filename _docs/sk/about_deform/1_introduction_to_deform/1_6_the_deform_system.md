---
lang: sk
title: "1.6. The DEFORM System"
---

# 1.6. The DEFORM System

1.6.1. Pre-processing

1.6.2. Running the Simulation

1.6.3. Post-processing

The DEFORM system consists of three major components:

## Pre-processing

A pre-processor for creating, assembling, or modifying the data required to analyze the simulation, and for generating the required database file. The DEFORM [pre-processor](/docs/sk/pre_processor/pre-processor_mainpg/) uses a graphical user interface to assemble the data required to run the simulation. Input data includes,

**Object description**

[Object description](/docs/sk/pre_processor/11_general_object_data_definition/11_general_object_data_definition/) includes all data associated with an object, including [geometry](/docs/sk/pre_processor/12_geometry_modelling/12_1_2d_geometry_data_defining/), [mesh](/docs/sk/pre_processor/13_mesh_generation/13_mesh_generation/), temperature, [material](/docs/sk/pre_processor/10_material_data/10_material_data/), etc.

**Material data**

[Material](/docs/sk/pre_processor/10_material_data/10_material_data/)[ data](/docs/sk/pre_processor/10_material_data/10_material_data/) includes data describing the behavior of the material under the conditions which it will reasonably experience during deformation.

**Inter object conditions**

[Inter object](/docs/sk/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/) conditions describes how the objects interact with each other, including contact, friction, and heat transfer between objects.

**Simulation controls**

[Simulation controls](/docs/sk/pre_processor/9_simulation_controls/9_simulation_controls/) includes instructions on the methods DEFORM should use to solve the problem, including the conditions of the processing environment, what physical processes should be modelled, how many discrete time steps should be used to model the process, etc.

**Inter material data**

[Inter material](/docs/sk/pre_processor/10_material_data/10_9_transformation_data/10_9_transformation_data/) data describes the physical process of one phase of a material transforming into other phases of the same material in a heat treatment process. For example, the transformation of austenite into pearlite, bainite, and martensite.

**Integrated Manufacturing Process (MO)**

DEFORM [Integrated Manufacturing Process (MO)](/docs/sk/integrated_manufacturing_process_setup/5_introduction_to_integrated_manufacturinghtm/)**** provides a user-friendly interface to construct many successive operations at the initial setup and simulate them sequentially without user interaction. MO environment facilitates the user to transfer objects across operations and connect different operations for transferring data.

## Running the simulation

A simulation engine for performing the numerical calculations required to analyze the process, and writing the results to the database file. The simulation engine reads the database file, performs the actual solution calculation, and appends the appropriate solution data to the database file. The simulation engine also works seamlessly with the Automatic Mesh Generation (AMG) system to generate a new FEM mesh on the workpiece whenever necessary. While the simulation engine is running, it writes status information, including any error messages, to the message (.MSG) and log (.LOG) files.

**Simulation engine**

The simulation engine is the program which actually performs the numerical calculations to solve the problem. The simulation engine reads input data from the database, then writes the solution data back out to the database. As it runs, it creates two user readable files which track its progress.

**Log (LOG) files**

Log files are created when a simulation is running. They contain general information on starting and ending times, remeshings (if any), may contain error messages if the simulation stops unexpectedly and type of FEM job running (32-bit or 64-bit simulation) in case of 3D jobs.

**Message (MSG) files**

Message files are also created when a simulation is running. They contain detailed information about the behavior of the simulation, and may contain information regarding why a simulation has stopped.

## **Post-processor**

A post-processor for reading the database file from the simulation engine and displaying the results graphically and for extracting numerical data. The postprocessor is used to view simulation data after the simulation has been run. The postprocessor features a graphical user interface to view geometry, field data such as strain, temperature, stress and other simulation data such as die loads. The postprocessor can also be used to extract graphic or numerical data for use in other applications. Post processor is also used to view and extract data from the simulation results in the database file. It provides an environment for the user to generate 3D PDF reports of simulation results, interpret results across database using PIP, plot results in region of interest, Coupons Data extraction to evaluate the microstructure and Mechanical property of a particular cut part along with the general post processing features.

**Related Topics:**

[Pre-Processor](/docs/sk/pre_processor/7_introduction_to_pre-processor/)

[Post-Processor](/docs/sk/post_processor/24_introduction_to_post_processor/24_introduction_to_post_processor/)

[Object Description](/docs/sk/pre_processor/11_general_object_data_definition/11_general_object_data_definition/)

[Material Data](/docs/sk/pre_processor/10_material_data/10_material_data/)

[Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/)

[Inter-Object Data](/docs/sk/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/)

[Simulation Controls](/docs/sk/pre_processor/9_simulation_controls/9_simulation_controls/)

[Simulator](/docs/sk/simulator/23_deform_simulator/23_introduction_to_deform_simulator/)

[2D Stub Shaft Labs](/docs/sk/labs/basic_labs/2d_labs/lab_25_stub_shaft_labs/)

[3D Stub Shaft Labs](/docs/sk/labs/basic_labs/3d_labs/lab05_stub_shaft_labs/)

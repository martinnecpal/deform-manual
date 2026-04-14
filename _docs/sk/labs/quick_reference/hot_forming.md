---
lang: sk
title: "Hot Forming"
---

# Hot Forming

When simulating hot forming, it is important to simulate all steps of the process including transfer from the furnace, and resting on the die, since the temperature loss due to transfer from the furnace and from die chilling can influence flow behavior. The procedure for simulating a multi-station process is detailed at the end of this section.

This section will outline the setup procedure for the following operations:

  1. Set uniform object temperature to simulate full furnace soak.

  2. Cool in air to simulate transfer from the furnace to the dies

  3. Rest on dies

  4. Forge

  5. Repeat for multiple forging blows

  1. **Create a new problem folder (directory)**

Each DEFORM problem should reside in its own folder. However, a given problem may contain many operations, all in the same database file.

  1. **Start the DEFORM preprocessor**

  2. **Set Basic Simulation Controls**

The simulation controls will be set for the first operation – simulating chilling during the transfer from the furnace to the press.

  1. Problem Title (optional)

Descriptive title for the problem – will be displayed on the screen during pre- and post-processing.

  1. Operation Name

Operation name

  1. Unit System

Select English or SI units. This will change many default values and affect how material data is imported.

  1. Select Simulation Mode

For simulating transfer of the workpiece from the furnace to the press, only heat transfer will be modeled, so turn on heat transfer, and turn off deformation.

  1. **Define the Material**

Define thermal properties for the material. For most steels, the files STEEL_E.KEY or STEEL_S.KEY contain reasonable thermal properties. These files can be loaded from the Material Properties menu on the main preprocessor window.

  1. **Define the Workpiece**

  1. Define Object Type

For most simulations, plastic object type is suitable.

  1. Define the Geometry

Geometry can be defined from an STL file.

Workpiece geometry requirements:

  * Geometry must be defined with normals facing outward

  * Always check the geometry.

  1. Mesh the Object

Typical progressions should use element sizes that represent the features of the part. When in doubt, more elements will tend to give more accurate results. Typical weights:

  * Curvature=0.9

  * Strain Rate=0.7

  * Strain =0.5

  * Temp=0

  1. Define Thermal Boundary Conditions

For solid parts, define heat exchange with the environment on all faces except the symmetry surfaces.

  1. Initialize Object Temperature

Set the initial object temperature to the furnace soak or preheat temperature.

  1. **Complete Simulation Controls**

  1. Define Number of Steps

A typical transfer operation can be simulated in 10 to 20 steps.

  1. Select the Primary Die

Enter object 1 (only object defined) as the primary die.

  1. Calculate the Time per Step

Divide the total transfer time by the number of steps.

  1. **Save the Data**

Save a Keyword file.

Go to Database Generation. Check the data. If there are any yellow or red flags, resolve them, then generate the database. Exit the preprocessor and start the simulation.

  1. **Loading Simulation Results Into the Preprocessor to Define Second Operation**

Return to the preprocessor, and load the last step from the database.

  1. **Define Material Data for the tools**

Specify thermal data for the tool material

  1. **Define the Tools**

  1. Assign Tool Names (optional)

For reference during pre- and post-processing.

  1. Define Tool Geometry

Import or define geometry for the upper die (punch) and lower die. The geometry rules detailed above for the workpiece all apply. Furthermore:

  * For multi-piece tools, draw a single tool boundary defining all inserts, knockouts, etc. The geometry can be separated later for die stress analysis. Refer to the manual or contact tech support if there is more than one moving tool for a given station.

  * Extend the tool geometry slightly across the centerline.

  * For tools with a sliding clearance between the punch and die, increase the OD of the punch to slightly intersect the die. Refer to the manual or training material for more details

  * Put a slight flat on the tip of any pointed punches.

  * While it is not strictly necessary, it is convenient to make object 2 the punch or moving object.

  1. Mesh the Tools

Use around 400 elements. Use user defined density with 3 at the contact surface and 1 on the back side of the die.

  1. Assign Tool Material

Be sure the proper material is assigned to both the tools and the workpiece

  1. Assign Tool Temperature

Set the uniform tool temperature before forming begins.

  1. **Define Interobject Data**

  1. Inter-Object Relationships

The workpiece should be slave to both tools. The interface heat transfer coefficient should be about 0.004 for English units, or 10 for SI units.

  1. Object Positioning

Using interference positioning, position the workpiece on the bottom die. Leave the top die away from the workpiece during this operation.

  1. Generate Contact Boundary Conditions

The default value of tolerance is adequate.

  1. **Complete Simulation Controls**

  1. Define Number of Steps

A typical die resting operation can be simulated in 10 to 20 steps.

  1. Select the Primary Die

Enter object 1 as the primary die.

  1. Calculate the Time per Step

Divide the total transfer time by the number of steps.

  1. Define Operation Name (optional)

  1. **Save the Data**

Save a Keyword file.

Go to Database Generation. Check the data. If there are any yellow or red flags, resolve them, then generate the database. Exit the preprocessor and start the simulation.

  1. **Loading Simulation Results Into the Preprocessor to Define Forming Operation**

Return to the preprocessor, and load the last step from the database.

  1. **Set Simulation Controls**

  1. Operation Name (optional)

  2. Select Simulation Mode

We will now simulate the forging operation, so turn deformation on (yes)

  1. **Define Material Data for Workpiece**

Assign plastic (flow) data for the workpiece material. Be sure the material selected covers the proper temperature range, including any deformation heating and die chilling.

  1. **Assign Top Die (punch) Movement**

Press behavior may play a role in results. Consult the manual or SFTC tech support for more information on press behavior.

Set the direction (typically downward). The stroke value should not be changed unless a mechanical press model is used.

  1. **Define Interobject Data**

  1. Inter-Object Relationships

Assign a friction factors. For lubricated hot forging, values of 0.2 to 0.3 are typical. For non-lubricated hot forging, values of 0.8 to 1.0 are typical..

  1. Object Positioning

Using interference, with the workpiece as the reference object, position both tools in contact with the workpiece.

  1. Generate Contact Boundary Conditions

The default value of tolerance is adequate.

  1. **Complete Simulation Controls**

  1. Define Number of Steps

  * For very limited deformation such as a square-up, use 50 steps

  * For average deformation, such as heading, use 100 steps

  * For problems with a large amount of deformation, such as extrusion, use 200 steps

  * Save every 5 to 10 steps.

  1. Select the Primary Die

Enter the object number for the punch(generally object #2)

  1. Calculate the Stroke per Step

Estimate the distance the punch will move (total stroke). Divide this value by the number of steps, and enter this value in Stroke per Step. If you are unsure of total punch stroke, add 10 or 15 extra steps. This will overshoot the goal, and you can back up a few steps to get the final result.

  1. Set stopping controls (optional)

If you know the exact distance the punch will move, enter this value under stopping controls. If no value was entered, the simulation will stop when all steps have been completed.

  1. Set substepping control

Under Advanced Step Controls, set **Strain per Step** to 0.025.

  1. **Save the Data**

Save a keyword file.

Go to Database generation, Check the data. If there are any yellow or red flags, resolve them, then generate the database. Exit the preprocessor and start the simulation.

  1. **Running a Second Operation**

  1. Identifying the endpoint of the first operation

After the simulation is completed, go to the Post-Processor, and check the results. Identify the step at which the first operation will be completed, and make a note of this step number.

  1. Loading Simulation Results Into the Preprocessor.

Return to the preprocessor, and load the appropriate step from the database.

  1. Simulate Chilling During Transfer to Next Station

Consider the transfer time between stations. Refer to the beginning of this section for guidelines on running heat transfer simulations.

  1. Changing Tool Geometry

Go to the Geometry editor, delete the tool geometry (not the whole object), and import or create new tool geometry for each tool.

  1. Positioning Objects

From Interobject reposition the tools against the workpiece using interference.

  1. Generate Contact

Initialize and generate contact boundary conditions.

  1. Reset Simulation Controls

Determine total steps and stroke per step as described above.

  1. Reset Stopping Stroke

If the stroke stopping control was used, reset the stroke to zero on object movement controls, and reset the stopping control under simulation controls.

  1. Write The Database

Writing an old database will append data to the end of the existing database. It will overwrite any steps after the step that was loaded.

  1. If the appropriate ending step is not saved…..

If you encounter a situation where, say, step 90 is not formed enough, step 100 is formed too much, and there are no steps saved in between, you can load step 90, change the save interval to 1 (save every step), then rerun the last 10 steps of the simulation to get the proper stopping step.

  

****

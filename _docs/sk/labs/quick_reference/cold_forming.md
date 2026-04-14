---
lang: sk
title: "Cold Forming"
---

# Cold Forming

When simulating cold forming, it is important to simulate all steps of the process, since the work hardening effects of early steps can influence behavior of later steps. The procedure for simulating a multi-station process is detailed at the end of this section.

  1. **Create a new problem folder (directory)**

Each DEFORM problem should reside in its own folder. However, a given problem may contain many operations, all in the same database file.

  1. **Start the DEFORM preprocessor**

  2. **Set Basic Simulation Controls**

  1. Problem Title (optional)

Descriptive title for the problem – will be displayed on the screen during pre- and post-processing.

  1. Unit System

Select English or SI units. This will change many default values and affect how material data is imported.

  1. Select Simulation Mode

For cold, isothermal simulations, deformation mode should be turned on (yes), heat transfer and all other modes should be turned off.

  1. **Define the Material**

Define Plastic material properties for the workpiece material. Material data can be loaded from the DEFORM material database. Be careful to select a material with data in the temperature range you will be simulating.

  1. **Define the Workpiece**

  1. Define Object Type

For most simulations, plastic object type is suitable.

  1. Define the Geometry

Geometry can be defined from an STL file, or by entering table data.

Workpiece geometry requirements:

  * Geometry normals must always face outward

  * Always check the geometry.

  1. **Mesh the Object**

Typical progressions should use element sizes representative of the geometric detail of the part. When in doubt, more elements will tend to give more accurate results. Typical weights:

  * Curvature=0.9

  * Strain Rate=0.7

  * Strain =0.5

  * Temp=0

  1. **Define Boundary Conditions**

Symmetric planes should be defined either with a velocity boundary condition or with a symmetry boundary condition.

  1. **Define the Tools**

  1. Assign Tool Names (optional)

For reference during pre- and post-processing.

  1. Define Tool Geometry

Import or define geometry for the punch and die. The geometry rules detailed above for the workpiece all apply. Furthermore:

  * For multi-piece tools, draw a single tool boundary defining all inserts, knockouts, etc. The geometry can be separated later for die stress analysis. Refer to the manual or contact tech support if there is more than one moving tool for a given station.

  * Extend the tool geometry slightly across the centerline.

  * For tools with a sliding clearance between the punch and die, increase the OD of the punch to slightly intersect the die. Refer to the manual or training material for more details

  * Put a slight flat on the tip of any pointed punches.

  * While it is not strictly necessary, it is convenient to make object 2 the punch or moving object.

  1. Define Press Movement for the Punch

In general, press speed will not influence simulation results for cold forming simulations. A constant press speed of 10 in/sec or 250mm/sec is generally adequate. Set the direction (typically downward for punch on top). The stroke value should generally not be changed by the user.

  1. **Define Interobject Data**

  1. Inter-Object Relationships

The workpiece should be slave to both tools. For well lubricated cold forming, a friction factor of 0.08 is reasonable.

  1. Object Positioning

Using interference, with the workpiece as the reference object, position both tools in contact with the workpiece. For extremely small parts, a smaller interference tolerance may be necessary to prevent excessive tool-workpiece overlap.

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

Estimate the distance the punch will move (total stroke). Divide this value by the number of steps, and enter this value in Stroke per Step. If you are unsure of total punch stroke, add 10 or 15 extra steps. This will overshoot the goal, and you can back up a few steps

to get the final result.

  1. Set stopping controls (optional)

If you know the exact distance the punch will move, enter this value under stopping controls. If no value was entered, the simulation will stop when all steps have been completed.

  1. Set substepping control

Under Advanced Step Controls, set **Strain per Step** to 0.025.

  1. **Save the Data**

Save a Keyword file.

Go to Database Generation. Check the data. If there are any yellow or red flags, resolve them, then generate the database. Exit the preprocessor and start the simulation.

  1. **Running a Second Operation**

  1. Identifying the endpoint of the first operation

After the simulation is completed, go to the Post-Processor, and check the results. Identify the step at which the first operation will be completed, and make a note of this step number.

  1. Loading Simulation Results Into the Preprocessor.

Return to the preprocessor, and load the appropriate step from the database.

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

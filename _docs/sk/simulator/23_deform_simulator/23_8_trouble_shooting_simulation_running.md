---
lang: sk
title: "23.8. Trouble Shooting Simulation Running"
---

# 23.8. Trouble Shooting Simulation Running

23.8.1. Message file messages

23.8.2. Simulation aborted by user error or License related errors

23.8.3. Cannot remesh at a negative step

23.8.4. Remeshing is highly recommended

23.8.5. Negative Jacobian

23.8.6. Solution does not converge

23.8.7. Stiffness matrix is non-positive definite

23.8.8. Zero pivot

23.8.9. Extrapolation of data

23.8.10. Bad Element Shape

23.8.11. Inconsistent Step Number

23.8.12. Exceed system memory limit

The message file is an iteration by iteration account of the simulation. It shows how close each iteration is to converging to the final solution by calculating a relative error norm between successive steps for both nodal velocities and nodal forces. There is also information given on node contact being generated and also if there is a sudden stop. The log file is an account of the module execution.

## Message file messages

If a simulation stops early, it is recommended to check the end of the message file to see why the simulation stopped. While a simulation is run under the batch mode of operation, there are three places in which the end of operation may be indicated. The message file is where the simulation will indicate a normal stoppage of the FEM module. If there is an abnormal stoppage in simulation, due to an illegal operation in the FEM module or in the mesh generation, this will be indicated in either the .LOG file or in the command window where DEFORM was initially called. This may be also accompanied by a core file which should be deleted as soon as possible since they often consume a large amount of disk space.

## Simulation aborted by user error or License related errors.

The following information is valid only up to DEFORM2D v9.1 or DEFORM3D v6.1. or while running these products using the license manager released with DEFORM v10.0.

When DEFORM is installed, the permission for the status file (which monitors simulations running on the machine) should be set using the command 'chmod 777 DEFORM.STA'. If this is not done, the FEM engine cannot write to the status file and hence exits. To restart the simulation, first go to the DEFORM_DIR, run INSTALL3D and select the option to regenerate the status file.

Note:

If the user gets the message Command not found, the user should run the INSTALL3D by typing ./INSTALL3D. This will force the operating system to override the paths and force the system to run only the file in the current directory.

Using DEFORM with new License Manager, if you experience any program stop with the following message/pop up dialog, the potential reasons when running the License Manager and DEFORM on the same machine: LManagerServer.exe has stopped working, did not start on a system restart, hardware key has been removed while DEFORM is running or bad combination of hardware key and password file are used.

When running the License Manager and DEFORM on different machines, apart from the above reasons, a break in network connection between the License Server and the client machine running DEFORM is a possibility. Fig. 23.8.1. shown the error message in this scenario.

![]({{ '/assets/images/simulator/23_deform_simulator/23_8_trouble_shooting_simulation_running/image001.jpg' | relative_url }})

License Server error

## Cannot remesh at a negative step

The FEM engine prints this message and exits when a remeshing has just taken place and in the current step a negative Jacobian is encountered so remeshing has to take place again. This simulation normally arises when remeshing has failed to produce a valid mesh. Stopping the simulation prevents the DEFORM system from encountering a never ending loop.

The reasons for this could be that the time step (DSMAX, DTMAX) may be large as might happen in extrusions where the ram speed might be low but the velocity of the extrudate might be very high causing severe mesh distortion near the die radius. Another example would be in a forging when material starts to flash and the elements near the flash region get severely distorted. To avoid this problem, the time step can be reduced, the number of mesh elements can be increased or the mesh density in the area where distortion occurs can be increased.

Plotting the node velocities in the [Preprocessor](/docs/sk/pre_processor/7_introduction_to_pre-processor/) can be helpful. It is not recommended for the displacement of the nodes each[ time step](/docs/sk/pre_processor/9_simulation_controls/9_2_defining_step/) be larger than the edge length of the elements. [Polygon edge length substepping](../../pre_processor/9_simulation_controls/9_2_defining_step.htm#Polygon_length_sub_step_\(DPLEN\)) can be useful in this case.

## Remeshing is highly recommended

  
Remeshing is Highly Recommended because of Unbalanced Mismatch between Master and Slave is a message that occurs when the size of the elements on the slave and master surface are not proper. When specifying master-slave relationships between objects the following rules should be adhered to:

  * the slave is the softer material

  * the slave should have a finer/denser mesh than the master

This mesh is very important in the region where the slave and master contact each other. If the mesh on the master is much denser than the slave's mesh in a region where they contact the results of the simulation will not be accurate. If the ratio of the number of elements on the contact surface between the master and slave is greater than 3:1 then the message 'Remeshing is highly recommended because of unbalanced mismatch between master and slave' is printed as a warning in the message file. This will reduce the accuracy of the solution and steps should be taken by the user to change the [mesh densities](/docs/sk/pre_processor/13_mesh_generation/13_mesh_generation/) on the objects.

## Negative Jacobian

  
DEFORM uses the finite element method to solve problems of large deformation and AMG (Automatic Mesh Generator) to automatically provide an optimized remeshing capability. In most cases, the meshing and remeshing runs very smoothly. There are cases though, where a simulation will not continue due to a negative Jacobian (unacceptable mesh) at a step immediately after a remeshing operation. In most cases, these can be easily identified from one of the following areas:

A closed forging lap will usually lead to this problem. Look at your progressions carefully and see is there is a small area where a lap has formed and closed. If such a lap is detected and you would like to continue the simulation, you may try,

  * Use the Surface Patch feature in the [Preprocessor](/docs/sk/pre_processor/7_introduction_to_pre-processor/) under Objects Geometry can be useful. Folds will appear as short red lines that do not appear to highlight a single element. Be sure to view the object from multiple angles before deciding that a red mark is a fold, because surface patches from the far side of the object can be misleading. Modify the geometry to remove the lap, and continue the simulation. This will require remeshing and interpolation to maintain the strain, temperature and damage history.

  * If, for any reason a node has penetrated one of the dies, the remeshing will become problematic. This can be evaluated by looking at the FEM MESH of all objects at the step just prior to remeshing. A node that is inside the die surface will move back to the die surface after remeshing and interpolation of boundary conditions, but an element that had an acceptable geometry can be highly distorted during this process.

  * If the user sets a problem with very large time steps, and little to no [substepping criteria](../../pre_processor/9_simulation_controls/9_2_defining_step.htm#Sub-stepping_Controls), this can lead to a problem resulting from a mesh distorting severely during the first step. Refer to [time step definition criteria](../../pre_processor/9_simulation_controls/9_2_defining_step.htm#9.2.2.Step_Increment) in the [Preprocessor](/docs/sk/pre_processor/7_introduction_to_pre-processor/) section of this manual.

  * If sub stepping is disabled in a 3D simulation, great care must be taken to use sufficiently small time steps. This means that any time a node displacement calculates a node position inside a rigid object, the node is pushed back to the die surface. This is not a bad assumption if the node displacements are small, however, if the node displacements are large this assumption may lose its validity.

These suggestions are intended as general guidelines and may not solve all of this class of problem. If all of these areas have been investigated and subsequent attempts to run your problem fail, we would recommend sending us a keyword file for further investigation.

## Solution does not converge

  
There are several common reasons for a solution not converging.

  1. The material has a large rigid body motion. Much of the deforming body has a very low strain rate or is rigid.

  2. The material is not strain rate sensitive.

  3. Elasto-plastic material is undergoing large deformation or has an inappropriate initial guess.

In cases where a problem will not converge, the following checklist should help with the troubleshooting process. This will help with the most common cases.

  * Increase your[ Force Norm or Velocity Norm](../../pre_processor/9_simulation_controls/9_5_solver_settings.htm#Convergence_error_limits_\(CVGERR\)) up to one order of magnitude. The Force Norm may in fact be raised as high as .1 or even eliminated for a few steps. This should not lead to significant error, but could result in reduced accuracy of load calculations. If convergence is improved, allow the simulation to run for 3 or 4 steps, then try reducing the settings to their original values.

  * If the simulation is being run with principal [die movement](/docs/sk/pre_processor/15_movement_controls_definition/15_movement_controls_settings/) under load or energy control, run a couple of steps under speed control to allow the solution to stabilize before continuing under the original mode.

  * Increase your [limiting strain rate](../../pre_processor/16_object_properties/16_1_deformation_properties.htm#16_1_6_Limiting_strain_rate_\(LMTSTR\)) to 1/50 or 1/100 of the average strain rate. This should not cause any significant effect on solution accuracy. If you have an extremely difficult case to converge, this value may be lowered to 1/10 of the average strain rate for a few steps, then reset to a more normal value. Over the years, we have recommended that the limiting strain rate should be 1/100 to 1/1000 of the average strain rate. If this value is set too low, it will result in an artificially lower load calculation.

  * Check your [material data](/docs/sk/pre_processor/10_material_data/10_material_data/) versus your process conditions to insure that no "strange" material properties are being passed to the FEM engine. Be particularly aware of extrapolation issues. For example, if your process conditions are in an area that is outside of the defined flow stress region, this "reverse strain rate sensitivity" create a problem (See Fig. 23.8.2.) that is almost impossible to allow DEFORM to converge on an accurate solution. This may be handled by re-evaluating your raw data and adjusting it as required. Since it is highly unlikely that a material has a lower flow stress at a higher strain rate, the common cause for this type of data is the lack of an adiabatic heating correction. In other words, adiabatic heating at the higher strain rates artificially heated and softened the material causing an apparently lower flow stress. If no clear cause can be determined, find data that does not exhibit this reverse strain rate sensitivity.

![]({{ '/assets/images/simulator/23_deform_simulator/23_8_trouble_shooting_simulation_running/image002.jpg' | relative_url }})

Extrapolation of the flow stress leading to reverse strain rate

  * Lower your [penalty constant](../../pre_processor/16_object_properties/16_1_deformation_properties.htm#16_1_4_Volume_penalty_constant_\(PENVOL\)) of plastic objects to 250,000 to 500,000 using a constant value ([PENVOL](/docs/sk/keyword_documentation/p/penvol/)). This may lead to volume loss if the value is much lower than 100,000 for typical engineering materials.

  * Reduce your time step. This advice applies particularly for elastic-plastic materials. A very small time step can frequently allow the DEFORM system to get through a tough region of convergence. After a large number of nodes are in contact with dies and the simulation is in progress, a larger time step can be resumed. This may be accomplished through either controlling the time step or a control modifier that will lead to sub stepping such as [DEMAX](/docs/sk/keyword_documentation/d/demax/).

  * Change the initial guess calculation method. Refer to [Object Properties](/docs/sk/pre_processor/16_object_properties/16_object_properties/) for a discussion of EP Initial Guess.

  * In the case of cold materials that exhibit little to no strain rate sensitivity, this is one of the hardest cases to gain convergence. In fact there should be a very slight strain rate sensitivity even in the cold forging world. A user may help with convergence by creating an artificial strain rate sensitivity. This is not far from reality and may be done by adding a data set of flow stress at a higher strain rate with slightly higher flow stress data. See Fig. 23.8.3. for an idea of how to handle this type of issue.

  * In a few cases, convergence problems can be caused by a course mesh in an area with high local deformation, such as under the corner of a punch during a piercing operation. In these cases, generate a finer mesh and set the remeshing criteria to have a higher bias towards boundary curvature and strain rate.

![]({{ '/assets/images/simulator/23_deform_simulator/23_8_trouble_shooting_simulation_running/image003.jpg' | relative_url }})

Extrapolation of the flow stress leading to reverse strain rate

  * In a few cases, convergence problems can be caused by a course mesh in an area with high local deformation, such as under the corner of a punch during a piercing operation. In these cases, generate a finer mesh and set the [remeshing criteria](../../pre_processor/13_mesh_generation/13_2_3d_tet_mesh_generation.htm#13.2.8._Remeshing_criteria) to have a higher bias towards boundary curvature and strain rate.

These suggestions are intended as general guidelines and may not solve all non-convergence problems. Although DEFORM has excellent convergence behavior for most problems, the occasional problem will occur where the user experiences some difficulty. If all of these attempts fail, we would recommend sending us a keyword file for further investigation.

## Stiffness matrix is non-positive definite

DEFORM uses the finite element method to solve problems of plastic deformation, heat transfer and elastic deflection. When using this method, a material stiffness matrix is defined by geometry and material properties. When the user sees a message "non positive definite stiffness" or "zero pivot", this is caused by a stiffness matrix that has a zero value. This problem is usually caused by a material property having a zero value that is related to the "stiffness" or resistance to flow, heat or deformation.

For a given type of simulation, there is a property that is most likely to lead to this problem. It is as follows:

  * **Heat Transfer** : [Heat Capacity](../../pre_processor/10_material_data/10_3_thermal_data/10_3_thermal_data.htm#Heat_capacity) and/or T[hermal Conductivity.](../../pre_processor/10_material_data/10_3_thermal_data/10_3_thermal_data.htm#Thermal_conductivity)

  * **Elastic** : [Young's Modulus](../../pre_processor/10_material_data/10_2_elastic_data/10_2_elastic_data.htm#Young's_modulus).

  * **Plastic****Deformation** : [Flow Stress](/docs/sk/pre_processor/10_material_data/10_1_plastic_data/10_1_1_flowstress/10_1_1_flow_stress_models/).

  * Heat transfer problems can be identified by the information in the message file. The iteration information will contain the heading Temperature Error Norm in the section just prior to the problem being terminated.

  * Plastic deformation problems can be identified clearly by the information in the message file. The iteration information will contain the headings Force Error Norm and Velocity Error Norm in the section just prior to the problem being terminated. These messages will also be seen during the elastic (die stress) type of problem.

## Zero pivot

Rigid body motion can lead to the "zero pivot" error. This leads to the velocity norm increasing and a resulting simulation failure. This typically results from the lack of adequate boundary conditions and can be resolved by properly defining these. For a 2D case, there are four possible geometric modes: [Axisymmetric](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#Axisymmetric), [Plane Strain](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#Plane_strain), [Plane Stress](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#Plane_stress) and [Torsion](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#Torsion) simulations. In the case of an axisymmetric and Torsion simulation, only the y-direction needs constraint. In the case of a plane strain and plane stress simulation, both the x and y directions need to be constrained for the meshed objects. For the case of rigid objects, these do not need any constraint since they act more as boundary conditions.

## Extrapolation of data

Many of these problems are not the result of "bad data" or the user neglecting to input the data properly. The problem has to do with a data set that does not cover the process being modeled. This being the case, the available data is extrapolated to the process window. In this case, the material needs to be updated to include data in the actual process window or adjusted (best estimate) to insure that values at or below zero cannot occur when these critical properties are included in the stiffness equations. See Fig. 23.8.4. for a further description.

![]({{ '/assets/images/simulator/23_deform_simulator/23_8_trouble_shooting_simulation_running/image004.jpg' | relative_url }})

Automatic extrapolation of the Heat Capacity data

## Bad Element Shape

This is a error created in the FEM engine which warns of dangerous distortion in the mesh of a 3D simulation. The two main causes for this error is a negative jacobian shape that cannot be resolved or a lack of flow stress values. In the case of the negative jacobian, the problematic elements (along with the node coordinates for the problem elements) will be listed in the file BUG.MSG. If every element in the mesh is listed, the flow stress for the object was probably not defined. If there are only a few elements listed, the user may try to load the bad step into the Pre-Processor and check the shape of the elements and the Boundary Condition code. The importance of well-defined boundary conditions cannot be overemphasized. This includes meaningful contact conditions and fixed velocity conditions.

## Inconsistent Step Number

This implies that a while the simulation was started/restarted, the most recent step in the database is not a negative step. In the case of DEFORM, a negative value on a step is simply a flag to indicate that a start/restart is possible. The negative value says nothing algebraic as it is merely a flag. The cause of this error can be any of the following:

An already run simulation was submitted and needs to have a negative step added to the end. Simply creating a negative step in the [Pre-Processor](/docs/sk/pre_processor/7_introduction_to_pre-processor/) and [submitting the simulation](/docs/sk/simulator/23_deform_simulator/23_1_start_stop_and_resume_simulations/) again can remedy this.

A simulation needed to be remeshed and a [Pre-Processor](/docs/sk/pre_processor/7_introduction_to_pre-processor/)could not generate a negative step prior to restarting the simulation. If this occurs, please review the simulation and make sure that no problems with [boundary conditions](/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/) occurred prior to the failure. Also, check that there is plenty of disk space available and that full write privileges are available in the directory of interest. If no reason can be determined, please contact SFTC at [support@deform.com](mailto:support@deform.com).

## Exceed system memory limit

For extremely large size model, the user may face FEM stop issue because of exceeding system memory limit. By default, the FEM solver will now switch from CG to SPARSE in all problems. This will provide improved runtime in most cases. The SPARSE solver consumes more system memory than the CG solver, though. Thus, 32bit or 64bit 3D FEM may now be more susceptible to stopping if the model size is too large to fit in available system memory. Memory limitations imposed on 32bit processes may also cause 32bit 3D FEM to stop due to model size. 64bit FEM is recommended for 3D simulations, particularly those with large models. The user can activate and control the solver switching in the [Simulation Control - Control Files](/docs/sk/pre_processor/9_simulation_controls/9_8_control_files/) page.

**Related Topics:**

[2D Geometry types](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#9.1.2._Geometry_type_\(GEOTYP\)_\[2D\])

[Step controls selection from Simulation controls](/docs/sk/pre_processor/9_simulation_controls/9_2_defining_step/)

[Step increment controls](../../pre_processor/9_simulation_controls/9_2_defining_step.htm#Step_increment_control_\(DSMAX/DTMAX\))

[Velocity and Force error norms settings in Simulation controls](../../pre_processor/9_simulation_controls/9_5_solver_settings.htm#Convergence_error_limits_\(CVGERR\))

[Object types](../../pre_processor/11_general_object_data_definition/11_general_object_data_definition.htm#11.4._Object_type)

[2D-remesh Criteria](../../pre_processor/13_mesh_generation/13_1_2d_mesh_generation.htm#13.1.8._Remeshing_criteria)

[3D-Remesh criteria](../../pre_processor/13_mesh_generation/13_2_3d_tet_mesh_generation.htm#13.2.8._Remeshing_criteria)

[Boundary conditions](/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/)

[Inter-Object contact conditions](/docs/sk/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/)

[Material properties](/docs/sk/pre_processor/10_material_data/10_material_data/)

[Object properties](/docs/sk/pre_processor/16_object_properties/16_object_properties/)

[Limiting strain rate settings in Object properties](../../pre_processor/16_object_properties/16_1_deformation_properties.htm#16_1_6_Limiting_strain_rate_\(LMTSTR\))

[EP Initial guess](../../pre_processor/16_object_properties/16_1_deformation_properties.htm#16_1_2_Elasto-plastic_initial_guess_\(ELPSOL\))

[Submitting the problem to simulate](/docs/sk/simulator/23_deform_simulator/23_1_start_stop_and_resume_simulations/)

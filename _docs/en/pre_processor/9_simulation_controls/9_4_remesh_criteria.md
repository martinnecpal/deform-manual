---
lang: en
title: "9.4. Remesh Criteria"
---

# 9.4. Remesh Criteria ![]({{ '/assets/icons/pre_icons/mo_remeshing_criteria.jpg' | relative_url }})

9.4.1. Maximum interference depth (RMDPTH)

9.4.2. Maximum stroke increment (RMSTRK)

9.4.3. Maximum time increment (RMTIME)

9.4.4. Maximum step increment (RMSTEP)

9.4.5. Penetration Distance (absolute)

9.4.6. Penetration Distance (relative)

9.4.7. Additional remeshing criteria

9.4.8. Remeshing Method

**[2D, 3D]** : Remeshing Criteria (Autoremesh) is the most convenient way to handle the remeshing of objects undergoing large plastic deformation. The Remeshing Criteria Window ( Fig. 9.4.1. )contains a group of parameters that control when and how often the mesh will be regenerated on a meshed object based on assignment of certain triggers.There are four keywords that control the initiation of a remeshing procedure ([RMDPTH](/docs/en/keyword_documentation/r/rmdpth/), [RMTIME](/docs/en/keyword_documentation/r/rmtime/), [RMSTEP](/docs/en/keyword_documentation/r/rmstep/) and [RMSTRK](/docs/en/keyword_documentation/r/rmstrk/)) for an object. When the remeshing criteria of any of these keywords has been fulfilled or the mesh becomes unusable (negative Jacobian), the object will be remeshed. During the simulation, if an object satisfies any of its remeshing criteria, a new mesh is generated, the solution information from the old mesh is interpolated onto the new mesh and the simulation continues.

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_4_remesh_criteria/9_4_image001.jpg' | relative_url }})

(a)

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_4_remesh_criteria/9_4_image002.jpg' | relative_url }})

(b)

Remeshing Criteria Window; (a) For 2D, (b) For 3D

## Maximum interference depth (RMDPTH) [2D, 3D]

The maximum Interference Depth ([RMDPTH](/docs/en/keyword_documentation/r/rmdpth/)) is used to start a remeshing procedure. If any portion of a master object penetrates a slave object beyond the depth specified under RMDPTH, remeshing will be triggered. 

## Maximum stroke increment (RMSTRK) [2D, 3D]

Anytime the maximum stroke increment ([RMSTRK](/docs/en/keyword_documentation/r/rmstrk/)) is exceeded by the stroke increment of the primary die since the last remeshing step, a new remeshing step will be initiated. 

## Maximum time increment (RMTIME) [2D, 3D]

Anytime the Maximum Time Increment ([RMTIME](/docs/en/keyword_documentation/r/rmtime/)) (Value of Elapsed Time) has elapsed since the last remeshing step, a new remeshing step will be initiated. 

## Maximum step increment (RMSTEP) [2D, 3D]

Anytime the Maximum Step Increment (Number of Steps) has occurred since the last remeshing step, a new remeshing step will be initiated.

**Purpose of Criteria [2D, 3D]**

When a sharp edge on a tool or die impinges on the workpiece, the sharp edge may deeply penetrate an element edge. If this depth is severe, the elements may get stretched out and remeshing may become difficult. Before this depth is achieved, remeshing with place nodes about the edge and allow the simulation to continue unhampered.

## Penetration Distance (absolute) [3D]:

If a positive number (in the unit of length) is entered, the program will conduct a check on each surface edge that has a contact node on each end. The distance from the middle of the edge to the die surface is calculated. If the maximum penetration depth exceeds the specified limit, remeshing will be triggered.

## Penetration Distance (relative) [3D]:

If a negative number (a fraction) is entered, the program will conduct a check on each surface edge that has a contact node on each end. The distance from the middle of the edge to the die surface is calculated and divided by the original length of the edge. If the ratio exceeds the magnitude of the specified value, remeshing will be triggered.

**Default Value [3D]:**

The pre-processor now has a default value 0.7 with a relative setting.

## Additional remeshing criteria [3D]

  * **Stretch limit** : Stretch of an edge is calculated as “(Current Length-Original Length)/Original Length”. If this value exceeds the specified limit, then remeshing is performed.

  * **Shrinking limit** : Shrink of an edge is calculated as “(Current Length-Original Length)/Original Length”. If this value exceeds the specified limit, then remeshing is performed.

##  Remeshing Method [3D]

**Global and Local Remeshing Options [3D]**

For DEFORM-3D, mesh generation has been enhanced with local meshing functionality.

Default settings point to existing global remeshing procedures, where in every element of the old mesh gets replaced with new mesh element, followed by interpolation.

New Local meshing functionality allows several options to control the element size and quality. Local remeshing also has options to keep the meshing truly local, to minimize the interpolation related errors .(See Fig. 9.4.3.) In the current version, all the local meshing related settings are stored in the local files, not in the database.

This means when the user copies the database file from one folder to another, local remesh settings will not be carried over unless all the files are copied to the working folder.

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_4_remesh_criteria/9_4_image003.jpg' | relative_url }})

Global Remeshing criteria window

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_4_remesh_criteria/9_4_image004.jpg' | relative_url }})

Local Remeshing criteria window

**Internal Elements:**

  * **S****ize control** :

  * **Average of Neighbors** : The size of the element is decided based on the average size of the surrounding elements of distorted mesh.
  * **Scaling Factor** : The size of the element will be scaled based on the scaling factor mentioned for each layer inward.

  * **Skip Elements with Good shape** :The elements which are of good shape will be skipped from remeshing.

**Related Topics:**

[9.1. Simulation type Settings](/docs/en/pre_processor/9_simulation_controls/9_1_simulation_type_settings/)

[9.2. Defining Step](/docs/en/pre_processor/9_simulation_controls/9_2_defining_step/)

[9.3. Stopping Controls](/docs/en/pre_processor/9_simulation_controls/9_3_stopping_controls/)

[9.5. Solver Settings](/docs/en/pre_processor/9_simulation_controls/9_5_solver_settings/)

[9.6. Process Conditions](/docs/en/pre_processor/9_simulation_controls/9_6_process_conditions/)

[9.7. Advanced Options](/docs/en/pre_processor/9_simulation_controls/9_7_advanced_options/)

[9.8. Control Files](/docs/en/pre_processor/9_simulation_controls/9_8_control_files/)

[9.9. Thermomechanical variables](/docs/en/pre_processor/9_simulation_controls/9_9_thermomechanical_variables/)

[13\. Mesh Data Definition](/docs/en/pre_processor/13_mesh_generation/13_mesh_generation/)

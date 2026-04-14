---
lang: sk
title: "2D Die Stress Analysis Theory"
---

# 2D Die Stress Analysis Theory

1\. Overview

2\. Types of analyses

3\. Practical Considerations

4\. Die Failure Modes

5\. Required Data

6\. Die Stress Setup

7\. Defining a Press Fit

8\. Quick Summary of Shrink Fit Boundary Condition

9\. Important Measurements of Stress

10\. Interpretation of Stress

## Overview

This section of the manual discusses the theoretical aspects of performing a die stress analysis. A die stress analysis is a computational method for determining the amount and distribution of stress in a tool during a forging (or any case with deformation) simulation. The purpose of a tool stress analysis is to help pinpoint the root cause of tool failure or to identify likely areas of tool failure in a given forging design. This requires a considerable amount of engineering understanding of stress and of how the assembly functions. Understanding stress will assist the user with a reasonable interpretation of the results. Engineering judgment is important in making decisions how to organize a meaningful simulation of the tool response and interpretation of results. Some key considerations in setting up die-stress analyses are:

Tools do not function in isolation. The tool objects need to react against other objects in order to deform by the forming stresses. How to define the boundary conditions for tools of interest is a very important concern for the simulation.

It is important to consider not only the behavior of the actual forming die or insert, but also the support structure for that tool. In cases where other tools directly interact with a tool, especially if there is some preload on a tool prior to loading, to obtain the correct stress state requires careful analysis of this preloading.

There are a several different approaches that may be applied in a simulation as well as many different criteria used to interpret the results. This document will explain the various methods for performing die stress as well as clarify which interpretation methods are best suited for particular cases. In Fig. 1 is seen a sample result of a die stress analysis with three objects considered. The output of the simulation is the stress in each body that will give an indication of potential failures.

![]({{ '/assets/images/operation_templates/30_die_stress/2d_die_stress_analysis_theory/image0001.jpg' | relative_url }})

Die stress analysis showing stresses in insert, case and backing plate

## Types of analyses

There are two general types of analysis (the first being the recommended case for most analyses):

  1. **Decoupled analysis (one step)** : In this analysis, a deformation simulation is first performed with a deformable workpiece and rigid dies (See Fig. 2). After this first step is performed, a new problem is created and the step of interest from the forming simulation is loaded. The forces from the deforming body are then interpolated on the elastic die. After this, one step of analysis is performed to compute the stresses within the elastic die. The pros for this type of analysis are that it is very simple to setup and is quick to run as well as the ability to experiment with support and/or insert shape without changing the cavity shape. The cons for this is only one instance of time is analyzed per analysis and the compliance of the tools is not considered in the deformation of the workpiece.

**Note:** This analysis is a reasonable approximation as long as the tool deflection is negligible. In most, but not all forming processes, this is a good assumption.

  1. **Coupled analysis (one or more deforming dies while the workpiece is deforming):** In this simulation, the tool of interest is made elastic and given a mesh (See Fig. 3). The entire deformation simulation is run with this die as elastic and stresses of the die are made available for every saved step. There are two drawbacks with running this type of simulation.

The run time is substantially longer than the case of the single deforming body.

The difficulty in setting up the problem is substantially increased.

![]({{ '/assets/images/operation_templates/30_die_stress/2d_die_stress_analysis_theory/image0002.jpg' | relative_url }})

Sketch of uncoupled die stress analysis

The left image shows that first a deformation analysis is performed and the right image shows that the forces are interpolated onto an elastic die to calculate the stresses on the die.

![]({{ '/assets/images/operation_templates/30_die_stress/2d_die_stress_analysis_theory/image0003.jpg' | relative_url }})

Sketch of a coupled analysis of deformable die and workpiece

##  Practical Considerations

Additionally, the following options may be considered for this analysis:

  1. Thermal analysis can be considered either as a coupled or one step analysis.

  * In the case of a coupled analysis, this may be important to consider for warm and hot forming simulations since the elastic properties for the tool material may change dramatically at these temperatures. 

  * In the case of a one step analysis, thermal expansion may be considered if necessary. During the deformation solving, the rigid die of interest should have a thermal profile consistent with practice.

  1. Forming equipment interaction can be included in either a coupled or one step analysis. 

  2. Multiple deforming bodies, including multiple shrink fits can be accurately simulated as discrete objects. In the case where the tool of interest has a shrink fit applied to it, it is necessary to consider this effect in order to calculate the correct stresses on the tools.

  3. Forging load. The correct forming load is necessary to obtain correct die stress values. In order to be able to predict an accurate forging load, several variables are required to be accurate. Among these are:

  * Material flow stress data

  * Workpiece history (e.g. Correct temperature, Correct strain distribution)

  * Die fill (In closed die forgings, load increases considerably as corners fill)

![]({{ '/assets/images/operation_templates/30_die_stress/2d_die_stress_analysis_theory/image0004.jpg' | relative_url }})

Mid-stroke die failure with the stress-stroke curve

## Die Failure Modes

The various modes of die failure are as follows:

  1. **Catastrophic failure by brittle fracture** \- This usually can be avoided through a simple force/area calculation.

  2. **Plastic deformation** \- This can be determined by comparing the stress results of the die stress analysis to the yield stress of the die material.

  3. **Low Cycle Fatigue (LCF) failure****by cyclic, thermal and mechanical loading** -This occurs when stresses are below yield for the die material but over many cycles of tensile loading lead to failure in the die. The manner in which to reduce this is to reduce or eliminate the tensile stresses.

  4. **Wear** \- The most preferred mode of failure for dies. The estimation of this is outside the scope of die stress analysis. (For more information on this topic, please refer to the [20.4. Inter-object Data Tool wear section](/docs/sk/pre_processor/20_inter-object_data_definition/20_4_tool_wear/) )

## Required Data

The required data to perform a die stress analysis are,

  1. Die geometry.

  2. Die support and mounting conditions.

  3. Forces on the surface of the die from the workpiece.

**Note** :

This requires an accurate load in the deformation simulation to accurately predict stress and deflection.

  1. Temperature distribution in the dies (for non-isothermal analysis).

  2. Elastic (and thermal if applicable) die material properties.

  3. Shrink fit.

  4. Any residual stress or other preloads.

## Die Stress Setup

  1. Run flow analysis.

  2. Identify critical steps in flow simulation.

  * End of stroke.

  * Other step where tools may see non-uniform load.

  1. Create a new problem for die stress analysis.

  2. Import critical stress from deformation database.

  3. Import support tools.

  4. Assign velocity boundary conditions to constrain tools.

  5. Interpolate forces from flow simulation workpiece to tool surfaces.

  6. Define press fits between tools and cases.

  7. Assign tool master-slave relationships.

  8. Write a database and run the simulation.

## Defining a Press Fit

A press fit is the case where two tools are fitted together with equilibrium dimensions that slightly overlap. When the two tools are fitted together, there is a significant amount of stress that is developed between the two objects before any forging load is applied. The purpose for this is to maintain a compressive circumferential preload that would control tensile stresses in the hoop direction. This is very important in the case of carbide tools where tool life is reduced significantly in the presence of tensile stresses.

Press fitting can be modeled using two elastic dies. An elastic object can be simplistically considered as a spring (See Fig. 5). When both objects are pressed together, the lowest amount of energy required to deflect both objects will determine the final stress state. Each die should be drawn to fit exactly coincident with the other die (i.e. no overlap). After this, the press fit should be applied as a “shrink fit” boundary condition on one of the dies. An insert-case combination cross-section is shown in Fig. 6a where the shrink fit is applied to the inner radius of the case. When the simulation starts, the case will apply a force to the insert. These two bodies will both deflect in order to minimize the total distortion energy stored in the two objects (See Fig. 6b). Similarly, this can also be done in terms of the shrink fit applied to the insert. The insert can be having an applied shrink fit to the outer radius (See Fig. 7a). When the simulation is performed, these two bodies will both deflect in order to minimize the total distortion energy stored in the two objects (See Fig. 7b). It is very important to consider a press fit for an accurate die stress analysis since often the press fit has a very significant contribution to the overall stress state of the assembly. It is good to check this with no interpolated forces for further assurance that the amount of press fit being used does not exceed limits for safety running a forging.

## Quick Summary of Shrink Fit Boundary Condition

As a quick summary to describe how to apply shrink fit boundary conditions, perform the following actions in order:

Draw tool surfaces together and position them so that the contacting surfaces coincide perfectly.

Assign a shrink fit boundary condition to either the insert or the case. The interference value should be one half of the diameter difference.

Generate contact between the two contacting objects. If contact is not generated with the default contact tolerance, please increase the contact tolerance slightly in order to generate contact.

![]({{ '/assets/images/operation_templates/30_die_stress/2d_die_stress_analysis_theory/image0005.jpg' | relative_url }})

Consider the insert and case to be 2 springs

![]({{ '/assets/images/operation_templates/30_die_stress/2d_die_stress_analysis_theory/image0006.jpg' | relative_url }})

(a) Assign a positive displacement to the inside of the case (b) When simulation starts, the system snaps into equilibrium

![]({{ '/assets/images/operation_templates/30_die_stress/2d_die_stress_analysis_theory/image0007.jpg' | relative_url }})

(a) Assign a positive displacement to the outside of the insert (b) When simulation starts, the system snaps into equilibrium.

## Important Measurements of Stress

Stress is a important concept in mechanical engineering. For a general overview, please refer to the fundamental concepts section in the manual. 

  1. **Effective Stress (Von Mises)** \- an accepted measurement of initial yielding when this stress exceeds the yield strength of the die material (at temperature).

  2. **Maximum Principal Stress** \- in the case of carbide, tensile stresses will certainly result in a premature LCF failure - in hardened die steels, this increases tendency towards LCF failures. This quantity is the maximum possible stress at a single point in some give orientation (See Fig. 8.).

  3. **Stress Components** \- when troubleshooting die problems, the components are very useful in determining root causes and studying design alternatives.

  4. **Mean Stress** \- this stress state is generally not of critical importance in die stress analysis.

![]({{ '/assets/images/operation_templates/30_die_stress/2d_die_stress_analysis_theory/image0008.jpg' | relative_url }})

Description of Principal Stress

## Interpretation of Stress

**Steels** :

In the case of steel, if the effective stress exceeds the yield stress at the operating temperature, the tool will yield. Moderate to low yielding can be very detrimental to the forging process since a different part will get produced than the intended one and the tools does not eventually fail altogether. High positive principal stress values may lead to fatigue failures, even if the stress is below the yield stress.

Harder tool steels generally have higher yield strength (See Fig. 9), but a lower tolerance for tensile fatigue loading. Lower hardness tool steels have lower yield strength, but a better tolerance for tensile fatigue.

**Carbide:**

Carbide can tolerate an extremely high effective stress, however, it is extremely intolerant of tensile (positive) principal stresses, and will fail easily in fatigue. Higher cobalt content increases fatigue resistance, but decreases wear resistance. Lower cobalt content has better wear characteristics, but is less tolerant of large positive principal stresses.

**Simplistic rules:**

Some very simple rules can often be useful in interpreting die stress results. Here is a short list of some things to keep in mind.

  1. Effective stress in steel should be below the yield stress. This is rather obvious, but it gives a good starting point from which to evaluate a situation where dies are failing or evaluating a prospective assembly.

  2. Max principal stress in carbide should be negative, or small positive values (10-20ksi or 50-100MPa). Since carbide is made of pressed together ceramic material, the grains tend to pull apart rather easily but the amount of stress these materials can handle in compression is rather astounding. So it is good to design an assembly where the carbide never sees a tensile stress during any time of a forging.

  3. Max principal stress in steels can be larger in steels, but very large values (100ksi or 700MPa) may lead to fatigue failures. One of the first laws of fatigue is that the closer to the yield stress a cyclic operation runs, the lower the number of cycles a process can exist before eventual failure. Even through a process is below the yield stress by a nominal margin, often lifetime improvement may be seen by further reduction in the maximum effective stress seen by the tools.

  4. If a high stress exists, stress components can be used to help identify the root cause of the stress. In an effort to correlate a failure on a shop floor to a die-stress simulation, the components where high stresses are seen can often be correlated to how the failure of the die occurred.

![]({{ '/assets/images/operation_templates/30_die_stress/2d_die_stress_analysis_theory/image0009.jpg' | relative_url }})

Comparison of idealized elastic stress-strain curves with ductile and brittle material curves

**Related Topics:**

[Object Boundary Condition](/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/)

[2D Die Stress Study with Multiple Steps](/docs/sk/labs/die_stess_study_labs/2d_die_stress_study_with_multiple_steps/)

[2D Die Stress Study with Single steps](/docs/sk/labs/die_stess_study_labs/2d_die_stress_study_with_single_step/)

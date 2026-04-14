---
lang: en
title: "Appendix XII: Modelling of Spring Loaded Die Using Force Controlled Objects"
---

# Appendix XII: Modelling of Spring Loaded Die using Force Controlled objects

**Overview:**

A simulation of a spring-loaded sliding die can be broken down into three typical phases of sliding die movement

  1. Force on the sliding die is below the preload - die is stationary resting on a stop or another die.

  2. Force on die exceeds preload - die begins moving under spring load control.

  3. Die hits a stop - forming process completes with die stationary.

**Note** :

Depending on the type of sliding die being modeled, this behavior may or may not be fully realized in any particular simulation. For example, some pneumatic springs don't require the modeling of a preload. In such a case, the first phase can be omitted.

**Methods for modeling sliding dies in DEFORM ®:**

**Option 1** : Make the sliding die as primary die, use load and/or stroke stopping controls to stop the simulation when die starts (Preload exceeded) or stops motion (spring goes solid), then change movement controls and restart.

**Option 2** : Use artificial elastic spacer (s) to allow the spring-loaded die to react against deformable body, and allow simulation to run through. (More initial setup time but less intervention during run time)

**Option 1 described:**

**Phase 1:** (See Fig. AXII.1.)

  1. Set object 2 velocity control.

  2. Object 4 primary die, no movement control.

  3. Stop on load = preload on object 4.

  4. Step control by time (primary die is not moving).

**Phase 2:**(See Fig. AXII.2.)

  1. Object 4 load control. Direction should be direction load is applied, not direction of movement.

  2. If movement of object 4 is limited, stop on stroke can be set.

![]({{ '/assets/images/appendices/appendix_xii_modelling_of_spring_loaded/image0001.jpg' | relative_url }})

Sketch of spring-loaded die simulation with spring-loaded die set with a stopping criteria based on load

![]({{ '/assets/images/appendices/appendix_xii_modelling_of_spring_loaded/image0002.jpg' | relative_url }})

Sketch of spring-loaded die simulation with spring-loaded die set with movement type based on load

**Option 2 described** : Using an artificial elastic “spacer” (See Fig. AXII.3. and Fig. AXII.4.)

  1. Create a thin elastic object (5 in this case) with about 10-20 elements

  2. Make object 5 slave to both objects 3 and 4.

  3. Set movement on object 4 to load control, with the load as the preload.

  4. Run the simulation. When load exceeds preload, die will automatically move up.

![]({{ '/assets/images/appendices/appendix_xii_modelling_of_spring_loaded/image0003.jpg' | relative_url }})

Sketch of spring-loaded die simulation with spring-loaded die set with movement type based on load and an additional elastic body (5) that provides a reaction force for the spring-loaded die (4).

![]({{ '/assets/images/appendices/appendix_xii_modelling_of_spring_loaded/image0004.jpg' | relative_url }})

Sketch of spring-loaded die simulation with spring-loaded die set with movement type based on load and an additional elastic body. At this stage, the material has filled beneath the sliding die and is pushing the sliding die upward.

**Related Topics:**

[Movement Controls](/docs/en/pre_processor/15_movement_controls_definition/15_movement_controls_settings/)

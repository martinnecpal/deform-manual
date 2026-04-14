---
lang: sk
title: "1.3. Capabilities"
---

# 1.3. Capabilities

1.3.1. Deformation

1.3.2. Heat Treatment

## Deformation

  * Coupled modelling of deformation and heat transfer for simulation of cold, warm, or hot forging processes (all products).

  * Extensive [material database](/docs/sk/pre_processor/10_material_data/10_material_data/) for many common alloys including steels, aluminium’s, titanium’s, and super-alloys. (all products).

  * User defined material data input for any material not included in the [material database](/docs/sk/pre_processor/10_material_data/10_material_data/). (all products).

  * Information on material flow, die fill, forging load, die stress, grain flow, defect formation and ductile fracture (all products).

  * Rigid, elastic, and thermo-viscoplastic material models, which are ideally suited for large deformation modelling (all products).

  * Elastic-plastic material model for residual stress and spring back problems. (2D, 3D).

  * Porous material model for modelling forming of powder metallurgy products (2D, 3D).

  * Integrated forming equipment models for hydraulic presses, hammers, screw presses, and mechanical presses (all products).

  * [User defined subroutines](/docs/sk/user_routines/56_user_routines_in_deform/56_1_introduction_to_user_routines/) for material modelling, press modelling, fracture criteria and other functions (2D, 3D).

  * Built in Flownet is an option where user can define flownet value before simulating a database file to visualize any potential irregularities in the grain structure or to view potential surface defects.

  * FLOWNET (2D, 3D) and point tracking (all products) for important material flow information.

  * Region of Interest (ROI), an arbitrary shape (2d or 3d) which defines an area from which to gather information from an object. These regions can be used to get min/max state variable values from a specific part on an object (2D, 3D).

  * Coupons Data extraction to evaluate the microstructure and Mechanical property of a particular cut part (2D, 3D).

  * Post-Processor has been extended to produce simulation output as .pdf (3D) and .ppt reports. This enables more flexibility to the user for [report generation](/docs/sk/post_processor/27_introduction_to_report_generation/27_introduction_to_report_generation/) (2D, 3D).

  * Contour plots of temperature, strain, stress, damage, and other key variables simplify post processing (all products). 

  * Self contact boundary condition with robust remeshing allows a simulation to continue to completion even after a lap or fold has formed (2D, 3D).

  * Multiple deforming body capability allows for analysis of multiple deforming work pieces or coupled die stress analysis. (2D, 3D).

  * Fracture initiation and crack propagation models based on well known damage factors allow modelling of shearing, blanking, piercing, and machining (2D, 3D).

## Heat Treatment

Simulate normalizing, annealing, quenching, tempering, and carburizing.

**Normalizing (not available yet)**

Heating a ferrous alloy to a suitable temperature above the transformation range and cooling in air to a temperature substantially below the transformation range.

**Annealing**

A generic term denoting a treatment, consisting of heating to and holding at a suitable temperature followed by cooling at a suitable rate, used primarily to soften metallic materials. In ferrous alloys, annealing usually is done above the upper critical temperature, but the time-temperature cycles vary both widely in both maximum temperature attained and in cooling rate employed.

**Tempering**

Tempering of martensite is a diffusion process, and can be modeled using time temperature transformation models with Martensite as the parent phase, and tempered martensite (or other products as required) as the child phase(s).

**Stress relieving**

Heating to a suitable temperature, holding long enough to reduce residual stresses, and then cooling slowly enough to minimize the development of new residual stresses.

**Quenching**

A rapid cooling whose purpose is for the control of microstructure and phase products.

  * Predict hardness, volume fraction metallic structure, distortion, and carbon content.

  * Specialized material models for creep, phase transformation, hardness and diffusion.

  * Jominy data can be input to predict hardness distribution of the final product. 

  * Modelling of multiple material phases, each with its own elastic, plastic, thermal, and hardness properties. Resultant mixture material properties depend upon the percentage of each phase present at any step in the heat treatment simulation.

DEFORM models a complex interaction between deformation, temperature and in the case of heat treatment, transformation and diffusion. There is coupling between the entire phenomenon, as illustrated in the Fig. 1.3.1. below. When appropriate modules are licensed and activated, these coupling effects include heating due to deformation work, thermal softening, temperature controlled transformation, latent heat of transformation, transformation plasticity, transformation strains, stress effects on transformation, and carbon content effects on all material properties.

[DEFORM HT](/docs/sk/operation_templates/37_heat_treatment/37_introduction_to_heat_treatment/) allows setup heat treatment operations in cycles at a time and simulating them sequentially.

![]({{ '/assets/images/about_deform/1_3_capabilities/1_3_image001.jpg' | relative_url }})

Relationship between various DEFORM modules

**Related Topics:**

[PRE-PROCESSOR](/docs/sk/pre_processor/7_introduction_to_pre-processor/)

[POST-PROCESSOR](/docs/sk/post_processor/24_introduction_to_post_processor/24_introduction_to_post_processor/)

[INV. HEAT TRANSFER](/docs/sk/inverse_heat/51_introduction_to_inverse_heat/)

[HEAT TREATMENT](/docs/sk/operation_templates/37_heat_treatment/37_introduction_to_heat_treatment/)

[Integrated Manufacturing Process](/docs/sk/integrated_manufacturing_process_setup/5_introduction_to_integrated_manufacturinghtm/) (MO)

[HT FURNACE](/docs/sk/operation_templates/38_furnace_heating/38_introduction_to_3d_ht_furnace/)

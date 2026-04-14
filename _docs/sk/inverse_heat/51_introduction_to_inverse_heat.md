---
lang: sk
title: "51 Introduction to Inverse Heat"
---

# 51\. Introduction to Inverse Heat 

51.1. Methodology

51.2. Input to the model

51.3. Output from the model

51.4. Overview of Wizard

The Inverse Heat wizard is used to determine the heat transfer coefficients as a function of surface temperature at different locations of the given part from the known temperature history. Heat transfer coefficients are the necessary thermal boundary conditions that are required to accurately model a quenching or heating process.

## Methodology

A generic heat treat geometry which is representative of a family of parts would be selected. This part would be instrumented with several thermocouples near the surface of the part as well as the inside of the part. The instrumented part would then be subjected to the quenching process. The time versus temperature data for all the thermocouple locations would be collected. Based on an initial guess of heat transfer coefficients, DEFORM would run an initial thermal simulation of the quench process. DEFORM optimization routines would then compare the simulated time-temperature modelling results with the experimental data and would modify the heat transfer coefficients until a good agreement between the simulation and the experimental data is reached.

## Input to the model

The following are the key inputs to the model

  1. Geometry of the part

  2. Thermocouple locations

  3. Time Vs temperature data for the thermocouple locations

  4. Definition of heat transfer coefficients zones (how many HTC functions around the part?)

  5. Initial guess for the heat transfer coefficients

  6. Thermal properties of the material

## Output from the model

The following are the key outputs from the model

  1. Heat transfer coefficients as a function of surface temperature for each zone

  2. Comparison of experimental and simulated temperature data

## Overview of Wizard

An overview of the inverse heat transfer wizard is as follows

  1. The wizard takes the user through a self-contained pre-processor, FEM/optimization engine and post-processor

  2. The wizard would allow only one object for rigid thermal analysis.

  3. The wizard allows an initial problem set up as well as a restart of an existing analysis.

  4. Model outputs can be viewed in the wizard itself.

  
Inverse HT module is available for both 2D and 3D geometries, please refer

[51.1. Inverse HT 2D manual](/docs/sk/inverse_heat/51_1_2d_inverse_heat_manual/)

[51.2. Inverse HT 3D manual](/docs/sk/inverse_heat/51_2_3d_inverse_heat_manual/)

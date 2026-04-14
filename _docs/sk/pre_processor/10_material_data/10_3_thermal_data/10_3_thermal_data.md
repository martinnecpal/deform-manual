---
lang: sk
title: "10.3. Thermal Data"
---

# 10.3. Thermal Data

10.3.1. Thermal conductivity   
10.3.2. Heat capacity   
10.3.3. Emissivity  
10.3.4. Mass Density

Thermal data is required for any object in the heat transfer mode as shown in Fig. 10.3.1.

![]({{ '/assets/images/pre-processor/10_material_data/10_3_thermal_data/10_3_image001.jpg' | relative_url }})

Thermal material data window 

## Thermal conductivity (THRCND)

Conduction is the process by which heat flows from a region of higher temperature to a region of lower temperature within a medium. The thermal conductivity ([THRCND](/docs/sk/keyword_documentation/t/thrcnd/)) in this case is the ability of the material in question to conduct heat within an object.  
The value can be a constant or a function of temperature, a function of atom content, or a function of temperature and atom content.

## Heat capacity (HEATCP)

Heat capacity is generally defined as the amount of heat an object must absorb to produce a unit change in its temperature.It is typically documented, more specifically, as heat capacity divided by an amount of material. The amount of material is usually a mass or volume.

Most reference values for heat capacity list the specific heat capacity, ![]({{ '/assets/equations/pre_processor/10_material_data/10_3_thermal_data/rcp.jpg' | relative_url }}), which is the heat capacity per unit mass. It defines the heat required to raisea unit mass of a substance by a unit temperature interval under constant pressure. In other words, it is the thermal energy per unit mass required to achieve a one degree increase in temperature.

The default heat capacity ([HEATCP](/docs/sk/keyword_documentation/h/heatcp/)) term used in DEFORM is the volumetric heat capacity, ρcp, which is the heat capacity per unit volume. It defines the heat required to raise a unit volume of a substance by a unit temperature interval under constant pressure. In other words, it is the thermal energy per unit volume required to achieve a one degree increase in temperature.

Volumetric heat capacity is obtained by multiplying specific heat capacity (heat capacity per unit mass) by density (mass per unit volume).

![]({{ '/assets/equations/pre_processor/10_material_data/10_3_thermal_data/eqn_10_3_1.jpg' | relative_url }}) |   
---|---  
  
The other heat capacity ([HEATCP](/docs/sk/keyword_documentation/h/heatcp/)) term available in DEFORM is the mass specific heat capacity. It is the specific heat capacity, but denoted as “mass specific heat” to highlight its relationship to the mass density input available in the thermal properties menu. Mass density must be defined if the mass specific heat capacity has been defined. Values for mass density and mass specific heat capacity must utilize consistent mass units. See Section [1.9. Units](/docs/sk/about_deform/1_introduction_to_deform/1_9_units/) for more details.

DEFORM utilizes the volumetric heat capacity for FEM calculations. If mass specific heat capacity has been defined, then DEFORM will calculate the volumetric heat capacity from the mass density and mass specific heat capacity during FEM calculations.

The volumetric or mass specific heat capacity may be input to DEFORM as a constant, a function of temperature, a function of atom content, or a function of both temperature and atom content.

## Emissivity (EMSVTY)

The emissive power, E, of a body is the total amount of radiation emitted by a body per unit area and time. The emissivity ([EMSVTY](/docs/sk/keyword_documentation/e/emsvty/)) of a body is the ratio of E/Eb where Eb is the emissive power of a perfect blackbody. For a more complete description of the properties of emissivity, consult any source dealing with heat transfer. The value can be a constant or a function of temperature.

## Mass Density (DENSTY)

The mass density ([DENSTY](/docs/sk/keyword_documentation/d/densty/)) of a material is its mass per unit volume. Mass density may be defined as a constant or a function of temperature. Mass density must be defined in models that involve gravity, body force, centrifugal force or the explicit solver.

Density values for various materials are readily available in online and print literature. It should be noted that the type of density listed in these references generally differs based on the specified unit system, as described below.

  * Density values published in the SI unit system typically represent the mass density of the material, in units of kg/m3 or equivalent.

  * Density values published in the English unit system typically represent the weight density of the material, in units of lbf/in3 or equivalent.

When working in English units, weight density must be converted to mass density before it is used in DEFORM. To obtain mass density, first recall the following fundamental physics relationship:

force = mass * acceleration

The equation can be altered to consider the relationship between weight (force), mass and gravity (acceleration):

weight = mass * gravity

The following relationship is obtained by assuming standard gravity, dividing each side of the equation by volume (to obtain densities) and rearranging the equation:

mass density = weight density / standard gravity

Standard gravity equals 32.17 ft/s2 (386.1 in/s2) in the English unit system.

Consider the following example, where the mass density of steel must be defined in either English or SI units. The published density values for a general steel are:

English units: 0.282 lbf/in3 (weight density)

SI units: 7800 kg/m3 (mass density)

If working in English units, weight density is first converted to mass density as shown below:

mass density = (0.282 lbf/in3) / (386.1 in/s2) = 0.730x10-3 lbf*s2/in4

The mass density must then be adjusted to the proper unit format by converting the lbf term to klbf:

0.730x10-3 lbf*s2/in4 * (1 klbf / 1000 lbf) = 0.730x10-6 klbf*s2/in4

The mass density value that should be defined in the English-unit DEFORM model is thus 0.730x10-6 klbf*s2/in4.

If working in SI units, then mass density is already known. Although, it must be converted to the proper unit format before it is used as input to DEFORM. This requires the following conversion:

1000 kg = 1 tonne

7800 kg/m3 * (1 tonne / 1000 kg) * (1 m / 1000 mm)3 = 7.80x10-9 tonne/mm3

The mass density value that should be defined in the SI-unit DEFORM model is thus 7.80x10-9 tonne/mm3.

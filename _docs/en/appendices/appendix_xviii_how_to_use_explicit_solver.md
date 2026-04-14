---
lang: en
title: "Appendix XVIII How to use Explicit Solver"
---

# Appendix XVIII: How to use Explicit Solver

## Simulation with Explicit Solver

With 4 additional setups user can use the Explicit solver those are,

**Step 1:** Object type should be “Elasto-plastic”.

From object general settings window select object type to Elasto-Plastic as shown in Fig. XVIII.1.

![]({{ '/assets/images/appendices/appendix_xviii_how_to_use_explicit_solver/image0001.jpg' | relative_url }})

Object General settings Window

**Step 2:** Mass density should be defined.

Make sure that Mass Density value defined from material thermal properties can be accessed from object material window by using the ![]({{ '/assets/icons/pre_icons/mo_material_edit_button.jpg' | relative_url }}) button. Material![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})thermal![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})mass density window is as shown in Fig. XVIII.2.

Note that the English unit system density values published in literature typically represent weight density, not mass density. Please review Section [10.3.4. Mass density](../pre_processor/10_material_data/10_3_thermal_data/10_3_thermal_data.htm#Mass_Density) to understand the requirements for defining mass density in DEFORM.

![]({{ '/assets/images/appendices/appendix_xviii_how_to_use_explicit_solver/image0002.jpg' | relative_url }})

Object Material Thermal properties editing window

**Step3:** Set “the number of steps” and “step increment to save” as big numbers.

From Simulation Controls ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Simulation Steps tab define Number of Steps and Step increment to save as shown in Fig. XVIII.3.

![]({{ '/assets/images/appendices/appendix_xviii_how_to_use_explicit_solver/image0003.jpg' | relative_url }})

Simulation control window Steps tab in export mode

**Step4:** Set mass scaling factor and damping. Newton-Raphson iteration method should be selected.

From Simulation Controls ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Iteration tab set Mass scaling factor and Damping coefficient for explicit solver and select Newton-Rapson Iteration method as shown in Fig. XVIII.4.

![]({{ '/assets/images/appendices/appendix_xviii_how_to_use_explicit_solver/image0004.jpg' | relative_url }})

Simulation control window Iteration tab in expert mode

**Selecting Mass Scaling Factor Metal Forming Processes:**

  * To select the mass scaling factor,

  * Run multiple whole (or partial) simulations with different speed of process.

  * Compare the results (deformation, stress and strain) with implicit or available measured data if possible. Filter out the obvious case of excessive deformation due to dynamic effect.

  * Mass scaling factors from previous examples (See Fig. XVIII.5.)

  * Rotary spinning : 300 ~ 1200, Rotary swaging : 200 ~ 500

  * Sheet forming : 500 ~ 5000

  * Backward extrusion : 10 ~ 30

![]({{ '/assets/images/appendices/appendix_xviii_how_to_use_explicit_solver/image0005.jpg' | relative_url }})

Mass Scaling factor for few forming processes from previous examples

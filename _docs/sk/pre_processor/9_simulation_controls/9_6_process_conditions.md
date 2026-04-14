---
lang: sk
title: "9.6. Process Conditions"
---

# 9.6. Process Conditions ![]({{ '/assets/icons/pre_icons/mo_process_conditions.jpg' | relative_url }})

9.6.1. Heat Transfer

  * Environment temperature (ENVTMP)

  * Convection coefficient (CNVCOF)

  * View Factor Calculation

  * Turn on diffusion-bonding calculation

9.6.2. Diffusion

  * Environment atom content (ENVATM)

  * Reaction rate coefficient (ACVCOF)

  * Atom (ATOMID)

9.6.3. Induction

  * Magnetic permeability (ENVMPR)

  * Magnetic permittivity (ENVMPT)

  * Source Energy Ratio (EHRATE)

  * Activate overlapped air mesh check box

  * Define Induction Heating Windows

  * Use reduce 3D BEM matrix

9.6.4. Constants 

  * Interface penalty constant (PENINF)

  * Mechanical to heat conversion (UNTE2H)

  * Time integration factor (TINTGF)

  * Boltzmann constant (BLZMAN)

  * Friction heat reduction factor (UNTE2H)

  * Thermal conductivity smoothing factor (TCONSF)

9.6.5. Additive Manufacturing

9.6.6. Heat Source

The processing conditions menu contains information about the process environment and constants related to general solution behavior.

## Heat Transfer [2D, 3D]

Heat transfer process conditions definitions have effect on process only by checking Heat transfer check box in Simulation controls Main tab and defining the respective Environment BCC. (See Fig. 9.6.1.) 

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_6_process_conditions/9_6_image001.jpg' | relative_url }})

(a)

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_6_process_conditions/9_6_image002.jpg' | relative_url }})

(b)

Heat transfer processing conditions; (a) For 2D (b) For 3D

  * **Environment temperature (ENVTMP)**

Environment temperature ([ENVTMP](/docs/sk/keyword_documentation/e/envtmp/)) is used in radiation and convection heat transfer calculations and represents the temperature of the area in which the modelled process is taking place. The environment temperature may be specified as a constant or as a function of time. Heat transfer to this temperature is considered to occur from any nodes not in contact with another object. (Unless heat exchange windows are used).

  * **Convection coefficient (CNVCOF)**

The convection coefficient ([CNVCOF](/docs/sk/keyword_documentation/c/cnvcof/)) is required for convection heat transfer calculations. The convection coefficient may be specified as a constant or as a function of temperature.

  * **View Factor Calculation**

Radiation will be calculated in the simulation when we check the "View factor calculation" check box option and also we can select the object/s for view factor calculation (object selection option available only for 3D as shown in Fig. 9.6.2.).

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_6_process_conditions/9_6_image003.jpg' | relative_url }})

Select object window for view factor calculation (in 3D)

### Turn on diffusion-bonding calculation

DIffusion bonding will we be calculated in the simulation when we check the "Turn on diffusion-bonding calculation "

## Diffusion [2D, 3D]

Diffusion process conditions definitions have effect on process only by checking Diffusion check box in Simulation controls Main tab and defining the respective Environment BCC. (See Fig. 9.6.3.)

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_6_process_conditions/9_6_image004.jpg' | relative_url }})

Diffusion processing conditions

  * **Environment atom content (ENVATM)**

The percentage atom content ([ENVATM](/docs/sk/keyword_documentation/e/envatm/)) of the dominant atom (usually carbon) in the environment for diffusion calculations.

  * **Reaction rate coefficient (ACVCOF)**

The surface reaction rate ([ACVCOF](/docs/sk/keyword_documentation/a/acvcof/)) with the atmospheric atom content for diffusion calculations.  
  
From DEFORM-v12 onwards user can define multiple types of atoms for Diffusion by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) button as show in Fig. 9.6.4.

  
Note: Current limitation is maximum 2 different types of atoms to be used.

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_6_process_conditions/9_6_image004.jpg' | relative_url }})

New Diffusion Process condition 

  * **Atom ([ATOMID](/docs/sk/keyword_documentation/a/atomid/))**

In the Atom field user can modify the name of each type of atom and can activate/deactivate the diffusion by turning on/turning off the check box.  
When we add 2 different types of Atom in Diffusion table, we can observe that the new field f(temperature, atom1, atom2) is added under Reaction rate coefficient as shown in Fig. 9.6.5.

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_6_process_conditions/9_6_image005.jpg' | relative_url }})

Reaction rate coefficient options

Also in Material properties, under Thermal conductivity and Heat Capacity type list we can observe that a new field f(Temperature, Aom1, Atom2) will be added.  
Even in Material properties Diffusion page we can observe multiple atoms defined in Simulation controls Diffusion page are shown under Atom list so that properties for each atom can be defined independently as shown in Fig. 9.6.6.

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_6_process_conditions/9_6_image006.jpg' | relative_url }})

Material Properties Diffusion page

Even in BCC page (see Fig. 9.6.7.), for all Diffusion BCC options we can observe both types of atoms defined in Simulation controls Diffusion page are available and we can define BCC for each Atom type separately.

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_6_process_conditions/9_6_image007.jpg' | relative_url }})

BCC page Multiple Atom option in Diffusion with Environment page

## Induction [2D, 3D]

The Induction tab (See Fig. 9.6.8.) is activated by checking the Heating check box in Simulation controls > Main tab.

(a)

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_6_process_conditions/9_6_image009.jpg' | relative_url }})

(b)

Induction processing constants ; (a) For 2D (b) For 3D.

  * **Magnetic permeability (ENVMPR)**

Permeability ([ENVMPR](/docs/sk/keyword_documentation/e/envmpr/)) is the property of a material that is equal to the magnetic flux density B established within the material by a magnetizing field divided by the magnetic field strength H of the magnetizing field.

The permeability of a vacuum (ENVMPR) is defined in the Simulation Controls > Process Conditions menu. The typical value is provided below for reference.

1.26 x 10-9 H/mm (SI)  
3.20 x 10-8 H/in (English)

  * **Magnetic permittivity (ENVMPT)**

Permittivity ([ENVMPT](/docs/sk/keyword_documentation/e/envmpt/)) is a quantity that describes how a magnetic field affects and is affected by a dielectric medium. It is determined by the ability of a material to polarize in response to the field and thereby reduce the total electric field inside the material. Thus, permittivity relates to a material's ability to transmit (or "permit") a magnetic field.

The permittivity of a vacuum (ENVMPT) is defined in the Simulation Controls > Process Conditions menu. The typical value is provided below for reference.

8.85 x 10-15 F/mm (SI)   
2.25 x 10-13 F/in (English)

  * **Source Energy Ratio (EHRATE)**

"Source Energy Ratio" ([EHRATE](/docs/sk/keyword_documentation/e/ehrate/)) is a conversion ratio from electric energy to heat.  
If "0" or "1000" is specified, it means 100% electric energy is converted to heat. If "500" is specified, it means 50% conversion.

  * **Activate overlapped air mesh check box [2D]**

  * **Define Induction Heating Windows [3D]**

  * **Use reduce 3D BEM matrix [3D]**

## Constants [2D, 3D]

For process conditions constants settings see Fig. 9.6.9.

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_6_process_conditions/9_6_image010.jpg' | relative_url }})

(a)

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_6_process_conditions/9_6_image011.jpg' | relative_url }})

(b)

Advanced process constants ; (a) For 2D (b) For 3D.

  * **Interface penalty constant (PENINF)**

A large positive number used to penalize the penetration velocity ([PENINF](/docs/sk/keyword_documentation/p/peninf/)) of a node through a master surface. The default value is adequate for most simulations. It should be at least two to three orders higher than the volume penalty constant ([PENVOL](/docs/sk/keyword_documentation/p/penvol/)).  
For objects of very small size (e.g. fasteners), it is recommended to reduce this number an order of magnitude or two to improve convergence. This will only aid convergence if the sparse solver is used. This constant can be edited only in Advanced user mode.

  * **Mechanical to heat conversion (UNTE2H)**

A constant coefficient to relate units of heat energy (E.g. BTU) to mechanical energy (E.g. klb-in). Appropriate constant values are automatically set for English and SI Units. This constant can be edited only in Advanced user mode. ([UNTE2H](/docs/sk/keyword_documentation/u/unte2h/))

  * **Time integration factor (TINTGF)**

The time integration factor ([TINTGF](/docs/sk/keyword_documentation/t/tintgf/)) is the forward integration coefficient for temperature integration over time. Its value should be between 0.0 and 1.0. The value of 0.75 is adequate for most simulations. This constant can be edited only in Advanced user mode.

  * **Boltzmann constant (BLZMAN)**

The Boltzmann constant ([BLZMN](/docs/sk/keyword_documentation/b/blzman/)) is required for radiation heat transfer calculations. Default values for English and SI are set automatically. In radiation heat calculations the nodal temperature will be automatically converted to absolute temperature (Rankin, Kelvin) based on the selected English or SI units. This constant can be edited only in Advanced user mode.

  * **Friction heat reduction factor (UNTE2H)**

  * **Thermal conductivity smoothing factor (TCONSF) [3D]**

## Additive Manufacturing [3D]

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_6_process_conditions/9_6_image012.jpg' | relative_url }})

Additive manufacturing process conditions

## Heat Source [3D]

![]({{ '/assets/images/pre-processor/9_simulation_controls/9_6_process_conditions/9_6_image013.jpg' | relative_url }})

Heat source process conditions

Related Topics:

[9.1. Simulation type Settings](/docs/sk/pre_processor/9_simulation_controls/9_1_simulation_type_settings/)   
[9.2. Defining Step](/docs/sk/pre_processor/9_simulation_controls/9_2_defining_step/)   
[9.3. Stopping Controls](/docs/sk/pre_processor/9_simulation_controls/9_3_stopping_controls/)   
[9.4. Remesh Criteria](/docs/sk/pre_processor/9_simulation_controls/9_4_remesh_criteria/)   
[9.5. Solver Settings](/docs/sk/pre_processor/9_simulation_controls/9_5_solver_settings/)   
[9.7. Advanced Options](/docs/sk/pre_processor/9_simulation_controls/9_7_advanced_options/)   
[9.8. Control Files](/docs/sk/pre_processor/9_simulation_controls/9_8_control_files/)   
[9.9. Thermomechanical variables](/docs/sk/pre_processor/9_simulation_controls/9_9_thermomechanical_variables/)

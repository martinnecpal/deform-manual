---
lang: en
title: "1.9. Units"
---

# 1.9. Units

DEFORM data may be supplied in any unit system, as long as all variables are consistent (i.e. length, force, time and temperature measurements are in the same units, and all derived units - such as velocity - are derived from the same base units). This task can be simplified by using either the British or SI system for the default unit system (See below table 1.9.1.).

**Variables** | **SI** | **Eng** | **Conversion Factor  
(SI ****→****Eng)**  
---|---|---|---  
**Area** | **mm^2** | **in^2** | 0.001550003  
**Body force/ weight density (![]({{ '/assets/icons/pre_icons/rho_symbol.jpg' | relative_url }}) *g)** | **N/mm^3** | **klbf/in^3** | 3.684  
**Bulk modulus** | **MPa** | **ksi** | 0.145037681  
**Centrifugal force (![]({{ '/assets/icons/pre_icons/rho_symbol.jpg' | relative_url }}) *Ω^2 )** | **N/mm^4** | **klbf/in^4** | 93.5725  
**Coating thickness** | **microns** | **microns** | ****  
**Convection coefficient** | **N/sec/mm/°C** | **Btu/sec/in^2/°F** | 0.000339789  
**Current density** | **A/mm^2** | **A/in^2** | 645.16  
**Diffusion coefficient** | **mm^2/second** | **in^2/second** | 0.001550003  
**Distance / length** | **mm** | **in** | 0.039370079  
**Electric field intensity** | **V/mm** | **V/in** | 25.4  
**Electric power 1** | **W** | **W** |   
**Electrical permittivity** | **farad/mm** | **farad/in** |   
**Electrical resistivity (material)** | **ohm·mm** | **ohm**·** in** | 0.039370079  
**Electrical interface resistivity** | **ohm·mm^2** | **ohm·in^2** | 0.001550003   
**Magnetic field intensity** | **A/mm** | **A/in** |   
**Magnetic permeability** | **H/mm** | **H/in** |   
**Relative magnetic permeability** | **magnetic permeability / magnetic permeability of a vacuum** |   
**Relative electrical permittivity** | **electrical permittivity / electrical permittivity of a vacuum** |   
**Force** | **N** | **klbf** | 0.000224809  
**Frequency** | **Hz** | **Hz** |   
**Grain size** | **micron** | **micron** |   
**Heat capacity** | **N/mm^2/°C** | **Btu/in^3/°F** | 0.008628872  
**Heat energy** | **N·mm** | **Btu** | 9.47867E-07  
**Heat flux rate** | **N/mm/sec** | **Btu/in^2/sec** | 1635.3  
**Interface heat transfer coefficient** | **N/sec/mm/°C** | **Btu/sec/in^2/°F** | 0.000339789  
**Mass** | **N**·** s^2/mm** | **klbf·s^2/in** | 0.005710148562313  
**Mass density (![]({{ '/assets/icons/pre_icons/rho_symbol.jpg' | relative_url }}))** | **tonne/mm^3** | **klbf·s^2/in^4** | 93.5725  
**Mass specific heat** | **N**·** mm/tonne·°C ** | **Btu**·** in/klbf**·** s^2**·°** F ** | 9.2216E-5  
**Mechanical energy** | **N·mm** | **klbf·in** | 8.84956E-06  
**Pressure; stress; Young's modulus** | **MPa** | **Ksi** | 0.145037681  
**Relative density** | **material density / fully-dense material density** | 1  
**Strain** | **mm/mm** | **in/in** | 1  
**Strain rate** | **(mm/mm)/sec** | **(in/in)/sec** | 1  
**Temperature** | **°C** | **°F** | (°C * 1.8) + 32  
**Thermal conductivity** | **N/sec/°C** | **Btu/sec/in/°F** | 1.33754E-05  
**Thermal expansion coefficient** | **1/°C** | **1/**°** F** | 0.555556  
**Time** | **sec** | **sec** | 1  
**Torque** | **N·mm** | **klb·in** | 8.85075E-06  
**Universal gas constant** | **J/(mol·K)** | **J/(mol·°F)** | 0.555556  
**Velocity** | **mm/sec** | **in/sec** | 0.039370079  
**Voltage** | **V** | **V** | ****  
**Volume** | **mm^3** | **in^3** | 6.1024E-05  
  
DEFORM unit system

It is important to select the unit system at the beginning of the simulation. Once numerical values have been entered in the pre-processor, the numerical value will remain unchanged even if the unit system designation is changed.

The Post-Processor has been equipped with a feature for unit conversion for database viewing (See [Fig. 26.5.6.](../../post_processor/26_post_processing_tools_and_controls/26_5_post_processing_options.htm#Fig_26_4_6_Unit_Conversion) ). The user has four options for unit conversion. If the conversion factor selected is Default, then the units are picked up automatically depending on whether the database is English or SI. Since there is no conversion necessary, all the conversion factors are set to 1.0 in this column. For the cases of converting English to SI or converting SI to English, the conversion factors and units are picked up from the dialog and the values are converted and displayed in the post-processor. The fourth option gives the user the option of viewing the data from the database in units that are not English or SI. The user is free to enter the conversion factors and the units corresponding to the conversion factors.

There is no user type unit conversion for temperature, since the temperature conversion is not a simple multiplication.

Unit consistency must be maintained when dealing with density. The table below outlines the various units that coincide with different density definitions.

| **UNIT1** | **UNIT2** | **UNIT3** | **UNIT4**  
---|---|---|---|---  
**Length** | m | mm | m | in  
**Force** | N | N | kN | Klbf  
**Mass** | kg | kg | tonne | (klbf)(s^2)/ in  
**Stress** | Pa | MPa | kPa | (ksi)  
**Density** | kg/m^3 | tonne/mm^3 | tonne/m^3 | (klbf)(s^2)/ in^4  
**Energy** | J | mJ | kJ | (in)(klbf)  
  
Important constants to setup Induction heating simulation:

**Magnetic Permeability of air / vacuum**

4 ![]({{ '/assets/images/about_deform/1_9_units/pi_symbol.jpg' | relative_url }})E-7 (1.26E-6 ) Henry/m

1.26E-9 Henry/mm

3.19E-8 Henry/inch

**Permittivity of air / vacuum**

1E-9 /(36 ![]({{ '/assets/images/about_deform/1_9_units/pi_symbol.jpg' | relative_url }})) (8.85E-12 ) Farad/m

8.85E-15 Farad/mm

2.25E-13 Farad/inch

Important constants unit in Grain boundary mobility and microstructure:

**Coefficient of grain boundary mobility(M0)** micron^2/Joule 

**Activation Energy (Q)** Joule   
**Energy** Joule

**Interface energy** Joule 

****1** Electric power** is given in Watts (N·m/s) for convenience relative to industry standard units. It deviates from the standard DEFORM unit system (N·mm/sec).

**Related Topics:**

[Unit System Selection Pre-Processor](../../pre_processor/9_simulation_controls/9_1_simulation_type_settings.htm#9.1.3._Units)

[Material Units Converter Pre-Processor](../../pre_processor/10_material_data/10_material_data.htm#Fig._10.7._Material_Unit_Convertor_window)

[Units Converter Post-Processor](../../post_processor/26_post_processing_tools_and_controls/26_5_post_processing_options.htm#26_5_6_Unit_Conversion)

[10.3.4. Mass Density](../../pre_processor/10_material_data/10_3_thermal_data/10_3_thermal_data.htm#Mass_Density)

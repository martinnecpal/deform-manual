---
lang: sk
title: "10.12. Miscellaneous Data"
---

# 10.12. Miscellaneous Data

10.12.1. Fracture Data (FRCMOD)  
10.12.2. Mechanical Work to Heat (FRAE2H)  
10.12.3. Force per unit volume or Body Force (FPERV)  
10.12.4. Centrifugal force  
10.12.5. Diffusion Bonding   
10.12.6. Size Model (SIZESH and SIZEMD)  
10.12.7. Sintering Driving Force model

  * Simple Elastic one-step

  * Skorohod

  * Cocks

  * Shinagawa

  * Ashby

  * [Raj/Ashby](10_12_miscellaneous_data.htm#Raj/Ashby)

10.12.8. Material data requirements

  
Fig. 10.12.1. shows the advanced material properties available for special applications.

![]({{ '/assets/images/pre-processor/10_material_data/10_12_miscellaneous_data/10_12_image001.jpg' | relative_url }})

Advanced material properties window

## Fracture Data (FRCMOD)

[FRCMOD](/docs/sk/keyword_documentation/f/frcmod/) specifies the damage model that one wishes to use for damage calculation. There are ten different models to choose from. Cockcroft & Latham is the Default damage model that is used to calculate damage in DEFORM. It is also possible to write a user subroutine, which can be used for the damage model. For Fracture models refer chapter [10.12.1. Fracture Models](/docs/sk/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/)

## Mechanical Work to Heat (FRAE2H)

Mechanical work to heat ([FRAE2H](/docs/sk/keyword_documentation/f/frae2h/)) specifies the fraction of mechanical work converted to heat. The conversion fraction would typically be 0.9 to 0.95. The default value is 0.9 and unless the user has a good feel for a value, this value should not be changed.

## Force per unit volume or Body Force (FPERV)

The following equation is used to calculate the body force ([FPERV](/docs/sk/keyword_documentation/f/fperv/)) (for example gravity) for porous, plastic and elasto-plastic materials:  

![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/eq_10_12_1.jpg' | relative_url }}) |   
---|---  
  
  
For example if density of steel in SI units is 7850 Kg/m^3, and acceleration due to gravity is 9.8 m/Sec^2, the bogy force input needs to be 0.00007693 ton/(mm^2. Sec^2) or 0.00007693 N/mm^3.

## Centrifugal force

Centrifugal force can be directly applied to the object without any rotational movement controls. When defined in the material data this represents the radial body force which is a product of mass density and square of rotational speed in radian/sec. For example in SI units when the object is rotating at 7000rpm which is 733.0382 rad/sec. Assuming material as steel, the centrifugal force is 4.21816 N when consistent units are used.

## Diffusion Bonding 

Diffusion bonding time is the time required to achieve 100% bonding under certain conditions like temperature and pressure. This option is available only in MO Environment.  
The Inter object relation need to be defined between bonding objects as Master-Slave relation. Diffusion bonding percentage will be calculated as a state variable of Slave Object. Diffusion bonding can be activated by checking Turn on Diffusion bonding Calculations check box in properties tab of Simulation Controls as shown in below Fig. 10.12.2.

![]({{ '/assets/images/pre-processor/10_material_data/10_12_miscellaneous_data/10_12_image002.jpg' | relative_url }})

Properties window showing diffusion bonding checkbox with red color

The Diffusion Bonding properties can be defined for slave object under Material properties Advanced Tab as shown in Fig. 10.12.3.

![]({{ '/assets/images/pre-processor/10_material_data/10_12_miscellaneous_data/10_12_image004.jpg' | relative_url }})

Advanced Material window showing Diffusion bonding with red color

If temperature or pressure is not constant, effective accumulated bonding percentage will be calculated based on the defined data. The bonding time for 1% and 99% needs to be specified as a function of temperature and pressure as shown in Fig. 10.12.4.

![]({{ '/assets/images/pre-processor/10_material_data/10_12_miscellaneous_data/10_12_image005.jpg' | relative_url }})

Diffusion bonding Function window Definition

## Size Model (SIZESH and SIZEMD)

This model (See below Fig. 10.12.5.) can record information regarding phases, beyond simple volume fraction transformed. Prior to the size model implementation, the only information available about a phase in a mixture material was its volume fraction in an element (for example 80% austenite, 20% martensite). This was sufficient for materials like steels (where properties can be derived by simply using the 'rule of mixtures' law), but not sufficient for materials like nickel base superalloys or aluminium alloys, for which small volume fractions of precipitates have big impacts.

![]({{ '/assets/images/pre-processor/10_material_data/10_12_miscellaneous_data/10_12_image006.jpg' | relative_url }})

Size model selection window

  
The [SIZESH](/docs/sk/keyword_documentation/s/sizesh/) stores information regarding the size of a 2nd phase and its shape. Thus, a 2nd phase (for example, delta phase particles in 718 nickel base super alloy) can be described as composing 5% of the volume fraction of each element of the material (defined in initial elemental volume fraction, [VOLFC](/docs/sk/keyword_documentation/v/volfc/)); but it can also be described as consisting of particles which, on average, are ~10 microns in diameter. By default, the [SIZESH](/docs/sk/keyword_documentation/s/sizesh/) keyword assumes that particles are spherical (See above Fig. 10.12.5.). By specifying the particle size model ([SIZEMD](/docs/sk/keyword_documentation/s/sizemd/)), one can define more about the properties of the particles described in [SIZESH](/docs/sk/keyword_documentation/s/sizesh/).  
  
Different particles size models available are,

  1. Spherical: 2nd phase particles are spherical
  2. Secondary Alpha Lath - General: 2nd phase particles are secondary alpha particles in Ti
  3. Secondary Alpha Lath - Cooling Rate: 
  4. Grain Boundary Alpha: 2nd phase particles are secondary alpha particles in Ti at grain boundaries
  5. Side Plate Alpha: 2nd phase particles are side plate alpha particles in Ti
  6. Gamma Prime Nickle: 2nd phase particles are particles which induce grain boundary pinning during growth and recrystallization (such as delta in 718)
  7. Precipitation – Size and Number:
  8. JMAK Grain Model:

This model is further extensible in the future, should one wish to model cuboidal particles (such as gamma prime in powder metallurgy nickel base superalloys), or plate, needle, or disk like particles in other alloys.

## Sintering Driving Force Model

Sintering driving force models simulate deformation behavior resulting from sintering processes. Sintering driving force models are only applicable to porous objects, with the exception of the “Simple elastic one step” model. 

  * **Simple Elastic one-step**

As the name indicates this model (See Fig. 10.12.6.) is used to simulate the shrinkage resulting from a sintering process using a single simulation step and an elastic workpiece. For a given relative density distribution and elastic properties this model will compute sintering shrinkage, when part reaches near full density levels after sintering. 

![]({{ '/assets/images/pre-processor/10_material_data/10_12_miscellaneous_data/10_12_image012.jpg' | relative_url }})

Simple Elastic one-step Sintering model

Volumetric strain is given by,

![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/eq_10_12_2.jpg' | relative_url }}) |   
---|---  
  
Sintering Stress is given by,

![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/eq_10_12_3.jpg' | relative_url }}) |   
---|---  
  
  
User needs to follow the below steps to perform sintering shrinkage using this model,

  1. Delete the die components
  2. Reset the velocity field
  3. Reset the displacement field
  4. Reset the strain
  5. Change the object to elastic
  6. Define elastic properties
  7. Use Newton Raphson Iterations
  8. Apply necessary boundary conditions
  9. Generate DB and simulate for 1 step

  
Note: 

  1. For 3D tet mesh models use mixed formulations

  2. The simple elastic one step model may alternatively be activated by placing a DEF_SINTER.DAT empty flag file in problem folder. 

**Skorohod**

For Skorohod equation input window see Fig. 10.12.7.

![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/eq_10_12_4.jpg' | relative_url }}) |   
---|---  
  
![]({{ '/assets/images/pre-processor/10_material_data/10_12_miscellaneous_data/10_12_image008.jpg' | relative_url }})

Skorohod window Definition

**Cocks**

For Cocks equation input window see Fig. 10.12.8.

![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/eq_10_12_5.jpg' | relative_url }}) |   
---|---  
  
![]({{ '/assets/images/pre-processor/10_material_data/10_12_miscellaneous_data/10_12_image009.jpg' | relative_url }})

Cocks window Definition

**Shinagawa**

For Shinagawa equation input window see Fig. 10.12.9.

![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/eq_10_12_6.jpg' | relative_url }}) |   
---|---  
  
![]({{ '/assets/images/pre-processor/10_material_data/10_12_miscellaneous_data/10_12_image010.jpg' | relative_url }})

Shinagawa window Definition

**Ashby**

For Ashby equation input window see Fig. 10.12.10.

![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/eq_10_12_7.jpg' | relative_url }}) |   
---|---  
  
![]({{ '/assets/images/pre-processor/10_material_data/10_12_miscellaneous_data/10_12_image011.jpg' | relative_url }})

Ashby window Definition

**Raj****/Ashby**

For Raj/Ashby equation input window see [Fig. 10.12.11.](10_12_miscellaneous_data.htm#Fig._10.12.11._Raj/Ashby__window_Definition)

![]({{ '/assets/equations/pre_processor/10_material_data/10_12_miscellaneous_data/eq_10_12_8.jpg' | relative_url }}) |   
---|---  
  
![]({{ '/assets/images/pre-processor/10_material_data/10_12_miscellaneous_data/10_12_image007.jpg' | relative_url }})

Raj/Ashby window Definition

## Material data requirements

**Guidelines**

  1. An isothermal forming problem with rigid dies and a rigid-viscoplastic workpiece.

| **Workpiece** | **Dies**  
---|---|---  
Material Data  |  |   
Flow Stress | X |   
Young's Modulus  |  |   
Poisons Ratio  |  |   
Thermal Expansion |  |   
Heat Capacity  |  |   
Conductivity  |  |   
Emissivity  |  |   
  
Material data guidelines for isothermal forming

  1. A Non-isothermal forming problem with rigid dies and a rigid-viscoplastic workpiece.

| **Workpiece** | **Dies**  
---|---|---  
Material Data  |  |   
Flow Stress | X |   
Young's Modulus  |  |   
Poisons Ratio  |  |   
Thermal Expansion |  |   
Heat Capacity  | X | X  
Conductivity  | X | X  
Emissivity  | X | X  
  
Material data guidelines for Non-isothermal forming

  1. Heat transfer analysis.

| **Workpiece** | **Dies**  
---|---|---  
Material Data  |  |   
Flow Stress |  |   
Young's Modulus  |  |   
Poisons Ratio  |  |   
Thermal Expansion |  |   
Heat Capacity  | X | X  
Conductivity  | X | X  
Emissivity  | X | X  
  
Material data guidelines for heat transfer

  1. Coupled analysis non-isothermal with thermal expansion Elastic dies and elasto-plastic workpiece.

| **Workpiece** | **Dies**  
---|---|---  
Material Data  |  |   
Flow Stress | X |   
Young's Modulus  | X | X  
Poisons Ratio  | X | X  
Thermal Expansion | X | X  
Heat Capacity  | X | X  
Conductivity  | X | X  
Emissivity  | X | X  
  
Material data guidelines for Non- isothermal analysis with thermal expansion

  1. Decoupled die stress analysis isothermal.

| **Workpiece** | **Dies**  
---|---|---  
Material Data  |  |   
Flow Stress | X |   
Young's Modulus  |  | X  
Poisons Ratio  |  | X  
Thermal Expansion |  |   
Heat Capacity  |  |   
Conductivity  |  |   
Emissivity  |  |   
  
Material data guidelines for isothermal de-coupled die stress analysis

  1. Decoupled die stress analysis non-isothermal.

| **Workpiece** | **Dies**  
---|---|---  
Material Data  |  |   
Flow Stress | X |   
Young's Modulus  |  | X  
Poisons Ratio  |  | X  
Thermal Expansion |  | X  
Heat Capacity  | X | X  
Conductivity  | X | X  
Emissivity  | X | X  
  
Material data guidelines for Non-isothermal de-coupled die stress analysis

Related Topics:

[10.12.1. Fracture Models](/docs/sk/pre_processor/10_material_data/10_12_miscellaneous_data/10_12_1_fracture_models/)

[Assigning Material to Object](../../../operation_templates/33_forming/33_1_2d_forming_setup.htm#Material)   
[1.11. DEFORM Units](/docs/sk/about_deform/1_introduction_to_deform/1_9_units/)  
[Material Editing](/docs/sk/labs/heat_treatment_labs/2d_ht_lab5_material_input/)  
[Material Units Converter](../10_material_data.htm#Material_Data)   
[Units Converter Next Gen Post](../../../post_processor/26_post_processing_tools_and_controls/26_5_post_processing_options.htm#26_5_6_Unit_Conversion)  
[Appendix IV: Determining 'R' coefficients for anisotropy models](/docs/sk/appendices/appendix_iv_determining_r_coefficientss/)  
[Running an inertia weld simulation in DEFORM](/docs/sk/applications/55_applications/55_inertia_welding/2d_inertia_welding/)  
[Running 2D creep simulations in DEFORM](/docs/sk/applications/55_applications/55_creep/2d_creep/)  
[Appendix X: Meshing an object with multiple material groups](/docs/sk/appendices/appendix_x_meshing_an_object_with_multiple_material_group/)  
[Setting up 2D induction heating in DEFORM](/docs/sk/applications/55_applications/55_4_induction_heating/setting_up_induction_heating_in_deform/)  
[Fracture with Element Deletion and Damage Softening](/docs/sk/applications/55_applications/55_fracture/3d_fracture/)  
[Setting up 2D fracture with element deletion with DEFORM](/docs/sk/applications/55_applications/55_fracture/2d_fracture/)  
[A Theoretical Background to Resistance Heating Concepts](/docs/sk/applications/55_applications/55_resistance_heating_labs/a_theoretical_background_to_resistance_heating/)   
[Setting up 3D machining models](/docs/sk/operation_templates/39_cutting/setting_up_3d_machining_models/)

---
lang: en
title: "17.2. Element Data Window"
---

# 17.2. Element Data Window ![]({{ '/assets/icons/pre_icons/mo_elemental_data_icon.jpg' | relative_url }})

17.2.1. Features of the display window include in Element Data window

17.2.2. Element Data Initializing

17.2.3. Deformation Tab

  * General Tab

  * Stress components Tab

  * Back Stress Components Tab

  * Strain Components Tab

  * Strain Rate Tab

  * Mat. Angle Tab

17.2.4. Hardness Tab

  * Hardness

  * Cooling Time

17.2.5. Electric Heating Tab

  * Electric field intensity R

  * Electric field intensity I

17.2.6. Microstructure Tab

  * Grain Tab

  * Phase Tab

17.2.7. Size Tab

17.2.8. Texture Tab

17.2.9. User tab

17.2.10. Thermomechanical Tab

17.2.11. Additive Manufacturing Tab

**[2D, 3D]** : From the element data dialog user can examine a complete set of elemental data that is applicable to a given model (See Fig. 17.2.1. and Fig. 17.2.2.). This data includes, stress, strain, strain rate, material axis, hardness, transformation data, heating data, grain data and user defined elemental variables.

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_2_element_data_window/17_2_image001.jpg' | relative_url }})

Elemental Deformation General data window for 2D

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_2_element_data_window/17_2_image002.jpg' | relative_url }})

Elemental Deformation General data window for 3D

The elements window displays all available information about the elements. All information can be modified, and many of the variables can be plotted.

## Features of the display window include in Element Data window

**Element** :

The number of the element for which information is being displayed. A element may be selected either by keying in the value or by using the select icon and mouse-picking an element.

**Elemental Connectivity** (ELMCON):

The element connectivity ([ELMCON](/docs/en/keyword_documentation/e/elmcon/)) specifies the numbers of the 4 or 8 nodes which define the corners of the element.

**Highlight Element** : To highlight the selected element in graphic display. 

**Initialize values** : ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}) icon initializes the specified variable value on Element in the object for,

  * a particular Element

  * Range of Element

  * Picking the Element using pick tools (See Fig. 17.2.3. and Fig. 17.2.4.)

  * Interpolation method

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_2_element_data_window/17_2_image003.jpg' | relative_url }})

Picking tools for selecting Element for 2D

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_2_element_data_window/17_2_image004.jpg' | relative_url }})

Picking tools for selecting Element for 3D

**Plot variable:**

![]({{ '/assets/icons/pre_icons/mo_plot_icon.jpg' | relative_url }}) Plots selected Element state variable in shaded contour.

Plot type can be changed by right mouse click option on contour bar in display window.

## Element Data Initializing

We can initialize the data using two methods, Assign and Interpolation methods.

We have another two options:

**Range** : Using Range option user can define the Start Element number and End Element number and the variable value. After defining the parameters when user clicks on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) button the data will be initialize to the selected nodes.

**Picking** : Using picking option user can select the Elements to initialize the value. 

Related to picking options refer 14. Boundary Condition [Picking options for 2D](../14_boundary_conditions/14_boundary_conditions.htm#Picking_option_for_2D) and [Picking options for 3D](../14_boundary_conditions/14_boundary_conditions.htm#Picking_option_for_3D).

## Deformation Tab **[2D, 3D]**

**General Tab**

  * **Material (MTLGRP)** : [MTLGRP](/docs/en/keyword_documentation/m/mtlgrp/) specifies the material number associated with each element.

  * **Density (DENSTY)** : [DENSTY](/docs/en/keyword_documentation/d/densty/) specifies the relative density of the material at each element. [DENSTY](/docs/en/keyword_documentation/d/densty/)is used when a porous material with relative densities less than 1.0 is being simulated. If no value is specified for density, it is assumed to be 1.0. The flow stress of porous objects should be specified for the fully dense material.

  * **Eff. Strain** **(STRAIN)** : [STRAIN](/docs/en/keyword_documentation/s/strain/) specifies the value of total effective strain at the centroid of each element. Elemental strains are interpolated between meshes during remeshing procedures. When user select "Integration" type Element/Nodal output for Strain under Simulation controls![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})Advanced options ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) [Advanced output](../9_simulation_controls/9_7_advanced_options.htm#9.7.4._Output_Control), for Brick mesh object we can observe 8 Integration outputs values for each element as shown in Fig. 17.2.5. User can also initalize the values for each integration points. Even for Damage and Stress state varaibles "Integration" type Element/Nodal output option is available.

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_2_element_data_window/17_2_image005.jpg' | relative_url }})

Eff.Strain Integration point display in Element data window

  * **Damage (DAMAGE) :**[DAMAGE](/docs/en/keyword_documentation/d/damage/) specifies the damage factor at each element based on the model selected under material dialog. The damage factor can be used to predict fracture in cold forming operations. The damage factor increases as a material is deformed. Fracture occurs when the damage factor has reached its critical value.

**Stress components Tab (STRESS)**  
**[2D, 3D]**[STRESS](/docs/en/keyword_documentation/s/stress/) defines the stress tensors of each element of an object. (See Fig. 17.2.6.)

In a 2Dplane strain model, displayed values are X/R is the value of ![]({{ '/assets/equations/pre_processor/17_object_data_initialization/sigma_x.png' | relative_url }}) , Y/Z is ![]({{ '/assets/equations/pre_processor/17_object_data_initialization/sigma_y.png' | relative_url }}), Z/Theta is ![]({{ '/assets/equations/pre_processor/17_object_data_initialization/sigma_z.png' | relative_url }}) and XY/RZ is ![]({{ '/assets/equations/pre_processor/17_object_data_initialization/tou_xy.png' | relative_url }}).

In an 2D axisymmetric model, displayed values X/R is the value of ![]({{ '/assets/equations/pre_processor/17_object_data_initialization/sigma_r.png' | relative_url }}), Y/Z is ![]({{ '/assets/equations/pre_processor/17_object_data_initialization/sigma_z.png' | relative_url }}), Z/Theta is ![]({{ '/assets/equations/pre_processor/17_object_data_initialization/sigma_theta.png' | relative_url }}) and XY/RZ is ![]({{ '/assets/equations/pre_processor/17_object_data_initialization/tou_rz.png' | relative_url }}).

In 3D stress value displayed are ![]({{ '/assets/equations/pre_processor/17_object_data_initialization/sigma_x.png' | relative_url }}),![]({{ '/assets/equations/pre_processor/17_object_data_initialization/sigma_y.png' | relative_url }}) , ![]({{ '/assets/equations/pre_processor/17_object_data_initialization/sigma_z.png' | relative_url }}),![]({{ '/assets/equations/pre_processor/17_object_data_initialization/sigma_xy.png' | relative_url }}) , ![]({{ '/assets/equations/pre_processor/17_object_data_initialization/sigma_yz.png' | relative_url }}) and ![]({{ '/assets/equations/pre_processor/17_object_data_initialization/sigma_zx.png' | relative_url }}).

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_2_element_data_window/17_2_image006.jpg' | relative_url }})

Stress Component in Element data window for 3D

**Back Stress Components Tab (YLDS)**  
**[2D, 3D]**[YLDS](/docs/en/keyword_documentation/y/ylds/) specifies the yield surface translation tensor for kinematic hardening. In the case of isotropic hardening, these values remain all zero. (See Fig. 17.2.7.)

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_2_element_data_window/17_2_image007.jpg' | relative_url }})

Back stress in Element data window for 3D

**Strain Components Tab**  
**[2D, 3D]** Specifies the Strain tensor of each element of an object.(See Fig. 17.2.8.)

To activate the Strain component output we have to select type of strain output check box like Plastic, Elastic, Creep, Transformation and Thermal volumetric and Transformation volumetric under Simulation control [Advanced output](../9_simulation_controls/9_7_advanced_options.htm#9.7.4._Output_Control) tab.

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_2_element_data_window/17_2_image008.jpg' | relative_url }})

Strain component in Element data window for 3D

**Strain Rate Tab**  
Specifies the Strain rate tensors of each element of an object.

In 2D Values for X/R, Y/Z, Z/Theta, XY/RZ are entered by clicking on initialize button to calculate Max.principal stress and Min.principal stress for a particular element. This is more useful once the simulation as completed, so that principal stress can be checked for each element either by selecting the element number or just clicking on a particular element of the object.

**Mat. Angle Tab (MATAXI)**  
The material angle ([MATAXI](/docs/en/keyword_documentation/m/mataxi/)) measures the amount and direction of rotation about the Z (perpendicular to the plane of the screen) axis. The direction follows the right-hand rule where counter-clockwise is positive and clockwise is negative. The units for the angle are in radians.

## Hardness Tab

**[2D, 3D]** For Hardness elemental data dialog see Fig. 17.2.9.

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_2_element_data_window/17_2_image009.jpg' | relative_url }})

Elemental Hardness data window

  * **Hardness****(HDNOBJ1)** : Hardness ([HDNOBJ1](/docs/en/keyword_documentation/h/hdnobj/)) specifies hardness value for each element.

  * **Cooling Time (HDNOBJ2)** : Cooling Time ([HDNOBJ2](/docs/en/keyword_documentation/h/hdnobj/)) specifies the time to cool from high temperature to low temperature for each element. This data can be used in conjunction with Jominy data to determine a hardness value.

## Electric Heating Tab

**[2D, 3D]** For Electric Heating elemental data dialog see Fig. 17.2.10.

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_2_element_data_window/17_2_image010.jpg' | relative_url }})

Elemental Electric Heating data window for Induction heating Type

**Electric field intensity R :** is the real value of the electric field intensity of each element.

**Electric field intensity I :** is the imaginary value of the electric field intensity of each element.

## **Microstructure Tab**

**Grain Tab**  
**[2D, 3D]** These are the element values for all the various grain state variables. (See Fig. 17.2.11.)

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_2_element_data_window/17_2_image011.jpg' | relative_url }})

Elemental Grain variable data window

**Phase (Transformation) Tab**  
For the elemental microstructure transformation phase data dialog see Fig. 17.2.12.

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_2_element_data_window/17_2_image012.jpg' | relative_url }})

Elemental Phase Transformation variable data window

  * **Current volume fraction (VOLFC):**[VOLFC](/docs/en/keyword_documentation/v/volfc/) specifies the initial volume fraction of a phase (material) in an element at the beginning of a simulation. In addition, throughout the simulation, [VOLFC](/docs/en/keyword_documentation/v/volfc/) stores the volume fraction of all phases in each element per step. The volume fraction is determined from the keyword [TTTD](/docs/en/keyword_documentation/t/tttd/), which specifies the model or data used in calculating the volume fraction of each phase. It is important that the user specifies the necessary input for the keyword [TTTD](/docs/en/keyword_documentation/t/tttd/) or else the volume fraction ([VOLFC](/docs/en/keyword_documentation/v/volfc/) ) will not be calculated for the object. The user must input the type of diffusion model and at least two Time-Temperature curves, the beginning of the transformation and the end of the transformation.

  * **Starting volume fraction (VOLFS) :**[VOLFS](/docs/en/keyword_documentation/v/volfs/) specifies the volume fraction limit of a phase in an element of an object. [VOLFS](/docs/en/keyword_documentation/v/volfs/) is only stored in the database at the beginning of a new phase transformation, ex. Austenite![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Pearlite or Austenite ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Martensite. The intent of [VOLFC](/docs/en/keyword_documentation/v/volfc/) is to assure that the volume fraction amount transformed from Austenite ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Pearlite does not exceed the volume fraction of Austenite prior to transformation. It should be noted that [VOLFC](/docs/en/keyword_documentation/v/volfc/) is different than [VOLFS](/docs/en/keyword_documentation/v/volfs/) in that [VOLFC](/docs/en/keyword_documentation/v/volfc/) stores the volume fraction of the phases every step. Typically, the user will only be concerned with inputting volume fractions for [VOLFS](/docs/en/keyword_documentation/v/volfs/) at the beginning of the simulation.

  * **Volume fraction change (DVOLF) :**[DVOLF](/docs/en/keyword_documentation/d/dvolf/) specifies the change in volume fraction of all the different phases that resulted from the transformation during each time step. [DVOLF](/docs/en/keyword_documentation/d/dvolf/) of each phase is initially set to zero in a simulation. [DVOLF](/docs/en/keyword_documentation/d/dvolf/) is determined by for each step where f is the volume fraction of a particular phase. [DVOLF](/docs/en/keyword_documentation/d/dvolf/) is used in calculating the latent heat due to transformation and the change in volume of the object. [DVOLF](/docs/en/keyword_documentation/d/dvolf/) can be invaluable in determining the progress of a transformation and aid the user in deciding whether to increase or decrease the time step for a particular transformation.

  * **Incubation time (TICF):**[TICF](/docs/en/keyword_documentation/t/ticf/) (consumption of incubation time) specifies the fraction of time that has occurred before the transformation has started. It is calculated for diffusion type transformation as follows: [TICF](/docs/en/keyword_documentation/t/ticf/) = where is the time increment and is the incubation time at temperature. The variable total is temperature dependent. If [TICF](/docs/en/keyword_documentation/t/ticf/) reaches, the transformation starts. This incubation time is not an input data, but computed by FEM.

## Size Tab

## Texture Tab

## User Tab

**[2D,3D]** The data for User element variables ([USRELM](/docs/en/keyword_documentation/u/usrelm/)) can be initialized, defined or examined here.

User element variable values can be defined using FORTRAN subroutines. [Refer chapter 56 section USRUPD subroutines.](../../user_routines/56_user_routines_in_deform/56_2_2d_user_defined_fem_routines.htm#56_2_3_3_User_defined_node_and_element_value_\(USRUPD\)) Each element value may accept both a name and a value. (See Fig. 17.2.13.) Also, an infinite number of variables may be defined. A minimum of 2 user element variables will be defined by default, however, the user may increase this to as large number as wished. User needs to be cautious that a large number of variables defined can lead to a large database file.

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_2_element_data_window/17_2_image013.jpg' | relative_url }})

User Elemental variable data window

## Thermomechanical Tab

**[2D, 3D]** Under Simulation controls - [Thermomechanical](/docs/en/pre_processor/9_simulation_controls/9_9_thermomechanical_variables/) variable page, added variables related to Element data will be listed under Thermomechanical variable ( [ERECID](/docs/en/keyword_documentation/e/erecid/)) tab in Element data window as shown in Fig. 17.2.14. Thermomechanical variable value can be initialized or examined here. 

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_2_element_data_window/17_2_image014.jpg' | relative_url }})

Thermomechanical Elemental variable data window

## Additive Manufacturing Tab

**[3D]** Under Additive manufacturing ([LAYRID](/docs/en/keyword_documentation/l/layrid/)) tab user can define the Layer ID for the sliced layers of the object used for Additive manufacturing process (see Fig. 17.2.15.). Even after doing [Slice Layers](../18_object_manipulation_tools/18_1_boolean.htm#Fig_18_1_8_Slice_layers_page) in [Boolean](/docs/en/pre_processor/18_object_manipulation_tools/18_1_boolean/) page, user can assign Layer ID for each sliced layers in 3D Geometry Examine page.

![]({{ '/assets/images/pre-processor/17_object_data_initialize/17_2_element_data_window/17_2_image015.jpg' | relative_url }})

Additive manufacturing Elemental variable data window

**Related Topics:**

[17\. Object Data Initialize](/docs/en/pre_processor/17_object_data_initialization/17_object_data_initialize/)

[17.1. Node Data Window](/docs/en/pre_processor/17_object_data_initialization/17_1_node_data_window/)

[17.3. Data Interpolation Window](/docs/en/pre_processor/17_object_data_initialization/17_3_data_interpolation_window/)

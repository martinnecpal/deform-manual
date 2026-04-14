---
lang: sk
title: "10.9. Transformation Data"
---

# 10.9. Transformation Data

10.9.1 Inter material Data  
10.9.2. Transformation relation (PHASTF)

  * Kinetics model (TTTD)

  * Latent heat and volume(PHASLH)

  * Latent Heat

  * Transformation induced volume change (PHASVL)

  * Transformation plasticity (TRNSFP)

  * Other

  * Thermal Direction

  * Equilibrium volume fraction

  * Variation selection model

  * Interface Energy

## Inter material Data

The purpose of inter-material data is to define the relationships between the phases of a mixture. As defined in the material data, a mixture is defined by the user as a set of phases. The relationships between the phases are defined in terms of the following transformation characteristics:

  * Transformation kinetics model
  * Latent heat of transformation
  * Transformation induced volume change
  * Transformation plasticity

The purpose of this section is to give the user an understanding of how to properly define a transformation relationship between two phases. This section will explain in how DEFORM handles the above concepts. Transformation is a crucial concept in metal forming and heat treatment. [Fig. 1.3.1.](../../../About_DEFORM/1_Introduction_to_DEFORM/1_3_Capabilities.htm#Fig._1.3.1._Relationship_between_various_DEFORM_modules) illustrates the coupling between temperature, deformation, transformation, and carbon content. Transformation is modelled by defining the volume fraction for each possible phase in each element of a meshed object. For low carbon steel object, each element may contain different volume fraction of Martensite, Bainite, Pearlite or Austenite. Each phase is defined by its own set of material properties. These material properties define the plastic behavior of the phase, the thermal properties of the phase, and possibly (if using an elastic-plastic mate-rial) the elastic properties of the phase. 

The relationship between the transformations from one phase to another is de-fined by the inter-material data. This relationship is defined in terms of a kinetics model (in order to determine rate of phase transformation) and a few relational properties such as latent heat and volume change.

## Transformation relation (PHASTF) 

In DEFORM, the manner in which transformation is defined is in terms of transformation relationships ([PHASTF](/docs/sk/Keyword_Documentation/P/PHASTF/)). The basic unit for transformation relationships are phases. Phases can be grouped together to define a mixture. A mixture corresponds to a material such as AISI-1045 or Ti-6Al-4V. For each phase defined, there may be a transformation relation to any other phase that is defined. For example, in the case of low carbon steel, austenite has a relationship to pearlite since austenite may form pearlite upon the proper cooling conditions. Also, upon proper heating conditions, pearlite can convert to austenite. Thus, in DEFORM, to specify the relationship of austenite converting to pearlite, one needs to select the austenite as Material 1 and the pearlite as Material 2 and then click the Phase 1 Phase 2 relationship. This will then allow the user to define the kinetics of the transformation, the latent heat of the transformation, volume change of the transformation, etc. (See [Fig. 1.3.1.](../../../About_DEFORM/1_Introduction_to_DEFORM/1_3_Capabilities.htm#Fig._1.3.1._Relationship_between_various_DEFORM_modules))

  
The mixture material data can be created by specifying the Mother material and its phases and defining there general material data and inter material or transformation data as mentioned below, (See Fig. 10.9.1.)

  1. Click on the ![](../../../../assets/Icons/Pre_icons/MO_Add_Icon2.jpg) button to create the material (See **1.1** in Fig. 10.9.1.), then select the Mixture material check box to make the added material as mixture material (See**1.2** in Fig. 10.9.1.), it becomes the Mother material of the mixture material.
  2. Select the Mother material (See **2.1** in Fig. 10.9.1.) and click on the ![](../../../../assets/Icons/Pre_icons/MO_Add_Phase_button.jpg) button (See **2.2** in Fig. 10.9.1.), this will add its phases, also added phases can be removed using the ![](../../../../assets/Icons/Pre_icons/MO_Remove_phase_button.jpg) button by selecting phases.
  3. Repeat the step**2** as many times as the number of phases (See **3** in Fig. 10.9.1.).
  4. Define the General material data using the plastic, Elastic, etc icons (See **4.1** in Fig. 10.9.1.) for Mother material and other phases, then click on Transformation icon (See **4.2** in Fig Fig. 10.9.1.) to define the Transformation data between the child phases. If user wants to define the Coarsening data than select the Coarsening icon.
  5. Select the Mother to Child phase transformation relation (See **5.1** and **5.2** in Fig. 10.9.1.) and then click on ![](../../../../assets/Icons/Pre_icons/MO_Add_Icon2.jpg) button (See 5.3 in Fig. 10.9.1.) then define the transformation kinetics, Latent heat, volume change, Transformation plasticity and other data (See 5.4 in Fig. 10.9.1.).
  6. Repeat the step 5 for the other phase’s transformations.

**Note** :  
Grain model data for the mixture materials can be defined only for the phases by selecting the Phases using the Grain button.

![](../../../../assets/Images/Pre-Processor/10_Material_Data/10_9_Transformation_Data/10_9_Image001.jpg)

Creating the mixture material

  * **Kinetics model (TTTD)**

![](../../../../assets/Images/Pre-Processor/10_Material_Data/10_9_Transformation_Data/10_9_Image002.jpg)

Transformation kinetics definition window

A kinetics model ([TTTD](/docs/sk/Keyword_Documentation/T/TTTD/)) is a function that defines the conditions and manner in which one phase may transform into another. The amount of data required is often considerable as in the case for a full TTT diagram, so unless necessary, often using coefficients for a function can suffice. A model defines one relationship only so many relationships are required for such cases as steel where many phases can be produced. There are two classifications for kinetics models, diffusion-type transformations, and diffusion less type transformations. The system is designed for both ferrous and nonferrous metals. Using carbon steel as an example, the Austenite-ferrite and Austenite-Pearlite structure changes and vice versa are governed by the diffusion type transformation. The transformation is driven by the diffusion processes depending on the temperature, stress history, and carbon content. The diffusion less transformation from Austenite to Martensite involves a shear process, which depends on the temperature, stress, and carbon content. For more information of Kinetics model Refer [Chapter 10.9.1.Transformation Kinetics Models.](/docs/sk/pre_processor/10_material_data/10_9_transformation_data/10_9_1_Transformation_Kinetics_Models/)

  * **Latent heat and Volume (PHASLH)**

![](../../../../assets/Images/Pre-Processor/10_Material_Data/10_9_Transformation_Data/10_9_Image003.jpg)

Transformation induced volume and latent heat window

  * **Latent Heat :****Latent heat** ([PHASLH](/docs/sk/Keyword_Documentation/P/PHASLH/)) accounts for the net energy gain or loss when a phase change occurs from one phase to another. Latent heat may be a constant value, a function of either temperature or a function of the dominant atom content.(See Fig. 10.9.3.) The energy release due to the latent heat can prolong the time of transformation. A positive sign on the latent heat value means that the transformation acts as a heat source and a negative sign means that the transformation acts as a heat sink. The units for this variable are Btu/in3 for English units and N/mm2 for SI units.

  * ******T****ransformation induced volume change ([PHASVL](/docs/sk/Keyword_Documentation/P/PHASVL/)) : **Volume change may be the result of a phase transformation. This volume change ([PHASVL](/docs/sk/Keyword_Documentation/P/PHASVL/)) may induce stresses in the transforming object and will certainly affect the final dimensions after processing. Volume change may be a constant value, a function of either temperature, dominant atom content or temperature and dominant atom content. The volume change due to transformation is induced by a change in the lattice structure of a metal. The transformation strain is used mainly to account for the structure change during the transformation and is in the form of: 

![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/EQ_10_9_1.JPG) |   
---|---  
  
  
A positive sign in the volume change means there is an increase in volume change and a negative sign means there is a decrease in volume over the transformation. This variable is without units.

  * **Transformation plasticity (TRNSFP)**

As a material undergoes transformation, it will plastically deform at a stress lower than the flow stress. This phenomenon is known as Transformation Plasticity ([TRNSFP](/docs/sk/Keyword_Documentation/T/TRNSFP/)). The change of the dimensions of a part due to transformation plasticity occurs in combination with the dimension changes due to transformation induced volume change. In DEFORM the equation for transformation plasticity is as shown in Fig. 10.9.4. and EQ(10.9.2).

  
![](../../../../assets/Images/Pre-Processor/10_Material_Data/10_9_Transformation_Data/10_9_Image004.jpg)

Transformation plasticity window

![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/EQ_10_9_2.jpg) |   
---|---  
  
The only data that the user needs to provide for this relationship is the transformation plasticity coefficient. The other terms are automatically calculated by DEFORM. The transformation plasticity coefficient may be a function of temperature.  
A general range for ![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/K_ij.jpg) for steel is given below,

  * Austenite - Ferrite, Pearlite or Bainite (4 - 13 *10-5 /MPa)
  * Austenite - Martensite (5 - 21 * 10-5 /MPa)
  * Ferrite & Pearlite - Austenite (6 - 21 *10-5 /MPa)

  * Other

  * **Thermal Direction :** Thermal direction gives the simulation a bit more information, so transformation does not errantly generate volume fraction. For example, when heating steel from room temperature to austentizing temperature, any bainite will be converted, over time, to austenite. During the heating, austenite may be converted back to bainite since it may be defined as a possibility. This definition prevents this. It is recommended to use this sparingly. (See Fig. 10.9.5 )

![](../../../../assets/Images/Pre-Processor/10_Material_Data/10_9_Transformation_Data/10_9_Image005.jpg)

Other transformation properties window

  * **Equilibrium volume fraction :** Equilibrium volume fraction defines the maximum amount of a phase volume fraction generation during an isothermal condition.

  * **Variation selection model**

  * **Interface Energy**

---
lang: sk
title: "10.9.1. Transformation Kinetics Models"
---

# 10.9.1. Transformation Kinetics Models

  * Diffusion type TTT table form (Temp, Stress, Atom)

  * Martensitic type (Tms, Tms50 Table form)

  * Diffusion type (function)

  * Diffusion type (function and table)

  * Martensitic type (function)

  * Diffusion type (simplified)

  * MEDC

  * Secondary alpha lath

  * Secondary alpha lath - Based on critical cooling rate

  * Ti-beta to grain boundary alpha

  * Ti-beta to side plate alpha

  * [Solid/Liquid phase transformation](10_9_1_Transformation_Kinetics_Models.htm#Solid/Liquid_phase_transformation)

  * Diffusion(Solubility curve)

  * Ni gamma prime precipitation model

  * Ni gamma prime dissolution model

  * User routine

Below are the Transformation Kinetics Models available in DEFORM (See Fig. 10.9.1.1.),

  1. Diffusion type TTT table form (Temp, Stress, Atom) 
  2. Martensitic type (Tms, Tms50 Table form) 
  3. Diffusion type (function)
  4. Diffusion type (function and table)
  5. Martensitic type (function)
  6. Diffusion type (simplified)
  7. MEDC
  8. Secondary alpha lath
  9. Secondary alpha lath - Based on critical cooling rate
  10. Ti-beta to grain boundary alpha
  11. Ti-beta to side plate alpha
  12. Solid/Liquid phase transformation
  13. Diffusion(Solubility curve)
  14. Ni gamma prime precipitation mode
  15. Ni gamma prime dissolution model
  16. User routine

![](../../../../assets/Images/Pre-Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/10_9_1_Image001.jpg)

Transformation Kinetics models

  * **Diffusion type TTT table form (Temp, Stress, Atom)**

This type defines a TTT diagram (See Fig. 10.9.1.2. and Fig. 10.9.1.3) whose independent variables are average element temperature, effective stress and dominant atom content. In the case of steel, dominant atom content is the weight percentage of carbon in the metal at each element. Using tabular data, DEFORM is trying to solve an Avrami equation, which has the form, 

![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/EQ_10_9_1_1.JPG) |   
---|---  
  
![](../../../../assets/Images/Pre-Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/10_9_1_Image002.jpg)

Log (Time) function definition window for Diffusion TTT kinetics model

In terms of TTT data, two curves are required in order to solve for k and n. If only one curve is input to DEFORM, the user must provide the Avrami number.

![](../../../../assets/Images/Pre-Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/10_9_1_Image003.jpg)

Example TTT curve

Fig. 10.9.1.3 shows an example of TTT diagram in DEFORM. In the case above, two curves are used to define the percent transformed for a given dominant atom content. Each curve has a value at which an amount of transformation is defined. The curve to the left has been defined in which starting percentage of the transformation from Austenite to Bainite. The curve to the right has been defined in which ending percentage of the Austenite to Bainite transformation.

  * **Martensitic type (Tms, Tms50 Table form)**

The transformation start and 50 % level temperature are inputted as a table format by depending on carbon content and stress levels.  
This kinetics is based on Koistinen-Marburger Equation [1]. And a more generalized form is employed in DEFORM as the following equation [2]:

![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/EQ_10_9_1_2.jpg) |   
---|---  
  
  
[1] D.P. Koistinen, R.E. Marburger, Acta Metall, 7 (1959), pp. 59-60  
[2] S. M. C. van Bohemen, J. Sietsma, Mater. Sci. Technol., 30(2014), pp. 1024-1033  
  
For Martensitic type function definition window see below Fig. 10.9.1.4.

![](../../../../assets/Images/Pre-Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/10_9_1_Image004.jpg)

Martensitic start and 50% temperature table form transformation kinetic function definition window

  * **Diffusion type (function)**

Volume fraction is represented by the Avrami equation as follows:

![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/EQ_10_9_1_3.JPG) |   
---|---  
  
  
Where   
![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/ft_T.jpg), ![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/fs_m.jpg) and ![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/Fc_c.jpg) are the functions of temperature (![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/T.JPG)), Mean stress (![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/Sigma_m.jpg)) and Carbon content (![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/C.JPG) ) respectively.

  
The power ![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/small_n.jpg) depends on the kinds of the transformation and ![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/ft_T.jpg) can be expressed by the following simplified formula, 

![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/EQ_10_9_1_4.JPG) |   
---|---  
  
![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/Fs_sigma_m.jpg) in addition, ![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/Fc_c.jpg) describes the stress and carbon content dependency of transformation, respectively as follows:

![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/EQ_10_9_1_5.JPG) |   
---|---  
  
![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/EQ_10_9_1_6.JPG) |   
---|---  
  
  
The coefficients ![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/As.jpg) is specified according to the stress dependency of TTT curves, ![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/Ac1.jpg) and ![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/Ac2.jpg) are determined by carbon content dependency.  
  
For diffusion function type model definition window see below Fig. 10.9.1.5.

![](../../../../assets/Images/Pre-Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/10_9_1_Image005.jpg)

Diffusion kinetic transformation model definition window

  * **Diffusion type (function and table)**

![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/EQ_10_9_1_7.JPG) |   
---|---  
  
Along with the equation EQ(2.4.3) table is used in this diffusion type as shown in Fig. 10.9.1.6.

  
![](../../../../assets/Images/Pre-Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/10_9_1_Image006.jpg)

Diffusion function and table kinetics model definition window

  * **Martensitic type (function)**

The volume fraction of diffusionless-type (martensite) transformation depended on temperature, stress and carbon content is introduced by modifying the Magee's equation as follows:

![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/EQ_10_9_1_8.JPG) |   
---|---  
  
  
When the martensite transformation start temperatures under carburized conditions and applied stress are given, ![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/Phi2_by_phi1.jpg) , ![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/Phi31_by_Phi1.jpg) and ![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/Phi32_byPhi1.jpg) can be determined, ![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/Phi1.jpg) and ![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/Phi4.jpg) are identified, if temperatures for martensite-start TMS and for 50% martensite TM50 at ![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/zeta_m.jpg) = 0 and ![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/zeta_m.jpg) = 0.5 are provided respectively.  
  
For martensitic model definition window see below Fig. 10.9.1.7.

![](../../../../assets/Images/Pre-Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/10_9_1_Image007.jpg)

Martensitic transformation kinetics model definition window

  * **Diffusion type (simplified)**

A simplified Diffusion function is defined by a function of the following form:

![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/EQ_10_9_1_9.jpg) |   
---|---  
  
  
This formula is a good first approximation for a diffusion-based transformation.  
The coefficients can be obtained using dilatation-temperature diagrams.  
See the below Fig. 10.9.1.8. for Diffusion simplified function definition window.

![](../../../../assets/Images/Pre-Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/10_9_1_Image008.jpg)

Diffusion simplified kinetic transformation kinetics model definition window

  * **MEDC**

MEDC model is developed by AFRL in the United States to predict the microstructure evolution during continuous cooling of wrought alpha/beta titanium alloys in the two-phase field. The growth of the primary (globular) alpha during cooling is modelled using an exact solution of the diffusion equation:

![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/EQ_10_9_1_10.JPG) |   
---|---  
  
  
The particle radius is converted to volume fraction using the following expression:

![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/EQ_10_9_1_11.JPG) |   
---|---  
  
  
  
The intrinsic diffusion coefficients of alloying elements in beta titanium can be expressed by,

![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/EQ_10_9_1_12.JPG) |   
---|---  
  
  
The parameter ![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/Lamda.jpg) in Equation 1 is related to the supersaturation ( ![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/OMEGA_s.jpg) ) by the following expression:

![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/EQ_10_9_1_13.JPG) |   
---|---  
  
  
In each calculation step, the supersaturation ( ![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/OMEGA_s.jpg) ) is determined as,

![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/EQ_10_9_1_14.JPG) |   
---|---  
  
Here, ![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/Cm.jpg) ,![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/Ci.jpg) and ![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/Cp.jpg) represent the compositions of the matrix far from the matrix-particle interface, the matrix at the matrix-particle interface, and the particle at the matrix- particle interface respectively. For a diffusion-controlled reaction, ![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/Ci.jpg) and ![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/Cp.jpg) correspond to the equilibrium matrix and particle compositions respectively and they were obtained from the phase diagram. ![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/Cm.jpg) considers the effect of soft impingement on the “far-field” matrix composition, and is calculated by the usual approximation derived from a mass balance:

![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/EQ_10_9_1_15.JPG) |   
---|---  
  
  
The input parameters of MEDC model include the beta approach curves (showing the volume fraction of beta as a function of temperature), the equilibrium chemical compositions of alpha and beta phases, and diffusivity as a function of temperature, solution temperature / initial volume fraction of alpha phase, initial alpha particle radius, and cooling rates. The initial volume fraction of primary alpha (![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/fao.jpg)) is automatically computed based on the provided beta approach curve in terms of the solution temperature (the starting temperature of the cooling process). The initial particle size (![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/Rao.jpg)) is determined by user, generally based on the experimental data. The evolution of primary alpha volume fraction and the size are computed based on the local cooling rate during DEFORM heat transfer simulation.  
If secondary alpha lath thickening model is defined, MEDC model is automatically coupled with secondary alpha growth model. The growth of primary alpha is terminated by the starting growth of secondary alpha.  
  
For MEDC model definition window see below Fig. 10.9.1.9.

![](../../../../assets/Images/Pre-Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/10_9_1_Image009.jpg)

MEDC kinetic transformation model definition windows

  * **Secondary alpha lath**

A fast acting model is developed to predict the thickening kinetics of secondary alpha lath. Considering the soft impingement between the adjacent advancing laths, the thickening kinetics of a secondary alpha in a colony structure can be expressed as:

![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/EQ_10_9_1_16.JPG) |   
---|---  
  
  
The alpha equilibrium disolving temperature is assumed to be 980°C.

The CCT curve to describe the secondary alpha starting temperatures under various cooling rates is fitted by a fifth order polynomial equation:

![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/EQ_10_9_1_17.JPG) |   
---|---  
  
  
See the below Fig. 10.9.1.10. for Secondary alpha lath general model definition window.

![](../../../../assets/Images/Pre-Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/10_9_1_Image010.jpg)

Secondary alpha lath general kinetic transformation model definition window

  * **Secondary alpha lath - Based on critical cooling rate**

  * **Ti-beta to grain boundary alpha**

A fast acting model is developed to predict the thickening kinetics of grain boundary alpha in Ti-6Al-4V. It is assumed that a layer of grain boundary alpha of negligible thickness develops right after the temperature drops below the beta transus. During further cooling or isothermal holding, grain boundary alpha continues to grow until the sideplate alpha starts to develop. Therefore, this type of transformation is generally coupled with Type 12 (Ti-beta to sideplate alpha). The thickening kinetics of grain boundary can be described as,

![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/EQ_10_9_1_18.JPG) |   
---|---  
  
  
The CCT curves to describe the grain boundary alpha starting temperature ( ![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/Tu.jpg)) and sideplate starting temperature (![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/Tl.jpg) ) under various cooling rates are fitted by a fifth order polynomial equation as follows:

![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/EQ_10_9_1_19.JPG) |   
---|---  
  
  
See the below Fig. 10.9.1.11. for Ti-beta to grain boundary alpha model definition window.

![](../../../../assets/Images/Pre-Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/10_9_1_Image011.jpg)

Ti-beta to grain boundary alpha kinetic transformation model definition window

  * **Ti-beta to side plate alpha**

A fast acting model is developed to predict the thickening kinetics of side plate alpha in Ti-6Al-4V. It is assumed that the sideplate alpha starts to develop when the growth of grain boundary alpha stops. Therefore, this type of transformation is coupled with Type 11 (Ti-beta to grain boundary alpha). Considering the soft impingement between the adjacent advancing plates, the thickening kinetics of a can be described as,

![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/EQ_10_9_1_20.JPG) |   
---|---  
  
![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/EQ_10_9_1_21.jpg) |   
---|---  
  
  
The two CCT curves describing the starting temperature of grain boundary alpha (![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/Tu.jpg)) and that of side plate (![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/Tl.jpg)) under various cooling rates are fitted by a fifth order polynomial equation as follows:

![](../../../../assets/Equations/Pre_Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/EQ_10_9_1_19.JPG) |   
---|---  
  
See the below Fig. 10.9.1.12. for Ti-beta to side plate alpha model definition window.

![](../../../../assets/Images/Pre-Processor/10_Material_Data/10_9_Transformation_Data/10_9_1_Transformation_Kinematic_Models/10_9_1_Image012.jpg)

Ti-beta to side plate alpha kinetic transformation model definition window

  * **Solid/Liquid phase transformation**

  * **Diffusion(Solubility curve)**

  * **Ni gamma prime precipitation model**

  * **Ni gamma prime dissolution model**

  * **User routine**

This model is set to required user routine number. Please refer Chapter 56. [USER ROUTINE](/docs/sk/User_Routines/User_routine_MainPg/) for further details.

**Related Topics:**

[Assigning Material to Object in Pre-Processor](../../../Operation_Templates/33_Forming/33_1_2D_Forming_Setup.htm#Fig_33_1_5_Add_material_from_Material_List_window)

[Deform Units](/docs/sk/About_DEFORM/1_Introduction_to_DEFORM/1_9_Units/)

[Material Editing in MO Lab](/docs/sk/Labs/Heat_Treatment_Labs/2D_HT_Lab5_Material_Input/)

[TTT Calculation Lab](/docs/sk/Labs/Material_Suite_labs/Material_Parameters_Fitting_labs/TTT_Calculation_Lab/)

[Material- Grain Models](/docs/sk/pre_processor/10_material_data/10_6_Grain_Data/10_6_Grain_Data/)

[Material-Fracture models](/docs/sk/pre_processor/10_material_data/10_12_Miscellaneous_Data/10_12_1_Fracture_Models/)

[Heat Treatment Labs](/docs/sk/Labs/Heat_Treatment_Labs/Heat_Treatment_Labs_Main_Pg/)

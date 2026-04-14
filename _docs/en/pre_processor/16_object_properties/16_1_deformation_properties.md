---
lang: en
title: "16.1. Deformation_Properties"
---

# 16.1. Deformation Properties

16.1.1. Creep calculation

16.1.2. Elasto-plastic initial guess

16.1.3. Target Volume

16.1.4. Volume penalty constant

16.1.5. Average strain rate

16.1.6. Limiting strain rate

[16.1.7. Generalized plane strain control](/docs/en/pre_processor/16_object_properties/16_7_symmetry_properties/)

16.1.8. Update Controls

![](../../../assets/Images/Pre-Processor/16_Object_Properties/16_Image001.jpg)

2D Object Properties window

![](../../../assets/Images/Pre-Processor/16_Object_Properties/16_Image002.jpg)

3D Object Properties window

## Creep calculation

Activates creep calculations ([CREEP](/docs/en/Keyword_Documentation/C/CREEP/)) for a particular object. For more information on available creep models, refer to section [10.1.2. Creep](/docs/en/pre_processor/10_Material_Data/10_1_Plastic_Data/10_1_2_Creep/10_1_2_Creep_Models/) (CREEP).

  
If the user would like to see the Creep strain in post processor then Creep check box in "Simulation controls![](../../../assets/Icons/Pre_icons/arrow_front.jpg) Advanced ![](../../../assets/Icons/Pre_icons/arrow_front.jpg) Output controls" path should be activated.

**Text to added related to new creep options**

## Elasto-plastic initial guess (ELPSOL) [2D, 3D]

The convergence of an Elasto-plastic solution ([ELPSOL](/docs/en/Keyword_Documentation/E/ELPSOL/)) is dependent on the initial guess of the stress-strain state. Three initial guess solutions are available:

  * **Plastic solution** : Uses the purely plastic deformation data to generate the initial guess.
  * **Elastic solution** : Uses the purely elastic deformation data to generate the initial guess.
  * **Previous step solution** : Uses the Elasto-plastic solution from the previous step to generate the initial guess.

The previous step solution seems to give the best convergence in most cases. If convergence  
is poor for a particular problem, the elastic or plastic solution can be used.

## Target Volume (TRGVOL) [2D, 3D]

Maintaining volume of the deforming object in the simulation is very important for accurate model predictions. Good mesh size and finer time step alone cannot ensure volume constancy for some class of the simulations. The user can now activate volume compensation under "Properties" option (See Fig. 16.1.1. and Fig. 16.1.2.)

  
You can turn on "Activate Target Volume Options" ([TRGVOL](/docs/en/Keyword_Documentation/T/TRGVOL/)) and then use ![](../../../assets/Icons/Pre_icons/MO_Target_volume_icon.jpg) to automatically calculate the volume. If the volume compensation is turned on then while running simulation the volume of the mesh will be compensated to the value mentioned.

  
There are several causes of volume loss in finite element analysis.

  * The penalty formulation used by DEFORM will naturally loose a fractional percentage of volume at each step. This is normal and generally not a significant cause of concern.

  * If a large time step is used and sub stepping is disabled, when contact occurs nodes will penetrate slave surfaces, then be repositioned at the end of the step. This repositioning can cause slight volume loss. Over the course of a simulation, this can become significant.

  * As elements of slave objects stretch around corners of master objects, the elements will cut the corner of the object. The volume which crosses the corner will be lost on remeshing. This phenomenon can be limited by the use of small elements around corners.

  
The system provides several controls to minimize this volume loss during the simulation.(See Fig. 16.1.1. and Fig. 16.1.2..) Typical volume compensation can be activated to maintain or restore part volume during remeshing. The target volume should be set to the initial part volume. This value can be obtained from the volume icon on the Meshing/Remeshing window.

  
For porous materials, the volume is expected to change throughout the simulation. If volume compensation is activated, the current part volume will be maintained during remeshing.

For certain geometries with large free surfaces, volume compensation can cause distortion.

If this distortion is unacceptable, the best alternative is to use a fine mesh, and set polygon length sub stepping to a small value. Frequent forced remeshing may be useful if element stretching around corners is a problem.

## Volume penalty constant (PENVOL) [2D, 3D]

The volume penalty constant ([PENVOL](/docs/en/Keyword_Documentation/P/PENVOL/)) specifies a large positive value that is used to enforce volume constancy of plastic objects. The default value of 106 is adequate for most simulations. If the value is too small, unacceptably large volume losses may occur. If the value is too large, the solution may have difficulty converging.

## Average strain rate (AVGSTR) [2D, 3D]

The average strain rate ([AVGSTR](/docs/en/Keyword_Documentation/A/AVGSTR/)) is a characteristic average value of the effective strain rate. An approximation of this value should be given at the start of the simulation. A reasonable approximation can be obtained from:

![](../../../assets/Equations/Pre_Processor/16_Object_Properties/EQ_16_1_1.jpg) |   
---|---  
  
## Limiting strain rate (LMTSTR) [2D, 3D]

The limiting strain rate ([LMTSTR](/docs/en/Keyword_Documentation/L/LMTSTR/)) defines a limiting value of effective strain rate below which a plastic or porous material is considered rigid and behaves as Newtonian fluid like material. The stress-strain-rate relationship in the rigid region is approximated by,

![](../../../assets/Equations/Pre_Processor/16_Object_Properties/EQ_16_1_2.jpg) |   
---|---  
  
DEFORM automatically maintains the ratio between average strain rate and limiting strain rate. Generally, the value of limiting strain rate should be 0.1% to 1.0% of the average strain rate.

If the limiting strain rate is too small, the solution may have difficulty converging. If it is too large, the accuracy of the solution will be degraded. If the problem is not converging, the limiting strain rate can be increased for 2 or 3 steps, then returned to the original value.

## Generalized plane strain control (ZSTR) [2D]

Generalized plane strain control ([ZSTR](/docs/en/Keyword_Documentation/Z/ZSTR/)) allows certain object to have thickness direction deformation for plane strain element. The thickness direction deformation can be controlled either by prescribed velocity or by traction in thickness direction. This option is available for Elasto-plastic material with both velocity and traction control and for rigid plastic material with velocity control only.

The object lies between two bounding planes which may move as rigid bodies with respect each other, thus causing strain of the thickness direction of the object. Let P0(X0, Y0) be a fixed point in the reference planes. The length between P0 and its image in the other plane P1 is t0 + DuZ , where t0 is the initial thickness and DuZ is change in length in thickness.

![](../../../assets/Equations/Pre_Processor/16_Object_Properties/EQ_16_1_3.jpg) |   
---|---  
  
In this definition the plane is only allowed to move parallel to the reference plane, therefore all the points in the object will have same thickness strain.

**Z Rate [2D]** :

This is applied usually for plain strain and sheet metal problems. The z strain rate is the rate of out of plane material flow.

This is defined as the ratio of total strain (natural log of reduction in cross sectional area) to process time. This specifies constant strain rate in the z-directions.

## Update Controls [3D]

**Related Topics:**

[16\. Object properties](/docs/en/pre_processor/16_object_properties/16_object_properties/)

[16.2. Thermal properties](/docs/en/pre_processor/16_object_properties/16_2_thermal_properties/)

[16.3. Reference](/docs/en/pre_processor/16_object_properties/16_3_Reference/)

[16.4. Fracture Properties](/docs/en/pre_processor/16_object_properties/16_4_Fracture_properties/)

[16.5. Hardness Properties](/docs/en/pre_processor/16_object_properties/16_5_hardness_properties/)

[16.6. Heating Properties](/docs/en/pre_processor/16_object_properties/16_6_heating_properties/)

[16.7. Symmetry Properties](/docs/en/pre_processor/16_object_properties/16_7_symmetry_properties/)

[16.8. Body Force](/docs/en/pre_processor/16_object_properties/16_8_body_force/)

[16.9. RSE](/docs/en/pre_processor/16_object_properties/16_9_rse/)

[16.10. User](/docs/en/pre_processor/16_object_properties/16_10_user/)

[Selecting the Creep strain from simulation output controls](../9_Simulation_Controls/9_7_Advanced_Options.htm#9.7.4._Output_Control)

[Material Creep models](/docs/en/pre_processor/10_Material_Data/10_1_Plastic_Data/10_1_2_Creep/10_1_2_Creep_Models/)

[Object type selection from object data definition window](../11_General_Object_Data_Definition/11_General_Object_Data_Definition.htm#11.4._Object_type)

[Remeshing-2D Settings](../13_Mesh_Generation/13_1_2D_Mesh_Generation.htm#13.1.8._Remeshing_criteria)  
[Remeshing-3D Settings](../13_Mesh_Generation/13_2_3D_Tet_Mesh_Generation.htm#13.2.8._Remeshing_criteria)

---
lang: en
title: "11. General Object Data Definition"
---

# 11\. General Object Data Definition

11.1. Objects list page

11.2. Object name

11.3. Object initial conditions

11.4. Object type

11.4.1. Plastic

11.4.2. Elastic

11.4.3. Elasto-plastic

11.4.4. Porous

11.4.5. Rigid

11.4.6. Hyper-Elastic 

11.4.7. User-Defined

11.4.8. Environment (Fluid(CFD))

11.4.9. Environment (Air(Electro-magnetic))

11.5. Primary Die

11.6. Import object from file

11.7. Import object from library

11.8. Save object to a file

11.9. Save object to library

The Object Tree in the Pre-processor shows all the currently available objects. (See Fig. 11.1.) The available objects data can be controlled by selecting specific data page under the object in the Object Tree. Once an object data page is selected, than in object data definition window contains the respective selected data such as the geometry, mesh, Material, boundary conditions, movement, initial conditions, and object specific numerical properties of the object.

![]({{ '/assets/images/pre-processor/11_object_general_definition/11_image001.jpg' | relative_url }})

Pre-processor with the object tree window with a red box

## Objects list page

![]({{ '/assets/images/pre-processor/11_object_general_definition/11_image002.jpg' | relative_url }})

Object list page

To add an object to the object tree, click on the ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) button as shown in Fig. 11.2. This will insert a new object into the first available object number. To delete an object, select the appropriate object and press the ![]({{ '/assets/icons/pre_icons/mo_delete_object_button.jpg' | relative_url }}) button. This will delete all entries associated with the selected object, including movement controls, boundary conditions, inter-object boundary conditions, etc.

User can duplicate an existing object by selecting it and clicking on ![]({{ '/assets/icons/pre_icons/mo_duplicate_object_button.jpg' | relative_url }}).

The object position in the tree can be changed using ![]({{ '/assets/icons/pre_icons/mo_move_object_down_button.jpg' | relative_url }}) ![]({{ '/assets/icons/pre_icons/mo_move_object_up_button.jpg' | relative_url }}) buttons.

User can import the object from a keyfile or database using ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}), the objects are appended to the existing object list.

Note: To replace an object geometry definition without deleting movement controls and inter-object relationships, it is possible to delete only the object geometry from the geometry window. This is useful for changing die geometries when performing two or more deformation operations on the same work piece. When redefining an object in this manner, it is extremely important to initialize and regenerate inter-object boundary conditions. It may also be necessary to reset the stroke definition in Movement controls to zero.

## Object name (OBJNAM)

The workpiece and each piece of tooling must be identified as a unique object and assigned an object number and name. (See Fig. 11.3.) The object name ([OBJNAM](/docs/en/keyword_documentation/o/objnam/)) is a string of up to 64 characters. It is highly recommended that it be set to something meaningful (e.g. punch, die, workpiece).

![]({{ '/assets/images/pre-processor/11_object_general_definition/11_image003.jpg' | relative_url }})

3D Object Data Definition window

## Object initial conditions

Initial conditions can be specified for any object related state variable in DEFORM. The most common initial condition specification is object temperature which can be specified in the respective object page.

For heat treatment problems with variable carbon content in the workpiece, dominant atom content may also be specified. For meshed objects, initial object temperature and initial dominant atom content are specified by assigning values to all the nodes by selecting the Object ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) object Nodes icon (![]({{ '/assets/icons/pre_icons/mo_nodal_data_icon.jpg' | relative_url }}))![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Diffusion tab.  
When a mesh is generated nodes and elements state variables will have their values initialized respectively based on the conditions defined for the object.  
Uniform object temperature can be specified in respective object window. Nodal values may also be specified by selecting the Object ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Object Nodes icon (![]({{ '/assets/icons/pre_icons/mo_nodal_data_icon.jpg' | relative_url }}))![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Thermal tab. Values for an entire object can be set using the initialize ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}) icon next to the appropriate data field.  
For non-meshed rigid tools, a constant object temperature may be set using the reference temperature ( [REFTMP](/docs/en/keyword_documentation/r/reftmp/)) under the [Objects Properties.](/docs/en/pre_processor/16_object_properties/16_object_properties/)

Note:  
Using this approximation will tend to over-estimate temperature loss as the die surface will not heat up during the simulation. This effect can be compensated for by reducing the inter-object heat transfer coefficient ([IHTCOF](/docs/en/keyword_documentation/i/ihtcof/)).

  
For porous object relative density must be specified as described in porous object type using the Assign density button. This initializes the relative density value for all the elements by the value defined. Using the Element data values we can specify the Objects ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Object Element icon (![]({{ '/assets/icons/pre_icons/mo_elemental_data_icon.jpg' | relative_url }}) ) ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Deformation ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) General tab.  
For any object defined as a mixture, the initial volume fraction ([VOLFC](/docs/en/keyword_documentation/v/volfc/)) and maximum volume fraction transformed ([VOLFS](/docs/en/keyword_documentation/v/volfs/)) must be assigned for all volume fractions. In general [VOLFC](/docs/en/keyword_documentation/v/volfc/) and [VOLFS](/docs/en/keyword_documentation/v/volfs/) should be initialized to the same value. The volume fraction can be defined by selecting the Object ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Objects Element icon (![]({{ '/assets/icons/pre_icons/mo_elemental_data_icon.jpg' | relative_url }})) ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) Transformation tab.

## Object type (OBJTYP)

The object type ([OBJTYP](/docs/en/keyword_documentation/o/objtyp/)) defines if and how deformation is modelled for each individual object in a DEFORM problem. 

Below are the different object type available in DEFORM: 

11.4.1. Plastc

11.4.2. Elastic

11.4.3. Elasto-plastic

11.4.4. Porous

11.4.5. Rigid

11.4.6. Hyper-Elastic

11.4.7. User-Defined

11.4.8. Environment (Fluid(CFD))

11.4.9. Environment (Air(Electro-magnetic))

### Plastic [2D, 3D]

Plastic objects are modelled as rigid-plastic or rigid-viscoplastic material depending on characteristics of materials. The formulation assumes that the material stress increases linearly with strain rate until a threshold strain rate, referred to as the limiting strain rate ([LMTSTR](/docs/en/keyword_documentation/l/lmtstr/)). The material deforms plastically beyond the limiting strain rate. The plastic material behaviour of the object is specified with a material flow stress function or flow stress data ([FSTRES](/docs/en/keyword_documentation/f/fstres/)).  
  
**Applications:**  
When used to model workpiece, provides very good simulation of real material behavior. Accurately captures strain rate sensitivity.  
  
**Limitations:**  
Does not model elastic recovery (spring back) and is therefore inappropriate for bending or other operations where spring back has a significant effect on the final part geometry. Does not model strains due to thermal expansion / contraction. Cannot capture residual stresses.

### Elastic [2D, 3D]

The elastic material behaviour is specified with Young's modulus ([YOUNG](/docs/en/keyword_documentation/y/young/)) and Poisson's ratio ([POISON](/docs/en/keyword_documentation/p/poison/)). Elastic objects are used if the knowledge of the tooling stress and deflection are important throughout the process. If maximum stress or deflection information is required for die stress, it is recommended that rigid dies be used for the deformation simulation, then a single step die stress simulation be used.  
Refer to the die stress 3D - [3D Die stress setup](/docs/en/operation_templates/30_die_stress/30_2_3d_die_stress_setup/) , 2D-  [2D Die Stress Analysis Theory](/docs/en/operation_templates/30_die_stress/2d_die_stress_analysis_theory/) and [Die Stress study](/docs/en/labs/die_stess_study_labs/die_stess_labs_across_single_steps_main_pg/) [ labs](/docs/en/labs/die_stess_study_labs/die_stess_labs_across_single_steps_main_pg/) in the online help for more information. For 3D at this time a fully coupled elastic tool with plastic workpiece analysis is required, to be recommended to use coupled die stress analysis as explained in [Coupled Die stress Analysis](/docs/en/operation_templates/30_die_stress/coupled_die_stress_analysis/).  
  
**Applications:**  
When used to model tooling, the elastic model can provide information on tool stress and deflection. Useful in rare situations when tooling deflection can have a significant influence on the shape of the part.  
**  
Limitations:**  
If yield stress for the tooling is exceeded, stress and deflection results will be incorrect. However, in most cases, if tooling yield stress is exceeded, this represents an unacceptable situation, and tooling deformation beyond yield is not useful. It is good practice to check stresses in simulations with elastic tooling to ensure that this situation is not violated.

### Elasto-plastic (Ela-Pla) [2D, 3D]

Elasto-plastic objects are treated as elastic objects until the yield point is reached.  
Then, any portions of the object that reach the yield point are treated as plastic, while the remainder of the object is treated as elastic. In the Elasto-plastic deformation the total strain in the object is a combination of elastic strain and non-elastic strain. The non-elastic strain consists of plastic strain, creep strain, thermal strain and transformation strain depending on the characteristics of materials. For more details related to material model refer the Chapter [10\. Material Data](/docs/en/pre_processor/10_material_data/10_material_data/). In the case of brick elements, the Elasto-plastic model is valid for all levels of strain.

Three element formulations are available for the elasto-plastic object type.

  * Standard – Default setting. Recommended for most applications.
  * Mixed (Tet mesh) – Suitable for heat treat simulations involving small deformation.
  * Assumed strain (Brick mesh) – Suitable for brick meshed models with only 1-2 layers of elements through the thickness.

**Assumed strain (Brick mesh)**

The "**Assumed strain** " setting should be activated in elasto-plastic sheet metal forming models that are limited to only 1-2 layers of brick elements though the sheet thickness. This setting helps to avoid a possible numerical shear locking by adopting the assumed transverse shear strain field. The "Assumed strain" setting is not necessary if the sheet metal object has 3 or more layers of brick elements through the thickness.

  
**Applications:**  
Provides a realistic simulation of elastic recovery (spring back), and strains due to the thermal expansion. Useful for problems such as bending where spring back has a significant effect on the final part geometry. Also useful for residual stress calculations. This object type can also handle strain rate sensitive materials. Object type must be elastic-plastic for creep calculations.  
  
**Limitations:**  
Generally, takes long solution time, convergence behaviour is greatly influence by material data defined for the initial yield conditions and the contact conditions of the deforming objects.  
  
**Note:** If flow stress is defined for multiple strain rates, the flow stress of an Elasto-plastic material is evaluated at the strain rate value specified in limiting strain rate under object->properties.

### Porous [2D, 3D]

Porous objects are treated the same as plastic objects (compressible rigid-viscoplastic materials) except that the material density is calculated and updated as part of the simulation. The material behavior is modelled similar to plastic objects but the model includes the compressibility of the material in the formulation. The limiting strain rate ([LMTSTR](/docs/en/keyword_documentation/l/lmtstr/)) and the flow stress ([FSTRES](/docs/en/keyword_documentation/f/fstres/)) must be specified at the fully dense state. The material density is specified at each element ([DENSTY](/docs/en/keyword_documentation/d/densty/)). Objects with changing material densities such as materials used in powder forming, should be modelled as Porous objects. The only iteration method currently available for the porous material is the direct solution method. This method does not have fast convergence capabilities, subsequently a porous simulation may take longer than a comparable plastic simulation.

For the sintering material models available in DEFORM refer [10.12.7. Sintering Driving Force Model.](../10_material_data/10_12_miscellaneous_data/10_12_miscellaneous_data.htm#10.12.7._Sintering_Driving_Force_model)

From v14.0, user can model the elastic behavior of porous materials by selecting the Elasto-plastic option from the Porous object type options as shown in Fig. 11.4.

![]({{ '/assets/images/pre-processor/11_object_general_definition/11_image004.jpg' | relative_url }})

Porous object type option

  
  
  
**Applications**  
Appropriate for compacted, sintered powders, beyond around 70 /accurately models consolidation and densification during forging.  
  
**Limitations**  
Is not designed to model loose powder compaction processes.

### Rigid [2D, 3D]

Rigid objects are modelled as non-deformable materials. In the deformation analysis, the object is represented by the geometric profile ([DIEGEO](/docs/en/keyword_documentation/d/diegeo/)). Deformation solution data available for rigid objects include object stroke, load, and velocity. The mesh for the rigid object is used only for thermal, transformation, and diffusion calculations.  
  
**Applications:**  
When used to model tooling, increases simulation speed (over elastic tooling) by reducing the number of deformable objects, and hence the number of equations which must be solved. Negligible loss of accuracy for typical simulations where the tools have a much higher yield stress than the workpiece.  
  
**Limitations:**  
Stress and deflection data for the dies is not available during deformation. This data can be obtained at selected single steps by performing a single step die stress analysis.

### Hyperelastic [2D,3D]

A hyperelastic material behaviour is specified with the hyperelastic ([HYPREL](/docs/en/keyword_documentation/h/hyprel/)) object type. A hyperelastic material is a type of constitutive model for ideally elastic material for which the stress-strain relationship derives from a strain energy density function. Hyperelastic objects are used for applications like rubber pad forming and when deforming certain polymer objects. User can select this option if the object type is hyper-elastic. In DEFORM, Neo-Hookean and Mooney-Rivlin are the two hyperelastic constitutive models provided to simulate hyperelasticity.  
  
**Applications**  
Rubber pad forming, deforming certain polymer objects, etc.  
  
**Limitations**  
Not available for 2D plane stress

### User Defined [2D] [3D]

User has been provided an option to customize the material behavior. Users can customize the material behavior using [usr_mat.f.](../../user_routines/56_user_routines_in_deform/56_2_2d_user_defined_fem_routines.htm#56_2_3_5_User_defined_material_models_\(USRMAT\)) by defining a unique constitutive model. Only one object with such definition is allowed, hence no need to pass any routine number. Users can model the elasto-plastic or rigid-plastic behavior and can select the respective option from the User Defined object type options as shown in Fig. 11.5. , Elasto-plastic for Elasto-plastic and Plastic for rigid-plastic. SP solver is suggested for user-defined elasto-plastic problems. From v12, this implementation replaces the UMAT.DAT function in previous versions.

![]({{ '/assets/images/pre-processor/11_object_general_definition/11_image005.jpg' | relative_url }})

User-defined object type

### Environment [Fluid(CFD)] [2D, 3D]

Users can define the Fluid environment using Environment (Fluid(CFD)) object type as shown in Fig. 11.6. This option will be available when user turns on the “CFD flow” simulation type from the Simulation controls page.

![]({{ '/assets/images/pre-processor/11_object_general_definition/11_image006.jpg' | relative_url }})

Environment Fluid(CFD) type object selection

### Environment [Air(Electro-magnetic)] [2D, 3D]

Air in Induction type electro-magnetic problems can be modeled using the Environment (Air(Electro-magnetic)) object type as shown in Fig. 11.7. This option is available to the users when the Induction type of Heating is selected under Heat Transfer in Simulation controls page.

![]({{ '/assets/images/pre-processor/11_object_general_definition/11_image007.jpg' | relative_url }})

Environment Air(Electro-magnetic) type object selection

### User Defined (Plastic) [2D] [3D]

User has been provided with an option to customize the plastic material behaviour. User can customize the material behaviour using [usr_mat.f.](../../user_routines/56_user_routines_in_deform/56_2_2d_user_defined_fem_routines.htm#User_Defined_\(Plastic\)) by defining an unique constitutive model. Only one object with such definition is allowed hence no need to pass any routine number. This object type can be used to simulate rigid-plastic material model. From v12 this new implementation replace the UMAT.DAT function in previous versions. In current v12 DEFORM, SP solver is suggested for user-defined elasto-plastic object problems.

## Primary Die (PDIE)

The primary die ([PDIE](/docs/en/keyword_documentation/p/pdie/)) specifies the primary object for the simulation. The primary object is usually assigned to the object most closely controlled by the forming machinery.  
For example, the die attached to the ram of a mechanical press would be designated as the primary die. Characteristics of the primary die can be used to control various aspects of a simulation including:

  * Simulation time step size ([DSMAX](/docs/en/keyword_documentation/d/dsmax/))
  * Object movement ([MOVCTL](../../keyword_documentation/m/movctl_\(2d\).htm))
  * Simulation termination criteria ([SMAX](/docs/en/keyword_documentation/s/smax/), [VMIN](/docs/en/keyword_documentation/v/vmin/) and [LMAX](/docs/en/keyword_documentation/l/lmax/))

The primary die is defined in using a check box (See Fig. 11.3.). Only one object can be defined as the primary die.

## **Import object from file**![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) :

User can import object from key file or Database. This import all the object data available in the Keyfile or DB like Geometry, Mesh, BCC, Movement, Material and Nodal and elemental data.

## **Import object from library** ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}):

User can import object from user library.

## **Save object to a file** ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}) :

User can save the object in key file format. This saved file can be imported back by ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) using import object option in any other deform problem setup.

## **Save object to library**![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}) :

User can save the object data to library and saved file can be imported back by using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) import object option in any other deform problem setup.

**Related Topics:**

[9\. Simulation Controls](/docs/en/pre_processor/9_simulation_controls/9_simulation_controls/)

[10\. Material Properties](/docs/en/pre_processor/10_material_data/10_material_data/)

[12\. Geometry Modelling](/docs/en/pre_processor/12_geometry_modelling/12_geometry_modelling/)

[13\. Mesh Generation](/docs/en/pre_processor/13_mesh_generation/13_mesh_generation/)

[14\. Boundary Conditions](/docs/en/pre_processor/14_boundary_conditions/14_boundary_conditions/)

[15\. Movement Controls Settings](/docs/en/pre_processor/15_movement_controls_definition/15_movement_controls_settings/)

[16\. Object Properties](/docs/en/pre_processor/16_object_properties/16_object_properties/)

[17\. Object Data Initialize](/docs/en/pre_processor/17_object_data_initialization/17_object_data_initialize/)

[18\. Advanced Object Data Definition](/docs/en/pre_processor/18_object_manipulation_tools/18_object_manipulation_tools/)

[19\. Object positioning](/docs/en/pre_processor/19_object_positioning/19_object_positioning/)

[20\. Inter-Object Definition](/docs/en/pre_processor/20_inter-object_data_definition/20_inter-object_data_definition/)

[21\. Database Generation](/docs/en/pre_processor/21_database_generation/21_database_generation/)

[22\. Convert 2D to 3D](/docs/en/pre_processor/22_convert_2d_to_3d/22_convert_2d_to_3d/)

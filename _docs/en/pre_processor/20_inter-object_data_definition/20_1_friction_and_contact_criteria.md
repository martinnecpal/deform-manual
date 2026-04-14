---
lang: en
title: "20.1. Friction and Contact criteria"
---

# 20.1. Friction and Contact criteria

20.1.1. Friction (FRCFAC)

  * Constant Shear (sticking)

  * Coulomb (sliding)

  * Hybrid

  * Tau (shear stress)

20.1.2. Anisotropic

20.1.3. Contact Criteria

20.1.4. Seperation Type

  * Separation Density

  * Separable

  * Non-separable

  * Adaptive contact BCC option

20.1.5. Separation Criteria

20.1.6. Friction Window

## Friction (FRCFAC) [2D, 3D]

The Friction coefficient ([FRCFAC](/docs/en/keyword_documentation/f/frcfac/)) specifies the friction at the interface between two objects. The friction coefficient may be specified as a constant, a function of time, temperature, pressure, pressure temperature surface stretch, pressure dependent, strain rate, and sliding velocity or user routine (See Fig. 20.1.1.).

The friction types allowed are Shear, Coulomb, Hybrid and Constant Tau. Constant Tau is available only in 2D.

![]({{ '/assets/images/pre-processor/20_inter-object_data_definition/20_1_friction_and_contact_criteria/20_1_image001.jpg' | relative_url }})

Inter Object Shear friction function options

**Constant Shear (sticking)** [2D, 3D]  
Constant shear friction is used mostly for bulk-forming simulations. The frictional force in the constant shear definition is defined by,

![]({{ '/assets/equations/pre_processor/20_inter-object_data_definition/eq_20_1_1.jpg' | relative_url }}) |   
---|---  
  
This states that the friction is a function of the yield stress of the deforming body.

**Coulomb (sliding)** [2D, 3D]  
Coulomb friction is used when contact occurs between two elastically deforming objects (could include an elastic-plastic object, if it is deforming elastically), or an elastic object and a rigid object. generally to model sheet forming processes. The frictional force in the coulomb law model is defined by,

![]({{ '/assets/equations/pre_processor/20_inter-object_data_definition/eq_20_1_2.jpg' | relative_url }}) |   
---|---  
  
There must be interfacial pressure between two bodies for frictional force to be present. If two bodies contact each other, however there is no force pressing the bodies together, there will be no resulting friction.

For contact between two plastic or porous objects, the frictional stress is calculated using the flow stress of the slave object.

**Hybrid** [2D, 3D]  
Hybrid is a combination of two friction models that can be applied between two objects in contact due to friction (See Fig. 20.1.2.).

![]({{ '/assets/images/pre-processor/20_inter-object_data_definition/20_1_friction_and_contact_criteria/20_1_image002.jpg' | relative_url }})

Inter Object Hybrid friction window

**Tau (shear stress)** [2D]  
The Tau model of friction lets the user to set the shear stress between two objects in contact due to friction. The user is allowed to set a constant value.

**Common Question** : What is a good value for a friction coefficient?

**Answer** : The lubricant used on the tooling plays a large role in the amount of friction that exists between the tooling and workpiece. The friction in turn affects the metal flow at contact surfaces.

Typical values (using constant shear only):

(0.08-0.1) for cold forming processes

(0.2) for warm forming processes

(0.2 to 0.3) for lubricated hot forming processes

(0.7-0.9) for dry surfaces

Most processes are not extremely sensitive to friction, and the typical values listed above are perfectly adequate. For processes which are very sensitive to lubrication conditions, friction values may be determined by experimentation.

Note:

  * Constant Shear (sticking) friction is used mostly for bulk-forming simulations.

  * Coulomb (sliding) friction is used for sheet metal forming operations since it most closely resembles the type of friction encountered in this process.

  * Tau friction can be used if the user needs to specify the shear stress on a surface.

**Remarks** : Two simple ways of gauging the sensitivity of the process to friction:

  1. Would you expect significant variation in the part depending on whether lubricant is applied well or applied poorly in production? If you would not, then the typical friction values listed above should be adequate.

  2. If you are still unsure, run two DEFORM simulations with, say, a 20 % variation in friction conditions from the typical values. (For lubricated cold forming, you might run one simulation at 0.08 and one simulation at 0.12). Compare the results, such as load versus stroke or final geometry, particularly the parameters you identified as critical. If there is substantial variation, more careful study of friction is warranted. If there is little variation, then the typical values are adequate.

DEFORM offers a variety of definitions to model accurate interaction of deforming work piece with other physical components of the system under varying processing conditions. These include definitions of the friction values as a function of time, interface pressure, interface temperature and surface stretch of the deforming work piece or a combination these. Additional definitions also include explicit models that define friction values as a function of pressure, strain rate and sliding velocity as indicated in the Fig. 20.1.3. to Fig. 20.1.8.

![]({{ '/assets/images/pre-processor/20_inter-object_data_definition/20_1_friction_and_contact_criteria/20_1_image003.jpg' | relative_url }})

Pressure dependent shear friction factor

![]({{ '/assets/images/pre-processor/20_inter-object_data_definition/20_1_friction_and_contact_criteria/20_1_image004.jpg' | relative_url }})

Strain-rate dependent shear friction factor

![]({{ '/assets/images/pre-processor/20_inter-object_data_definition/20_1_friction_and_contact_criteria/20_1_image005.jpg' | relative_url }})

Sliding velocity dependent shear friction factor

![]({{ '/assets/images/pre-processor/20_inter-object_data_definition/20_1_friction_and_contact_criteria/20_1_image006.jpg' | relative_url }})

Pressure dependent coulomb friction factor

![]({{ '/assets/images/pre-processor/20_inter-object_data_definition/20_1_friction_and_contact_criteria/20_1_image007.jpg' | relative_url }})

Strain rate dependent coulomb friction factor

![]({{ '/assets/images/pre-processor/20_inter-object_data_definition/20_1_friction_and_contact_criteria/20_1_image008.jpg' | relative_url }})

Sliding velocity dependent coulomb friction factor

  
**Caution** :

Be careful when using the self-contact condition. If not monitored, a fold might develop and cover itself up during the simulation. The Post-Processor will allow the user to find the folds easily.

Shear, Coulomb and Hybrid friction factor model equations are shown in below Fig. 20.1.9.

![]({{ '/assets/images/pre-processor/20_inter-object_data_definition/20_1_friction_and_contact_criteria/20_1_image009.jpg' | relative_url }})

Coulomb, shear and hybrid friction model equations

_Friction models can be selected on the following conditions_ :

  * **Shear:**

  * Sticking friction

  * Most bulk forming cases

  * Best Convergence

  * **Coulomb:**

  * Sliding friction

  * Lightly supported workpieces in bulk forming

  * Sheet metal forming

  * **Hybrid:**

  * Coulomb law at low pressure

  * Shear law at high pressure

  * Not available in Forming Express

  
Shear and Coulomb friction factor values for few applications are tabulated in below table.

**Application** | **Shear friction factor** | **Coulomb friction factor**  
---|---|---  
Sheet metal forming | 0.08-0.12 | 0.05-0.10  
Cold forming  | 0.08-0.12 | 0.05-0.10  
Warm forging | 0.2-0.3 |   
Glass lubricated hot forging | 0.1-0.2 |   
Graphite/oil lubricated hot forging  | 0.3-0.4 |   
Unlubricated hot forging | 0.7-1.0 |   
Unlubricated extrusion | 0.7-1.0 |   
Rolling | 0.7-1.0 |   
  
## Anisotropic [3D]

The Anisotropic ([FRCFAI](/docs/en/keyword_documentation/f/frcfai/)) option allows the user to define the different friction scaling factor values along each axis, when different scaling factors for each axis are defined then the defined friction value will be scaled according to the scaling factor and applied to respective axis. (See Fig. 20.1.10.)

![]({{ '/assets/images/pre-processor/20_inter-object_data_definition/20_1_friction_and_contact_criteria/20_1_image010.jpg' | relative_url }})

Anisotropic model 

**Contact Tab:**

From DEFORM -V12 Separation criteria options are added under Deformation - Contact tab, additional contact and separation criteria based on distance and geometry has been implemented (See Fig. 20.1.11. (2D) and Fig. 20.1.12. (3D)). Also contact method options are moved to Simulation Controls ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})Advanced ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})[Contact](../9_simulation_controls/9_7_advanced_options.htm#9.7.5._Contact_) tab.

![]({{ '/assets/images/pre-processor/20_inter-object_data_definition/20_1_friction_and_contact_criteria/20_1_image011.jpg' | relative_url }})

2D Contact tab window 

![]({{ '/assets/images/pre-processor/20_inter-object_data_definition/20_1_friction_and_contact_criteria/20_1_image012.jpg' | relative_url }})

3D Contact tab window

## **Contact criteria**

Following options are available under contact criteria to define when a node should be considered as contact node.

  * **System default** : When we use System default method nodal contact, system is going to determine whether the node is a contact node or not.

  * **Absolute distance** : If the node is within the distance specified here from master object then that node is considered as contact node.

  * **(%) of element size** : If the node is within the distance of defined % of nearest slave object element size from master object than that node is considered as contact node.

  * **Contact search within friction window** : When users use this option then the system will look for contact nodes only within the friction window. To use this option, we need to define Friction window and then select this option and the friction coefficient should be defined in the friction window page, not the global friction page.

  * **Select all surface nodes within friction window (only for 3D)** : This option will only be available in 3D and it will be coupled with “Do not update” option under node coordinate update. All surface nodes within friction window will be assigned with contact BCC. Node will separate once it exits the window. The friction coefficient should be defined in the friction window page, not the global friction page.

Under Node coordinate updates list we have:

  * **System update** : System will automatically update the co-ordinates of the contact node once the node is determined as contact node based on the contact criteria to generate contact with master object when we use System update option.

  * **Do not update** : Node co-ordinates will not be updated even though the node is determined as contact node based on the contact criteria to generate contact with master object when we use Do not update option.

## Separation Type

  * **Separation Density****[2D**]: Separation density ([SEPDEN](/docs/en/keyword_documentation/s/sepden/)) is used to model the behavior of porous objects that have not been fully compacted. It defines the separation criterion of contacting nodes involving porous objects. Unless the density of the material is greater than density, nodal separation is not considered.

  * **Separable [3D]:** The separation criteria ([SEPRES](/docs/en/keyword_documentation/s/sepres/)) defines how the nodes at the Inter object interface will behave when acted upon by a tensile force. Three ways of defining the separation criteria exist.

  * **Non-separable [3D]:** The Separation Relation ([SEPRES](/docs/en/keyword_documentation/s/sepres/)) allows nodal contact to be defined as non-separable under any condition. This condition should generally only be used to attach nodes to a rigid symmetry plane when defining symmetry on a plane other than the XY, YZ, or ZX planes.

  * **Adaptive contact BCC option [3D]** : This option will be used in the special contact relationship between two multiple deforming dies. The interface of two deforming dies is mechanically separable but keep the contact BCC so that the no node is allowed to go into the gap between two deforming dies.

## Separation criterion

In Pressure based criteria we have:

  * **System default** : This setting will cause normal separation when the contacting node experiences a tensile force or pressure greater than 0.1.

  * **(%) of flow stress** : This setting will cause nodal separation when the tension on the contact node is greater than a given percentage of flow stress of the slave object. This percentage must be input by the user in the Separation Criteria box.

  * **Absolute pressure:** This setting will cause nodal separation when the tension experienced by the node is greater than the input pressure. This pressure must be indicated in the box marked separation criteria.

In Geometry based criteria we have:

  * **Absolute distance** : Absolute distance: If the distance between the master surface and the node is greater than the distance defined in the absolute distance than the contact with that node is removed.

  * **(%) of element size** : If the distance between the master surface and the node is greater than the % of nearest slave element size than the contact with that node is removed.

  * **Plane based:** A point and normal vector define the location and direction of the plane. Contact will not be allowed on the side of the plane that faces in the normal direction. Contact will be allowed on the side of the plane that faces opposite the normal direction.

## Friction Window

**[2D, 3D]** : Friction windows ([FRCWIN](/docs/en/keyword_documentation/f/frcwin/)) can be applied to a simulation as shown in Fig. 20.1.13. and Fig. 20.1.14. One of the purposes of this function is to allow the user to apply different friction conditions at specified regions of an object to simulate differences in the lubrication condition. Applying a window is done in the same manner as only other window function. In the case of two overlapping windows, the lower order number window takes precedence.

Friction windows allow the user to specify different friction coefficient values for different contact regions of the same object pair. The friction window defines a friction coefficient for the specific area that is defined in the display window. The friction coefficient specifies the friction encountered by any object in contact with the workpiece.

The window defined friction values can also use all the friction model definition available in the system, as explained in the Inter-Object data definition. The friction window can also be defined to follow another object's movement or have its own velocity defined.

![]({{ '/assets/images/pre-processor/20_inter-object_data_definition/20_1_friction_and_contact_criteria/20_1_image013.jpg' | relative_url }})

Inter Object Friction window definition window for 2D 

![]({{ '/assets/images/pre-processor/20_inter-object_data_definition/20_1_friction_and_contact_criteria/20_1_image014.jpg' | relative_url }})

Inter Object Friction window definition window for 3D

Note:

If there is not a friction window assigned for portions of objects that are in contact. The global friction coefficient assigned in the Inter object interface will be used.

**Related Topics:**

[20\. Inter-Object Data Definition]()

[20.2. Interface Thermal Data](/docs/en/pre_processor/20_inter-object_data_definition/20_2_interface_thermal_data/)

[20.3. Interface Resisitivity](/docs/en/pre_processor/20_inter-object_data_definition/20_3_interface_resisitivity/)

[20.4. Tool Wear](/docs/en/pre_processor/20_inter-object_data_definition/20_4_tool_wear/)

[20.5. Rigid Contact](/docs/en/pre_processor/20_inter-object_data_definition/20_5_rigid_contact/)

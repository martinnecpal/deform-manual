---
lang: sk
title: "45.1. Boolean Operator"
---

# 45.1. Boolean Operator

45.1.1. Defining 2D Boolean Operator

45.1.1.1. Add 2D Boolean operation

45.1.1.2. Pass objects for subsequent operations across boolean operator

45.1.1.3. Add objects

45.1.1.4. Define Boolean object

45.1.1.5. Define Cutter object

45.1.1.6. Define Cutter geometry

45.1.1.7. Position cutter

45.1.1.8. Preview Boolean

45.1.1.9. Generate Database

45.1.1.10. Continue with subsequent operation

45.1.1.11. Post processing 2D Boolean results

45.1.2. Defining 3D Boolean operator

45.1.2.1. Add Objects

45.1.2.2. Defining Boolean object

45.1.2.3. Define Cutter object

45.1.2.4. Define Cutter geometry

45.1.2.5. Position cutter

45.1.2.6. Preview Boolean

45.1.2.7. Generate Database

45.1.2.8. Post processing the 3D boolean results

45.1.2.9. Continuing the further operations

## Defining 2D Boolean Operator

Boolean operation normally added as subsequent operation in multiple operations to boolean the unwanted material from the object. 2D Boolean is explained in this manual for extrusion example, so that total extrusion divided into 3 stages and after 1st and 2nd stage outside the interested area of extruded material is booleaned to reduce the computational time of simulation.

Before going to the add the Boolean operation first open the Integrated Manufacturing Process in SI units ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) add 2D Forming operation ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) import the 2D SI Extrusion example **EXTR1_SI.KEY** in guided mode as shown in Fig. 45.1.1. ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) select Step branch from operation tree and set number of steps to 300 ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) and generate DB.

![]({{ '/assets/images/operation_templates/45_boolean_operator/45_1_boolean_operator/image0001.jpg' | relative_url }})

Import and setup 2d extrusion example

### Add 2D Boolean operation

After the 2D operation setup database generation add 2D Boolean operator from MO explorer Simulation operator group as shown in Fig. 45.1.2.

![]({{ '/assets/images/operation_templates/45_boolean_operator/45_1_boolean_operator/image0002.jpg' | relative_url }})

Add 2d Boolean operation

Add another 2D forming operation after 2d Boolean operation as shown in Fig. 45.1.3. to continue the further extrusion taking less simulation computational time.

![]({{ '/assets/images/operation_templates/45_boolean_operator/45_1_boolean_operator/image0003.jpg' | relative_url }})

Add forming operation after Boolean operation

### Pass objects for subsequent operations across Boolean operator

Pass first operation workpiece object to all operations as shown in Fig. 45.1.4., similarly pass remaining objects to all operations. If user is continuing the operations after Boolean with previous objects other than first object then those objects must be passed to Boolean operation before adding objects in Boolean operation.

![]({{ '/assets/images/operation_templates/45_boolean_operator/45_1_boolean_operator/image0004.jpg' | relative_url }})

Passing workpiece object to all operations

After passing all objects in operation editor user can observe the link established for all the three objects across the operations as shown in Fig. 45.1.5. Select the boolean operation in operation editor to open boolean operation as shown in Fig. 45.1.5.

![]({{ '/assets/images/operation_templates/45_boolean_operator/45_1_boolean_operator/image0005.jpg' | relative_url }})

Open Boolean operation

###  Add objects

System automatically selects the workpiece or first object as boolean object as shown in Fig. 45.1.5. For Cutter new object can be added by selecting the Add new object option (See Fig. 45.1.5.) and clicking ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to the object window as shown in Fig. 45.1.6. Any object from previous operation can also be selected as cutter object.

![]({{ '/assets/images/operation_templates/45_boolean_operator/45_1_boolean_operator/image0006.jpg' | relative_url }})

A new object added for Cutter object in operation tree

### Define Boolean object

In Object window (See Fig. 45.1.6. ) no need to change any settings, it gives the details about the object type. For boolean object only Deformation boundary conditions constrains (BCC) and initialize state variable windows will be available, user can change the BCC in schedule before Boolean by checking “Redefine BCC” check box (See Fig. 45.1.7.). For more details on different BCC definition and its definition refer [14\. Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/).

![]({{ '/assets/images/operation_templates/45_boolean_operator/45_1_boolean_operator/image0007.jpg' | relative_url }})

Schedule BCC definition window for boolean object

Similarly state variables can be initialized before Boolean by checking the respective available check boxes as shown in Fig. 45.1.8. For more details on state variables initialization refer [17\. Object Data Initialize](/docs/sk/pre_processor/17_object_data_initialization/17_object_data_initialize/).

![]({{ '/assets/images/operation_templates/45_boolean_operator/45_1_boolean_operator/image0008.jpg' | relative_url }})

Schedule state variables initialize window for Boolean object

In this example no need to change or select any option for Boolean object (workpiece) so select Cutter object to continue setup.

### Define Cutter object

Cutter object can be named and imported from DEFORM previous project DB or Keyword files using Import object from a file ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) and Load object from library ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) options as shown in Fig. 45.1.9.

![]({{ '/assets/images/operation_templates/45_boolean_operator/45_1_boolean_operator/image0009.jpg' | relative_url }})

Cutter object window

### Define Cutter geometry

Simple Cutter geometry can be created from the geometry primitives or 2D geometry editor options as shown in Fig. 45.1.10. Even the 2D geometries can be imported from GEO, IGS and DXF formats. Based on the geometry type of previous operation respective geometry primitives will be available in boolean operation. As cutter object does not need the mesh Extract border from mesh option will not activate.

For more details about the geometry available option refer [12.1. 2D Geometry Data Defining](/docs/sk/pre_processor/12_geometry_modelling/12_1_2d_geometry_data_defining/) and [12.2. 2D Geometry Data Editing](/docs/sk/pre_processor/12_geometry_modelling/12_2_2d_geometry_editing/). In this example we will create 2D geometry using ![]({{ '/assets/icons/pre_icons/mo_edit_lable.jpg' | relative_url }}) option as shown in Fig. 45.1.11.

![]({{ '/assets/images/operation_templates/45_boolean_operator/45_1_boolean_operator/image0010.jpg' | relative_url }})

Cutter geometry definition window

![]({{ '/assets/images/operation_templates/45_boolean_operator/45_1_boolean_operator/image0011.jpg' | relative_url }})

Cutter geometry creating from Edit option

### Position cutter

Cutter can be positioned in exact location by using the positioning options, this can be accessed from ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) button as shown in Fig. 45.1.12.

![]({{ '/assets/images/operation_templates/45_boolean_operator/45_1_boolean_operator/image0012.jpg' | relative_url }})

Object positioning window

### Preview Boolean

Preview Boolean window is provided for future development when this operation supports interactive mode setup to visualize how the booleaned object looks like. This button will be deactivated for the read from DB object type. As this operation currently supports only batch mode, so only Read from DB object will become boolean object hence preview boolean will be deactivated in this mode (See Fig. 45.1.13.).

![]({{ '/assets/images/operation_templates/45_boolean_operator/45_1_boolean_operator/image0013.jpg' | relative_url }})

Preview Boolean window

### Generate Database

User has to generate the database in case if previous operation is simulated, if not database will generate while running after completion of previous operation automatically.(See Fig. 45.1.14.)

**Generate Database :** By clicking on this ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button, it generates the Database for the setup.

**Append Key file:** Any information that is not defined in the wizard but still applicable to the process can be loaded as .key file. This option is also useful in the cases where only few values needs to be changed then those values can be defined as .key file and only .key file can be changed and simulation can be resubmitted.

User can observe the cutter object placed in the extrusion direction so that after first extrusion operation certain out of interest extruded workpiece portion from tip will be booleaned.

![]({{ '/assets/images/operation_templates/45_boolean_operator/45_1_boolean_operator/image0014.jpg' | relative_url }})

Database generation window

### Continue with subsequent operation

After Boolean subsequent operations can be added and continue the setup. In this example further extrusion operation can be setup by opening the third operation and adding default inter-object relations and selecting the total number of steps to 100 and defining the step increment, that is 0.1905mm stroke increment (See Fig. 45.1.15.).

![]({{ '/assets/images/operation_templates/45_boolean_operator/45_1_boolean_operator/image0015.jpg' | relative_url }})

Continue with subsequent operation after Boolean

After this setup to repeat the similar cycle of Booleaning the uninterested area and continuing the extrusion to reduce the computational time user can add the Cycle operation. To add the cycle select Boolean and second forming operation and using right mouse button option select Add cycles as shown in Fig. 45.1.16. Select the number of cycles as 2, so boolean operation repeats twice after the first and second extrusion operations.

![]({{ '/assets/images/operation_templates/45_boolean_operator/45_1_boolean_operator/image0016.jpg' | relative_url }})

Cycling boolean and forming operation

### Post processing 2D Boolean results

After completion of simulation to preform post processing switch to MO post mode by selecting the![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) button as shown in Fig. 45.1.17.

![]({{ '/assets/images/operation_templates/45_boolean_operator/45_1_boolean_operator/image0017.jpg' | relative_url }})

Material flow at boolean previous operation last step

Select the last step of the operation previous to boolean and then select the boolean operation step from step browser as shown in Fig. 45.1.17. and Fig. 45.1.18.

![]({{ '/assets/images/operation_templates/45_boolean_operator/45_1_boolean_operator/image0018.jpg' | relative_url }})

Workpiece object after boolean

## Defining 3D Boolean operator

3D Boolean is explained in this manual for closed die T-shape forging case which is already simulated, now we need to remove the flash material.

We are adding 3D Boolean operator from explorer as shown in Fig. 45.1.19. and follow as mentioned below.

![]({{ '/assets/images/operation_templates/45_boolean_operator/45_1_boolean_operator/image0019.jpg' | relative_url }})

Add 3D boolean operation after previous operation simulation

### Add Objects

Select the boolean operation in operation editor to open boolean operation, system automatically selects the workpiece or first object of previous operation as boolean object and Add New object option for cutter as shown in Fig. 45.1.20.

![]({{ '/assets/images/operation_templates/45_boolean_operator/45_1_boolean_operator/image0020.jpg' | relative_url }})

Adding objects to boolean objects

Clicking ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to the object window will add these objects to operation tree as shown in Fig. 45.1.21. Any object from previous operation passed to the boolean operation can also be selected as cutter object.

![]({{ '/assets/images/operation_templates/45_boolean_operator/45_1_boolean_operator/image0021.jpg' | relative_url }})

A new object added for Cutter object in operation tree

###  Defining Boolean object

In Object window (See Fig. 45.1.21.) no need to change any settings, it gives the details about the object type. For boolean object only Symmetry and Deformation boundary conditions constrains (BCC) and initialize state variable windows will be available, user can change the Advanced BCC in schedule before Boolean by checking “Redefine BCC” check box (See Fig. 45.1.22.). For more details on different BCC definition and its definition refer [14\. Boundary Conditions](/docs/sk/pre_processor/14_boundary_conditions/14_boundary_conditions/).

![]({{ '/assets/images/operation_templates/45_boolean_operator/45_1_boolean_operator/image0022.jpg' | relative_url }})

Schedule BCC definition window for boolean object

Similarly state variables can be initialized before Boolean by checking the respective available check boxes as shown in Fig. 45.1.23. For more details on state variables initialization refer [17\. Object Data Initialize](/docs/sk/pre_processor/17_object_data_initialization/17_object_data_initialize/).

![]({{ '/assets/images/operation_templates/45_boolean_operator/45_1_boolean_operator/image0023.jpg' | relative_url }})

Schedule Initialize window for boolean object

In this example no need to change or select any option for Boolean object (workpiece) so select Cutter object to continue setup. 

### Define Cutter object

Cutter object can be named and imported from DEFORM previous project DB or Keyword files using Import object from a file ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) and Load object from library ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) options as shown in Fig. 45.1.24.

![]({{ '/assets/images/operation_templates/45_boolean_operator/45_1_boolean_operator/image0024.jpg' | relative_url }})

Cutter object window

### Define Cutter geometry

Simple Cutter geometry can be created from the geometry primitives or 3D geometry editor options as shown in Fig. 45.1.25. Even the 3D geometries can be imported from GEO, STL, PDA, NAS and UNV formats. For more details about the geometry available option refer [12.3. 3D Geometry Data Defining ](/docs/sk/pre_processor/12_geometry_modelling/12_3_3d_geometry_data_defining/) In this example we will import the 3D geometry for cutter object.

![]({{ '/assets/images/operation_templates/45_boolean_operator/45_1_boolean_operator/image0025.jpg' | relative_url }})

Cutter geometry definition window

### Position cutter

Cutter can be positioned in exact location by using the positioning options, this can be accessed from ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) button as shown in Fig. 45.1.26.

![]({{ '/assets/images/operation_templates/45_boolean_operator/45_1_boolean_operator/image0026.jpg' | relative_url }})

Cutter object Positioning window

### Preview Boolean

For 3D object, we have two type Boolean method, Geometry based (new method) and Solid mesh based (old method).**** For 3D Object Boolean preview button will be active, when we click on ![]({{ '/assets/icons/pre_icons/mo_preview_boolean_button.jpg' | relative_url }}) we can observe the preview of boolean workpiece as shown in Fig. 45.1.27. and Fig. 45.1.28.

  * **Geometry based (new method)** : Using Geometry based option if we do Boolean operation, it will Perform Boolean and then Local Remeshing as per the defined input. This will generate smooth mesh as shown in Fig. 45.1.27.

![]({{ '/assets/images/operation_templates/45_boolean_operator/45_1_boolean_operator/image0028.jpg' | relative_url }})

Geometry based method Boolean preview

  * **Solid mesh based (old method)** : Using Solid mesh based if we do Boolean operation, it will perform boolean and then generate only Solid mesh, please refer Fig. 45.1.28.

![]({{ '/assets/images/operation_templates/45_boolean_operator/45_1_boolean_operator/image0027.jpg' | relative_url }})

Solid mesh method Boolean preview

For more information related to Boolean option refer [18.1. Boolean](/docs/sk/pre_processor/18_object_manipulation_tools/18_1_boolean/). 

### Generate Database

User has to generate the database in case if previous operation is simulated (see Fig. 45.1.29.), if not database will generate while running after completion of previous operation automatically. In this example as the previous operation is simulated ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button is activated, so click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database.

![]({{ '/assets/images/operation_templates/45_boolean_operator/45_1_boolean_operator/image0029.jpg' | relative_url }})

Database generation window if previous operation is simulated

**Generate Database**![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) : By clicking on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button, it generates the Database for the setup.

**Append Key file:** Any information that is not defined in the wizard but still applicable to the process can be loaded as .key file. This option is also useful in the cases where only few values needs to be changed then those values can be defined as .key file and only .key file can be changed and simulation can be resubmitted.

### Post processing the 3D boolean results

User has to simulate the DB to perform the boolean operation and then switch to MO post mode by selecting the ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) button as shown in Fig. 45.1.30.

![]({{ '/assets/images/operation_templates/45_boolean_operator/45_1_boolean_operator/image0030.jpg' | relative_url }})

Material flow at boolean previous operation last step

Select the last step of the operation previous to boolean and then select the boolean operation step from step browser as shown in Fig. 45.1.30. and Fig. 45.1.31.

![]({{ '/assets/images/operation_templates/45_boolean_operator/45_1_boolean_operator/image0031.jpg' | relative_url }})

Workpiece object after boolean

### Continuing the further operations

User can continue the further operations by adding respective operation from MO pre mode, user will get the booleaned object and other objects which are passed from operation previous to boolean operation (user need to pass object needed after boolean operation into boolean operation setup as explained in 2D boolean operator section 45.1.1.2. Pass objects for subsequent operations across boolean operator).

****

**Related Topics:**

[18.1. Boolean](/docs/sk/pre_processor/18_object_manipulation_tools/18_1_boolean/)

[45\. Introduction to Boolean Operation](/docs/sk/operation_templates/45_boolean_operation/43_introduction_to_boolean_operation/)

---
lang: en
title: "Deformation Texture lab"
---

# Deformation Texture Lab 

1.1 Creating a New problem

1.2. Adding Forming operation

1.3. Simulation controls

1.4. Loading Material from library

1.5 Adding Objects

1.6. Workpiece

1.6.1. Create Workpiece geometry

1.6.2. Workpiece mesh generation

1.6.3. Assign Workpiece material

1.6.4. Workpiece Boundary condition

1.6.5. Workpiece Properties

1.6.6. Defining Elements data

1.7. Top Die

1.7.1. Create Top die geometry

1.7.2. Top die mesh generation

1.7.3. Assign Top die material

1.7.4. Top die Movement

1.8. Positioning objects

1.9. Contact

1.10. Defining Step controls

1.11. Generate Database

1.12. Running Simulation

1.13. Post Processing

1.13.1 Contours of state variables

1.13.2. Point tracking of CPISV

In this lab we will be using double cone profile billet with Crystal plasticity flow stress model to predict the deformation texture. The profile of double-cone sample is shown in below figure. Due to axisymmetry, only a 1/8th of sample will be modeled. User can load the keyword file "Double_Cone_Forging_woTexture.key" from "MANUALS\PDF\DEFORM3D_Texture_Evolution_Lab" folder into the Pre-processor, in which the FEM model is well defined except the basic texture information of each material and the initial values of orientation distribution functions (ODFs). For each material, we will define the basic texture information (refer to Fig. 3DDTL1.6.\- Fig. 3DDTL1.10.) and crystal plasticity (CP) parameters (refer section 1.6.6. Defining Elements data) to complete the setup and run the simulation. After the simulation is completed, the user can load the database into Post-processor and plot Pole figure from the elemental data of the Workpiece. 

![]({{ '/assets/images/applications/55_deformation_texture_lab/image0000.jpg' | relative_url }})

## Creating a New problem

On a Windows machine, go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button, select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** v1x.x from the menu. The DEFORM GUI Main window will appear.

Create a new problem either by selecting **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ****New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in Fig. 3DDTL1.1. Select " **Integrated Manufacturing Process** " radio button and "**SI** " radio button in Unit field. Define Problem Name as "******Double_cone_Deformation_Txr******" and**Title** as "**Deformation texture".** Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/applications/55_deformation_texture_lab/image0001.jpg' | relative_url }})

Problem type selection window

Multiple operation wizard will open with the New Project dialog as shown in Fig. 3DDTL1.2., at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. We will use ‘****Double_cone_Deformation_Txr** **” as the project name and "**Deformation texture** " title in this session. 3D Forming operation can also be added in the "New Project" dialog (see Fig. 3DDTL1.2.), but we will add 3D Forming operation from operations list in Explorer for this lab, so do not check "First operation" check box in "New Project" dialog. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

![]({{ '/assets/images/applications/55_deformation_texture_lab/image0002.jpg' | relative_url }})

Adding 3D Forming Operation in MO Wizard from new Project window.

## Adding Forming operation

Add one 3D Forming operation from the Explorer Operations list. Operation can be added by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button adjacent to 3D Forming in Explorer or user can also add by drag and drop into the Operation Editor (see Fig. 3DDTL1.3.). As we add operation, the Process page will be opened in the properties area.

![]({{ '/assets/images/applications/55_deformation_texture_lab/image0003.jpg' | relative_url }})

Adding 3D Forming Operation from explorer.

## Simulation controls

Switch to Expert mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) button,**** under **Main****settings![]({{ '/assets/icons/pre_icons/mo_main_setting.jpg' | relative_url }})** , Turn on “**Deformation** ”, "**Heat Transfer** " and "**Transformation** "mode check box as shown in Fig. 3DDTL1.4. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to material list page.

![]({{ '/assets/images/applications/55_deformation_texture_lab/image0004.jpg' | relative_url }})

Expert mode Simulation controls 

## Loading Material from library

In Material list page, load the material **Ti-6Al-4V[70-1850F(20-1000C)]** from the **Titanium** category in the DEFORM Material library under using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load material data from library) option. Change the name of material to "**Ti64-test** ", select the material and check the checkbox of "Mixture material". Click ![]({{ '/assets/icons/pre_icons/mo_add_phase_button.jpg' | relative_url }}) twice to add two phases, then rename the added two phases to "**Alpha** " and "**Beta** " respectively (see Fig. 3DDTL1.5.). Using ![]({{ '/assets/icons/pre_icons/mo_copy_properties.jpg' | relative_url }}) option, copy the thermal properties of parent phase (Ti64-test) to child phases (Alpha and Beta).

Then load the material ******AISI-D3** from DEFORM Material library's, from **Die_material** category using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) (Load material data from library) option. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until the Alpha page.

![]({{ '/assets/images/applications/55_deformation_texture_lab/image0005.jpg' | relative_url }})

Added Alpha and Beta phase material for Ti64-test

Once you are in the Alpha material page, click the **Texture** icon to define the basic texture information. Select the**Crystal type** as **HCP**(hexagonal close packed), the Texture representation type as **Rodrigues****space** and the **Texture****mesh****type** as **Mesh 2: 111 nodes, 288 elements** as shown in Fig. 3DDTL1.6.

![]({{ '/assets/images/applications/55_deformation_texture_lab/image0006.jpg' | relative_url }})

Basic texture information of Alpha 

Then click on ![]({{ '/assets/icons/pre_icons/mo_plastic_button.jpg' | relative_url }}) tab to define plastic flow model for the material and its constant, select ![]({{ '/assets/images/applications/55_deformation_texture_lab/cp_flow_stress_model.jpg' | relative_url }}) model as shown in Fig. 3DDTL1.7. Click on ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) button. 

![]({{ '/assets/images/applications/55_deformation_texture_lab/image0007.jpg' | relative_url }})

Selecting Crystal plasticity Flow stress model

the window for definition of flow stress model pops up, Fig. 3DDTL1.8. shows an example to define the CP flow stress model for an HCP crystal. For **HCP** crystal, we need to specify **c/a** ratio (like 1.588 for titanium alloys). The deformation mode is defined according to the family of slip plane and slip direction. In the current DEFORM CP code, twinning deformation mode is not considered. HCP crystal has three deformation modes: basal slip (3 x {0001}<11-20>), prismatic slip (3 x {10-10}<11-20>), and pyramidal slip (6 x {10-11}<11-20> +12 x {10-11}<11-23> \+ 6 x {11-22}<11-23>).  
The symbols in flow rule and hardening rule are briefly explained in GUI, and not repeated here. The CP material parameters can be constants or functions of temperature. It is user's responsibility to specify the appropriate CP material parameters, for example, obtaining from literature, determining by user's own approach, or fitting by DEFORM flow stress module in material suite in terms of the experimentally measured flow stress data and initial microstructure (beyond the scope of this lab and not further discussed here).  
  
In this Lab, all deformation modes of each phase are activated, and CP hardening rule 2 (Voce) is adopted. The following CP material parameters are specified as shown in Fig. 3DDTL1.8. for Alpha phase: 

  
**c/a** =**1.588**

![]({{ '/assets/images/applications/55_deformation_texture_lab/alpha_material.jpg' | relative_url }})

![]({{ '/assets/images/applications/55_deformation_texture_lab/image0008.jpg' | relative_url }})

Crystal plasticity material parameters of alpha

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Beta material page. Click the **Texture** icon to define the basic texture information for Beta material like we did for Alpha material. Select the**Crystal type** as **BCC**(body centered cubic), the Texture representation type as **Rodrigues****space** , and the **Texture****mesh****type** as **Mesh 2: 145 nodes, 448 elements** as shown in Fig. 3DDTL1.9. Then click on ![]({{ '/assets/icons/pre_icons/mo_plastic_button.jpg' | relative_url }}) tab, select ![]({{ '/assets/images/applications/55_deformation_texture_lab/cp_flow_stress_model.jpg' | relative_url }}) model as shown in Fig. 3DDTL1.9. Click on ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}) button. 

![]({{ '/assets/images/applications/55_deformation_texture_lab/image0009.jpg' | relative_url }})

Basic texture information of Beta

For phase material “Beta” (BCC crystal), three deformation modes are available: 12 x {110}<111>, 12 x {112}<111>, 24 x {123} <111> (see Fig. 3DDTL1.10.). The CP material parameters are defined for each deformation mode and latent hardening is defined among deformation modes. The following CP material parameters are specified as shown in Fig. 3DDTL1.10. for Beta phase. 

![]({{ '/assets/images/applications/55_deformation_texture_lab/beta_material.jpg' | relative_url }})

![]({{ '/assets/images/applications/55_deformation_texture_lab/image0010.jpg' | relative_url }})

Crystal plasticity material parameters of Beta

Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Object page.

## Adding Objects 

We required only two objects for this lab. By default, three objects will be added in Forming operation list. Select the Bottom die from the list and click on ![]({{ '/assets/icons/pre_icons/mo_delete_object_button.jpg' | relative_url }}) (delete object) button to delete the selected objects. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Workpiece page.

## Workpiece

Accept the default object name **Workpiece**. Assign the temperature as **955** °C and keep the object type as **P****lastic**. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Geometry page.

### Create Workpiece geometry 

Import "**Texture_billet.stl** " from "**3D\LABS\Deformation_Texture_Lab** " installation folder using Load Geometry from a file ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }}) button.

As the object is 1/8th of the model we need to define the symmetry planes of the Workpiece. 

Click on ![]({{ '/assets/icons/pre_icons/mo_symmetry_planes_label.jpg' | relative_url }}) label. Select **Planar Symmetry** and assign Planar symmetry on Symmetry surfaces ((-1,0,0), (0,-1,0)) and also on the bottom surface (0,0,-1) as shown in Fig. 3DDTL1.11. Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the Symmetry planes page. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Mesh page.

![]({{ '/assets/images/applications/55_deformation_texture_lab/image0011.jpg' | relative_url }})

Assigned symmetry plane for workpiece

### Workpiece mesh generation

In Mesh page, define the **Target Number of Elements** as **25000** and **Size ratio** as **2,** click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button and click ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}) in "Default Boundary Conditions" popup. The Mesh generated looks like as shown in Fig. 3DDTL1.12. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button to Material page.

![]({{ '/assets/images/applications/55_deformation_texture_lab/image0012.jpg' | relative_url }})

Mesh generation for workpiece

### Assign Workpiece material

Select the "**Ti64-test** " material from the material list in the Material page as shown in Fig. 3DDTL1.13. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button to BCC page.

![]({{ '/assets/images/applications/55_deformation_texture_lab/image0013.jpg' | relative_url }})

Assigning material to workpiece

### Workpiece Boundary condition

Verify symmetry planes defined on the Symmetry plane and on Bottom surface in Boundary Conditions page, symmetry BCC (see Fig. 3DDTL1.14.) are assigned by default during mesh generation as symmetry planes were defined in Geometry page. Assigned Heat exchange BCC for other surfaces (except Symmetry plane) are as shown in Fig. 3DDTL1.15. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Properties page. 

![]({{ '/assets/images/applications/55_deformation_texture_lab/image0014.jpg' | relative_url }})

Assigned Symmetry plane BCC on Workpiece

![]({{ '/assets/images/applications/55_deformation_texture_lab/image0015.jpg' | relative_url }})

Assigned Heat exchange with Environment BCC on Workpiece

### Workpiece Properties

Under **Deformation** tab, define **Average** strain rate as**0.1** and **Limiting** strain rate as **0.001** as shown in Fig. 3DDTL1.16.

![]({{ '/assets/images/applications/55_deformation_texture_lab/image0016.jpg' | relative_url }})

Workpiece properties page

### Defining Elements data

Click on ![]({{ '/assets/icons/pre_icons/mo_elemental_data_icon.jpg' | relative_url }}) Element data on the tool bar for the initial values of the element data, the following state variables need to be initialized: (1) orientation distribution functions of each phase (ODFs), defined in the global reference system; (2) volume fraction of each phase; (3) CPISV (CP internal state variables). 

To import the initial texture data conveniently, five types of orientation data formats are designed in DEFORM: 

(1) Random orientation distribution, for which ODFs values are 1.0 at every independent node in Rodrigues space. For material with isotropic mechanical properties, this type of texture can be applied. 

  
(2) EBSD TSL/General (Bunge, radians), Euler angles are expressed in radians in Bunge's notation. This is the default setting in DEFORM to calculate orientation matrix. The effective EBSD data (assuming the number of orientations is N) are rearranged in the following format: 

![]({{ '/assets/images/applications/55_deformation_texture_lab/eq_1.jpg' | relative_url }})

(3)**** EBSD HKL (Bunge, degrees), the Euler angles are expressed in degrees in Bunge's notation. The effective EBSD data (assuming the number of orientations is N) are rearranged in the following format: 

![]({{ '/assets/images/applications/55_deformation_texture_lab/eq_2.jpg' | relative_url }})

Before calculating the orientation matrix, the first Euler angles are substracted by 90 degrees to convert from HKL format to TSL format. 

(4) WTD (Kocks, Degrees, Weights), Euler angles with weights are expressed in degrees in Kock's notation. The effective orientation data (assuming the number of orientations is N) are rearranged in the following format (Euler angles and weights): 

![]({{ '/assets/images/applications/55_deformation_texture_lab/eq_3.jpg' | relative_url }})

(5) WTD (Bunge, Radians, Weights), the Euler angles with weights are expressed in radians in Bunge's notation. The effective orientation data (assuming the number of orientations is N) are rearranged in the following format (Euler angles and weights): 

![]({{ '/assets/images/applications/55_deformation_texture_lab/eq_3.jpg' | relative_url }})

If the original experimentally measured texture data is not in these formats, then user should convert the original data to one of these five designed formats and import the converted data file. 

  
In this Lab, texture distribution is assumed to be axisymmetric. Two WTD orientation data files (**DEFORM_Sample_XRD_alpha.wts** and **DEFORM_Sample_XRD_beta.wts** under "**MANUALS\PDF\DEFORM3D_Texture_Evolution_Lab"** folder) are provided as examples to initialize ODFs. The initialization of ODFs for Alpha phase is illustrated in Fig. 3DDTL1.17. (same procedure for Beta phase). In the element dialogue (see Fig. 3DDTL1.17.(a)), select an element where the EBSD data are experimentally measured and click ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}) button, the initialization window for ODFs pops up (see Fig. 3DDTL1.17.(b)). The window has two tabs. In the first tab “**Orientation****data** ”, the orientation data of the reference point is specified. The reference point is the material point on workpiece where EBSD data is experimentally measured. The required input data include data format, data file path, the location of the reference point, RD, TD, and ND directions defined in the global coordinate system of reference point, and the smoothing angle to calculate ODFs in Rodrigues space. If the selected element is not close to the reference point, then user can manually input the coordinates (X,Y,Z) of the reference point, and click "**Reposition** ” to move it to the correct position. RD, TD, and ND directions of the reference point are displayed on the workpiece, which are unit vectors, perpendicular to one another, and satisfy the right-hand rule. User can edit RD, TD, and ND directions, and then click “**Apply****axis** ” to accept the new values. Typically, the smoothening angle is **10****** degrees for Rodrigues mesh type 2, 5 degrees for Rodrigues mesh type 3, and 2.5 degrees for Rodrigues mesh type 4. For the original orientation data, the contour of ODFs in Rodrigues space and pole figures can be plotted (without any coordinate transformation), as shown in Fig. 3DDTL1.18. for Alpha phase and Fig. 3DDTL1.19. for Beta phase. The purpose of such plots is for user to make sure the input orientation data file is correct.

In the second tab “**Domain****assignment** ”, select “**Global********ODF** ” radio button. Two simple texture distributions with location can be considered: uniform and axi-symmetric. In this lab, select “**Axi****-symmetric** ” radio button, and define the rotation axis by specifying two points: point 1(0, 0, 0) and point 2 (0, 0, 1). Click ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) button, the cursor changes to a “busy” status. We should wait until the initialization is completed and the cursor changes back to an “idle” status. For axisymmetric texture, the time for initialization of ODFs in Rodrigues space depends on the crystal type, the Rodrigues mesh type, the number of orientations in the input file, and the number of elements of workpiece. In this lab, ODFs initialization takes few minutes approximately for alpha phase (110 orientations) and half an hour for beta phase (1000 orientations), depending on the computer performance. Finally, click ![]({{ '/assets/icons/pre_icons/mo_close_button2.jpg' | relative_url }}) button to return to the element dialogue. The initialized ODF values with orientations represented in the global coordinate system are listed in the table. ODFs can be displayed in Rodrigues space or displayed as pole figures with user-specified setup. 

For HCP metals, 4 types of pole figures: (0001), (11-20), (10-10), and all three pole figures can be plotted. For BCC metals, 4 types of pole figures: (100), (110), (111), and all three pole figures can be plotted. In the pole figure setup, the following parameters should be defined: (HKL) type, RD-TD-ND direction in the global reference system, ODF reference system (global), and combined phase. For example, if an element has texture information of primary alpha and secondary alpha, the pole figures of total alpha can be plotted. The pole figures of beta phase of one element are shown in Fig. 3DDTL1.20. After plotting ODFs contour or pole figures, click the close icon ![]({{ '/assets/icons/post_icons/mo_odf_close_button.jpg' | relative_url }}) to exit the ODFs displaying mode. 

![]({{ '/assets/images/applications/55_deformation_texture_lab/image0017.jpg' | relative_url }})

(a)

![]({{ '/assets/images/applications/55_deformation_texture_lab/image0018.jpg' | relative_url }})

(b)

Initialization of orientation distribution functions(ODF)

![]({{ '/assets/images/applications/55_deformation_texture_lab/image0019.jpg' | relative_url }})

(a)

![]({{ '/assets/images/applications/55_deformation_texture_lab/image0020.jpg' | relative_url }})

(b)

****ODFs in Rodrigues space and pole figures of primary Alpha

![]({{ '/assets/images/applications/55_deformation_texture_lab/image0021.jpg' | relative_url }})

(a)

![]({{ '/assets/images/applications/55_deformation_texture_lab/image0022.jpg' | relative_url }})

(b)

ODFs in Rodrigues space and pole figures of primary Beta

![]({{ '/assets/images/applications/55_deformation_texture_lab/image0023.jpg' | relative_url }})

Pole figures of beta phase with user-specified setup

Fig. 3DDTL1.21(a) shows the initialization of CPISV. The default names and initial values (zeroes) are automatically defined and usually it is not necessary to make any change. The data structure of CPISV is explained in Fig. 3DDTL1.21(b). For VPSC model, it consists of three parts. In part 1, for each grain of each phase, the following state variables are calculated: deviatoric stresses (6 components), accumulated shear amount (1 component) and the slip resistance of each deformation mode. Part 2 includes macroscopic compliance of 81 components and back-extrapolated strain rate term (6 components). Part 3 includes statistical information of each phase, such as contribution fraction to total shear rate, average number of active systems per grain (AVACS), and relative slip activity of each deformation mode. These statistic quantities are calculated in terms of the shear strain rate of each slip system in a simulation step. For VPTL model, part 2 is not needed.

![]({{ '/assets/images/applications/55_deformation_texture_lab/image0024.jpg' | relative_url }})

(a)

![]({{ '/assets/images/applications/55_deformation_texture_lab/image0025.jpg' | relative_url }})

(b)

(a) Initialization of CPISV; (b) data structure of CPISV 

Fig. 3DDTL1.22. shows the initialization of volume fraction of each phase. In the properties window, the volume fraction of each phases is listed under **Microstructure**![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **Phase**. We can initialize the volume fraction of each phase separately by assigning a specific value, as in a general way. For Titanium alloys with two phases (Alpha and Beta), we can use the so-called "**Beta approach curve** " to initialize volume fraction of both phases. We need to specify the material names for both Alpha phase and Beta phase. Depending on the average temperature of each element, the volume fractions will be initialized automatically. The Beta approach curve defines the volume fractions of Beta phase in the equilibrium state at different solution temperatures. It can be loaded directly if the data file is ready or can be defined manually by clicking the ![]({{ '/assets/icons/pre_icons/mo_define_button2.jpg' | relative_url }}) button. The data format of the beta approach curve is described as follows (Semiatin et al., Metall. Mater. Trans. 34A (2003), pp. 2386-2377): 

  
Alloy="Ti64", chemistry in weight percent   
Al=6.4   
C=0.016   
Fe=0.14   
O=0.19   
V=4.2   
Ti=-1 

  
T[C] f(BCC_A2) f(HCP_A3) 

1025 1 0   
1000 1 0   
975 0.83 0.17   
950 0.7 0.3   
925 0.58 0.42   
900 0.48 0.52   
875 0.39 0.61   
850 0.31 0.69   
800 0.22 0.78   
775 0.2 0.8   
750 0.19 0.81   
725 0.18 0.82

The first 12 lines define the chemical composition and the title of data line. For each data line, there are three values: solution temperature, volume fraction of beta, and volume fraction of alpha ("**Ti64_BetaApproachCurve.dat** " file available under "**3D\LABS\Deformation_Texture_Lab** " folder for reference of beta approach curve data). For each element, in terms of average temperature, the volume fraction of each phase is calculated by a linear interpolating method.

![]({{ '/assets/images/applications/55_deformation_texture_lab/image0026.jpg' | relative_url }})

Initialization of volume fraction using beta approach curve

After initializing the elemental data, close the Elemental data dialog and click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top die page.

## Top Die

Accept the default object name **Top Die**. Assign the temperature as **600** °C and keep the object type as **Rigid**. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Geometry page.

### Create Top die geometry 

Click on ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}), select **Cylinder** and define a **Height**(H) as **5** mm and **Radius**(R) as **20** mm. Define **Start angle** as **0** , **Revolve Angle** as **90** , **Sections** as **90** and click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}). Click on ![]({{ '/assets/icons/pre_icons/mo_symmetry_planes_label.jpg' | relative_url }}) label, define Planar Symmetry on symmetry planes with the normal directions of (-1,0,0) and (0,-1,0)) as shown in  Fig. 3DDTL1.23. Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the Symmetry planes window. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Mesh page.

![]({{ '/assets/images/applications/55_deformation_texture_lab/image0027.jpg' | relative_url }})

Assigned Planar symmetry on Top die

### Top die mesh generation

In Mesh page, define **Target Number of Elements** as **10000** and **Size ratio** as **2,** click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) button and click ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}) in "Default Boundary Conditions" popup. The generated mesh looks like a shown in Fig. 3DDTL1.24. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) button to Material page.

![]({{ '/assets/images/applications/55_deformation_texture_lab/image0028.jpg' | relative_url }})

Mesh generation for Top die

### Assign Top die material

Select the "**AISI-D3** " material in material list as shown in Fig. 3DDTL1.25. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Top die movement page.

![]({{ '/assets/images/applications/55_deformation_texture_lab/image0029.jpg' | relative_url }})

Assigning material for workpiece

### Top die Movement 

In Top die movement page, select "**Hydraulic press** " radio button, define constant **speed** of **1.5** mm/sec and select direction as **-Z** direction as shown in Fig. 3DDTL1.26. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Positioning page

![]({{ '/assets/images/applications/55_deformation_texture_lab/image0030.jpg' | relative_url }})

Top die movement page

## Positioning objects

We will position the **Top Die** over the **Workpiece** using interference positioning. In the **positioning** page, click the ![]({{ '/assets/icons/pre_icons/mo_positioning_objects_button.jpg' | relative_url }}) icon, select "**Interference** " as the positioning method, select "**Top Die** " as **Positioning****object** and "**Workpiece** " as the **Reference** ,**** select -**Z** **Axis** as the approach direction and click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) and then ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close the Positioning dialog, click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Contact page.

## Contact

Select '**User** ' type contact and click on ![]({{ '/assets/icons/pre_icons/mo_add_default_relations_button.jpg' | relative_url }}) button. It will add a relationship between the Top Die and Workpiece. Highlight the **Top Die - Workpiece** relationship and click on the ![]({{ '/assets/icons/pre_icons/mo_edit..._2_button.jpg' | relative_url }}) button to modify the contact conditions, enter **Shear****friction** as **0.3** and **Heat****transfer****Coefficient** as **10** and close the Inter-object data dialog. Click on ![]({{ '/assets/icons/pre_icons/mo_tolerance_icon.jpg' | relative_url }}) button to calculate default tolerance value and then click on ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) to generate contact between Workpiece and Top die. Generated contact is as shown in the Fig. 3DDTL1.27. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Step page.

![]({{ '/assets/images/applications/55_deformation_texture_lab/image0031.jpg' | relative_url }})

Inter-Object data definition window

## Defining Step controls

Click on "**Simulation steps** " ![]({{ '/assets/icons/pre_icons/mo_simulation_step.jpg' | relative_url }}) tab, define **Number of Simulation steps** as **500** and **Step Increment to save** as **10**. Then click on "**Step increment** " ![]({{ '/assets/icons/pre_icons/mo_step_increment.jpg' | relative_url }}) tab, select **Time** as **Solution step definition type** and define **constant** **time** increment of **0.008** sec as shown in Fig. 3DDTL1.28.

![]({{ '/assets/images/applications/55_deformation_texture_lab/image0032.jpg' | relative_url }})

Defining simulation steps and Step increment 

Click on “**Solver setting** ” ![]({{ '/assets/icons/pre_icons/mo_solver_settings.jpg' | relative_url }}) icon, under “**Deformation** ” tab, select “**SPOOLES** ” solver and “**Direct iteration** ” method. Click on “**Crystal plasticity** ” tab (see Fig. 3DDTL1.29.), select the radio button “**Viscoplastic self-consistent (VPSC)”** for homogenization scheme and “**Affine** ” for grain level linear scheme. Set the maximum number of iterations for **overall modulus** to **100** and for **grain stress** to **200**. Check “**Calculate mode activities** ” to calculate slip activity of each mode and the deformation contribution of each phase. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Generate DB page.

![]({{ '/assets/images/applications/55_deformation_texture_lab/image0033.jpg' | relative_url }})

Simulation controls - Solvers settings 

## Generate Database

In '**Generate DB** ' page, click ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) to see if anything was missed in the setup and then click on the ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database. Observe the message in Message tab informing database generation status.

## Running Simulation

Once the database has been generated, switch to the Simulation mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the operation tree. Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. 3DDTL1.30. Use the default **Continue Run** option with “**Continue from the last step** ” (from step -1) option and then select the Simulation mode as **Interactive.** Click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation. 

In this lab, the workpiece has 26409 tetrahedral elements and simulation step is 500. It took 40 hours for 4 processors (AMD Ryzen 9 5950X 16-core processors, 3.4GHz) to complete the FEM simulation. 

![]({{ '/assets/images/applications/55_deformation_texture_lab/image0034.jpg' | relative_url }})

Run Simulation Window

Monitor the progress of the simulation by looking at the Simulation Message and Simulation Log tab, making sure that the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked.

## Post Processing

When the simulation is completed, review the results by switching to Post mode using the ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) button above the Simulation tool bar.

Select the last step in the step browser. We can plot the contour of state variable, contour of ODF in Rodrigues space and pole figures, and do point tracking for CPISV (CP internal state variables). 

### Contours of state variables 

Click the ![]({{ '/assets/icons/post_icons/mo_state_variable_icon.jpg' | relative_url }}) icon for state variables and select the state variable that you are interested to plot from the corresponding category, such as **effective strain** , and click ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}) to display the contour of this state variable (see Fig. 3DDTL1.31.).

![]({{ '/assets/images/applications/55_deformation_texture_lab/image0035.jpg' | relative_url }})

Displaying the contour of state variable 

![]({{ '/assets/images/applications/55_deformation_texture_lab/image0036.jpg' | relative_url }})

Displaying the contour of a CPISV component 

In order to display CPISV (CP internal state variables), select the Workpiece and click the ![]({{ '/assets/icons/pre_icons/mo_elemental_data_icon.jpg' | relative_url }}) icon from the tool bar, as shown in Fig. 3DDTL1.32. Expand the "**Microstructure** " item and “**Texture** ” subitem in the list tree, and click “**CPISV** ” subitem, the CPISV components and values are displayed. Select the component you are interested in, then click the ![]({{ '/assets/icons/pre_icons/mo_preview_icon.jpg' | relative_url }}) button to display the contour of selected state variable. Fig. 3DDTL1.32. shows the contour of component **1353**(contribution fraction of phase 2 to plastic deformation). ODFs contours in Rodrigues space and pole figures. To view texture information, expand the "**Texture** " item in the list tree, select the phase you are interested in, then the ODFs of the selected phase of the picked element will be listed in the ODF table. Click the ![]({{ '/assets/icons/post_icons/mo_plot_odf_in_redrigues_space_button.jpg' | relative_url }}) icon of Rodrigues space to display the contours of ODFs in Rodrigues space. The ODF contours of Alpha and Beta of element 5520 are shown in Fig. 3DDTL1.33

![]({{ '/assets/images/applications/55_deformation_texture_lab/image0037.jpg' | relative_url }})

Displaying ODFs in Rodrigues space 

  
Fig. 3DDTL1.34. shows the setup for plotting pole figures. Unlike ODFs, pole figures depend on the user-defined RD, TD, and ND directions in the global reference frame. For the picked element (Element # 5520), we set RD in the radius direction (+X), TD in the axis direction (+Z), and ND in negative Y direction (-Y). That is, in the global reference system, RD=(1,0,0), and TD=(0,0,1),and ND=(0,-1,0). ODF reference system is “**Global** ”. With this setting, the pole figures of Alpha and Beta are shown in Fig. 3DDTL1.35.

It should be noted that, for the phases with the same crystal structure (but different phase shape, size, or distribution), besides plotting pole figures of each phase separately, we can plot the overall pole figures of two phases by specifying the additional phase using “Combined with phase” combo box. 

![]({{ '/assets/images/applications/55_deformation_texture_lab/image0038.jpg' | relative_url }})

Setup for pole figures

![]({{ '/assets/images/applications/55_deformation_texture_lab/image0039.jpg' | relative_url }})

Displaying pole figures of alpha phase and beta phase 

### Point tracking of CPISV 

At user-interested locations, point tracking can be performed to investigate the evolution of CPISV (CP internal state variables) with deformation. In this Lab, two points are picked on Workpiece, "P1" (0.80411, 0, 0.0579917, 1) and "P2" (8.51791, 0, 8.78666, 1) (see Fig. 3DDTL1.36.). Point tracking results for phase contribution to deformation, average number of active systems per grain (AVACS), and relative slip activity of each deformation mode are shown in Fig. 3DDTL1.37. ~ Fig. 3DDTL1.39. Fig. 3DDTL1.37. plots the contribution fraction of each phase to total shear rate. It can be seen that Beta phase makes a dominant contribution (75%~80%) to plastic deformation because it is much softer than Alpha phase. Fig. 3DDTL1.38. shows the evolution of AVACS with deformation. Only 2~3 slip families are activated in Alpha phase while 7~ 15 slip families are activated in Beta phase. Fig. 3DDTL1.39. shows the relative slip activity of each deformation mode in each phase. For Alpha phase, basal slip and prismatic slip make a significant contribution while pyramid slip makes a minor contribution; for Beta phase, the contribution of (110)<111> and (112)<111> is approximately 25% respectively, while the contribution of {123}<111> is close to 50%. 

![]({{ '/assets/images/applications/55_deformation_texture_lab/image0040.jpg' | relative_url }})

Point tracking data 

![]({{ '/assets/images/applications/55_deformation_texture_lab/image0041.jpg' | relative_url }})

Relative contribution to total shear rate: (a) Alpha phase; (b) Beta phase 

  
![]({{ '/assets/images/applications/55_deformation_texture_lab/image0042.jpg' | relative_url }})

Evolution of AVACS with deformation: (a) alpha phase; (b) beta phase 

![]({{ '/assets/images/applications/55_deformation_texture_lab/image0043.jpg' | relative_url }})

Relative slip activity of each deformation model: (a) Alpha phase; (b) Beta phase

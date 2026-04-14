---
lang: sk
title: "RVE Lab2"
---

# RVE Lab2 : RVE model for fracture of Hard inclusion 

2.1. Introduction to RVE model

2.2. Launch RVE model in Material suite

2.3. Object selection and point selection

2.4. Setting up RVE model

2.4.1. Defining RVE Model dimension

2.4.2. Defining materials for RVE Model

2.4.3. Defining RVE Model

2.4.4. Generating mesh for RVE Model

2.4.5. Defining inclusion settings

2.4.6. Generating Database to simulate RVE model

2.5. Simulating RVE model

2.6. RVE model Output

## Introduction to RVE model

Representative volume element (RVE) models at micro-scale via point tracking of a given database. Using RVE model, we can study detailed micro level response (local stress and strain, defects/matrix interaction, void closure), evaluation of microstructure (particle size, volume fraction, shape orientation etc), evaluation of textures, etc. 

In this lab, we will demonstrate how to use RVE to model fracture of hard inclusion.

## Launch RVE model in Material suite

On a Windows machine, go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button, select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2 and select DEFORM GUI Main v1x.xx from the menu. The DEFORM GUI Main window will appear.

We require a nominal DB to perform RVE model in material suite, for this lab we will use Forging_2D_Uniform.key from **\2D\LABS\RVE_LABS** folder to generate nominal DB. Open **NG Pre** (![]({{ '/assets/icons/pre_icons/2d_3d_pre_radio_button.jpg' | relative_url }})) to create a new problem either by selecting **File![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }})****New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon as shown in [Fig. RVEL2.1.]() Define problem Name as "**Forging_2D_Uniform** " and "**System****International****(SI)** " unit System radio button in New Problem window as shown in [Fig. RVEL2.1.]() Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button.

![]({{ '/assets/images/labs/material_suite_labs/rve_lab2/image0001.jpg' | relative_url }})

Creating New problem 

![]({{ '/assets/images/labs/material_suite_labs/rve_lab2/image0002.jpg' | relative_url }})

NG Pre New problem window

  
NG Pre GUI will open, keep Problem ID as "**Forging_2D_Uniform** " button and "**System International (SI)** " unit System , select "**2D** " Dimension radio button in New Problem window as shown in Fig. RVEL2.2. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to close the New Problem dialog. Import “**Forging_2D_Uniform.ke** y” from “**\2D\LABS\RVE_LABS** ” folder using “**Import Keyfile** ” from File menu in NG Pre as shown in Fig. RVEL2.3.

![]({{ '/assets/images/labs/material_suite_labs/rve_lab2/image0003.jpg' | relative_url }})

Importing Forging_2D_Uniform keyfile using Import Keyfile option

Navigate to Generate DB page and click on ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) to generate database. Close the NG Pre and run the simulation from GUI Main, make sure simulation stops normally without any issue. Now from GUI Main, without selecting **Forging_2D_Uniform**.DB file click on **Material****Suite** under “Post Processor” to open Material Suite module as shown in Fig. RVEL2.4.

![]({{ '/assets/images/labs/material_suite_labs/rve_lab2/image0004.jpg' | relative_url }})

Opening Material Suite from GUI Main

  
After the main window for material suite is opened, click "Open..." icon **(![]({{ '/assets/icons/pre_icons/mo_open_icon.jpg' | relative_url }}))** in the top tool bar to import the database simulated above (**Forging_2D_Uniform****.DB**). The default task item "**DEFORM** " is added to the task tree. Expand "**Microstructure** " item and click on "**RVE Model** " icon from Microstructure list as shown in Fig. RVEL2.5., the new task item "RVE model" is added to the task tree.

![]({{ '/assets/images/labs/material_suite_labs/rve_lab2/image0005.jpg' | relative_url }})

Launching RVE model in material suite

## Object selection and point selection

In the "DEFORM" task tree, click on "**O****bject selection** " item and select "**workpiece** " (see Fig. RVEL2.6.). Click on "**Point****selection** " item, since we are at first step when DB was loaded, the step number will be "-1" in step number field ( Fig. RVEL2.7.). Define one point on Workpiece as shown in Fig. RVEL2.7. The coordinate of point1 (**P1**) is (61.6289, 129.55, 0, 1). Users can choose any step number convenient for them. 

![]({{ '/assets/images/labs/material_suite_labs/rve_lab2/image0006.jpg' | relative_url }})

Selecting object to be used to model RVE

![]({{ '/assets/images/labs/material_suite_labs/rve_lab2/image0007.jpg' | relative_url }})

Point selection on Workpiece

## Setting up RVE model

Click on "**Config** " item from RVE Model Task tree, Configuration window appears. We need to specify the executable for FEM simulation and the working directory using the ![]({{ '/assets/icons/post_icons/mo_import_button.jpg' | relative_url }}) button adjacent to the field. The default executable for RVE model simulation is “DEF_SIMULATION.EXE", which is in installation directory of DEFORM software. The directory containing nominal database is set as Working directory as shown in Fig. RVEL2.8.

![]({{ '/assets/images/labs/material_suite_labs/rve_lab2/image0008.jpg' | relative_url }})

RVE Model Configuration settings

### Defining RVE Model dimension

Click on “**RVE model dimension** ” item under RVE model Task Tree, select RVE model dimension as “**2D** ” as shown in Fig. RVEL2.9. Using “**Import Project** ” option, we can import previously saved RVE model project and using “**Save Project** ” option, we can save the RVE model project.

![]({{ '/assets/images/labs/material_suite_labs/rve_lab2/image0009.jpg' | relative_url }})

Selecting RVE model dimension

### Defining materials for RVE Model

Click on "**RVE model Materials** " item under RVE model Task Tree, the first material listed in the list is the material of Workpiece in the nominal database. In this lab, we will be importing one inclusion material, click on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Add button), one “New material” will be added to the list, select the "New material" in list and import " **Hard_Inclusion_Material.key** " from "2D\LABS\RVE_LABS" folder using Import ![]({{ '/assets/icons/pre_icons/mo_import_file_icon.jpg' | relative_url }})option. In Matrix material (Steel) flow stress model from nominal DB is ![]({{ '/assets/images/labs/material_suite_labs/rve_lab2/matrix_material_eq.jpg' | relative_url }}) and imported Hard inclusion material flow stress model is ![]({{ '/assets/images/labs/material_suite_labs/rve_lab2/hard_inclusion_eq.jpg' | relative_url }}) . After loading the materials, RVE Model Materials page looks like as shown in Fig. RVEL2.10. We can also import the material data from library using ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) button, save the material using ![]({{ '/assets/icons/pre_icons/mo_save_to_a_file_icon.jpg' | relative_url }}) button and we can also Edit the material using ![]({{ '/assets/icons/pre_icons/mo_edit_material_button.jpg' | relative_url }}) button. 

![]({{ '/assets/images/labs/material_suite_labs/rve_lab2/image0010.jpg' | relative_url }})

Loading material required for RVE Model

### Defining RVE Model

Click on "**RVE model setup** " item under RVE model Task Tree, here we can create RVE model geometry using primitive option (2D circular inner void, 2D ellipse inner void and 2D semi-ellipse surface void) or using 2D user defined RVE model option.

Under 2D user defined RVE model option, we can import geometry for Matrix and for Substructure as geometry file or keyfile using "Import user integrated RVE model from a file" button.

Under Substructure, we have following options:

  * **Import** geometry file button - to import Substructure geometry from a file.

  * **Translation** \- Translates the selected geometry to the translation coordinates.

  * **Rotation** – Rotates the selected geometry based on defined rotation axis and Rotation angle (Degrees) data.

  * **Scale** \- Scales the selected geometry based on scaling factor in X and Y direction.

  * **Duplicate** \- We can duplicate the selected geometry and position the duplicated geometry based on the translation.

  * **Delete** \- Deletes the selected geometry in list.

  * **Submodel** \- We can define the RVE fracture plane data for the selected geometry and generate tessellation inside the selected geometry. This option will not be active for voids.

In this lab, we are creating three substructures using Submodels option. In "**RVE****model** **setup** " page, select “**2D****circular****inner****void** ”, specify **RVE****model****size** (**L**) as **1.5** and**Radius(R)** as **0.1** this will be geometry of the central substructure. Click on ![]({{ '/assets/icons/post_icons/ms_rve_generate_geo_button.jpg' | relative_url }}) button, created RVE model will look like as shown in Fig. RVEL2.11.

![]({{ '/assets/images/labs/material_suite_labs/rve_lab2/image0011.jpg' | relative_url }})

RVE model geometry

To create submodels, select Substructure Material as “**Hard****inclusion** ” using pulldown menu as shown in Fig. RVEL2.11. and click on ![]({{ '/assets/icons/pre_icons/mo_define_button2.jpg' | relative_url }}) button, RVE Fracture Planes definition window will open. In RVE Fracture Planes, we have two options to create substructures, 

  * **By individual plane (line)** : using this this option we can split the substructure into sub model using defined individual plane data. 

  * **By random seeds** : using this this option we can create sub model as per defined seeds # data.

After defining plane data when user clicks on ![]({{ '/assets/icons/post_icons/ms_tessellation_button.jpg' | relative_url }}) button, substructure geometry will be created.

In this lab, we will use “**By individual plane(line)** ” option to create submodels. Select “**By individual plane(line)** ” radio button, click on ![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }}) (Add) button twice to add two planes. For **FP1** , define Point 1 as -0.04 (X), -0.2 (Y) and Point 2 as -0.04 (X), 0.2 (Y). Similarly, define Point 1 as 0.04 (X), -0.2 (Y) and Point 2 as 0.04 (X), 0.2 (Y) for **FP2** and click on ![]({{ '/assets/icons/post_icons/ms_tessellation_button.jpg' | relative_url }}) to create Submodels. Created submodels will be as shown in Fig. RVEL2.12. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) to close RVE Fracture Planes page. 

![]({{ '/assets/images/labs/material_suite_labs/rve_lab2/image0012.jpg' | relative_url }})

Creating RVE Substructure geometry

### Generating mesh for RVE Model

Click on "**RVE model mesh** " item under RVE model Task Tree, we will consider the substructures as separate objects, hence turn on "**Make inclusions separate objects** " check box. For **Matrix** , define**No. of** **elements** as **5000** and **size****ratio** as**2** and for **smallest****inclusion** , define **No. of elements** as **100** and size ratio as **1**. Click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) to generate mesh, generated mesh for RVE model looks like as shown in Fig. RVEL2.13.

![]({{ '/assets/images/labs/material_suite_labs/rve_lab2/image0013.jpg' | relative_url }})

Mesh settings for RVE model inclusions

### Defining inclusion settings

Click on "**Inclusion settings** " item under RVE model Task Tree. In **Matrix****-****inclusion** contact relation, select contact type as "**Non sticking** " and friction type as "**Shear** " with friction coefficient of**0.25** , then select Pressure-based separation criteria as “**Absolute****value** ” and define Absolute value as**250** as shown in Fig. RVEL2.14. Similarly, In **Inclusion-inclusion** contact relation, select friction type as "**Shear** " with friction coefficient of **0.25** , select Pressure-based separation criteria as “**Absolute****value** ” and define Absolute value as **60** as shown in Fig. RVEL2.14.

![]({{ '/assets/images/labs/material_suite_labs/rve_lab2/image0014.jpg' | relative_url }})

Defining Inclusion settings

### Generating Database to simulate RVE model

Click on "**RVE model DB generation** " item under RVE model Task Tree, we can observe the RVE model setup information in RVE model DB generation page. Click on ![]({{ '/assets/icons/post_icons/ms_generate_database_button.jpg' | relative_url }}) button to generate Database to simulate the RVE model. After generating Database successfully, we can observe "Database files are generated successfully for all tracked points!" message in Status bar (See Fig. RVEL2.15.)

After generating database, we can observe that RVE_MODEL folder is created under working directory. Inside RVE_MODEL directory, separate directories for each point will be created with “Point *” containing RVE model database along with .txt files of point tracking data for stress components, mean temperature and Velocity gradient state variables. 

![]({{ '/assets/images/labs/material_suite_labs/rve_lab2/image0015.jpg' | relative_url }})

Database generation page for RVE model

## Simulating RVE model

Click on "**Run** " item in the task tree and click on "**Compute** " button in the data window to run the simulation (see Fig. RVEL2.16.).

![]({{ '/assets/images/labs/material_suite_labs/rve_lab2/image0016.jpg' | relative_url }})

RVE model Run page

## RVE model Output

After completion of simulation, click on "**Point1** " item under “**Output** ” in task tree, go to last step and plot Strain Effective state variable (see Fig. RVEL2.17.). We can play the animation to observe the material fracture behavior during forming operation. Fig. RVEL2.18. shows the fracture of submodels at different steps.

![]({{ '/assets/images/labs/material_suite_labs/rve_lab2/image0017.jpg' | relative_url }})

Point1 Output at last step with Effective Strain state variable

![]({{ '/assets/images/labs/material_suite_labs/rve_lab2/image0018.jpg' | relative_url }})

Point1 Fracture with Hard inclusion at different steps

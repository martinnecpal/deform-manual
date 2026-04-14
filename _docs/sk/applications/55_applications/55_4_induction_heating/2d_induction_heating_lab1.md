---
lang: sk
title: "2D Induction Heating Lab 1"
---

# 2D Induction Heating Lab 1

Induction Heating Surface of 30mm Radius Bar: 

This Induction Heating lab will show the proper way to set up an induction heating of a bar with a copper coil(s). The lab will allow the user to add the necessary material properties to conduct the electro-magnetic portion of the calculations.

1.1. Creating a New Problem

1.2. Adding Operation

1.3. Selecting Geometry Type

1.4. Simulation Controls

1.5. Material list

1.6. Adding Objects

1.7. Workpiece

1.8. Bottom Coil

1.9. Lower Middle Coil

1.10. Middle Coil

1.11. Upper Middle Coil

1.12. Top Coil

1.13. Air

1.14. Contact

1.15. Stopping controls

1.16. Generate DB

1.17. Running Simulation

1.18. Post Processing

## Creating a New Problem

On a Windows machine, go to the ![]({{ '/assets/icons/pre_icons/windows_start.jpg' | relative_url }}) button select DEFORM-v1x.xxx (.xxx indicates version number E.g. v14.0.2) and select **DEFORM GUI Main** v1x.x from the menu. The DEFORM GUI Main window will appear, as shown in Fig. 2DINDL1.1.

![]({{ '/assets/images/applications/55_2_arc_welding/image0001.jpg' | relative_url }})

DEFORM GUI Main window

Create a new problem either by selecting **File**![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) **New Problem** or by clicking the New Problem ![]({{ '/assets/icons/pre_icons/mo_new_problem_icon.jpg' | relative_url }}) icon. The Problem Setup window will appear as shown in Fig. 2DINDL1.2. Select " **Integrated Manufacturing Process** " radio button and unit system as "**SI** " radio button in unit field. Define Problem Name as " **IH_Lab_2DFEM1a** " and make sure the “**Show option dialog** ” check box is turned on (if we do not turn on the “**Show option dialog** ” check box, then we will not get the New Project dialog in MO UI). Then click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to open a new Problem using the Deform Integrated Manufacturing Process.

![]({{ '/assets/images/applications/55_2_arc_welding/image0002.jpg' | relative_url }})

New Problem page

Multiple operation wizard will open with the New Project dialog, at this point user will be prompted to specify a project name (system will create a separate folder with this project name) and title for this session. In this session we will use "**IH_Lab_2DFEM1a** " as the project name. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) to continue to open the operation.

## Adding Operation

Add **2D****Forming** operation from the Explorer Operations list. Add the operation by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_operation_icon.jpg' | relative_url }}) button available next to 2D Forming Operation or user can also add by drag and drop into the Operation Editor. When we add the 2D Forming operation, process settings window will open by default (see Fig. 2DINDL1.3.).

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab1/image0003.jpg' | relative_url }})

Adding 2D Forming operation

## Selecting Geometry Type

In this lab we will be using Axisymmetric geometries, so select **2D****Axisymmetric** radio button from geometry type page (see Fig. 2DINDL1.4.), then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) .

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab1/image0004.jpg' | relative_url }})

Geometry type selection

## Simulation Controls

Switch to Expert mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_expert_mode_icon.jpg' | relative_url }}) icon, Enter Operation name as " **Initial Heat Up** " and be sure that **Heat****transfer** , **Transformation** and **Heating** are checked with the **Enthalpy** type for **Solidification** and **Induction** as **Heating** method selected from drop boxes as shown in Fig. 2DINDL1.5.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab1/image0005.jpg' | relative_url }})

Simulation controls - Main page

Click on **Simulation** Steps ![]({{ '/assets/icons/pre_icons/mo_simulation_step.jpg' | relative_url }}) , enter the **Number****of****simulation****steps** as **1000** and keep **Step****increment****to****save** as **10** as shown in Fig. 2DINDL1.6.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab1/image0006.jpg' | relative_url }})

Simulation controls -Simulation steps page

Click on **Step****increment![]({{ '/assets/icons/pre_icons/mo_step_increment.jpg' | relative_url }})** , under the **General** tab, select the Solution step definition as **Temperature** and define Initial time step as **0.1** sec, Max temperature change as **5** °C, Min time step as **0.0001** sec and Max Time Step as **0.25** sec as shown in Fig. 2DINDL1.7.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab1/image0007.jpg' | relative_url }})

Simulation controls - Step increment page

Click on **Stopping****criteria![]({{ '/assets/icons/pre_icons/mo_stopping_criteria.jpg' | relative_url }}) **and enter **Process** **duration** as **10** sec as shown in Fig. 2DINDL1.8.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab1/image0008.jpg' | relative_url }})

Simulation controls - Stopping criteria page

Click on **Advanced** options, under **Frequency** tab for **Maxwell****equation** solving select **User- defined** using drop-down list and define every **10** step(s) as shown in Fig. 2DINDL1.9., this is done so that electro-magnetic calculations are done for every 10 steps instead of each step. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Material Page.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab1/image0009.jpg' | relative_url }})

Simulation controls - Advanced option Frequency page

## Material list

In Material list Window, click on ![]({{ '/assets/icons/pre_icons/mo_load_from_library_icon.jpg' | relative_url }}) to Load material data from Library and select the category **Steel** and load material “**JIS-S45C (Heat Treatment)** ”. The material you added will show up as **S45C-JAPAN** with 3 phases beneath it. Create 2 new materials Click on (![]({{ '/assets/icons/pre_icons/mo_add_icon2.jpg' | relative_url }})) and by double clicking the names change to **Coil** and **Air** respectively (see Fig. 2DINDL1.10.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Austenite material page.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab1/image0010.jpg' | relative_url }})

Material list

In **Austenite** page, click on **Elec./Mag.** tab and define the **Electrical****resistivity** as **1** , **Relative magnetic permeability** as **1** and **Relative****electrical****permitivity** as **0** as shown in Fig. 2DINDL1.11. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Pearlite material page.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab1/image0011.jpg' | relative_url }})

Austenite- Electro-magnetic material page

In **Pearlite** page, click on **Elec./Mag.** tab and select **Electrical** **resistivity** as **Function of Temperature** and define the below table and click on ![]({{ '/assets/icons/pre_icons/mo_apply_button2.jpg' | relative_url }}) button.

|  **Temperature** |  **Resistivity**  
---|---|---  
1 |  -100 |  0.000159  
2 |  0 |  0.000159  
3 |  50 |  0.00019  
4 |  100 |  0.00022  
5 |  200 |  0.000296  
6 |  300 |  0.000395  
7 |  400 |  0.000495  
8 |  500 |  0.00063  
9 |  600 |  0.000766  
10 |  650 |  0.000849  
11 |  700 |  0.000932  
12 |  725 |  0.000975  
13 |  750 |  0.00102  
14 |  800 |  0.0011  
15 |  1300 |  0.00125  
  
Electrical resistivity plot should like as shown in Fig. 2DINDL1.12.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab1/image0012.jpg' | relative_url }})

Electrical resistivity plot

For **Relative****magnetic****permeability** select **Function of Temperature** and define the below table and click on ![]({{ '/assets/icons/pre_icons/mo_apply_button2.jpg' | relative_url }}) button.

|  **Temperature** |  **Magnetic** **permeability**  
---|---|---  
1 | 0 | 30  
2 | 500 | 30  
3 | 575 | 29  
4 | 600 | 26  
5 | 625 | 23  
6 | 650 | 19  
7 | 675 | 13  
8 | 725 | 3  
9 | 750 | 1  
10 | 1300 | 1  
  
**Relative** **magnetic****permeability** plot should like as shown in Fig. 2DINDL1.13. We will define **0** for **Relative****electrical****permittivity**. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Coil material page.

.![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab1/image0013.jpg' | relative_url }})

Relative magnetic permeability

In **Coil** page, click on **Thermal** tab and for **Thermal****conductivity** select **Function of Temperature** and define the below table and click on ![]({{ '/assets/icons/pre_icons/mo_apply_button2.jpg' | relative_url }}) button. Thermal conductivity plot should like as shown in Fig. 2DINDL1.14.

|  **Temperature** |  **Thermal****conductivity**  
---|---|---  
1 | -123 | 368  
2 | -23 | 347  
3 | 27 | 341  
4 | 327 | 329  
5 | 527 | 319  
6 | 727 | 307  
7 | 927 | 294  
  
![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab1/image0014.jpg' | relative_url }})

Thermal conductivity plot

Under **Thermal****Conductivity** select **Vol. Heat cap** radio button and select **Function of Temperature** , define the below table and click on ![]({{ '/assets/icons/pre_icons/mo_apply_button2.jpg' | relative_url }}) button. Heat capacity plot should like as shown in Fig. 2DINDL1.15. Define **Mass****density** as **7.85839E-09**.

|  **Temperature** |  **Heat capacity**  
---|---|---  
1 | -123 | 2.895  
2 | -23 | 3.365  
3 | 27 | 3.428  
4 | 327 | 3.732  
5 | 527 | 3.88  
6 | 727 | 4.046  
7 | 927 | 4.162  
  
![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab1/image0015.jpg' | relative_url }})

Heat capacity plot

Click on **Elec./Mag.** tab, define **Electrical****Resistivity** as **1e-05** , **Relative****Permeability** as **1** and **Relative****Permittivity** as **0** as shown in Fig. 2DINDL1.16. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to **Air** material page.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab1/image0016.jpg' | relative_url }})

Coil Electro - magnetic page

In **Air** page, click on **Thermal** tab and define **Thermal****conductivity** as **0.0257** , **Heat****capacity** as **0.001210758** and **Mass****density** as **1.275e-12**. Thermal properties should like as shown in Fig. 2DINDL1.17.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab1/image0017.jpg' | relative_url }})

Air Thermal properties page

Click on **Elec./Mag**. tab, define **Electrical****Resistivity** as **1e20** , **Relative****Permeability** as **1** and **Relative****Permittivity** as **0** as shown in Fig. 2DINDL1.18. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Object page.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab1/image0018.jpg' | relative_url }})

Air Electro - magnetic material page

##  Adding Objects

For this lab we need **7****objects** in this lab, by default 3 objects will be added in list so, we need to add another 4 objects to the list. Add another 4 objects by clicking on ![]({{ '/assets/icons/pre_icons/mo_add_object_button.jpg' | relative_url }}) button (see Fig. 2DINDL1.19.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Workpiece page.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab1/image0019.jpg' | relative_url }})

Objects page

## Workpiece

Keep the default Workpiece Object name as Workpiece, object type as **Plastic** and object temperature as **20** °C. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Geometry page (see Fig. 2DINDL1.20.).

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab1/image0020.jpg' | relative_url }})

Workpiece General page

### Workpiece Geometry

Click on ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}), select **Cylinder** and define **Radius** as **30** , **Height** as **150** as shown in Fig. 2DINDL1.21. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button to accept all the changes, and go back to the Geometry definition, click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Material page to assign material.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab1/image0021.jpg' | relative_url }})

Workpiece Geometry page

### Workpiece Material

Select "**S45C-JAPAN** " from the list to assign material for Workpiece as shown in Fig. 2DINDL1.22. Click on ![]({{ '/assets/icons/pre_icons/mo_back_button.jpg' | relative_url }}) to generate mesh for workpiece.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab1/image0022.jpg' | relative_url }})

Workpiece material page

### Workpiece Mesh

  * For this problem, we will be heating workpiece to achieve austenitization temperature for a depth of about 3mm from the surface. This should produce a case depth of about 3mm upon proper cooling. For now, we are only looking at the heating parameters.

  * Let’s define the **Target number of elements** as **1500**.

  * To get a uniform mapped mesh, we have a geometry height to width ratio of 150/30 or 5/1. If you take 1500 and divide by 5, you get 300. If you take the square root of 300, you get about 17; define **Thickness****elements** as **17**. This should give you a relatively square mesh of 1500 elements. Define the **Size****ratio** as **12**. Make sure the **Mapped mesh** generation box is checked.

  * Click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) .

  * Coating mesh should be slightly deeper than estimated skin depth, remember that estimated skin depth is determined by:

Remembering that estimated skin depth is determined by:

![]({{ '/assets/equations/applications/55_induction_heating/eq_2dind_lab1.jpg' | relative_url }})

  * Coating mesh should be slightly deeper than estimated skin depth

  * Using a resistivity of about 0.0011 approaching the Curie point and a constant relative permeability of 3 approaching the Curie point and a frequency of 6,000Hz we get a skin depth of about .4mm.

  * 3-6 mesh layers in the coating mesh is recommended to cover 0.5mm thickness, so we will put 4 layers with coating mesh. To get a good mesh to handle the 0.5mm on the outer surface we will generate a graded mesh with thinner elements near the surface with at least 4 elements within 0.5mm.

To get a good mesh to handle the 0.5mm on the outside, we will put a coating mesh with at least 4 elements in the outside 0.5mm of surface this will be a graded mesh with thinner elements near the surface.

Click on the **Coating** tab.

Click on ![]({{ '/assets/icons/pre_icons/mo_add_icon.jpg' | relative_url }}) button 4 times and put in a thickness of **70** to the outer coating layer. All dimensions for the coating are in microns. Verify that the **1-S45C-JAPAN** is selected as material for coating.

Add additional coating thicknesses of **100** , **150** and **180** microns for the successive layers to generate graded mesh and verify that the **1-S45C-JAPAN** is selected as material for all layers.

Click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) and click on ![]({{ '/assets/icons/pre_icons/mo_yes_button.jpg' | relative_url }}) in "Do you want to generate coating mesh" popup. Generated mesh is as shown in Fig. 2DINDL1.23. You can zoom in to verify that the coating mesh is generated properly. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}).

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab1/image0023.jpg' | relative_url }})

Workpiece mesh

### Initialize Volume Fraction

Click on ![]({{ '/assets/icons/pre_icons/mo_elemental_data_icon.jpg' | relative_url }}) to access to the element dialog to initialize the volume fraction. On the item list window click ‘**Microstructure** ’ ![]({{ '/assets/icons/pre_icons/arrow_front.jpg' | relative_url }}) ‘**Phase** ’. Then choose ‘**Pearlite** ’ and click on ![]({{ '/assets/icons/pre_icons/mo_initialize_icon.jpg' | relative_url }}) to ‘Initialize Element Data’. Type **1** , then click on ![]({{ '/assets/icons/pre_icons/mo_apply_button.jpg' | relative_url }}), then close the window. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Boundary condition page.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab1/image0024.jpg' | relative_url }})

Workpiece Element page

### Boundary Conditions

It can be seen that ‘**Heat****Exchange with****Environment** ’ BCC has been already defined on the entire object surface (which does not include the centerline since these nodes are inside the object) when mesh was generated (see Fig. 2DINDL1.25.). If not assigned, then select Heat Exchange with Environment and select Top edge, right side edge and bottom edge on workpiece and click on ![]({{ '/assets/icons/pre_icons/mo_add_bcc_button.jpg' | relative_url }}). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) Top die page.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab1/image0025.jpg' | relative_url }})

Workpiece Boundary condition

## Bottom Coil

Change the Object name of Top Die to **Bottom****Coil** , keep default object type as **Rigid** and object temperature as **20** °C. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Geometry page.

### Bottom Coil Geometry

Click on ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}), select **Hollow****Cylinder** and define the **Inner****radius** as **38 ,****Outer****radius** as **46** and **Height** as **30** as shown in Fig. 2DINDL1.26. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button to close the Geometry primitive dialog. Click on ![]({{ '/assets/icons/pre_icons/mo_object_positioning_icon.jpg' | relative_url }}) icon below object tree, using **Offset** positioning and move the Bottom Coil object in -Y direction by **-16** mm as shown in Fig. 2DINDL1.27. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Mesh page.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab1/image0026.jpg' | relative_url }})

Bottom Coil geometry

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab1/image0039.jpg' | relative_url }})

Positioning Bottom coil geometry

### Bottom Coil mesh

Leave the **Thickness****elements** as **4**. For 4 elements through the thickness the number of elements in the Y direction is 4*30/8=15. The Number of elements is then 4*15=60. Enter **60** for **Target number of elements**. This should give relatively square elements. Make sure **Mapped mesh generation** is turned on, then click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). Generated mesh for Bottom coil is as shown in Fig. 2DINDL1.28., click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Material page.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab1/image0027.jpg' | relative_url }})

Bottom Coil Mesh page

### Bottom Coil Material

Select " **Coil** " from the list to assign material for Bottom Coil (see Fig. 2DINDL1.29.). Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Boundary condition page.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab1/image0028.jpg' | relative_url }})

Bottom Coil Material page

### Bottom Coil Boundary condition

Check that entire object surface is selected for heat exchange with environment, click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Properties page.

### Bottom Coil Properties

In Bottom Coil properties page click on **Heating** tab, select **Current****frequency** type as **Single** , define **Current****Frequency** of **6000****Hz** and a **Current****density** of **18** **A/mm 2 **as shown in Fig. 2DINDL1.30. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Bottom Die page.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab1/image0029.jpg' | relative_url }})

Bottom Coil Properties page

## Lower Middle Coil

Change the object name of Bottom Die to **Lower****Middle****Coil** , keep default object type as **Rigid** and object temperature as **20** °C. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Geometry page.

### Lower Middle Coil Geometry

Click on ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}). Select **Hollow****Cylinder** , define the **Inner****radius** as **38 ,****Outer****radius** as **46** and **Height** as **30** as shown in Fig. 2DINDL1.31. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button.jpg' | relative_url }}) button to close the Geometry primitive dialog. Click on ![]({{ '/assets/icons/pre_icons/mo_object_positioning_icon.jpg' | relative_url }}) icon below object tree and using **Offset** positioning move the Lower Middle Coil object in **Y** direction by **22** mm, similar to Fig. 2DINDL1.27. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Mesh page.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab1/image0030.jpg' | relative_url }})

Lower Middle Coil Geometry page

### Lower Middle Coil mesh

In Lower Middle Coil mesh page, define**Thickness elements** as **4** , **Target number of elements** as **60** and turn on **Mapped mesh** **generation** check box, then click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). Generated mesh for Lower Middle Coil is same as Bottom coil, click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Material page.

### Lower Middle Coil Material

Select "**Coil** " from the list to assign material for Lower Middle Coil. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Boundary condition page.

### Lower Middle Coil Boundary condition

Check that entire object surface is selected for heat exchange with environment, click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Properties page.

### Lower Middle Coil Properties

In Lower Middle Coil properties page click on **Heating** tab, select **Current****frequency** type as **Single** , define **Current****Frequency** of **6000****Hz** and **Current****density** of **18****A/mm 2 **as shown in Fig. 2DINDL1.30. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Object 4 page.

## Middle Coil

Change the object name of Object 4 to **Middle****Coil** , keep default object type as **Rigid** and object temperature as **20** °C. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Geometry page.

### Middle Coil Geometry

Click on ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}). Select **Hollow****Cylinder** , define the **Inner****radius** as **38,****Outer****radius** as **46** and **Height** as **30******as shown in Fig. 2DINDL1.32. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button close the Geometry primitive dialog. Click on ![]({{ '/assets/icons/pre_icons/mo_object_positioning_icon.jpg' | relative_url }}) icon below object tree, using **Offset** positioning move the Middle Coil object in **Y** direction by **60** , similar to Fig. 2DINDL1.27. Click ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Mesh page.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab1/image0031.jpg' | relative_url }})

Middle Coil Geometry page

### Middle Coil mesh

In Middle Coil mesh page, define **Thickness****elements** as **4** , **Target number of elements** as **60** and turn on **Mapped****mesh****generation** check box, then click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). Generated mesh for Middle Coil looks same as Bottom coil, click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Material page.

### Middle Coil Material

Select "**Coil** " from the list to assign material for Middle Coil. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Boundary condition page.

### Middle Coil Boundary condition

Check that entire object surface is selected for heat exchange with environment, click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Properties page.

### Middle Coil Properties

In Middle Coil properties page click on **Heating** tab, select **Current****frequency** type as **Single** , define **Current****Frequency** of **6000** **Hz** and **Current****density** of **18** A/mm2 as shown in Fig. 2DINDL1.30. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Object 5 page.

## Upper Middle Coil

Change the object name of Object 5 to **Upper****Middle****Coil** , keep default object type as **Rigid** and object temperature as **20** °C. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Geometry page.

### Upper Middle Coil Geometry

Click on ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}). Select **Hollow****Cylinder** , define thedefine the **Inner****radius** as **38 ,****Outer****radius** as **46** and **Height** as **30******as shown in Fig. 2DINDL1.33. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button to close the Geometry primitive dialog. Click on ![]({{ '/assets/icons/pre_icons/mo_object_positioning_icon.jpg' | relative_url }}) from below object tree and using **Offset** positioning move the Upper Middle Coil object in **Y** direction by **98** , similar to Fig. 2DINDL1.27. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Mesh page.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab1/image0032.jpg' | relative_url }})

Upper Middle Coil Geometry page

### Upper Middle Coil mesh

In Upper Middle Coil mesh page, define **Thickness****elements** as **4** , **Target number of elements** as **60** and turn on **Mapped** **mesh****generation** check box, then click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). Generated mesh for Upper Middle Coil looks same as Bottom coil, click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Material page.

### Upper Middle Coil Material

Select "**Coil** " from the list to assign material for Upper Middle Coil. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Boundary condition page.

### Upper Middle Coil Boundary condition

Check that entire object surface is selected for heat exchange with environment, click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Properties page.

### Upper Middle Coil Properties

In Upper Middle Coil properties page click on **Heating** tab, select **Current frequency** type as **Single** , define **Current****Frequency** of **6000****Hz** and **Current****density** of **18** A/mm2 as shown in Fig. 2DINDL1.30. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Object 6 page.

## Top Coil

Change the object name of Object 6 to **Top Coil** , keep default object type as **Rigid** and object temperature as **20** °C. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Geometry page.

### Top Coil Geometry

Click on ![]({{ '/assets/icons/pre_icons/mo_define_primitive_label.jpg' | relative_url }}), Select **Hollow****Cylinder** , define the ****define the**Inner****radius** as **38 ,****Outer****radius** as **46** and **Height** as **30** as shown in Fig. 2DINDL1.34. Click on ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) button to close the Geometry primitive dialog. Click on ![]({{ '/assets/icons/pre_icons/mo_object_positioning_icon.jpg' | relative_url }}) from below object tree, using **Offset** positioning move the Top Coil object in**Y** direction by **136** , similar to Fig. 2DINDL1.27. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Mesh page.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab1/image0033.jpg' | relative_url }})

Top Coil Geometry page

### Top Coil mesh

In Top Coil mesh page, define **Thickness****elements** as **4** , **Target****number****of****elements** as **60** and turn on **Mapped mesh generation** check box, then click on ![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}). Generated mesh for Top Coil looks same as Bottom coil, click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Material page.

### Top Coil Material

Select "**Coil** " from the list to assign material for Top Coil. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Boundary condition page.

### Top Coil Boundary condition

Check that entire object surface is selected for heat exchange with environment, click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until properties page.

### Top Coil Properties

In Top Coil Properties page click on **Heating** tab, select **Current****frequency** type as **Single** , define **Current** **Frequency** of **6000****Hz** and **Current****density** of **18****A/mm 2** as shown in Fig. 2DINDL1.30. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Object 7 page.

## Air

Change the object name of object 7 to **Air** , keep default object type as **Rigid** and object temperature as 20°C. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Geometry page.

### Air Geometry

The surrounding air should be at least as ½ as thick as the minimum dimension of the whole model. In this case that would be about 75mm. Click the **Construct by Subtraction** button and then **select all objects in the popup** as shown in Fig. 2DINDL1.35. The starting point will be **X, Y** at **0** ,**-75** and **width (W)** of **125** and **height (H)** of **300** and Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}). Created geometry is as shown in Fig. 2DINDL1.35., then click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Mesh page.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab1/image0034.jpg' | relative_url }})

Air Geometry - Construct by Subtraction page

###  Air Mesh

  * The **Target number of elements** should be **3000** and **Thickness** **elements** should be **8** and **Size ratio** should be **12**.

  * Click **Weighting****Factor** tab and set **Boundary****Curvature** roughly to **0.3** and **Mesh****windows** to **1** everything else should be **0** (see Fig. 2DINDL1.36.).

  * Click **Mesh****Windows** , add **3** **windows** and define **Relative****element** **size** as**0.1** for **first****window** ,**0.3** for **second****window** and **1.0** for **third****window**. This should look roughly as shown in Fig. 2DINDL1.37. but it does not have to look exactly like this.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab1/image0035.jpg' | relative_url }})

Air Mesh - Weighting factor page

  * Mesh windows use the lowest number window first and go out from there. They can overlap which is best for multiple windows, so the system does not have large discontinuities between sizes.

  * Once the mesh windows look the way you want them, go ahead and Generate mesh by clicking on![]({{ '/assets/icons/pre_icons/mo_generate_mesh.jpg' | relative_url }}) . Generated mesh is as shown in Fig. 2DINDL1.37., click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) Material page.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab1/image0036.jpg' | relative_url }})

Air Mesh - Mesh windows page

### Air Material

Select "**Air** " from the list to assign material for Air. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Boundary condition page.

### Air Boundary Condition

Check that entire object surface is selected for heat exchange with environment, click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Contact page.

## Contact

The next step will be to generate contact between the various objects, where the air is master to the workpiece and the coils(s) are master to the air. So, click on button 6 times to add six relations.

  * In first relation, select **Air** as Master and **Workpiece** as Slave, then click on ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}). Define **heat****transfer****coefficient** as **0.3** (in the Thermal tab) and click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}) .

  * In Second relation, select **Bottom Coil** as Master and **Air** as Slave, then click on ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}). Define **heat transfer coefficient** as **0.3** (in the Thermal tab) and click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}).

  * In third relation, select **Lower****Middle****Coil** as Master and **Air** as Slave, then click on ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}). Define **heat transfer coefficient** as **0.3** (in the Thermal tab) and click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}).

  * In forth relation, select **Middle****Coil** as Master and **Air** as Slave, then click on ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}). Define **heat transfer coefficient** as **0.3** (in the Thermal tab) and click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}).

  * In fifth relation, select **Upper****Middle****Coil** as Master and **Air** as Slave, then click on ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}). Define **heat transfer coefficient** as **0.3** (in the Thermal tab) and click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}).

  * In sixth relation, select Master as **Top****Coil** as Master and **Air** as Slave, then click on ![]({{ '/assets/icons/pre_icons/mo_define_button.jpg' | relative_url }}). Define **heat transfer coefficient** as **0.3** (in the Thermal tab) and click ![]({{ '/assets/icons/pre_icons/mo_ok_button2.jpg' | relative_url }}).

Click ![]({{ '/assets/icons/pre_icons/mo_generate_all_button.jpg' | relative_url }}) to generate contact for all the relationships, generated contacts between objects is as shown in Fig. 2DINDL1.38. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) to Stopping controls.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab1/image0037.jpg' | relative_url }})

Contact page

## Stopping controls

Click on **Thermal** tab under Stopping controls page, select "**Workpiece** " object with stopping method as "**Any Node** " and define **Temperature range** as **Min****0** and **Max** **1200**. Select " S**top when temperature is outside range** " radio button as shown in Fig. 2DINDL1.39. Click on ![]({{ '/assets/icons/pre_icons/mo_next_button.jpg' | relative_url }}) until Generate DB page.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab1/image0038.jpg' | relative_url }})

Stopping controls - Thermal tab

## Generate DB

In 'Generate DB' page, click ![]({{ '/assets/icons/pre_icons/mo_check_data_button.jpg' | relative_url }}) to see if anything was missed in the setup and then click on the ![]({{ '/assets/icons/pre_icons/mo_generate_database.jpg' | relative_url }}) button to generate the database. Observe the message in Message tab informing database generation status.

## Running Simulation

Once the database has been generated, switch to the Simulation mode by clicking on ![]({{ '/assets/icons/pre_icons/mo_simulation_mode_button.jpg' | relative_url }}) button above the operation tree. Click on the ![]({{ '/assets/icons/simulator_icons/mo_run_label_button.jpg' | relative_url }}) action label to open the Run Options dialog as shown in Fig. 2DINDL1.40. Use the default **Continue Run** option to select “**Continue from the last step** ” (from step -1) option and then select the Simulation mode as **Interactive** and click on ![]({{ '/assets/icons/simulator_icons/mo_run_job_button.jpg' | relative_url }}) button to run the simulation.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab1/image0041.jpg' | relative_url }})

Run Simulation Window

When the problem is running, you can check the Simulation message window and verify that the TOTAL AMOUNT POWER LOSS: is a positive number. This is a sign that the problem is at least set up for generating some heat transfer.

Monitor the progress of the simulation by looking at the Simulation Message and Simulation Log tab, making sure that the ![]({{ '/assets/icons/simulator_icons/mo_auto_update_option.jpg' | relative_url }}) option is checked. User can view the Induction heating process as the simulation proceeds to the specified Step definition from Simulation graphics.

## Post Processing

When the simulation is completed, review the results by switching to Post mode using the ![]({{ '/assets/icons/pre_icons/mo_post_mode_button.jpg' | relative_url }}) button above the Simulation tool bar.

Go to last step of simulation and Plot **temperature** state variable and observe the temperature distribution on the ends is shallower than the middle as shown in Fig. 2DINDL1.41.

![]({{ '/assets/images/applications/55_induction_heating/2d_induction_heating_lab1/image0040.jpg' | relative_url }})

Temperature distribution at the last step
